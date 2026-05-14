---
title: Social Media Style
category: Persuasive
best_for: LinkedIn posts, X (Twitter) posts, and internal Slack or Teams announcements where the goal is to communicate with authenticity and engage an audience that is scrolling quickly. Particularly effective for thought leadership, company announcements, product moments, and professional insights shared by individuals or organisations.
not_good_for: Formal business communication requiring professional register (use Board Paper Style or Executive Briefing); technical documentation for practitioners (use Technical Documentation); crisis communications requiring precision and completeness (use Crisis Communications).
default_tone: Conversational and authentic. Platform-specific — professional on LinkedIn, punchy on X, casual on Slack. Direct and opinionated.
typical_length: LinkedIn: up to 1,300 characters (short) or 3,000 characters (long form); X: under 280 characters per post; Slack: 1–5 short paragraphs
aliases: [Social Posts, LinkedIn Post, X Post, Twitter Post]
---

# Social Media Style

## What this style is

Social media writing is the art of communicating in a noisy, fast-moving environment where the reader's attention is measured in seconds. The fundamental challenge is the same across all platforms: earn the next line. Social media readers make an instant decision — keep reading or scroll — and that decision is made in the first two or three words of the post.

Effective social media writing is not informal corporate communication — it is authentic, opinionated, and human. It tells a story, shares a perspective, or reveals something the reader does not already know. It earns engagement by offering genuine value: insight, entertainment, or connection. Writing that sounds like a press release or a brand announcement will be scrolled past. Writing that sounds like a real person with a real perspective will stop the scroll.

**Core principle**: Hook → Point → Engagement. The first line earns the read; the point delivers the value; the engagement element (question, CTA, or perspective) earns the response.

## When to use it

- LinkedIn posts sharing professional insight, career reflections, or industry observations
- Company announcement posts on LinkedIn or X for product launches, milestones, or hires
- Thought leadership posts from founders, executives, or senior practitioners
- X (Twitter) commentary on industry news, trends, or conference moments
- Internal Slack or Teams announcements for product launches, team wins, or culture moments
- Community engagement posts inviting discussion, feedback, or perspective sharing

## When not to use it

- Formal business communication requiring professional register — use [Board Paper Style](board-paper-style.md) or [Executive Briefing](executive-briefing.md) instead
- Technical documentation for practitioners — use [Technical Documentation](technical-documentation.md) instead
- Crisis communications — use [Crisis Communications](crisis-communications.md) instead
- Persuasive recommendations for business decisions — use [Consulting Style](consulting-style.md) instead

## Platform considerations

**LinkedIn**: Professional audience; up to 3,000 characters for long-form posts; the first 2–3 lines appear before "see more" — they must hook the reader. Line breaks between every 1–3 sentences. Bullet points work well. Questions at the end drive comments. Tone: professional but personal; first person; opinionated.

**X (Twitter)**: 280 characters per post; punchy and conversational; threads work for longer points. No filler words — every word must earn its place. Questions and hot takes drive engagement. Tone: confident, direct, often humorous or provocative.

**LinkedIn Newsletter**: Long-form; 1,000–3,000 words; more like a blog post. Structured with headers. Deeper analysis and perspective. Sent to subscribers.

**Slack / Teams**: Casual; short paragraphs; emoji acceptable; links to further detail. Tone: friendly, direct, human.

## Core structure

```
[HOOK — FIRST 1–3 LINES]
Must earn the "see more" click or the continued read.
Options:
- A counterintuitive statement ("I was wrong about X")
- A specific number or fact ("We cut our cloud bill by 42% in 90 days")
- A question the reader wants answered ("What actually causes most IAM incidents?")
- A short, punchy observation that is not obvious

[THE POINT]
The substance of the post.
The insight, the story, the lesson, or the perspective.
Be specific — specificity is what makes it real and shareable.

[THE EVIDENCE OR STORY]
What makes the point credible.
A specific example, a data point, a personal experience.
Not a generic claim — something the reader cannot get elsewhere.

[THE ENGAGEMENT ELEMENT]
A question that invites response.
A perspective statement that invites disagreement or agreement.
A clear call to action (share this, try this, read this).
```

