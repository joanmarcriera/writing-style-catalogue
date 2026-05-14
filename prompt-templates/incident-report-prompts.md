---
title: Incident Report Prompts
template_type: Incident Report / Postmortem
use_case: Write a blameless incident postmortem that documents what happened, analyses the root cause, assesses impact, and produces a clear set of prevention actions with owners and deadlines.
audience: Engineering teams, IT leadership, incident management teams, and — in regulated environments — compliance or audit functions
output_format: Structured incident report with summary, timeline, root cause analysis, impact assessment, lessons learned, and action items
---

# Incident Report Prompts

## Purpose

A good incident report is a learning document, not a blame document. Its purpose is to understand what happened well enough to prevent it from happening again — and to do that without the report becoming a political exercise in self-protection. Use this template when you need to write a postmortem or incident report following a service outage, security incident, data breach, compliance failure, or significant operational disruption. The output must be factual, precise, and structured — with a detailed timeline, an honest root cause analysis, and specific, assigned prevention actions. The report should be written and distributed within 24–72 hours of the incident being resolved, while detail is still fresh.

## Copy-paste prompt

```
You are an experienced incident manager and postmortem facilitator. Write a clear, blameless incident report that helps the team understand what happened, why, and how to prevent recurrence.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all available information: incident timeline, detection method, root cause, impact data, actions taken, and proposed prevention measures):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 800–1,500 words depending on incident severity]

FORMAT: [FORMAT — recommended: Incident Summary / Timeline / Detection and Initial Response / Root Cause Analysis / Impact Assessment / Lessons Learned / Prevention Actions / Open Items]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with an incident summary: a two-to-four sentence description of what happened, when it started and ended, the severity level, and the headline impact (e.g. number of users affected, duration of outage, data records involved).
3. Timeline: construct a precise chronological timeline with timestamps (at least to the minute where known). Each entry should state: time / event / who took action (by role, not name, unless the organisation requires names). Do not smooth over gaps in the timeline — if there is a period where nothing happened that should have, note it.
4. Root cause analysis: use the "5 Whys" or a structured cause-and-effect approach. Identify the proximate cause (the immediate trigger) and the contributing causes (the systemic factors that made the incident possible or worse). A good RCA will surface process, tooling, and design issues — not just human error.
5. If human error is identified as a contributing cause, also identify the system or process conditions that made that error possible. Blaming individuals without examining systemic factors is not useful and is not blameless.
6. Impact assessment: quantify the impact where data is available — number of users affected, duration of service degradation or outage, data records affected, estimated financial impact (if calculable), regulatory or contractual implications.
7. Lessons learned: what did this incident reveal about the system, the process, or the team's capabilities? Be honest. "The monitoring was insufficient" is a lesson; "the team performed well" is not.
8. Prevention actions: each action must have: a specific description, an owner (by role), a due date, and a priority (P1 = critical, implement immediately; P2 = important, implement within 30 days; P3 = improvement, implement within 90 days). Do not list vague actions such as "improve monitoring" — write "configure an alert in Azure Monitor for B2C token error rate >2% over 5 minutes, threshold currently missing (P1, due: 20 May 2026)".
9. Distinguish facts (confirmed by logs or system data), assumptions (inferred from available evidence), and open items (things that still need to be investigated).
10. Preserve all timeline entries and figures from the input — do not smooth or omit details that might be uncomfortable.
11. Tone: [TONE — recommended: factual, analytical, blameless — focused on systems and processes, not individuals].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the incident report. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read the report. Examples: "Platform Engineering team, Head of Technology, and the Risk & Compliance function", "the board Audit and Risk Committee (monthly incident summary)", "the incident response team and relevant vendors".
- `[PURPOSE]` — what incident is being documented. Examples: "postmortem for the Azure AD B2C authentication outage on 8 May 2026", "incident report for the IAM privilege escalation security incident on 3 April 2026".
- `[CONTEXT]` — background for the LLM. Examples: "the authentication service handles login for 50,000 retail customers; this was a P1 incident with full customer impact for 47 minutes", "the incident involved stale privileged access being exploited; this is the third access-related incident in 12 months".
- `[INPUT]` — everything known: the incident timeline (with times), how it was detected, actions taken to resolve it, root cause analysis already performed, impact data, and proposed prevention measures.
- `[DESIRED_OUTCOME]` — what the report should achieve. Examples: "the engineering team has a shared understanding of what happened and clear, owned actions", "the Audit Committee has sufficient detail to assess the adequacy of the response without needing a technical briefing".
- `[TONE]` — "factual, analytical, blameless". Focus on systems and processes.
- `[LENGTH]` — P1 incidents: 1,000–1,500 words; P2 incidents: 600–900 words.
- `[FORMAT]` — use the recommended structure. For security incidents, add a "Containment and Eradication" section between Response and Root Cause Analysis.
- `[CONSTRAINTS]` — examples: "this report will be shared with the FCA — avoid speculative language", "do not include specific user account names — use role descriptors", "severity classification follows the organisation's incident classification standard ICS-2024".

## Example input

```
AUDIENCE: Platform Engineering team, Head of Technology, Head of Information Security, and Risk & Compliance
PURPOSE: Postmortem for the Azure AD B2C authentication outage — 8 May 2026
CONTEXT: Azure AD B2C is the customer authentication service for the Meridian customer portal — 50,000 retail customers. The incident was classified as P1 (full customer impact). The system was restored at 11:47. This postmortem is being written on 10 May 2026.
INPUT:
  Incident severity: P1
  Service affected: Azure AD B2C customer authentication (meridian-prod tenant)
  Duration: 09:14 – 11:47 (2 hours 33 minutes)
  Impact: 100% of customer login attempts failed during outage; approximately 2,100 active sessions were unaffected (existing tokens remained valid until expiry); estimated 4,800 customer login attempts failed during the window

  Timeline (reconstructed from Azure Monitor logs and PagerDuty):
  09:14 — First B2C token error logged (Azure Monitor)
  09:19 — B2C_TOKEN_FAILURE alert fires in PagerDuty (5-minute window threshold: 2% error rate)
  09:22 — Alert acknowledged by on-call engineer (L2)
  09:35 — L2 engineer begins diagnosis; checks App Insights — no clear error code identified immediately (error code not in known runbook)
  09:51 — L2 engineer escalates to L3 (Platform Engineering lead)
  10:03 — L3 identifies error as AADB2C90072 (expired signing certificate)
  10:09 — Certificate rotation runbook (RBK-CERT-001) initiated
  10:47 — Certificate rotation complete; first successful tokens issued
  11:47 — Full service restoration confirmed; error rate back to baseline

  Root cause: B2C signing certificate expired at 09:14 on 8 May 2026. The certificate had a 12-month validity period and was due for quarterly rotation. The last rotation occurred 14 months ago (March 2025). There was no automated alert for certificate expiry; the quarterly rotation process relied on a calendar reminder that was not actioned.

  Contributing causes:
  1. No automated certificate expiry monitoring in place
  2. The quarterly rotation process was manual and calendar-dependent — no escalation if not actioned
  3. The L2 runbook did not include the AADB2C90072 error code, causing a 28-minute diagnosis delay
  4. Certificate rotation team change in August 2025 — handover did not include calendar reminder transfer

  Lessons learned:
  - Certificate expiry monitoring must be automated
  - The L2 runbook has gaps; AADB2C90072 is a known error code that should have been documented
  - The team change in August created a process gap that was not identified until this incident

  Proposed prevention actions:
  - Configure Azure Monitor certificate expiry alert (14-day warning) — P1
  - Update L2 runbook to include AADB2C90072 and all B2C error codes — P1
  - Implement automated certificate rotation using Azure Key Vault with 90-day validity — P2
  - Conduct process handover review for all critical manual processes — P2
