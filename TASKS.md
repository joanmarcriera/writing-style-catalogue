# Tasks

## P0 — Professional bundle release

- [x] Define and validate a machine-readable Markdown bundle contract.
  - Completion: the contract documents required metadata and sections, and validation fails clearly for missing or broken fields.
- [x] Upgrade all eleven existing examples and add the LinkedIn launch-post bundle.
  - Completion: twelve examples contain a labelled source packet, completed prompt, output excerpt, rubric scorecard, human review requirements, and working asset links.
- [x] Add missing decision-record, incident-report, and LinkedIn-post rubrics.
  - Completion: each bundle links to a relevant five-point rubric with a stated pass threshold.
- [x] Generate bundle data and replace the hard-coded workflow showcase.
  - Completion: the site renders twelve generated bundles with accessible Brief, Prompt, Output, and Review tabs.
- [x] Add launch metadata and refreshed screenshots.
  - Completion: canonical/Open Graph metadata is present and the social preview is 1200×630.
- [x] Add automated tests and CI gates.
  - Completion: parser, schema, links, generation, JavaScript, and stale-generated-file checks pass locally and in GitHub Actions.
- [x] Deploy and verify the public release.
  - Completion: `main` is pushed, GitHub Pages succeeds, and live desktop/mobile checks show the new bundle experience with no runtime errors.
- [x] Return the final LinkedIn copy.
  - Completion: paste-ready text reflects only live, verified catalogue claims; no external post is created or scheduled.
