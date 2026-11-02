import sys
import tempfile
import unittest
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH / "scripts"))

from bundle_contract import (  # noqa: E402
    BundleContractError,
    build_bundle,
    parse_critical_criteria,
)


RUBRIC_WITH_MARKER = """---
title: Synthetic Rubric
category: Rubric
critical: [Decision required, Risk]
---

# Synthetic Rubric
"""

RUBRIC_WITHOUT_MARKER = """---
title: Synthetic Rubric
category: Rubric
---

# Synthetic Rubric
"""

PROMPT = (
    "You are a professional drafter. Use British English. Do not invent facts. "
    "If anything critical is absent, return a MISSING INFORMATION list instead. "
) + ("Use only the source packet supplied below and keep every figure traceable. " * 10)


def bundle_text(risk_score: int, risk_gate: str) -> str:
    return f"""---
bundle_id: synthetic-bundle
artefact: Synthetic paper
audience: Test reader
scenario: labelled-composite
style_path: refs/style.md
pattern_path: refs/pattern.md
prompt_path: refs/prompt.md
rubric_path: rubrics/synthetic-rubric.md
---

## Professional context

Context.

## Source packet

Source.

## Completed prompt

```text
{PROMPT}
```

## Output excerpt

Output.

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Decision required | 5 | Clear ask. | Pass |
| Risk | {risk_score} | Some risks. | {risk_gate} |
| Structure | 3 | Adequate. | Pass |
| Tone | 4 | Formal. | Pass |

## Human review before use

Reviewer checks.

## Reuse this bundle

Links.
"""


class CriticalCriterionGateTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        (self.base / "refs").mkdir()
        (self.base / "rubrics").mkdir()
        (self.base / "examples").mkdir()
        for name in ("style", "pattern", "prompt"):
            (self.base / "refs" / f"{name}.md").write_text("# Ref\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rubric: str, bundle: str) -> Path:
        (self.base / "rubrics" / "synthetic-rubric.md").write_text(rubric, encoding="utf-8")
        path = self.base / "examples" / "synthetic-bundle.md"
        path.write_text(bundle, encoding="utf-8")
        return path

    def test_parse_marker_forms(self):
        self.assertEqual(
            parse_critical_criteria(RUBRIC_WITH_MARKER), ["Decision required", "Risk"]
        )
        self.assertIsNone(parse_critical_criteria(RUBRIC_WITHOUT_MARKER))
        self.assertIsNone(parse_critical_criteria("# No front matter\n"))

    def test_passing_bundle(self):
        # Critical criterion at 4 with Pass; non-critical criterion at 3 with Pass.
        path = self.write(RUBRIC_WITH_MARKER, bundle_text(4, "Pass"))
        notices: list[str] = []
        bundle = build_bundle(path, self.base, notices)
        self.assertEqual(bundle["id"], "synthetic-bundle")
        self.assertEqual(notices, [])

    def test_critical_below_four_with_revise_gate_is_allowed(self):
        path = self.write(RUBRIC_WITH_MARKER, bundle_text(3, "Revise"))
        build_bundle(path, self.base)

    def test_failing_bundle_names_bundle_criterion_and_score(self):
        path = self.write(RUBRIC_WITH_MARKER, bundle_text(3, "Pass"))
        with self.assertRaises(BundleContractError) as caught:
            build_bundle(path, self.base)
        message = str(caught.exception)
        self.assertIn("synthetic-bundle", message)
        self.assertIn("critical criterion 'Risk'", message)
        self.assertIn("scored 3", message)
        self.assertIn("Gate = Pass", message)

    def test_rubric_without_marker_is_noop_with_notice(self):
        # Same scorecard that fails above, but the rubric has no marker.
        path = self.write(RUBRIC_WITHOUT_MARKER, bundle_text(3, "Pass"))
        notices: list[str] = []
        build_bundle(path, self.base, notices)
        self.assertEqual(len(notices), 1)
        self.assertIn("synthetic-bundle", notices[0])
        self.assertIn("rubrics/synthetic-rubric.md", notices[0])
        self.assertIn("skipped", notices[0])


if __name__ == "__main__":
    unittest.main()
