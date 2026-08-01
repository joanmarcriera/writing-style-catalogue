---
title: Technical Runbook — API Connection Pool Exhaustion
category: Example
description: A worked operational bundle with bounded diagnostics, approval gates, rollback, escalation, and measurable recovery.
bundle_id: technical-runbook
artefact: Production incident runbook
audience: Authorised on-call engineers and service owners
scenario: labelled-composite
style_path: styles/technical-documentation.md
pattern_path: patterns/objective-scope-procedure-exceptions.md
prompt_path: prompt-templates/technical-documentation-prompts.md
skill_path: skills/create-runbook.md
rubric_path: rubrics/technical-documentation-rubric.md
---

# Technical Runbook — API Connection Pool Exhaustion

## Professional context

An authorised on-call engineer needs safe triage and recovery guidance. Commands are illustrative placeholders and the runbook must stop operators from running an untested restart or rollback blindly.

## Source packet

```text
SCENARIO: Labelled composite; commands and identifiers are illustrative and must be tested locally.
SERVICE: orders-api in Kubernetes namespace production.
TRIGGER: pool utilisation above 90% for five minutes plus “Timeout waiting for connection from pool”.
READ-ONLY COMMANDS APPROVED: kubectl -n production get deploy orders-api; kubectl -n production get pods -l app=orders-api; kubectl -n production rollout history deploy/orders-api.
BASELINE: API error rate below 1%; pool utilisation below 70%.
CHANGE GATE: Restart or rollback requires active incident ticket, incident commander approval, confirmed rollback target, and operator authorisation.
RECOVERY OPTIONS: pause order-reconciliation CronJob; restart deployment; roll back latest deployment. Exact write commands must be taken from the locally tested command register, not generated.
ESCALATE: checkout failures exceed 15 minutes; database CPU above 85%; rollback fails; cause unknown after 20 minutes.
RESOLUTION: baselines hold for ten minutes; synthetic checkout passes; paused jobs restored or explicitly tracked.
OWNER: Platform Operations. LAST TESTED: not supplied.
```

## Completed prompt

```text
You are a senior site-reliability engineer writing a runbook for authorised on-call staff. Use only the SOURCE PACKET to document connection-pool exhaustion for orders-api.

Do not invent commands, dashboards, database queries, contacts, rollback revisions, timings, permissions, or success evidence. Include the three approved read-only commands verbatim. For any state-changing step, describe the gate and write “use the locally tested command register”; never generate a kubectl patch, restart, or rollback command. If authorisation, change gate, escalation path, recovery threshold, or last-tested evidence is missing, return MISSING INFORMATION for that part and do not present the runbook as production-ready.

Use British English and structure: Purpose; Scope and authority; Detection; First five minutes; Decision tree; State-changing recovery gates; Escalation; Resolution verification; Restoration; Post-incident actions; Ownership and test record. Make stop conditions explicit. State at the top that LAST TESTED is missing and the document cannot be approved for production until a tabletop or staging test is recorded. Keep it between 800 and 1,050 words. Output only the runbook.

Before finalising, apply the Technical Documentation Rubric for accuracy, prerequisites, safety, decision branches, verification, rollback, escalation, and maintainability. Treat an unverified command as a critical failure.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Approval status: NOT PRODUCTION-READY — no last-tested date is supplied.

First five minutes
1. Confirm the alert is current and open or join the active incident ticket.
2. Run only the approved read-only checks:
   kubectl -n production get deploy orders-api
   kubectl -n production get pods -l app=orders-api
   kubectl -n production rollout history deploy/orders-api
3. Confirm both the pool alert and timeout log pattern. If either is absent, stop and use the generic API-degradation runbook.

State-changing recovery
Do not restart, roll back, or pause a job unless the incident commander approves the change, the operator is authorised, and the locally tested command register identifies the exact command and rollback target.

Resolution requires ten continuous minutes below 1% API errors and 70% pool utilisation, a passing synthetic checkout, and restoration or explicit tracking of every paused job.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Accuracy | 4 | Only approved read-only commands are reproduced. | Human check |
| Safety | 5 | All state changes require authority and a tested command register. | Pass |
| Decision branches | 5 | Stop, continue, escalate, and resolve conditions are measurable. | Pass |
| Verification | 5 | Recovery requires sustained metrics and a synthetic transaction. | Pass |
| Maintainability | 3 | Ownership exists, but last-tested evidence is missing. | Revise |

## Human review before use

- Platform Operations must replace illustrative identifiers with locally verified values.
- An authorised engineer must test every command in staging and record the date and evidence.
- Security and change-management owners must approve permissions and state-changing gates.
- The runbook cannot be marked production-ready while the maintainability gate remains `Revise`.

## Reuse this bundle

- [Technical Documentation Style](../styles/technical-documentation.md)
- [Objective / Scope / Procedure / Exceptions Pattern](../patterns/objective-scope-procedure-exceptions.md)
- [Technical Documentation Prompts](../prompt-templates/technical-documentation-prompts.md)
- [Create Runbook Skill](../skills/create-runbook.md)
- [Technical Documentation Rubric](../rubrics/technical-documentation-rubric.md)
