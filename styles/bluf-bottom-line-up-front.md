---
title: BLUF (Bottom Line Up Front)
category: Concise
best_for: Any professional email, memo, or short document where the reader needs to understand the answer or required action immediately without reading through background first. Particularly effective for approval requests, decision escalations, and status updates requiring a response.
not_good_for: Complex recommendations where the argument needs to be built carefully before the conclusion (use Minto Pyramid); narrative content where the journey matters as much as the destination (use Narrative Storytelling).
default_tone: Professional and direct. Confident, not aggressive.
typical_length: 150–300 words
aliases: [Answer First, BLUF Email]
---

# BLUF – Bottom Line Up Front

## What this style is

BLUF puts the answer, recommendation, or key message in the very first sentence. Context, supporting facts, and background follow in subsequent paragraphs. The reader gets complete clarity the moment they begin reading and can stop there if they are pressed for time, confident they have grasped the essential point.

The approach originates in US military communication, where officers are trained to lead every written communication with the bottom line so that commanders can act immediately without reading to the end. It has since been adopted widely in professional and corporate communication for the same reason: readers are busy, and clarity must come first.

**Core principle**: Answer first, explain second. The first sentence must contain the complete bottom line.

## When to use it

- Emails requiring approval, a decision, or a specific action from the reader
- Short internal memos where background is already known
- Status updates that require a decision or escalation
- Problem statements requiring a rapid response
- Requests for resources, budget, or headcount
- Internal announcements where the key fact must land immediately
- Any document shorter than one page where the reader needs to act

## When not to use it

- Complex recommendations where the argument must be built before the conclusion — use [Minto Pyramid Principle](minto-pyramid-principle.md) instead
- Teaching, explanation, or onboarding — use [Socratic Explainer](socratic-explainer.md) or [Plain English](plain-english.md) instead
- Formal board or governance documents requiring thorough presentation of options — use [Board Paper Style](board-paper-style.md) instead
- Narrative or storytelling communications — use [Narrative Storytelling](narrative-storytelling.md) instead
- Building a structured logical case for a sceptical audience — use [Consulting Style](consulting-style.md) instead

## Core structure

```
[BLUF — BOTTOM LINE IN FIRST SENTENCE]
The clear, actionable answer, recommendation, or decision.
One sentence. No preamble.

[CONTEXT]
Why this is needed. 1–3 sentences maximum.

[KEY POINTS]
Supporting facts, rationale, or detail.
Use bullet points, not paragraphs.

[ACTION REQUIRED]
What the reader must do.
Include the deadline explicitly.

[NEXT STEPS OR QUESTIONS]
Who to contact; when follow-up happens.
```

## Copy-paste prompt

```
You are a BLUF (Bottom Line Up Front) writing expert. Write a professional email or memo in strict BLUF style from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Head of IT Operations", "CFO", "Procurement team"]
PURPOSE: [PURPOSE — e.g. "Approval request for contract extension", "Escalation of a supplier issue", "Status update requiring a decision"]
CONTEXT: [CONTEXT — e.g. "Contract expires in six weeks; vendor has offered current-rate extension for 24 months"]
INPUT: [INPUT — paste the raw facts, notes, or situation description here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Reader approves the contract extension by end of day Friday"]
TONE: [TONE — e.g. "Professional and direct", "Collaborative but firm", "Factual and neutral"]
LENGTH: [LENGTH — e.g. "Under 250 words total"]
FORMAT: [FORMAT — subject line + BLUF sentence + context + bulleted facts + action required]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not quote specific figures until approved by Finance", "Must be suitable for forwarding to the supplier"]

INSTRUCTIONS:
1. The very first sentence must be the bottom line — the recommendation, answer, or decision. It must be complete and standalone.
2. Write 1–3 sentences of context explaining why this matters. Do not front-load context before the bottom line.
3. List supporting facts as bullet points (3–5 maximum). Each bullet must be one sentence with a specific fact.
4. State the required action clearly: what the reader must do, and by when.
5. Use British English throughout (colour, organisation, licence, favour, practise, etc.).
6. Preserve all factual claims exactly as provided in [INPUT]. Flag any assumptions with "(assumed)" in parentheses.
7. Use "must" for obligations, "should" for recommendations, "may" for options. Avoid "might want to consider" or similar hedges.
8. Total length must not exceed [LENGTH].

Output the email or memo only. No preamble, no commentary.
```

