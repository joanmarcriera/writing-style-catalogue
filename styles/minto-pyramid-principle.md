---
title: Minto Pyramid Principle
category: Formal
best_for: Strategic recommendations, business cases, and decision papers where the reader needs to be persuaded by structured logic. Ideal when you have a clear recommendation and need to present it to a sceptical or time-pressured senior audience who will scrutinise the reasoning.
not_good_for: Quick informational updates where no argument is needed (use Smart Brevity or BLUF); highly emotional or cultural communications where logical structure feels cold (use Narrative Storytelling).
default_tone: Formal and analytical. Confident and evidence-led.
typical_length: 800–2,000 words (document); 5–10 slides (presentation)
aliases: [Pyramid Principle, Logical Argument, SCQ Structure]
---

# Minto Pyramid Principle

## What this style is

The Minto Pyramid Principle, developed by Barbara Minto at McKinsey, organises writing around a simple structural rule: the conclusion or recommendation goes at the very top, followed by a small number of grouped supporting arguments, each of which is then backed by evidence. The structure resembles a pyramid — broad base of evidence, narrowing upward to a single point.

This inverts the way most people naturally write, which is to present background and evidence first and work toward a conclusion. The pyramid puts the conclusion first precisely because readers in professional settings already know the topic and need the answer, not the journey to it. Context and evidence exist only to justify the conclusion, not to build it from scratch.

**Core principle**: Conclusion first, then grouped supporting arguments, then detailed evidence. Each layer must logically support the layer above it.

## When to use it

- Strategic recommendations to senior leadership or the board
- Business case documents requiring logical persuasion
- Problem-solving memos where the cause-and-recommendation structure matters
- Consultant-style analyses of complex issues with multiple variables
- Decision papers where the reader will challenge the reasoning
- Proposals for significant investment, change, or strategic direction
- Change management documents justifying a new approach

## When not to use it

- Quick operational updates where no argument is needed — use [Smart Brevity](axios-smart-brevity.md) or [BLUF](bluf-bottom-line-up-front.md) instead
- Formal board documents requiring full options analysis — use [Board Paper Style](board-paper-style.md) instead
- Technical specifications — use [Technical Documentation](technical-documentation.md) instead
- Teaching or learning content — use [Socratic Explainer](socratic-explainer.md) or [Tutorial Style](tutorial-style.md) instead
- Narrative communications where tone and emotion matter more than logic — use [Narrative Storytelling](narrative-storytelling.md) instead

## Core structure

```
[PYRAMID TIP — THE RECOMMENDATION OR CONCLUSION]
One clear statement of your recommendation or conclusion.
Must be complete and standalone.

[SITUATION] (optional scene-setter)
Brief context: what is happening that makes this relevant now?

[COMPLICATION] (optional)
What has changed or gone wrong that makes the recommendation necessary?

[QUESTION] (optional)
The question your recommendation answers.

[SECOND LEVEL — EXACTLY 3 SUPPORTING ARGUMENTS]
Argument 1: [Clear label — e.g. "Financial Impact"]
Argument 2: [Clear label — e.g. "Operational Risk"]
Argument 3: [Clear label — e.g. "Strategic Fit"]

[THIRD LEVEL — EVIDENCE FOR EACH ARGUMENT]
Evidence 1a, 1b, 1c — supporting Argument 1
Evidence 2a, 2b, 2c — supporting Argument 2
Evidence 3a, 3b, 3c — supporting Argument 3

[CLOSING — IMPLICATIONS AND NEXT STEPS]
What this recommendation means in practice.
What must happen next and when.
```

## Copy-paste prompt

```
You are an expert in the Minto Pyramid Principle. Your task is to structure the following recommendation into strict pyramid format.

AUDIENCE: [AUDIENCE — e.g. "CTO and senior engineering leadership", "board of directors", "steering committee"]
PURPOSE: [PURPOSE — e.g. "Recommend adoption of zero-trust network architecture", "Justify cloud migration investment", "Propose supplier consolidation strategy"]
CONTEXT: [CONTEXT — e.g. "Following two security incidents in Q1; board has requested a review of network access controls"]
INPUT: [INPUT — paste your raw analysis, notes, facts, and recommendation here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Reader agrees with the recommendation and approves the proposed next steps"]
TONE: [TONE — e.g. "Formal and analytical", "Direct and evidence-led", "Professional and persuasive"]
LENGTH: [LENGTH — e.g. "1,000–1,500 words" or "8–10 slides"]
FORMAT: [FORMAT — e.g. "Written document with headed sections" or "Slide deck with one point per slide"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Budget figures must not exceed what is in [INPUT]", "Do not reference the Q1 incidents by name", "Must be suitable for sharing with the vendor"]

INSTRUCTIONS:
1. Begin with the recommendation or conclusion as the pyramid tip. State it in one clear, complete sentence.
2. Identify exactly three grouped supporting arguments. Label each clearly (e.g. "Financial Impact," "Operational Risk," "Strategic Alignment"). Do not use two arguments or four — group ideas to reach exactly three.
3. Under each argument, provide 2–3 pieces of specific evidence drawn from [INPUT]. Evidence must be data, facts, or analysis — not opinion or assertion.
4. Where [INPUT] provides quantitative data, use it exactly. Do not invent numbers.
5. Where you are uncertain whether something is a confirmed fact or an assumption, label it "(assumed)."
6. Close with a section on implications and next steps: what the reader should do, in what sequence, and by when.
7. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
8. Use formal, professional language. No hedging ("might," "perhaps," "could potentially"). Use "will," "is," "has."
9. Total length must not exceed [LENGTH].

Output only the pyramid document. No preamble, no commentary.
```

