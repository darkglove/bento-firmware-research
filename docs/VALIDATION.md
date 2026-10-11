# Validation record

Validated on a Windows host using the exact supported archive. No firmware is distributed.

- Firmware-free unittest suite: four tests passed.
- Public builder: completed with exact archive/component hash gates and built-in altered-input/double-application checks.
- Independent verifier: passed exact one-byte diff, expected output hash, unchanged companion, original rollback and manifest checks.
- Negative integration checks: independently altered candidate bytes and manifest text were both rejected.
- Optional Ghidra helper workflow has prior local analysis evidence; public commands/platform combinations are not exhaustively tested.
- No hardware installation, boot, audio behavior or recovery validation is claimed.

Run the tutorial yourself; this record does not establish results on your computer or device. Test inputs/outputs remain local and ignored by Git.
