# Guide for agents

This file explains how to change the skills collection without breaking its package or prompts.

## What this repo contains

This repository is a collection of agent skills written in Markdown. Each skill lives in `skills/<skill-name>/SKILL.md`. The repo has no build step.

Keep the skill portable. Do not write instructions that limit it to one or two agent tools.

## Key files

- `skills/` contains one directory per skill. Each directory has a required `SKILL.md` and may have `agents/`, `scripts/`, `references/`, or `assets/`.
- `README.md` explains installation, use, patterns, and version history.
- A skill's `agents/openai.yaml` holds optional UI metadata for OpenAI-compatible agents.
- `scripts/validate-package.py` checks every skill's frontmatter and package structure.

## Rules for changes

Keep each skill's `SKILL.md` and the relevant README sections in sync.

- **Patterns:** Patterns are numbered from 1 without gaps, strongest and most frequent first. A new tell earns a pattern only when no existing pattern already implies it; prefer folding it into an existing pattern. If you add, remove, or renumber a pattern, update the README tables, the README section title, and every §reference. The validator derives the count from the headings.
- **Version:** Keep each skill's version in its own `SKILL.md` under `metadata.version`. If a provider manifest declares a version, keep it in sync with that skill.
- **Compatibility:** Keep install and use instructions neutral across agents. Names such as Claude Code, OpenCode, and Codex are examples, not limits.
- **History:** Add a short README version note for any behavior change or non-obvious fix.
- **Checks:** Before publishing, run `python3 scripts/validate-package.py`, list the package with the relevant Skills CLI, and validate any provider-specific manifests that are present.

## Writing style

Use Plain Language in code comments, prompts, documentation, descriptions, validation messages, and progress reports.

- Lead with the main point.
- Use common words and active voice.
- Keep sentences and paragraphs short.
- Use one term for the same item.
- Use `must` for requirements.
- Use headings, lists, and tables when they help the reader.
- Remove repeated or unnecessary words.
- Limit acronyms and explain technical terms.
- Avoid double negatives.
- Keep exact identifiers, commands, paths, schema fields, quotations, watched phrases, and behavior-bearing examples.
- Keep the full technical meaning.

## Editing the skill

- Keep the YAML metadata valid.
- Treat the prompt below the metadata as the product.
- Prefer a short, clear instruction over another exception or repeated explanation.
