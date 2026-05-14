---
title: Structure Patterns
category: Reference
---

# Common Structural Patterns

The structure of a document determines whether its argument is accessible or opaque. Choose a structure that matches your message type — not the structure you habitually use or the one that was easiest to draft. The right structure makes the reader's job effortless; the wrong one makes them work to find your point.

---

## Pattern 1: BLUF — Bottom Line Up Front

**Best for**: Executive emails, status updates, memos, any communication where the reader needs the answer before the evidence.

**When to use it**: When your audience is senior, time-constrained, or when the conclusion is known and you are seeking approval or awareness.

**When not to use it**: When the conclusion is controversial and the reader needs to be led to it through evidence before they encounter the recommendation.

```
┌─────────────────────────────────────┐
│  BOTTOM LINE                        │
│  (The answer, recommendation, or    │
│   key fact — in the first sentence) │
├─────────────────────────────────────┤
│  EVIDENCE                           │
│  (The 3–5 facts that support it)    │
├─────────────────────────────────────┤
│  CONTEXT                            │
│  (Background, if needed)            │
├─────────────────────────────────────┤
│  ACTION / ASK                       │
│  (What you need from the reader)    │
└─────────────────────────────────────┘
```

**Example**: "We recommend proceeding with the Azure migration. Annual savings of £800k from year 2 outweigh the one-off cost of £2.1M, with a 32-month payback. We need board approval by 15 June to meet the procurement timeline."

---

## Pattern 2: Problem → Solution → Action

**Best for**: Business cases, proposals, recommendations, problem-solving memos.

**When to use it**: When the reader needs to understand the problem before they will accept the solution — when the recommendation is non-obvious.

**When not to use it**: When the reader already knows the problem well — you can skip straight to the solution.

```
┌─────────────────────────────────────┐
│  PROBLEM                            │
│  (What is broken, costly, or risky) │
│  (Quantify: how bad, how often)     │
├─────────────────────────────────────┤
│  WHY IT MATTERS NOW                 │
│  (Urgency: what changes if we wait) │
├─────────────────────────────────────┤
│  SOLUTION                           │
│  (What you propose)                 │
│  (Why this option over others)      │
├─────────────────────────────────────┤
│  EVIDENCE / ANALYSIS                │
│  (Data, financial model, options)   │
├─────────────────────────────────────┤
│  ACTION / NEXT STEPS                │
│  (What happens now; who does what)  │
└─────────────────────────────────────┘
```

**Example**: A business case for an IAM programme: current state (access-related incidents, compliance gaps, provisioning delays), urgency (ISO 27001 audit in 6 months), solution (3-phase IAM programme), evidence (financial model, risk reduction), ask (board approval for £1.4M).

---

## Pattern 3: Situation → Complication → Resolution (SCR)

**Best for**: Incident updates, change announcements, strategic pivots, storytelling in executive communications.

**When to use it**: When the reader needs context to understand why you are taking a specific action — when something has changed that requires a response.

**When not to use it**: When there is no complication — do not manufacture complexity to fit the pattern.

```
┌─────────────────────────────────────┐
│  SITUATION                          │
│  (What was true; the stable state)  │
├─────────────────────────────────────┤
│  COMPLICATION                       │
│  (What changed; the disruption)     │
├─────────────────────────────────────┤
│  RESOLUTION                         │
│  (What we are doing in response)    │
├─────────────────────────────────────┤
│  NEXT STEPS                         │
│  (Timeline and owners)              │
└─────────────────────────────────────┘
```

**Example**: An incident post-mortem: Situation (authentication service running normally), Complication (Azure AD outage caused 45-minute login failure for 600 users), Resolution (failover to backup auth path; Microsoft resolved root cause at 14:22), Next steps (implement redundant auth path by Q3; post-mortem review 20 May).

---

## Pattern 4: Question → Analysis → Conclusion (QAC)

**Best for**: Tax technical notes, legal opinions, analytical memos, research documents, ADRs.

**When to use it**: When the output is an answer to a specific question — and when the evidence must be presented before the conclusion can be understood.

**When not to use it**: When the audience needs the answer first (use BLUF for a summary, then QAC for the detail).

```
┌─────────────────────────────────────┐
│  QUESTION                           │
│  (State the precise question)       │
├─────────────────────────────────────┤
│  FACTS                              │
│  (The relevant circumstances)       │
├─────────────────────────────────────┤
│  ANALYSIS                           │
│  (Apply the law / framework / data  │
│   to the facts, step by step)       │
├─────────────────────────────────────┤
│  CONCLUSION                         │
│  (The answer; with confidence level │
│   and any conditions or caveats)    │
├─────────────────────────────────────┤
│  NEXT STEPS                         │
│  (Recommended actions; filings;     │
│   further research needed)          │
└─────────────────────────────────────┘
```

**Note**: For a professional reader in a hurry, add a "Summary of conclusion" section immediately after the Question — giving the answer upfront before walking through the analysis. The QAC body then functions as the detailed support.

---

## Pattern 5: Options Analysis (A vs. B vs. C)

