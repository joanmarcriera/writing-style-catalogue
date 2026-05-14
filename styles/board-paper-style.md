---
title: Board Paper Style
category: Formal
aliases: [Board Pack, Formal Memo]
---

# Board Paper Style

## What This Style Is

Comprehensive, formal documentation for board-level decision-making. Includes background, options analysis, recommendation, and risk assessment. Professional formatting and thorough coverage.

**Core principle**: Complete information for informed governance decision-making.

## When to Use It

- Board meeting materials
- Major strategic decisions
- Acquisition/divestiture analyses
- Material policy changes
- Capital allocation decisions
- High-stakes governance matters

## When NOT to Use It

- Quick updates (use Smart Brevity)
- Detailed operational guidance (use Technical Documentation)
- Teaching (use Socratic)
- Quick recommendations (use BLUF or Minto)

## Core Structure

```
[TITLE PAGE]

[EXECUTIVE SUMMARY]
1-page overview of issue, options, recommendation.

[BACKGROUND]
Context; why this matters now; prior decisions.

[ANALYSIS OF OPTIONS]
For each option: pros, cons, financial impact, risks.

[BOARD RECOMMENDATION]
Which option and why; success criteria.

[GOVERNANCE AND RISK]
Legal, compliance, strategic risks; mitigation.

[IMPLEMENTATION]
Timeline; resources; dependencies; milestones.

[APPENDICES]
Detailed data, comparisons, financial models.
```

## Copy-Paste Prompt Template

```
You are a board papers expert. Create a comprehensive board paper from:

ISSUE:
[The strategic question or decision needed]

BACKGROUND:
[Why this matters; timing; prior context]

OPTIONS:
[3 options for board consideration]

FOR EACH OPTION:
- Pros and cons
- Financial impact (5-year view)
- Timeline to implement
- Key risks

RECOMMENDATION:
[Which option and why]

CONSTRAINTS:
[Regulatory, market, or timing constraints]

SUCCESS CRITERIA:
[How you'll know if this was the right call]

INSTRUCTIONS:
1. Create a professional, thorough board paper
2. Ensure executive summary is 1 page
3. Present all options objectively
4. Show quantified impact (financial and operational)
5. Address governance and risk explicitly
6. Include timeline and milestones
7. Length: 8–15 pages (excluding appendices)

Output only the board paper. No preamble.
```

## Short Example (Condensed)

**Board Paper: Cloud Infrastructure Migration**

**Executive Summary**
We recommend migrating to AWS to reduce operating costs by £1.5M annually and improve system reliability to 99.9% uptime. Initial investment is £600k. Implementation timeline is 18 months. Key execution risk is project delivery; we'll mitigate with external partner support.

**Background**
Current data centre lease expires in 36 months. Renewal would cost £3.6M over 5 years. Additionally, our infrastructure cannot scale efficiently for projected 5x growth.

**Options Analysis**

*Option A: Renew Current Lease*
• Cost: £3.6M over 5 years
• Scalability: Limited (capacity-constrained)
• Risk: High (vendor dependency; outdated technology)
• Pros: Minimal disruption
• Cons: Higher cost; cannot support growth

*Option B: Migrate to AWS*
• Cost: £600k upfront; £1.5M annual operating
• Scalability: Unlimited (elastic resources)
• Risk: Moderate (project delivery complexity)
• Pros: Cost savings; scalability; modern capabilities
• Cons: Complex migration; temporary dual operations

*Option C: Build Private Data Centre*
• Cost: £2.8M capital + £1.2M annual
• Scalability: Limited (capital-intensive to expand)
• Risk: High (operational complexity; compliance burden)
• Pros: Full control
• Cons: Highest cost; highest operational burden

**Board Recommendation**
Approve Option B (AWS migration) based on:
• Lowest total cost of ownership (£3.0M over 5 years vs. £3.6M or £4.0M)
• Scalability to support growth without additional capital
• Enhanced reliability and compliance (99.9% SLA; GDPR/SOC 2 native)

**Risk Mitigation**
• Project delivery: Engage AWS partner programme; allocate dedicated internal team (£150k budget)
• Technical transition: Phased migration with 6-month parallel operations (absorb cost in operating budget)
• Stakeholder change: Detailed comms plan; training for ops team

**Implementation Timeline**
- Q2 2026: Planning and pilot (£200k)
- Q3 2026–Q4 2027: Phased migration (£400k)
- Q1 2028: Full transition; decommission on-premises

**Success Criteria**
• On-time, on-budget delivery (±5%)
• 99.5%+ uptime during transition
• Zero unplanned data loss or corruption
• All teams trained and self-sufficient by end Q1 2028

**Approval Requested**
Board approval of Option B and authorisation to engage AWS partner by 30 June 2026.

## Quality Checklist

- [ ] Executive summary is 1 page and complete
- [ ] Background is clear and compelling
- [ ] All options presented objectively
- [ ] Financial impact is quantified for each option
- [ ] Risks are identified with mitigation strategies
- [ ] Recommendation is clear and well-justified
- [ ] Implementation timeline is specific
- [ ] Success criteria are measurable
- [ ] Professional formatting throughout
- [ ] Appendices support main document

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Buried recommendation | Board can't find the ask | State clearly in executive summary |
| Only one option presented | Looks biased | Always present 2–3 alternatives |
| Vague financials | Board can't assess value | Quantify all financial impact |
| Risks not addressed | Unacceptable governance | Name specific risks and mitigation |
| No timeline | Implementation unclear | Provide detailed milestones |

---

See [skills/create-board-pack.md](../skills/create-board-pack.md) for multi-part board pack generation.

See [examples/board-paper.md](../examples/board-paper.md) for a complete example.
