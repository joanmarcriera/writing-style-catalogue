---
title: IAM Strategy Workflow
category: Workflow
---

# Workflow: Identity & Access Management Strategy

An IAM (Identity and Access Management) strategy document defines how an organisation controls who has access to what systems, data, and resources — and how that access is governed over time. IAM sits at the intersection of security, compliance, IT operations, and HR, which means the strategy must speak to all of those audiences simultaneously. This workflow covers the development of the strategy document itself, the executive briefing that justifies the investment, and the technical and change management communications that follow approval.

## Style to use

[Executive Briefing Style](../styles/executive-briefing.md) for the board/executive approval document — formal, structured, conclusion-first, with a financial case. [Technical Documentation](../styles/technical-documentation.md) for the architecture design document and implementation guide. [Narrative Storytelling](../styles/narrative-storytelling.md) for the change management communication to staff — IAM changes affect how people log in and access systems every day, and they respond better to "here is why this is happening and what it means for you" than to a policy document.

## Skill to use

[Create Business Case](../skills/create-business-case.md) for the investment justification. [Create Roadmap](../skills/create-roadmap.md) for the 12–24 month implementation timeline. [Create Training Material](../skills/create-training-material.md) for the staff awareness and admin training. [Create Playbook](../skills/create-playbook.md) for the IAM incident response and operational playbook. [Create Risk Register](../skills/create-risk-register.md) for the programme risk documentation.

## Prompt template to start from

[Strategy Prompts](../prompt-templates/strategy-prompts.md) for the strategy document itself. [Board Paper Prompts](../prompt-templates/board-paper-prompts.md) for the executive approval document.

## Inputs required

Before beginning, gather:
- Current state assessment: how is identity and access currently managed? What tools, processes, and gaps exist?
- Compliance and regulatory requirements: ISO 27001, SOC 2, Cyber Essentials Plus, FCA requirements, or sector-specific mandates
- Security incident history: any access-related incidents or near-misses in the past 24 months
- Technology landscape: current identity providers, directory services, SSO solutions, and privileged access tools
- Headcount and user types: employees, contractors, service accounts, third-party vendors
- Target state: what does mature IAM look like for your organisation? What are the gaps?
- Budget and resource constraints
- Stakeholder map: who owns identity (IT, CISO, HR, Compliance)?

## Copy-paste master prompt

```
You are a cybersecurity consultant and IAM specialist. Produce an IAM strategy document for the organisation described below.

AUDIENCE: [Who this strategy is for — e.g. CISO and executive team for approval / IT leadership team for planning / Board for budget sign-off]
PURPOSE: To define how the organisation will manage identity and access over the next [12/24/36] months; to justify the investment required; and to provide a clear implementation roadmap.
CONTEXT: [Organisation size, sector, regulatory environment; current IAM maturity level; any recent security incidents or audit findings; technology stack]
INPUT:
Current state: [Describe current identity providers, directory services, access review processes, privileged access controls, and key gaps]
Compliance requirements: [List applicable standards and their IAM-specific requirements]
Target state: [Describe the desired IAM capabilities — e.g. single identity provider, automated provisioning/deprovisioning, PAM solution, ZTNA, regular access reviews]
Programme scope: [List the IAM workstreams — e.g. PAM, Identity Governance, ZTNA, User Awareness]
Roadmap: [Phases with timelines and dependencies]
Investment: [Budget required, broken down by phase and type — people, tools, implementation]
DESIRED_OUTCOME: [Approved strategy and budget / Aligned technical team / Staff prepared for changes]
TONE: [Formal and evidence-led for executive/board / Technical and precise for implementation team / Clear and reassuring for staff]
LENGTH: [Strategy document: 10–15 pages / Executive briefing: 3–5 pages / Staff communication: 1 page]
FORMAT: [Strategy: numbered sections with roadmap table / Executive briefing: business case format / Staff comms: FAQ or narrative]
CONSTRAINTS: Use British English. Do not use jargon without definition for non-technical audiences. Every investment item must have a justification. Output only the document; no preamble.
```

