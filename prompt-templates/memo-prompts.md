---
title: Memo Prompts
template_type: Memo
use_case: Write clear, structured internal memos that inform, align, or request a decision from an internal audience.
audience: Internal teams, department heads, or specific named colleagues
output_format: Formal memo header followed by purpose statement, key points, and explicit action with deadline
---

# Memo Prompts

## Purpose

A memo is the right format when an email feels too informal and a full report feels excessive. Use it for internal communications that need a clear record: policy changes, programme decisions, resource requests, process updates, or anything that benefits from a permanent written trace. Memos work well for audiences who are peers or colleagues rather than external parties, and when the communication needs to stand on its own without a covering conversation. The decision memo variant is for situations where you are escalating a choice to a decision-maker — it presents options objectively, makes a clear recommendation, and asks for sign-off with a specific deadline.

## Copy-paste prompt — Standard memo

```
You are an expert memo writer. Write a clear, professional internal memo.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant facts, decisions, and background to include):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one page, two pages maximum]

FORMAT: [FORMAT — recommended: formal memo header / purpose paragraph / key points as bullets / action required with deadline]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Use the standard memo header: TO / FROM / DATE / SUBJECT — each on its own line.
3. Open with a concise purpose statement: one or two sentences that explain why the memo exists and what it requires of the reader.
4. Present the body as structured bullet points under clear sub-headings, not as dense paragraphs.
5. Preserve all factual content from the input — do not invent figures, names, or decisions.
6. Clearly distinguish facts (confirmed information), assumptions (inferred or estimated), and recommendations (proposed actions) — use brief labels such as "Note:" or "Assumption:" where helpful.
7. State the required action and deadline explicitly in a clearly labelled section.
8. Write in a professional but not stiff tone — clear, direct, respectful. Avoid jargon, acronyms (unless explained on first use), and corporate filler.
9. Provide a brief caveat where there is material uncertainty.
10. Length: [LENGTH].
11. Apply these constraints: [CONSTRAINTS].
12. Output only the memo. No preamble, no commentary.

MEMO FORMAT:
MEMORANDUM

TO:        [Recipients]
FROM:      [Sender Name / Role]
DATE:      [Date]
SUBJECT:   [Clear, specific subject line]

Purpose
[One to two sentences stating why this memo exists and what the reader needs to do]

[Section heading]
[Bullet points]

[Section heading]
[Bullet points]

Action Required
[What is needed, from whom, and by when]
```

## Copy-paste prompt — Decision memo

