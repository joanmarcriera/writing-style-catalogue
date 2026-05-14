---
title: Cloud Migration Briefing Workflow
category: Workflow
---

# Workflow: Cloud Migration Briefing

A cloud migration briefing is the strategic communication that enables a board or executive team to make an informed decision about a major infrastructure change. It must answer three questions clearly: what are we proposing and why, what does it cost and what does it save, and what are the risks and how are they managed? This workflow covers the full process from business analysis through to board approval and implementation planning communication — including the technical, financial, and governance layers.

## Style to use

[Executive Briefing Style](../styles/executive-briefing.md) for the board or executive version — structured, formal, and conclusion-first. For the technical delivery team, use [Technical Documentation](../styles/technical-documentation.md) for architecture documents and runbooks. For the change management communication to staff, use [Narrative Storytelling](../styles/narrative-storytelling.md) to explain why the change is happening and what it means for them.

## Skill to use

[Create Business Case](../skills/create-business-case.md) for the board approval document. [Create Slide Deck](../skills/create-slide-deck.md) for the board presentation. [Create Runbook](../skills/create-runbook.md) for operational procedures during migration. [Create Risk Register](../skills/create-risk-register.md) for the programme risk documentation.

## Prompt template to start from

[Board Paper Prompts](../prompt-templates/board-paper-prompts.md) for the board document. [Presentation Prompts](../prompt-templates/presentation-prompts.md) for the slide deck.

## Inputs required

Before beginning, you need:
- Current state costs: annual infrastructure spend (hosting, hardware, maintenance, support) broken down by line item
- Proposed cloud architecture: provider, service model (IaaS/PaaS/SaaS), and migration approach (lift-and-shift, re-platform, greenfield)
- Migration cost model: one-off migration costs, and first-year and steady-state cloud costs
- Financial analysis: 5-year NPV, payback period, and sensitivity table (what if benefits are 20% lower)
- Risk register: technical, operational, financial, and regulatory risks with mitigations
- Phased implementation plan: phases, timelines, milestones, and owners
- Regulatory context: any FCA, GDPR, or sector-specific compliance implications

## Copy-paste master prompt

```
You are a management consultant and cloud transformation specialist. Produce a cloud migration briefing document for the audience described below.

AUDIENCE: [e.g. Board of directors seeking approval / CIO and CFO making a funding decision / Technical leadership team planning delivery]
PURPOSE: To enable [audience] to [approve the investment / plan the programme / understand the change].
CONTEXT: [Current infrastructure: on-premise / co-location / hybrid. Provider under consideration: AWS / Azure / GCP. Organisation size, sector, and any regulatory requirements. Any prior decisions or commitments.]
INPUT:
Current state: [Annual costs by category; performance and resilience issues; contract expiry dates]
Proposed state: [Cloud architecture; provider; migration approach; phasing]
Financial model: [One-off cost; annual cloud cost year 1 and steady-state; annual savings; NPV over [X] years; payback period]
Options considered: [Do nothing, partial migration, full migration — costs and trade-offs for each]
Risks: [Top 8 risks with likelihood, impact, owner, mitigation]
Implementation: [Phases with timeline, milestones, and owners]
DESIRED_OUTCOME: [Approval to proceed / Programme plan accepted / Change understood and supported]
TONE: [Formal and measured for board / Direct and technical for delivery team / Clear and reassuring for staff]
LENGTH: [8–12 pages for board paper / 20 slides for board presentation / 2 pages for staff communication]
FORMAT: [Board paper: numbered sections, financial tables, risk register table / Slide deck: slide-by-slide outline with speaker notes / Staff comms: narrative paragraphs with FAQ]
CONSTRAINTS: Use British English. Financial figures in £. All claims backed by specific data. "Do nothing" must be costed, not just mentioned. Output only the document; no preamble.
```

## Step-by-step process

1. **Phase 1 — Technical and financial analysis** (1–2 weeks):
   - Build the current-state cost model (pull from finance system and supplier contracts)
   - Design the target architecture with the cloud/infrastructure team
   - Build the 5-year financial model in a spreadsheet; have the CFO or finance team validate it
   - Complete the risk register with the technical and operations teams
   - Draft the phased implementation plan

2. **Phase 2 — Produce the board document** (3–5 days):
   - Use the master prompt with the [Create Business Case](../skills/create-business-case.md) skill
   - Draft the board paper covering: strategic rationale, options analysis, financial case, risk register, implementation plan
   - Internal review: CFO (financials), CTO (technical accuracy), legal counsel (regulatory implications)
   - Revise and finalise

3. **Phase 3 — Produce the board presentation** (1–2 days):
   - Use [Create Slide Deck](../skills/create-slide-deck.md) to build the 20-slide presentation
   - Key slides: current state costs, options considered, recommended approach, 5-year financial case, top risks and mitigations, phased implementation timeline, proposed resolution
   - Rehearse; anticipate CFO questions on cost assumptions and sensitivity

4. **Phase 4 — Stakeholder review** (1 week):
   - Finance: validate all cost and saving assumptions
   - Engineering: confirm technical feasibility and timeline realism
   - Operations: review runbook and operational continuity plan
   - Compliance: confirm regulatory requirements are addressed

5. **Phase 5 — Board approval** (the meeting):
   - Present the executive summary and recommendation (5 minutes)
   - Walk through the financial case and top risks (10 minutes)
   - Open for board questions (15 minutes)
   - Propose the resolution

6. **Phase 6 — Implementation communication** (post-approval):
   - Staff briefing: why are we doing this, what changes for you, when does it happen, where to get help
   - Technical team: architecture document, migration playbook, runbooks for each phase
   - Steering group: establish a monthly update pack using [Create Meeting Pack](../skills/create-meeting-pack.md)

**Total time: 6–10 weeks from initiation to board approval**

## Review checklist

- [ ] Financial model reviewed and signed off by the CFO or finance team
- [ ] "Do nothing" option is explicitly costed — annual cost, contract renewal risk, performance limitations
- [ ] Risk register covers technical, financial, regulatory, and operational risks
- [ ] Sensitivity analysis shows the case survives if benefits are 20% lower or costs 20% higher
- [ ] Implementation plan has phases with specific milestones, owners, and dates
- [ ] Regulatory implications reviewed by legal or compliance team
- [ ] Board presentation rehearsed and CFO-level questions anticipated
- [ ] British English throughout; no Americanisms

## Example output excerpt

> **5. Financial analysis**
>
> 5.1 The recommended full migration (Option 3) requires a one-off investment of £2.1M, to be funded from the 2025/26 and 2026/27 capital budgets. Annual cloud costs in steady state are modelled at £420k — a reduction of £800k per annum compared to current on-premise costs of £1.22M.
>
> 5.2 The programme produces a positive NPV of £1.9M over five years at a 10% discount rate, with a payback period of 32 months from programme completion. Under a downside scenario (cloud costs 20% higher and migration savings 20% lower than modelled), the programme remains NPV-positive at £640k.
>
> | Scenario | NPV (5-year, 10%) | Payback period |
> |----------|-------------------|----------------|
> | Base case | £1.9M | 32 months |
> | Downside (–20% savings, +20% costs) | £640k | 44 months |
> | Upside (+20% savings) | £3.1M | 24 months |
