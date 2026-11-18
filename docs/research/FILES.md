# Project, patch and settings formats

Scope: static CM4 analysis and later executed load/save paths for 1.6.8. Examples below are newly written structural illustrations, not copied factory files. They are not complete playable projects.

## XML containers and object creation

Projects and patches share a `document` / `session` container. The current writer uses session version 2; earlier content uses version 1. A patch can use the same structure with one track. Settings and patch metadata have separate roots:

```xml
<document><session version="2"><track type="wttrack"/></session></document>
<document><settings><params/><preset name="Example"/></settings></document>
<patchmetadata version="1"><patch path="Example"><tag>Test</tag></patch></patchmetadata>
```

These are three separate examples, not one recommended multiple-root file. The native parser showed permissive behaviors that a replacement should investigate explicitly rather than assume from another XML library version.

The session stores at most twelve track objects, with a separate limit of eight instrument tracks. Type names resolve through a runtime table. Unknown cell types are skipped; each recognized cell creates a new object. Native construction and file-service upload were tested later than the original static inspection.

`params` attribute names are registry storage keys. Unknown keys are skipped. Missing or nonnumeric values can become zero in the inspected paths. A writer only emits parameters it can name. Do not assume schema defaults and missing-file values are always the same.

The [object table](../reference/object-model-1.6.8.md) distinguishes track, oscillator, sample-asset, envelope, filter and sequence objects. A sample's slices belong to the `samasst` asset (type 5), not to the Slicer instrument object itself. Wavetable/granular oscillator cells can load a `filename` attribute first and then overwrite it from `params`.

## Modulation

A `modsource` associates destination, source, slot and amount. MIDI CC needs the explicit `src="midicc"` discriminator plus `mchan` and `ccnum`; those attributes alone do not select the MIDI source path. The packed source is `0x8000 | ((mchan & 15) << 7) | (ccnum & 127)`.

Unknown source/destination lookups become zero in the tested path. Slot narrowing and signed amount narrowing occur when records are uploaded. Validating only the XML text can miss the effective value received by the engine.

## Sequences and automation

Time uses 960 ticks per quarter note. Event kinds include `note`, `auto`, `xyvalue`, `steplen` and the loader's `sceneitem`. Note attributes include exact start/length ticks, pitch, velocity, condition and channel. If `lentks` is present, its exact-tick path differs from the quarter-note `lencount` path.

Native events are 24-byte records. The format has kind, condition, channel, timing and two payload words. This describes a decoded interface, not a dump of vendor event data.

Four automation lanes hold up to 256 signed 16-bit values each. XML text is run-length encoded in six-hex-digit groups: `CCVVVV`, where `CC` is a repeat count and `VVVV` a signed 16-bit value. The lane has its own slide flag. Short data preserves unwritten values in the tested path; do not assume every partial load clears a reused object.

A malformed sequence event with no `step` could leave the loader repeating the same element in the executed test. Unknown event types and nonnumeric values also have observed fallback behavior. A compatible replacement should use bounded parsing and make a deliberate choice about unsafe malformed-input behavior instead of reproducing a hang.

## Version migration

For version 1 or earlier, sampler types 1–4 apply an overdrive/gain migration when overdrive is positive. The recorded calculation is `clamp(trunc(gaindb * 0.02768) + overdrive, 0, 1000)` for overdrive, with gain raised by 12000 and capped at 12000. Units are raw parameter units. Check conversion order and truncation against the baseline when implementing compatibility.

## Wavetable file organization

The examined factory wavetable format is mono 24-bit PCM, 48 kHz, with 1,040,384 samples. It stores seven consecutive octave levels, each containing 256 cycles:

| Level | Samples per cycle | Starting sample |
|---|---:|---:|
| 0 | 2048 | `0x00000` |
| 1 | 1024 | `0x80000` |
| 2 | 512 | `0xc0000` |
| 3 | 256 | `0xe0000` |
| 4 | 128 | `0xf0000` |
| 5 | 64 | `0xf8000` |
| 6 | 32 | `0xfc000` |

This is a structural observation about supplied content, not a rule for all ordinary audio WAV files. Parse RIFF chunks; do not assume a fixed PCM offset because additional chunks can precede `data`. No factory WAV or copied preset XML is included here.

See [sequencing](SEQUENCING.md) for running loaded data, and [storage](STORAGE.md) for persistence limits.
