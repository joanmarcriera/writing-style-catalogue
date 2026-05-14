---
title: Executive Briefing
category: Formal
best_for: Formal, polished summaries for C-level executives and board members who need comprehensive context, analysis, and a clear recommendation in a single document. Ideal for high-stakes proposals, strategic decisions, annual reviews, and investor or stakeholder communications requiring both depth and clarity.
not_good_for: Quick status updates where a recommendation is already known (use Smart Brevity); detailed technical specifications that require engineering-level depth (use Technical Documentation); informal team communications.
default_tone: Formal and authoritative. Clear and direct. Confident without being dismissive of risk.
typical_length: 2–4 pages (600–1,500 words)
aliases: [Executive Summary, C-Suite Brief, Leadership Brief]
---

# Executive Briefing

## What this style is

An Executive Briefing is a formal, polished document written specifically for the most senior readers in an organisation — those who have the authority to make significant decisions but limited time to read lengthy analysis. It combines the concision of a summary with the substance of a full analysis: every claim is backed, every risk is named, and the recommendation is explicit and unambiguous.

Unlike a board paper (which presents multiple options for governance approval), an executive briefing presents a single, well-argued recommendation supported by analysis. Unlike a consulting document (which leads with the issue), an executive briefing leads with the recommendation and provides context behind it. The executive is not asked to work through evidence to reach a conclusion — the conclusion is stated upfront and the evidence justifies it.

**Core principle**: Inform and advise at the highest level. Every section earns its place by supporting the recommendation or managing the risk.

## When to use it

- Board or C-suite decision materials for strategic proposals
- Formal briefings prior to significant investment, acquisition, or structural decisions
- High-stakes proposals requiring risk assessment and explicit recommendation
- Annual or strategic reviews requiring comprehensive summary and forward direction
- Investor or major stakeholder briefings requiring both narrative and evidence
- Post-incident or post-crisis summaries for leadership teams
- Regulatory or compliance updates requiring leadership action

## When not to use it

- Quick operational updates — use [Smart Brevity](axios-smart-brevity.md) instead
- Detailed technical specifications — use [Technical Documentation](technical-documentation.md) instead
- Teaching or explanation for non-specialist audiences — use [Plain English](plain-english.md) instead
- Detailed multi-option business case requiring governance approval — use [Board Paper Style](board-paper-style.md) instead
- Persuasive analytical argument requiring full evidence-building — use [Consulting Style](consulting-style.md) instead

## Core structure

```
[TITLE]
Document title and date. Optional: version number.

[EXECUTIVE SUMMARY — 1 PARAGRAPH]
The core issue, the recommendation, and the key supporting rationale.
Maximum 100 words. A reader who reads only this paragraph must understand
the complete situation and what they are being asked to decide or do.

[BACKGROUND]
Context: why this matter exists and why it is relevant now.
Prior decisions or commitments relevant to this briefing.
2–4 short paragraphs or bulleted context points.

[ANALYSIS]
Key findings that support the recommendation.
Data, evidence, and expert assessment.
Use subheadings if multiple threads of analysis are present.

[RECOMMENDATION]
What you recommend. One clear statement.
Why this is the right choice (summary of analysis).
What alternatives were considered and why they were not selected.

[RISKS AND MITIGATION]
2–4 specific risks associated with the recommendation.
For each risk: likelihood, potential impact, and mitigation approach.

[NEXT STEPS]
What must happen next, in sequence.
Who owns each action.
Key decision required: by whom, by when.
```

## Copy-paste prompt

```
You are an expert in executive-level communication. Your task is to write a formal Executive Briefing from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Group CTO and board members", "CFO and Audit Committee", "Investor relations committee"]
PURPOSE: [PURPOSE — e.g. "Recommend cloud migration strategy", "Brief the board on a security incident and remediation plan", "Summarise the case for a new supplier contract"]
CONTEXT: [CONTEXT — e.g. "Current data centre lease expires in 36 months; infrastructure cannot scale for projected growth; three cloud migration options have been assessed"]
INPUT: [INPUT — paste all supporting data, analysis notes, and your recommendation here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Reader approves the recommended approach and authorises the budget and team to proceed"]
TONE: [TONE — e.g. "Formal and authoritative", "Clear and direct", "Measured and balanced — acknowledging risk without being alarmist"]
LENGTH: [LENGTH — e.g. "2–3 pages (700–1,000 words)"]
FORMAT: [FORMAT — headed sections: Executive Summary, Background, Analysis, Recommendation, Risks and Mitigation, Next Steps]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not reveal the vendor name until contracts are signed", "Budget figures must align with those approved in the January board pack", "Suitable for sharing with the external auditor"]

INSTRUCTIONS:
1. Begin with a one-paragraph Executive Summary (maximum 100 words) that contains: the core issue, the recommendation, and the primary rationale. A reader who reads only this paragraph must understand everything essential.
2. Write a Background section that explains why this matter exists and why it is relevant now. Use plain, formal prose. No jargon.
3. Write an Analysis section with key findings. Support every finding with a number, fact, or named source from [INPUT]. Do not assert without evidence.
4. State the Recommendation explicitly and in full. Explain briefly why alternatives were not selected.
5. Identify 2–4 specific, named risks. For each risk, provide: what could go wrong, how likely it is, what the impact would be, and how you will mitigate it.
6. Close with a clear Next Steps section: sequenced actions, owners, and the specific decision required from the reader.
7. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
8. Preserve all factual claims exactly as provided in [INPUT]. Flag assumptions with "(assumed)" in parentheses.
9. Use formal language. No hedging ("seems to," "could potentially," "might"). Use "will," "is," "has."
10. Total length must not exceed [LENGTH].

Output the Executive Briefing only. No preamble, no commentary.
```

