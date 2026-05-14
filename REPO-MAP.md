---
title: Repository Map
category: Navigation
description: A practical map of the catalogue directories, what each one contains, and when to use it.
---

# Repository Map

This repository is organised around how professional writing actually gets produced: choose a style, choose a structure, copy a prompt, generate an artefact, then review it.

## Directory map

| Area | Purpose | Use when |
|---|---|---|
| [styles/](styles/) | Writing frameworks: tone, structure, when to use, examples, and style-specific prompts | You need to decide how the document should sound and be structured |
| [patterns/](patterns/) | Small reusable structures such as BLUF, SCQA, options analysis, and decision records | You need a section-level pattern inside a larger document |
| [prompt-templates/](prompt-templates/) | Copy-paste prompts by document type | You want to generate a first draft from notes |
| [meta-prompts/](meta-prompts/) | Prompts that improve prompts or critique outputs | The draft or prompt is not good enough yet |
| [skills/](skills/) | Production processes for specific artefacts | You need the steps to make a PDF, slide deck, board pack, runbook, ADR, or tax note |
| [personal-workflows/](personal-workflows/) | End-to-end workflows for recurring professional tasks | You need the full process, not just a single prompt |
| [examples/](examples/) | Realistic sample outputs | You want to see the expected shape before drafting |
| [checklists/](checklists/) | Fast final checks | You need a quick pre-send quality review |
| [rubrics/](rubrics/) | More rigorous scoring guides | You need to assess whether an output is strong enough for professional use |
| [reference/](reference/) | Tone, structure, prompting, document types, glossary, and resources | You need background guidance or a reusable explanation |
| [scripts/](scripts/) | Maintenance utilities | You need to regenerate [INDEX.md](INDEX.md) or validate links |

## Root navigation files

| File | Role |
|---|---|
| [START-HERE.md](START-HERE.md) | Fastest route from task to style, prompt, skill, and rubric |
| [CHEATSHEET.md](CHEATSHEET.md) | Main lookup table for common situations |
| [STYLE-SELECTION-GUIDE.md](STYLE-SELECTION-GUIDE.md) | Systematic style decision guide |
| [INDEX.md](INDEX.md) | Auto-generated complete file index |
| [QUICKSTART.md](QUICKSTART.md) | Five-minute beginner path |
| [README.md](README.md) | Project overview and contribution model |

## Maintenance workflow

After adding or renaming files:

```bash
python3 scripts/generate_index.py
python3 scripts/validate_links.py
```

Keep public repository hygiene in mind:

- Do not commit local agent context, private notes, credentials, client files, or unpublished legal/tax advice.
- Use realistic but anonymised examples.
- Do not invent citations, statutory references, sources, or external URLs.
- Keep prompts operational: role, audience, purpose, context, input, output format, tone, constraints, assumptions, and review criteria.
