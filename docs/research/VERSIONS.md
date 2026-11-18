# Versions, parameters and object types

The historical survey covered 18 builds from 1.2.4 through the image labeled 1.6, whose component bytes match the supported 1.6.1 pair. Official 1.6.8 was added later and is the current analysis baseline. The vendor [downloads page](https://1010music.com/downloads) was checked on 18 November 2026 and listed 1.6.8.

## What changed in 1.6.8

The main image grew by 12,024 bytes; the companion image remained byte-identical. Growth in the update-file region allocation is in CM4. This does not mean the audio code is unchanged: normalized comparison and subsequent execution found targeted audio changes as well.

Documented binary evidence includes project packing, card-error handling, Save As failure reporting, a Cut Group menu entry, slice-to-pad labels, and a persisted `lastknowndate` value. Feature strings alone are leads; later traced data flow gives stronger evidence.

Selected later findings:

- Choke-group selection includes a track-lane key, rather than using only a global group number.
- External-track `in1gain` is stored on the track and applied in the appropriate live-input path. Emulated ratios at 0, -6 and -20 dB were 1, approximately 0.501187 and 0.1. The normal recording path was a separate case.
- The step-sequencer note-off calculation was corrected: the older mirrored in-block offset and the later direct offset were distinguished in paired tests. This was not a blanket fix for every Slicer note path.
- Slicer/Shredder LFO advancement can wait for a note's initial sample-offset countdown; the Clip path differs.
- Phones gain affects the metronome in the newer isolated engine test. This is distinct from the unfinished end-to-end controller-driven amplitude experiment.
- Some structural changes remain only leads. Never identify a release-note fix solely from nearby changed instructions.

## Parameter IDs are not stable names

Both main cores construct matching parameter registries. Each descriptor supplies a slot ID, storage key, display label, type, range/options and related metadata. IDs shift when entries are inserted or removed. Use a storage key as the logical identity, then resolve its numeric ID against the exact image version.

The [1.6.8 registry](../reference/parameter-registry-1.6.8.md), [options](../reference/enums-1.6.8.md), and [object schema](../reference/object-model-1.6.8.md) provide decoded facts. They are research tables, not vendor documentation or a guarantee that every option is exposed in the UI.

Most percentage-like values use 0–1000. Gain commonly uses milli-decibels and pitch milli-semitones, but inspect each parameter's type rather than applying a universal unit conversion. Enum ordering is part of a version-specific interface.

The 1.6.8 schema contains 764 eight-byte records grouped by object type. Runtime type-name initialization and lookup were checked separately. **Table position is not type ID:** the corrected mapping places Multisample at `0x0f` and Loop at `0x11`.

## Porting an address or patch

1. Hash both source components and choose an explicit baseline.
2. Locate the semantic target through storage keys, strings, constructors, call sites and data use.
3. Check original bytes and register/stack assumptions at the new site.
4. Validate behavior and a negative control on the new image.

Large rebuilds can move code and change field offsets while preserving functionality. Raw byte-diff volume overstates semantic change. Normalized function matching is useful but can pair the wrong functions; it is supporting evidence, not proof of a safe relocation.

The old [text-patch tutorial](../TUTORIAL.md) intentionally remains pinned to 1.6.1. Its offsets must not be used on 1.6.8.
