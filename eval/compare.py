#!/usr/bin/env python3
"""Compare two Clearwriter evaluation runs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TOKEN_RE = re.compile(r"`[^`]+`|https?://\S+|\b\d+(?:\.\d+)?\b")


def load(path: Path) -> dict[str, dict[str, object]]:
    file = path / "outputs.jsonl"
    if not file.exists():
        raise SystemExit(f"Missing {file}")
    return {item["id"]: item for item in (json.loads(line) for line in file.read_text(encoding="utf-8").splitlines() if line.strip())}


def tokens(text: str) -> set[str]:
    return {token.rstrip(".,;:!?)") for token in TOKEN_RE.findall(text)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    baseline, candidate = load(args.baseline), load(args.candidate)
    ids = list(dict.fromkeys([*baseline.keys(), *candidate.keys()]))
    print(f"{'case':24} {'base words':>10} {'new words':>10} {'ratio':>8}  checks")
    print("-" * 78)
    for case_id in ids:
        old = str(baseline.get(case_id, {}).get("output", ""))
        new = str(candidate.get(case_id, {}).get("output", ""))
        old_words, new_words = len(old.split()), len(new.split())
        ratio = new_words / old_words if old_words else 0
        missing = sorted(tokens(str(baseline.get(case_id, {}).get("input", ""))) - tokens(new))
        checks = "ok" if not missing else "missing:" + ",".join(missing[:3])
        print(f"{case_id:24} {old_words:10} {new_words:10} {ratio:8.2f}  {checks}")
    print("\nReview saved outputs manually for fidelity, plain language, coherence, and technical precision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
