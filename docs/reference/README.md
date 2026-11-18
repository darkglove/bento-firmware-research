# Decoded reference facts

These are curated research tables, not original vendor files or proprietary code exports. The main-image identity is recorded in [firmware profiles](firmware-profiles.json).

- [Parameter registry, 1.6.8](parameter-registry-1.6.8.md): keys, version-specific IDs, labels, raw ranges and related types.
- [Enumeration options, 1.6.8](enums-1.6.8.md): decoded option lists.
- [Object schema, 1.6.8](object-model-1.6.8.md): type/property/default relationships and corrected runtime names.
- [UI state routing, 1.6.8](ui-states-1.6.8.md): states, events, queue types and class addresses; firmware text strings omitted.
- [Traced pin configuration, 1.6.1](pin-map-1.6.1.md): version-limited register facts, not a schematic.
- [Integration checkpoints](integration-checkpoints.json): machine-readable index of the 74 later checkpoints.
- [Publication provenance](publication-provenance.json): source-record hashes, dates and limitations.

Parameter IDs and addresses are not portable to another build. Storage keys are the preferred logical identities. A decoded option is not proof that the corresponding UI or audio behavior is exposed or working. The original extraction harness is not packaged; see [evidence limits](../research/EVIDENCE.md).
