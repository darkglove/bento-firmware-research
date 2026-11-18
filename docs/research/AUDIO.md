# Audio engines, modulation and effects

This chapter combines static structure with later original-code emulation and differential models. It describes selected covered paths; it does not claim that a complete standalone replacement instrument suite is distributed here.

## Engine organization

The audio engine is built from typed modules and dynamically assigned units. Tracks, pads, sequencers and voice pools are connected through unit IDs, parameter commands and audio buses. Commands have their own message vocabulary; the fact that two records are 24 bytes long does not make their fields interchangeable.

The initial model identified eight per-track units, 128 per-pad units, two Wavetable pools with ten slots each, and a Granular pool with six slots. Slot count is not the same as advertised polyphony: the examined Wavetable settings cap polyphony at eight and Granular at four. Version-match the dispatcher and assignment protocol before constructing an engine configuration.

## Wavetable and Granular

A Wavetable voice combines two band-limited table readers, a basic oscillator, two envelopes, two low-frequency oscillators and two filters. Rendering includes a doubled-rate stage and an 11-tap half-band decimator. Table morphing and octave-level selection depend on the stored mip pyramid described in [file formats](FILES.md).

The investigation progressed through envelopes, filter coefficient/state handling, table reads, oscillator processing, output/decimation, modulation, macros, sequencing and whole-voice cases. Floating-point operation order, denormal handling and persistent voice state mattered to exact comparison. Agreement for a default patch was not treated as coverage of every modulation route.

The shared pool logic covers note allocation, release, sustain, voice stealing and unison. Unison uses separate voices with a pan spread and random detune; it is not just a louder single oscillator. Stealing preferences and pending retriggers influence transient behavior. Source signals such as mod wheel and pressure must use the actual message representation and scaling.

Granular voices use two grain generators, with sixteen grain slots per generator in the examined structure. Work covered grain startup, scheduling, rendering, generator processing, voice/pool integration and selected whole-instrument comparisons. File and live-input sources are separate configurations. Do not infer a physical live-input latency guarantee from an offline render.

## Modulation and sequencing

Smoothed parameters use a base value and source slots. The numbered modulation-source table and MIDI-CC source range are distinct from parameter IDs. A 32-step per-voice modulation sequencer is distinct from the track sequencer's four automation lanes, each with 256 signed 16-bit values.

Envelope timing, oscillator rate, filter routing, XY macros, LFO synchronization and inherited voice state all affect results. Preserve the order of updates when making a compatible model; replacing all these paths with nominally similar equations can produce audible and sample-level differences.

## Sample families and Shredder

Loop, One-shot, Multisample, Slicer and Shredder have different dispatch and playback behavior. The per-pad Slicer and per-track Shredder are separate engines. Shredder reuses granular scheduling machinery and adds its own resampling/windowing/pan/overlap behavior. It should not be described as merely a UI alias for the Granular synth.

Later integration work connected loaded sample assets, slice positions, project modulation and native sequence uploads to original audio processing. Some normal playback cases matched reference samples across 86,016 stereo frames. That is bounded test evidence, not proof of all sample rates, file formats, timing or failure cases.

## Effects and controller reverb

The main-engine investigation identified compressor, ducker, delay, an effects rack, mixers, preview, metronome, recorders, pad-launch/choke handling and song sequencing. Coverage differs: identifying a setter or module does not establish complete signal processing.

The reverb-send path leaves CM7 over a serial-audio stream and returns from the controller. Later analysis located reverb in `bento2.bin`, superseding the early statement that it was simply an unexplained external loop. Room-path constructor/setter, core processing and module behavior were modeled and compared with original execution, including flush-to-zero effects. Do not extend that Room result to every reverb style or shimmer configuration.

The unchanged companion hash between 1.6.1 and 1.6.8 supports reuse of controller-image findings for that exact file. It does not by itself prove unchanged main-side routing, input levels or system timing. EQ implementation/coverage must likewise not be inferred from the CM4 response-curve UI.

No factory wavetables, preset packages, rendered audio, vendor lookup-table dumps, decompilation or port binaries accompany this chapter. Reproduction should use legitimate local inputs or synthetic signals and explicitly state what was supplied.
