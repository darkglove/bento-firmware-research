# Safety and recovery

> [!WARNING]
> **EXPERIMENTAL TESTING ONLY — NOT PROVEN TO WORK ON A BENTO.**
> No modified firmware produced by this project has been demonstrated here to install, boot, function correctly, or avoid damaging or bricking a Bento. **It has not been proven safe.**
> Passing Python tests, matching hashes, or changing only one byte does not establish hardware safety. Attempting installation could leave your Bento unusable and require repair; successful recovery is not guaranteed.
> This is research material, not a recommended firmware upgrade. Do not install it on hardware you cannot afford to render unusable. An AI assistant cannot certify it safe.

This is unsupported experimental firmware research. A one-byte cosmetic edit is not a guarantee of a harmless update. Byte-level verification does not test the installer's erase/write behavior, integrity policy or hardware boot.

Possible outcomes include rejection, an application failure recoverable through the bootloader, or failure requiring servicing/hardware programming. No measured probability is available.

A device owner reported receiving confirmation that the bootloader should survive interrupted updates or power loss. The underlying correspondence was not inspected and recovery was not tested; treat this as an unverified report, not a vendor guarantee or proof of modified-image acceptance. Seek current advice for your exact device.

Before any experiment: back up projects/the SD card, retain the exact original pair separately, establish the vendor recovery procedure and use reliable external power. A rollback folder is not evidence that recovery will succeed. Never interrupt an update already underway. The reviewed manual requires external power and warns that the bootloader hardware-test option emits extremely loud audio: disconnect speakers/headphones before exploring that option; it is not needed for this text test.

No automatic flashing is implemented. No checksum/signature bypass, bootloader patch or executable-code injection is provided. Do not share generated firmware, private identifiers, credentials or proprietary decompilations in issues or pull requests.
