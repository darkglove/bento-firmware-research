# Object model (ROM schema), Bento 1.6.8

ROM table at `0x08199254`: 764 eight-byte records `[u8 type][u8 0][u16 property id][u32 default]`, grouped by object type.
Property ids resolve through the 1.6.8 registry to storage keys. `defaults` are raw integers in registry units.
XML tags/FourCC are verified by executing initializer `0x812fd24` and all 48 name lookups. Table position is not type ID: Multisample = 0x0f; Loop = 0x11 (corrected 2026-11-15).
Runtime type-name initialization was exercised in the recorded research; the raw execution report is not published. Property sets below come from the ROM schema; role descriptions remain separately qualified.

## 0x01 — Sample-instrument cell (one-shot / multisample pad) (`saminst`/`INST`) — 32 properties

Role: Sample-instrument cell (one-shot / multisample pad): trigger, env, loop mode, multisample+interp+legato. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `gaindb` | 0 | 1.2.4 |
| `pitch` | 0 | 1.2.4 |
| `panpos` | 0 | 1.2.4 |
| `cellmode` | 0 | 1.2.4 |
| `samtrigtype` | 0 | 1.2.4 |
| `loopmodes` | 0 | 1.2.4 |
| `reverse` | 0 | 1.2.4 |
| `envattack` | 0 | 1.2.4 |
| `envdecay` | 0 | 1.2.4 |
| `envsus` | 1000 | 1.2.4 |
| `envrel` | 200 | 1.2.4 |
| `velamount` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `polymode` | 0 | 1.2.4 |
| `chokegrp` | 0 | 1.2.4 |
| `dualfilcutoff` | 0 | 1.2.4 |
| `res` | 500 | 1.2.4 |
| `fx1send` | 0 | 1.2.4 |
| `fx2send` | 0 | 1.2.4 |
| `overdrive` | 0 | 1.2.4 |
| `multisammode` | 0 | 1.2.4 |
| `interpqual` | 0 | 1.2.4 |
| `loopfadeamt` | 0 | 1.2.4 |
| `lfowave` | 0 | 1.2.4 |
| `lforate` | 100 | 1.2.4 |
| `lfoamount` | 1000 | 1.2.4 |
| `lfokeytrig` | 0 | 1.2.4 |
| `lfobeatsync` | 0 | 1.2.4 |
| `lforatebeatsync` | 0 | 1.2.4 |
| `legatomode` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `padmute` | 0 | 1.6 |

## 0x02 — Loop cell (`loopinst`/`LINS`) — 32 properties

Role: Loop cell: loop mode, quantise, sync, beat count, clip length, pad mute. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `gaindb` | 0 | 1.2.4 |
| `pitch` | 0 | 1.2.4 |
| `panpos` | 0 | 1.2.4 |
| `cellmode` | 1 | 1.2.4 |
| `samtrigtype` | 2 | 1.2.4 |
| `loopmode` | 1 | 1.2.4 |
| `reverse` | 0 | 1.2.4 |
| `envattack` | 0 | 1.2.4 |
| `envdecay` | 0 | 1.2.4 |
| `envsus` | 1000 | 1.2.4 |
| `envrel` | 200 | 1.2.4 |
| `velamount` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `polymode` | 0 | 1.2.4 |
| `chokegrp` | 0 | 1.2.4 |
| `dualfilcutoff` | 0 | 1.2.4 |
| `res` | 500 | 1.2.4 |
| `fx1send` | 0 | 1.2.4 |
| `fx2send` | 0 | 1.2.4 |
| `overdrive` | 0 | 1.2.4 |
| `lfowave` | 0 | 1.2.4 |
| `lforate` | 100 | 1.2.4 |
| `lfoamount` | 1000 | 1.2.4 |
| `lfokeytrig` | 0 | 1.2.4 |
| `lfobeatsync` | 0 | 1.2.4 |
| `lforatebeatsync` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `padmute` | 0 | 1.6 |
| `quantsize` | 3 | 1.2.4 |
| `synctype` | 5 | 1.2.4 |
| `beatcount` | 0 | 1.2.4 |
| `cliplength` | 0 | 1.2.4 |

## 0x03 — Slicer instrument (`slicer`/`SINT`) — 34 properties

