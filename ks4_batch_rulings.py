#!/usr/bin/env python3
"""ks4_batch_rulings.py — the port mechanics for a batch whose lessons are
DESIGN'S OWN delivery, placed verbatim (docs/ks4/design-reference/batch-4/).

Batches 2 and 3 were authored in their final form (docs/ks4/batch-engine.md
§2), so their compile path has nothing to fix up. Batch 4 is Design's
delivery, which still carries the review-tool shape the pilot's rulings
remove: a Route <select>, two static "Combined · Triple" / "Foundation ·
Higher" chips, hard-coded `.dc.html` prev/next and connects hrefs, and the
Ks4Practice number parse. This module applies exactly the pilot's rulings
for each of those, GENERICALLY (the pilot's own functions in ks4_rulings.py
are keyed by pilot design_file / slug and stay untouched), so the lesson
files on disk remain byte-identical to Design's (MD5SUMS) and every change
is a named, fail-loud ruling rather than a hand edit.

  B-R1      Route <select> dropped            (= ks4_rulings R1)
  B-R12     two header chips -> ONE route chip (= ks4_rulings R12; a
            Triple-only lesson's "Triple only" chip is the pathway span)
  B-PREVNEXT endPrev/endNext -> this.props.mrbPrevNext (= R-PREVNEXT)
  B-CONNECTS `X.dc.html` hrefs -> KS4.hrefFor('<slug>', R) (= R-CONNECTS,
            resolved against THIS batch's source files)
  B-PRACTICE-PARSE Ks4Practice's calc number parse reads "6,3" as 6.3 and
            "63,000" as 63000 (= R16 for the new block)

Applied only to a lesson record carrying `port_rulings=True`; batches 2 and
3 never carry it, so their bytes cannot move.
"""
import re

import ks4_rulings
from ks4_rulings import RulingError, _require


def _chip(slug, tpl):
    _require(tpl, ks4_rulings.R12_TIER_LINE, slug, "B-R12 (tier span)")
    tpl = tpl.replace(ks4_rulings.R12_TIER_LINE, "", 1)
    std = ks4_rulings.R12_PATHWAY_STD_SPAN
    only = std.replace("Combined · Triple", "Triple only")
    if tpl.count(std) == 1:
        pathway = std
    else:
        pathway = only
    _require(tpl, pathway, slug, "B-R12 (pathway span)")
    return tpl.replace(pathway, ks4_rulings.R12_CHIP_BLOCK, 1)


_HREF_RE = re.compile(r"href: '([\w.\-]+)\.dc\.html'")


def apply_connects(source_file, logic, slug_by_file):
    replaced = []

    def sub(m):
        f = m.group(1) + ".dc.html"
        if f not in slug_by_file:
            raise RulingError(
                "ks4_batch_rulings B-CONNECTS: %s links to %r, which is not "
                "one of this batch's lessons." % (source_file, f))
        replaced.append(slug_by_file[f])
        return "href: KS4.hrefFor('%s', R)" % slug_by_file[f]
    return _HREF_RE.sub(sub, logic), replaced


PRACTICE_PARSE_FROM = "const v = parseFloat(String(st.num).replace(/[\\s,]/g, ''));"
PRACTICE_PARSE_TO = ("const v = (" + ks4_rulings.R16_PARSE_FN + ")(st.num); // ⊕ B-PRACTICE-PARSE (R16 for Ks4Practice)")


