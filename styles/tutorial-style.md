---
title: Tutorial Style
category: Educational
best_for: Step-by-step procedural guides where a reader must accomplish a specific task — setting up a tool, completing a process, or following a procedure — and may be unfamiliar with the domain. Ideal for onboarding documentation, setup guides, how-to articles, and learning-by-doing content where success is a concrete, verifiable outcome.
not_good_for: Executive communication where the reader needs a summary and recommendation, not instructions (use Smart Brevity or Executive Briefing); technical reference documentation for practitioners who already understand the system (use Technical Documentation); conceptual understanding where the goal is insight rather than task completion (use Socratic Explainer).
default_tone: Clear, encouraging, and practical. Patient without being patronising.
typical_length: 500–2,000 words depending on the scope of the task; simple single-purpose tutorials are 500–800 words; multi-step complex procedures may be 1,500–2,000 words
aliases: [How-To Guide, Step-by-Step Guide, Procedural Guide]
---

# Tutorial Style

## What this style is

A tutorial is a piece of writing that gets a reader from a starting state to a known end state by guiding them through every step in sequence. It assumes the reader wants to accomplish a specific outcome and may not know how. Every step is explicit — nothing is left implied. The tutorial succeeds when a reader with the stated prerequisites can complete the task from start to finish without asking for help.

The hallmark of a great tutorial is not the quality of its prose but the quality of its thinking about the reader. The writer must inhabit the novice's perspective: What does the reader see on their screen at each step? What could go wrong? What should they check before proceeding? The verification step — checking that the previous step worked before continuing — is one of the most important elements and the one most often omitted.

**Core principle**: Every step is crystal clear. A reader with the stated prerequisites can follow this from start to finish without external help and know when they have succeeded.

## When to use it

- Setup and installation guides for tools, platforms, or environments
- Onboarding procedures for new team members or customers
- How-to guides for operational procedures (e.g. deploying a release, rotating a credential)
- Learning-by-doing content for technical or operational skill development
- Process documentation where the sequence and exactness of steps matters
- Troubleshooting guides for known failure scenarios with step-by-step resolution

## When not to use it

- Executive communication — use [Smart Brevity](axios-smart-brevity.md) or [Executive Briefing](executive-briefing.md) instead
- Technical reference documentation for practitioners who understand the system — use [Technical Documentation](technical-documentation.md) instead
- Conceptual learning where insight matters more than task completion — use [Socratic Explainer](socratic-explainer.md) instead
- Formal governance documents — use [Board Paper Style](board-paper-style.md) instead

## Core structure

```
[TITLE]
"How to [accomplish the specific goal]"
Specific enough that the reader knows immediately if this is for them.

[INTRODUCTION — 2–4 SENTENCES]
What the reader will accomplish.
Why this matters or when they would need to do this.
How long it takes (give a realistic estimate).

[PREREQUISITES]
Everything the reader must have in place before starting.
Access, accounts, installed tools with version numbers.
Knowledge assumed (be specific — "basic familiarity with the command line").
If a prerequisite is missing, where to get it.

[OVERVIEW — OPTIONAL]
A one-paragraph map of what the reader will do.
Helpful for multi-step tutorials so the reader knows where they are going.

[STEP 1: [STEP TITLE]]
What this step accomplishes (one sentence).
The exact action to take — specific commands, clicks, or entries.
Expected output or result — what the reader sees when it has worked.

[STEP 2: [STEP TITLE]]
[Continue for each step — same pattern.]

[VERIFICATION]
How to confirm the entire task was completed successfully.
The exact commands, checks, or outputs to look for.
"If you see X, you have succeeded."

[TROUBLESHOOTING]
The most common failure modes with their symptoms.
For each: the error or symptom, the likely cause, the resolution.
Where to look for more information.

[NEXT STEPS]
What to do after completing this tutorial.
Related tutorials or documentation.
How to go further or explore the topic.
```

## Copy-paste prompt

