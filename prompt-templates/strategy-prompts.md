---
title: Strategy Prompts
template_type: Strategic Analysis / Strategy Document
use_case: Write a rigorous strategic analysis or recommendation that frames a business question clearly, examines options honestly, and makes a well-reasoned recommendation with an implementation path.
audience: Senior leadership, executive teams, boards, or strategy committees
output_format: Multi-section strategy document with issue framing, findings, option analysis, recommendation, implementation approach, and success metrics
---

# Strategy Prompts

## Purpose

A strategy document is not a slideshow with bullets — it is a structured argument. Use this template when you need to think through and communicate a significant strategic question: entering a new market, making a build-versus-buy decision, responding to a competitive threat, restructuring a business unit, or defining a multi-year technology direction. The output should work for a senior audience that will challenge the argument: it must be logically sound, evidenced, honest about trade-offs, and clear about what it recommends and why. The Minto Pyramid principle applies — lead with the recommendation, then build the argument beneath it.

## Copy-paste prompt

```
You are a strategy consultant with experience advising senior leadership on significant business and technology decisions. Write a rigorous, well-structured strategic analysis that frames the issue, examines the options, and makes a clear, well-reasoned recommendation.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant background: business context, market information, data, constraints, options under consideration, and any existing analysis):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 1,500–2,500 words]

FORMAT: [FORMAT — recommended: Issue / Context and Findings / Strategic Options / Analysis of Trade-offs / Recommendation / Implementation Approach / Success Metrics]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a clear statement of the strategic question being addressed. The reader should know immediately what decision or choice this document is about.
3. Lead with the recommendation (Minto Pyramid). State what you recommend in the first section, then build the argument. Do not save the recommendation for the end.
4. Distinguish clearly between: facts (confirmed information from the input), assumptions (estimates or inferences — label as "Assumption:"), and recommendations (proposed actions).
5. Present two or three genuine strategic options. Each option should be fairly characterised — do not frame alternatives as obviously inferior just to make the recommendation look stronger. If the evidence genuinely points strongly to one option, explain that clearly.
6. Analyse the trade-offs for each option. What does each option give up? What does it require? What could go wrong?
7. The recommendation must include explicit rationale — not just "Option A is best" but why, and against what criteria.
8. Where relevant, include financial or operational impact (quantified where data is provided; qualified where it is not). Do not invent numbers — if figures are not available, say so and explain what would be needed to produce them.
9. The implementation section should be specific enough to be actionable: what are the first three to five steps, who owns them, and what is the timeline?
10. Define success metrics that are measurable. "Improved performance" is not a metric; "reduce average identity provisioning time from 4 hours to under 30 minutes within 6 months" is.
11. If there is material uncertainty in the analysis — market data that is incomplete, assumptions that are load-bearing, risks that are hard to quantify — acknowledge it clearly rather than papering over it.
12. Avoid empty strategy language: no "leverage", "synergies", "best-in-class", "transformational", "game-changing". Be precise.
13. Tone: [TONE].
14. Length: [LENGTH].
15. Apply these constraints: [CONSTRAINTS].
16. Output only the strategy document. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read and act on this document. Examples: "IT Leadership Team and CIO at Meridian Financial Services", "Group Board and executive committee", "the product strategy committee making a build-versus-buy decision".
- `[PURPOSE]` — the strategic question being answered. Examples: "determine whether to build or buy an IAM platform for the next five years", "assess the strategic case for entering the SME tax advisory market", "define a three-year cloud strategy for the Group IT function".
- `[CONTEXT]` — the business, market, and operational context. Examples: "Meridian currently manages identity manually across 12 systems; the team spends approximately 30% of its time on provisioning and deprovisioning tasks", "two competitors have launched AI-assisted tax advisory tools in the past 12 months".
- `[INPUT]` — all source material: existing analysis, data, stakeholder views, market research, financial data, operational constraints, and any prior work.
- `[DESIRED_OUTCOME]` — what should happen after the reader finishes. Examples: "the IT Leadership Team agrees on an IAM direction and can proceed to vendor evaluation", "the board approves the market entry strategy and allocates budget".
- `[TONE]` — almost always "analytical, direct, measured" for strategy documents. Avoid advocacy in the analysis sections — save that for the recommendation.
- `[LENGTH]` — 1,500–2,500 words for a substantive strategy paper. A shorter briefing note may be 800–1,200 words.
- `[FORMAT]` — use the recommended structure; adapt headings to the organisational context.
- `[CONSTRAINTS]` — examples: "do not include specific vendor names — use generic descriptions", "the budget ceiling is £2M — options above this are out of scope", "must address the regulatory requirement for data residency in the UK".

## Example input

```
AUDIENCE: IT Leadership Team (CIO, Head of Infrastructure, Head of Security, Head of Applications) at Meridian Financial Services
PURPOSE: Determine the strategic direction for Identity and Access Management (IAM) for the next five years — specifically, whether to continue with the current fragmented approach, consolidate on a COTS platform, or build a centralised IAM service in-house
CONTEXT: Meridian currently manages staff identity across 12 systems, with no central directory for cloud applications. The IT team spends an estimated 30% of its time on manual provisioning and deprovisioning. Three security incidents in 2025 were directly attributable to stale access not being revoked (audit finding AF-2025-08). The organisation is migrating to Azure (cloud migration programme approved, June 2026). FCA digital operational resilience requirements (aligned to DORA) require improved access control visibility by Q4 2026.
INPUT:
  Current state problems:
  - No central identity platform for cloud applications
  - Manual provisioning across 12 systems; average provisioning time: 4 hours; deprovisioning: 48+ hours
  - Three 2025 security incidents linked to stale access (audit finding AF-2025-08)
  - FCA DORA-aligned requirements: documented access controls and automated deprovisioning by Q4 2026

  Options:
  Option A — COTS IAM platform (recommended by IT team): Deploy Microsoft Entra ID (+ Entra Governance) as the central IAM platform, integrated with the Azure migration. All 12 systems federated via SAML/OIDC. Automated provisioning via HR system integration. Cost: £220k implementation + £85k/year licensing.
  Option B — Build in-house: Build a central identity service using open-source tooling (Keycloak + custom orchestration). Full control; no licensing. Cost: £480k+ implementation; ongoing engineering overhead estimated at 1–1.5 FTE.
  Option C — Status quo / incremental improvement: Continue with current approach; make targeted improvements to the worst-performing systems. Low upfront cost; does not address FCA compliance deadline or audit finding.

  Key data:
  - Current provisioning cost (staff time): estimated £180k/year
  - Option A expected to reduce provisioning time to <30 minutes, deprovisioning to <1 hour
  - Option A timeline: 9 months to full deployment
  - Option B timeline: 18–24 months (estimated; no prior delivery of similar scope)
