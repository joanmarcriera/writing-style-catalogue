---
title: Journalistic Style
category: Engaging
aliases: [News Writing, Storytelling]
---

# Journalistic Style

## What This Style Is

Engaging narrative writing with news hook, story structure, and human interest. Answers "who, what, when, where, why" upfront, then elaborates. Used for news, announcements, and compelling external communications.

**Core principle**: Hook first, then story, then sources or context.

## When to Use It

- Press releases
- Company announcements
- Public-facing news
- Internal communications with narrative
- Marketing or thought leadership
- Customer communications

## When NOT to Use It

- Formal governance documents (use Board Paper)
- Quick decisions (use BLUF)
- Technical explanations (use Technical Documentation)
- Persuasive recommendations (use Consulting)

## Core Structure

```
[HEADLINE]
Clear, compelling, answers the main question.

[LEDE (OPENING PARAGRAPH)]
Answers who, what, when, where, why. Essential facts first.

[SUPPORTING FACTS]
Expands on lede; includes quotes or context.

[BACKGROUND]
Historical context or market situation.

[IMPLICATIONS]
Why this matters; what comes next.

[SOURCES OR CONTACT]
Where to learn more.
```

## Copy-Paste Prompt Template

```
You are a journalist. Write a news story from:

MAIN NEWS:
[What happened]

CONTEXT:
[Why does it matter]

KEY FACTS:
[Who, what, when, where, relevant details]

QUOTES OR REACTIONS:
[Stakeholder perspectives]

IMPLICATIONS:
[What's the impact or next step]

INSTRUCTIONS:
1. Write a compelling headline
2. Lead with the main fact (lede)
3. Expand with supporting details
4. Provide context and background
5. End with implications or forward look
6. Aim for 500–800 words
7. Use active voice and specific language

Output only the news story. No preamble.
```

## Short Example

**Headline: Engineering Team Launches Open-Source Analytics Platform**

A 12-person engineering team at TechCorp has released DataMesh, an open-source analytics platform that simplifies data pipeline building for mid-sized companies. The platform eliminates boilerplate code, cutting typical setup time from 3 months to 2 weeks.

The release comes amid rising demand for flexible, self-managed analytics tools. DataMesh is available on GitHub starting today and is already attracting interest from data engineering communities.

"We built DataMesh because we kept solving the same problems in customer projects," says Alex Chen, lead engineer on the project. "Open-sourcing it lets the community improve it faster than we could alone."

The platform uses a declarative configuration model, allowing engineers to define data pipelines in YAML without writing custom code. Early adopters in the beta programme reduced development time by 40%.

The move represents a shift toward open-source tooling in enterprise data engineering. Competitors like Apache Airflow dominate complex orchestration; DataMesh targets the simpler use cases where existing tools are overkill.

TechCorp's commercial offering, DataMesh Enterprise, will provide hosted infrastructure, monitoring, and professional support. The open-source release aims to build community and reduce adoption barriers.

DataMesh is available at github.com/techcorp/datamesh. Documentation and tutorials are at datamesh.dev.

## Quality Checklist

- [ ] Headline is clear and compelling
- [ ] Lede answers who, what, when, where, why
- [ ] Most important facts come first
- [ ] Story is engaging and human
- [ ] Source or context is provided
- [ ] Length is appropriate (500–800 words)
- [ ] Active voice throughout

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Burying the news | Reader doesn't know what happened | Lead with the main fact in lede |
| Too much background | Story gets lost | Save context for second half |
| Missing quotes | Sounds impersonal | Include stakeholder perspectives |
| Vague headlines | Reader doesn't know if story is relevant | Be specific: name the news |
| No implications | Reader unsure why they should care | Explain impact or forward look |

---

See [prompt-templates/presentation-prompts.md](../prompt-templates/presentation-prompts.md) for public comms templates.
