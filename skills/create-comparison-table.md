---
title: Create Comparison Table
skill_type: Document generation
output: A structured Markdown or formatted table comparing multiple options, vendors, or approaches across a consistent set of criteria — designed to support a specific decision
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor or Word
difficulty: Easy
---

# Skill: Create Comparison Table

## What this skill does

Organises information about multiple options, vendors, tools, or approaches into a structured table that allows a decision-maker to evaluate them against the same criteria simultaneously. A good comparison table is decision-specific: the criteria chosen are the ones that actually discriminate between the options for this particular decision, not a generic feature checklist. The table should make the recommended option obvious to someone who reads only the table — without the author having to explain it in accompanying text.

## When to use it

- Comparing cloud providers (AWS vs. Azure vs. GCP) for a specific workload type
- Evaluating IAM vendors or identity platforms against security, cost, and integration criteria
- Assessing three migration approaches (lift-and-shift vs. re-platform vs. re-architect) for a board decision
- Comparing payroll software options for a finance team with specific compliance requirements
- Producing a vendor shortlist table for a procurement decision where multiple stakeholders will review independently

## Inputs required

- The specific decision the table supports — stated in one sentence
- The options to compare (2–6 is optimal; more than 6 becomes unwieldy)
- The criteria to compare on — ideally 5–8 criteria that actually distinguish the options
- Data for each option against each criterion — where data is missing, note it as "Unknown" or "To be confirmed"
- A weighting or priority for each criterion if some matter more than others
- The intended reader and their level of technical familiarity

## Copy-paste prompt

```
You are a decision analyst and consultant. Create a comparison table for the decision described below.

AUDIENCE: [Who will use this table — e.g. board, CTO, procurement team, finance director]
PURPOSE: [The specific decision this table supports]
CONTEXT: [Why this decision is being made; any constraints or non-negotiables]
INPUT: [List the options to compare; list the criteria to use; provide data for each option where available]
DESIRED_OUTCOME: [The table should make the recommended option clear to a reader who reads only the table]
TONE: Objective and analytical. Comparison tables must be balanced — do not structure criteria to favour a predetermined conclusion.
LENGTH: One table of up to 6 columns and 8 rows. Add a short summary paragraph (3–5 sentences) below the table explaining the headline finding.
FORMAT: Markdown table with bold headers. Use consistent notation: ✓ (meets criterion), ✗ (does not meet), ~ (partially meets), or quantitative values where available. Add a "Recommended" row at the bottom. Add a weighting column if criteria are not equally important.
CONSTRAINTS: Use British English. Do not pad cells with vague assessments ("good", "strong", "competitive") — use specific numbers or named capabilities. Where data is unknown, write "To be confirmed" rather than leaving the cell blank. Output the table and summary paragraph only; no preamble.

TABLE STRUCTURE:
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| [Criterion 1] | High | [data] | [data] | [data] |
| [Criterion 2] | Medium | [data] | [data] | [data] |
| [Criterion 3] | Low | [data] | [data] | [data] |
| **Overall** | | ✓ Meets all high-weight criteria | ~ Meets some | ✗ Significant gaps |
| **Recommended?** | | ✓ Yes | ✗ No | ✗ No |

**Summary**: [3–5 sentences explaining what the table shows and which option is recommended and why]
```

## Suggested output structure

- **Table header** — options as columns, criteria as rows; weight column if applicable
- **Criteria rows** — 5–8 criteria; specific, measurable values wherever possible; consistent notation throughout
- **Overall assessment row** — a summary judgement for each option (Meets requirements / Partial fit / Does not meet requirements)
- **Recommendation row** — clearly indicates the preferred option
- **Summary paragraph** — 3–5 sentences: what the table shows; which option is recommended; what the decisive factor was; any conditions on the recommendation

## Quality controls

- [ ] No more than 6 options (columns) — more than 6 is a shortlist, not a comparison
- [ ] No more than 8 criteria (rows) — more than 8 means the table is not doing its job of discriminating
- [ ] Every cell has specific data — no cell contains only a vague descriptor like "good" or "strong"
- [ ] The criteria chosen actually discriminate between the options — if every option scores the same on a criterion, remove it
- [ ] The recommendation row is present and unambiguous
- [ ] The summary paragraph states the recommended option and the single most decisive reason
- [ ] The table is balanced — criteria are not chosen solely to justify a predetermined answer

## Common failure modes

- **Too many criteria**: A table with 15 rows covers everything but discriminates nothing — choose the 5–8 criteria that matter most for this decision
- **Vague cell values**: "Strong security posture" in a cell is not comparable to a number — replace with "SOC 2 Type II certified, MFA enforced, data encrypted at rest and in transit" or a comparable quantitative measure
- **Criteria that do not differentiate**: If all options offer the same thing on a criterion, that criterion does not help the decision — remove it
- **Missing "so what"**: A table without a summary paragraph or recommendation row forces the reader to draw their own conclusions — the author's job is to make the recommendation, not present raw data and step back
- **Asymmetric data**: If Option A has detailed data and Options B and C have sparse data, the table is not a fair comparison — gather comparable data or note gaps explicitly

## Example request

"Create a comparison table for selecting an IAM platform for our organisation. Options: Microsoft Entra ID (currently in use), Okta, and Ping Identity. Criteria: integration with Azure AD, MFA support, SSO support, cost per user per month (we have 800 users), ISO 27001 compliance evidence, UK data residency available, and vendor support quality. Decision: CTO and Head of Security. Recommendation should address our primary constraint: Azure-native integration and UK data residency are non-negotiable."
