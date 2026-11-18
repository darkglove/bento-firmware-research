# Safety and recovery limits

**This is experimental firmware research. It is not a safe-to-install firmware distribution.** A modified image may be rejected, fail to start, damage stored data or require recovery/service. No measured general failure probability is available.

An anonymized owner reported that the original one-byte 1.6.1 text probe loaded and displayed the changed title. A separate code experiment was reported to reset-loop, followed by a successful stock rollback. Neither report establishes general reliability, uninterrupted-update safety or recoverability from every failure.

The later 1.6.8 batch was built and checked offline. No device acceptance for that batch is claimed here. The [current recovery assessment](research/RECOVERY.md) supersedes older statements that the recovery route was wholly unexplored, while preserving the distinction between a documented route and a demonstrated result on a particular device.

Preserve the bootloader, disk-mode image, calibration and stock restoration material. Establish an application-independent recovery route, back up user data and follow current vendor power/install requirements before any separately authorized experiment. Do not interrupt an update already underway. The bootloader's hardware-test option is not an install step and can emit very loud audio.

Nothing in this repository flashes hardware. Read-only inspection does not test installer behavior. Matching candidate hashes, limiting a diff or emulating a boot does not certify safety. No generic debug/boot-mode recovery should be assumed accessible on the physical board.

Original vendor files and generated candidate/rollback files stay local and outside Git. See [publication rules](../PUBLICATION.md).
