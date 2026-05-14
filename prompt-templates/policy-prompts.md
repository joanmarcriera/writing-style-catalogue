---
title: Policy Prompts
template_type: Policy Document / Policy Brief
use_case: Write a clear, enforceable organisational policy or a structured policy brief that analyses a policy question, presents options, and recommends an approach.
audience: Employees (for policy documents) or decision-makers and leadership teams (for policy briefs)
output_format: Structured policy document with purpose, scope, policy statements, and responsibilities — or a policy brief with issue, evidence, options, and recommendation
---

# Policy Prompts

## Purpose

Policies are different from guidelines: a policy sets out mandatory requirements, whereas a guideline offers recommended practice. Use the policy document prompt when you need to write or update an organisational policy that employees or contractors must comply with — for example, an information security policy, an acceptable use policy, an expense policy, or an access control policy. Use the policy brief prompt when you are advising a decision-maker on a policy question and need to present options, analyse trade-offs, and make a recommendation. Both types of output must be clear, unambiguous, and actionable. A policy that cannot be followed or enforced is worse than no policy.

## Copy-paste prompt — Organisational policy document

```
You are an experienced policy writer. Write a clear, enforceable organisational policy document.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all relevant requirements, regulatory obligations, existing rules, and any draft content to incorporate):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 600–1,500 words depending on scope]

FORMAT: [FORMAT — recommended: Policy Header / Purpose / Scope / Definitions / Policy Statements / Responsibilities / Compliance and Exceptions / Review Date]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a policy header: policy title, version number, effective date, review date, policy owner, and approval authority.
3. Purpose: one to three sentences stating what this policy covers and why it exists. Do not pad — state the intent plainly.
4. Scope: define precisely who and what this policy applies to (e.g. all employees, contractors, third parties with access to systems; all systems processing personal data). Also state any explicit exclusions.
5. Definitions: define any terms that could be ambiguous or that have a specific meaning in the context of this policy.
6. Policy statements: write each requirement as a clear, active statement of obligation. Use "must", "must not", "shall", or "is required to" rather than "should" or "is encouraged to" — unless the statement is genuinely aspirational rather than mandatory. Each statement should be testable: it should be possible to determine whether someone is complying or not.
7. Responsibilities: list the specific obligations of each role mentioned in the policy (e.g. all staff, line managers, IT department, policy owner).
8. Compliance and exceptions: state what happens if the policy is not followed (e.g. disciplinary action, access revocation), and how exceptions can be requested and approved.
9. Review date: all policies must have a stated review date. Annual review is standard; more frequent for high-risk areas.
10. Preserve all requirements and obligations from the input — do not omit regulatory or legal requirements.
11. Distinguish between mandatory requirements ("must") and recommended practice ("should") — use them deliberately and consistently.
12. Do not write the policy as a narrative or essay. Use numbered or bulleted statements where possible.
13. Tone: [TONE — recommended: formal, clear, precise].
14. Apply these constraints: [CONSTRAINTS].
15. Output only the policy document. No preamble.
```

## Copy-paste prompt — Policy brief

