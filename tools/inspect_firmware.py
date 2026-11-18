"""Read-only identity and change-range inspection. Never writes or flashes firmware."""
import argparse
import hashlib
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
PROFILES = json.loads((ROOT / 'docs/reference/firmware-profiles.json').read_text(encoding='utf-8'))
BASE = int(PROFILES['main_load_address'], 16)
MAX_BYTES = 4 * 1024 * 1024


def read_image(path):
    path = Path(path)
    if not path.is_file() or path.is_symlink():
        raise ValueError('Input must be a regular, non-symlink file')
    with path.open('rb') as stream:
        data = stream.read(MAX_BYTES + 1)
    if not data or len(data) > MAX_BYTES:
        raise ValueError('Input is empty or exceeds the inspection size limit')
    return data


def identity(data):
    return {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def require_stock(data, version, component):
    expected = PROFILES['versions'][version][component]
    if identity(data) != expected:
        raise ValueError('Input does not match the selected stock component')


def ranges(indices):
    result = []
    for index in indices:
        if result and index == result[-1][1] + 1:
            result[-1][1] = index
        else:
            result.append([index, index])
    return result


def inspect_pair(main, companion, version):
    require_stock(main, version, 'bento1.bin')
    require_stock(companion, version, 'bento2.bin')
    regions = []
    for region in PROFILES['main_regions']:
        start = int(region['start'], 16)
        end = int(region['end'], 16) if region['end'] else BASE + len(main)
        offset = start - BASE
        stack, reset = struct.unpack_from('<II', main, offset)
        regions.append({'name': region['name'], 'start': hex(start), 'end_exclusive': hex(end),
                        'initial_stack': hex(stack), 'reset_vector': hex(reset)})
    return {'version': version, 'components': {'bento1.bin': identity(main), 'bento2.bin': identity(companion)},
            'regions': regions, 'hardware_safety_assessed': False}


def compare(main, candidate, version):
    require_stock(main, version, 'bento1.bin')
    if not candidate or len(candidate) > MAX_BYTES:
        raise ValueError('Candidate is empty or exceeds the inspection size limit')
    common = min(len(main), len(candidate))
    changes = ranges(i for i in range(common) if main[i] != candidate[i])
    changed_count = sum(end - start + 1 for start, end in changes)
    if len(main) != len(candidate):
        changes.append([common, max(len(main), len(candidate)) - 1])
    affected = []
    for region in PROFILES['main_regions']:
        lo = int(region['start'], 16) - BASE
        hi = (int(region['end'], 16) - BASE) if region['end'] else max(len(main), len(candidate))
        if any(start < hi and end >= lo for start, end in changes):
            affected.append(region['name'])
    end_address = BASE + len(candidate)
    return {'version': version, 'original': identity(main), 'candidate': identity(candidate),
            'changed_existing_bytes': changed_count, 'appended_bytes': max(0, len(candidate) - len(main)),
            'removed_bytes': max(0, len(main) - len(candidate)), 'range_count': len(changes),
            'ranges_shown': [{'start': hex(BASE + a), 'end_inclusive': hex(BASE + b)} for a, b in changes[:64]],
            'ranges_truncated': len(changes) > 64, 'affected_regions': affected,
            'candidate_end_exclusive': hex(end_address),
            'same_end_sector_as_stock': (end_address - 1) // 0x20000 == (BASE + len(main) - 1) // 0x20000,
            'hardware_safety_assessed': False,
            'limits': 'Range comparison only; no instruction semantics, bootloader acceptance or companion verification in compare mode.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('inspect', 'compare'):
        command = sub.add_parser(name)
        command.add_argument('--version', choices=sorted(PROFILES['versions']), required=True)
        command.add_argument('--main', required=True, help='Local stock bento1.bin')
        command.add_argument('--companion' if name == 'inspect' else '--candidate', required=True)
    args = parser.parse_args()
    try:
        stock = read_image(args.main)
        result = (inspect_pair(stock, read_image(args.companion), args.version) if args.command == 'inspect'
                  else compare(stock, read_image(args.candidate), args.version))
    except (ValueError, OSError, struct.error) as exc:
        # Do not print an OSError containing a user's absolute input path.
        parser.exit(2, 'Inspection refused: ' + (str(exc) if isinstance(exc, ValueError) else 'input read/format error') + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
