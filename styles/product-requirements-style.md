---
title: Product Requirements Style
category: Operational
best_for: Product requirement documents (PRDs) and feature specifications that align engineering, design, and business stakeholders on what is being built, why, and how success will be measured. Ideal for new features, product improvements, and platform changes where multiple teams need a shared, unambiguous reference document.
not_good_for: Strategic recommendations for the product roadmap (use Consulting Style or Minto Pyramid); technical implementation guides for engineers (use Technical Documentation); executive updates on product progress (use Smart Brevity or Executive Briefing).
default_tone: Clear and precise. Customer-focused and outcome-oriented. Neutral on implementation approach.
typical_length: 500–1,500 words for a feature PRD; 2,000–4,000 words for a full product specification
aliases: [PRD, Product Specification, Feature Spec, Product Brief]
---

# Product Requirements Style

## What this style is

A product requirements document (PRD) is the written agreement between product, engineering, design, and business stakeholders on what a feature or product must do, why it matters, and what success looks like. It is the primary tool for aligning multiple teams working on the same problem from different starting points — the PM, the engineers, the designer, the QA analyst, and the go-to-market team must all be able to read the same document and walk away with a shared understanding.

A well-written PRD answers "what" and "why" — it does not answer "how." The implementation approach is for the engineering team to determine; the PRD provides the requirements that any implementation must satisfy. Requirements that describe how something should be built (rather than what it must do) constrain the engineering team unnecessarily and often reflect the PM's technical assumptions rather than genuine user needs.

**Core principle**: Goal → Requirements → Success Metrics. The document specifies what must be true when the feature is done, not how to make it true.

## When to use it

- New feature development requiring cross-functional alignment before engineering begins
- Product improvements where the scope and success criteria need to be formally agreed
- Platform or infrastructure changes that have user-visible implications requiring product sign-off
- Significant scope changes mid-development that require a revised written agreement
- Acceptance criteria definition for agile feature delivery
- Product roadmap item documentation for investor, stakeholder, or board visibility

## When not to use it

- Strategic product roadmap recommendations — use [Consulting Style](consulting-style.md) or [Minto Pyramid Principle](minto-pyramid-principle.md) instead
- Technical implementation guides — use [Technical Documentation](technical-documentation.md) instead
- Executive product updates — use [Smart Brevity](axios-smart-brevity.md) or [Executive Briefing](executive-briefing.md) instead
- Teaching product concepts — use [Socratic Explainer](socratic-explainer.md) instead

## Core structure

```
[TITLE AND METADATA]
Feature or product name.
Author, date, version, and status (Draft / In Review / Approved).
Stakeholders: PM, engineering lead, design lead, QA lead, business sponsor.

[OVERVIEW]
1–3 sentences stating what this document describes.
Which product or feature; the scope of this PRD.

[GOAL / OPPORTUNITY]
The problem being solved or the opportunity being captured.
Why this feature exists: what customer pain or business need drives it.
Why now: why this is the right time to build this.

[TARGET USERS AND JOBS TO BE DONE]
Who the primary user is.
What job they are trying to do that this feature enables.
Any secondary users or edge cases worth noting.

[REQUIREMENTS]
Functional requirements: what the product must do.
Non-functional requirements: performance, reliability, security, accessibility.
Each requirement: specific and verifiable — not "users can do X" but "the system must allow users to do X within 2 seconds."
Must / Should / Must Not (using MoSCoW or similar prioritisation).

[SUCCESS METRICS]
How you will know this feature succeeded.
Leading indicators (engagement, adoption) and lagging indicators (retention, revenue impact).
Each metric: measurable, with a target value and a timeframe.

[ACCEPTANCE CRITERIA]
The specific conditions that must be true for the feature to be considered done.
Written as testable statements: "Given [condition], when [action], then [outcome]."
These are the engineering team's exit criteria.

[OUT OF SCOPE]
What this PRD explicitly does not cover.
Related features or work items that belong in a separate PRD.
Prevents scope creep during build.

[DEPENDENCIES]
Other systems, teams, or initiatives this feature depends on.
What must be true before development can begin or complete.

[CONSTRAINTS]
Technical, regulatory, or business constraints the implementation must respect.
Things that cannot be changed regardless of the preferred engineering approach.

[OPEN QUESTIONS]
Decisions not yet made that must be resolved before or during development.
Who owns each decision and by when.
```

