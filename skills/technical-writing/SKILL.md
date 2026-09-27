---
name: technical-writing
description: Edit research papers and technical documents for clear claims, precise definitions, plain language, rigorous evidence, and readable structure.
license: MIT
metadata:
  version: "1.0.0"
---

# Writing guidelines

Use this skill when writing or reviewing research papers, technical reports, and related documentation.

## Tone and rigor

- State claims literally. Do not use rhetorical flourishes, metaphors, or aphorisms to carry important meaning.
- Use plain, humanized language: short sentences, concrete verbs, and no stacked relative clauses.
- Do not use em dashes. Use commas, parentheses, or colons.
- Make result headings state findings, not jokes or slogans.

## Definitions and terms

- Define every project-specific term at first use. Add a short example when it helps.
- Do not assume the reader knows the codebase. Explain terms that are obvious only to people working in the repository.
- State precisely what a reported study contains, including the protocol, data, environment, and registered prediction when relevant.
- Use one term consistently for one concept.

## Structure

- Follow a clear argument: abstract, introduction, related work, methodology, results, discussion, and conclusion. Put implementation detail in an appendix when it does not support the main argument.
- Give each paragraph one job. Put the main claim early, then provide the evidence, assumptions, limitations, or example that supports it.
- Use numbered definitions when later sections need to refer to precise concepts.
- Add mathematics only when it sharpens a definition or argument.

## Figures and tables

- Add a figure when a process or relationship is easier to understand visually.
- Give every figure a self-contained caption. Give every table a legend that explains its columns and classifications.
- Inspect rendered output for overflow, crowded labels, broken references, and unreadable tables.

## Sources and results

- Verify sources before citing them. Include a clickable identifier such as an arXiv ID or DOI and the real author list.
- Use author-year citations when appropriate, linked to the reference entry.
- Report preliminary numbers as pilots and include the configuration version and known audit limits.
- Keep capability scores separate from cost, latency, and other operational measures.

## Keep out of the paper

Development utilities, quick modes, resume mechanics, dashboards, and harness plumbing belong in engineering documentation or an appendix unless they are part of the experimental design.
