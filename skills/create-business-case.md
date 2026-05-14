---
title: Create Business Case
skill_type: Document generation
output: A comprehensive investment justification document with financial analysis, strategic rationale, options assessment, risk register, and implementation plan — typically 8–15 pages
tools_needed: LLM (Claude/ChatGPT/Gemini), spreadsheet (Excel or Google Sheets for financial modelling), Word or PDF converter
difficulty: Complex
---

# Skill: Create Business Case

## What this skill does

Builds a structured document that justifies a proposed investment or change to a decision-making body — typically a board, investment committee, or senior leadership team. A business case does not sell an idea; it presents a rigorous, balanced analysis that allows decision-makers to evaluate the proposal on its merits. It must cover the problem being solved, the options considered, the financial analysis (costs, benefits, ROI, payback), the risks, and the implementation plan. The LLM is effective at structuring the narrative and drafting sections; the financial model must be built in a spreadsheet and verified by the finance team.

## When to use it

- Seeking board or investment committee approval for a capital expenditure (cloud migration, ERP implementation, data centre exit)
- Justifying a new programme or team that requires budget allocation outside the normal planning cycle
- Supporting an M&A, JV, or partnership decision with a documented financial and strategic rationale
- Responding to a regulatory requirement or audit finding that requires a funded remediation programme
- Building the internal case for a technology refresh or security uplift programme

## Inputs required

- The initiative being proposed — named and described precisely
- The problem or opportunity it addresses — with evidence (cost data, incident history, regulatory requirement, market data)
- The options considered — minimum two alternatives plus the "do nothing" baseline
- Financial data for each option: one-off costs, ongoing costs, expected benefits (quantified), timing
- NPV/IRR/payback period calculations (from the finance team or your own model)
- Risk assessment: what could go wrong and how it affects the financials
- Implementation plan: phases, timeline, ownership, key milestones
- Strategic context: how this initiative connects to organisational strategy

## Copy-paste prompt

```
You are a management consultant and business analyst. Write a business case for the investment described below.

AUDIENCE: [Who makes the decision — e.g. board investment committee / CFO and CTO / senior leadership team]
PURPOSE: [To justify a specific investment and obtain approval from the decision-making body]
CONTEXT: [Organisational context; current state; any prior decisions or commitments related to this proposal]
INPUT: [Describe the initiative; the problem it solves; the options considered; financial data for each option; key risks; implementation plan outline]
DESIRED_OUTCOME: [Approval to proceed with the recommended option, with budget and resource commitment from the decision-making body]
TONE: Formal, objective, and evidence-led. A business case must be credible to a sceptical CFO — every claim must be supported by data.
LENGTH: 8–15 pages excluding financial appendices. Executive summary 1 page; body sections 7–12 pages; appendices as needed.
FORMAT: Numbered sections. Financial data in clearly labelled tables. Options presented in a comparison table. Risk register in standard table format. Use H2 for major sections.
CONSTRAINTS: Use British English. Present all financial figures in £ with consistent decimal places. Do not cherry-pick — present the full financial picture including worst-case scenarios. "Do nothing" must be an explicit option with its own costs and consequences. Output only the business case; no preamble.

STRUCTURE:
1. Executive Summary (1 page — recommendation, cost, benefit, ROI, ask)
2. Background and Strategic Context
3. Problem Statement and Current State
4. Options Analysis
   4.1 Option 1: Do nothing
   4.2 Option 2: [Alternative]
   4.3 Option 3: Recommended option
5. Financial Analysis
   5.1 Cost summary
   5.2 Benefit summary
   5.3 NPV, IRR, payback period
   5.4 Sensitivity analysis
6. Risk Assessment
7. Implementation Plan
8. Recommendation
9. Appendices (detailed financial model, technical specifications, vendor assessment)
```

## Suggested output structure

- **Executive summary** — recommendation, total investment, total NPV benefit, payback period, and specific ask (approval of £X for Option Y)
- **Background** — why this is needed now; regulatory, competitive, or operational driver
- **Problem statement** — evidence of the current-state cost or risk (quantified where possible)
- **Options analysis** — 3 options (do nothing, partial solution, full solution); comparison table; clear recommendation
- **Financial analysis** — 5-year cost/benefit model; NPV; IRR; payback period; sensitivity table showing what happens if benefits are 20% lower or costs 20% higher
- **Risk assessment** — risk register table (top 8–10 risks); residual risk after mitigations
- **Implementation plan** — phased timeline; milestones; governance; resource requirements
- **Recommendation** — restate the recommendation; specify what is being asked (budget, headcount, approval authority)

## Quality controls

- [ ] "Do nothing" is an explicitly costed option — not a straw man but a genuine baseline with its own costs and consequences
- [ ] Financial claims are traceable to a source or model — not asserted without basis
- [ ] Sensitivity analysis shows the case at 80% of expected benefits and 120% of expected costs — decision-makers need to know the worst case
- [ ] Executive summary is self-contained — a decision-maker can read only the executive summary and have what they need to decide
- [ ] Risk register includes risks to the business case itself (delay, cost overrun) not just project risks
- [ ] Implementation plan is realistic — phases have named owners and the timeline allows for procurement and onboarding

## Common failure modes

- **No "do nothing" option**: Omitting "do nothing" makes the business case look like a foregone conclusion — always cost the status quo baseline, including its ongoing costs and risks
- **Benefits overestimated**: LLMs will state benefit claims that are aspirational rather than evidenced — every benefit must be traceable to a specific assumption; add a sensitivity table to show the case survives if benefits are lower than expected
- **Financial figures not verified by finance**: A business case written without finance team input on the numbers will be challenged in the room — involve finance before submission
- **Strategy section disconnected**: A business case that does not connect the investment to a named strategic objective looks opportunistic — reference the specific strategy document or board directive
- **Ask not specific**: "We would welcome board support" is not an ask — "We request board approval for £2.1M capital expenditure, to be allocated from the 2025/26 capex budget, with authority to proceed delegated to the CTO" is an ask

## Example request

"Write a business case for our Azure cloud migration programme (18-month, 3-phase programme). Investment: £2.1M one-off, £420k ongoing per year (cloud costs). Current on-premise costs: £1.22M per year. Expected savings from year 2: £800k per year vs. current state. Strategic context: digital transformation strategy 2024–2027 commits to exiting all on-premise infrastructure by 2027. Regulatory driver: FCA operational resilience requirements around disaster recovery. Options: (1) do nothing and renew on-premise contracts, (2) partial migration (non-critical systems only), (3) full migration (recommended). Decision-maker: board investment committee. British English. Executive summary must fit one page."
