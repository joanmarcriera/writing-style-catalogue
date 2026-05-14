---
title: Create PDF
category: Generation
---

# Skill: Create PDF

## What This Skill Does

Converts a document into a well-formatted, print-ready PDF with proper styling, page breaks, and visual hierarchy.

## When to Use It

- Converting reports to PDF for distribution
- Creating formal documents with consistent formatting
- Generating board papers or executive briefings in PDF
- Creating documents that need to be archived

## Inputs Required

- Document content (text, structure, any tables/lists)
- Document type (report, brief, whitepaper, etc.)
- Branding or formatting requirements
- Page layout preferences

## Copy-Paste Prompt

```
You are a document formatting specialist. Create a PDF-ready document from:

CONTENT:
[Your document content]

DOCUMENT TYPE:
[Report, brief, whitepaper, proposal, etc.]

FORMATTING REQUIREMENTS:
[Logo, colours, fonts, if any]

INSTRUCTIONS:
1. Use clear markdown formatting
2. Add proper spacing and breaks
3. Use consistent heading styles
4. Include page numbers where appropriate
5. Format tables clearly
6. Create table of contents if needed

Output markdown ready for PDF conversion. No preamble.
```

## Suggested Output Structure

- Title Page
- Table of Contents
- Executive Summary (1 page)
- Body Sections (with H1, H2 headings)
- Appendices (if needed)
- References (if needed)

## Quality Controls

- [ ] Consistent formatting throughout
- [ ] Proper page breaks between sections
- [ ] Table of contents is accurate
- [ ] All links and references are complete
- [ ] Renders well across PDF viewers
- [ ] Professional appearance
- [ ] All content is legible at print size

## Common Failure Modes

- Markdown doesn't convert cleanly to PDF (test before finalising)
- Page breaks in wrong places (specify manually if needed)
- Images or tables don't scale properly (check in final PDF)
- Inconsistent styling (maintain consistent heading hierarchy)

## Example Request

"Create a PDF-ready board paper about cloud migration. Include title page, executive summary, background, options analysis, and recommendation. Use consistent formatting and professional layout. Add table of contents."

---

Use tools like Pandoc, Markdown-PDF, or online converters to generate final PDF.
