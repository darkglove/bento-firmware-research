"""Independently compare a candidate with the exact supported archive. Never flashes."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ARCHIVE='ecb16e9cab1fefe8ee234169b9311640f1f89575fbe4a3154710f9e7ba7fff67'
MAIN='14475e9d5068f5659d0fe0b00fc1278c1479c43ed9fda3d40654d5f3a7a6bbb3'
SECOND='8100906327093463fb58f531ee28583423a9881ea3a7d5b77874a7700735e99d'
OUTPUT='b7bc3141b1acb4fac737a1ad4a0b754787d6c4375dd2bb9bdc1abc9dc385f443'
def sha(b): return hashlib.sha256(b).hexdigest()
def require(ok,message):
    if not ok: raise ValueError(message)
def verify(archive,candidate):
    require(sha(archive.read_bytes())==ARCHIVE,'Wrong archive hash')
    with zipfile.ZipFile(archive) as z:
        original=z.read('bento1.bin'); second=z.read('bento2.bin')
    require(sha(original)==MAIN and sha(second)==SECOND,'Wrong component hash')
    modified=(candidate/'bento1.bin').read_bytes()
    require(len(modified)==len(original)==1523516,'Wrong main image length')
    changes=[(i,a,b) for i,(a,b) in enumerate(zip(original,modified)) if a!=b]
    require(changes==[(0x14be1f,0x53,0x73)],'Unexpected byte differences')
    require(sha(modified)==OUTPUT,'Wrong output hash')
    require((candidate/'bento2.bin').read_bytes()==second,'Companion changed')
    require((candidate/'rollback/bento1.bin').read_bytes()==original,'Wrong main rollback')
    require((candidate/'rollback/bento2.bin').read_bytes()==second,'Wrong companion rollback')
    m=json.loads((candidate/'manifest.json').read_text(encoding='utf-8'))
    for k,v in {'archive_sha256':ARCHIVE,'bento1_original_sha256':MAIN,'bento1_candidate_sha256':OUTPUT,'bento2_unchanged_sha256':SECOND,'bento1_size':1523516,'bento2_size':85696,'changed_file_offset':'0x14be1f','old_byte':'53','new_byte':'73','old_text':'Global Settings','new_text':'Global settings'}.items():
        require(m.get(k)==v,'Manifest mismatch: '+k)
    print('PASS: exact baseline, one intended byte, unchanged companion, rollback and manifest verified')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',required=True,type=Path)
    p.add_argument('--candidate',required=True,type=Path)
    a=p.parse_args();verify(a.archive,a.candidate)
