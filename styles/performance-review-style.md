---
title: Performance Review Style
category: Personal
best_for: Formal written assessments of an employee's performance during a defined review period — annual reviews, mid-year reviews, probationary assessments, and promotion evaluations. Effective for 360-degree feedback documentation and performance improvement plan frameworks where a balanced, evidence-based written record is required.
not_good_for: Ongoing informal feedback conversations (use direct conversation, not written review format); disciplinary proceedings where legal and HR guidance governs the process; quick notes or team announcements (use Smart Brevity); situations requiring immediate corrective action (seek HR and legal advice first).
default_tone: Constructive and specific. Balanced and growth-focused. Evidence-based, not impressionistic.
typical_length: 500–1,000 words for a complete review; individual feedback sections 100–250 words each
aliases: [Employee Feedback, Performance Assessment, Appraisal]
---

# Performance Review Style

## What this style is

A performance review is a structured written assessment of an employee's contributions, strengths, and development areas during a defined review period. Its purpose is to give the employee a clear, honest, and specific picture of their performance — what they have done well, where they have room to grow, and what they should focus on in the period ahead. A good performance review contains no surprises: it captures what has already been discussed in ongoing conversations, not news delivered for the first time.

The most important quality of a performance review is specificity. Vague feedback — "a strong communicator" or "needs to improve leadership" — is useless. Useful feedback names specific situations, describes specific behaviours, and where possible quantifies the impact. The reader should be able to act on the feedback immediately without needing to ask what it means.

**Core principle**: Specific → Constructive → Growth-focused. Every point is backed by a specific example and tied to a growth opportunity or recognition of genuine impact.

## When to use it

- Annual or mid-year performance reviews covering a defined period
- 360-degree feedback synthesis for compilation into a written assessment
- Promotion or progression evaluations submitted to HR or a review panel
- Probationary period assessments with clear pass/fail criteria
- Performance improvement plan (PIP) documentation frameworks
- Talent development conversations formalised in writing for an HR record

## When not to use it

- Disciplinary proceedings — these require HR and legal processes, not a performance review format
- Quick informal feedback — use direct conversation; this format implies a formal review process
- Public recognition or team announcements — use [Smart Brevity](axios-smart-brevity.md) or [Narrative Storytelling](narrative-storytelling.md) instead
- Situations where corrective action is required immediately — seek HR advice before writing anything

## Core structure

```
[EMPLOYEE AND REVIEW DETAILS]
Employee name, role, team, and manager.
Review period (start date to end date).
Reviewer name and date of review.
Overall rating (if applicable to the organisation's framework).

[OVERALL ASSESSMENT]
2–4 sentences capturing the review period as a whole.
The headline view of the employee's contribution and trajectory.
Set the context: significant projects, team changes, or external challenges.

[STRENGTHS]
2–4 specific strengths, each with a named example.
Structure: Strength → Example → Impact.
Business impact stated where possible (metric, outcome, or stakeholder feedback).

[DEVELOPMENT AREAS]
1–3 specific development areas with constructive framing.
Structure: Behaviour or gap → Example → Suggested approach.
Not a list of failures — areas where growth would increase the employee's effectiveness.

[ACHIEVEMENTS THIS PERIOD]
Key accomplishments during the review period.
Bulleted for clarity.
Quantified where possible.

[DEVELOPMENT PLAN]
Specific, time-bound goals for the next review period.
For each goal: what success looks like and how the organisation will support it.
2–4 goals — not a wish list.

[OVERALL RATING] (if applicable)
Clear rating statement using the organisation's rating framework.
Brief rationale.

[NEXT STEPS]
Follow-up meeting date.
Invitation for the employee to share their perspective.
Any HR process steps that follow.
```

## Copy-paste prompt

