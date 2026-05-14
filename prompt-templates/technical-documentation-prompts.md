---
title: Technical Documentation Prompts
template_type: Technical Documentation
use_case: Write clear, structured technical documentation — including system overviews, runbooks, API references, and how-to guides — that enables engineers and operators to understand and work with a system confidently.
audience: Software engineers, DevOps engineers, solutions architects, or technical operators — defined per document
output_format: Structured document with overview, prerequisites, explanation, examples, troubleshooting, and reference sections
---

# Technical Documentation Prompts

## Purpose

Good technical documentation answers three questions: what does this system do, how do I use it, and what do I do when it breaks? Use this template when you need to write documentation for a system, service, API, infrastructure component, or operational process. It works for both internal runbooks (e.g. how to respond to a PagerDuty alert for the IAM service) and externally published references (e.g. an API integration guide for a partner). The output should be structured, scannable, and precise — technical readers do not read documentation linearly; they search for the section they need and want the answer quickly. All examples must be real and working, not pseudocode placeholders.

## Copy-paste prompt

```
You are a senior technical writer with experience documenting enterprise software systems and cloud infrastructure. Write clear, accurate, and well-structured technical documentation.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (everything known about the system, process, or component being documented — architecture, behaviour, configuration, common errors, and any existing notes or diagrams):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH]

FORMAT: [FORMAT — recommended: Overview / Prerequisites / How It Works / Step-by-Step Guide or Reference / Examples / Troubleshooting / Reference]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a clear overview that explains what the system or component is, what it does, and when you would use it. One to three sentences. No history, no background story.
3. List prerequisites explicitly and specifically — versions, permissions, environment variables, and dependencies required before the reader can proceed. Do not assume.
4. Structure the body with clear H2 and H3 headings. Technical readers navigate by scanning headings; every heading should be descriptive enough to be useful on its own.
5. Use numbered steps for sequential processes. Use bullet points for lists of options or attributes. Never use paragraph prose for step-by-step instructions.
6. Include at least one realistic, working example. Examples must be complete (not partial snippets that leave the reader guessing) and drawn from the context provided. Do not invent examples that contradict the input.
7. Distinguish between facts (confirmed behaviour), assumptions (behaviour inferred from context), and recommendations (suggested approaches) — use Note, Warning, or Tip callouts where appropriate.
8. Write the troubleshooting section based on the failure modes described in the input. Each entry should follow the pattern: symptom → likely cause → resolution. Do not invent issues that are not mentioned in the input.
9. Avoid vague instructions like "configure appropriately" or "ensure you have the correct permissions". Be specific: say exactly what configuration or permission is needed.
10. Do not use marketing language or corporate filler. This is a reference document, not a product brochure.
11. Where there is genuine uncertainty about system behaviour (e.g. the input is unclear), flag it with a Note callout rather than guessing.
12. Tone: [TONE — recommended: precise, direct, neutral].
13. Length: [LENGTH].
14. Apply these constraints: [CONSTRAINTS].
15. Output only the documentation. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will read and use this document. Examples: "senior DevOps engineers operating a Kubernetes cluster on Azure AKS", "integration developers building against the Meridian Payments API", "Level 2 support engineers responding to IAM service alerts".
- `[PURPOSE]` — what the documentation must enable the reader to do. Examples: "understand the IAM token refresh mechanism and diagnose failures", "integrate with the Payments API endpoint and handle error responses", "execute the monthly certificate rotation runbook without assistance".
- `[CONTEXT]` — background information about the system. Examples: "the IAM service is built on Okta with a custom claims enrichment layer; it runs on Azure AKS behind an APIM gateway", "the Payments API is RESTful, uses OAuth 2.0, and returns JSON. Rate limit is 100 requests per minute per client ID".
- `[INPUT]` — all source material: architecture diagrams described in text, existing notes, Confluence pages, code comments, Slack threads, or any other raw information about the system.
- `[DESIRED_OUTCOME]` — what the reader should be able to do after reading. Examples: "an engineer who has never worked with the IAM service can diagnose a token refresh failure within 15 minutes", "a new developer can make a successful API call within 30 minutes of reading the guide".
- `[TONE]` — almost always "precise, direct, neutral" for technical docs. For internal runbooks, "direct and operational" works well.
- `[LENGTH]` — varies widely. A runbook may be 500–1,000 words; a full API reference guide may be 3,000–5,000 words.
- `[FORMAT]` — use the recommended structure above; for runbooks, replace "How It Works" with "When to Use This Runbook" and lead with the alert or trigger condition.
- `[CONSTRAINTS]` — examples: "use Azure CLI examples only — no Terraform", "all code examples must be in Python 3.10+", "do not include internal IP ranges or resource names — use placeholders", "include the security classification 'Internal' in the header".

## Example input

```
AUDIENCE: Level 2 and Level 3 support engineers and DevOps engineers at Meridian Financial Services
PURPOSE: Runbook for diagnosing and resolving failures in the Azure AD B2C token issuance service used for customer authentication
CONTEXT: Meridian's customer authentication uses Azure AD B2C with a custom policy (Identity Experience Framework). Tokens are issued on login and refreshed silently every 60 minutes. The service runs behind Azure API Management (APIM). Monitoring is via Azure Monitor and PagerDuty. Alert "B2C_TOKEN_FAILURE" triggers when the token error rate exceeds 2% over a 5-minute window.
INPUT:
  System components:
  - Azure AD B2C tenant: meridian-prod.b2clogin.com
  - Custom sign-in policy: B2C_1A_SignIn_v3
  - APIM gateway: apim-meridian-prod.azure-api.net
  - Token endpoint: POST /meridian-prod.b2clogin.com/oauth2/v2.0/token

  Common failure modes:
  1. Expired signing certificate — B2C stops issuing tokens; all logins fail. Certificate rotated quarterly. Check: Azure AD B2C > Identity Experience Framework > Keys. Resolution: rotate certificate using runbook RBK-CERT-001.
  2. Custom policy syntax error after a deployment — tokens fail with AADB2C90011 error. Check: B2C App Insights logs, filter on "PolicyId = B2C_1A_SignIn_v3". Resolution: roll back policy to last known good version in Azure DevOps.
  3. APIM quota exceeded — 429 errors upstream; token endpoint returns 503 to clients. Check: APIM > Analytics > Capacity. Resolution: increase APIM unit scale or implement exponential backoff in calling applications.
  4. Dependency failure (downstream claims enrichment API) — token issued but missing custom claims; causes downstream authorisation failures. Check: APIM > Backends > ClaimsEnrichmentAPI health. Resolution: investigate and restart claims enrichment service.

  Alert thresholds: B2C_TOKEN_FAILURE fires at >2% error rate over 5 minutes. P1 if >10%; P2 if 2–10%.
