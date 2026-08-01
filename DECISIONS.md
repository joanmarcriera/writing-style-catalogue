# Decisions

## 2026-08-01 — Treat worked examples as the public bundle source of truth

**Decision:** Store bundle metadata and the four visible stages in the Markdown example files, then generate the website data from those files.

**Alternatives considered:** Keep the bundle catalogue hard-coded in JavaScript; introduce a separate JSON manifest; create a new bundle-file directory.

**Rationale:** The repository promises Markdown source for everything. Reusing the example files prevents a second editorial source from drifting and preserves a useful GitHub-only experience.

**Consequences:** Examples must follow a strict section and frontmatter contract. The generator and validation tooling become responsible for converting that contract into static site data.

**Revisit when:** The Markdown contract cannot represent a required interaction without fragile parsing.

## 2026-08-01 — Use labelled composites for professional examples

**Decision:** Existing professional scenarios will be clearly labelled composites. The LinkedIn launch bundle may use facts verified directly from this public repository.

**Alternatives considered:** Present examples without provenance labels; use real client cases; make examples generic and number-free.

**Rationale:** Composite source packets can be realistic and internally auditable without exposing confidential data or implying client evidence.

**Consequences:** No example may imply that a fictional company, event, metric, quotation, or decision is real. High-stakes external claims require primary-source verification and an as-of date.

**Revisit when:** A real case is supplied with explicit permission and independently verifiable source material.

## 2026-08-01 — Keep the site dependency-free

**Decision:** Extend the existing Python and browser JavaScript rather than add a framework or third-party Markdown parser.

**Alternatives considered:** Introduce a static-site generator; use a client-side Markdown library; migrate to a JavaScript build pipeline.

**Rationale:** The current GitHub Pages site is fast, portable, and operationally simple. The bundle format can be parsed safely with constrained standard-library code.

**Consequences:** Bundle sections use deliberately simple Markdown conventions and render as trusted preformatted content rather than arbitrary HTML.

**Revisit when:** Rich document rendering becomes more important than the zero-dependency deployment model.