Role: Slicer instrument: active slice, slice sequencing, slice quantise, pad start. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `gaindb` | 0 | 1.2.4 |
| `pitch` | 0 | 1.2.4 |
| `panpos` | 0 | 1.2.4 |
| `cellmode` | 2 | 1.2.4 |
| `samtrigtype` | 0 | 1.2.4 |
| `loopmode` | 0 | 1.2.4 |
| `envattack` | 0 | 1.2.4 |
| `envdecay` | 0 | 1.2.4 |
| `envsus` | 1000 | 1.2.4 |
| `envrel` | 200 | 1.2.4 |
| `velamount` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `polymodeslice` | 0 | 1.2.4 |
| `chokegrp` | 0 | 1.2.4 |
| `dualfilcutoff` | 0 | 1.2.4 |
| `res` | 500 | 1.2.4 |
| `fx1send` | 0 | 1.2.4 |
| `fx2send` | 0 | 1.2.4 |
| `overdrive` | 0 | 1.2.4 |
| `lfowave` | 0 | 1.2.4 |
| `lforate` | 100 | 1.2.4 |
| `lfoamount` | 1000 | 1.2.4 |
| `lfokeytrig` | 0 | 1.2.4 |
| `lfobeatsync` | 0 | 1.2.4 |
| `lforatebeatsync` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `actslice` | 1 | 1.2.4 |
| `slicestepmode` | 0 | 1.2.4 |
| `slicerquantsize` | 13 | 1.2.4 |
| `beatcount` | 0 | 1.2.4 |
| `playthru` | 0 | 1.2.4 |
| `synctype` | 6 | 1.2.4 |
| `slicepadstart` | 1 | 1.2.4 |
| `slicersync` | 0 | 1.2.4 |

## 0x04 — Shredder instrument (`granslicer`/`GSIN`) — 43 properties

Role: Shredder instrument: slicer params + grain params (grans*). Confidence: high.

| key | default | first seen |
|---|---:|---|
| `gaindb` | 0 | 1.2.4 |
| `pitch` | 0 | 1.2.4 |
| `panpos` | 0 | 1.2.4 |
| `cellmode` | 2 | 1.2.4 |
| `samtrigtype` | 0 | 1.2.4 |
| `loopmode` | 0 | 1.2.4 |
| `envattack` | 0 | 1.2.4 |
| `envdecay` | 0 | 1.2.4 |
| `envsus` | 1000 | 1.2.4 |
| `envrel` | 200 | 1.2.4 |
| `velamount` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `polymodeslice` | 0 | 1.2.4 |
| `chokegrp` | 0 | 1.2.4 |
| `dualfilcutoff` | 0 | 1.2.4 |
| `res` | 500 | 1.2.4 |
| `fx1send` | 0 | 1.2.4 |
| `fx2send` | 0 | 1.2.4 |
| `overdrive` | 0 | 1.2.4 |
| `lfowave` | 0 | 1.2.4 |
| `lforate` | 100 | 1.2.4 |
| `lfoamount` | 1000 | 1.2.4 |
| `lfokeytrig` | 0 | 1.2.4 |
| `lfobeatsync` | 0 | 1.2.4 |
| `lforatebeatsync` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `actslice` | 1 | 1.2.4 |
| `slicestepmode` | 0 | 1.2.4 |
| `slicerquantsize` | 13 | 1.2.4 |
| `beatcount` | 0 | 1.2.4 |
| `playthru` | 1 | 1.2.4 |
| `synctype` | 6 | 1.2.4 |
| `slicepadstart` | 1 | 1.2.4 |
| `slicersync` | 0 | 1.2.4 |
| `gransplaymode` | 1 | 1.5.3 |
| `gransgrainsize` | 500 | 1.5.3 |
| `gransgraindensity` | 500 | 1.5.3 |
| `gransgrainjitter` | 0 | 1.5.3 |
| `gransgrainwindow` | 0 | 1.5.3 |
| `gransgraindetune` | 0 | 1.5.3 |
| `gransgrainbeatsync` | 0 | 1.5.3 |
| `granssyncrate` | 0 | 1.5.3 |
| `gransspeed` | 1000 | 1.5.3 |

## 0x05 — Sample asset / zone (`samasst`/`ASST`) — 13 properties

