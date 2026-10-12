# Safety and recovery

> [!WARNING]
> **EXPERIMENTAL TESTING — ONE OWNER-REPORTED SUCCESS, NOT PROVEN SAFE.**
> The device owner reports that this one-byte test firmware loaded without issue and displayed the lowercase `s` in `Global settings` after the usual firmware-update procedure. This was not independently witnessed; no installation logs or long-term results were supplied.
> This does **not** establish safety, reliability, rollback/recovery, broader device compatibility or support for other patches. Firmware experiments could leave a Bento unusable; recovery is not guaranteed. Do not install on hardware you cannot afford to render unusable.
> Offline tests and matching hashes are not hardware-safety certification. An AI assistant cannot certify this firmware safe.

On 2026-10-12T06:56:25+00:00, the device owner reported that the one-byte test firmware loaded without issue, that the lowercase `s` in `Global settings` was visible, and that installation followed the usual firmware-update procedure. This is **owner-reported hardware evidence**, not an independently witnessed test. The report does not document installation logs, prolonged operation, audio/MIDI behavior, repeatability on other units, stock rollback, or interrupted-update recovery. Modified firmware remains experimental and is not proven safe from damage or bricking.

This is unsupported experimental firmware research. A one-byte cosmetic edit is not a guarantee of a harmless update. Byte-level verification does not test the installer's erase/write behavior, integrity policy or hardware boot.

Possible outcomes include rejection, an application failure recoverable through the bootloader, or failure requiring servicing/hardware programming. No measured probability is available.

A device owner reported receiving confirmation that the bootloader should survive interrupted updates or power loss. The underlying correspondence was not inspected and recovery was not tested; treat this as an unverified report, not a vendor guarantee or proof of modified-image acceptance. Seek current advice for your exact device.

Before any experiment: back up projects/the SD card, retain the exact original pair separately, establish the vendor recovery procedure and use reliable external power. A rollback folder is not evidence that recovery will succeed. Never interrupt an update already underway. The reviewed manual requires external power and warns that the bootloader hardware-test option emits extremely loud audio: disconnect speakers/headphones before exploring that option; it is not needed for this text test.

No automatic flashing is implemented. No checksum/signature bypass, bootloader patch or executable-code injection is provided. Do not share generated firmware, private identifiers, credentials or proprietary decompilations in issues or pull requests.
