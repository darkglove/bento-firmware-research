# Bento firmware research: a reproducible first patch

An independent, experimental toolkit for studying 1010music Bento firmware and reproducing a minimal binary patch. Not affiliated with or endorsed by 1010music.

**Status: offline build and byte-level verification only. No successful hardware installation, boot, or recovery test is established here.** This is not vendor source code, an SDK, or a general custom-firmware framework.

## Start here

1. Read [the worked tutorial](docs/TUTORIAL.md).
2. Obtain your own legitimate copy of the exact supported firmware archive. No firmware downloads are provided here.
3. Run the builder and independent verifier locally. They never flash a device.
4. If using an AI assistant, give it [this onboarding prompt](AI_START_HERE.md).

The worked example changes `Global Settings` to `Global settings`: exactly one byte in bento1.bin. bento2.bin remains unchanged. Version stays 1.6.1.

## Contents

- [Tutorial](docs/TUTORIAL.md): inputs, commands, expected results, troubleshooting and hardware-test boundaries.
- [Technical findings](docs/RESEARCH.md): address assumptions, CRC observations, evidence and limitations.
- [Optional Ghidra workflow](docs/GHIDRA.md): reproduce local analysis without distributing decompilations.
- [Safety](docs/SAFETY.md): recovery uncertainty and update precautions.
- [AI prompt](AI_START_HERE.md): ask an assistant to use real tools and report actual results.
- `tools/`: standard-library Python builder and independent verifier.
- `tests/`: tests that need no vendor firmware; these are not hardware tests.
- `ghidra/`: analysis/export helpers, not firmware source.

Python 3.10+ is recommended. The minimal patch needs only Python's standard library; Ghidra is optional. Commands are intended for Windows, macOS and Linux. Actual validation for this release was on a Windows host; cross-platform execution is not claimed tested.

Vendor firmware, manuals, Ghidra databases, generated images and proprietary decompilations are intentionally absent. The tools require user-supplied inputs and fail closed on different hashes. Public availability of this repository does not grant rights to vendor materials. No third-party firmware or source licence is implied.
