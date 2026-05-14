---
title: Consulting Style
category: Strategic
aliases: [McKinsey Style, Structured Analysis]
---

# Consulting Style

## What This Style Is

A structured, issue-driven approach to analysis. Frames problems clearly, examines multiple perspectives, and recommends specific actions. Used extensively in strategy consulting.

**Core principle**: Issue → Analysis → Recommendation → Implementation.

## When to Use It

- Strategic analyses and recommendations
- Complex problem-solving
- Major business decisions
- Change management plans
- Market or competitive analysis
- Operational improvement recommendations

## When NOT to Use It

- Quick updates (use Smart Brevity)
- Teaching (use Socratic)
- Formal board documents (use Board Paper)
- Simple decisions (use BLUF)

## Core Structure

```
[ISSUE/OPPORTUNITY]
The specific problem or question to solve.

[FINDINGS]
Analysis of the issue. Multiple perspectives examined.

[IMPLICATIONS]
What these findings mean.

[RECOMMENDATION]
Specific action or strategy.

[IMPLEMENTATION APPROACH]
How to execute; timeline; resources needed.

[SUCCESS METRICS]
How you'll measure if this worked.
```

## Copy-Paste Prompt Template

```
You are a strategy consultant. Write a consulting-style analysis:

ISSUE:
[The problem or question to solve]

CONTEXT:
[Background and why this matters]

ANALYSIS AREAS:
[3–5 key areas you should examine]

FINDINGS:
[For each area: what did you find?]

OPTIONS CONSIDERED:
[What alternatives were evaluated?]

RECOMMENDATION:
[What you recommend and why]

TIMELINE:
[How long to implement?]

INSTRUCTIONS:
1. Frame the issue as a specific question
2. Present findings objectively
3. Show that alternatives were considered
4. Recommend one specific path
5. Provide implementation approach
6. Include success metrics
7. Length: 1500–2500 words

Output a consulting-style analysis. No preamble.
```

## Short Example

**Improving Engineering Velocity – Strategic Analysis**

**Issue**
Engineering velocity has declined 23% over 18 months despite headcount increases. We need to understand root causes and recommend interventions.

**Findings**

*Process and Tools (Analysis)*
• Build time increased from 2 minutes to 5 minutes; infrastructure bottleneck identified
• Testing harness is manual; 40% of sprint time spent on test execution and remediation
• Code review cycle averages 48 hours; waiting time is primary blocker

*Knowledge and Staffing (Analysis)*
• Junior engineers (5 of 8 recent hires) require 2–3 months onboarding; productivity ramp is 6 months
• Architectural knowledge is siloed; document coverage is 30% of codebase

*Workload (Analysis)*
• Incident response pulls engineers off planned work 8 hours/week on average
• Technical debt backlog has grown to 120 story points

**Implications**
Our infrastructure and process have not scaled with headcount. New hires cannot reach productivity quickly, and veteran engineers spend time on process overhead instead of value creation.

**Recommendation**

1. **Invest in infrastructure** (Q2 2026; 6 weeks)
   - Parallel build pipelines: Reduce build time to 90 seconds
   - Automated testing framework: Eliminate manual test execution

2. **Restructure onboarding** (Q2 2026 onwards)
   - Mentorship pairs (1 senior + 1 junior); 12-week structured curriculum
   - Architectural documentation sprint; target 70% coverage

3. **Reduce incident load** (Q3 2026)
   - On-call rotation (1 engineer per week); escalation path
   - Post-incident review process; root cause analysis for all incidents > P2

**Success Metrics**
• Velocity: Return to 35 story points/sprint within 6 months
• Build time: < 90 seconds (from 5 minutes)
• Junior engineer productivity: 80% of team average by month 6 (from 40%)
• Incident MTTR: < 1 hour for P1; < 4 hours for P2

## Quality Checklist

- [ ] Issue is framed as a specific question
- [ ] Findings are objective and data-driven
- [ ] Analysis covers multiple perspectives
- [ ] Recommendation is specific and actionable
- [ ] Implementation approach includes timeline and resources
- [ ] Success metrics are measurable
- [ ] Length appropriate (1500–2500 words)

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Vague issue statement | Analysis meanders | Frame as specific question: "Why did velocity decline?" |
| Biased findings | Analysis is not credible | Show multiple perspectives; acknowledge trade-offs |
| Weak recommendation | Reader unsure what to do | Be specific: "Launch X by date Y with £Z budget" |
| No implementation path | Recommendation can't be executed | Include timeline, resources, and sequencing |
| No success metrics | Can't tell if recommendation worked | Define measurable outcomes upfront |

---

See [prompt-templates/strategy-prompts.md](../prompt-templates/strategy-prompts.md) for strategy templates.
