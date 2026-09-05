# Writing Style Catalogue — CLAUDE.md

**What this project is**: A curated catalogue of professional writing styles, prompt templates, document-generation skills, patterns, examples, rubrics, and workflows. Published as a searchable static GitHub Pages site at [p.riera.co.uk](https://p.riera.co.uk) — asset-light, no external dependencies, Markdown + Python scripts.

**Purpose**: Help professionals draft high-quality documents (board papers, tax notes, incident reports, briefings, ADRs, runbooks, etc.) using LLMs, with copy-paste prompts, worked examples, and human-review gates. Designed for IT leaders, finance professionals, consultants, marketers, job seekers, and learners.

---

## Layout & Conventions

**Content structure** (all in Markdown with YAML frontmatter):
- `styles/` — 25 writing frameworks (BLUF, Consulting, Board Paper, Executive Briefing, etc.)
- `patterns/` — reusable argument/section structures
- `prompt-templates/` — copy-paste prompts for 20+ document types
- `skills/` — 26 document-generation processes (create-board-pack, create-pdf, etc.)
- `personal-workflows/` — 9 end-to-end workflows combining styles + skills
- `examples/` — 12 worked bundles (source → prompt → output → review scorecard)
- `checklists/` — quick QA review gates
- `rubrics/` — scoring guides for professional review
- `reference/` — tone guides, prompting principles, bundle standard, SEO audit evidence rules

**Frontmatter & naming**:
- All styles/skills/templates use YAML frontmatter (title, category, aliases, etc.)
- Filenames are kebab-case matching content title
- `meta-prompts/` for improving drafts and prompts themselves
- `use-cases/` folder is empty (known gap)

**Standards**:
- British English throughout (non-negotiable)
- Copy-paste readiness is critical — every prompt must work as-is
- No fabricated citations; verify high-stakes sources
- Every bundle's scorecard must pass its review gate before marking "shipped"
- No external dependencies in scripts

---

## How to Run & Test

**Local preview** (no build step needed):
```bash
python3 scripts/generate_site_data.py       # Build catalogue index
python3 -m http.server 8765                  # Serve locally
# Then visit http://127.0.0.1:8765/
```

**Validation & tests** (run before committing):
```bash
python3 scripts/validate_bundles.py          # Check professional bundle contract (12 bundles expected)
python3 -m unittest discover -s tests -v     # Run unit tests
python3 scripts/generate_site_data.py        # Regenerate catalogue data
python3 scripts/generate_index.py            # Regenerate INDEX.md
python3 scripts/validate_links.py            # Check all internal Markdown links
```

**GitHub Pages deployment**:
- Workflow lives in `.github/workflows/pages.yml`
- Runs all 4 validation steps above, regenerates assets, deploys to `p.riera.co.uk`
- Enable in repo settings: **GitHub Pages > Build and deployment > GitHub Actions**

---

## Key Files & Flows

| File | Purpose |
|------|---------|
| `reference/professional-prompt-bundle-standard.md` | Contract for worked examples (context, source, 600+ char prompt, output, scorecard, human-review note) |
| `scripts/bundle_contract.py` | Loads and validates all example bundles |
| `scripts/validate_bundles.py` | Ensures EXPECTED_BUNDLE_COUNT = 12 and all bundles pass contract |
| `tests/test_bundle_contract.py` | Unit tests for bundle structure & review gate consistency |
| `scripts/generate_site_data.py` | Outputs `assets/catalogue-data.js` (searchable catalogue UI data) |
| `scripts/generate_index.py` | Outputs `INDEX.md` (text-searchable file index) |
| `index.html` + `assets/site.{js,css}` | Static GitHub Pages UI — tabs, search, copy-paste, links |
| `.nojekyll` | Tells GitHub Pages: use as-is, no Jekyll processing |
| `CNAME` | DNS routing to `p.riera.co.uk` |

---

## Common Tasks

**Add a new style**:
1. Copy `styles/bluf-bottom-line-up-front.md` as template
2. Complete YAML frontmatter (title, category, best_for, not_good_for, typical_length, aliases)
3. Fill 10 sections: What this style is, When to use it, When NOT to use it, Core structure, Copy-paste prompt, Example, Quality checklist, Common mistakes
4. Keep ~500–1000 words
5. Run validation: `python3 scripts/validate_links.py` (after regenerating)

**Add a worked example**:
1. Read `reference/professional-prompt-bundle-standard.md` — mandatory contract
2. Create file in `examples/` with all required sections (context, source packet, prompt, output, scorecard, human-review note)
3. Run `python3 scripts/validate_bundles.py` — must pass all checks
4. **Important**: Update `scripts/bundle_contract.py` `EXPECTED_BUNDLE_COUNT` if adding/removing examples (explicit release decision)

**Publish to p.riera.co.uk**:
1. Commit to main branch
2. GitHub Actions workflow fires automatically
3. Validates all bundles, regenerates site data, deploys to GitHub Pages
4. Live within ~60 seconds

---

## Gotchas & Important Constraints

1. **Bundle count is fixed**: `EXPECTED_BUNDLE_COUNT = 12` in `scripts/bundle_contract.py`. Adding a 13th example requires explicitly changing this constant — no silent additions.

2. **No external dependencies**: Python 3.x only; all scripts use stdlib. Don't add `pip install` requirements.

3. **Review gates are hard boundaries**: If a bundle's scorecard has score < 3 or critical "Human check" unchecked, gate must be "Revise" or "Human check" — never "Pass". Tests enforce this.

4. **Prompt readiness is non-negotiable**: Every prompt template must be tested with an LLM and work exactly as pasted. Flag missing inputs explicitly rather than inventing data.

5. **British English throughout**: Spelling, grammar, date formats (dd Mmm yyyy). Non-negotiable for published content.

6. **Links are validated before deploy**: `python3 scripts/validate_links.py` must pass. Broken internal links will block the GitHub Actions workflow.

7. **Index and site data are generated**: Don't hand-edit `INDEX.md` or `assets/catalogue-data.js` — they're outputs. Always regenerate both scripts after editing content.

8. **No fabricated citations**: Every claim must be verifiable or flagged as an assumption. High-stakes claims (legal, tax, financial) must be reviewed by a human expert before shipping.

---

## Project State (as of 2026-08-01)

- **Status**: Shipped & verified. Professional bundle release (commit `5ad2de7`) live at `p.riera.co.uk`.
- **Last maintenance**: 1 Aug 2026 (`14f3a67`, no active development since; dormant until new content needed).
- **Tests**: All passing (4 unit tests, 12 bundle validations, 152 link checks, GitHub Pages pipeline).
- **Known gaps**: use-cases/ folder empty; no before/after style comparison matrices yet.
- **Blockers**: None.

---

## Useful Links

- Live site: https://p.riera.co.uk/
- Quick start: [QUICKSTART.md](QUICKSTART.md)
- Start here guide: [START-HERE.md](START-HERE.md)
- Cheat sheet: [CHEATSHEET.md](CHEATSHEET.md)
- Contributing guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Repository map: [REPO-MAP.md](REPO-MAP.md)
- Project state: [PROJECT_STATE.md](PROJECT_STATE.md)
