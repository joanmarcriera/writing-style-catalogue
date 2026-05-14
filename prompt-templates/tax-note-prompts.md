---
title: Tax Note Prompts
template_type: Tax Advisory Note
use_case: Draft a structured tax technical note that analyses a specific tax question by applying law to facts, states a conclusion with an appropriate confidence level, and identifies uncertainties and next steps.
audience: Tax advisers, in-house tax teams, finance directors, or clients receiving tax advice
output_format: Structured advisory note with question, facts, analysis, conclusion, and next steps
---

# Tax Note Prompts

## Purpose

A tax note is a formal technical document that applies the law to a specific set of facts and reaches a reasoned conclusion. It serves multiple purposes: advising a client or colleague, creating a record of the analysis for file, and demonstrating that a position has been considered and supported before it is adopted. Use this template when you need to analyse a specific tax question — whether on corporation tax, VAT, employment taxes, stamp duty, or any other head of charge — and produce output that is rigorous, clearly structured, and honest about uncertainty. The note must distinguish between law that is settled, areas where HMRC's position is known, and areas where genuine uncertainty exists. It should not overstate confidence in a position.

**Important:** Tax technical notes generated using this template should be reviewed by a qualified tax adviser before being relied upon. LLM-generated output may not reflect recent legislative changes, case law, or HMRC practice updates. Always verify statutory references independently.

## Copy-paste prompt

```
You are a tax adviser with specialist knowledge of UK tax law. Write a structured tax technical note that analyses the question below, applies the relevant law to the facts, reaches a conclusion, and identifies uncertainties and recommended next steps.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (the tax question, relevant facts, and any specific areas of law to address):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 500–1,500 words depending on complexity]

FORMAT: [FORMAT — recommended: Question / Facts and Assumptions / Legal Framework / Analysis / Conclusion / Uncertainties and Caveats / Next Steps]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. State the tax question precisely at the outset — a focused question is essential to a focused analysis.
3. Set out the facts clearly and separately from the analysis. List any assumptions you are making explicitly — label them as "Assumption:" so they are unambiguous.
4. Identify and summarise the relevant statutory provisions, case law, or HMRC guidance that governs the question. Cite references precisely only where they are supplied in [INPUT] or you are explicitly asked to use them. If you are uncertain of the precise reference, create a "References to verify" note rather than citing a potentially incorrect provision.
5. Apply the law to the facts in the analysis section. Work through the argument step by step — do not jump to the conclusion.
6. State the conclusion with an explicit confidence level, using language such as: "We consider this position to be well-supported", "this is a defensible position but not free from doubt", or "there is material uncertainty here and we recommend seeking a formal opinion or advance clearance".
7. Identify all material uncertainties, ambiguities in the legislation, areas of HMRC challenge risk, and any pending developments (consultations, tribunal cases) that could affect the position.
8. Recommend specific next steps: additional information needed, documentation to prepare, whether to seek counsel's opinion or HMRC clearance, filing positions, and any protective actions.
9. Do not overstate certainty. Tax law is frequently uncertain; acknowledging that is a sign of rigour, not weakness.
10. Preserve all factual content from the input — do not invent transactions, amounts, or entities.
11. Tone: [TONE — typically: technical, precise, measured].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the tax note. No preamble or commentary.

IMPORTANT CAVEAT TO INCLUDE AT THE TOP OF THE NOTE:
"This note has been prepared using an AI language model as a drafting tool. It should be reviewed by a qualified tax adviser before being relied upon. Statutory references and HMRC guidance should be independently verified. This note does not constitute formal tax advice."
```

## Variables to customise

- `[AUDIENCE]` — who will read the note. Examples: "in-house tax team at Meridian Financial Services", "Finance Director with no specialist tax background — avoid technical jargon where possible", "external client (sole trader, basic tax knowledge)".
- `[PURPOSE]` — the objective of the analysis. Examples: "advise on the tax treatment of a termination payment", "confirm the VAT position on a software-as-a-service supply", "assess the employment status of an IR35-caught contractor".
- `[CONTEXT]` — background to the question. Examples: "the client is a technology consultancy operating through a personal service company; the end-client is a large UK bank classified as a medium/large client for IR35 purposes", "the acquisition completed on 1 April 2026 and the tax position needs to be confirmed before the filing deadline".
- `[INPUT]` — the specific question, full facts, any prior advice or HMRC correspondence, and the jurisdiction. Be as precise as possible.
- `[DESIRED_OUTCOME]` — what the reader needs from the note. Examples: "a clear position on whether the payment is taxable, including confidence level and any protective steps", "a summary the Finance Director can present to the audit committee".
- `[TONE]` — tax notes are typically "technical and precise". If the audience is non-specialist, add "with plain English summaries of technical points".
- `[LENGTH]` — simple questions: 500–700 words; complex or multi-issue questions: 1,000–1,500 words.
- `[FORMAT]` — use the recommended structure. Add a "Summary for the Client" section at the end if the audience is non-specialist.
- `[CONSTRAINTS]` — examples: "jurisdiction is England and Wales only; do not address Scottish tax differences", "assume the transaction has already completed — protective steps are retrospective only", "include a plain English summary at the end for a non-specialist reader".

