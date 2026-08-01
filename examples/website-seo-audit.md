---
title: Website Audit — Specialist Consultancy
category: Example
description: A worked website-audit bundle that separates observed evidence, hypotheses, missing private data, and prioritised actions.
bundle_id: website-seo-audit
artefact: Website marketing and SEO audit
audience: Founder, marketing lead, and web delivery team
scenario: labelled-composite
style_path: styles/consulting-style.md
pattern_path: patterns/problem-impact-recommendation-next-steps.md
prompt_path: prompt-templates/website-marketing-seo-prompts.md
skill_path: skills/create-website-marketing-seo-audit.md
rubric_path: rubrics/website-marketing-seo-rubric.md
---

# Website Audit — Specialist Consultancy

## Professional context

A founder needs an actionable public-site review. The auditor has page observations but no analytics, Search Console, CRM, keyword-volume, or conversion data, so the output must not manufacture performance findings.

## Source packet

```text
SCENARIO: Labelled composite; example.test is not a real audited website.
BUSINESS: UK specialist cloud-cost consultancy serving organisations with 200–2,000 staff.
GOAL: Qualified discovery-call enquiries.
PUBLIC PAGES INSPECTED: homepage, services, two case studies, about, contact, privacy, robots.txt, sitemap.xml.
OBSERVED: Homepage headline says “Transform your cloud journey”; no buyer, problem, or outcome named. One primary navigation CTA says “Get in touch”. Two case studies name the work but contain no quantified result. Contact form asks for nine fields. Service pages have unique titles and one H1 each. Sitemap contains 17 URLs. Robots.txt does not block public content.
NOT OBSERVED: pricing guidance, delivery process, qualification criteria, client quotations, author biographies on articles.
NOT AVAILABLE: analytics, Search Console, CRM outcomes, rankings, backlinks, keyword volume, Core Web Vitals field data, form completion.
CONSTRAINT: Two-person team can deliver no more than six material page changes per month.
```

## Completed prompt

```text
You are a senior website marketing, technical SEO, and conversion auditor. Produce an evidence-led audit for the founder, marketing lead, and web delivery team using only the SOURCE PACKET.

Do not invent traffic, rankings, conversions, search demand, backlinks, technical performance, revenue, customer opinions, competitor evidence, or CMS behaviour. Label every finding Observed, Inferred, or Not available. An inference must identify the observation that supports it and the data needed to test it. If inspected pages, business goal, access limits, or team capacity are missing, return MISSING INFORMATION rather than a prioritised plan.

Use British English. Structure: Executive summary; Scope and evidence; Current-state scorecard; Findings by positioning, trust, conversion, content, technical SEO, and measurement; Prioritised recommendations; 30/60/90-day plan; Delivery backlog; Missing evidence. Give every action an owner role, impact, effort, confidence, dependency, and testable acceptance criterion. Respect the limit of six material page changes per month. Do not score a private performance dimension without data. Keep the audit between 1,200 and 1,600 words. Output only the audit.

Before finalising, apply the Website Marketing and SEO Rubric. Evidence discipline, commercial alignment, prioritisation, acceptance criteria, and missing-information honesty are critical gates.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Executive summary
The public site explains that cloud consulting is offered but does not yet help the target buyer recognise whether the service fits their organisation or what outcome to expect. This is an Observed messaging gap, not evidence of poor conversion: analytics and form-completion data were not available.

Priority 1 — Replace the generic homepage proposition
Evidence: Observed headline “Transform your cloud journey” names neither the 200–2,000-person buyer nor the cloud-cost problem.
Action: Marketing lead drafts and tests a proposition naming audience, problem, and evidence-backed outcome.
Acceptance: one H1 names the target organisation and problem; supporting copy contains no unsupported result; CTA describes a discovery-call outcome.

Priority 2 — Reduce untested form friction
Evidence: Observed nine-field contact form. Inference: field count may discourage enquiries; no completion data is available.
Acceptance: instrument start/completion events before changing fields, then compare a six-field variant for four weeks.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Evidence discipline | 5 | Observations, inferences, and unavailable data remain distinct. | Pass |
| Commercial alignment | 5 | Recommendations serve qualified discovery calls. | Pass |
| Prioritisation | 5 | Work respects the six-change monthly capacity. | Pass |
| Technical integrity | 4 | Public technical facts are bounded to inspected artefacts. | Human check |
| Actionability | 5 | Owners and acceptance criteria define completion. | Pass |

## Human review before use

- Reinspect the live pages and capture dated evidence before issuing a client report.
- Connect analytics, Search Console, CRM, and performance data before making outcome claims.
- Validate accessibility, legal, brand, and implementation constraints with responsible owners.

## Reuse this bundle

- [Consulting Style](../styles/consulting-style.md)
- [Problem / Impact / Recommendation / Next Steps Pattern](../patterns/problem-impact-recommendation-next-steps.md)
- [Website Marketing and SEO Prompts](../prompt-templates/website-marketing-seo-prompts.md)
- [Create Website Marketing and SEO Audit Skill](../skills/create-website-marketing-seo-audit.md)
- [Website Marketing and SEO Rubric](../rubrics/website-marketing-seo-rubric.md)
