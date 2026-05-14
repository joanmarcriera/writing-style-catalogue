---
title: Tutorial Style
category: Educational
aliases: [How-To Guide, Step-by-Step]
---

# Tutorial Style

## What This Style Is

Clear, step-by-step instruction for doing something. Assumes reader may be a beginner. Emphasises clarity, encouraging tone, and practical examples.

**Core principle**: Every step is crystal clear. Novice can follow without outside help.

## When to Use It

- Setup and installation guides
- How-to articles
- Process documentation
- Onboarding procedures
- Learning-by-doing content
- Troubleshooting guides

## When NOT to Use It

- Executive communication (use Smart Brevity)
- Precise technical reference (use Technical Documentation)
- Theory or explanation (use Socratic)
- Formal governance (use Board Paper)

## Core Structure

```
[INTRODUCTION]
What you'll learn and why it matters.

[PREREQUISITES]
What you need before starting.

[OVERVIEW]
What you'll do at a high level.

[STEPS]
1. Clear first step
2. Clear second step
3. [Continue...]

[VERIFICATION]
How to know if you did it right.

[TROUBLESHOOTING]
What could go wrong and fixes.

[NEXT STEPS]
What to learn next.
```

## Copy-Paste Prompt Template

```
You are a tutorial writer. Write a step-by-step guide from:

GOAL:
[What will the reader accomplish]

AUDIENCE:
[Skill level: beginner, intermediate, advanced]

PREREQUISITES:
[What do they need before starting]

PROCESS:
[What are the main steps]

COMMON PROBLEMS:
[What breaks and how to fix it]

INSTRUCTIONS:
1. Write clear, numbered steps
2. Each step should take 1–2 minutes
3. Use specific commands or actions (no vague instructions)
4. Include screenshots or examples if possible
5. Write for a beginner; assume nothing
6. End with verification and troubleshooting

Output only the tutorial. No preamble.
```

## Short Example

**Setting Up a GitHub Repository – A Tutorial**

**What You'll Learn**
How to create a new GitHub repository and clone it to your computer. Takes 10 minutes.

**Prerequisites**
- GitHub account (free; sign up at github.com)
- Git installed on your computer

**Overview**
You'll create a new repo on GitHub, add a README file, then clone it to your computer.

**Step 1: Create a Repository on GitHub**
1. Log in to github.com
2. Click the "+" icon (top right)
3. Select "New repository"
4. Enter a repository name (e.g., "my-first-repo")
5. Leave all other settings as default
6. Click "Create repository"

**Step 2: Clone to Your Computer**
1. On the repository page, click the green "Code" button
2. Copy the HTTPS link (it should look like `https://github.com/yourname/my-first-repo.git`)
3. Open your terminal
4. Type: `git clone [paste the link here]`
5. Press Enter. Wait for the clone to finish.

**Step 3: Verify It Worked**
1. Type: `cd my-first-repo` (this enters the folder)
2. Type: `ls -la` (this lists files)
3. You should see a README.md file and a .git folder

If you see those, you're done!

**Troubleshooting**

*Command not found: git*
Git isn't installed. Download and install from git-scm.com

*Permission denied (publickey)*
GitHub authentication issue. Follow GitHub's SSH setup guide (verify online before relying on availability).

**Next Steps**
Learn how to add files, commit changes, and push to GitHub.

## Quality Checklist

- [ ] Introduction explains what reader will learn
- [ ] Prerequisites are explicit and complete
- [ ] Each step is clear and unambiguous
- [ ] Steps are numbered and in order
- [ ] Verification shows reader they succeeded
- [ ] Troubleshooting covers common failures
- [ ] Tone is encouraging
- [ ] Beginner could follow without outside help

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Skips obvious steps | Reader gets lost | Explain every action, even "obvious" ones |
| Vague instructions | Ambiguous what to do | Use specific commands or exact actions |
| No verification step | Reader unsure if they succeeded | Tell them exactly what success looks like |
| Missing troubleshooting | Reader stuck with no help | Include common problems and solutions |
| Assumes too much knowledge | Lost reader midway | Write for a beginner; explain everything |

---

See [prompt-templates/learning-notes-prompts.md](../prompt-templates/learning-notes-prompts.md) for learning material templates.

See [examples/technical-runbook.md](../examples/technical-runbook.md) for a detailed procedural example.
