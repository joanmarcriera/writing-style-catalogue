---
title: Incident Report Style
category: Operational
best_for: Post-incident reviews (postmortems) following service outages, security incidents, or significant operational failures — where the goal is to understand what happened, why, and how to prevent recurrence. Suitable for both internal engineering reviews and formal reports shared with leadership, customers, or regulators.
not_good_for: Active incident updates where speed is paramount (use Crisis Communications instead); disciplinary or performance matters related to an incident (use HR and legal processes); strategic decisions triggered by an incident pattern (use Consulting Style or Executive Briefing).
default_tone: Factual and blameless. Analytical and learning-focused. Objective and precise.
typical_length: 500–1,500 words for an engineering postmortem; 1,000–2,500 words for a formal report shared externally or with leadership
aliases: [Postmortem, Post-Incident Review, Incident Analysis, RCA]
---

# Incident Report Style

## What this style is

An incident report is a structured, factual analysis of a significant failure or incident — its timeline, impact, root cause, and the actions that will prevent recurrence. It is the primary vehicle for organisational learning from failure. A good incident report does not assign blame to individuals; it examines the systems, processes, and conditions that allowed the failure to occur, and it produces specific, owned, time-bound action items to address those conditions.

The blameless postmortem culture — pioneered at companies such as Google, Etsy, and Amazon — is based on the insight that most failures are caused by systemic factors, not individual incompetence or negligence. People operate within systems; the systems create the conditions for failure. Fixing systems produces durable improvement; fixing blame produces defensiveness and silence.

**Core principle**: Timeline → Root Cause → Prevention. The report answers three questions: What happened exactly? Why did it happen (systemic causes)? What will we do differently to prevent recurrence?

## When to use it

- Post-incident reviews following service outages, whether brief or prolonged
- Security incident analysis following a breach, unauthorised access, or data exposure
- Operational failure analysis following a significant process breakdown
- Process improvement documentation capturing lessons from near-misses
- Formal reports to customers, regulators, or leadership following a material incident
- Learning reviews for incidents that were resolved well, to capture what worked

## When not to use it

- Active incident communications — use [Crisis Communications](crisis-communications.md) instead
- Blame assignment — never appropriate; if a performance matter exists, use HR and legal processes
- Quick post-incident updates — use [Smart Brevity](axios-smart-brevity.md) for a brief "all clear" notification
- Formal governance decisions triggered by an incident pattern — use [Consulting Style](consulting-style.md) or [Board Paper Style](board-paper-style.md) instead

## Core structure

```
[INCIDENT TITLE AND REFERENCE]
"Incident Report: [Service/System] — [Date]"
Internal reference number if applicable.
Severity classification (P1 / P2 / etc.) and current status (Resolved).

[INCIDENT SUMMARY]
What happened and what was the impact.
Duration: start time to resolution time.
Services or systems affected.
Number of users or transactions affected.
Estimated business impact (revenue, data, reputation).

[TIMELINE]
Chronological sequence of events from first anomaly to full resolution.
Each entry: time (to the minute) and what occurred.
Include: first alert, initial diagnosis, key actions, resolution, all-clear.
Include false starts and incorrect diagnoses — these are part of the learning.

[DETECTION AND RESPONSE]
How the incident was detected (alert, customer report, manual observation).
Who was involved in the response and in what roles.
Communications sent during the incident.
Quality of the response: what worked, what was slow or confused.

[ROOT CAUSE ANALYSIS]
The underlying cause(s) of the incident.
Distinguish proximate cause (what immediately caused the failure) from root cause (what allowed the failure to occur).
Use a structured approach: Five Whys, fault tree analysis, or similar.
Contributing factors: what made the system vulnerable to this failure.
Do not stop at "human error" — ask what system or process allowed the human error to occur.

[IMPACT ASSESSMENT]
Quantified impact on users (number affected, duration of impact).
Quantified business impact (estimated revenue impact, SLA credits owed, etc.).
Data integrity: was any data lost, corrupted, or exposed?
Reputational or regulatory impact.

[PREVENTION — ACTION ITEMS]
Specific, prioritised actions to prevent recurrence.
Each action: what it is, who owns it, and by when.
Actions should address systemic factors — not just patch the immediate failure.
Categorise by type: Detection, Prevention, Response, Process.

[LESSONS LEARNED]
What worked well in detection and response.
What could have been better.
What would have made this incident shorter, smaller, or prevented.
Systemic insights relevant to other services or teams.
```