## Copy-paste prompt

```
You are an experienced product manager. Your task is to write a product requirements document from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Engineering lead, frontend and backend engineers, UX designer, QA lead, and the Head of Product", "Full-stack product team for a B2B SaaS identity management platform", "Cross-functional delivery team including engineering, security, and customer success"]
PURPOSE: [PURPOSE — e.g. "Define requirements for a new automated access review feature in the IAM platform", "Write the PRD for a weekly email digest notification feature", "Define the product requirements for the zero-trust conditional access module"]
CONTEXT: [CONTEXT — e.g. "Access reviews are currently manual and take an average of 11 days per cycle; customers have requested automation in 73% of support tickets in Q1; this is the top roadmap priority for Q3 2026"]
INPUT: [INPUT — paste all relevant context including: the customer problem, user research findings, technical constraints, proposed solution description, stakeholder input, success metrics discussion, and any engineering pre-assessment here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Engineering team can begin sprint planning from this PRD without needing further clarification from PM", "QA team has clear acceptance criteria to write test cases from", "Product and engineering are fully aligned on scope and what done looks like"]
TONE: [TONE — e.g. "Precise and unambiguous — every requirement must be testable", "Outcome-focused — focus on what must be true, not how it must be built", "Neutral on implementation — the requirements are constraints, not instructions"]
LENGTH: [LENGTH — e.g. "800–1,200 words for a feature PRD", "2,000–3,000 words for a full product specification"]
FORMAT: [FORMAT — headed sections: Overview / Goal / Target Users / Requirements / Success Metrics / Acceptance Criteria / Out of Scope / Dependencies / Constraints / Open Questions]
CONSTRAINTS: [CONSTRAINTS — e.g. "Must use the existing email sending infrastructure — no new vendor", "GDPR: must not store email content, only metadata", "Must be accessible at WCAG 2.1 AA standard"]

INSTRUCTIONS:
1. Write requirements as testable statements specifying what the system must do — not how it must do it. Use "the system must" not "the feature will" or "we will build."
2. Prioritise requirements using MoSCoW: Must Have (required for launch), Should Have (high priority but not launch-blocking), Could Have (nice to have), Must Not Have (explicitly excluded).
3. Write acceptance criteria in Given/When/Then format. Each criterion must be independently testable.
4. Success metrics must be specific: name the metric, the target value, and the timeframe. "70% adoption" is not complete — "70% of active users will use the feature at least once in the first 30 days after launch" is.
5. Explicitly state what is Out of Scope. This prevents scope creep and protects the engineering team.
6. List all dependencies with their current status (e.g. "Dependent on email infrastructure upgrade — in progress, target complete June 2026").
7. List all technical, regulatory, or business constraints that limit the implementation approach.
8. Capture all unresolved questions as Open Questions with a named owner and resolution date.
9. Use British English throughout (colour, organisation, licence, favour, etc.).
10. Preserve all facts, user research findings, and technical constraints exactly as provided in [INPUT]. Do not invent requirements or metrics not grounded in [INPUT].

Output the PRD only. No preamble, no commentary.
```

## Output format

A PRD is typically published in a product management tool (Confluence, Notion, Linear, or Jira) or as a Google Doc / Word document. It contains:

- **Title block**: Feature name, author, date, version, status, and stakeholders
- **Headed sections**: Each with a clear H2 heading
- **Requirements**: Numbered list (FR-1, FR-2 for functional; NFR-1, NFR-2 for non-functional); MoSCoW priority for each
- **Acceptance criteria**: Numbered list in Given/When/Then format; each independently testable
- **Success metrics**: Table with Metric / Target / Timeframe columns
- **Open questions**: Table with Question / Owner / Due Date columns

