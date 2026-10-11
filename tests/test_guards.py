"""Firmware-free rejection tests; not evidence of successful firmware execution."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    s=importlib.util.spec_from_file_location(name,ROOT/'tools'/(name+'.py'))
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
builder=load('build_minimal_text_probe');verifier=load('verify_probe')
class Guards(unittest.TestCase):
    def test_empty_image_rejected(self):
        with self.assertRaisesRegex(ValueError,'Wrong main image hash'): builder.transform(b'')
    def test_wrong_image_rejected(self):
        with self.assertRaisesRegex(ValueError,'Wrong main image hash'): builder.transform(b'Global Settings\0')
    def test_wrong_archive_creates_no_output(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);(p/'bad.zip').write_bytes(b'not firmware')
            with self.assertRaisesRegex(ValueError,'Wrong archive hash'): builder.build(p/'bad.zip',p/'output')
            self.assertFalse((p/'output').exists())
    def test_verifier_rejects_wrong_archive(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);(p/'bad.zip').write_bytes(b'not firmware')
            with self.assertRaisesRegex(ValueError,'Wrong archive hash'): verifier.verify(p/'bad.zip',p/'missing')
if __name__=='__main__':unittest.main()
