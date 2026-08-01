# Quick Start Guide

For the fastest task-to-artefact route, start with [START-HERE.md](START-HERE.md). Use this page if you are new to the catalogue and want the basic workflow.

## 5 minutes to your first document

### Step 1: Choose Your Style (1 minute)

What kind of document do you need?

- **Brief, punchy updates?** → Smart Brevity
- **Executive summary?** → BLUF (Bottom Line Up Front)
- **Recommendation memo?** → Minto Pyramid Principle
- **Board presentation?** → Board Paper Style
- **Technical explanation?** → Technical Documentation
- **Website or SEO audit?** → Executive Briefing + Consulting Style

See [CHEATSHEET.md](CHEATSHEET.md) for a full comparison.

### Step 2: Find Your Prompt (1 minute)

Navigate to `prompt-templates/` and find your document type:

- Email? → `email-prompts.md`
- Executive update? → `executive-summary-prompts.md`
- Board paper? → `board-paper-prompts.md`
- Technical doc? → `technical-documentation-prompts.md`
- Website audit? → `website-marketing-seo-prompts.md`

### Step 3: Copy the Template (1 minute)

Copy the entire prompt from the file. It includes:

Good templates include role, audience, purpose, context, input, output format, tone, constraints, assumptions, and review criteria.

### Step 4: Customise and Submit (2 minutes)

Replace the placeholder variables with your content:

- `[TOPIC]` → Your actual topic
- `[AUDIENCE]` → Your actual readers
- `[KEY_POINTS]` → Your actual key points

Paste into Claude or your LLM of choice and submit.

### Step 5: Apply the Review Gate

Before publishing, score the draft with the linked rubric and complete the relevant checklist. A professional draft is not ready while a critical criterion scores below 4, any criterion scores below 3, or a required human check remains unresolved.

- Executive Readiness Checklist
- Clarity Checklist
- AI Output Review Checklist

To see the complete sequence first, open any worked bundle in `examples/`: professional context, source packet, completed prompt, output excerpt, scorecard, and human-review requirements.

---

## Common Workflows

### Creating an Executive Update

1. Copy template from `prompt-templates/executive-summary-prompts.md`
2. Use `styles/axios-smart-brevity.md` for structure
3. Follow checklist in `checklists/executive-readiness-checklist.md`
4. See example in `examples/smart-brevity-update.md`

### Creating a Board Paper

1. Copy template from `prompt-templates/board-paper-prompts.md`
2. Use `styles/board-paper-style.md` for detail
3. Use skill from `skills/create-board-pack.md` for multi-part generation
4. Review with `checklists/board-paper-checklist.md`
5. See example in `examples/board-paper.md`

### Creating Technical Documentation

1. Copy template from `prompt-templates/technical-documentation-prompts.md`
2. Use `styles/technical-documentation.md` for structure
3. Review with `checklists/technical-document-checklist.md`

### Auditing a Website from a URL

1. Copy template from `prompt-templates/website-marketing-seo-prompts.md`
2. Follow `personal-workflows/website-marketing-seo-audit-workflow.md`
3. Use `skills/create-website-marketing-seo-audit.md` for the main report
4. Review with `rubrics/website-marketing-seo-rubric.md`

---

## Getting Help

- **Confused about which style to use?** → [STYLE-SELECTION-GUIDE.md](STYLE-SELECTION-GUIDE.md)
- **Need to know where everything lives?** → [REPO-MAP.md](REPO-MAP.md)
- **Need to improve a prompt or draft?** → [meta-prompts/](meta-prompts/)
- **Need to score output quality?** → [rubrics/](rubrics/)
- **Want to see a real example?** → [examples/](examples/)
- **Need to validate output?** → [checklists/](checklists/)
- **Looking for a reference?** → [reference/](reference/)

That's it. Now go write something.