```
You are an experienced HR professional and manager. Your task is to write a performance review from the following brief.

AUDIENCE: [AUDIENCE — e.g. "The employee (Senior Engineer, Identity Platform team)", "The employee and their HR file", "The employee, their manager, and the promotion review panel"]
PURPOSE: [PURPOSE — e.g. "Annual performance review for a senior software engineer", "Mid-year review for a cloud architect in their first year in role", "Probationary assessment at the six-month mark for a junior security analyst"]
CONTEXT: [CONTEXT — e.g. "Review period January–December 2025; employee led the IAM migration project; team grew from 4 to 8 during the period; company went through a restructure in Q3"]
INPUT: [INPUT — paste all specific examples of strong performance, development areas, key achievements, feedback from stakeholders, and your assessment of the employee's contribution here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Employee has a clear, specific, balanced view of their performance and knows exactly what to focus on in 2026", "Promotion panel has sufficient evidence to assess the employee against the Senior Principal Engineer criteria"]
TONE: [TONE — e.g. "Constructive and growth-focused — honest but supportive", "Balanced — neither entirely positive nor focused on gaps; approximately 60% strengths and 40% development", "Evidence-based — every point backed by a specific example"]
LENGTH: [LENGTH — e.g. "700–900 words for a complete annual review", "400–600 words for a mid-year check-in"]
FORMAT: [FORMAT — headed sections: Overall Assessment, Strengths, Development Areas, Achievements, Development Plan, Next Steps]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not include any details about the disciplinary process — that is a separate HR matter", "The employee has requested that feedback from specific named colleagues not be attributed — use 'stakeholder feedback indicates' not individual names", "Rating scale: Exceeds Expectations / Meets Expectations / Partially Meets Expectations / Does Not Meet Expectations"]

INSTRUCTIONS:
1. Write an Overall Assessment of 2–4 sentences that captures the review period honestly. Include context (significant projects, changes, challenges) that affected performance.
2. Write 2–4 Strengths sections. For each: name the strength, provide a specific named example from [INPUT], and state the impact. "Strong communicator" is not sufficient — "Led the cross-team IAM migration kick-off meeting; aligned four teams to a shared delivery timeline in a single session" is.
3. Write 1–3 Development Areas. Frame constructively: not "Alex is poor at planning" but "Project estimation would benefit from additional structure — the payment migration ran short on contingency twice due to integration testing time not being included in estimates."
4. List key achievements as a bulleted list. Quantify where possible — include story points, percentages, team sizes, or outcomes.
5. Write a Development Plan with 2–4 specific, time-bound goals. For each goal, state what success looks like and what support the organisation will provide.
6. Invite the employee's perspective explicitly in the Next Steps section.
7. Use British English throughout (colour, organisation, licence, favour, etc.).
8. Preserve all specific examples exactly as provided in [INPUT]. Do not invent examples or outcomes not provided.
9. Distinguish observed facts from inferences. If you are making an inference about the employee's motivation or intent, note it as such.
10. Total length must not exceed [LENGTH].

Output the performance review only. No preamble, no commentary.
```

## Output format

A performance review is a formal HR document, typically stored in an HR system or personnel file and shared as a PDF or Word document. It contains:

- **Header**: Employee name, role, review period, reviewer, date
- **Overall Assessment**: Short prose paragraph (2–4 sentences)
- **Strengths**: 2–4 sub-sections, each with a heading (the strength) and 2–4 sentences of evidence
- **Development Areas**: 1–3 sub-sections, each with a heading and 2–4 sentences of constructive guidance
- **Achievements**: Bulleted list (4–8 items), quantified where possible
- **Development Plan**: 2–4 goals in a table or short list, each with success criteria and support offered
- **Rating**: Clear statement of rating (if applicable) with brief rationale
- **Next Steps**: 1–2 sentences on follow-up and invitation to respond

Total word count: 500–1,000 words for a full annual review. The review should not exceed two pages — length is not a proxy for quality.

## Example

**Performance Review: Aisha Mensah — Senior Cloud Architect**
*Review period: 1 January – 31 December 2025*
*Reviewer: James Whitfield, Director of Infrastructure | Date: 14 May 2026*

---

**Overall Assessment**

Aisha has had a genuinely strong year — her technical contributions were high-quality, and her leadership on the AWS migration programme elevated the whole team's delivery. She joined a team that was technically strong but lacked architectural coordination; by year end she had established herself as the person others sought out for design decisions. The one area where investment would significantly increase her impact is structured communication for non-technical stakeholders — something she has already identified and begun working on.

**Strengths**

*Technical Architecture*
Aisha led the architectural design for the AWS landing zone, resolving a six-month-old disagreement between infrastructure and security teams by designing a hub-and-spoke network model that satisfied both teams' requirements. The resulting design has been adopted as the standard for all new cloud workloads. Her architectural decision records (ADRs) are consistently cited as the clearest in the repository by engineers onboarding to the codebase — a practical mark of quality.

