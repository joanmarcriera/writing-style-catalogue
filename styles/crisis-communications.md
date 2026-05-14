---
title: Crisis Communications
category: Operational
best_for: Urgent communications during an active incident, outage, security breach, or safety event — when stakeholders need factual information immediately and trust depends on transparency. Also used for the first external communication following a significant incident before a full post-incident report is ready.
not_good_for: Routine operational updates (use Smart Brevity); post-incident analysis and learning documentation (use Incident Report Style); strategic or governance decisions triggered by a crisis (use Board Paper Style or Executive Briefing).
default_tone: Calm, factual, and direct. Transparent about what is known and unknown. No spin or premature reassurance.
typical_length: 200–400 words for an initial incident update; 400–700 words for a customer-facing incident notification
aliases: [Emergency Response, Incident Update, Critical Communications]
---

# Crisis Communications

## What this style is

Crisis communications is the discipline of communicating clearly, honestly, and rapidly when something has gone seriously wrong. It applies during active incidents (outages, security breaches, safety events) and in the immediate aftermath before full analysis is complete. Its core function is to maintain trust precisely when trust is most at risk.

The distinguishing feature of good crisis communication is that it says what it does not know as clearly as what it does. Premature reassurance — "everything is under control" when it is not — destroys trust more completely than the incident itself. The goal is not to manage perception but to ensure that everyone who needs information has it, in a form they can act on.

**Core principle**: Fact → Action → Transparency → Next Update. State what happened, what you are doing, what you do not yet know, and exactly when the next communication will come.

## When to use it

- Service outage or partial degradation affecting customers or users
- Security incidents including data breaches, unauthorised access, or ransomware
- Safety events involving physical harm or environmental impact
- Significant operational failures with broad stakeholder impact
- Regulatory incidents requiring immediate notification
- Employee safety or welfare emergencies
- Any situation where silence or delay would cause more harm than a factual but incomplete communication

## When not to use it

- Routine status updates after a resolved incident — use [Incident Report Style](incident-report-style.md) instead
- Strategic decisions triggered by a crisis — use [Board Paper Style](board-paper-style.md) or [Executive Briefing](executive-briefing.md) instead
- Performance updates or operational summaries — use [Smart Brevity](axios-smart-brevity.md) instead

## Core structure

```
[HEADLINE / SUBJECT]
What happened. Direct and factual. Not a euphemism.
"Service Outage — Payment Processing Unavailable"
Not "Update on Recent Technical Events"

[WHAT WE KNOW]
The confirmed facts as of the time of writing.
Specific times, systems, and populations affected.
What the reader needs to know to act or prepare.

[IMPACT]
Who is affected. In what way. Since when.
Quantified where possible (number of users, percentage of traffic, etc.).
Geographic scope if relevant.

[WHAT WE ARE DOING]
Specific, active steps being taken right now.
Not "we are investigating" — "our infrastructure team is restarting the affected queue consumers"
What has already been done. What is in progress. What is planned next.

[WHAT WE DO NOT YET KNOW]
Explicit acknowledgement of open questions.
Root cause, full scope, estimated resolution time — if unknown, say so.
Do not speculate. Say "we are investigating X and will confirm Y by Z."

[NEXT UPDATE]
Exactly when the next communication will be sent.
Through what channel.
Who to contact if the reader needs help now.

[CONTACT]
How to reach the team for urgent help.
Support channel, email, or phone number.
```

## Copy-paste prompt

```
You are a crisis communications expert. Your task is to write a clear, factual incident update from the following brief.

AUDIENCE: [AUDIENCE — e.g. "All customers of the payment processing platform", "All employees of the company", "Shareholders and board members", "Regulatory body receiving a mandatory notification"]
PURPOSE: [PURPOSE — e.g. "Initial notification of a payment processing outage to affected customers", "Internal update to all staff during an active security incident", "First customer communication following a data breach"]
CONTEXT: [CONTEXT — e.g. "Outage began at 14:20 GMT; root cause not yet confirmed; approximately 2,000 transactions have failed; the engineering team is actively working on resolution"]
INPUT: [INPUT — paste all confirmed facts, timeline, affected systems, actions underway, and open questions here. Separate confirmed facts from things still under investigation.]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Customers understand what has happened, what they should do if affected, and when they will hear next — without needing to contact support for this information"]
TONE: [TONE — e.g. "Calm and factual — not apologetic or defensive", "Direct and transparent — no corporate euphemisms", "Empathetic but matter-of-fact"]
LENGTH: [LENGTH — e.g. "Under 300 words for an initial incident update", "400–600 words for a customer data breach notification"]
FORMAT: [FORMAT — e.g. "Headed sections: What We Know / Impact / What We Are Doing / What We Do Not Yet Know / Next Update", "Plain email format without headers"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not speculate on root cause before forensic investigation is complete", "Do not include any figures that have not been confirmed by the security team", "This communication will be shared with the ICO — language must be precise and factual"]

INSTRUCTIONS:
1. Begin with a clear, direct headline or subject line that states what happened. Do not use euphemisms or vague language.
2. State the confirmed facts first. Use specific times, system names, and affected populations. Do not combine confirmed facts with speculation.
3. State the impact clearly: who is affected, how, and since when. Quantify where possible.
4. Describe the specific actions being taken — not "we are working on it" but what specifically is being done, by whom, and what the next action is.
5. Explicitly acknowledge what is not yet known. This is not a weakness — it is what builds trust.
6. State the exact time and channel of the next update. Do not leave any ambiguity.
7. Provide a clear contact for people who need help now.
8. Use British English throughout (colour, organisation, licence, favour, etc.).
9. Preserve all confirmed facts exactly as provided in [INPUT]. Do not add information not confirmed. Do not omit confirmed information that is material to the audience.
10. Clearly separate confirmed facts from those still under investigation. Anything uncertain must be framed as "we are investigating" — not stated as fact.

Output the crisis communication only. No preamble, no commentary.
```

