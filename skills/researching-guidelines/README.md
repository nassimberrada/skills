# Researching guidelines

Researching Guidelines helps an agent plan, run, and document research experiments so that each result can be checked, reproduced, and reused.

## Core principles

- Separate observations, open questions, planned checks, and hypotheses.
- Make each hypothesis specific enough for an experiment to support or reject it.
- Record the configuration, inputs, results, and conclusion for every meaningful run.
- Keep an experiments journal with links to traces, data, and visualizations.
- Start with a representative quick test before spending time on a statistically significant run.
- Export raw data and detailed traces, not only a final summary.
- Record versions, parameters, and stopping conditions with the outputs.

## Design

The skill treats research as an iterative loop: define the context, state testable hypotheses, run a quick validation, inspect the traces, then run and document the fuller experiment. The quick mode is part of the design, not an informal shortcut; it should catch configuration and logic errors while remaining representative enough to be useful.

The resulting record should let another person reconstruct what happened and reuse the data for later analysis or visualization.

The detailed operating instructions are in [`SKILL.md`](SKILL.md). The current skill version is `1.0.0`.

## License

MIT