Role: Sample asset / zone: file, root note, key + velocity range, start/length/loop. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `filename` | 0 | 1.2.4 |
| `rootnote` | 0 | 1.2.4 |
| `id121:None` | 0 | — |
| `keyrangebottom` | 0 | 1.2.4 |
| `keyrangetop` | 0 | 1.2.4 |
| `velroot` | 0 | 1.2.4 |
| `velrangebottom` | 0 | 1.2.4 |
| `velrangetop` | 0 | 1.2.4 |
| `samstart` | 0 | 1.2.4 |
| `samlen` | 0 | 1.2.4 |
| `id38:StreamLength` | 0 | — |
| `loopstart` | 0 | 1.2.4 |
| `loopend` | 0 | 1.2.4 |

## 0x06 — Wavetable oscillator slot (WT1/WT2) (`wavetable`/`WT`) — 7 properties

Role: Wavetable oscillator slot (WT1/WT2): wavetable select, position, pitch, level. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `pitch` | 0 | 1.2.4 |
| `level` | 1000 | 1.2.4 |
| `wavesel` | 0 | 1.2.4 |
| `wavepos` | 0 | 1.2.4 |
| `samlen` | 0 | 1.2.4 |
| `id38:StreamLength` | 0 | — |
| `filename` | 0 | 1.2.4 |

## 0x07 — Granular grain slot (GR1/GR2) (`grainosc`/`GR`) — 26 properties

Role: Granular grain slot (GR1/GR2): grain size/density/shape/freeze/live input. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `pitch` | 0 | 1.2.4 |
| `level` | 1000 | 1.2.4 |
| `grainbeatsync` | 0 | 1.2.4 |
| `grainbeatrate` | 10 | 1.2.4 |
| `graindensity` | 600 | 1.2.4 |
| `grainsizeperc` | 300 | 1.2.4 |
| `grainshape` | 0 | 1.2.4 |
| `gainssrcwin` | 0 | 1.2.4 |
| `grainjitter` | 0 | 1.2.4 |
| `grainpanrnd` | 0 | 1.2.4 |
| `grainfreezemode` | 0 | 1.2.4 |
| `grainfreezepos` | 0 | 1.2.4 |
| `samstart` | 0 | 1.2.4 |
| `samstartpercent` | 0 | 1.2.4 |
| `grainreadspeed` | 1000 | 1.2.4 |
| `grainliveinpos` | 0 | 1.2.4 |
| `grainliveinputfreeze` | 0 | 1.4.1 |
| `grainsaveattack` | 0 | 1.2.4 |
| `grainpitchpatt` | 0 | 1.2.4 |
| `graindetune` | 0 | 1.2.4 |
| `grainliveinput` | 0 | 1.2.4 |
| `loopmodes` | 0 | 1.2.4 |
| `samlen` | 0 | 1.2.4 |
| `id38:StreamLength` | 0 | — |
| `wavesel` | 0 | 1.2.4 |
| `filename` | 0 | 1.2.4 |

## 0x08 — Basic oscillator (`osc`/`OSC`) — 4 properties

Role: Basic oscillator: waveform + pulse width (the 'Osc' of wavetable/granular). Confidence: high.

| key | default | first seen |
|---|---:|---|
| `pitch` | 0 | 1.2.4 |
| `level` | 1000 | 1.2.4 |
| `waveform` | 1 | 1.2.4 |
| `dutycyc` | 500 | 1.2.4 |

## 0x09 — Envelope (`env`/`Env`) — 5 properties

Role: Envelope: A/D/S/R + velocity amount. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `envattack` | 50 | 1.2.4 |
| `envdecay` | 100 | 1.2.4 |
| `envsus` | 900 | 1.2.4 |
| `envrel` | 100 | 1.2.4 |
| `velamount` | 0 | 1.2.4 |

## 0x0a — Filter (`filter`/`FILT`) — 5 properties

Role: Filter: type, cutoff, resonance, enable, serial/parallel. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `filtertype` | 0 | 1.2.4 |
| `cutoff` | 600 | 1.2.4 |
| `res` | 400 | 1.2.4 |
| `filtenable` | 0 | 1.2.4 |
| `filtparallel` | 0 | 1.2.4 |

## 0x0b — LFO (`lfo`/`LFO`) — 6 properties

