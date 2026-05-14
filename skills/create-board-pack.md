---
title: Create Board Pack
skill_type: Document generation
output: A complete board meeting package including cover letter, agenda, individual board papers, financial summary, and decision templates — typically 20–40 pages in total
tools_needed: LLM (Claude/ChatGPT/Gemini), Word or Google Docs, PDF converter
difficulty: Complex
---

# Skill: Create Board Pack

## What this skill does

Assembles and drafts all materials required for a board meeting: the agenda with time allocations, individual board papers for each substantive item, a financial performance summary, a risk update, and formal decision or resolution templates. Each board paper follows the same structure — executive summary, background, options analysis, recommendation, risk assessment — so the board can navigate the pack consistently. The LLM helps draft each paper and the connecting materials; a human reviewer must check legal accuracy, financial figures, and compliance requirements before distribution.

## When to use it

- Preparing quarterly or annual board meetings where formal papers are required
- Seeking board approval for a major capital investment, strategic initiative, or policy change
- Creating the governance documentation package for an audit, regulatory review, or investor due diligence exercise
- Onboarding a new company secretary who needs a template set to work from
- Producing a special board meeting pack for an urgent decision (M&A, crisis response, leadership change)

## Inputs required

- Meeting date, location, and list of attendees (directors, executives, company secretary)
- Agenda items with the type of action required for each (decision, noting, discussion)
- For each major paper: background context, options considered, financial data, recommendation, and key risks
- Current financial performance data (P&L summary, cash position, key variances)
- Any standing items (approval of previous minutes, matters arising, risk register update)
- Regulatory or legal requirements specific to the entity type (plc, private, charity, etc.)
- Any pre-read materials that should accompany but not form part of the formal pack

## Copy-paste prompt

```
You are a company secretary and governance specialist. Draft a board pack for the meeting described below.

AUDIENCE: [e.g. PLC board / Private company directors / Trustee board / Advisory board]
PURPOSE: [Primary decisions and matters the board must address at this meeting]
CONTEXT: [Company stage, sector, any recent events or context the board is aware of]
INPUT: [Paste agenda items, background notes, financial data, and any existing drafts here]
DESIRED_OUTCOME: [What decisions must be made and what the board should know by the end of the meeting]
TONE: Formal and precise. Board papers are legal documents — language must be unambiguous.
LENGTH: Cover letter 1 page; agenda 1 page; each board paper 3–5 pages; financial summary 2 pages; appendices as needed. Total pack 20–40 pages.
FORMAT: Each section as a separate clearly labelled document within the pack. Each board paper must have: paper number, title, author, date, status (for decision / for noting / for discussion), executive summary, background, analysis, recommendation, financial implications, risk assessment, and proposed resolution wording.
CONSTRAINTS: Use British English. All financial figures in £ with consistent decimal places. Use passive voice sparingly — prefer "The board resolved to..." over "It was resolved that..." Output only the pack content; no preamble.

QUALITY BAR:
- Every decision item must have proposed resolution wording.
- Every financial figure must reconcile across the pack.
- Facts, assumptions, estimates, and recommendations must be visibly separate.
- Do not invent legal, tax, regulatory, or financial claims. Flag missing inputs instead.

PACK STRUCTURE:
1. Cover letter from Chair or CEO (1 page)
2. Agenda with time allocations
3. Board Paper 1: [First agenda item]
4. Board Paper 2: [Second agenda item]
5. [Additional papers as needed]
6. Financial Performance Summary
7. Risk Register Update
8. Any Other Business items
9. Decision/Resolution Templates (one per paper requiring a vote)
```

## Suggested output structure

- **Cover letter** — from the Chair or CEO; summarises the key agenda items; flags any pre-reading required; confirms quorum
- **Agenda** — numbered items with time allocations, action type (decision/noting/discussion), and paper reference number
- **Board Paper(s)** — one per substantive agenda item; each containing:
  - Paper number, title, author, date, status
  - Executive summary (half page maximum)
  - Background and context (1–2 pages)
  - Options analysis (if decision required)
  - Recommendation with rationale
  - Financial implications
  - Risk assessment
  - Proposed resolution wording
- **Financial performance summary** — P&L highlights, cash position, key variances vs. budget, year-on-year comparisons
- **Risk register update** — top risks, changes since last meeting, mitigations
- **Resolution templates** — pre-drafted formal wording for each vote

## Quality controls

- [ ] Every agenda item that requires a decision has a corresponding board paper with proposed resolution wording
- [ ] Each board paper is self-contained — a director can read any single paper without needing to cross-reference others
- [ ] Financial figures are internally consistent across all papers and the financial summary
- [ ] The pack can be reviewed in full in under 3 hours (this is the practical limit for non-executive directors)
- [ ] All recommendations have a clear rationale — "we recommend Option B because..." not just "we recommend Option B"
- [ ] Legal or compliance implications are flagged and the company's legal adviser has reviewed those sections
- [ ] Version, date, and "CONFIDENTIAL" classification appear on every page

## Common failure modes

- **Papers too long**: Board members read packs in limited time; papers over 5 pages are rarely read in full — move detail to appendices and keep the main paper tight
- **Recommendation buried**: The executive summary should state the recommendation in the first sentence; never make the board wade through background to find what they are being asked to decide
- **Inconsistent financials**: If the P&L summary shows different numbers from the board paper, trust collapses — have one person reconcile all figures before distribution
- **Missing resolution wording**: Without precise proposed resolution text, the meeting may produce ambiguous minutes — draft resolution wording for every decision item
- **No options analysis**: A paper that presents only one option looks like a fait accompli and invites board resistance — always show at least two alternatives and explain why you are not recommending them

## Example request

"Draft the board pack for our Q2 board meeting on 15 June. The key agenda item is approval of the Azure cloud migration (Phase 1, £600k, 18-month programme). Also include the Q1 financial performance paper (revenue £4.2M, 12% ahead of budget; EBITDA £820k), a risk register update (two new risks: AI governance and supplier concentration), and the standard approval of Q1 board minutes. We are a private limited company in financial services. Directors: CEO, CFO, CTO, two independent NEDs."
