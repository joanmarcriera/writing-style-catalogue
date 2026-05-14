---
title: Board Paper Prompts
template_type: Board Paper
use_case: Write a comprehensive, governance-quality board paper that enables directors to make an informed decision on a significant strategic or operational matter.
audience: Board of Directors or equivalent governance body
output_format: Multi-section formal document with executive summary, background, option analysis, recommendation, risk assessment, and implementation plan
---

# Board Paper Prompts

## Purpose

A board paper is a formal governance document, not an email or a report. It must give directors everything they need to discharge their duty of care: sufficient context to understand the issue, an objective analysis of the options considered, a clear recommendation with rationale, and a transparent view of risks and their mitigations. Use this template for significant decisions — investment approvals, policy changes, strategic commitments, programme initiations, or any matter that requires a formal board resolution. The paper must work for a non-executive director who has not been involved in the day-to-day — it must stand alone, be accurate, and be honest about uncertainty.

## Copy-paste prompt

```
You are a governance specialist and expert board paper writer. Write a comprehensive, governance-quality board paper that enables directors to make a fully informed decision.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all background, analysis, options, financial data, and risk information to include):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 8–15 pages excluding appendices]

FORMAT: [FORMAT — recommended: executive summary / background / option analysis / recommendation / risk assessment / implementation plan / appendices]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Structure the paper in numbered sections with clear headings. Each section should be self-contained so that a reader can navigate to any section without losing meaning.
3. Open with a one-page executive summary that states: the issue, the board recommendation, the approval requested, and the key financial and risk implications. A director who reads only the executive summary should understand the decision they are being asked to make.
4. Present options objectively before giving the recommendation. Each option should include: a description, the key advantages, the key disadvantages, and the financial or resource implication. Do not present options as a formality — if two options are genuinely comparable, say so; if one is clearly inferior, explain why.
5. Make a single, clear recommendation with explicit rationale. If the recommendation involves trade-offs or residual uncertainty, state them plainly.
6. Distinguish clearly between facts (confirmed data), assumptions (estimates or projections used in the analysis), and recommendations (proposed actions). Use labels where helpful.
7. Include a risk section that identifies each material risk, its likelihood and potential impact (qualitative), and the proposed mitigation. Do not downplay risks to make the recommendation look stronger.
8. Include a proposed resolution for the board to pass (e.g. "The board resolves to approve...").
9. Avoid corporate filler and management-speak. Write plainly and precisely. A non-executive director with no technical background should be able to understand the paper without assistance.
10. Where projections or estimates are used, state the basis and any sensitivity. Do not present forecasts as certainties.
11. Tone: [TONE].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Do not invent financial figures, legal conclusions, market benchmarks, supplier claims, or regulatory obligations. If the input is missing material information, flag it in a "Missing information for review" section.
15. Output only the board paper. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — the governance body. Examples: "Group Board of Directors (eight members; mix of executive and non-executive)", "Audit and Risk Committee", "Investment Committee".
- `[PURPOSE]` — what the board is being asked to decide. Examples: "approve a £3.2M cloud migration programme", "endorse a new data governance policy", "authorise the acquisition of a minority stake in a software vendor".
- `[CONTEXT]` — the strategic and operational background. Examples: "the current on-premises data centre lease expires in December 2027", "three previous attempts at this integration have failed; this paper presents a revised approach".
- `[INPUT]` — all source material: financial models, feasibility reports, risk registers, prior board decisions, and any analysis. Paste or summarise the key content here.
- `[DESIRED_OUTCOME]` — what happens after the board reads the paper. Examples: "the board approves the recommendation and authorises the CEO to proceed", "the board requests further analysis on Option B before the September meeting".
- `[TONE]` — register to use. Board papers are almost always "formal, measured, and objective". Avoid advocacy in the body of the paper; the recommendation section is where you make your case.
- `[LENGTH]` — 8–15 pages is standard for a substantive board paper, excluding appendices.
- `[FORMAT]` — use the structure below; adapt section headings to match the organisation's house style if needed.
- `[CONSTRAINTS]` — restrictions. Examples: "do not include commercially sensitive vendor names in the main body — use Appendix A", "financial projections must reference the CFO sign-off date", "include a legal counsel note on regulatory implications".

## Example input

```
AUDIENCE: Group Board of Directors — Meridian Financial Services plc (nine members; Chair, four NEDs, CEO, CFO, CTO, General Counsel)
PURPOSE: Seek board approval to proceed with the Azure cloud migration programme and authorise £3.2M capital expenditure
CONTEXT: Meridian's current on-premises infrastructure (hosted in two leased data centres in London) is approaching end-of-life. The primary data centre lease expires in December 2027. The board agreed in principle at the September 2025 meeting to evaluate cloud options. A technical feasibility study has now been completed by the infrastructure team with support from external advisers.
INPUT:
  Feasibility study findings:
  - 147 workloads assessed; 112 (76%) cloud-compatible; 23 (16%) require refactoring; 12 (8%) legacy — decommission pre-migration
  - Preferred platform: Microsoft Azure (selected over AWS on cost, existing Microsoft licensing, and regulatory compliance posture)
  - Total migration cost: £3.2M over 24 months
  - Annual operating savings from Year 3: £1.8M (data centre lease, hardware maintenance, licensing)
  - NPV (5-year): £4.1M positive; IRR: 28%
  - Payback period: 26 months

  Options:
  Option A — Full cloud migration (recommended): migrate all compatible workloads; decommission legacy systems; exit both data centres by Dec 2027. Cost: £3.2M. Saves £1.8M/year from Year 3.
  Option B — Hybrid (partial migration): migrate 60% of workloads; retain one data centre. Cost: £2.1M. Saves £900k/year. Does not resolve the lease expiry risk.
  Option C — Do nothing / renew leases: estimated cost £5.8M over 5 years; no modernisation benefit; increasing operational risk as hardware ages.

  Key risks:
  - Data migration continuity (Medium likelihood / High impact) — mitigated by phased migration and rollback capability
  - Staff capability gap in cloud operations (Medium / Medium) — mitigated by structured training programme and retained managed service
  - Vendor lock-in (Low / Medium) — mitigated by Azure architecture designed for portability
  - Regulatory compliance during transition (Low / High) — mitigated by FCA pre-notification and external compliance review

  Resource needs: dedicated programme manager, external SI partner (procurement in progress), 4 FTE internal commitment

  Proposed resolution: "The Board resolves to approve the cloud migration programme (Option A) and authorises capital expenditure of £3.2M to be drawn down over financial years 2026–27 and 2027–28, subject to quarterly programme reporting to the Board."
