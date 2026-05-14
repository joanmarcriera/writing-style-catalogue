---
title: Decision Record Prompts
template_type: Decision Record
use_case: Document a significant business, operational, or organisational decision — including the context, options considered, rationale, and consequences — creating a permanent record that explains the "why" to future stakeholders.
audience: The decision-maker, the team that must implement the decision, and future stakeholders who need to understand it
output_format: Structured decision record with decision statement, context, alternatives, rationale, implications, and owners
---

# Decision Record Prompts

## Purpose

A decision record is distinct from an Architecture Decision Record (ADR): where an ADR focuses on a technical design choice, a decision record captures significant business, operational, or governance decisions. Use it when a decision is significant enough that someone — a new team member, an auditor, or a future leadership team — might legitimately ask: "Why did we decide that?" Examples include: deciding to exit a market, changing an organisational structure, selecting a vendor after a procurement exercise, adopting a new policy, or choosing not to pursue an opportunity. A good decision record is a permanent artefact — it does not get updated as circumstances change; if the decision is superseded, a new record is created.

## Copy-paste prompt

```
You are an expert at documenting business and organisational decisions. Write a clear, complete decision record that captures what was decided, why, and what the implications are — in a format that will be useful to someone reading it months or years from now.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant information: the decision made, the decision-maker, the options considered, the rationale, and the consequences):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 400–700 words]

FORMAT: [FORMAT — recommended: Decision / Decision Maker / Date / Context / Alternatives Considered / Rationale / Implications / Implementation Owners / Review Date]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. State the decision in a single, precise sentence at the top. The statement should be unambiguous — someone reading it in two years should know exactly what was decided without needing further context.
3. Record who made the decision and on what date. If the decision was made by a group or committee, name the body and the date of the meeting.
4. Context: explain concisely why this decision was needed. What problem was it solving? What would have happened without a decision? Why did it need to be made now?
5. Alternatives Considered: list the alternatives that were evaluated. Describe each briefly and explain why it was not chosen. Do not omit alternatives to make the decision look inevitable — if alternatives were genuinely considered, record them honestly.
6. Rationale: explain why this decision was chosen. This is the most important section. Give the actual reasons, not a post-hoc rationalisation. If the decision involved a genuine trade-off or uncertainty, say so.
7. Implications: describe what changes as a result of the decision — for the organisation, the team, customers, partners, or finances. Include both the expected positive outcomes and the costs or trade-offs accepted.
8. Implementation Owners: who is responsible for acting on this decision?
9. Review Date (optional): if the decision should be reviewed or revisited at a specific point in future, note it. If the decision is intended to be permanent, note that too.
10. Distinguish between facts (confirmed information at the time of the decision), assumptions (estimates or inferences that supported the decision), and the decision itself.
11. Do not retrospectively improve the rationale — record what was actually known and considered at the time.
12. Tone: [TONE — recommended: factual, clear, precise].
13. Length: [LENGTH].
14. Apply these constraints: [CONSTRAINTS].
15. Output only the decision record. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read the record. Examples: "the programme team and future team members who may join the cloud migration project", "the board audit committee", "all staff affected by the organisational restructure".
- `[PURPOSE]` — what decision is being recorded. Examples: "document the decision to select CloudBridge Ltd as the second delivery partner for Phase 2 of the cloud migration", "record the decision to exit the German market", "capture the board's decision to adopt a new expense policy".
- `[CONTEXT]` — background for the LLM. Examples: "this decision was made at the steering group meeting on 2 June 2026 following a procurement process that began in April", "the organisation has been reviewing its supplier base since Q1; this is the first formal decision in that process".
- `[INPUT]` — all relevant facts: the decision, who made it, when, the alternatives considered, the rationale, and the consequences.
- `[DESIRED_OUTCOME]` — what the record should do. Examples: "any team member joining the programme in 2027 can read this record and understand why CloudBridge was selected", "the audit committee can confirm that the procurement process was properly documented".
- `[TONE]` — "factual, clear, precise". Decision records are not narratives; they are permanent records.
- `[LENGTH]` — 400–700 words. Concise, but complete.
- `[FORMAT]` — use the recommended structure.
- `[CONSTRAINTS]` — examples: "do not include vendor pricing — this is commercially sensitive; refer to 'cost basis' only", "include the procurement reference number PROC-2026-014", "this record will be filed with the audit committee — use formal register".

## Example input

```
AUDIENCE: Cloud Migration Programme team, future team members, and the programme audit trail
PURPOSE: Document the decision to engage CloudBridge Ltd as a second delivery partner for Phase 2 of the Azure cloud migration programme
CONTEXT: The Cloud Migration Steering Group made this decision on 2 June 2026. The background: the primary delivery partner, Nexus Solutions, confirmed on 10 May 2026 that it could not resource Phase 2 from July 2026. Without a second partner, Phase 2 would slip by 6–8 weeks, moving the go-live from October 2026 to February 2027.
INPUT:
  Decision: Engage CloudBridge Ltd as second delivery partner for Phase 2 of the Azure cloud migration programme.
  Decision maker: Cloud Migration Programme Steering Group (chaired by CIO), meeting of 2 June 2026.

  Alternatives considered:
  1. Continue with Nexus Solutions only and accept the 6–8 week slip — rejected because it moves the go-live to February 2027, delaying £1.8M annual savings by one quarter and creating uncertainty around the FCA DORA compliance deadline.
  2. Engage a different second partner (two others were assessed: TechForce Consulting and Azure Partners Ltd) — TechForce was assessed as not having sufficient Entra/Azure migration experience for the workload profile; Azure Partners Ltd is at capacity until September 2026.
  3. Reduce Phase 2 scope to what Nexus can deliver — rejected because it would require descoping 20 workloads, which cannot be migrated later without a further programme and cost, and would not resolve the data centre exit requirement.

  Rationale for CloudBridge: CloudBridge has Azure and Entra migration accreditation; its team profile matches the Phase 2 workload requirements; availability confirmed from July; cost (£180k) falls within programme contingency (£220k). Legal review of the contract was satisfactory.

  Implications:
  - Phase 2 delivery proceeds on the original October 2026 timeline
  - Programme cost increases by £180k (within contingency; total programme cost remains within the approved £3.2M envelope)
  - Two delivery partners now require active co-ordination — the Programme Manager will manage interface between Nexus and CloudBridge

  Implementation owner: Programme Manager
  Review: Decision is final; no scheduled review. If CloudBridge performance is unsatisfactory at the 6-week review (mid-August 2026), the Steering Group will convene an emergency session.
