# Native startup and the emulator boundary

The later work moved from direct function calls toward original startup and task execution. “Native” here means **original firmware instructions executed inside an emulator**, not execution on a physical Bento.

## Covered startup layers

CM7 work progressed through reset data/BSS initialization, heap state, allocation/ledger behavior, native outer-object placement, static constructors, clocks, memory protection, caches, floating-point startup, audio DMA dispatch and the main audio loop. Later startup joined peripheral initialization and the CM4 handoff.

CM4 work covered reset, original scheduler setup, task creation, SVC/PendSV handler execution, context restoration, supplied interrupt wakeups and application service loops. The examined task priorities were streaming 5, USB 4 and the default application task 3. Resource failures and starvation-like retry behavior were tested with explicit execution bounds.

The system was then extended through native settings/project discovery, framebuffer rendering, touch-menu handling and controller-driven parameter persistence. [CHECKPOINTS.md](CHECKPOINTS.md) shows the staged coverage; an earlier checkpoint's “next” boundary can be closed by a later one.

## What remains supplied

Register storage and hardware transitions must be modeled: clocks becoming ready, SD responses, USB status/FIFOs, graphics transfer effects, touch packets, controller replies and interrupt arrival. Two CPU instances exchange state sequentially in these fixtures. They are not cycle-accurate simultaneous processors.

Some interrupt adapters use saved CPU context and a return sentinel instead of complete architectural exception entry, prioritization and nesting. Other focused scheduling tests execute original SVC/PendSV code with supplied architectural frames. Keep those two claims distinct.

Floating-point configuration required a documented startup adapter to address differences between emulator behavior and the firmware's expected defaults. Graphics observation ranges also needed correction. Neither change should be described as a firmware repair.

## Why independent replay matters

The stronger checks reconstruct outcomes from recorded operations rather than trusting a success flag:

- CPU/DMA stores reconstruct graphics memory and each displayed frame.
- Shared-memory writes reconstruct commands and consumption order.
- Task/interrupt records check restored registers and selected contexts.
- Sector transfers reconstruct disk state; separate FAT decoding verifies files.
- Audio samples are compared to a separate reference where that claim is made.

An output image alone does not show which code produced it. Likewise, a saved report that says PASS is weaker than a checker that can reproduce its invariants and reject an altered input.

## Safety consequences

Early fixtures allowed execution in memory that the real CM4 protection setup would reject. The later 1.6.8 test-batch fixture explicitly removed CM4 execute permission from bank 1 and included a deliberately invalid jump control. That improves the test boundary but still does not model the installation bootloader, flash erase policy, physical timing or every MPU/cache interaction.

No full device emulator, bootloader implementation or hardware-safety certificate is supplied by this public edition. It publishes the findings and portable inspection tools, while keeping vendor inputs and large execution artifacts local.
