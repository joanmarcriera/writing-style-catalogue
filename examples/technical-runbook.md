---
title: Technical Runbook Example
category: Example
---

# Technical Runbook Example

**Runbook: Database Connection Pool Exhaustion**

**Incident Type:** Database Performance Degradation

**Detection / Trigger**
- Monitoring alert: "Database connection pool at 95%"
- Application logs: "Unable to acquire connection; queue exceeded"
- Customer impact: API responses slow or timing out

**Initial Response (0–10 minutes)**

1. Log into monitoring dashboard
   - Confirm connection pool exhaustion
   - Check query execution time and queue depth
   - Identify which application(s) are consuming connections

2. Check application logs
   - Search for connection timeout errors
   - Identify problematic queries or services
   - Look for any recent deployments

3. Immediate mitigation
   - Increase connection pool size (temporary increase: +30%)
   - Monitor recovery (allow 5 minutes)
   - If recovery doesn't occur, proceed to Escalation

**Escalation (if not recovered)**

Contact:
- Database Administrator (on-call)
- Engineering lead for problematic service
- VP Engineering (if issue persists >30 minutes)

**Resolution Options**

**Option A: Scale Database (Faster)**
- Increase database instance size (adds more CPU, connection capacity)
- Timeline: 15–30 minutes
- Risk: Brief connection interruption during resize

**Option B: Fix Application (Proper)**
- Kill or restart problematic service
- Deploy connection pool fix
- Timeline: 30–60 minutes

**Verification**
1. Connection pool is <80% utilised
2. Query queue is empty
3. API response times return to normal
4. Customer reports normal service

**Post-Incident**
1. Declare incident resolved
2. Schedule post-mortem for 24 hours later
3. Document root cause and prevention measures

---

**Key principles shown:**
- Clear trigger/detection
- Step-by-step response
- Escalation path defined
- Multiple resolution options
- Verification steps clear
- Designed for someone in crisis
