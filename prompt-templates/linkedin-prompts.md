---
title: LinkedIn Prompts
template_type: LinkedIn Content
use_case: Write LinkedIn posts, profile sections, and connection messages that are authentic, specific, and generate genuine engagement from a professional audience.
audience: LinkedIn connections and followers — professional peers, potential clients, recruiters, or industry contacts
output_format: LinkedIn post with a strong hook, line-broken paragraphs, a key insight, and a clear call to action — or a profile section (About, Experience summary) in first person
---

# LinkedIn Prompts

## Purpose

LinkedIn content fails when it is vague, self-promotional, or indistinguishable from a hundred other posts. It works when it is specific, honest, and gives the reader something — an insight, a useful perspective, a piece of knowledge they can use. Use these prompts when you want to write a post that goes beyond announcing a promotion or sharing a bland opinion, a profile About section that says something real about who you are and what you offer, or a connection message that earns a reply. All LinkedIn content should sound like a real person, not a corporate communications department.

## Copy-paste prompt — LinkedIn post

```
You are a LinkedIn content strategist with experience writing for professionals in technology, finance, and advisory services. Write a LinkedIn post that earns genuine engagement from a professional audience.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (the insight, experience, story, or information to share; any data or examples to include):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 150–400 words; LinkedIn posts over 400 words work only if the content is genuinely substantive]

FORMAT: [FORMAT — recommended: hook (1–2 lines) / insight or story (3–5 short paragraphs with line breaks between each) / key takeaway / call to action or question]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a hook in the first one or two lines that makes the reader stop scrolling. The hook should state a surprising fact, a counter-intuitive observation, a specific question, or a strong opinion. Do not open with "I'm excited to share...", "I recently had the opportunity to...", or "In today's fast-paced world...".
3. Use short paragraphs and line breaks between each. LinkedIn is read on mobile. Dense paragraphs are skipped.
4. Be specific. A post about "the importance of access control" tells the reader nothing. A post about "discovering 340 stale privileged accounts at a firm that thought its IAM was under control" tells a story.
5. Include at least one concrete detail, statistic, or named example from the input. Vague generalities do not earn engagement.
6. The key takeaway should be a single, clear insight that the reader can take away and use or share. Avoid "the lesson here is that communication is important".
7. End with a call to action or an open question that invites a specific type of response — not "what do you think?" but something that gives the reader a hook to reply to.
8. Do not use corporate filler: no "exciting", "thrilled", "honoured", "humbled", "game-changing", "transformational". Write as a direct, thoughtful professional.
9. Distinguish between personal experience and general claims. If you are sharing an observation from your own work, frame it as such ("in our experience" or "I've seen this in three separate engagements") — do not present it as universal truth.
10. If the input includes uncertainty or caveats, preserve them — do not flatten nuance to make a point sharper.
11. Tone: [TONE].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the post. No preamble.
```

## Copy-paste prompt — LinkedIn About section

