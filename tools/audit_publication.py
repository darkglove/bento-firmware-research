"""Audit Git content before publication. A check aids, but cannot replace, human review."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = {'.md', '.py', '.java', '.json'}
SPECIAL = {'.gitignore', '.gitattributes'}
ALLOWED_DIRS = {'docs', 'tools', 'tests', 'ghidra'}
MAX_FILE_BYTES = 250_000
PATTERNS = {
    'credential': re.compile(r'(?<![A-Za-z0-9_-])(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16}|sk-[A-Za-z0-9_-]{25,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)'),
    'personal machine path': re.compile(r'(?:[A-Za-z]:[\\/](?:Users|Dropbox|Projects)[\\/]|/(?:home|Users)/[A-Za-z0-9_.-]+/)', re.I),
    'private network address': re.compile(r'\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b'),
    'private conversation link': re.compile(r'discord(?:app)?\.com/channels/\d+', re.I),
    'large encoded payload': re.compile(r'(?<![A-Za-z0-9+/])[A-Za-z0-9+/]{500,}={0,2}'),
}
EMAIL = re.compile(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], stderr=subprocess.DEVNULL)


def inspect_text(data, denylist=()):
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return ['non-UTF-8 data']
    findings = ['binary NUL byte'] if '\0' in text else []
    findings += [label for label, pattern in PATTERNS.items() if pattern.search(text)]
    if any(not email.lower().endswith('@users.noreply.github.com') for email in EMAIL.findall(text)):
        findings.append('personal or non-anonymous email')
    if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', text, re.I) for term in denylist):
        findings.append('private denylist match')
    return findings


def inspect_file(name, data, denylist=()):
    path = PurePosixPath(name)
    findings = []
    if path.suffix.lower() not in SUFFIXES and name not in SPECIAL:
        findings.append('file type not approved for publication')
    if len(path.parts) > 1 and path.parts[0] not in ALLOWED_DIRS:
        findings.append('directory not approved for publication')
    if len(data) > MAX_FILE_BYTES:
        findings.append('file exceeds review size limit')
    if path.suffix.lower() == '.json' and path.parent.as_posix() != 'docs/reference':
        findings.append('JSON outside reviewed reference directory')
    return findings + inspect_text(data, denylist)


def audit(staged=False, history=False, denylist=(), history_commit=None):
    findings = []
    files = git('ls-files', '-z').decode().split('\0')
    checked = 0
    for name in filter(None, files):
        mode = git('ls-files', '--stage', '--', name).split()[0]
        if mode not in (b'100644', b'100755'):
            findings.append({'path': name, 'scope': 'current', 'rules': ['non-regular Git entry']})
            continue
        if not staged and (ROOT / name).is_symlink():
            findings.append({'path': name, 'scope': 'working tree', 'rules': ['symlink working file']})
            continue
        data = git('show', ':' + name) if staged else (ROOT / name).read_bytes()
        rules = inspect_file(name, data, denylist)
        checked += 1
        if rules:
            findings.append({'path': name, 'scope': 'index' if staged else 'working tree', 'rules': rules})
    blob_count = 0
    commit_count = 0
    if history:
        for row in git('rev-list', '--objects', history_commit or '--all').decode().splitlines():
            sha, _, name = row.partition(' ')
            kind = git('cat-file', '-t', sha).strip()
            if kind not in (b'blob', b'commit'):
                continue
            data = git('cat-file', kind.decode(), sha)
            if kind == b'blob':
                blob_count += 1
                rules = inspect_file(name, data, denylist)
            else:
                commit_count += 1
                rules = inspect_text(data, denylist)
            if rules:
                findings.append({'path': name or '(commit metadata)', 'scope': 'history', 'object': sha, 'rules': rules})
    return {'current_files': checked, 'historical_blobs': blob_count, 'historical_commits': commit_count,
            'history_scope': history_commit or ('all locally reachable refs' if history else None),
            'findings': findings, 'passed': not findings,
            'limits': 'Only selected Git content and configured patterns are checked; human provenance review is required.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staged', action='store_true', help='Inspect actual index bytes, not working-tree bytes')
    parser.add_argument('--history', action='store_true', help='Also inspect all locally reachable fetched Git history')
    parser.add_argument('--history-commit', help='With --history, audit only this exact 40-hex commit and its ancestors')
    parser.add_argument('--denylist-file', type=Path, help='Private local file: one private term per line; never commit it')
    args = parser.parse_args()
    if args.history_commit and (not args.history or not re.fullmatch(r'[0-9a-f]{40}', args.history_commit)):
        parser.error('--history-commit requires --history and an exact 40-hex commit')
    denylist = []
    if args.denylist_file:
        denylist = [line.strip() for line in args.denylist_file.read_text(encoding='utf-8').splitlines() if line.strip()]
    result = audit(args.staged, args.history, denylist, args.history_commit)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
