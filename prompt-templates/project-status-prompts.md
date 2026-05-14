---
title: Project Status Prompts
template_type: Project Status Report
use_case: Write a concise, honest project status update that gives stakeholders a clear picture of where the project stands, what is at risk, and what action is needed.
audience: Project steering group, programme sponsor, senior leadership, or programme management office
output_format: One-page structured status report with RAG status, accomplishments, blockers, next steps, and any escalation needed
---

# Project Status Prompts

## Purpose

A project status report exists to give stakeholders the truth about a project, quickly. It should take no more than five minutes to read and must answer three questions: are we on track, what is at risk, and what do we need from you? Use this template for regular reporting cycles (weekly, fortnightly, monthly) or for ad hoc escalation updates when something significant has changed. The output should be honest — a status report that says everything is green when it is not destroys trust the moment the problem surfaces. Use the RAG (Red / Amber / Green) convention for status indicators, and be specific about blockers: name them, quantify their impact, and say what mitigation is in place.

## Copy-paste prompt

```
You are a project manager writing a clear, honest status report for a project steering committee. Write a concise, structured project status update that gives stakeholders an accurate picture of progress, risks, and required actions.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant information: accomplishments, metrics, blockers, risks, financials, and any escalations needed):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one page; two pages maximum]

FORMAT: [FORMAT — recommended: summary header / overall RAG status with one-sentence rationale / accomplishments / blockers and risks / next period priorities / escalations or decisions needed]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a summary header: project name, reporting period, overall RAG status, and one sentence explaining the status.
3. Use RAG status (Red / Amber / Green) for the overall project and for each key workstream or delivery area. Define: Green = on track; Amber = at risk but manageable; Red = off track, requires intervention.
4. Accomplishments: list what was completed in this period. Be specific — "completed user acceptance testing for Phase 1 (47 of 50 test cases passed)" is useful; "good progress on testing" is not.
5. Blockers and risks: list each blocker or risk with: (a) a one-line description, (b) the likely impact if not resolved (time delay, cost overrun, quality risk), and (c) the mitigation or resolution in progress. Do not list risks without at least a partial mitigation.
6. Financial position: include budget vs. actual if provided. State clearly whether spend is within the approved contingency. Do not omit a budget variance if one exists.
7. Next period priorities: list the three to five most important things happening in the next reporting period.
8. Escalations: if any issue requires a decision from the steering group or sponsor, state it explicitly under a separate "Decision Required" heading. Do not bury escalation needs in the body of the report.
9. Distinguish between facts (confirmed data), assumptions (estimates based on current trajectory), and recommendations (proposed actions).
10. Do not pad. One page is the target. Every sentence must earn its place.
11. Tone: [TONE — recommended: honest, direct, professional. Do not write a status report that understates problems to avoid difficult conversations].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the status report. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read the report. Examples: "Cloud Migration Programme Steering Group (CIO, CFO, Head of Infrastructure)", "Programme Sponsor and PMO", "Board audit committee (monthly programme update)".
- `[PURPOSE]` — what this report covers. Examples: "weekly status update for the Azure cloud migration programme — Week 18", "ad hoc escalation report following the discovery of a significant scope gap in Phase 2".
- `[CONTEXT]` — background for the LLM. Examples: "the programme is a 24-month Azure cloud migration; we are in Month 6, Phase 1 pilot; the steering group meets fortnightly", "this is an escalation report — the project was Green last week but a critical dependency has just been identified as at risk".
- `[INPUT]` — the raw data: what happened this period, what metrics exist, what is blocked, what is coming next, and any budget or timeline variance information.
- `[DESIRED_OUTCOME]` — what the report should achieve. Examples: "the steering group has a clear picture of the Amber status and knows what decision is needed from them", "the sponsor approves the revised timeline before Friday".
- `[TONE]` — "honest, direct, professional". Status reports are not sales documents. If the project is at risk, say so.
- `[LENGTH]` — one page is the target; two pages for complex programmes with multiple workstreams.
- `[FORMAT]` — use the recommended structure; add a workstream table if the programme has multiple parallel streams.
- `[CONSTRAINTS]` — examples: "follow the organisation's RAG reporting standard (see PMO-STD-003)", "include project code PRJ-2026-007", "do not include individual staff names — reference roles only".

## Example input

```
AUDIENCE: Cloud Migration Programme Steering Group — CIO, CFO, Head of Infrastructure, Head of Security (meets fortnightly)
PURPOSE: Fortnightly status update — Reporting Period: 29 April – 13 May 2026 (Week 18 of 96)
CONTEXT: 24-month Azure cloud migration programme. Phase 1 (pilot — 38 workloads) is complete and signed off. Phase 2 (main migration — 74 workloads) began on 1 May. The overall programme target is October 2026 go-live for Phase 2.
INPUT:
  Overall status: AMBER
  Reason for Amber: Phase 2 primary delivery partner (Nexus Solutions) has confirmed capacity constraints from July; without a second delivery partner, Phase 2 will slip by 6–8 weeks (go-live moves to February 2027).

  Accomplishments (this period):
  - Phase 1 sign-off completed and accepted by steering group on 29 April
  - Phase 2 mobilisation complete; first 12 workloads in assessment
  - Azure security baseline passed independent audit (zero critical findings)
  - HR system integration scoping for IAM complete; data cleanse plan agreed

  Blockers:
  1. Nexus Solutions capacity from July — programme team has identified CloudBridge Ltd as a qualified second delivery partner. Proposal received; legal review in progress. Decision needed by 20 June.
  2. Legacy system decommission for 6 workloads delayed — legal review of data retention obligations for the legacy CRM data is taking longer than expected. Current estimate: 2-week delay in starting Phase 2 migration for these 6 workloads. No impact on overall programme timeline yet, but will become one if not resolved by 31 May.

  Financial position:
  - Q1 spend: £610k against £600k budget (£10k over; within contingency)
  - Full-year forecast: £1.85M against £1.8M budget (£50k variance; within contingency of £220k)

  Next period priorities:
  - Progress CloudBridge legal review to completion by 20 June
  - Resolve legal data retention question for legacy CRM by 31 May
  - Complete assessment of next 25 Phase 2 workloads
  - Begin IAM pilot deployment (50 users)

  Decision needed: Steering group to approve engagement of CloudBridge Ltd as second delivery partner at the next meeting (2 June).
