---
title: Create Roadmap
skill_type: Planning
output: A phased, timeline-based roadmap showing initiatives, milestones, dependencies, and ownership — formatted as a structured Markdown document or a table suitable for executive or board communication
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor or Roadmap tool (Productboard, Aha!, Azure DevOps, or a simple spreadsheet)
difficulty: Medium
---

# Skill: Create Roadmap

## What this skill does

Develops a timeline-based roadmap that shows what will be delivered, in what sequence, over a defined horizon. A roadmap is a communication tool first and a planning tool second: it tells a specific audience (executives, board, engineering team, customers) what to expect and when. This skill produces the narrative structure and content of a roadmap, not the Gantt chart software output — the LLM generates a Markdown table or phase-based structure that can be transferred to any roadmap tool. Good roadmaps show sequencing and dependencies, not just a list of initiatives.

## When to use it

- Communicating a technology or infrastructure roadmap (cloud migration, IAM programme, ERP replacement) to board or executive level
- Presenting a product development roadmap to investors or a customer advisory board
- Planning a multi-phase programme with interdependent workstreams (a 24-month security uplift programme)
- Producing the "what and when" section of a business case or strategy document
- Updating stakeholders on a programme that is changing — showing what has slipped, what has accelerated, and what has been added

## Inputs required

- The initiative or programme being roadmapped — named precisely
- The time horizon (6 months, 12 months, 3 years) and unit of time (month, quarter, half-year)
- The initiatives, features, or workstreams to include — with any known sequencing constraints
- Dependencies between initiatives (Initiative B cannot start until Initiative A is complete)
- Owners or responsible teams for each initiative
- Milestone or decision gates that the roadmap should show
- The intended audience and how much detail they need

## Copy-paste prompt

```
You are a programme manager and strategic planner. Create a roadmap for the programme described below.

AUDIENCE: [Who will read this roadmap — e.g. board, C-suite, engineering team, product team, customers]
PURPOSE: [What the roadmap must communicate — sequence, timeline, priorities, dependencies, or all of the above]
CONTEXT: [Why this programme exists; what problem it solves; what constraints apply (budget, headcount, technology dependencies)]
INPUT: [List of initiatives or workstreams; known dependencies; any fixed deadlines or milestones; owner information]
DESIRED_OUTCOME: [A clear, credible roadmap that the audience can understand and trust; must show sequencing and dependencies explicitly]
TONE: [e.g. Formal and strategic for board / Direct and practical for engineering team / Optimistic and outcome-focused for customers]
LENGTH: One page summary table plus narrative section of 200–400 words explaining the phasing rationale.
FORMAT: Phase-based structure with a Markdown table (rows = initiatives; columns = time periods). Use symbols: ● = in progress, ○ = planned, ✓ = complete, ⚠ = at risk, → = dependency. Follow with a narrative section explaining phase logic.
CONSTRAINTS: Use British English. Do not include more initiatives than can realistically be delivered in the stated time horizon — a credible roadmap is better than an aspirational one. Flag dependencies explicitly — do not embed them invisibly in sequencing. Output only the roadmap and narrative; no preamble.

ROADMAP TABLE FORMAT:
| Initiative | Owner | Q1 | Q2 | Q3 | Q4 | Q5–Q6 | Q7–Q8 |
|------------|-------|----|----|----|----|----|-----|
| [Initiative 1] | [Team] | ● | ✓ | | | | |
| [Initiative 2 — depends on 1] | [Team] | → | ● | ○ | | | |
| [Initiative 3] | [Team] | | | ● | ○ | | |

**Phase 1 (Q1–Q2): [Phase name]** — [50–80 word narrative]
**Phase 2 (Q3–Q4): [Phase name]** — [50–80 word narrative]
**Phase 3 (Q5–Q8): [Phase name]** — [50–80 word narrative]
```

## Suggested output structure

- **Roadmap summary table** — initiatives as rows, time periods as columns; symbols indicate status and dependencies
- **Phase narratives** — one paragraph per phase (50–80 words) explaining what is being delivered, why in this order, and what it enables
- **Dependencies section** — explicit list of critical dependencies with the consequence of each dependency failing
- **Milestones** — 3–5 key decision points or delivery milestones that the audience should track
- **Assumptions and risks** — what the roadmap assumes to be true; what risks could cause slippage

## Quality controls

- [ ] Every initiative has a named owner — not "TBC"
- [ ] Dependencies are shown explicitly — not buried in sequencing
- [ ] The time horizon matches the audience's planning cycle (executives plan in quarters; engineers plan in sprints)
- [ ] The roadmap is credible — initiatives are sized realistically; there is slack for the unexpected
- [ ] Phase names describe outcomes, not activities ("Cloud infrastructure stabilised" beats "Phase 2")
- [ ] The roadmap can be explained verbally in under 5 minutes
- [ ] Version and date are noted — roadmaps change; stakeholders need to know which version they have

## Common failure modes

- **Over-ambitious**: Packing every initiative into the first two quarters destroys credibility — sequence realistically, even if that means deferring some things the audience wants
- **Dependencies invisible**: If Initiative B requires Initiative A to be complete but this is not shown, the audience assumes they are independent — make every dependency explicit
- **Wrong time unit for audience**: Monthly granularity is appropriate for an engineering team; quarterly is appropriate for executives; annual for a board 3-year roadmap
- **No ownership**: A roadmap where no initiative has a named owner is a wish list, not a plan — every row needs an accountable person or team
- **Never updated**: A roadmap that is not reviewed as conditions change misleads stakeholders; establish a quarterly review cycle from the outset

## Example request

"Create a 24-month roadmap for our IAM (Identity and Access Management) programme. The programme has four workstreams: (1) Privileged Access Management — deploy CyberArk, Q1–Q3; (2) Identity Governance — implement Entra ID Governance, Q2–Q4, depends on PAM baseline; (3) Zero Trust Network Access — deploy ZTNA solution, Q4–Q6, depends on Identity Governance; (4) User Awareness Training — ongoing from Q1. Audience: board and executive team. Milestones: ISO 27001 audit readiness by end of Q4; full programme close by end of Q8. British English throughout."
