# Reproduce the first firmware patch

Read [SAFETY.md](SAFETY.md) first. This tutorial builds files on your computer; it does not install them. The goal is a controlled proof-of-concept, not new firmware compiled from source.

## 1. Get the toolkit

```sh
git clone https://github.com/darkglove/bento-firmware-research.git
cd bento-firmware-research
python --version
python -m unittest discover -s tests -v
```

Use Python 3.10 or later. If your system uses `python3` or `py -3`, substitute that launcher consistently. No pip install is required for the patch.

## 2. Supply the exact firmware archive

Obtain Bento 1.6.1 from a legitimate source such as the vendor's [downloads page](https://1010music.com/downloads), subject to their access requirements and availability. Put your own archive at `inputs/bento-1.6.1.ZIP` (create `inputs` yourself), or supply a quoted absolute path with `--archive`.

The required archive SHA-256 is:

```text
ecb16e9cab1fefe8ee234169b9311640f1f89575fbe4a3154710f9e7ba7fff67
```

Its root ZIP entries must be `bento1.bin` and `bento2.bin`. The original components are:

- bento1.bin: 1,523,516 bytes; SHA-256 `14475e9d5068f5659d0fe0b00fc1278c1479c43ed9fda3d40654d5f3a7a6bbb3`.
- bento2.bin: 85,696 bytes; SHA-256 `8100906327093463fb58f531ee28583423a9881ea3a7d5b77874a7700735e99d`.

The previously studied release notes call the release 1.6; the archive name and internal version string are 1.6.1. Names alone are not validation. A differently compressed ZIP can have a different archive hash even when its components match: this conservative builder rejects that too. Do not rename another release or remove the hash gate to force acceptance.

## 3. Build into a NEW directory

```sh
python tools/build_minimal_text_probe.py --archive inputs/bento-1.6.1.ZIP --output output/first-probe
```

Expected files:

```text
output/first-probe/
  bento1.bin
  bento2.bin
  manifest.json
  rollback/bento1.bin
  rollback/bento2.bin
```

The script prints a manifest. The resulting bento1.bin SHA-256 must be:

```text
b7bc3141b1acb4fac737a1ad4a0b754787d6c4375dd2bb9bdc1abc9dc385f443
```

The builder refuses an existing output directory to avoid overwriting results. For another run choose a different directory. Never use your SD card as the output location.

## 4. Independently verify the result

```sh
python tools/verify_probe.py --archive inputs/bento-1.6.1.ZIP --candidate output/first-probe
```

A successful run prints `PASS: exact baseline, one intended byte, unchanged companion, rollback and manifest verified`.

These are expected results, not proof that your local commands have run. Keep the actual output and manifest for your own evidence.

## 5. Understand precisely what changed

The null-terminated ASCII string starts at file offset `0x14be18`. At offset `0x14be1f`, `0x53` (S) becomes `0x73` (s):

```text
Global Settings -> Global settings
```

The file length, null terminator and every other byte stay unchanged. The version remains 1.6.1; bento2.bin stays byte-identical. In the inferred main-image mapping, the changed address is `0x0818be1f`.

The implementation gates the exact baseline hash, checks the unique original string and fixed offset, splices equal-length bytes, checks the diff and inverse transformation, and saves original rollback files. This technique is specific to this image, not portable offsets for other releases.

## 6. Stop at the hardware boundary

A verified output is an **untested firmware candidate**, not proof of bootability or safety. Before any installation establish a recovery route, preserve stock files and back up your card. No tool in this repository flashes hardware.

The previously reviewed v1.2 manual, PDF pages 15-16 (printed 6-7), describes placing both firmware files in the microSD root, entering the Bootloader screen, then pressing REC to install with external power connected. Wait for completion and automatic restart; do not interrupt power or remove the card. Confirm the current vendor instructions for your own device. Bento does not simply execute these SD files on normal boot.

If you independently decide to test: after a completed installation and restart, use PROJ to cycle to Global Settings and look for lowercase `s`. Record installation messages, a photo, normal basic operation and any stock-recovery test. An unchanged version number is expected and proves nothing by itself.

## Troubleshooting

- Wrong archive/image hash: stop; confirm the exact input. Do not weaken validation.
- Output already exists: choose a new directory; the builder will not overwrite it.
- Missing ZIP entry: wrong package structure; obtain the supported archive.
- Verifier failure: do not install; preserve diagnostics and compare against a clean rebuild.
- Device rejection or failure: record the exact message and use only an established vendor recovery route. Do not infer a signature/checksum cause or attempt bypasses from the error alone.

## Beyond this example

Read [GHIDRA.md](GHIDRA.md) and [RESEARCH.md](RESEARCH.md). For another patch, identify a new target for an exact image hash, trace all uses, define invariants and independently verify the output. Executable-code changes require substantially more analysis and testing. No appended-code technique or general feature injection is validated here.
