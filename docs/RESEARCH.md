# Technical findings and evidence limits

These static observations apply to the exact input hashes in [TUTORIAL.md](TUTORIAL.md). Research date: 2026-10-11. They derive from binary inspection and Ghidra/Capstone analysis, not recovered vendor symbols. Subsequent owner-reported device evidence is recorded separately below.

## Image layout

Both components have Cortex/Thumb-style vectors. Inferred raw load bases: bento1.bin `0x08040000`, bento2.bin `0x90000000`. Initial stack/reset values are `0x2404cda0` / `0x080403cd` and `0x20013868` / `0x900003c3` respectively. Odd reset addresses encode Thumb state. Ghidra 12.1.4 analysis recovered 4,609 functions / 2,874 strings in the main image and 413 / 9 in the companion. Automatic inventories are not proof of complete or correct recovery. Exact MCU, core assignment and companion role remain unresolved.

## Why this string was chosen

`Global Settings` is unique at file offset `0x14be18`, mapped address `0x0818be18`. Ghidra traced a reference from `FUN_08141944`, switch case `0x19`, via literal `0x08141fcc` and instruction `0x08141f58`. It passes the string to byte-copy helper `0x0818704e` and then a screen-title buffer. Capstone independently confirmed the load/call and null-padding copy loop. A second raw pointer at `0x08198134` is adjacent to a Project Settings pointer in a table; a menu interpretation is plausible but full indirect use is unproven. This is better supported than changing arbitrary text or a persistence key, not a guarantee of safety.

## CRC observations

`FUN_0809dc40` and `FUN_0809dd60` iterate bytes +8 through +0x4b of a record and store at +0x4c. These are 68-byte payloads. The former copies 0x48 bytes first and computes twice; a recovered caller alternates 0x50-sized records. `FUN_080e2f90` is a length-parameterized CRC-like helper; recovered callers `FUN_080e2fcc` and `FUN_080e2ffa` pass 0x44, again 68 bytes. These observed paths are not whole-image verification. Exact record semantics and indirect callers remain unresolved; decompiler signatures can omit arguments.

No match was found for the tested simple trailing CRC/word-sum layouts across 18 main images. This does NOT prove absence of checksums. Lack of familiar SHA/MD5/AES constants does NOT prove absence of signing; hardware-assisted or external checks remain possible. Installation bootloader policy is unexamined.

## Embedded disk-mode lead

`FUN_080a5140` references a vector region at `0x080e0000`, with stack `0x24029898` and Thumb reset `0x080e03c3`. This is an embedded-image/disk-mode lead, not proof that the installation bootloader is included in the supplied image. The manual explicitly distinguishes installed firmware from running SD files.

## Historical comparisons

A local collection of 18 versions / 36 binaries mapped to 22 unique images: 18 main images and four companion variants. Compilation shifts code; fixed offsets do not safely carry between releases. Adjacent-page identity is not semantic function equivalence. Two historical decompilations had unresolved-constructor warnings (1.5.3 at 0x0817e444, 1.5.32 at 0x0818127c); those functions need disassembly review. No historical vendor files or proprietary exports are distributed here.

## Prior-art distinction

[blackbox-mod](https://github.com/j3threejay/blackbox-mod), studied at revision `47f4312276a841548d1a5c82b930699fd1a45d11`, demonstrates techniques for Blackbox 3.1.9. It is NOT a Bento patch. Do not reuse its addresses, images or boot assumptions. No third-party code from that project is copied here.

## Evidence status

The supplied builder, original-input hash gates, exact-diff verifier and analysis helpers make the minimal example reproducible from user-supplied inputs. Original raw Ghidra exports are not distributed. The owner reports the one-byte candidate loaded and showed the lowercase `s`, but this repository does not independently verify the installation or establish full emulation, audio behavior, rollback success or appended-code support. Contribute evidence with exact hashes, method, observed output and limitations; avoid personal information or vendor binaries.

## Owner-reported device test — 2026-10-12T06:56:25+00:00

On 2026-10-12T06:56:25+00:00, the device owner reported that the one-byte test firmware loaded without issue, that the lowercase `s` in `Global settings` was visible, and that installation followed the usual firmware-update procedure. This is **owner-reported hardware evidence**, not an independently witnessed test. The report does not document installation logs, prolonged operation, audio/MIDI behavior, repeatability on other units, stock rollback, or interrupted-update recovery. Modified firmware remains experimental and is not proven safe from damage or bricking. Source: owner messages in the private project conversation; no private identifiers or binary evidence are published here. Applies only to the one-byte 1.6.1 probe with expected output SHA-256 `b7bc3141b1acb4fac737a1ad4a0b754787d6c4375dd2bb9bdc1abc9dc385f443`; device-file hash was not measured independently. Next: request logs/photo and a separate, recovery-aware rollback check if the owner wants to establish those claims.
