---
title: Create Template from Example
category: Meta Prompt
description: Extracts a reusable template and prompt from a strong example document.
---

# Create Template from Example

Use when you have one strong example and want a reusable structure.

## Copy-paste prompt

```text
You are a senior technical writer and template designer.

TASK:
Analyse the example below and turn it into a reusable template and LLM prompt.

EXAMPLE:
[PASTE EXAMPLE]

INTENDED REUSE:
[Who will use the template and for what recurring task]

CONSTRAINTS:
[British English, tone, length, any required sections]

INSTRUCTIONS:
1. Identify the document type, audience, purpose, tone, and structure.
2. Extract the reusable section structure without copying unique facts.
3. Identify which parts are fixed wording and which parts should become placeholders.
4. Create a clean template with placeholders in square brackets.
5. Create a copy-paste LLM prompt that will generate a new document in the same style.
6. Include a short quality checklist.
7. Do not preserve confidential or identifying details from the example unless explicitly instructed.

OUTPUT FORMAT:
- Template diagnosis
- Reusable template
- Copy-paste generation prompt
- Quality checklist
```
