# Technical writing

Technical Writing helps agents produce research papers, technical reports, and related documentation with precise claims, clear definitions, readable structure, and evidence that matches the conclusion.

## Core principles

- State claims literally and avoid rhetorical flourishes, metaphors, and slogans.
- Use plain language, short sentences, concrete verbs, and one term for one concept.
- Define project-specific terms at first use and explain repository-specific context.
- State what a reported study contains, including its protocol, data, environment, and registered prediction when relevant.
- Give each paragraph one job: lead with the claim, then provide evidence, assumptions, limits, or examples.
- Separate capability scores from cost, latency, and other operational measures.
- Verify sources and provide a clickable identifier and accurate author list when citing them.
- Report preliminary numbers as pilots and include the configuration version and known audit limits.
- Keep development utilities and harness mechanics out of the paper unless they are part of the experimental design.

## Design

The skill organizes technical writing around a clear argument: abstract, introduction, related work, methodology, results, discussion, and conclusion. Definitions, figures, tables, citations, and limitations support that argument rather than decorate it.

It treats precision as a structural property. Claims should appear near their conditions and evidence; headings should state findings; figures and tables should stand on their own; and the strength of a conclusion should match the evidence available.

The detailed operating instructions are in [`SKILL.md`](SKILL.md). The current skill version is `1.0.0`.

## License

MIT
