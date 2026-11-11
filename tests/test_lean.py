# -*- coding: utf-8 -*-
"""Tests for the lean lesson shape: lean_blocks.py output and lean_check.py rules.
No browser. Run:  python3 tests/test_lean.py
"""
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import lean_blocks as lb
import lean_check as lc


class TryLink(unittest.TestCase):
    """No pilot lesson has a matching simulation, so no pilot page shows the link.
    The renderer is proved here instead."""

    def test_none_renders_nothing(self):
        self.assertEqual(lb.try_link(None), "")

    def test_link_opens_in_the_same_tab(self):
        h = lb.try_link({"label": "Ripple tank", "href": "/simulations/physics/wave-motion-lab/"})
        self.assertIn('href="/simulations/physics/wave-motion-lab/"', h)
        self.assertIn("Try it: Ripple tank", h)
        self.assertNotIn("target=", h)          # same tab, so Back returns to the lesson
        self.assertNotIn("rel=", h)


class Cards(unittest.TestCase):
    CARD = {"kind": "card", "title": "Where wasted energy goes",
            "body": ["Plain sentence with <strong>bold</strong> and a <script>.",
                     {"points": ["one", "two"]},
                     {"mistakes": [("wrong idea", "right idea")]}]}

    def test_card_is_a_real_button_with_aria(self):
        h = lb.card(lb.Ctx(), self.CARD)
        self.assertRegex(h, r'<button type="button" class="lean-card-btn" id="(\S+)" aria-controls="(\S+)" aria-expanded="false">')
        bid, cid = re.search(r'id="(lean-b-\d+)" aria-controls="(lean-c-\d+)"', h).groups()
        self.assertIn('id="%s"' % cid, h)
        self.assertIn("<strong>bold</strong>", h)
        self.assertNotIn("<script>", h)        # only strong, em, sub, sup survive
        self.assertIn("Wrong: ", h)            # the mark is drawn, the word is for screen readers
        self.assertIn("Right: ", h)

    def test_ks4_state_lives_outside_the_template(self):
        """KS4's runtime rewrites any attribute the template names, so the template carries
        neither aria-expanded nor hidden; lean.js adds them."""
        h = lb.card(lb.Ctx(state_attrs=False), self.CARD)
        self.assertNotIn("aria-expanded", h)
        self.assertNotRegex(h, r"\shidden[\s>=]")

    def test_ks4_reveal_carries_no_state_attribute(self):
        t = {"kind": "reveal", "title": "T", "cols": ["In"], "rows": [("Ribs", "Up")]}
        h = lb.reveal(lb.Ctx(state_attrs=False), t)
        self.assertNotIn("aria-pressed", h)
        self.assertNotIn("aria-expanded", h)
        self.assertIn('aria-pressed="false"', lb.reveal(lb.Ctx(), t))

    def test_ids_are_unique_and_controls_resolve(self):
        ctx = lb.Ctx()
        reveal = {"kind": "reveal", "title": "In and out", "cols": ["In", "Out"],
                  "rows": [("Ribs", "Up", "Down"), ("Volume", "Up", "Down")]}
        h = (lb.knowledge(ctx, [self.CARD, reveal]) + lb.deeper(ctx, [self.CARD])
             + lb.key_words(ctx, ["a", "b", "c"]))
        ids = re.findall(r'\bid="([^"]+)"', h)
        self.assertEqual(len(ids), len(set(ids)))
        for target in re.findall(r'aria-controls="([^"]+)"', h):
            self.assertIn(target, ids)

    def test_reveal_is_a_real_table(self):
        h = lb.reveal(lb.Ctx(), {"kind": "reveal", "title": "T", "cols": ["In", "Out"],
                                  "rows": [("Ribs", "Up", "Down")]})
        for tag in ("<table", "<thead>", "<tbody>", '<th scope="col">', '<th scope="row">'):
            self.assertIn(tag, h)
        self.assertEqual(h.count("data-lean-cell"), 2)
        self.assertEqual(h.count("data-lean-showall"), 1)
        with self.assertRaises(ValueError):
            lb.reveal(lb.Ctx(), {"kind": "reveal", "title": "T", "cols": ["In", "Out"],
                                 "rows": [("Ribs", "only one cell")]})

    def test_dive_deeper_is_closed_until_tapped(self):
        h = lb.deeper(lb.Ctx(), [self.CARD])
        self.assertNotIn("data-lean-open", h)
        self.assertIn('class="lean-deeper-btn"', h)


