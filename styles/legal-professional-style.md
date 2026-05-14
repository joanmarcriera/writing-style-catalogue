---
title: Legal Professional Style
category: Specialist
best_for: Formal legal documents — contracts, service level agreements, terms of service, privacy notices, legal opinions, and compliance policies — where precision, defined terms, and legal defensibility are essential. Suitable for any document that may be relied upon in a dispute, audit, or regulatory review.
not_good_for: Internal business communication where legal precision is not required (use Consulting Style or BLUF); public-facing communications requiring plain language accessibility (use Plain English); educational explanations of legal concepts for non-specialists (use Socratic Explainer).
default_tone: Formal and precise. Neutral and defined. Authoritative without ambiguity.
typical_length: Varies widely — NDAs may be 2–4 pages; service agreements 10–30 pages; enterprise contracts 50+ pages with schedules
aliases: [Legal Writing, Formal Legal, Contract Drafting, Legal Drafting]
---

# Legal Professional Style

## What this style is

Legal professional style is the formal written register of law: contracts, agreements, policies, opinions, and compliance documentation. It is designed for documents that may be interpreted, enforced, or disputed by parties who were not present when the document was written. Every word is chosen for its legal meaning; every term that could be ambiguous is defined; every obligation is stated as a condition and consequence pair.

Unlike other professional writing styles that prioritise clarity and concision, legal drafting prioritises precision and completeness. A legal document must mean exactly the same thing to every person who reads it, regardless of their prior knowledge, assumptions, or relationship with the other party. Ambiguity is not a stylistic flaw — it is a legal liability.

**Core principle**: Exact language, no ambiguity, every term defined, every obligation and right explicitly stated as a condition and consequence.

## When to use it

- Commercial contracts and supplier agreements
- Service level agreements (SLAs) and master service agreements (MSAs)
- Terms of service and terms and conditions for products or platforms
- Privacy notices and data processing agreements (DPAs) under UK GDPR
- Employment contracts and settlement agreements
- Compliance policies with legal force (e.g. acceptable use policies, data retention policies)
- Formal legal opinions and memoranda
- Non-disclosure and confidentiality agreements (NDAs)

## When not to use it

- Internal business communication where legal precision is not required — use [Consulting Style](consulting-style.md) or [BLUF](bluf-bottom-line-up-front.md) instead
- Public-facing communications requiring accessibility — use [Plain English](plain-english.md) instead; consider a plain English summary alongside the legal document
- Educational explanations of legal concepts for non-specialists — use [Socratic Explainer](socratic-explainer.md) instead
- Tax technical analysis — use [Tax Advisory Style](tax-advisory-style.md) instead

## Core structure

```
[PARTIES AND DATE]
Full legal names of all parties.
Registered addresses.
Date of agreement.

[RECITALS / BACKGROUND] (optional)
Brief context for the agreement.
What the parties intend.
Does not create legal obligations — factual only.

[DEFINITIONS]
Defined terms listed alphabetically (or in order of first use).
Each definition: "Term" means [precise definition].
All capitalised terms throughout the document are defined here.

[OPERATIVE PROVISIONS]
Numbered articles and sections.
Each section covers one legal topic.
Structured: obligation → condition → consequence.

[RIGHTS AND OBLIGATIONS]
For each party: what they must do, what they may do, what they must not do.
"Shall" / "must" for obligations.
"May" for discretionary rights.
"Must not" / "shall not" for prohibitions.

[CONDITIONS AND TERM]
When the agreement starts and ends.
Conditions precedent to obligations taking effect.
Renewal, extension, or termination mechanics.

[TERMINATION]
Events that permit or require termination.
Notice periods and process.
Consequences of termination.

[LIABILITY AND INDEMNITY]
Limitation of liability clauses.
Indemnification provisions.
Exclusions of consequential loss.

[STANDARD CLAUSES / BOILERPLATE]
Governing law and jurisdiction.
Entire agreement clause.
Severability.
Notices and service.
Waiver provisions.
Amendments process.

[SCHEDULES / ANNEXES]
Detailed specifications, pricing, service descriptions.
Referred to in the body but not part of the operative provisions.
```

## Copy-paste prompt