```
You are a policy analyst. Write a structured policy brief that analyses a policy question, presents options with trade-offs, and makes a clear recommendation.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (the policy question, relevant evidence, options under consideration, and any constraints):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 800–1,500 words]

FORMAT: [FORMAT — recommended: Policy Issue / Context and Significance / Evidence / Policy Options / Analysis of Trade-offs / Recommendation / Implementation Approach]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Frame the policy issue clearly at the outset — a single sentence stating the question being addressed.
3. Present evidence objectively. Where evidence is contested or incomplete, say so — do not present a one-sided evidence base as settled.
4. Present two or three genuine policy options. Each option should be characterised fairly: what it is, who it affects, its advantages, and its disadvantages.
5. Analyse trade-offs for each option — who bears the cost, who benefits, and what risks does each option carry?
6. Make a single recommendation with clear rationale. If the evidence is genuinely uncertain, acknowledge that.
7. Include implementation considerations: what would be needed to put the recommended approach into effect?
8. Distinguish facts (confirmed data), assumptions (inferences or estimates), and recommendations.
9. Tone: [TONE — recommended: analytical, balanced, precise].
10. Apply these constraints: [CONSTRAINTS].
11. Output only the policy brief. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — for a policy document: "all Meridian Financial Services employees, contractors, and third-party service providers with access to company systems". For a policy brief: "Chief Information Security Officer and IT Leadership Team".
- `[PURPOSE]` — what the policy or brief covers. Examples: "set out the mandatory requirements for privileged access management across all Meridian IT systems", "advise on whether to adopt a BYOD (bring your own device) policy for mobile access".
- `[CONTEXT]` — background. Examples: "this policy replaces version 2.1 (effective January 2024); the update is required to incorporate FCA DORA operational resilience requirements", "the IT team has received 40+ requests for mobile access from staff working remotely; a policy decision is needed before the next board meeting".
- `[INPUT]` — source material: existing policy drafts, regulatory requirements, audit findings, stakeholder views, or technical constraints.
- `[DESIRED_OUTCOME]` — what the output should achieve. Examples: "a policy that is clear enough to be followed by a non-technical employee without further guidance", "a brief that enables the CISO to make a recommendation to the board in under 10 minutes of reading".
- `[TONE]` — policy documents: "formal, clear, precise". Policy briefs: "analytical, balanced, precise".
- `[LENGTH]` — policy documents: 600–1,500 words (longer for complex, multi-area policies). Policy briefs: 800–1,500 words.
- `[FORMAT]` — use the recommended structures above.
- `[CONSTRAINTS]` — examples: "must align with ISO 27001:2022 controls", "must reference the FCA DORA operational resilience requirements", "use the organisation's standard policy template header (version, owner, approval authority)".

## Example input — Policy document

```
AUDIENCE: All Meridian Financial Services employees, contractors, and third-party providers with access to company IT systems
PURPOSE: Define the mandatory requirements for privileged access management (PAM) across all Meridian IT systems
CONTEXT: Following audit finding AF-2025-08 (three security incidents attributable to stale privileged access), the Head of Information Security is required to produce an updated Privileged Access Management Policy by 30 June 2026. The previous policy (version 1.0, 2021) did not cover cloud environments. The new policy must align with the FCA's DORA-aligned operational resilience requirements and ISO 27001:2022 control A.8.2 (Privileged access rights).
INPUT:
  Key requirements to include:
  - Privileged access must be approved by the line manager and Information Security before being granted
  - Privileged accounts must not be used for routine, non-administrative tasks
  - Privileged access must be reviewed quarterly; unused access must be revoked within 5 business days of the review
  - All privileged access sessions must be logged and those logs retained for 12 months
  - Privileged access to production cloud environments (Azure) requires MFA
  - Temporary privileged access (break-glass) must be approved by the CIO or CISO and documented
  - Non-compliance is a disciplinary matter under the employee handbook
  - Exceptions require written approval from the CISO
