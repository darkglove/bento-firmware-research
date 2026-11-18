# Recovery evidence and experimental test boundaries

**Modified firmware can leave a device unusable. Offline execution and a matching hash do not establish safe installation or recovery.** This chapter records evidence and limits; it is not an instruction to flash a candidate.

## What is supported

Reviewed vendor documentation describes a bootloader entry at power-up and stock installation from the card. Preserving that loader and reinstalling the matching stock pair is a supported recovery approach. Consult the current [vendor documentation](https://1010music.com/downloads) for the exact device procedure and power requirements. The bootloader's hardware-test option is separate from installation and can emit very loud audio.

An earlier one-byte 1.6.1 text probe was reported to load and show the changed title. A later executable-code experiment was reported to reset-loop, with stock rollback restoring operation. The exact recovery-entry and power-off sequence was not recorded well enough to count as an independently demonstrated general recovery procedure. These reports are anonymized; no personal device records are published.

The failed experiment placed code near `0x080ff000`, outside the CM4's stock executable flash region and within the disk-mode sector. Protection and region preservation are therefore concrete concerns, not hypothetical substitutes for testing. The relative contribution of each issue to that hardware report is not independently isolated.

## The offline 1.6.8 batch

Four locally built cases were checked in November. No candidate files, rollback binaries or screenshots are distributed here.

| Case | Change | Recorded offline result |
|---|---|---|
| T0 | Unmodified stock pair | Reference startup/render |
| T1 | One title data byte at `0x0818e2f7`, S to s | Main-screen render unchanged; the title page itself was not demonstrated by this render |
| T2 | Palette entry 3 at `0x081b6d3c`, dark grey to blue | Same framebuffer indices; only the expected palette entry changes |
| T3 | Retarget one palette-loading call to appended code/table | Same indices; expected green palette change; 76 bytes appended |

T3's exclusive end is `0x081b6e80`, compared with stock `0x081b6e34`. The builder kept the companion unchanged, checked expected original bytes, limited modifications to the CM4 region, kept the end in the same flash sector and verified an in-memory reversal. The emulator used the CM4 execute restriction. A deliberately bad bank-1 target failed as required. Each normal case reached 201 application updates in the recorded offline test.

The batch's **device results are not recorded** in this edition. T1's main-screen equality does not prove its title page. T3's emulated execution does not prove loader acceptance. Keeping the end in a sector does not by itself prove the bootloader's actual erase policy.

## External comparison

At reviewed revision `960e4b1`, [bento-community-lab](https://github.com/hunting-ghosts/bento-community-lab/tree/960e4b1) described related modification and recovery experience. At `9e817b9`, [bento-playground](https://github.com/hunting-ghosts/bento-playground/tree/9e817b9) described a modified 1.6.8 build running on its maintainer's hardware. Those reports support the feasibility of appended application code; they do not certify this batch or another unit. The projects share a maintainer, so they are not two independent demonstrations. Their source is not copied here.

## Minimum evidence before a changed-image device test

1. Identify the installed and candidate versions by exact component hashes. Retain legitimately obtained stock files separately.
2. Back up user data and establish a bootloader-entry route that does not rely on the application working.
3. Preserve the bootloader, disk-mode image, factory calibration, option bytes and controller image unless a separately reviewed test explicitly concerns one of them.
4. Check changed ranges, execution permissions, image end and original-byte gates. Include a negative control in offline checks.
5. Use one bounded test with a visible expected result, explicit stopping conditions and a recorded route back to stock.
6. Record actual device observations separately from emulation and externally reported results.

The update images do not contain the full loader. Its complete integrity checks, erase granularity, power-loss behavior and all recovery failure modes remain unresolved. A small patch and an unchanged companion reduce the changed surface; they do not eliminate risk.
