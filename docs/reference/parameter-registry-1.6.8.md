# Parameter registry, Bento 1.6.8 (CM7 copy; CM4 copy is identical)

Source image `bento1.bin` SHA-256 `cb8f830ec3ab45a92d120ae9688e380573b24ad88710a3ad3d21af6ffb3c8d0d`.
Decoded by emulating the registry constructor at `0x08068be0`. The original extraction harness is not packaged in this edition.
**`id` is a per-build slot index and is renumbered whenever a parameter is inserted; the storage `key` is the stable identity.**
Ranges are raw integers; most percent-like values are 0..1000 (= 0.0..100.0 %), gains are milli-dB, pitch is milli-semitones.

`first` = first version whose registry contains the key. `types` = object types (see object-model-1.6.8.md) whose ROM schema lists the key.

| id | key | label | code | range / options | first | types |
|---:|---|---|---:|---|---|---|
| 2 | `gaindb` | Level | 9 | -96000..12000 | 1.2.4 | 01,02,03,04 |
| 3 | `pitch` | Pitch | 14 | -24000..24000 | 1.2.4 | 01,02,03,04,06,07,08 |
| 4 | `panpos` | Pan | 11 | -1000..1000 | 1.2.4 | 01,02,03,04 |
| 5 | `samtrigtype` | LaunchMode | 7 | enum[3]: Trigger, Gate, Toggle | 1.2.4 | 01,02,03,04 |
| 6 | `samtrigtype` | LaunchMode | 7 | enum[2]: Trigger, Gate | 1.2.4 | 01,02,03,04 |
| 7 | `loopmode` | Loop Mode | 6 | 0..1000 | 1.2.4 | 02,03,04 |
| 8 | `loopmodes` | Loop Mode | 7 | enum[3]: None, Forward, Bidirect | 1.2.4 | 01,07 |
| 9 | `midiinport` | MIDI In Port | 7 | enum[4]: All, TRS 1, TRS 2, USB | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 10 | `midiinchan` | MIDI In Chan | 7 | enum[17]: None,  1,  2,  3,  4,  5, … | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 11 | `cc1inport` | CC 1 Port | 7 | enum[4]: All, TRS 1, TRS 2, USB | 1.2.4 | 0e,0f,10,11,12,13,14,17 |
| 12 | `cc1inchan` | CC 1 Chan | 7 | enum[17]: None,  1,  2,  3,  4,  5, … | 1.2.4 | 0e,0f,10,11,12,13,14,17 |
| 13 | `cc2inport` | CC 2 Port | 7 | enum[4]: All, TRS 1, TRS 2, USB | 1.2.4 | 0e,0f,10,11,12,13,14,17 |
| 14 | `cc2ininchan` | CC 2 Chan | 7 | enum[17]: None,  1,  2,  3,  4,  5, … | 1.2.4 | 0e,0f,10,11,12,13,14 |
| 15 | `midioutport` | MIDIOutPrt | 7 | enum[4]: All, TRS 1, TRS 2, USB | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 16 | `midioutchan` | MIDI OutCh | 7 | enum[17]: None,  1,  2,  3,  4,  5, … | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 19 | `projmidiinport` | ProjMidiInPrt | 7 | enum[4]: All, TRS 1, TRS 2, USB | 1.5.9 | 15 |
| 20 | `projmidiinchan` | ProjMidiInCh | 7 | enum[17]: None,  1,  2,  3,  4,  5, … | 1.5.9 | 15 |
| 21 | `padrec` | Pad Rec | 7 | enum[2]: Off, On | 1.6 | 0e,11,17 |
| 22 | `metroopts` | Metronome: | 7 | enum[3]: Off, Rec, Play | 1.2.4 | 15 |
| 23 | `metoutbus` | Met Output: | 7 | enum[3]: 1, 2, 3 | 1.2.4 | 15 |
| 24 | `metgain` | Met Gain: | 9 | -60000..6000 | 1.2.4 | 2d |
| 27 | `reccountdown` | Count In: | 6 | 0..1000 | 1.2.4 | 15 |
| 28 | `reverse` | Reverse | 6 | 0..1000 | 1.2.4 | 01,02 |
| 29 | `cellmode` | Pad Mode | 7 | enum[6]: Multisample, Clip, Slicer, Granular, New Rec, New Multi | 1.2.4 | 01,02,03,04 |
| 30 | `envattack` | Attack | 10 | 0..1000 | 1.2.4 | 01,02,03,04,09 |
| 31 | `envdecay` | Decay | 10 | 0..1000 | 1.2.4 | 01,02,03,04,09 |
| 32 | `envsus` | Sustain | 10 | 0..1000 | 1.2.4 | 01,02,03,04,09 |
| 33 | `envrel` | Release | 10 | 0..1000 | 1.2.4 | 01,02,03,04,09 |
| 34 | `samstart` | Start | 15 | 0..1000 | 1.2.4 | 05,07 |
| 35 | `samlen` | Length | 15 | 0..1000 | 1.2.4 | 05,06,07 |
| 36 | `loopstart` | Loop Start | 15 | 0..1000 | 1.2.4 | 05 |
| 37 | `loopend` | Loop End | 15 | 0..1000 | 1.2.4 | 05 |
| 38 | `—` | StreamLength | 2 | 0..-1 | — |  |
| 39 | `quantsize` | Quant Size | 7 | enum[9]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/4, … | 1.2.4 | 02,0c |
| 40 | `synctype` | Sync | 7 | enum[7]: Slice, 1 bar, 1/2, 1/4, 1/8, 1/16, … | 1.2.4 | 02,03,04 |
| 41 | `actslice` | Act Slice | 2 | 1..128 | 1.2.4 | 03,04 |
| 43 | `slicepadstart` | Pad Start | 2 | 1..127 | 1.2.4 | 03,04 |
| 45 | `outputbus` | Output | 7 | enum[4]: 1, 1 w/ Mod FX, 2, 3 | 1.2.4 | 01,02,03,04,0e,0f,10,11,12,13,14,16,17 |
| 46 | `polymode` | Poly Mode | 7 | enum[6]: Mono, Poly 2, Poly 4, Poly 6, Poly 8, Poly X | 1.2.4 | 01,02 |
| 47 | `polymodeslice` | Poly Mode | 7 | enum[2]: Mono, Poly 2 | 1.2.4 | 03,04 |
| 48 | `slicestepmode` | Slice Seq | 7 | enum[5]: None, Forward, Backwards, Random, Stagger | 1.2.4 | 03,04 |
| 49 | `chokegrp` | Choke Grp | 7 | enum[5]: None, A, B, C, D | 1.2.4 | 01,02,03,04 |
| 50 | `dualfilcutoff` | Filter | 11 | -1000..1000 | 1.2.4 | 01,02,03,04 |
| 51 | `res` | Resonance | 10 | 0..1000 | 1.2.4 | 01,02,03,04,0a |
| 52 | `rootnote` | Root Note | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.2.4 | 05 |
| 53 | `beatcount` | Beat Count | 7 | enum[513]: Auto, 1, 2, 3, 4, 5, … | 1.2.4 | 02,03,04 |
| 54 | `fx1send` | Delay Send | 10 | 0..1000 | 1.2.4 | 01,02,03,04,1d |
| 55 | `fx2send` | ReverbSend | 10 | 0..1000 | 1.2.4 | 01,02,03,04,1d |
| 56 | `fx3send` | FX3 Send | 10 | 0..1000 | 1.2.4 |  |
| 57 | `fx4send` | FX4 Send | 10 | 0..1000 | 1.2.4 |  |
| 58 | `multisammode` | MultiSam | 6 | 0..0 | 1.2.4 | 01 |
| 59 | `interpqual` | Interp | 7 | enum[2]: Normal, HighQ | 1.2.4 | 01 |
| 60 | `playthru` | Play Thru | 6 | 0..0 | 1.2.4 | 03,04 |
| 61 | `slicerquantsize` | Quant Size | 7 | enum[14]: 2 bars, 1 bar, 1/2, 1/2T, 1/4, 1/4T, … | 1.2.4 | 03,04 |
| 62 | `slicersync` | Sync | 6 | 0..1000 | 1.2.4 | 03,04 |
| 63 | `gransplaymode` | Play Mode | 7 | enum[3]: Slice, Granular, Slice+Grain | 1.5.3 | 04 |
| 64 | `gransgrainsize` | Grain Size | 10 | 0..1000 | 1.5.3 | 04 |
| 65 | `gransgraindensity` | Density | 10 | 0..1000 | 1.5.3 | 04 |
| 66 | `gransgrainjitter` | Jitter | 10 | 0..1000 | 1.5.3 | 04 |
| 67 | `gransgrainwindow` | Window | 10 | 0..1000 | 1.5.3 | 04 |
| 68 | `gransgraindetune` | Detune | 10 | 0..1000 | 1.5.3 | 04 |
| 69 | `gransgrainbeatsync` | Beat Sync | 6 | 0..1 | 1.5.3 | 04 |
| 70 | `granssyncrate` | Sync Rate | 7 | enum[15]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, … | 1.5.3 | 04 |
| 71 | `gransspeed` | Speed | 10 | 0..2000 | 1.5.3 | 04 |
| 72 | `padnote` | Pad Note | 7 | enum[128]: Default, C#-1, D-1, D#-1, E-1, F-1, … | 1.2.4 |  |
| 73 | `loopfadeamt` | Loop Fade | 10 | 0..1000 | 1.2.4 | 01 |
| 74 | `lfowave` | LFO Shape | 7 | enum[9]: Rev Saw, Saw, Triangle, Pos Tri, Sine, Pos Sine, … | 1.2.4 | 01,02,03,04,0b |
| 75 | `lforate` | LFO Rate | 10 | 0..1000 | 1.2.4 | 01,02,03,04,0b,1e,1f |
| 76 | `lfoamount` | LFO Depth | 10 | 0..1000 | 1.2.4 | 01,02,03,04,0b |
| 77 | `lfokeytrig` | Restart | 6 | 0..1000 | 1.2.4 | 01,02,03,04,0b |
| 78 | `lfobeatsync` | Beat Sync | 6 | 0..1000 | 1.2.4 | 01,02,03,04,0b |
| 79 | `lforatebeatsync` | LFO Rate | 7 | enum[15]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, … | 1.2.4 | 01,02,03,04,0b |
| 80 | `grainsizeperc` | Grain Size | 10 | 0..1000 | 1.2.4 | 07 |
| 81 | `grainscat` | Scatter | 10 | 0..1000 | 1.2.4 |  |
| 82 | `grainpanrnd` | Pan Random | 10 | 0..1000 | 1.2.4 | 07 |
| 83 | `graindensity` | Density | 10 | 0..1000 | 1.2.4 | 07 |
| 84 | `slicemode` | Slice Mode | 6 | 0..1000 | 1.2.4 |  |
| 85 | `legatomode` | Legato | 6 | 0..1 | 1.2.4 | 01 |
| 86 | `gainssrcwin` | Window | 10 | 0..1000 | 1.2.4 | 07 |
| 87 | `grainreadspeed` | Speed | 10 | 0..2000 | 1.2.4 | 07 |
| 88 | `grainliveinputfreeze` | Freeze | 6 | 0..1000 | 1.4.1 | 07 |
| 89 | `recpresetlen` | Length | 7 | enum[11]: Custom, 1/4, 1/2, 1 bar, 2 bars, 4 bars, … | 1.2.4 | 0e,10,11,12,13,14,17 |
| 90 | `recquant` | Rec Quant | 7 | enum[9]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/4, … | 1.2.4 | 0e,10,11,12,13,14,17 |
| 91 | `recinput` | Rec Input | 7 | enum[9]: In 1, In 2, In 3, USB, In 1L, In 2L, … | 1.2.4 | 0e,10,11,12,13,14,17,2d |
| 92 | `recusethres` | Rec Thresh | 6 | 0..1 | 1.2.4 | 0e,10,11,12,13,14,17,2d |
| 93 | `recthresh` | Threshold | 9 | -96000..0 | 1.2.4 | 0e,10,11,12,13,14,17,2d |
| 94 | `recmonoutbus` | Mon Output | 7 | enum[4]: 1, 1 w/ Mod FX, 2, 3 | 1.2.4 |  |
| 95 | `velamount` | Velocity | 11 | -1000..1000 | 1.2.4 | 01,02,03,04,09 |
| 96 | `notesteplen` | Step Len | 7 | enum[15]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, … | 1.2.4 | 18 |
| 97 | `seqstepmode` | Snap Mode | 6 | 0..1000 | 1.2.4 | 18 |
| 98 | `notestepcount` | Step Count | 7 | enum[257]: Open, 1, 2, 3, 4, 5, … | 1.2.4 | 18 |
| 100 | `seqplayenable` | PlayMode | 6 | 0..0 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 103 | `midiouttype` | MIDI Type | 7 | enum[2]: Type A, Type B | 1.2.4 | 2d |
| 104 | `quantsizeseq` | Quant Size: | 7 | enum[13]: 2 bars, 1 bar, 1/2, 1/2T, 1/4, 1/4T, … | 1.2.4 | 18 |
| 105 | `sceneplaycount` | Play Count | 2 | 1..32 | 1.2.4 | 2b |
| 106 | `songmode` | Song Mode | 6 | 0..1 | 1.2.4 | 15 |
| 107 | `quantsizesong` | Quant Size: | 7 | enum[13]: 2 bars, 1 bar, 1/2, 1/2T, 1/4, 1/4T, … | 1.2.4 | 15 |
| 108 | `songSceneHold` | Scene Hold | 6 | 0..1 | 1.2.4 | 15 |
| 109 | `songloop` | Song Loop | 6 | 0..1 | 1.2.4 | 15 |
| 110 | `lgmask` | Group Loops | 1 | 0..65535 | 1.5.3 | 2e |
| 111 | `lgindex` | Group Index | 1 | 0..7 | 1.5.3 | 2e |
| 112 | `lgcustom` | Custom Name | 1 | 0..1 | 1.5.30 | 2e |
| 114 | `cliplength` | ClipLength | 1 | 0..256 | 1.2.4 | 02 |
| 115 | `celldisppos` | Disp Pos | 1 | 0..15 | 1.2.4 | 01,02,03,04,0e,0f,10,11,12,13,14,16,17,18,2b |
| 116 | `selcellpos` | Selected Cell Pos | 1 | 0..15 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 117 | `selscenepos` | Selected Scene Pos | 1 | 0..15 | 1.2.4 | 15 |
| 118 | `scenetrackindex` | Track Index | 1 | 0..7 | 1.2.4 | 2c |
| 119 | `sceneseqindex` | Seq Index | 1 | 0..15 | 1.2.4 | 2c |
| 122 | `keyrangebottom` | Low Note | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.2.4 | 05 |
| 123 | `keyrangetop` | High Note | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.2.4 | 05 |
| 124 | `velroot` | Vel Root: | 1 | 0..127 | 1.2.4 | 05 |
| 125 | `velrangebottom` | Low Vel: | 1 | 0..127 | 1.2.4 | 05 |
| 126 | `velrangetop` | High Vel: | 1 | 0..127 | 1.2.4 | 05 |
| 129 | `filename` | Filename | 19 | 0..0 | 1.2.4 | 05,06,07 |
| 130 | `cellname` | Cell Name | 19 | 0..0 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17,18,2b,2e |
| 131 | `screenbrightness` | Brightness | 10 | 0..1000 | 1.2.4 | 2d |
| 132 | `padbrightness` | Pad Bright | 7 | enum[6]: 1, 2, 3, 4, 5, 6 | 1.6 | 2d |
| 139 | `sdsafemode` | SD Mode: | 7 | enum[2]: High Speed, Compatible | 1.2.4 | 2d |
| 140 | `globtempo` | BPM | 2 | 40..250 | 1.2.4 | 0d,15 |
| 141 | `keymode` | Scale | 7 | enum[23]: Chromatic, Major, Major Pent, Minor, Minor Pent, Minor Blues, … | 1.2.4 | 15 |
| 142 | `keyroot` | Root Note | 7 | enum[12]: A, A#, B, C, C#, D, … | 1.2.4 | 15 |
| 143 | `swing` | Swing | 2 | 1..99 | 1.2.4 | 15 |
| 156 | `globcomp` | Compressor: | 6 | 0..1 | 1.2.4 | 23 |
| 162 | `padthresh` | Pad Thresh | 10 | 1..1000 | 1.2.4 | 2d |
| 163 | `autosleep` | Sleep | 6 | 0..1000 | 1.2.4 | 2d |
| 164 | `battchargelimit` | Battery | 7 | enum[2]: Runtime, Lifespan | 1.5.32 | 2d |
| 169 | `maingain` | Main | 9 | -60000..6000 | 1.2.4 | 15 |
| 193 | `—` | Trim Start | 15 | 0..1000 | — |  |
| 194 | `—` | Trim End | 15 | 0..1000 | — |  |
| 195 | `waveform` | Waveform | 7 | enum[5]: Rev Saw, Triangle, Square, Sine, Noise | 1.2.4 | 08 |
| 196 | `level` | Level | 10 | 0..1000 | 1.2.4 | 06,07,08 |
| 197 | `dutycyc` | Pulse Width | 10 | 0..1000 | 1.2.4 | 08 |
| 198 | `oscphasereset` | WTOscReset | 6 | 0..1 | 1.2.4 | 0d |
| 199 | `wavesel` | Wavetable | 7 | enum[103]: AEAHOHOOo, AllSquares, AmpMod1, AmpModSlow, AngularAM, AnimSaws, … | 1.2.4 | 06,07 |
| 201 | `wavepos` | Position | 1 | 0..255 | 1.2.4 | 06 |
| 202 | `wtblusepolymode` | Poly Mode Used | 6 | 0..1000 | 1.2.16 | 0d |
| 203 | `wtblpolymode` | Poly Mode | 7 | enum[15]: Unison 1, Unison 2, Unison 3, Unison 4, Unison 5, Unison 6, … | 1.2.16 | 0d |
| 206 | `cutoff` | Cutoff | 12 | 0..1000 | 1.2.4 | 0a |
| 207 | `cutoffFx` | Cutoff | 12 | 0..1000 | 1.2.4 | 1c,21 |
| 208 | `filtertype` | Type | 7 | enum[4]: Low Pass, High Pass, Band Pass, Notch | 1.2.4 | 0a |
| 209 | `filtenable` | Filter | 6 | 0..1 | 1.2.4 | 0a,1c,21 |
| 210 | `filtparallel` | Mode | 7 | enum[3]: Serial, Parallel, Per Osc | 1.2.4 | 0a |
| 211 | `filtwvtblparallel` | Mode | 7 | enum[2]: Serial, Parallel | 1.2.16 |  |
| 212 | `steplen` | Step Len | 7 | enum[13]: 2 bars, 1 bar, 1/2, 1/2T, 1/4, 1/4T, … | 1.2.4 | 0c |
| 213 | `seqsteps` | Steps | 2 | 2..32 | 1.2.4 | 0c |
| 214 | `seqkeytrig` | Key Trig | 6 | 0..1000 | 1.2.4 | 0c |
| 215 | `seqquant` | Quantize | 6 | 0..1000 | 1.2.4 | 0c |
| 216 | `unisonmode` | Unison | 6 | 0..1 | 1.2.4 | 0d |
| 217 | `unisondetune` | Detune | 10 | 0..1000 | 1.2.4 | 0d |
| 218 | `unisonspread` | Pan Spread | 10 | 0..1000 | 1.2.4 | 0d |
| 219 | `unisonvcount` | Voices | 1 | 1..8 | 1.2.4 | 0d |
| 222 | `macroxsnap` | X Mod Snap | 11 | -1000..1000 | 1.2.4 | 0d |
| 223 | `macroysnap` | Y Mod Snap | 11 | -1000..1000 | 1.2.4 | 0d |
| 225 | `midibend` | MIDIBndRng | 2 | 1..12 | 1.2.4 | 0d,2d |
| 228 | `graninput` | Input | 7 | enum[8]: In 1, In 2, In 3, USB, In 1L, In 2L, … | 1.3.30 | 13 |
| 229 | `overdrive` | Overdrive | 10 | 0..1000 | 1.2.4 | 01,02,03,04 |
| 230 | `amount` | Wet Amount | 10 | 0..1000 | 1.2.4 | 1e,20,21,22 |
| 231 | `feedback` | Feedback | 10 | 0..1000 | 1.2.4 | 1c,1e,1f,21 |
| 232 | `feedback` | Feedback | 11 | -1000..1000 | 1.2.4 | 1c,1e,1f,21 |
| 233 | `delay` | Delay | 10 | 0..1000 | 1.2.4 | 1c,21 |
| 234 | `delaymustime` | Delay | 7 | enum[12]: 1/64, 1/32, 1/16, 1/8T, 1/16D, 1/8, … | 1.2.4 | 1c,21 |
| 235 | `dealybeatsync` | Beat Sync | 6 | 0..1000 | 1.2.4 | 1c,21 |
| 236 | `delaypingpong` | Ping Pong | 6 | 0..1 | 1.2.4 | 1c,21 |
| 241 | `fxholda` | Hold A | 6 | 0..1 | 1.5.3 | 15 |
| 242 | `fxholdb` | Hold B | 6 | 0..1 | 1.5.3 | 15 |
| 243 | `filtquality` | Width | 10 | 0..1000 | 1.2.4 | 1c,21 |
| 244 | `wet` | Wet/Dry: | 10 | 0..1000 | 1.2.4 | 19 |
| 245 | `rptlen` | Rpt Len | 7 | enum[4]: 1/4, 1/8, 1/16, 1/32 | 1.5.3 |  |
| 246 | `gatelen` | Gate Len | 7 | enum[4]: 1/4, 1/8, 1/16, 1/32 | 1.5.3 |  |
| 247 | `gateduty` | Duty Cyc | 10 | 0..1000 | 1.5.3 |  |
| 248 | `echodly` | Delay | 7 | enum[11]: 1/2, 1/2T, 1/4, 1/4T, 1/8, 1/8T, … | 1.5.3 |  |
| 249 | `echofb` | Feedback | 10 | 0..1000 | 1.5.3 |  |
| 250 | `echohpf` | HPF | 12 | 0..1000 | 1.5.3 |  |
| 251 | `echo2dly` | Delay | 7 | enum[6]: 1/2, 1/4, 1/8, 1/16, 1/32, 1/64 | 1.5.3 |  |
| 252 | `fxliveatype` | LiveA FX | 7 | enum[3]: Repeater, Gater, Filter | 1.5.3 | 15 |
| 253 | `fxlivebtype` | LiveB FX | 7 | enum[6]: Bitcrusher, Filter, Echo, Echo HPF, Flanger, Echo 2 | 1.5.3 | 15 |
| 254 | `decay` | Decay | 10 | 0..1000 | 1.2.4 | 1a,22 |
| 255 | `damping` | Damping | 10 | 0..1000 | 1.2.4 | 1a,22 |
| 256 | `predelay` | Pre-Delay | 10 | 0..1000 | 1.2.4 | 1a,22 |
| 259 | `fx3type` | Type | 7 | enum[3]: Flanger+Dist, Chorus, Phaser | 1.2.4 | 1d |
| 261 | `prevtargid` | PrevTargID | 1 | 0..-1 | 1.2.31 |  |
| 262 | `prevtargclr` | PrevTargClr | 6 | 0..1 | 1.2.31 |  |
| 263 | `prevsamplen` | PrevSampleLen | 2 | 1..480000 | 1.2.31 |  |
| 264 | `eqgain` | Gain: | 9 | -24000..24000 | 1.2.4 |  |
| 265 | `eqcutoff` | Freq: | 12 | 0..1000 | 1.2.4 |  |
| 266 | `eqres` | Q: | 13 | 0..1000 | 1.2.4 |  |
| 267 | `eqenable` | Enable: | 6 | 0..1 | 1.2.4 |  |
| 268 | `eqtype` | Type: | 8 | enum[6]: None, L Cut, L Shelf, Param, H Shelf, H Cut | 1.2.4 |  |
| 269 | `eqgain2` | Gain: | 9 | -24000..24000 | 1.2.4 |  |
| 270 | `eqcutoff2` | Freq: | 12 | 0..1000 | 1.2.4 |  |
| 271 | `eqres2` | Q: | 13 | 0..1000 | 1.2.4 |  |
| 272 | `eqenable2` | Enable: | 6 | 0..1 | 1.2.4 |  |
| 273 | `eqtype2` | Type: | 8 | enum[6]: None, L Cut, L Shelf, Param, H Shelf, H Cut | 1.2.4 |  |
| 274 | `eqgain3` | Gain: | 9 | -24000..24000 | 1.2.4 |  |
| 275 | `eqcutoff3` | Freq: | 12 | 0..1000 | 1.2.4 |  |
| 276 | `eqres3` | Q: | 13 | 0..1000 | 1.2.4 |  |
| 277 | `eqenable3` | Enable: | 6 | 0..1 | 1.2.4 |  |
| 278 | `eqtype3` | Type: | 8 | enum[6]: None, L Cut, L Shelf, Param, H Shelf, H Cut | 1.2.4 |  |
| 279 | `eqgain4` | Gain: | 9 | -24000..24000 | 1.2.4 |  |
| 280 | `eqcutoff4` | Freq: | 12 | 0..1000 | 1.2.4 |  |
| 281 | `eqres4` | Q: | 13 | 0..1000 | 1.2.4 |  |
| 282 | `eqenable4` | Enable: | 6 | 0..1 | 1.2.4 |  |
| 283 | `eqtype4` | Type: | 8 | enum[6]: None, L Cut, L Shelf, Param, H Shelf, H Cut | 1.2.4 |  |
| 285 | `eqbypass` | Bypass | 6 | 0..1 | 1.2.4 |  |
| 286 | `eqactband` | Band | 1 | 0..3 | 1.2.4 |  |
| 287 | `eqbandbypass` | Bypass | 6 | 0..1 | 1.5.3 |  |
| 288 | `eqbandbypass2` | Bypass | 6 | 0..1 | 1.5.3 |  |
| 289 | `eqbandbypass3` | Bypass | 6 | 0..1 | 1.5.3 |  |
| 290 | `eqbandbypass4` | Bypass | 6 | 0..1 | 1.5.3 |  |
| 291 | `cattack` |   Attack: | 17 | 0..250 | 1.2.4 | 23 |
| 292 | `crelease` |   Release: | 17 | 0..10000 | 1.2.4 | 23 |
| 293 | `cthreshdb` |   Thresh: | 9 | -48000..0 | 1.2.4 | 23 |
| 294 | `cratio` |   Ratio: | 18 | 1..100 | 1.2.4 | 23 |
| 295 | `cautomakeup` |   AutoMkup: | 6 | 0..1 | 1.2.4 | 23 |
| 302 | `cgaindb` |   Gain: | 9 | -36000..36000 | 1.2.4 | 23 |
| 303 | `cbypass` |   Bypass: | 6 | 0..1 | 1.2.4 |  |
| 304 | `peaklimit` | Peak Limit: | 6 | 0..1 | 1.2.4 | 23 |
| 307 | `selseqpos` | Selected Cell Pos | 1 | 0..15 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 308 | `trkgain` | Level | 9 | -60000..6000 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 309 | `out1gain` | Out 1 | 9 | -60000..6000 | 1.2.4 | 2d |
| 310 | `out2gain` | Out 2 | 9 | -60000..6000 | 1.2.4 | 2d |
| 311 | `out3gain` | Out 3 | 9 | -60000..6000 | 1.2.4 | 2d |
| 312 | `outphonesgain` | Phones | 9 | -60000..0 | 1.2.4 | 2d |
| 313 | `in1gain` | Input Gain | 9 | -60000..12000 | 1.2.4 | 16 |
| 314 | `ledbrightness` | LED Brightness | 9 | 0..1000 | 1.2.4 |  |
| 315 | `trkmute` | Mute | 6 | 0..1 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 316 | `trksolo` | Solo | 6 | 0..1 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 317 | `trkpan` | Pan | 11 | -1000..1000 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 318 | `trkfx1send` | Delay Send | 10 | 0..1000 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 319 | `trkfx2send` | Reverb Send | 10 | 0..1000 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 321 | `trkinput` | Input | 7 | enum[8]: In 1, In 2, In 3, USB, In 1L, In 2L, … | 1.2.4 | 16,17 |
| 323 | `graninputgain` | Gain | 9 | -60000..12000 | 1.3.30 | 13 |
| 324 | `grainjitter` | Jitter | 10 | 0..1000 | 1.2.4 | 07 |
| 325 | `grainbeatsync` | Beat Sync | 6 | 0..1000 | 1.2.4 | 07 |
| 326 | `grainbeatrate` | Rate | 7 | enum[15]: 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, … | 1.2.4 | 07 |
| 327 | `grainpitchpatt` | Pattern | 7 | enum[3]: None, Octaves, Fifths | 1.2.4 | 07 |
| 329 | `grainfreezemode` | Play Mode | 7 | enum[2]: Moving, Fixed | 1.2.4 | 07 |
| 330 | `grainfreezepos` | Play Pos | 10 | 0..1000 | 1.2.4 | 07 |
| 331 | `grainliveinpos` | Live Pos | 10 | -1000..0 | 1.2.4 | 07 |
| 332 | `graindetune` | Detune | 10 | 0..1000 | 1.2.4 | 07 |
| 333 | `grainsaveattack` | Presrv Atk | 6 | 0..1000 | 1.2.4 | 07 |
| 334 | `grainliveinput` | Live Input | 6 | 0..1000 | 1.2.4 | 07 |
| 335 | `grainshape` | Gr Shape | 7 | enum[3]: Smooth, Ramp Down, Ramp Up | 1.2.4 | 07 |
| 336 | `samstartpercent` | Start Pos | 10 | 0..1000 | 1.2.4 | 07 |
| 337 | `granpolymode` | Poly Mode | 7 | enum[5]: Mono, Poly 2, Poly 3, Poly 4, Poly X | 1.2.4 | 13,17 |
| 338 | `grancpuamount` | CPU | 10 | 0..1000 | 1.2.4 | 13,17 |
| 339 | `combamt` | Comb Amount | 11 | -1000..1000 | 1.2.4 | 19 |
| 340 | `combtime` | Comb Time | 10 | 0..1000 | 1.2.4 | 19 |
| 341 | `combfb` | Comb FB | 11 | -1000..1000 | 1.2.4 | 19 |
| 342 | `comblfoamt` | Comb LFO | 10 | 0..1000 | 1.2.4 | 19 |
| 343 | `comblfort` | Comb LFO Rt | 10 | 0..1000 | 1.2.4 | 19 |
| 344 | `cabdistamt` | Distortion | 10 | 0..1000 | 1.2.4 | 19 |
| 345 | `cabdisttype` | Dist Type | 7 | enum[3]: Artificial, Solid State, Tube | 1.2.4 | 19 |
| 346 | `cabprefreq` | Pre Freq | 12 | 0..1000 | 1.2.4 | 19 |
| 347 | `cabpostfreq` | Post Freq | 12 | 0..1000 | 1.2.4 | 19 |
| 348 | `flangeamount` | Flng Depth | 10 | 0..1000 | 1.2.4 | 1d,1f |
| 349 | `flangelforate` | Flng Rate | 10 | 0..1000 | 1.2.4 | 1d |
| 350 | `flangefeedback` | Flng Fdbk | 11 | -1000..1000 | 1.2.4 | 1d |
| 351 | `flangphase` | Phase | 10 | 0..1000 | 1.5.3 |  |
| 352 | `flangfb` | Feedback | 10 | 0..1000 | 1.5.3 |  |
| 353 | `bitdepth` | Bit Depth | 10 | 0..1000 | 1.5.3 |  |
| 354 | `ratereduc` | Rate Reduc | 10 | 0..1000 | 1.5.3 |  |
| 355 | `distamount` | Dist Depth | 10 | 0..1000 | 1.2.4 | 1d,1f |
| 356 | `phaseamount` | Phase Amt | 10 | 0..1000 | 1.2.4 | 1d |
| 357 | `phasefeedback` | Phse Fdbk | 11 | -1000..1000 | 1.2.4 | 1d |
| 358 | `phaselforate` | Phase Rate | 10 | 0..1000 | 1.2.4 | 1d |
| 359 | `chorusamount` | Chrs Depth | 10 | 0..1000 | 1.2.4 | 1d |
| 360 | `chorusrate` | Chrs Rate | 10 | 0..1000 | 1.2.4 | 1d |
| 361 | `chorrate` | Chrs Rate | 10 | 0..1000 | 1.2.4 | 20 |
| 362 | `—` | Page | 4 | 0..341 | — |  |
| 363 | `—` | Line | 4 | 0..2048 | — |  |
| 364 | `previewvolume` | Prev Vol | 9 | -60000..0 | 1.5.3 | 2d |
| 365 | `—` | Step | 4 | 2..32 | — |  |
| 366 | `—` | Amount | 2 | -1000..1000 | — |  |
| 367 | `—` | Source 1 | 4 | 0..34 | — |  |
| 368 | `—` | Amount 1 | 11 | -1000..1000 | — |  |
| 369 | `—` | Source 2 | 4 | 0..34 | — |  |
| 370 | `—` | Amount 2 | 11 | -1000..1000 | — |  |
| 371 | `—` | Source 3 | 4 | 0..34 | — |  |
| 372 | `—` | Amount 3 | 11 | -1000..1000 | — |  |
| 374 | `padrowoffset` | Pad Row Offset | 1 | -5..5 | 1.2.4 | 0e,0f,10,11,12,13,14,16,17 |
| 375 | `—` | Slice Pos | 15 | 0..1000 | — |  |
| 376 | `—` | Scroll | 6 | 0..1000 | — |  |
| 377 | `scanthres` | Threshold | 10 | 0..1000 | 1.2.4 |  |
| 378 | `gridcount` | Slices | 2 | 2..128 | 1.2.4 |  |
| 379 | `—` | Sel Slice | 2 | 1..128 | — |  |
| 380 | `—` | Event | 2 | 1..1 | — |  |
| 381 | `—` | Start | 2 | 0..256 | — |  |
| 382 | `—` | Length | 2 | 1..16384 | — |  |
| 383 | `—` | Start | 10 | 0..1000 | — |  |
| 384 | `—` | Length | 10 | 20..1000 | — |  |
| 385 | `—` | Velocity | 1 | 1..127 | — |  |
| 386 | `evtcond` | Prob | 7 | enum[100]: 1%%, 2%%, 3%%, 4%%, 5%%, 6%%, … | 1.2.4 |  |
| 387 | `—` | Note | 7 | enum[127]: C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), F#-1 (6), … | — |  |
| 388 | `—` | Pad | 3 | 1..16 | — |  |
| 389 | `patchPickType` | Type | 7 | enum[8]: All, Granular, Loop, Multisample, One-Shot, Shredder, … | 1.2.16 |  |
| 390 | `uiSequencerType` | Sequencer Type | 1 | 0..1 | 1.5.3 | 0e |
| 391 | `uiSelectedPad` | Selected Pad | 1 | 0..15 | 1.5.3 | 2d |
| 392 | `uiPadFrameOffset` | Pad Frame Offset | 1 | 0..32767 | 1.5.3 | 18 |
| 393 | `noteSeqStepOffset` | Offset | 1 | -470..470 | 1.5.3 |  |
| 394 | `—` | Offset | 1 | -47..47 | — |  |
| 396 | `r2predelay` | Pre Delay | 17 | 0..4990 | 1.2.4 | 1b |
| 410 | `r2freeze` | Freeze | 6 | 0..1000 | 1.2.4 | 1b |
| 417 | `r2style` | Style: | 7 | enum[15]: Tight Amb, Bright Room, Large Room, Wide Slap, Notchy Amb, Reso Room, … | 1.2.4 | 1b |
| 421 | `r2lowcut` | Low Cutoff: | 10 | 0..1000 | 1.2.4 | 1b |
| 422 | `r2highcut` | Hi Cutoff | 10 | 0..1000 | 1.2.4 | 1b |
| 425 | `r2metatime` | Time | 10 | 0..1000 | 1.2.4 | 1b |
| 426 | `r2metalevel` | Level: | 10 | 0..1000 | 1.2.4 | 1b |
| 428 | `shimfeedbk` | Shim Fbk | 10 | 0..1000 | 1.2.4 | 1b |
| 429 | `shimshift` | Shift | 2 | -24..24 | 1.2.4 | 1b |
| 438 | `rvbalgo` | Reverb | 7 | enum[2]: Room, Shimmer | 1.6 | 1b |
| 440 | `recautoplay` | RecToPlay: | 6 | 0..1 | 1.2.4 | 0e,10,11,12,13,14,17 |
| 441 | `recactive` | Rec Active: | 6 | 0..1 | 1.2.4 | 0e,10,11,12,13,14,17 |
| 443 | `recmonmode` | Rec Mon | 7 | enum[2]: Off, Auto | 1.2.4 | 0e,10,11,12,13,14,17,2d |
| 444 | `recgain` | Rec Gain | 9 | -60000..12000 | 1.2.4 | 0e,10,11,12,13,14,17,2d |
| 453 | `mrnotelen` | Note Len | 2 | 1..60 | 1.2.4 | 2d |
| 454 | `mrrellen` | Release: | 2 | 1..15 | 1.2.4 | 2d |
| 455 | `mrecmidich` | MIDI OutCh | 2 | 1..16 | 1.2.4 | 2d |
| 457 | `mrstartnote` | Start Note: | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.2.4 | 2d |
| 458 | `mrendnote` | End Note: | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.2.4 | 2d |
| 459 | `mrstride` | Rec Every | 2 | 1..16 | 1.2.4 | 2d |
| 460 | `mrvellayers` | Vel Layers: | 2 | 1..16 | 1.2.4 | 2d |
| 461 | `mrmaxvel` | Max Vel: | 2 | 1..127 | 1.2.4 | 2d |
| 466 | `dateyear` | Year | 2 | 2000..2100 | 1.3.17 |  |
| 467 | `datemonth` | Month | 2 | 1..12 | 1.3.17 |  |
| 468 | `dateday` | Day | 2 | 1..31 | 1.3.17 |  |
| 469 | `datehour` | Hour | 2 | 0..23 | 1.3.17 |  |
| 470 | `dateminute` | Minute | 2 | 0..59 | 1.3.17 |  |
| 471 | `lastknowndate` | LastDate | 2 | 0..21001231 | 1.6.8 | 2d |
| 472 | `bp_uiSeqKnobMode` | Selected Knob Mode | 1 | 0..2 | 1.5.20 | 18 |
| 474 | `seqslide` | Slide | 6 | 0..1000 | 1.6 | 0c,18 |
| 475 | `—` | Lane | 7 | enum[4]: Auto A, Auto B, Auto C, Auto D | — |  |
| 476 | `—` | Step | 2 | 1..256 | — |  |
| 477 | `—` | Amount | 11 | -1000..1000 | — |  |
| 478 | `—` | Automation | 7 | enum[2]: Hide, Show | — |  |
| 479 | `padmute` | Mute | 6 | 0..1 | 1.6 | 01,02 |
| 480 | `—` | Pad | 2 | 1..16 | — |  |
| 481 | `—` | Target | 2 | 1..256 | — |  |
| 482 | `—` | Amount | 11 | -1000..1000 | — |  |
| 484 | `duckattack` | Attack | 20 | 1..20 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 485 | `duckhold` | Hold | 16 | 0..500 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 486 | `duckrelease` | Release | 16 | 0..500 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 487 | `duckdepth` | Depth | 10 | 0..1000 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 488 | `ducktrig` | Trigger | 7 | enum[5]: Track, Pad, Clock, Audio, MIDI | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 489 | `duckclkdiv` | Division | 7 | enum[5]: 1/16, 1/8, 1/4, 1/2, 1/1 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 490 | `ducktrkin` | Source | 7 | enum[8]: Track 1, Track 2, Track 3, Track 4, Track 5, Track 6, … | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 491 | `duckthresh` | Threshold | 10 | 0..1000 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 492 | `duckmidinote` | Note | 7 | enum[128]: None, C#-1 (1), D-1 (2), D#-1 (3), E-1 (4), F-1 (5), … | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 493 | `duckmidich` | Channel | 7 | enum[17]: Omni, 1, 2, 3, 4, 5, … | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 494 | `duckextin` | Source | 7 | enum[4]: In 1, In 2, In 3, USB | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 495 | `duckbypass` | Bypass | 6 | 0..1 | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 496 | `duckpadtrk` | Source Track | 7 | enum[8]: Track 1, Track 2, Track 3, Track 4, Track 5, Track 6, … | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
| 497 | `duckpad` | Source Pad | 7 | enum[16]: Pad 1, Pad 2, Pad 3, Pad 4, Pad 5, Pad 6, … | 1.6 | 0e,0f,10,11,12,13,14,16,17,2f |
