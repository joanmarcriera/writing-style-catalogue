---
title: Build Style Guide from Samples
category: Meta Prompt
description: Extracts a concise house style guide from sample writing.
---

# Build Style Guide from Samples

Use when you have examples of a person's or organisation's writing and need guidance that an LLM can follow.

## Copy-paste prompt

```text
You are a senior editor building a practical house style guide from writing samples.

TASK:
Analyse the samples below and produce a concise style guide that can be used to write new material in the same style.

SAMPLES:
[PASTE 2-5 REPRESENTATIVE SAMPLES]

INTENDED FUTURE OUTPUTS:
[e.g. executive emails, board papers, LinkedIn posts, tax notes, technical documentation]

AUDIENCE:
[Who the future outputs will be for]

CONSTRAINTS:
[British English, professional register, no copyrighted excerpts in the guide]

INSTRUCTIONS:
1. Identify recurring structure, tone, sentence length, vocabulary, level of formality, and use of evidence.
2. Distinguish style features from one-off content features.
3. Do not quote long passages from the samples. Paraphrase style rules.
4. Produce practical "Do" and "Do not" rules.
5. Include a short prompt that applies the style to new input.
6. Include a review checklist.

OUTPUT FORMAT:
- Style summary
- Structural rules
- Tone and vocabulary rules
- Evidence and specificity rules
- Do / Do not table
- Copy-paste style prompt
- Review checklist
```