```
You are a professional profile writer. Write a LinkedIn About section that is authentic, specific, and gives a reader a clear sense of who this person is and what they offer.

AUDIENCE: [AUDIENCE — e.g. potential clients, hiring managers, professional peers]

PURPOSE: [PURPOSE — e.g. attract inbound opportunities, support a career transition, establish thought leadership]

CONTEXT: [CONTEXT]

INPUT (career background, key achievements, specialist areas, professional values, and what the person is looking for or offering):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE — recommended: first person, professional but human]

LENGTH: [LENGTH — recommended: 200–350 words]

FORMAT: [FORMAT — recommended: opening statement of professional identity / two to three paragraphs of specific experience and expertise / what you offer or are looking for / optional: a human detail that makes you memorable]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English in first person ("I", not "James is a...").
2. Open with a clear, specific statement of professional identity — not a job title, but a sentence that says what you do and for whom, or what problem you solve.
3. Include at least two specific achievements or areas of expertise with concrete evidence.
4. Write as a human being, not a corporate bio. Avoid: "results-driven", "strategic thinker", "dynamic leader", "passionate about", "proven track record".
5. If appropriate, include one sentence that humanises the person — a perspective, a working principle, or an interest that is genuine and professional.
6. End with what you are looking for or what you offer to people who connect with you.
7. Output only the About section. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who you are writing for on LinkedIn. Examples: "CIOs, Heads of IT, and senior technology leaders in UK financial services", "recruiters and hiring managers in professional services", "peers in the identity and access management community".
- `[PURPOSE]` — what the post or profile section needs to achieve. Examples: "share a lesson from a recent IAM programme", "announce a new role in a way that adds professional value", "attract inbound enquiries for cloud advisory work".
- `[CONTEXT]` — background for the LLM. Examples: "the author just completed a major IAM transformation at a UK insurer", "the author is transitioning from consulting to in-house and wants to signal this to their network", "this is a thought leadership post — the author has no specific news to share, just an insight worth sharing".
- `[INPUT]` — the specific content: the story, insight, data, or experience to draw on. The more specific, the better.
- `[DESIRED_OUTCOME]` — what you want to happen. Examples: "the post generates 20+ comments from technology peers", "the profile attracts five inbound messages from potential clients per month", "the post leads to at least one speaking invitation".
- `[TONE]` — for posts: "direct, thoughtful, conversational". For About sections: "first person, professional but human".
- `[LENGTH]` — posts: 150–400 words. About sections: 200–350 words.
- `[FORMAT]` — use the recommended structures. For posts, do not write in bullet points — LinkedIn posts perform better as short prose paragraphs.
- `[CONSTRAINTS]` — examples: "do not name the client in the post — refer to 'a UK financial services firm'", "include a hashtag recommendation (3–5 relevant hashtags)", "the author prefers not to use emojis".

## Example input — LinkedIn post

```
AUDIENCE: CIOs, Heads of IT Security, and senior technology leaders in UK financial services
PURPOSE: Share a counter-intuitive lesson from a recent IAM (Identity and Access Management) programme
CONTEXT: The author is a cloud and IAM consultant at Meridian Advisory. The post should establish credibility and generate conversation about IAM governance.
INPUT:
  The insight: most organisations think their IAM problem is a technology problem. They buy a platform, implement it, and still have the same access hygiene issues 12 months later. The real problem is that no one owns the governance model — the questions of who should have access to what, how often it should be reviewed, and who approves exceptions. Without clear governance, any platform will accumulate stale access.
  Specific example: at a recent engagement (UK financial services firm, anonymised), a pre-migration audit found 340 stale privileged accounts — some belonging to people who had left the organisation two years prior. The firm had an IAM platform in place. They just hadn't defined who was responsible for reviewing accounts after departure.
  Key takeaway: the platform is not the solution. The governance model is.
DESIRED_OUTCOME: Post generates 15+ comments from technology and security professionals; ideally leads to inbound enquiries about IAM advisory work.
TONE: Direct, thoughtful, opinionated but evidence-based — not preachy
LENGTH: 200–280 words
CONSTRAINTS: Do not name the client. Do not use the word "journey". Include 3–4 relevant hashtags at the end.
```

## Example output

---

340 privileged accounts belonging to people who'd already left the organisation.

Some had been dormant for two years.

This wasn't a small firm with no IT budget. They had an IAM platform. They had a security team. They just hadn't answered a basic question: who is responsible for reviewing access after someone leaves?

We found this during a pre-migration audit at a UK financial services firm. The accounts weren't being used — as far as we could tell. But "as far as we could tell" is a deeply uncomfortable phrase when you're dealing with privileged access in a regulated environment.

The common assumption is that IAM is a technology problem. Buy the right platform, configure it correctly, and the access hygiene problem goes away.

It doesn't.

The platform can automate what you tell it to automate. But someone has to define: what access should each role have? How often should it be reviewed? Who approves exceptions? What happens when someone changes role but keeps their old access?

These are governance questions, not technology questions. And in most organisations, no one has clean ownership of the answers.

The firms I've seen run successful IAM programmes start by defining the governance model. The technology comes second — and the implementation is considerably faster when the hard questions have already been answered.

If your organisation has an IAM platform and still has access review completion rates below 80%, the platform isn't the problem.

What's your experience? Are governance or technology problems the bigger barrier where you work?

#IAM #IdentityAndAccessManagement #CyberSecurity #CloudSecurity #FinancialServices

---

## Review checklist

- [ ] Hook appears in the first one to two lines and does not open with a cliché
- [ ] Short paragraphs with line breaks between each — no dense blocks
- [ ] At least one specific detail, statistic, or example from the input
- [ ] Key takeaway is a single, clear, usable insight
- [ ] Call to action or question at the end invites a specific type of response
- [ ] No corporate filler: no "excited", "thrilled", "honoured", "game-changing"
- [ ] Observations are framed as the author's experience, not universal truth
- [ ] Caveats and nuance from the input are preserved
- [ ] British English used throughout
- [ ] Length is within the recommended range

---

See [styles/social-media-style.md](../styles/social-media-style.md) for social media style.
