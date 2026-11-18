# Validation for the November 2026 public edition

Publication date: 18 November 2026. These checks validate the public documentation/tools and privacy boundary; they do not rerun the historical full-system emulator or establish device safety.

## Checks run for this edition

- Firmware-free Python tests: **17 passed**, including the original four guards, read-only inspection behavior and publication-rule rejection tests.
- Read-only inspector accepted the exact local **1.6.1 and 1.6.8** stock pairs and reported their expected component hashes and executable-region vectors.
- Comparing 1.6.8 stock with itself reported no differences.
- Comparing the existing local 1.6.8 T3 candidate reported **3 changed existing bytes, 76 appended bytes**, CM4-only affected ranges and exclusive end `0x081b6e80`. This is byte comparison, not loader or hardware acceptance. The candidate file is not published.
- Local documentation links, JSON structure and staged whitespace/content are checked before publication.
- Publication review uses an explicit file list, text/type checks, a private denylist and a reachable-history audit. Anonymous commit metadata is checked separately. No original vendor files, firmware binaries or private project history are included in the publication set.

See [PUBLICATION.md](../PUBLICATION.md) for audit limits and handling of historical personal information. The optional private denylist is not distributed.

## Earlier 1.6.1 tutorial evidence

The earlier release recorded a successful public builder run, independent one-byte/companion/rollback verification, and rejection of altered candidate bytes and manifest text. Its four firmware-free guards were rerun for this edition. A new firmware build was not required for this documentation/inspection-tool update.

The one-byte load is an anonymized owner report, not an independently witnessed test. Optional Ghidra commands and all supported operating systems were not exhaustively retested.

## Historical research results

The native startup/audio/storage/graphics/controller results in the [research guide](research/README.md) are carried forward from recorded experiments with explicit supplied environments. Raw traces and the complete harness are not included. Do not describe this publication's unit tests as reproducing those historical integration results.

The final controller-driven output-amplitude experiment remains unverified. The 1.6.8 hardware-test batch has offline results but no recorded device acceptance in this edition.
