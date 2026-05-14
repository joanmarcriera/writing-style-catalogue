---
title: Create Website Marketing and SEO Audit
skill_type: Analysis and action planning
output: A URL-led website audit report with current-state scorecard, evidence, recommendations, 30/60/90-day plan, and implementation backlog
tools_needed: LLM with browsing or supplied page evidence; optional crawler, analytics, Search Console, PageSpeed/Lighthouse, CMS access, keyword tool
difficulty: Complex
---

# Skill: Create Website Marketing and SEO Audit

## What this skill does

Produces a practical website marketing and SEO audit from a URL and supporting context. The output should explain the current state, identify the biggest constraints on discoverability and conversion, and convert findings into a prioritised action plan.

This is not a generic SEO checklist. The report must connect technical, content, messaging, trust, measurement, and conversion findings to the organisation's commercial goal.

## When to use it

- You have a website URL and need to know what is working, what is weak, and what to do next
- You are preparing a marketing, SEO, or website improvement plan
- You need an executive-friendly diagnosis plus a delivery backlog
- You want to compare the public site against competitors without inventing private performance data
- You are about to brief a developer, content writer, agency, or marketing team

## Inputs required

- Primary URL and any important sub-pages to review
- Business context: offer, market, business model, geography, and sales cycle
- Target audience and conversion goal
- Known competitors or reference sites, if available
- Access available: public site only, analytics, Search Console, CMS, CRM, heatmaps, keyword tool
- Known constraints: brand, compliance, budget, CMS, engineering capacity, launch dates
- Any existing evidence: sitemap, robots.txt, analytics export, Search Console query data, page copy, screenshots, crawl results

## Process

1. **Define scope**
   - State which pages, tools, and evidence will be reviewed.
   - Capture what cannot be known from the available access.
   - Identify whether the priority is SEO, conversion, brand clarity, technical hygiene, or all of them.

2. **Inspect the site**
   - Review the homepage, navigation, top commercial pages, important content pages, forms/CTAs, footer, robots.txt, sitemap, metadata, headings, and visible structured data where available.
   - Check mobile rendering and page layout if screenshots or browser access are available.
   - Record page-level evidence, not just impressions.

3. **Separate evidence from inference**
   - Use three labels: Observed, Inferred, and Not observed.
   - Do not invent rankings, traffic, conversion rate, keyword volume, Core Web Vitals, backlinks, revenue, or CMS implementation details.
   - Where a metric is missing, name the access needed to verify it.

4. **Score the current state**
   - Score 1-5 across positioning, audience fit, information architecture, on-page SEO, technical SEO, content quality, internal linking, conversion path, trust/proof, and measurement readiness.
   - Add one evidence sentence for each score.

5. **Diagnose the system**
   - Positioning: Is the value proposition clear within seconds?
   - Search intent: Do pages match what the target audience is likely trying to find?
   - Information architecture: Can users and crawlers understand the site structure?
   - Technical SEO: Are there visible crawl, indexability, rendering, metadata, schema, canonical, redirect, or performance risks?
   - Conversion: Is there a clear path from problem to proof to action?
   - Trust: Are proof points, credentials, case studies, pricing cues, and risk reducers credible?
   - Measurement: Can the team tell whether changes improve outcomes?

6. **Prioritise recommendations**
   - Classify each recommendation by impact, effort, confidence, and dependency.
   - Avoid long undifferentiated lists. A good audit should make sequencing obvious.
   - Assign likely owners: marketing, content, design, engineering, analytics, or leadership.

7. **Produce the report**
   - Write for both executives and delivery teams.
   - Put the conclusion and priority actions near the top.
   - Include the backlog and 30/60/90-day plan.

## Copy-paste prompt

```text
You are a senior website marketing strategist, SEO consultant, conversion optimisation specialist, and technical auditor. Produce a practical website marketing and SEO audit from the URL and evidence below.

AUDIENCE: [Founder / marketing lead / product owner / executive sponsor / technical team]
PRIMARY_URL: [URL]
BUSINESS_CONTEXT: [Offer, market, business model, maturity, geography]
TARGET_AUDIENCE: [Audience, needs, objections, buying journey]
COMMERCIAL_GOAL: [Leads / sales / bookings / sign-ups / authority / support deflection]
KNOWN_COMPETITORS: [URLs or names]
ACCESS_AVAILABLE: [Public site only / analytics / Search Console / CMS / CRM / heatmaps / keyword tools]
EVIDENCE_PROVIDED: [Paste page text, screenshots, HTML, sitemap, analytics, Search Console data, crawl notes, or prior findings]
CONSTRAINTS: [Budget, CMS, compliance, brand, engineering capacity, timing]

Write an audit report with:
1. Executive summary
2. Scope and evidence inspected
3. Current-state scorecard
4. Positioning and messaging diagnosis
5. Conversion journey diagnosis
6. Technical SEO diagnosis
7. Content and search intent diagnosis
8. Trust and credibility diagnosis
9. Measurement gaps
10. Prioritised recommendations
11. 30/60/90-day action plan
12. Implementation backlog
13. Missing information and assumptions

Constraints:
- Use British English.
- Separate Observed facts, Inferred hypotheses, and Not observed information.
- Do not invent traffic, rankings, conversion rates, keyword volumes, backlinks, Core Web Vitals, revenue, or analytics findings.
- If data is missing, say what access would be needed to verify it.
- Prioritise by impact, effort, confidence, and dependency.
- Make each recommendation specific enough for an owner to act on.
- Output only the report.
```

## Suggested output structure

- **Executive summary**: five to eight bullets, including the top three actions.
- **Scope and evidence**: pages inspected, data sources, exclusions, and limitations.
- **Scorecard**: 1-5 scores with evidence, not opinion-only scores.
- **Diagnosis**: grouped findings across positioning, conversion, SEO, content, trust, and measurement.
- **Prioritised recommendations**: few enough to act on; specific enough to brief owners.
- **30/60/90-day plan**: quick wins, structural fixes, and growth work.
- **Backlog**: table with owner, impact, effort, confidence, dependency, and acceptance criteria.

## Quality controls

- [ ] The report names the pages and evidence inspected.
- [ ] No private metrics are invented from public pages.
- [ ] Each major recommendation has a visible cause, not just a preference.
- [ ] SEO fixes are linked to business outcomes and user intent.
- [ ] The backlog distinguishes critical blockers, quick wins, and strategic work.
- [ ] Measurement gaps are explicit.
- [ ] British English is used throughout.

## Common failure modes

- **Invented SEO data**: Public inspection does not reveal rankings, traffic, conversion, or backlinks. Mark these as missing unless data is supplied.
- **Checklist dump**: A long list of generic SEO tasks is not a strategy. Prioritise and sequence.
- **Technical-only audit**: Fixing titles and schema will not help if the offer and conversion path are weak.
- **No owner**: Recommendations without an accountable owner are unlikely to happen.
- **No measurement plan**: A good action plan says how improvement will be detected.

## Example request

"Audit `https://example.com` as if it were a small B2B cyber security consultancy targeting UK mid-market CFOs and CIOs. Public URL only. Goal: increase qualified enquiries for incident response retainers. Competitors: two named consultancies. Produce an executive summary, SEO and conversion diagnosis, and 90-day action plan. Do not invent traffic or ranking data. Use British English."
