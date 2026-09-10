#!/usr/bin/env python3
"""Run writing-skill evaluation cases through headless Codex."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = Path(__file__).resolve().parent / "cases.jsonl"


def read_cases(path: Path) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as error:
            raise SystemExit(f"Invalid JSON in {path}:{line_number}: {error}")
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not isinstance(case.get("input"), str):
            raise SystemExit(f"Each case needs string fields 'id' and 'input': {path}:{line_number}")
        cases.append(case)
    if not cases:
        raise SystemExit(f"No cases found in {path}")
    return cases


def skill_for_ref(ref: str) -> str:
    if ref in {"working", "current", "."}:
        return (ROOT / "SKILL.md").read_text(encoding="utf-8")
    path = Path(ref)
    if path.is_file():
        return path.read_text(encoding="utf-8")
    result = subprocess.run(
        ["git", "show", f"{ref}:SKILL.md"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise SystemExit(f"Could not read SKILL.md from git ref {ref!r}: {result.stderr.strip()}")
    return result.stdout


def skill_name(skill: str) -> str:
    match = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", skill)
    if not match:
        raise SystemExit("Selected SKILL.md has no top-level 'name' field")
    return match.group(1).strip('"\'')


def prompt_for(name: str, text: str) -> str:
    return (
        f"${name}\n\n"
        "Rewrite the following text using the selected skill. Return only the final rewrite. "
        "Do not explain your process or add a critique. Preserve all supported facts and do not invent details.\n\n"
        "Text to rewrite:\n"
        f"{text}"
    )


def run_case(codex_bin: str, skill: str, case: dict[str, object], args: argparse.Namespace) -> str:
    name = skill_name(skill)
    with tempfile.TemporaryDirectory(prefix="writing-skill-eval-") as temp_name:
        temp_dir = Path(temp_name)
        skill_path = temp_dir / ".agents" / "skills" / name / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text(skill, encoding="utf-8")
        output_path = temp_dir / "last-message.txt"
        command = [
            codex_bin,
            "exec",
            "--skip-git-repo-check",
            "--json",
            "--model",
            args.model,
            "-c",
            f"model_reasoning_effort={args.reasoning_effort}",
            "--output-last-message",
            str(output_path),
            prompt_for(name, str(case["input"])),
        ]
        if args.dry_run:
            print("$", " ".join(command))
            return ""
        result = subprocess.run(command, cwd=temp_dir, text=True, capture_output=True, check=False)
        if result.returncode:
            raise RuntimeError(
                f"Codex failed for case {case['id']} (exit {result.returncode}):\n{result.stderr.strip()}"
            )
        if output_path.exists():
            return output_path.read_text(encoding="utf-8").strip()
        # Fallback for older CLIs that ignore --output-last-message.
        messages: list[str] = []
        for line in result.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "item.completed":
                item = event.get("item", {})
                if item.get("type") == "agent_message":
                    messages.append("".join(part.get("text", "") for part in item.get("content", []) if isinstance(part, dict)))
        if messages:
            return messages[-1].strip()
        raise RuntimeError(f"Codex returned no final message for case {case['id']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Git ref containing SKILL.md, or a path to SKILL.md")
    parser.add_argument("--label", required=True, help="Directory name for the saved run")
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--output-root", type=Path, default=Path(__file__).resolve().parent / "runs")
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", "codex"))
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--reasoning-effort", default="low")
    parser.add_argument("--case-id", help="Run only the case with this ID")
    parser.add_argument("--append", action="store_true", help="Append to an existing output directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cases = read_cases(args.cases)
    if args.case_id:
        cases = [case for case in cases if case["id"] == args.case_id]
        if not cases:
            raise SystemExit(f"No case with ID {args.case_id!r} found in {args.cases}")
    skill = skill_for_ref(args.version)
    run_dir = args.output_root / args.label
    if run_dir.exists() and not args.dry_run and not args.append:
        raise SystemExit(f"Output directory already exists: {run_dir}; choose another --label")
    if not args.dry_run:
        run_dir.mkdir(parents=True, exist_ok=True)
        metadata_path = run_dir / "metadata.json"
        if not (args.append and metadata_path.exists()):
            metadata = {
                "version": args.version,
                "model": args.model,
                "reasoning_effort": args.reasoning_effort,
                "case_count": len(read_cases(args.cases)),
                "started_at": datetime.now(timezone.utc).isoformat(),
            }
            metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    outputs: list[dict[str, object]] = []
    for index, case in enumerate(cases, 1):
        print(f"[{index}/{len(cases)}] {case['id']}", file=sys.stderr)
        try:
            output = run_case(args.codex_bin, skill, case, args)
        except RuntimeError as error:
            if not args.dry_run and not args.append:
                shutil.rmtree(run_dir, ignore_errors=True)
            raise SystemExit(str(error))
        outputs.append({"id": case["id"], "input": case["input"], "goals": case.get("goals", []), "output": output})

    if not args.dry_run:
        output_file = run_dir / "outputs.jsonl"
        existing = output_file.read_text(encoding="utf-8") if args.append and output_file.exists() else ""
        output_file.write_text(
            existing + "".join(json.dumps(output, ensure_ascii=False) + "\n" for output in outputs), encoding="utf-8"
        )
        completed = sum(1 for line in output_file.read_text(encoding="utf-8").splitlines() if line.strip())
        (run_dir / "summary.json").write_text(json.dumps({"case_count": completed}, indent=2) + "\n", encoding="utf-8")
        print(f"Saved {len(outputs)} outputs to {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