*Mentorship and Knowledge Transfer*
Aisha took on the development of two junior cloud engineers without being asked. Both have passed their AWS Solutions Architect Associate certification this year. One has since independently designed and delivered a secondary VPC peering project — work that would have required senior involvement six months ago. This is a direct result of Aisha's coaching approach.

*Cross-functional Collaboration*
During the Q3 2025 restructure, Aisha maintained project continuity across two team mergers without requiring escalation. She proactively built working relationships with the new security team, creating a shared access control review process that removed a four-week delay from the migration timeline.

**Development Areas**

*Executive-level Communication*
Aisha's technical communication within the engineering team is excellent. In two Steering Committee presentations during H1 2025, however, the level of technical detail was above what the audience needed to make the decision being asked of them, and the recommendation was not stated clearly until the Q&A. This is a solvable gap: with preparation on structuring for executive audiences, Aisha's substantive knowledge would land much more effectively at that level.

*Proactive Risk Escalation*
On two occasions during the migration programme, Aisha identified a technical risk but raised it informally rather than through the programme's risk register, which delayed resolution. The programme risk register exists precisely to give risks visibility and ownership. Raising risks through the formal channel — while also flagging them informally — would improve the team's overall risk management.

**Key Achievements — 2025**

- Led architectural design and delivery of the AWS landing zone serving 47 production applications
- Authored 12 Architecture Decision Records adopted as team standards
- Mentored 2 junior engineers to AWS certification; both now delivering independently
- Removed 4-week delay from migration timeline through cross-functional access control process
- Completed AWS Solutions Architect Professional certification (March 2025)
- Designed hub-and-spoke network model resolving 6-month team disagreement

**Development Plan — 2026**

| Goal | Success Looks Like | Support |
|------|-------------------|---------|
| Deliver one Steering Committee presentation with a clear executive recommendation | Chair provides positive feedback; decision is made without technical clarification Q&A | Manager to review slides and structure with Aisha before each presentation |
| Formally raise all technical risks through the programme risk register within 24 hours of identification | Zero informal-only risk escalations in H1 2026 | Team lead to review risk register with Aisha weekly for Q1 |
| Lead one cross-team technical initiative as programme lead (not technical contributor) | Initiative delivered on time with positive feedback from stakeholders | Manager to identify a suitable initiative by end of Q1 and agree scope with Aisha |

**Rating**: Exceeds Expectations

Aisha consistently delivered above the requirements of her role in technical quality and team impact. The development areas identified are growth opportunities for a Principal Engineer trajectory, not gaps that diminish the overall assessment.

**Next Steps**

A follow-up conversation is scheduled for 22 May to discuss this review and Aisha's goals and perspectives on the year. Aisha, please review this ahead of that conversation and note any points where your experience differs from the assessment above — your perspective is important and will be included in the HR record.

---

*Note: Approach sensitive feedback with care. Consult HR and legal for any sensitive matters.*

## Quality checklist

- [ ] Every strength is backed by a named, specific example from the review period
- [ ] Impact of each strength is stated — not just the behaviour
- [ ] Development areas are framed constructively — growth opportunity, not failure catalogue
- [ ] Development areas are specific enough to act on without asking "what do you mean?"
- [ ] Achievements are quantified where possible
- [ ] Development Plan goals are time-bound with clear success criteria
- [ ] Employee is explicitly invited to share their perspective
- [ ] Balance of strengths and development areas is approximately 60/40
- [ ] British English used throughout
- [ ] Review contains no surprises — everything has been discussed in ongoing conversations

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Vague feedback ("great communicator," "needs more initiative") | Employee cannot act on it | Use specific examples: "In the March Steering Committee, Aisha… " |
| All strengths, no development areas | Lacks credibility; reads as a reference letter | Include specific, growth-oriented development areas |
| All development areas, no strengths | Demoralising; employee cannot see what they are doing right | Balance approximately 60% strengths, 40% development |
| Surprise feedback | Undermines trust; a review should confirm, not reveal | Performance conversations must happen throughout the year |
| Development plan with no support | Employee feels alone in their growth | State what the organisation will do to support each goal |
| Too long | Employee overwhelmed; key points buried | Keep to two pages; stay focused on the most significant observations |

---

*Note: Approach sensitive feedback with care. Consult HR and legal for any sensitive matters.*

See [prompt-templates/pdf-document-prompts.md](../prompt-templates/pdf-document-prompts.md) for formatting a review as a PDF.