## Output format

A crisis communication is typically delivered as an email, a status page update, a Slack or Teams message, or an SMS. The format depends on the channel, but the content structure is consistent:

- **Subject or headline**: States what happened — factual, direct, no euphemism
- **Body**: Short paragraphs (2–3 sentences each); white space is essential for legibility under stress
- **Headed sections** (for longer notifications): What We Know / Impact / What We Are Doing / What We Do Not Yet Know / Next Update
- **Contact information**: At the end; clearly labelled
- **Timestamp**: Date and time of the communication clearly stated
- **No bullet points for the "What We Are Doing" section**: Bullet points imply static status; use prose to convey active work

Length: 200–300 words for an initial internal update; 350–600 words for an external customer notification. A brief, honest, incomplete update sent quickly is always better than a comprehensive, polished update sent late.

## Example

**Subject: Payment Processing Service Disruption — Update at 15:00 GMT**

*Sent: 14 May 2026, 15:02 GMT*

Our payment processing service has been unavailable since approximately 14:20 GMT today. Customers attempting to make purchases on our platform are receiving an error message and transactions are not completing.

**What we know**

The service failure began at 14:20 GMT. Our monitoring system detected a database connection pool exhaustion event at 14:22 GMT. The engineering team identified that a scheduled data migration job launched at 14:15 GMT was consuming connections at a rate that exceeded the pool configuration. The payment API began rejecting new requests at 14:20 GMT when the pool was fully exhausted.

At 14:45 GMT, we deployed an emergency configuration change to increase the connection pool capacity. This has partially restored service — approximately 60% of transaction requests are now completing successfully. Full restoration is in progress.

**Impact**

Approximately 2,000 attempted payment transactions failed between 14:20 GMT and 14:45 GMT. Customers who attempted a payment during this window will have received an error message; their payment has not been taken and their card has not been charged. We are contacting affected customers individually.

**What we are doing**

Our infrastructure team is completing the connection pool reconfiguration and scaling the migration job to run during an off-peak window tonight. We expect full service restoration by 15:30 GMT.

**What we do not yet know**

We are still investigating whether the data migration job was scheduled correctly or whether a configuration error caused it to run at peak trading hours. We will include root cause analysis in the post-incident report.

**Next update**

We will send an update at 16:00 GMT confirming service restoration or providing a revised timeline. We will publish a full post-incident report within 48 hours.

**Need help now?**

If you attempted a payment between 14:20 and 14:45 GMT and need urgent assistance, contact our support team at support@company.com or call 0800 000 0000.

---

## Quality checklist

- [ ] Subject or headline states what happened — direct and factual, no euphemism
- [ ] Confirmed facts are stated separately from things still under investigation
- [ ] Impact is quantified: who is affected, how many, since when
- [ ] Actions described are specific — not "we are working on it"
- [ ] Unknown factors are explicitly acknowledged — not omitted
- [ ] Next update time and channel are stated precisely
- [ ] Contact information is clear and actionable
- [ ] No premature reassurance ("everything will be fine") without factual basis
- [ ] Timestamp of the communication is clearly stated
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Euphemistic headline ("Technical event," "Service update") | Reader does not understand the severity; trust erodes | State what happened directly: "Payment Service Outage" |
| Downplaying severity | Feels dishonest; destroys trust when full truth emerges | State impact accurately: give real numbers of affected users |
| Premature reassurance ("Our systems are secure") | Unverifiable during active incident; sounds like PR | Only state what is confirmed; say "we are investigating" for unknowns |
| Vague about actions ("We are working on it") | Reader has no confidence anything is being done | Describe specific actions: what, who, what is next |
| No acknowledgement of unknowns | Appears like a cover-up | Explicitly name what you do not yet know |
| No next update time | Audience feels abandoned and speculates | Always state exactly when the next update will come |
| Long delay before first communication | Silence breeds rumour | Send a brief, honest, incomplete update fast — then follow with detail |

---

See [prompt-templates/incident-report-prompts.md](../prompt-templates/incident-report-prompts.md) for post-incident analysis.
