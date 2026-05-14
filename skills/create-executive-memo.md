---
title: Create Executive Memo
skill_type: Document generation
output: A formal 1–2 page memo that briefs a senior executive on a strategic or operational matter, states a clear recommendation, and requests a specific decision or action
tools_needed: LLM (Claude/ChatGPT/Gemini), Word or Google Docs
difficulty: Easy
---

# Skill: Create Executive Memo

## What this skill does

Writes a formal memorandum for executive review on strategic or operational matters. The memo follows the BLUF (Bottom Line Up Front) structure: it states the recommendation or key finding in the first sentence, then provides supporting evidence, and ends with a specific ask and timeline. Unlike a board paper, a memo is a lean, fast-read document — never more than two pages — designed for an executive who has limited time and needs a clear answer quickly. It is the workhorse of senior internal communications.

## When to use it

- Proposing a policy change and requesting sign-off before implementation
- Briefing a CIO, CFO, or CEO on an emerging risk that requires a decision this week
- Requesting budget or resource approval outside the normal annual planning cycle
- Communicating the outcome of an analysis or review and recommending next steps
- Escalating a supplier, compliance, or personnel issue that requires executive awareness
- Providing a written record of a verbal decision for governance and audit purposes

## Inputs required

- The recipient (name, title, and their level of familiarity with the topic)
- The recommendation or key message — stated in one sentence before drafting begins
- 3–5 supporting facts, data points, or analysis findings
- The specific action or decision needed from the recipient
- The deadline by which the decision is required and why
- Any stakeholders who have already been consulted or who will be affected
- Any constraints (budget limits, regulatory requirements, existing commitments)

## Copy-paste prompt

```
You are a senior communications specialist. Write a formal executive memo for the recipient described below.

AUDIENCE: [Name and title of recipient, e.g. "Sarah Chen, Chief Financial Officer"]
PURPOSE: [The single thing this memo must achieve — approval, awareness, escalation, or decision]
CONTEXT: [Background the recipient needs; what they already know; what has changed recently]
INPUT: [Paste your supporting facts, analysis findings, or raw notes here]
DESIRED_OUTCOME: [The exact decision or action you need, and by when]
TONE: Formal and direct. Memos are internal professional documents — clear, unambiguous, no padding.
LENGTH: 1–2 pages maximum. 400–600 words of body text.
FORMAT: Standard memo header (TO / FROM / DATE / RE), then structured body with labelled sections. Use short paragraphs (2–3 sentences maximum). Use numbered bullets for lists of facts or options. Bold the key recommendation.
CONSTRAINTS: Use British English. Lead with the recommendation — never bury it after background. Every claim must be supported by a specific fact or figure from the input. Avoid hedge phrases ("it might be considered that...") — state your view clearly. Output only the memo; no preamble.

STRUCTURE:
TO: [Recipient name and title]
FROM: [Author name and title]
DATE: [Date]
RE: [Clear subject — state the topic and action in 8 words or fewer]

**Recommendation** (first paragraph): State the recommendation or key finding in the opening sentence.

**Background** (1 short paragraph): Provide the minimum context the recipient needs. Do not repeat what they already know.

**Analysis** (2–4 bullets): The key facts that support the recommendation.

**Risks and considerations** (1–2 bullets): The most important downside or constraint.

**Action required**: State precisely what you need from the recipient and by when.
```

## Suggested output structure

- **Header block** — TO, FROM, DATE, RE (subject line should state topic and action, not just topic)
- **Recommendation** — first paragraph, first sentence; state what you recommend and why in brief
- **Background** — one short paragraph; context only, no history lesson
- **Supporting evidence** — 3–4 numbered points with specific data
- **Risks** — 1–2 bullets on the most material risks; include mitigations
- **Action required** — one paragraph: what you need, who decides, and the deadline

## Quality controls

- [ ] Recommendation appears in the first paragraph, first sentence
- [ ] Subject line (RE:) states what decision or action is needed — not just the topic
- [ ] Body is 2 pages or under at standard font size (11pt, 2.5cm margins)
- [ ] Every assertion is backed by a specific number or named fact
- [ ] Action required is unambiguous — the reader knows exactly what to do
- [ ] Tone is direct without being abrupt; no unnecessary softening language
- [ ] British English throughout; no Americanisms

## Common failure modes

- **Burying the recommendation**: Starting with two paragraphs of background before getting to the point — executives stop reading; put the ask first
- **Vague subject line**: "RE: Cloud Migration" tells the reader nothing about what they need to do; "RE: Approval required — Azure migration Phase 1, £600k" is actionable
- **Too much background**: If the recipient already knows the context, omit it; if they need it, one paragraph is enough — memos are not reports
- **Passive voice overuse**: "It is recommended that..." is weaker than "I recommend..." — use first person for recommendations
- **No deadline**: An action request without a "by when" will be deprioritised — always include the date a decision is needed and why

## Example request

"Write an executive memo to the CTO requesting approval to engage an external penetration testing firm for our annual security review. Budget required: £45k. The current supplier's contract expires next month and we must act to maintain ISO 27001 certification. Three vendors were shortlisted; we recommend CyberShield Ltd based on their sector experience and fixed-price model. Decision needed by 20 May to meet the June testing window. Author: Head of Information Security."
