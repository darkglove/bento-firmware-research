# UI, touch and front-panel control

Evidence: static UI/protocol reconstruction and later native startup, graphics, touch and controller fixtures. Device pixels and physical controls were modeled, not independently observed on hardware.

## Display and UI architecture

The panel timing is 600 × 1280 portrait. The application's observed drawing area is **1280 × 480 landscape**, stored as 480 × 1280 AL44 pixels: one byte combines four alpha bits and four palette-index bits. These are different dimensions, not competing measurements of the same buffer.

Four allocated application surfaces each hold 614,400 bytes. Layer 1 uses a narrower panel window; buffer selection and a separate vertical-blank reload request control scanout. Allocation addresses must not be treated as universal constants. A replacement RGB565 buffer for the same application area would need twice as many bytes.

The reconstructed UI family contains 131 virtual tables, with 109 classified under the main UI-item family: 34 page classes and 75 controls. Inheritance is partly inferred from constructors and matching slots. The [screen-state table](../reference/ui-states-1.6.8.md) records routing facts without including firmware strings or screenshots.

CM4 also owns session state, files, streaming services, power-related work and communications. Replacing its screen renderer alone is not a drop-in replacement for the whole CM4 application.

## Native display and touch evidence

Original startup was extended through settings/project discovery and main-screen rendering. Independent replay reconstructed CPU memory stores, drawing-register operations, copy sources, buffer changes and captured frames.

Touch uses an I2C4 device at 7-bit address `0x5d`. The examined register interface includes product/configuration information at `0x8140`, status at `0x814e`, and eight-byte contact records from `0x814f`. Status clearing and read failures matter as well as coordinate conversion.

One supplied press/release sequence reached native menu behavior and changed the rendered interface. The test initially hit an observation-boundary failure when a menu surface extended outside the captured graphics region; enlarging the observation range fixed the fixture without changing firmware code. This is evidence for one interaction, not every gesture, widget or physical calibration.

## Controller packet interfaces

The link transfers 72-byte frames. Relevant little-endian fields include:

| Direction/type | Offset | Meaning |
|---|---:|---|
| Main to controller, type 2 | 8 | Master brightness, 32-bit value |
| Type 2 | 12 | LED mask; LED n uses bit `31-n` |
| Type 2 | 16 / 32 / 48 | Sixteen red / green / blue bytes |
| Type 2 | 64 | Signed 16-bit pad threshold |
| Controller to main, type 3 | 8 | Sixteen button bits |
| Type 3 | 10 | Eight signed 16-bit knob values |
| Type 3 | 26 | Sixteen unsigned 16-bit pad values |
| Type 3 | 58 | Observed constant `0x0101`; meaning unresolved |

The frame header carries type and length. Type 7 is an **inbound reverb-parameter message to the controller**, not a controller state reply.

The controller scans analog signal pairs for the eight endless knobs; they are not digital encoder inputs. It accumulates movement and publishes a wrapped value. Pad processing applies crosstalk compensation, threshold/hysteresis and a square-law pressure transform; onset/velocity interpretation is a later main-side operation. Controller SPI1 drives LEDs, SPI2 reads switches, and SPI3 is the main link. Do not confuse those with the main processor's own SPI numbering.

## Integrity caveat

A 352-case native audit found that the examined main-side receiver copies the packet, calculates a checksum, **overwrites the supplied checksum**, recalculates and compares the computed values. The incoming trailer therefore did not determine acceptance on that path. Type/length predicates and the input parser impose additional conditions.

The algorithm uses polynomial `0xedb88320` with arithmetic shifts, so substituting ordinary logical-shift CRC32 does not reproduce it. The transmit path also sets its sequence halfword after calculating the checksum in the recorded sequence. These observations concern the tested main-side paths; complete far-end acceptance remains a separate question. A replacement must explicitly choose compatibility versus stronger validation.

## A control change that reached persistence

The integrated controller fixture drove original SPI register/FIFO handling and callbacks. A small knob change produced a consumed UI event but no visible adjustment, providing a useful negative control. A larger change crossed the native widget's hysteresis threshold:

- Phones changed from -6.0 to -7.3 dB.
- CM4 published the parameter command; original CM7 processing consumed it.
- The synthetic card received saved settings with `outphonesgain="-7300"` and a native autosave project.
- Graphics, shared-memory traffic, tasks, disk sectors and captured frames were independently replayed.

The extended run included 220 application updates, 5,761 SPI transfers and 38 synthetic card writes. It did **not** prove the expected change in actual output sample amplitude. The attempted follow-on audio-gain fixture failed before capturing audio, and the revised run was interrupted. That final amplitude claim remains open.
