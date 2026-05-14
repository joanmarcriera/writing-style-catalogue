---
title: Board Paper Style
category: Formal
best_for: Major governance decisions requiring a full record of the issue, all options considered, the recommendation, financial analysis, risk assessment, and implementation plan. Required for board meetings, committee approvals, and any decision that must be formally minuted and defensible to external scrutiny.
not_good_for: Quick updates or internal briefings (use Smart Brevity or Executive Briefing); detailed technical specifications (use Technical Documentation); analytical arguments where only one option is being proposed (use Consulting Style or Minto Pyramid).
default_tone: Formal, neutral, and comprehensive. Objective in analysis; explicit in recommendation.
typical_length: 8–15 pages (2,500–5,000 words), plus appendices
aliases: [Board Pack, Board Memo, Committee Paper, Governance Paper]
---

# Board Paper Style

## What this style is

A board paper is the formal governance document that presents a significant decision to a board of directors, audit committee, investment committee, or similar governance body. It is comprehensive by design: the board is accountable for the decisions it makes, and the paper must provide everything needed to make an informed, defensible decision — including all relevant options, their financial impact, their risks, and a clear recommendation.

Board papers differ from executive briefings in scope and in audience relationship. Where an executive briefing informs and advises, a board paper seeks formal approval. The board is not the executive — it governs. A board paper therefore presents multiple options objectively, identifies what the board is being asked to approve, and contains a formal resolution or recommendation for the minutes. The standard of evidence, completeness, and governance language is higher than any other document type in this catalogue.

**Core principle**: Complete information for informed governance decision-making. The board must be able to make a sound, defensible decision from this document alone.

## When to use it

- Board of directors meetings requiring formal approval of a strategic decision
- Major capital investment or budget allocation decisions (typically above a defined materiality threshold)
- Acquisition, divestiture, merger, or partnership decisions
- Material policy changes (remuneration, risk appetite, data governance)
- Major contractual commitments with long-term financial or reputational consequences
- Regulatory, compliance, or legal matters requiring board sign-off
- Significant operational changes with strategic implications (e.g. cloud migration at scale, major restructuring)

## When not to use it

- Quick operational or performance updates — use [Smart Brevity](axios-smart-brevity.md) instead
- Detailed technical or operational guidance — use [Technical Documentation](technical-documentation.md) instead
- Teaching or educational content — use [Socratic Explainer](socratic-explainer.md) instead
- Quick recommendations not requiring formal approval — use [BLUF](bluf-bottom-line-up-front.md) or [Minto Pyramid Principle](minto-pyramid-principle.md) instead

## Core structure

```
[COVER PAGE]
Title of the paper.
Meeting date and agenda item reference.
Author(s) and date prepared.
Document classification (Confidential / Restricted).
Version number.

[EXECUTIVE SUMMARY — 1 PAGE MAXIMUM]
The issue or decision required.
Options considered (headline only).
Recommendation and rationale summary.
Financial summary.
Key risk summary.
What the board is asked to approve.

[BACKGROUND]
Why this matter is before the board.
Relevant prior board decisions or commitments.
Strategic or regulatory context.
What has changed to make this decision necessary now.

[ANALYSIS OF OPTIONS]
For each option (2–3 minimum):
- Description of the option
- Financial impact (initial cost, ongoing cost, 5-year NPV or TCO where appropriate)
- Operational implications
- Strategic alignment
- Key risks specific to this option
- Pros and cons summary

[BOARD RECOMMENDATION]
Which option is recommended and why.
Summary of why alternatives were not selected.
Success criteria: how will we know this was the right decision?

[GOVERNANCE AND RISK]
Legal and regulatory requirements.
Compliance obligations triggered.
Key strategic, operational, financial, and reputational risks.
Risk mitigation approach for each.
Insurance or indemnity considerations if applicable.

[IMPLEMENTATION]
High-level implementation plan with phases.
Resource requirements: people, budget, external support.
Key dependencies and critical path.
Milestone dates and approval gates.

[FINANCIAL SUMMARY]
Cost table: capital expenditure, operating expenditure, total cost of ownership.
Comparison across options (5-year view recommended).
Budget source and approval status.
Financial assumptions.

[APPENDICES]
Supporting data, models, third-party reports, or detailed analysis.
Referenced but not required to be read for the decision.
```

## Copy-paste prompt

