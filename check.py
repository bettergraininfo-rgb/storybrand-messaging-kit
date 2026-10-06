"""Run with python3 check.py; no dependencies or network."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
skill = root / '.agents/skills/storybrand-messaging/SKILL.md'
assert skill.is_file(), 'Missing canonical skill'
text = skill.read_text()
assert text.startswith('---\nname: storybrand-messaging\ndescription: Use when ')
lessons = skill.parent / 'references/lessons.md'
assert len(re.findall(r'^## \d+\.', lessons.read_text(), re.M)) == 10
for file in root.rglob('*.md'):
    if '.git' in file.parts:
        continue
    content = file.read_text()
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if not link.startswith(('https://', 'http://', '#')):
            assert (file.parent / link.split('#')[0]).exists(), (file, link)
    for private in ('/home/', 'BRAIN.toon', 'transcripts/'):
        assert private.lower() not in content.lower(), (file, private)
assert 'Read .agents/skills/storybrand-messaging/SKILL.md and its linked lessons.' in (root / 'README.md').read_text()
assert len(list(root.rglob('SKILL.md'))) == 1, 'Keep one canonical skill'
assert not any(p.suffix.lower() in {'.pdf', '.toon', '.mp4', '.zip'} for p in root.rglob('*'))
print('PASS: canonical skill, 10 lessons, local links, adapter, publication hygiene')
