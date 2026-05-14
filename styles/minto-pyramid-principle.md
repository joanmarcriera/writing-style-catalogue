---
title: Minto Pyramid Principle
category: Strategic
aliases: [Pyramid Principle, Logical Argument]
---

# Minto Pyramid Principle

## What This Style Is

The Minto Pyramid puts your conclusion or recommendation at the top, then supports it with grouped ideas below. Each layer is built on logical reasoning, making recommendations or arguments clear and persuasive.

**Core principle**: Conclusion first, then grouped supporting arguments, then detailed evidence.

## When to Use It

- Strategic recommendations
- Problem-solving memos
- Persuasive documents (moderate to high stakes)
- Consultant-style analyses
- Decision papers
- Proposals requiring logic and evidence
- Change management communications

## When NOT to Use It

- Quick updates (use Smart Brevity or BLUF)
- Complex formal documentation (use Board Paper)
- Technical specifications (use Technical Documentation)
- Teaching (use Socratic or Tutorial)
- Narrative content (use Narrative Storytelling)

## Core Structure

```
[PYRAMID TIP – THE CONCLUSION]
Your main recommendation or conclusion.

[SECOND LEVEL – 3 SUPPORTING ARGUMENTS]
Argument 1
Argument 2
Argument 3

[THIRD LEVEL – EVIDENCE FOR EACH ARGUMENT]
Evidence supporting Argument 1
Evidence supporting Argument 2
Evidence supporting Argument 3

[CLOSING]
Implications or next steps.
```

## Copy-Paste Prompt Template

```
You are a Minto Pyramid expert. Structure this recommendation into Pyramid format:

SITUATION:
[Describe the problem or decision point]

YOUR RECOMMENDATION:
[What you recommend]

WHY YOU RECOMMEND IT:
[List 3 main reasons why this is the right choice]

EVIDENCE FOR EACH REASON:
[For each reason, provide 2–3 supporting facts or analyses]

INSTRUCTIONS:
1. Start with the recommendation as your pyramid tip
2. List 3 grouped reasons supporting it
3. Back each reason with evidence (facts, data, analysis)
4. Total length: 1000–1500 words
5. Use a logical, evidence-based structure
6. End with implications or next steps

Format:

**RECOMMENDATION**
[State your recommendation clearly]

**Why This Is the Right Choice**

**Reason 1: [Clear category]**
[2–3 sentences of explanation and evidence]

**Reason 2: [Clear category]**
[2–3 sentences of explanation and evidence]

**Reason 3: [Clear category]**
[2–3 sentences of explanation and evidence]

**Implications**
[What this means; next steps]

Output only the document. No preamble.
```

## Short Example (Condensed)

**RECOMMENDATION**
We should migrate our payment processing to CloudPay, replacing our current legacy system.

**Why This Is the Right Choice**

**Reason 1: Operational Risk**
Our current system fails 2–3 times per month, causing payment delays and customer frustration. CloudPay has 99.95% uptime SLA and handles 3x our current transaction volume with zero incidents. This eliminates our largest operational vulnerability.

**Reason 2: Financial Impact**
Migration costs are £180k. Operating savings are £120k/year (reduced maintenance, licensing, and incident response). Payback period is 18 months. Beyond that, we save £120k annually in perpetuity.

**Reason 3: Strategic Flexibility**
Our current vendor is sunsetting support in 24 months. CloudPay integrates with 40+ payment methods and supports expansion to new markets. This keeps us ahead of vendor lockout and market change.

**Implications**
The 6-month migration is complex but low-risk. We should start Q2 to complete before vendor sunsetting. Recommend appointing a dedicated migration lead.

## Quality Checklist

- [ ] Recommendation is clear and stated upfront
- [ ] Exactly 3 supporting reasons (not 2, not 4)
- [ ] Each reason has a clear label/category
- [ ] Evidence backs each reason (data, analysis, facts)
- [ ] Logic flows from reason to evidence
- [ ] No hedging or weak language
- [ ] Conclusion/implications are explicit
- [ ] Reader can skim by reading headers only

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| More than 3 reasons | Reader loses track of logic | Group arguments under 3 main categories |
| Recommendation buried | Reader has to dig for the point | State it first, then explain |
| Evidence not grouped | Argument structure collapses | Each reason gets its own evidence section |
| Weak evidence | Argument is unconvincing | Use data, facts, or analysis; avoid opinions |
| No clear labels for reasons | Reader doesn't follow structure | Label each reason: "Risk," "Cost," "Capability" |
| Too detailed too soon | Loses the pyramid structure | Keep each level summary; nest detail below |
| No implications | Reader unsure what happens next | Always end with "what this means" |

---

See [prompt-templates/strategy-prompts.md](../prompt-templates/strategy-prompts.md) for strategic recommendation templates.

See [examples/minto-recommendation.md](../examples/minto-recommendation.md) for a complete example.
