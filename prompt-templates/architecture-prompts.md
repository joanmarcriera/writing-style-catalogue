---
title: Architecture Prompts
template_type: Architecture Decision Record (ADR)
use_case: Document a significant architecture or technical design decision, the context in which it was made, the alternatives considered, and the consequences — creating a permanent, searchable record for the team.
audience: Software engineers, solutions architects, technical leads, and future team members who need to understand why a design choice was made
output_format: Structured ADR with title, status, context, decision, rationale, trade-offs, consequences, and alternatives
---

# Architecture Prompts

## Purpose

An Architecture Decision Record (ADR) is a short document that captures a significant technical decision, the context that made it necessary, and the reasoning behind it. ADRs are not project documentation — they are durable records of the "why" behind a design, intended to be read by engineers who join the team months or years later and need to understand why the system is built the way it is. Write an ADR whenever a decision is significant enough that a future team member might question it, override it, or need to understand its consequences. Common triggers: choosing a cloud platform, selecting an authentication pattern, deciding between microservices and a monolith, adopting a new framework, or accepting a known trade-off. Keep ADRs short, honest, and permanent — once accepted, they should not be edited, only superseded by a new ADR.

## Copy-paste prompt

```
You are a senior solutions architect with experience writing Architecture Decision Records. Write a clear, concise ADR that captures a technical decision, the context that drove it, the alternatives considered, and the consequences for the team and system.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant information about the decision: the problem being solved, constraints, options evaluated, and the chosen approach):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 400–800 words; ADRs should be short]

FORMAT: [FORMAT — use the standard ADR format: Title / Status / Context / Decision / Rationale / Trade-offs / Consequences / Alternatives Considered]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Title the ADR as "ADR-[NNN]: [Short decision statement]" — e.g. "ADR-012: Use Azure AD B2C for Customer Identity and Access Management".
3. Status must be one of: Proposed / Accepted / Deprecated / Superseded by ADR-NNN.
4. Context: explain the situation that made this decision necessary. Include the constraints, requirements, and forces at play. A future reader should be able to understand why this was a real choice, not an obvious one.
5. Decision: state what was decided, precisely and in one or two sentences.
6. Rationale: explain why this option was chosen. This is the most important section — give the actual reasoning, not a post-hoc justification. If the decision involved genuine uncertainty or trade-offs between equally valid options, say so.
7. Trade-offs: be honest about what is being given up or accepted. An ADR that claims no trade-offs is not credible.
8. Consequences: describe what changes because of this decision — for the system, for the team, and for future decisions. Include both positive and negative consequences.
9. Alternatives Considered: list the other options evaluated, each with a brief note on why it was not chosen. Do not present alternatives as obviously inferior if they were genuinely competitive.
10. Preserve all factual content from the input — do not invent constraints, performance figures, or requirements.
11. Distinguish between facts (confirmed requirements or constraints), assumptions (estimates or inferences made during the decision), and recommendations (suggested actions going forward).
12. If there are material uncertainties that should be revisited, flag them explicitly.
13. Tone: [TONE — recommended: technical, direct, honest].
14. Length: [LENGTH].
15. Apply these constraints: [CONSTRAINTS].
16. Output only the ADR. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read the ADR now and in future. Examples: "current platform engineering team and future engineers joining the squad", "solutions architects across the organisation who may reference this pattern".
- `[PURPOSE]` — what decision is being recorded. Examples: "record the decision to use Azure AD B2C for customer IAM rather than a self-built solution", "document the choice to adopt an event-driven architecture for the payments pipeline".
- `[CONTEXT]` — background for the LLM. Examples: "the team is building a new customer portal for a regulated financial services firm; authentication must support MFA and comply with FCA digital identity guidance", "the existing monolith is causing deployment bottlenecks; the team is considering breaking it apart".
- `[INPUT]` — all the raw information: the problem being solved, the constraints that shaped the decision (time, budget, skills, regulation), the options evaluated, the chosen approach, and any performance data or proof-of-concept results.
- `[DESIRED_OUTCOME]` — what the ADR should achieve. Examples: "any engineer who joins the team in the next three years can understand why Azure B2C was chosen and what they should not change without first updating this ADR", "the architecture review board can assess and approve the decision".
- `[TONE]` — "technical, direct, honest". ADRs should not oversell decisions; they should inform.
- `[LENGTH]` — 400–800 words. ADRs are intentionally short. If the decision is complex enough to require more, consider whether it should be split into two records.
- `[FORMAT]` — use the standard ADR format above. Do not add unnecessary sections.
- `[CONSTRAINTS]` — examples: "use the organisation's ADR numbering convention (ADR-NNN)", "reference the relevant technical standard TS-IAM-003", "do not include vendor pricing information — this is commercially sensitive".

## Example input

```
AUDIENCE: Platform Engineering team (6 engineers, 2 architects) and future team members
PURPOSE: Record the decision to use Microsoft Entra External ID (formerly Azure AD B2C) for customer Identity and Access Management (IAM) on the Meridian customer portal
CONTEXT: Meridian Financial Services is building a new customer-facing portal to replace a legacy application. The portal will serve approximately 50,000 retail customers. The authentication solution must support: MFA, passwordless login, social identity (Google, Apple), fine-grained claims for downstream authorisation, and compliance with FCA Consumer Duty guidance on digital accessibility. The team had 8 weeks to evaluate options and begin implementation.
INPUT:
  Decision: Use Microsoft Entra External ID for customer IAM

  Options evaluated:
  1. Microsoft Entra External ID (formerly Azure AD B2C) — cloud-managed CIAM platform; supports all requirements; integrates with existing Azure estate; custom policies via Identity Experience Framework (IEF); estimated implementation: 6 weeks; annual cost at 50k MAU: ~£18k
  2. Auth0 (Okta) — strong CIAM platform; excellent developer experience; supports all requirements; not in existing estate; licensing model less predictable at scale; estimated implementation: 5 weeks; annual cost at 50k MAU: ~£28k–£35k depending on tier
  3. Self-built on ASP.NET Core Identity + OpenID Connect — full control; no licensing cost; significant build and maintenance overhead; estimated implementation: 16–20 weeks; ongoing maintenance burden on the team; regulatory compliance is the team's responsibility throughout

  Chosen option: Microsoft Entra External ID
  Reason: Best fit with existing Azure estate (SSO with staff directory, shared monitoring); lowest licensing cost; meets all requirements; IEF provides the custom claims enrichment needed for authorisation. Auth0 was close on capability but the licensing cost and absence of Azure integration were differentiating factors. Self-build was ruled out on timeline and maintenance risk.

  Known trade-offs:
  - IEF (custom policy language) has a steep learning curve; only two team members have experience with it
  - Vendor dependency on Microsoft
  - IEF tooling and debugging is weaker than Auth0's developer experience