## Output format

The finished document is a formal written paper, typically two to four pages long. It is suitable for printing as a board-meeting attachment or circulating as a PDF. It contains:

- **Title block**: Document title, date, author(s), and document status (Draft / Final)
- **Executive Summary**: One paragraph, maximum 100 words, standing alone as a complete summary
- **Background**: 2–4 paragraphs of plain formal prose
- **Analysis**: 3–5 headed sub-sections or a structured set of bulleted findings with brief prose commentary
- **Recommendation**: One clear sentence, then 1–2 paragraphs of justification
- **Risks and Mitigation**: A table or 2–4 headed paragraphs covering each risk
- **Next Steps**: A numbered list with owners and dates

The document uses formal headings in bold or title case, no informal language, and consistent formatting throughout. It does not contain appendices (these belong in a board paper); any supporting data is summarised in the Analysis section.

## Example

**Cloud Infrastructure Migration — Executive Briefing**
*Prepared for: Group CTO | Date: 14 May 2026 | Status: Final*

---

**Executive Summary**
We recommend migrating our on-premises infrastructure to AWS over an 18-month programme beginning Q3 2026. This reduces capital expenditure by £2.1M over five years, improves system reliability from 98.5% to a contracted 99.9%, and positions us to scale without further capital investment. The primary risk is project delivery complexity; we will mitigate this through a phased migration and an external delivery partner.

**Background**
Our current data centre lease expires in March 2029. Renewal would cost £3.6M over five years, plus ongoing maintenance estimated at £480,000 annually. The infrastructure was designed for a headcount of 200 and cannot efficiently support the projected growth to 600 staff and 5× data volume by 2028. Three incidents in the past 12 months — each attributable to hardware capacity constraints — resulted in 14 hours of unplanned downtime and an estimated £340,000 in lost productivity. The board's digital strategy, approved in January, commits to cloud-first architecture for all new workloads; this programme completes that transition for existing workloads.

**Analysis**

*Financial impact*
AWS total cost of ownership over five years is £4.2M, compared with £5.6M for data centre renewal (including maintenance). This represents a net saving of £1.4M. Capital expenditure of £600,000 (migration and tooling) replaces ongoing lease commitments, improving cash flow profile. Gross margin on hosting is projected to improve by 2.1 percentage points as AWS reserved instances replace per-server provisioning costs.

*Operational and reliability impact*
AWS guarantees 99.9% uptime across its multi-availability-zone architecture, compared with our current measured reliability of 98.5% (132 hours of downtime annually). Three AWS regions have been assessed; EU-West-2 (London) meets our data residency requirements under UK GDPR. Our current SOC 2 Type I report will need updating; AWS infrastructure is natively SOC 2 Type II certified, which streamlines our audit obligations.

*Strategic alignment*
Our four largest enterprise clients have indicated preference for cloud-hosted SaaS in their 2026 procurement questionnaires. Two clients have contractual review clauses triggered if we remain on non-certified infrastructure beyond 2027. Migrating to AWS resolves both contractual risks and enables the API gateway architecture required for our 2027 product roadmap.

**Recommendation**
Approve the 18-month AWS migration programme with a total budget of £600,000, beginning Q3 2026. A data-centre-renewal approach was assessed but rejected on cost, scalability, and client contractual grounds. A hybrid approach (partial cloud) was assessed but adds operational complexity without proportionate cost benefit and delays full compliance.

**Risks and Mitigation**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Programme delay beyond 18 months | Medium | High — lease negotiation required | Engage AWS Partner Network delivery firm; appoint dedicated internal programme lead |
| Data migration error or loss | Low | Critical | Phased migration with six-month parallel operation; full data validation at each phase gate |
| Staff capability gap on AWS tooling | Medium | Medium | Training programme for infrastructure team begins Q2; two AWS-certified engineers to be hired |
| Cost overrun | Low | Medium | Fixed-price contract with delivery partner; contingency of £60,000 (10%) held in reserve |

**Next Steps**
1. CTO approves programme and budget allocation — by 28 May 2026
2. Procurement issues RFP to three AWS Partner Network firms — by 4 June 2026
3. Delivery partner selected and contracted — by 25 June 2026
4. Programme kick-off and Phase 1 planning begins — 1 July 2026

**Decision required**: CTO approval of £600,000 capital budget and programme mandate by 28 May 2026.

## Quality checklist

- [ ] Executive summary is one paragraph, under 100 words, and fully standalone
- [ ] Recommendation is explicit — one clear sentence stating what is recommended
- [ ] Every claim in the Analysis section is supported by a number, fact, or named source
- [ ] Risks are specific and named — not generic ("project risk")
- [ ] Each risk has a mitigation approach stated
- [ ] Next steps are numbered, sequenced, and have named owners and dates
- [ ] Decision required is explicitly stated with a deadline
- [ ] Tone is formal and confident — no hedging language
- [ ] British English used throughout
- [ ] Length is within 2–4 pages

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Recommendation buried in the body | Executives must read to find the ask | State recommendation in the Executive Summary |
| Vague or generic risks | Reader cannot assess true exposure | Name specific risks: "data migration error" not "implementation risk" |
| Missing data to support claims | Recommendation lacks credibility | Every finding needs a number, fact, or attribution |
| Too much detail too early | Violates executive briefing format; loses the reader | Lead with summary; depth goes in the Analysis section |
| No decision deadline | Urgency is unclear; decision may not happen | Always state who must decide and by when |
| Passive analysis language | Sounds uncertain | Use strong verbs: "This will reduce costs by £X" not "Costs could potentially be reduced" |

---

See [prompt-templates/executive-summary-prompts.md](../prompt-templates/executive-summary-prompts.md) for more templates.
