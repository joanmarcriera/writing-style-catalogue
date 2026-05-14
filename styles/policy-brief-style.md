---
title: Policy Brief Style
category: Formal
best_for: Structured analysis of a policy question for decision-makers, stakeholders, or governing bodies — where the goal is to present evidence-based options objectively and recommend one. Ideal for board policy recommendations, regulatory impact assessments, government or institutional policy analysis, and research-informed advocacy.
not_good_for: Quick operational updates (use Smart Brevity); technical specifications (use Technical Documentation); narrative or opinion content (use Narrative Storytelling or Journalistic Style); formal legal documents (use Legal Professional Style).
default_tone: Objective and analytical. Evidence-based. Clear and direct in recommendation, neutral in options analysis.
typical_length: 800–2,000 words for an internal policy brief; 2,000–4,000 words for a government or institutional submission
aliases: [Policy Analysis, Evidence-Based Brief, Policy Recommendation]
---

# Policy Brief Style

## What this style is

A policy brief presents a defined policy question, examines the relevant evidence, outlines distinct policy options, analyses their trade-offs, and recommends one course of action. It is written for decision-makers who are accountable for the policy outcome but may not be specialists in the underlying domain. It is the standard format for evidence-based governance at institutional, board, and government level.

The policy brief differs from a consulting document in its relationship to evidence: where consulting style shows its analytical reasoning, policy brief style shows its evidentiary basis. Recommendations in a policy brief derive from research, data, and precedent — not primarily from analytical framework. The brief must also engage explicitly with affected stakeholders and with the distributional effects of each option: who gains, who loses, and what are the unintended consequences?

**Core principle**: Issue → Evidence → Options → Analysis → Recommendation. Each option is assessed on the same criteria. The recommendation follows from the analysis — not the other way around.

## When to use it

- Board or committee policy recommendations requiring an evidence-based options analysis
- Regulatory impact assessments submitted to government or regulators
- Government or NGO policy submissions and consultation responses
- Internal corporate policy changes requiring formal analysis and approval
- Research-informed advocacy to governing bodies or decision-makers
- Strategic policy guidance for senior leadership on a defined policy question
- IT, data, security, or operational policy proposals requiring board approval

## When not to use it

- Quick operational updates — use [Smart Brevity](axios-smart-brevity.md) instead
- Technical specifications — use [Technical Documentation](technical-documentation.md) instead
- Narrative or opinion content — use [Narrative Storytelling](narrative-storytelling.md) or [Journalistic Style](journalistic-style.md) instead
- Formal legal documents — use [Legal Professional Style](legal-professional-style.md) instead
- Strategic business case with single recommended option — use [Consulting Style](consulting-style.md) or [Minto Pyramid Principle](minto-pyramid-principle.md) instead

## Core structure

```
[TITLE]
"Policy Brief: [Policy Question]"
Specific enough to define the question being answered.

[EXECUTIVE SUMMARY — 1 PARAGRAPH]
The policy issue, the options considered, and the recommendation.
Suitable for a decision-maker who reads only this paragraph.

[ISSUE / PROBLEM STATEMENT]
The specific policy question being addressed.
Why this question matters now.
What is at stake if the decision is not made or is delayed.
Scope: what this brief does and does not address.

[CONTEXT AND BACKGROUND]
How the current situation arose.
Prior decisions or policies relevant to this question.
Regulatory or strategic context.
Any deadlines or external triggers.

[EVIDENCE BASE]
Research, data, comparable examples, and expert opinion informing the analysis.
Distinguish confirmed evidence from assumptions or projections.
Cite sources.
Acknowledge gaps in the evidence where they exist.

[POLICY OPTIONS]
2–3 distinct, viable options.
Each option presented using the same analytical structure:
- Description (what this option involves)
- Financial or resource implications
- Stakeholder impact (who gains, who loses)
- Key risks
- Precedent or comparator (has this been done elsewhere?)

[ANALYSIS OF OPTIONS]
Objective comparison of the options.
Use consistent criteria for all options.
Trade-offs made explicit.
Do not reveal the recommendation here — that comes next.

[RECOMMENDATION]
Which option is recommended and why.
The primary reasons the recommended option is preferred over alternatives.
Conditions on which the recommendation depends.

[IMPLEMENTATION]
How the recommended option would be implemented.
Key milestones and responsible parties.
Resource requirements.
Stakeholder engagement plan.

[MONITORING AND EVALUATION]
How success will be measured.
Indicators, review schedule, and escalation if indicators are not met.
```

