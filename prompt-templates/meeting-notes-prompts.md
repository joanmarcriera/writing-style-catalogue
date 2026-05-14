---
title: Meeting Notes Prompts
template_type: Meeting Notes / Minutes
use_case: Convert raw meeting notes, a transcript, or a verbal briefing into clear, structured meeting notes with decisions and action items that can be distributed and acted on immediately.
audience: Meeting attendees, absent stakeholders who need to be informed, and any future reader who needs to understand what was decided
output_format: Structured meeting record with header, topic summaries, decisions, and a clear action items table with owners and due dates
---

# Meeting Notes Prompts

## Purpose

Meeting notes serve two purposes: they confirm what was decided to the people who were there, and they brief people who were not. A good set of notes captures decisions and actions, not discussions — the nuances of a conversation belong in the room, not in a document that will be read three months later. Use this template when you have raw notes, a transcript, or a voice recording (transcribed) from a meeting and need to produce a clean, distributable record within 24 hours. The output should be scannable: a busy stakeholder should be able to identify all actions and decisions without reading the full document.

## Copy-paste prompt

```
You are a professional meeting scribe. Convert the raw notes, transcript, or briefing provided into a clear, structured meeting record that can be distributed to attendees and relevant stakeholders.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (raw notes, transcript, or description of what was discussed — paste the full content here):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one to two pages]

FORMAT: [FORMAT — recommended: meeting header / attendees / agenda items with brief topic summaries / decisions / action items table]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a meeting header: meeting name, date, time, location or platform, and the note-taker.
3. List attendees by name and role. If someone was invited but did not attend, note them as "Apologies".
4. For each agenda topic or discussion area: write a brief summary (two to four sentences maximum) capturing the key points raised. Do not transcribe the discussion — distil it.
5. Decisions: list all decisions made in the meeting explicitly under a "Decisions" heading. Each decision should be a clear, unambiguous statement. If a decision was deferred, note that explicitly ("Decision deferred to [date/meeting]").
6. Action items: present in a table with columns: Action / Owner / Due Date. Be specific — "James to send the CloudBridge contract to Legal for review by 20 May" is an action; "James to look into the contract" is not.
7. Do not attribute opinions or positions to named individuals unless this is specifically asked for or the attendees are senior and the attribution is material to understanding the record.
8. Preserve all facts, figures, and named commitments from the input — do not infer decisions that were not made or actions that were not agreed.
9. If the input is ambiguous — a decision was discussed but not clearly concluded, or an action was mentioned without a clear owner — flag it with a note: "[Clarification needed: was X agreed?]" rather than guessing.
10. Distinguish between confirmed decisions (agreed in the meeting), actions (specific tasks assigned to named owners), and items for information (discussed but no action required).
11. Tone: [TONE — recommended: neutral, professional, factual].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the meeting notes. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will receive the notes. Examples: "all meeting attendees plus the Programme Director who was absent", "the steering group mailing list", "the team only — not for external distribution".
- `[PURPOSE]` — what meeting is being documented. Examples: "fortnightly Cloud Migration Steering Group — 13 May 2026", "IAM workstream weekly stand-up", "supplier contract negotiation session with CloudBridge Ltd".
- `[CONTEXT]` — background that helps the LLM interpret the raw input. Examples: "this is a fortnightly steering group for the Azure cloud migration programme; attendees are the CIO, CFO, and workstream leads", "this was a technical design session; the output will be distributed to engineers and an architect — some technical detail should be retained".
- `[INPUT]` — the raw notes, transcript, or voice memo transcription. Include as much detail as possible; the LLM will distil it.
- `[DESIRED_OUTCOME]` — what the notes need to do. Examples: "attendees can confirm the record is accurate and use the action table to track their commitments", "the absent Programme Director is fully briefed without needing to ask follow-up questions".
- `[TONE]` — "neutral, professional, factual". Meeting notes are a record, not a narrative.
- `[LENGTH]` — one page for short meetings; two pages for longer steering group sessions. Err towards shorter.
- `[FORMAT]` — use the recommended structure. If the meeting follows a formal agenda, align section headings to the agenda items.
- `[CONSTRAINTS]` — examples: "do not attribute individual positions or opinions — summarise the group view only", "include full first names and roles for all attendees", "meeting is commercially sensitive — add 'CONFIDENTIAL' to the header".

## Example input

```
AUDIENCE: Cloud Migration Programme Steering Group members and the Programme Director (who was absent)
PURPOSE: Document the fortnightly Cloud Migration Steering Group — 13 May 2026
CONTEXT: Fortnightly steering group meeting. The group consists of: CIO (chair), CFO, Head of Infrastructure, Head of Security, Programme Manager. The Programme Director was absent — apologies sent. Meeting was held on Microsoft Teams.
INPUT:
  Discussion notes (rough, from Programme Manager):

  Opened at 10:00. CIO chaired.

  1. Phase 1 close-out
  CIO confirmed that the Phase 1 sign-off note had been circulated and accepted. No further actions. Head of Infrastructure confirmed the Azure audit report has been filed with Risk & Compliance. This item is closed.

  2. Phase 2 delivery partner situation
  Programme Manager briefed on the Nexus Solutions capacity issue (see escalation report circulated 10 May). CloudBridge Ltd proposal has been received. Legal review commenced on 12 May. Programme Manager expects legal review to be complete by 28 May.
  CFO asked whether the CloudBridge cost (£180k) could be absorbed in contingency — Programme Manager confirmed yes, contingency currently stands at £220k.
  CIO confirmed that the group is supportive of the CloudBridge engagement in principle.
  Group agreed that formal approval would be given at the next steering group (2 June) once legal review is complete. Programme Manager to circulate the contract summary to group by 30 May.

  3. IAM workstream update
  Head of Infrastructure confirmed the IAM pilot (50 users) is scheduled to start 19 May. Okta — sorry, Entra — has been configured and is ready. No blockers.

  4. Risk review
  Head of Security raised the legacy CRM data retention question as a risk — six workloads cannot be migrated until the Legal team confirms the data retention position. Head of Security to chase Legal for a response by 20 May. If not resolved by 31 May, escalate to CFO.

  5. Next steps
  Next steering group: 2 June, 10:00. Programme Manager to send calendar invite and pre-read by 30 May.

  Meeting closed at 10:45.
