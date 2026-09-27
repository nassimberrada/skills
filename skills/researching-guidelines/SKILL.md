---
name: researching-guidelines
description: Plan and document research experiments with clear hypotheses, fast validation runs, detailed traces, and reusable results.
license: MIT
metadata:
  version: "1.0.0"
---

# Researching guidelines

Use this skill when planning, running, or documenting a research experiment.

For each research direction, define a short context with:

- observations: what is already known;
- questions: what remains unclear;
- research: what will be checked;
- hypotheses: predictions that the experiment can support or reject.

Keep an experiments journal. Each entry must record what was done, the configuration used, the results, and the conclusions. Include links to relevant traces, data, and visualizations.

Optimize for fast iteration. Every experiment should have a quick test mode that checks the idea and the pipeline before the more statistically significant run. Keep the test mode representative enough to catch configuration and logic errors.

Export detailed traces and raw data for every meaningful run. Results should be usable for later interactive visualizations, not only for a final summary. Record the experiment version, inputs, parameters, and stopping conditions with the outputs.
