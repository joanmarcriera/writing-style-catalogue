---
title: Professional Prompt Bundle Standard
category: Reference
description: The source, prompt, output, and review contract used by every worked example in the catalogue.
---

# Professional Prompt Bundle Standard

A professional prompt is not judged by fluency. It is judged by whether a qualified reader can trace the output back to supplied evidence, understand what the model was asked to do, and stop the draft when a critical review gate fails.

## Required metadata

Every worked example in `examples/` must include these frontmatter fields:

```yaml
bundle_id: stable-kebab-case-id
artefact: Human-readable artefact name
audience: Specific professional reader or decision-maker
scenario: labelled-composite | verified-public-project
style_path: styles/example-style.md
pattern_path: patterns/example-pattern.md
prompt_path: prompt-templates/example-prompts.md
skill_path: skills/create-example.md
rubric_path: rubrics/example-rubric.md
```

`skill_path` is optional when the artefact does not require a separate production process. Every other field is required, and every path must resolve to a tracked file.

## Required sections

Each bundle uses these second-level headings exactly:

1. `## Professional context`
2. `## Source packet`
3. `## Completed prompt`
4. `## Output excerpt`
5. `## Review scorecard`
6. `## Human review before use`
7. `## Reuse this bundle`

The generator treats the first six sections as the public interactive bundle. The final section provides normal Markdown links for repository readers.

## Source packet standard

The source packet is the evidence boundary. It must:

- identify whether the scenario is a labelled composite or verified public project;
- supply every name, date, number, decision, constraint, caveat, and quotation used later;
- distinguish confirmed facts from assumptions and unresolved questions;
- omit confidential or personal information;
- date and link any high-stakes external source that the output relies on.

## Completed prompt standard

The filled prompt must specify:

- professional role, audience, purpose, and desired decision or action;
- the complete source material and an instruction to use no facts outside it;
- required structure, length, register, and output-only contract;
- how to label facts, assumptions, inferences, caveats, and recommendations;
- what to do when critical information is missing: stop and return a `MISSING INFORMATION` list rather than inventing a usable-looking draft;
- the relevant rubric and any critical criteria that must pass.

## Output excerpt standard

The output must be traceable to the source packet. It must not silently strengthen evidence, remove uncertainty, or imply that an illustrative excerpt is a complete production artefact.

## Review scorecard standard

Use a four-column Markdown table:

```markdown
| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Factual integrity | 5 | Every figure maps to the source packet. | Pass |
```

Scores use the linked rubric's 1–5 scale. `Gate` is `Pass`, `Revise`, or `Human check`. A bundle cannot claim to pass when a critical criterion scores below 4 or any criterion scores below 3.

## Human review standard

State the checks that remain outside the model's authority: source verification, legal or tax review, operational command testing, approval authority, confidentiality, accessibility, or publication sign-off.

The final rule is simple: the model finishing is not a release event. The relevant human reviewer must accept the evidence, caveats, and rubric result.
