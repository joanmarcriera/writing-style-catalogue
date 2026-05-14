---
title: Website Marketing and SEO Prompts
template_type: Website Marketing / SEO Audit / Growth Plan
use_case: Analyse a website from a URL and produce a practical current-state report, prioritised recommendations, and next-action plan.
audience: Founders, marketing leads, product owners, consultants, technical teams, and executive sponsors
output_format: URL audit report, prioritised action plan, content roadmap, conversion improvement backlog, and measurement plan
---

# Website Marketing and SEO Prompts

## Purpose

Use these prompts when you can provide a URL and need a clear professional report on the website's current marketing and SEO position: what is working, what is not, what cannot be known from public inspection alone, and what should happen next.

A good website audit is evidence-led. It should inspect the live site where possible, separate facts from assumptions, avoid invented SEO metrics, and convert findings into a practical backlog.

## Before you start

Provide as much of this as possible:

```text
PRIMARY_URL:
BUSINESS_CONTEXT:
TARGET_AUDIENCE:
COMMERCIAL_GOAL:
GEOGRAPHY:
KNOWN_COMPETITORS:
KEY_PRODUCTS_OR_SERVICES:
ACCESS_AVAILABLE: [public URL only / analytics / Search Console / CMS / CRM / heatmaps]
KNOWN_CONSTRAINTS:
OUTPUT_NEEDED: [executive report / technical backlog / content plan / landing page audit / 30-60-90 day plan]
```

If live browsing is not available, paste page text, screenshots, HTML extracts, metadata, sitemap/robots content, analytics exports, Search Console queries, and competitor URLs.

## Master prompt: website marketing and SEO audit from a URL

```text
You are a senior website marketing strategist, SEO consultant, conversion optimisation specialist, and technical auditor. Produce an evidence-led website marketing and SEO audit from the URL and context below.

AUDIENCE: [Founder / marketing lead / product owner / executive sponsor / technical team]

PURPOSE: Assess the current state of the website and recommend what to do next to improve discoverability, relevance, trust, conversion, and measurable commercial performance.

PRIMARY_URL:
[URL]

BUSINESS_CONTEXT:
[What the organisation does, market, business model, offer, maturity, constraints, and known goals]

TARGET_AUDIENCE:
[Who the site must persuade, inform, or convert]

COMMERCIAL_GOAL:
[Leads / sales / bookings / subscriptions / enquiries / authority / recruitment / support deflection]

GEOGRAPHY:
[Country, region, language, local/international scope]

KNOWN_COMPETITORS:
[URLs or names, if available]

ACCESS_AVAILABLE:
[Public site only / analytics / Search Console / CMS / CRM / heatmaps / keyword tools]

INPUTS PROVIDED:
[Paste any page copy, sitemap, analytics, Search Console export, CMS notes, brand notes, screenshots, or prior audit findings]

OUTPUT_FORMAT:
Write a professional audit report with these sections:
1. Executive summary
2. Scope and evidence inspected
3. Current-state scorecard
4. Positioning and messaging diagnosis
5. Conversion journey diagnosis
6. Technical SEO diagnosis
7. Content and search intent diagnosis
8. Trust, proof, and credibility diagnosis
9. Measurement and analytics gaps
10. Prioritised recommendations
11. 30/60/90-day action plan
12. Implementation backlog
13. Missing information and assumptions

TONE:
Direct, practical, evidence-led, and commercially literate. Use British English. Avoid inflated marketing language.

CONSTRAINTS:
- Inspect the URL and available evidence before making recommendations.
- Separate observed facts, inferred hypotheses, and missing information.
- Do not invent traffic, rankings, conversion rates, keyword volumes, backlinks, Core Web Vitals, CMS details, revenue, or analytics findings.
- If a metric is not available, write "Not observed" and state what access would be needed.
- Cite the pages or URLs inspected in the scope section.
- Prioritise actions by likely impact, effort, confidence, and dependency.
- Include risks, caveats, and implementation constraints.
- Make recommendations specific enough to assign to marketing, content, design, engineering, or analytics owners.
- Output only the report. No preamble.

CURRENT-STATE SCORECARD:
Score each area 1-5 and add one sentence of evidence:
- Positioning and value proposition
- Audience and search intent fit
- Information architecture
- On-page SEO
- Technical SEO hygiene
- Content quality and depth
- Internal linking
- Conversion path
- Trust and proof
- Measurement readiness

IMPLEMENTATION BACKLOG FORMAT:
Use this table:
| Priority | Area | Issue | Evidence | Recommendation | Owner | Impact | Effort | Confidence | Dependency |

REVIEW CRITERIA:
The report is successful if a senior stakeholder can understand the current state in five minutes, and a delivery team can start work from the backlog without asking what the recommendation means.
```

## Technical SEO triage prompt

Use this when you need engineering-facing fixes rather than a marketing narrative.

```text
You are a technical SEO auditor working with a web engineering team. Audit the supplied URL and evidence for crawlability, indexability, rendering, metadata, structured data, performance signals, internationalisation, canonicalisation, redirects, internal linking, and sitemap/robots hygiene.

URL:
[URL]

SITE_CONTEXT:
[CMS/framework if known, site type, markets, language, migration history, known issues]

EVIDENCE:
[Paste crawl notes, robots.txt, sitemap URLs, response headers, page HTML, Search Console coverage issues, Lighthouse/PageSpeed output, or other observations]

OUTPUT:
1. Technical SEO summary
2. Critical crawl/indexing risks
3. Page template issues
4. Metadata and structured data issues
5. Performance and Core Web Vitals observations
6. International/local SEO observations, if relevant
7. Engineering backlog
8. Tests to confirm fixes

CONSTRAINTS:
- Use British English.
- Do not claim measured Core Web Vitals unless field or lab data is supplied.
- Do not invent crawl size, index coverage, schema validity, or rendering behaviour.
- Mark each finding as Observed, Inferred, or Needs access.
- Include exact pages, selectors, tags, headers, or URLs where evidence is available.
- Prioritise issues by business impact and implementation dependency.
```

