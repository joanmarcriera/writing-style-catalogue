# Style Selection Guide

How to choose the right writing style for your document.

## Selection by Purpose

### You Need to Update Someone Quickly

**Smart Brevity** or **BLUF**

- Smart Brevity: Good for status updates, company news, announcements
- BLUF: Better for emails that require action, decisions, or responses

**Use when:** Audience is busy, time is limited, information is straightforward

**Avoid:** Complex decisions, major strategic changes (use Minto instead)

### You Need to Recommend Something

**Minto Pyramid Principle** or **Consulting Style**

- Minto: For logical, step-by-step recommendations
- Consulting: For strategic, high-stakes recommendations

**Use when:** Decision-maker needs convincing, complex analysis required, stakes are moderate to high

**Avoid:** Quick updates (use Smart Brevity), simple instructions (use Plain English)

### You Need to Explain Something

**Plain English**, **Socratic Explainer**, or **Tutorial**

- Plain English: For any audience, jargon-free
- Socratic: For teaching and learning, interactive feel
- Tutorial: For step-by-step how-to guides

**Use when:** Audience has mixed expertise, clarity is paramount, education is the goal

**Avoid:** Technical audience needing precision (use Technical Documentation)

### You Need Formal Documentation

**Board Paper**, **Technical Documentation**, or **Legal Professional**

- Board Paper: For board meetings, major strategic decisions
- Technical: For engineering, architecture, detailed specifications
- Legal: For contracts, compliance, formal agreements

**Use when:** Permanence required, legal/formal context, comprehensive detail needed

**Avoid:** Quick communication (use BLUF), narrative content (use storytelling)

## Selection by Audience

| Audience | Primary Style | Alternatives |
|----------|---------------|---------------|
| C-Suite Executive | Smart Brevity, BLUF, Executive Briefing | Minto Pyramid |
| Board Members | Board Paper, Executive Briefing | Consulting Style |
| Engineering Team | Technical Documentation, ADR | Plain English |
| Sales Team | Persuasive Sales, Narrative Storytelling | BLUF |
| Legal/Compliance | Legal Professional, Tax Advisory | Board Paper |
| General Internal | Smart Brevity, BLUF, Narrative Storytelling | Plain English |
| Public/External | Journalistic, Crisis Communications, Plain English | Persuasive Sales |
| Students/Learners | Socratic Explainer, Tutorial, Plain English | Narrative Storytelling |

## Selection by Document Type

| Document | Recommended Style | Template Location |
|----------|-------------------|-------------------|
| Executive Update | Smart Brevity | prompt-templates/executive-summary-prompts.md |
| Email | BLUF | prompt-templates/email-prompts.md |
| Memo | Minto or Consulting | prompt-templates/memo-prompts.md |
| Board Paper | Board Paper | prompt-templates/board-paper-prompts.md |
| Technical Doc | Technical Documentation | prompt-templates/technical-documentation-prompts.md |
| Architecture Decision | ADR | prompt-templates/decision-record-prompts.md |
| Incident Report | Incident Report | prompt-templates/incident-report-prompts.md |
| Policy Brief | Policy Brief | prompt-templates/policy-prompts.md |
| Proposal/Business Case | Consulting or Minto | prompt-templates/strategy-prompts.md |
| Job Cover Letter | Job Application | prompt-templates/job-application-prompts.md |
| LinkedIn Post | Social Media | prompt-templates/linkedin-prompts.md |
| Sales Outreach | Persuasive Sales | prompt-templates/sales-outreach-prompts.md |

## Decision Tree

**Start here:**

1. **How much time do you have?**
   - **Less than 30 minutes** → Smart Brevity or BLUF
   - **More than 30 minutes** → Proceed to next question

2. **What is the primary goal?**
   - **Update/inform** → Smart Brevity
   - **Get action/decision** → BLUF or Minto Pyramid
   - **Recommend change** → Minto Pyramid or Consulting Style
   - **Teach/explain** → Plain English, Socratic, or Tutorial
   - **Formal record** → Board Paper, ADR, or Technical Documentation

3. **Who is the audience?**
   - **Very senior, busy** → Smart Brevity
   - **Technical specialists** → Technical Documentation
   - **Legal/compliance** → Legal Professional or Tax Advisory
   - **Board/investors** → Board Paper or Executive Briefing
   - **Mixed audience** → Plain English

4. **What is the complexity?**
   - **Simple, straightforward** → BLUF
   - **Moderately complex** → Minto Pyramid or Consulting
   - **Highly technical** → Technical Documentation
   - **Multi-faceted with options** → Board Paper

5. **Pick your style** from recommendations above.

---

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Using Minto for quick updates | It's too detailed for busy audiences | Use Smart Brevity or BLUF |
| Using Board Paper for emails | Too formal, too long for email | Use BLUF |
| Using Plain English for technical specs | Loses precision | Use Technical Documentation or ADR |
| Mixing multiple styles in one doc | Confuses reader | Pick one primary style, one secondary if needed |
| Ignoring audience expertise | Creates mismatch (too simple or too complex) | Choose style matching audience knowledge |
| Writing without structure | Loses impact | Pick a style *first*, then write |

---

See [CHEATSHEET.md](CHEATSHEET.md) for a quick style comparison table.

See individual style files in `styles/` for deep guidance on each framework.
