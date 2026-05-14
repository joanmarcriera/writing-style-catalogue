---
title: Memo Prompts
category: Common
---

# Memo Prompts

## Purpose

Write clear, actionable memos for internal distribution.

## Copy-Paste Prompt – Standard Memo

```
You are a memo writer. Write an internal memo from:

TO:
[Recipient(s)]

FROM:
[Your name]

DATE:
[Today's date]

SUBJECT:
[Clear subject line]

PURPOSE:
[Why you're writing this memo]

KEY POINTS:
[3–5 main points]

ACTION REQUIRED:
[What you need from readers]

BACKGROUND:
[Context if needed]

INSTRUCTIONS:
1. Keep total length under 1 page
2. Use bullet points for lists
3. Lead with key information
4. End with clear action and deadline
5. Professional but conversational tone

Format:

MEMORANDUM

TO:        [Recipients]
FROM:      [Your Name]
DATE:      [Today]
SUBJECT:   [Clear subject]

[Opening paragraph: what this is about and why it matters]

[Key Points]
• Point 1
• Point 2
• Point 3

[Action Required]
[What you need and by when]

[Background/Context if needed]

Output only the memo. No preamble.
```

## Copy-Paste Prompt – Decision Memo

```
You are a decision memo specialist. Write a memo asking for a decision from:

DECISION NEEDED:
[What decision are you requesting]

CONTEXT:
[Why this decision is needed now]

OPTIONS:
[2–3 options for decision-maker to consider]

RECOMMENDATION:
[Which option and why]

TIMELINE:
[When you need the decision]

INSTRUCTIONS:
1. Lead with the decision needed
2. Present options objectively
3. Recommend one option clearly
4. Give timeline for decision
5. Length: 1–2 pages

Output only the memo. No preamble.
```

## Variables to Customise

- `[TO]` → Recipients
- `[SUBJECT]` → Clear, specific subject
- `[PURPOSE]` → Why you're writing
- `[KEY POINTS]` → Essential information
- `[ACTION REQUIRED]` → What you need

## Example Input

```
To: Product team
Subject: New feature release timeline
Purpose: Inform about Q3 launch
Points: Launched Q3, 3 core features, timeline, resource needs
Action: Confirm timeline; allocate resources
```

## Example Output

**MEMORANDUM**

TO:        Product Team
FROM:      Alex (Product Lead)
DATE:      15 May 2026
SUBJECT:   Q3 Feature Release – Timeline and Resource Confirmation

**Purpose**

We're launching three core features in Q3 2026. This memo outlines timeline and confirms resource allocation.

**Timeline**

• Q2 (May–June): Development and testing
• Q3 (July–August): Launch and post-launch optimisation
• Target launch: 1 August 2026

**Requested Resources**

• Engineering: 3 FTE for full duration
• QA: 1 FTE for June–August
• Product/Design: 0.5 FTE for coordination

**Action Required**

Please confirm resource allocation by end of week. Once confirmed, we'll lock the timeline with stakeholders.

**Questions?**
Let me know by Friday. Timeline cannot shift without resource confirmation.

## Review Checklist

- [ ] Subject is clear and specific
- [ ] Purpose is stated upfront
- [ ] Key points are bulleted
- [ ] Action and deadline are explicit
- [ ] Length is under 2 pages
- [ ] Tone is professional
- [ ] Professional memo format used

---

See [styles/minto-pyramid-principle.md](../styles/minto-pyramid-principle.md) for logical argument structure.
