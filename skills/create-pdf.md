---
title: Create PDF
skill_type: Document generation
output: A formatted, print-ready PDF document with consistent visual hierarchy, page structure, and professional layout
tools_needed: LLM (Claude/ChatGPT/Gemini), Markdown editor, PDF converter (Pandoc, Markdown-PDF, or Docraptor)
difficulty: Medium
---

# Skill: Create PDF

## What this skill does

Produces a well-structured, print-ready PDF document from source content by first generating correctly formatted Markdown, then converting it to PDF using a rendering tool. The LLM's role is to write the content and structure in clean Markdown with appropriate heading hierarchy, table of contents entries, and page-break hints. The conversion step (Pandoc, Docraptor, or similar) handles the final rendering. This skill is most effective when you know your target page count and layout requirements before you start prompting.

## When to use it

- Producing formal reports for board, executive, or regulatory audiences that must be distributed as a fixed-format file
- Archiving completed project documentation in a permanent, non-editable form
- Generating client-facing deliverables such as tax technical notes, business cases, or proposals
- Creating runbooks, SOPs, or playbooks that field teams will print or reference offline
- Packaging a multi-section analysis where visual consistency and page numbering matter

## Inputs required

- Full source content (text, data, tables, any charts described in words)
- Document type (report, brief, whitepaper, technical note, board paper, etc.)
- Target page count or length constraint
- Intended audience and distribution method (print, email, secure portal)
- Branding requirements: heading fonts, accent colours, logo placement if any
- Whether a table of contents is needed
- Any required disclaimers, version numbers, or classification markings

## Fast workflow: notes to PDF

1. **Draft in Markdown first** using [PDF Document Prompts](../prompt-templates/pdf-document-prompts.md). Do not start with visual layout.
2. **Review content** against the relevant style and rubric before converting. Fix facts, assumptions, and structure while the document is still editable text.
3. **Add PDF signals**: title page, table of contents, numbered headings, page-break markers, appendix labels, and table titles.
4. **Convert to PDF** using Pandoc, LibreOffice, a Markdown-to-PDF tool, or the organisation's approved document workflow.
5. **Inspect the rendered PDF**: page breaks, table wrapping, headings, footers, classification markings, and page numbers.
6. **Final proofread from the PDF**, not only from the Markdown. Layout changes often reveal errors that were not visible in source text.

## Copy-paste prompt

```
You are a professional document writer and formatter. Your task is to produce clean, well-structured Markdown that will be converted to a PDF.

DOCUMENT TYPE: [e.g. Executive briefing / Board paper / Technical runbook / Tax note]
AUDIENCE: [e.g. Board of directors / C-suite / Technical engineers / External client]
PURPOSE: [What this document must achieve — decision, information, instruction, approval]
CONTEXT: [Background the reader needs to understand the document]
INPUT: [Paste your raw content, notes, or data here]
DESIRED_OUTCOME: [What you want the reader to do or believe after reading]
TONE: [e.g. Formal and measured / Professional and direct / Technical and precise]
LENGTH: [e.g. 4 pages / 8–10 pages / Under 2,000 words]
FORMAT: Markdown with H1 for title, H2 for major sections, H3 for subsections. Use tables where comparative data appears. Use bulleted lists for items without sequence; numbered lists for steps or ranked items.
CONSTRAINTS: Use British English throughout. Avoid filler phrases ("it is important to note", "in conclusion"). Do not pad content to hit length — cut to what matters. Output only the document itself; no preamble, no meta-commentary.

STRUCTURE REQUIRED:
1. Title block (document title, date, version, author/organisation, classification if applicable)
2. Table of contents (list section headings with placeholder page numbers — e.g. "…3")
3. Executive summary (150–250 words; lead with the key finding or recommendation)
4. [Body sections per document type — see Suggested output structure below]
5. Appendices (if referenced in body)

Write in full, precise sentences. Every claim must be supported by a fact, figure, or source reference provided in the input. Do not invent data.
```

## Suggested output structure

