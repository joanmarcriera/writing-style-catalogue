---
title: Create One-Page Brief
skill_type: Document generation
output: A single-page summary document that conveys a complex situation, recommendation, or decision request to a busy senior reader in under two minutes
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor or Word
difficulty: Easy
---

# Skill: Create One-Page Brief

## What this skill does

Distils complex information — a project update, business case, policy proposal, or strategic decision — into a single, scannable page structured for a senior audience. The one-pager leads with the key message or ask, supports it with the minimum necessary evidence, and ends with a clear next step. It is not a summary of everything you know; it is a carefully curated set of the facts that drive a specific decision or action. Brevity is the point: if it needs two pages, it is not a one-pager.

## When to use it

- Requesting capital approval or budget sign-off from the CFO or board
- Briefing a new stakeholder on a project or initiative before a meeting
- Providing an executive with context before a media interview, negotiation, or client call
- Summarising a complex tax or regulatory issue for a non-specialist decision-maker
- Pitching a new initiative to a leadership team that has limited time for long documents
- Providing a "leave-behind" after a meeting that reinforces the main ask

## Inputs required

- The single decision or action you are requesting — stated precisely
- 3–5 supporting facts that make the case for that decision (numbers are better than assertions)
- The most important risk or counter-argument (omitting it reduces credibility)
- A clear deadline or timing reason ("we need a decision by 30 May because...")
- The audience's existing knowledge level — what do they already know?
- Any non-negotiable constraints (budget caps, regulatory requirements)

## Copy-paste prompt

```
You are a senior communications adviser. Write a one-page executive brief on the topic below.

AUDIENCE: [e.g. CFO / Board chair / CIO / Hiring manager / Client partner]
PURPOSE: [The single thing this brief must achieve — approval, awareness, decision, or action]
CONTEXT: [What the reader already knows; what has changed recently that makes this relevant]
INPUT: [Paste your raw notes, data, or background information here]
DESIRED_OUTCOME: [Exact decision or action you need the reader to take, and by when]
TONE: [e.g. Formal and direct / Professional and confident / Measured and objective]
LENGTH: Exactly one printed page — approximately 400–500 words including heading and subheadings
FORMAT: Use a bold headline (one sentence, the main message), then short labelled sections with 1–3 bullets each. No paragraphs longer than two sentences. Close with a single "Ask" or "Next Step" line in bold.
CONSTRAINTS: Use British English. Lead with the recommendation or ask — never bury it. Quantify every claim where data exists. Do not include nice-to-know background; include only must-know facts. Output only the brief; no preamble.

STRUCTURE:
**[Headline — the key message in one sentence]**

**Situation** — [2–3 bullets: what is happening and why it matters now]
**Recommendation** — [1–2 bullets: what you propose and why it is the right choice]
**Supporting evidence** — [2–3 bullets: key data points, comparisons, or precedents]
**Risks and mitigations** — [1–2 bullets: the most important risk and how it is managed]
**Ask** — [One sentence: specific decision or action needed, with deadline if applicable]
```

## Suggested output structure

- **Headline** — one sentence that states the recommendation or key finding; not a topic label
- **Situation** — 2–3 bullets explaining what is happening and why it requires a decision now
- **Recommendation** — what you are proposing; keep to 1–2 bullets
- **Supporting evidence** — the 2–3 data points or facts that most strongly support the recommendation
- **Key risk** — one bullet on the most important downside and how it is mitigated
- **Ask** — one bold sentence stating exactly what you need, from whom, and by when

## Quality controls

- [ ] The document fits on one printed A4 page (test in print preview before finalising)
- [ ] The headline states the recommendation or finding — not the topic
- [ ] Every bullet is one sentence or fewer; no bullet exceeds 20 words
- [ ] At least two data points with specific numbers (not "significant savings" but "£1.5M annually")
- [ ] The "Ask" is unambiguous — the reader knows exactly what they are being asked to do
- [ ] A senior executive can read it cold and understand the key message in under 90 seconds
- [ ] British English used throughout; no Americanisms

## Common failure modes

- **Too long for one page**: Start by listing only the must-know facts; cut everything that is merely useful-to-know. If still too long, split the brief into two versions: one for the decision-maker, one as a supporting note
- **Buried ask**: If the reader reaches the end before they know what you need, rewrite — the ask should appear in the headline or the first section
- **Vague headline**: "Cloud Migration Update" is a topic; "Approving Azure migration will save £800k per year from 2027" is a message — always use the latter form
- **Missing the "why now"**: Decision-makers deprioritise briefs that lack urgency; always include a timing reason in the Situation section
- **All assertion, no evidence**: "This is the right approach" without numbers or comparisons will not persuade a CFO — replace assertions with data

## Example request

"Write a one-page brief for our CFO requesting approval to proceed with Phase 1 of the Azure cloud migration. Total Phase 1 cost is £600k. Expected savings: £1.5M annually from year 2, payback in 18 months. The current on-premise contract renews in September — if we miss this window we lose £200k in early-exit savings. Three alternatives were assessed; Azure was selected on cost, compliance, and vendor support grounds. Approval needed by 31 May to meet procurement timelines."
