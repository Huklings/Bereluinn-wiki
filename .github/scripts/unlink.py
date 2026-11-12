"""Turn wikilinks to private notes into plain text before the site is built.

Runs in CI on the checked-out copy only; the vault keeps its real links.
Usage: python unlink.py <vault dir> <list file>
"""
import pathlib
import re
import sys

vault = pathlib.Path(sys.argv[1])
names = {
    line.strip().lower()
    for line in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
}

# ![[...]] or [[...]]; inner text may contain an escaped table pipe "\|".
LINK = re.compile(r"(!?)\[\[([^\]]+?)\]\]")


def replace(m: re.Match) -> str:
    embed, inner = m.group(1), m.group(2)
    parts = re.split(r"\\?\|", inner, maxsplit=1)
    target = parts[0]
    alias = parts[1] if len(parts) > 1 else None
    note = target.split("#", 1)[0].strip()
    if note.lower() not in names:
        return m.group(0)
    if embed:
        return ""
    return alias if alias else note


changed = 0
for path in vault.rglob("*.md"):
    if any(p.startswith(".") for p in path.relative_to(vault).parts):
        continue
    text = path.read_text(encoding="utf-8")
    new = LINK.sub(replace, text)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1
print(f"Unlinked private notes in {changed} file(s)")
