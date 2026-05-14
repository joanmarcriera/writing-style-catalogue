---
title: PDF Document Prompts
template_type: PDF-Ready Formatted Document
use_case: Write a complete, publication-ready document formatted for PDF export — including reports, whitepapers, briefings, and formal reference documents with clear structure, consistent headings, and professional layout.
audience: Any intended recipient of a formal document — clients, stakeholders, regulators, partners, or internal audiences
output_format: Fully structured document with title page elements, table of contents outline, headed sections, tables, and appendices ready for PDF conversion
---

# PDF Document Prompts

## Purpose

Use this template when you need to produce a document that will be exported as a PDF and distributed formally — not sent as an email attachment, but as a standalone professional document. This includes client-facing reports, technical whitepapers, policy documents, regulatory submissions, annual reviews, and research papers. The output should be structured for readability in PDF format: clear H1/H2/H3 heading hierarchy, logical section flow, tables for comparative data, and explicit page break signals. A well-formatted PDF document should require minimal editing before distribution.

## Copy-paste prompt

```
You are a professional document specialist with experience producing publication-quality reports, whitepapers, and formal reference documents. Write a complete, well-structured document formatted for PDF export.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all content to include: data, arguments, findings, analysis, and any existing drafts or notes):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — specify approximate page count or word count]

FORMAT: [FORMAT — recommended: Title Page elements / Table of Contents / Executive Summary / Numbered sections with H1/H2/H3 headings / Tables where comparative data exists / Appendices / References]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Structure the document with a clear heading hierarchy:
   - H1 for major sections (e.g. "1. Introduction", "2. Findings")
   - H2 for sub-sections (e.g. "2.1 Key Finding One")
   - H3 for detailed sub-topics where needed
   Headings should be numbered for a professional document.
3. Open with title page elements: document title, subtitle (if applicable), date, version number, author/organisation, and classification (if relevant — e.g. Confidential / Internal / Public).
4. Include a table of contents outline as a bulleted list of sections and sub-sections with placeholder page numbers (e.g. "1. Introduction ....... 3").
5. Write an executive summary (one to two pages) that captures the key findings, conclusion, and recommendations in a format that can stand alone.
6. Body sections should be logically ordered, with transitions between sections. Use paragraph prose for analysis and argument; use bullet points for lists of items or findings; use numbered lists for sequential steps.
7. Use tables for comparative or structured data. Each table should have a clear title and column headers.
8. Distinguish between facts (confirmed data), assumptions (estimates or projections — label clearly), and recommendations (proposed actions).
9. Where figures, projections, or estimates are used, state the basis and any sensitivity or caveat.
10. Include appendices for supporting material that would interrupt the flow of the main document (e.g. full data tables, methodology notes, glossary).
11. Signal page breaks where a new major section should begin on a new page (use "---PAGE BREAK---" as a marker).
12. Do not pad. Every paragraph should earn its place. A well-structured 2,000-word document is more valuable than a padded 5,000-word one.
13. Tone: [TONE].
14. Length: [LENGTH].
15. Apply these constraints: [CONSTRAINTS].
16. Do not invent facts, citations, URLs, legal or tax references, or external sources. If source material is missing, include a "Missing information for review" section.
17. Output only the document. No preamble or commentary.
```

## Variables to customise

- `[AUDIENCE]` — who will receive the document. Examples: "Chief Financial Officers at UK financial services firms", "the FCA as part of a regulatory submission", "internal senior leadership team — marked Confidential", "prospective enterprise clients in the cloud advisory space".
- `[PURPOSE]` — what the document is for. Examples: "a whitepaper positioning Meridian's cloud advisory practice", "a technical report on the IAM programme outcomes for the board audit committee", "a regulatory submission document for FCA review".
- `[CONTEXT]` — background for the LLM. Examples: "this is an annual technology trends report to be published on the company website", "this is the programme completion report for the Azure migration — it covers outcomes, lessons learned, and recommendations for the next phase".
- `[INPUT]` — all the substance: research, data, findings, analysis, drafts, and any structured notes.
- `[DESIRED_OUTCOME]` — what the document should do. Examples: "a board-quality report the audit committee can cite as evidence of programme governance", "a client-facing whitepaper that establishes Meridian as a credible IAM advisory voice".
- `[TONE]` — varies by document type. Formal reports: "formal, precise, authoritative". Whitepapers: "authoritative but accessible". Briefings: "clear and direct".
- `[LENGTH]` — specify page count or word count. Examples: "5–8 pages", "2,000–3,000 words", "15 pages including appendices".
- `[FORMAT]` — use the recommended structure; adapt section headings to the document type.
- `[CONSTRAINTS]` — examples: "classification: Confidential — include on every page header", "must include a disclaimer that this is not legal or regulatory advice", "use Meridian house style: dark blue headers, serif body font", "include version history table on the title page".