## Copy-paste prompt

```
You are a skilled postmortem facilitator and technical writer. Your task is to write a comprehensive incident report from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Engineering team and engineering leadership", "Customer success team and affected enterprise customers", "CISO and audit committee receiving a security incident report"]
PURPOSE: [PURPOSE — e.g. "Internal postmortem following a 47-minute payment API outage", "External customer-facing report following a data access incident", "Formal RCA report for a P1 security incident submitted to the Information Commissioner's Office"]
CONTEXT: [CONTEXT — e.g. "The outage was caused by a database connection pool exhaustion during a migration job; this is the third incident in four months related to the same legacy payment service"]
INPUT: [INPUT — paste all incident timeline notes, alert data, communication logs, action items, contributing factors, and any initial root cause analysis here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Engineering team has a shared, accurate understanding of what happened and why, and owns specific action items to prevent recurrence", "Leadership can present this report to the board and to affected customers with confidence that it is complete and honest"]
TONE: [TONE — e.g. "Blameless and analytical — focus on systems and processes, not individuals", "Factual and transparent — suitable for sharing with affected customers", "Technical and precise — written for an engineering audience"]
LENGTH: [LENGTH — e.g. "800–1,200 words for an internal engineering postmortem", "1,500–2,000 words for a formal external report"]
FORMAT: [FORMAT — headed sections: Incident Summary / Timeline / Detection and Response / Root Cause Analysis / Impact Assessment / Prevention / Lessons Learned]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not name individual engineers in the public-facing version", "Root cause must not be attributed to a single person — focus on systemic factors", "Revenue impact figures must be approved by Finance before inclusion"]

INSTRUCTIONS:
1. Write an Incident Summary that answers: what happened, when, how long it lasted, what was affected, and the headline impact. Maximum 150 words.
2. Write a Timeline section with precise timestamps. Include every significant event: first alert, initial diagnosis, key actions, resolution. Include false starts and incorrect diagnoses — these are part of the learning record.
3. In Root Cause Analysis, distinguish proximate cause from root cause. Use a Five Whys structure or equivalent. Do not accept "human error" as a root cause — ask what system or process allowed the error to occur.
4. Assign blameless, systemic language throughout. Say "the monitoring system did not alert on queue depth" not "the engineer missed the queue depth alert."
5. Write specific action items with assigned owners and due dates. Each action must address a systemic factor identified in the root cause analysis.
6. Include a Lessons Learned section noting what worked well as well as what could be improved.
7. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
8. Preserve all facts and timeline data exactly as provided in [INPUT]. Do not invent events, times, or figures.
9. Distinguish confirmed facts from estimates or inferences. Flag estimates with "(estimated)" and inferences with "(inferred)."
10. Total length must not exceed [LENGTH].

Output the incident report only. No preamble, no commentary.
```

## Output format

An incident report is typically published in a shared document (Confluence, Notion, Google Docs) and may also be shared as a PDF for formal distribution. It contains:

- **Title and metadata**: Incident title, date, severity, status, author, and review date
- **Summary box** (for longer reports): 3–4 sentences covering what, when, duration, and headline impact
- **Timeline table or list**: Timestamped entries in chronological order
- **Root Cause Analysis**: Structured prose — not a bullet list of factors
- **Action items table**: Owner, due date, and status column (Open / In Progress / Complete)
- **Lessons Learned**: Two headed sections — "What worked well" and "What could be improved"

The tone is consistently blameless and analytical. Individual names are used only where necessary for context (e.g. "the on-call engineer acknowledged the alert at 14:22"). No language that implies individual fault, incompetence, or negligence.