## Copy-paste prompt

```
You are an expert policy analyst. Your task is to write a policy brief from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Board of Directors and the Audit Committee", "Secretary of State and departmental policy team", "Information Commissioner reviewing a data governance framework submission"]
PURPOSE: [PURPOSE — e.g. "Recommend a data retention policy for personally identifiable information held in cloud infrastructure", "Advise the board on three options for remote working policy following the end of the formal review period", "Provide evidence-based analysis of three approaches to IAM governance at enterprise scale"]
CONTEXT: [CONTEXT — e.g. "The current data retention practice is informal and inconsistent; the ICO has signalled that UK GDPR compliance requires a documented, enforced policy; three approaches have been assessed over a six-month internal review"]
INPUT: [INPUT — paste all evidence, data, stakeholder analysis, policy options, and your recommendation here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "The board approves the recommended option and mandates its implementation within 90 days", "The policy team has a complete, submission-ready brief for the regulatory consultation"]
TONE: [TONE — e.g. "Objective and analytical — neutral in options analysis, direct in recommendation", "Evidence-based and formal — appropriate for submission to a regulator", "Accessible to a non-specialist decision-maker — explain technical concepts in plain terms"]
LENGTH: [LENGTH — e.g. "1,200–1,800 words for a board brief", "2,500–3,500 words for a regulatory submission"]
FORMAT: [FORMAT — headed sections: Executive Summary, Issue, Context and Background, Evidence Base, Policy Options, Analysis, Recommendation, Implementation, Monitoring]
CONSTRAINTS: [CONSTRAINTS — e.g. "Options analysis must be strictly neutral — do not allow the framing to favour the recommended option before the Recommendation section", "All data cited must be from [INPUT] — do not introduce external sources not provided", "Must comply with the organisation's Evidence Standards Policy"]

INSTRUCTIONS:
1. Write a one-paragraph Executive Summary containing the policy issue, the options considered, and the recommendation. A decision-maker who reads only this paragraph must be fully informed.
2. Frame the Issue section as a specific policy question — not a topic label. "Should the organisation adopt a mandatory six-month data retention limit for Category A personal data?" not "Data Retention."
3. Present each policy option using a consistent structure: description, financial or resource implications, stakeholder impact, key risks, and precedent. Do not signal a preference in the options section.
4. In the Analysis section, compare options against the same criteria for all options. Make trade-offs explicit.
5. In the Recommendation section, state the recommended option and explain why. Explain why alternatives were not selected.
6. Include an Implementation section with realistic milestones, resource requirements, and stakeholder engagement.
7. Include monitoring indicators and a review schedule.
8. Distinguish confirmed evidence from assumptions, projections, or precedent from other contexts. Flag assumptions with "(assumed)" in parentheses.
9. Use British English throughout (colour, organisation, licence, favour, analyse, programme, etc.).
10. Total length must not exceed [LENGTH].

Output the policy brief only. No preamble, no commentary.
```

## Output format

A policy brief is a formal document suitable for a board pack, a government submission, or a committee meeting. It contains:

- **Title block**: Document title, author, commissioning body, date, and document status
- **Executive Summary**: One paragraph, self-contained, suitable for minutes
- **Headed sections**: Numbered (1. Issue, 2. Context, 3. Evidence, etc.)
- **Options table or structured paragraphs**: Consistent format for all options
- **Evidence citations**: Inline references (Author, Year) or footnotes depending on house style
- **Implementation table**: Phase, milestone, owner, date — tabular format for clarity

