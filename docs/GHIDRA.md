# Optional local Ghidra analysis

Not required to build the one-byte probe. Install Ghidra and its supported JDK using [official instructions](https://github.com/NationalSecurityAgency/ghidra). The research used Ghidra 12.1.4; version differences may change analysis.

Extract your verified archive locally, preserving originals. Verify component hashes from [TUTORIAL.md](TUTORIAL.md). Create a NEW Ghidra project and import each as raw binary, language `ARM:LE:32:Cortex`, compiler specification `default`. Use load base `0x08040000` for bento1.bin and `0x90000000` for bento2.bin. These bases are inferred from vectors, not a complete hardware map.

Add this repo's `ghidra` directory to Script Manager paths. `SeedCortexVectors.java` seeds vector entry points/Thumb context; `ExportBentoSummary.java` exports summaries, indexes and reset-handler pseudocode to a supplied local output directory. Do not publish those proprietary exports.

Headless example (POSIX shell; use the equivalent Ghidra launcher and quoting on Windows):

```sh
mkdir -p analysis/project
"$GHIDRA_HOME/support/analyzeHeadless" analysis/project BentoLocal -import inputs/bento1.bin -processor ARM:LE:32:Cortex -cspec default -loader BinaryLoader -loader-baseAddr 08040000 -scriptPath ghidra -preScript SeedCortexVectors.java -postScript ExportBentoSummary.java analysis/reports -analysisTimeoutPerFile 180 -max-cpu 2
```

`GHIDRA_HOME` means your own Ghidra installation directory; do not copy someone else's absolute paths. Do not overwrite an existing project. Review logs for success, errors and timeouts; an exit code alone is insufficient. For the second component use its filename and base, importing it into the same project only after the first run finishes.

For a saved main-image program, the targeted helper can be run without repeating analysis:

```sh
"$GHIDRA_HOME/support/analyzeHeadless" analysis/project BentoLocal -process bento1.bin -readOnly -noanalysis -scriptPath ghidra -postScript InspectMinimalPatch.java analysis/minimal-review -max-cpu 2
```

This exports candidate CRC routines, selected UI/update string xrefs and direct callers. Inspect both pseudocode and disassembly; automated xrefs do not cover every indirect use. Ghidra read-only processing may update project index bookkeeping; separately rehash firmware originals. These portable commands are guidance based on the original analysis workflow, not a claim that every platform/version combination was exercised.
