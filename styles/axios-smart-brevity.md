---
title: Smart Brevity
category: Concise
best_for: Executive status updates, company-wide announcements, and board or investor communications where the reader has limited time and needs the key facts in under 60 seconds. Ideal for recurring update formats such as weekly leadership briefs, incident summaries, or product milestone announcements.
not_good_for: Complex strategic recommendations requiring full argument and evidence (use Minto Pyramid); formal governance documents requiring narrative depth (use Board Paper); technical specifications (use Technical Documentation).
default_tone: Direct and confident. Factual, not conversational. No hedging.
typical_length: 150–250 words
aliases: [Axios Style, Smartsheet]
---

# Smart Brevity

## What this style is

Smart Brevity is a rapid, scannable format developed by Axios for busy readers who cannot afford to read long updates. Every piece follows a strict structure: a single-sentence headline that captures the whole story, three to five bullet points with the most important facts, a short paragraph of supporting context, and — where relevant — a clear next steps line.

The style was designed around the insight that most professional writing buries the key message in paragraphs of context. Smart Brevity inverts this: the reader should understand the story entirely from the headline and bullets, and read the context paragraph only if they want more.

**Core principle**: Readers should understand the full story in 30 seconds. Everything else is optional context.

## When to use it

- Weekly or monthly executive status updates to leadership or the board
- Company-wide announcements about a decision, change, or milestone
- Incident or outage summaries sent to stakeholders during or after an event
- Market or competitive intelligence updates for senior audiences
- Product launch announcements to internal or external audiences
- Quarterly performance summaries shared with investors or the board
- Meeting recaps requiring follow-up action

## When not to use it

- Complex recommendations requiring logical argument — use [Minto Pyramid Principle](minto-pyramid-principle.md) instead
- Detailed technical specifications or runbooks — use [Technical Documentation](technical-documentation.md) instead
- Teaching or onboarding — use [Tutorial Style](tutorial-style.md) or [Socratic Explainer](socratic-explainer.md) instead
- Formal board documents requiring depth and governance rigour — use [Board Paper Style](board-paper-style.md) instead
- Legal or compliance documents where omitting context creates risk

## Core structure

```
[HEADLINE]
One clear, punchy sentence that captures the whole story.
Include a number or outcome where possible.

[SUBHEADING] (optional)
One-line additional context or framing.

[KEY POINT 1]
Specific fact or finding. One sentence.

[KEY POINT 2]
Specific fact or finding. One sentence.

[KEY POINT 3]
Specific fact or finding. One sentence.

[KEY POINT 4] (optional)
Add only if genuinely distinct from points above.

[KEY POINT 5] (optional)
Add only if genuinely distinct from points above.

[CONTEXT]
One short paragraph of background or supporting numbers.
This is the only paragraph-format section.

[NEXT STEPS] (optional)
What happens next. Who is responsible. By when.
```

## Copy-paste prompt

```
You are a Smart Brevity writing expert. Your task is to convert the following input into a Smart Brevity update.

AUDIENCE: [AUDIENCE — e.g. "C-suite leadership team", "board of directors", "all-company"]
PURPOSE: [PURPOSE — e.g. "weekly engineering status update", "incident summary", "product milestone announcement"]
CONTEXT: [CONTEXT — e.g. "This follows last quarter's 15% velocity decline; team has since completed technical debt work"]
INPUT: [INPUT — paste the raw information, notes, or draft here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "Reader understands the situation and knows the next step without needing to ask follow-up questions"]
TONE: [TONE — e.g. "Direct and factual", "Confident but not triumphalist", "Calm during an incident"]
LENGTH: [LENGTH — e.g. "150–200 words total"]
FORMAT: [FORMAT — headline + bullets + context paragraph + next steps]
CONSTRAINTS: [CONSTRAINTS — e.g. "Do not include any unconfirmed figures", "Avoid mentioning the vendor by name", "Must be suitable for external sharing"]

INSTRUCTIONS:
1. Write a single-sentence headline that captures the whole story. Include a specific number or outcome if available.
2. Write 3–5 bullet points. Each must be one sentence maximum. Each must contain a specific fact — no vague claims.
3. Write one short context paragraph (3–5 sentences) with supporting background or numbers.
4. If action is required, add a "Next Steps" line stating what happens, who owns it, and by when.
5. Total length must not exceed [LENGTH].
6. Use British English throughout (colour, organisation, licence, favour, etc.).
7. Preserve all factual claims exactly as provided in [INPUT]. If you are uncertain whether something is a fact or an assumption, flag it with "(assumed)" in parentheses.
8. Do not add information not present in [INPUT]. Do not remove facts that are present.
9. Use active voice throughout. No hedging language ("seems," "quite," "relatively," "potentially").

Output the Smart Brevity update only. No preamble, no commentary.
```

