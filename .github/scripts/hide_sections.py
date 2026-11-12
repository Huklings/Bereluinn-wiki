"""Remove listed sections from notes before the site is built.

Runs in CI on the checked-out copy only; the vault keeps every section.
Usage: python hide_sections.py <vault dir> <list file>
"""
import pathlib
import re
import sys

vault = pathlib.Path(sys.argv[1])
prefixes = [
    line.strip().lower()
    for line in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
]

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def strip(text: str) -> str:
    out, skip_level, in_fence = [], None, False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
        m = None if in_fence else HEADING.match(line)
        if m:
            level = len(m.group(1))
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and m.group(2).lower().startswith(tuple(prefixes)):
                skip_level = level
        if skip_level is None:
            out.append(line)
    return "".join(out)


changed = 0
for path in vault.rglob("*.md"):
    if any(p.startswith(".") for p in path.relative_to(vault).parts):
        continue
    text = path.read_text(encoding="utf-8")
    new = strip(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1
print(f"Hid sections in {changed} file(s)")