## Output format

The finished document reads as a professional email or internal memo. It contains:

- **Subject line**: Clear and specific — states the topic and the type of ask (e.g. "Approval needed: Supplier contract extension by 17 May")
- **BLUF sentence**: First sentence of the body. One sentence only. Contains the complete bottom line.
- **Context**: 1–3 sentences of plain prose. Explains why this is needed.
- **Supporting facts**: 3–5 bullet points, each one sentence with a specific fact or figure
- **Action required**: One or two sentences stating exactly what the reader must do and by when
- **Contact or next steps**: Brief closing with contact details or follow-up timing

Total word count: 150–300 words. The document fits entirely in the preview pane of an email client.

## Example

**Subject: Approval needed — IAM vendor contract renewal by 21 May**

We should renew our identity management platform contract with Okta on the 24-month extension they have offered, as this locks in current pricing and avoids a projected 18% increase at renegotiation.

Our current contract expires on 30 June. Okta have offered a 24-month extension at the existing rate of £42,000 per annum through to June 2028. If we allow the contract to lapse and renegotiate in Q3, industry benchmarking indicates we would face a rate increase of 15–20%, adding approximately £6,300–£8,400 annually.

**Supporting facts:**
- Current annual spend: £42,000 (£3,500/month, 850 users)
- Extension period: 24 months, same terms and SLA (99.9% uptime)
- Estimated cost if we renegotiate at market rates: £48,300–£50,400 per annum
- No service changes; all existing integrations with Azure AD remain in place
- Legal have reviewed the extension terms and confirmed no material changes to liability clauses

**Action required:**
Please approve the renewal by 21 May so that our Head of Procurement can countersign before the vendor's offer deadline. I will execute the contract immediately upon receiving your approval.

Questions? Contact me directly or reach the IT procurement inbox at it-procurement@company.com.

## Quality checklist

- [ ] First sentence contains the complete bottom line — recommendation, answer, or decision
- [ ] Bottom line is self-contained and actionable without reading further
- [ ] Context is concise (1–3 sentences only)
- [ ] Supporting facts are bulleted, not prose paragraphs
- [ ] Action and deadline are explicit and unambiguous
- [ ] Total length is under 300 words
- [ ] No hedging language ("seems," "quite," "relatively," "might want to consider")
- [ ] British English used throughout
- [ ] "Must," "should," and "may" used with precision

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Burying the bottom line | Reader must hunt for the answer; defeats the entire purpose | Put the answer in sentence one — no exceptions |
| Starting with context or background | Delays clarity; loses busy readers before the key point | Front-load the bottom line; context follows |
| Vague action items | Reader is unsure what to do | "Approve by Friday 21 May" not "Let me know your thoughts" |
| Missing deadline | Action may never happen | Always include a specific date |
| Too many supporting facts | Overwhelms the reader | Keep to 3–5 maximum; cut the rest |
| Weak modal verbs | Sounds uncertain and unpersuasive | Use "must" or "should" — not "might want to consider" |
| Missing numbers | Impact is unclear | "Saves £50k annually" not "significant savings" |
| Multiple asks in one email | Reader unsure which is most important | One BLUF per communication; split if needed |

---

See [prompt-templates/email-prompts.md](../prompt-templates/email-prompts.md) for more email templates.

See [examples/bluf-email.md](../examples/bluf-email.md) for a complete email example.
