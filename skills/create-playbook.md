---
title: Create Playbook
skill_type: Document generation
output: A structured collection of named "plays" — specific, reusable response strategies for recurring scenarios — with trigger conditions, step-by-step actions, templates, and success metrics
tools_needed: LLM (Claude/ChatGPT/Gemini), Confluence, Notion, or Word
difficulty: Medium
---

# Skill: Create Playbook

## What this skill does

Documents a set of repeatable, proven response strategies (called "plays") for specific recurring scenarios that require a consistent, high-quality response. Each play defines when to use it (trigger), what to do (steps), any templates or scripts, and how to measure success. Unlike a runbook (which is for operational emergencies) or an SOP (which documents a single process), a playbook is modular — plays can be combined, adapted, and selected based on context. A security incident response playbook might contain plays for ransomware, data exfiltration, and phishing — each distinct but drawing on shared escalation protocols.

## When to use it

- Creating an incident response playbook for a security operations or infrastructure team covering named incident types
- Building a sales playbook that equips account managers with specific plays for different buyer types, objections, or deal stages
- Documenting a crisis communications playbook for a PR or executive team facing scenarios like service outages, regulatory investigations, or leadership changes
- Producing a client onboarding playbook for a professional services team so every engagement starts consistently
- Developing a cloud migration playbook that defines plays for different migration pattern types (lift-and-shift, re-platform, greenfield)

## Inputs required

- The domain the playbook covers (incident response, sales, crisis communications, etc.)
- The specific scenarios or play types to include (not "all possible scenarios" — define the scope)
- For each play: the trigger condition, the response steps, any decision points, templates or scripts, success criteria
- The intended users: their role, experience level, and time constraints during execution
- Any shared resources (escalation contacts, communication templates, approval authorities) that apply across multiple plays
- The review and versioning process

## Copy-paste prompt

```
You are an experienced practitioner in [domain]. Create a professional playbook for the scenarios described below.

AUDIENCE: [Who will use this playbook — role, experience level, and context of use (under pressure vs. planned)]
PURPOSE: [What the playbook enables — consistent response, faster resolution, quality assurance, knowledge preservation]
CONTEXT: [Domain and organisational context; any relevant policies, tools, or escalation structures]
INPUT: [List the plays to include; for each play: trigger condition, key steps, decision points, templates needed, success criteria]
DESIRED_OUTCOME: [A practitioner can pick up this playbook, find the relevant play, and execute it correctly without asking for guidance]
TONE: Practical and direct. Playbooks are used under pressure — every word must earn its place.
LENGTH: Introduction and shared resources section (1 page), then one section per play (1–2 pages each).
FORMAT: H2 for each play name. Each play includes: trigger, context, step-by-step actions (numbered), decision points, templates or scripts, success metrics, and review notes.
CONSTRAINTS: Use British English. Steps must be specific enough to be followed without interpretation. Decision points must specify the exact condition and the exact consequence. Templates must be complete and copy-paste ready. Output only the playbook; no preamble.

PLAY STRUCTURE:
## Play [Number]: [Play Name]
**Trigger**: [The specific condition that activates this play]
**Context**: [What situation this play addresses; any prerequisites]
**Owner**: [Role responsible for executing this play]

### Steps
1. [Action — specific, verb-led]
2. [Action — specific, verb-led]

### Decision point
If [condition A] → [specific action]
If [condition B] → [specific action]

### Template / Script
[Copy-paste ready template or communication script]

### Success criteria
[Measurable definition of a successfully completed play]
```

## Suggested output structure

- **Playbook header** — domain, scope, version, owner, review date
- **How to use this playbook** — brief instructions for navigating the plays; index of plays
- **Shared resources** — escalation contacts, communication channels, approval authorities, key tools — referenced by all plays
- **Play 1–N** — each play containing trigger, context, owner, steps, decision points, templates, and success criteria
- **After-action review** — instructions for capturing lessons learned after a play is executed
- **Version history** — track changes; note which plays were added, updated, or retired

## Quality controls

- [ ] Every play has a clear, specific trigger — not "when things go wrong" but "when [named alert fires / [named condition] occurs]"
- [ ] Steps are numbered, verb-led, and specific enough to follow without interpretation
- [ ] Every decision point specifies both the condition and the consequence ("If X → do Y; if not X → do Z")
- [ ] Templates are complete and copy-paste ready — not placeholders requiring significant drafting under pressure
- [ ] Success criteria are measurable — not "issue resolved" but "service health metric returns to baseline; no new incidents within 4 hours"
- [ ] Shared resources (contacts, channels, tools) are current and reviewed quarterly
- [ ] Version and last-reviewed date appear on the cover page

## Common failure modes

- **Plays too generic**: A play called "Handle security incident" is not a play — it is a category. "Respond to suspected ransomware infection on endpoint" is a play that can be executed
- **Steps require knowledge not documented**: "Escalate to the on-call engineer" requires knowing who the on-call engineer is — include a reference to a live rota or named contact list
- **Templates missing**: A comms play that says "send notification to affected users" without providing a template will produce inconsistent, panicked communications under pressure
- **Playbook never tested**: A playbook that has not been used in a table-top exercise or real scenario will fail at its first real application — test every play before declaring the playbook production-ready
- **Too many plays**: A playbook with 30 plays is not navigable under pressure — scope it to the 8–12 most common or most critical scenarios; create separate playbooks for other domains

## Example request

"Create a security incident response playbook for our cloud infrastructure team. Plays to include: (1) Suspected ransomware on endpoint; (2) Suspected data exfiltration; (3) Privileged account compromise; (4) Azure service outage (Microsoft-side). For each play: trigger is a named alert in Microsoft Sentinel; response steps must include isolation, investigation, containment, and communication. Include a communication template for each play. Success criteria: incident closed in ServiceDesk with full timeline documented. Audience: Tier 2 security analysts and on-call cloud engineers. British English."
