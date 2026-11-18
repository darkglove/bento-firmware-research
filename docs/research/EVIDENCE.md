# Evidence, provenance and reproduction

## Four different kinds of evidence

**Static:** bytes, vectors, tables, strings, instructions or reconstructed data flow were inspected. A string or menu entry alone does not establish working behavior.

**Emulated:** original instructions ran against explicitly supplied memory, peripheral responses, interrupts or files. This can establish exact instruction behavior for the tested inputs. It does not establish electrical behavior, physical timing, cache coherence or recovery on a device.

**Modeled:** an independently written reference calculation or replay was compared with execution. Sample-exact means the tested sample sequences matched; it does not mean every parameter, timing or hardware state was covered.

**Reported hardware:** a device owner or external maintainer described an outcome. These reports are attributed without publishing personal information. They are not independent observations by this repository.

## Baselines

The exact component hashes are in [firmware-profiles.json](../reference/firmware-profiles.json). Earlier research uses the 1.6.1 pair; later integration work uses 1.6.8. The companion image is byte-identical between these two baselines. Addresses and numeric parameter IDs must always be tied to a baseline.

The 1.6.8 research includes 74 numbered integration checkpoints, ending with controller traffic, UI changes and persistence on 16 November. The following recovery/reference review was recorded on 17 November. The [checkpoint index](CHECKPOINTS.md) lists that scope without exposing execution-session identifiers, machine paths, private logs or personal project history.

## What is reproducible from this public checkout

- Firmware-free tests for the existing 1.6.1 patch guards.
- Read-only identity, region and vector inspection of separately supplied supported images.
- Read-only byte-range comparison of a supported original and a local candidate.
- The original 1.6.1 tutorial's build and independent verification, with a separately supplied exact archive.
- Review of decoded parameter, object, option and UI-state tables.
- Publication checks over tracked content and reachable Git history.

The large native-execution harness, complete raw traces, proprietary disassembly/decompilation, firmware-generated screen captures, factory projects, samples and vendor files are **not included**. Accordingly, the historical full-system emulation claims are reported research results, not tests a fresh public checkout can reproduce in one command. The source checkpoint hashes in [publication provenance](../reference/publication-provenance.json) identify the records used for this edition; hashes alone do not let a reader independently validate those records.

## How to extend the research

For each claim, record the image SHA-256, addresses, inputs, setup assumptions, native versus supplied operations, expected output, actual output, failure controls and unresolved boundary. Use synthetic projects and generated signals where possible. Keep vendor inputs and device-derived outputs outside Git.

For graphics, compare decoded memory writes and drawing-register operations with every captured frame. For storage, independently reconstruct the final filesystem and file bytes. For audio, compare samples and state against a separate reference, including a control with the tested service disabled. A checker that merely repeats the producer's implementation is weaker evidence.

Do not hide an emulator workaround. Earlier startup adapters, floating-point handling, interrupt-return models and observation bounds changed the meaning of some tests. Label those changes and keep the original failure evidence locally. A failed fixture is not a firmware defect; a recovered file is not proof that no input samples were lost.

## External references

- [1010music downloads and documentation](https://1010music.com/downloads): official firmware and documentation source. No vendor files are mirrored here.
- [bento-community-lab](https://github.com/hunting-ghosts/bento-community-lab/tree/960e4b1): external research reviewed at revision `960e4b1`.
- [bento-playground](https://github.com/hunting-ghosts/bento-playground/tree/9e817b9): external source-only modification project reviewed at revision `9e817b9`.
- [blackbox-mod](https://github.com/j3threejay/blackbox-mod/tree/47f4312276a841548d1a5c82b930699fd1a45d11): historical technique reference for another device. Its offsets and compatibility do not apply to Bento.

External reports are supporting evidence, not independent verification of this project's candidates. No third-party repository code is imported in this publication. Public availability does not remove a source's license conditions or grant rights to firmware or factory content.