## Step-by-step process

1. **Phase 1 — Current state assessment** (2 weeks):
   - Interview stakeholders: CISO, Head of IT, HR (for joiners/movers/leavers process), Compliance, key business unit leads
   - Audit current IAM tools and processes: directory services, SSO, MFA, PAM, access review process
   - Review incident history for access-related events
   - Map current-state capability against your target framework (e.g. NIST Identity Framework, Microsoft Zero Trust)
   - Identify and prioritise gaps

2. **Phase 2 — Strategy development** (2–3 weeks):
   - Define target state for each IAM domain: Identity Governance, Access Management, Privileged Access, Authentication, Directory Services
   - Build the implementation roadmap: phases, dependencies, milestones
   - Develop the investment case: tools, implementation, staffing, training costs by phase
   - Write the strategy document using the master prompt with [Create Business Case](../skills/create-business-case.md)
   - Build the 24-month roadmap using [Create Roadmap](../skills/create-roadmap.md)

3. **Phase 3 — Stakeholder communication** (2–3 weeks):
   - **Executive briefing** (3–5 pages): strategic rationale, investment required, expected benefits (compliance, security, efficiency), risks of inaction, proposed resolution. Use [Executive Briefing Style](../styles/executive-briefing.md)
   - **Technical deep-dive** (for IT and security team): architecture design, tool selection rationale, integration approach, phase-by-phase technical requirements
   - **Change management plan** (for HR and comms): how changes will affect staff (new login processes, MFA, access changes); timeline; training and support available

4. **Phase 4 — Approval and planning** (1–2 weeks):
   - Present to executive team or board using [Create Slide Deck](../skills/create-slide-deck.md)
   - Secure budget allocation and programme mandate
   - Establish programme governance: steering group, workstream leads, reporting cycle
   - Produce project initiation document

5. **Phase 5 — Implementation** (12–24 months):
   - Execute by workstream: PAM first (highest security impact), then Identity Governance, then ZTNA
   - Produce phase-specific runbooks and SOPs using [Create Runbook](../skills/create-runbook.md) and [Create SOP](../skills/create-sop.md)
   - Train IT staff using [Create Training Material](../skills/create-training-material.md)
   - Monthly steering group meetings with [Create Meeting Pack](../skills/create-meeting-pack.md)
   - Quarterly board reporting using [Create Executive Memo](../skills/create-executive-memo.md)

**Total time: 6–10 weeks to approval; 12–24 months for full implementation**

## Review checklist

- [ ] Current state assessment is based on direct observation or interviews — not assumptions
- [ ] Target state is specific and measurable — not "improve our IAM posture" but "automate provisioning for 95% of joiners, reduce provisioning time from 5 days to 4 hours"
- [ ] Compliance requirements are mapped to specific IAM controls — not just listed
- [ ] Investment is broken down by phase and type; verified by finance
- [ ] Risk of inaction is quantified — what is the financial or reputational exposure of not acting?
- [ ] The roadmap is realistic — phases have named owners and the timeline accounts for procurement, configuration, testing, and training
- [ ] Staff impact is addressed — the change management plan exists before implementation begins
- [ ] British English throughout; technical terms defined for non-technical audiences

## Example output excerpt

> **3. Strategic objectives**
>
> The IAM programme has four strategic objectives, each linked to a measurable outcome:
>
> | Objective | Current state | Target state | Timeline |
> |-----------|---------------|--------------|----------|
> | Reduce provisioning time | 5 business days | 4 hours (automated) | Q2 2026 |
> | Close compliance gaps | 6 open ISO 27001 controls | Zero open controls | Q4 2025 |
> | Eliminate shared credentials | 47 shared admin accounts identified | Zero shared accounts | Q1 2026 |
> | Achieve Cyber Essentials Plus | Not certified | Certified | Q3 2025 |
>
> Achieving these objectives requires a phased investment of £1.4M over 24 months, delivering estimated annual risk-adjusted benefits of £620k — a payback period of 27 months.