## Example input

```
AUDIENCE: Chief Information Officers and Head of IT Operations at UK mid-market financial services firms (500–5,000 employees); this is a client-facing whitepaper
PURPOSE: Establish Meridian's cloud advisory practice as a credible voice on IAM (Identity and Access Management) for financial services, and generate inbound enquiries from prospective clients
CONTEXT: Meridian's advisory practice has completed three IAM transformations at UK financial services firms in 2025–2026. This whitepaper draws on those engagements (anonymised) and the team's experience. It should be practical and opinionated, not generic.
INPUT:
  Key themes:
  1. IAM in financial services is uniquely complex: FCA DORA requirements, multiple legacy systems, high-privilege user population, audit obligations
  2. The biggest failure mode: IAM transformation treated as a technology project rather than a business process change
  3. Three patterns we've seen in successful IAM transformations:
     a. Start with a clear identity governance model before choosing technology
     b. Automate deprovisioning first — it's where the risk lives
     c. Treat the first 90 days as a trust-building exercise with the business, not just a technical delivery
  4. Technology options: Microsoft Entra, Okta, SailPoint — each has a distinct fit profile
  5. Metrics that matter: provisioning time, deprovisioning time, access review completion rate, privileged access exceptions outstanding
  6. Common mistake: buying a platform before understanding the access model
  Anonymised example outcomes:
  - Client A (UK insurer, 3,000 staff): reduced provisioning time from 4 hours to 22 minutes; deprovisioning automated to <1 hour
  - Client B (asset manager, 800 staff): passed FCA audit on first attempt after 6-month IAM programme
  - Client C (payments firm, 1,500 staff): eliminated 340 stale privileged accounts discovered in pre-migration audit
DESIRED_OUTCOME: A 6–8 page whitepaper that a CIO reads in full and shares with their team; generates 5+ inbound enquiries per month from the target audience.
TONE: Authoritative, practical, direct — opinionated but evidence-based. Not a marketing brochure.
LENGTH: 6–8 pages (approximately 2,500–3,500 words)
CONSTRAINTS: Anonymise all client examples (use "a UK insurer", not a name). Include a brief about Meridian's advisory practice on the final page (150 words maximum). Include a disclaimer that outcomes vary by engagement. Do not use the word "leverage".
```

## Example output

---

**[PAGE BREAK — TITLE PAGE]**

# Identity and Access Management in Financial Services: What Works, What Fails, and What to Do First

**Meridian Advisory — Cloud and Security Practice**
**May 2026**
**Version 1.0**
**Classification: Public**

*The experiences and outcomes referenced in this paper are drawn from anonymised client engagements. Results vary by organisation, scope, and implementation approach.*

---

**[PAGE BREAK — TABLE OF CONTENTS]**

## Contents

1. Introduction ...................................................... 3
2. Why IAM Is Harder in Financial Services ..................... 3
3. The Most Common Failure Mode ................................. 4
4. Three Patterns of Successful IAM Transformation ........... 4
   4.1 Governance before technology ........................... 4
   4.2 Automate deprovisioning first .......................... 5
   4.3 Treat the first 90 days as a business exercise ........ 5
5. Choosing the Right Platform .................................. 6
6. Metrics That Actually Matter ................................. 7
7. What to Do First: A Practical Starting Point .............. 7
8. About Meridian Advisory ...................................... 8

---

**[PAGE BREAK — EXECUTIVE SUMMARY]**

## Executive Summary

Identity and Access Management (IAM) is a critical control in any financial services organisation — and one of the most frequently mismanaged. Regulatory pressure (FCA DORA-aligned operational resilience requirements), complex legacy estates, and a large population of privileged users make IAM transformation in financial services uniquely challenging.

Based on three IAM programmes completed with UK financial services clients in 2025–2026, this paper identifies the most common failure mode (treating IAM as a technology project), the three patterns consistently seen in successful transformations, and the practical steps that generate the fastest risk reduction.

**Key findings:**
- The most impactful first step is automating deprovisioning — the point at which stale access accumulates and incidents occur
- Platform selection should follow governance design, not precede it
- Three platforms (Microsoft Entra, Okta, SailPoint) have distinct fit profiles; the choice should be driven by existing estate and team capability, not vendor marketing

