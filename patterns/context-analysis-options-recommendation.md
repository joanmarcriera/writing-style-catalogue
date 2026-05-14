---
title: Context / Analysis / Options / Recommendation
category: Pattern
description: A decision-support pattern for comparing options fairly before recommending one.
---

# Context / Analysis / Options / Recommendation

Use this pattern when a decision-maker needs to compare alternatives before approving a recommendation.

## Structure

```text
Context: [Why the decision is needed now]
Analysis: [Facts, constraints, evaluation criteria, and assumptions]
Options: [Two to four options assessed on the same basis]
Recommendation: [Preferred option, rationale, trade-offs, and decision requested]
```

## Good for

- Board papers
- Investment cases
- Procurement recommendations
- Architecture options papers
- Policy choices

## Prompt line

```text
Use Context / Analysis / Options / Recommendation. Assess all options against the same criteria before stating the recommendation. Include a do-nothing option unless instructed otherwise.
```

## Quality check

- Evaluation criteria are explicit.
- Options are real, not strawman choices.
- Financials use the same time horizon.
- The recommendation names trade-offs and residual risk.
