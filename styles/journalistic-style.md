---
title: Journalistic Style
category: Persuasive
best_for: Press releases, company announcements, public-facing news content, and internal communications requiring a compelling narrative. Ideal when the audience is mixed, the content has a genuine news element, and the goal is engagement as much as information transfer. Works well for product launches, partnership announcements, and thought leadership pieces.
not_good_for: Formal governance documents requiring complete options analysis (use Board Paper Style); technical explanations for practitioner audiences (use Technical Documentation); persuasive recommendations requiring structured logical argument (use Consulting Style or Minto Pyramid).
default_tone: Engaging and clear. Active and specific. Confident without being promotional.
typical_length: 400–800 words for a press release or news story; 800–1,500 words for a feature or announcement piece
aliases: [News Writing, Press Release Style, Inverted Pyramid]
---

# Journalistic Style

## What this style is

Journalistic style is the craft of communicating news in a way that is immediately clear, engaging, and trustworthy. It answers the essential questions — who, what, when, where, why — in the opening paragraph (the "lede"), then provides supporting detail, context, and background in descending order of importance. The structure is known as the inverted pyramid: the most important information appears first, the least important last.

The power of journalistic style is its reader orientation. Every sentence earns its place by adding information the reader needs or wants. Quotes bring human perspective and credibility. Context explains why this matters. Implications look forward to what comes next. The reader can stop at any point and will have received the most important information first.

**Core principle**: Hook first — with the essential fact — then story, then context and sources. The most important information always appears before the less important.

## When to use it

- Press releases for product launches, funding rounds, partnerships, or corporate announcements
- Company blog posts or thought leadership pieces for public audiences
- Internal company announcements where the narrative matters as much as the facts
- Customer communications announcing a significant service change or milestone
- Marketing content that needs to feel credible and newsworthy rather than promotional
- Case studies or success stories written for external publication
- Speeches or remarks for public events that will be quoted or reported

## When not to use it

- Formal governance documents — use [Board Paper Style](board-paper-style.md) instead
- Quick internal decisions — use [BLUF](bluf-bottom-line-up-front.md) instead
- Detailed technical explanations for practitioner audiences — use [Technical Documentation](technical-documentation.md) instead
- Persuasive structured recommendations — use [Consulting Style](consulting-style.md) or [Minto Pyramid Principle](minto-pyramid-principle.md) instead
- Personal, emotional communications — use [Narrative Storytelling](narrative-storytelling.md) instead

## Core structure

```
[HEADLINE]
Clear and compelling. Answers what happened.
8–12 words. Specific — includes a name, number, or outcome.
Not a teaser — tells the story, not just hints at it.

[LEDE — OPENING PARAGRAPH]
The single most important fact.
Answers: who, what, when, where, why (and sometimes how).
Written as one to three sentences.
A reader who reads only this paragraph must understand the story.

[NUT GRAF — "NUTSHELL" PARAGRAPH]
Why this matters. Context for the news.
Why now. What changes for the reader.
1–2 sentences connecting the news to broader significance.

[SUPPORTING FACTS]
Expansion of the lede. Key details and data.
Quotes from key figures (with full name and title).
Specific numbers and evidence that substantiate the claim.

[BACKGROUND]
Historical context. Prior state of affairs.
Market or industry context.
How we got here. Prior decisions or milestones relevant to this story.

[IMPLICATIONS OR FORWARD LOOK]
What happens next. What this means going forward.
Future milestones or decisions.
Broader industry impact.

[CONTACT OR SOURCE]
Where to get more information.
Press contact details (for press releases).
Links to further reading or resources.
```

## Copy-paste prompt

```
You are an experienced journalist and communications writer. Your task is to write a news story or press release from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Technology journalists and editors at national and trade publications", "All employees receiving an internal announcement", "Potential customers and partners in the cloud infrastructure space"]
PURPOSE: [PURPOSE — e.g. "Announce the completion of a cloud migration programme", "Write a press release for a £5M Series A funding round", "Publish an internal announcement about a new IAM platform go-live"]
CONTEXT: [CONTEXT — e.g. "The migration was completed four days ahead of schedule; this is the culmination of an 18-month programme; we are the first UK financial services firm to run fully on AWS in this sector"]
INPUT: [INPUT — paste all relevant facts, quotes, data, background information, and your key messages here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Journalists have all the facts they need to write an accurate story without follow-up; employees feel informed and proud of the achievement"]
TONE: [TONE — e.g. "Clear and engaging, not promotional", "Confident without being boastful", "Warm and celebratory for an internal announcement"]
LENGTH: [LENGTH — e.g. "500–700 words for a press release", "300–400 words for an internal announcement"]
FORMAT: [FORMAT — e.g. "Press release format with headline, dateline, body, and boilerplate", "News story format with headline, lede, and inverted pyramid structure"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not disclose investor names until embargo lifts on 16 May", "All financial figures must be approved by the CFO before use", "Do not quote any individual who has not approved their quote"]

INSTRUCTIONS:
1. Write a headline that tells the story specifically — not a teaser. Include a name, number, or outcome. Maximum 12 words.
2. Write a lede paragraph (1–3 sentences) that answers who, what, when, where, and why. This paragraph must stand alone — a reader who reads only this must understand the news.
3. Write a nut graf explaining why this matters and why now.
4. Expand with supporting facts from [INPUT]. Use specific numbers and evidence. Every factual claim must come from [INPUT] — do not add information not provided.
5. Include at least one quote with full name and job title. The quote must provide human perspective or insight — not restate the facts.
6. Provide background context in the final third of the piece.
7. Close with a forward-looking implication or next step.
8. Use British English throughout (colour, organisation, licence, favour, etc.).
9. Distinguish facts from assumptions. Flag any claim not confirmed in [INPUT] with "(assumed)" in parentheses.
10. Total length must not exceed [LENGTH].

Output the news story or press release only. No preamble, no commentary.
```

