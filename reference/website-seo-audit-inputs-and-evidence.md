---
title: Website SEO Audit Inputs and Evidence
category: Reference
description: Explains what can and cannot be inferred from a public URL when producing a website marketing or SEO audit.
---

# Website SEO Audit Inputs and Evidence

A URL is enough to start a useful website audit, but it is not enough to prove everything. The strongest reports are clear about what was observed, what was inferred, and what still needs access.

## What a public URL can usually show

- Public page structure, navigation, internal links, headings, visible copy, and calls to action
- Basic metadata visible in HTML
- Visible structured data, where present
- robots.txt and XML sitemap availability, where public
- Public page templates and obvious duplication
- Visible trust signals, proof, case studies, testimonials, credentials, contact details, and policies
- Obvious message clarity, offer clarity, and conversion friction
- Mobile layout issues if reviewed in a browser
- Some performance signals if lab tools are run

## What a public URL cannot prove on its own

- Organic rankings
- Traffic volume
- Conversion rate
- Revenue or lead quality
- Keyword volume or difficulty
- Backlink profile
- Search Console coverage and query data
- Core Web Vitals field data
- Actual user behaviour, scroll depth, or form abandonment
- Paid media spend or campaign performance
- Competitor traffic, conversion, or internal strategy
- Full CMS configuration or deployment pipeline

## Evidence hierarchy

| Evidence | Strength | Use |
|---|---:|---|
| Analytics, Search Console, CRM, CMS, crawler export | High | Baselines, performance, queries, conversions, coverage, page inventory |
| Live public page inspection | Medium | Messaging, structure, metadata, visible SEO and conversion issues |
| Screenshots, page text, HTML extracts | Medium | Review when browsing is unavailable |
| Competitor public pages | Medium | Positioning and content pattern comparison |
| Stakeholder notes | Useful but subjective | Context, goals, constraints, objections |
| LLM inference | Low | Hypotheses only; must be labelled |

## Labelling standard

Use these labels in every report:

- **Observed**: directly visible in the page, data export, screenshot, or supplied evidence.
- **Inferred**: reasonable hypothesis based on evidence, but not directly proven.
- **Not observed**: unavailable from current evidence. Name the access required.

Example:

```text
Observed: The homepage has a generic H1 and no industry-specific proof above the fold.
Inferred: This may weaken relevance for CFO visitors arriving from high-intent search.
Not observed: Conversion rate by landing page. Requires analytics or CRM data.
```

## Recommended input pack

For a strong audit, provide:

- Primary URL and target geography
- Commercial goal and main conversion event
- Target audience and buying journey
- Competitor URLs
- Sitemap or page inventory
- Analytics export: sessions, conversions, landing pages, source/medium, device split
- Search Console export: queries, pages, impressions, clicks, CTR, position, coverage
- Current keyword or paid search terms, if any
- CRM or sales notes on lead quality and objections
- CMS, brand, legal, and engineering constraints

## Minimum useful output from public URL only

Even with public URL only, a good report can still produce:

- Scope and limitations
- Positioning diagnosis
- Conversion journey diagnosis
- Visible on-page and technical SEO hygiene review
- Content gap hypotheses
- Trust and proof assessment
- Measurement gaps
- Prioritised action plan

It should not present missing analytics as fact.