```
You are a decision memo specialist. Write a structured memo that presents a decision clearly and requests sign-off.

AUDIENCE: [AUDIENCE — the decision-maker(s)]

PURPOSE: [PURPOSE — what decision is being requested]

CONTEXT: [CONTEXT — why this decision is needed now; what happens if it is not made]

INPUT (options, analysis, recommendation, and any constraints):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. the director approves Option B and confirms resource allocation]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one to two pages]

FORMAT: [FORMAT — recommended: header / executive summary of decision needed / options presented objectively / recommendation with rationale / deadline]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English.
2. Lead with the decision needed — the very first paragraph must state what is being asked and by when.
3. Present two or three options, each with a brief description, key advantages, key disadvantages, and cost or resource implication. Present them objectively before giving a recommendation.
4. Make a single, clear recommendation with concise rationale. If the evidence genuinely does not support a strong preference, say so — do not manufacture false certainty.
5. Flag assumptions explicitly (e.g. "This analysis assumes current headcount; a further FTE review is scheduled for July.").
6. Include the consequence of inaction or delay.
7. Apply constraints: [CONSTRAINTS].
8. Output only the memo. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who the memo is addressed to. Examples: "Head of Infrastructure and IT Leadership Team", "Programme Steering Group", "Chief Information Officer".
- `[PURPOSE]` — what the memo is communicating. Examples: "inform the team of a Q3 feature release timeline and confirm resource allocation", "request approval to extend the contract with vendor Apex Systems", "communicate a change to the identity governance policy".
- `[CONTEXT]` — background for the writer and the LLM. Examples: "this follows the infrastructure review completed in April 2026", "the original contract expires on 31 July and a gap in service cover would affect 300 users".
- `[INPUT]` — the raw facts, data, and decisions to be captured. Paste bullet points, notes, or any source material.
- `[DESIRED_OUTCOME]` — what the memo should achieve. Examples: "the product team confirms resource allocation by end of the week", "the CIO signs off on Option A before the next steering committee on 2 June".
- `[TONE]` — register to use. Examples: "professional and collegial", "formal and structured", "direct and urgent".
- `[LENGTH]` — one page is the standard; two pages maximum.
- `[FORMAT]` — use the standard format above; override only if the organisation has a specific house style.
- `[CONSTRAINTS]` — restrictions to apply. Examples: "do not reference the staff restructure — this will be communicated separately", "include the project code PRJ-2026-014 in the header".

## Example input — Standard memo

```
AUDIENCE: Cloud Infrastructure Programme team (six people including two engineers, a solution architect, a project manager, a business analyst, and the programme sponsor)
PURPOSE: Confirm the Q3 deployment schedule and resource commitments for the Azure IAM rollout
CONTEXT: The IAM (Identity and Access Management) rollout is part of the wider cloud migration programme. The team had an informal discussion in the weekly stand-up on 12 May but no written confirmation exists. The programme manager needs written confirmation before the steering committee on 2 June.
INPUT:
  - Go-live target: 1 August 2026
  - Phase 1 (pilot — 50 users): June
  - Phase 2 (business-wide rollout — 1,200 users): July–August
  - Resources needed: 2 FTE engineers June–August; 0.5 FTE BA for June only
  - External vendor (Okta) confirmed and contracted
  - Assumption: no further scope changes after 30 May
DESIRED_OUTCOME: All six team members acknowledge the schedule and confirm their availability by 23 May.
TONE: Professional, clear, collegial
LENGTH: One page
CONSTRAINTS: Mention the steering committee date (2 June). Include the project code: PRJ-2026-007.
```

## Example output

---

MEMORANDUM

TO:        Cloud Infrastructure Programme Team
FROM:      [Programme Manager Name]
DATE:      14 May 2026
SUBJECT:   IAM Rollout — Q3 Deployment Schedule and Resource Confirmation (PRJ-2026-007)

**Purpose**

This memo confirms the Q3 deployment schedule for the Azure Identity and Access Management (IAM) rollout and requests that all team members confirm their availability by 23 May, ahead of the steering committee on 2 June.

**Deployment schedule**

- **Phase 1 — Pilot (50 users)**: June 2026
- **Phase 2 — Business-wide rollout (1,200 users)**: July–August 2026
- **Go-live target**: 1 August 2026
- External vendor (Okta) is contracted and confirmed for both phases.

**Resource requirements**

- Engineering: 2 FTE committed from June through August
- Business Analysis: 0.5 FTE required during June only
- Assumption: no further scope changes will be introduced after 30 May. Any changes after that date will require a formal change request and may affect the go-live date.

**Action Required**

Please reply to this memo by **Friday 23 May** to confirm:
1. Your availability to meet the resource commitments above, or
2. Any constraints that may affect your availability.

Responses are needed before the steering committee on 2 June. If you cannot confirm by 23 May, please contact [Programme Manager Name] directly.

---

## Review checklist

- [ ] Memo header is complete (TO / FROM / DATE / SUBJECT)
- [ ] Purpose is stated in the opening paragraph — clear and concise
- [ ] Key points are bulleted under sub-headings, not buried in prose
- [ ] Facts, assumptions, and recommendations are distinguishable
- [ ] Action required is explicit — states what, from whom, and by when
- [ ] Tone is professional but not stiff
- [ ] No jargon or unexplained acronyms
- [ ] British English spellings used throughout
- [ ] Length is within the one-to-two-page target

---

See [styles/minto-pyramid-principle.md](../styles/minto-pyramid-principle.md) for logical argument structure.
