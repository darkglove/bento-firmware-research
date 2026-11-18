import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('publication', ROOT / 'tools/audit_publication.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Publication(unittest.TestCase):
    def test_vendor_binary_rejected_even_if_text(self):
        self.assertIn('file type not approved for publication', audit.inspect_file('firmware.bin', b'example'))

    def test_disguised_binary_rejected(self):
        self.assertIn('binary NUL byte', audit.inspect_file('docs/example.md', b'example\0'))

    def test_local_input_directory_rejected(self):
        self.assertIn('directory not approved for publication', audit.inspect_file('inputs/example.md', b'example'))

    def test_private_denylist_is_case_insensitive(self):
        self.assertIn('private denylist match', audit.inspect_text(b'Project ExamplePerson notes', ['exampleperson']))

    def test_fake_credential_rejected_without_echo(self):
        value = ('gh' + 'p_' + 'x' * 30).encode()
        findings = audit.inspect_text(value)
        self.assertIn('credential', findings)
        self.assertNotIn(value.decode(), str(findings))

    def test_anonymous_commit_email_allowed(self):
        email = 'contributors' + '@' + 'users.noreply.github.com'
        self.assertEqual(audit.inspect_text(email.encode()), [])

    def test_personal_email_rejected(self):
        email = 'example' + '@' + 'example.invalid'
        self.assertIn('personal or non-anonymous email', audit.inspect_text(email.encode()))

    def test_utf8_rejected_if_invalid(self):
        self.assertIn('non-UTF-8 data', audit.inspect_text(bytes([255])))


if __name__ == '__main__':
    unittest.main()
