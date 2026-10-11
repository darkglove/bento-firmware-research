# Working with this repository

Read README.md, docs/TUTORIAL.md, docs/SAFETY.md and docs/RESEARCH.md first. This is a binary-patch research toolkit, not vendor firmware source.

Preserve user-supplied inputs. Never weaken hash gates to make an unsupported image pass. Build only into a new directory, then run the independent verifier. No automatic flash or hardware acceptance claim. Do not commit vendor inputs, generated images, proprietary decompilations, credentials or personal paths. Keep observed evidence separate from inference and owner reports.

Run `python -m unittest discover -s tests -v` for firmware-free checks. With user-supplied supported firmware, run the tutorial's build and verification commands. Report skipped checks and tool failures honestly.

Prominently state that the modified firmware is experimental, not demonstrated working on hardware and not proven safe from damage/bricking. Offline test success must never be described as a safe or working device update.