DESIRED_OUTCOME: A clear, enforceable policy that employees and contractors can follow, and that the audit committee can cite as evidence of a strengthened control environment.
TONE: Formal, clear, unambiguous
LENGTH: 700–1,000 words
CONSTRAINTS: Reference audit finding AF-2025-08 in the context section. Reference ISO 27001:2022 control A.8.2. Policy version: 2.0. Effective date: 1 July 2026. Review date: 30 June 2027. Policy owner: Head of Information Security. Approval authority: Chief Information Security Officer.
```

## Example output

---

## Privileged Access Management Policy

| | |
|---|---|
| **Policy title** | Privileged Access Management Policy |
| **Version** | 2.0 |
| **Effective date** | 1 July 2026 |
| **Review date** | 30 June 2027 |
| **Policy owner** | Head of Information Security |
| **Approval authority** | Chief Information Security Officer |
| **Replaces** | Privileged Access Management Policy v1.0 (2021) |

---

### 1. Purpose

This policy defines the mandatory requirements for granting, managing, monitoring, and revoking privileged access to Meridian Financial Services IT systems. It applies to all on-premises and cloud environments, including Microsoft Azure. This policy is issued in response to audit finding AF-2025-08 and aligns with ISO 27001:2022 control A.8.2 (Privileged access rights) and FCA operational resilience requirements.

---

### 2. Scope

This policy applies to:
- All Meridian employees with privileged access to any IT system
- All contractors and third-party service providers with privileged access to Meridian systems
- All IT systems, including on-premises infrastructure, cloud platforms (including Azure), and SaaS applications

*Exclusions: Read-only access and standard user accounts are governed by the Identity and Access Management Policy, not this policy.*

---

### 3. Definitions

**Privileged access**: access rights that permit actions beyond those required for standard business use, including administrative rights, root/super-user access, ability to modify security configurations, and access to sensitive or production data environments.

**Break-glass account**: an emergency privileged account used only when normal administrative access is unavailable.

**Privileged Access Review**: a formal quarterly review of all privileged accounts to verify that access remains appropriate.

---

### 4. Policy Statements

#### 4.1 Approval and provisioning
4.1.1 Privileged access must be approved by the individual's line manager and the Information Security team before it is granted.
4.1.2 The request and approval must be documented in the IT service management system.
4.1.3 Privileged accounts must be separate from the individual's standard user account. Privileged accounts must not be used for routine, non-administrative tasks such as email or web browsing.

#### 4.2 Authentication
4.2.1 All privileged access to production environments, including Microsoft Azure, must be protected by multi-factor authentication (MFA).
4.2.2 Shared privileged accounts are prohibited. Each privileged account must be individually attributed to a named individual.

#### 4.3 Session logging
4.3.1 All privileged access sessions must be logged, including the account used, the systems accessed, and the actions performed.
4.3.2 Privileged access logs must be retained for a minimum of 12 months and must not be modified or deleted by the account holder.

#### 4.4 Access reviews and revocation
4.4.1 The Information Security team must conduct a formal Privileged Access Review every quarter.
4.4.2 Any privileged access identified as no longer required must be revoked within five business days of the review.
4.4.3 Privileged access must be revoked on the same day as an individual's departure from the organisation or change to a role that no longer requires it.

#### 4.5 Break-glass access
4.5.1 Break-glass accounts must only be used when normal privileged access is unavailable and a business-critical need exists.
4.5.2 Use of a break-glass account must be approved in advance by the CIO or CISO, and documented in the IT service management system within two hours of use.

---

### 5. Responsibilities

| Role | Responsibility |
|------|---------------|
| All privileged account holders | Comply with this policy; report any suspected compromise of privileged accounts immediately |
| Line managers | Approve privileged access requests; notify Information Security on the same day when a team member leaves or changes role |
| Information Security team | Process access requests; conduct quarterly reviews; maintain privileged access logs; report non-compliance |
| CISO | Approve exceptions to this policy; approve break-glass account use; review policy annually |

---

### 6. Compliance and Exceptions

Non-compliance with this policy is a serious matter and may result in disciplinary action in accordance with the employee handbook, up to and including dismissal. For contractors and third parties, non-compliance may result in immediate access revocation and termination of the engagement.

Exceptions to any requirement in this policy must be requested in writing to the CISO, with a business justification. Exceptions are time-limited and must be reviewed at least every 90 days.

---

### 7. Related Documents

- Identity and Access Management Policy
- Information Security Policy
- ISO 27001:2022 control A.8.2
- FCA operational resilience requirements (DORA-aligned)

---

## Review checklist

- [ ] Policy header is complete (version, effective date, review date, owner, approval authority)
- [ ] Purpose is stated plainly in one to three sentences
- [ ] Scope defines precisely who and what is covered — and what is excluded
- [ ] All policy statements use "must" or "must not" for mandatory requirements — not "should"
- [ ] Each statement is testable — it is clear whether someone is complying
- [ ] Responsibilities are listed by role, not individual name
- [ ] Consequences of non-compliance are stated
- [ ] Exception process is defined
- [ ] Review date is specified
- [ ] All regulatory references from the input are included
- [ ] British English used throughout

---

See [styles/policy-brief-style.md](../styles/policy-brief-style.md) for policy brief style.
