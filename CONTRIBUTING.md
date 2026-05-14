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

1. Create a file in `examples/` for each style/document type
2. Provide realistic but concise examples
3. Keep examples under 500 words where possible
4. Ensure examples demonstrate the style accurately

## Before Committing

1. Run the index generation script: `python scripts/generate_index.py`
2. Validate internal links: `python scripts/validate_links.py`
3. Ensure all YAML front matter is valid
4. Check British English spelling and grammar
5. Remove fabricated citations; keep references generic
6. Verify all prompts are copy-paste ready

## Standards

- **Language**: British English throughout
- **Tone**: Practical, direct, minimal jargon
- **Length**: Concise but complete; first-pass quality is fine
- **Format**: Consistent Markdown formatting
- **Examples**: Real-world and realistic
- **Prompts**: Copy-paste ready, with clear variables
- **Attribution**: No fabricated citations; acknowledge sources generically

## What Not to Do

- Don't copy copyrighted material
- Don't fabricate external citations
- Don't over-optimise content in first pass
- Don't make every file perfect (good enough is good enough)
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
