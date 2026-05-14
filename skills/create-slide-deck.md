---
title: Create Slide Deck
skill_type: Document generation
output: A complete slide-by-slide outline with speaker notes, visual specifications, and narrative flow, ready to build in PowerPoint, Keynote, or Google Slides
tools_needed: LLM (Claude/ChatGPT/Gemini), Presentation software (PowerPoint / Keynote / Google Slides / Pitch)
difficulty: Medium
---

# Skill: Create Slide Deck

## What this skill does

Produces a complete slide deck outline — with content, speaker notes, and visual specifications — for any presentation context, from executive briefings to investor pitches to team all-hands. The LLM generates a slide-by-slide plan with headline text, supporting bullet points, visual descriptions, and timing guidance. You then build the actual slides in your tool of choice. The prompt also produces a separate speaker notes script, so the presenter can deliver with or without notes on screen.

## When to use it

- Preparing a board or executive presentation where narrative flow and brevity matter more than slide count
- Building an investor pitch that must convey a market opportunity, product, and funding ask in under 20 minutes
- Creating a team briefing on a major change (cloud migration, IAM programme, org restructure)
- Designing training or onboarding slides that need to work for both live delivery and self-paced viewing
- Producing a conference or external speaking slot where visual impact is as important as content

## Inputs required

- Presentation topic and specific goal (what must the audience do or believe after?)
- Target audience: technical/non-technical, internal/external, seniority level
- Duration and approximate slide count
- 3–5 key messages that must land
- Any data, case studies, or evidence to include
- Branding constraints (colours, fonts, logo placement)
- Whether slides need to stand alone without a presenter (e.g. emailed after meeting)

## Fast workflow: topic to slide deck

1. **Write the decision or audience outcome first**. A deck without a clear ask becomes a report in landscape format.
2. **Choose the narrative pattern**: problem → evidence → recommendation → action for most executive decks; SCQA for strategy decks; What / So What / Now What for updates.
3. **Generate an outline before slide copy** using [Presentation Prompts](../prompt-templates/presentation-prompts.md).
4. **Rewrite every slide title as a message**, not a topic label.
5. **Move detail into speaker notes**. Slides should carry the point; notes carry the nuance.
6. **Review with the [Slide Deck Rubric](../rubrics/slide-deck-rubric.md)** before building in PowerPoint, Keynote, or Google Slides.

## Copy-paste prompt

```
You are a presentation strategist and designer. Create a complete slide deck outline for the following presentation.

AUDIENCE: [e.g. Board of directors / Investor panel / Engineering team / New joiners]
PURPOSE: [What the audience must do, decide, or believe after seeing this]
CONTEXT: [Why this presentation is happening now; what the audience already knows]
INPUT: [Key messages, data points, case studies, or raw notes to draw from]
DESIRED_OUTCOME: [Specific decision, action, or change in belief you need]
TONE: [e.g. Authoritative and concise / Energetic and persuasive / Calm and informative]
LENGTH: [Total duration in minutes; target slide count]
FORMAT: Slide-by-slide outline. For each slide include: (1) slide title — 6 words maximum; (2) 2–3 bullet points of content — each under 12 words; (3) speaker notes — 3–5 sentences the presenter would say; (4) visual specification — describe the chart, diagram, image, or icon to use.
CONSTRAINTS: Use British English. No slide should try to say more than one thing. Avoid bullet-point dumps — each slide must have a clear single message. Output only the slide outline and speaker notes; no preamble.

NARRATIVE STRUCTURE:
- Open with the problem or opportunity (slides 1–3)
- Build context and evidence (slides 4–7)
- Present the solution or recommendation (slides 8–10)
- Address risks or objections (slide 11)
- Close with a clear call to action (final main slide)
- Put Q&A, contact details, and objection-handling material in appendix slides if needed

Adjust slide count proportionally if the stated duration is shorter or longer than 25 minutes.
```

## Suggested output structure

- **Slide 1**: Title — presentation name, presenter, date, organisation logo
- **Slide 2**: Agenda — 4–5 section titles; sets expectations
- **Slides 3–4**: Problem or opportunity — what is broken, missing, or changing?
- **Slides 5–6**: Context and evidence — data, market trends, current state costs
- **Slides 7–9**: Solution — what you are proposing and why it is the right choice
- **Slide 10**: Options considered — shows rigour; explains what was ruled out and why
- **Slide 11**: Risks and mitigations — credibility builder; do not omit
- **Slide 12**: Implementation or roadmap — phases, timeline, owners
- **Slide 13**: Call to action — one specific ask; decision, approval, or next step
- **Appendix slides**: Q&A prompts, contact details, financial backup, objection-handling detail

