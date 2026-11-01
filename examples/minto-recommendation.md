---
title: Minto Recommendation — Service Desk Consolidation
category: Example
description: A worked recommendation bundle that leads with one answer and supports it with mutually exclusive reasons.
bundle_id: minto-recommendation
artefact: Structured executive recommendation
audience: Chief operating officer and technology leadership team
scenario: labelled-composite
style_path: styles/minto-pyramid-principle.md
pattern_path: patterns/situation-complication-question-answer.md
prompt_path: prompt-templates/strategy-prompts.md
skill_path: skills/create-executive-memo.md
rubric_path: rubrics/executive-communication-rubric.md
---

# Minto Recommendation — Service Desk Consolidation

## Professional context

Leadership must decide whether to consolidate three regional service desks. The recommendation should be persuasive because its logic is explicit, not because alternatives are caricatured.

## Source packet

```text
SCENARIO: Labelled composite.
SITUATION: Three regional service desks use separate queues, reporting, and overnight cover.
EVIDENCE: 18% of tickets are transferred between regions; median resolution is 14.2 hours; annual operating cost is £2.4m.
COMPLICATION: A single global tool is already contracted, but operating processes and ownership remain regional.
OPTIONS: retain regional model; consolidate queues only; create one follow-the-sun operating model.
RECOMMENDATION: Follow-the-sun model, phased over six months.
SUPPORTING REASONS: one accountable queue owner; continuous cover using existing shifts; one reporting model.
ESTIMATE: implementation cost £310,000; expected annual saving £420,000 from contractor and duplicate-tool retirement.
ASSUMPTIONS: No redundancies; shifts remain within existing contracts; savings estimate has not passed finance assurance.
RISK: regional knowledge may be lost during transition.
DECISION: Approve detailed design and finance validation, not full implementation.
```

## Completed prompt

```text
You are a strategy director writing a Minto-style recommendation for the Chief Operating Officer and technology leadership team. The decision is whether to approve detailed design and finance validation for a follow-the-sun service desk model.

Use only the SOURCE PACKET. Do not invent customer satisfaction, staffing reductions, regulatory benefits, validated savings, implementation dependencies, or option scores. Present the £420,000 saving as an unassured estimate and preserve the no-redundancy and employment-contract assumptions. If the decision, viable alternatives, evidence, financial estimate, or material risk is absent, return MISSING INFORMATION rather than a recommendation.

Write in British English. Lead with the answer in one sentence. Support it with three mutually exclusive reasons: accountability, coverage, and management information. Then use Situation, Complication, Question, Answer; Evidence; Alternatives and trade-offs; Financial assumptions; Risk and mitigation; Decision requested. Explain why queue-only consolidation and the status quo were not selected without dismissing them. Keep it between 600 and 850 words and output only the recommendation.

Before finalising, test bottom line, audience fit, evidence, decision clarity, risk and caveats, brevity, and tone against the Executive Communication Rubric.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Recommendation
Approve detailed design and finance validation for a six-month transition to one follow-the-sun service desk operating model.

Why this is the right next decision
1. Accountability: one queue owner removes ambiguous hand-offs across three regional teams.
2. Coverage: existing regional shifts can provide continuous cover, subject to confirmation that current employment terms permit the design.
3. Management information: one reporting model makes transfer rate, ageing, and resolution performance comparable.

The estimated £420,000 annual saving has not passed finance assurance. Approval therefore covers detailed design and validation of the £310,000 implementation estimate—not full implementation.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Bottom line | 5 | The first sentence states the recommended decision and its scope. | Pass |
| Audience fit | 4 | Leaders can approve a bounded next step without approving delivery; the alternatives are outside the excerpt. | Pass |
| Evidence | 4 | Cost and saving figures carry their assurance status; the transfer-rate and resolution baselines are outside the excerpt. | Pass |
| Decision clarity | 4 | The decision is limited to design and validation; the source packet gives no deadline, so none is stated. | Pass |
| Risk and caveats | 4 | The unassured saving and employment-terms caveat are visible; regional knowledge loss is not in the excerpt. | Pass |
| Brevity | 5 | One answer is supported by three non-overlapping reasons and one caveat paragraph. | Pass |
| Tone | 5 | Measured and confident without overstating the saving. | Pass |

## Human review before use

- Finance must assure the cost and saving model.
- HR and legal must validate shift and employment assumptions.
- Regional service owners must validate the knowledge-transfer risk and proposed controls.

## Reuse this bundle

- [Minto Pyramid Principle](../styles/minto-pyramid-principle.md)
- [SCQA Pattern](../patterns/situation-complication-question-answer.md)
- [Strategy Prompts](../prompt-templates/strategy-prompts.md)
- [Create Executive Memo Skill](../skills/create-executive-memo.md)
- [Executive Communication Rubric](../rubrics/executive-communication-rubric.md)
