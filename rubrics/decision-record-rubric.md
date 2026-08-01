---
title: Decision Record Rubric
category: Rubric
description: Scores whether a decision record preserves the context, alternatives, rationale, consequences, and revisit conditions future readers need.
---

# Decision Record Rubric

Use this before accepting an ADR or non-technical decision record.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Decision clarity | Choice is absent or ambiguous | Choice is identifiable | One unambiguous decision statement names scope and status |
| Evidence boundary | Claims are unsupported | Main facts are supplied | Facts, assumptions, constraints, and unknowns are visibly separate |
| Alternatives | No alternatives recorded | Alternatives are named | Genuine alternatives use consistent criteria and rejection reasons |
| Rationale | Preference presented as proof | Some reasoning is visible | Decision criteria link evidence and trade-offs to the chosen option |
| Consequences | Only benefits appear | Some drawbacks appear | Positive, negative, operational, and follow-on consequences are explicit |
| Ownership and timing | No decision authority or date | Partial metadata | Owner, date, status, implementation responsibility, and review trigger are clear |
| Future usefulness | Record depends on current memory | Understandable now | A future maintainer can reconstruct why the choice was reasonable at the time |

## Pass standard

Decision clarity, evidence boundary, alternatives, and rationale must score at least **4**. No criterion may score below **3**.

## Red flags

- The record rewrites history to make the chosen option look inevitable.
- A rejected option is a straw man rather than a viable alternative.
- Consequences omit migration, lock-in, skills, cost, or reversal implications.
- The record contains facts or benchmarks not present in the source material.
