---
title: BLUF Approval Email — Supplier Renewal
category: Example
description: A worked executive email bundle with a precise approval request, deadline, commercial facts, and fallback.
bundle_id: bluf-approval-email
artefact: BLUF approval email
audience: Chief financial officer approving a time-sensitive supplier renewal
scenario: labelled-composite
style_path: styles/bluf-bottom-line-up-front.md
pattern_path: patterns/bluf.md
prompt_path: prompt-templates/email-prompts.md
rubric_path: rubrics/executive-communication-rubric.md
---

# BLUF Approval Email — Supplier Renewal

## Professional context

A technology director needs a decision from the CFO without hiding the deadline, cost increase, or fallback. The email must be ready to send after commercial figures are checked.

## Source packet

```text
SCENARIO: Labelled composite.
SENDER: Technology Director
RECIPIENT: Chief Financial Officer
DECISION: Approve a 12-month monitoring-platform renewal at £186,000 excluding VAT.
DEADLINE: 16:00 on 21 August 2026; the quoted price expires then.
CURRENT ANNUAL COST: £174,000 excluding VAT.
CHANGE: £12,000 / 6.9% increase.
BUDGET: Approved operations budget contains £190,000 for this service.
PROCUREMENT: Commercial and security reviews complete; legal review complete with no material exceptions.
FALLBACK: A one-month extension is available for £18,000, but written confirmation is required by the same deadline.
UNKNOWN: None material to the approval request.
```

## Completed prompt

```text
You are an executive communications adviser. Draft a BLUF email from the Technology Director to the Chief Financial Officer requesting one decision: approval of the 12-month monitoring-platform renewal.

Use only the supplied SOURCE PACKET. Do not invent savings, service risks, negotiation outcomes, vendor claims, approvals, or urgency. If the amount, deadline, budget position, review status, or fallback is missing or contradictory, return MISSING INFORMATION and list the exact gap instead of drafting the email.

Write a specific subject line. In the first sentence state the decision, amount, term, and deadline. Then give no more than four short bullets covering: price movement; budget position; completed assurance; fallback and its cost. Close with the precise response required. Keep the email between 130 and 190 words, use British English, and use £ figures consistently with “excluding VAT”. Do not add pleasantries, background history, or an invented consequence of non-renewal. Output only the subject line and email body.

Before finalising, check instruction fit, factual integrity, specificity, structure, professional tone, risk awareness, and usefulness against the Executive Communication Rubric. Preserve the fallback caveat exactly.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Subject: Approval required by 16:00, 21 August — £186,000 monitoring renewal

Please approve the 12-month monitoring-platform renewal at £186,000 excluding VAT by 16:00 on 21 August 2026.

• The price is £12,000 (6.9%) above the current annual cost of £174,000.
• The approved operations budget contains £190,000 for this service.
• Procurement, security, and legal reviews are complete, with no material legal exceptions.
• If approval cannot be given, a one-month extension costs £18,000 and must be confirmed by the same deadline.

Please reply “approved” or identify the remaining question before the deadline.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Instruction fit | 5 | The requested decision, length, and format are followed. | Pass |
| Factual integrity | 5 | Every amount and status maps to the source packet. | Pass |
| Structure | 5 | The decision is first and supporting facts are scannable. | Pass |
| Professional tone | 4 | Direct without becoming abrupt or promotional. | Pass |
| Usefulness | 5 | The recipient knows exactly how and when to respond. | Pass |

## Human review before use

- Finance must confirm the budget and VAT treatment.
- Procurement must confirm the quote and fallback remain open at send time.
- The sender must verify names, deadline, and approval authority.

## Reuse this bundle

- [BLUF Style](../styles/bluf-bottom-line-up-front.md)
- [BLUF Pattern](../patterns/bluf.md)
- [Email Prompts](../prompt-templates/email-prompts.md)
- [Executive Communication Rubric](../rubrics/executive-communication-rubric.md)