Role: LFO: shape, rate, depth, restart, beat sync. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `lfowave` | 2 | 1.2.4 |
| `lforate` | 500 | 1.2.4 |
| `lfoamount` | 1000 | 1.2.4 |
| `lfokeytrig` | 0 | 1.2.4 |
| `lfobeatsync` | 0 | 1.2.4 |
| `lforatebeatsync` | 6 | 1.2.4 |

## 0x0c — Modulation sequencer (`seqmod`/`SEQ`) — 6 properties

Role: Modulation sequencer: step length, steps, key trig, quantise, slide. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `steplen` | 4 | 1.2.4 |
| `seqsteps` | 16 | 1.2.4 |
| `seqkeytrig` | 0 | 1.2.4 |
| `seqquant` | 0 | 1.2.4 |
| `seqslide` | 0 | 1.6 |
| `quantsize` | 0 | 1.2.4 |

## 0x0d — Voice/part parameters (`partparms`/`Preset`) — 11 properties

Role: Voice/part parameters: poly+unison, osc phase reset, macro X/Y, MIDI bend range. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `globtempo` | 120 | 1.2.4 |
| `midibend` | 2 | 1.2.4 |
| `wtblusepolymode` | 0 | 1.2.16 |
| `wtblpolymode` | 10 | 1.2.16 |
| `unisonmode` | 0 | 1.2.4 |
| `unisonvcount` | 4 | 1.2.4 |
| `oscphasereset` | 1 | 1.2.4 |
| `unisondetune` | 0 | 1.2.4 |
| `unisonspread` | 0 | 1.2.4 |
| `macroxsnap` | 0 | 1.2.4 |
| `macroysnap` | 0 | 1.2.4 |

## 0x0e — One-shot track (padrec + uiSequencerType = step/piano-roll) (`samtrack`/`TRKS`) — 46 properties

Role: One-shot track (padrec + uiSequencerType = step/piano-roll). Confidence: high.

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `padrec` | 0 | 1.6 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `uiSequencerType` | 1 | 1.5.3 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x0f — Multisample track (`multisamtrack`/`TRMS`) — 35 properties

Role: Multisample track. Confidence: high (runtime XML registry).

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |

## 0x10 — Slicer track (`slicertrack`/`TRSL`) — 44 properties

Role: Slicer track. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x11 — Loop track (`looptrack`/`TRLP`) — 45 properties

Role: Loop track. Confidence: high (runtime XML registry).

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 0 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `padrec` | 0 | 1.6 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x12 — Wavetable track (`wttrack`/`TRKW`) — 44 properties

Role: Wavetable track. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `outputbus` | 0 | 1.2.4 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x13 — Granular track (granpolymode, grancpuamount, live input) (`grtrack`/`TRKG`) — 48 properties

Role: Granular track (granpolymode, grancpuamount, live input). Confidence: high.

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `granpolymode` | 1 | 1.2.4 |
| `grancpuamount` | 800 | 1.2.4 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `graninput` | 0 | 1.3.30 |
| `graninputgain` | 0 | 1.3.30 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x14 — Shredder track (`grainchoptrack`/`TRGC`) — 44 properties