def apply_practice_parse(text):
    _require(text, PRACTICE_PARSE_FROM, "Ks4Practice.dc.html", "B-PRACTICE-PARSE")
    return text.replace(PRACTICE_PARSE_FROM, PRACTICE_PARSE_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# SCIENCE RULINGS — named, fail-loud (exactly one occurrence), each logged in
# docs/ks4/BATCH4-SCIENCE-LOG.md with its source line. Design's files stay
# byte-identical on disk; these are applied at compile time only.
# ═══════════════════════════════════════════════════════════════════════
_P_TRANS_OLD = ('<p style="margin: 14px 0 0; font-size: 17px; line-height: 1.55; max-width: 62ch;">'
                'The transition metals, between Groups 2 and 3, have their own lesson on the Triple route.</p>')
SCIENCE = [
    # Mide's ruling (TASK-AA): hot-metal colours. A 700 C stop is added (the
    # slider's six stops had no stop at which "dull red" was true); the Planck
    # functions and every peak value are untouched.
    dict(id="B4-IRB-GLOW-1", slug="infrared-black-bodies", layer="logic",
         old="const TEMPS = [500, 1000, 1500, 2500, 3500, 5500];",
         new="const TEMPS = [500, 700, 1000, 1500, 2500, 3500, 5500]; // \u2295 B4-IRB-GLOW"),
    dict(id="B4-IRB-GLOW-2", slug="infrared-black-bodies", layer="logic",
         old=("  ['A dull red glow.', 'Enough of the longest visible wavelengths are now emitted to see.'],\n"
              "  ['Orange.', 'More of the visible band is emitted, and more at shorter wavelengths. The peak is still in the infrared.'],\n"
              "  ['Yellow-white.', 'All visible wavelengths are emitted strongly. The peak is still in the infrared.'],\n"
              "  ['White.', 'The peak has nearly reached the visible band.'],\n"),
         new=("  ['A dull red glow.', 'Enough of the longest visible wavelengths are now emitted to see. The peak is still in the infrared.'],\n"
              "  ['Orange.', 'More of the visible band is emitted, and more at shorter wavelengths. The peak is still in the infrared.'],\n"
              "  ['Yellow-white.', 'All visible wavelengths are emitted strongly. The peak is still in the infrared.'],\n"
              "  ['White.', 'All the visible wavelengths mix, so it looks white. The peak is still in the infrared.'],\n"
              "  ['White.', 'The peak has nearly reached the visible band.'],\n")),
    dict(id="B4-IRB-GLOW-3", slug="infrared-black-bodies", layer="logic",
         old="hook: null, ti: 1, moved: false,", new="hook: null, ti: 2, moved: false,"),
    dict(id="B4-IRB-GLOW-4", slug="infrared-black-bodies", layer="template",
         old='min="0" max="5" step="1" value="{{ ti }}"', new='min="0" max="6" step="1" value="{{ ti }}"'),
    # infrared: its renderVals returns a fresh object rather than spreading the
    # route helper, so the one route chip (B-R12) got no words or menu.
    dict(id="B4-IRB-CHIP", slug="infrared-black-bodies", layer="logic",
         old="route, onRoute: R.onRoute, isHigher,",
         new="route, onRoute: R.onRoute, isHigher, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,"),
    # thermal-conductivity: the "about the same" verdict described the changes
    # the wrong way round (a third as thick would raise the rate ninefold).
    dict(id="B4-TC-VERDICT", slug="thermal-conductivity", layer="logic",
         old=("One change raises the rate as much as the other lowers it: here the material conducts about "
              "three times better but the wall is a third as thick, or the reverse."),
         new="One change raises the rate threefold and the other lowers it threefold, so they cancel out."),
    # periodic-table: pack F1 — transition metals are Triple only; a pointer to
    # "the Triple route" is shown on Triple routes only.
    dict(id="B4-PT-F1", slug="periodic-table", layer="template", old=_P_TRANS_OLD,
         new='<sc-if value="{{ isTriple }}">' + _P_TRANS_OLD + '</sc-if>'),
    # development-periodic-table: potassium was known long before argon.
    dict(id="B4-DPT-F3", slug="development-periodic-table", layer="template",
         old="Argon and potassium, found later, show the same thing.",
         new="Argon, found later, and potassium show the same thing."),
    # atmospheric-pollutants: a camping stove flame does make some NOx; the
    # reply must not say it is "not hot enough". And catalytic converters are
    # off-spec (pack F2/F8): not even as a distractor in practice.
    dict(id="B4-AP-STOVE", slug="atmospheric-pollutants", layer="logic",
         old="A camping stove is not hot enough; the issue is the oxygen running out.",
         new="Oxides of nitrogen are linked to the high temperatures in engines. Here the danger is the oxygen running out."),
    dict(id="B4-AP-F2", slug="atmospheric-pollutants", layer="logic",
         old="['The catalytic converter', false]", new="['The engine oil', false]"),
]
APPLIED = []


def apply_science(slug, layer, text):
    for r in SCIENCE:
        if r["slug"] != slug or r["layer"] != layer:
            continue
        n = text.count(r["old"])
        if n != 1:
            raise RulingError("ks4_batch_rulings %s: expected exactly 1 occurrence in %s (%s), found %d.\n  looking for: %r"
                              % (r["id"], slug, layer, n, r["old"][:160]))
        text = text.replace(r["old"], r["new"], 1)
        APPLIED.append(r["id"])
    return text


def port_lesson(lesson, tpl, logic, slug_by_file):
    """-> (tpl, logic, report-dict)."""
    src = lesson["source_file"]
    tpl = ks4_rulings.apply_r1_route_selector(src, tpl)
    tpl = _chip(lesson["slug"], tpl)
    logic, n_prev, n_next = ks4_rulings.apply_r_prevnext(src, logic)
    logic, connects = apply_connects(src, logic, slug_by_file)
    tpl = apply_science(lesson["slug"], "template", tpl)
    logic = apply_science(lesson["slug"], "logic", logic)
    # B-R12's chip reads routeWords / routeSwitchOptions off the render values.
    if "Object.assign({}, R," not in logic and "routeWords" not in logic:
        raise RulingError("ks4_batch_rulings B-R12: %s's renderVals neither spreads the route helper nor "
                          "passes routeWords; the route chip would render empty." % lesson["slug"])
    return tpl, logic, dict(has_prev=bool(n_prev), has_next=bool(n_next), connects=connects)
