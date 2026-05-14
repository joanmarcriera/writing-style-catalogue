---
title: Crisis Communications
category: Urgent
aliases: [Emergency Response, Critical Updates]
---

# Crisis Communications

## What This Style Is

Clear, factual, calm communication during emergencies. Prioritises facts over reassurance. Transparent about what happened, what we know, and what we're doing. Builds trust through honesty.

**Core principle**: Fact → Action → Transparency → Next Update.

## When to Use It

- Service outages or incidents
- Security breaches
- Safety issues
- Public emergencies
- Major operational failures
- Employee or customer safety concerns

## When NOT to Use It

- Routine updates (use Smart Brevity)
- Strategic decisions (use Board Paper)
- Teaching (use Socratic)
- Persuasion (use Consulting)

## Core Structure

```
[HEADLINE]
What happened. Be direct.

[WHAT WE KNOW]
Facts as of now. Acknowledge unknowns.

[IMPACT]
Who is affected. How.

[WHAT WE'RE DOING]
Specific actions underway.

[TIMELINE]
When you'll hear more.

[CONTACT]
How to reach us if you need help.
```

## Copy-Paste Prompt Template

```
You are a crisis communications expert. Write an emergency update from:

INCIDENT:
[What happened]

AFFECTED PARTIES:
[Who is impacted]

KNOWN FACTS:
[What we know for certain]

UNKNOWN FACTORS:
[What we're still investigating]

ACTIONS UNDERWAY:
[Specific steps being taken]

NEXT COMMUNICATION:
[When and how we'll update]

INSTRUCTIONS:
1. Lead with the fact (what happened)
2. State impact clearly
3. List concrete actions underway
4. Acknowledge what you don't know yet
5. Give timeline for next update
6. Use calm, factual language
7. No spin or reassurance without basis

Output only the crisis update. No preamble.
```

## Short Example

**Customer Data – Service Update**

A security vulnerability in our payment processing system allowed unauthorised access to customer payment data between 14:00 and 16:30 GMT on 15 May 2026.

**What We Know**
- The vulnerability was in our payment API authentication layer
- Access was detected and the system was taken offline at 16:30
- Approximately 8,500 customers may have been affected
- Payment data (card numbers, expiry dates) was exposed
- Customer names and email addresses were not accessed

**What We're Doing**
1. All affected customers have been notified by email (sent 20:00 today)
2. We've issued complimentary credit monitoring for all affected customers (12 months)
3. We've hired external security firm CyberSecure to conduct full forensic analysis
4. Our engineering team is patching the vulnerability (patch deployed 18:00 today)

**What We Don't Yet Know**
- Whether any data was copied or misused
- Whether any other systems were compromised
- Root cause of the vulnerability (forensic analysis underway)

**Your Next Update**
We'll provide a full incident report within 48 hours. We'll update customers every 24 hours until the investigation is complete.

**Need Help?**
Contact our customer support team: support@[company].com or call [phone].

---

## Quality Checklist

- [ ] Lead with what happened (not our feelings about it)
- [ ] Facts are clear and specific
- [ ] Impact is stated clearly
- [ ] Actions are concrete and underway
- [ ] Unknown factors are acknowledged
- [ ] Next update timeline is stated
- [ ] Tone is calm and matter-of-fact
- [ ] Contact information is clear

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Downplaying severity | Feels dishonest; erodes trust | State impact clearly and accurately |
| Vague about what happened | Creates speculation and fear | Be specific about facts |
| No acknowledgement of unknowns | Seems like a cover-up | Say "We're investigating" when unsure |
| Over-reassurance | Feels hollow | Provide facts and actions, not comfort |
| No timeline for next update | People feel abandoned | Always say when they'll hear again |

---

See [prompt-templates/incident-report-prompts.md](../prompt-templates/incident-report-prompts.md) for post-incident analysis.
