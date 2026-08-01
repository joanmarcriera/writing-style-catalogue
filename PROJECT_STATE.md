# Project State

## Current objective

Upgrade the public catalogue so each worked example visibly demonstrates a professional bundle: source packet, completed prompt, output excerpt, and review gate. Publish the verified result to `p.riera.co.uk` through the existing GitHub Pages workflow.

## Completed work

- Defined a strict Markdown contract for professional prompt bundles and documented it in `reference/professional-prompt-bundle-standard.md`.
- Upgraded all eleven existing examples and added a twelfth LinkedIn launch-post bundle.
- Added missing decision-record, incident-report, and LinkedIn-post rubrics.
- Replaced the hard-coded showcase with generated bundle data and accessible Brief, Prompt, Output, and Review tabs.
- Added complete prompt copying, clickable component links, keyboard tab navigation, and honest review gates.
- Added canonical, Open Graph, and Twitter metadata plus refreshed desktop, mobile, and 1200x630 social-preview images.
- Added bundle unit tests and GitHub Pages validation gates.
- Completed a local desktop/mobile browser walkthrough of every bundle.

## Current implementation state

- The professional bundle release is deployed from commit `5ad2de7` and verified at `https://p.riera.co.uk/`.
- No social post has been created or scheduled.
- The paste-ready LinkedIn copy has been prepared for manual publication.

## Files changed

- Twelve files under `examples/` now implement the professional bundle contract.
- Three purpose-built rubrics were added under `rubrics/`.
- `scripts/bundle_contract.py`, `scripts/validate_bundles.py`, and `tests/test_bundle_contract.py` enforce the contract.
- `scripts/generate_site_data.py`, `assets/catalogue-data.js`, `assets/site.js`, `assets/site.css`, and `index.html` provide the generated public experience.
- README, quick-start, contribution, start-here, index, project-state, task, decision, CI, and screenshot assets were updated.

## Tests run

- `python3 scripts/validate_bundles.py`: passed, 12 bundles.
- `python3 -m unittest discover -s tests -v`: passed, 4 tests.
- `python3 scripts/validate_links.py`: passed, 152 Markdown files.
- `node --check assets/site.js`: passed.
- `python3 -m py_compile ...`: passed for changed Python modules and tests.
- `git diff --check`: passed.
- Re-running both generators produced byte-identical `INDEX.md` and `assets/catalogue-data.js` hashes.
- Local browser walkthrough: passed for all 12 bundles; each exposed 4 tabs, at least 5 component links, 5 score rows, and valid gate labels. Desktop and 390px layouts had no horizontal overflow or broken images.
- GitHub Pages workflow `30694125883`: passed every validation and deployment step for commit `5ad2de7`.
- Live hash comparison: `index.html`, `assets/catalogue-data.js`, `assets/site.js`, and `assets/social-card.png` matched the local release byte for byte.
- Live browser walkthrough: passed all 12 bundles at desktop size and at 390×844; no failed bundle checks, broken images, or horizontal overflow.

## Unresolved defects or risks

- The contract intentionally expects exactly 12 examples; adding another example requires updating `EXPECTED_BUNDLE_COUNT` as an explicit release decision.
- External readers must still perform the stated human review before using any output, especially the tax note and untested runbook.
- The local Ollama review wrapper failed before returning findings; authoritative validation and review were completed in the primary agent instead.
- The successful Pages run reported a non-blocking GitHub Actions warning that several upstream actions still target the deprecated Node.js 20 runtime and were forced onto Node.js 24.

## Known blockers

- None.

## Next recommended action

Monitor the upstream GitHub Pages actions and update their major versions when Node.js 24-native releases are available.