## Output format

A press release or news story in journalistic style is formatted as follows:

- **Headline**: Bold, title case, 8–12 words
- **Dateline** (for press releases): City, date — e.g. "London, 14 May 2026 —"
- **Lede**: 1–3 sentences, plain prose, maximum 60 words
- **Body**: Short paragraphs of 2–3 sentences each; total 400–800 words
- **Quotes**: Attributed with full name and current job title; introduced with a comma, not a colon
- **Boilerplate** (for press releases): "About [Company]" section of 50–100 words at the end
- **Press contact** (for press releases): Name, email, telephone number

Internal announcements follow the same inverted pyramid structure but may omit the dateline, boilerplate, and press contact. They may use a slightly warmer tone and may end with a team acknowledgement or call to celebrate.

## Example

**Headline: UK Financial Services Firm Completes AWS Migration Ahead of Schedule — Reducing Infrastructure Costs by 34%**

*London, 14 May 2026* — Acme Financial Services has completed the migration of its entire production infrastructure to Amazon Web Services (AWS), finishing the 18-month programme four days ahead of the original deadline and 8% under budget. The migration eliminates the firm's last on-premises data centre and is expected to reduce infrastructure operating costs by £840,000 annually.

The completion marks a milestone in Acme's three-year cloud-first technology strategy, approved by the board in 2023. The firm becomes one of the first mid-sized UK financial services organisations to operate with no on-premises infrastructure.

"This project was about more than cost savings," said Priya Nair, Chief Technology Officer at Acme Financial Services. "Running entirely on AWS gives us the elasticity to scale our systems in hours rather than months — that's a genuine competitive advantage when market conditions change rapidly."

The migration involved moving 47 production applications, 2,300 user accounts, and over 14 terabytes of operational data across three phases. An external delivery partner provided specialist AWS migration expertise alongside a 12-person internal engineering team. The parallel-operation period — during which both on-premises and cloud infrastructure ran simultaneously — was reduced from a planned six months to four months, contributing to the schedule improvement.

The move resolves two audit control gaps identified in Acme's December 2025 ISO 27001 review: centralised audit logging and automated configuration compliance monitoring are now managed natively through AWS CloudTrail and AWS Config. The firm expects to complete its ISO 27001 recertification by November 2026.

**Background**

Acme Financial Services has operated its own data centre since 2008. The facility's lease was due for renewal in 2029 at a projected cost of £3.6M over five years, providing the economic impetus for the migration decision. The board approved the cloud migration programme and £600,000 capital budget in January 2025 following a six-month options assessment.

**What comes next**

The engineering team will now focus on optimising AWS costs through reserved instance commitments and automated scaling policies. The firm has set a target of a further 12% reduction in cloud operating costs by Q1 2027 through these measures. A full programme retrospective and lessons-learned document will be shared with the board in June 2026.

*For media enquiries: communications@acme-financial.com | +44 20 7000 0000*

**About Acme Financial Services**
Acme Financial Services is a UK-based financial services firm providing asset management, fund administration, and investor reporting services to institutional clients across Europe. Founded in 1997 and headquartered in London, the firm manages assets totalling £4.2 billion on behalf of clients in 12 countries.

## Quality checklist

- [ ] Headline is specific — contains a name, number, or outcome; not a teaser
- [ ] Lede answers who, what, when, where, and why in 1–3 sentences
- [ ] Nut graf explains why this matters and why now
- [ ] Most important facts appear before less important context
- [ ] At least one quote with full name and current job title
- [ ] Quote adds perspective — does not merely restate the facts
- [ ] All factual claims come from [INPUT] — no invented details
- [ ] Background context appears in the final third, not the first
- [ ] Length is appropriate for the stated format and audience
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Burying the news | Reader does not know what happened | Lead with the main fact in the lede — every time |
| Teaser headline | Reader scrolled past before reading the story | Tell the story in the headline: "Company Completes X" not "Big News on X" |
| Too much background before the news | Story is lost; reader has already moved on | Save context for the second half of the piece |
| Missing or weak quotes | Sounds impersonal and unconvincing | Include a specific, human quote that adds perspective |
| Promotional language | Reads like an advert; loses credibility | Use factual, specific language — let the facts do the selling |
| Vague implications | Reader unsure why they should care | Explain the impact: "this means X for customers" |
| No boilerplate or press contact | Journalists cannot write the story or follow up | Always include company description and media contact |

---

See [prompt-templates/presentation-prompts.md](../prompt-templates/presentation-prompts.md) for public comms templates.
