---
title: Website Marketing and SEO Audit Workflow
category: Workflow
---

# Workflow: Website Marketing and SEO Audit

Use this workflow when you have a URL and need a strong report on the website's current marketing, SEO, content, conversion, and measurement position.

The workflow produces two outputs: an executive-friendly current-state report and a delivery-ready backlog. It is designed for public-site audits, but it becomes much stronger when analytics, Search Console, CMS, CRM, or keyword data are supplied.

## Style to use

Use [Executive Briefing Style](../styles/executive-briefing.md) for the summary and recommendation. Use [Consulting Style](../styles/consulting-style.md) for the diagnosis and prioritised plan. Use [Technical Documentation](../styles/technical-documentation.md) for engineering-facing SEO fixes.

## Skills to use

- [Create Website Marketing and SEO Audit](../skills/create-website-marketing-seo-audit.md) for the main URL-led report
- [Create SEO Content Plan](../skills/create-seo-content-plan.md) for search intent, topic clusters, and content briefs
- [Create Conversion Landing Page Audit](../skills/create-conversion-landing-page-audit.md) for high-value landing pages and journeys
- [Create Roadmap](../skills/create-roadmap.md) for sequencing work beyond 90 days

## Prompt template to start from

Start with [Website Marketing and SEO Prompts](../prompt-templates/website-marketing-seo-prompts.md). Use the master prompt first, then use the technical, content, conversion, or competitor prompts where the audit needs more depth.

## Minimum viable inputs

```text
PRIMARY_URL:
BUSINESS_CONTEXT:
TARGET_AUDIENCE:
COMMERCIAL_GOAL:
GEOGRAPHY:
KNOWN_COMPETITORS:
ACCESS_AVAILABLE: Public URL only
KNOWN_CONSTRAINTS:
```

## Better inputs

- Analytics summary: traffic by channel, conversions, top landing pages, device split, geography
- Search Console: queries, pages, clicks, impressions, CTR, position, index coverage
- CMS export or sitemap
- Paid search terms and advert copy, if landing pages are campaign-driven
- CRM or sales notes: lead quality, objections, common questions
- Heatmap or session recording notes
- Competitor URLs
- Brand, compliance, and technical constraints

## Step-by-step process

1. **Frame the audit**
   - Define the commercial goal: enquiries, bookings, sales, subscriptions, authority, support deflection, or recruitment.
   - Confirm the audience and geography.
   - State the access level and limitations. A public URL alone cannot reveal analytics, conversions, rankings, or revenue.

2. **Inspect the public site**
   - Review the homepage, navigation, main service/product pages, high-value content pages, footer, forms, calls to action, trust signals, metadata, headings, robots.txt, and sitemap where available.
   - Capture evidence by page. Avoid unsupported impressions.

3. **Run the master audit prompt**
   - Use the master prompt from [Website Marketing and SEO Prompts](../prompt-templates/website-marketing-seo-prompts.md).
   - Require Observed, Inferred, and Not observed labels.
   - Generate the current-state scorecard and first backlog.

4. **Deepen the areas that matter**
   - If crawl/indexing issues appear material, run the technical SEO triage prompt.
   - If the site lacks topic coverage, run the content and search intent gap prompt.
   - If the offer is unclear or leads are weak, run the conversion and messaging audit prompt.
   - If competitors are supplied, run the competitor comparison prompt.

5. **Create the delivery backlog**
   - Consolidate duplicate recommendations.
   - Assign owner, impact, effort, confidence, dependency, and acceptance criteria.
   - Separate critical blockers, quick wins, structural work, and growth experiments.

6. **Create the 30/60/90-day plan**
   - Days 1-30: measurement, critical technical blockers, message clarity, obvious conversion friction.
   - Days 31-60: priority page rewrites, internal linking, proof/trust assets, content briefs.
   - Days 61-90: topic cluster expansion, experiments, template improvements, reporting cadence.

7. **Review against the rubric**
   - Use [Website Marketing and SEO Rubric](../rubrics/website-marketing-seo-rubric.md).
   - Fail the report if it invents private metrics or gives generic recommendations without evidence.

## Copy-paste master prompt

```text
You are a senior website marketing strategist, SEO consultant, conversion optimisation specialist, and technical auditor. Produce a current-state audit and 30/60/90-day plan for the website below.

PRIMARY_URL: [URL]
BUSINESS_CONTEXT: [What the business does, market, offer, constraints]
TARGET_AUDIENCE: [Who the website must persuade or help]
COMMERCIAL_GOAL: [Primary measurable goal]
GEOGRAPHY: [Market and language]
KNOWN_COMPETITORS: [URLs or names]
ACCESS_AVAILABLE: [Public URL only / analytics / Search Console / CMS / CRM / heatmaps / keyword tools]
SUPPLIED_EVIDENCE: [Paste relevant data or notes]

Write a professional report with executive summary, scope, current-state scorecard, findings, prioritised recommendations, 30/60/90-day plan, backlog, and missing information.

Use British English. Separate Observed facts, Inferred hypotheses, and Not observed information. Do not invent traffic, rankings, conversion rate, keyword volume, backlinks, Core Web Vitals, revenue, CMS details, or analytics findings. Prioritise by impact, effort, confidence, and dependency.
```

## Review checklist

- [ ] Scope and pages inspected are explicit.
- [ ] Private performance data is not invented.
- [ ] The executive summary states the top three priorities.
- [ ] Technical SEO, content, conversion, trust, and measurement are all considered.
- [ ] Recommendations are prioritised and sequenced.
- [ ] Each backlog item has an owner and acceptance criteria.
- [ ] The 30/60/90-day plan is realistic for the team capacity.
- [ ] British English is used throughout.

## Typical outputs

- Executive website audit report
- Technical SEO backlog
- Landing page conversion audit
- SEO content roadmap
- 30/60/90-day growth plan
- Monthly website performance review template
