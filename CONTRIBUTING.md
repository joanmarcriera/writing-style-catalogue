# Contributing

This catalogue is designed to be expanded and improved over time.

## How to Add Content

### Adding a New Style

1. Create a file in `styles/` named after the style (e.g., `new-style-name.md`)
2. Use the template structure from existing style files:
   - YAML front matter (title, category, aliases)
   - What the style is
   - When to use it
   - When NOT to use it
   - Core structure
   - Copy-paste prompt template
   - Short example
   - Quality checklist
   - Common mistakes

3. Keep content concise (aim for 500–1000 words per style)
4. Use real-world examples where possible
5. Make the prompt template copy-paste ready

### Adding a New Prompt Template

1. Create a file in `prompt-templates/` named after the document type
2. Include:
   - YAML front matter
   - Purpose section
   - Copy-paste prompt (marked clearly)
   - Variables to customise
   - Example input/output
   - Review checklist

3. Test the prompt with an LLM before including it
4. Keep templates modular and reusable

### Adding a New Skill

1. Create a file in `skills/` named `create-[document-type].md`
2. Include:
   - What this skill does
   - When to use it
   - Inputs required
   - Copy-paste prompt
   - Suggested output structure
   - Quality controls
   - Failure modes
   - Example request

### Adding a New Workflow

1. Create a file in `personal-workflows/`
2. Explain:
   - Which styles to use
   - Which skills to combine
   - Which templates to start from
   - Inputs required
   - Review checklist before publication

### Adding Examples

1. Read [Professional Prompt Bundle Standard](reference/professional-prompt-bundle-standard.md)
2. Create a file in `examples/` with the required bundle metadata and exact section headings
3. Label the source as a composite or verified public project
4. Supply a complete prompt of at least 600 characters, including missing-information behaviour
5. Include a rubric scorecard and explicit human-review requirements
6. Ensure every claim in the output maps to the source packet

## Before Committing

1. Validate bundles: `python3 scripts/validate_bundles.py`
2. Run tests: `python3 -m unittest discover -s tests -v`
3. Regenerate data and index: `python3 scripts/generate_site_data.py` and `python3 scripts/generate_index.py`
4. Validate internal links: `python3 scripts/validate_links.py`
5. Check British English spelling and grammar
6. Remove fabricated citations and verify every high-stakes source
7. Verify all prompts are copy-paste ready

## Standards

- **Language**: British English throughout
- **Tone**: Practical, direct, minimal jargon
- **Length**: Concise but complete; professional bundles must pass their review gate
- **Format**: Consistent Markdown formatting
- **Examples**: Real-world and realistic
- **Prompts**: Copy-paste ready, with clear variables
- **Attribution**: No fabricated citations; acknowledge sources generically

## What Not to Do

- Don't copy copyrighted material
- Don't fabricate external citations
- Don't confuse fluent first-pass output with approved professional work
- Don't mark a bundle as passed while a critical criterion or human check is unresolved
- Don't add dependencies to scripts
- Don't add incomplete implementations

## Known Gaps for Next Iteration

- use-cases/ folder is empty; add specific business scenarios
- More real-world examples with variations
- Expanded reference section with more patterns
- Integration examples for multi-document workflows
- Style comparison matrices
- Before/after examples showing impact of style choice

---

**Questions?** See [README.md](README.md) or review existing files for structure examples.
