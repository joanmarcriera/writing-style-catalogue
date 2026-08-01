---
title: Tax Note — Imported SaaS and UK Reverse Charge
category: Example
description: A worked tax-analysis bundle that separates facts, supplied authority, assumptions, conclusion, and adviser checks.
bundle_id: tax-technical-note
artefact: UK VAT technical note
audience: UK finance director and qualified VAT adviser
scenario: labelled-composite
style_path: styles/tax-advisory-style.md
pattern_path: patterns/context-analysis-options-recommendation.md
prompt_path: prompt-templates/tax-note-prompts.md
skill_path: skills/create-tax-technical-note.md
rubric_path: rubrics/tax-note-rubric.md
---

# Tax Note — Imported SaaS and UK Reverse Charge

## Professional context

A finance director needs a provisional treatment for imported SaaS before a qualified VAT adviser signs it off. The prompt is constrained to supplied HMRC material and must not invent statutory references or overseas tax consequences.

## Source packet

```text
SCENARIO: Labelled composite; not tax advice.
AS-OF DATE: 1 August 2026.
CUSTOMER: UK-established, VAT-registered trading company using the service for taxable business activity.
SUPPLIER: US-established company with no UK establishment stated in the contract.
SUPPLY: Annual access to standard cloud-hosted project-management software; invoice £24,000; invoice shows no UK VAT.
ASSUMPTIONS: Customer and supplier act in business capacities; no special place-of-supply rule applies; no private use; supplied contract facts are complete.
QUESTION: Does the UK customer account for VAT using the reverse charge, and what records should finance retain?
SUPPLIED AUTHORITY: HMRC, “Place of supply of services (VAT Notice 741A)”, current page checked 1 August 2026: https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a . Section 1.3 identifies VAT Act 1994 section 7A as covering the general B2B rule, section 8 as covering the reverse-charge mechanism for services received from outside the UK, and section 9 as covering where a person belongs.
LIMIT: The packet does not reproduce the full notice or test special rules. A qualified adviser must confirm the conclusion against the current notice and transaction documents.
```

## Completed prompt

```text
You are assisting a qualified UK VAT adviser. Draft a provisional technical note for the finance director on the imported SaaS invoice described in the SOURCE PACKET.

Use only the supplied facts and authority. Do not invent legislation, HMRC paragraphs, cases, rates, filing boxes, overseas tax treatment, supplier status, or special-rule analysis. Do not quote material that is not in the packet. Keep facts, assumptions, supplied authority, analysis, provisional conclusion, and adviser checks separate. If business status, establishment, use, invoice amount, authority, or the assumption about special rules is missing or contradictory, return MISSING INFORMATION rather than a conclusion.

Use British English and structure the note as: Question; Facts; Assumptions; Authority supplied; Analysis; Provisional conclusion; Records to retain; Adviser verification required. Explain the logical route from the supplied B2B, belonging, and reverse-charge references without claiming that the packet contains a complete legal review. Do not calculate a VAT amount because no current rate is supplied. Keep the note between 650 and 850 words. Output only the note.

Before finalising, apply the Tax Note Rubric. Factual accuracy, authority integrity, assumption visibility, reasoning, caveats, and review requirements are critical gates. State prominently that the note is illustrative and not tax advice.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Provisional conclusion
On the supplied facts and assumptions, the transaction should be tested under the general B2B place-of-supply and UK reverse-charge provisions identified in VAT Notice 741A. The customer is UK-established and VAT-registered; the supplier is stated to be US-established with no UK establishment; and the software is used for taxable business activity.

The packet is not sufficient to state the accounting amount or return entries. It supplies no VAT rate and does not reproduce the detailed HMRC rules or test whether a special provision applies. Finance should not post the final treatment until a qualified VAT adviser has checked the current notice, contract, invoice, establishment evidence, business-use evidence, and applicable rate.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Facts and assumptions | 5 | Business status, establishments, use, and special-rule assumption are separate. | Pass |
| Authority | 4 | The note uses one verified HMRC page without fabricating paragraphs. | Human check |
| Analysis | 4 | Reasoning follows the supplied B2B, belonging, and reverse-charge route. | Human check |
| Conclusion and caveats | 5 | The conclusion is provisional and refuses an unsupported calculation. | Pass |
| Professional usefulness | 4 | Finance receives a concrete adviser-verification list. | Human check |

## Human review before use

- A qualified VAT adviser must verify the current law, special rules, VAT rate, and return treatment.
- Finance must retain the contract, invoice, supplier-establishment evidence, business-purpose evidence, and adviser approval.
- The as-of date must be refreshed whenever the note is reused.

## Reuse this bundle

- [Tax Advisory Style](../styles/tax-advisory-style.md)
- [Context / Analysis / Options / Recommendation Pattern](../patterns/context-analysis-options-recommendation.md)
- [Tax Note Prompts](../prompt-templates/tax-note-prompts.md)
- [Create Tax Technical Note Skill](../skills/create-tax-technical-note.md)
- [Tax Note Rubric](../rubrics/tax-note-rubric.md)