class Routes(unittest.TestCase):
    def test_flags(self):
        self.assertEqual(lb.route_flag(["CH", "TH"]), "isHigher")
        self.assertEqual(lb.route_flag(["TF", "TH"]), "isTriple")
        self.assertEqual(lb.route_flag(["CF", "TF"]), "notHigher")
        self.assertEqual(lb.route_flag(["CF", "CH"]), "notTriple")
        self.assertEqual(lb.route_flag(["TH"]), "isTH")
        self.assertIsNone(lb.route_flag(None))
        self.assertIsNone(lb.route_flag(["CF", "CH", "TF", "TH"]))
        with self.assertRaises(ValueError):
            lb.route_flag(["CF", "TH"])

    def test_route_wrap_is_applied(self):
        ctx = lb.Ctx(route_wrap=lambda f, h: "<sc-if value=\"{{ %s }}\">%s</sc-if>" % (f, h))
        h = lb.card(ctx, {"kind": "card", "title": "H", "body": ["x"], "routes": ["CH", "TH"]})
        self.assertTrue(h.startswith('<sc-if value="{{ isHigher }}">'))


class Check(unittest.TestCase):
    def probs(self, text, kind="teach", ks=4):
        return lc.check_text("t", text, kind, ks)

    def test_never_use_phrases(self):
        for p in ("It's important to note that heat flows", "Crucially, the volume changes",
                  "This is essentially a pump", "In fact it falls", "Let's explore pressure",
                  "Notice that the ribs rise", "Simply put, air moves"):
            self.assertTrue(self.probs(p), p)
        self.assertFalse(self.probs("The ribs move up and out."))

    def test_contrasts(self):
        self.assertTrue(self.probs("It is not a pump, it's a pressure change."))
        self.assertTrue(self.probs("Energy isn't just stored, it's transferred."))
        self.assertFalse(self.probs("Wasted energy is not destroyed."))

    def test_dashes_and_questions(self):
        self.assertTrue(self.probs("Volume first — then pressure."))
        self.assertTrue(self.probs("Pages 5– and more"))
        self.assertFalse(self.probs("Level 3 · 5–6 marks"))
        self.assertTrue(self.probs("Does it recover?"))
        self.assertFalse(self.probs("Which one wastes more?", kind="start"))

    def test_ks3_sentence_length(self):
        long = "The diaphragm and the intercostal muscles contract at the same time so the whole chest gets much bigger."
        self.assertTrue(self.probs(long, ks=3))
        self.assertFalse(self.probs(long, ks=4))

    def test_ladder_stems_are_quiz_items(self):
        self.assertFalse(self.probs("Using what you learnt — explain why? Yes.", kind="stem", ks=3))
        self.assertTrue(self.probs("Crucially, why?", kind="stem", ks=3))

    def test_record_shape(self):
        rec = {"slug": "x", "start": {"question": "q?", "options": [("a", "r")], "answer": 2},
               "words": ["a", "b"], "knowledge": [], "deeper": [], "key_fact": "Fine."}
        msgs = " ".join(lc.check_record(rec, 4))
        self.assertIn("2 key words", msgs)
        self.assertIn("1 options", msgs)
        self.assertIn("answer must be 0 or 1", msgs)


if __name__ == "__main__":
    unittest.main(verbosity=1)
