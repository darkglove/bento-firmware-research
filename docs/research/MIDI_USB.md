# MIDI, USB and routing boundaries

Scope: 1.6.8 original-code execution plus explicit peripheral models. Physical link timing, every device descriptor and all user-facing configurations are not certified.

## Input and track routing

The research followed serial MIDI bytes, CM4 USB-host receive queues, CM7 USB-device input, and project scene requests as separate paths. Track channel and port configuration was exercised across eight tracks. Matching tracks can fan out one input; duplicate destinations are not necessarily deduplicated across tracks.

The Multisample study covered all note numbers and controller routing, nonlinear controller conversion and scene-map precedence. Other instrument families were then tested independently. A matching but inactive track can suppress project-level routing. Do not replace those rules with a single global MIDI filter.

Pitch bend, channel pressure, program requests and controller families use different message representations. Global program gating and consumer behavior were checked separately. Some captured request types fell through the tested shared-ring consumers' default branches. This is a bounded negative result, not proof that a feature is broken on every real device.

## Learn and generic binding storage

Native learn capture/export and binding installation/removal were tested. The recorded cases included a number-127 overlap with learn-state storage. Ordinary input on the tested route did not read those generic binding tables, and the examined CM4 consumer did not turn the exported learn record into a demonstrated assignment workflow.

Consequently, storage and capture are not evidence of working end-to-end MIDI learn. A complete test must identify the UI producer, storage ownership, active input consumer, precedence and observable target change.

## Output

CM7 generation, USB-device completion, CM4 ring-Y serialization, output queues, native UART register writes and interrupt chaining were exercised. The UI file-service queue is a different queue and must not be mistaken for the serializer.

The tested USB-host output converter accepted notes and transport bytes F8/FA/FC while dropping CC/pitch messages on that path. This is path-specific; do not generalize it to every USB direction. MIDI Type settings parsing and application of mode-dependent GPIO setup were also tested.

## USB-host lifecycle

Later fixtures progressed from native endpoint/pipe initialization through descriptor parsing, enumeration, controller submission, FIFO data, interrupts, reset/port events and the actual worker queue. A modeled reconnect selected a stale MIDI interface from the preceding device. Malformed descriptor and endpoint-slot cases were recorded rather than silently normalized.

The native host worker's queue holds sixteen two-byte messages. The tested task-context zero-timeout send still waited one tick. Allocation failures did not always propagate as initialization failure, and a missing queue produced an immediate retry loop in a bounded test. These are useful failure cases for a replacement's resource/error design; they are not measured device failure rates.

Controller register storage, self-clearing bits, connection events and completion timing were supplied by the emulator. Native initialization could return success despite some modeled reset/flush/mode timeout conditions. Therefore “initializer returned zero” is insufficient acceptance evidence.

## USB audio and remote testing

Descriptor/code analysis identifies six-channel, 24-bit, 48 kHz USB capture for outputs 1–3, and a stereo USB playback input. The phones pair is not that capture stream. Capturing USB audio is therefore not a direct measurement of every output gain.

SD Reader Mode runs the separate mass-storage image; it is not concurrent normal audio-engine operation. The documented USB MIDI/audio interfaces are not a general protocol for pressing front-panel buttons or injecting touch. Those controls arrive over the controller SPI link and touch I2C interface.

See [startup](STARTUP.md) for scheduling integration and [UI/controller](UI_CONTROLLER.md) for the actual front-panel path.
