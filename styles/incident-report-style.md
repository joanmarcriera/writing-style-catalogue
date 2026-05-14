---
title: Incident Report Style
category: Specialist
aliases: [Postmortem, Incident Analysis]
---

# Incident Report Style

## What This Style Is

Factual analysis of an incident. Focus on understanding what happened, why, and how to prevent recurrence. Blameless and learning-focused.

**Core principle**: Timeline → Root Cause → Prevention.

## When to Use It

- Post-incident reviews
- Outage analyses
- Security incident reviews
- Operational failure analysis
- Learning capture
- Process improvement documentation

## When NOT to Use It

- Blame assignment (never appropriate)
- Quick incident notes (use Crisis Communications for that)
- Performance reviews (use Performance Review)
- Formal governance (use Board Paper)

## Core Structure

```
[INCIDENT SUMMARY]
What happened; impact; duration.

[TIMELINE]
When events occurred; what was observed.

[DETECTION AND RESPONSE]
How incident was found; what actions taken.

[ROOT CAUSE]
Why did this happen; contributing factors.

[PREVENTION]
What will prevent recurrence.

[ACTION ITEMS]
Specific, assigned, with due dates.
```

## Copy-Paste Prompt Template

```
You are a postmortem facilitator. Write an incident report from:

INCIDENT:
[What happened]

TIMELINE:
[When did events occur]

DETECTION:
[How was incident found]

IMPACT:
[What was affected and for how long]

ROOT CAUSE:
[Why did this happen]

PREVENTION:
[How do we prevent recurrence]

INSTRUCTIONS:
1. Focus on facts, not blame
2. Create clear timeline
3. Analyse root cause objectively
4. Identify systemic improvements
5. Assign specific actions
6. Include all perspectives

Output only the incident report. No preamble.
```

## Short Example

**Incident Report: Payment Processing Outage – 15 May 2026**

**Incident Summary**
Payment processing API was unavailable for 47 minutes (14:20–15:07 GMT), affecting approximately 2,000 transactions. Customers received "Service Unavailable" errors when attempting to make purchases.

**Timeline**
- 14:20: Monitoring alerts triggered; database connection pool exhausted
- 14:22: On-call engineer acknowledged alert
- 14:25: Engineering team identified queue processing hitting database limits
- 14:45: Temporary fix deployed (increased connection pool from 20 to 50)
- 15:07: Service recovered; normal performance restored
- 15:15: Incident declared resolved

**Impact**
- 2,000 attempted transactions failed
- Estimated revenue impact: £18,000
- Customer support received 150 complaint emails
- No data loss or security exposure

**Root Cause**
A data migration job queued transactions at 10x the normal rate but the consumer process wasn't scaled to match. The database connection pool was exhausted; new requests were rejected. The queue monitoring alerting triggered on failure count, but not on queue depth—delaying root cause detection.

**Prevention**

1. **Monitoring improvement**: Add queue depth alerting (trigger at 80% of consumer capacity)
2. **Capacity planning**: Review queue consumer sizing quarterly; align with peak processing rates
3. **Runbook enhancement**: Add "high queue depth" procedure to on-call runbook
4. **Chaos engineering**: Test connection pool exhaustion scenarios monthly

**Action Items**
- [ ] Add queue depth monitoring by 22 May (Alice)
- [ ] Review consumer scaling; update if needed by 29 May (Bob)
- [ ] Update runbook by 26 May (Charlie)
- [ ] Schedule chaos engineering session for June (Diana)

---

## Quality Checklist

- [ ] Summary captures what happened and impact
- [ ] Timeline is accurate and detailed
- [ ] Root cause is objective and systemic
- [ ] Prevention focuses on systems, not people
- [ ] Actions are specific and assigned
- [ ] Blameless tone throughout
- [ ] Actionable improvements identified

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Blaming individuals | Creates defensiveness; stops learning | Focus on systems that enabled failure |
| Vague root cause | Doesn't prevent recurrence | Dig into systemic factors |
| No prevention measures | Incident will recur | Design specific system improvements |
| Missing timeline details | Hard to understand sequence | Record exact times and observations |
| No assigned actions | Improvements don't happen | Assign specific, dated tasks |

---

See [prompt-templates/incident-report-prompts.md](../prompt-templates/incident-report-prompts.md) for more incident report templates.

See [examples/incident-report.md](../examples/incident-report.md) for a complete example.
