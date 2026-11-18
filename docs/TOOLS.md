# Read-only inspection tools

Python 3.10+ is required. No package installation is needed. Obtain your own legitimate firmware from the vendor; no automatic downloader is included.

## Inspect an exact stock pair

```sh
python tools/inspect_firmware.py inspect --version 1.6.8 --main inputs/bento1.bin --companion inputs/bento2.bin
```

Both component sizes and SHA-256 hashes must match the selected [profile](reference/firmware-profiles.json). The tool prints component identities, the main executable-region boundaries and each region's initial vector values. It does not modify files, extract firmware, flash hardware or include the input path in its JSON report.

Use `--version 1.6.1` only with that pair. A mismatch is an error, not an invitation to disable validation. Identical companion files do not make the main images interchangeable.

## Compare an existing local candidate

```sh
python tools/inspect_firmware.py compare --version 1.6.8 --main inputs/bento1.bin --candidate output/example/bento1.bin
```

This command requires an exact supported original. It reports changed byte ranges, additions/removals, affected regions, hashes and whether the image ends in the same 128 KiB sector as stock. It shows at most 64 ranges and explicitly reports truncation.

It does **not** validate instruction semantics, execution permissions, the companion file, bootability, loader acceptance or hardware safety. A result with `same_end_sector_as_stock: true` is a location fact, not a safety pass. Compare mode does not create a candidate.

## Older patch workflow

The [1.6.1 tutorial](TUTORIAL.md) uses the existing builder and independent verifier. It remains separate from these read-only tools. New research documentation does not change its hashes or version support.

## Publication check

```sh
python -m unittest discover -s tests -v
python tools/audit_publication.py --staged --history
```

Run the audit after explicitly staging the reviewed publication set. It reads the actual Git index, so unstaged changes cannot substitute for what will be committed. A zero result is only one part of [publication review](../PUBLICATION.md).
