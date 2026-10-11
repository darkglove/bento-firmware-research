// Read-only targeted export: CRC candidates, direct callers, and UI/update string xrefs.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.address.*;
import java.io.*;
import java.util.*;
public class InspectMinimalPatch extends GhidraScript {
 public void run() throws Exception {
  File dir=new File(getScriptArgs()[0]); dir.mkdirs();
  LinkedHashSet<Function> selected=new LinkedHashSet<>();
  try(PrintWriter out=new PrintWriter(new File(dir,"xref-report.txt"),"UTF-8")) {
   out.println("Program="+currentProgram.getName()+" SHA256="+currentProgram.getExecutableSHA256());
   for(String s:new String[]{"0809dc40","0809dd60","080e2f90"}) {Function f=getFunctionAt(toAddr(s)); if(f!=null)selected.add(f);}
   DataIterator it=currentProgram.getListing().getDefinedData(true);
   while(it.hasNext()) {Data d=it.next(); Object v=d.getValue(); if(!(v instanceof String))continue; String s=(String)v;
    if(!s.matches("(?is).*(firmware|bootloader|1\\.6|global settings|project management|disk mode).*"))continue;
    out.println("STRING "+d.getAddress()+" "+s);
    for(Reference r:getReferencesTo(d.getAddress())) {Function f=getFunctionContaining(r.getFromAddress()); out.println("  REF "+r+" function="+(f==null?"none":f.getName())); if(f!=null)selected.add(f);}
   }
   LinkedHashSet<Function> roots=new LinkedHashSet<>(selected);
   for(Function f:roots) {out.println("ROOT "+f.getName()); for(Reference r:getReferencesTo(f.getEntryPoint())) {Function caller=getFunctionContaining(r.getFromAddress()); out.println("  CALLER "+r+" function="+(caller==null?"none":caller.getName())); if(caller!=null)selected.add(caller);}}
  }
  DecompInterface decomp=new DecompInterface(); decomp.openProgram(currentProgram);
  try(PrintWriter out=new PrintWriter(new File(dir,"decompiled.c"),"UTF-8")) {for(Function f:selected) {monitor.checkCancelled(); out.println("\n/* FUNCTION "+f.getName()+" "+f.getEntryPoint()+" */"); DecompileResults r=decomp.decompileFunction(f,45,monitor); if(r.decompileCompleted())out.println(r.getDecompiledFunction().getC()); else out.println("FAILED: "+r.getErrorMessage());}}
  decomp.dispose(); println("MINIMAL_PATCH_EXPORT_OK functions="+selected.size());
 }
}
