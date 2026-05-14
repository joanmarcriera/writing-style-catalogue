---
title: Smart Brevity
category: Concise
aliases: [Axios Style, Smartsheet]
---

# Smart Brevity

## What This Style Is

Smart Brevity is a rapid, scannable format for busy executives. Every update follows a simple structure: headline, 3–5 key points, and essential context. No filler, no long paragraphs.

**Core principle**: Readers should understand the story in 30 seconds.

## When to Use It

- Executive status updates
- Company announcements
- Board or investor updates
- Quick pivots or alerts
- Meeting recaps
- Market news analysis
- Quarterly performance summaries

## When NOT to Use It

- Complex recommendations (use Minto Pyramid)
- Detailed technical specifications (use Technical Documentation)
- Teaching or education (use Socratic or Tutorial)
- Formal board documents requiring depth (use Board Paper)
- Legal or compliance documents

## Core Structure

```
[HEADLINE]
One clear, punchy sentence that captures the story.

[SUBHEADING] (optional)
One-line additional context.

[KEY POINT 1]
Specific fact or finding.

[KEY POINT 2]
Specific fact or finding.

[KEY POINT 3]
Specific fact or finding.

[CONTEXT] (optional)
Background or numbers supporting the points above.

[NEXT STEPS] (optional)
What happens next.
```

## Copy-Paste Prompt Template

```
You are a Smart Brevity expert. Your task is to convert the following information into a Smart Brevity update:

INFORMATION:
[Paste your source material here]

INSTRUCTIONS:
1. Write a single-sentence headline that captures the core story
2. Add 3–5 bullet points with the most important facts
3. Keep each bullet to one clear sentence
4. Include one paragraph of supporting context
5. Add a "Next Steps" line if action is required
6. Total length: 150–250 words

Format the output as:

**[HEADLINE]**

• Key point 1
• Key point 2
• Key point 3

**Context**
[One paragraph of supporting information]

**Next Steps**
[What comes next, if applicable]

Output only the Smart Brevity update. No preamble.
```

## Short Example

**Software Engineering Productivity Down 15% This Quarter**

• Development velocity declined as team shifted focus to technical debt reduction
• Refactoring legacy payment service removed 40% of critical bugs from production logs
• Expected return to normal velocity next quarter after debt elimination

**Context**
We identified cascading failures in our payment service that were causing 2–3 production incidents per week. The team pivoted from feature work to address root causes. This short-term trade-off prevents larger outages and reduces on-call burden. The refactoring is 80% complete.

**Next Steps**
Complete payment service rollout by end of Q2. Resume regular feature velocity thereafter.

## Quality Checklist

- [ ] Headline is a single, clear sentence
- [ ] Each bullet point is one sentence maximum
- [ ] No jargon or undefined acronyms
- [ ] Numbers and facts are included where needed
- [ ] Total length under 250 words
- [ ] Next steps are clear (if applicable)
- [ ] Can be understood in 30 seconds
- [ ] No unnecessary adverbs or qualifiers ("quite," "rather," "seems")

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Headline is vague | Reader doesn't know what the update is about | Make it specific: "Revenue up 23%" not "Good news on financials" |
| Too many bullet points | Overwhelms reader; defeats purpose | Keep to 3–5 maximum |
| Long paragraphs of context | Loses the scanning advantage | Break into short paragraphs or bullets |
| Weak verbs and hedging | Sounds uncertain | Use active voice: "We reduced costs" not "Costs were reduced" |
| Missing numbers | Vague impact | Always include metrics: "23% up" not "significant improvement" |
| No next steps | Reader doesn't know what to do | Always end with what comes next |
| Mixing multiple stories | Confuses narrative | One headline per update; use separate updates for multiple stories |

---

See [prompt-templates/executive-summary-prompts.md](../prompt-templates/executive-summary-prompts.md) for detailed prompt templates.

See [examples/smart-brevity-update.md](../examples/smart-brevity-update.md) for a complete example.
