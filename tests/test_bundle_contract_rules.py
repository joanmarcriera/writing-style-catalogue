"""Negative tests for rules that scripts/bundle_contract.py enforces.

The suite in test_bundle_contract.py only exercises the shipped bundles,
which all pass. These tests build synthetic bundles in a temporary
directory so each rule is proven to reject drift.
"""

import sys
import tempfile
import unittest
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH / "scripts"))

import bundle_contract  # noqa: E402
from bundle_contract import (  # noqa: E402
    BundleContractError,
    build_bundle,
    load_bundles,
    parse_scorecard,
    strip_single_fence,
)


PROMPT = (
    "You are a professional adviser. Use only the SOURCE PACKET. Do not invent facts. "
    "If anything critical is absent, return MISSING INFORMATION and list each gap. "
    "Write in British English. "
) + "Keep the structure tight and traceable to the source. " * 12

SCORECARD = """| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Instruction fit | 5 | Follows the brief. | Pass |
| Factual integrity | 4 | Figures map to source. | Pass |
| Structure | 4 | Clear headings. | Pass |
| Usefulness | 3 | Needs light edits. | Human check |"""


def bundle_text(frontmatter=None, sections=None, drop_sections=()):
    fields = {
        "title": "Synthetic bundle",
        "bundle_id": "synthetic",
        "artefact": "Synthetic artefact",
        "audience": "Test reader",
        "scenario": "labelled-composite",
        "style_path": "styles/s.md",
        "pattern_path": "patterns/p.md",
        "prompt_path": "prompt-templates/t.md",
        "rubric_path": "rubrics/r.md",
    }
    fields.update(frontmatter or {})
    body = {
        "Professional context": "Context.",
        "Source packet": "```text\nSCENARIO: Labelled composite.\n```",
        "Completed prompt": f"```text\n{PROMPT}\n```",
        "Output excerpt": "```text\nOutput.\n```",
        "Review scorecard": SCORECARD,
        "Human review before use": "- A human checks it.",
        "Reuse this bundle": "- Links.",
    }
    body.update(sections or {})
    lines = ["---"] + [f"{k}: {v}" for k, v in fields.items() if v is not None] + ["---", "", "# Synthetic", ""]
    for heading, content in body.items():
        if heading in drop_sections:
            continue
        lines += [f"## {heading}", "", content, ""]
    return "\n".join(lines)


class ContractRuleTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        for rel in ("styles/s.md", "patterns/p.md", "prompt-templates/t.md", "rubrics/r.md", "skills/k.md"):
            target = self.base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# stub\n", encoding="utf-8")
        (self.base / "examples").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, text, name="bundle.md"):
        path = self.base / "examples" / name
        path.write_text(text, encoding="utf-8")
        return path

    def assertRejected(self, text, message):
        with self.assertRaises(BundleContractError) as ctx:
            build_bundle(self.write(text), self.base)
        self.assertIn(message, str(ctx.exception))

    def test_valid_synthetic_bundle_builds(self):
        bundle = build_bundle(self.write(bundle_text({"skill_path": "skills/k.md"})), self.base)
        self.assertEqual(bundle["id"], "synthetic")
        self.assertIn("skill", [link["kind"] for link in bundle["links"]])
        self.assertEqual(len(bundle["scorecard"]), 4)

    def test_missing_frontmatter_block_is_rejected(self):
        self.assertRejected("# No frontmatter\n", "missing YAML frontmatter")

    def test_each_required_frontmatter_field_is_enforced(self):
        for key in bundle_contract.REQUIRED_FRONTMATTER:
            with self.subTest(field=key):
                self.assertRejected(bundle_text({key: None}), f"missing frontmatter field {key}")

    def test_scenario_must_be_allowed(self):
        self.assertRejected(bundle_text({"scenario": "invented"}), "scenario must be")

    def test_each_required_section_is_enforced(self):
        for heading in bundle_contract.REQUIRED_SECTIONS:
            with self.subTest(section=heading):
                self.assertRejected(bundle_text(drop_sections=(heading,)), f"section {heading!r}")

    def test_unresolved_paths_are_rejected_including_optional_skill(self):
        self.assertRejected(bundle_text({"rubric_path": "rubrics/gone.md"}), "rubric_path does not resolve")
        self.assertRejected(bundle_text({"skill_path": "skills/gone.md"}), "skill_path does not resolve")

    def test_short_prompt_is_rejected(self):
        short = "```text\nMISSING INFORMATION. Do not invent. British English.\n```"
        self.assertRejected(bundle_text(sections={"Completed prompt": short}), "at least 600 characters")

    def test_required_prompt_phrases_are_enforced(self):
        for phrase in ("MISSING INFORMATION", "Do not invent", "British English"):
            with self.subTest(phrase=phrase):
                prompt = "```text\n" + PROMPT.replace(phrase, "") + "\n```"
                self.assertRejected(bundle_text(sections={"Completed prompt": prompt}), repr(phrase))

    def test_scorecard_needs_four_criteria(self):
        three = "\n".join(SCORECARD.splitlines()[:5])
        self.assertRejected(bundle_text(sections={"Review scorecard": three}), "at least four criteria")

    def test_score_outside_range_is_rejected(self):
        card = SCORECARD.replace("| Structure | 4 |", "| Structure | 6 |")
        self.assertRejected(bundle_text(sections={"Review scorecard": card}), "score outside 1-5 range for Structure")

    def test_non_numeric_score_is_rejected(self):
        card = SCORECARD.replace("| Structure | 4 |", "| Structure | four |")
        self.assertRejected(bundle_text(sections={"Review scorecard": card}), "invalid score")

    def test_unknown_gate_is_rejected(self):
        card = SCORECARD.replace("Clear headings. | Pass", "Clear headings. | Maybe")
        self.assertRejected(bundle_text(sections={"Review scorecard": card}), "invalid gate for Structure")

    def test_score_below_three_cannot_pass(self):
        card = SCORECARD.replace("| Structure | 4 |", "| Structure | 2 |")
        self.assertRejected(bundle_text(sections={"Review scorecard": card}), "score below 3 cannot pass: Structure")

    def test_low_score_with_revise_gate_is_allowed(self):
        card = SCORECARD.replace("| Structure | 4 | Clear headings. | Pass", "| Structure | 2 | Weak. | Revise")
        bundle = build_bundle(self.write(bundle_text(sections={"Review scorecard": card})), self.base)
        self.assertIn({"criterion": "Structure", "score": 2, "evidence": "Weak.", "gate": "Revise"}, bundle["scorecard"])

    def test_duplicate_bundle_ids_are_rejected(self):
        self.write(bundle_text(), "a.md")
        self.write(bundle_text(), "b.md")
        with self.assertRaises(BundleContractError) as ctx:
            load_bundles(self.base)
        self.assertIn("duplicate bundle ids: synthetic", str(ctx.exception))

    def test_bundle_count_must_match_expected(self):
        self.write(bundle_text(), "a.md")
        with self.assertRaises(BundleContractError) as ctx:
            load_bundles(self.base)
        self.assertIn(f"expected {bundle_contract.EXPECTED_BUNDLE_COUNT} bundles, found 1", str(ctx.exception))


class ParserHelperTests(unittest.TestCase):
    def test_strip_single_fence(self):
        self.assertEqual(strip_single_fence("```text\nhello\n```"), "hello")
        self.assertEqual(strip_single_fence("```markdown\nhello\n```"), "hello")
        self.assertEqual(strip_single_fence("plain"), "plain")

    def test_parse_scorecard_skips_header_and_separator(self):
        rows = parse_scorecard(SCORECARD)
        self.assertEqual([row["criterion"] for row in rows][0], "Instruction fit")
        self.assertEqual(len(rows), 4)


if __name__ == "__main__":
    unittest.main()
