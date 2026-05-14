---
title: Create Email Sequence
skill_type: Communication
output: A set of 3–6 coordinated emails with subject lines, body copy, send-timing guidance, and CTAs — written as a coherent campaign rather than isolated messages
tools_needed: LLM (Claude/ChatGPT/Gemini), Email platform (Outlook, Gmail, Mailchimp, HubSpot)
difficulty: Easy
---

# Skill: Create Email Sequence

## What this skill does

Develops a series of coordinated emails — each with its own angle, subject line, and call to action — that work together to achieve a single campaign goal over a defined period. Each email builds on the previous one without repeating it. The sequence is designed for a specific audience in a specific context: supplier outreach, client onboarding, candidate follow-up, or stakeholder communication. Unlike a single email, a sequence accounts for non-response and re-engages from different angles until the recipient acts or opts out.

## When to use it

- Cold outreach to potential suppliers, importers, or channel partners where multiple touchpoints are expected
- Following up with prospective clients after an initial meeting or proposal submission
- Onboarding new clients, team members, or system users through a structured information flow
- Communicating a major change (system migration, policy update, leadership change) in stages to allow time to absorb
- Reactivating dormant contacts or lapsed customers with a structured re-engagement campaign

## Inputs required

- Campaign goal: what the sequence must achieve (a meeting booked, a decision, a form completed)
- Target audience: who they are, what they care about, what they are currently experiencing
- Number of emails and the timing between them (e.g. Day 1, Day 4, Day 9)
- Key messages and value propositions — what is the offer or reason to engage?
- Specific CTA for each email — does it escalate (low-friction first, higher ask later)?
- Tone and sender persona: formal professional, friendly peer, brief and direct?
- Any personalisation tokens available (first name, company name, specific product referenced)

## Copy-paste prompt

```
You are a professional copywriter specialising in B2B and professional services communication. Write an email sequence for the campaign described below.

AUDIENCE: [Who receives these emails — role, seniority, sector, what they care about]
PURPOSE: [What this sequence must achieve — meeting, reply, decision, purchase, action]
CONTEXT: [Why you are contacting them; what relationship exists; what they already know]
INPUT: [Key facts about your offering, value propositions, case studies, or talking points]
DESIRED_OUTCOME: [The specific action the final email in the sequence should produce]
TONE: [e.g. Formal and measured / Direct and brief / Warm and collegial / Professional but human]
LENGTH: [Number of emails; timing between each, e.g. Day 1, 4, 9, 16]
FORMAT: For each email output: (1) Send timing; (2) Subject line (two options); (3) Full email body; (4) CTA instruction; (5) Brief note on the angle or strategy for this email.
CONSTRAINTS: Use British English throughout. Each email must feel independently readable — assume the reader has not seen the previous one. No email should exceed 200 words of body text. Subject lines under 50 characters. Avoid hollow openers ("I hope this finds you well", "Following up on my previous email"). Output only the sequence; no preamble.

SEQUENCE STRATEGY:
- Email 1: Lead with a specific insight about their situation or sector; introduce yourself briefly; low-friction CTA (a question, not a meeting request)
- Email 2: Provide value — a relevant case study, data point, or tool — before asking for anything
- Email 3: Address the most common objection directly; re-state what you offer in a different way
- Email 4 (if needed): Social proof or peer reference; create mild urgency without fabricating scarcity
- Final email: Brief close — acknowledge you will not follow up again; leave door open professionally
```

## Suggested output structure

- **Email 1 — Hook and introduction** (Day 1): Specific insight + who you are + one low-friction question as CTA
- **Email 2 — Value add** (Day 3–4): Share something useful (data, case study, tool) before asking for anything; light CTA
- **Email 3 — Reframe** (Day 8–10): Different angle on the same proposition; address the obvious objection; meeting request CTA
- **Email 4 — Social proof** (Day 15–16): Reference a peer or comparable organisation; mild timing reason; repeat meeting CTA
- **Email 5 — Close** (Day 22–28): Acknowledge you are signing off; one final door left open; no pressure

## Quality controls

- [ ] Each email reads independently — context is not assumed from previous emails
- [ ] No email repeats the same subject line angle twice
- [ ] CTA escalation is logical: low-friction first, higher commitment later
- [ ] Every email has one and only one CTA — not three options
- [ ] No email exceeds 200 words of body copy (excluding subject line and sign-off)
- [ ] Tone is consistent with the sender persona across all emails
- [ ] British English throughout; no Americanisms

## Common failure modes

- **All emails sound the same**: If every email says "I wanted to follow up", the reader tunes out after email 1 — vary the angle completely for each email
- **CTA escalates too fast**: Asking for a 45-minute meeting in Email 1 kills response rates — start with a yes/no question or a simple reply
- **Over-personalisation with sparse data**: "[FIRST NAME], I saw you recently attended [EVENT]" looks creepy if the data is wrong — use personalisation tokens only when the data is reliable
- **Too long**: Professional sequences in B2B contexts should be brief; long emails signal that the sender has not respected the reader's time — cut to 150 words maximum
- **No logical sequence**: Each email should feel like a natural continuation of a professional relationship, not a new cold outreach — reference previous context subtly

## Example request

"Write a 4-email outreach sequence targeting operations directors at UK food importers. Our company provides cold-chain logistics software that reduces spoilage by an average of 18%. The goal is to book a 20-minute discovery call. Tone: direct and professional. Timing: Day 1, 4, 10, 18. The sector is dealing with rising energy costs and post-Brexit import complexity, which we should reference. British English. No marketing fluff."