**Outcomes from recent engagements:**
- A UK insurer reduced provisioning time from 4 hours to 22 minutes
- An asset manager passed its FCA audit on first attempt following a 6-month IAM programme
- A payments firm eliminated 340 stale privileged accounts identified in a pre-migration audit

*Disclaimer: outcomes vary by engagement scope, organisational maturity, and implementation approach.*

---

**[PAGE BREAK — SECTION 1]**

## 1. Introduction

Every financial services CIO understands that identity is security. Who has access to what — and whether that access is appropriate, up to date, and auditable — is foundational to both operational resilience and regulatory compliance.

Yet IAM remains one of the most common sources of audit findings, security incidents, and regulatory challenge in the sector. The problem is rarely a lack of investment; it is usually a mismatch between how IAM is approached and what it actually requires.

This paper is for CIOs and IT operations leaders at UK mid-market financial services firms considering, planning, or executing an IAM transformation. It does not cover every scenario. It shares what we have observed — in practical terms — about what works, what fails, and where to start.

---

## 2. Why IAM Is Harder in Financial Services

Financial services organisations face IAM challenges that are more acute than in most other sectors:

**Regulatory obligation.** FCA operational resilience requirements (DORA-aligned) require demonstrable access controls, automated deprovisioning, and auditable access reviews. These are not aspirational targets — they are requirements that examiners will test.

**Legacy complexity.** Most mid-market firms operate across 8–15 separate systems with no central identity authority. Each system has its own user store, its own provisioning process, and its own audit trail — or lack of one.

**Privileged user population.** Financial services firms typically have a larger-than-average proportion of privileged users (system administrators, finance system operators, data analysts with read access to sensitive records). Managing and auditing this population is non-trivial.

**High consequence of failure.** Stale access at a logistics firm is an operational risk. Stale access at a bank or insurer is a regulatory and reputational risk. The cost of an access-related incident — in remediation, regulatory notification, and potential fine — is an order of magnitude higher.

---

## 3. The Most Common Failure Mode

The most consistent pattern we observe in failed or stalled IAM programmes is this: **the programme is framed as a technology project**.

A platform is selected, a project team is assembled, and the focus becomes configuration and integration. The business — the people who own the joiner-mover-leaver process, who approve access requests, who conduct access reviews — is treated as a stakeholder to be consulted, not a partner to be engaged.

The result is a technically capable platform that the business does not trust, does not use consistently, and does not maintain. The stale access problem that prompted the programme in the first place does not go away — it migrates to the new system.

IAM is a people and process problem that technology can support. It is not a technology problem that, once solved, fixes the process.

---

## 4. Three Patterns of Successful IAM Transformation

### 4.1 Governance before technology

In every successful programme we have observed, the team defined the identity governance model before selecting or configuring a platform. This means: what are the roles in the organisation? What access should each role have? Who approves exceptions? How are access reviews conducted, and by whom?

This work is unglamorous. It requires conversations with HR, line managers, and business system owners. It surfaces disagreements about who should have access to what. It takes time.

It also prevents the most expensive failure mode: discovering, six months into a platform implementation, that the access model the technology has been configured to enforce does not match how the business actually operates.

*A practical starting point:* map the ten highest-risk roles in the organisation (typically: IT administrators, finance system operators, senior managers with broad data access). Define their intended access profile. Compare it to what they actually have. The gap between the two is your first priority.

### 4.2 Automate deprovisioning first

Provisioning (granting access when someone joins or changes role) is visible — someone notices if it is slow. Deprovisioning (revoking access when someone leaves or changes role) is invisible — nobody notices stale access until an incident occurs.

In one engagement, a pre-migration audit at a payments firm identified 340 privileged accounts belonging to individuals who had left the organisation — some over two years prior. None of these accounts had been flagged as a risk, because no one was looking.

Automated deprovisioning — triggered by the HR system on the day of departure or role change — is the highest-impact, lowest-controversy place to start. It reduces risk immediately, is relatively straightforward to implement, and demonstrates value to the business quickly.

### 4.3 Treat the first 90 days as a business exercise

The first 90 days of an IAM programme set the tone. If the programme team spends that time in the technical environment with no visible business engagement, the programme will be perceived as an IT project. When the programme eventually needs the business to adopt new access review processes or change how they submit access requests, the relationship will not be there to support it.

