---
title: Create Data Room Index
skill_type: Document generation
output: A structured document index and folder taxonomy for a virtual data room, with document metadata, access controls, and a completeness tracker — suitable for M&A due diligence, regulatory audit, or investor review
tools_needed: LLM (Claude/ChatGPT/Gemini), Excel or Google Sheets, VDR platform (Ansarada, Intralinks, SharePoint, or Datasite)
difficulty: Medium
---

# Skill: Create Data Room Index

## What this skill does

Designs and populates the organisational structure (folder taxonomy and document index) for a virtual data room used in M&A due diligence, regulatory submissions, investor reviews, or audit processes. The index defines the folder hierarchy, assigns a reference number to each expected document, notes which documents are available and which are outstanding, and applies access tiers (who can see what). A well-organised data room accelerates the due diligence process, reduces information requests from the other party, and signals that the organisation is professionally managed. A poorly organised one delays transactions and erodes buyer or investor confidence.

## When to use it

- Preparing the sell-side data room for an M&A process, fundraising round, or management buyout
- Organising documentation for a regulatory submission (FCA authorisation, CMA merger clearance, ICO audit)
- Setting up a buy-side due diligence tracking structure to manage information requests from a target
- Preparing the data room for an investor due diligence process ahead of a Series A, B, or growth equity round
- Creating an audit-readiness documentation package for ISO 27001, SOC 2, or internal audit

## Inputs required

- The purpose of the data room (M&A sell-side, fundraising, regulatory, audit)
- The stage of the process (initial tease, full due diligence, confirmatory)
- The organisation type (company, fund, charity, regulated entity)
- A list of departments or business areas whose documents will be included
- Any documents already confirmed as available
- Access control requirements: who gets access to which sections (standard vs. senior buyer only vs. advisers only)
- Any documents that must be excluded or redacted for commercial sensitivity reasons

## Copy-paste prompt

```
You are a corporate finance adviser and data room specialist. Create a data room index for the transaction described below.

AUDIENCE: [Who will access this data room — e.g. buyer's legal and financial advisers, FCA reviewers, investor due diligence team]
PURPOSE: [What the data room supports — M&A sell-side, buy-side tracking, regulatory submission, investor round, audit]
CONTEXT: [Organisation type, sector, size; stage of the process; any special sensitivities or exclusions]
INPUT: [List of business areas or departments to cover; any documents confirmed as available; any known gaps; access control tiers required]
DESIRED_OUTCOME: [A complete folder taxonomy with document index, reference numbers, availability status, and access tiers — ready to implement in a VDR platform]
TONE: Formal and structured. Data room indexes are professional transaction documents — precision in naming and categorisation matters.
LENGTH: Full folder taxonomy (as deep as needed) plus a document index table with one row per expected document.
FORMAT: Numbered folder taxonomy (e.g. 1.0, 1.1, 1.2), then a Markdown table with columns: Ref | Section | Document name | Format | Status | Access tier. Follow with an access control matrix.
CONSTRAINTS: Use British English. Document names must be specific — not "contracts" but "Material customer contracts (>£100k annual value)". Status options: Available | Outstanding | Redacted | Excluded. Output only the index and access matrix; no preamble.

FOLDER TAXONOMY FORMAT:
1.0 Corporate and Legal
  1.1 Incorporation and constitutional documents
  1.2 Share capital and ownership
  1.3 Regulatory licences and permissions
  ...

DOCUMENT INDEX TABLE FORMAT:
| Ref | Section | Document | Format | Status | Access |
|-----|---------|----------|--------|--------|--------|
| 1.1.1 | Corporate | Certificate of Incorporation | PDF | Available | All |
| 1.1.2 | Corporate | Articles of Association (current) | PDF | Available | All |

ACCESS CONTROL MATRIX:
Tier 1 (All parties): Sections 1, 2, 3
Tier 2 (Senior buyers only): Sections 4, 5
Tier 3 (Legal advisers only): Section 6 (litigation)
```

## Suggested output structure

- **Data room overview** — purpose, transaction reference, date established, administrator contact
- **Folder taxonomy** — numbered hierarchy from top-level categories (Corporate, Financial, Operational, Legal, Technical, HR, Environmental) to document-level items
- **Document index table** — one row per expected document; reference, section, document name, format, status, access tier
- **Completeness tracker** — summary of documents outstanding by section; percentage complete
- **Access control matrix** — who (by role or party) can access which sections
- **Document upload protocol** — naming convention, version control rules, and process for adding new documents

## Quality controls

- [ ] Every section of the business has a corresponding folder section — no area left unindexed
- [ ] Document names are specific enough that any adviser can identify what is needed without asking
- [ ] Every document has an access tier assigned — no document defaults to open access
- [ ] Outstanding documents are flagged, not omitted — a buyer who finds gaps later will be more concerned than one who sees them tracked
- [ ] The naming convention is consistent throughout — use the same format for all document names
- [ ] The index has been reviewed by legal counsel before the data room is opened to any external party

## Common failure modes

- **Generic folder names**: Folders named "Contracts" or "Legal" are not specific enough — "Material commercial contracts (>£100k p.a.)" and "Litigation and disputes — active and threatened" are navigable
- **Missing access tiers**: A data room with no access controls exposes commercially sensitive information to parties who should not see it (e.g. management accounts visible to a trade buyer who is also a competitor)
- **Index not maintained**: A data room index that is not updated as documents are added or removed becomes misleading — assign a data room administrator and update the index daily during active due diligence
- **Outstanding documents not tracked**: Showing a blank cell for missing documents is worse than showing "Outstanding" — buyers assume concealment; transparency about gaps builds more trust
- **No naming convention**: If each document is named differently (some with dates, some without; some with versions, some without), the data room becomes navigable only by the person who built it — define and enforce a naming convention from day one

## Example request

"Create a sell-side data room index for the acquisition of a UK fintech company (Series B, 80 employees, FCA-regulated). The buyer is a listed financial services group. Data room sections needed: Corporate and legal, Financial (3 years of accounts plus management accounts), Products and technology, Customers and commercial contracts (redact customer names in initial phase), Regulatory (FCA authorisation, compliance policies), HR and key people, IT infrastructure and security (high sensitivity — Tier 2 access only), and IP and data. Provide a completeness tracker showing which sections are complete and which have outstanding documents."
