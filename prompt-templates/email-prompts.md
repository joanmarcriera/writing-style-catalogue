---
title: Email Prompts
template_type: Email
use_case: Write professional, action-oriented emails that get read and responded to.
audience: Internal colleagues, senior stakeholders, external contacts, or clients — defined per use
output_format: Structured email with clear subject line, BLUF opening, bulleted facts, and explicit ask
---

# Email Prompts

## Purpose

Use these prompts when you need to write a professional email that achieves a specific outcome: securing approval, providing an update, making a request, or reaching out to an external contact. The BLUF (Bottom Line Up Front) format is the default because busy recipients decide in the first sentence whether to act — so the ask or key point must come first. Use the outreach variant when cold-contacting a supplier, partner, or prospective client. Both variants are written for British English and a professional register that avoids empty formality.

## Copy-paste prompt — Professional email (BLUF)

```
You are an expert professional email writer. Write a clear, concise email that gets a specific response or action.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (key facts, background, and any draft content):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: under 300 words]

FORMAT: [FORMAT — recommended: subject line / BLUF opening sentence / 2–3 sentence context / bulleted facts / explicit ask with deadline]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout (organise, recognise, colour, licence as noun, practise as verb).
2. Open with the bottom line: what you need and when. The recipient must understand the ask from the first sentence alone.
3. Keep the body to 2–3 short paragraphs maximum. If listing more than two items, use bullet points.
4. State the deadline or required response date explicitly.
5. Preserve all factual figures and named details from the input — do not invent data.
6. Distinguish between confirmed facts and assumptions where relevant (e.g. "subject to board approval" or "assuming current pricing").
7. Avoid corporate filler: no "please do not hesitate", "as per my previous email", "going forward", or "leveraging synergies". Be direct and human.
8. Tone: [TONE].
9. Apply these constraints: [CONSTRAINTS].
10. If a critical piece of information — such as the recipient's name or the specific deadline — is missing and you cannot infer it, note it with [MISSING: X] rather than guessing.
11. Output only the email (subject line through sign-off). No preamble or commentary.

FORMAT TO USE:
Subject: [specific, action-oriented subject line]

[Bottom line: what you need in one sentence]

[2–3 sentences of context — why this matters and why now]

[Bulleted facts if there are more than two supporting points]

[Explicit ask + deadline]

[Sign-off]
```

## Copy-paste prompt — Outreach email

```
You are a professional outreach specialist. Write a short, personalised outreach email that earns a reply.

AUDIENCE: [AUDIENCE — who you are contacting and their role/organisation]

PURPOSE: [PURPOSE — what you want from this contact]

CONTEXT: [CONTEXT — why you are reaching out now; any shared connection or relevant hook]

INPUT (background on the recipient, their organisation, or prior interaction):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. a 30-minute call, an introduction, agreement to review a proposal]

TONE: [TONE — recommended: warm and professional, not salesy]

LENGTH: [LENGTH — recommended: under 150 words]

FORMAT: [FORMAT — recommended: personalised hook / one-sentence value proposition / specific low-friction ask / sign-off]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English.
2. Open with a personalised hook that references something specific about the recipient's work, company, or a shared context — not a generic compliment.
3. State in one sentence what you do and why it is relevant to them. Focus on their gain, not your product or service.
4. Make a single, specific ask with a low barrier: suggest two or three times for a call, or offer a one-paragraph summary they can forward. Do not ask for "a quick chat sometime".
5. Do not use pressure language, urgency tactics, or flattery.
6. Distinguish what you know about the recipient (stated in the input) from assumptions — do not present inferences as facts.
7. Apply these constraints: [CONSTRAINTS].
8. Output only the email. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who is receiving the email. Examples: "Sarah Chen, Finance Director at Meridian Group", "the IT leadership team", "a procurement contact at a prospective cloud vendor".
- `[PURPOSE]` — what the email is trying to achieve. Examples: "obtain approval for a £600k infrastructure budget", "notify the team of a platform outage resolution", "arrange an introductory call with a potential IAM vendor".
- `[CONTEXT]` — why this email is being sent now and any relevant background. Examples: "budget cycle closes on 30 June", "the outage ran from 09:14 to 11:47 and affected 400 users", "we met briefly at the Cloud Expo in March".
- `[INPUT]` — the raw material: facts, a previous draft, bullet-point notes, or a situation description.
- `[DESIRED_OUTCOME]` — what success looks like. Examples: "the Finance Director replies with written approval by Friday", "the vendor sends a pricing proposal within five working days".
- `[TONE]` — register to use. Examples: "professional and direct", "formal and cautious", "warm and collegial", "confident but not pushy".
- `[LENGTH]` — target length. Under 300 words for internal professional emails; under 150 words for outreach.
- `[FORMAT]` — structure of the output. The defaults above work well; override if needed.
- `[CONSTRAINTS]` — any restrictions. Examples: "do not mention the ongoing redundancy process", "must reference the contract reference number CR-2026-041", "no bullet points — prose only".

## Example input — Professional email

```
AUDIENCE: James Okafor, Group Finance Director, Vertex Holdings
PURPOSE: Request approval for a £600k cloud infrastructure investment
CONTEXT: The infrastructure programme is due to begin in Q3 2026. Vendor commitment is needed by 30 June. The business case was submitted to Finance three weeks ago.
INPUT:
  - Annual operating savings: £1.5M from Year 2
  - Total investment: £600k over 18 months
  - Payback period: approximately 14 months
  - Risk is low — phased rollout with external delivery partner
  - Three vendors shortlisted; preferred vendor selected pending budget sign-off
DESIRED_OUTCOME: James replies with written budget approval by end of Friday 29 May.
TONE: Professional, respectful, direct — James is senior but we have a good working relationship
LENGTH: Under 250 words
FORMAT: Standard BLUF email
CONSTRAINTS: Reference the business case document submitted on 24 April
```

## Example output

**Subject: Cloud Infrastructure Budget Approval — £600k — Response Needed by 29 May**

James,

I need your approval to proceed with the cloud infrastructure investment of £600k, which we need to confirm to the preferred vendor by 30 June.

The business case submitted on 24 April sets out the full rationale. In brief:

- **Total investment**: £600k over 18 months
- **Annual savings from Year 2**: £1.5M (data centre decommission, hardware and licensing costs)
- **Payback period**: approximately 14 months
- **Risk**: low — phased rollout with external delivery partner and rollback capability at each stage

Three vendors were assessed; the preferred partner has been selected and is awaiting our commitment. Delaying past 30 June risks losing our Q3 start date and deferring savings by at least one financial year.

Could you confirm approval by end of day Friday 29 May? I am happy to set up a brief call beforehand if that would help.

Thanks,
[Name]

## Review checklist

- [ ] Subject line is specific and includes the key ask or topic
- [ ] First sentence contains the bottom line — what is needed
- [ ] Facts and figures are accurate and match the input
- [ ] Assumptions are flagged where present (not stated as certainties)
- [ ] Tone is appropriate for the recipient's seniority and relationship
- [ ] Bullet points used for lists of three or more items
- [ ] Deadline is stated explicitly
- [ ] No filler phrases or corporate language
- [ ] British English spellings used throughout
- [ ] Total length is within the specified target

---

See [styles/bluf-bottom-line-up-front.md](../styles/bluf-bottom-line-up-front.md) for BLUF style guide.
