---
title: Good vs. Bad Prompts
category: Reference
---

# Good vs. Bad Prompts: Examples

Learn by comparison. See exactly what makes a prompt produce a usable output versus a generic one. Each example shows the same task prompted badly and well — and explains why the good version works.

---

## Example 1: Executive email

**Bad prompt**
```
Write an email
```
Output: Generic placeholder with no context, no audience, no purpose, no tone. Unusable.

**Good prompt**
```
You are a senior communications specialist. Write a professional email from the CTO to the board requesting approval for a £600k cloud migration investment.

TO: Board of directors
FROM: CTO
PURPOSE: Formal request for capital approval before the June board meeting

Key facts to include:
- Azure migration Phase 1 cost: £600k (one-time)
- Annual savings from year 2: £1.5M
- Payback period: 18 months
- Timeline: start Q3 2025; complete Q1 2027
- Reason for urgency: current on-premise contract expires September 2025

Tone: professional and direct. Lead with the bottom line.
Length: under 300 words.
Format: standard email format with subject line.
Constraints: Use British English. No filler phrases. Output only the email; no preamble.
```
Output: A ready-to-send executive email with the correct structure, specific data, and appropriate tone.

**Why the good prompt works**:
- Assigns a role to the model (communications specialist)
- Specifies audience, sender, purpose
- Provides specific financial data — the model does not have to invent it
- Sets explicit length and format constraints
- Suppresses filler with a constraint
- Instructs British English

---

## Example 2: Strategic analysis

**Bad prompt**
```
Analyse this market opportunity
```
Output: A generic market analysis essay with invented assumptions and generic frameworks. Confidently useless.

**Good prompt**
```
You are a strategy consultant. Analyse the market opportunity for cold-chain logistics software targeting UK food importers.

CONTEXT:
- Market size: approximately £380M addressable in the UK
- Client's current product: real-time temperature monitoring and predictive routing software
- Client's proven benefit: 18% average reduction in spoilage-related write-offs
- Competitive landscape: 2 established players (Sensitech, Controlant), 5+ smaller vendors
- Sector pressures: post-Brexit customs dwell-time increasing cold-chain exposure; rising energy costs

PROVIDE:
1. Market fit assessment (strong / moderate / weak) with rationale
2. Top 3 customer acquisition approaches with rationale for each
3. Top 3 competitive risks and how to mitigate them
4. A 12-month revenue target range with the key assumptions

Tone: analytical and direct. State your view; do not hedge.
Length: 600–800 words.
Format: numbered sections matching the structure above.
Constraints: Use British English. No invented figures — use only the data provided; flag any assumption explicitly. Output only the analysis; no preamble.
```
Output: A focused, structured analysis based on the provided data — with clear recommendations and flagged assumptions.

---

## Example 3: Process documentation

**Bad prompt**
```
Document this process
```
Output: A brief, vague outline that requires the author to rewrite it entirely to be usable.

**Good prompt**
```
You are a process documentation specialist. Write an SOP for the new joiner IT account provisioning process.

USER: IT administrator (familiar with Active Directory and Microsoft 365; may be new to Azure AD/Entra ID)
PROCESS SCOPE: From receiving the approved new joiner request from HR to closing the ServiceDesk ticket

STEPS TO DOCUMENT (in this order):
1. Receive new joiner form from HR via ServiceDesk ticket
2. Create Active Directory account (username format: firstname.lastname@[domain])
3. Assign Microsoft 365 licence (E3 for employees; Guest access only for contractors)
4. Add to security groups based on role (use the Role-to-Group Matrix in Appendix A)
5. Provision laptop via IT procurement queue
6. Enable MFA and send registration link to personal email
7. Send welcome email with secure credential link (use Keeper for credential sharing — never plain email)
8. Mark ticket Resolved; set 3-day follow-up reminder

DECISION POINT: If new joiner is a contractor → assign Guest access only (not E3 licence); skip laptop provisioning
HARD GATE: MFA must be enabled before credentials are shared — do not skip this step

Format: numbered steps; decision branches clearly labelled; hard gate marked with ⚠️ STOP. Include a version control table and a sign-off block.
Constraints: Use British English. Every step must begin with an action verb. Do not combine two actions in one step. Output only the SOP; no preamble.
```
Output: A complete, auditable SOP with decision branches, hard gates, and version control — ready for ISO 27001 audit review.

---

## Example 4: Tax technical note

**Bad prompt**
```
Write a tax note on the earn-out
```
Output: A generic description of earn-out tax principles with no application to facts, invented scenarios, and no specific statutory references. Professionally unusable.

