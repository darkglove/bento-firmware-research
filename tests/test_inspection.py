import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('inspection', ROOT / 'tools/inspect_firmware.py')
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class Inspection(unittest.TestCase):
    def test_unknown_stock_is_rejected(self):
        with self.assertRaises(ValueError):
            tool.require_stock(b'synthetic', '1.6.8', 'bento1.bin')

    def test_ranges(self):
        self.assertEqual(tool.ranges([1, 2, 4, 8, 9]), [[1, 2], [4, 4], [8, 9]])

    def test_change_append_and_truncate(self):
        # Synthetic profile exists only inside this test; shipped hashes stay fixed.
        data = b'abcdefgh'
        profiles = {'versions': {'fixture': {'bento1.bin': tool.identity(data)}},
                    'main_regions': [{'name': 'fixture', 'start': hex(tool.BASE), 'end': None}]}
        with patch.object(tool, 'PROFILES', profiles):
            changed = tool.compare(data, b'abZdefgh12', 'fixture')
            self.assertEqual(changed['changed_existing_bytes'], 1)
            self.assertEqual(changed['appended_bytes'], 2)
            self.assertEqual(changed['range_count'], 2)
            self.assertFalse(changed['hardware_safety_assessed'])
            short = tool.compare(data, data[:3], 'fixture')
            self.assertEqual(short['removed_bytes'], 5)
            self.assertEqual(short['changed_existing_bytes'], 0)

    def test_empty_file_rejected_without_change(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'empty.bin'
            p.write_bytes(b'')
            with self.assertRaises(ValueError):
                tool.read_image(p)
            self.assertEqual(p.read_bytes(), b'')

    def test_read_does_not_modify_input(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'input.bin'
            p.write_bytes(b'synthetic')
            self.assertEqual(tool.read_image(p), b'synthetic')
            self.assertEqual(p.read_bytes(), b'synthetic')


if __name__ == '__main__':
    unittest.main()
