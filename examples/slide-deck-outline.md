---
title: Slide Deck Outline — Cloud Exit Decision
category: Example
description: A worked executive-deck bundle with message titles, visual evidence, speaker caveats, and a precise ask.
bundle_id: slide-deck-outline
artefact: Executive slide deck outline
audience: Investment committee deciding whether to fund discovery
scenario: labelled-composite
style_path: styles/consulting-style.md
pattern_path: patterns/problem-impact-recommendation-next-steps.md
prompt_path: prompt-templates/presentation-prompts.md
skill_path: skills/create-slide-deck.md
rubric_path: rubrics/slide-deck-rubric.md
---

# Slide Deck Outline — Cloud Exit Decision

## Professional context

An investment committee needs a seven-slide decision narrative. The ask is permission to fund discovery, not approval of a migration programme that has not yet been costed.

## Source packet

```text
SCENARIO: Labelled composite.
DECISION: Approve £95,000 and eight weeks for discovery of data-centre exit options.
DRIVER: Primary co-location lease ends 30 September 2028; renewal terms are available only 12 months before expiry.
CURRENT COST: £1.26m per year excluding internal staff.
KNOWN CONDITION: 74 applications; 19 have unsupported operating-system components; dependency mapping incomplete for 28 applications.
OPTIONS FOR DISCOVERY: renew/modernise in place; hybrid migration; cloud-first migration.
NOT YET KNOWN: validated five-year cost, migration schedule, vendor selection, application-by-application disposition.
DISCOVERY OUTPUTS: dependency map, option cost model, delivery risk assessment, sourcing recommendation, decision paper.
SUCCESS GATE: committee receives an assured options case by 15 December 2026.
```

## Completed prompt

```text
You are an executive presentation strategist. Create a seven-slide outline for an investment committee deciding whether to approve £95,000 and eight weeks of discovery for data-centre exit options.

Use only the SOURCE PACKET. Do not invent savings, target architecture, vendor preference, migration duration, regulatory drivers, application disposition, or a preferred exit option. Do not turn the lease expiry into false immediate urgency. If the decision, amount, timebox, known estate facts, unknowns, or discovery outputs are missing, return MISSING INFORMATION rather than a deck.

For each slide provide: a message title that states the conclusion; two to four evidence bullets; a visual specification using only supplied data; and speaker notes that preserve caveats. Use this narrative: decision and timing; current estate; why evidence is insufficient; three options to investigate; discovery scope; governance and success gate; decision requested. Use British English. Keep slide text sparse and speaker notes substantive. The final slide must ask for discovery funding only. Output only the slide-by-slide outline.

Before finalising, apply the Slide Deck Rubric for decision clarity, narrative, evidence, visual usefulness, speaker notes, restraint, and final ask. Any invented business case is a failure.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Slide 1 — We need evidence before the 2028 lease deadline becomes a constraint
• Decision today: £95,000 for an eight-week discovery.
• The lease ends 30 September 2028; renewal terms arrive only 12 months before expiry.
Visual: horizontal timeline from discovery to lease expiry, with no invented programme dates.
Speaker note: This is not a request to approve migration or select cloud. It buys the evidence needed for that later decision.

Slide 3 — The current estate is not understood well enough to price an exit
• 74 applications.
• 19 contain unsupported operating-system components.
• Dependency mapping is incomplete for 28 applications.
Visual: three-number estate diagnostic, explicitly labelled as current known facts.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Decision clarity | 5 | Funding, duration, and discovery scope are explicit. | Pass |
| Narrative | 5 | Each slide advances the evidence-to-decision story. | Pass |
| Evidence | 5 | Visuals use only supplied dates, counts, and cost. | Pass |
| Speaker notes | 5 | Caveats prevent discovery from becoming programme approval. | Pass |
| Final ask | 5 | The ask is bounded to £95,000 and eight weeks. | Pass |

## Human review before use

- Finance must verify the current cost and discovery budget.
- Estate owners must reconcile application and dependency counts.
- The committee secretary must confirm decision wording and meeting time.
- A designer must check legibility and accessibility in the rendered deck.

## Reuse this bundle

- [Consulting Style](../styles/consulting-style.md)
- [Problem / Impact / Recommendation / Next Steps Pattern](../patterns/problem-impact-recommendation-next-steps.md)
- [Presentation Prompts](../prompt-templates/presentation-prompts.md)
- [Create Slide Deck Skill](../skills/create-slide-deck.md)
- [Slide Deck Rubric](../rubrics/slide-deck-rubric.md)
