"""Build an UNTESTED offline text probe from the exact supported archive.
No flashing, no checksum bypass, no edits to originals. Standard library only.
"""
from pathlib import Path
import hashlib
import json
import zipfile
import argparse

ARCHIVE_HASH = 'ecb16e9cab1fefe8ee234169b9311640f1f89575fbe4a3154710f9e7ba7fff67'
MAIN_HASH = '14475e9d5068f5659d0fe0b00fc1278c1479c43ed9fda3d40654d5f3a7a6bbb3'
SECOND_HASH = '8100906327093463fb58f531ee28583423a9881ea3a7d5b77874a7700735e99d'
OFFSET = 0x14BE18
OLD = b'Global Settings\0'
NEW = b'Global settings\0'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def transform(main):
    require(sha(main) == MAIN_HASH, 'Wrong main image hash')
    require(main.count(OLD) == 1, 'Expected unique original string')
    require(main[OFFSET:OFFSET+len(OLD)] == OLD, 'Wrong original bytes at offset')
    require(len(OLD) == len(NEW), 'Length change prohibited')
    patched = main[:OFFSET] + NEW + main[OFFSET+len(OLD):]
    diffs = [i for i, (a, b) in enumerate(zip(main, patched)) if a != b]
    require(len(main) == len(patched), 'Image length changed')
    require(diffs == [OFFSET+7], 'Not exactly the intended single byte')
    require(patched[:OFFSET+7] + bytes([main[OFFSET+7]]) + patched[OFFSET+8:] == main,
            'Inverse patch did not recover original')
    return patched

def build(archive, output):
    archive_data = archive.read_bytes()
    require(sha(archive_data) == ARCHIVE_HASH, 'Wrong archive hash')
    with zipfile.ZipFile(archive) as z:
        main, second = z.read('bento1.bin'), z.read('bento2.bin')
    require(sha(second) == SECOND_HASH, 'Wrong secondary image hash')
    patched = transform(main)
    # Rejection regression: tampering and applying twice must fail.
    rejected = 0
    for bad in (bytes([main[0] ^ 1])+main[1:], patched):
        try:
            transform(bad)
        except ValueError:
            rejected += 1
    require(rejected == 2, 'Negative tests failed')
    manifest = {
        'status': 'OFFLINE CANDIDATE ONLY - NOT HARDWARE TESTED',
        'archive_sha256': ARCHIVE_HASH,
        'bento1_original_sha256': MAIN_HASH,
        'bento1_candidate_sha256': sha(patched),
        'bento2_unchanged_sha256': SECOND_HASH,
        'bento1_size': len(main), 'bento2_size': len(second),
        'string_file_offset': hex(OFFSET), 'changed_file_offset': hex(OFFSET+7),
        'changed_address_in_inferred_map': hex(0x08040000+OFFSET+7),
        'old_byte': '53', 'new_byte': '73',
        'old_text': OLD[:-1].decode(), 'new_text': NEW[:-1].decode(),
        'checks': ['exact archive and both image hashes', 'unique exact original string',
                   'one byte changed', 'same image length', 'inverse recovers original',
                   'modified input rejected', 'double application rejected',
                   'output readback byte equality'],
        'limits': ['Bootloader integrity policy unknown', 'Not executed or flashed',
                   'Secondary component role unresolved', 'Rollback not hardware verified']
    }
    output.mkdir(parents=True, exist_ok=False)
    (output/'rollback').mkdir()
    for path, data in [(output/'bento1.bin',patched),(output/'bento2.bin',second),
                       (output/'rollback/bento1.bin',main),(output/'rollback/bento2.bin',second)]:
        path.write_bytes(data)
        require(path.read_bytes() == data, 'Output readback failed: '+str(path))
    require(sha(archive.read_bytes()) == ARCHIVE_HASH, 'Archive changed during build')
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2))

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',type=Path,default=Path('inputs/bento-1.6.1.ZIP'))
    p.add_argument('--output',type=Path,required=True)
    args = p.parse_args()
    build(args.archive,args.output)
