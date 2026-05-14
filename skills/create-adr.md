---
title: Create ADR
skill_type: Document generation
output: An Architecture Decision Record documenting the context, options considered, decision made, and consequences — as a permanent record of why a technical choice was made
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor, Git repository or Confluence
difficulty: Easy
---

# Skill: Create ADR (Architecture Decision Record)

## What this skill does

Documents a significant technical or architectural decision in a structured, permanent format that captures not just what was decided but why — including the alternatives that were rejected. ADRs prevent the repeated re-litigation of old decisions by giving future teams the full context. A well-written ADR is concise (1–2 pages), written close to the time of the decision, and stored alongside the code or system it relates to. It is a log entry, not a report — once accepted, it should not be edited; superseded decisions should be linked to a new ADR.

## When to use it

- Making a significant technology or framework selection (database engine, cloud provider, authentication protocol, API design pattern)
- Choosing an architectural pattern that will constrain future development (event-driven vs. request-response, monolith vs. microservices)
- Documenting the outcome of a technical spike or proof of concept that drives a directional decision
- Recording a deliberate non-decision or a decision to accept technical debt with a documented rationale
- Preserving institutional knowledge before an architecture review or a team restructure

## Inputs required

- The specific decision being made — stated as a complete sentence ("We will use Azure AD B2C for external customer authentication")
- The context that made this decision necessary — the technical problem, constraint, or opportunity
- 2–3 alternatives that were genuinely evaluated (not just mentioned to appear thorough)
- The chosen option and the primary reasons for choosing it
- The most significant trade-offs or downsides of the chosen option
- The expected consequences — what changes because of this decision
- The status: Proposed (not yet accepted), Accepted, Deprecated, or Superseded

## Copy-paste prompt

```
You are a software architect. Write an Architecture Decision Record (ADR) for the decision described below.

AUDIENCE: [Current and future engineers and architects who need to understand this decision]
PURPOSE: [To document a technical decision permanently so it is not re-litigated and its context is not lost]
CONTEXT: [The technical problem, constraint, or opportunity that made this decision necessary; system architecture context]
INPUT: [The decision made; the alternatives evaluated; the rationale for choosing this option; the known trade-offs and consequences]
DESIRED_OUTCOME: [A permanent, searchable record that explains why this decision was made and what was rejected]
TONE: Neutral, factual, and precise. ADRs are technical records — avoid advocacy; present the reasoning objectively.
LENGTH: 400–600 words. 1–2 pages maximum.
FORMAT: Use the standard ADR template below. Use H2 for section headers. Use bullet lists for options, pros, and cons. Include a status indicator.
CONSTRAINTS: Use British English. Write in past tense for context and analysis; present tense for status and consequences. Do not use ADR jargon — write clearly enough for a new team member to understand. Output only the ADR; no preamble.

STRUCTURE:
# ADR-[NUMBER]: [Short Decision Title]

**Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]
**Date**: [Date]
**Authors**: [Names or team]
**Deciders**: [Who approved this decision]

## Context
[What situation, problem, or constraint made this decision necessary? Include system architecture context.]

## Decision
[State the decision clearly in one sentence: "We will [action] using [approach]."]

## Alternatives considered

### Option A: [Name]
[Description]
- **Pros**: [bullet list]
- **Cons**: [bullet list]

### Option B: [Name]
[Description]
- **Pros**: [bullet list]
- **Cons**: [bullet list]

### Option C (chosen): [Name]
[Description]
- **Pros**: [bullet list]
- **Cons / trade-offs**: [bullet list]

## Rationale
[Why was Option C chosen? What factors were most decisive? What constraints ruled out other options?]

## Consequences
[What changes because of this decision? What becomes easier? What becomes harder? What technical debt is accepted?]

## Related decisions
[Links to related ADRs, RFCs, or design documents]
```

## Suggested output structure

- **Title** — ADR number and a concise decision title (not a topic label)
- **Status block** — status, date, authors, deciders
- **Context** — the problem or constraint; enough background that someone unfamiliar with the system understands why this decision was needed
- **Decision** — one clear sentence stating what was decided
- **Alternatives considered** — 2–3 options with balanced pros and cons for each; avoid making rejected options look strawman
- **Rationale** — the 2–3 decisive factors; acknowledge trade-offs honestly
- **Consequences** — concrete effects: what is now constrained, what is enabled, what requires follow-up work
- **Related decisions** — links to predecessor or successor ADRs

## Quality controls

- [ ] The decision is stated as a complete action sentence, not a topic label
- [ ] At least two genuine alternatives are documented with honest pros and cons
- [ ] The rationale section explains the decisive factors — not just "it was the best option"
- [ ] Consequences include at least one constraint or trade-off accepted (no decision is free)
- [ ] Status is set correctly — a decision in discussion should be Proposed, not Accepted
- [ ] The ADR is written at the time of the decision, not reconstructed months later
- [ ] ADR number follows the team's numbering convention and is filed in the correct location

## Common failure modes

- **Decision statement too vague**: "We will use a cloud-native approach" is not a decision — "We will use Azure Kubernetes Service (AKS) for all containerised workloads" is
- **Alternatives not genuinely evaluated**: Listing alternatives with no pros and just cons makes the ADR look like post-hoc justification — show the genuine strengths of each option
- **Consequences section missing**: Every architectural decision constrains something — if you cannot identify a consequence, you have not thought hard enough; common consequences include vendor lock-in, migration complexity, and required skills changes
- **ADR written too late**: An ADR written 6 months after the decision relies on memory and misses the true context — write it within a week of the decision, ideally the same day
- **Too long**: ADRs that run to 5+ pages are not read — the value of an ADR is that it can be read in 5 minutes; move detail to appendices or design documents

## Example request

"Write an ADR for our decision to use Azure AD B2C for external customer identity and access management. Context: we are building a B2C portal for 50,000 external users and need an identity provider that handles registration, MFA, and social login without us building and maintaining it ourselves. Alternatives evaluated: Auth0 (too expensive at scale), AWS Cognito (we are primarily Azure and would create multi-cloud complexity), Azure AD B2C (chosen — Azure-native, cost effective at our scale, supports custom policies and social login). Key trade-off: custom policy language (XML-based) is complex. Status: Accepted. Authors: Platform Architecture team."
