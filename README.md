# Bento firmware research

Independent research and original inspection tools for the 1010music Bento. **Updated 18 November 2026**, covering research through 17 November and the **1.6.8 analysis baseline**.

> **Experimental research, not a safe-to-install firmware release.** This repository contains no firmware, original vendor files, factory content or proprietary decompilation. Obtain legitimate inputs separately. No tool here flashes a device, and offline checks do not establish hardware safety or recovery.

## Start here

- **Understand the current research:** [Research guide](docs/research/README.md).
- **Inspect your own firmware without changing it:** [Read-only tools](docs/TOOLS.md).
- **Look up interfaces:** [1.6.8 parameter, option, object and UI-state tables](docs/reference/README.md).
- **Reproduce the older minimal patch:** [1.6.1 tutorial](docs/TUTORIAL.md). It remains hash-locked to 1.6.1.
- **Work with an AI assistant:** [Onboarding instructions](AI_START_HERE.md).
- **Contribute safely:** [Publication and privacy rules](PUBLICATION.md).

## What the current edition covers

The public research now covers the three main-image regions and separate controller, version differences, audio engines and effects, project/patch/settings formats, sequencing, MIDI/USB, storage and recording, native startup, UI rendering, touch, front-panel packets, recovery evidence and remaining work.

It includes a [74-checkpoint integration index](docs/research/CHECKPOINTS.md) and decoded factual reference tables. A controller-driven Phones change was observed in the native UI, consumed by the running engine and saved to a synthetic card. Its final output-amplitude effect remains unverified. Some modeled recording and queue failures are documented with their limits.

This is a curated public research edition, not a copy of a private workspace or a complete emulator distribution. Large local execution traces, vendor-derived outputs and the full native harness are not packaged. [Evidence and reproduction limits](docs/research/EVIDENCE.md) distinguish reported historical results from tests available in this checkout.

## Quick check

Python 3.10+ and Git are sufficient for the public tools and firmware-free tests; the optional Ghidra workflow has its own dependencies.

```sh
python -m unittest discover -s tests -v
python tools/audit_publication.py --history
```

The publication audit is a review aid, not proof that every possible secret or vendor-derived file has been detected. See [validation](docs/VALIDATION.md) for this edition's actual checks.

## Status and source boundaries

The 1.6.1 one-byte title patch has an anonymized owner-reported successful load. A later code experiment was reported to reset-loop and recover after stock rollback. The 1.6.8 T0–T3 batch has offline results; this repository does not claim recorded device acceptance for that batch. [Recovery guidance](docs/research/RECOVERY.md) explains the distinctions.

Official inputs and current product documentation belong at [1010music's downloads page](https://1010music.com/downloads). This project is not affiliated with or endorsed by 1010music. No rights to vendor firmware, manuals, presets, samples, trademarks or third-party code are granted by this repository.
