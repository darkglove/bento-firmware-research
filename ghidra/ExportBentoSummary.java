// Export a compact local inventory and one decompilation check.
// @category Bento
import java.io.File;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Data;
import ghidra.program.model.listing.DataIterator;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.mem.MemoryBlock;

public class ExportBentoSummary extends GhidraScript {
    private String field(String value) {
        return value.replace("\\", "\\\\").replace("\t", "\\t").replace("\r", "\\r").replace("\n", "\\n");
    }

    @Override
    public void run() throws Exception {
        File directory = new File(getScriptArgs()[0], currentProgram.getName());
        if (!directory.isDirectory() && !directory.mkdirs()) {
            throw new IllegalStateException("Cannot create report directory");
        }
        int functions = 0;
        try (PrintWriter output = new PrintWriter(new File(directory, "functions.tsv"), StandardCharsets.UTF_8)) {
            output.println("address\tname\tbody_bytes");
            FunctionIterator iterator = currentProgram.getFunctionManager().getFunctions(true);
            while (iterator.hasNext()) {
                monitor.checkCancelled();
                Function function = iterator.next();
                output.println(function.getEntryPoint() + "\t" + field(function.getName()) + "\t" + function.getBody().getNumAddresses());
                functions++;
            }
        }
        int strings = 0;
        try (PrintWriter output = new PrintWriter(new File(directory, "strings.tsv"), StandardCharsets.UTF_8)) {
            output.println("address\tvalue");
            DataIterator iterator = currentProgram.getListing().getDefinedData(true);
            while (iterator.hasNext()) {
                monitor.checkCancelled();
                Data data = iterator.next();
                if (data.hasStringValue()) {
                    output.println(data.getAddress() + "\t" + field(String.valueOf(data.getValue())));
                    strings++;
                }
            }
        }
        MemoryBlock image = currentProgram.getMemory().getBlocks()[0];
        Address base = image.getStart();
        long stack = Integer.toUnsignedLong(currentProgram.getMemory().getInt(base));
        long reset = Integer.toUnsignedLong(currentProgram.getMemory().getInt(base.add(4)));
        Address resetAddress = base.getAddressSpace().getAddress(reset & ~1L);
        Function resetFunction = getFunctionAt(resetAddress);
        if (resetFunction == null || functions == 0) {
            throw new IllegalStateException("Missing reset function or function inventory");
        }
        DecompInterface decompiler = new DecompInterface();
        boolean decompiled;
        try {
            if (!decompiler.openProgram(currentProgram)) {
                throw new IllegalStateException("Decompiler could not open program");
            }
            DecompileResults result = decompiler.decompileFunction(resetFunction, 30, monitor);
            decompiled = result.decompileCompleted() && result.getDecompiledFunction() != null;
            try (PrintWriter output = new PrintWriter(new File(directory, "reset-handler.c"), StandardCharsets.UTF_8)) {
                output.print(decompiled ? result.getDecompiledFunction().getC() : result.getErrorMessage());
            }
        } finally {
            decompiler.dispose();
        }
        try (PrintWriter output = new PrintWriter(new File(directory, "summary.txt"), StandardCharsets.UTF_8)) {
            output.println("Program: " + currentProgram.getName());
            output.println("Ghidra: " + ghidra.framework.Application.getApplicationVersion());
            output.println("Language: " + currentProgram.getLanguageID());
            output.println("Compiler: " + currentProgram.getCompilerSpec().getCompilerSpecID());
            output.println("Image SHA-256: " + currentProgram.getExecutableSHA256());
            output.println("Memory: " + image.getStart() + " - " + image.getEnd() + " (" + image.getSize() + " bytes)");
            output.println(String.format("Initial stack: 0x%08X", stack));
            output.println(String.format("Reset vector (Thumb bit set): 0x%08X", reset));
            output.println("Vector words: 166 (including stack and reserved entries)");
            output.println("Functions: " + functions);
            output.println("Instructions: " + currentProgram.getListing().getNumInstructions());
            output.println("Defined strings: " + strings);
            output.println("Reset decompilation completed: " + decompiled);
            output.println("Import assumptions: Cortex/Thumb little endian; base inferred from contiguous vector targets.");
            output.println("Exact chip, component roles, RAM/peripheral maps and updater integrity requirements remain unverified.");
            output.println("Automatic static analysis only; independently verify input hashes; no hardware test performed by this script.");
        }
        if (!decompiled) {
            throw new IllegalStateException("Reset handler decompilation failed");
        }
        println("BENTO_EXPORT_OK: " + currentProgram.getName() + "; functions=" + functions + "; strings=" + strings);
    }
}