```
You are an expert technical writer specialising in tutorials and how-to guides. Your task is to write a clear, step-by-step tutorial from the following brief.

AUDIENCE: [AUDIENCE — e.g. "Software engineers with command-line experience but no prior Kubernetes knowledge", "IT administrators configuring Okta for the first time", "Business analysts setting up a data pipeline in dbt — no coding background required"]
PURPOSE: [PURPOSE — e.g. "Guide the reader through setting up SCIM provisioning between Okta and a downstream SaaS application", "Walk a new engineer through their first Kubernetes deployment", "Show an IT admin how to rotate API keys in the secrets vault"]
CONTEXT: [CONTEXT — e.g. "This replaces a two-hour shadowing session with a senior engineer; new team members will use this guide in their first week", "The current documentation is out of date for v2 of the tool — this must cover v2 specifically"]
INPUT: [INPUT — paste all steps, commands, expected outputs, screenshots descriptions, prerequisites, and common errors here]
DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. "The reader completes the task successfully without asking for help and knows exactly what success looks like", "A new team member can complete this task on day two without blocking anyone else"]
TONE: [TONE — e.g. "Clear and encouraging — reassuring for beginners without being condescending", "Direct and practical — assumes technical competence; no hand-holding on basics already covered in prerequisites"]
LENGTH: [LENGTH — e.g. "800–1,200 words", "Under 1,000 words — concise and focused on one specific task"]
FORMAT: [FORMAT — e.g. "Markdown with numbered steps, code blocks for all commands, and a troubleshooting table at the end"]
CONSTRAINTS: [CONSTRAINTS — e.g. "All commands must work on macOS 14 and Ubuntu 22.04 — specify when a command differs", "Do not include any production credentials or internal hostnames", "Maximum three levels of numbered steps — do not nest more deeply"]

INSTRUCTIONS:
1. Write a title in the format "How to [accomplish the specific goal]."
2. Write a 2–4 sentence introduction stating what the reader will accomplish, why it matters, and how long it takes.
3. List all prerequisites explicitly and specifically. Include version numbers for tools. Include links or instructions for obtaining missing prerequisites.
4. Number every step. Each step must have a title, the exact action to take (including the precise command or click path), and the expected output or result.
5. After the final step, include a Verification section with the exact command or check that confirms the task was completed successfully.
6. Include a Troubleshooting section covering the most common failure modes from [INPUT]. For each: the symptom, the likely cause, and the resolution.
7. Close with a Next Steps section pointing to related tutorials or further reading.
8. Use British English throughout (colour, organisation, licence, favour, etc.).
9. Preserve all commands, file paths, version numbers, and expected outputs exactly as provided in [INPUT]. Do not invent commands or modify syntax.
10. Flag any step where the behaviour or output may differ between operating systems or versions.

Output the tutorial only. No preamble, no commentary.
```

## Output format

A tutorial is typically published in Markdown (for developer portals, GitHub, or documentation platforms) or as a Word/PDF document. It contains:

- **Title**: "How to [goal]" — specific and outcome-oriented
- **Introduction**: 2–4 sentences of plain prose
- **Prerequisites**: Bulleted list with version numbers and links
- **Steps**: Numbered (Step 1, Step 2, etc.) with sub-steps as numbered or bulleted lists within each step
- **Code blocks**: All commands, file contents, and expected outputs in fenced code blocks with language identifier
- **Verification**: A distinct headed section with confirmation commands and expected output
- **Troubleshooting**: Table or headed sub-sections — each with Symptom / Cause / Resolution
- **Next Steps**: 3–5 bullet points with links or references

The tutorial does not use dense prose. White space is essential. Each step is visually distinct. Code blocks are used generously — any text the reader must type or copy should be in a code block.

## Example

**How to Configure SCIM Provisioning Between Okta and Slack**

This tutorial walks you through setting up automated user provisioning between Okta and Slack using SCIM 2.0. When complete, Okta will automatically create, update, and deactivate Slack user accounts as people join or leave your organisation. The setup takes approximately 30 minutes.

**Prerequisites**

Before starting, you need:
- Okta Super Administrator or Application Administrator access
- Slack Workspace Owner access
- Slack Business+ or Enterprise Grid plan (SCIM is not available on Free or Pro plans — confirm with your Slack admin)
- The Okta and Slack integration enabled on your Okta tenant (confirm by navigating to Applications → Browse App Catalogue and searching for "Slack")

---

**Step 1: Generate a SCIM API Token in Slack**

Slack requires a bearer token to authenticate provisioning requests from Okta.

1. Log into your Slack workspace as a Workspace Owner.
2. Navigate to **[your-workspace].slack.com/admin/scim** — replace `[your-workspace]` with your Slack subdomain.
3. Click **Generate Token**.
4. Copy the token immediately. **You will not be able to view it again after leaving this page.** Store it in your organisation's secrets vault.

Expected result: You have a token that looks like `xoxp-...` (a long alphanumeric string beginning with `xoxp-`).

---

**Step 2: Add and Configure the Slack Application in Okta**

1. In the Okta Admin Console, navigate to **Applications → Applications**.
2. Click **Browse App Catalogue**.
3. Search for "Slack" and select the **Slack** application (published by Slack Technologies).
4. Click **Add Integration**.
5. On the General Settings tab, enter your Slack workspace subdomain (e.g. `acme-team` if your workspace URL is `acme-team.slack.com`).
6. Click **Done**.

