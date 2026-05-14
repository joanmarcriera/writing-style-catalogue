---
title: Tax Technical Note Workflow
category: Workflow
---

# Workflow: Creating a Tax Technical Note

A tax technical note is a formal professional document that applies law to facts to answer a specific tax question. It is the primary output of a tax adviser working on a client matter, a transaction, or a compliance issue. The note creates a written record of the analysis — important for audit defence, professional standards compliance, and client service. An LLM can draft the structure and standard analysis efficiently; a qualified tax adviser must verify every legal position before any external use. This workflow covers the full process from clarifying the question to delivering a reviewed note.

## Style to use

[Tax Advisory Style](../styles/tax-advisory-style.md) — formal, structured, and precise. Tax notes use conclusion-first structure (state the answer at the top, then prove it), numbered paragraphs, precise statutory references, and appropriate confidence qualifiers. Avoid hedging language that conceals uncertainty — use explicit confidence statements ("we consider this position to be robust", "this position carries medium risk") instead.

## Skill to use

[Create Tax Technical Note](../skills/create-tax-technical-note.md) — use this skill to structure and draft the note. For the associated client communication, use [Create Executive Memo](../skills/create-executive-memo.md) as a cover letter framework.

## Prompt template to start from

[Tax Note Prompts](../prompt-templates/tax-note-prompts.md)

## Inputs required

Before drafting, you must have:
- The tax question — stated as a single, precise interrogative sentence (not a topic)
- All relevant facts: parties, transaction structure, amounts, dates, jurisdictions
- The applicable statute: act name, section, and paragraph; relevant HMRC manual references
- Any case law or tribunal decisions on point (at least the citation, ideally the key finding)
- Areas of uncertainty: where does the law conflict, where is HMRC's position unclear?
- The purpose of the note: client advice, audit defence, due diligence, return support
- The confidence level: do you believe this position is robust, or is it a reasoned view in an uncertain area?

## Copy-paste master prompt

```
You are a UK tax adviser with expertise in [relevant tax area — e.g. corporate tax, VAT, employment tax, capital gains]. Write a professional tax technical note for the matter described below.

AUDIENCE: [e.g. Client's finance director — non-tax specialist / Internal tax team / Senior tax counsel / HMRC officer in an enquiry]
PURPOSE: [e.g. Client advice on the tax treatment of [transaction] / Audit defence / Due diligence / Supporting the filing position in the [year] return]
CONTEXT: [Client type: UK-resident individual / UK trading company / Offshore trust / etc. Sector: [sector]. Any prior advice or agreed positions relevant to this question.]
INPUT:
Question: [State the tax question as a single interrogative sentence]
Facts: [Set out all relevant facts — parties, structure, amounts, dates, jurisdictions, any elections made]
Applicable law: [List statutes, HMRC guidance, and case law — with section references and citations]
Areas of uncertainty: [Where the law is ambiguous, where HMRC's position is unclear, where alternative interpretations exist]
Confidence: [Your view on the strength of this position: robust / reasonable / uncertain / risky]
DESIRED_OUTCOME: A clear, evidenced conclusion with a confidence level; specific recommendations for what the client or team should do next.
TONE: Formal and measured. State conclusions clearly but qualify them appropriately where the law is uncertain. Do not overstate HMRC's published position.
LENGTH: 1,500–3,000 words. 3–6 pages.
FORMAT: Standard tax note structure: (1) Question; (2) Summary of conclusion; (3) Facts; (4) Law and analysis; (5) Conclusion; (6) Recommendations; (7) Limitations.
CONSTRAINTS: Use British English throughout. Statutory references in the form "s.XXX ITTOIA 2005" or "para. X Sch. Y FA 2003". Conclusions must include a confidence level. Do not state more confidently than the law supports — use "we consider", "it is our view", "HMRC is likely to" as appropriate. Output only the note; no preamble.
```

## Step-by-step process

1. **Clarify the question** (30 minutes): Meet with or email the client to get the precise question in writing. Do not accept a vague instruction like "look at the tax on the deal" — nail down the specific legal question. Confirm facts in writing; do not draft from memory.

2. **Research** (2–4 hours): Review the relevant statute in full (not just the section you think applies — read the surrounding provisions for context). Check HMRC's published manuals. Search for relevant case law. Note where HMRC's guidance and case law diverge — that is your most important finding.

3. **Analyse** (1–2 hours): Apply the law to the facts. Work through each limb of the statutory test. Identify the most favourable interpretation and the most conservative one. Decide which view you hold and why.

4. **Draft with the prompt** (45–60 minutes): Use the master prompt above. Populate all INPUT fields from your research notes. The LLM will produce a structured draft — it is a starting point, not a finished product. The LLM does not know the law — it will pattern-match from training data. Every statutory reference and legal conclusion must be verified by you.

5. **Verify every legal position** (1–2 hours): Read the draft against the actual legislation. Correct any statutory references. Add any case law the LLM missed. Adjust any conclusions that overstate or understate the legal position. This step is non-negotiable.

6. **Senior review** (1–2 hours): For any note that will be delivered to a client or used to support a filed position, a qualified senior tax adviser must review the note. This is a professional standards requirement, not a formality.

7. **Incorporate review feedback and finalise** (30 minutes): Make all changes from the senior review. Update the version number and date.

8. **Deliver with covering communication** (15 minutes): Send to the client with a brief covering email. Offer a call to discuss the conclusions. Retain a copy on file with the date delivered and the recipient.

**Total time: 8–12 hours including research**

## Review checklist

- [ ] The question is stated as a single, precise interrogative sentence in Section 1
- [ ] The conclusion appears in Section 2 (upfront) and is not only at the end
- [ ] Every statutory reference is verified against the actual legislation
- [ ] Areas of uncertainty are explicitly flagged with appropriate confidence qualifiers
- [ ] The note does not overstate HMRC's published position
- [ ] A qualified senior tax adviser has reviewed and signed off before delivery
- [ ] The limitations section is present and not watered down
- [ ] The note is dated, versioned, and has a privilege/confidentiality marking

## Example output excerpt

> **2. Summary of conclusion**
>
> It is our view that the earn-out consideration payable to the Sellers is likely to be treated as capital (within the charge to capital gains tax under TCGA 1992 s.48), rather than as employment income under ITEPA 2003, provided the earn-out obligation is not linked to the Sellers' continued employment and is structured as a deferred element of the sale consideration.
>
> We assess this position as carrying moderate risk. HMRC has challenged earn-out arrangements in a number of recent cases (see paragraph 4.3 below) and will scrutinise any arrangement where the Sellers are also directors of the target company. We recommend that the Sale and Purchase Agreement contains explicit language confirming that the earn-out is not conditional on continued employment.
