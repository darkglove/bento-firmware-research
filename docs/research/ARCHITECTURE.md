# Architecture and hardware

Evidence: image layout and instruction/data inspection, with later native startup execution in modeled peripherals. Exact hardware part identification and electrical measurements remain separate questions.

## Update image layout

| Region | Address interval | Role |
|---|---|---|
| Preserved area before the update | `0x08000000–0x0803ffff` | Bootloader region; absent from the supplied main update file |
| Main CM7 image | `0x08040000–0x080dffff` | Audio engine, routing and shared-state setup |
| SD-reader image | `0x080e0000–0x080fffff` | Separate USB mass-storage mode |
| Main CM4 image | `0x08100000` to the main file's end | UI, project/session management and file services |
| Calibration sector | Starts at `0x081e0000` | Factory calibration data read at startup |
| Companion image | Mapped at `0x90000000` | Front-panel processing and reverb on a separate controller |

These are file/memory boundaries, not permission to write them. Disk mode is executable firmware, not a convenient empty patch area. The installation bootloader itself is not available in the update images, so its complete erase and integrity policy cannot be established by analyzing those files alone.

The 1.6.8 main file is 1,535,540 bytes and ends at exclusive address `0x081b6e34`. The 1.6.1 main file is 1,523,516 bytes and ends at `0x081b3f3c`. Component identity must be checked by hash, not just a version string.

## Processor responsibilities

The observed register and core arrangement is consistent with an STM32H747/H757-class dual-core main processor. The precise package/part marking is not proved by the image alone. CM4 has its own reset path and waits for CM7's startup handoff through hardware semaphore 0. Shared-memory queues connect application requests, audio processing, file services and control events.

The controller has separate clocks and firmware. Its tasks include analog pad/knob acquisition, button scanning, LEDs, the SPI control link, and the serial-audio reverb path. It is not simply a passive input scanner.

## Clocks and memory

The decoded main startup uses a 6.144 MHz external-clock value and configures a 479.232 MHz system clock. The serial-audio kernel is 12.288 MHz, giving 48 kHz under the STM32H7 SAI divider configuration. The native initializer also requests 48,000 Hz. Audio processing uses 128-frame half-buffer blocks; 256-frame circular buffers support the DMA transfers.

The SDRAM controller is configured for 128 MiB. Physical capacity, memory protection coverage and allocator budgets are different facts and must not be conflated. Native allocator and shared-region accounting were subsequently exercised; exhausting or reserving memory changes those budgets.

**CM4 execution protection matters:** the stock memory-protection setup permits executable flash in `0x08100000–0x081fffff`, without a permissive default map. A CM4 call to code placed in flash bank 1 can fail even when a desktop emulator mapped that memory executable. Mapping all memory with unrestricted permissions is not an adequate patch test.

Four 8 KiB native audio buffers were traced in the later 1.6.8 startup: two in AXI SRAM and two in D2 SRAM. Earlier notes that placed all four in one AXI area should not be applied to the newer startup result.

## Peripherals and preservation boundaries

- Main display: LTDC plus MIPI-DSI. Display setup belongs initially to CM7; CM4 manages application drawing and framebuffer use.
- Touch: I2C4, address `0x5d`, with a Goodix-style register interface. Family identification remains an inference from the interface.
- Storage: SDMMC1 and native filesystem services on CM4; card-detect behavior is distinct from a successful data transfer.
- USB device and host responsibilities differ. USB audio/MIDI and SD-reader mode are not a general remote front-panel interface.
- Power and charging are firmware-controlled. A display-only experiment must not incidentally change charger, rails, codec or watchdog behavior.

The examined application paths read a 224-byte calibration record at `0x081e0000`; fourteen floats are range-checked, with defaults used on failure. The exact meaning of each trim is unresolved. No application erase/program sequence was found in the inspected paths. This is not proof of what the external installer erases. Preserve the calibration sector, bootloader, option bytes and controller image in any narrowly scoped application experiment.

Continue with [UI/controller details](UI_CONTROLLER.md), [startup boundaries](STARTUP.md), and [recovery](RECOVERY.md).
