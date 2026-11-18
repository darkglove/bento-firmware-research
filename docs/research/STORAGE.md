# Storage, streaming and recording

Scope: bounded 1.6.8 native-code execution against synthetic disks and modeled SD hardware. No real card was written by these fixtures.

## From file calls to native storage

The early fixtures supplied RAM files. Later work replaced those boundaries in stages: native filesystem calls, disk completion queues, SDMMC commands, interrupt delivery, initialization/capacity parsing, and production streaming-task scheduling.

FAT16 and FAT32 mount/open/read/seek/close were exercised, including fragmented files. Native SD reads, status/stop commands and delayed completion were then joined to a task that blocked and resumed through interrupts and scheduling. Register values, DMA transfers and card responses still came from the model.

The normal playback integration eventually used one persistent native CM4 storage/task instance for initial WAV load, prefetch and subsequent demand from CM7. The recorded four-file case made 1,199 transfers and produced 86,016 stereo frames matching the independent reference. Earlier stages supplied initial metadata or prefetched chunks; those earlier limits should not be confused with the later first-load result.

## Writes and persistence

Native single/multiple-block writes and FAT operations were tested with independent decoding after remount. Recording was then joined to the filesystem and to production task waits. Twelve scheduled recorder cases included 2,203 storage waits and 6,032 native switches, with floating-point context and stop/reopen behavior checked.

Fixed timestamps and supplied card/peripheral behavior remain assumptions. A correct remounted file proves the tested sector/file transformation, not physical write durability or immunity to power loss.

## Recorded failure behavior

The following are **modeled failure cases**, not blanket claims about deployed units:

- Some recorder cases retain a short final PCM-tail loss, even when the file is otherwise valid.
- SD errors can leave a task waiting until a 5,000-tick timeout.
- A completion arriving after timeout can remain in the queue and interfere with a later retry.
- Two tested stale-completion retries ended with empty recording entries and unreferenced clusters. A deliberately labeled queue-drain control restored the reference result; that control was not a stock-firmware fix.
- Continuous-input tests filled sixteen prepared chunks during an error wait and then lost input. The recorded mono/stereo losses were 133,888 and 125,696 frames in those particular fixtures. Retained samples still matched exactly.
- The examined caller callbacks did not emit a failure-dependent signal for rejected input. Ordinary stop completion therefore did not prove that all input had been retained.

These cases establish why “the filesystem recovered” and “the recording is lossless” are different acceptance conditions. Their physical frequency, behavior with other card timings, concurrent recording loads and all UI reporting paths remain open.

## Requirements for a replacement

Associate completions with the operation that owns them. Define timeout, cancellation and late-event behavior. Bound queues and memory, expose overruns, and verify that saved audio duration matches accepted input frames. Check recovery through independent filesystem reconstruction, not only a successful native return code.

The public edition contains no synthetic disk images, native-generated project files, recordings, factory samples or binary execution traces. [Evidence boundaries](EVIDENCE.md) explain what can be reproduced from this checkout.
