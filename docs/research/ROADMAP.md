# Remaining work and contribution gates

The long-term objective is enough understanding to replace parts or all of the firmware. Substantial original-code emulation and interface decoding exist. A complete replacement and a generally demonstrated recovery procedure do not.

## Near-term priorities

**Recovery first.** Resolve the specific application-independent entry, installer-preservation and stock-restoration evidence gaps. Exhaustive bootloader reverse engineering is not automatically necessary, but generic processor debug features are not a proven recovery route for this board.

**Close the last control-to-audio gap.** The UI value, consumed engine command and saved settings are verified in modeled execution. Capture and compare the resulting audio amplitude with an appropriate output path. Preserve the failed prior fixture as a failed fixture; do not relabel it successful.

**Make reproduction portable.** The larger research harness depends on local inputs and generated analysis. A separate porting effort must remove personal paths, declare dependencies, create synthetic fixtures and check every bundled file's provenance before publishing it. This edition does not pretend that work is complete.

## New UI route

A staged design can replace CM4 while retaining the stock CM7 engine. That narrows the audio rewrite, but CM4 also provides storage, sequencing upload, communications, settings and power-related services. The shared-memory contract and native startup ownership must be maintained deliberately.

Useful milestones are a desktop screen prototype; synthetic project load and engine messages; a recovery-gated device display test; touch input; project/sample service; then complete screen workflows, recording, save/load, MIDI/USB and power behavior. A graphics library choice is a proposal, not an implemented port. No new UI implementation is included here.

## Full firmware route

A complete replacement needs validated hardware initialization, memory/cache/MPU ownership, inter-core messaging, controller/reverb interfaces, filesystem durability, audio timing and error handling. It also needs compatible project/preset interpretation and defined behavior when inputs are malformed or resources run out.

Specific open areas include physical timing and cache coherence; all error paths under concurrent audio/storage/USB load; complete project-model round trips; audible integration of all controls; coverage of every effect/style; calibration meaning; and power-loss/installation behavior.

## Useful contributions

- Small, version-pinned reproductions with synthetic inputs and explicit expected outcomes.
- An independently checked correction to a table or interface contract.
- A test that distinguishes native behavior from a supplied model assumption.
- A portable original tool that requires local vendor inputs rather than bundling them.
- An anonymized hardware report with exact candidate identity, method, observed result and limitations, without uploading firmware or private device data.

Follow [PUBLICATION.md](../../PUBLICATION.md). Do not publish manuals, release-note PDFs, factory content, binary dumps, proprietary decompilation, personal paths, raw sessions or credentials. A research summary, an address, or a parameter key is not permission to redistribute its source image.