The PRD does not use dense prose paragraphs in the requirements or acceptance criteria sections. Lists and tables are the primary format. The document is designed to be read in non-linear order — engineers may jump to Requirements and Acceptance Criteria; QA to Acceptance Criteria; business stakeholders to Goal and Success Metrics.

## Example

**PRD: Automated Access Review — IAM Platform**
*Author: Jordan Mensah, Senior Product Manager | Date: 14 May 2026 | Version: 1.2 | Status: Approved*
*Stakeholders: Aisha Kaur (Engineering Lead), Marcus Liu (UX Design), Sarah Brennan (QA Lead), Priya Nair (CTO)*

---

**Overview**

This document defines the product requirements for the Automated Access Review feature in the Acme IAM Platform. It covers the automated scheduling, execution, and reporting of periodic access certification reviews for all managed user accounts and role assignments.

---

**Goal / Opportunity**

Access reviews — the periodic process of confirming that users have appropriate access to systems and data — are currently a manual process managed via spreadsheet. The average review cycle takes 11 days (measured across Q1 2026 data). 34% of reviews are not completed within the required 30-day window, creating a compliance gap that was flagged in the December 2025 external audit report.

Automating access reviews will reduce cycle time, improve completion rates, and generate an auditable evidence trail required for ISO 27001 and SOC 2 compliance. This is the top-voted feature in our Q1 2026 customer survey (73% of enterprise customers rated it "critical").

This feature must be live before the November 2026 ISO 27001 recertification audit.

---

**Target Users and Jobs to Be Done**

*Primary user*: IT Security Administrator or Identity Manager
*Job to be done*: Schedule and run periodic access reviews across all managed accounts without manual coordination; collect reviewer responses; generate a compliance-ready evidence report.

*Secondary user*: Individual access reviewer (manager or resource owner)
*Job to be done*: Review and certify or revoke assigned access items efficiently, with enough context to make a good decision.

---

**Requirements**

*Functional Requirements (Must Have)*

| # | Requirement | Priority |
|---|-------------|----------|
| FR-1 | The system must allow an administrator to create an access review campaign targeting a defined scope (all accounts, by group, by system, or by access level) | Must Have |
| FR-2 | The system must automatically assign access items to the designated reviewer (as configured in the user directory) for each account in scope | Must Have |
| FR-3 | The system must send an email notification to each reviewer when a review item is assigned, including a direct link to the review interface | Must Have |
| FR-4 | The system must send a reminder notification to reviewers 7 days and 2 days before the review deadline for any uncompleted items | Must Have |
| FR-5 | Reviewers must be able to certify (approve) or revoke access for each item from within the review interface, with a mandatory comment field for revocations | Must Have |
| FR-6 | The system must automatically deprovision access for any item marked as revoked within 24 hours of the reviewer's decision | Must Have |
| FR-7 | The system must generate a downloadable compliance report in PDF and CSV formats containing all review decisions, reviewer names, timestamps, and comments | Must Have |
| FR-8 | An administrator must be able to escalate overdue items to a secondary reviewer or manager | Should Have |
| FR-9 | The review interface must display the last 90 days of login activity for each account under review, to support the reviewer's decision | Should Have |

*Non-Functional Requirements*

| # | Requirement | Priority |
|---|-------------|----------|
| NFR-1 | Review assignment processing must complete within 5 minutes for campaigns covering up to 5,000 accounts | Must Have |
| NFR-2 | The review interface must meet WCAG 2.1 AA accessibility standards | Must Have |
| NFR-3 | Email notifications must be delivered within 15 minutes of the trigger event | Must Have |
| NFR-4 | The system must not store reviewer decision data in the email service — all decisions are stored in the IAM platform database only | Must Have |

---

**Success Metrics**

| Metric | Target | Timeframe |
|--------|--------|-----------|
| Review cycle time (average) | Under 5 days (from 11 days) | Within 60 days of launch |
| On-time completion rate | 95% of review items completed within the 30-day window | Within 90 days of launch |
| Feature adoption | 80% of enterprise customers have run at least one automated review | Within 90 days of launch |
| Auditor satisfaction | Compliance report accepted without manual supplement by external auditor | November 2026 ISO audit |

