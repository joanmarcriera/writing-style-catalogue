---
title: LLM Output Quality Rubric
category: Rubric
description: Scores whether a generated draft is safe, useful, and ready for human editing.
---

# LLM Output Quality Rubric

Use this after generating any draft with an LLM.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Instruction fit | Ignores key constraints | Follows most instructions | Meets role, audience, purpose, format, tone, and constraints |
| Factual integrity | Adds or changes facts | Mostly preserves facts | Preserves supplied facts and flags missing or assumed information |
| Specificity | Generic advice | Some concrete detail | Uses the supplied context, numbers, names, and constraints accurately |
| Structure | Rambling | Adequate headings | Clear structure matched to the artefact and reader |
| Professional tone | AI-sounding or inflated | Acceptable but bland | Plain, precise, British English with no filler |
| Risk awareness | Omits risks | Mentions risks | Separates facts, assumptions, risks, caveats, and recommendations |
| Usefulness | Needs full rewrite | Useful first draft | Copy-editable, artefact-ready, and easy to review |

## Pass standard

For professional use, require no score below **3** and rewrite any criterion scoring **1 or 2** before sharing.

## Red flags

- Fake citations, URLs, cases, statistics, or product claims.
- Confident legal, tax, medical, or financial advice without caveats and verification.
- Polished prose that does not answer the actual question.
- Missing constraints that the prompt explicitly required.