## Content and search intent gap prompt

```text
You are an SEO content strategist. Build a content and search intent gap analysis for the website below.

WEBSITE_URL:
[URL]

BUSINESS_CONTEXT:
[Products/services, business model, audience, geography, sales cycle]

TARGET_AUDIENCE:
[Decision-makers, users, influencers, pain points, objections]

KNOWN_COMPETITORS:
[URLs or names]

SEED_TOPICS_OR_KEYWORDS:
[Optional]

EXISTING_CONTENT:
[Paste sitemap, blog/category URLs, page titles, or content inventory if available]

OUTPUT:
1. Content strategy summary
2. Audience intent map
3. Existing content strengths and gaps
4. Recommended topic clusters
5. Priority page opportunities
6. Content briefs for the top five pages
7. Internal linking recommendations
8. 90-day editorial roadmap

CONSTRAINTS:
- Use British English.
- Do not invent keyword volume, difficulty, traffic, or rankings. If keyword tool data is not supplied, use "relative opportunity" and explain the basis.
- Separate evergreen educational content, commercial landing pages, comparison content, trust/proof content, and support content.
- Each recommended page must have: target intent, audience, primary question, page goal, suggested title, outline, proof points needed, CTA, and internal links.
- Flag claims that require subject-matter expert review.
```

## Conversion and messaging audit prompt

```text
You are a conversion optimisation and website messaging consultant. Audit the supplied page or journey and recommend practical improvements.

URLS_TO_REVIEW:
[Homepage / landing page / pricing page / service page / checkout / enquiry flow]

PAGE_GOAL:
[Enquiry / booking / demo / purchase / sign-up / call / download]

TRAFFIC_CONTEXT:
[Search / paid ads / social / referral / direct / unknown]

TARGET_AUDIENCE:
[Who lands here and what they are trying to decide]

OFFER:
[What the page is asking the visitor to do]

EVIDENCE:
[Screenshots, copy, analytics, heatmap notes, form data, user feedback, sales objections]

OUTPUT:
1. Above-the-fold diagnosis
2. Message hierarchy assessment
3. Friction and trust issues
4. CTA and form assessment
5. Objection handling
6. Copy improvements
7. Experiment backlog
8. Measurement plan

CONSTRAINTS:
- Use British English.
- Do not invent conversion rate, bounce rate, scroll depth, or user behaviour.
- If analytics are absent, mark behavioural findings as hypotheses.
- Recommend copy changes that are specific, not generic.
- Include a testable hypothesis for each experiment: "If we change X for audience Y, we expect Z because..."
```

## Competitor comparison prompt

```text
You are a website marketing strategist comparing a primary website against named competitors. Produce a practical comparison that identifies positioning, SEO, content, conversion, and trust gaps.

PRIMARY_URL:
[URL]

COMPETITOR_URLS:
[URL 1]
[URL 2]
[URL 3]

BUSINESS_CONTEXT:
[Market, offer, audience, geography, commercial goal]

OUTPUT:
1. Comparison summary
2. Positioning differences
3. Page and information architecture differences
4. Content depth and search intent coverage
5. Conversion and trust signals
6. Technical observations visible from public pages
7. Opportunities the primary site can act on
8. Risks of copying competitors
9. Prioritised action plan

CONSTRAINTS:
- Use British English.
- Compare only what is visible or supplied.
- Do not assume competitor traffic, conversion, rankings, spend, or internal strategy.
- Avoid copying competitor wording. Extract patterns and opportunities.
- Be explicit where the primary site should not imitate a competitor.
```

## 30/60/90-day action plan prompt

```text
You are a website growth lead. Convert the audit findings below into a practical 30/60/90-day action plan.

AUDIT_FINDINGS:
[Paste findings or backlog]

TEAM_CAPACITY:
[Marketing/content/design/engineering/analytics capacity]

CONSTRAINTS:
[Budget, CMS, brand, legal review, launch dates, technical dependencies]

COMMERCIAL_GOAL:
[Lead volume / qualified enquiries / sales / sign-ups / authority / local visibility]

OUTPUT:
1. Executive summary
2. Actions for days 1-30
3. Actions for days 31-60
4. Actions for days 61-90
5. Measurement plan
6. Decision points and dependencies
7. Risks and mitigations

CONSTRAINTS:
- Use British English.
- Start with fixes that unlock measurement and remove critical blockers.
- Separate quick wins from structural work.
- Assign a likely owner to each action.
- Include success measures and review cadence.
- Do not assume budget, tools, or headcount not supplied in the input.
```

## Quality controls

- The report says what was inspected and what was not.
- Observations, assumptions, hypotheses, and recommendations are clearly labelled.
- No invented metrics, rankings, traffic numbers, backlink claims, or analytics conclusions.
- Recommendations connect to commercial goals, not just SEO hygiene.
- The action plan has owners, dependencies, and testable success measures.