DESIRED_OUTCOME: The steering group has a clear picture of the Amber status and approves the CloudBridge engagement at the 2 June meeting.
TONE: Direct, honest, professional
LENGTH: One page
CONSTRAINTS: Project code PRJ-2026-007. Reference role titles, not individual names. Include the decision required prominently.
```

## Example output

---

## Cloud Migration Programme — Status Report
**Project:** Azure Cloud Migration (PRJ-2026-007)
**Reporting period:** 29 April – 13 May 2026 (Week 18 of 96)
**Overall status:** 🟡 **AMBER** — Phase 2 delivery partner capacity constraint requires a steering group decision by 2 June to protect the October 2026 go-live.

---

### Accomplishments (this period)

- Phase 1 pilot (38 workloads) signed off and accepted — ahead of the original sign-off date
- Phase 2 mobilised; first 12 workloads in assessment
- Azure security baseline passed independent audit — zero critical findings
- IAM HR system integration scoped; data cleanse plan agreed with HR

---

### Blockers and risks

| # | Blocker / Risk | Impact if unresolved | Status / Mitigation |
|---|---------------|---------------------|---------------------|
| 1 | Primary delivery partner (Nexus Solutions) at capacity from July | Phase 2 slips 6–8 weeks; go-live moves from October 2026 to February 2027 | Second partner (CloudBridge Ltd) identified and assessed; proposal received; legal review in progress. **Decision required at 2 June steering group.** |
| 2 | Legal data retention review for 6 legacy CRM workloads delayed | 2-week delay to Phase 2 start for these workloads; no programme-level impact yet, but critical path by 31 May | Head of Legal engaged; resolution expected by 28 May. Programme team monitoring daily. |

---

### Financial position

| | Budget | Actual / Forecast | Variance | Status |
|--|--------|------------------|---------|--------|
| Q1 spend | £600k | £610k | +£10k | Within contingency |
| Full-year forecast | £1.8M | £1.85M | +£50k | Within contingency (£220k available) |

---

### Next period priorities (14–27 May)

1. Progress CloudBridge legal review to completion — target: contract ready for steering group approval on 2 June
2. Resolve legacy CRM data retention question with Legal by 31 May
3. Complete assessment of next 25 Phase 2 workloads
4. Begin IAM pilot deployment (50 users, target: 19 May)

---

### ⚠ Decision Required — Steering Group Action (2 June)

**Issue:** Nexus Solutions cannot resource Phase 2 from July. Without a second delivery partner, Phase 2 will miss the October 2026 go-live by 6–8 weeks.

**Request:** Approve engagement of CloudBridge Ltd as second delivery partner. Estimated additional cost: £180k (within existing programme contingency). Legal review expected complete by 30 May; contract can be signed immediately after steering group approval.

**If approved:** Programme remains on track for October 2026 go-live.
**If deferred:** Phase 2 go-live moves to February 2027 at the latest.

---

## Review checklist

- [ ] Overall RAG status is stated with a single-sentence rationale
- [ ] Accomplishments are specific — not vague ("completed X of Y", not "good progress")
- [ ] Each blocker includes: description, impact, and mitigation status
- [ ] Budget variance is included and clearly related to the contingency envelope
- [ ] Next period priorities are listed and specific
- [ ] Decision required is prominent and clearly actionable
- [ ] Facts, assumptions, and recommendations are distinguishable
- [ ] No individual names used — roles only (per constraints)
- [ ] British English used throughout
- [ ] Length is within the one-to-two-page target

---

Use [styles/axios-smart-brevity.md](../styles/axios-smart-brevity.md) for a more concise format if the audience prefers narrative over tables.