**Good prompt**
```
You are a UK corporate tax adviser with expertise in M&A transactions. Write a professional tax technical note on the tax treatment of earn-out consideration.

QUESTION: Is the earn-out consideration payable to the selling shareholders of XYZ Ltd taxable as capital gains or employment income?

FACTS:
- Sellers: three UK-resident individuals; held shares for 4 years; all three are continuing as directors post-completion
- Transaction: share sale completed 1 January 2025; base consideration £8M
- Earn-out: contingent on cumulative EBITDA targets over 3 years post-completion; payable in cash; maximum earn-out £4M
- Earn-out is not conditional on continued employment (confirmed in the SPA)

APPLICABLE LAW:
- TCGA 1992 s.48 (earn-outs as contingent deferred consideration)
- ITEPA 2003 (employment income risk — sellers are continuing directors)
- HMRC's earn-out guidance (Employment Related Securities Manual ERS 40000+)

AREAS OF UNCERTAINTY:
- HMRC has challenged earn-out arrangements in recent cases where sellers are also directors
- The line between capital and income depends on whether the earn-out is truly independent of employment

PURPOSE: Client advice — to be reviewed by a qualified tax partner before delivery

Tone: formal and measured. State the conclusion with a confidence level. Use appropriate qualifiers ("it is our view", "we consider") where the law is uncertain.
Length: 2,000–2,500 words. 4–5 pages.
Format: standard tax note structure: (1) Question; (2) Summary of conclusion; (3) Facts; (4) Law and analysis; (5) Conclusion; (6) Recommendations; (7) Limitations.
Statutory reference format: "s.48 TCGA 1992" or "s.62 ITEPA 2003".
Constraints: Use British English. Do not state more confidently than the law supports. Flag areas where HMRC may challenge. Output only the note; no preamble.
```
Output: A professionally structured tax note with the correct statutory references, appropriate qualification of uncertainty, and a clear conclusion — ready for partner review.

---

## Example 5: Incident runbook

**Bad prompt**
```
Write a runbook for when the database goes down
```
Output: A generic 5-step list ("check the server", "restart the service") that provides no diagnostic guidance and no escalation path. Useless in a 2am incident.

**Good prompt**
```
You are an SRE and incident response specialist. Write an operational runbook for a specific incident type.

INCIDENT: Azure SQL Database — connection pool exhaustion on the production reporting database
SEVERITY: P2
DETECTION: Azure Monitor alert "SQLConnectionPoolExhausted" fires when active connections exceed 480/500 for more than 2 minutes

DIAGNOSTIC STEPS (to be completed in first 5 minutes):
1. Check Azure Monitor alert details — confirm which database and connection pool
2. Query sys.dm_exec_sessions to identify sessions by application and login_name
3. Check for long-running transactions (> 5 minutes): query sys.dm_exec_requests WHERE total_elapsed_time > 300000
4. Check recent deployments in Azure DevOps — was a new version released in the last 2 hours?

RESPONSE STEPS:
- If long-running transaction identified: KILL [session_id] — document session_id and login in incident ticket
- If recent deployment: initiate rollback via Azure DevOps pipeline [link to pipeline]
- If neither: scale up the Azure SQL tier from S4 to P1 (temporary — must be reviewed within 24 hours)

ESCALATION TRIGGER: If connection count does not fall below 400 within 15 minutes of taking action, escalate to Head of Infrastructure via PagerDuty

ESCALATION CONTACT: Head of Infrastructure — PagerDuty ID: [ID]; provide: alert name, current connection count, steps already taken

RESOLUTION VERIFICATION: Alert must be clear (connections below 400) for 10 consecutive minutes before marking resolved

POST-INCIDENT: Update ServiceDesk ticket with full timeline; trigger post-mortem if P2 lasted > 30 minutes; notify application owners if service was degraded

Format: numbered steps; commands in code blocks; decision branches clearly labelled; escalation in a clearly marked section. Include a header with severity, last tested date, and owner.
Constraints: Use British English. Every step must be an action. Include exact commands — do not say "run the diagnostic query" without providing the query. Output only the runbook; no preamble.
```
Output: A complete, executable runbook with specific queries, decision branches, escalation contacts, and resolution verification — ready for on-call use.

---

## Prompt anatomy: what every good prompt contains

```
┌─────────────────────────────────────────────────────────────┐
│ ROLE                                                         │
│ "You are a [specific expert type] with expertise in [domain]"│
├─────────────────────────────────────────────────────────────┤
│ TASK DEFINITION                                              │
│ "Write / Draft / Create / Analyse [specific document type]" │
│ "for [specific audience] to achieve [specific purpose]"     │
├─────────────────────────────────────────────────────────────┤
│ CONTEXT AND INPUT DATA                                       │
│ The specific facts, figures, and background the model needs │
│ to write from — not summaries, but the actual data          │
├─────────────────────────────────────────────────────────────┤
│ FORMAT SPECIFICATION                                         │
│ Document type / Length / Structure / Markdown or plain text │
├─────────────────────────────────────────────────────────────┤
│ TONE AND LANGUAGE                                            │
│ Formal / Professional / Conversational                       │
│ "Use British English throughout"                            │
├─────────────────────────────────────────────────────────────┤
│ CONSTRAINTS (what NOT to do)                                 │
│ "Do not include preamble" / "Do not invent figures"         │
│ "Do not use filler phrases" / "No Americanisms"             │
├─────────────────────────────────────────────────────────────┤
│ OUTPUT INSTRUCTION                                           │
│ "Output only the [document]; no preamble, no commentary"   │
└─────────────────────────────────────────────────────────────┘
```

| Bad prompt element | Good prompt element |
|-------------------|---------------------|
| One sentence | Multiple structured sections |
| No context | Specific facts and data |
| No audience | Named audience with role |
| No format | Explicit format, length, structure |
| No constraints | Explicit "do not" instructions |
| Relies on model to invent facts | Provides all data; asks model to write |
| American English default | "Use British English throughout" |
| Missing output instruction | "Output only the document; no preamble" |

---

The time you spend writing a good prompt is returned tenfold in reduced editing time. A 5-minute prompt that produces an 80%-usable draft beats a 1-minute prompt that produces something you must rewrite from scratch.

See [reference/llm-prompting-principles.md](../reference/llm-prompting-principles.md) for the full principles behind these examples.