DESIRED_OUTCOME: The IT Leadership Team agrees to proceed with Option A and approves the next steps (vendor engagement, programme initiation).
TONE: Analytical, direct, clear — no management-speak
LENGTH: 1,500–2,000 words
CONSTRAINTS: Reference audit finding AF-2025-08 and the FCA DORA deadline. Do not include vendor pricing from sources other than those in the input.
```

## Example output

---

# IAM Strategic Direction — Five-Year Recommendation

**Prepared for:** IT Leadership Team, Meridian Financial Services
**Date:** May 2026
**Author:** [Strategy Lead]

---

## Recommendation

Meridian should deploy Microsoft Entra ID with Entra Governance as the central IAM platform (Option A), integrated with the approved Azure cloud migration. This is the only option that meets the FCA compliance deadline, resolves the audit finding, and does so within a commercially viable timeline and cost envelope.

The implementation should begin in Q3 2026. The programme manager appointment and vendor engagement are the critical first steps.

---

## Issue

Meridian's identity and access management is fragmented across 12 systems with no central control point. The consequences are material: three 2025 security incidents were directly attributable to stale access not being revoked (audit finding AF-2025-08), and the IT team spends an estimated 30% of its time on manual provisioning and deprovisioning tasks at an estimated annual cost of £180k.

The FCA's DORA-aligned digital operational resilience requirements — specifically, documented access controls and automated deprovisioning — must be met by Q4 2026. The current state cannot meet that deadline.

This paper assesses three strategic options and recommends one.

---

## Context and Findings

**Current state — provisioning**
Manual provisioning across 12 systems averages four hours per user. Deprovisioning averages 48+ hours and is not fully automated, creating an ongoing window of exposure when staff leave or change roles.

**Regulatory position**
The FCA DORA-aligned requirement for automated access control and deprovisioning must be demonstrably met by Q4 2026. Option C (status quo) fails this test. Option B (build in-house) cannot be delivered within the required timeline. *Assumption: the Q4 2026 deadline is firm; any slippage would need to be agreed directly with the FCA and is not assumed to be available.*

**Strategic alignment**
The cloud migration programme (approved June 2026) is moving Meridian to Azure. An IAM strategy that is not Azure-native would create integration complexity and additional cost. Option A aligns natively with the Azure direction; Options B and C do not.

---

## Strategic Options

### Option A — Microsoft Entra ID with Entra Governance (recommended)
Deploy Microsoft Entra ID as the central identity platform and Entra Governance for automated lifecycle management. All 12 systems federated via SAML/OIDC. Provisioning automated via integration with the HR system.

- **Cost**: £220k implementation + £85k/year licensing
- **Timeline**: 9 months to full deployment
- **Expected outcome**: provisioning time reduced to <30 minutes; deprovisioning to <1 hour; full audit trail for FCA

### Option B — Build in-house (Keycloak + custom orchestration)
Build a centralised identity service using open-source tooling. No licensing cost; full control over the architecture.

- **Cost**: £480k+ implementation; ongoing 1–1.5 FTE engineering overhead
- **Timeline**: 18–24 months (estimated; no comparable delivery on record)
- **FCA compliance**: cannot be delivered by Q4 2026

### Option C — Status quo with incremental improvement
Continue with the current approach; make targeted improvements to the highest-risk systems.

- **Cost**: Low upfront; estimated £180k/year in continuing staff overhead
- **Timeline**: N/A
- **FCA compliance**: does not meet the DORA access control requirements by Q4 2026

---

## Analysis of Trade-offs

**Option A** is the most commercially viable and the only one that meets the regulatory deadline. The trade-off is vendor dependency on Microsoft and a licensing commitment. Given Meridian's Azure migration, this dependency is already structurally present — this option deepens it in a direction that is already approved strategy. The implementation timeline of 9 months is achievable; it is tighter than ideal and requires a dedicated programme manager and prompt vendor engagement.

**Option B** would provide maximum control and avoids licensing costs, but at a significantly higher implementation cost (£480k+ vs. £220k) and an 18–24 month delivery estimate that misses the FCA deadline by 6–15 months. Building IAM in-house also introduces a permanent engineering overhead of 1–1.5 FTE — resource Meridian does not currently have on the team. If the build is delayed or encounters technical complexity (both realistic risks for a first-time delivery of this scope), the FCA exposure increases materially.

**Option C** resolves nothing. It does not address the audit finding, does not meet the FCA deadline, and continues the £180k/year operational overhead. The three 2025 incidents indicate that the current approach is not merely inefficient — it is a source of active risk.

---

## Recommendation and Rationale

**Recommendation: Proceed with Option A.**

Option A is recommended on four grounds:

1. **Regulatory compliance**: it is the only option that can meet the Q4 2026 FCA deadline
2. **Risk reduction**: automated deprovisioning directly addresses audit finding AF-2025-08
3. **Strategic alignment**: Microsoft Entra integrates natively with the Azure migration programme already under way
4. **Commercial case**: at £220k implementation plus £85k/year, and assuming a reduction in provisioning-related staff overhead from £180k to approximately £60k/year (based on provisioning time reduction to <30 minutes), the programme pays back within approximately 30 months

*Assumption: the £180k/year current provisioning cost is an estimate based on 30% of IT team time. A more precise figure would require a time-tracking exercise, but the order of magnitude is consistent with provisioning volumes reported by the team.*

---

## Implementation Approach

**Month 1–2 (Q3 2026)**
- Appoint programme manager
- Engage Microsoft Entra specialist SI partner (two shortlisted; assessment to complete in June)
- Conduct HR system integration scoping (provisioning automation depends on HR data quality — a data cleanse may be needed before integration)

**Month 3–5**
- Deploy Entra ID; federate the four highest-risk systems (those with the longest deprovisioning times)
- Run pilot with one business unit (200 users)

**Month 6–9**
- Roll out federation across all 12 systems
- Enable Entra Governance lifecycle policies
- Conduct FCA compliance evidence collection (audit trail, policy documentation)

**Month 10 onwards**
- Business-as-usual; quarterly access reviews via Entra Governance
- Decommission redundant identity stores in federated systems

---

## Success Metrics

| Metric | Current baseline | Target (Month 9) |
|--------|-----------------|-----------------|
| Average provisioning time | 4 hours | <30 minutes |
| Average deprovisioning time | 48+ hours | <1 hour |
| Stale access incidents | 3 in 2025 | 0 |
| FCA compliance evidence readiness | Not available | Full audit trail in place |
| IT team time on manual provisioning | ~30% | <10% |

---

## Review checklist

- [ ] Recommendation is stated upfront — not at the end
- [ ] Issue is framed clearly — the reader understands why this decision is needed
- [ ] All three options are characterised fairly before the recommendation
- [ ] Trade-offs are specific and honest — nothing is minimised to strengthen the recommendation
- [ ] Facts, assumptions, and recommendations are clearly distinguishable
- [ ] Financial figures are used only where provided in the input
- [ ] Implementation steps are specific and actionable, with owners implied
- [ ] Success metrics are measurable — not vague
- [ ] No management-speak or empty strategy language
- [ ] British English used throughout

---

See [styles/consulting-style.md](../styles/consulting-style.md) for consulting-style analysis.

See [styles/minto-pyramid-principle.md](../styles/minto-pyramid-principle.md) for logical argument structure.
