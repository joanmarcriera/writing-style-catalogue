import sys
import tempfile
import unittest
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH / "scripts"))

from bundle_contract import BundleContractError, build_bundle  # noqa: E402


RUBRIC = """# Sample Rubric

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Bottom line | Missing | Present | First |
| Evidence | Vague | Some | Specific |
| Decision clarity | None | Weak | Explicit |
| Tone | Casual | Bland | Direct |

## Other table

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Not a criterion | a | b | c |
"""

PROMPT = (
    "Use only the SOURCE PACKET. Do not invent facts. If anything is missing, return "
    "MISSING INFORMATION. Write in British English. "
) + "Keep every figure traceable to the packet. " * 15


def bundle_text(criteria):
    rows = "\n".join(f"| {name} | 4 | Evidence sentence. | Pass |" for name in criteria)
    return f"""---
bundle_id: sample
artefact: Sample
audience: Testers
scenario: labelled-composite
style_path: ref.md
pattern_path: ref.md
prompt_path: ref.md
rubric_path: rubrics/sample-rubric.md
---

# Sample

## Professional context

Context.

## Source packet

Facts.

## Completed prompt

```text
{PROMPT}
```

## Output excerpt

Output.

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
{rows}

## Human review before use

- Check it.

## Reuse this bundle

- Links.
"""


class ScorecardRubricMatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        (self.base / "rubrics").mkdir()
        (self.base / "examples").mkdir()
        (self.base / "ref.md").write_text("ref\n", encoding="utf-8")
        (self.base / "rubrics" / "sample-rubric.md").write_text(RUBRIC, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def write_bundle(self, criteria):
        path = self.base / "examples" / "sample.md"
        path.write_text(bundle_text(criteria), encoding="utf-8")
        return path

    def test_matching_criteria_pass_case_insensitively(self):
        path = self.write_bundle(["Bottom line", "evidence", " Decision Clarity ", "Tone"])
        bundle = build_bundle(path, self.base)
        self.assertEqual(len(bundle["scorecard"]), 4)

    def test_mismatching_criterion_names_bundle_criterion_and_rubric(self):
        path = self.write_bundle(["Bottom line", "Evidence", "Instruction fit", "Not a criterion"])
        with self.assertRaises(BundleContractError) as caught:
            build_bundle(path, self.base)
        message = str(caught.exception)
        self.assertIn("examples/sample.md", message)
        self.assertIn("'Instruction fit'", message)
        self.assertIn("'Not a criterion'", message)
        self.assertIn("rubrics/sample-rubric.md", message)
        self.assertNotIn("'Bottom line'", message)


if __name__ == "__main__":
    unittest.main()
