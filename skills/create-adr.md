---
title: Create ADR
category: Documentation
---

# Skill: Create ADR (Architecture Decision Record)

## What This Skill Does

Documents significant technical decisions for future reference and team alignment.

## When to Use It

- Major technology or framework choices
- Architectural pattern decisions
- Trade-off documentation
- Knowledge preservation for future teams

## Copy-Paste Prompt

```
You are an architect. Write an Architecture Decision Record for:

DECISION:
[What technical decision]

CONTEXT:
[Why this decision was needed]

OPTIONS:
[2–3 alternatives evaluated]

DECISION:
[Which option and why]

CONSEQUENCES:
[What changes because of this]

INSTRUCTIONS:
1. State decision clearly
2. Explain context and constraints
3. Show alternatives were considered
4. Justify the choice
5. Note implications
6. Keep to 1–2 pages

Output only the ADR. No preamble.
```

## Structure

- Title: ADR-[Number]: [Decision]
- Status: Accepted/Proposed/Superseded
- Context
- Decision
- Rationale
- Trade-offs
- Consequences

---

See [styles/architecture-decision-record-style.md](../styles/architecture-decision-record-style.md) for detailed ADR style.
