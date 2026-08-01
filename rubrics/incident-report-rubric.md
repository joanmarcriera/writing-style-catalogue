---
title: Incident Report Rubric
category: Rubric
description: Scores whether an incident report is evidence-led, blameless, operationally useful, and accountable for prevention work.
---

# Incident Report Rubric

Use this before closing a material service or security incident review.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Impact | Vague or minimised | Duration or users stated | Duration, affected services/users, business effect, and data/security status are evidenced |
| Timeline | Missing or contradictory | Main events listed | Timestamped detection, decisions, mitigations, recovery, and verification align with records |
| Causal analysis | Blames a person or guesses | Immediate cause identified | Trigger, contributing conditions, control gaps, and evidence limits are separated |
| Response assessment | Declares success without evidence | Actions summarised | What helped, what delayed recovery, and why are supported by the timeline |
| Corrective actions | Generic recommendations | Owners or dates present | Each action has owner, due date, priority, acceptance test, and tracking reference |
| Factual integrity | Invented certainty or metrics | Most claims traceable | Every claim maps to logs, tickets, monitoring, or an explicitly labelled assumption |
| Learning quality | Restates the event | Some useful lessons | Lessons change a control, runbook, test, alert, or decision process |

## Pass standard

Impact, timeline, causal analysis, corrective actions, and factual integrity must score at least **4**. No criterion may score below **3**.

## Red flags

- “Root cause” is asserted without distinguishing evidence from hypothesis.
- The report names individual error while ignoring system conditions.
- Actions use verbs such as “improve” or “review” without an acceptance test.
- Resolution is declared before service and customer-impact measures are stable.