DESIRED_OUTCOME: A clean, distributable record that the absent Programme Director can use to stay informed, and that attendees can use to track their actions.
TONE: Neutral, professional, factual
LENGTH: One to two pages
CONSTRAINTS: CONFIDENTIAL. Include full names and roles where known; for those I've listed by role only, use the role title. Note that "Okta" in the raw notes should be corrected to "Microsoft Entra" in the final notes.
```

## Example output

---

**CONFIDENTIAL**

## Cloud Migration Programme — Steering Group Meeting Notes

**Meeting:** Cloud Migration Programme Steering Group
**Date:** 13 May 2026, 10:00–10:45
**Platform:** Microsoft Teams
**Chair:** Chief Information Officer
**Note-taker:** Programme Manager

**Attendees:**
- Chief Information Officer (Chair)
- Chief Financial Officer
- Head of Infrastructure
- Head of Security
- Programme Manager

**Apologies:**
- Programme Director

---

### 1. Phase 1 close-out

The Phase 1 sign-off note, circulated prior to the meeting, was accepted by the group. The Azure security audit report has been filed with Risk & Compliance by the Head of Infrastructure. This item is now closed; no further actions.

---

### 2. Phase 2 delivery partner — CloudBridge engagement

The Programme Manager briefed the group on the Nexus Solutions capacity constraint (as detailed in the escalation report of 10 May). The CloudBridge Ltd proposal has been received and a legal review commenced on 12 May.

The CFO confirmed that the estimated CloudBridge cost of £180k can be absorbed within the existing programme contingency (currently £220k). The group confirmed in-principle support for the engagement.

**Decision:** Formal approval to engage CloudBridge Ltd will be given at the next steering group on 2 June, subject to satisfactory completion of the legal review.

---

### 3. IAM workstream

The IAM pilot (50 users) is scheduled to commence on 19 May 2026. Microsoft Entra has been configured and is ready for deployment. No blockers reported.

---

### 4. Risk review — legacy CRM data retention

The Head of Security flagged that six Phase 2 workloads cannot be migrated until the Legal team confirms the data retention position for the legacy CRM system. This creates a risk to the Phase 2 timeline if not resolved by 31 May.

---

### Decisions

1. Formal approval to engage CloudBridge Ltd as second delivery partner will be given at the 2 June steering group, subject to satisfactory completion of the legal review.
2. Phase 1 close-out is complete; no further steering group actions required.

---

### Action Items

| Action | Owner | Due Date |
|--------|-------|----------|
| Complete legal review of CloudBridge contract | Legal (coordinated by Programme Manager) | 28 May 2026 |
| Circulate CloudBridge contract summary and legal review outcome to steering group | Programme Manager | 30 May 2026 |
| Chase Legal for data retention position on legacy CRM workloads | Head of Security | 20 May 2026 |
| Escalate legacy CRM data retention issue to CFO if unresolved | Head of Security | 31 May 2026 |
| Send calendar invite and pre-read for 2 June steering group | Programme Manager | 30 May 2026 |
| Begin IAM pilot deployment (50 users) | Head of Infrastructure | 19 May 2026 |

---

**Next meeting:** 2 June 2026, 10:00 (Microsoft Teams)

---

## Review checklist

- [ ] Meeting header is complete (meeting name, date, time, platform, chair, note-taker)
- [ ] All attendees and apologies are listed with roles
- [ ] Each agenda item has a brief, distilled summary — not a transcript
- [ ] All decisions are listed explicitly under the Decisions heading
- [ ] Deferred decisions are noted as such (with the date of next review)
- [ ] All action items are in a table with owner, action, and due date — no vague tasks
- [ ] Ambiguous items are flagged with a clarification note rather than guessed at
- [ ] No individual opinions attributed unless specifically required
- [ ] British English used throughout
- [ ] Notes are ready to distribute within 24 hours of the meeting

---

Share notes within 24 hours of the meeting.