## Example

**Incident Report: Payment Processing API — Database Connection Pool Exhaustion**
*Incident reference: INC-2026-047 | Date: 14 May 2026 | Severity: P1 | Status: Resolved*
*Authors: Platform Engineering Team | Review date: 22 May 2026*

---

**Incident Summary**

The payment processing API was unavailable for 47 minutes (14:20–15:07 GMT) on 14 May 2026, affecting approximately 2,000 customer transactions. Customers received "Service Unavailable" (HTTP 503) errors during checkout. No payment was processed or charged during the outage; no data was lost or exposed. The estimated revenue impact is £18,000 in abandoned transactions (estimated — pending Finance review). Service was fully restored at 15:07 GMT.

---

**Timeline**

| Time (GMT) | Event |
|-----------|-------|
| 14:15 | Scheduled data migration job for the user analytics pipeline began execution |
| 14:18 | Database CPU usage reached 85% — no alert triggered (alert threshold: 95%) |
| 14:20 | Payment API began returning HTTP 503 errors as database connection pool (limit: 20) was exhausted |
| 14:20 | Automated uptime monitoring detected HTTP 503 on `/api/v2/payments/process` — alert sent to on-call channel |
| 14:22 | On-call engineer (platform team) acknowledged alert and began investigation |
| 14:25 | Initial hypothesis: application deployment issue — rolled back last deployment |
| 14:32 | Rollback completed; errors continued — hypothesis rejected |
| 14:35 | Database connection pool exhaustion identified as the cause via CloudWatch metrics |
| 14:38 | Root cause hypothesis: migration job consuming database connections |
| 14:45 | Emergency configuration change deployed — connection pool limit increased from 20 to 50 |
| 14:47 | Partial service recovery — approximately 60% of payment requests now succeeding |
| 15:04 | Migration job throttled and rescheduled to 02:00 GMT |
| 15:07 | Full service recovery confirmed — connection pool back within normal operating range |
| 15:15 | Incident declared resolved; customer update sent |

---

**Detection and Response**

The incident was detected by automated uptime monitoring at 14:20 GMT — the same minute the outage began. This was effective. Alert routing to the on-call channel was immediate.

The initial response took seven minutes from acknowledgement (14:22) to first action (14:25). The first hypothesis — a deployment issue — was reasonable given recent deployment activity, but the rollback consumed 10 minutes without resolving the incident. The actual root cause was identified at 14:35, 13 minutes after alert acknowledgement. In hindsight, checking database connection metrics earlier in the diagnosis sequence would have reduced total incident duration by approximately 10 minutes.

Customer communications were sent at 15:00 GMT and 15:15 GMT, using the standard incident communication template.

---

**Root Cause Analysis**

*Proximate cause*: The scheduled data migration job (`user-analytics-migration-v2`) executed during peak trading hours and consumed database connections at a rate that exceeded the payment API's connection pool limit (20 connections), causing new payment requests to fail with a connection pool exhaustion error.

*Root cause — Five Whys*:

1. Why did the payment API fail? The database connection pool was exhausted.
2. Why was the connection pool exhausted? The migration job consumed all available connections simultaneously.
3. Why was the migration job scheduled during peak hours? The job scheduling configuration had no awareness of trading peak hours; it was set by absolute time (14:00 GMT) rather than by load or time-window constraints.
4. Why was there no alert before the connection pool was exhausted? The monitoring system alerting covered CPU utilisation and API error rate, but not connection pool utilisation — a metric that would have given 5–8 minutes of warning.
5. Why did the monitoring system not cover connection pool utilisation? This metric was not included in the standard monitoring template when the payment service was onboarded in 2023; no process required a review of monitoring coverage when infrastructure changes were made.

*Contributing factors*:
- The connection pool limit of 20 was set in 2023 for a lower traffic volume and had not been reviewed as traffic grew
- The `user-analytics-migration-v2` job was a new migration with higher parallelism than previous jobs; its connection consumption was not tested against production traffic patterns before scheduling

---

**Impact Assessment**

