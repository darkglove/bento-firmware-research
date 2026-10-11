# Validation record

> [!WARNING]
> **EXPERIMENTAL TESTING ONLY — NOT PROVEN TO WORK ON A BENTO.**
> No modified firmware produced by this project has been demonstrated here to install, boot, function correctly, or avoid damaging or bricking a Bento. **It has not been proven safe.**
> Passing Python tests, matching hashes, or changing only one byte does not establish hardware safety. Attempting installation could leave your Bento unusable and require repair; successful recovery is not guaranteed.
> This is research material, not a recommended firmware upgrade. Do not install it on hardware you cannot afford to render unusable. An AI assistant cannot certify it safe.

Validated on a Windows host using the exact supported archive. No firmware is distributed.

- Firmware-free unittest suite: four tests passed.
- Public builder: completed with exact archive/component hash gates and built-in altered-input/double-application checks.
- Independent verifier: passed exact one-byte diff, expected output hash, unchanged companion, original rollback and manifest checks.
- Negative integration checks: independently altered candidate bytes and manifest text were both rejected.
- Optional Ghidra helper workflow has prior local analysis evidence; public commands/platform combinations are not exhaustively tested.
- No hardware installation, boot, audio behavior or recovery validation is claimed.

Run the tutorial yourself; this record does not establish results on your computer or device. Test inputs/outputs remain local and ignored by Git.
