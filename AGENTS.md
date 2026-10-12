# Working with this repository

Read README.md, docs/TUTORIAL.md, docs/SAFETY.md and docs/RESEARCH.md first. This is a binary-patch research toolkit, not vendor firmware source.

Preserve user-supplied inputs. Never weaken hash gates to make an unsupported image pass. Build only into a new directory, then run the independent verifier. No automatic flash. Attribute Matt's reported successful one-byte load and visible lowercase `s`; do not generalize it to recovery or other patches. Do not commit vendor inputs, generated images, proprietary decompilations, credentials or personal paths. Keep observed evidence separate from inference and owner reports.

Run `python -m unittest discover -s tests -v` for firmware-free checks. With user-supplied supported firmware, run the tutorial's build and verification commands. Report skipped checks and tool failures honestly.

Prominently state that the modified firmware is experimental. One owner reports a successful load and visible lowercase `s`, but this does not prove reliability or safety from damage/bricking. Offline test success must never be described as a safe device update.