DESIRED_OUTCOME: Board passes the proposed resolution at the June 2026 meeting.
TONE: Formal, measured, objective — appropriate for a regulated financial services plc
LENGTH: 10–12 pages
CONSTRAINTS: Include all financial figures and the NPV/IRR. Reference the FCA regulatory consideration. Note that the vendor selection analysis is in Appendix B.
```

## Example output

---

**MERIDIAN FINANCIAL SERVICES PLC**
**BOARD PAPER**

**Subject:** Cloud Infrastructure Migration Programme — Capital Expenditure Approval
**Paper reference:** BP-2026-14
**Date:** June 2026
**Prepared by:** Chief Technology Officer
**Status:** For decision

---

### 1. Executive Summary

Meridian's on-premises infrastructure is approaching end-of-life. The primary data centre lease expires in December 2027, and the hardware estate is beyond its planned replacement cycle. This paper presents the findings of a technical feasibility study and recommends that the board approve a full cloud migration to Microsoft Azure at a total cost of £3.2M over 24 months.

The programme will deliver annual operating savings of £1.8M from Year 3, a 5-year NPV of £4.1M, and an IRR of 28%, with a payback period of 26 months. The financial case is robust; the primary risks are manageable with established mitigations.

**The board is asked to pass the following resolution:**
*"The Board resolves to approve the cloud migration programme (Option A) and authorises capital expenditure of £3.2M to be drawn down over financial years 2026–27 and 2027–28, subject to quarterly programme reporting to the Board."*

---

### 2. Background and Strategic Context

Meridian operates 147 IT workloads across two leased data centres in London. The primary lease expires in December 2027. Hardware refresh costs are estimated at £1.2M if the current estate is maintained for a further five years. Operational risk is increasing as legacy systems age beyond vendor support.

The board noted at its September 2025 meeting that a cloud evaluation should be commissioned. The feasibility study was completed in April 2026 by the infrastructure team with support from external advisers (technical adviser report at Appendix A).

---

### 3. Workload Assessment

Of 147 workloads assessed:
- **112 (76%)** are directly cloud-compatible with minimal rework
- **23 (16%)** require moderate refactoring (estimated within the programme budget)
- **12 (8%)** are legacy systems that must be decommissioned or replaced before migration can proceed

The preferred cloud platform is Microsoft Azure, selected over Amazon Web Services on the basis of cost, Meridian's existing Microsoft enterprise licensing, and Azure's stronger compliance posture for UK financial services regulation. Full vendor selection analysis is at Appendix B.

---

### 4. Options Analysis

**Option A — Full cloud migration (recommended)**
Migrate all 135 compatible and refactored workloads to Azure; decommission 12 legacy systems; exit both data centres by December 2027.
- Cost: £3.2M over 24 months
- Annual savings from Year 3: £1.8M
- 5-year NPV: £4.1M positive; IRR: 28%; payback: 26 months
- Fully resolves lease expiry and hardware risk

**Option B — Hybrid (partial migration)**
Migrate approximately 60% of workloads; retain one data centre on a renewed lease.
- Cost: £2.1M
- Annual savings: £900k/year
- Does not resolve the December 2027 lease expiry; a further migration decision will be required within 3–4 years. Total 5-year cost is higher than Option A.

**Option C — Do nothing / renew both leases**
Renew both data centre leases and refresh hardware in place.
- Estimated 5-year cost: £5.8M
- No operational modernisation; increasing support risk as hardware ages further
- Does not address the strategic direction of the Group

*Assessment: Option A presents the strongest financial case and the only option that fully resolves the infrastructure risk. Option B defers rather than resolves the problem and costs more over a 5-year horizon.*

---

### 5. Recommendation

The board is recommended to approve **Option A** — full cloud migration to Microsoft Azure — and authorise capital expenditure of £3.2M over financial years 2026–27 and 2027–28.

**Rationale:** Option A delivers the strongest financial return, eliminates the infrastructure risk before the lease expiry, and positions Meridian for a modern, scalable operating model. The risk profile is manageable with the mitigations in section 6.

*Assumption: The £1.8M annual savings figure is based on current data centre lease costs, hardware maintenance contracts, and licensing spend. It has not been stress-tested against a significant change in Azure pricing. A 20% increase in cloud costs would reduce annual savings to approximately £1.4M — the programme would remain NPV-positive.*

---

### 6. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Data migration continuity | Medium | High | Phased migration; rollback capability at each stage; tested in pilot environment before main migration |
| Staff capability gap | Medium | Medium | Structured cloud training programme from Month 3; retained managed service for 12 months post-migration |
| Vendor lock-in | Low | Medium | Azure architecture designed for portability; key workloads containerised |
| Regulatory compliance during transition | Low | High | FCA pre-notification completed; external compliance review commissioned for Q3 2026 |

---

### 7. Implementation Approach

- **Month 1–2**: Programme initiation; programme manager appointment; SI partner contract
- **Month 3–6**: Legacy system decommission; Phase 1 (pilot — 30 workloads)
- **Month 7–18**: Phase 2 main migration (82 workloads)
- **Month 19–24**: Phase 3 final migration and data centre exit

Resource requirements: one dedicated programme manager, external SI partner (procurement under way), approximately 4 FTE internal commitment across the programme.

Governance: quarterly programme reports to the board; a programme initiation document will be presented at the September 2026 meeting.

---

### 8. Proposed Board Resolution

*"The Board resolves to approve the cloud migration programme (Option A) and authorises capital expenditure of £3.2M to be drawn down over financial years 2026–27 and 2027–28, subject to quarterly programme reporting to the Board."*

---

**Appendices**
- Appendix A: External technical adviser report (feasibility study)
- Appendix B: Vendor selection analysis (Azure vs. AWS)
- Appendix C: Full financial model (5-year NPV, sensitivity analysis)
- Appendix D: Risk register

---

## Review checklist

- [ ] Executive summary is self-contained — a director can read it alone and understand the decision
- [ ] All options are presented objectively before the recommendation
- [ ] Financial figures are accurate and the basis for projections is stated
- [ ] Facts, assumptions, and recommendations are clearly distinguishable
- [ ] A proposed board resolution is included and is precise
- [ ] Risks are identified with likelihood, impact, and mitigation — not minimised
- [ ] No unexplained jargon or acronyms
- [ ] British English spellings used throughout
- [ ] Length is within the 8–15 page target (excluding appendices)
- [ ] Appendices are listed and the main body references them correctly

---

See [styles/board-paper-style.md](../styles/board-paper-style.md) for detailed board paper style guide.

See [skills/create-board-pack.md](../skills/create-board-pack.md) for multi-part board pack creation.