Length: 800–2,000 words for a board or internal brief; 2,000–4,000 words for a government or regulatory submission. The document should be printable as a standalone paper and readable without prior briefing.

## Example

**Policy Brief: Data Retention Standards for Personally Identifiable Information in Cloud Infrastructure**
*Prepared for: Board of Directors and Audit Committee | Author: Group Data Protection Officer | Date: 14 May 2026 | Status: Final*

---

**Executive Summary**

The Company's current data retention practice is informal and inconsistent across business units, creating material UK GDPR compliance exposure and increasing incident response complexity. Three approaches have been assessed: retaining current informal practices (Option A), adopting a documented policy without automated enforcement (Option B), and adopting a documented, automated retention policy with system-level controls (Option C). This brief recommends Option C: a documented, automated policy. This option addresses the compliance exposure, reduces the risk of a regulatory fine (up to £17.5M or 4% of global turnover under UK GDPR), and aligns with the ICO's published guidance on data minimisation. Implementation requires an estimated investment of £95,000 over 12 months and is achievable before the Company's next scheduled ICO audit.

---

**1. Issue**

Should the Company adopt a formally documented, automated data retention policy for personally identifiable information (PII) held in cloud infrastructure — and if so, which of the three assessed approaches should be implemented?

The question is urgent. The Information Commissioner's Office (ICO) has written to the Company twice in the past 18 months noting that the absence of a documented retention policy is inconsistent with the UK GDPR's data minimisation principle (Article 5(1)(e)). The Company's next ICO audit is scheduled for January 2027. Failure to demonstrate meaningful progress before that audit increases the risk of formal enforcement action.

---

**2. Context and Background**

The Company holds approximately 1.4 million PII records across 14 cloud-hosted systems, accumulated over 12 years of operation. There is no formal policy governing how long PII is retained or when it must be deleted. In practice, data is retained indefinitely unless manually deleted by a system administrator. A review completed in March 2026 found that 28% of PII records in the Company's CRM system relate to individuals who have had no contact with the Company for more than five years — a clear data minimisation risk.

The Board approved a data governance programme in September 2025 with a total budget of £250,000. This brief uses £95,000 of that budget (assumed — subject to Board approval).

---

**3. Evidence Base**

*Regulatory position*: ICO guidance on Article 5(1)(e) requires that personal data is "kept in a form which permits identification of data subjects for no longer than is necessary." The ICO's regulatory action record shows that absence of a retention policy has been cited in 34% of UK GDPR enforcement actions in 2024–2025 (ICO Annual Report 2025).

*Operational data*: Internal analysis of the Company's 14 cloud systems found that 340,000 PII records (24% of total) relate to individuals with no active relationship with the Company. Of these, 180,000 records are more than seven years old. Deleting these records would reduce cloud storage costs by an estimated £18,000 annually (assumed — based on current storage pricing).

*Comparator organisations*: Three comparable organisations in the Company's sector have implemented automated retention policies in the past two years. All three reported resolution of ICO concerns within 12 months of implementation. None reported significant operational disruption during implementation (assumed — based on industry peer group conversations).

---

**4. Policy Options**

**Option A: Retain current informal practices**

Retention decisions remain at the discretion of individual system administrators. No documented policy; no automated enforcement.

| Dimension | Assessment |
|-----------|-----------|
| Financial implications | No implementation cost; ongoing ICO fine risk up to £17.5M |
| Stakeholder impact | No operational change; continued risk for data subjects |
| Key risks | High — regulatory enforcement likely before January 2027 audit |
| Precedent | Not consistent with ICO guidance or sector practice |

**Option B: Documented policy, manual enforcement**

A formal policy is adopted and published; retention periods are defined; enforcement relies on manual review by system administrators.

| Dimension | Assessment |
|-----------|-----------|
| Financial implications | £25,000 (policy development and training) (assumed) |
| Stakeholder impact | Policy clarity for data subjects; enforcement consistency depends on admin diligence |
| Key risks | Medium — manual enforcement is prone to inconsistency; audit evidence weak |
| Precedent | Acceptable to ICO as an interim measure but insufficient long-term |

