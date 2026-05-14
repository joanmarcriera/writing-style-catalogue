---
title: Technical Runbook Example
category: Example
description: A practical operational runbook with detection, triage, response, escalation, verification, and post-incident actions.
---

# Technical Runbook Example

## Runbook: API Connection Pool Exhaustion

**Severity:** P2 unless customer-facing outage exceeds 15 minutes
**Owner:** Platform Operations
**Last tested:** 14 May 2026
**Systems:** `orders-api`, managed PostgreSQL database, application load balancer

## 1. Detection

Use this runbook when any of the following triggers occur:

- Alert: `orders-api-db-pool-utilisation > 90% for 5 minutes`
- Application log pattern: `Timeout waiting for connection from pool`
- API error rate above 5% with database timeout errors
- Customer support reports intermittent checkout failures

## 2. Initial Triage (first 5 minutes)

1. Confirm the alert is current, not a delayed notification.

```bash
kubectl -n production get deploy orders-api
kubectl -n production get pods -l app=orders-api
```

2. Check current API error rate in the monitoring dashboard.

Expected baseline: error rate below 1%.

3. Check whether a deployment occurred in the last 60 minutes.

```bash
kubectl -n production rollout history deploy/orders-api
```

4. Check database connection count and active queries using the approved database console.

If active connections are above 90% and most are from `orders-api`, continue to Section 3.

If active connections are normal, stop and use the generic API degradation runbook.

## 3. Response Steps

1. Pause non-critical scheduled jobs that call `orders-api`.

```bash
kubectl -n production patch cronjob order-reconciliation -p '{"spec":{"suspend":true}}'
```

Record the change in the incident ticket. Do not leave the cron job suspended after resolution.

2. Restart one `orders-api` pod to clear leaked connections.

```bash
kubectl -n production rollout restart deploy/orders-api
```

3. Wait 3 minutes, then check error rate and connection count.

If error rate falls below 1% and pool utilisation falls below 70%, go to Section 5.

If error rate remains above 5%, continue to Step 4.

4. Roll back the most recent deployment if it occurred within the last 60 minutes and correlates with the alert.

```bash
kubectl -n production rollout undo deploy/orders-api
```

5. If rollback is not appropriate or does not recover service within 10 minutes, escalate.

## 4. Escalation

Escalate immediately if:

- customer-facing checkout failure exceeds 15 minutes;
- database CPU is above 85% as well as connection exhaustion;
- rollback fails;
- you cannot confirm the cause within 20 minutes.

Escalation path:

| Role | Contact method | Information to provide |
|---|---|---|
| Platform Operations Lead | PagerDuty: `platform-lead` | Alert time, current error rate, actions taken |
| Database Administrator | PagerDuty: `database-on-call` | Connection count, active query summary, CPU |
| Incident Manager | Teams channel: `#incident-command` | Customer impact, severity recommendation |

## 5. Resolution Verification

Declare resolved only when all conditions hold for 10 consecutive minutes:

- API error rate below 1%.
- Database connection pool utilisation below 70%.
- No new `Timeout waiting for connection from pool` errors.
- Checkout synthetic monitor passing.
- Paused scheduled jobs either re-enabled or tracked in the incident ticket.

## 6. Post-Incident Actions

1. Update the incident ticket with timeline, commands run, and current service state.
2. Re-enable any paused scheduled jobs.

```bash
kubectl -n production patch cronjob order-reconciliation -p '{"spec":{"suspend":false}}'
```
3. If severity was P1 or P2, schedule a post-incident review within 2 working days.
4. Add any missing alert, dashboard, or command improvements to the platform backlog.
5. If a deployment caused the issue, link the incident to the release ticket and require a regression test before redeployment.

## Why this example works

- The trigger is specific.
- The responder has exact commands where appropriate.
- Decision branches tell the responder when to continue, roll back, or escalate.
- Resolution criteria are measurable.
- Post-incident actions preserve learning and accountability.
