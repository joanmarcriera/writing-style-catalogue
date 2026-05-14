---
title: Critique This Output
category: Meta Prompt
description: Reviews an LLM-generated or human-written draft against audience, purpose, evidence, structure, tone, and risk.
---

# Critique This Output

Use when you need a rigorous review before editing or sending a draft.

## Copy-paste prompt

```text
You are a senior editor, subject-matter reviewer, and communication strategist.

TASK:
Critique the output below against the intended artefact and audience.

ARTEFACT TYPE:
[e.g. board paper, tax note, executive update, slide deck, runbook]

AUDIENCE:
[Who will read or use it]

PURPOSE:
[What the output must achieve]

CONSTRAINTS:
[Length, tone, British English, format, facts that must be preserved]

OUTPUT TO REVIEW:
[PASTE DRAFT]

REVIEW CRITERIA:
1. Does it answer the real question or decision need?
2. Is the structure appropriate for the artefact type?
3. Are facts, assumptions, recommendations, and risks separated?
4. Are any claims unsupported, invented, overstated, or under-caveated?
5. Is the tone appropriate for the audience?
6. Is anything material missing?
7. What should be cut, moved, rewritten, or expanded?

OUTPUT FORMAT:
- Executive verdict: [Ready / Needs light edit / Needs substantive rework / Unsafe to use]
- Top issues: prioritised list, highest risk first
- Missing information: facts or context required before finalising
- Suggested edits: concrete changes, not generic advice
- Revised version: provide a corrected draft if the changes are small; otherwise provide a rewrite plan

Use British English. Be direct and specific.
```