**Option C: Documented policy, automated enforcement (Recommended)**

A formal policy is adopted; automated retention rules are implemented in each cloud system; records are automatically deleted or pseudonymised at the end of the retention period.

| Dimension | Assessment |
|-----------|-----------|
| Financial implications | £95,000 over 12 months (assumed — tooling, implementation, and testing) |
| Stakeholder impact | Strongest protection for data subjects; consistent enforcement |
| Key risks | Low — automated enforcement removes human inconsistency; comprehensive audit trail |
| Precedent | ICO-preferred approach; consistent with sector best practice |

---

**5. Analysis**

Options A and B both carry regulatory exposure. Option A is indefensible before the January 2027 audit and risks the highest fine exposure. Option B reduces legal risk marginally but does not satisfy the ICO's preference for automated controls, and manual enforcement in an estate of 14 systems across multiple teams is unreliable in practice.

Option C is the only option that fully resolves the compliance exposure, generates a comprehensive audit trail, and aligns with the ICO's published guidance. The £95,000 cost is modest against the maximum fine exposure and is within the approved data governance programme budget. The operational disruption during implementation is manageable through a phased approach.

---

**6. Recommendation**

Option C is recommended: adoption of a documented, automated data retention policy covering all 14 cloud-hosted systems containing PII, with implementation completed by 31 October 2026.

Options A and B are rejected because neither resolves the compliance exposure within the available audit window, and neither provides the automated enforcement controls the ICO expects.

The recommendation is conditional on: (a) Board approval of the £95,000 budget allocation; (b) engagement of an external data engineering partner to implement automated controls (internal capacity is insufficient); (c) completion of staff training before automated deletion begins.

---

**7. Implementation**

| Phase | Activity | Owner | Completion |
|-------|----------|-------|-----------|
| 1 | Policy drafting and legal review | DPO + Legal | 30 June 2026 |
| 2 | Retention period definition per data category | DPO + Business leads | 31 July 2026 |
| 3 | Automated control implementation in all 14 systems | External partner + IT | 30 September 2026 |
| 4 | Staff training and communication | HR + DPO | 15 October 2026 |
| 5 | First automated deletion run and audit evidence pack | DPO + IT | 31 October 2026 |

---

**8. Monitoring and Evaluation**

Success indicator: Zero PII records retained beyond the defined retention period for their category — audited quarterly.

Review schedule: The DPO will report compliance metrics to the Audit Committee quarterly, beginning Q1 2027.

Escalation: If automated deletion fails for more than 1% of due records in any quarter, the DPO will escalate to the Board within 30 days with a remediation plan.

## Quality checklist

- [ ] Issue section frames a specific, answerable policy question — not a topic label
- [ ] Executive Summary is one paragraph and fully standalone
- [ ] Each option is presented using an identical analytical structure
- [ ] Options analysis does not signal preference — strictly neutral
- [ ] Recommendation section states which option and why, and why alternatives were rejected
- [ ] Evidence is cited and distinguished from assumptions
- [ ] Stakeholder impact is addressed for each option
- [ ] Implementation plan is phased with realistic milestones and named owners
- [ ] Monitoring and evaluation indicators are specific and measurable
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Issue framed as a topic, not a question | Analysis lacks a clear endpoint | Frame as a specific answerable question: "Should the Company adopt X?" |
| Options analysis favours the recommendation | Appears biased; damages credibility | Use identical analytical structure for all options; keep neutral language |
| Insufficient evidence base | Recommendations feel arbitrary | Cite data, research, and precedent; acknowledge gaps explicitly |
| Stakeholder impact missing | Policy appears disconnected from reality | Explain who gains, who loses, and what the unintended consequences are for each option |
| No implementation detail | Approved option cannot be executed | Include phases, milestones, owners, and resource requirements |
| No monitoring plan | No way to know if the policy worked | Define specific indicators and a review schedule |

---

See [prompt-templates/policy-prompts.md](../prompt-templates/policy-prompts.md) for more policy brief templates.