Role: Shredder track. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `cc2ininchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `recactive` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |

## 0x15 — Project / master object (`mastrack`/`TRKM`) — 19 properties

Role: Project / master object: tempo, swing, key, metronome, song mode, DJ-FX selectors, main gain. Confidence: high (runtime XML registry).

| key | default | first seen |
|---|---:|---|
| `globtempo` | 120 | 1.2.4 |
| `swing` | 50 | 1.2.4 |
| `keymode` | 3 | 1.2.4 |
| `keyroot` | 3 | 1.2.4 |
| `metroopts` | 1 | 1.2.4 |
| `metoutbus` | 0 | 1.2.4 |
| `reccountdown` | 1 | 1.2.4 |
| `maingain` | 0 | 1.2.4 |
| `selscenepos` | 0 | 1.2.4 |
| `projmidiinport` | 0 | 1.5.9 |
| `projmidiinchan` | 0 | 1.5.9 |
| `songmode` | 0 | 1.2.4 |
| `quantsizesong` | 1 | 1.2.4 |
| `songSceneHold` | 0 | 1.2.4 |
| `songloop` | 0 | 1.2.4 |
| `fxliveatype` | 0 | 1.5.3 |
| `fxlivebtype` | 0 | 1.5.3 |
| `fxholda` | 0 | 1.5.3 |
| `fxholdb` | 0 | 1.5.3 |

## 0x16 — External track (`extrack`/`TRKE`) — 33 properties

Role: External track: trkinput + MIDI out, no recording params. Confidence: high (runtime XML registry).

| key | default | first seen |
|---|---:|---|
| `selcellpos` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `trkinput` | 0 | 1.2.4 |
| `in1gain` | 0 | 1.2.4 |
| `trkgain` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `outputbus` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `midiinport` | 0 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |

## 0x17 — Union/superset track (granular + record + input params), keys listed alphabetically (`cliptrack`/`TRCP`) — 47 properties

Role: Union/superset track (granular + record + input params), keys listed alphabetically. Confidence: low.

| key | default | first seen |
|---|---:|---|
| `celldisppos` | 0 | 1.2.4 |
| `cellname` | 0 | 1.2.4 |
| `cc1inchan` | 0 | 1.2.4 |
| `cc1inport` | 0 | 1.2.4 |
| `cc2inport` | 0 | 1.2.4 |
| `grancpuamount` | 800 | 1.2.4 |
| `granpolymode` | 1 | 1.2.4 |
| `midiinchan` | 0 | 1.2.4 |
| `padrec` | 0 | 1.6 |
| `midiinport` | 0 | 1.2.4 |
| `midioutchan` | 0 | 1.2.4 |
| `midioutport` | 0 | 1.2.4 |
| `outputbus` | 0 | 1.2.4 |
| `padrowoffset` | 0 | 1.2.4 |
| `recactive` | 0 | 1.2.4 |
| `recautoplay` | 0 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `recpresetlen` | 0 | 1.2.4 |
| `recquant` | 3 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `selcellpos` | 0 | 1.2.4 |
| `selseqpos` | 0 | 1.2.4 |
| `seqplayenable` | 1 | 1.2.4 |
| `trkfx1send` | 0 | 1.2.4 |
| `trkfx2send` | 0 | 1.2.4 |
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
| `trkgain` | 0 | 1.2.4 |
| `trkinput` | 0 | 1.2.4 |
| `trkmute` | 0 | 1.2.4 |
| `trkpan` | 0 | 1.2.4 |
| `trksolo` | 0 | 1.2.4 |

## 0x18 — Note sequence (`noteseq`/`NTSQ`) — 9 properties

Role: Note sequence: step length/count, snap, quantise, knob mode, pad frame offset. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `cellname` | 0 | 1.2.4 |
| `notesteplen` | 10 | 1.2.4 |
| `notestepcount` | 16 | 1.2.4 |
| `seqstepmode` | 1 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `quantsizeseq` | 1 | 1.2.4 |
| `bp_uiSeqKnobMode` | 1 | 1.5.20 |
| `uiPadFrameOffset` | 0 | 1.5.3 |
| `seqslide` | 0 | 1.6 |

## 0x19 — Cabinet distortion + comb filter FX (`fxcabdist`/`FXCB`) — 10 properties

Role: Cabinet distortion + comb filter FX. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `wet` | 0 | 1.2.4 |
| `cabprefreq` | 10 | 1.2.4 |
| `cabdistamt` | 0 | 1.2.4 |
| `cabdisttype` | 0 | 1.2.4 |
| `cabpostfreq` | 800 | 1.2.4 |
| `combamt` | 500 | 1.2.4 |
| `combtime` | 10 | 1.2.4 |
| `combfb` | 0 | 1.2.4 |
| `comblfoamt` | 0 | 1.2.4 |
| `comblfort` | 200 | 1.2.4 |

## 0x1a — Classic reverb (`fxblkreverb`/`FXRB`) — 3 properties

Role: Classic reverb: decay, pre-delay, damping. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `decay` | 600 | 1.2.4 |
| `predelay` | 40 | 1.2.4 |
| `damping` | 500 | 1.2.4 |

## 0x1b — Reverb v2 (`fxbluereverb`/`FXRL`) — 10 properties

Role: Reverb v2: styles, low/high cut, freeze, Room/Shimmer algo, shimmer shift+feedback. Confidence: high (content).

| key | default | first seen |
|---|---:|---|
| `r2style` | 7 | 1.2.4 |
| `r2metatime` | 454 | 1.2.4 |
| `r2metalevel` | 811 | 1.2.4 |
| `r2highcut` | 1000 | 1.2.4 |
| `r2lowcut` | 0 | 1.2.4 |
| `r2predelay` | 300 | 1.2.4 |
| `r2freeze` | 0 | 1.2.4 |
| `rvbalgo` | 0 | 1.6 |
| `shimshift` | 5 | 1.2.4 |
| `shimfeedbk` | 400 | 1.2.4 |

## 0x1c — Delay (`fxdelay`/`FXDL`) — 8 properties

Role: Delay: time/musical time, feedback, ping-pong, filter. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `feedback` | 400 | 1.2.4 |
| `filtenable` | 0 | 1.2.4 |
| `cutoffFx` | 1000 | 1.2.4 |
| `filtquality` | 1000 | 1.2.4 |
| `delaypingpong` | 1 | 1.2.4 |
| `dealybeatsync` | 1 | 1.2.4 |
| `delay` | 400 | 1.2.4 |
| `delaymustime` | 7 | 1.2.4 |

## 0x1d — Mod FX bank (`fxlemon`/`FXLM`) — 12 properties

Role: Mod FX bank: flanger, dist, phaser, chorus + sends + type. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `flangeamount` | 0 | 1.2.4 |
| `flangelforate` | 500 | 1.2.4 |
| `flangefeedback` | 600 | 1.2.4 |
| `distamount` | 0 | 1.2.4 |
| `phaseamount` | 0 | 1.2.4 |
| `phaselforate` | 500 | 1.2.4 |
| `phasefeedback` | 500 | 1.2.4 |
| `chorusamount` | 0 | 1.2.4 |
| `chorusrate` | 500 | 1.2.4 |
| `fx1send` | 0 | 1.2.4 |
| `fx2send` | 0 | 1.2.4 |
| `fx3type` | 0 | 1.2.4 |

## 0x1e — Mod FX sub-type (amount, rate, feedback) (`phaser`/`FXPH`) — 3 properties

Role: Mod FX sub-type (amount, rate, feedback). Confidence: low.

| key | default | first seen |
|---|---:|---|
| `amount` | 200 | 1.2.4 |
| `lforate` | 500 | 1.2.4 |
| `feedback` | 500 | 1.2.4 |

## 0x1f — Mod FX sub-type flanger+dist (`flangerdist`/`FXFD`) — 4 properties

Role: Mod FX sub-type flanger+dist. Confidence: low.

| key | default | first seen |
|---|---:|---|
| `flangeamount` | 0 | 1.2.4 |
| `lforate` | 500 | 1.2.4 |
| `feedback` | 600 | 1.2.4 |
| `distamount` | 0 | 1.2.4 |

## 0x20 — Mod FX sub-type chorus (amount, rate) (`chorus`/`FXCH`) — 2 properties

Role: Mod FX sub-type chorus (amount, rate). Confidence: low.

| key | default | first seen |
|---|---:|---|
| `amount` | 200 | 1.2.4 |
| `chorrate` | 500 | 1.2.4 |

## 0x21 — Delay variant (amount+feedback+filter+time) (`delay`/`FXLD`) — 9 properties

Role: Delay variant (amount+feedback+filter+time). Confidence: low.

| key | default | first seen |
|---|---:|---|
| `amount` | 500 | 1.2.4 |
| `feedback` | 400 | 1.2.4 |
| `filtenable` | 0 | 1.2.4 |
| `cutoffFx` | 500 | 1.2.4 |
| `filtquality` | 1000 | 1.2.4 |
| `delaypingpong` | 0 | 1.2.4 |
| `dealybeatsync` | 1 | 1.2.4 |
| `delay` | 400 | 1.2.4 |
| `delaymustime` | 6 | 1.2.4 |

## 0x22 — Reverb variant (amount+decay+pre-delay+damping) (`reverb`/`FXLR`) — 4 properties

Role: Reverb variant (amount+decay+pre-delay+damping). Confidence: low.

| key | default | first seen |
|---|---:|---|
| `amount` | 500 | 1.2.4 |
| `decay` | 600 | 1.2.4 |
| `predelay` | 40 | 1.2.4 |
| `damping` | 500 | 1.2.4 |

## 0x23 — Master compressor (`compressor`/`FXCM`) — 8 properties

Role: Master compressor: attack, release, threshold, ratio, gain, auto makeup, peak limit. Confidence: high (content).

| key | default | first seen |
|---|---:|---|
| `globcomp` | 1 | 1.2.4 |
| `cattack` | 100 | 1.2.4 |
| `crelease` | 2500 | 1.2.4 |
| `cthreshdb` | 4294957296 | 1.2.4 |
| `cratio` | 4 | 1.2.4 |
| `cgaindb` | 0 | 1.2.4 |
| `cautomakeup` | 1 | 1.2.4 |
| `peaklimit` | 1 | 1.2.4 |

## 0x2b — Scene (`scene`/`SCEN`) — 3 properties

Role: Scene: name, display pos, play count. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `cellname` | 0 | 1.2.4 |
| `celldisppos` | 0 | 1.2.4 |
| `sceneplaycount` | 1 | 1.2.4 |

## 0x2c — Scene entry (`sceneEntry`/`SEEN`) — 2 properties

Role: Scene entry: track index + sequence index. Confidence: medium.

| key | default | first seen |
|---|---:|---|
| `scenetrackindex` | 0 | 1.2.4 |
| `sceneseqindex` | 0 | 1.2.4 |

## 0x2d — Global settings (`global`/`GLOB`) — 30 properties

Role: Global settings: in/out gains, brightness, battery, SD mode, multisample-recorder settings. Confidence: high.

| key | default | first seen |
|---|---:|---|
| `id305:None` | 0 | — |
| `out1gain` | 4294961296 | 1.2.4 |
| `out2gain` | 4294961296 | 1.2.4 |
| `out3gain` | 4294961296 | 1.2.4 |
| `outphonesgain` | 4294961296 | 1.2.4 |
| `previewvolume` | 4294957296 | 1.5.3 |
| `screenbrightness` | 1000 | 1.2.4 |
| `padbrightness` | 5 | 1.6 |
| `padthresh` | 500 | 1.2.4 |
| `autosleep` | 1 | 1.2.4 |
| `battchargelimit` | 1 | 1.5.32 |
| `midibend` | 2 | 1.2.4 |
| `midiouttype` | 1 | 1.2.4 |
| `mrstartnote` | 36 | 1.2.4 |
| `mrendnote` | 84 | 1.2.4 |
| `mrstride` | 1 | 1.2.4 |
| `mrvellayers` | 1 | 1.2.4 |
| `mrmaxvel` | 100 | 1.2.4 |
| `mrnotelen` | 5 | 1.2.4 |
| `mrrellen` | 2 | 1.2.4 |
| `mrecmidich` | 1 | 1.2.4 |
| `recinput` | 0 | 1.2.4 |
| `recgain` | 0 | 1.2.4 |
| `recusethres` | 0 | 1.2.4 |
| `recthresh` | 4294937296 | 1.2.4 |
| `recmonmode` | 1 | 1.2.4 |
| `sdsafemode` | 0 | 1.2.4 |
| `metgain` | 4294957296 | 1.2.4 |
| `uiSelectedPad` | 0 | 1.5.3 |
| `lastknowndate` | 0 | 1.6.8 |

## 0x2e — Loop group (`loopgroup`/`LPGP`) — 4 properties

Role: Loop group: mask, index, custom name. Confidence: high (content).

| key | default | first seen |
|---|---:|---|
| `cellname` | 0 | 1.2.4 |
| `lgindex` | 0 | 1.5.3 |
| `lgmask` | 0 | 1.5.3 |
| `lgcustom` | 0 | 1.5.30 |

## 0x2f — Main-output ducker (`ducker`/`FXDK`) — 14 properties

Role: Main-output ducker: duck* params (same set as every track). Confidence: high (content).

| key | default | first seen |
|---|---:|---|
| `duckattack` | 1 | 1.6 |
| `duckhold` | 10 | 1.6 |
| `duckrelease` | 100 | 1.6 |
| `duckdepth` | 500 | 1.6 |
| `ducktrig` | 1 | 1.6 |
| `duckclkdiv` | 1 | 1.6 |
| `ducktrkin` | 0 | 1.6 |
| `duckthresh` | 500 | 1.6 |
| `duckmidinote` | 36 | 1.6 |
| `duckmidich` | 1 | 1.6 |
| `duckextin` | 0 | 1.6 |
| `duckbypass` | 1 | 1.6 |
| `duckpadtrk` | 0 | 1.6 |
| `duckpad` | 8 | 1.6 |
