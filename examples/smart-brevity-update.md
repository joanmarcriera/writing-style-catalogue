---
title: Smart Brevity Update — Release Readiness
category: Example
description: A worked short update that makes status, consequence, owner, and next checkpoint visible in under a minute.
bundle_id: smart-brevity-update
artefact: Smart Brevity leadership update
audience: Product and engineering leadership
scenario: labelled-composite
style_path: styles/axios-smart-brevity.md
pattern_path: patterns/what-so-what-now-what.md
prompt_path: prompt-templates/executive-summary-prompts.md
skill_path: skills/create-one-page-brief.md
rubric_path: rubrics/executive-communication-rubric.md
---

# Smart Brevity Update — Release Readiness

## Professional context

Leaders need a 30-second readiness update that does not disguise a conditional launch as green. The output must keep status logic and the exact go/no-go checkpoint.

## Source packet

```text
SCENARIO: Labelled composite.
RELEASE: Customer reporting v2; target 18 August 2026.
STATUS: Amber until performance gate passes.
READY: security review complete; support guide approved; rollback rehearsal passed in staging.
OPEN: peak-load test at 2,000 concurrent report requests; test scheduled 13 August, owned by Performance Engineering.
THRESHOLD: p95 response below 2.5 seconds and error rate below 1% for 30 minutes.
CONSEQUENCE: failing either threshold moves launch to 25 August; no executive exception path.
NEXT CHECKPOINT: go/no-go meeting at 14:00 on 14 August.
UNKNOWN: Peak-load result.
```

## Completed prompt

```text
You are writing a Smart Brevity release-readiness update for product and engineering leadership. Produce a 30-second read using only the SOURCE PACKET.

Do not invent test results, customer impact, confidence, mitigations, dependencies, or executive discretion. The release remains Amber until both supplied performance thresholds pass. If the target date, status logic, open gate, owner, threshold, consequence, or checkpoint is missing, return MISSING INFORMATION rather than an update.

Use British English and this format: one-line headline; Why it matters; Ready; Still open; What happens next. Keep it between 120 and 170 words. Use short labels and no more than five bullets. State the 25 August fallback and that there is no exception path. Do not describe completed security or rollback work as proof of performance. Output only the update.

Before finalising, review factual integrity, signal-to-noise, status clarity, owner/date visibility, caveat preservation, and actionability against the Executive Communication Rubric. A fluent update that implies Green is a failed draft.

SOURCE PACKET:
[Paste the complete source packet above here.]
```

## Output excerpt

```text
Customer reporting v2 remains Amber pending one performance gate.

Why it matters: The 18 August launch depends on evidence that peak reporting load meets the agreed service threshold.

Ready
• Security review, support guide, and staging rollback rehearsal are complete.

Still open
• Performance Engineering will test 2,000 concurrent report requests on 13 August.
• Pass = p95 below 2.5 seconds and errors below 1% for 30 minutes.

What happens next: Go/no-go is 14:00 on 14 August. Failure of either threshold moves launch to 25 August; there is no executive exception path.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Factual integrity | 5 | No test result or confidence is invented. | Pass |
| Structure | 5 | Status, gate, threshold, consequence, and checkpoint scan quickly. | Pass |
| Professional tone | 5 | Direct, calm, and free of launch theatre. | Pass |
| Risk awareness | 5 | Amber status and the non-negotiable fallback remain clear. | Pass |
| Usefulness | 5 | Leaders know the owner, test, date, and decision point. | Pass |

## Human review before use

- The release manager must confirm current status immediately before distribution.
- Performance Engineering must verify the threshold and test schedule.
- The meeting owner must confirm the go/no-go time and attendee list.

## Reuse this bundle

- [Smart Brevity Style](../styles/axios-smart-brevity.md)
- [What / So What / Now What Pattern](../patterns/what-so-what-now-what.md)
- [Executive Summary Prompts](../prompt-templates/executive-summary-prompts.md)
- [Create One-Page Brief Skill](../skills/create-one-page-brief.md)
- [Executive Communication Rubric](../rubrics/executive-communication-rubric.md)