```
You are an expert legal drafter. Your task is to draft a formal legal document from the following brief.

AUDIENCE: [AUDIENCE — e.g. "The parties to the agreement and their respective legal counsel", "Internal legal team reviewing a supplier SLA", "Data protection officer reviewing a DPA"]
PURPOSE: [PURPOSE — e.g. "Draft a service level agreement between a cloud provider and an enterprise customer", "Draft an NDA for sharing commercially sensitive information during an M&A due diligence process", "Draft a data processing agreement under UK GDPR Article 28"]
CONTEXT: [CONTEXT — e.g. "The supplier provides managed identity services; the customer requires 99.9% uptime and incident response within 15 minutes for critical failures; the contract term is 24 months"]
INPUT: [INPUT — paste all agreed commercial terms, service descriptions, obligations, and any draft clauses here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "A complete, legally defensible agreement that clearly states each party's obligations and can be executed without substantive amendment by either party's lawyers"]
TONE: [TONE — e.g. "Formal legal register", "Precise and unambiguous", "Standard commercial — not aggressive or one-sided"]
LENGTH: [LENGTH — e.g. "6–10 pages for the main agreement, with schedules as needed"]
FORMAT: [FORMAT — numbered articles and sections; definitions section; schedules for technical specifications]
CONSTRAINTS: [CONSTRAINTS — e.g. "Governing law must be England and Wales", "Liability cap must reflect the figures in [INPUT]", "Must comply with UK GDPR where personal data is processed", "This is a template — do not include any party-specific confidential information"]

INSTRUCTIONS:
1. Draft all defined terms in a Definitions section. Every capitalised term used in the agreement must be defined. Use "means" not "refers to."
2. Use "shall" or "must" for obligations; "may" for discretionary rights; "must not" or "shall not" for prohibitions. Never use "should," "might," "could potentially," or "it is expected that."
3. Structure each operative section as: obligation → condition → consequence. E.g. "If [condition], the Provider shall [obligation] within [timeframe]."
4. Number all articles and sections. Use sub-sections for nested obligations (e.g. 3.1, 3.1(a), 3.1(b)).
5. Use defined terms consistently throughout. Once a term is defined, use only that defined term — do not use synonyms or pronouns where ambiguity could arise.
6. Include all standard boilerplate clauses: entire agreement, severability, governing law, notices, waiver, and amendments.
7. Use British English throughout (colour, organisation, licence, favour, etc.). Note: "licence" (noun) vs "license" (verb).
8. Preserve all commercial terms exactly as provided in [INPUT]. Do not change figures, dates, service descriptions, or obligations.
9. Flag any gap in [INPUT] where a term must be agreed by the parties but has not been specified — use [TO BE AGREED] as a placeholder.
10. Include a prominent disclaimer that this is a template and must be reviewed by a qualified lawyer before execution.

Output the legal document only. No preamble, no commentary.
```

## Output format

A legal document is a formal printed or digital document, typically delivered as a Word or PDF file on headed paper (for opinions) or in standard commercial format (for contracts). It contains:

- **Title and parties block**: Document title, full legal names, registered details, and date
- **Numbered sections**: Articles (1, 2, 3) containing sub-sections (1.1, 1.2) containing paragraphs (1.1(a), 1.1(b))
- **Definitions section**: Alphabetically ordered or in order of first appearance; each definition on a new line
- **Tables**: Used for service levels, pricing schedules, and matrix-format obligations
- **Signature block**: Space for signatories with name, title, company, date, and witness (where required)
- **Schedules**: Attached after the main agreement body; each labelled Schedule 1, Schedule 2, etc.

Legal documents do not use bullet points in the operative provisions (these are replaced by numbered sub-clauses). They do not use informal language, contractions, or conversational register. Headers are formal and descriptive.

## Example

**Service Level Agreement (Extract)**

*Between: CloudPlatform Ltd (registered in England and Wales, company number 09876543) ("Provider")*
*And: Acme Financial Services Ltd (registered in England and Wales, company number 01234567) ("Customer")*
*Date: 14 May 2026*

---

**1. Definitions**

In this Agreement, the following terms shall have the meanings set out below:

**"Agreement"** means this Service Level Agreement together with all Schedules attached hereto.

**"Business Day"** means any day other than a Saturday, Sunday, or public holiday in England and Wales.

**"Critical Incident"** means any Service failure that renders the Service wholly unavailable or that affects fifty per cent (50%) or more of Customer's authorised users.

**"Customer Data"** means all data, content, and information submitted to or processed by the Service by or on behalf of the Customer.

**"Planned Maintenance"** means maintenance activity notified to the Customer at least seventy-two (72) hours in advance in accordance with clause 5.2.

**"Response Time"** means the period between the Provider receiving a support request via the Support Portal and a qualified engineer commencing active investigation of that request.

**"Service"** means the cloud-hosted identity and access management platform described in Schedule 1, including all updates and releases made available during the Term.

