---
title: Incident Report Example
category: Example
---

# Incident Report Example

**Incident Report: Payment Processing Outage – 15 May 2026**

**Summary**
Payment processing API was unavailable for 47 minutes (14:20–15:07 GMT), affecting approximately 2,000 transactions. Estimated revenue impact: £18,000. No data loss or security exposure.

**Timeline**
- 14:20: Monitoring alert triggered; database connection pool exhausted
- 14:22: On-call engineer paged
- 14:25: Root cause identified (queue processing exceeded pool limits)
- 14:45: Temporary fix deployed (connection pool increased 20→50)
- 15:07: Service recovered; normal performance restored
- 15:15: Incident resolved

**Root Cause**
A data migration job queued transactions at 10x normal rate. The queue consumer wasn't scaled to match. Database connection pool exhausted; new requests rejected. Queue depth monitoring didn't exist; root cause detection was delayed.

**What We Could Have Done Better**
- Queue depth monitoring would have alerted earlier
- Consumer process scaling should have been reviewed before migration
- On-call runbook didn't include "high queue depth" procedures

**Prevention Measures**

1. **Monitoring:** Add queue depth alerting (trigger at 80% capacity) – Owner: Alice – Due: 22 May
2. **Capacity Planning:** Quarterly review of consumer scaling vs. queue rates – Owner: Bob – Due: 29 May
3. **Runbook:** Add "high queue depth" troubleshooting procedure – Owner: Charlie – Due: 26 May
4. **Testing:** Monthly chaos engineering scenario testing – Owner: Diana – Starting June

**Lessons**
This incident shows that monitoring gaps can delay response. Even with good on-call response, detection time matters. Proactive capacity planning would have prevented this entirely.

---

**Key principles shown:**
- Blameless; focuses on systems not people
- Timeline is precise with exact times
- Root cause is systemic, not individual
- Prevention measures are specific and assigned
- Learning-focused tone