## Output format

The finished document is typically a single screen on a mobile device or one third of a page. It contains:

- **Headline**: Bold, one sentence, 10–15 words maximum
- **Bullets**: 3–5 items, each one sentence, each starting with a capital letter, no full stop required
- **Context**: One paragraph, 3–5 sentences, plain prose
- **Next Steps**: One or two sentences, plain prose or a single bullet

The document has no formal header, no date line (unless convention requires it), and no signature block. It is designed to be read in an email body, a Slack message, or the first slide of a deck. Total word count: 150–250 words.

## Example

**IAM Platform Migration Complete — Identity Incidents Down 78% Since Go-Live**

- The legacy identity and access management platform was decommissioned on 30 April, four days ahead of schedule
- Role-based access control policies have been applied across all 14 production systems; 2,300 user accounts migrated
- Identity-related security incidents dropped from 18 per month to four in the first 30 days post-migration
- Privileged access review cycle time fell from 11 days to two days using the new automated workflow
- Three legacy service accounts remain open pending supplier confirmation; expected closure by 16 May

**Context**
The IAM migration was initiated in January following two access-control breaches linked to shared credentials on the legacy system. The project ran across four squads over 16 weeks, integrating with our Azure Active Directory tenant and replacing a bespoke on-premises tool. All audit logging is now centralised in the SIEM platform, which satisfies the ISO 27001 control gap identified in last year's external audit. Supplier SLAs for the new platform include a 99.9% uptime commitment with 15-minute incident response.

**Next Steps**
Close the three remaining legacy service accounts by 16 May (owner: Identity Team). Present final migration report to the CISO by 23 May.

## Quality checklist

- [ ] Headline is a single sentence containing a specific outcome or number
- [ ] Each bullet is one sentence maximum with a concrete fact
- [ ] No bullet is vague or a repeat of another
- [ ] Bullet count is between 3 and 5
- [ ] Context paragraph is plain prose, not a list
- [ ] No jargon or unexplained acronyms
- [ ] Total word count is under 250 words
- [ ] Next steps are clear with owner and date (if applicable)
- [ ] British English used throughout
- [ ] Can be fully understood in 30 seconds

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Vague headline | Reader does not know what the update is about | Make it specific: "IAM incidents down 78%" not "Good progress on identity" |
| Too many bullet points | Overwhelms the reader; defeats the purpose of the format | Keep to 3–5 maximum; merge or cut |
| Long context paragraph | Loses the scanning advantage | Break into short sentences; cut anything non-essential |
| Weak verbs and hedging | Sounds uncertain and unprofessional | Use active voice: "We reduced costs" not "Costs were reduced" |
| Missing numbers | Impact is unclear and unverifiable | Always include metrics: "23% up" not "significant improvement" |
| No next steps | Reader does not know what to do | Always end with what comes next, who owns it, and by when |
| Multiple stories in one update | Confuses narrative; reader cannot track the main point | One headline per update; use separate updates for multiple stories |

---

See [prompt-templates/executive-summary-prompts.md](../prompt-templates/executive-summary-prompts.md) for detailed prompt templates.

See [examples/smart-brevity-update.md](../examples/smart-brevity-update.md) for a complete example.
