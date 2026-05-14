---
title: Academic Style
category: Specialist
best_for: Research papers, academic journal submissions, theses, and scholarly analyses where the primary obligation is to advance knowledge through a well-argued, evidence-based thesis. Also suitable for policy papers requiring academic rigour and peer-review-standard documentation of methodology and sources.
not_good_for: Business communication where the audience values conclusions over methodology (use Consulting Style); general audiences who need accessible language (use Plain English); quick updates or status reports (use Smart Brevity).
default_tone: Formal and scholarly. Objective and rigorous. Third-person throughout.
typical_length: 3,000–12,000 words for a journal article; 15,000–80,000 words for a thesis; 500–2,000 words for a literature review section
aliases: [Scholarly Writing, Research Paper, Academic Paper]
---

# Academic Style

## What this style is

Academic style is the formal written register of scholarly inquiry. It communicates research findings, theoretical arguments, and critical analysis to a community of peers who share domain expertise and who will evaluate the work against standards of rigour, evidence, and methodological transparency. Unlike professional writing styles that value brevity and conclusions, academic writing values completeness: the reader must be able to assess not just what the author found, but how they found it, what prior work they are building on, and what the limits of their findings are.

Academic writing has a distinctive epistemic character: it distinguishes between established knowledge, contested claims, and the author's own contribution. It uses citations not merely as attribution but as a way of positioning the argument within an existing scholarly conversation. It acknowledges limitations not as weakness but as intellectual honesty.

**Core principle**: Thesis → Argument → Evidence → Conclusion. Every claim is grounded in evidence or clearly identified as the author's analytical inference. Limitations and counterarguments are engaged, not ignored.

## When to use it

- Research papers and theses submitted to universities and academic institutions
- Journal article submissions in peer-reviewed publications
- Systematic literature reviews or scoping reviews
- Scholarly analysis of policy, technology, or social phenomena
- Evidence-based policy papers requiring academic rigour and full citation
- Conference papers in academic or research settings
- Contributions to edited volumes and academic collections

## When not to use it

- Business communication where methodology is less important than conclusions — use [Consulting Style](consulting-style.md) instead
- General audiences requiring accessible language — use [Plain English](plain-english.md) instead
- Quick updates or executive summaries — use [Smart Brevity](axios-smart-brevity.md) instead
- Teaching or onboarding content — use [Socratic Explainer](socratic-explainer.md) or [Tutorial Style](tutorial-style.md) instead

## Core structure

```
[TITLE AND ABSTRACT]
Title: descriptive and specific.
Abstract: 150–300 words summarising research question, methodology,
key findings, and contribution. Standalone — readable without the paper.

[INTRODUCTION]
Background context establishing the research area.
Identification of the gap in existing knowledge.
Clear statement of the research question or hypothesis.
Scope: what this paper does and does not address.
Paper structure overview (for longer papers).

[LITERATURE REVIEW]
Critical survey of prior work relevant to the research question.
Organised thematically or chronologically.
Identifies agreements, debates, and gaps in the existing literature.
Positions this paper's contribution relative to prior work.

[METHODOLOGY]
How the research was conducted.
Research design (quantitative, qualitative, mixed methods).
Data sources, sampling, and data collection methods.
Analytical methods or interpretive framework.
Ethical considerations (where applicable).
Limitations of the methodology.

[FINDINGS OR ARGUMENT]
For empirical papers: what the data shows, organised by theme or research question.
For theoretical papers: the analytical argument, built step by step.
Evidence is presented and interpreted — not merely described.
Counterarguments and alternative interpretations are engaged.

[DISCUSSION]
Implications of the findings for the field.
Relationship of findings to prior literature.
Theoretical or practical contributions.
Limitations of the study and their implications.
Directions for future research.

[CONCLUSION]
Restatement of the research question.
Summary of key findings and their significance.
The paper's contribution to knowledge.
Closing reflection (optional — depends on field conventions).

[REFERENCES]
All sources cited in the text.
Consistent citation style throughout (APA, Harvard, Chicago, Vancouver, etc.).
No sources in references not cited in text; no citations without references.
```

## Copy-paste prompt

