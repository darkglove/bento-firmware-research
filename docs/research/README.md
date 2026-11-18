# Research edition: November 2026

This edition summarizes research recorded through 17 November 2026. The main analysis baseline is **Bento 1.6.8**. The original one-byte patch tutorial remains specific to **1.6.1**; it has not silently become a 1.6.8 builder.

This is independent research, not vendor source, a complete replacement firmware, or a certification that modified firmware is safe. Firmware and original vendor files must be obtained separately from their rights holder. Nothing in this repository flashes a device.

## Read by subject

1. [Evidence and reproduction limits](EVIDENCE.md): what was observed, what was modeled, and what this public edition includes.
2. [Architecture and hardware](ARCHITECTURE.md): image boundaries, cores, clocks, memory, peripherals and calibration.
3. [Versions and parameter model](VERSIONS.md): 1.6.1 versus 1.6.8, stable keys, moving IDs and factual reference tables.
4. [Audio engines and effects](AUDIO.md): Wavetable, Granular, sample families, modulation, effects and controller reverb.
5. [Projects, patches and settings](FILES.md): XML contracts, event formats, automation and wavetable storage.
6. [Sequencing and scenes](SEQUENCING.md): loaded projects, automation, scene boundaries and queue behavior.
7. [MIDI and USB](MIDI_USB.md): routing, output, host enumeration, queues and known limits.
8. [Storage and recording](STORAGE.md): native FAT/SD integration, scheduling, persistence and modeled loss cases.
9. [UI and front-panel control](UI_CONTROLLER.md): graphics, touch, knobs, packet layout and saved parameter changes.
10. [Startup and emulation](STARTUP.md): native startup coverage, supplied peripherals and independent replay.
11. [Recovery and test boundaries](RECOVERY.md): supported stock recovery, the failed-code lesson, and the offline 1.6.8 batch.
12. [Remaining work](ROADMAP.md): practical acceptance gates for a new UI or complete firmware.

The [74-checkpoint index](CHECKPOINTS.md) preserves the coverage of the later integration research. Its entries describe research checkpoints, not 74 independent hardware tests. The [reference tables](../reference/README.md) contain decoded interface facts, not copied firmware or vendor documents.

## Important corrections to the original public tutorial's research notes

- The main update file contains **three executable regions**: CM7 audio, a separate SD-reader image, and CM4 application code. The companion file runs the front panel **and reverb** on another processor.
- Wavetable, Granular and Room-reverb research progressed from static inspection to native-code emulation and selected differential models. That does not establish complete replacement-firmware coverage.
- Original CM4 startup, filesystem services, display rendering, one touch-menu interaction, and controller-driven parameter persistence have been exercised in supplied peripheral models.
- A Phones control change reached the audio engine and was saved. The final end-to-end change in captured audio amplitude remains **unverified**.
- Recovery through a preserved bootloader and stock reinstall is supported by documentation and reports. A complete, independently demonstrated recovery procedure for arbitrary failures is not established.

The publication date is not a new hardware-test date. See [validation](../VALIDATION.md) for checks actually run for this edition.