## Example input

```
AUDIENCE: In-house tax team at Vertex Holdings Ltd; finance director will also read the note
PURPOSE: Advise on the UK corporation tax treatment of a management incentive plan (MIP) payment made on exit to a key employee who holds restricted shares
CONTEXT: Vertex Holdings Ltd acquired a portfolio company, Clearpath Analytics Ltd, in a secondary buyout in March 2026. On completion, certain managers who held MIP shares in Clearpath received cash payments representing their share of the exit proceeds. The largest payment was £850,000 to the Head of Technology, who had held the shares for 3 years and 4 months under a restricted share plan. The shares were acquired at market value at grant. Vertex's tax team needs to understand: (a) whether the payment is a capital gain or employment income for the individual, and (b) whether Vertex / Clearpath has any PAYE/NIC withholding obligation.
INPUT:
  Question: Is the £850,000 MIP payment received by the Head of Technology on the Clearpath exit (a) chargeable to capital gains tax or (b) subject to income tax and Class 1 NICs as employment income? Does Clearpath have a PAYE withholding obligation?

  Facts:
  - Payer: Clearpath Analytics Ltd (now a subsidiary of Vertex Holdings Ltd)
  - Recipient: Head of Technology (employed by Clearpath)
  - Payment amount: £850,000
  - Nature of payment: cash received on the sale of restricted shares held under a MIP
  - Shares acquired: March 2022 at market value (confirmed by independent valuation)
  - Shares sold: March 2026 (completion date of the Vertex acquisition)
  - Holding period: 3 years and 4 months
  - Restriction: shares were restricted and subject to good leaver / bad leaver provisions; the employee is treated as a good leaver
  - No s.431 ITEPA 2003 election was made at acquisition
DESIRED_OUTCOME: A clear tax position with confidence level; confirmation of the PAYE/NIC position; recommended next steps including any documentation Clearpath should prepare.
TONE: Technical and precise, but with a brief plain English summary at the end for the Finance Director
LENGTH: 800–1,200 words
CONSTRAINTS: UK law only (England and Wales); the transaction has completed — advice on retrospective protective steps only; include the statutory caveat at the top.
```

## Example output

---

**TAX TECHNICAL NOTE**

*This note has been prepared using an AI language model as a drafting tool. It should be reviewed by a qualified tax adviser before being relied upon. Statutory references and HMRC guidance should be independently verified. This note does not constitute formal tax advice.*

**Prepared for:** Vertex Holdings Ltd — In-House Tax Team
**Date:** 14 May 2026
**Subject:** Corporation tax and PAYE/NIC treatment of MIP exit payment — Head of Technology, Clearpath Analytics Ltd

---

**1. Question**

(a) Is the £850,000 payment received by the Head of Technology on the exit of Clearpath Analytics Ltd chargeable to capital gains tax (CGT) or subject to income tax as employment income?

(b) Does Clearpath Analytics Ltd have a PAYE withholding and Class 1 NIC obligation in respect of the payment?

---

**2. Facts and Assumptions**

The following facts have been provided:
- The Head of Technology received £850,000 on the sale of restricted shares held under a MIP, on completion of the Vertex acquisition (March 2026).
- Shares were acquired in March 2022 at market value, confirmed by independent valuation.
- The shares were restricted (subject to good/bad leaver provisions). The employee is treated as a good leaver.
- Holding period: 3 years and 4 months.
- No election under s.431 ITEPA 2003 was made at the time of acquisition.

*Assumption: the shares constitute "employment-related securities" within the meaning of Part 7 ITEPA 2003, which is almost certain given they were acquired by reason of employment.*

*Assumption: the market value at acquisition was correctly determined and robustly documented. If this valuation is later challenged by HMRC, the analysis may change.*

---

**3. Legal Framework**

The tax treatment of gains on employment-related securities is governed by Part 7 ITEPA 2003 (securities income) and Chapter 3 (restricted securities). The key provisions are:

