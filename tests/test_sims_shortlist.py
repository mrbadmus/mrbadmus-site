# -*- coding: utf-8 -*-
"""Tests for tools/sims_shortlist_page.py. No browser. Run:  python3 tests/test_sims_shortlist.py"""
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sims_shortlist_page as sp

RESULTS = {
    "ks3/physics/forces/a-lesson.html": {
        "title": 'Forces <b>& "friction"</b>', "route": "ks3/physics/forces/a-lesson.html",
        "blocks": [{"found": True, "after_img": "img/x-0-after.jpg"}]},
    "ks4/chemistry/bonding/ionic.html": {
        "title": "Ionic bonding", "route": "combined/foundation/chemistry/bonding/ionic.html", "blocks": []},
}
VERDICTS = {"ks3/physics/forces/a-lesson.html": {"verdict": "works and helps", "line": "Slider moves the arrows."}}


class Page(unittest.TestCase):
    def setUp(self):
        self.h = sp.build_page(RESULTS, VERDICTS, copy_images=False,
                               all_routes={"ks4/chemistry/bonding/ionic.html": ["combined/foundation/x.html", "triple/higher/x.html"]})

    def test_title_and_viewport(self):
        self.assertIn("<title>Sims shortlist</title>", self.h)
        self.assertIn("width=device-width", self.h)

    def test_no_external_urls(self):
        self.assertIsNone(re.search(r"(https?:)?//[a-z0-9.-]+\.[a-z]{2,}", self.h))
        self.assertNotIn("<link", self.h)
        self.assertNotIn("src=\"http", self.h)

    def test_buttons_per_item(self):
        self.assertEqual(self.h.count('class="keep"'), 2)
        self.assertEqual(self.h.count('class="remove"'), 2)
        self.assertEqual(self.h.count('aria-pressed="false"'), 4)

    def test_escaping(self):
        self.assertNotIn("<b>&", self.h)
        self.assertIn("Forces &lt;b&gt;&amp; &quot;friction&quot;&lt;/b&gt;", self.h)

    def test_verdicts(self):
        self.assertIn("Slider moves the arrows.", self.h)
        self.assertIn("Verdict pending", self.h)

    def test_groups_and_routes(self):
        self.assertLess(self.h.index("<h2>KS3</h2>"), self.h.index("<h2>KS4</h2>"))
        self.assertIn("triple/higher/x.html", self.h)

    def test_dark_mode_and_background(self):
        self.assertIn("prefers-color-scheme:dark", self.h)
        self.assertIn("background:var(--bg)", self.h)


if __name__ == "__main__":
    unittest.main()
