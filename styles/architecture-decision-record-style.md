---
title: Architecture Decision Record Style
category: Operational
best_for: Documenting significant technical decisions in a lightweight, persistent format that future team members and stakeholders can read to understand why a choice was made — not just what was chosen. Particularly valuable in fast-moving engineering teams where institutional knowledge is at risk of being lost as people join, leave, or move between teams.
not_good_for: Quick, low-stakes technical decisions that do not need a permanent record (use BLUF for communication of the decision); detailed implementation guides (use Technical Documentation); strategic business decisions with financial and governance implications (use Board Paper Style or Consulting Style).
default_tone: Factual and direct. Analytical but concise. Written for a future reader who was not in the room.
typical_length: 300–800 words; an ADR should fit on one to two pages
aliases: [ADR, Technical Decision Record, Architecture Record]
---

# Architecture Decision Record Style

## What this style is

An Architecture Decision Record (ADR) is a short, structured document that captures a significant technical decision, the context in which it was made, the reasoning behind it, and the consequences it creates. ADRs are typically stored in a repository alongside the code they relate to, and they accumulate over time to form a decision log that future engineers can read to understand why the system is the way it is.

The value of an ADR is not primarily in the decision it records — it is in the reasoning and context it preserves. Without ADRs, teams repeatedly ask "why was this done this way?" and either cannot find the answer, or spend time reconstructing an analysis that was already done. With ADRs, the reasoning is accessible to anyone who joins the team, regardless of when they join.

**Core principle**: Decision → Context → Consequence. A future team member who was not present should be able to read this ADR and understand why the decision was made, what trade-offs were accepted, and what constraints it places on future decisions.

## When to use it

- Major technology or framework choices (e.g. choice of database, message queue, authentication protocol)
- Significant architectural patterns or structural decisions (e.g. moving to event-driven architecture, adopting a monorepo)
- Trade-off decisions where alternatives were seriously considered and rejected
- Decisions that constrain future choices (e.g. "we will use PostgreSQL; therefore NoSQL is not available for new services")
- Reversals of previous decisions (a new ADR can supersede an old one)
- Technical strategy records that inform a roadmap (e.g. "we will use Kubernetes for all new workloads")

## When not to use it

- Quick, low-stakes technical decisions — use [BLUF](bluf-bottom-line-up-front.md) to communicate the decision; no permanent record needed
- Detailed implementation guides or how-to documentation — use [Technical Documentation](technical-documentation.md) instead
- Strategic business decisions with financial and governance implications — use [Board Paper Style](board-paper-style.md) instead
- Policy decisions — use [Policy Brief Style](policy-brief-style.md) instead

## Core structure

```
[TITLE]
"ADR-NNN: [Decision in past tense — one sentence]"
E.g. "ADR-0023: Adopted PostgreSQL as the primary data store for the analytics platform"
The title states what was decided — not the question that was being answered.

[STATUS]
Accepted | Proposed | Superseded by ADR-NNN | Deprecated

[DATE]
Date the decision was accepted (not the date the ADR was written).

[CONTEXT]
Why this decision was needed.
What problem or requirement triggered the decision.
Constraints that applied (technical, commercial, team capability, timeline).
Do not include the decision here — only the situation that required it.

[DECISION]
What was decided. One clear paragraph.
State the decision affirmatively: "We will use X" or "We have adopted Y."
Explain the primary reason for this choice (2–3 sentences).

[CONSEQUENCES]
What changes as a result of this decision.
Both positive consequences (what this enables or improves) and negative consequences (what is harder, more constrained, or ruled out).
Future decisions that are now constrained by this decision.
Operational or maintenance implications.

[ALTERNATIVES CONSIDERED]
Each alternative that was seriously evaluated.
For each: what it is, and the primary reason it was rejected.
Do not invent alternatives that were not genuinely considered.

[REFERENCES] (optional)
Links to supporting documents, discussions, or prior ADRs this supersedes.
```

## Copy-paste prompt

