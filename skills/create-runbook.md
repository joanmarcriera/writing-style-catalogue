---
title: Create Runbook
skill_type: Document generation
output: An operational runbook with numbered response steps, decision trees, escalation paths, and resolution verification — designed to be followed under time pressure by an on-call engineer or incident responder
tools_needed: LLM (Claude/ChatGPT/Gemini), Confluence, Notion, or Markdown editor
difficulty: Medium
---

# Skill: Create Runbook

## What this skill does

Documents the step-by-step response procedure for a specific operational situation or incident type — a database outage, a failed deployment, an authentication service degradation, a security alert. Unlike an SOP, a runbook assumes urgency: the person following it is often under pressure, possibly at 2am, and may be less experienced than usual because senior staff are busy elsewhere. The runbook must therefore be faster to read, more prescriptive, and more explicit about escalation triggers. It should include enough diagnostic guidance to identify the problem and enough response steps to resolve it or safely hand it off.

## When to use it

- Documenting the response procedure for any incident that has occurred more than once (if it happened once, it will happen again)
- Creating on-call handover documentation for a cloud infrastructure, application support, or security operations team
- Satisfying an ISO 27001 or SOC 2 requirement for documented incident response procedures
- Reducing mean time to resolution (MTTR) for known failure modes by removing the need to diagnose from scratch
- Onboarding an on-call engineer who must be able to respond to incidents they have not seen before

## Inputs required

- The specific incident or situation the runbook covers (named precisely: "Azure SQL Database connection pool exhaustion", not "database issues")
- How the situation is typically detected — monitoring alert, user report, automated ticket, or observed anomaly
- The diagnostic steps to identify the root cause
- The response steps to resolve the incident
- Decision points: when to escalate vs. when to continue resolving alone
- Escalation contacts — names, roles, and contact methods (phone, PagerDuty, Teams)
- How to verify the incident is resolved
- Post-incident actions (ticket update, post-mortem trigger, communication to users)

## Copy-paste prompt

```
You are an SRE (Site Reliability Engineer) and incident response specialist. Write an operational runbook for the incident type described below.

AUDIENCE: [Who will use this runbook — e.g. on-call cloud engineer, Tier 1 support, security analyst]
PURPOSE: [The specific incident or situation this runbook covers]
CONTEXT: [System architecture context; what systems are involved; any known causes of this incident]
INPUT: [Describe: how the incident is detected; known diagnostic steps; known resolution steps; escalation contacts; resolution verification method]
DESIRED_OUTCOME: [What "resolved" looks like — the specific state that confirms the incident is closed]
TONE: Terse, imperative, and explicit. The user is under pressure — no preamble, no explanation of why, just what to do.
LENGTH: As long as the process requires. Prioritise clarity over brevity — a runbook that is too short leaves the responder guessing.
FORMAT: Numbered steps. Decision points as explicit branches ("If [condition] → Go to Step X. If [condition] → Escalate: see Section 4"). Commands in code blocks. Escalation contacts in a clearly labelled box. Resolution check as a separate section.
CONSTRAINTS: Use British English. Every step must be an action. Avoid passive voice. Include exact commands, menu paths, or query strings where the process requires them — do not write "run the diagnostic query" if you can write the actual query. Output only the runbook; no preamble.

STRUCTURE:
# Runbook: [Incident Name]
**Severity**: [P1 / P2 / P3]
**Last tested**: [Date]
**Owner**: [Team or role]

## 1. Detection
[What triggers this runbook — alert name, threshold, symptom]

## 2. Initial triage (first 5 minutes)
[Quick diagnostic steps to confirm what is happening]

## 3. Response steps
[Numbered steps with decision branches]

## 4. Escalation
[When to escalate; who to contact; how]

## 5. Resolution verification
[How to confirm the incident is resolved]

## 6. Post-incident actions
[Ticket update, post-mortem trigger, user communication]
```

## Suggested output structure

- **Header** — incident name, severity level (P1/P2/P3), last tested date, owning team
- **Detection** — the specific alert, threshold, or symptom that triggers this runbook; include the monitoring tool and alert name
- **Initial triage** — 3–5 quick checks to confirm what is happening and rule out false alarms (5 minutes maximum)
- **Response steps** — numbered sequential steps with explicit decision branches; commands in code blocks; any required credentials or access noted
- **Escalation section** — clear trigger conditions for escalation; named contacts with role and contact method; what information to provide when escalating
- **Resolution verification** — specific, measurable checks that confirm the incident is resolved; what to monitor for recurrence in the next 30 minutes
- **Post-incident actions** — update the ticket, trigger post-mortem if P1, send user communication if service was impacted, update monitoring if alert was wrong

## Quality controls

- [ ] The runbook covers a specific, named incident type — not a category (not "database issues" but "SQL connection pool exhaustion")
- [ ] Diagnostic steps come before response steps — the responder must confirm what is wrong before taking action
- [ ] Every escalation trigger is explicit — the responder never has to decide whether to escalate based on vague guidance
- [ ] Exact commands, queries, or API calls are included wherever the process requires technical execution
- [ ] Resolution verification is measurable — a specific metric or system state, not "confirm it's working"
- [ ] The runbook has been tested against a real or simulated incident at least once
- [ ] Post-incident actions include a post-mortem trigger for P1 and P2 incidents

## Common failure modes

- **Too generic**: A runbook that says "check the logs" without specifying which logs, where to find them, and what to look for is not useful under pressure — be specific about every diagnostic step
- **No decision branches**: Real incidents branch; a runbook that assumes a linear resolution path will leave the responder stranded when the first approach does not work
- **Escalation contacts outdated**: If the named escalation contact has left the team, the responder panics — use role names and team queues rather than individual names; review quarterly
- **Missing resolution verification**: Responders often declare an incident resolved too early — always include a specific check (metric back to baseline, service health endpoint returning 200, error rate below threshold) before closing
- **Commands not tested**: Commands written from memory may have wrong flags or syntax — test every command in the runbook against a non-production environment before publishing

## Example request

"Write a runbook for 'Azure Active Directory authentication service degraded' — a P2 incident. Detection: Azure Monitor alert 'AAD Sign-in Failure Rate > 15%'. Triage: check Azure Service Health dashboard, check AAD sign-in logs in Entra admin centre for error codes. Response: if Microsoft-side issue, post status update and monitor; if tenant-side, check conditional access policies changed in last 2 hours, roll back if necessary. Escalation: after 20 minutes unresolved, page the Head of Infrastructure. Resolution: sign-in failure rate below 2% for 10 consecutive minutes. Post-incident: update incident ticket, send all-staff notification if outage exceeded 30 minutes."
