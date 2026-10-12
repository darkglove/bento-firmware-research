# Validation record

> [!WARNING]
> **EXPERIMENTAL TESTING — ONE OWNER-REPORTED SUCCESS, NOT PROVEN SAFE.**
> The device owner reports that this one-byte test firmware loaded without issue and displayed the lowercase `s` in `Global settings` after the usual firmware-update procedure. This was not independently witnessed; no installation logs or long-term results were supplied.
> This does **not** establish safety, reliability, rollback/recovery, broader device compatibility or support for other patches. Firmware experiments could leave a Bento unusable; recovery is not guaranteed. Do not install on hardware you cannot afford to render unusable.
> Offline tests and matching hashes are not hardware-safety certification. An AI assistant cannot certify this firmware safe.

Validated on a Windows host using the exact supported archive. No firmware is distributed.

- Firmware-free unittest suite: four tests passed.
- Public builder: completed with exact archive/component hash gates and built-in altered-input/double-application checks.
- Independent verifier: passed exact one-byte diff, expected output hash, unchanged companion, original rollback and manifest checks.
- Negative integration checks: independently altered candidate bytes and manifest text were both rejected.
- Optional Ghidra helper workflow has prior local analysis evidence; public commands/platform combinations are not exhaustively tested.
- Hardware: On 2026-10-12T06:56:25+00:00, the device owner reported that the one-byte test firmware loaded without issue, that the lowercase `s` in `Global settings` was visible, and that installation followed the usual firmware-update procedure. This is **owner-reported hardware evidence**, not an independently witnessed test. The report does not document installation logs, prolonged operation, audio/MIDI behavior, repeatability on other units, stock rollback, or interrupted-update recovery. Modified firmware remains experimental and is not proven safe from damage or bricking.
- No independent hardware observation, audio behavior or recovery validation is claimed.

Run the tutorial yourself; this record does not establish results on your computer or device. Test inputs/outputs remain local and ignored by Git.
