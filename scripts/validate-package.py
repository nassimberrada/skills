#!/usr/bin/env python3
"""Validate the multi-skill package without external dependencies."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

def fail(message: str) -> None:
    raise SystemExit(message)

if not SKILLS_DIR.is_dir():
    fail("Create a skills/ directory")

skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
if not skill_files:
    fail("Add at least one skills/<name>/SKILL.md file")

names: set[str] = set()
for path in skill_files:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.relative_to(ROOT)} must begin with YAML metadata")
    metadata = match.group(1)
    name_match = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", metadata)
    description_match = re.search(r"(?m)^description:\s*(.+)$", metadata)
    version_match = re.search(r'''(?m)^\s+version:\s*["']?([0-9]+\.[0-9]+\.[0-9]+)["']?\s*$''', metadata)
    if not name_match or not description_match or not version_match:
        fail(f"{path.relative_to(ROOT)} needs name, description, and metadata.version")
    name = name_match.group(1).strip('"\'')
    if name != path.parent.name:
        fail(f"{path.relative_to(ROOT)} name {name!r} must match its directory")
    if name in names:
        fail(f"Duplicate skill name: {name}")
    names.add(name)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"Invalid skill name: {name}")

for name in names:
    case_file = ROOT / "eval" / "cases" / f"{name}.jsonl"
    if not case_file.exists():
        fail(f"Add evaluation cases for {name}: {case_file.relative_to(ROOT)}")

print(f"Validated {len(names)} skills: {', '.join(sorted(names))}")