DESIRED_OUTCOME: Any team member or auditor can read this record and understand why CloudBridge was selected and why the alternatives were rejected.
TONE: Factual, precise, formal enough for an audit trail
LENGTH: 500–700 words
CONSTRAINTS: Procurement reference: PROC-2026-014. Do not include specific financial figures for the alternatives — refer to 'cost basis' only for CloudBridge. Include the date of the steering group meeting.
```

## Example output

---

## Decision Record: Engagement of CloudBridge Ltd as Second Delivery Partner

**Reference:** PROC-2026-014
**Decision:** Engage CloudBridge Ltd as second delivery partner for Phase 2 of the Azure cloud migration programme.
**Decision Maker:** Cloud Migration Programme Steering Group (Chair: Chief Information Officer)
**Date of Decision:** 2 June 2026
**Status:** Final

---

### Context

The primary delivery partner for the Azure cloud migration programme, Nexus Solutions, confirmed on 10 May 2026 that it could not resource Phase 2 of the programme from July 2026. Phase 2 covers the migration of 74 workloads and is scheduled for completion in October 2026. Without additional delivery resource, Phase 2 would slip by six to eight weeks, moving the programme go-live to February 2027 at the earliest. This would delay the realisation of annual operating savings and create uncertainty around the organisation's ability to meet its FCA DORA-aligned compliance requirements by Q4 2026.

A procurement exercise was conducted between 10 May and 30 May 2026 to identify a qualified second delivery partner.

---

### Alternatives Considered

**1. Continue with Nexus Solutions only; accept 6–8 week slip**
This would move go-live to February 2027 and delay annual savings by one quarter. It would also increase uncertainty around the FCA compliance deadline. Rejected.

**2. Engage TechForce Consulting**
Assessed and rejected. TechForce does not have sufficient Microsoft Entra and Azure migration experience for the workload profile in Phase 2.

**3. Engage Azure Partners Ltd**
Assessed and rejected. Azure Partners Ltd confirmed it is at capacity until September 2026 and cannot begin engagement in time to meet the Phase 2 schedule.

**4. Reduce Phase 2 scope to what Nexus Solutions can deliver**
Descoping 20 workloads would defer their migration to a future programme, incurring additional cost and complexity, and would not resolve the requirement to exit the primary data centre by December 2027. Rejected.

---

### Rationale

CloudBridge Ltd was selected on the following grounds:

- Microsoft Azure and Entra ID migration accreditation confirmed
- Team profile (engineers and architects) assessed as a good match for the Phase 2 workload complexity
- Availability confirmed from July 2026 — consistent with the programme schedule
- Cost is within the programme contingency envelope; total programme cost remains within the approved budget
- Legal review of the contract was satisfactory; no material issues identified

*Assumption: the CloudBridge availability commitment is based on a contract signed on 2 June 2026. Capacity availability is subject to CloudBridge not taking on conflicting engagements during the Phase 2 period. This risk will be managed through the programme's risk register.*

---

### Implications

- Phase 2 delivery proceeds on the original October 2026 schedule
- Programme cost increases within the approved contingency; the total programme cost remains within the £3.2M envelope approved by the board in June 2026
- The Programme Manager will manage active co-ordination between Nexus Solutions and CloudBridge Ltd; a clear workstream split will be documented in the Phase 2 delivery plan

---

### Implementation Owner

Programme Manager (supported by the Head of Infrastructure)

---

### Review

This decision is final. CloudBridge performance will be reviewed at the six-week programme checkpoint in mid-August 2026. If performance is unsatisfactory at that point, the Steering Group will convene an emergency session.

---

## Review checklist

- [ ] Decision is stated in a single, precise, unambiguous sentence
- [ ] Decision maker and date are recorded explicitly
- [ ] Context explains why the decision was needed — the reader can understand the problem without prior knowledge
- [ ] All alternatives considered are documented with reasons for rejection — alternatives are not dismissed superficially
- [ ] Rationale explains why this option was chosen (actual reasons, not post-hoc justification)
- [ ] Assumptions are explicitly labelled
- [ ] Implications cover both positive outcomes and costs or trade-offs accepted
- [ ] Implementation owner is named
- [ ] Review date or permanence is noted
- [ ] British English used throughout
- [ ] Length is within 400–700 words

---

Similar to ADR but for business or organisational decisions, not just technical choices. See [architecture-prompts.md](./architecture-prompts.md) for the ADR variant.
