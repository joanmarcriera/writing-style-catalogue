---
title: Board Paper Workflow
category: Workflow
---

# Workflow: Creating a Board Paper

A board paper is a formal governance document that enables a board of directors to make an informed decision on a significant matter. It is not a report, a briefing note, or a PowerPoint — it is a structured document with a defined format that presents the decision being sought, the analysis supporting it, and a clear recommendation. A board paper that is too long will not be read in full; one that is too thin will not have the evidence to carry a decision. This workflow takes you from a raw brief to a board-ready paper in 3–4 weeks.

## Style to use

[Board Paper Style](../styles/board-paper-style.md) — formal, measured, and structured. Board papers use numbered sections, avoid contractions, reference financial data precisely, and lead every section with its conclusion. Do not use Smart Brevity or BLUF style for board papers — the board expects a document format it can navigate, annotate, and retain as a governance record.

## Skill to use

[Create Board Pack](../skills/create-board-pack.md) — use this skill to assemble the full pack, including the cover letter, agenda, individual papers, and decision templates. For a single paper within an existing pack, use [Create Business Case](../skills/create-business-case.md) if the paper is seeking a financial approval.

## Prompt template to start from

[Board Paper Prompts](../prompt-templates/board-paper-prompts.md)

## Inputs required

Before drafting, you must have:
- A precise statement of the decision the board is being asked to make
- The strategic context (how this connects to a board-approved strategy)
- 2–3 options with financial implications for each, including "do nothing"
- Your recommended option and the primary reasons for it
- A risk assessment (top 5–8 risks with mitigations and owners)
- Financial figures reviewed and signed off by the finance team
- Legal or compliance flags, if any — reviewed by counsel
- The proposed resolution wording (the exact text of the motion to be passed)

## Copy-paste master prompt

```
You are a company secretary and governance specialist. Write a formal board paper for the matter described below.

AUDIENCE: Board of directors — [describe board composition: e.g. independent NEDs with financial services background; executive directors CTO and CFO]
PURPOSE: To enable the board to make an informed decision on [specific matter] at the [date] board meeting.
CONTEXT: [Organisation type, size, sector; any prior board discussions or resolutions related to this matter; any regulatory or compliance context]
INPUT:
Decision sought: [The exact decision the board is being asked to make]
Background: [Why this matter is before the board now; what has changed]
Option 1 — Do nothing: [Description; financial implications; risks of inaction]
Option 2 — [Alternative]: [Description; financial implications; risks]
Option 3 — Recommended: [Description; financial implications; rationale for recommendation]
Risks: [Top 5–8 risks with likelihood, impact, owner, and mitigation]
Financial data: [Relevant figures — verified by finance team]
Proposed resolution: [Draft resolution wording for the board minute]
DESIRED_OUTCOME: The board reads this paper, has sufficient information to debate the options, and passes the proposed resolution.
TONE: Formal and precise. Board papers are governance documents — language must be unambiguous. Use numbered sections. Avoid contractions and colloquial expressions.
LENGTH: 8–12 pages excluding appendices.
FORMAT: Numbered sections (1. Executive Summary; 2. Background; 3. Options Analysis; 4. Recommendation; 5. Financial Implications; 6. Risk Assessment; 7. Implementation; 8. Proposed Resolution). Financial data in clearly labelled tables. Appendices for supporting detail.
CONSTRAINTS: Use British English. All financial figures in £ with two decimal places. Every claim backed by data. Do not present only one option — options analysis must show genuine alternatives. Output only the board paper; no preamble.
```

## Step-by-step process

1. **Week 1 — Define the decision** (2 hours): Write a single, precise sentence stating what the board is being asked to decide. If you cannot state it in one sentence, you do not yet know what the paper is for. Identify 2–3 genuine alternatives including "do nothing."

2. **Week 1 — Gather supporting data** (4–8 hours over the week): Collect financial data (have finance review all figures), legal or compliance input (have counsel review any legal implications), and operational evidence (data, benchmarks, risk register). Do not draft until you have this material.

3. **Week 2 — Draft with the prompt** (3–4 hours): Use the master prompt above. Populate all INPUT fields with your gathered data. The LLM will produce a structured draft — treat it as a first draft requiring expert review, not a finished paper.

4. **Week 2–3 — Internal review** (2–4 hours of review time plus revision): Circulate to: CFO (financial accuracy), legal counsel (legal/compliance sections), and the paper's executive sponsor. Set a clear deadline for feedback. Incorporate all substantive comments; document why any feedback was not incorporated.

5. **Week 3 — Pre-board briefing** (1 hour): Brief the board chair on the paper's content. The chair should not encounter surprises in the meeting. Address any reservations the chair raises before the meeting — either in the paper or via a separate conversation.

6. **Week 4 — Final polish and distribution** (2 hours): Run the review checklist below. Convert to PDF. Distribute via the board portal or secure email at least 5 working days before the meeting.

7. **Board meeting — Present and decide** (15–20 minutes): Present the executive summary (5 minutes). Open for questions (10 minutes). Propose the resolution. Record the decision and any material discussion points in the minutes.

**Total time: 3–4 weeks from initiation to board meeting**

## Review checklist

- [ ] The decision being sought is stated in one precise sentence in the executive summary
- [ ] At least three options are presented, including "do nothing" with its costs and risks
- [ ] All financial figures have been reviewed and approved by the finance team
- [ ] Legal or compliance implications have been reviewed by counsel
- [ ] The proposed resolution wording is legally correct and unambiguous
- [ ] The paper is under 12 pages excluding appendices
- [ ] The board chair has been briefed and has no unresolved concerns
- [ ] Distributed at least 5 working days before the board meeting

## Example output excerpt

> **2. Background**
>
> 2.1 The company operates on-premise infrastructure at two co-location sites under contracts expiring in September 2025. The current annual cost of these contracts is £1.22M, comprising hosting fees (£740k), maintenance (£290k), and support services (£190k).
>
> 2.2 In October 2024, the Board approved a preliminary assessment of cloud migration options. That assessment, completed in February 2025 by the Infrastructure team with support from an external cloud adviser, concluded that a phased migration to Microsoft Azure would reduce ongoing infrastructure costs by approximately £800k per annum from 2027, with a one-off migration investment of £2.1M.
>
> 2.3 The board is now asked to approve Phase 1 of the migration programme — the migration of non-critical development and test environments — at a cost of £600k, to be funded from the 2025/26 capital budget.
