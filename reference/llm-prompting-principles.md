---
title: LLM Prompting Principles
category: Reference
---

# LLM Prompting Principles

The quality of an LLM's output is almost entirely determined by the quality of the prompt. A poor prompt produces a generic, unfocused document that requires significant rewriting. A well-structured prompt produces a first draft that is 80% usable with targeted edits. These principles apply to Claude, ChatGPT, Gemini, and any comparable large language model.

---

## Principle 1: Assign a role before describing the task

Tell the LLM what expert it is playing before giving the task. This is not metaphor — it changes the vocabulary, the level of detail, and the conventions the model applies.

**Without role**: "Write a tax note on earn-outs."
**With role**: "You are a UK corporate tax adviser with expertise in M&A transactions. Write a professional tax technical note on the CGT treatment of earn-out consideration."

**Why it works**: The role primes the model to use the conventions, vocabulary, and structure of that domain. A "board paper specialist" writes differently from a "blogger."

---

## Principle 2: Specify the output format before the task

Define what you want back — the format, structure, and length — before you describe the content. This prevents the model from choosing a format by default.

**Vague**: "Summarise this document."
**Specific**: "Summarise this document in 5 bullets, each under 20 words, using active voice. Start each bullet with the most important word."

**Checklist of format elements to specify**:
- [ ] Document type (memo, board paper, FAQ, bullet list, table, numbered steps)
- [ ] Length (word count, page count, or number of items)
- [ ] Structure (specific section headings, or named structural pattern)
- [ ] Visual format (Markdown, plain text, table, code block)
- [ ] Tone (formal, professional-conversational, technical, plain English)

---

## Principle 3: Provide specific context, not general topic

Context is the difference between a usable output and a generic one. The more specific and real the context, the more specific and useful the output.

**Generic context**: "We are a company considering cloud migration."
**Specific context**: "We are a 200-person UK financial services firm currently running 140 servers across two co-location sites at a total annual cost of £1.22M. Our contracts expire in September 2025. We are considering a phased migration to Azure IaaS, with a £2.1M one-off investment, delivering annual savings of £800k from year 2."

**The specificity rule**: Replace every vague descriptor ("significant", "large", "growing", "important") with a number, a name, or a specific fact.

---

## Principle 4: Give the model the raw material — do not rely on it to invent facts

LLMs are excellent at structuring and writing; they are unreliable when asked to generate specific facts, figures, or legal positions from their training data. Always provide the facts; ask the model to write.

**Relying on the model (risky)**: "Write a business case for cloud migration including the financial analysis."
**Providing the material (reliable)**: "Write a business case for cloud migration. Financial data: current costs £1.22M, migration cost £2.1M, annual cloud costs £420k, savings from year 2 £800k, NPV over 5 years £1.9M at 10% discount rate, payback 32 months."

**Key rule**: Never use an LLM-generated number or legal citation without verifying it independently. Models confabulate specific figures convincingly.

---

## Principle 5: Specify what the LLM must NOT do

Negative constraints are often more powerful than positive instructions. They prevent the model from defaulting to its most common behaviours.

**Common behaviours to suppress**:
- "Do not include a preamble or meta-commentary — output only the document."
- "Do not use filler phrases: 'it is important to note', 'in conclusion', 'it goes without saying'."
- "Do not pad to reach the word count — cut content if necessary."
- "Do not invent specific figures, names, or legal citations — use only the information I have provided."

**Example**: "Write a one-page brief. Do not open with 'In today's rapidly evolving...'. Do not include a conclusion section — end with the Ask. Do not use the word 'leverage'. Output only the brief; no preamble."

---

## Principle 6: Use British English as a standing instruction

If you work in a UK context, include "Use British English throughout" in every prompt. LLMs default to American English (analyze, organization, color, license as a verb). This affects not just spelling but vocabulary choices and legal terminology.

**Always include**: "Use British English throughout. British spellings: colour, organisation, licence (noun), favour, recognise."

**Bonus**: Also specify any terminology preferences: "Use 'staff' not 'employees'; 'board' not 'board of directors'; 'HMRC' not 'the IRS'."

---

## Principle 7: Instruct the model to output only the artefact

By default, LLMs open with a commentary ("Certainly! Here is a draft of...") and sometimes close with suggestions ("Let me know if you'd like me to adjust..."). Suppress this with a standing instruction.

**Instruction**: "Output only the [document type]; no preamble, no commentary, no suggestions for revision."

**Why it matters**: Every sentence of meta-commentary is text you must delete before you can use the output. It also signals that the model is in "assistant mode" rather than "writer mode" — the framing affects the output quality.

---

## Principle 8: Chain complex tasks into steps

For complex outputs (a board paper, a business case, a training module), do not ask for everything in one prompt. Break the task into steps and build iteratively.

**Single prompt (risky)**: "Write a full business case for the Azure migration including financial analysis, options analysis, risk register, and implementation plan."

**Chained approach (better)**:
1. "Draft the executive summary and options analysis for the Azure migration business case. [Provide context and data]."
2. "Now draft the financial analysis section, using these figures: [data]."
3. "Now draft the risk register. Use this table format: [format]. Here are the risks I have identified: [list]."

**Why it works**: Each step produces a reviewable, editable section. You can correct errors before they propagate through the whole document. You maintain control of the narrative.

---

## Principle 9: Show an example of what good looks like

Providing a short example of the style, tone, or format you want is often more effective than describing it. LLMs are exceptional at pattern-matching.

**Describe the style**: "Write in a formal, conclusion-first style."
**Show the style**: "Write in this style — notice the conclusion-first sentence, the numbered evidence, and the direct close: 'We recommend approval of the Azure migration. Three reasons support this: (1) cost savings of £800k per year from 2027; (2) FCA resilience compliance achieved by Q3 2026; (3) current contract renewal would lock in £1.22M annual costs for another 5 years. We request board approval at the June meeting.'"

---

## Principle 10: Iterate, do not rewrite from scratch

If the first draft is not right, do not abandon it and start over. Use targeted follow-up prompts to refine specific sections.

**Targeted refinement prompts**:
- "Rewrite the executive summary in under 150 words. Keep the same recommendations and facts."
- "The tone in Section 3 is too casual. Rewrite it to match the formal tone of Section 1."
- "The risk register is missing a financial risk. Add a row for 'Risk that cloud costs exceed forecast by more than 20%', scored Likelihood 3, Impact 4."
- "Rewrite the opening sentence. It should not start with 'In recent years'. Start with the key fact instead."

---

## What to always include in a prompt — checklist

| Element | Why it matters |
|---------|----------------|
| **Role** ("You are a [expert]...") | Sets domain conventions and vocabulary |
| **Audience** | Calibrates vocabulary, tone, and assumed knowledge |
| **Purpose** | Tells the model what the document must achieve |
| **Context** | Prevents generic output; enables specific content |
| **Input data** | The raw material to write from — do not ask the model to invent facts |
| **Desired outcome** | What success looks like; what the reader should do or believe |
| **Tone** | Formal / professional / conversational; explicit is better than implied |
| **Format** | Document type, structure, length, markdown vs. plain text |
| **Constraints** | What not to do; what not to include; what words to avoid |
| **Language** | "Use British English throughout" |
| **Output instruction** | "Output only the document; no preamble" |

---

See [reference/good-vs-bad-prompts.md](../reference/good-vs-bad-prompts.md) for before/after examples applying these principles.

See [prompt-templates/](../prompt-templates/) for copy-paste prompt templates following these principles for specific document types.
