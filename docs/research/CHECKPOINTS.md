# Integration checkpoint coverage

Research recorded 15–16 November 2026 on the exact 1.6.8 baseline.
This index records scope, not a claim that every subsystem or device behavior is complete.
Later entries may close limits that were open in earlier ones. Full raw traces and the large execution harness are not distributed.
See [evidence](EVIDENCE.md) and the linked subject chapters for outcomes and limits.

| Checkpoint | Tested boundary | Public chapter |
|---|---|---|
| 6.1 | Executed XML files, parameters and sequences | [Files](FILES.md) |
| 6.2 | Original project-object construction | [Files](FILES.md) |
| 6.3 | Upload dispatch from loaded objects | [Files](FILES.md) |
| 6.4 | Loaded assets through the file service and the engine | [Files](FILES.md) |
| 6.5 | Loaded streamed sample families | [Files](FILES.md) |
| 6.6 | Executed project-relative filenames | [Files](FILES.md) |
| 6.7 | Four loaded Multisample assets | [Files](FILES.md) |
| 6.8 | Loaded projects beyond prefetch | [Files](FILES.md) |
| 6.9 | XML-owned slice markers through playback | [Files](FILES.md) |
| 6.10 | XML modulation wiring through upload and playback | [Files](FILES.md) |
| 6.11 | XML automation through native lane upload and engine storage | [Files](FILES.md) |
| 6.12 | Full track sequence upload and running lanes | [Files](FILES.md) |
| 6.13 | Native bank finalization and selection overwrite | [Files](FILES.md) |
| 6.14 | Finalized sample sequences produce exact audio | [Sequencing](SEQUENCING.md) |
| 6.15 | Finalized synth sequences produce exact audio | [Sequencing](SEQUENCING.md) |
| 6.16 | XML automation changes loaded sequence audio | [Sequencing](SEQUENCING.md) |
| 6.17 | Mixed tracks share loaded sequence and automation audio | [Sequencing](SEQUENCING.md) |
| 6.18 | Native scenes switch loaded track sequences | [Sequencing](SEQUENCING.md) |
| 6.19 | Scene-boundary voice timing | [Sequencing](SEQUENCING.md) |
| 6.20 | Native scene loop, hold, counts and unequal lengths | [Sequencing](SEQUENCING.md) |
| 6.21 | Stepped automation across native scenes | [Sequencing](SEQUENCING.md) |
| 6.22 | Sliding scenes and transport-grid pattern repeats | [Sequencing](SEQUENCING.md) |
| 6.23 | Manual scene commands and late quantization | [Sequencing](SEQUENCING.md) |
| 6.24 | CM4 live scene queue and engine replay | [Sequencing](SEQUENCING.md) |
| 6.25 | Empty-scene forward search, wrap and stop | [Sequencing](SEQUENCING.md) |
| 6.26 | Queued replacement and separate track/scene timing | [Sequencing](SEQUENCING.md) |
| 6.27 | Native MIDI scene mapper and CM4 playback bridge | [Sequencing](SEQUENCING.md) |
| 6.28 | Serial MIDI bytes through native CM4 and CM7 | [Midi Usb](MIDI_USB.md) |
| 6.29 | CM4 USB MIDI reception, queue limits and scene routing | [Midi Usb](MIDI_USB.md) |
| 6.30 | CM7 USB-device MIDI input and duplicate filter | [Midi Usb](MIDI_USB.md) |
| 6.31 | MIDI-learn capture, export and CM4 receive behaviour | [Midi Usb](MIDI_USB.md) |
| 6.32 | MIDI-binding storage, boundaries and ordinary input | [Midi Usb](MIDI_USB.md) |
| 6.33 | Per-track MIDI channel, port and Multisample routing | [Midi Usb](MIDI_USB.md) |
| 6.34 | MIDI family tables, command notes and inactive targets | [Midi Usb](MIDI_USB.md) |
| 6.35 | MIDI expression, program gating and CM4 ring-X requests | [Midi Usb](MIDI_USB.md) |
| 6.36 | MIDI output serialization and the actual ring-Y consumer | [Midi Usb](MIDI_USB.md) |
| 6.37 | MIDI output pump, UART interrupts and USB-host worker | [Midi Usb](MIDI_USB.md) |
| 6.38 | MIDI settings files and USB-host initialization | [Midi Usb](MIDI_USB.md) |
| 6.39 | USB native enumeration, descriptor parsing and reconnect | [Midi Usb](MIDI_USB.md) |
| 6.40 | USB controller submission, FIFO and interrupt handling | [Midi Usb](MIDI_USB.md) |
| 6.41 | USB initialization, reset and port interrupts | [Midi Usb](MIDI_USB.md) |
| 6.42 | USB native task creation, queues and bounded scheduling | [Midi Usb](MIDI_USB.md) |
| 6.43 | CM4 native scheduler, context switching and USB interrupt wake | [Startup](STARTUP.md) |
| 6.44 | CM4 boot-created application tasks and interrupt scheduling | [Startup](STARTUP.md) |
| 6.45 | CM4 scheduled four-file demand service and queued reopen | [Storage](STORAGE.md) |
| 6.46 | CM7 audio demand with native scheduled CM4 streaming | [Storage](STORAGE.md) |
| 6.47 | Native filesystem reads and SD completion queue | [Storage](STORAGE.md) |
| 6.48 | Native SDMMC commands and delayed read completion | [Storage](STORAGE.md) |
| 6.49 | Native SD initialization and discovered capacity | [Storage](STORAGE.md) |
| 6.50 | Production streaming through native FAT and SD | [Storage](STORAGE.md) |
| 6.51 | Native queued WAV prefetch and completion | [Storage](STORAGE.md) |
| 6.52 | Native first-load state through full audio demand | [Storage](STORAGE.md) |
| 6.53 | Native SD writes and FAT file persistence | [Storage](STORAGE.md) |
| 6.54 | Native recorder through FAT and SD persistence | [Storage](STORAGE.md) |
| 6.55 | Production scheduled recording with native SD waits | [Storage](STORAGE.md) |
| 6.56 | Production recorder write faults and late completion | [Storage](STORAGE.md) |
| 6.57 | Late SD completion disrupts recorder retry in modeled timings | [Storage](STORAGE.md) |
| 6.58 | Continuous recording loses input after prepared chunks fill | [Storage](STORAGE.md) |
| 6.59 | Recording callers do not signal rejected input in tested callbacks | [Storage](STORAGE.md) |
| 6.60 | Native reset memory setup completes CM7 engine initialization | [Startup](STARTUP.md) |
| 6.61 | Native CM7 allocator limits ledger and startup accounting | [Startup](STARTUP.md) |
| 6.62 | Native CM7 outer objects and shared startup | [Startup](STARTUP.md) |
| 6.63 | Native CM7 static constructors and audio startup controls | [Startup](STARTUP.md) |
| 6.64 | Native CM7 reset clock MPU and cache startup | [Startup](STARTUP.md) |
| 6.65 | Native CM7 floating-point startup boundary | [Startup](STARTUP.md) |
| 6.66 | Native CM7 audio DMA handler dispatch | [Startup](STARTUP.md) |
| 6.67 | Native CM7 DMA-to-audio main loop | [Startup](STARTUP.md) |
| 6.68 | Native CM7 main startup and core handoff | [Startup](STARTUP.md) |
| 6.69 | Native CM4 reset through initial task scheduling | [Startup](STARTUP.md) |
| 6.70 | Native CM4 application services with running CM7 audio | [Startup](STARTUP.md) |
| 6.71 | Native startup settings and project discovery | [Startup](STARTUP.md) |
| 6.72 | Native startup and main-interface rendering | [Ui Controller](UI_CONTROLLER.md) |
| 6.73 | Native touch through menu rendering | [Ui Controller](UI_CONTROLLER.md) |
| 6.74 | Native SPI controller input and packet integrity | [Ui Controller](UI_CONTROLLER.md) |
