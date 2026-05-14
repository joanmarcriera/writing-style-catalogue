---
title: Consulting Style
category: Formal
best_for: Complex business problems requiring structured analysis across multiple perspectives, leading to a specific, evidence-backed recommendation. Ideal for strategic reviews, operational improvement programmes, market analyses, and major change decisions where showing rigour and examining alternatives builds credibility.
not_good_for: Quick updates or simple decisions where the answer is already clear (use BLUF or Smart Brevity); formal board governance documents requiring full options-analysis format (use Board Paper Style); educational content (use Socratic Explainer).
default_tone: Professional and analytical. Objective and structured. Confident but not dogmatic.
typical_length: 1,500–3,000 words (document); 15–25 slides (deck)
aliases: [McKinsey Style, Structured Analysis, Issue-Based Analysis]
---

# Consulting Style

## What this style is

Consulting style is a structured, issue-driven approach to analysis and recommendation. It originated in strategy consulting firms — McKinsey, BCG, Bain — and has become the standard format for serious business analysis across industries. It frames a problem as a specific question, examines it across multiple analytical dimensions, draws implications from each dimension, and then makes a single, specific recommendation with an implementation path.

What distinguishes consulting style from other analytical formats is its insistence on showing the work: the reader sees the issue statement, the analytical framework, the findings from each area, the implications, and only then the recommendation. This structure is persuasive because it demonstrates that the analysis was rigorous, that alternatives were considered, and that the recommendation is the logical output of the evidence — not a predetermined conclusion.

**Core principle**: Issue → Analysis → Implication → Recommendation → Implementation. Each layer earns the next.

## When to use it

- Strategic analyses and recommendations for senior leadership or external clients
- Complex problem-solving where root causes are not obvious
- Major business decisions requiring examination of multiple options
- Change management proposals requiring buy-in from a sceptical audience
- Market or competitive analyses informing strategic direction
- Operational improvement recommendations requiring sequenced action
- Programme business cases where rigour and alternatives must be visible

## When not to use it

- Quick operational updates — use [Smart Brevity](axios-smart-brevity.md) or [BLUF](bluf-bottom-line-up-front.md) instead
- Teaching or onboarding — use [Socratic Explainer](socratic-explainer.md) instead
- Formal board governance documents requiring full options analysis and approval format — use [Board Paper Style](board-paper-style.md) instead
- Simple, low-stakes decisions — use [BLUF](bluf-bottom-line-up-front.md) instead

## Core structure

```
[ISSUE STATEMENT]
The specific question or problem being analysed.
Framed as a question: "Why has X happened?" or "What should we do about Y?"

[SITUATION / CONTEXT]
Brief background. Why this matters now. What is at stake.

[ANALYTICAL FRAMEWORK]
The dimensions along which we will examine the issue.
Typically 3 lenses: e.g. Financial / Operational / Strategic.

[FINDINGS — ONE SECTION PER ANALYTICAL DIMENSION]
For each dimension:
- What the data or evidence shows
- What is working and what is not
- Quantified where possible

[IMPLICATIONS]
What the findings collectively mean.
What they reveal about root cause or the decision.

[OPTIONS CONSIDERED]
2–3 options that were evaluated.
Brief assessment of each: pros, cons, feasibility.

[RECOMMENDATION]
One specific, actionable recommendation.
Why this option, over the alternatives.

[IMPLEMENTATION APPROACH]
How to execute: phases, timeline, resources, owners.
Sequenced and realistic.

[SUCCESS METRICS]
How you will know whether the recommendation worked.
Measurable, time-bound indicators.
```

## Copy-paste prompt

