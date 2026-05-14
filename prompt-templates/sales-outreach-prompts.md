---
title: Sales Outreach Prompts
template_type: Sales Outreach Email / Sequence
use_case: Write personalised, prospect-focused sales outreach emails that earn a reply by leading with the recipient's problem rather than the sender's product.
audience: Prospective clients, procurement contacts, or decision-makers being contacted for the first time or as part of a follow-up sequence
output_format: Short, personalised outreach email (under 150 words) with a specific hook, a relevant value proposition, and a low-friction ask
---

# Sales Outreach Prompts

## Purpose

Sales outreach fails when it is about the sender: "I'm reaching out because we help companies like yours..." Effective outreach is about the recipient: it shows you understand their specific situation, you have something relevant to offer, and the next step you are proposing is easy to take. Use these prompts when you need to write a cold outreach email, a follow-up in a sequence, or a re-engagement message to a prospect who has gone quiet. The output should be short, specific, and focused on the recipient's gain — not your product's features. It should sound like it was written by a person who did their research, not by a CRM automation tool.

## Copy-paste prompt — Initial outreach email

```
You are a senior sales professional who understands that the best outreach is about the prospect's problem, not the sender's product. Write a personalised, relevant, concise outreach email that earns a reply.

AUDIENCE: [AUDIENCE — the specific prospect, their role, organisation, and any known context]

PURPOSE: [PURPOSE — what action you want the recipient to take]

CONTEXT: [CONTEXT — why you are reaching out now; any trigger event, shared connection, or relevant news about their organisation]

INPUT (everything known about the prospect, their likely challenges, and how your offering is relevant to their specific situation):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. a reply agreeing to a 20-minute call]

TONE: [TONE — recommended: direct, warm, professional — not pushy or salesy]

LENGTH: [LENGTH — recommended: under 150 words body; 60–100 is ideal]

FORMAT: [FORMAT — recommended: personalised hook (1–2 sentences) / relevant value proposition (1–2 sentences) / specific, low-friction ask (1 sentence) / sign-off]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a personalised hook that references something specific about the prospect's organisation, role, or a recent relevant event — not a generic statement about their industry. Do not open with "I hope this finds you well" or "I wanted to reach out".
3. State your value proposition in one or two sentences, framed around the prospect's likely problem — not your product's features. Focus on what they gain, not what you offer.
4. Make a single, specific ask with a low barrier: suggest two or three specific times for a call, offer a one-page summary they can forward, or ask one specific question. Do not ask for "a quick chat sometime" — be concrete.
5. Do not use pressure language, false urgency ("limited slots available"), excessive flattery, or superlatives.
6. Preserve all facts provided in the input — do not invent details about the prospect's organisation.
7. Distinguish between confirmed facts (things you know about the prospect) and inferences (things you are assuming based on their role or sector). If you are making an assumption, frame it accordingly ("organisations at your stage often...").
8. Tone: [TONE].
9. Length: [LENGTH]. If the email is over 150 words, it is too long — cut it.
10. Apply these constraints: [CONSTRAINTS].
11. Output only the email. No preamble.
```

## Copy-paste prompt — Follow-up email (prospect gone quiet)

