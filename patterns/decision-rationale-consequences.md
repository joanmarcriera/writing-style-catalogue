---
title: Decision / Rationale / Consequences
category: Pattern
description: A concise record pattern for documenting what was decided, why, and what follows.
---

# Decision / Rationale / Consequences

Use this pattern when the important thing is the record of why a choice was made.

## Structure

```text
Decision: [What has been decided, stated as a complete action sentence]
Rationale: [The decisive reasons, constraints, and rejected alternatives]
Consequences: [What becomes easier, harder, constrained, or required next]
```

## Good for

- Architecture Decision Records
- Policy decisions
- Governance minutes
- Product trade-off notes
- Technical debt acceptance records

## Prompt line

```text
Use Decision / Rationale / Consequences. Include at least two alternatives considered and one consequence or trade-off accepted.
```

## Quality check

- The decision is not just a topic.
- Rationale includes alternatives.
- Consequences include costs or constraints.
- The record can be understood by someone joining later.