```
You are an experienced software architect. Your task is to write a well-structured Architecture Decision Record (ADR) from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Current and future members of the platform engineering team", "Any engineer or architect who works on this system in the next three years"]
PURPOSE: [PURPOSE — e.g. "Record the decision to use Okta as the identity provider for all new services, replacing the bespoke authentication library", "Document the choice of Kafka over RabbitMQ for the event streaming platform", "Record the decision to adopt a hexagonal architecture pattern for the new domain services"]
CONTEXT: [CONTEXT — e.g. "The team was choosing between three message queue options as part of the platform modernisation programme; the decision was made in April 2026 after a six-week evaluation"]
INPUT: [INPUT — paste all context notes, options evaluated, the decision made, the rationale, the trade-offs accepted, and the consequences expected here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "A future engineer joining the team can read this ADR and understand why Okta was chosen, what the trade-offs were, and what constraints the decision places on future identity work"]
TONE: [TONE — e.g. "Factual and direct — no advocacy; record what was decided and why", "Concise — written for a technical reader who is comfortable with the domain"]
LENGTH: [LENGTH — e.g. "300–600 words" or "Under one page"]
FORMAT: [FORMAT — standard ADR format: Title / Status / Date / Context / Decision / Consequences / Alternatives Considered]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not include alternatives that were not genuinely evaluated", "This ADR supersedes ADR-0011 — note this in the Status field", "Commercial sensitivity: do not include vendor pricing in the main ADR — reference Appendix A"]

INSTRUCTIONS:
1. Write the title as "ADR-NNN: [Decision in past tense]." The title states what was decided — not the question.
2. In Context, describe only the situation that required the decision — not the decision itself.
3. In Decision, state the choice affirmatively ("We will use X" or "We have adopted Y") and give the primary reason in 2–3 sentences.
4. In Consequences, cover both positive and negative consequences. Include future decisions that are now constrained.
5. In Alternatives Considered, include only alternatives that were genuinely evaluated. For each, give the primary reason for rejection in one to two sentences.
6. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
7. Preserve all technical facts exactly as provided in [INPUT]. Do not invent options, technical characteristics, or outcomes.
8. Distinguish confirmed facts from assumptions. Flag assumptions with "(assumed)" in parentheses.
9. Keep the ADR concise — it must fit on one to two pages. Do not pad.
10. The ADR should be readable by a future engineer three years from now who has no context — explain acronyms and initialisms on first use.

Output the ADR only. No preamble, no commentary.
```

## Output format

An ADR is typically a Markdown file stored in a repository alongside the code it relates to (commonly in a `/docs/decisions/` or `/adr/` directory). It is formatted as a flat document with no nesting beyond two levels of heading. It contains:

- **Filename**: `NNNN-brief-title.md` — e.g. `0023-adopt-postgresql-for-analytics.md`
- **Title**: H1 heading in the format "ADR-NNNN: [Decision]"
- **Status**: One word or phrase — Accepted, Proposed, Superseded (with link to superseding ADR)
- **Date**: ISO 8601 format (YYYY-MM-DD) of the decision date
- **Body sections**: H2 headings — Context, Decision, Consequences, Alternatives Considered
- **No sub-sections beyond H2**: ADRs are intentionally flat and brief

An ADR does not use tables, diagrams, or appendices in the main document (these may be linked as supporting documents). It is intentionally short — an ADR that grows beyond two pages is too long and should be split or summarised.

## Example

**ADR-0031: Adopted Okta as the Identity Provider for All New Services, Replacing the Bespoke Authentication Library**

**Status**: Accepted

**Date**: 2026-04-15

---

**Context**

The platform engineering team has been operating a bespoke Python authentication library (`auth-lib`) since 2019. The library handles JWT issuance, token validation, and session management for all internal services. It has accumulated significant technical debt: it lacks native support for OAuth 2.0 PKCE flow, does not support machine-to-machine authentication, and requires custom integration work for each new service that onboards. The library has no active maintainer — the original author left in 2024 and no team member has full knowledge of it.

In Q1 2026, the security team identified three vulnerabilities in `auth-lib` during a penetration test. Patching them required two weeks of senior engineering time. The team has flagged that ongoing maintenance of a bespoke authentication library is not a viable long-term strategy.

The IAM migration programme (completing Q2 2026) is introducing Okta as the company-wide identity platform. This creates an opportunity to standardise all service authentication on Okta rather than maintaining the parallel bespoke library.

**Decision**

