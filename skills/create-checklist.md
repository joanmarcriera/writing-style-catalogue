---
title: Create Checklist
skill_type: Document generation
output: A grouped, actionable checklist with checkbox items, section headings, and a sign-off block — formatted for practical use in print or digital form
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor or Word
difficulty: Easy
---

# Skill: Create Checklist

## What this skill does

Builds a practical, grouped checklist for any process, quality gate, or task sequence where reliable consistency matters. A good checklist is not a comprehensive list of everything that could be done — it is the critical minimum that a competent person could miss under pressure. This skill distinguishes between items that must be verified (a gate: do not proceed if unchecked) and items that should be completed (a task: complete and mark done). The output is a scannable, print-ready document that can be used in the field without interpretation.

## When to use it

- Creating a pre-deployment or pre-release quality gate for technical changes (cloud migration steps, IAM role changes)
- Documenting a handover process so nothing is lost when a team member is absent or leaves
- Producing a readiness checklist before a board meeting, client presentation, or regulatory audit
- Standardising an onboarding or offboarding process across a team or organisation
- Building a daily or weekly operational review checklist for an operations or infrastructure team

## Inputs required

- The process or task the checklist covers — stated precisely (not "deployment" but "Azure VM deployment to production")
- Who will use it (engineer on-call, new joiner, project manager, auditor)
- When they will use it (before, during, or after a specific event)
- The steps or checkpoints in the process — as many as you know; the LLM will organise them
- Any hard gates (items where failure means stopping the process entirely)
- Any items that are optional or context-dependent

## Copy-paste prompt

```
You are a process documentation specialist. Create a practical, field-ready checklist for the process below.

AUDIENCE: [Who will use this checklist — e.g. on-call engineer, project manager, new joiner]
PURPOSE: [What the checklist governs — quality gate, task completion, readiness review]
CONTEXT: [When and where this checklist is used; any constraints on the environment]
INPUT: [List the steps, tasks, or checkpoints you want included — in any order; include any hard gates]
DESIRED_OUTCOME: [What "done correctly" looks like — how will the user know the checklist is complete?]
TONE: Direct and instructional. Checklists are tools, not documents — language must be unambiguous.
LENGTH: As short as possible while capturing every critical item. Aim for under 30 items total; use sections to group.
FORMAT: Markdown checklist with [ ] checkboxes. Group related items under clear section headings. Mark hard gates with ⚠️ STOP. Include a sign-off block at the end with fields for: Completed by, Date, Sign-off.
CONSTRAINTS: Use British English. Every item must be an action (verb-led: "Confirm", "Verify", "Check", "Notify"). Do not include items that are automatic or system-enforced — only items a human must check. Output only the checklist; no preamble.

STRUCTURE:
# [Checklist Title]
**Purpose**: [One sentence]
**Used by**: [Role]
**Used when**: [Timing]

## [Section 1]
- [ ] [Action item]

## [Section 2]
- [ ] [Action item]

## Sign-off
- Completed by: _______________
- Date: _______________
- Reviewed by: _______________
```

## Suggested output structure

- **Header** — checklist title, purpose, "used by" role, and "used when" timing
- **Section 1: Pre-conditions** — things that must be true before the process starts (access, permissions, tools)
- **Section 2: Core steps** — the main process items in order; include ⚠️ STOP markers for hard gates
- **Section 3: Verification** — items to check after the process to confirm it completed correctly
- **Section 4: Communications** — who must be notified and what records must be created
- **Sign-off block** — completed by, date, reviewed by (if a second pair of eyes is required)

## Quality controls

- [ ] Every item is an action (verb-led) — not a noun or a question
- [ ] Hard gates are clearly marked and distinguished from regular tasks
- [ ] The checklist is usable by someone working under pressure or time constraint — no item requires interpretation
- [ ] Items are grouped logically so the user can work through sections sequentially
- [ ] The sign-off block includes all fields needed for audit trail
- [ ] Total item count is under 30; if more are needed, split into two separate checklists
- [ ] Tested mentally by walking through a realistic use scenario — does it catch the things that go wrong?

## Common failure modes

- **Too comprehensive**: A checklist that tries to capture everything a competent person knows becomes unusable — keep only the items that a competent person could reasonably miss
- **Items not action-led**: "Security" as a checklist item means nothing — "Verify MFA is enabled for all admin accounts" is checkable
- **No hard gates**: If the checklist does not distinguish between "nice to have" and "must stop if this fails", a user under pressure will skip items — use ⚠️ STOP markers explicitly
- **Wrong audience**: A checklist written for an expert reads as insultingly basic to them; one written for a novice leaves an expert without the detail they need — always specify the intended user
- **Never updated**: Processes change; a checklist that is not reviewed annually will contain obsolete items that erode trust in the whole document

## Example request

"Create a pre-deployment checklist for Azure infrastructure changes going to production. Users are senior cloud engineers. The checklist covers: change approval (CAB sign-off required), backup verification, rollback plan documented, peer review complete, monitoring alerts configured, comms sent to operations team, deployment window confirmed, and post-deployment smoke test. Any step that fails the STOP criteria means the deployment must be aborted and rescheduled."
