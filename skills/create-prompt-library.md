---
title: Create Prompt Library
skill_type: Document generation
output: A curated, organised collection of reusable LLM prompts for a specific domain — each with a purpose statement, the full prompt text, variables to customise, and an example output
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor, Notion or Confluence for hosting
difficulty: Medium
---

# Skill: Create Prompt Library

## What this skill does

Curates a structured collection of high-quality, reusable prompts for a specific domain or team — covering the tasks that are done repeatedly and where inconsistent prompting produces inconsistent results. A prompt library is more than a list of prompts; it includes the context for each prompt (why it exists, when to use it), the variables to customise for each use, and an example of a good output. It transforms ad hoc prompting into a repeatable capability and allows a team to build on each other's prompting knowledge rather than starting from scratch every time.

## When to use it

- Building a prompt library for a professional services team that uses LLMs to draft tax notes, board papers, or client communications
- Creating a shared resource for an IT or cloud team to prompt consistently for runbooks, incident summaries, and architecture documents
- Developing a team AI onboarding resource that gives new joiners a starting point rather than a blank prompt box
- Documenting the prompts that work well for a specific use case so they are not lost when the person who discovered them leaves
- Standardising LLM output quality across a team by defining the prompts that produce the best results

## Inputs required

- The domain or team the library serves (tax advisory, cloud operations, IAM, executive communications, etc.)
- The specific use cases to cover — the tasks done most frequently or where output quality matters most
- Any house style, tone, or output format requirements that apply across all prompts
- Example outputs from prompts that have worked well (used to define "what good looks like")
- Any constraints: LLM platform(s) available; maximum prompt length; data sensitivity rules
- Who will use the library: their technical level with LLMs; their domain expertise

## Copy-paste prompt

```
You are a prompt engineering specialist and domain expert. Create a prompt library for the domain and use cases described below.

AUDIENCE: [Who will use this library — role, LLM experience level, domain expertise]
PURPOSE: [To standardise LLM prompting for [domain] and eliminate the time wasted on poor prompts]
CONTEXT: [Domain context; LLM platform(s) available; any house style or output format standards; data sensitivity rules]
INPUT: [List the use cases to cover — be specific about each task; include any example prompts or outputs that work well]
DESIRED_OUTCOME: [A practitioner can copy any prompt from the library, fill in the variables, and get a high-quality, usable output without further iteration]
TONE: Clear and instructional. The library is a practical tool — every prompt must work immediately.
LENGTH: One section per use case. Each section: purpose (2 sentences), when to use (3 bullets), the full prompt (copy-paste ready), variables to customise (bulleted), example output (50–100 word excerpt), and common mistakes (2–3 bullets).
FORMAT: H2 for use case name. Prompts in code blocks. Variables in [SQUARE BRACKETS]. Example outputs in blockquotes.
CONSTRAINTS: Use British English in all prompt text and instructions. Every prompt must include "Use British English" as a constraint. Every prompt must instruct the LLM to "Output only the [document type]; no preamble." Prompts must work in Claude, ChatGPT, and Gemini without modification. Output only the library; no preamble.

LIBRARY STRUCTURE:
# Prompt Library: [Domain]
**Version**: [Version number]
**Maintained by**: [Team or person]
**Last reviewed**: [Date]

## Introduction
[2–3 sentences: what this library is, who it is for, how to use it]

## Use Case 1: [Task name]
**Purpose**: [Why this prompt exists]
**When to use**:
- [Situation 1]
- [Situation 2]

**Prompt**:
```
[Full, copy-paste ready prompt with [VARIABLES]]
```

**Variables**:
- [VARIABLE]: [What to replace it with]

**Example output**:
> [50–100 word excerpt from a good output]

**Common mistakes**:
- [Mistake and fix]
```

## Suggested output structure

- **Library header** — domain, version, maintainer, last reviewed date
- **Introduction** — purpose, audience, how to use the library, how to request additions
- **Use case sections (1–N)** — one per task; purpose, when to use, full prompt, variables, example output, common mistakes
- **Usage tips** — general guidance on how to get the best from these prompts (e.g. always provide context, never copy output without review)
- **Maintenance instructions** — how to add new prompts, how to retire outdated ones, review cycle

## Quality controls

- [ ] Every prompt is tested against at least one real use case before inclusion — no theoretical prompts
- [ ] Every prompt includes "Use British English" and "Output only the [document]; no preamble"
- [ ] Variables are clearly marked in [SQUARE BRACKETS] and listed with descriptions
- [ ] Example outputs are realistic excerpts from actual good outputs — not fabricated
- [ ] The library covers the 80% of use cases that account for 80% of the team's prompting activity
- [ ] Prompts tested in Claude, ChatGPT, and Gemini to verify platform compatibility

## Common failure modes

- **Prompts too vague to reuse**: A prompt that works perfectly for one specific case but has the specifics baked in (e.g. a client name, a specific date) cannot be reused — extract all specifics into named variables
- **No example output**: Without seeing what "good" looks like, a new user cannot judge whether the LLM output is good or mediocre — include at least a 50-word excerpt
- **Library never maintained**: A prompt library that is not reviewed every 6 months will contain outdated prompts, missing use cases, and prompts that no longer reflect the team's house style — assign a maintainer and a review cycle
- **Too many prompts**: A library with 50 prompts is not navigable — curate ruthlessly; 10–15 well-tested prompts are more useful than 50 mediocre ones
- **Platform-specific prompts**: Prompts that use Claude-specific syntax (XML tags, extended thinking) will not work in ChatGPT or Gemini — either make prompts platform-neutral or clearly label them as platform-specific

## Example request

"Create a prompt library for our tax advisory team. Use cases to cover: (1) drafting a tax technical note on a specific question; (2) summarising an HMRC consultation response for partner review; (3) drafting a client-facing summary of a complex tax position in plain English; (4) writing an internal file note recording a tax advice conversation; (5) creating a comparison table of three tax structuring options for a transaction. LLM platform: Claude. House style: formal, British English, conclusion first. Data sensitivity rule: never include real client names or specific figures in prompts — use placeholders."
