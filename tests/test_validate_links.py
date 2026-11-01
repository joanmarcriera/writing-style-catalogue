import sys
import tempfile
import unittest
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH / "scripts"))

import validate_links  # noqa: E402


class ValidateLinksTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name)
        (self.base / "docs").mkdir()
        self.page = self.base / "docs" / "page.md"
        self.page.write_text("# Page title\n\n## Next steps (draft)\n\n## Next steps (draft)\n\n```\n# not a heading\n```\n", encoding="utf-8")
        self.source = self.base / "README.md"
        self.source.write_text("", encoding="utf-8")
        validate_links._anchor_cache.clear()

    def tearDown(self):
        self._tmp.cleanup()

    def check(self, link):
        return validate_links.validate_link(self.base, self.source, link)[0]

    def test_heading_slug_matches_github_style(self):
        self.assertEqual(validate_links.heading_slug("Next steps (draft)"), "next-steps-draft")
        self.assertEqual(validate_links.heading_slug("Use `code` and [links](x.md)"), "use-code-and-links")

    def test_files_directories_and_anchors(self):
        self.assertTrue(self.check("docs/page.md"))
        self.assertTrue(self.check("docs/"))
        self.assertTrue(self.check("docs/page.md#page-title"))
        self.assertTrue(self.check("docs/page.md#next-steps-draft-1"))
        self.assertFalse(self.check("docs/page.md#not-a-heading"))
        self.assertFalse(self.check("docs/missing.md"))
        self.assertFalse(self.check("docs/missing.png"))

    def test_external_links_are_ignored_and_images_included(self):
        links = validate_links.find_markdown_links(
            "[a](https://example.com) [b](mailto:x@example.com) ![c](img/x.png) [d](page.md \"Title\")"
        )
        self.assertEqual(links, [("c", "img/x.png"), ("d", "page.md")])
        html = validate_links.find_html_links('<a href="https://x.test"></a><a href="#top"></a><script src="a.js"></script>')
        self.assertEqual(html, [("#top", "#top"), ("a.js", "a.js")])


if __name__ == "__main__":
    unittest.main()
