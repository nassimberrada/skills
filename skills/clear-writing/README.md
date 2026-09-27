# Clear writing

Clear Writing rewrites AI-sounding prose so it reads naturally, uses simple language, and preserves the original meaning. It is designed for editing prose, not for generating unsupported content.

## Core principles

- Preserve the source's facts, claims, qualifications, opinions, uncertainty, and instructions.
- Remove repetition, filler, staged framing, inflated significance, stock AI vocabulary, and decorative formatting.
- Prefer common words, concrete verbs, active voice, and one main idea per sentence and paragraph.
- Keep technical terms when they carry meaning, and use one term consistently for one concept.
- Make logical relationships explicit. Do not turn sequence into causation, correlation into causation, examples into proof, or possibilities into certainties.
- Keep conditions, limits, time ranges, and uncertainty next to the claims they qualify.
- Never invent names, numbers, dates, sources, opinions, or other details. Ask when a missing detail is necessary.

## Design

The skill uses a four-stage editing process:

1. Mark the source's claims and AI-writing patterns.
2. Draft a rewrite that preserves the claim ledger while removing low-value language.
3. Check the draft for lost or added facts, unclear references, weak transitions, and claims stronger than their evidence.
4. Return the final prose in a direct, readable form.

The pattern catalogue groups common problems into five classes: staging instead of stating, rhythm by rule, inflated or borrowed authority, formatting by rule, and leftovers from chat or drafting. Strong patterns justify an edit after one sighting. Weaker patterns, such as a single dash or repeated sentence opening, need context before they are changed.

The default response is only the final rewrite. In file mode, the skill changes prose while leaving code, data, frontmatter, commands, paths, and link targets unchanged.

## Sources and versioning

The pattern catalogue is based on [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup). Its technical-language guidance draws on [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/) and [Google Technical Writing](https://developers.google.com/tech-writing).

The detailed rules and examples are in [`SKILL.md`](SKILL.md). The current skill version is `1.1.1`.

## License

MIT