## Output format

The finished document is typically 800–2,000 words for a written paper, or 8–12 slides for a presentation. It contains the following headed sections:

- **Recommendation**: The pyramid tip — one bold declarative sentence
- **Reason 1 / [Label]**: 2–3 sentences of explanation plus supporting evidence
- **Reason 2 / [Label]**: 2–3 sentences of explanation plus supporting evidence
- **Reason 3 / [Label]**: 2–3 sentences of explanation plus supporting evidence
- **Implications**: 1–2 paragraphs on what this means and what must happen next

Headers are essential — a reader scanning only the headers must be able to follow the entire argument. The recommendation and each reason label must be informative, not generic (e.g. "Operational risk is unacceptable without this change" rather than "Risk").

## Example

**RECOMMENDATION**
We should adopt a zero-trust network architecture across all production systems, replacing perimeter-based controls by Q4 2026, to eliminate our most significant identity and access risk before our ISO 27001 re-certification audit.

**Why this is the right decision**

**Reason 1: Our current perimeter model cannot contain insider and credential-based threats**
Two of the three security incidents in Q1 2026 involved valid credentials used from inside the network perimeter — a scenario perimeter firewalls are designed to trust, not block. In both cases, lateral movement was undetected for more than 72 hours. Zero-trust architecture authenticates every request regardless of network origin, limiting lateral movement to the scope of a single compromised credential rather than the entire network segment. Internal incident analysis identified credential misuse as the common failure mode; this is precisely the attack vector that perimeter controls cannot address.

**Reason 2: Zero-trust adoption is required to maintain ISO 27001 certification and meet client contractual obligations**
Our external auditor flagged network segmentation and least-privilege access as a priority control gap in the December 2025 audit report. Three enterprise clients have contractual SLAs requiring ISO 27001 certification; losing certification would trigger contract review clauses with two of them. Additionally, our largest client's security questionnaire now explicitly asks whether we operate zero-trust controls — a question we currently cannot answer affirmatively. Adopting zero-trust resolves the audit gap, protects certification, and satisfies client requirements simultaneously.

**Reason 3: The total cost of adoption is lower than the projected cost of a significant breach**
External implementation of a zero-trust model using our existing Microsoft Entra ID and Defender for Cloud tooling is estimated at £180,000 over 12 months (assumed — based on three vendor quotes). Our cyber insurance broker has indicated that a network-wide credential breach would likely exceed £1.2M in incident response, regulatory notification, and reputational costs based on comparable incidents. Additionally, insurance premiums are projected to fall by 12–15% upon certification of zero-trust controls, saving approximately £22,000 annually. The payback period is under 18 months.

**Implications and next steps**
Approving this recommendation authorises the Identity and Security team to begin vendor selection in May, with a target go-live for Phase 1 (privileged access) in September 2026. A phased approach means production systems remain operational throughout. The ISO 27001 re-certification window opens in November 2026, giving sufficient time to demonstrate the control. The Steering Committee should appoint a programme sponsor at the June meeting and approve the £180,000 budget allocation from the IT capital reserve.

## Quality checklist

- [ ] Recommendation is stated as the very first line — clear, complete, and standalone
- [ ] Exactly three supporting reasons are used — not two, not four
- [ ] Each reason has a clear, informative label (not a generic word like "Risk")
- [ ] Each reason is backed by specific evidence from the source material
- [ ] Evidence is distinguished from assumptions — assumptions flagged explicitly
- [ ] Logic flows cleanly: reading only the headers tells the whole story
- [ ] Closing section covers implications and concrete next steps
- [ ] No hedging language; confident, formal register throughout
- [ ] British English used throughout
- [ ] Total length is within the stated range

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| More than three supporting reasons | Reader loses track of the logical structure | Group arguments under three clear categories |
| Recommendation buried | Reader has to read to find the point | State it first — always |
| Evidence not grouped by reason | Argument structure collapses; feels like a list | Each reason gets its own evidence section |
| Weak or vague evidence | Argument is unconvincing | Use data, facts, or analysis — not assertions |
| Non-informative reason labels | Reader cannot skim effectively | Label each reason with an outcome: "Cost savings justify investment" not "Cost" |
| Too much detail too early | Loses the pyramid structure | Keep each level summary; nest detail below |
| No implications section | Reader unsure what to do next | Always close with "what this means and what comes next" |

---

See [prompt-templates/strategy-prompts.md](../prompt-templates/strategy-prompts.md) for strategic recommendation templates.

See [examples/minto-recommendation.md](../examples/minto-recommendation.md) for a complete example.
