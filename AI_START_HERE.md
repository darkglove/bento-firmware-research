# Instructions for an AI research assistant

Read [README.md](README.md), [PUBLICATION.md](PUBLICATION.md), [the evidence limits](docs/research/EVIDENCE.md), [safety](docs/SAFETY.md), and the subject chapter relevant to the task.

Use the following task brief:

```text
Help me work with this public Bento research repository. The current analysis baseline is 1.6.8; the original minimal text-patch builder remains specific to 1.6.1.

Start by identifying the intended outcome and exact baseline. Separate static inspection, native-code emulation, independent models and reported hardware results. Do not turn a successful emulator run into a claim of safe installation.

Use the current research guide and reference tables. Treat numeric parameter IDs and addresses as version-specific. The companion image is identical between the supported 1.6.1 and 1.6.8 pairs, but main-side behavior can differ.

Run available checks with real tools and report actual results. This checkout does not include the complete native emulator harness or its raw traces. Do not invent a reproduction command or claim to have rerun historical integration results.

If firmware inspection is needed, use the read-only tool with locally supplied, legitimate inputs. Do not download substitute firmware, weaken hash gates, upload inputs, or print personal paths into published evidence. The 1.6.1 tutorial can build local outputs only when I ask for that task and provide the supported archive.

Keep personal data, credentials, private paths, raw sessions, vendor firmware, manuals, release notes, factory patches/samples, generated images and proprietary decompilation outside Git. Publication requires explicit file review and the publication audit. No automatic flash or device changes.

For a research contribution, record exact image identity, method, assumptions, tested inputs, expected and observed outcomes, negative controls and remaining gaps. Use synthetic examples and publicly attributable sources. Do not claim that a proposal, saved report or stopped process proves completion.
```

[The roadmap](docs/research/ROADMAP.md) lists useful next contributions. An assistant must not silently expand a documentation task into device experimentation or public release of excluded material.
