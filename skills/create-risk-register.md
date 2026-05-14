---
title: Create Risk Register
skill_type: Document generation
output: A structured risk register table with identified risks, likelihood and impact scores, risk scores, owners, mitigations, and review dates — formatted for ongoing management use
tools_needed: LLM (Claude/ChatGPT/Gemini), Excel or Google Sheets (for live management), Word or Markdown (for snapshot reporting)
difficulty: Medium
---

# Skill: Create Risk Register

## What this skill does

Produces a structured risk register that identifies, assesses, and tracks risks for a project, programme, or organisation. Each risk is described, assessed for likelihood and impact, scored, assigned an owner, given a mitigation action, and scheduled for review. The LLM is effective at drafting an initial risk register from a description of the context, identifying risks the author may have overlooked, and writing clear, consistent risk descriptions. The register must then be validated by people with operational knowledge and reviewed on a defined cycle — a risk register that is not reviewed is worse than no register.

## When to use it

- Starting a cloud migration, system implementation, or major infrastructure change and needing to identify and track risks from the outset
- Preparing a board or audit committee risk report that shows the organisation's top risks and mitigations
- Satisfying an ISO 27001, SOC 2, or regulatory requirement for a documented risk management process
- Completing a project initiation document that requires a risk assessment section
- Reviewing and updating an existing risk register after a significant change in the operating environment

## Inputs required

- The context: what is being assessed (a project, a programme, an organisational function, or the whole enterprise)
- The scope: what risks are in scope (technical, operational, financial, regulatory, reputational, strategic)
- A preliminary list of risks — as many as you can identify; the LLM will add more
- The scoring scales to use: likelihood (1–5 or High/Medium/Low), impact (1–5 or High/Medium/Low)
- The risk appetite statement, if one exists (what score triggers escalation to board?)
- The risk owner model (individual owners vs. team owners)
- The review cycle (monthly, quarterly, or event-triggered)

## Copy-paste prompt

```
You are a risk management specialist. Create a risk register for the context described below.

AUDIENCE: [Who will maintain and review this register — e.g. project manager, CISO, board audit committee]
PURPOSE: [What this register is for — project risk management, board reporting, ISO audit, regulatory compliance]
CONTEXT: [What is being assessed; the organisation type and sector; any known constraints or upcoming events]
INPUT: [Describe the situation, project, or organisation; list any risks you have already identified; include any known incidents or near-misses]
DESIRED_OUTCOME: [A complete, reviewable register with identified risks, scores, owners, and mitigations]
TONE: Factual and precise. Risk descriptions must be specific enough that any reviewer can understand the risk without asking for clarification.
LENGTH: As many risks as the context warrants — typically 10–20 for a project; 20–40 for an enterprise register. Each risk in one row.
FORMAT: Markdown table with columns: ID | Risk description | Category | Likelihood (1–5) | Impact (1–5) | Risk score (L×I) | Rating | Owner | Mitigation | Residual score | Review date. Below the table, list the top 5 risks by score as a narrative "Key risks" section.
CONSTRAINTS: Use British English. Risk descriptions must follow the format: "Risk that [event] occurs, resulting in [consequence]." Every risk must have a mitigation — "monitor" is not a mitigation; it is a review activity. Output only the register and key risks section; no preamble.

SCORING KEY:
Likelihood: 1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost certain
Impact: 1 = Negligible, 2 = Minor, 3 = Moderate, 4 = Major, 5 = Critical
Risk score = Likelihood × Impact
Rating: 1–6 = Low, 7–12 = Medium, 13–19 = High, 20–25 = Critical
```

## Suggested output structure

- **Risk register table** — one row per risk with all columns populated
- **Key risks narrative** — top 5 risks by score, described in 2–3 sentences each with mitigation status
- **Risk heat map** (optional) — a 5×5 matrix showing risk distribution by likelihood and impact; useful for board reporting
- **Governance section** — who reviews the register, how often, and what escalation path applies for Critical-rated risks

## Quality controls

- [ ] Every risk description follows the "Risk that [event] occurs, resulting in [consequence]" format
- [ ] Likelihood and impact scores are applied consistently — a 4 (Likely) means the same thing across all risks
- [ ] Every risk has a named owner — not a team name alone (teams do not own risks; individuals do)
- [ ] Every mitigation is an action (something that reduces likelihood or impact), not just monitoring
- [ ] Residual score is lower than inherent score — if the mitigation is effective, the residual risk should be smaller
- [ ] Top risks by score are narratively summarised for board or executive reporting
- [ ] Review dates are specified — not "quarterly" but an actual date

## Common failure modes

- **Risks too vague**: "Technology risk" is a category, not a risk — "Risk that the Azure migration is delayed by 3 months due to underestimated data migration complexity, resulting in cost overrun of £150k" is a risk
- **Mitigations that are just monitoring**: "Monitor closely" does not reduce the likelihood or impact of a risk — mitigations should change something (add a control, reduce exposure, transfer the risk, implement a contingency plan)
- **All risks rated the same**: If every risk is rated Medium (3×3), the register is not doing its job of distinguishing priorities — use the full scale and be willing to rate some risks as Low and others as High
- **No owner**: Risks without a named owner are never acted on — every risk needs one person accountable for monitoring and mitigation
- **Never reviewed**: A risk register that is not reviewed on its stated cycle provides false assurance — build the review cycle into a recurring calendar event from day one

## Example request

"Create a risk register for the Azure cloud migration project (Phase 1: lift-and-shift of on-premise infrastructure to Azure IaaS, 18-month timeline, £2.1M budget). Scope: technical, financial, security, and operational risks. Key risks I am already aware of: data migration failure, cost overrun, team capability gaps, Azure service outage during cutover, and GDPR compliance for data in transit. Please identify any additional risks I may have missed. Owner model: individual owners from the project team. Review cycle: monthly. We need this for the project initiation document."