## Copy-paste prompt

```
You are an expert social media writer specialising in professional platforms. Your task is to write a social media post from the following brief.

AUDIENCE: [AUDIENCE — e.g. "IT security professionals and CISOs on LinkedIn", "Engineering leaders and architects on X", "Product managers and SaaS founders on LinkedIn", "Internal engineering team on Slack"]
PURPOSE: [PURPOSE — e.g. "Share an insight from our IAM migration on what made it succeed", "Announce the launch of our zero-trust product module", "Comment on a common misconception about Kubernetes that engineers encounter", "Celebrate the team completing the cloud migration ahead of schedule"]
CONTEXT: [CONTEXT — e.g. "We completed an 18-month IAM migration last week; the most important lesson was not technical", "We are launching at 09:00 tomorrow — the post goes live at 08:45"]
INPUT: [INPUT — paste the key insight, story, data point, or message you want to communicate here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Engineers who have experienced this problem recognise it and share or comment", "Potential customers click through to the product page", "Team feels genuinely celebrated and proud of the achievement"]
TONE: [TONE — e.g. "Personal and authentic — first person, no corporate language", "Direct and slightly provocative — challenge a common assumption", "Warm and celebratory for an internal Slack post"]
LENGTH: [LENGTH — e.g. "LinkedIn long-form: 1,000–1,500 characters", "X post: under 260 characters", "Slack announcement: 150–200 words"]
FORMAT: [FORMAT — e.g. "LinkedIn post with line breaks between every 1–2 sentences, bullet points for a list section, and a question at the end", "X thread of 4–5 posts", "Slack message with emoji, bold for key points, and a link"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not mention competitor products by name", "Do not disclose the specific customer involved in the example", "Must be suitable for reposting by individuals on their own profiles without modification"]

INSTRUCTIONS:
1. Write a hook in the first 1–3 lines that earns the "see more" click or the continued read. It must not begin with "I'm excited to share," "Thrilled to announce," or any variation. It must not be generic.
2. Deliver specific, real value in the body. The reader must learn, recognise, or feel something they would not get from a generic post.
3. Use line breaks between every 1–3 sentences for LinkedIn. Do not write dense paragraphs.
4. Include a closing engagement element: a question, a perspective statement, or a clear CTA. Not all three.
5. Match the tone exactly to [TONE] and the length to [LENGTH]. A LinkedIn long-form post is not the same length as an X post.
6. Use British English throughout (colour, organisation, licence, favour, etc.).
7. Preserve all facts, figures, and specific details exactly as provided in [INPUT]. Do not invent metrics or outcomes.
8. Flag any claim that is an assumption rather than confirmed with "(assumed)" in parentheses.
9. Do not use: "I'm excited to share," "thrilled to announce," "game-changing," "groundbreaking," "revolutionary," "leverage," "synergies," or any corporate-speak equivalent.
10. Total length must be within [LENGTH].

Output the social media post only. No preamble, no commentary.
```

## Output format

Social media posts are plain text with manual line breaks. They do not use Markdown headers or formal formatting. The visual structure comes from short paragraphs and deliberate line breaks.

**LinkedIn post:**
- First 2–3 lines before "see more": hook only — no context yet
- Body: short paragraphs of 1–3 sentences, separated by single blank lines
- Lists: bullet points (•) or numbers; not more than 6 items
- Close: question or CTA on its own line
- No hashtags required; 2–3 relevant hashtags acceptable if natural

**X (Twitter) post:**
- Single post: under 280 characters, ideally under 240 for retweet headroom
- Thread: 4–8 posts; first post is the hook; each subsequent post adds one point; last post is the CTA or question

**Slack / Teams:**
- Bold for key terms or the headline point (`*bold*` in Slack)
- Emoji acceptable and expected
- Link at the end
- @mention if action is required from a specific person

## Example

**LinkedIn — Long Form Post (IT leadership / cloud migration context)**

