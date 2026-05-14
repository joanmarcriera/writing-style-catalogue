---
title: Product Requirements Style
category: Specialist
aliases: [PRD, Product Specification]
---

# Product Requirements Style

## What This Style Is

Structured specification of product features and requirements. Clear about what will be built, why, and how success is measured. Used by product teams to align engineering and business.

**Core principle**: Goal → Requirements → Success Metrics.

## When to Use It

- Product requirement documents (PRDs)
- Feature specifications
- Product proposals
- Engineering briefs
- Acceptance criteria definitions
- Product roadmap items

## When NOT to Use It

- Strategic recommendations (use Consulting)
- Executive updates (use Smart Brevity)
- Teaching (use Socratic)
- Technical implementation (use Technical Documentation)

## Core Structure

```
[OVERVIEW]
What product or feature this describes.

[GOAL/OPPORTUNITY]
Why we're building this.

[REQUIREMENTS]
What the product must do.

[SUCCESS METRICS]
How we measure if this succeeded.

[ACCEPTANCE CRITERIA]
Specific conditions for completion.

[DEPENDENCIES]
What else must be true.

[CONSTRAINTS]
What we cannot change.
```

## Copy-Paste Prompt Template

```
You are a product manager. Write a PRD from:

FEATURE:
[What are you building]

GOAL:
[Why does this matter]

PROBLEM SOLVED:
[What customer problem does this address]

REQUIREMENTS:
[What must the product do]

SUCCESS METRICS:
[How will you know this succeeded]

ACCEPTANCE CRITERIA:
[What does "done" look like]

INSTRUCTIONS:
1. Start with clear overview
2. State goal and rationale
3. List concrete requirements
4. Define measurable success criteria
5. Specify acceptance criteria
6. Identify dependencies
7. Length: 3–8 pages

Output only the PRD. No preamble.
```

## Short Example

**Product Requirement: Notification Digest Feature**

**Overview**
A weekly email digest summarising key notifications instead of individual alert emails.

**Goal**
Reduce notification fatigue while ensuring users don't miss important updates. Target: 30% reduction in email volume; 80% engagement with digest.

**Problem Solved**
Users receive 40+ notification emails per week, leading to fatigue and missed important alerts. A consolidated digest allows users to scan all updates at once.

**Requirements**

Functional:
- User can select notification types to include in digest
- Digest is generated weekly (Friday 09:00 GMT)
- Digest is sent via email in HTML format
- User can view digest in web interface
- User can unsubscribe from digest without losing individual notifications

Non-Functional:
- Digest generation must complete within 5 minutes for all users
- HTML must render correctly on mobile and desktop

**Success Metrics**
- 70% adoption among active users
- 30% reduction in notification email volume
- 80%+ open rate on digest emails
- NPS increase of 5+ points among users using digest

**Acceptance Criteria**
- [x] Digest generation system is built and tested
- [x] Email template is responsive
- [x] User preferences UI is complete
- [x] Digest is generated for all active users
- [x] Acceptance testing completed

**Constraints**
- Must use existing email service
- Cannot require new database schema changes
- Privacy: Do not store email content; only metadata

---

## Quality Checklist

- [ ] Overview is clear and concise
- [ ] Goal/rationale is compelling
- [ ] Requirements are specific and measurable
- [ ] Success metrics are defined
- [ ] Acceptance criteria are testable
- [ ] Dependencies are identified
- [ ] Constraints are explicit

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Vague requirements | Engineering unsure what to build | Use specific, measurable requirements |
| Success metrics missing | Can't tell if feature succeeded | Define metrics upfront |
| No acceptance criteria | Ambiguity about when feature is "done" | List specific, testable criteria |
| Too much detail | Spec is overwhelming | Focus on what, not how (that's engineering) |
| Undocumented assumptions | Team discovers misalignment mid-build | Explicitly state assumptions |

---

See [prompt-templates/](../prompt-templates/) for prompts and templates for various document types.
