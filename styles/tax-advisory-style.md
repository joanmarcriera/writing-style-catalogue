---
title: Tax Advisory Style
category: Specialist
aliases: [Tax Technical Note, Professional Analysis]
---

# Tax Advisory Style

## What This Style Is

Professional, precise analysis of tax questions. Structured as Question → Analysis → Conclusion. Uses facts, precedent, and reasoning. Suitable for tax advisers or informed business stakeholders.

**Core principle**: Question clearly stated, analysis thorough, conclusion certain.

## When to Use It

- Tax technical analyses
- Adviser-to-client memos
- Board tax policy summaries
- Complex tax positions
- Transaction tax analysis
- Compliance or structural questions

## When NOT to Use It

- General business communication (use Smart Brevity)
- Marketing or sales (use Persuasive Sales)
- Operational guidance (use Plain English)
- Teaching basics (use Socratic)

## Core Structure

```
[QUESTION]
The specific tax question being analysed.

[FACTS]
Relevant facts; assumptions; limitations.

[ANALYSIS]
Application of law, guidance, or precedent.

[CONCLUSION]
Clear answer to the question; confidence level.

[NEXT STEPS]
Documentation requirements; further actions.

[APPENDICES]
Detailed authority references; calculations.
```

## Copy-Paste Prompt Template

```
You are a tax adviser. Write a tax technical note from:

QUESTION:
[The specific tax question]

SITUATION:
[Relevant facts]

JURISDICTION:
[Applicable law: UK, other]

KEY PRECEDENT OR GUIDANCE:
[Relevant court cases, tax guidance, etc.]

INSTRUCTIONS:
1. State the question clearly
2. Set out relevant facts
3. Analyse application of law to facts
4. State conclusion with confidence level
5. Identify remaining uncertainties
6. Suggest documentation approach
7. Keep professional but clear

Output only the tax note. No preamble.
```

## Short Example

**Tax Technical Note: Claim Date for Loss Relief**

**Question**
When a partnership makes an accounting loss in the year ended 31 December 2025, can the loss be claimed against prior-year profits for the year ended 31 December 2024?

**Facts**
- Partnership makes £200k accounting loss in year to 31 Dec 2025
- Partnership made £150k profit in year to 31 Dec 2024
- No prior loss carryforward
- Partnership is UK resident and not a limited partnership

**Analysis**

Under ITA 2007 s.83, a partnership loss can be carried back one year. The loss must arise from a trade; relief is automatic unless the partnership elects not to claim.

This loss (2025) is eligible for carry-back against the 2024 profit. The relief is restricted to the 2024 profit (£150k). The remaining loss (£50k) can be carried forward under s.83(2).

**Conclusion**

The partnership can claim:
• £150k loss relief against 2024 profit
• £50k carry-forward to 2026

Confidence level: High. Well-established relief under ITA 2007 s.83.

**Next Steps**

1. Ensure tax return for 2025 includes loss claim statement
2. Document loss calculation
3. Amend 2024 tax return (if filed) or notify HMRC of claim
4. Retain supporting working papers

---

See [prompt-templates/tax-note-prompts.md](../prompt-templates/tax-note-prompts.md) for more templates.

See [examples/tax-note.md](../examples/tax-note.md) for a complete example.