Successful programme teams in the first 90 days: run workshops with business system owners, communicate what is changing and why, involve HR and line managers in defining the governance model, and show early wins (typically, a reduction in provisioning time for a pilot group).

---

## 5. Choosing the Right Platform

Three platforms account for the majority of enterprise IAM implementations in UK financial services: Microsoft Entra, Okta (Workforce Identity), and SailPoint. They are not interchangeable.

| Platform | Best fit | Key strength | Consider if |
|---------|---------|-------------|------------|
| Microsoft Entra | Organisations in the Microsoft ecosystem (Azure, M365, existing Microsoft licensing) | Native Azure integration; cost-effective at scale in the Microsoft estate; strong DORA alignment | You are already significantly committed to Microsoft; existing licensing makes the incremental cost low |
| Okta (Workforce Identity) | Organisations with a diverse, multi-cloud application estate | Best-in-class developer experience; strong multi-cloud federation; excellent API ecosystem | Your application estate is heterogeneous and not Microsoft-centric; developer experience matters |
| SailPoint | Large organisations with complex governance requirements, many joiner-mover-leaver scenarios, and a significant compliance audit function | Deep identity governance capability; strong access certification workflow; mature for regulated environments | You have a large, complex access governance requirement and an existing enterprise software procurement process |

*Note: this comparison is based on the fit profile observed in our engagements. Platform capabilities evolve; validate against current vendor documentation for your specific requirements.*

---

## 6. Metrics That Actually Matter

IAM programmes frequently measure what is easy to measure (number of accounts migrated, number of integrations completed) rather than what matters (reduction in risk and operational burden). The metrics that indicate a programme is working:

- **Provisioning time**: time from HR action (new starter, role change) to access being granted. Baseline typically 4–8 hours for manual processes; target <30 minutes automated.
- **Deprovisioning time**: time from HR departure action to access being revoked. Baseline typically 24–72 hours; target <1 hour automated.
- **Access review completion rate**: percentage of access reviews completed on time. A rate below 80% indicates the review process is not fit for purpose.
- **Privileged access exceptions outstanding**: number of active exceptions to the privileged access policy. This should trend to zero; a growing number indicates the governance model is not being enforced.
- **Stale account count**: accounts not used in 90+ days. Reducing this number is the most direct indicator of improved access hygiene.

---

## 7. What to Do First: A Practical Starting Point

If your organisation is at the beginning of an IAM journey and resources are limited, prioritise in this order:

1. **Audit your privileged accounts.** Before any platform work, run an inventory of all privileged accounts. Compare to current staff lists and role profiles. Revoke any stale privileged access immediately — this is the highest-risk exposure and requires no platform investment to address.

2. **Connect your HR system.** The most reliable trigger for deprovisioning is an HR system event. Before any platform implementation, assess whether your HR system can generate reliable departure and role-change events. Data quality issues at this stage will undermine any automated workflow built on top.

3. **Define your first governance model.** Pick your highest-risk user population (typically IT administrators). Define what access they should have, who approves it, and how often it is reviewed. Implement that model manually if necessary, while platform selection proceeds in parallel.

4. **Then select a platform.** Armed with a clear governance model and a known integration requirement (HR system, key applications), you can evaluate platforms against actual requirements rather than marketing claims.

---

**[PAGE BREAK — ABOUT MERIDIAN]**

## 8. About Meridian Advisory

Meridian Advisory's Cloud and Security Practice works with UK financial services firms on cloud migration, identity and access management, and operational resilience programmes. The practice has completed IAM transformations at insurers, asset managers, and payments firms, working alongside in-house IT teams and major cloud platforms. Engagements range from governance design and platform selection advisory to full programme delivery. For enquiries, contact [contact details].

---

## Review checklist

- [ ] Title page includes document title, date, version, author/organisation, and classification
- [ ] Table of contents covers all major sections with sub-sections
- [ ] Executive summary stands alone — key findings, conclusions, and recommendations in two pages or fewer
- [ ] Heading hierarchy is consistent (H1 for major sections, H2 for sub-sections, H3 for detailed topics)
- [ ] Tables are used for comparative data and have clear titles and column headers
- [ ] Facts, assumptions, and recommendations are distinguishable
- [ ] All projections and estimates have stated bases and caveats
- [ ] Page break markers are in place before major sections
- [ ] Appendices (if required) are listed and referenced from the main body
- [ ] British English used throughout
- [ ] Length is within the specified target

---

Include spacing and formatting that renders well in PDF.