We will migrate all new services to use Okta as the identity provider, using Okta's OAuth 2.0 / OIDC implementation for user authentication and Okta's Client Credentials flow for machine-to-machine authentication. Existing services will be migrated to Okta in a prioritised backlog starting Q3 2026.

The primary reasons for this decision: Okta eliminates the ongoing maintenance burden of `auth-lib`; it natively supports all required authentication flows; and it provides centralised audit logging required for our ISO 27001 compliance obligations.

**Consequences**

*Positive consequences:*
- Elimination of the `auth-lib` maintenance burden — estimated 15 engineering days per year recovered
- Centralised authentication audit log in Okta's event system — satisfies ISO 27001 control A.9.4.2
- Native support for MFA, conditional access, and federated identity — features that would require significant custom development in `auth-lib`
- Consistent authentication pattern across all services — reduces onboarding time for engineers new to the codebase

*Negative consequences and constraints:*
- All new services must integrate with Okta — self-hosted or alternative identity providers are not available for new services without an explicit exception approved by the architecture review board
- Okta introduces a vendor dependency — if Okta experiences an outage, all services relying on it for authentication will be affected; we must ensure our service degradation design accounts for this
- Existing services using `auth-lib` will require migration effort — this is a planned cost, not an incidental one; a migration roadmap is maintained by the IAM team
- Monthly Okta cost will increase by approximately £800/month as new services are onboarded (assumed — based on per-application pricing)

**Alternatives Considered**

*Keycloak (self-hosted open-source IdP)*
Evaluated during Q4 2025. Rejected because: self-hosting introduces operational complexity the infrastructure team does not have capacity to absorb; the security team requires IdP audit logs to be managed externally for independence; the team has no Keycloak expertise and ramp-up would delay the IAM programme by at least two months.

*Retain and modernise `auth-lib`*
Evaluated as an option during Q1 2026. Rejected because: the penetration test vulnerabilities revealed that the library's security model is structurally weak, not merely out of date; patching individual vulnerabilities does not address the architectural root cause; the library lacks an active maintainer; and the cost of a full rewrite equals or exceeds the cost of Okta over a three-year horizon.

*AWS Cognito*
Briefly considered in Q4 2025. Not fully evaluated because: the Company has standardised on Azure Active Directory for directory services; Okta integrates natively with Azure AD whereas Cognito would require a separate federation layer. Cognito may be reconsidered if the Company migrates directory services to AWS in future.

---

**References**
- Supersedes: ADR-0008 (Auth-lib as the standard authentication library — accepted 2019-03-12)
- Related: IAM Migration Programme brief (Board paper, January 2026)
- Security assessment: Penetration test report, February 2026 (restricted — contact CISO for access)

## Quality checklist

- [ ] Title states the decision in past tense — "ADR-NNN: Adopted X" not "ADR-NNN: Should we use X?"
- [ ] Status is clearly stated: Accepted, Proposed, or Superseded (with link to superseding ADR)
- [ ] Context describes the situation — not the decision
- [ ] Decision is stated affirmatively in one clear paragraph
- [ ] Consequences include both positive and negative consequences
- [ ] Future constraints introduced by this decision are explicitly stated
- [ ] Only alternatives that were genuinely evaluated are listed
- [ ] Each alternative has a clear reason for rejection
- [ ] ADR fits on one to two pages — it is concise
- [ ] A future engineer reading this three years from now will understand why the decision was made

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Title is a question ("Should we use X?") | The ADR records the decision — not the deliberation | State the decision: "ADR-0023: Adopted X as Y" |
| Decision is unclear | Future team does not know what was decided | State the decision in one sentence: "We will use X for Y" |
| Context section includes the decision | Confuses the record | Context is only the situation — the decision comes in the Decision section |
| Only positive consequences listed | Incomplete and misleading — omits constraints placed on future decisions | Always include negative consequences and future constraints |
| Alternatives that were not genuinely evaluated | Artificial padding; reduces credibility | Only include alternatives the team actually considered |
| ADR is too long | No longer serves as a lightweight reference | Keep to one to two pages; link to supporting documents |
| Jargon or acronyms unexplained | Future reader (or reader from another team) cannot follow | Explain acronyms on first use |

---

See [skills/create-adr.md](../skills/create-adr.md) for ADR generation skills.

See [examples/architecture-decision-record.md](../examples/architecture-decision-record.md) for a complete example.