- **Title block** — document title, subtitle, date, version number, author, classification (Confidential / Internal / Public)
- **Table of contents** — H2 and H3 headings listed with section numbers
- **Executive summary** — 1 page maximum; recommendation or key finding first
- **Section 1: Background / Context** — why this document exists
- **Section 2: Analysis or main content** — the substance; use sub-sections with H3 headings
- **Section 3: Options or findings** — if decision-support document
- **Section 4: Recommendation** — what to do and why
- **Section 5: Implementation or next steps** — timeline, owners, dependencies
- **Section 6: Risk considerations** — what could go wrong; mitigations
- **Appendices** — raw data, methodology, supporting tables, references

## Design and layout considerations

- **Page margins**: 2.5 cm all sides is standard for formal documents; wider margins look more authoritative
- **Font hierarchy**: Use a single sans-serif face (e.g. Calibri, Arial) for body; weight and size differentiate headings. Never use more than two typefaces.
- **Heading levels**: H1 = document title only; H2 = numbered section (e.g. "1. Background"); H3 = sub-section; avoid H4 in printed docs
- **Page breaks**: Force a new page before each H2 section in Pandoc with `\newpage` or via CSS `page-break-before: always`
- **Tables**: Keep under 6 columns; use bold headers; alternate row shading improves readability
- **White space**: Padding above H2 headings (at least 12pt) prevents visual clutter
- **Colour**: One accent colour maximum (e.g. dark navy `#1A2B5A`) for headings and table headers; body text in near-black `#1C1C1C`

### Prompt for generating the PDF artefact (not the content)

```
Convert the following Markdown document to a PDF using these layout rules. Preserve the content exactly; change layout only.

PAPER SIZE: A4
MARGINS: 2.5 cm all sides
BODY FONT: Calibri or Arial, 11pt, line spacing 1.4
HEADING 1: 22pt bold, [accent colour], centred, on its own page
HEADING 2: 16pt bold, [accent colour], preceded by page break
HEADING 3: 12pt bold, black
TABLE HEADERS: bold, [accent colour] background, white text
FOOTER: document title (left), page number (right), date (centre)
HEADER: organisation logo (right-aligned, 1 cm height) on all pages except title

Pandoc command:
pandoc input.md -o output.pdf --pdf-engine=wkhtmltopdf --css=style.css -V papersize=a4 -V margin-top=2.5cm -V margin-bottom=2.5cm -V margin-left=2.5cm -V margin-right=2.5cm

[Paste Markdown content here]
```

## Quality controls

- [ ] Table of contents entries match actual section headings exactly
- [ ] Executive summary is self-contained — a reader who reads only that page understands the key message
- [ ] No section exceeds its allocated page count without good reason
- [ ] All tables have clear headers and consistent units
- [ ] Page breaks fall at logical points (not mid-paragraph, not mid-table)
- [ ] Disclaimer, version number, and date appear on the title page
- [ ] Fonts and colours are consistent throughout the converted PDF
- [ ] Document renders correctly in both screen and print preview

## Common failure modes

- **Markdown converts poorly**: Tables with merged cells or complex nesting break in most PDF converters — keep tables simple; split complex ones into two
- **Page breaks in wrong places**: Pandoc does not auto-break before H2 sections without explicit CSS or `\newpage` commands — add these manually after generating Markdown
- **Content too long for stated length**: LLMs pad when they don't have enough input — provide more source material or reduce the number of sections, not the word target
- **Heading hierarchy inconsistent**: Skipping from H2 to H4 breaks PDF bookmark trees — use levels sequentially
- **Images and diagrams not rendering**: LLMs cannot embed images; describe visuals as "[INSERT CHART: revenue by quarter, bar chart]" placeholders for manual insertion after conversion

## Example request

"I need a 6-page executive briefing PDF on our proposed cloud migration from on-premise to Azure. The audience is the CIO and CFO. The key recommendation is to proceed with a phased migration over 18 months at a total cost of £2.1M, delivering annual savings of £800k from year 2. Include an executive summary, background on the current infrastructure costs, the three migration options we considered, the recommended approach, a risk register summary, and implementation timeline. Use formal, measured tone. British English throughout."
