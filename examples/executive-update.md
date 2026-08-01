---
title: Executive Update — Customer Migration Programme
category: Example
description: A worked leadership update that separates delivery evidence, forecast, risks, and the decision needed.
bundle_id: executive-update
artefact: Executive programme update
audience: Executive committee members sponsoring a customer migration programme
scenario: labelled-composite
style_path: styles/executive-briefing.md
pattern_path: patterns/what-so-what-now-what.md
prompt_path: prompt-templates/project-status-prompts.md
skill_path: skills/create-one-page-brief.md
rubric_path: rubrics/executive-communication-rubric.md
---

# Executive Update — Customer Migration Programme

## Professional context

An executive committee needs the current delivery position, not a progress narrative. The update must expose the difference between achieved results and forecast outcomes and end with one decision.

## Source packet

```text
SCENARIO: Labelled composite.
REPORTING DATE: 31 July 2026
OVERALL STATUS: Amber
SCOPE: Migrate 120 enterprise customers by 30 November 2026.
DELIVERED: 46 customers migrated; 44 passed acceptance first time; 2 required data correction and then passed.
FORECAST: 112–120 customers by deadline, depending on specialist partner capacity from September.
BUDGET: £1.84m spent of £3.20m approved; current forecast £3.05m–£3.28m.
RISKS: partner capacity unconfirmed after 1 September; eight customers have unresolved data-retention requirements.
DECISION REQUIRED BY 7 AUGUST: reserve £180,000 contingency for a second migration partner. Spending still requires procurement approval.
NEXT MILESTONES: partner commitment by 14 August; retention decisions by 21 August; 75 customers migrated by 30 September.
```

## Completed prompt

```text
You are a chief-of-staff writer preparing a one-page executive update for the sponsors of a customer migration programme. The readers need to understand current performance, forecast uncertainty, material risks, and one decision.

Use only the SOURCE PACKET. Do not invent causes, savings, customer sentiment, partner commitments, mitigations, or confidence. Keep actual results, ranges, forecasts, and unresolved requirements visibly distinct. If reporting date, scope, achieved results, forecast, budget, risks, or decision are missing or inconsistent, return MISSING INFORMATION and do not draft the update.

Use British English and this order: Bottom line; What has happened; So what; Decision required; Next 30 days. Keep it between 300 and 450 words. Lead with Amber status and the forecast range. State both the £3.05m–£3.28m forecast and the £3.20m approval; do not call the programme within budget. Explain that reserving contingency does not itself authorise spending. Use short paragraphs and a compact table only if it improves comparison. Output only the update.

Before finalising, review instruction fit, factual integrity, specificity, structure, tone, risk awareness, and usefulness against the Executive Communication Rubric. Preserve every uncertainty and deadline.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Bottom line — Amber
Forty-six of 120 enterprise customers have migrated. The programme forecasts 112–120 completions by 30 November, but the upper end depends on specialist partner capacity that is not confirmed after 1 September.

Budget
£1.84m of £3.20m has been spent. The current forecast is £3.05m–£3.28m, so the downside case exceeds the approved envelope.

Decision required by 7 August
Reserve £180,000 contingency for a second migration partner. This reservation does not authorise expenditure; any engagement remains subject to procurement approval.

Next 30 days
Confirm partner capacity by 14 August, resolve eight data-retention decisions by 21 August, and protect the 75-customer milestone due 30 September.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Factual integrity | 5 | Actuals, forecast range, budget, and deadlines map to source. | Pass |
| Structure | 5 | Status, implication, decision, and next actions are immediately visible. | Pass |
| Risk awareness | 5 | Partner and retention uncertainty remain explicit. | Pass |
| Professional tone | 4 | Direct and non-defensive without overstating control. | Pass |
| Usefulness | 5 | The committee has one dated decision and three milestones. | Pass |

## Human review before use

- The programme director must confirm actuals and forecast at the reporting cut-off.
- Finance must confirm spend and forecast ranges.
- Procurement must confirm the wording around contingency and spending authority.

## Reuse this bundle

- [Executive Briefing Style](../styles/executive-briefing.md)
- [What / So What / Now What Pattern](../patterns/what-so-what-now-what.md)
- [Project Status Prompts](../prompt-templates/project-status-prompts.md)
- [Create One-Page Brief Skill](../skills/create-one-page-brief.md)
- [Executive Communication Rubric](../rubrics/executive-communication-rubric.md)
