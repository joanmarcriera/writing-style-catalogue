---
title: Create SOP
skill_type: Document generation
output: A Standard Operating Procedure document with numbered steps, decision points, verification criteria, and a version control header — usable by any competent person without additional guidance
tools_needed: LLM (Claude/ChatGPT/Gemini), Word or Google Docs, version control system (optional)
difficulty: Medium
---

# Skill: Create SOP (Standard Operating Procedure)

## What this skill does

Documents a repeatable process in enough detail that a competent person who has never performed it before can complete it correctly and consistently. An SOP is more structured than a checklist — it explains not just what to do but why each step matters, what the expected output looks like, and what to do if something goes wrong. SOPs are the foundation of operational consistency, audit readiness, and knowledge retention. A well-written SOP replaces the need to ask a colleague how something is done.

## When to use it

- Documenting a critical IT process (user provisioning, backup verification, incident escalation) so it survives staff turnover
- Creating onboarding documentation for a new team member who must learn a process independently
- Standardising a process that is currently done differently by different team members, causing quality variation
- Satisfying an ISO, SOC 2, or regulatory audit requirement for documented operational procedures
- Preserving institutional knowledge before a subject matter expert leaves the organisation

## Inputs required

- The name of the process — stated precisely (not "onboarding" but "new joiner IT account provisioning")
- The intended user: their role, their technical level, and how often they will perform this process
- A description of how the process is currently performed (even if imperfect)
- What "done correctly" looks like — the measurable success criterion
- Any decision points in the process (if X, do Y; if Z, escalate to...)
- Any tools, systems, or access required before starting
- Known failure modes or common mistakes the SOP should warn against
- Who approves this SOP and how often it must be reviewed

## Copy-paste prompt

```
You are a process documentation specialist. Write a Standard Operating Procedure (SOP) for the process described below.

AUDIENCE: [Who will follow this SOP — role, technical level, frequency of use]
PURPOSE: [What this SOP governs; why consistency matters here]
CONTEXT: [Tools and systems involved; regulatory or compliance context if any]
INPUT: [Describe how the process is currently done; list the steps you know; include decision points and known failure modes]
DESIRED_OUTCOME: [What the measurable success criterion looks like — how does the user know they have completed the process correctly?]
TONE: Clear, instructional, and precise. SOPs are reference documents — language must leave no room for interpretation.
LENGTH: As long as the process requires — typically 3–8 pages for a complex process, 1–2 pages for a simple one.
FORMAT: Numbered steps for sequential actions. Conditional steps as clearly labelled branches ("If [condition], go to Step X"). Warnings and notes as clearly labelled callouts. Include a version control header. Include a prerequisites section before Step 1.
CONSTRAINTS: Use British English. Every step must begin with an action verb. Do not combine two distinct actions in one step — split them. Output only the SOP; no preamble.

STRUCTURE:
# SOP: [Process Name]
| Version | Date | Author | Approved by | Review date |
|---------|------|--------|-------------|-------------|

**Purpose**: [One sentence]
**Scope**: [What this SOP covers and what it does not cover]
**Owner**: [Role responsible for this SOP]

## Prerequisites
[Access, tools, permissions required before starting]

## Procedure
Step 1: [Action verb] ...
Step 2: [Action verb] ...

## Verification
[How to confirm the process completed correctly]

## Troubleshooting
[Common failure modes and resolution steps]

## Related documents
[Links to related SOPs, checklists, or runbooks]
```

## Suggested output structure

- **Version control table** — version number, date, author, approver, next review date
- **Purpose** — one sentence: what this SOP does and why it exists
- **Scope** — what is and is not covered (prevents misapplication)
- **Prerequisites** — system access, tools, credentials, or prior steps required
- **Procedure** — numbered sequential steps; conditional branches clearly labelled; screenshots or diagram placeholders where needed
- **Verification** — specific, measurable checks that confirm the process completed correctly
- **Troubleshooting** — 3–5 common failure modes with their resolution steps
- **Related documents** — links to relevant runbooks, checklists, or upstream/downstream SOPs

## Quality controls

- [ ] Every step begins with an action verb (Create, Verify, Select, Enter, Confirm, Notify)
- [ ] No step combines more than one distinct action
- [ ] Conditional branches are explicitly labelled — "If [condition]: go to Step X; otherwise: continue to Step Y"
- [ ] The verification section specifies measurable outcomes, not vague states ("ticket status shows 'Resolved'" not "confirm it worked")
- [ ] A person who has never performed this process can complete it successfully without asking questions
- [ ] Version control table is complete and includes a review date no more than 12 months out
- [ ] Troubleshooting section covers the 3 most common failure modes

## Common failure modes

- **Steps too broad**: "Configure the server" is not a step — "Navigate to Server Manager → Add Roles and Features → select Web Server (IIS) → click Install" is — be specific enough for the user to follow without guessing
- **No decision branches**: Real processes have conditions; an SOP that pretends every run is identical will fail when the user encounters an edge case
- **Outdated screenshots or menu paths**: UI changes faster than SOPs are updated — use screenshots sparingly or reference by menu path name, which is easier to update
- **Missing prerequisites**: A user who starts the process without the right access will fail partway through — list every prerequisite explicitly at the start
- **Written by expert for expert**: The subject matter expert who writes the SOP often omits steps they consider obvious — have a colleague follow the draft SOP cold and note every point of confusion

## Example request

"Write an SOP for the new joiner IT account provisioning process. User: IT administrator. Process: create Active Directory account, assign licence in Microsoft 365, add to correct security groups based on role, provision laptop, configure MFA, send welcome email with credentials via secure link, close the ServiceDesk ticket. The SOP must meet our ISO 27001 audit requirements. Decision point: if the new joiner is a contractor, do not assign a full M365 licence — assign Guest access only. Review annually."