```
You are an expert in board governance documentation. Your task is to write a comprehensive board paper from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Board of Directors", "Audit and Risk Committee", "Investment Committee"]
PURPOSE: [PURPOSE — e.g. "Seek board approval for a £3.2M cloud migration programme", "Present options for the renewal or replacement of the identity management platform", "Recommend adoption of a new data governance policy"]
CONTEXT: [CONTEXT — e.g. "Data centre lease expires in 36 months; renewal costs are projected at £3.6M; the board digital strategy commits to cloud-first architecture; three vendors have been evaluated over six months"]
INPUT: [INPUT — paste all analysis, financial data, risk assessments, vendor assessments, and your recommendation here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Board formally approves Option B (AWS migration) and authorises the programme budget"]
TONE: [TONE — e.g. "Formal and comprehensive", "Neutral in options analysis, explicit in recommendation", "Suitable for external audit scrutiny"]
LENGTH: [LENGTH — e.g. "10–14 pages excluding appendices"]
FORMAT: [FORMAT — Executive Summary (1 page) + Background + Options Analysis + Recommendation + Governance and Risk + Implementation + Financial Summary + Appendices]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not disclose vendor pricing in the main body — include in Appendix A marked Commercially Sensitive", "All financial figures must match those in the January board-approved budget", "Paper must comply with the company's Board Paper Policy v3.2"]

INSTRUCTIONS:
1. Write a one-page Executive Summary that contains: the decision required, a headline summary of each option, the recommendation and its primary rationale, key financial figures, the top two risks, and the formal resolution being sought.
2. Analyse each option using a consistent structure so the board can compare like with like. Include financial impact (5-year view), operational implications, strategic alignment, and key risks for each option.
3. Present options objectively in the Analysis section — do not allow the framing or language to favour the recommended option before the Recommendation section.
4. In the Recommendation section, state clearly which option is recommended, why, and why alternatives were rejected. Include success criteria.
5. In Governance and Risk, name specific risks — not categories. For each risk, provide: description, likelihood, potential impact, and mitigation.
6. Provide a realistic high-level implementation plan with phases, milestones, and resource requirements.
7. Include a financial summary table comparing all options on a 5-year basis.
8. Use British English throughout (colour, organisation, licence, favour, analyse, programme, etc.).
9. Preserve all factual claims exactly as provided in [INPUT]. Flag assumptions explicitly with "(assumed)" in parentheses.
10. Formal board language: use "the Board is asked to approve" not "please approve"; use "the Company" and defined entity names consistently.
11. Total length must not exceed [LENGTH] excluding appendices.

Output the board paper only. No preamble, no commentary.
```

## Output format

A board paper is a formal printed or PDF document, typically 8–15 pages in the main body plus appendices. It follows a defined structure that is consistent meeting-to-meeting so board members can navigate it efficiently. It contains:

- **Cover page**: Title, meeting reference, date, author, classification, version
- **Executive Summary**: 1 page maximum, standing alone as a complete overview
- **Main body sections**: Headed with numbered titles (e.g. "3. Analysis of Options")
- **Tables**: Used for financial comparisons, risk registers, and option comparisons
- **Formal resolution or recommendation**: Stated in the language used in board minutes
- **Appendices**: Labelled A, B, C — clearly cross-referenced from the main body

The document uses formal third-person language ("the Board," "the Company," "the Chief Financial Officer"), precise financial figures with sources cited, and consistent formatting. The Executive Summary must be a complete standalone document: a board member reading only the Executive Summary should be fully informed to vote.

## Example

**Board Paper: Identity and Access Management Platform — Renewal or Replacement**
*Board of Directors | Meeting: 18 June 2026 | Agenda Item 7 | Author: Chief Information Officer*
*Classification: Confidential | Version: Final*

---

**1. Executive Summary**

The Company's identity and access management (IAM) platform contract with LegacyAuth Ltd expires on 31 December 2026. The Board is asked to approve one of three options for the period beyond that date.

Three options have been assessed: renew with the existing vendor, migrate to a modern cloud-native platform (Okta), or build a bespoke internal solution. The recommendation is Option B: migration to Okta, at an estimated total cost of £620,000 over five years (assumed — based on vendor quotes and internal estimates), compared to £840,000 for renewal and £1.4M for internal build.

The primary risk is migration complexity; this will be mitigated through a phased 12-month programme with an external delivery partner. Migration resolves two outstanding audit findings and satisfies three enterprise client contractual requirements effective from January 2027.

**The Board is asked to approve Option B (Okta migration) and authorise the £620,000 five-year budget allocation from the IT capital reserve.**

---

**2. Background**

The current IAM platform manages authentication and access control for 1,850 staff and 340 systems across the Company. It was implemented in 2017 and has received no major updates since 2021. The platform handles all privileged access, single sign-on (SSO), and multi-factor authentication (MFA) across production systems.

In its December 2025 report, the external auditor identified two control weaknesses related to the current platform: absence of automated access certification reviews, and lack of real-time anomalous access alerting. Both are required by ISO 27001 clause A.9.2 and must be remediated before the Company's recertification audit in November 2026.

Three enterprise clients — representing 34% of annual recurring revenue — have updated their supplier security questionnaires to require evidence of modern IAM controls, including conditional access policies and continuous authentication monitoring. These requirements take effect from 1 January 2027.

---

**3. Analysis of Options**

**Option A: Renew with LegacyAuth Ltd (24-month contract)**

LegacyAuth has offered a 24-month renewal at £168,000 per annum. The current platform does not natively support automated access certification or real-time anomaly detection; both would require bespoke customisation estimated at £95,000 (assumed).

| Dimension | Assessment |
|-----------|-----------|
| 5-year cost | £840,000 (renewal + customisation + ongoing maintenance) |
| Audit compliance | Partial — requires customisation; delivery risk remains |
| Client requirements | Does not satisfy all three client requirements natively |
| Strategic alignment | Low — platform is approaching end of vendor support |
| Implementation risk | Low — no migration required |

