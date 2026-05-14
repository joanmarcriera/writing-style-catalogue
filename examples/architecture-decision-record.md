---
title: Architecture Decision Record Example
category: Example
---

# Architecture Decision Record Example

**ADR-0042: Use PostgreSQL for Primary Data Store**

**Status:** Accepted (Date: 15 June 2025)

**Context**
We needed to select a primary database for our new analytics platform. Requirements: structured data with complex joins, strong consistency, operational simplicity, cost-efficiency.

**Decision**
Use PostgreSQL as our primary data store.

**Rationale**

PostgreSQL meets our requirements:

1. **Strong consistency:** Analytics requires exact numbers; eventual consistency is unacceptable
2. **Complex queries:** Relational structure supports 4–6 table joins efficiently; MongoDB would require denormalisation
3. **Operational maturity:** Excellent backup, replication, and monitoring; our team has deep experience
4. **Cost:** Open-source; no vendor lock-in; cloud-hosted options are cost-effective

**Trade-offs**

**Pros:**
- Guaranteed consistency
- Strong query flexibility
- Mature operational tooling
- No vendor lock-in
- Team expertise

**Cons:**
- Schema must be designed upfront (less flexibility than documents)
- Scaling beyond 10TB requires read replicas or sharding
- Horizontal scaling more complex than NoSQL

**Consequences**

- Schema design must happen before development
- Scaling strategy required for future growth
- Team maintains PostgreSQL operational knowledge
- We gain consistency guarantees; analytics outputs are reliable

**Alternatives Considered**

**MongoDB:** Rejected – data consistency is a must-have; flexibility is nice-to-have.

**DynamoDB:** Rejected – query patterns require complex secondary indexes; cost scales with request volume.

**Snowflake:** Rejected – overkill for our write patterns; higher cost.

---

**Key principles shown:**
- Decision stated clearly upfront
- Context explains why it was needed
- Rationale is specific and reasoned
- Trade-offs acknowledged
- Consequences thought through
- Alternatives documented and rejected

This remains as reference for why choices were made.
