---
title: LLM Prompting Principles
category: Reference
---

# LLM Prompting Principles

How to write effective prompts for Claude and other LLMs.

## Principle 1: Be Specific

**Bad:** "Write about cloud migration"

**Good:** "Write a 2-page executive briefing on cloud migration ROI for a financial services company. Include cost comparison, timeline, and risks."

More specificity = Better output.

## Principle 2: Provide Context

**Without context:** "Create a sales email"

**With context:** "Create a sales email to a manufacturing company's operations manager. Emphasise cost savings and operational simplification. We're selling a supply chain software. The prospect looked at our pricing page yesterday."

## Principle 3: Show Examples

Provide examples of style, tone, or output format you want.

```
"Write in this style:
'Revenue was up 23%. Here's why...'"
```

## Principle 4: Define Output Format

Specify exactly what you want back.

**Vague:** "Summarise this document"

**Specific:** "Summarise this document in 3 bullet points, each under 20 words. Use active voice."

## Principle 5: Specify Audience

Different audiences need different language.

```
"Write for:
- Audience: C-Suite executives
- Knowledge level: Non-technical
- Tone: Confident but realistic"
```

## Principle 6: Chain Steps

For complex tasks, break into steps.

```
"Step 1: Extract key metrics from the document
Step 2: Calculate year-over-year change
Step 3: Format as executive summary"
```

## Principle 7: Set Constraints

Define what you DON'T want.

```
"Don't:
- Use jargon without explanation
- Include external citations
- Go over 300 words"
```

---

See [prompt-templates/](../prompt-templates/) for copy-paste templates following these principles.
