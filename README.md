# Agent skills

This repository is a collection of portable agent skills. It currently includes:

- `clear-writing` for clear, plain, logically consistent prose;
- `researching-guidelines` for planning and documenting research experiments;
- `technical-writing` for research papers and technical documents.

## Installation

Install the collection with the Skills CLI:

```bash
npx skills add nassimberrada/skills --global
```

Leave off `--global` to install the skills only in the current project. Add `--agent <name>` or `--agent '*'` to choose which agents receive them, then reload their skills.

Claude Code 2.1.142 or newer can install the plugin instead:

```text
/plugin marketplace add nassimberrada/skills
/plugin install skills@skills
```

For a manual install, copy the skill directory you need from `skills/` into the agent's skill folder. Each skill's README describes its purpose and design.

## Repository structure

Each skill is self-contained:

```text
skills/<skill-name>/
├── SKILL.md              # Agent instructions
├── README.md             # Principles and design notes
└── agents/openai.yaml    # Optional provider metadata
```

Evaluation cases live in `eval/cases/<skill-name>.jsonl`, and saved runs live in `eval/runs/<skill-name>/<version>/`.

## Evaluation

Use the shared harness to run a skill against its cases:

```bash
python3 eval/run.py --skill clear-writing --version working --label candidate
python3 eval/run.py --skill researching-guidelines --version working --label candidate
python3 eval/run.py --skill technical-writing --version working --label candidate
```

Compare two runs for the same skill:

```bash
python3 eval/compare.py eval/runs/clear-writing/v1.0.0 eval/runs/clear-writing/candidate
```

See [`eval/README.md`](eval/README.md) for options and the case format.

## Adding a skill

Create `skills/<skill-name>/SKILL.md` with frontmatter containing `name`, `description`, and `metadata.version`. Add a `README.md` explaining the skill's core principles and design, optional provider metadata, and `eval/cases/<skill-name>.jsonl`. Run:

```bash
python3 scripts/validate-package.py
```

## License

MIT