```
You are a strategy consultant writing a structured analytical document. Your task is to produce a consulting-style analysis from the following brief.

AUDIENCE: [AUDIENCE — e.g. "CTO and engineering leadership team", "Board of directors", "Client executive sponsor and their direct reports"]
PURPOSE: [PURPOSE — e.g. "Analyse the root cause of a 23% decline in engineering velocity and recommend corrective action", "Assess whether to build or buy an identity management solution", "Recommend a supplier consolidation strategy"]
CONTEXT: [CONTEXT — e.g. "Velocity declined over 18 months despite 40% headcount growth; three prior interventions have not resolved it; board has asked for a structured root-cause analysis"]
INPUT: [INPUT — paste all data, findings, interview notes, metrics, and your initial hypotheses here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Leadership agrees on the root cause, endorses the recommended interventions, and assigns programme ownership"]
TONE: [TONE — e.g. "Professional and analytical", "Direct and evidence-led", "Objective — do not favour any particular outcome in the findings section"]
LENGTH: [LENGTH — e.g. "1,500–2,500 words" or "18–22 slides"]
FORMAT: [FORMAT — e.g. "Written document with headed sections" or "Consulting slide deck with one assertion per slide"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not reference individual engineers by name in the findings", "Budget figures must come from [INPUT] only — do not estimate", "Must be suitable for sharing externally with the client"]

INSTRUCTIONS:
1. Frame the issue as a specific question at the top of the document. The question must be answerable — not "what is happening" but "why has X happened" or "what should we do about Y."
2. Choose three analytical dimensions (lenses) appropriate to [PURPOSE]. Name each clearly (e.g. "Process and Tooling," "People and Knowledge," "Workload and Priorities").
3. For each analytical dimension, present findings objectively. Use specific data from [INPUT]. Do not assert without evidence. Where data is missing, note the gap explicitly.
4. Draw implications from the findings before presenting the recommendation. Implications explain what the findings mean, not what to do about them.
5. Present 2–3 options that were considered. Assess each honestly — including strengths of alternatives — before recommending one.
6. State the recommendation specifically: what, when, who, and how much (if known).
7. Provide a phased implementation approach with realistic timelines.
8. Define success metrics: specific, measurable, and time-bound.
9. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
10. Distinguish facts from assumptions throughout. Flag assumptions with "(assumed)" in parentheses.
11. Total length must not exceed [LENGTH].

Output the consulting analysis only. No preamble, no commentary.
```

## Output format

The finished document is typically 1,500–3,000 words for a written analysis, or 15–25 slides for a consulting deck. It is structured with clear headed sections, and in a slide format each slide carries one assertion as its title (not a neutral label like "Findings" but an active claim like "Build time has tripled in 18 months due to infrastructure under-investment").

The written format contains:
- **Issue statement**: One clear sentence or question
- **Context**: 1–2 short paragraphs
- **Findings** (per analytical dimension): Each dimension has a sub-heading, 2–4 bulleted findings, and a brief prose summary
- **Implications**: 1 paragraph drawing the findings together
- **Options considered**: Brief table or 3 short labelled paragraphs
- **Recommendation**: One sentence, then 1–2 paragraphs of justification
- **Implementation approach**: Numbered phases with timeline and owners
- **Success metrics**: 4–6 specific, measurable indicators with target values and dates

## Example

**Improving Engineering Velocity — Strategic Analysis**
*Prepared for: CTO | May 2026*

---

**Issue Statement**
Why has engineering velocity declined by 23% over 18 months despite a 40% increase in engineering headcount, and what specific interventions will return it to prior levels within two quarters?

**Context**
Engineering velocity — measured as story points delivered per sprint — has fallen from 45 to 35 points over the period January 2024 to May 2026. Over the same period, the team grew from 12 to 17 engineers. This is the inverse of the expected relationship: more engineers should deliver more, or at minimum maintain, velocity. Three prior interventions (a sprint retrospective programme, a new standup format, and a tooling refresh in Q3 2025) produced no measurable improvement. The CTO has requested a structured root-cause analysis.

**Analytical Findings**

*Process and Tooling*
Build time has increased from two minutes to five minutes and 40 seconds since the Q3 2025 infrastructure change — a 183% increase. This affects every engineer on every commit. The testing harness remains manual: engineers spend an average of seven hours per sprint executing regression tests that could be automated. Code review cycle time averages 51 hours from submission to merge; 38 of those hours are waiting time, not review time. Three engineers account for 70% of all code reviews, creating a bottleneck that cannot be resolved by adding more reviewers without structural change.

*People and Knowledge*
Five of the eight engineers hired in the past 12 months are in their first professional role. Internal data shows new engineers reach 80% of peer productivity in approximately seven months, but our current onboarding programme provides only four weeks of structured support. Architectural documentation covers 28% of the codebase; new engineers consistently cite documentation gaps as the primary reason they escalate or block. Two senior engineers with deep system knowledge have left in the past 18 months, and their knowledge was not captured before departure.

*Workload and Priorities*
Incident response consumes an average of 9.2 engineer-hours per week across the team — equivalent to two full sprint days of capacity per fortnight. The root cause of 60% of P2 and P3 incidents is the same legacy payment service, which has not been refactored. The technical debt backlog stands at 134 story points and is growing. Sprint planning data shows that technical debt and incident work displace planned feature work in six of the last eight sprints.