DESIRED_OUTCOME: The engineering team has a shared, complete record of the incident and clear, owned actions. The Head of Technology has the information needed to brief the Risk & Compliance function.
TONE: Factual, analytical, blameless
LENGTH: 900–1,200 words
CONSTRAINTS: Reference the runbook by name (RBK-CERT-001). Do not include individual staff names — use role titles. This report may be reviewed by the Audit Committee.
```

## Example output

---

## Incident Report: Azure AD B2C Authentication Outage — 8 May 2026

**Incident ID:** INC-2026-0047
**Service affected:** Azure AD B2C — Meridian customer authentication (meridian-prod tenant)
**Severity:** P1 (full service impact)
**Duration:** 09:14 – 11:47, 8 May 2026 (2 hours 33 minutes)
**Status:** Resolved
**Report prepared:** 10 May 2026

---

### Incident Summary

On 8 May 2026 at 09:14, the Meridian customer authentication service (Azure AD B2C) stopped issuing tokens following the expiry of the signing certificate. All new customer login attempts failed for 2 hours and 33 minutes. Approximately 4,800 login attempts were unsuccessful during the outage window. Existing customer sessions with unexpired tokens were not affected. Service was fully restored at 11:47 following manual certificate rotation using runbook RBK-CERT-001.

---

### Timeline

| Time | Event |
|------|-------|
| 09:14 | B2C signing certificate expired; token issuance fails. First error logged in Azure Monitor. |
| 09:19 | `B2C_TOKEN_FAILURE` PagerDuty alert fires (5-minute threshold reached; error rate 100%). |
| 09:22 | Alert acknowledged by on-call engineer (L2 Support). |
| 09:35 | L2 engineer begins diagnosis in Azure Application Insights. Error code `AADB2C90072` is present in logs but is not documented in the L2 runbook. Diagnosis stalls. |
| 09:51 | L2 engineer escalates to L3 (Platform Engineering lead). 29 minutes have elapsed since the alert was acknowledged. |
| 10:03 | L3 engineer identifies error code `AADB2C90072` — expired signing certificate. Certificate rotation runbook (RBK-CERT-001) is located. |
| 10:09 | Certificate rotation initiated using RBK-CERT-001. |
| 10:47 | Certificate rotation complete. Azure B2C begins issuing tokens successfully. |
| 11:47 | Full service restoration confirmed; error rate returned to baseline (<0.1%). PagerDuty alert resolved. |

*Note: a 16-minute gap between certificate rotation completion (10:47) and full restoration confirmation (11:47) reflects propagation time and cache clearing. This duration is within expected parameters for B2C certificate rotation.*

---

### Detection and Initial Response

The `B2C_TOKEN_FAILURE` alert fired correctly and within the expected 5-minute window. The alert was acknowledged promptly. The 29-minute delay between acknowledgement and escalation to L3 was caused by the L2 runbook not containing the `AADB2C90072` error code — the L2 engineer was unable to identify the cause from the available documentation and attempted to diagnose it independently before escalating. This is the primary source of avoidable delay in this incident.

---

### Root Cause Analysis

**Proximate cause:** The Azure AD B2C signing certificate expired at 09:14 on 8 May 2026. The certificate, with a 12-month validity period, had not been rotated since March 2025 (14 months prior). The quarterly rotation process required for 12-month certificates was not executed.

**Contributing causes:**

1. **No automated certificate expiry monitoring.** There was no Azure Monitor alert configured to warn of certificate expiry in advance. The first notification was the production outage itself.

2. **Manual, calendar-dependent rotation process.** The quarterly certificate rotation relied on a calendar reminder in an individual engineer's calendar. There was no escalation mechanism or shared team process to ensure it was completed.

3. **Process handover gap.** The engineer responsible for certificate rotation left the team in August 2025. The handover process did not include transfer of the calendar reminder or explicit ownership of the rotation process. This gap was not identified until this incident.

4. **Runbook gap.** The L2 support runbook did not include the `AADB2C90072` error code (expired certificate). This caused a 29-minute diagnosis delay that could have been avoided.

*Note: The root cause is a process and tooling failure, not an individual failure. The conditions that made this incident possible — no automated monitoring, a manual process, and an undocumented handover gap — existed independently of any individual's actions on the day.*

---

### Impact Assessment

| Metric | Value |
|--------|-------|
| Outage duration | 2 hours 33 minutes |
| Failed login attempts (estimated) | 4,800 |
| Active sessions unaffected | ~2,100 |
| Customer-facing impact | 100% of new login attempts failed |
| Financial impact | Not calculated; under assessment by Finance |
| Regulatory notification required | Under assessment by Risk & Compliance |

---

### Lessons Learned

1. Automated monitoring must be the default for time-critical dependencies such as certificate expiry. A calendar reminder is not a reliable control.
2. The L2 runbook has material gaps. If an L2 engineer cannot diagnose a known error code from the runbook, the runbook is not fit for purpose.
3. Process ownership — particularly for periodic maintenance tasks — must be explicitly tracked in the team's operating model and reviewed when team membership changes.
4. The team change in August 2025 created a process gap that was not caught by any existing control. Team change processes should include a review of owned periodic tasks.

---

### Prevention Actions

| # | Action | Owner | Due Date | Priority |
|---|--------|-------|----------|----------|
| 1 | Configure Azure Monitor alert for B2C signing certificate expiry — 30-day warning and 14-day critical alert | Head of Infrastructure | 20 May 2026 | P1 |
| 2 | Update L2 runbook (RBK-B2C-001) to include `AADB2C90072` and all documented B2C error codes | Platform Engineering Lead | 20 May 2026 | P1 |
| 3 | Implement automated certificate rotation using Azure Key Vault with 90-day validity (eliminates manual rotation process) | Platform Engineering team | 30 June 2026 | P2 |
| 4 | Conduct a review of all manual periodic processes owned by the Platform Engineering team; assign explicit owners and escalation contacts | Head of Infrastructure | 31 May 2026 | P2 |
| 5 | Include periodic process ownership review in the team change and onboarding checklist | People Lead (IT) | 30 June 2026 | P3 |

---

### Open Items

- Financial impact assessment: Finance to confirm whether customer compensation obligations apply.
- Regulatory notification: Risk & Compliance assessing whether FCA notification is required under DORA operational incident reporting requirements. Assessment due: 15 May 2026.

---

## Review checklist

- [ ] Incident summary covers: what happened, when, severity, and headline impact — in four sentences or fewer
- [ ] Timeline has timestamps to the minute for all key events — no gaps are smoothed over
- [ ] Root cause analysis identifies both the proximate cause and contributing systemic causes
- [ ] Human error, where identified, is accompanied by the systemic conditions that made it possible
- [ ] Impact is quantified with specific figures
- [ ] Lessons learned are honest — they name real gaps, not just "the team did well"
- [ ] Every prevention action has: a specific description, an owner (by role), a due date, and a priority
- [ ] No vague prevention actions ("improve monitoring" — not acceptable)
- [ ] Open items are flagged explicitly
- [ ] British English used throughout

---

See [styles/incident-report-style.md](../styles/incident-report-style.md) for detailed incident report style.
