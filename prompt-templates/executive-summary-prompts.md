---
title: Executive Summary Prompts
template_type: Executive Summary
use_case: Distil a detailed document or complex situation into a one-to-two page executive brief that enables a senior audience to understand the issue and make a decision.
audience: C-suite, board members, senior leadership, or investors with limited time
output_format: Structured summary with headline, key findings as bullets, financial or strategic impact, and a clear ask or recommendation
---

# Executive Summary Prompts

## Purpose

An executive summary is not an introduction — it is a complete, self-contained document that a senior leader can read in under five minutes and act on without reading the source material. Use this template when you have a lengthy report, business case, feasibility study, or operational review that needs to be communicated upward. It is especially useful before board meetings, investment decisions, programme approval gates, or strategic reviews. The output must answer three implicit questions the reader always has: What is happening? So what? What do you need from me?

## Copy-paste prompt

```
You are an expert executive communications specialist. Write a concise, self-contained executive summary that enables a senior leadership audience to understand the key points and take a decision without reading the underlying document.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (the full document, situation description, or detailed notes to summarise):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one page; two pages maximum]

FORMAT: [FORMAT — recommended: one-sentence headline capturing the story / key findings as bullet points / financial or strategic impact / clear ask or recommendation]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout (organise, recognise, programme, licence as noun, etc.).
2. Open with a single-sentence headline that captures the core story — not a title, but a statement (e.g. "The cloud migration programme is on track to deliver £1.8M in annual savings but requires board approval of a £3.2M investment by 30 June.").
3. Do not introduce new information not present in the input. Summarise; do not embellish.
4. Use bullet points for findings and facts. Do not write dense paragraphs that bury the point.
5. Clearly distinguish facts (confirmed data from the source), assumptions (inferred or estimated values), and recommendations (proposed actions or decisions). Use brief labels where needed.
6. Quantify financial, operational, or strategic impact wherever the source material provides the data.
7. End with a single, explicit ask: what decision, approval, or action is required, and by when.
8. Avoid unexplained jargon or acronyms. Write for a generalist senior audience, not a technical specialist.
9. Do not use filler language: no "it is important to note that", "in conclusion", or "it goes without saying". Say it plainly.
10. Where the source material is uncertain or incomplete, reflect that honestly — do not present estimates as confirmed facts.
11. Tone: [TONE].
12. Length: [LENGTH]. Cut ruthlessly to meet it.
13. Apply these constraints: [CONSTRAINTS].
14. Output only the executive summary. No preamble, no meta-commentary.
```

## Variables to customise

- `[AUDIENCE]` — who will read the summary. Examples: "Group Board of Directors", "Chief Financial Officer and Chief Operating Officer", "investment committee members with no technical background".
- `[PURPOSE]` — what the summary needs to achieve. Examples: "secure board approval for the cloud migration programme", "inform the CFO of the Q1 cost overrun and proposed remediation", "brief the investment committee before the Series B decision".
- `[CONTEXT]` — background for the LLM. Examples: "this condenses a 40-page technical feasibility report into a board-ready brief for the June meeting", "the CEO has 10 minutes before a call and needs the key points only".
- `[INPUT]` — the full source material: paste the document, report, or notes here.
- `[DESIRED_OUTCOME]` — what should happen after the reader finishes. Examples: "the board votes to approve the programme", "the CFO asks for a one-page remediation plan", "the reader understands the risk without needing the full technical appendix".
- `[TONE]` — register to use. Examples: "confident and authoritative", "cautious and balanced", "urgent but measured".
- `[LENGTH]` — target length. One page is standard; two pages is the absolute maximum for a true executive summary.
- `[FORMAT]` — structure. The recommended format above works well for most contexts.
- `[CONSTRAINTS]` — restrictions. Examples: "must not reference the vendor by name at this stage", "include IRR and payback period if available in the source", "strip all technical appendix references — those will be attached separately".

## Example input

```
AUDIENCE: Group Board of Directors (eight members; non-technical; finance and legal backgrounds predominate)
PURPOSE: Brief the board on Q1 cloud programme performance and request approval to engage a second delivery partner
CONTEXT: The cloud migration programme began in January 2026. The board receives quarterly programme updates. This is the Q1 update for the June board meeting. A programme manager report and financial summary are the source documents.
INPUT:
  Q1 Progress:
  - 38 of 112 planned workloads migrated (34% — on track against 35% Q1 target)
  - Phase 1 (pilot environment) complete and signed off
  - Azure landing zone configured and security baseline passed independent audit

  Cost position:
  - Q1 spend: £610k against £600k budget (1.7% overspend — within contingency)
  - Full-year forecast: £1.85M against £1.8M budget (£50k variance — manageable)

  Risk:
  - Original delivery partner (Nexus Solutions) at capacity from July; cannot support Phase 2 acceleration
  - Without a second partner, Phase 2 will slip by 6–8 weeks, delaying go-live to February 2027 (was October 2026)
  - A second accredited partner (CloudBridge Ltd) has been assessed and is available

  Ask:
  - Board to approve engagement of CloudBridge Ltd as second delivery partner
  - Estimated additional cost: £180k (within overall programme contingency of £220k)
  - Decision needed by 20 June to avoid Phase 2 delay
DESIRED_OUTCOME: Board approves engagement of CloudBridge Ltd at the June meeting.
TONE: Confident, transparent, measured
LENGTH: One page
CONSTRAINTS: Include all financial figures; note that the cost variance is within contingency; do not name individuals — reference roles only.
```

## Example output

---

**Cloud Migration Programme: Q1 On Track — Board Approval Requested to Engage Second Delivery Partner**

The programme is progressing to plan and within budget, but a capacity constraint with the primary delivery partner requires board approval to engage a second partner by 20 June to protect the October 2026 go-live.

**Q1 performance**
- 38 of 112 workloads migrated (34% — on plan against 35% target)
- Phase 1 pilot environment complete and signed off; Azure security baseline passed independent audit
- Q1 spend: £610k against £600k budget — 1.7% over, within the £220k programme contingency

**Risk requiring action**
The primary delivery partner (Nexus Solutions) will reach full capacity in July and cannot resource Phase 2. Without a second partner, Phase 2 delivery will slip by six to eight weeks, deferring go-live from October 2026 to February 2027 and delaying Year 2 savings of £1.8M by one quarter (estimated financial impact: £450k).

**Proposed resolution**
Engage CloudBridge Ltd — an accredited Azure partner — as second delivery partner for Phase 2. CloudBridge has been assessed by the programme team and is confirmed as available. Estimated cost: £180k, which falls within the existing contingency allowance of £220k. Total programme cost forecast remains within the approved £3.2M envelope.

*Assumption: CloudBridge availability is based on a verbal commitment received on 10 May 2026. Formal confirmation is subject to contract signature.*

**Board ask**
Approve engagement of CloudBridge Ltd as second delivery partner at the June board meeting. A decision is required by 20 June to avoid programme delay.

---

## Review checklist

- [ ] Opening sentence captures the full story in one line
- [ ] Key findings are bulleted — not buried in prose
- [ ] All financial figures from the source are included and accurate
- [ ] Facts, assumptions, and recommendations are clearly distinguishable
- [ ] The ask is explicit: what is needed, from whom, and by when
- [ ] No unexplained jargon or acronyms
- [ ] No filler language or padding
- [ ] British English spellings used throughout
- [ ] Length is within one to two pages

---

See [styles/axios-smart-brevity.md](../styles/axios-smart-brevity.md) for Smart Brevity structure.

See [styles/executive-briefing.md](../styles/executive-briefing.md) for formal executive briefing style.
