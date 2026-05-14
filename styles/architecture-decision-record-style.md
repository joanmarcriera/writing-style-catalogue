---
title: Architecture Decision Record Style
category: Specialist
aliases: [ADR, Technical Decision Record]
---

# Architecture Decision Record Style

## What This Style Is

Lightweight documentation of significant technical decisions. Records the decision, context, reasoning, and consequences for future reference. Helps teams understand why choices were made.

**Core principle**: Decision → Context → Consequence.

## When to Use It

- Major technology or framework choices
- Architectural patterns or approaches
- Trade-off decisions
- System design documentation
- Technical strategy records
- Learning from past decisions

## When NOT to Use It

- Quick technical decisions (use BLUF)
- Detailed implementation (use Technical Documentation)
- Strategic business decisions (use Board Paper)
- Policy decisions (use Policy Brief)

## Core Structure

```
[TITLE]
"ADR-NNN: [Decision Title]"

[STATUS]
Accepted, Proposed, or Superseded.

[CONTEXT]
Why this decision was needed.

[DECISION]
What we decided and why.

[CONSEQUENCES]
What changes because of this decision.

[ALTERNATIVES]
What we considered and why we rejected them.
```

## Copy-Paste Prompt Template

```
You are an architect. Write an ADR from:

DECISION:
[What technical decision were you making]

CONTEXT:
[Why was this decision needed]

OPTIONS CONSIDERED:
[What alternatives did you evaluate]

RATIONALE:
[Why did you choose this option]

TRADE-OFFS:
[What are the pros and cons]

CONSEQUENCES:
[What changes because of this decision]

INSTRUCTIONS:
1. Be concise; use bullet points
2. Record decision clearly
3. Explain context and rationale
4. Acknowledge trade-offs
5. Consider future consequences
6. Length: 1–2 pages

Output only the ADR. No preamble.
```

## Short Example

**ADR-0015: Use PostgreSQL Instead of MongoDB**

**Status**: Accepted (12 June 2025)

**Context**
We needed to choose a primary data store for our new analytics platform. Requirements: structured data, complex joins, strong consistency, operational simplicity.

**Decision**
We will use PostgreSQL as our primary data store.

**Rationale**
- Strong consistency: Analytics requires exact numbers; eventual consistency is unacceptable
- Complex queries: Our schema requires 4–6-table joins; PostgreSQL is optimized for relational queries
- Operational maturity: PostgreSQL has mature backup, replication, and monitoring tools
- Cost: PostgreSQL is open-source; we avoid vendor lock-in
- Team expertise: Our team has deep PostgreSQL experience; minimal ramp-up

**Trade-offs**

Pros:
- Guaranteed consistency
- Strong query flexibility
- Mature operational tooling
- No vendor lock-in

Cons:
- Less flexible schema evolution than document databases
- Requires upfront schema design
- Horizontal scaling is more complex than NoSQL options
- Cost of scaling larger datasets (vs. cloud-native NoSQL)

**Consequences**

- We must design the schema before implementation starts
- Scaling beyond 10TB will require read replicas or sharding strategy
- Team must maintain PostgreSQL operational knowledge
- Complex schema changes require migration planning
- We gain consistency guarantees; analytics outputs are reliable

**Alternatives Considered**

*MongoDB (Document DB)*
Rejected: Schema flexibility is nice-to-have; data consistency is must-have.

*DynamoDB (Managed NoSQL)*
Rejected: Query patterns require complex secondary indexes; cost scales with request volume.

*Snowflake (Cloud Data Warehouse)*
Rejected: Good for analytics but overkill for our write patterns; higher cost.

---

## Quality Checklist

- [ ] Decision is stated clearly
- [ ] Context explains why decision was needed
- [ ] Rationale is specific and reasoned
- [ ] Trade-offs are acknowledged
- [ ] Consequences are thought through
- [ ] Alternatives were considered
- [ ] Team can understand reasoning years later

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Decision unclear | Future team doesn't know what was chosen | State decision in one clear sentence |
| Context missing | No understanding of why | Explain the problem and constraints |
| No alternatives | Feels arbitrary | Show what else was considered |
| Ignores consequences | Future surprises | Think through downstream impact |
| Too detailed | ADR becomes implementation doc | Record decision and rationale; not how-to |

---

See [skills/create-adr.md](../skills/create-adr.md) for ADR generation skills.

See [examples/architecture-decision-record.md](../examples/architecture-decision-record.md) for a complete example.
