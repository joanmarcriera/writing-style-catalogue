---
title: Technical Documentation
category: Specialist
best_for: Explaining how a system, process, API, or technology works to an audience with sufficient technical background to implement, operate, or troubleshoot it. Ideal for runbooks, architecture guides, API references, setup guides, and infrastructure documentation that engineers, DevOps teams, or architects will rely on during their daily work.
not_good_for: Executive audiences who need a summary and recommendation rather than technical detail (use Executive Briefing or Smart Brevity); beginners who need step-by-step guided learning (use Tutorial Style); policy or compliance documents for non-technical audiences (use Plain English or Policy Brief Style).
default_tone: Precise and objective. Professional without being formal. Neutral and authoritative.
typical_length: 500–5,000 words depending on scope; runbooks tend toward 500–1,500 words; architecture guides toward 2,000–5,000 words
aliases: [Technical Writing, Engineering Docs, Runbook, Architecture Guide]
---

# Technical Documentation

## What this style is

Technical documentation explains how a system or process works with enough precision that a qualified reader can implement, operate, or troubleshoot it without external assistance. It is the reference layer of technical knowledge — the document that an engineer reads when they need to understand a system they did not build, when they join a new team, or when something breaks at 2am.

Good technical documentation is organised around the reader's tasks, not the system's internal structure. It assumes the reader has relevant domain expertise but does not assume they know this particular system. It is precise about version numbers, configuration values, and error messages. It gives real examples that can be copied and used, not illustrative pseudocode. And it is honest about what it does not cover — missing documentation is better signposted than silently absent.

**Core principle**: Explain exactly how something works with enough precision and completeness that a qualified reader can implement, operate, or troubleshoot it without external help.

## When to use it

- System architecture documentation for engineering teams and new joiners
- API documentation for internal or external developers consuming a service
- Operational runbooks for on-call engineers responding to incidents
- Technical specifications for systems being designed or procured
- Infrastructure and deployment documentation (cloud, Kubernetes, CI/CD)
- Configuration guides for tools, platforms, or integrations
- Troubleshooting guides capturing known failure modes and their resolution

## When not to use it

- Executive updates on technical matters — use [Smart Brevity](axios-smart-brevity.md) or [Executive Briefing](executive-briefing.md) instead
- Teaching beginners who need guided learning — use [Tutorial Style](tutorial-style.md) or [Socratic Explainer](socratic-explainer.md) instead
- Policy or compliance documents for non-technical audiences — use [Plain English](plain-english.md) or [Legal Professional Style](legal-professional-style.md) instead
- Quick decisions or recommendations — use [BLUF](bluf-bottom-line-up-front.md) instead

## Core structure

```
[OVERVIEW]
What this document covers.
Who should read it and when.
What the reader will be able to do after reading it.
Scope: what is and is not covered.

[PREREQUISITES]
Required knowledge: what the reader must already know.
Required access or permissions.
Required tools or software and their versions.
External dependencies or accounts needed.

[ARCHITECTURE OR CONCEPTUAL OVERVIEW] (for system documentation)
How the system is structured.
Key components and their relationships.
Data flows or sequence diagrams where helpful.

[CORE EXPLANATION]
How the system or process works, in the reader's operational sequence.
Break into headed sub-sections for each major function or component.
Include configuration examples with real values.

[COMMON USE CASES OR PROCEDURES]
The 3–5 most common tasks a reader will use this document for.
Each as a mini-procedure: goal, steps, expected outcome.

[TROUBLESHOOTING]
Known failure modes with their symptoms.
Root cause and resolution for each.
Where to look for logs, alerts, or diagnostic information.

[REFERENCE]
Complete API endpoints, CLI commands, or configuration parameters.
Error codes and their meaning.
Links to external documentation (version-pinned where possible).

[GLOSSARY] (optional)
Terms specific to this system or domain.
```

## Copy-paste prompt