---

**Acceptance Criteria**

AC-1: **Given** an administrator has created an access review campaign, **when** they confirm the campaign, **then** the system assigns all in-scope access items to the appropriate reviewer within 5 minutes.

AC-2: **Given** a review item is assigned to a reviewer, **when** the assignment is made, **then** the reviewer receives an email within 15 minutes containing a direct link to the review interface and a summary of their assigned items.

AC-3: **Given** a reviewer has certified or revoked an access item, **when** they submit their decision, **then** the system records the decision, reviewer name, and timestamp and makes it available in the compliance report immediately.

AC-4: **Given** a reviewer has marked an access item as revoked, **when** the decision is submitted, **then** the access is automatically deprovisioned within 24 hours and a confirmation is sent to the administrator.

AC-5: **Given** a campaign is complete, **when** the administrator requests the compliance report, **then** the system generates a downloadable PDF and CSV within 60 seconds containing all decisions, reviewer names, timestamps, and comments.

---

**Out of Scope**

This PRD does not cover:
- Automated access reviews for privileged access accounts — covered in PRD-0044 (Privileged Access Review)
- Integration with third-party GRC platforms — planned for Q1 2027
- Self-certification flows (where users certify their own access) — not supported in this release
- Mobile interface for reviewers — desktop web only in this release

---

**Dependencies**

| Dependency | Status | Owner |
|-----------|--------|-------|
| Email infrastructure upgrade (required for notification volume) | In progress — target 30 June 2026 | Platform team |
| User directory attribute "designated_reviewer" must be populated for all managed accounts | Not started — required by 1 August 2026 | Identity team |
| Access data model update to support review status fields | Design complete — development begins June 2026 | Backend engineering |

---

**Constraints**

- Must use existing email sending infrastructure (SendGrid) — no new email vendor
- Must not store any email content — only metadata (timestamp, recipient, type)
- Must be deployable without downtime to existing IAM platform users
- All data must remain in the EU-West-2 (London) AWS region — UK GDPR data residency

---

**Open Questions**

| Question | Owner | Due |
|---------|-------|-----|
| What should happen to access items where the designated reviewer is on extended leave? (Options: auto-escalate to manager; hold until reviewer returns; reassign to administrator) | Jordan Mensah (PM) | 1 June 2026 |
| Is a 24-hour deprovisioning window sufficient for enterprise customers, or do we need a real-time option for high-risk revocations? | Aisha Kaur (Engineering) + Customer Success | 15 June 2026 |

## Quality checklist

- [ ] Overview is 1–3 sentences and clearly states what the PRD covers
- [ ] Goal section answers why this feature exists and why now
- [ ] Target users are defined with their specific jobs to be done
- [ ] Every requirement is specific, testable, and uses "must" not "should" for Must Have items
- [ ] Requirements are prioritised (Must Have / Should Have / Must Not Have)
- [ ] Success metrics are specific: metric name, target value, and timeframe
- [ ] Acceptance criteria are in Given/When/Then format and independently testable
- [ ] Out of Scope is explicit — prevents scope creep
- [ ] Dependencies are listed with current status and owner
- [ ] Open questions are captured with owner and due date
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Vague requirements ("users can easily find their items") | Engineering cannot build to this; QA cannot test it | Use specific, testable requirements: "within 3 clicks from the dashboard" |
| Requirements that specify implementation ("use a REST API") | Constrains engineering unnecessarily | Specify what must be true; let engineering determine how |
| Missing success metrics | Cannot tell if the feature succeeded | Define specific metrics with target values and timeframes |
| Acceptance criteria that are not independently testable | QA cannot write test cases | Use Given/When/Then; each criterion must be testable in isolation |
| No out-of-scope section | Scope creep; team argues about what is included | Explicitly list what this PRD does not cover |
| Unstated assumptions | Team discovers mid-build that a key assumption was wrong | List all assumptions explicitly; raise as open questions if unvalidated |

---

See [prompt-templates/](../prompt-templates/) for prompts and templates for various document types.