**Implications**
Velocity has not declined because of people quality or team size — it has declined because the systems around the engineers are broken. Build infrastructure slows every commit; manual testing multiplies review time; documentation gaps prevent new engineers from contributing independently; and a legacy service generates a disproportionate incident burden. Adding headcount without fixing these systems will continue to produce diminishing returns.

**Options Considered**

*Option A: Process intervention only (retrospectives, planning ceremonies, working agreements)*
Lowest cost; no infrastructure change required. However, this has already been attempted three times without effect. The root causes are structural, not behavioural. This option does not address any of the three identified causal factors.

*Option B: Targeted infrastructure and tooling investment (recommended)*
Address the three highest-leverage bottlenecks: build pipeline, test automation, and code-review workflow. Estimated cost: £85,000 in tooling and engineering time (assumed — based on comparable programmes). Expected velocity improvement: 8–12 story points per sprint within two quarters. This option is targeted, measurable, and addresses confirmed root causes.

*Option C: Full engineering transformation programme (process, tooling, culture, and recruitment)*
Comprehensive but slow and expensive. Timeline of 12–18 months; estimated cost £300,000+. Appropriate if this analysis had identified cultural or leadership failure as a root cause. It has not. This level of intervention is disproportionate to the identified problem.

**Recommendation**
Implement Option B: a targeted 16-week engineering infrastructure programme addressing build pipelines, test automation, and code-review process redesign in that priority sequence. Assign a dedicated engineering lead to own the programme. Do not launch a broader transformation until these foundational fixes are in place and measured.

**Implementation Approach**

Phase 1 — Build pipeline (Weeks 1–4): Implement parallel build execution; target build time under 90 seconds. Owner: Infrastructure team lead. Cost: £15,000 in tooling.

Phase 2 — Test automation (Weeks 5–10): Automate regression suite; target 90% automated coverage. Owner: QA lead working with three nominated engineers. Cost: £35,000 in engineering time.

Phase 3 — Code review redesign (Weeks 11–16): Implement review rotation; introduce automated pre-review checks; redistribute review ownership. Owner: Engineering manager. Cost: £12,000 in process design and tooling.

Legacy payment service refactoring: Separate 12-week stream running alongside Phases 2–3. Owner: Senior engineer (to be assigned). Budget: £23,000 (assumed).

**Success Metrics**

| Metric | Current | Target | Date |
|--------|---------|--------|------|
| Story points per sprint | 35 | 45 | 31 October 2026 |
| Build time | 5 min 40 sec | Under 90 sec | 30 June 2026 |
| Automated test coverage | 20% | 90% | 31 August 2026 |
| Code review cycle time | 51 hours | Under 24 hours | 31 August 2026 |
| Incident hours per week | 9.2 | Under 4 | 31 October 2026 |
| Junior engineer ramp time | 7 months | Under 4 months | 31 December 2026 |

## Quality checklist

- [ ] Issue is framed as a specific, answerable question — not a topic label
- [ ] Three analytical dimensions are named and examined with data
- [ ] Findings are objective — evidence from [INPUT], not assertion
- [ ] Implications draw the findings together before the recommendation is made
- [ ] At least two alternatives are assessed honestly, including their strengths
- [ ] Recommendation is specific: what, when, who, and cost
- [ ] Implementation is phased with realistic timelines and named owners
- [ ] Success metrics are specific, measurable, and time-bound
- [ ] British English used throughout
- [ ] Facts are distinguished from assumptions; assumptions flagged

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Vague issue statement | Analysis meanders; reader unsure what question is being answered | Frame as a specific answerable question: "Why did velocity decline?" not "Engineering productivity" |
| Biased findings | Analysis is not credible; reader suspects predetermined conclusion | Present data objectively; name contrary evidence; acknowledge what you do not know |
| Implications before findings | Inverts the logical flow | Show the findings first; draw implications from them |
| Weak or absent alternatives | Recommendation looks predetermined | Assess alternatives honestly, including their genuine strengths |
| Vague recommendation | Reader unsure what to actually do | Be specific: "Launch X by date Y with Z budget, owned by person A" |
| No implementation path | Recommendation cannot be executed | Include phases, timeline, resources, and sequencing |
| No success metrics | Cannot tell whether the recommendation worked | Define measurable outcomes with target values and dates |

---

See [prompt-templates/strategy-prompts.md](../prompt-templates/strategy-prompts.md) for strategy templates.