**Best for**: Decision documents, board papers, strategic choice communications, comparisons.

**When to use it**: When the reader must choose between alternatives — and when showing you considered multiple options is as important as the recommendation itself.

**When not to use it**: When there is genuinely only one viable option. Presenting a "choice" between one good option and two obvious strawmen destroys credibility.

```
┌─────────────────────────────────────┐
│  DECISION CONTEXT                   │
│  (Why a decision is needed now)     │
├─────────────────────────────────────┤
│  OPTION A: Do nothing               │
│  Description | Costs | Risks        │
│  Pros | Cons                        │
├─────────────────────────────────────┤
│  OPTION B: [Alternative]            │
│  Description | Costs | Risks        │
│  Pros | Cons                        │
├─────────────────────────────────────┤
│  OPTION C: [Recommended]            │
│  Description | Costs | Risks        │
│  Pros | Cons                        │
├─────────────────────────────────────┤
│  RECOMMENDATION                     │
│  (Which option; decisive factors;   │
│   conditions on the recommendation) │
└─────────────────────────────────────┘
```

**Key rule**: "Do nothing" must always be Option A, with its genuine costs and risks — not just listed to be dismissed. Board members and CFOs will ask what happens if we do nothing; have the answer.

---

## Pattern 6: Before → After → Results

**Best for**: Case studies, transformation stories, project close-out reports, investor updates highlighting progress.

**When to use it**: When you have completed something and need to demonstrate the impact — especially for audiences who approved the investment.

**When not to use it**: For documents about future plans (use Roadmap or Problem-Solution instead).

```
┌─────────────────────────────────────┐
│  BEFORE (Initial situation)         │
│  (Quantify the starting point)      │
├─────────────────────────────────────┤
│  WHAT WE DID                        │
│  (The intervention — specific,      │
│   named actions and decisions)      │
├─────────────────────────────────────┤
│  AFTER (Measurable results)         │
│  (Quantify the change; compare to   │
│   the starting point and the plan)  │
├─────────────────────────────────────┤
│  LESSONS                            │
│  (What we would do differently;     │
│   what applies to future projects)  │
└─────────────────────────────────────┘
```

**Example**: Cloud migration close-out: Before (£1.22M annual on-premise cost; 72h RTO; 3 incidents last year), What we did (18-month Azure migration in 3 phases), After (£420k annual cloud cost; 4h RTO; 0 infrastructure incidents in 12 months), Lessons (PAM should have been implemented earlier in Phase 1; change management for staff took twice as long as planned).

---

## Pattern 7: Pyramid (Minto Pyramid Principle)

**Best for**: Consulting-style recommendations, complex analytical documents, management presentations.

**When to use it**: When you have a complex analysis with multiple supporting arguments — when the reader needs to understand the full logical structure, not just the conclusion.

**When not to use it**: For short documents or when the audience wants bullet-point brevity.

```
        ┌─────────────┐
        │  CONCLUSION  │
        │ (one sentence│
        │ — the answer)│
        └──────┬───────┘
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│Key msg 1│ │Key msg 2│ │Key msg 3│
└────┬────┘ └────┬────┘ └────┬────┘
     │           │           │
  (evidence)  (evidence)  (evidence)
```

**Structure rule**: Every point at one level must either support the point above it (deductive) or be part of a mutually exclusive, collectively exhaustive (MECE) set at the same level.

---

## Pattern 8: Narrative Arc (for change communications)

**Best for**: Staff communications about major changes, leadership announcements, investor letters, change management messaging.

**When to use it**: When the audience needs to feel the journey, not just receive information — when emotional engagement matters alongside intellectual understanding.

**When not to use it**: For analytical or decision documents — narrative is engaging but not precise enough for governance.

```
┌─────────────────────────────────────┐
│  WHERE WE WERE                      │
│  (The old state — acknowledge it    │
│   honestly; do not dismiss it)      │
├─────────────────────────────────────┤
│  WHAT CHANGED                       │
│  (The external force or internal    │
│   decision that required a change)  │
├─────────────────────────────────────┤
│  WHAT WE ARE DOING                  │
│  (The response — specific actions)  │
├─────────────────────────────────────┤
│  WHAT THIS MEANS FOR YOU            │
│  (Audience-specific impact)         │
├─────────────────────────────────────┤
│  WHAT COMES NEXT                    │
│  (Timeline; how they will be kept   │
│   informed; where to get help)      │
└─────────────────────────────────────┘
```

---

## Choosing the right pattern

| Message type | Recommended pattern |
|--------------|---------------------|
| Need approval for a recommendation | BLUF or Pyramid |
| Explaining a problem and proposing a fix | Problem → Solution → Action |
| Answering a specific technical question | QAC |
| Major change announcement to staff | Narrative Arc or SCR |
| Choosing between alternatives | Options Analysis |
| Demonstrating impact of completed work | Before → After → Results |
| Analytical report for senior audience | Pyramid |
| Incident or crisis update | SCR |

---

Match your structure to your message type. The right structure makes your argument clearer than any individual sentence improvement can.
