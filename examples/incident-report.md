---
title: Incident Report — Checkout API Degradation
category: Example
description: A worked incident-review bundle with an evidence-bounded timeline, causal analysis, and testable actions.
bundle_id: incident-report
artefact: Blameless incident report
audience: Engineering, service ownership, risk, and customer-support leadership
scenario: labelled-composite
style_path: styles/incident-report-style.md
pattern_path: patterns/issue-risk-control-owner-date.md
prompt_path: prompt-templates/incident-report-prompts.md
rubric_path: rubrics/incident-report-rubric.md
---

# Incident Report — Checkout API Degradation

## Professional context

The service team needs a defensible record of a 47-minute checkout incident. The report must distinguish observed evidence from the still-unproven reason a deployment increased database connection use.

## Source packet

```text
SCENARIO: Labelled composite.
INCIDENT: INC-2026-081; severity P2.
WINDOW: 14:20–15:07 UTC on 15 July 2026.
IMPACT: 1,842 checkout attempts returned HTTP 503; 1,307 were retried successfully within 24 hours; no evidence of data loss or unauthorised access; revenue impact not calculated.
14:20: error-rate alert fired. 14:23: on-call acknowledged. 14:28: database connection saturation confirmed. 14:36: deployment 2026.07.15.2 identified as the only production change in the previous hour. 14:45: rollback began. 14:52: error rate below 1%. 15:07: ten-minute stability gate passed.
CONFIRMED TECHNICAL CAUSE: application instances exhausted their database connection pools after the deployment.
UNPROVEN CONTRIBUTING HYPOTHESIS: a changed retry path retained connections longer; code-level verification pending.
CONTROL GAP: release test did not measure connection duration under retry load.
ACTIONS: add retry-load connection test (Platform Engineering, 29 July); add pool-saturation deployment gate (SRE, 5 August); verify retry-path hypothesis and attach evidence to INC-2026-081 (Application Team, 22 July).
```

## Completed prompt

```text
You are a senior incident-review facilitator. Write a blameless incident report for engineering, service ownership, risk, and customer-support leadership using only the SOURCE PACKET.

Do not invent revenue impact, customer behaviour, log evidence, code defects, security conclusions, detection delays, or action status. Keep the confirmed connection-pool exhaustion separate from the unproven retry-path hypothesis. “No evidence of” must not become “there was no”. If the impact window, evidence, recovery gate, causal status, or action ownership is missing or contradictory, return MISSING INFORMATION instead of a report.

Use British English and structure the report as: Executive summary; Customer and business impact; Detection and response timeline; Confirmed technical cause; Contributing hypotheses and evidence gaps; What worked; What delayed certainty; Corrective actions; Closure and follow-up. Use UTC consistently. Each corrective action must retain its owner role, due date, acceptance evidence, and incident reference. Keep the report between 750 and 1,000 words. Output only the incident report.

Before finalising, apply the Incident Report Rubric. Impact, timeline, causal analysis, corrective actions, and factual integrity are critical gates. Do not call the hypothesis a root cause until the named verification action is complete.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Executive summary
Checkout API degradation between 14:20 and 15:07 UTC caused 1,842 HTTP 503 responses. Of those checkout attempts, 1,307 were retried successfully within 24 hours. Revenue impact has not been calculated. There is no evidence in the supplied incident record of data loss or unauthorised access.

Causal analysis
The confirmed technical cause was exhaustion of application database connection pools after deployment 2026.07.15.2. The team has not yet proved why the deployment increased connection duration. A changed retry path is the current hypothesis and remains subject to code-level verification by 22 July.

Closure condition
Service recovery was accepted at 15:07 after the error rate remained below 1% for ten minutes. INC-2026-081 remains open for corrective-action evidence.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Impact | 5 | Duration, failed attempts, retries, and evidence limits are explicit. | Pass |
| Timeline | 5 | Detection, diagnosis, rollback, recovery, and stability gate align. | Pass |
| Causal analysis | 5 | Confirmed mechanism and unproven hypothesis are separate. | Pass |
| Corrective actions | 4 | Owners, dates, and expected evidence are retained. | Human check |
| Factual integrity | 5 | The excerpt does not add revenue or security certainty. | Pass |

## Human review before use

- The incident commander must reconcile timestamps with monitoring and ticket records.
- Security must approve the wording about data loss and unauthorised access.
- Action owners must confirm dates and attach acceptance evidence before closure.

## Reuse this bundle

- [Incident Report Style](../styles/incident-report-style.md)
- [Issue / Risk / Control / Owner / Date Pattern](../patterns/issue-risk-control-owner-date.md)
- [Incident Report Prompts](../prompt-templates/incident-report-prompts.md)
- [Incident Report Rubric](../rubrics/incident-report-rubric.md)
