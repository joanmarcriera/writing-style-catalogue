---
title: Executive Update Workflow
category: Workflow
---

# Workflow: Creating an Executive Update

An executive update is a periodic communication — monthly, quarterly, or event-driven — that keeps senior leadership and investors informed about performance, progress, and priorities. The goal is not to report everything; it is to surface the most important 3–5 facts, place them in context, acknowledge challenges honestly, and state what decisions or support you need. This workflow takes you from raw data to a polished, board-ready update in under a day.

## Style to use

[Smart Brevity](../styles/axios-smart-brevity.md) — the Smart Brevity framework is built for this context: headline first, facts in bullets, no filler. Executives read updates between meetings; if the opening sentence does not earn their attention, the rest will not be read. Use [Investor Update Style](../styles/investor-update-style.md) if the audience includes external investors or shareholders.

## Skill to use

[Create One-Page Brief](../skills/create-one-page-brief.md) for a concise update under 500 words, or [Create Executive Memo](../skills/create-executive-memo.md) for a longer, more detailed communication requiring a specific decision.

## Prompt template to start from

[Executive Summary Prompts](../prompt-templates/executive-summary-prompts.md)

## Inputs required

Before starting, gather the following:
- Financial performance: revenue, growth rate, margin, cash position — actuals vs. plan
- Operational highlights: 2–3 significant achievements this period with specific outcomes
- Challenges: 1–2 honest statements of what is not going to plan and what you are doing about it
- Forward look: top 3 priorities for the next period with milestones
- Ask (if any): the specific decision, resource, or input you need from the leadership team
- Audience's existing context: what do they already know? What is new?

## Copy-paste master prompt

```
You are a senior communications specialist. Write a concise executive update for the period described below.

AUDIENCE: [e.g. Board of directors / Investor group / Executive leadership team]
PURPOSE: To keep senior stakeholders informed about performance, progress, and priorities; to flag challenges transparently; and to state any asks clearly.
CONTEXT: [Organisation type and size; what has happened since the last update; any particularly significant events]
INPUT:
Financial performance: [Revenue £X, growth Y%, margin Z%, cash £W — vs. plan: ahead/on track/behind by X%]
Achievements: [List 3–5 specific achievements with measurable outcomes]
Challenges: [List 1–2 honest challenge statements with what you are doing about them]
Next period priorities: [List 3 priorities with milestones and owners]
Ask: [Any specific decision or support needed from the audience, with a deadline]
DESIRED_OUTCOME: The audience finishes reading this update fully informed, reassured about challenges, clear on priorities, and aware of what you need from them.
TONE: Confident and direct. Lead with facts. Acknowledge challenges without catastrophising. Use "we" not passive voice.
LENGTH: 400–600 words. Fits one page at standard font size.
FORMAT: Bold headline (the single most important message this period). Then sections: Performance | Highlights | Challenges | Priorities | Ask. Each section: 2–4 bullets. Final section in bold: the ask, if one exists.
CONSTRAINTS: Use British English. Every bullet must include a specific number or named fact — no vague assertions. Do not write a narrative essay — write in the Smart Brevity style: short sentences, no filler phrases. Output only the update; no preamble or meta-commentary.
```

## Step-by-step process

1. **Gather data** (45 minutes): Pull financial actuals from finance system; collect achievement notes from your team; identify 1–2 honest challenges; draft the next-period priorities list. Do not start writing until you have this raw material.

2. **Identify the headline** (15 minutes): Ask yourself: if the audience reads only one sentence, what must they know? This is your headline. Write it as a specific fact, not a topic label. "Revenue £4.2M — 8% ahead of budget" not "Revenue Update."

3. **Draft with the prompt** (30 minutes): Paste the master prompt above into Claude, ChatGPT, or Gemini. Fill in all INPUT fields with your gathered data. Run the prompt. Do not accept the first draft — read it critically.

4. **Edit for honesty** (20 minutes): Check the challenges section. If it reads as defensive or minimising, rewrite it. Decision-makers trust updates that acknowledge problems directly — "Hiring is behind plan: 4 of 8 roles unfilled; we have extended to two additional agencies" is better than "Hiring is progressing."

5. **Check the ask** (10 minutes): Is the ask specific? Does it have a deadline? Does the audience have the authority to give you what you are asking for? If the ask is missing, add it.

6. **Send for internal review** (30 minutes): Share with one peer (CFO or COO) for a sense-check on financial accuracy and tone. Incorporate feedback.

7. **Final review against checklist** (10 minutes): Use the checklist below.

8. **Distribute** (5 minutes): Send via the appropriate channel (board portal, email, or shared document).

**Total time: approximately 2.5–3 hours**

## Review checklist

- [ ] The headline is a specific fact, not a topic label
- [ ] Financial figures are actuals, not rounded estimates, and match the finance team's numbers
- [ ] Challenges are stated honestly — not buried or softened to the point of invisibility
- [ ] Every bullet contains a specific number, name, or measurable outcome
- [ ] The ask is specific, actionable, and has a deadline
- [ ] The update fits one page at standard font size
- [ ] British English throughout; no Americanisms
- [ ] Reviewed by at least one colleague before sending

## Example output excerpt

> **Revenue 8% ahead of budget — cloud costs and hiring remain the watch items.**
>
> **Performance**
> - Revenue £4.2M in Q2, up 8% vs. budget; EBITDA £820k (margin 19.5%, in line with plan)
> - Cash position £2.4M; runway 14 months at current burn rate
>
> **Highlights**
> - Closed three new enterprise contracts totalling £480k ARR; largest single deal in company history
> - Azure Phase 1 migration completed on schedule; monthly cloud spend tracking £12k below forecast
>
> **Challenges**
> - Hiring behind plan: 4 of 8 open roles unfilled; extended to two additional agencies from 1 July
>
> **Ask**
> - Board approval requested for Phase 2 scope by 15 July to preserve programme timeline
