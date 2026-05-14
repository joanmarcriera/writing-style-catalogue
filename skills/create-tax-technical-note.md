---
title: Create Tax Technical Note
skill_type: Document generation
output: A professional tax analysis document that states a specific tax question, applies the relevant law to the client's facts, reaches a clear conclusion, and quantifies any exposure or saving
tools_needed: LLM (Claude/ChatGPT/Gemini), tax research database (Tolley's, HMRC manuals), Word or PDF converter
difficulty: Complex
---

# Skill: Create Tax Technical Note

## What this skill does

Produces a structured, professional tax analysis in the format used by UK tax advisers and in-house tax teams. The note states a specific question, sets out the relevant facts, applies statute and HMRC guidance, identifies areas of uncertainty, and reaches a clear conclusion with a confidence level. An LLM can draft the structure and standard analysis, but a qualified tax adviser must verify every legal position before the note is delivered to a client or used to support a return. The LLM's role is speed and structure; the adviser's role is accuracy and professional responsibility.

## When to use it

- Advising a client on the tax treatment of a specific transaction (M&A, restructuring, property disposal, employment arrangement)
- Documenting the legal basis for a tax position taken in a return, for audit defence purposes
- Analysing the UK corporation tax implications of a cross-border structure or intra-group transaction
- Responding to an HMRC enquiry with a formal written explanation of a technical position
- Preparing a due diligence tax note on a target company's tax exposure for an acquirer

## Inputs required

- The specific tax question — stated precisely as a single interrogative sentence
- The relevant facts — client details, transaction structure, amounts, dates, jurisdictions
- The applicable tax legislation — the act, section, and statutory instrument
- Any relevant HMRC guidance (manuals, briefs, statements of practice)
- Any known case law or tribunal decisions on point
- The jurisdiction (UK — specify England & Wales, Scotland, or Northern Ireland if relevant; or cross-border)
- The purpose of the note (client advice, return support, due diligence, dispute response)
- Any areas of uncertainty or alternative interpretations to acknowledge

## Copy-paste prompt

```
You are a UK tax adviser. Write a professional tax technical note for the matter described below.

AUDIENCE: [e.g. Client's finance director / Internal tax team / External tax counsel / HMRC officer]
PURPOSE: [e.g. Client advice on transaction tax treatment / Audit defence / Due diligence note / Return support]
CONTEXT: [Client type (individual, company, trust); sector; any previous related advice; relationship to current position]
INPUT: [State the facts clearly: parties, transaction structure, amounts, dates, jurisdiction, any elections or prior positions taken]
DESIRED_OUTCOME: [A clear conclusion on the tax question with a confidence level; any recommended actions or alternative positions]
TONE: Formal and measured. Tax technical notes are professional advisory documents — conclusions must be stated clearly but with appropriate qualification where the law is uncertain.
LENGTH: 1,500–3,000 words depending on complexity. Typically 3–6 pages.
FORMAT: Standard tax note structure (see below). Use numbered sections. Use statutory references in the form "s.XXX ITTOIA 2005" or "para. X, Sch. Y FA 2003". Summarise conclusions in a separate section — do not bury them in the analysis.
CONSTRAINTS: Use British English. Do not state conclusions more confidently than the law supports — use "it is our view", "we consider", or "HMRC is likely to" as appropriate. Use only statutory references, HMRC guidance, and case law supplied in the input or independently verified by the adviser; if a reference is missing, write "[reference to verify]" rather than inventing one. Flag any areas where HMRC guidance conflicts with case law. Output only the note; no preamble.

STRUCTURE:
# Tax Technical Note: [Short description]
**Client / Matter**: [Name or matter reference]
**Date**: [Date]
**Author**: [Name, qualifications]
**Status**: [Advice / Draft for review / Privileged and confidential]

## 1. Question
[State the tax question being answered as a single clear sentence.]

## 2. Summary of conclusion
[State the conclusion and confidence level before the analysis — busy readers need to know the answer upfront.]

## 3. Facts
[Set out the relevant facts in numbered paragraphs. Include only facts that affect the analysis.]

## 4. Law and analysis
[Apply the legislation to the facts, section by section. Reference statutes precisely. Acknowledge alternative interpretations.]

## 5. Conclusion
[Restate the conclusion; specify any conditions or caveats; quantify the exposure or saving if instructed.]

## 6. Recommendations and next steps
[What the client or team should do; any elections, disclosures, or filings required; timing.]

## 7. Limitations
[Standard limitations paragraph: this note is based on the facts as stated; does not constitute legal advice; should be reviewed by a qualified adviser before reliance.]
```

## Suggested output structure

- **Header** — matter reference, date, author with qualifications, privilege/confidentiality status
- **Section 1: Question** — one sentence; precise enough that a reader knows exactly what is being answered
- **Section 2: Summary conclusion** — the answer upfront with a confidence descriptor (high confidence / moderate / uncertain)
- **Section 3: Facts** — numbered paragraphs; only material facts; no narrative padding
- **Section 4: Law and analysis** — statutory provisions applied to facts; HMRC guidance; case law where relevant; alternative interpretations acknowledged
- **Section 5: Conclusion** — clear answer; any conditions; quantification of tax at stake
- **Section 6: Recommendations** — elections, disclosures, filings, timing, or further steps
- **Section 7: Limitations** — standard advisory limitations; reliance restrictions if applicable

## Quality controls

- [ ] The question is stated as a single interrogative sentence — not a topic
- [ ] The conclusion appears in Section 2 (upfront) and is restated in Section 5 — not only at the end
- [ ] Every legal position references a specific statute by section and act name
- [ ] Areas of uncertainty are explicitly flagged with an appropriate confidence qualifier
- [ ] Quantification of the tax at stake appears if the facts permit it
- [ ] The note does not overstate HMRC's published position or understate case law uncertainty
- [ ] A qualified tax adviser has reviewed the note before delivery to any external party
- [ ] The limitations section is present and not watered down

## Common failure modes

- **Over-confident conclusions**: An LLM will often state "X is not taxable" without qualification — in tax, almost nothing is black and white; always add appropriate confidence qualifiers
- **Statutory references missing**: A tax note that says "under the relevant legislation" without citing the section is not useful for audit defence — be precise about every statutory reference
- **Invented authorities**: Never allow an LLM to invent statute sections, HMRC manual references, or case names — mark missing references for adviser verification
- **Facts not verified**: The LLM works from the facts as provided; if those facts are incomplete or assumed, the analysis is unreliable — gather all facts before prompting
- **Question too broad**: "What are the tax implications of this acquisition?" produces a generic essay; "Is the earn-out consideration in the sale of XYZ Ltd subject to capital gains tax or income tax for the selling shareholders?" produces a useful answer
- **Recommendations missing**: A note that concludes "this is a grey area" without telling the client what to do next is incomplete — always include recommended actions

## Example request

"Write a tax technical note on whether the earn-out consideration payable to the selling shareholders of a UK trading company is taxable as capital gains or income. The sellers are UK resident individuals who owned shares for 4 years. The earn-out is contingent on EBITDA targets over 3 years post-completion and will be paid in cash. The acquisition completed 1 January 2025. Analyse under TCGA 1992 s.48 (contingent consideration), ITEPA 2003 (employment income risk if sellers are also directors), and HMRC's earn-out guidance. Provide a clear conclusion with confidence level and recommend any elections or disclosures. Audience: client's finance director."
