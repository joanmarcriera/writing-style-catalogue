---
title: Create Conversion Landing Page Audit
skill_type: Conversion optimisation
output: Landing page or journey audit with messaging diagnosis, friction map, copy recommendations, experiment backlog, and measurement plan
tools_needed: LLM with browsing or supplied screenshots/copy; optional analytics, heatmaps, session recordings, form data, CRM data, paid search terms
difficulty: Medium
---

# Skill: Create Conversion Landing Page Audit

## What this skill does

Analyses a page or conversion journey to identify why visitors may not act and what to change next. The output should cover message clarity, offer strength, trust, proof, friction, calls to action, forms, and testable experiments.

The audit should distinguish visible page issues from behavioural hypotheses. Without analytics or user research, it cannot claim actual conversion behaviour.

## When to use it

- A landing page gets traffic but few enquiries, bookings, sign-ups, or sales
- A homepage or service page does not explain the offer clearly
- Paid campaign traffic needs a better page or message match
- You need a practical test backlog for design, copy, or form changes
- A stakeholder wants conversion recommendations without vague CRO advice

## Inputs required

- URL or screenshots of the page/journey
- Page goal and primary CTA
- Traffic source and search/ad/message context, if known
- Target audience and stage of awareness
- Offer, pricing model, proof points, objections, and risk reducers
- Analytics, form data, heatmaps, session recordings, user feedback, or sales objections, if available
- Brand, legal, technical, or CMS constraints

## Process

1. **Clarify the conversion job**
   - Define what the page should make the visitor understand, believe, and do.
   - Identify whether the page is for cold traffic, warm traffic, existing customers, or a mixed audience.

2. **Review the first screen**
   - Check whether the headline, subheading, proof, visual context, and CTA communicate the offer quickly.
   - Identify whether the visitor can answer: "Is this for me?", "What do I get?", "Why trust this?", "What next?"

3. **Assess message hierarchy**
   - Review page sections in order.
   - Look for missing problem framing, benefits, differentiators, process, proof, risk reducers, and objection handling.

4. **Find friction**
   - Inspect forms, CTA placement, navigation distractions, pricing ambiguity, trust gaps, slow-loading media, mobile constraints, and unclear next steps.
   - Mark issues as Observed or Hypothesis.

5. **Recommend changes**
   - Provide copy improvements, layout changes, proof additions, form changes, and measurement fixes.
   - Make each recommendation testable.

6. **Create the experiment backlog**
   - Use a clear hypothesis for each test: "If we change X for audience Y, we expect Z because..."
   - Prioritise by likely impact, effort, confidence, and risk.

## Copy-paste prompt

```text
You are a conversion optimisation and website messaging consultant. Audit the landing page or conversion journey below and recommend practical improvements.

URLS_TO_REVIEW: [URLs]
PAGE_GOAL: [Enquiry / booking / demo / purchase / sign-up / download / call]
TRAFFIC_CONTEXT: [Search / paid ads / social / referral / direct / unknown]
TARGET_AUDIENCE: [Who lands here and what they need to decide]
OFFER: [What the page is asking the visitor to do]
KNOWN_OBJECTIONS: [Price, trust, timing, complexity, risk, alternatives]
EVIDENCE: [Screenshots, copy, analytics, heatmap notes, form data, user feedback, sales objections]
CONSTRAINTS: [Brand, legal, CMS, design system, engineering capacity]

Output:
1. Page purpose and audience fit
2. Above-the-fold diagnosis
3. Message hierarchy assessment
4. Trust, proof, and objection handling
5. CTA, form, and journey friction
6. Copy and layout recommendations
7. Experiment backlog
8. Measurement plan
9. Assumptions and missing evidence

Constraints:
- Use British English.
- Do not invent conversion rate, bounce rate, scroll depth, heatmap behaviour, or user behaviour.
- Mark each behavioural point as Observed, Inferred, or Needs data.
- Make copy changes specific enough to test.
- Include a testable hypothesis and success measure for each experiment.
- Output only the audit.
```

## Suggested output structure

| Section | What it should answer |
|---|---|
| Page purpose | What action should the page drive? |
| Audience fit | Does the page match the visitor's intent and awareness? |
| First screen | Is the offer clear without scrolling? |
| Message hierarchy | Is the argument in the right order? |
| Trust and proof | Why should the visitor believe the claim? |
| Friction map | What makes action harder than necessary? |
| Experiment backlog | What should be tested first? |
| Measurement plan | How will improvement be detected? |

## Quality controls

- [ ] Recommendations map to the page goal.
- [ ] Behavioural claims are not stated as facts without evidence.
- [ ] Copy suggestions are concrete and audience-specific.
- [ ] Tests include hypotheses and success measures.
- [ ] The plan includes low-risk changes and larger structural improvements.
- [ ] Measurement gaps are named before experiments are proposed.

## Common failure modes

- **Changing design before message**: A better layout cannot fix an unclear offer.
- **Assuming all visitors are ready to buy**: Cold visitors often need problem framing and proof before a CTA.
- **Too many CTAs**: Multiple competing actions weaken the page's job.
- **No trust path**: Claims without proof, process, credentials, or examples create friction.
- **Untestable advice**: "Make it more compelling" is not a recommendation. Say what to change and why.
