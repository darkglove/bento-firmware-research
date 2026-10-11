// Seed raw Cortex-M firmware from a validated, contiguous vector table.
// @category Bento
import java.math.BigInteger;
import java.util.HashSet;
import java.util.Set;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.data.DWordDataType;
import ghidra.program.model.lang.Register;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.symbol.RefType;
import ghidra.program.model.symbol.SourceType;

public class SeedCortexVectors extends GhidraScript {
    @Override
    public void run() throws Exception {
        MemoryBlock image = currentProgram.getMemory().getBlocks()[0];
        Address base = image.getStart();
        long start = base.getOffset();
        long end = image.getEnd().getOffset();
        Register thumb = currentProgram.getLanguage().getRegister("TMode");
        currentProgram.getProgramContext().setValue(thumb, base, image.getEnd(), BigInteger.ONE);
        Set<Long> handlers = new HashSet<>();
        String[] names = {"Initial_SP", "Reset", "NMI", "HardFault", "MemManage",
            "BusFault", "UsageFault", "Reserved_7", "Reserved_8", "Reserved_9",
            "Reserved_10", "SVCall", "Reserved_12", "Reserved_13", "PendSV", "SysTick"};
        int vectors = 0;
        for (int index = 0; index < 256; index++) {
            monitor.checkCancelled();
            Address slot = base.add(index * 4L);
            long word = Integer.toUnsignedLong(currentProgram.getMemory().getInt(slot));
            if (index > 0 && word != 0 && ((word & 1) == 0 || word - 1 < start || word - 1 > end)) {
                break;
            }
            createData(slot, DWordDataType.dataType);
            String name = index < names.length ? names[index] : "IRQ_" + (index - 16);
            createLabel(slot, "vector_" + name, true);
            vectors++;
            if (index == 0 || word == 0) {
                continue;
            }
            Address target = base.getAddressSpace().getAddress(word & ~1L);
            currentProgram.getReferenceManager().addMemoryReference(slot, target,
                RefType.DATA, SourceType.USER_DEFINED, 0);
            currentProgram.getSymbolTable().addExternalEntryPoint(target);
            if (handlers.add(target.getOffset())) {
                if (!disassemble(target)) {
                    throw new IllegalStateException("Cannot disassemble vector " + index + " at " + target);
                }
                if (createFunction(target, name + "_Handler") == null && getFunctionAt(target) == null) {
                    throw new IllegalStateException("Cannot create handler at " + target);
                }
            }
        }
        if (vectors != 166) {
            throw new IllegalStateException("Unexpected vector count: " + vectors);
        }
        println("BENTO_VECTOR_SEED: " + vectors + " words; " + handlers.size() + " unique handlers; base=" + base);
    }
}
