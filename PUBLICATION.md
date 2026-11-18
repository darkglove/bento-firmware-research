# Publication, privacy and provenance

This repository publishes original research explanations, decoded interface facts and reviewed original tools. It must remain separate from any private research repository's Git history.

## Never include

- Personal names or contact details from private work, account/session identifiers, private conversation links, machine paths, private network addresses, credentials or raw agent logs.
- Original 1010music firmware, update archives, manuals, release-note documents, factory projects, presets, wavetables, samples or other vendor files, regardless of extension.
- Patched firmware, rollback copies, compiled images, binary dumps, screenshots derived from firmware, proprietary decompilation/disassembly exports or encoded copies of those assets.
- Private project trackers, handoffs, working notes, unrelated project details or operational infrastructure.
- Third-party code without a separate provenance/license review.

A filename extension or an ignore rule cannot prove content is safe. Hashes, addresses, parameter names and independently written interface descriptions can be published as factual research after review. They are not a license to redistribute the source files.

## Publication procedure

1. Write or curate material in this separate public checkout. Use a reviewed file list; never copy the entire source workspace or merge its history.
2. Check every new file's origin and content. Use synthetic examples. Remove personal attribution and unnecessary exact session times. Cite public external sources with revision/date and label their claims as reports.
3. Run the firmware-free tests and check local documentation links.
4. Stage only the reviewed files. Run `python tools/audit_publication.py --staged --history`. A private local denylist can be supplied with `--denylist-file`; never commit that file.
5. Review the staged diff and commit author/committer identity. Use the repository's anonymous contributor identity. Do not include local absolute paths in output receipts.
6. Push only this repository's reviewed branch. Verify remote commit equality. Report evidence limitations and any historical finding honestly.

The audit checks approved text types/directories, size, UTF-8/NUL content, selected credential and private-context patterns, optional private terms, and locally reachable fetched history. It does not inspect inaccessible GitHub objects, forks, search caches, issues, attachments or every conceivable encoding. Human review remains required.

If personal information is already in a published commit, deleting the current line does not remove history. Prepare and review a narrowly scoped history correction, then obtain authorization before rewriting a shared remote. Never promise that force-pushing removes copies retained by others.

## Inputs and outputs

Keep local inputs under `inputs/`, generated material under `output/` or `analysis/`, and all such directories ignored. The tracked repository is text-only. Git can force-add ignored files, so the staged-content audit is mandatory for publication.

## Rights and claims

No vendor or third-party license is assigned by this repository. Do not add a blanket license over materials whose rights have not been established. Firmware analysis and a safety assessment are different activities; document failures and modeled boundaries as carefully as successes.