Expected result: The Slack application appears in your Okta Applications list with Status: Active.

---

**Step 3: Configure SCIM Provisioning in Okta**

1. Open the Slack application in Okta (click the application name in the list).
2. Navigate to the **Provisioning** tab.
3. Click **Configure API Integration**.
4. Check the box labelled **Enable API Integration**.
5. In the **API Token** field, paste the bearer token you copied in Step 1.
6. Click **Test API Credentials**. You should see: *"Slack was verified successfully."*

If you see an error, verify that:
- The token begins with `xoxp-` (not `xoxs-` or `xoxb-`)
- Your Slack plan is Business+ or Enterprise Grid
- The token was not accidentally truncated when copied

7. Click **Save**.

---

**Step 4: Enable Provisioning Actions**

1. On the Provisioning tab, click **To App** in the left sidebar.
2. Enable the following options by clicking **Edit** and checking each box:
   - **Create Users** — required for automatic account creation
   - **Update User Attributes** — required to keep names, emails, and roles in sync
   - **Deactivate Users** — required for automatic offboarding
3. Click **Save**.

Expected result: All three provisioning actions show as enabled (green checkmarks).

---

**Step 5: Assign Users to the Slack Application**

Provisioning only runs for users or groups assigned to the application in Okta.

1. Navigate to the **Assignments** tab.
2. Click **Assign** and choose **Assign to Groups** (recommended) or **Assign to People**.
3. Select the group or individual users who should have Slack access.
4. Click **Assign** and then **Done**.

Expected result: Okta sends a provisioning request for each assigned user within approximately two minutes.

---

**Verification**

To confirm provisioning is working:

1. In Okta, navigate to **Reports → System Log**.
2. Filter by **Event Type: provision_user**.
3. You should see events with **Result: SUCCESS** for each user assigned in Step 5.

In Slack:
1. Navigate to **[your-workspace].slack.com/admin/members**.
2. The newly provisioned users should appear with **Provisioned** status.

---

**Troubleshooting**

| Symptom | Likely Cause | Resolution |
|---------|-------------|-----------|
| "API credentials could not be verified" | Token invalid or expired | Regenerate the token in Slack and update in Okta |
| Users provisioned in Okta but not appearing in Slack | Slack plan does not support SCIM | Confirm Business+ or Enterprise Grid plan with Slack account owner |
| User deactivated in Okta but still active in Slack | "Deactivate Users" not enabled | Enable in Provisioning → To App → Deactivate Users |
| Provisioning delays of more than five minutes | Okta provisioning queue backlog | Normal for large initial syncs; check System Log for progress |
| Error: "User already exists" | User pre-exists in Slack outside Okta | Import existing Slack users into Okta: Provisioning → To Okta → Import |

---

**Next steps**

- Configure attribute mappings — customise which Okta fields map to which Slack fields (see Okta documentation: help.okta.com)
- Set up group-based provisioning — provision Slack channels and user types based on Okta groups
- Monitor provisioning with Okta System Log — set up alerts for provisioning failures

## Quality checklist

- [ ] Title is in the format "How to [accomplish the specific goal]"
- [ ] Introduction states what the reader will accomplish, why it matters, and how long it takes
- [ ] All prerequisites are listed with version numbers and links where applicable
- [ ] Every step is numbered with a title, exact action, and expected output
- [ ] All commands are in code blocks — nothing the reader must type is in prose
- [ ] Verification section confirms the whole task succeeded — not just the last step
- [ ] Troubleshooting covers the most common failure modes with resolution
- [ ] British English used throughout
- [ ] No step assumes knowledge not covered in the prerequisites
- [ ] A reader with the stated prerequisites could complete this without asking for help

## Common mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Skipping "obvious" steps | Reader gets lost — what is obvious to the writer is not obvious to the reader | Explain every action, including navigation and UI interactions |
| Vague instructions ("configure the settings") | Reader does not know what to do | Use exact paths, names, and values: "Navigate to Applications → Provisioning → To App" |
| Missing expected outputs | Reader does not know if they succeeded | After each step, state exactly what the reader should see |
| No verification step | Reader completes the tutorial but does not know if it worked | Always include a final check that confirms end-to-end success |
| Commands in prose, not code blocks | Reader makes transcription errors | Every command or value the reader must type goes in a code block |
| Outdated version numbers or paths | Reader follows incorrect instructions | Pin all version references; add a "Last updated" date to the tutorial |

---

See [prompt-templates/learning-notes-prompts.md](../prompt-templates/learning-notes-prompts.md) for learning material templates.

See [examples/technical-runbook.md](../examples/technical-runbook.md) for a detailed procedural example.