```
You are a sales professional writing a follow-up to a prospect who engaged briefly but then went quiet. Write a short, non-pushy follow-up that re-opens the conversation.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT — what prior contact has occurred; how long since the last exchange]

INPUT (prior conversation context, what was discussed or sent previously, and why now is a good time to re-engage):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE — recommended: light, direct, not desperate]

LENGTH: [LENGTH — recommended: under 100 words]

FORMAT: [FORMAT — recommended: brief acknowledgement of silence / one new piece of value or updated context / a simple yes/no question]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English.
2. Do not guilt or pressure the prospect. Do not say "I wanted to follow up on my previous email" as the opening.
3. Offer something new — a relevant insight, a piece of content, or an updated piece of context that gives them a reason to re-engage beyond just being chased.
4. End with a simple question that requires a yes or a no, or a one-word answer. Make it easy to reply.
5. If the input provides no new information to offer, write a break-up email instead: a brief, respectful message that acknowledges they may not be interested and leaves the door open.
6. Output only the email. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — the specific prospect. Examples: "Sarah Chen, Head of IT Security at Pinnacle Asset Management — a 900-person UK-based asset manager currently mid-way through an Azure migration", "James Okafor, CIO at a UK regional insurer — recently appointed; prior firm ran on AWS".
- `[PURPOSE]` — the desired action. Examples: "arrange a 20-minute discovery call to discuss IAM advisory support", "share a relevant case study and invite a conversation", "follow up on a proposal sent three weeks ago".
- `[CONTEXT]` — why you are reaching out now. Examples: "the prospect's firm was mentioned in an FCA DORA compliance bulletin last month", "we met briefly at the Cloud Expo in April", "a mutual contact (name) suggested I reach out", "the prospect commented on a LinkedIn post about IAM governance".
- `[INPUT]` — everything known: the prospect's role, their organisation, their likely pain points (based on sector, size, or publicly available information), the trigger for outreach, and how your offering is specifically relevant to them.
- `[DESIRED_OUTCOME]` — what success looks like. Examples: "the prospect replies and agrees to a call", "the prospect forwards the email to their IT director", "the prospect asks for more information".
- `[TONE]` — "direct, warm, professional" for initial outreach. "Light and confident" for follow-up. Never "pushy" or "desperate".
- `[LENGTH]` — under 150 words for initial outreach; under 100 words for follow-up.
- `[FORMAT]` — use the recommended formats. Do not use bullet points in a cold email — it reads like a template.
- `[CONSTRAINTS]` — examples: "do not mention competitors by name", "the prospect is at a firm that was recently in the press about a data breach — do not reference this directly, but the context informs the hook", "include a P.S. line if it adds something useful".

## Example input — Initial outreach

```
AUDIENCE: Head of Information Security at a UK financial services firm (asset management firm, approximately 1,200 staff, London-based). The prospect's firm is known to be in the middle of an Azure migration. Her name is Dr Priya Nair.
PURPOSE: Arrange a 20-minute discovery call to explore whether Meridian Advisory's IAM advisory service is relevant to their migration programme.
CONTEXT: Dr Nair posted on LinkedIn two weeks ago about the challenges of maintaining FCA compliance during cloud migration. That post is the trigger for outreach — she specifically mentioned "identity governance gaps during workload migration" as a concern. No prior contact.
INPUT:
  What we know about the prospect and her organisation:
  - Azure migration in progress (public LinkedIn post); identity governance is a stated concern
  - FCA DORA compliance is clearly on her radar (mentioned in the LinkedIn post)
  - 1,200 staff — likely 20–30 privileged IT accounts at minimum; standard IAM complexity for this size

  How Meridian Advisory is relevant:
  - Meridian has completed three IAM transformations at UK financial services firms during Azure migrations
  - We reduced provisioning/deprovisioning times dramatically in each case and helped all three firms pass FCA access control audits
  - We have a specific methodology for maintaining IAM governance continuity during cloud migration (not all IAM firms have migration-specific experience)
DESIRED_OUTCOME: Dr Nair replies and agrees to a 20-minute call in the next two weeks.
TONE: Professional, direct, respectful — not salesy or pushy
LENGTH: Under 140 words body
CONSTRAINTS: Do not use "leverage". Reference the LinkedIn post as the trigger — it shows this is not a mass email. Do not promise specific outcomes — frame as "in our experience" not "we will".
```

## Example output

---

**Subject: IAM governance during cloud migration — a few thoughts from your LinkedIn post**

Dr Nair,

Your LinkedIn post about identity governance gaps during workload migration caught my attention — it's exactly the problem we've been working on with three UK financial services clients who are at similar stages of their Azure journeys.

In each case, the core issue was the same: migration teams focus on workload compatibility and security baselines, while the access governance model — who should have what access, how it's reviewed, what happens when someone changes role — gets deferred. The FCA compliance exposure during that window is real.

We have a specific approach to maintaining IAM governance continuity through migration. I'd welcome 20 minutes to share what we've seen and whether it might be relevant to your programme.

Are you free for a brief call the week of 26 May or 2 June?

Best regards,
[Name]
Meridian Advisory

---

## Review checklist

- [ ] Opening hook references something specific about the prospect — not a generic industry statement
- [ ] Value proposition is framed around the prospect's problem, not the sender's product
- [ ] The ask is single, specific, and low-friction
- [ ] No pressure language, false urgency, or flattery
- [ ] Assumptions about the prospect are framed as such ("organisations at your stage often...")
- [ ] No invented details about the prospect's organisation
- [ ] Total body length is under 150 words
- [ ] No bullet points — prose only for outreach emails
- [ ] British English used throughout
- [ ] Tone is professional and direct — not desperate or aggressive

---

See [styles/persuasive-sales-style.md](../styles/persuasive-sales-style.md) for persuasive sales style.