DESIRED_OUTCOME: A clear, honest ADR that future engineers can use to understand the decision and its constraints.
TONE: Technical, direct, honest — no marketing language
LENGTH: 500–700 words
CONSTRAINTS: Use ADR-014 as the reference number. Note the IEF learning curve explicitly as a consequence.
```

## Example output

---

## ADR-014: Use Microsoft Entra External ID for Customer Identity and Access Management

**Status:** Accepted
**Date:** May 2026
**Authors:** Platform Engineering Team
**Applies to:** Meridian Customer Portal

---

### Context

The Meridian customer portal requires a customer identity and access management (CIAM) solution to handle authentication and authorisation for approximately 50,000 retail customers. The solution must support multi-factor authentication (MFA), passwordless login, social identity providers (Google, Apple), and the ability to enrich tokens with custom claims for downstream authorisation services. It must also comply with FCA Consumer Duty guidance on digital accessibility.

The team evaluated options over eight weeks. Key constraints were: alignment with the existing Azure estate, an 8-week implementation window before the portal development freeze, regulatory compliance (FCA), and a predictable licensing cost model.

---

### Decision

We will use **Microsoft Entra External ID** (formerly Azure AD B2C) as the CIAM platform for the Meridian customer portal.

---

### Rationale

Entra External ID meets all functional requirements and integrates natively with Meridian's existing Azure environment — sharing the monitoring estate (Azure Monitor, App Insights) and enabling single sign-on with the internal staff directory where needed. At 50,000 monthly active users (MAU), the annual cost is approximately £18k, which is the lowest of the viable options. Custom token enrichment is achievable via the Identity Experience Framework (IEF), which — while complex — provides the fine-grained claims control needed for the authorisation design.

Auth0 (Okta) was a close second on capability and has a stronger developer experience than IEF. It was not selected primarily because it sits outside the Azure estate (requiring separate monitoring and integration effort) and its licensing cost at scale is less predictable (estimated £28k–£35k/year).

A self-built solution using ASP.NET Core Identity was considered and ruled out. The 16–20 week implementation estimate exceeded the available window, and the ongoing maintenance and compliance burden on the team was assessed as unacceptable for a regulated environment.

---

### Trade-offs

- The Identity Experience Framework (IEF) has a steep learning curve. At the time of decision, only two team members had IEF experience. This is a genuine risk and is noted as a consequence below.
- Choosing a Microsoft-managed service creates a vendor dependency. Migration away from Entra External ID in future would be a significant undertaking.
- Debugging and local development tooling for IEF is weaker than Auth0's equivalent. Engineers should expect a slower initial development velocity on custom policies.

---

### Consequences

**Positive:**
- Native integration with the Azure monitoring estate — alerts, dashboards, and logs flow into existing tooling
- Predictable, low licensing cost at the current customer volume
- Reduced compliance overhead — Microsoft manages the platform's FCA-relevant security controls

**Negative / to manage:**
- IEF skill gap: the team must invest in training before or alongside implementation. At least three engineers should complete the Microsoft IEF learning path. *Assumption: this can be completed within the first two sprints.*
- All custom authentication logic must be implemented in IEF XML policy files — a proprietary format. Any engineer maintaining this system must learn IEF specifically.
- If Meridian's customer volume grows significantly beyond 50,000 MAU, licensing costs should be re-evaluated against Auth0 (Auth0's pricing may be more competitive at higher volumes).

---

### Alternatives Considered

| Option | Reason not selected |
|--------|-------------------|
| Auth0 (Okta) | Outside Azure estate; licensing cost £28k–£35k/year vs. £18k; strong developer experience but not a differentiator given the team's existing Azure fluency |
| Self-built (ASP.NET Core Identity + OIDC) | 16–20 week implementation exceeds available window; ongoing maintenance and regulatory compliance burden unacceptable for a team of this size |

---

## Review checklist

- [ ] ADR title follows the "ADR-NNN: [Decision statement]" convention
- [ ] Status is set explicitly (Proposed / Accepted / Deprecated / Superseded)
- [ ] Context explains the situation clearly — a future reader with no prior knowledge should understand why this was a real choice
- [ ] Decision is stated precisely in one or two sentences
- [ ] Rationale gives the actual reasoning — not a post-hoc justification
- [ ] Trade-offs are honest and specific — nothing is glossed over
- [ ] Consequences cover both positive and negative outcomes
- [ ] Alternatives section presents each option fairly with a clear reason for not selecting it
- [ ] Facts and assumptions are distinguishable
- [ ] British English used throughout
- [ ] Length is within the 400–800 word target

---

See [styles/architecture-decision-record-style.md](../styles/architecture-decision-record-style.md) for ADR style.

See [examples/architecture-decision-record.md](../examples/architecture-decision-record.md) for further examples.