DESIRED_OUTCOME: An engineer receiving the B2C_TOKEN_FAILURE alert can diagnose and resolve the issue, or correctly escalate it, within 15 minutes.
TONE: Precise, direct, operational
LENGTH: 800–1,200 words
CONSTRAINTS: Include exact Azure portal navigation paths. Do not include production URLs in the document — use placeholders where needed. Security classification: Internal.
```

## Example output

---

**INTERNAL — MERIDIAN FINANCIAL SERVICES**

# Runbook: B2C_TOKEN_FAILURE — Azure AD B2C Token Issuance Failure

**Last reviewed:** May 2026
**Applies to:** Azure AD B2C (meridian-prod tenant), APIM gateway (apim-meridian-prod)
**Alert:** B2C_TOKEN_FAILURE (PagerDuty)
**Owner:** Platform Engineering

---

## Overview

This runbook covers diagnosis and resolution of the `B2C_TOKEN_FAILURE` PagerDuty alert, which fires when the Azure AD B2C token error rate exceeds 2% over a 5-minute window. The alert indicates that customer logins or token refreshes are failing. Resolution time target is 15 minutes.

**Severity:**
- P1: error rate >10% (customer-facing login unavailable)
- P2: error rate 2–10% (degraded authentication; some customers affected)

---

## Prerequisites

Before starting diagnosis, confirm you have:
- Azure portal access with Reader rights to the `meridian-prod` B2C tenant
- Access to Azure Application Insights (workspace: `meridian-prod-appinsights`)
- Access to APIM (gateway: `apim-meridian-prod.azure-api.net`)
- Access to Azure DevOps for policy rollback (project: `Platform / B2C-Policies`)
- PagerDuty alert link open — the alert includes the exact error rate and time window

---

## Step 1: Identify the error type (2 minutes)

1. Open **Azure Portal** > **Azure AD B2C** > **meridian-prod** > **Monitoring** > **Application Insights**.
2. Run the following query (last 10 minutes):

```kusto
traces
| where timestamp > ago(10m)
| where message contains "error" or message contains "fail"
| project timestamp, message, customDimensions
| order by timestamp desc
```

3. Look for the error code in the `message` column. Match against the table below.

| Error code | Likely cause | Go to |
|------------|-------------|-------|
| `AADB2C90072` | Expired signing certificate | Step 2 |
| `AADB2C90011` | Custom policy syntax error | Step 3 |
| HTTP 429 / 503 from APIM | APIM quota exceeded | Step 4 |
| Token issued but missing claims | Claims enrichment failure | Step 5 |
| Unknown error | Escalate to Platform Engineering L3 | — |

---

## Step 2: Expired signing certificate

**Symptom:** All token requests failing; error `AADB2C90072` in App Insights logs.

**Check:**
1. Azure Portal > **Azure AD B2C** > **Identity Experience Framework** > **Policy Keys**.
2. Locate the key named `B2C_1A_TokenSigningKeyContainer`. Check the expiry date.

**Resolution:** If the certificate has expired, follow **Runbook RBK-CERT-001** (Certificate Rotation). Do not attempt to rotate the certificate without following that runbook — incorrect rotation will extend the outage.

---

## Step 3: Custom policy syntax error

**Symptom:** Token requests failing after a recent deployment; error `AADB2C90011` in App Insights.

**Check:**
1. Azure Portal > **Azure AD B2C** > **Identity Experience Framework** > **Custom Policies**.
2. Confirm the active policy version for `B2C_1A_SignIn_v3`.
3. Check Azure DevOps (project: `Platform / B2C-Policies`) for recent deployments in the last 4 hours.

**Resolution:** Roll back to the previous policy version:
1. In Azure DevOps, open the last successful pipeline run before the failure.
2. Select **Redeploy** on the pipeline run.
3. Monitor App Insights for 5 minutes post-rollback to confirm error rate has dropped.
4. Raise a P2 incident ticket for the development team to investigate the failed deployment.

---

## Step 4: APIM quota exceeded

**Symptom:** Clients receiving HTTP 503; APIM returning 429 upstream; token endpoint unreachable.

**Check:**
1. Azure Portal > **API Management** > **apim-meridian-prod** > **Analytics** > **Capacity**.
2. If capacity is at or near 100%, the APIM unit is saturated.

**Resolution:**
- **Immediate:** Increase APIM units: **API Management** > **Scale and pricing** > add one unit. (Note: scaling takes 15–45 minutes. This is not an instant fix for an active P1.)
- **Interim:** Contact calling application teams to implement exponential backoff (minimum 2-second retry interval) while scaling completes.
- **Post-incident:** Review APIM capacity trends in Azure Monitor and raise a capacity planning ticket.

---

## Step 5: Claims enrichment API failure

**Symptom:** Tokens are being issued successfully (no B2C errors) but downstream services are rejecting them due to missing custom claims.

**Check:**
1. Azure Portal > **API Management** > **Backends** > **ClaimsEnrichmentAPI**.
2. Check the health endpoint status and last response time.

**Resolution:**
1. If the claims enrichment service is down, restart it via Azure Portal > **App Service** > **[ClaimsEnrichmentAPI service name]** > **Restart**.
2. Monitor for 5 minutes to confirm health check returns 200.
3. If the restart does not resolve the issue, escalate to the Identity Platform team (L3).

---

## Escalation

If the issue is not resolved within 15 minutes, or if the error type is not covered above, escalate to:
- **L3 Platform Engineering** (on-call PagerDuty rotation)
- Provide: the App Insights query results, the alert time window, and the steps already taken.

---

## Review checklist

- [ ] Overview explains what the system does and what the alert means
- [ ] Prerequisites list exact permissions and tools needed — no vague requirements
- [ ] Each step is numbered and uses specific portal navigation paths
- [ ] Error table covers the four known failure modes from the input
- [ ] All code examples (KQL query) are complete and usable as written
- [ ] Troubleshooting pattern is: symptom → cause → resolution
- [ ] No invented failure modes — content matches input only
- [ ] No internal URLs or production resource names exposed
- [ ] British English used throughout
- [ ] Security classification header included

---

See [styles/technical-documentation.md](../styles/technical-documentation.md) for technical documentation style.