```
You are an expert academic writer. Your task is to write an academic paper section from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Peer reviewers and readers of the Journal of Information Systems Security", "Examiners of a PhD thesis in organisational behaviour", "Participants at the IEEE CloudCom conference"]
PURPOSE: [PURPOSE — e.g. "Write the Introduction and Literature Review sections of a paper on zero-trust architecture adoption in financial services", "Draft the Methodology section for a mixed-methods study of DevOps adoption in regulated industries", "Write an abstract for a paper on the relationship between IAM maturity and security incident frequency"]
CONTEXT: [CONTEXT — e.g. "The paper builds on Smith et al. (2023) and challenges their finding that perimeter security is sufficient for SME environments; our dataset covers 47 UK financial services firms over three years"]
INPUT: [INPUT — paste your research notes, data, prior literature references, and any draft sections here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "A complete Introduction section that positions the research gap clearly and states the research question unambiguously, suitable for submission to a peer-reviewed journal"]
TONE: [TONE — e.g. "Formal academic register", "Objective and scholarly", "Third-person throughout — no first-person singular except where journal style requires"]
LENGTH: [LENGTH — e.g. "Introduction: 600–900 words; Literature Review: 1,500–2,500 words"]
FORMAT: [FORMAT — e.g. "APA 7th edition citations and references", "Headed sections with H2 subheadings for major themes in the Literature Review"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not cite sources not provided in [INPUT]", "Follow the journal's style guide — maximum three levels of heading", "Do not make claims beyond what [INPUT] supports"]

INSTRUCTIONS:
1. Write a clear thesis statement or research question in the Introduction. It must be specific, significant, and answerable.
2. In the Literature Review, organise prior work thematically. Synthesise sources — do not merely summarise each in turn. Show where scholars agree, where they disagree, and what gap remains.
3. Distinguish between what prior literature has established, what is contested, and what is this paper's own analytical contribution. Use appropriate hedging for contested claims: "it has been argued that" not "it is the case that."
4. Use appropriate academic hedging language: "the findings suggest," "the evidence indicates," "this analysis contends." Do not over-claim certainty.
5. Use the citation style specified in [FORMAT]. Every factual claim must be cited unless it is the author's own original analysis clearly identified as such.
6. Acknowledge limitations in the methodology, data, or scope of argument. Do not omit limitations.
7. Use British English throughout (colour, organisation, analyse, favour, practise, etc.). Note: academic British English uses "-ise" not "-ize" (analyse, organise, conceptualise) unless journal style requires "-ize."
8. Preserve all citations, data points, and factual claims exactly as provided in [INPUT]. Do not fabricate citations or alter figures.
9. Flag any claim in [INPUT] that appears to be an assumption or interpretation rather than established evidence — mark with "(author's inference)" or appropriate hedging.
10. Total length must not exceed [LENGTH].

Output the academic text only. No preamble, no commentary.
```

## Output format

An academic paper is a formal document published in a journal, conference proceedings, or institutional repository. It follows field-specific conventions (STEM papers differ significantly from humanities papers in structure and citation style). However, the general format contains:

- **Title**: Specific and informative — not a topic label but an analytical claim or descriptive research statement
- **Abstract**: 150–300 words, structured (Background, Methods, Results, Conclusion) or narrative depending on field
- **Headed sections**: Introduction, Literature Review, Methodology, Findings, Discussion, Conclusion, References
- **In-text citations**: Consistent with the specified style (APA: Author, Year; Chicago: footnote; Vancouver: numbered)
- **Reference list**: Complete, consistently formatted, alphabetical (APA/Harvard) or numbered (Vancouver/IEEE)
- **Tables and figures**: Numbered sequentially, with title above (APA convention), sources cited below
- **Word count**: Strictly within the journal or institution's specified limits

Academic papers do not use bullet points in the main body (tables and figures are acceptable). They use paragraph-structured prose throughout, with clearly headed sections.

## Example

**Architectural Documentation Quality and Onboarding Velocity in Distributed Engineering Teams: A Mixed-Methods Study**

**Abstract**

The relationship between software architectural documentation quality and the speed at which new engineers reach full productivity — "onboarding velocity" — has received limited empirical attention despite its operational and economic significance for technology organisations. This paper presents findings from a mixed-methods study of 23 distributed engineering teams across six UK financial services firms (n = 312 engineers) over an 18-month period. Using a validated architectural documentation quality index (ADQI) and a self-reported productivity timeline instrument, we find a statistically significant negative correlation between ADQI score and onboarding time (r = −0.61, p < 0.001): teams with higher-quality architectural documentation achieved full onboarding velocity 34% faster on average than teams with low documentation quality. Qualitative interview data from 47 participants provides contextual depth, revealing that documentation quality is most impactful during the first 90 days of tenure and that the effect is amplified in systems with high component interdependency. These findings contribute to the growing body of evidence that documentation is a strategic investment in team capacity, not merely a compliance activity, and have implications for engineering leadership practice and platform team prioritisation.

**1. Introduction**

The productivity of newly onboarded software engineers — measured as the time between joining a team and reaching full independent contribution — represents a significant organisational cost that is poorly understood in empirical terms. Industry surveys consistently identify onboarding velocity as a top engineering productivity concern (Forsgren et al., 2021; DORA, 2024), yet the interventions most likely to accelerate it remain contested. Mentorship programmes, pair programming, structured curricula, and tooling investment have each been proposed and studied, but the role of architectural documentation — the written record of how a software system is structured and why — has received disproportionately little scholarly attention.

