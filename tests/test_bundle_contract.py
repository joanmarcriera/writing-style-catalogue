import sys
import unittest
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH / "scripts"))

from bundle_contract import EXPECTED_BUNDLE_COUNT, load_bundles  # noqa: E402


class BundleContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundles = load_bundles(BASE_PATH)

    def test_expected_bundle_count_and_unique_ids(self):
        self.assertEqual(len(self.bundles), EXPECTED_BUNDLE_COUNT)
        self.assertEqual(len({bundle["id"] for bundle in self.bundles}), EXPECTED_BUNDLE_COUNT)

    def test_every_bundle_has_all_public_stages(self):
        for bundle in self.bundles:
            with self.subTest(bundle=bundle["id"]):
                self.assertTrue(bundle["context"])
                self.assertTrue(bundle["sourcePacket"])
                self.assertGreaterEqual(len(bundle["prompt"]), 600)
                self.assertTrue(bundle["output"])
                self.assertGreaterEqual(len(bundle["scorecard"]), 4)
                self.assertTrue(bundle["humanReview"])

    def test_every_link_resolves(self):
        for bundle in self.bundles:
            for link in bundle["links"]:
                with self.subTest(bundle=bundle["id"], path=link["path"]):
                    self.assertTrue((BASE_PATH / link["path"]).is_file())

    def test_review_scores_and_gates_are_consistent(self):
        for bundle in self.bundles:
            for row in bundle["scorecard"]:
                with self.subTest(bundle=bundle["id"], criterion=row["criterion"]):
                    self.assertIn(row["score"], range(1, 6))
                    self.assertIn(row["gate"], {"Pass", "Revise", "Human check"})
                    self.assertFalse(row["score"] < 3 and row["gate"] == "Pass")


if __name__ == "__main__":
    unittest.main()
