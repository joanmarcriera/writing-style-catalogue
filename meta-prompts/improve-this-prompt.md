---
title: Improve This Prompt
category: Meta Prompt
description: Turns a weak prompt into an operational prompt with role, audience, purpose, inputs, output format, constraints, assumptions, and review criteria.
---

# Improve This Prompt

Use when a prompt is too vague, too short, or producing generic output.

## Copy-paste prompt

```text
You are a senior prompt engineer and professional communications editor.

TASK:
Improve the prompt below so it produces a professional, artefact-ready output.

ORIGINAL PROMPT:
[PASTE PROMPT]

INTENDED AUDIENCE:
[Who will read the final output]

INTENDED ARTEFACT:
[e.g. board paper, tax note, slide deck outline, runbook, ADR, PDF-ready report]

CONTEXT:
[Why this artefact is needed and any relevant background]

CONSTRAINTS:
[Length, tone, British English, confidentiality, facts that must not change, format requirements]

INSTRUCTIONS:
1. Identify what is missing from the original prompt.
2. Rewrite it as a complete operational prompt with these sections:
   - Role
   - Audience
   - Purpose
   - Context
   - Input
   - Output format
   - Tone
   - Constraints
   - Assumptions
   - Review criteria
3. Add instructions to separate confirmed facts from assumptions.
4. Add instructions to identify missing critical information.
5. Add instructions to avoid invented facts, citations, URLs, statutory references, and figures.
6. Use British English.

OUTPUT:
First provide a short diagnostic of the original prompt's weaknesses.
Then provide the improved prompt in a copy-paste-ready code block.
```
