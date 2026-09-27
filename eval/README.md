# Writing-skill evaluation harness

This harness runs skill-specific JSONL cases against different `SKILL.md` versions through headless Codex and saves the outputs for comparison.

## Requirements

- A working `codex` executable with `codex exec` support.
- Access to the selected model.
- Python 3.10 or newer.

The initial defaults are `gpt-5.6-luna` and low reasoning effort. They are command-line options, so the evaluation setup can change later.

## Run one version

From this directory:

```bash
python3 eval/run.py --skill clear-writing --version working --label candidate
```

Run a tagged baseline and the current checkout:

```bash
python3 eval/run.py --skill clear-writing --version v1.0.0 --label v1.0.0
python3 eval/run.py --skill clear-writing --version working --label candidate
```

The runner stores one JSON object per case in `eval/runs/<skill>/<label>/outputs.jsonl`, plus metadata and a summary. Cases live in `eval/cases/<skill>.jsonl`. The selected skill is copied into an isolated temporary `.agents/skills/<skill-name>/` directory for each run. Use a Git tag or commit such as `v1.0.0` for a saved version.

If the executable is not on `PATH`, pass it explicitly:

```bash
python3 eval/run.py --skill clear-writing --codex-bin /path/to/codex --version working --label candidate
```

Use `--dry-run` to inspect commands without making model calls.

For long runs, execute one case at a time and append the results. This makes the run resumable:

```bash
python3 eval/run.py --skill clear-writing --version working --label current --case-id verbose-technical
python3 eval/run.py --skill clear-writing --version working --label current --case-id logic-overclaim --append
```

## Compare versions

```bash
python3 eval/compare.py eval/runs/clear-writing/v1.0.0 eval/runs/clear-writing/candidate
```

This reports output length, length ratio, changed cases, and basic preservation checks for URLs, inline code, numbers, and dates. It does not judge meaning automatically; use the saved outputs for a blind human review of fidelity, brevity, plain language, coherence, and technical precision.

For less variable results, keep the model, reasoning effort, and cases fixed. If the model is nondeterministic, run each version more than once and compare the distribution rather than one output.

## Adding cases

Add one JSON object per line to `eval/cases/<skill>.jsonl` with an `id`, `input`, optional `request`, and optional `goals` array. The request lets non-rewriting skills define the task given to the agent. Keep real failure cases in the skill's file. They become regression tests for later revisions.
