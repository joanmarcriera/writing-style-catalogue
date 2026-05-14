---
title: Patterns
category: Patterns
description: Reusable section-level structures for professional writing, prompts, and document design.
---

# Patterns

Patterns are smaller than styles. A style governs the whole document; a pattern gives one section a reliable shape.

Use patterns when a prompt needs a clear structure or when a draft has the right content but poor organisation.

## Pattern library

| Pattern | Best for |
|---|---|
| [BLUF](bluf.md) | Approval emails, short recommendations, urgent updates |
| [What / So What / Now What](what-so-what-now-what.md) | Updates, retrospectives, executive summaries |
| [Situation / Complication / Question / Answer](situation-complication-question-answer.md) | Strategy memos, consulting narratives, business cases |
| [Problem / Impact / Recommendation / Next Steps](problem-impact-recommendation-next-steps.md) | Escalations, change proposals, operational briefings |
| [Context / Analysis / Options / Recommendation](context-analysis-options-recommendation.md) | Decision papers and options appraisals |
| [Issue / Risk / Control / Owner / Date](issue-risk-control-owner-date.md) | Risk logs, audit actions, control summaries |
| [Decision / Rationale / Consequences](decision-rationale-consequences.md) | ADRs, policy decisions, architecture choices |
| [Objective / Scope / Procedure / Exceptions](objective-scope-procedure-exceptions.md) | SOPs, runbooks, policies, operating procedures |

## How to use a pattern in a prompt

Add a line like this:

```text
Structure the output using the Context / Analysis / Options / Recommendation pattern. Keep each section clearly headed. Separate confirmed facts from assumptions.
```

For whole-document guidance, use [styles/](../styles/) first, then apply one of these patterns to the section that needs structure.
