---
title: One-Page Study Summary Workflow
category: Workflow
---

# Workflow: One-Page Study or Learning Summary

A one-page learning summary is one of the most powerful personal knowledge tools available: it forces you to compress what you have learned to its essential core, test whether you actually understand it, and produce a reference you will actually re-read. Writing the summary is also a learning activity in itself — the act of translating complex ideas into plain language reveals what you understood and what you only thought you understood. This workflow applies whether you are summarising a book, a research paper, a course, a conference talk, or a professional development session.

## Style to use

[Plain English](../styles/plain-english.md) for general learning summaries — the discipline of plain English forces you to translate jargon and abstraction into concepts you can actually explain. [Socratic Explainer](../styles/socratic-explainer.md) for technical or academic material where the concept is complex enough to benefit from a question-and-answer structure that guides the reader's understanding step by step.

## Skill to use

[Create One-Page Brief](../skills/create-one-page-brief.md) — the one-page brief structure works equally well for learning summaries: headline (the core thesis), key points (the 3–5 concepts), evidence/examples, how you will apply it, and what questions remain.

## Prompt template to start from

[Learning Notes Prompts](../prompt-templates/learning-notes-prompts.md)

## Inputs required

Before drafting, you need:
- Your raw notes from the material (even messy notes are better than nothing)
- The source: title, author, date, and format (book, paper, course, talk)
- The core thesis or argument — what is the single most important claim or idea?
- The 3–5 concepts or insights that most changed your thinking or are most applicable to your work
- One concrete example for each concept — from the source material or from your own experience
- At least one thing you will do differently as a result of this learning
- Any questions the material left unanswered

## Copy-paste master prompt

```
You are a learning specialist and instructional designer. Help me create a one-page study summary for the material described below.

AUDIENCE: My future self — someone who read this material 6 months ago and needs a concise reminder of what it contained and why it mattered.
PURPOSE: To create a permanent, scannable reference that captures the essential ideas and my intended application of them.
CONTEXT: [Type of material: book / research paper / course / conference talk / professional development session. Domain: e.g. cloud architecture, tax law, behavioural economics, leadership, cybersecurity]
INPUT:
Source: [Title, author, date, format]
Core thesis: [The single most important argument or idea — in one sentence, in your own words]
Key concepts:
- Concept 1: [Name] — [your explanation in 2 sentences] — [one concrete example]
- Concept 2: [Name] — [your explanation in 2 sentences] — [one concrete example]
- Concept 3: [Name] — [your explanation in 2 sentences] — [one concrete example]
How I will apply this: [Specific, named actions or changes to how you work — not vague "I will think about this more"]
Unanswered questions: [What the material did not resolve; what you want to explore further]
DESIRED_OUTCOME: A one-page summary I will actually re-read and find useful 6 months from now.
TONE: My own words, not the author's. Clear and direct. No academic hedging. Explain as if to a smart colleague who has not read the source.
LENGTH: Exactly one printed page. Approximately 350–450 words plus a title block.
FORMAT: Bold headline (the core thesis in one sentence). Then sections: Source | Core thesis | Key concepts (3–5 with examples) | How I will apply this | Open questions. Use short paragraphs or bullets — not academic prose.
CONSTRAINTS: Use British English. Explain concepts in your own words — do not quote the source extensively. Every "how I will apply this" item must be a specific, named action. Output only the one-page summary; no preamble.
```

## Step-by-step process

1. **Complete the material** (variable): Read, watch, or attend the source in full. Take notes as you go — messy is fine. Mark anything you want to come back to.

2. **Wait and review** (30 minutes, ideally the day after): Sleep on it. The following day, review your notes and identify: what do you still remember? What has already faded? The concepts that stuck are the ones worth capturing. The ones that faded were either not important or not well understood.

3. **Identify the core thesis** (15 minutes): Ask yourself: if you had to explain what this material is about in one sentence to a colleague, what would you say? This is harder than it sounds. If you cannot do it, you did not understand the material well enough yet — re-read the key sections.

4. **Select 3–5 concepts** (20 minutes): From your notes, select the 3–5 ideas that most changed your thinking, most surprised you, or are most directly applicable to your work. For each, write one concrete example — either from the source or from your own experience. If you cannot think of an example, you have not understood the concept yet.

5. **Draft with the prompt** (20 minutes): Populate all INPUT fields and run the master prompt. The output will give you structure and language — but check that every sentence is actually true to your understanding, not just plausible-sounding.

6. **Refine and constrain** (20 minutes): The one-page constraint is the most important discipline in this workflow. If the draft runs to two pages, cut — not by making the font smaller, but by cutting content. Ask for each paragraph: would I miss this in 6 months? If not, cut it.

7. **File and schedule a review** (5 minutes): Save the summary with the source reference. Add it to a personal learning library (Notion, Obsidian, or a simple folder). Set a calendar reminder to re-read it in 3 months. Re-reading is where the value accumulates.

**Total time: 2–3 hours from completing the material to a filed summary**

## Review checklist

- [ ] The summary fits on one printed page at standard font size
- [ ] The core thesis is in your own words — not a quote or paraphrase of the author
- [ ] Every concept has a concrete example — not an abstract description
- [ ] "How I will apply this" contains at least one specific, named action — not a vague intention
- [ ] You could explain any concept on this page to a colleague without re-reading the source
- [ ] The summary has the source reference (title, author, date) at the top
- [ ] British English throughout

## Example output excerpt

> **Thinking in systems: the behaviour of complex systems cannot be predicted from their components.**
>
> **Source**: *Thinking in Systems* — Donella Meadows (2008)
>
> **Core thesis**: Most of the problems we try to fix are systems problems — they arise from the structure of the system, not from bad actors or bad luck. Changing the structure changes the behaviour; fixing individual components rarely does.
>
> **Key concepts**
>
> *Feedback loops*: Systems regulate themselves through reinforcing loops (which amplify change) and balancing loops (which resist it). Our cloud cost overrun in Q3 was a reinforcing loop — developers provisioned resources freely because the cost was invisible to them; cost overruns triggered audit reviews that delayed future provisioning, which made developers over-provision to buffer against delays, which increased costs further. The fix was not to punish developers but to change the structure: make costs visible in real time.
>
> **How I will apply this**
> - Before proposing a fix to a recurring operational problem, map the system and identify the feedback loops involved
> - When a policy produces unintended consequences, look for the balancing loop it disrupted rather than adding more rules