I spent 18 months on a cloud migration.

The hardest part was not the technology.

We moved 47 production applications, 2,300 user accounts, and 14TB of data from a data centre we had operated since 2008 to AWS.

The architecture was complex. The data migration was meticulous. The parallel-operation period — running both systems for four months — was genuinely difficult.

But none of that was the hard part.

The hard part was the moment our most senior infrastructure engineer said, in a call with 12 people, "I got the VPC peering configuration wrong. We need to redesign the spoke network."

She had spent three weeks on that design.

The room went quiet for about four seconds.

Then one of the junior engineers said: "OK. Let's look at what we have and work out what changes."

That was it.

No blame. No defensiveness. No lengthy post-mortem about how we got here. Just: what do we have, and what do we do next?

We lost three days. We recovered everything and completed the migration four days ahead of schedule overall.

Here is what I took from that moment:

• Psychological safety is not a nice-to-have. It is the single biggest multiplier on a team's ability to recover from failure.
• The speed of recovery depends on whether people can say "I got this wrong" in a room of peers without consequences.
• You build that culture before the crisis, not during it.

The next migration I lead, I will spend as much time on team culture as I spend on architecture.

What is the hardest part of a large-scale technical programme you have worked on? I would be curious whether it matched the one people expected.

---

**X post (same context, condensed)**

18 months. 47 apps. 14TB. AWS migration.

The hardest part wasn't the architecture.

It was a senior engineer saying "I got the VPC design wrong" in front of 12 people.

We lost 3 days. Still finished 4 days early.

Psychological safety > architectural elegance.

---

**Slack post (internal team celebration)**

🎉 **We're done.**

The migration is complete. 47 apps, 2,300 accounts, 14TB — all on AWS. Four days ahead of schedule, 8% under budget.

This was 18 months of work across four teams. Every one of you contributed something to make it happen — from the junior engineers running weekend deployment checks to the architects who redesigned the spoke network from scratch in three days when we needed to.

The platform team will share the full retrospective on 22 May. For now: thank you. This was genuinely hard, and you did it brilliantly.

Grab a drink at the team lunch tomorrow — details in the calendar invite. 🍻

---

## Quality checklist

- [ ] First line hooks the reader — does not begin with "excited to share" or generic corporate language
- [ ] The body delivers specific, real value — not a generic observation
- [ ] Line breaks used appropriately for the platform (LinkedIn: between every 1–3 sentences)
- [ ] Length is appropriate for the platform: LinkedIn under 3,000 characters; X under 280 characters per post
- [ ] A closing question, CTA, or perspective statement is included
- [ ] Language is conversational — sounds like a real person, not a brand
- [ ] No corporate buzzwords or filler phrases
- [ ] Specific details from [INPUT] are preserved exactly — no invented figures
- [ ] British English used throughout
- [ ] Post is appropriate for the named platform

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Opening with "I'm excited to share" or "Thrilled to announce" | Most scrolled-past opener on professional platforms; signals generic content | Open with the specific insight, result, or counterintuitive point |
| Dense paragraphs on LinkedIn | Hard to read; most readers stop before the end | Single blank line between every 1–3 sentences |
| Generic observations ("culture matters," "communication is key") | No value for the reader; they already know this | Make the specific point with specific evidence from your experience |
| No engagement element | Low comments and shares | End with a genuine question or a perspective that invites response |
| Corporate-speak ("leverage synergies," "move the needle") | Sounds like a brand, not a person | Write as yourself; use plain, direct language |
| Same post across all platforms | X post is too long; LinkedIn post is too short; Slack tone is wrong | Write a platform-specific version for each — they are genuinely different |
| Too many hashtags | Looks desperate; reduces credibility | 0–3 hashtags maximum; only where genuinely relevant |

---

See [prompt-templates/linkedin-prompts.md](../prompt-templates/linkedin-prompts.md) for LinkedIn templates.

See [prompt-templates/sales-outreach-prompts.md](../prompt-templates/sales-outreach-prompts.md) for outreach posts.
