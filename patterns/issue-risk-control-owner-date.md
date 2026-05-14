---
title: Issue / Risk / Control / Owner / Date
category: Pattern
description: A compact risk and control pattern for audit, governance, and remediation tracking.
---

# Issue / Risk / Control / Owner / Date

Use this pattern when converting findings into an action-oriented control or remediation log.

## Structure

| Field | What to capture |
|---|---|
| Issue | The observed problem or gap |
| Risk | What could happen if it is not addressed |
| Control | The mitigation, control, or remediation action |
| Owner | One accountable role or team |
| Date | Target date and review date |

## Good for

- Audit action plans
- Risk registers
- Security control summaries
- Compliance remediation trackers
- Board risk updates

## Prompt line

```text
Convert the findings into an Issue / Risk / Control / Owner / Date table. Each issue must have one accountable owner, one target date, and a clear control or remediation action.
```

## Quality check

- Issues are observable facts.
- Risks describe consequences, not causes.
- Controls are testable.
- Owners are roles or teams, not vague groups.
- Dates include a review point.
