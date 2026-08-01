---
title: Board Paper — Identity Platform Decision
category: Example
description: A worked governance bundle with comparable options, financial assumptions, risks, and resolution wording.
bundle_id: board-paper
artefact: Board decision paper
audience: Board directors and non-executive directors
scenario: labelled-composite
style_path: styles/board-paper-style.md
pattern_path: patterns/context-analysis-options-recommendation.md
prompt_path: prompt-templates/board-paper-prompts.md
skill_path: skills/create-board-pack.md
rubric_path: rubrics/board-paper-rubric.md
---

# Board Paper — Identity Platform Decision

## Professional context

A board must select one of three identity-platform options. The paper must compare options on the same basis and retain the uncertainty in cost estimates and delivery capacity.

## Source packet

```text
SCENARIO: Labelled composite; all organisations, figures, and findings are fictional.
DECISION: Select an identity-platform option and authorise the associated five-year envelope.
DEADLINE: Current contract ends 31 December 2027.
OPTION A — RENEW: five-year cost £840,000; lowest transition risk; two control gaps require separate remediation.
OPTION B — MANAGED CLOUD: five-year cost £620,000; migration estimate includes £260,000 one-off and £72,000 annual licence; addresses both control gaps; 12-month migration; delivery confidence medium.
OPTION C — INTERNAL BUILD: five-year cost £1,420,000; 18-month estimate; engineering capacity not allocated; delivery confidence low.
ASSUMPTIONS: Costs exclude VAT and internal staff time. Option B estimate is based on an indicative quote, not a final tender.
TOP RISKS FOR B: migration delay; access-data integrity; user disruption; vendor dependency.
RECOMMENDATION: Option B, subject to competitive procurement, an independent migration assurance plan, and quarterly board reporting.
FUNDING: Technology capital reserve has £700,000 uncommitted.
```

## Completed prompt

```text
You are a board-governance writer. Prepare a condensed but decision-ready board paper for directors and non-executive directors on the identity-platform decision in the SOURCE PACKET.

Use only supplied facts. Do not invent legal requirements, audit clauses, vendor capabilities, savings, implementation dates, staffing, or certainty. Label assumptions and unresolved procurement evidence. If the decision, comparable costs, recommendation, funding source, or material risks are absent or contradictory, stop and return MISSING INFORMATION rather than producing a paper.

Use: Executive Summary; Decision Required; Background; Comparable Options Table; Recommendation and Rationale; Financial Analysis and Assumptions; Governance and Risk; Implementation Gates; Proposed Resolution. Present all three options using identical criteria before recommending one. State that Option B pricing is indicative and excludes VAT and internal staff time. Give each risk a consequence, control, owner role, and review gate, but do not invent named individuals. Use formal, neutral British English and no more than 1,400 words. Output only the board paper.

Before finalising, apply the Board Paper Rubric. Decision clarity, options analysis, financial analysis, risk, and evidence separation are critical gates. Preserve the conditions attached to the recommendation in the proposed resolution.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Executive Summary
The Board is asked to select an identity-platform option and authorise the associated five-year expenditure envelope. Three options were assessed on cost, control coverage, delivery confidence, and transition risk.

Option B, a managed cloud platform, is recommended at an estimated five-year cost of £620,000. This is an indicative estimate excluding VAT and internal staff time, not a final tender price. It addresses both identified control gaps, but carries medium delivery confidence and material migration risks.

Proposed resolution
The Board approves Option B and authorises expenditure up to £620,000 over five years, subject to competitive procurement confirming value within that envelope, approval of an independent migration-assurance plan, and quarterly progress and risk reporting to the Board.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Decision required | 5 | The ask and conditional resolution are explicit. | Pass |
| Options analysis | 4 | Three genuine options use consistent criteria. | Pass |
| Financial analysis | 4 | Comparable costs and exclusions are visible. | Human check |
| Risk | 4 | Named risks and governance conditions survive the summary. | Pass |
| Evidence and assumptions | 5 | Indicative pricing and exclusions are not presented as facts. | Pass |

## Human review before use

- Finance must reconcile every figure with the approved model and confirm funding authority.
- Procurement must validate the tender condition and commercial sensitivity.
- Legal, security, and the executive sponsor must approve their respective sections.
- The company secretary must confirm that the resolution wording fits the board's authority.

## Reuse this bundle

- [Board Paper Style](../styles/board-paper-style.md)
- [Context / Analysis / Options / Recommendation Pattern](../patterns/context-analysis-options-recommendation.md)
- [Board Paper Prompts](../prompt-templates/board-paper-prompts.md)
- [Create Board Pack Skill](../skills/create-board-pack.md)
- [Board Paper Rubric](../rubrics/board-paper-rubric.md)
