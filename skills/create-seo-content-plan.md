---
title: Create SEO Content Plan
skill_type: Content strategy
output: SEO content strategy with topic clusters, priority pages, content briefs, internal linking plan, and 90-day editorial roadmap
tools_needed: LLM with browsing or supplied content inventory; optional keyword tool, Search Console, analytics, competitor URLs, CMS export
difficulty: Medium
---

# Skill: Create SEO Content Plan

## What this skill does

Turns a website, topic, product, or service into a practical SEO content plan. The output should identify the pages that need to exist, the intent each page should satisfy, how pages should link to each other, and what should be produced first.

The plan must not pretend to know search volume or ranking difficulty unless that data is supplied. Where keyword data is absent, use relative opportunity and clearly explain the basis.

## When to use it

- Planning a new website section, service page set, knowledge hub, or blog programme
- Turning a business topic into SEO-friendly page ideas and briefs
- Improving an existing site where content is thin, duplicated, or badly mapped to user intent
- Briefing a writer, subject-matter expert, or agency
- Building a 90-day content roadmap after a website audit

## Inputs required

- Website URL or content inventory
- Business context and products/services
- Target audience and buying journey
- Geography and language
- Competitors or reference sites
- Seed topics or keywords, if available
- Search Console, analytics, or keyword data, if available
- Content constraints: compliance review, SME availability, brand voice, CMS limits

## Process

1. **Map audience intent**
   - Identify what the audience needs to know at awareness, consideration, decision, and retention stages.
   - Separate informational, commercial, comparison, local, and support intent.

2. **Assess existing content**
   - Review visible pages or supplied inventory.
   - Note content strengths, duplication, thin coverage, missing proof, stale pages, and orphaned pages.

3. **Define topic clusters**
   - Build clusters around services, problems, industries, locations, comparisons, and buyer objections.
   - Each cluster should have a hub page and supporting pages where useful.

4. **Prioritise page opportunities**
   - Prioritise by commercial relevance, intent clarity, current gap severity, proof availability, production effort, and confidence.
   - Do not prioritise by invented search volume.

5. **Write content briefs**
   - For each priority page, define audience, intent, page goal, suggested title, outline, required proof, CTA, internal links, and review owner.

6. **Create the roadmap**
   - Sequence the work over 30, 60, and 90 days.
   - Include measurement and maintenance actions.

## Copy-paste prompt

```text
You are an SEO content strategist and editorial planner. Build a practical SEO content plan from the website and context below.

WEBSITE_URL: [URL]
BUSINESS_CONTEXT: [What the organisation sells, market, business model, differentiators]
TARGET_AUDIENCE: [Personas, roles, needs, objections, buying journey]
GEOGRAPHY_AND_LANGUAGE: [Markets, regions, local/international scope]
KNOWN_COMPETITORS: [URLs or names]
SEED_TOPICS_OR_KEYWORDS: [Optional]
EXISTING_CONTENT: [Sitemap, URLs, page titles, blog list, CMS export, or page copy]
DATA_AVAILABLE: [Search Console / analytics / keyword tool / none]
CONSTRAINTS: [Compliance, SME availability, brand, CMS, budget, timing]

Output:
1. Content strategy summary
2. Audience and intent map
3. Existing content strengths and gaps
4. Recommended topic clusters
5. Priority page opportunities
6. Content briefs for the top five pages
7. Internal linking plan
8. 90-day editorial roadmap
9. Measurement plan
10. Assumptions and missing data

Constraints:
- Use British English.
- Do not invent keyword volume, ranking difficulty, traffic, or rankings.
- If keyword data is not supplied, use relative opportunity and explain the basis.
- Separate commercial pages, educational pages, comparison pages, proof pages, local pages, and support pages.
- Each content brief must include: audience, search intent, primary question, page goal, suggested title, outline, proof points needed, CTA, internal links, and SME/reviewer.
- Flag claims that require expert or legal review.
```

## Suggested output structure

| Section | What it should contain |
|---|---|
| Content strategy summary | What content should do commercially and where the current gap is |
| Intent map | Audience questions by funnel stage |
| Topic clusters | Hub and support pages grouped by theme |
| Priority pages | Ranked opportunities with rationale |
| Content briefs | Copy-ready briefs for writers or SMEs |
| Internal linking plan | Hub, spoke, commercial, and proof-page links |
| Roadmap | 30/60/90-day content schedule |
| Measurement plan | Search Console, analytics, conversions, engagement, and review cadence |

## Quality controls

- [ ] No invented keyword volume or ranking claims.
- [ ] Every recommended page has a clear user intent and commercial reason to exist.
- [ ] Content briefs include proof points, not just headings.
- [ ] Internal links support both users and crawl paths.
- [ ] The roadmap is feasible for the available writers and reviewers.
- [ ] Measurement is defined before publication.

## Common failure modes

- **Blog-first thinking**: Many SEO opportunities require service, comparison, proof, or local pages, not blog posts.
- **Keyword list without intent**: A keyword is not a brief. Define the user's question and decision stage.
- **No proof**: High-intent pages need evidence: case studies, credentials, results, pricing cues, process, or guarantees.
- **No maintenance**: Content plans need refresh triggers for stale claims, pricing, law, product changes, and market shifts.