## Design and layout considerations

- **One idea per slide**: If you need a sub-point, create a new slide — do not add a fourth bullet
- **Headline as message**: The slide title should state the conclusion, not the topic. "Cloud costs fell 34%" beats "Cloud cost analysis"
- **Visual over text**: Replace any bullet that can be shown as a chart, diagram, or image with a visual plus a single caption
- **Colour hierarchy**: Use brand primary colour for section headers; secondary colour for data highlights; neutral grey for supporting content
- **Font size minimums**: Body text ≥ 24pt; slide titles ≥ 36pt; never use less than 18pt for any on-screen text
- **Slide density**: Aim for 40% white space on every slide — content that breathes is easier to absorb
- **Animation**: Use sparingly; build-in animations for data reveals only; avoid decorative transitions

### Prompt for generating the slide artefact

```
You are a presentation designer. Based on the outline below, produce slide content formatted for direct entry into PowerPoint or Google Slides.

For each slide output exactly:
SLIDE [NUMBER]
TITLE: [6 words maximum]
CONTENT: [2–3 bullets, each under 12 words]
VISUAL: [One-line description: chart type, what it shows, suggested colours]
SPEAKER NOTES: [What the presenter says — 60–90 words]
---

Apply these design rules:
- Title font: [Brand font], bold, 36pt, [accent colour]
- Body font: [Brand font], regular, 24pt, dark grey #333333
- Background: white or very light grey #F5F5F5
- Accent colour: [e.g. #1A2B5A navy]
- Each slide: one visual element + max 3 text bullets

[Paste slide outline here]
```

### Common conversion and rendering mistakes

- **Exporting from Google Slides to PowerPoint**: Fonts not embedded in PPTX cause text reflow — embed fonts or export as PDF for final distribution
- **Aspect ratio mismatch**: Build in 16:9 (1920×1080) for screen; switch to 4:3 only if projecting in older venues — never mix ratios in one deck
- **Image resolution**: Low-resolution images (under 150 DPI) pixelate on large screens — source images at 300 DPI minimum or use SVG
- **Colour shift on projector**: Projectors desaturate colours — test your brand colours under projection light; darken background colours by 15–20% in the projected version
- **Speaker notes not printing**: In PowerPoint, always use File → Print → Notes pages to verify notes export correctly before handing to presenter

## Quality controls

- [ ] Every slide has exactly one headline message stated as a conclusion
- [ ] Slide count fits the stated time allocation (roughly 1.5–2 minutes per slide)
- [ ] Visual specification is specific enough for a designer to act on without further input
- [ ] Speaker notes are full sentences, not bullet fragments — presenter can read them cold
- [ ] The narrative arc is clear: problem → evidence → solution → action
- [ ] Call-to-action slide states one specific ask, not three
- [ ] Deck can be understood by someone reading the slide titles alone (no speaker present)
- [ ] All data claims reference a source or are clearly labelled as estimates

## Common failure modes

- **Too many bullets per slide**: More than three bullets per slide fragments attention — cut or split the slide
- **Weak slide titles**: "Overview" or "Background" conveys nothing — rewrite every title as a message sentence
- **Missing visual specs**: The outline says "add a chart" without specifying axes, data series, or chart type — the designer cannot proceed without this detail
- **No escalation path for objections**: If the audience raises a challenge (cost, risk, timeline), the presenter has no rebuttal slides — build an appendix with 3–4 objection-handling slides
- **Narrative doesn't flow**: Jumping from problem to solution without evidence loses the audience — always show the data before the recommendation

## Example request

"Create a 20-slide deck for a 30-minute board presentation on our proposed IAM (Identity and Access Management) programme. The board needs to approve a £1.4M budget. Key messages: our current access controls are non-compliant with ISO 27001; three incidents last year were access-related; the programme will close compliance gaps, reduce incident risk, and reduce provisioning time from 5 days to 4 hours. Tone: formal and measured. Include risk and cost slides. British English throughout."
