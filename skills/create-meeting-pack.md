---
title: Create Meeting Pack
skill_type: Document generation
output: A complete meeting pack including agenda, pre-read briefing, decision templates, and a post-meeting action log template — structured so attendees arrive informed and leave with clear next steps
tools_needed: LLM (Claude/ChatGPT/Gemini), Word or Google Docs
difficulty: Easy
---

# Skill: Create Meeting Pack

## What this skill does

Assembles all materials required for a productive, time-efficient meeting: a structured agenda with time allocations and owners, a concise pre-read that brings all attendees to the same level of understanding, discussion frameworks for complex agenda items, decision templates for items requiring a formal outcome, and a next-steps tracker template. The pack is designed to eliminate the "can everyone just get up to speed first?" opening 15 minutes and ensure the meeting produces decisions rather than discussions. Good meeting packs are read before the meeting — they must therefore be concise enough that attendees actually read them.

## When to use it

- Preparing for a board paper approval meeting where attendees need structured pre-reading
- Running a project steering group meeting with multiple workstream updates and a decision required
- Organising a client workshop or discovery session where a shared agenda improves output quality
- Facilitating a strategy session where all participants need background context before the working session
- Convening an incident review meeting where stakeholders need briefing on what happened before the discussion

## Inputs required

- Meeting type and purpose (decision meeting, working session, briefing, review)
- List of attendees with roles (to calibrate the pre-read depth and decision authority)
- Agenda items with the type of outcome required for each (decision, update, discussion, approval)
- Estimated duration for each agenda item
- Background material for the pre-read (can be raw notes, existing documents, or key data points)
- Any decisions to be made, with the options to be considered
- Next steps from the previous meeting (if this is a recurring meeting)

## Copy-paste prompt

```
You are a skilled meeting facilitator and executive assistant. Create a complete meeting pack for the meeting described below.

AUDIENCE: [List of attendees — roles and seniority; note any non-native speakers or accessibility requirements]
PURPOSE: [What this meeting must achieve — list specific decisions, approvals, or outcomes]
CONTEXT: [Background on why this meeting is happening; what has changed since the last meeting; what the attendees already know]
INPUT: [Paste agenda items, background notes, decisions to be made, and any previous action items]
DESIRED_OUTCOME: [Specific decisions made; next steps assigned; all attendees aligned on the outcome]
TONE: Professional and efficient. Meeting materials should respect the attendees' time — no padding.
LENGTH: Agenda 1 page; pre-read 1–2 pages; decision templates 1 page per major item; action log template 1 page.
FORMAT: Separate clearly labelled sections for each document in the pack. Agenda as a table. Pre-read as headed sections. Decision templates as structured forms. Action log as a table.
CONSTRAINTS: Use British English. Pre-read must fit on 2 pages maximum — if the background is complex, create an additional reference document and link to it. Every agenda item must have a time allocation, an owner, and an outcome type. Output only the pack content; no preamble.

PACK STRUCTURE:
1. AGENDA
| Time | Item | Owner | Duration | Outcome |
|------|------|-------|----------|---------|
| 10:00 | [Item 1] | [Name] | 15 min | Decision |

2. PRE-READ BRIEFING
[Concise background on the meeting context and agenda items — written so an attendee who reads only this is ready to contribute]

3. DECISION TEMPLATE (one per decision item)
Decision: [What is being decided]
Options: [Option A / Option B]
Recommendation: [If one exists]
Decision made: ___________
Rationale: ___________

4. ACTION LOG
| Action | Owner | Due date | Status |
|--------|-------|----------|--------|
```

## Suggested output structure

- **Agenda** — meeting title, date, location/link, attendees; items in a table with time, owner, duration, and outcome type; AOB slot; close time
- **Pre-read briefing** — 1–2 pages; one section per major agenda item; purpose is to level-set, not to pre-decide; end with a prompt question for each item to focus discussion
- **Decision templates** — one per decision item; states what is being decided, the options, the recommendation (if one), and space for the decision and rationale
- **Parking lot** — a named space for items raised but deferred; prevents meetings from running over on tangents
- **Action log template** — table with columns: action, owner, due date, dependencies, status; pre-populated with actions carried over from previous meeting

## Quality controls

- [ ] Every agenda item has a time allocation, a named owner, and an outcome type (decision / update / discussion)
- [ ] The total agenda time fits the meeting duration — with a 5-minute buffer and a comfort break if over 90 minutes
- [ ] The pre-read is under 2 pages — if longer, the meeting will not have been fully prepared for
- [ ] Decision items have a decision template — the meeting should not end with an undocumented verbal agreement
- [ ] Action log from the previous meeting is included in the pack — carryover accountability
- [ ] The pack was sent to attendees at least 48 hours before the meeting

## Common failure modes

- **Pre-read too long**: A 10-page pre-read will not be read — cut to 2 pages; if the context is complex, a 30-minute pre-meeting briefing is more effective than a long document
- **Agenda without outcome types**: An agenda that lists topics but not expected outcomes produces meetings that run over and fail to reach decisions — every item must state whether it ends in a decision, an update, or a discussion
- **No decision templates**: Verbal decisions made in meetings are frequently mis-remembered differently by different attendees — a written decision template prevents this
- **Meeting pack sent the night before**: Attendees need at least 48 hours to read and prepare — send 72 hours before for complex strategic sessions
- **No parking lot**: Without a designated parking lot, tangential discussions consume decision time — introduce it explicitly at the start of the meeting

## Example request

"Create a meeting pack for a 90-minute Project Steering Group meeting for the Azure cloud migration programme. Attendees: CTO (chair), CFO, Head of Infrastructure (Project Sponsor), Project Manager, and two external consultants from the delivery partner. Agenda: (1) Actions from last meeting — 10 min; (2) Phase 1 status update — 20 min; (3) Decision: approve Phase 2 scope and budget (£800k) — 30 min; (4) Risk review — 15 min; (5) Stakeholder communications update — 10 min; (6) AOB — 5 min. The Phase 2 decision needs a formal decision template. British English."