| Dimension | Detail |
|-----------|--------|
| Duration | 47 minutes (14:20–15:07 GMT) |
| Users affected | Approximately 2,000 customers attempting payment during the window |
| Transactions failed | Approximately 2,000 attempted transactions — none processed or charged |
| Revenue impact | £18,000 in abandoned transactions (estimated) |
| Data integrity | No data lost; no data exposed |
| SLA credits | 2 enterprise customers with SLA uptime guarantees — credits assessment in progress |
| Customer support volume | 150 support emails received during outage |

---

**Prevention — Action Items**

| # | Action | Owner | Due | Category |
|---|--------|-------|-----|----------|
| 1 | Add database connection pool utilisation alerting to all services using the standard monitoring template | Platform team | 22 May 2026 | Detection |
| 2 | Enforce peak-hours scheduling restrictions for all data migration jobs — migrations must run between 01:00 and 05:00 GMT | Data engineering lead | 25 May 2026 | Prevention |
| 3 | Review and right-size database connection pool limits for all production services — assess against current peak traffic, not 2023 configuration | Platform team | 29 May 2026 | Prevention |
| 4 | Require load testing for all new migration jobs before production scheduling — add to migration runbook | Data engineering lead | 22 May 2026 | Process |
| 5 | Add "database connection pool utilisation" to the standard on-call diagnosis checklist | On-call lead | 22 May 2026 | Response |

---

**Lessons Learned**

*What worked well*
Automated monitoring detected the outage at the same minute it began — alert latency was effectively zero. The on-call engineer followed the escalation process correctly and communicated proactively. The connection pool configuration change was deployed quickly once the root cause was identified. Customer communication was clear and factual.

*What could be improved*
The initial diagnosis hypothesis (deployment issue) was reasonable but consumed time that could have been saved by checking database metrics earlier. The on-call runbook did not include a "database connection pool exhaustion" scenario — this delayed the diagnosis by approximately 8 minutes. The migration job scheduling had no safeguard against peak-hours execution; this is a systemic gap that allowed a routine job to cause a P1 incident.

*Systemic insights for other teams*
Any data migration job that operates against a shared production database is a latent P1 risk unless its connection consumption is profiled against peak traffic. Teams should review whether their migration jobs have scheduling guardrails and whether their monitoring covers database connection pool utilisation, not just CPU and error rates.

## Quality checklist

- [ ] Incident Summary captures what happened, when, duration, and headline impact in under 150 words
- [ ] Timeline is in chronological order with precise timestamps (to the minute)
- [ ] Timeline includes false starts and incorrect diagnoses — not just the successful path
- [ ] Root Cause Analysis distinguishes proximate cause from root cause
- [ ] Five Whys or equivalent used to reach systemic root cause — not stopping at "human error"
- [ ] Language is blameless throughout — focuses on systems and processes
- [ ] Impact is quantified: users affected, duration, revenue or data impact
- [ ] Action items are specific, assigned to named owners, with due dates
- [ ] Lessons Learned includes what worked well as well as what could be improved
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Blaming individuals | Creates defensiveness; stops learning; individuals operate within systems | Focus on the system conditions that enabled the failure |
| Stopping root cause at "human error" | Does not prevent recurrence — the human condition will occur again | Ask what system or process allowed the human error to occur |
| Vague or generic root cause | Produces vague or generic action items that do not prevent recurrence | Dig to specific systemic factors using Five Whys |
| Timeline only covers successful actions | Omits learning opportunities from false starts | Include everything — incorrect diagnoses, abandoned approaches |
| Unassigned or vague action items | Improvements do not happen | Every action: specific, assigned, dated |
| No impact quantification | Leadership cannot assess severity or SLA obligations | Quantify users, duration, revenue, and data impact |
| No lessons for the wider organisation | Learning stays within the responding team | Include systemic insights applicable to other services or teams |

---

See [prompt-templates/incident-report-prompts.md](../prompt-templates/incident-report-prompts.md) for more incident report templates.

See [examples/incident-report.md](../examples/incident-report.md) for a complete example.
