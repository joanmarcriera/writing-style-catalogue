---
title: Technical Documentation Rubric
category: Rubric
description: Scores whether technical documentation is accurate, usable, and safe for engineers or operators.
---

# Technical Documentation Rubric

Use this for runbooks, ADRs, SOPs, architecture guides, API docs, and operational procedures.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Audience and scope | Unclear | Basic scope stated | Reader, purpose, scope, and exclusions are explicit |
| Prerequisites | Missing | Some access/tools listed | Access, tools, versions, permissions, and assumed knowledge are complete |
| Procedure quality | Vague prose | Some steps actionable | Numbered, testable steps with exact commands or paths where needed |
| Technical accuracy | Unverified or invented | Plausible but not tested | Claims, commands, versions, and examples verified or flagged as needing verification |
| Troubleshooting | Missing | Basic symptoms listed | Symptoms, causes, checks, resolutions, and escalation triggers included |
| Safety | Risks not mentioned | Some warnings present | Destructive actions, rollback, data loss, permissions, and blast radius are explicit |
| Maintainability | No owner or date | Owner/date present | Owner, review cycle, last tested date, and change trigger stated |
| Structure | Hard to scan | Reasonable headings | Task-oriented structure with clear headings, tables, and code blocks |

## Pass standard

Runbooks and SOPs should not be published unless procedure quality, technical accuracy, and safety score **4 or higher**.

## Red flags

- "Check the logs" without naming the system, path, query, or expected result.
- Commands are included but not tested.
- No rollback or escalation path for risky actions.
- The document assumes tribal knowledge from the original author.