**Option B: Migrate to Okta (Recommended)**

Okta is a cloud-native IAM platform used by over 18,000 organisations globally. It natively meets both audit findings and all three client requirements. Migration has been scoped at 12 months.

| Dimension | Assessment |
|-----------|-----------|
| 5-year cost | £620,000 (assumed — licence £72,000/annum; migration £260,000 one-off) |
| Audit compliance | Full — both findings resolved natively; no customisation required |
| Client requirements | Fully satisfies all three client requirements |
| Strategic alignment | High — aligns with cloud-first strategy; SaaS reduces maintenance burden |
| Implementation risk | Medium — migration complexity; mitigated by phased approach |

**Option C: Internal build**

An internal IAM solution was scoped by the engineering team. Initial build cost is estimated at £480,000 over 18 months, with ongoing maintenance of £185,000 per annum (assumed).

| Dimension | Assessment |
|-----------|-----------|
| 5-year cost | £1.4M (assumed) |
| Audit compliance | Achievable but dependent on internal delivery capacity |
| Client requirements | Achievable but requires independent security certification |
| Strategic alignment | Neutral — builds internal capability but diverts engineering resource |
| Implementation risk | High — depends on engineering capacity currently committed to other priorities |

---

**4. Board Recommendation**

The Board is recommended to approve Option B: migration to the Okta IAM platform, at a total five-year cost of £620,000.

Option A was rejected because it does not fully resolve the audit findings without significant customisation risk and does not position the Company for client requirements beyond 2027. Option C was rejected because the cost is disproportionate and internal engineering capacity is insufficient to absorb the build alongside committed product delivery.

Success criteria: (a) ISO 27001 recertification achieved in November 2026 with both audit findings closed; (b) all three enterprise client questionnaire requirements satisfied by 31 December 2026; (c) programme delivered within budget (±10%).

---

**5. Governance and Risk**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Migration delay beyond December 2026 | Medium | High — audit and client deadlines missed | Phased delivery plan; engage external delivery partner; monthly programme board |
| Data integrity issue during migration | Low | Critical — access control failure | Full parallel operation during transition; independent testing at each phase gate |
| User disruption during cutover | Medium | Medium — productivity impact | Phased rollout by user group; helpdesk support reinforced during transition |
| Okta vendor dependency | Low | Medium — future pricing and service risk | Standard contractual protections; exit plan documented at outset |

---

**6. Implementation**

Phase 1 (July–September 2026): Privileged access and admin accounts — 120 users
Phase 2 (October–November 2026): All staff SSO and MFA — 1,850 users
Phase 3 (December 2026): Legacy platform decommission and final audit evidence pack

External delivery partner to be procured by 30 June 2026. Internal programme lead: Head of IT Security.

---

**7. Financial Summary**

| Option | Year 1 | Years 2–5 (pa) | 5-Year Total |
|--------|--------|----------------|--------------|
| A — Renew | £358,000 | £168,000 | £840,000 |
| B — Okta (recommended) | £332,000 | £72,000 | £620,000 |
| C — Internal build | £480,000 | £185,000 | £1,420,000 |

*All figures assumed unless otherwise stated. Source: vendor quotes and internal cost model. Budget source: IT capital reserve (current balance £1.1M).*

---

**Appendix A**: Vendor assessment scorecard (Confidential — Commercially Sensitive)
**Appendix B**: Audit finding extracts from December 2025 external audit report
**Appendix C**: Client contractual requirement extracts

## Quality checklist

- [ ] Executive Summary is one page and fully standalone — a reader can vote from it alone
- [ ] All three (or more) options are presented using an identical analytical structure
- [ ] No option is favoured by language or framing in the Analysis section
- [ ] Financial impact is quantified for all options on a 5-year basis
- [ ] Specific named risks are identified with likelihood, impact, and mitigation
- [ ] The formal resolution or decision sought is stated clearly and unambiguously
- [ ] Success criteria are defined and measurable
- [ ] Implementation plan is phased with realistic milestones and named owners
- [ ] Assumptions are explicitly flagged and distinguished from confirmed facts
- [ ] British English and formal board language used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Buried recommendation | Board cannot find the ask quickly | State clearly in Executive Summary: "The Board is asked to approve…" |
| Only one option presented | Appears pre-determined; fails governance standard | Always present at least two genuine alternatives |
| Vague financials | Board cannot assess value or compare options | Quantify all options on the same basis (5-year TCO) |
| Generic risks ("project risk") | Board cannot assess actual exposure | Name specific risks with likelihood, impact, and mitigation |
| Executive Summary too long | Defeats the purpose of the one-page summary | Hard limit of one page; move detail to the body |
| No formal resolution language | Paper cannot be properly minuted | Include "The Board is asked to approve/note/ratify…" |

---

See [skills/create-board-pack.md](../skills/create-board-pack.md) for multi-part board pack generation.

See [examples/board-paper.md](../examples/board-paper.md) for a complete example.