This gap is consequential. Architectural documentation differs from other onboarding interventions in that it is a persistent artefact: unlike a mentor, it is available at any hour; unlike a curriculum, it is specific to the actual system the engineer will work on. If documentation quality is a significant predictor of onboarding velocity, then investment in architectural documentation should be prioritised alongside — or perhaps ahead of — other more visible interventions.

This paper investigates the following research question: *To what extent does architectural documentation quality predict onboarding velocity in distributed engineering teams, and what mechanisms explain this relationship?*

We operationalise "architectural documentation quality" using the Architectural Documentation Quality Index (ADQI) (Kruchten et al., 2019), a validated instrument assessing coverage, currency, accessibility, and precision of system documentation. We operationalise "onboarding velocity" as the number of days from contract start date to the first independently delivered and peer-reviewed feature, as self-reported and validated against version-control records.

The study makes three contributions to the literature. First, it provides the first large-sample empirical test of the documentation-onboarding relationship in financial services engineering. Second, it identifies the 90-day window as the critical period during which documentation quality has its greatest impact. Third, it provides qualitative context for the mechanisms through which documentation affects productivity, informing practical guidance for engineering leaders.

**2. Literature Review**

*2.1 Onboarding velocity in software engineering*

The concept of onboarding velocity — the rate at which a new engineer reaches full productivity — has been studied primarily in the context of developer experience (DevEx) research. Forsgren et al. (2021) identify time-to-first-commit as a leading indicator of onboarding success, finding that teams with structured onboarding programmes achieve their first commit 40% faster than teams without. However, their study does not control for documentation quality, and their measure of "first commit" may not capture meaningful productivity.

Sedano et al. (2017) identify "incomplete knowledge" as one of nine categories of software waste, finding that knowledge gaps — including gaps in architectural understanding — account for approximately 17% of engineering time lost to rework and re-explanation. This study provides theoretical grounding for the expectation that documentation quality would reduce knowledge gaps and therefore improve onboarding outcomes, but it does not test this relationship directly.

*2.2 Architectural documentation and system comprehension*

The relationship between documentation and system comprehension has been studied extensively in the software maintenance literature. Lethbridge et al. (2003) find that up-to-date documentation significantly reduces the time required for engineers to locate relevant code components, with effects largest for engineers who did not participate in the original system design — a condition directly applicable to onboarding. More recently, Aghajani et al. (2020) conducted a large-scale analysis of 878 open-source projects, finding that documentation quality (measured by coverage and recency) is positively associated with contributor retention, suggesting that documentation affects the experience of engineers who are new to a codebase.

However, the existing literature has two significant limitations relevant to this study. First, most prior work examines open-source contribution, where engineers self-select projects partly based on documentation quality; this selection effect does not apply in employed settings where engineers are assigned to systems. Second, prior work focuses on documentation volume and coverage rather than the multi-dimensional quality constructs captured by the ADQI. This study addresses both limitations.

[Paper continues with Methodology, Findings, Discussion, and Conclusion sections...]

## Quality checklist

- [ ] Thesis or research question is explicitly and precisely stated in the Introduction
- [ ] Literature Review synthesises prior work — not a series of summaries
- [ ] Methodology is complete enough for replication — no missing steps
- [ ] Every factual claim is cited or clearly identified as the author's inference
- [ ] Appropriate hedging language is used for contested or uncertain claims
- [ ] Limitations are acknowledged in Methodology and/or Discussion
- [ ] Discussion engages with prior literature — not just restates findings
- [ ] Conclusion restates the research question and its contribution to knowledge
- [ ] Reference list is complete, consistently formatted, and alphabetical
- [ ] British English used throughout

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Vague or unanswerable thesis | Argument has no clear destination | State thesis explicitly: "This paper argues that…" or "The research question is…" |
| Literature Review as a series of summaries | Fails to show the scholarly conversation or identify the gap | Organise thematically; show where authors agree, disagree, and what remains unresolved |
| Unsupported claims | Lacks credibility; fails peer review | Cite every non-original factual claim |
| Over-claiming certainty | Overstates findings; invites justified criticism | Use academic hedging: "the findings suggest," "the data indicate" |
| Missing limitations | Appears uncritical; undermines credibility | Acknowledge scope, data, and methodological limitations explicitly |
| No contribution statement | Reader unclear why the paper matters | State explicitly what this paper adds to the existing literature |

---

See [reference/recommended-resources.md](../reference/recommended-resources.md) for citation format guidance.
