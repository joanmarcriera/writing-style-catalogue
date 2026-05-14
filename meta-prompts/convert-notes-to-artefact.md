---
title: Convert Notes to Artefact
category: Meta Prompt
description: Converts messy notes into a selected professional artefact with explicit assumptions and missing information.
---

# Convert Notes to Artefact

Use when you have rough notes and know the document type you need.

## Copy-paste prompt

```text
You are a senior professional writer and document strategist.

TASK:
Convert the notes below into the specified artefact.

ARTEFACT TYPE:
[e.g. board paper, tax technical note, CIO briefing, slide deck outline, runbook, ADR, PDF-ready report]

AUDIENCE:
[Who will read/use it]

PURPOSE:
[Decision, advice, update, instruction, approval, record]

CONTEXT:
[Background and why this is needed now]

NOTES:
[PASTE NOTES]

OUTPUT FORMAT:
[Exact format required: headings, tables, slide fields, numbered sections, etc.]

TONE:
[e.g. formal and measured, technical and precise, direct and executive]

CONSTRAINTS:
[Length, British English, facts to preserve, confidentiality, disclaimers, no invented data]

INSTRUCTIONS:
1. Use only the information in the notes. Do not invent facts, figures, citations, URLs, laws, names, or dates.
2. Separate confirmed facts from assumptions.
3. If a critical fact is missing, include a short "Missing critical information" section before the draft unless the artefact must not include it.
4. If the artefact requires options, risks, owners, dates, or financials and they are absent, flag the gap clearly.
5. Produce an artefact-ready draft in British English.
6. End with a short review checklist tailored to the artefact.

OUTPUT ONLY:
1. Missing critical information
2. Assumptions made
3. Draft artefact
4. Review checklist
```
