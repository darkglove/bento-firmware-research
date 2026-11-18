# Loaded sequences, automation and scenes

Evidence: original 1.6.8 instructions run in bounded fixtures, compared with independently calculated event/state/audio results. The later integration checkpoint series is indexed in [CHECKPOINTS.md](CHECKPOINTS.md).

## Loading is not playback

The investigation separated several boundaries: XML parsing, native object construction, upload dispatch, asset/file service, engine storage, track bank finalization and actual rendering. Passing one does not imply the next.

Native project-relative filenames and multiple simultaneous assets were exercised. Sample and streamed families use different paths. Slice markers loaded from sample assets, modulation source records and automation lanes were then followed through upload into the receiving engine state.

Track finalization and selection can overwrite state prepared earlier in the load. A useful test must inspect the final selected bank, not merely observe upload calls. Later finalized sample and synth sequences produced exact reference audio in the tested cases; mixed tracks and XML automation were checked separately.

## Track lanes and scene timing

Track sequencing and the song/scene layer have different timing responsibilities. Four automation lanes, notes, modulation-sequencer steps and scene entries cannot be treated as one interchangeable event list.

Tests covered scene switching, boundary voice timing, loop/hold/count behavior, unequal track lengths, stepped automation, linear sliding and transport-grid repeats. These are behavior-specific checkpoints. The phrase “scenes work” would hide the differences between loading a scene, scheduling it, replacing a queued request, and hearing the expected transition.

Manual scene commands were tested both before and after quantization boundaries. A late request can be scheduled differently from one submitted at the beginning of a block. The native CM4 live-scene queue was joined to engine replay, so the tested record layout and queue consumption came from the application side rather than only direct engine injection.

## Empty scenes and replacement

Empty-scene handling includes forward search, wrap and stopping behavior. A reader should not assume an empty scene means either “immediately stop everything” or “repeat forever” without the corresponding native case.

Queued replacement was tested separately from normal progression. Track and scene timing remain distinct: replacing the pending scene is not equivalent to resetting every track's local play position at the same instant. Tests need to record the submitted request time, selected scene, per-track event order and output samples.

## MIDI scene bridge

The project-level MIDI mapper can submit scene requests through the CM4/CM7 bridge. Ordinary track routing has precedence rules: a matching track can suppress project-level scene handling even when it has no valid allocated instrument destination. A silent instrument therefore does not prove that the project mapper received the note.

Serial MIDI, USB-host MIDI and USB-device MIDI have different ingress paths. The [MIDI chapter](MIDI_USB.md) describes those boundaries. Emitting a scene request alone is not proof that the scene was consumed, played or displayed.

## What remains

The normal-path audio comparisons and many boundary cases are substantial compatibility evidence. They do not establish simultaneous physical core execution, arbitrary tempo/swing combinations, every malformed project, real storage latency or the entire UI workflow. Keep fixture assumptions and actual event/audio comparisons alongside any extension to these results.