```
You are an expert technical writer. Your task is to write technical documentation from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Senior infrastructure engineers with three or more years of Kubernetes experience", "Backend developers consuming the payments API for the first time", "On-call engineers who may not be familiar with this specific service"]
PURPOSE: [PURPOSE — e.g. "Document the IAM platform's SCIM provisioning integration so engineers can configure new identity providers without involving the security team", "Write an on-call runbook for the payment processing service", "Document the cloud network architecture for the new AWS landing zone"]
CONTEXT: [CONTEXT — e.g. "This replaces tribal knowledge currently held by two engineers; we need it documented before the team expands", "The service has had three incidents in the past month; engineers are spending too long diagnosing the same failure modes"]
INPUT: [INPUT — paste all architecture notes, code snippets, configuration examples, known issues, and any existing documentation here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "An engineer new to this service can understand its architecture, configure a basic integration, and diagnose the five most common failure modes without asking for help"]
TONE: [TONE — e.g. "Precise and authoritative", "Neutral and factual", "Helpful without being condescending — assumes domain expertise but not system knowledge"]
LENGTH: [LENGTH — e.g. "1,000–2,000 words" or "One runbook of 800–1,200 words"]
FORMAT: [FORMAT — e.g. "Markdown with headed sections, code blocks for all commands and config, tables for reference material"]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not include any internal IP addresses or production credentials — use placeholders", "All code examples must use the v2 API — the v1 API is deprecated", "Must be suitable for publication in our public developer documentation"]

INSTRUCTIONS:
1. Begin with an Overview section that states what this document covers, who should read it, and what they will be able to do after reading it.
2. List all prerequisites explicitly: assumed knowledge, required access, required tools with version numbers.
3. Organise the core explanation around the reader's operational sequence — what they will do first, second, third — not the system's internal structure.
4. Include real, working code examples or configuration snippets from [INPUT]. Do not use pseudocode or illustrative placeholders unless [INPUT] does not contain real examples — in that case, flag the gap explicitly.
5. Cover the 3–5 most common use cases as short procedures: goal, numbered steps, expected outcome.
6. Include a Troubleshooting section covering the most common failure modes from [INPUT] with symptoms, root cause, and resolution.
7. Include a Reference section for any API endpoints, CLI commands, or configuration parameters.
8. Use British English throughout (colour, organisation, licence, favour, analyse, etc.).
9. Preserve all technical claims exactly as provided in [INPUT]. Do not invent version numbers, URLs, configuration values, or error messages. Flag any gaps in [INPUT] explicitly.
10. Distinguish confirmed technical facts from assumptions. Flag assumptions with "(assumed)" in parentheses.

Output the technical documentation only. No preamble, no commentary.
```

## Output format

Technical documentation is typically published in Markdown (for version control and developer portals), Confluence, or a documentation platform such as ReadTheDocs or GitBook. The format contains:

