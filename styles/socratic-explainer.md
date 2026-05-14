---
title: Socratic Explainer
category: Educational
aliases: [Question-Driven Learning, Exploratory]
---

# Socratic Explainer

## What This Style Is

Educational writing that teaches through questions. Rather than telling, guide readers to discover answers themselves. Interactive and engaging for learners.

**Core principle**: Ask questions that lead to understanding.

## When to Use It

- Educational content
- Learning guides
- Onboarding materials
- Teaching complex concepts
- FAQ sections
- Internal training

## When NOT to Use It

- Quick decisions (use BLUF)
- Technical precision (use Technical Documentation)
- Formal governance (use Board Paper)
- Persuasive recommendations (use Consulting)

## Core Structure

```
[OPENING QUESTION]
What are we exploring today?

[FOUNDATIONAL QUESTIONS]
What do you already know?

[GUIDING QUESTIONS]
Lead reader to discover answers.

[WORKED EXAMPLES]
Show application of learning.

[REFLECTION QUESTIONS]
What does this mean in your context?

[DEEPER QUESTIONS]
What comes next? What else might you explore?
```

## Copy-Paste Prompt Template

```
You are a Socratic educator. Write an exploratory guide from:

CONCEPT:
[What are you teaching]

AUDIENCE:
[Who are they and what do they know]

GOAL:
[What do you want them to understand]

KEY INSIGHTS:
[What discoveries should they make]

INSTRUCTIONS:
1. Start with an opening question
2. Ask questions that lead to discovery
3. Provide examples but let reader find the pattern
4. Use "Why?" and "What if?" frequently
5. Avoid telling; guide instead
6. End with deeper questions for reflection

Output only the Socratic guide. No preamble.
```

## Short Example

**Understanding Kubernetes Namespaces – A Socratic Guide**

Have you ever wanted to keep your home office separate from your living room? What problem does that separation solve?

In Kubernetes, namespaces do something similar. But before we explain that, let's think about what problem it solves.

Imagine you have 50 different applications running on one Kubernetes cluster. They all share the same resources—networking, storage, computing power. If one application uses too many resources, what happens to the others?

What if you could create separate "spaces" where applications couldn't see or interfere with each other? What would that let you do differently?

That's what namespaces provide. They're like separate environments within one cluster.

Now, here's a question for you: If you have a development team and a production team sharing one cluster, why might you create separate namespaces for each?

Think about it before we look at examples...

[Guide would continue with examples, more guiding questions, and reflections]

## Quality Checklist

- [ ] Opens with compelling question
- [ ] Questions guide rather than lecture
- [ ] Examples show, not tell
- [ ] Reader must think to find answers
- [ ] Tone is curious and inviting
- [ ] Ends with deeper questions
- [ ] Appropriate difficulty level for audience

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Asks questions then answers immediately | Removes opportunity to discover | Wait; let reader think before revealing |
| Questions are too leading | No real thinking required | Ask open-ended questions |
| Too many questions | Reader overwhelmed | Pace questions; leave space for reflection |
| No grounding examples | Questions feel abstract | Provide concrete examples to anchor learning |

---

See [prompt-templates/learning-notes-prompts.md](../prompt-templates/learning-notes-prompts.md) for learning material templates.
