---
title: Create FAQ
skill_type: Document generation
output: A structured set of questions and answers, grouped by topic, that addresses the most common and most important questions a defined audience has about a subject
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor, Knowledge base platform (Confluence, Notion, SharePoint)
difficulty: Easy
---

# Skill: Create FAQ

## What this skill does

Compiles a structured set of questions and clear, direct answers to address the most common uncertainties, concerns, or queries that a specific audience has about a topic, system, process, or change. A good FAQ is audience-led: the questions are the ones people actually ask (or will ask), not the ones the author thinks they should ask. Each answer is self-contained and complete — the reader should not need to read elsewhere to understand the response. FAQs are living documents: they improve over time as actual questions replace assumed ones.

## When to use it

- Supporting the rollout of a new system or policy by pre-answering the questions the communications team knows will arrive (IAM rollout, cloud migration go-live, new expense policy)
- Providing a self-service resource for a support team that handles repetitive queries
- Supplementing a technical document with a plain-English layer for non-technical readers
- Preparing a client-facing FAQ for a tax advisory document or transaction process
- Producing the "Q&A" section of a board paper or investor document to address anticipated objections

## Inputs required

- The topic the FAQ covers — stated precisely
- The target audience: their role, knowledge level, and what they are most worried about
- Actual questions, if available (from a support inbox, previous meetings, or stakeholder interviews)
- If no real questions are available: a description of the context and the likely concerns
- Any topics that are out of scope (to prevent the FAQ from being used as a substitute for proper advice)
- An escalation path for questions the FAQ does not answer

## Copy-paste prompt

```
You are a knowledge management specialist. Create a FAQ for the topic and audience described below.

AUDIENCE: [Who will use this FAQ — role, knowledge level, and their primary concerns]
PURPOSE: [What the FAQ is for — pre-empting support queries, supplementing a document, supporting a rollout]
CONTEXT: [What is changing, being implemented, or being communicated; any background the author should know]
INPUT: [Paste any real questions received, support ticket themes, or notes on anticipated concerns; if none, describe the situation in detail]
DESIRED_OUTCOME: [The reader finds the answer to their specific question without needing to contact anyone]
TONE: Clear, direct, and reassuring. FAQ answers should sound like a knowledgeable colleague, not a legal disclaimer.
LENGTH: 15–25 Q&A pairs grouped under 4–6 topic headings. Each answer: 2–5 sentences.
FORMAT: H2 for topic group headings. Bold for each question. Plain prose for each answer. End with a contact/escalation section.
CONSTRAINTS: Use British English. Answers must be complete — do not say "refer to the relevant policy" without specifying where the policy is. Avoid passive voice in answers. Do not include rhetorical questions as entries. Output only the FAQ; no preamble.

STRUCTURE:
# FAQ: [Topic]
**Last updated**: [Date]
**Applies to**: [Audience]

## [Topic group 1]

**Q: [Question as the reader would ask it]**
A: [Clear, direct answer — 2–5 sentences. State any conditions or exceptions. Include specific next steps if the situation requires action.]

## Contact
If your question is not answered here, contact [team/person] via [channel] — [response time commitment].
```

## Suggested output structure

- **Header** — topic, last updated date, applies-to audience
- **Topic group 1–N** — 4–6 groups of related questions; group by the reader's concern, not the author's categorisation
- **3–6 Q&A pairs per group** — questions written as the reader would ask them; answers complete and specific
- **Escalation section** — who to contact, how, and what response time to expect
- **Related documents** — links to the SOP, policy, runbook, or other reference documents the FAQ supplements

## Quality controls

- [ ] Every question is written as the reader would ask it — not as the author would state it
- [ ] Every answer is self-contained — the reader does not need to read something else to understand the answer
- [ ] No answer says "refer to [document]" without providing a direct link or the key information from that document
- [ ] Questions reflect real or highly probable concerns — not hypothetical edge cases that only 1 in 1,000 readers will have
- [ ] The escalation section specifies a contact, channel, and response time commitment
- [ ] British English throughout; technical terms defined if the audience may not know them

## Common failure modes

- **Questions written from author's perspective**: "What are the benefits of the new IAM system?" is what the author wants to say; "Will my current passwords still work after the migration?" is what the user is actually asking — write from the user's worry, not the author's message
- **Incomplete answers**: An answer that says "this depends on your situation" without explaining the conditions is not an answer — specify the conditions
- **Too many entries**: A 50-item FAQ is not navigable; keep to 25 maximum; move edge cases to a separate technical reference document
- **Never updated**: An FAQ published at go-live and never updated will contain outdated answers within months — assign an owner and a quarterly review date
- **No escalation path**: A reader who finds no answer to their question and has no way to ask will lose confidence in the whole document — always include a clear escalation route

## Example request

"Create a FAQ for staff about the new Entra ID MFA rollout. We are requiring all 600 staff to register for MFA by 30 June. Staff use a mix of Windows and Mac laptops and personal mobile phones. Anticipated questions: what MFA is, why we are doing it, what they need to do, what happens if they are travelling without a signal, what happens if they lose their phone, what happens if they miss the deadline, and how to get help. Audience: non-technical staff. Tone: reassuring and plain English. British English throughout."