- **Headed sections**: H1 for the document title; H2 for major sections; H3 for sub-sections
- **Code blocks**: All commands, configuration snippets, API payloads, and file contents in fenced code blocks with language identifier (e.g. ` ```yaml `)
- **Tables**: Used for reference material — API parameters, error codes, configuration options
- **Numbered lists**: For any sequential procedure
- **Bullet points**: For non-sequential lists (prerequisites, features, options)
- **Note or warning callouts**: For important cautions (e.g. "This action cannot be undone")
- **Internal links**: Between sections for navigability

Length varies by scope: a runbook is typically 800–1,500 words; an architecture guide 2,000–5,000 words; an API reference can be longer. Each section should stand alone to the degree possible — engineers often link directly to the Troubleshooting or Reference section.

## Example

**IAM Platform — SCIM Provisioning Integration Guide**
*Applies to: Okta Identity Engine v3.4+ | Last updated: May 2026*

---

**Overview**

This document covers the configuration of SCIM 2.0 provisioning between Okta and downstream applications that support automated user lifecycle management. After reading this guide, an engineer should be able to: configure a new SCIM integration from scratch, enable group-based provisioning, and diagnose the five most common provisioning failures.

This guide does not cover Okta SSO configuration (see: SSO Integration Guide) or LDAP synchronisation (see: Legacy Directory Integration Guide).

**Prerequisites**

- Okta administrator access (Super Admin or Application Admin role required)
- Target application with SCIM 2.0 endpoint URL and bearer token — obtain from the application vendor or your team's secrets vault
- Understanding of SCIM 2.0 schema: Users, Groups, and the `/Users` and `/Groups` endpoints
- The Okta SCIM provisioning feature must be enabled on your Okta tenant (confirm with the Identity team)

**How SCIM Provisioning Works**

Okta acts as the SCIM client (the provisioning source). When a user is assigned to an application in Okta — either directly or via a group — Okta sends a `POST /Users` request to the application's SCIM endpoint to create the user account. When the user is removed or deactivated, Okta sends a `PATCH /Users/{id}` with `"active": false` to deactivate the account.

The provisioning flow is:
1. User is assigned to app in Okta (directly or via group membership)
2. Okta evaluates the user's profile attributes against the app's attribute mapping
3. Okta sends `POST /Users` to the SCIM endpoint
4. Application creates the account and returns `201 Created` with the new user's SCIM ID
5. Okta stores the SCIM ID for future updates and deprovisioning

**Configuring a SCIM Integration**

Step 1: Add the SCIM endpoint to Okta

In the Okta Admin Console, navigate to **Applications → Applications → [Your App] → Provisioning → Integration**.

```
SCIM connector base URL: https://scim.example.invalid/scim/v2
Unique identifier field for users: userName
Authentication mode: HTTP Header
Authorization: Bearer <your-bearer-token>
```

Click **Test Connector Configuration**. You should receive: `{"status": "success", "message": "Connector configuration test succeeded"}`.

If you receive a `401 Unauthorized`, the bearer token is incorrect or expired. Obtain a fresh token from the application vendor or secrets vault.

Step 2: Enable provisioning actions

Under **Provisioning → To App**, enable:
- **Create Users** — required for automated onboarding
- **Update User Attributes** — required to keep profile data in sync
- **Deactivate Users** — required for automated offboarding

Do not enable **Sync Password** unless the application explicitly supports Okta-managed passwords.

**Common Failure Modes**

*Symptom: User not provisioned after assignment*

Check the Okta provisioning logs: **Reports → System Log → filter by "provision user"**. Common causes:

| Error | Root Cause | Resolution |
|-------|-----------|------------|
| `400 Bad Request: userName already exists` | User with this username exists in the target app outside of Okta provisioning | Manually link existing account: import the user, then assign |
| `401 Unauthorized` | Bearer token expired | Rotate token in secrets vault; update in Okta app configuration |
| `503 Service Unavailable` | SCIM endpoint is down | Check application health; provisioning will retry automatically |
| `409 Conflict: email already in use` | Target app enforces unique email across tenant | Ensure Okta username format matches target app's requirements |

*Symptom: User deactivated but account remains active in target app*

Confirm **Deactivate Users** is enabled in Provisioning → To App. If enabled, check the system log for `deactivate user` events — if none are present, the assignment was not removed in Okta (the user may have been removed at the directory level instead).

**Reference: SCIM Endpoints**

| Endpoint | Method | Purpose |
|---------|--------|---------|
| `/scim/v2/Users` | GET | List all provisioned users |
| `/scim/v2/Users` | POST | Create a new user |
| `/scim/v2/Users/{id}` | GET | Get a specific user by SCIM ID |
| `/scim/v2/Users/{id}` | PATCH | Update user attributes or deactivate |
| `/scim/v2/Groups` | GET | List all provisioned groups |
| `/scim/v2/Groups/{id}` | PATCH | Add or remove group members |

All requests require the `Authorization: Bearer <token>` header. All responses are `application/scim+json`.

## Quality checklist

- [ ] Overview states clearly what the document covers, who it is for, and what the reader will be able to do
- [ ] Prerequisites are explicit: assumed knowledge, access, tools, and version numbers
- [ ] Core explanation follows the reader's operational sequence — not the system's internal structure
- [ ] All code examples, commands, and configuration snippets are real and copy-paste ready (not pseudocode)
- [ ] Troubleshooting covers the most common failure modes with symptoms and resolution
- [ ] Reference material is complete and consistent (endpoints, parameters, error codes)
- [ ] No unexplained jargon or acronyms for the stated audience level
- [ ] Links and version numbers are current and correct
- [ ] British English used throughout
- [ ] Assumptions are flagged; gaps in source information are noted explicitly

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Assumes too much system knowledge | Readers get lost and cannot use the document | State prerequisites clearly; write for someone new to this system |
| Pseudocode or illustrative examples | Cannot be copied and used; readers must guess real syntax | Use real, working examples from the actual system |
| No troubleshooting section | Readers stuck when something breaks — the most common reason they are reading the document | Add the most common failure modes with symptoms and resolution |
| Structure follows system internals, not reader tasks | Hard to find the information you need | Organise around what the reader is trying to do |
| Outdated code examples or version references | Readers follow incorrect guidance | Pin version numbers; review when system changes |
| Missing prerequisite access or tool requirements | Reader cannot start | List all prerequisites including access levels and tool versions |
| No scope statement | Reader unsure if this document covers their use case | State explicitly what is and is not covered |

---

See [prompt-templates/technical-documentation-prompts.md](../prompt-templates/technical-documentation-prompts.md) for more templates.

See [examples/technical-runbook.md](../examples/technical-runbook.md) for a complete example.
