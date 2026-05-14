---
title: Board Paper Example (Condensed)
category: Example
description: A condensed board paper showing decision request, options analysis, risks, financials, and resolution wording.
---

# Board Paper Example (Condensed)

**Company:** Northstar Software Group Ltd
**Meeting:** Board of Directors, 18 June 2026
**Paper:** BP-2026-07
**Subject:** Identity and Access Management Platform Renewal or Replacement
**Author:** Chief Information Officer
**Status:** For decision
**Classification:** Confidential

## 1. Executive Summary

The Company's identity and access management (IAM) platform contract expires on 31 December 2026. The Board is asked to approve Option B: migrate to a cloud-native IAM platform over 12 months at a five-year total cost of £620,000. This option resolves two audit findings, satisfies enterprise client security requirements due from January 2027, and costs £220,000 less than renewing the current platform with custom remediation.

Three options have been assessed:

| Option | Description | Five-year cost | Assessment |
|---|---|---:|---|
| A | Renew current platform and customise controls | £840,000 | Lowest change risk, but does not fully resolve audit issues |
| B | Migrate to cloud-native IAM platform | £620,000 | Recommended: best balance of compliance, cost, and delivery risk |
| C | Build internal IAM capability | £1.4M | Rejected: cost and delivery risk are disproportionate |

**The Board is asked to approve Option B and authorise a five-year budget of £620,000, funded from the IT capital reserve and operating technology budget.**

## 2. Background

The current IAM platform was implemented in 2017 and has received no major functional upgrade since 2021. It supports single sign-on, multi-factor authentication, and privileged access workflows for 1,850 staff and 340 applications.

The December 2025 external audit identified two control weaknesses:

- access certification reviews are manual and not consistently evidenced;
- anomalous access activity is not detected in real time.

Three enterprise clients, representing 34% of annual recurring revenue, have updated their supplier security questionnaires to require automated access certification and conditional access controls from 1 January 2027. Failure to meet these requirements would create renewal risk during the 2027 client review cycle.

## 3. Options Analysis

### Option A: Renew current platform

The incumbent supplier has offered a 24-month renewal at £168,000 per annum. The audit findings would require bespoke development estimated at £95,000.

**Advantages**

- No migration required.
- Existing administrators already know the platform.
- Lowest short-term operational disruption.

**Disadvantages**

- Custom remediation does not provide real-time anomaly detection without further tooling.
- The platform remains near end of vendor support.
- Five-year cost is higher than Option B.

### Option B: Migrate to cloud-native IAM platform (recommended)

The preferred supplier provides automated access certification, conditional access, anomaly detection, and standard integration with the Company's Microsoft estate.

**Advantages**

- Resolves both audit findings using native functionality.
- Satisfies client questionnaire requirements before January 2027.
- Reduces five-year cost by £220,000 compared with Option A.
- Aligns with the Board-approved cloud-first technology strategy.

**Disadvantages**

- Requires a 12-month migration programme.
- Creates short-term training and change management requirements.
- Introduces dependency on a new supplier.

### Option C: Build internal IAM capability

The engineering team assessed an internal build covering access certification, workflow automation, anomaly detection, and reporting.

**Advantages**

- Maximum design control.
- Potential long-term reuse across internal platforms.

**Disadvantages**

- Estimated five-year cost of £1.4M.
- Delivery would divert engineering capacity from committed product roadmap work.
- Independent assurance would still be required before audit reliance.

## 4. Recommendation

The Board is recommended to approve Option B.

Option B provides the strongest combination of compliance coverage, cost, and execution feasibility. Option A is cheaper in the first year but does not fully resolve the control weaknesses. Option C is not proportionate given cost, time, and internal capacity constraints.

Success will be measured by:

- closure of both audit findings before the November 2026 recertification review;
- completion of client questionnaire evidence packs by 31 December 2026;
- migration delivered within approved budget tolerance of plus or minus 10%;
- privileged access review cycle reduced from 11 days to 2 days.

## 5. Risk Assessment

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Migration delay beyond December 2026 | Medium | High | Phased plan; external delivery partner; monthly programme board | CIO |
| Data integrity issue during migration | Low | Critical | Parallel running; reconciliation at each phase gate; rollback plan | Head of Security |
| User disruption at cutover | Medium | Medium | Pilot rollout; enhanced service desk cover; targeted communications | IT Operations |
| Supplier dependency | Low | Medium | Contract exit provisions; documented data export process; annual supplier review | Procurement |

## 6. Financial Summary

| Option | Year 1 | Years 2-5 (per year) | Five-year total |
|---|---:|---:|---:|
| A: Renew | £358,000 | £168,000 | £840,000 |
| B: Migrate | £332,000 | £72,000 | £620,000 |
| C: Build | £480,000 | £185,000 | £1,420,000 |

Assumptions: figures are based on supplier proposals and internal effort estimates as at May 2026. Finance has reviewed the model for arithmetic consistency; procurement due diligence remains outstanding.

## 7. Proposed Resolution

The Board resolves to approve Option B, the migration to a cloud-native identity and access management platform, and authorises expenditure of up to £620,000 over five years, subject to final procurement approval and quarterly programme reporting to the Board.

## Why this example works

- The decision required is visible in the executive summary.
- Options are compared on the same basis.
- Recommendation follows the options analysis, not before it.
- Risks have owners and mitigations.
- Resolution wording is ready for minutes.
