---
title: Architecture Decision Record — Primary Data Store
category: Example
description: A worked ADR bundle that traces a database decision from supplied constraints to a reviewable record.
bundle_id: architecture-decision-record
artefact: Architecture decision record
audience: Software engineers, platform operators, architects, and future maintainers
scenario: labelled-composite
style_path: styles/architecture-decision-record-style.md
pattern_path: patterns/decision-rationale-consequences.md
prompt_path: prompt-templates/architecture-prompts.md
skill_path: skills/create-adr.md
rubric_path: rubrics/decision-record-rubric.md
---

# Architecture Decision Record — Primary Data Store

## Professional context

A platform architecture group must record why a new analytics service will use PostgreSQL. The record must remain useful after the original team has moved on and must not turn estimates into proven limits.

## Source packet

```text
SCENARIO: Labelled composite; no real company or benchmark is represented.
DECISION DATE: 15 June 2026
STATUS: Accepted
SYSTEM: New operational analytics service
CONFIRMED REQUIREMENTS: transactional writes; strong consistency; relational queries joining 4–6 entities; managed backup and point-in-time recovery; EU region; team already operates PostgreSQL.
OPTIONS ASSESSED: managed PostgreSQL, MongoDB Atlas, DynamoDB.
DECISION CRITERIA: consistency, query fit, operating capability, reversible migration path, five-year cost envelope.
CONFIRMED FINDING: PostgreSQL meets every mandatory requirement. MongoDB and DynamoDB would require redesign of the current relational query model.
ASSUMPTION: Dataset remains below 8 TB during the first three years.
UNKNOWN: Validated workload benchmark at peak ingestion rate.
CONSEQUENCE: Benchmarking is required before production approval; scaling design is reviewed at 5 TB or 18 months, whichever comes first.
```

## Completed prompt

```text
You are a principal architect preparing ADR-0042 for engineers, platform operators, architects, and future maintainers. Write a concise architecture decision record whose purpose is to preserve why managed PostgreSQL was selected for the operational analytics service.

Use only the SOURCE PACKET below. Do not invent benchmarks, prices, service capabilities, dates, requirements, or rejection reasons. Separate confirmed requirements, the stated assumption, and the unresolved benchmark. If any information essential to the decision is absent or contradictory, stop and return a heading named MISSING INFORMATION with a precise list; do not produce the ADR.

Structure the record as: Title; Status and date; Context; Decision; Decision criteria; Alternatives considered; Rationale; Positive consequences; Negative consequences and risks; Validation and review triggers. Explain that the 8 TB figure is an assumption, not a proven product limit. Do not claim that an alternative is technically incapable when the source only says it requires redesign. Use neutral, durable language and British English. Keep the record between 550 and 750 words. Output only the ADR.

Before finalising, check it against the Decision Record Rubric: decision clarity, evidence boundary, genuine alternatives, rationale, consequences, ownership/timing, and future usefulness. Preserve every caveat from the source.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
ADR-0042: Use managed PostgreSQL for the operational analytics service
Status: Accepted — 15 June 2026

Decision
The service will use managed PostgreSQL as its primary transactional data store.

Rationale
PostgreSQL meets the mandatory consistency, relational-query, recovery, regional-hosting, and team-operability requirements. MongoDB Atlas and DynamoDB remain viable technologies, but adopting either would require redesign of the current 4–6-entity relational query model. No workload benchmark has yet validated peak ingestion performance.

Consequences and review triggers
The team can reuse existing PostgreSQL operating capability and retains a conventional migration path. It must complete peak-load benchmarking before production approval. The assumption that data remains below 8 TB for three years will be reviewed when storage reaches 5 TB or after 18 months, whichever occurs first.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Decision clarity | 5 | Technology, scope, status, and date are explicit. | Pass |
| Evidence boundary | 5 | The capacity figure and missing benchmark remain labelled. | Pass |
| Alternatives | 4 | Viable alternatives and the actual redesign trade-off are retained. | Pass |
| Consequences | 5 | Benefits, required benchmark, and review triggers are actionable. | Pass |
| Future usefulness | 4 | A later maintainer can reconstruct the decision from the record. | Pass |

## Human review before use

- The service owner must confirm that the source packet reflects the approved architecture assessment.
- Platform engineering must run and retain the peak-load benchmark before production approval.
- The decision owner must confirm the review thresholds and record any superseding ADR.

## Reuse this bundle

- [Architecture Decision Record Style](../styles/architecture-decision-record-style.md)
- [Decision / Rationale / Consequences Pattern](../patterns/decision-rationale-consequences.md)
- [Architecture Prompts](../prompt-templates/architecture-prompts.md)
- [Create ADR Skill](../skills/create-adr.md)
- [Decision Record Rubric](../rubrics/decision-record-rubric.md)