- **s.417–s.421 ITEPA 2003** — restricted securities; charge on chargeable events (including disposal)
- **s.431 ITEPA 2003** — election to disapply the restricted securities rules and treat shares as unrestricted
- **s.698 ITEPA 2003** — PAYE obligation where employer is the payer; also relevant where a third party makes a readily convertible asset or cash payment
- **Schedule 1 SSCR 2001** — Class 1 NIC on payments from employment-related securities

---

**4. Analysis**

**(a) Income tax vs. CGT**

Because the shares are employment-related securities and no s.431 election was made, the restricted securities rules under Chapter 3 Part 7 ITEPA 2003 apply. On a chargeable event (here, the disposal on exit), any post-acquisition growth in value attributable to the lifting of restrictions is charged to income tax as employment income, not CGT.

The starting position is that the full gain (market value at disposal less acquisition cost) is subject to income tax under s.426 ITEPA 2003, because the restrictions were lifted on the same occasion as the disposal. The employee cannot access capital gains treatment on the restricted shares portion.

*Note:* If a s.431 election had been made in March 2022, the full gain would have been a capital gain. It was not, and no retrospective election is available.

*Assessment: We consider the income tax characterisation to be well-supported and consistent with settled law. The risk that HMRC would accept a CGT argument is very low.*

**(b) PAYE and Class 1 NIC**

Section 698 ITEPA 2003 and regulation 94 Income Tax (PAYE) Regulations 2003 impose a PAYE obligation on the employer where an employment-related securities event gives rise to employment income. As the payment is income from employment-related securities, Clearpath Analytics Ltd has a PAYE withholding obligation in respect of the £850,000 payment.

Class 1 NICs (employer and employee) are also due, by reference to Schedule 1 SSCR 2001, as the employment-related securities rules bring the gain within the definition of earnings for NIC purposes.

The PAYE and NIC should have been operated by Clearpath on or before the date of payment (March 2026). If this has not been done, Clearpath is now in default and interest and penalties may accrue.

---

**5. Conclusion**

(a) The £850,000 payment is subject to income tax as employment income, not CGT. This is a well-supported position.

(b) Clearpath Analytics Ltd has a PAYE and Class 1 NIC obligation in respect of the payment. If PAYE was not operated at completion, Clearpath is at risk of a PAYE audit and associated penalties.

---

**6. Uncertainties and Caveats**

- The valuation of the shares at acquisition has not been independently reviewed for the purposes of this note. If HMRC challenge the acquisition value, the taxable amount may increase.
- This note does not address whether Business Asset Disposal Relief (formerly Entrepreneurs' Relief) could have applied — it would not be available here given the lack of a s.431 election, but the analysis would differ if a qualifying EMI scheme had been in place.
- HMRC may scrutinise valuation and employment-related securities analysis where the facts are incomplete or the commercial rationale is unclear. Robust documentation of the March 2022 valuation is essential; any specific tribunal authority should be added only after qualified adviser review.

---

**7. Next Steps**

1. **Immediate:** Confirm whether PAYE and NICs were operated at completion. If not, make a voluntary disclosure to HMRC promptly to reduce penalty exposure.
2. **Documentation:** Retrieve and retain the independent share valuation report from March 2022. Ensure the restricted share plan rules, the good leaver determination, and the s.431 non-election are all documented on file.
3. **Filing:** The employment-related securities event must be reported on the ERS annual return (due 6 July 2026 for the 2025–26 tax year).
4. **Consideration:** Vertex Holdings should review whether other MIP participants in the same acquisition may have similar PAYE exposure.

---

**Plain English Summary (for Finance Director)**

The Head of Technology's £850,000 payment is taxable as employment income, not as a capital gain. This is because the shares held were restricted, and no special election was made when the shares were granted that would have allowed the gain to be taxed as a capital gain. As the employer, Clearpath was required to deduct income tax and National Insurance Contributions from the payment when it was made. If that was not done, it should be corrected as soon as possible by making a voluntary disclosure to HMRC.

---

## Review checklist

- [ ] The statutory caveat appears at the top of the note
- [ ] The question is stated precisely and is answerable from the facts provided
- [ ] All assumptions are explicitly labelled as such
- [ ] Statutory references are included (and flagged as uncertain if not verified)
- [ ] The analysis works through the argument step by step — it does not jump to the conclusion
- [ ] The conclusion includes an explicit confidence level
- [ ] Uncertainties and HMRC challenge risks are identified honestly
- [ ] Next steps are specific and actionable
- [ ] British English used throughout
- [ ] A plain English summary is included where the audience includes non-specialists

---

See [styles/tax-advisory-style.md](../styles/tax-advisory-style.md) for detailed tax advisory style.