**"Support Hours"** means 08:00 to 18:00 GMT on Business Days. Emergency support outside Support Hours is available in accordance with clause 4.3.

**"Uptime"** means the percentage of hours in each calendar month during which the Service is available and functioning in accordance with Schedule 1, excluding Planned Maintenance.

---

**2. Service Levels**

2.1 **Uptime Commitment.** The Provider shall maintain Uptime of no less than ninety-nine point nine per cent (99.9%) in each calendar month, measured across all Provider availability zones hosting the Service.

2.2 **Exclusions.** Uptime calculations shall exclude:

- (a) periods of Planned Maintenance notified in accordance with clause 5.2;
- (b) failures caused by Customer's own configuration, data, or actions taken by Customer outside the Provider's recommended operating parameters; and
- (c) force majeure events as defined in clause 12.

2.3 **Measurement.** Uptime shall be calculated using the Provider's monitoring platform, records of which shall be made available to the Customer on request within five (5) Business Days.

---

**3. Incident Response**

3.1 **Critical Incidents.** Upon detection of a Critical Incident, the Provider shall:

- (a) acknowledge the incident to the Customer via the Support Portal and by telephone to the Customer's designated contact within fifteen (15) minutes of detection;
- (b) provide a written status update to the Customer every sixty (60) minutes until the Critical Incident is resolved; and
- (c) publish a post-incident report to the Customer within forty-eight (48) hours of resolution, in accordance with the format set out in Schedule 2.

3.2 **Standard Incidents.** For all other incidents, the Provider shall acknowledge the Customer's support request within the Response Times set out in Schedule 3.

3.3 **Escalation.** If the Customer reasonably believes that the Provider is not responding in accordance with this clause 3, the Customer may escalate to the Provider's service delivery manager using the contact details in Schedule 4.

---

**4. Service Credits**

4.1 If Uptime in any calendar month falls below the level specified in clause 2.1, the Customer shall be entitled to claim service credits as follows:

| Monthly Uptime | Service Credit |
|---------------|---------------|
| 99.0% to 99.8% | Ten per cent (10%) of the monthly fee for that month |
| 98.0% to 98.9% | Twenty-five per cent (25%) of the monthly fee for that month |
| Below 98.0% | Fifty per cent (50%) of the monthly fee for that month |

4.2 Service credits shall be applied as a deduction against the Customer's next invoice. Credits shall not be applied as a cash payment.

4.3 **Sole Remedy.** Save in respect of the Provider's obligations under the Data Processing Agreement, service credits shall constitute the Customer's sole financial remedy for any failure of the Provider to meet the service levels set out in this Agreement.

---

*Note: This is an extract for illustrative purposes only. This document does not constitute legal advice and must be reviewed by a qualified lawyer before execution.*

## Quality checklist

- [ ] All key terms are defined in the Definitions section — every capitalised term has a definition
- [ ] "Shall" and "must" are used for obligations; "may" for discretionary rights; "must not" for prohibitions
- [ ] No ambiguous pronouns — defined terms used consistently throughout
- [ ] All sections are numbered consistently (article → section → paragraph)
- [ ] Every obligation states the condition, the obligation, and the consequence
- [ ] All commercial terms from [INPUT] are accurately reflected without alteration
- [ ] [TO BE AGREED] placeholders mark any gaps from [INPUT]
- [ ] Standard boilerplate clauses are present: entire agreement, severability, governing law, notices, waiver
- [ ] British English used throughout
- [ ] Professional disclaimer is included

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Undefined terms used | Ambiguity creates disputes; term may be interpreted differently by each party | Define every capitalised term in the Definitions section |
| "Should" instead of "shall" or "must" | Legal obligation is unclear; "should" implies aspiration not duty | Use "shall" or "must" for obligations — unambiguously |
| Ambiguous pronouns ("it," "they," "the party") | Creates genuine interpretation disputes | Use defined terms consistently; repeat the noun |
| Missing conditions | Creates unintended absolute obligations | State "if [condition], then [obligation]" explicitly |
| Overly complex sentences | Hard to interpret; may be unenforceable for uncertainty | Break into numbered sub-clauses of no more than 30 words each |
| Schedules not cross-referenced | Schedules may not form part of the agreement | Reference each schedule in the operative provisions |
| No entire agreement clause | Prior representations may create liability | Include standard entire agreement clause in boilerplate |

---

**Note**: This is a template. Always have a qualified lawyer review before execution.

See [reference/glossary.md](../reference/glossary.md) for common legal terms.
