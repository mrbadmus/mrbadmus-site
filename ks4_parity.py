#!/usr/bin/env python3
"""ks4_parity.py — the KS4 pilot parity gate (docs/ks4/pilot-build-contract.md).

    python3 ks4_parity.py [--lesson SLUG] [--width N] [--json OUT.json]

Drives all 54 ported KS4 pilot pages (14 lessons x their routes) in headless
Chrome and checks them against `docs/ks4/pilot-inventory/reference.json` —
the real-browser measurement of Design's own 14 `.dc.html` pages taken by
`docs/ks4/pilot-inventory/measure_design.py`. Exits 1 on any FAIL.

Reuses `measure_design.py`'s own measurement functions VERBATIM wherever a
selector-based reading is generic (rail, ladder, key note, question bank,
focusables, overflow, computed styles, the interaction sequence) — the port
and Design's page are measured by IDENTICAL code so a difference in the
result is a difference in the PAGE, not in how it was read.

── Legitimate differences from Design's reference (the whitelist) ─────────

Every one of these is a *documented ruling* in `ks4_rulings.py`, not a gate
weakening — a difference NOT on this list is a real FAIL.

  R1            the Route <select> control and its "Route ... Combined
                Foundation/Combined Higher/..." text is gone from the header
                on every port page (one URL = one route).
  R6            series-parallel-circuits' R_total card gains a
                "Not on the sheet - learn it" chip Design's page never had.
  R7            series-parallel-circuits / resistors lose their whole
                "Examiner tip ... Draft - awaiting approval" section.
  R8            metals-alloys' rung-2 prompt gains "model data for".
  R9            states-of-matter / polymers / metals-alloys hide their
                "Contains Higher"/"Contains Triple" header badge on a route
                where that flag is false (Design's page shows it always).
  R-PREVNEXT    prev/next neighbours are the REAL per-route topic order
                (all_subtopics_*.py), not Design's hardcoded pilot-internal
                guess — checked against `build_ks4.compute_prev_next()`
                directly rather than against Design's text.
  R-CONNECTS    "Connects to" links point at real site URLs, not sibling
                `.dc.html` filenames.
  R-SLUG        (no visible-text effect; not in this whitelist)
  ks4_science_rulings.py  (not yet landed — see `science_rulings_for()`)
  R11/R12       (Mide's ruling, 27 Sep 2026) the header's two static
                "Combined · Triple" / "Foundation · Higher" chips are gone
                on every port page, replaced by one route-stating chip +
                switcher (checked directly: `check_route_chip()` proves
                there is exactly one, its words match the page's own
                route, and its menu names exactly the lesson's OTHER
                existing routes at their real URLs; `check_route_switch_
                keyboard()` proves Enter/Space/Esc/focus-return).
  R13           (Mide's ruling, 27 Sep 2026) `series-parallel-circuits` /
                `resistors` gain the FINAL, approved exam tip in place of
                the removed draft (R7, superseded — see below); checked
                directly against `all_subtopics_physics_triple_higher.py`'s
                `examiner_tip` field, not merely excused.
  R14           (Mide's ruling, 27 Sep 2026) a Triple route's eyebrow/
                key-note spec number is the separate science's own
                (8462/8463), not Combined's (8464). ⊕ D13 (theme-run audit,
                27 Sep 2026): Combined routes are no longer byte-identical
                either — they now NAME 8464 the same way Triple always
                named its own code (`build_ks4.SPEC_TEXT`'s "combined"
                values), and nanoparticles (outside SPEC_TEXT, R5) gained
                "(8462)" on both its routes. Checked directly against
                `build_ks4.SPEC_TEXT` / R5's two literals by
                `check_spec_numbers()`, not merely excused.

  R7 above is SUPERSEDED by R13, 27 Sep 2026: the two physics lessons no
  longer lose the section, they gain the FINAL text in it, so
  `R7_SLUGS` is now empty and the section is compared like any other
  (its OLD/NEW text substitution lives in `apply_text_whitelist`).

Reference.json's own asymmetry is preserved rather than fought: the DEFAULT
route (Triple Higher, "TH") is swept at all 5 widths and gets the full D/E/F/
G/H passes; the other 3 routes are compared at 1280 only for structure/text/
layout (reference has no other-width data for them) but still get their own
overflow/rail/console/keyboard checks at every width, since those don't need
a reference value to be meaningful.

`docs/ks4/pilot-inventory/reference.json` lives under `docs/` and so CANNOT
appear in this gate's `gate_registry.py` `watches` list (CLAUDE.md's
gate-machinery rule: nothing under `docs/**` may be watched) — see this
file's registry row `why` for the named, accepted gap this leaves, mirroring
the wording CLAUDE.md itself uses for `ks3_rail_manifest` / `ks3_statutory`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, os.path.join(REPO_ROOT, "docs", "ks4", "pilot-inventory"))

import ks3_browser as cdp  # noqa: E402
import ks4_lessons  # noqa: E402
from ks4_lessons import blocks as ks4_blocks  # noqa: E402
import ks4_rulings  # noqa: E402
import build_ks4  # noqa: E402
import measure_design as MD  # noqa: E402  (reused verbatim per the contract)
from theme_head import THEME_HEAD  # noqa: E402

try:
    import ks4_science_rulings as _KSR  # noqa: E402
except ImportError:
    _KSR = None

REFERENCE_PATH = os.path.join(REPO_ROOT, "docs", "ks4", "pilot-inventory", "reference.json")
WIDTHS = [1280, 1340, 820, 390, 360]
DEEP_ROUTE = "TH"  # matches reference.json's "default_route": "Triple Higher"
ROUTE_LABEL = ks4_lessons.ROUTE_LABELS
ROUTE_FLAGS = {  # route code -> (isHigher, isTriple)
    "CF": (False, False), "CH": (True, False),
    "TF": (False, True), "TH": (True, True),
}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config_env  # noqa: E402 — shared/config.js's worlds
# The production backend's host, read out of shared/config.js (B2C unit 6).
BACKEND_HOST = config_env.PROD_BACKEND_HOST

# ═══════════════════════════════════════════════════════════════════════
# the whitelist — every substitution/removal a known ruling licenses
# ═══════════════════════════════════════════════════════════════════════
_WS_RE = re.compile(r"\s+")


def normalize_ws(s):
    return _WS_RE.sub(" ", s or "").strip()


def squash(s):
    """Whitespace removed entirely, for EQUALITY only. The browser-side
    template compiler (build_ks4.py's `_COMPILE_JS` walk()) drops
    whitespace-only text nodes between elements (`if (!v.trim()) return
    null`) — a `.dc.html` source with real newline/indent whitespace between
    e.g. `<h1>` and `<p>` has a real (collapsing-to-one-space) text node
    there; the compiled/baked port DOM does not, because that node was
    never in the compiled template at all. Both render IDENTICALLY (h1/p
    are block-level; the visual line break doesn't depend on an inter-
    element text node), but `.textContent` on the two DOMs differs by
    exactly the missing spaces at every such boundary — universally, on
    every section, on every lesson. Comparing on content with all
    whitespace removed (not single-spaced) is the fix: it can never be
    fooled by a genuine word-boundary content change (two real words losing
    their separating space would show up as one new word, which the
    original text - reference or port - would already have had), while it
    stops flagging this compiler artifact as a text divergence. Reported
    diff windows still use `normalize_ws` for human readability."""
    return _WS_RE.sub("", s or "")


ROUTE_SELECT_NEEDLE = normalize_ws(
    "Route Combined FoundationCombined HigherTriple FoundationTriple Higher")

R6_ADDITION_TEXT = "Not on the sheet · learn it"  # ks4_rulings.R6 (series-parallel-circuits)
R8_FROM_TEXT = "The table shows the hardness of iron mixed with different percentages of carbon."
R8_TO_TEXT = "The table shows model data for the hardness of iron mixed with different percentages of carbon."
# ⊕ Superseded 27 Sep 2026 (Mide's ruling, R13). This used to read
# `{"series-parallel-circuits", "resistors"}` and `reference_sections_
# after_rulings()` DROPPED the "Examiner tip" section from Design's
# reference for both, because R7 used to remove that section from the port
# entirely (flag 11: the draft tip was never approved). R13 replaces R7:
# the section is no longer removed, it gets the FINAL approved text — so
# Design's reference and the port now both carry it, section counts match
# with no adjustment, and its TEXT is proven directly against
# `all_subtopics_physics_triple_higher.py` by `compare_section_text()`'s own
# R13 branch, not merely excused. Left as an empty set (not deleted) so a
# FUTURE lesson whose ruling genuinely removes a whole section still has
# this mechanism to use.
R7_SLUGS = set()

# ⊕ R12 (Mide's ruling, 27 Sep 2026) — the two static header chips Design's
# page always carried, in the ONE place they ever appear (index 0, the
# header section). `build_ks4.ROUTE_WORDS` are the NEW chip's four possible
# labels — the routeWords/routeSwitchOptions link text baked into the port,
# stripped from the PORT side in `compare_section_text()` (symmetric to
# this constant being stripped from the REFERENCE side here).
R12_OLD_TIER_CHIP = "Foundation · Higher"
R12_OLD_PATHWAY_CHIP = {"nanoparticles": "Triple"}  # default (13 of 14): "Combined · Triple"



def science_rulings_for(slug):
    """Reader of `ks4_science_rulings.py`'s 99+2 rows (landed 26 Sep 2026:
    `dict(id=..., lesson=..., layer=..., old=..., new=..., why=..., spec=...)`
    in its `ROWS` list). Returns (old, new) pairs scoped to `slug`.

    Applying every row's substitution to rendered, normalized textContent —
    regardless of its `layer` — is safe even for the ~40 `layer="logic"`
    rows that rewrite JS source rather than prose (state-variable renames
    like `fZero`->`fMin`, or `old` strings that carry the JS literal's OWN
    quote characters, e.g. `"'Hydrogen sits above Group 1...'"`): those
    `old` needles never occur inside a rendered section's textContent in the
    first place (textContent has no source-code punctuation, no quote
    marks, no JS identifiers), so the `.replace()` is a harmless no-op for
    them. It only ever fires for the subset whose `old` is itself a chunk of
    rendered prose — which is exactly the subset this gate needs.

    Defensive about the container name (`ROWS`/`RULINGS`/`SCIENCE_RULINGS`)
    and row shape (dict or simple object) in case either moves again."""
    if _KSR is None:
        return []
    rows = (getattr(_KSR, "ROWS", None) or getattr(_KSR, "RULINGS", None)
            or getattr(_KSR, "SCIENCE_RULINGS", None) or [])
    out = []
    for r in rows:
        get = r.get if isinstance(r, dict) else (lambda k, d=None: getattr(r, k, d))
        r_lesson = get("lesson") or get("slug")
        if r_lesson is not None and r_lesson != slug:
            continue
        old = get("old") or get("before") or get("design_text")
        new = get("new") or get("after") or get("port_text")
        if old and new is not None:
            out.append((old, new))
    return out


DRAFT_BANNER_TEXT = "Draft — not yet science-reviewed."
# ⊕ THEME RUN (26 Sep 2026, THEME-CONTRACT.md) — R15's `data-mrb-theme` slot
# mounts shared/theme.js's Light/Dark/System control. Its accessible text
# (a real `<legend>` plus one visually-hidden `.mrb-theme-sr` label per
# radio — screen-reader content, so it DOES appear in `textContent` even
# though nothing is visible) is new on every one of these 54 pages and
# exists NOWHERE in Design's reference, captured before the theme run.
# Order matches theme.js's own PREFS/LABELS arrays and DOM order (legend,
# then light/dark/system in that order) with no whitespace between —
# confirmed against the DOM (`_WS_RE` normalizes runs of whitespace to
# single spaces but never INSERTS one where the compiled DOM has none,
# which is the case here: legend and each `.mrb-theme-sr` span are
# adjacent siblings with no text node between them).
#
# ⊕ D11 (theme-run audit, 27 Sep 2026) — R15 moved the slot OUT of the
# lesson's own index-0 header section and into the shared Ks4Chrome block
# (the nav, brand + breadcrumb), so this text no longer appears in ANY
# lesson's own `sections` list at all — Ks4Chrome is shared boilerplate,
# not one of the per-lesson sections `compare_section_text()` walks
# against `reference.json`. The `port_norm.replace(THEME_CONTROL_TEXT, "")`
# call at index==0 below is consequently a no-op on every lesson now (the
# text it used to strip is not there to find) — left in place rather than
# deleted, because a no-op `.replace()` is harmless and this stays correct
# if a future ruling ever puts a lesson-hero copy of the control back.
THEME_CONTROL_TEXT = "Colour theme" + "Light" + "Dark" + "System"
_BANK_TALLY_RE = re.compile(r"\d+\s+of\s+\d+\s+answered\s*·\s*\d+\s+matched the mark scheme"
                             r"|\d+\s+answered\s*·\s*\d+\s+matched the mark scheme")


def badge_removal_for(slug, route):
    """R9: the header badge text ('Contains Higher'/'Contains Triple') to
    strip from Design's reference header text when this route's flag is
    false. `None` when this lesson has no R9 badge at all."""
    hit = ks4_rulings.R9_TARGETS.get(slug)
    if hit is None:
        return None
    flag, label, _style = hit
    is_higher, is_triple = ROUTE_FLAGS[route]
    active = is_higher if flag == "isHigher" else is_triple
    return None if active else label


# ═══════════════════════════════════════════════════════════════════════
# TEXT_EXEMPTIONS — job 1, docs/ks4/pilot-build-contract.md.
#
# `science_rulings_for()`'s generic `.replace(old, new)` pass (above) only
# ever fires when a ruling's `old` is ITSELF a chunk of rendered prose — its
# own docstring says so. Two whole classes of `ks4_science_rulings.ROWS` row
# are NOT that, and both are real, in this corpus:
#
#   1. `old`/`new` are JS or JSX SOURCE, not prose — a `K.find(...)` call
#      chain, a ternary, a `prompt="..."` JSX attribute, an HTML tag with a
#      style attribute. The literal `old` string (quotes, parens, `label: `,
#      `<p style="...">` and all) never occurs in extracted textContent,
#      which has no source-code punctuation at all — so `.replace()` is a
#      harmless no-op and the SAME text divergence that the ruling in fact
#      causes is left unexplained by the generic pass.
#   2. `op: 'drop_item'` / a fallback-chain EDIT changes *which* authored
#      bank item or ladder rung is selected, or reorders a `Ks4Sort` card
#      list whose render order is `items.sort by hash(item.text)` (so
#      editing three cards' text also silently reorders them) — there is no
#      `old`/`new` substitution that could ever express "a different item
#      entirely" or "these six lines in a new order".
#
# Every entry below was individually traced BEFORE being added: the
# design-vs-port diff was read in full (not just the 80-char window the
# gate prints) and matched against the named ruling's `new` value, in one
# case (ionic-compounds) by literally reimplementing `Ks4Sort`'s own
# `H(text)` FNV-1a hash in Python and proving the reference's card order is
# exactly `sorted(old_texts, key=H)` and the port's is exactly
# `sorted(new_texts, key=H)`. A pair NOT explained this way is a real port
# defect, not a candidate for this table — none were found here; all 61
# pre-existing FAILs trace to exactly the 13 TEXT_EXEMPTIONS keys below (14
# raw (lesson, section) pairs — polymers' bank fails under two different
# route-labelled eyebrows that collapse to one key; see the note below the
# table — first counted at 10 from the printed table alone, corrected to 14
# by re-reading every row's FULL detail string).
#
# Shape: {(lesson, exemption_key): [ {"routes": set(...)|None, "rulings":
# [ruling ids]}, ... ]}. `routes=None` means "every route this lesson
# ships" (the ruling's effect is route-independent); a route SET scopes the
# exemption to only the routes/widths where that ruling's own logic
# actually fires — checked against `ks4_lessons.LESSONS`'s route list, not
# against a blanket tolerance. Every ruling id is verified at import time
# to exist in `ks4_science_rulings.ROWS` — an unknown id raises, per the
# contract ("the gate raises if an id is unknown").
#
# ⚠️ This table was FIRST built by reading only the first `text_fails`
# entry printed per (route, width) row — `Results.record()` joins up to
# three failing sections with " | " into one printed `detail`, and two rows
# (properties-ionic-compounds/CH, giant-covalent-structures/CH) each carried
# a SECOND failing section past the first one printed. The true count is 14
# distinct (lesson, section) pairs, not the 10 first identified — found by
# re-parsing every row's FULL `detail` string (split on " | "), not by
# eyeballing the printed table. Both extra pairs are the exact same defect
# class as `metallic-bonding-C1`/`nanoparticles-C7` above (a `command:`
# override object literal, `old`/`new` including the JS property-key
# syntax) and are listed under their own lessons below.
TEXT_EXEMPTIONS = {
    # design: "...even though it sits above Group 1." (KeyNote line 05)
    # port:   "...even though it has one outer electron like Group 1."
    # chemical-bonds-C4's `old`/`new` are JS string LITERALS (their own
    # quote marks included) — never present in rendered text as such.
    ("chemical-bonds", "s-keynote"): [
        {"routes": None, "rulings": ["chemical-bonds-C4"]},
    ],
    # Ks4Sort renders its 6 limitation-cards in
    # `items.slice().sort((a,b) => H(a.text)-H(b.text))` order — FNV-1a of
    # the card's OWN (possibly ruled) text. C5/C6/C7 each rewrite one
    # card's text for 8462 4.2.1.3 accuracy; because the sort key is a hash
    # of that same text, rewording also reorders the deck. Verified:
    # sorted(unruled 6 texts, key=H) == reference.json's measured order;
    # sorted(ruled 6 texts, key=H) == the port's measured order, exactly.
    ("ionic-compounds", "s-models"): [
        {"routes": None, "rulings": ["ionic-compounds-C5", "ionic-compounds-C6",
                                      "ionic-compounds-C7"]},
    ],
    # design rung 1: "Name the particles that are free to move in a metal."
    # port rung 1:   "Describe the structure of a metal..."
    # metallic-bonding-C1 swaps the priority of two `K.find()` fallback
    # calls (CF/TF only — CH/TH already picked the "Describe" item, per the
    # ruling's own `why`), so the WHOLE rung-1 item changes, not one phrase.
    ("metallic-bonding", "s-ladder"): [
        {"routes": {"CF", "TF"}, "rulings": ["metallic-bonding-C1"]},
    ],
    # design bench caption: "... · switch open"; port: "... · before the
    # test". properties-ionic-compounds-C4's `old`/`new` are a JS ternary's
    # two string arms with the ternary's own `(on ? '...' : '...')` syntax
    # wrapped around them.
    ("properties-ionic-compounds", "s-bench"): [
        {"routes": None, "rulings": ["properties-ionic-compounds-C4"]},
    ],
    # rung 1's command chip flips 'State' -> 'Explain' on CH/TH (R.isHigher)
    # — properties-ionic-compounds-C6, an object-literal `command: '...'`
    # override, same JS-syntax gap.
    ("properties-ionic-compounds", "s-ladder"): [
        {"routes": {"CH", "TH"}, "rulings": ["properties-ionic-compounds-C6"]},
    ],
    # design: "The state of hexane at 25 °C"; port adds "(it melts at
    # −95 °C)" — properties-small-molecules-C6's `old`/`new` are a JS
    # object property (`label: '...'`), quotes and key included.
    ("properties-small-molecules", "s-ladder"): [
        {"routes": None, "rulings": ["properties-small-molecules-C6"]},
    ],
    # rung 1 swaps to the Combined-appropriate item on CF/CH (R.isTriple
    # branch in a ternary/`K.find()` chain — polymers-C1).
    ("polymers", "s-ladder"): [
        {"routes": {"CF", "CH"}, "rulings": ["polymers-C1"]},
    ],
    # the question bank has no section `id`; keyed by its eyebrow prefix
    # (route name stripped — see `exemption_key()`). polymers-C7/-C8 each
    # `op: 'drop_item'` the (chemistry-only, 4.7.3.1) monomer stem from the
    # CF/CH pool respectively — a dropped item has no `old`/`new` pair to
    # substitute at all, and removing it changes every later item's
    # position in the rendered list. polymers-C6 edits a surviving CF/TF
    # item's explanation in the same pool.
    ("polymers", "eyebrow:Practice set"): [
        {"routes": {"CF"}, "rulings": ["polymers-C6", "polymers-C7"]},
        {"routes": {"CH"}, "rulings": ["polymers-C8"]},
    ],
    # design hook prompt: "...same very high melting point. What differs?"
    # port: "...both very high melting points. What differs?"
    # giant-covalent-structures-C1's `old`/`new` are a JSX attribute
    # (`prompt="..."`), quotes included.
    ("giant-covalent-structures", "s-hook"): [
        {"routes": None, "rulings": ["giant-covalent-structures-C1"]},
    ],
    # rung 1's command chip flips 'Identify' -> 'Explain' on CH/TH
    # (R.isHigher) — giant-covalent-structures-C5, same object-literal gap.
    ("giant-covalent-structures", "s-ladder"): [
        {"routes": {"CH", "TH"}, "rulings": ["giant-covalent-structures-C5"]},
    ],
    # design KeyNote line 01: "...positive ions in regular layers,
    # surrounded by delocalised electrons."; port: "...with strong
    # metallic bonding, so most have high melting and boiling points."
    # metals-alloys-C9's `old`/`new` are JS string literals, quotes
    # included.
    ("metals-alloys", "s-keynote"): [
        {"routes": None, "rulings": ["metals-alloys-C9"]},
    ],
    # TF only (TH's rung-3 already matched, per the ruling's own `why`):
    # nanoparticles-C7 deletes a `K.find(...) || ` fallback needle
    # entirely (`new` is `''`), so TF's rung 3 falls through to a
    # different authored item.
    ("nanoparticles", "s-ladder"): [
        {"routes": {"TF"}, "rulings": ["nanoparticles-C7"]},
    ],
    # design: a plain "V = I R" equation card with no chip; port adds an
    # "Equation sheet" badge (matching L13's identical card) —
    # resistors-C9's `old`/`new` are raw HTML (`<p style="...">`), and the
    # inserted `<span>Equation sheet</span>` text never existed on
    # Design's side to substitute FROM.
    ("resistors", "s-equation"): [
        {"routes": None, "rulings": ["resistors-C9"]},
    ],
}


def _validate_text_exemptions():
    known_ids = set()
    if _KSR is not None:
        rows = (getattr(_KSR, "ROWS", None) or getattr(_KSR, "RULINGS", None)
                or getattr(_KSR, "SCIENCE_RULINGS", None) or [])
        for r in rows:
            rid = r.get("id") if isinstance(r, dict) else getattr(r, "id", None)
            if rid:
                known_ids.add(rid)
    for (lesson, key), entries in TEXT_EXEMPTIONS.items():
        for entry in entries:
            for rid in entry["rulings"]:
                if rid not in known_ids:
                    raise SystemExit(
                        "ks4_parity: TEXT_EXEMPTIONS[(%r, %r)] names ruling "
                        "id %r, which does not exist in "
                        "ks4_science_rulings.ROWS — the exemption has "
                        "drifted from the rulings it claims to rest on."
                        % (lesson, key, rid))


_validate_text_exemptions()


def exemption_key(sec):
    """The TEXT_EXEMPTIONS lookup key for a section: its `id` when it has
    one, else its eyebrow with any ` · <route name>` suffix stripped (the
    ONE eyebrow-keyed exemption, the polymers question bank, carries a
    route-specific eyebrow — 'Practice set · Combined Foundation' etc — and
    the exemption is keyed on the route-independent prefix)."""
    if sec.get("id"):
        return sec["id"]
    eyebrow = (sec.get("eyebrow") or "").split(" · ")[0].strip()
    return ("eyebrow:" + eyebrow) if eyebrow else None


APPLIED_EXEMPTIONS = []  # (lesson, key, route, ruling ids) actually exercised


def exemption_for(slug, route, sec):
    key = exemption_key(sec)
    if key is None:
        return None
    for entry in TEXT_EXEMPTIONS.get((slug, key), ()):
        if entry["routes"] is None or route in entry["routes"]:
            return entry["rulings"]
    return None


def section_key(sec):
    if sec.get("id"):
        return "id:" + sec["id"]
    if sec.get("eyebrow"):
        return "eyebrow:" + sec["eyebrow"][:40]
    return "text:" + normalize_ws(sec.get("text", ""))[:30]


def is_examiner_tip_section(sec):
    return normalize_ws(sec.get("text", "")).startswith("Examiner tip")


def is_endmatter_section(sec):
    t = normalize_ws(sec.get("text", ""))
    return sec.get("class") == "sc-host" and t.startswith("Previous and next")


def reference_sections_after_rulings(slug, sections):
    """Design's section list, with R7's whole removed section dropped when
    this lesson carries that ruling."""
    if slug not in R7_SLUGS:
        return list(sections)
    out = [s for s in sections if not is_examiner_tip_section(s)]
    if len(out) == len(sections):
        raise SystemExit(
            "ks4_parity: %s is in R7_SLUGS but reference.json carries no "
            "'Examiner tip' section to remove — ks4_rulings.py R7 or this "
            "whitelist has drifted from the delivery." % slug)
    return out


def apply_text_whitelist(slug, route, index, sec, ref_text_norm):
    """Design's normalized text for one section, with every licensed
    substitution/removal applied, ready to compare byte-for-byte against
    the port's normalized text for the SAME section."""
    t = ref_text_norm
    if index == 0:  # the header
        t = t.replace(ROUTE_SELECT_NEEDLE, "").strip()
        t = _WS_RE.sub(" ", t)
        badge = badge_removal_for(slug, route)
        if badge:
            t = t.replace(badge, "").strip()
            t = _WS_RE.sub(" ", t)
        # ⊕ R12 — the two static chips Design's page always carried here.
        # The port's replacement chip/switcher text is stripped from the
        # PORT side instead (compare_section_text(), symmetrically).
        t = t.replace(R12_OLD_PATHWAY_CHIP.get(slug, "Combined · Triple"), "")
        t = t.replace(R12_OLD_TIER_CHIP, "")
        t = _WS_RE.sub(" ", t).strip()
    # ⊕ R14 — a Triple route's spec number is the separate science's own,
    # not Combined's. Applied on WHATEVER section carries it (the header's
    # eyebrow is always index 0; the KeyNote child component's `spec` prop
    # renders inside whichever section that dc-import sits in, lesson by
    # lesson) — a plain substring replace is exact and safe here because
    # every `combined` string below is the FULL literal citation Design's
    # page shows nowhere else (verified when `build_ks4.SPEC_TEXT` was
    # built: each string is unique to its own eyebrow/key-note line).
    #
    # ⊕ D13 (theme-run audit, 27 Sep 2026) — `spec_entry["combined"]` is now
    # the RENDER-TIME value (with "(8464)"), but `t` here is Design's
    # ORIGINAL reference text, which never had "(8464)" on any route — it
    # is the literal her template was compiled from, before D13 gave
    # `build_ks4.compile_lesson()` a reason to swap it for anything. So the
    # substitution SOURCE is always `old_combined_spec_text()` regardless
    # of route, and the destination now branches both ways: a Triple route
    # (TF/TH) reconciles to `entry["triple"]` exactly as it always did, and
    # a Combined route (CF/CH) — new with D13 — reconciles to `entry
    # ["combined"]` itself, since that is no longer byte-identical to what
    # `t` already contains.
    spec_entry = build_ks4.SPEC_TEXT.get(slug)
    if spec_entry is not None:
        old_spec = build_ks4.old_combined_spec_text(slug)
        want = spec_entry["triple" if route in ("TF", "TH") else "combined"]
        t = t.replace(normalize_ws(old_spec["eyebrow"]),
                      normalize_ws(want["eyebrow"]))
        t = t.replace(normalize_ws(old_spec["keynote"]),
                      normalize_ws(want["keynote"]))
    # ⊕ D13/R5 (theme-run audit, 27 Sep 2026) — nanoparticles is outside
    # `SPEC_TEXT` (see that dict's own comment: no Combined route), so the
    # block above never reaches it. `ks4_rulings.apply_r5_nanoparticles_
    # spec` adds "(8462)" to its eyebrow and key-note on both its routes
    # (TF, TH — nanoparticles has no CF/CH at all), which Design's
    # reference text never carried; reconciled here the same way as R14.
    if slug == "nanoparticles":
        t = t.replace(
            normalize_ws("AQA Chemistry 4.2.4 (chemistry only) · Quantitative"),
            normalize_ws("AQA Chemistry (8462) 4.2.4 (chemistry only) · Quantitative"))
        t = t.replace(normalize_ws("AQA 4.2.4 (chemistry only)"),
                      normalize_ws("AQA 4.2.4 (8462) (chemistry only)"))
    if slug == "series-parallel-circuits" and R6_ADDITION_TEXT not in t:
        # R6 is an ADDITION on the port side; nothing to strip from Design's
        # side — the port's own text will carry the extra chip, handled by
        # comparing port_text.replace(R6_ADDITION_TEXT, '') instead (see
        # compare_section_text()).
        pass
    if slug == "metals-alloys":
        t = t.replace(R8_FROM_TEXT, R8_TO_TEXT)
    for old, new in science_rulings_for(slug):
        t = t.replace(normalize_ws(old), normalize_ws(new))
    # ⊕ R-TUTOR-NAME (ks4_rulings.py, 9 Oct 2026) — Ks4End's tutor card is
    # headed "Ask MrBadmus", not Design's "Ask Mr Badmus AI". A no-op on any
    # section that does not carry the card.
    t = t.replace("Ask Mr Badmus AI", "Ask MrBadmus")
    return t


R13_TIP_SLUGS = {"series-parallel-circuits", "resistors"}


def _approved_tip_text(slug):
    """The FINAL, approved exam-tip text for one of R13_TIP_SLUGS, read
    straight from `all_subtopics_physics_triple_higher.py`'s `examiner_tip`
    field — the SAME record `build_ks4.build_source_record()` serves onto
    the page via `shared/ks4-source.js` (never a second, hand-copied literal
    here that could drift from it)."""
    import all_subtopics_physics_triple_higher as _phys_th
    for topic_list in _phys_th.PHYSICS_SUBTOPICS_ALL.values():
        for st in topic_list:
            if st.get("id") == slug:
                return st.get("examiner_tip") or ""
    return ""


# ⊕ R18 (Mide's rule 1, 2 Oct 2026; ks4_rulings.apply_r18_start_here) — every
# pilot lesson's `#s-hook` is Design's two-option Ks4Guess carrying its record
# in ks4_lessons/start_here.py, no longer Design's pilot Ks4Choice hook. Like
# R13, the replacement is PROVED (every rendered piece present, in order, and
# the old hook gone), not merely excused.
R18_SLUGS = ks4_rulings.r18_slugs()


def _r18_expected(slug):
    from ks4_lessons import start_here
    r = start_here.START_HERE[slug]
    return ["Start here", r["title"], r["scene"],
            "If you had to guess, " + r["question"],
            r["options"][0]["text"], r["options"][1]["text"]]


def _r18_check(slug, port_text_norm):
    port_sq = squash(normalize_ws(port_text_norm))
    pos = 0
    for frag in _r18_expected(slug):
        i = port_sq.find(squash(normalize_ws(frag)), pos)
        if i < 0:
            return "R18 opener: %r missing or out of order" % frag[:80]
        pos = i + 1
    if "Commit first" in port_text_norm:
        return "R18 opener: Design's Ks4Choice hook is still present"
    return None


def compare_section_text(slug, route, index, sec, ref_text_norm, port_text_norm):
    if slug in R18_SLUGS and sec.get("id") == "s-hook":
        return _r18_check(slug, port_text_norm)
    # ⊕ R13 — proves the approved exam tip is present BYTE-EXACT, rather
    # than merely excusing a known difference from Design's (unapproved,
    # different-wording) draft. Both physics lessons' tip section carries
    # this on every route (examiner_tip is not route-varying).
    if slug in R13_TIP_SLUGS and is_examiner_tip_section(sec):
        expected = normalize_ws(_approved_tip_text(slug))
        got = normalize_ws(port_text_norm.replace("Examiner tip", "", 1))
        if not expected:
            return ("R13: no examiner_tip found for %r in "
                     "all_subtopics_physics_triple_higher.py" % slug)
        if got != expected:
            return "R13 approved exam tip mismatch: expected=%r got=%r" % (
                expected[:160], got[:160])
        return None
    ref_norm = apply_text_whitelist(slug, route, index, sec, ref_text_norm)
    port_norm = port_text_norm
    if index == 0:
        # ⊕ R12 — the port's replacement chip/switcher text (symmetric to
        # the OLD chip text being stripped from the reference side in
        # apply_text_whitelist()). Every one of these four phrases is the
        # site's own fixed vocabulary (build_ks4.ROUTE_WORDS) and appears
        # NOWHERE else in any lesson's prose.
        for words in build_ks4.ROUTE_WORDS.values():
            port_norm = port_norm.replace(words, "")
        port_norm = port_norm.replace(THEME_CONTROL_TEXT, "")
        port_norm = _WS_RE.sub(" ", port_norm).strip()
    # The header's "Draft — not yet science-reviewed." chip tracks
    # `ks4_lessons.LESSONS[...]["review_state"]` (mount prop `showDraft`).
    # ks4_science_rulings.py landing flips reviewed lessons off draft, so
    # Design's reference (always drafted, measured before any review) and
    # the port (draft state may have just changed) can legitimately differ
    # on ONLY this chip's presence. Stripped from BOTH sides symmetrically
    # rather than gated on a specific route/lesson, since whether it's
    # present is a review-state fact this gate has no independent way to
    # assert against reference.json (which predates the whole review pass).
    ref_norm = normalize_ws(ref_norm.replace(DRAFT_BANNER_TEXT, ""))
    port_norm = normalize_ws(port_norm.replace(DRAFT_BANNER_TEXT, ""))
    # The question-bank's "N answered / N matched" tally (Ks4QuizBank) reads
    # a per-slug localStorage answer log that is written by BOTH the bank
    # AND the ladder (shared underlying question ids) and is never cleared
    # between page loads on the same origin. Design's OWN reference capture
    # (measure_design.py) drives the ladder for the SAME lesson earlier in
    # its own per-lesson flow before it measures the bank, so reference.json
    # itself already carries non-zero, session-order-dependent tallies (e.g.
    # "10 answered", "2 answered") that are an artefact of ITS measurement
    # order, not stable page content — and this gate's own multi-route sweep
    # (one shared browser/origin across a lesson's routes) is exactly as
    # order-sensitive. Comparing this counter at all compares two unrelated
    # test sessions' click histories, not the page. Stripped from both sides.
    ref_norm = _BANK_TALLY_RE.sub("", ref_norm).strip()
    port_norm = _BANK_TALLY_RE.sub("", port_norm).strip()
    if slug == "series-parallel-circuits":
        port_norm = port_norm.replace(R6_ADDITION_TEXT, "").strip()
        port_norm = _WS_RE.sub(" ", port_norm)
    ref_sq, port_sq = squash(ref_norm), squash(port_norm)
    # measure_design.measure_sections() (reused verbatim, on BOTH sides)
    # slices raw textContent at 4000 chars before it ever reaches us. The
    # port's compiled DOM has fewer inter-element whitespace characters per
    # unit of real content than Design's raw pre-compile DOM (squash()'s own
    # docstring), so on the one section long enough to actually hit that cap
    # (the ladder, ~2000+ words) the two 4000-RAW-char windows capture
    # different amounts of real content near the tail — a truncation-offset
    # artifact, not a text difference. Only the overlapping prefix is a fair
    # comparison whenever Design's raw capture hit the cap.
    if len(sec.get("text") or "") >= 3999:
        n = min(len(ref_sq), len(port_sq))
        ref_sq, port_sq = ref_sq[:n], port_sq[:n]
    if ref_sq == port_sq:
        return None
    # First index of divergence, walked on the SQUASHED forms — not the
    # spaced ones. Every whitespace-boundary compiler artifact (see
    # squash()'s docstring) is itself a spot where the SPACED forms
    # disagree; walking those directly finds that harmless spot first and
    # reports it as "the" difference even when the REAL divergence (the one
    # squash() actually detected) sits much later. Windows are re-inflated
    # with single spaces (regex-insert before capitals/digits is overkill;
    # plain readability is enough for a diagnostic message) by reporting
    # from the ORIGINAL spaced strings at the proportionally-matching
    # position instead of the raw squashed slice, which would read as one
    # illegible run-on word.
    n = min(len(ref_sq), len(port_sq))
    i = 0
    while i < n and ref_sq[i] == port_sq[i]:
        i += 1
    # map the squashed index back to an approximate position in the spaced
    # string by walking it while counting non-space characters.
    def spaced_slice_from(spaced, squashed_idx, length=80):
        count, pos = 0, 0
        for pos, ch in enumerate(spaced):
            if ch != " ":
                if count == squashed_idx:
                    break
                count += 1
        return spaced[pos:pos + length]
    return ("design=%r port=%r"
            % (spaced_slice_from(ref_norm, i), spaced_slice_from(port_norm, i)))


# ═══════════════════════════════════════════════════════════════════════
# style comparison (layer D)
# ═══════════════════════════════════════════════════════════════════════
_PX_RE = re.compile(r"(-?\d+(?:\.\d+)?)px")


def _lengths_close(a, b, tol=1.0):
    la = [float(x) for x in _PX_RE.findall(a)]
    lb = [float(x) for x in _PX_RE.findall(b)]
    if len(la) != len(lb):
        return False
    return all(abs(x - y) <= tol for x, y in zip(la, lb))


def style_value_matches(prop, a, b):
    if a == b:
        return True
    if a is None or b is None:
        return False
    if prop == "font-family":
        name = a.split(",")[0].strip().strip('"').strip("'")
        return name in b
    a_wo = _PX_RE.sub("PXPX", a)
    b_wo = _PX_RE.sub("PXPX", b)
    if a_wo != b_wo:
        return False
    return _lengths_close(a, b)


STYLE_PROPS = ["font-family", "font-size", "font-weight", "color",
               "background-color", "border", "border-radius", "padding",
               "box-shadow"]


# ═══════════════════════════════════════════════════════════════════════
# result bookkeeping
# ═══════════════════════════════════════════════════════════════════════
class Results:
    def __init__(self):
        self.rows = []  # {slug, route, width, layer, status, detail}
        self.fail_count = 0
        self.pass_count = 0

    def record(self, slug, route, width, layer, ok, detail=""):
        status = "PASS" if ok else "FAIL"
        self.rows.append(dict(slug=slug, route=route, width=width,
                               layer=layer, status=status, detail=detail))
        if ok:
            self.pass_count += 1
        else:
            self.fail_count += 1
        line = "%-4s %-28s %-4s %-6s %-12s %s" % (
            status, slug, route, width if width is not None else "-", layer, detail)
        print(line)

    def summary(self):
        return "%d PASS, %d FAIL (%d total checks)" % (
            self.pass_count, self.fail_count, self.pass_count + self.fail_count)


# ═══════════════════════════════════════════════════════════════════════
# per-page layers
# ═══════════════════════════════════════════════════════════════════════
def check_structure_and_text(R, slug, route, width, ref_widths_entry, port_sections):
    ref_sections_raw = ref_widths_entry["sections"]
    ref_sections = reference_sections_after_rulings(slug, ref_sections_raw)

    ok_struct = True
    struct_detail = []
    if len(ref_sections) != len(port_sections):
        ok_struct = False
        struct_detail.append("section count: design=%d (after rulings) port=%d"
                              % (len(ref_sections), len(port_sections)))
    R.record(slug, route, width, "A-struct", ok_struct, "; ".join(struct_detail) or "ok")

    if not ok_struct:
        return  # index-wise text compare would be meaningless

    text_fails = []
    for i, (rsec, psec) in enumerate(zip(ref_sections, port_sections)):
        if is_endmatter_section(rsec):
            continue  # R-PREVNEXT/R-CONNECTS — checked separately, not by prose
        rid = rsec.get("id")
        pid = psec.get("id")
        if rid and pid and rid != pid:
            text_fails.append("index %d: design id=%r port id=%r" % (i, rid, pid))
            continue
        ref_norm = normalize_ws(rsec.get("text", ""))
        port_norm = normalize_ws(psec.get("text", ""))
        diff = compare_section_text(slug, route, i, rsec, ref_norm, port_norm)
        if diff:
            rulings = exemption_for(slug, route, rsec)
            if rulings:
                APPLIED_EXEMPTIONS.append((slug, exemption_key(rsec), route, tuple(rulings)))
                continue
            text_fails.append("section %r (index %d): %s" % (section_key(rsec), i, diff))
    R.record(slug, route, width, "B-text", not text_fails,
              "ok" if not text_fails else " | ".join(text_fails[:3]))


def check_layout(R, slug, route, width, ref_widths_entry, port_widths_entry, have_ref):
    ov = port_widths_entry["overflow"]
    ok = not ov["overflow"]
    R.record(slug, route, width, "C-overflow", ok,
              "ok" if ok else "scrollWidth=%s innerWidth=%s offender=%s"
              % (ov["scrollWidth"], ov["innerWidth"], ov["offender"]))

    rail = port_widths_entry["rail"]
    if width >= 1340:
        ok = rail["sideVisible"] and not rail["topVisible"]
        R.record(slug, route, width, "C-rail-wide", ok,
                  "ok" if ok else "side=%s top=%s" % (rail["sideVisible"], rail["topVisible"]))
    else:
        ok = not rail["sideVisible"]
        R.record(slug, route, width, "C-rail-narrow", ok,
                  "ok" if ok else "side visible below 1340: %s" % rail["sideVisible"])
        ras = port_widths_entry.get("rail_after_scroll")
        ok2 = bool(ras and ras["topVisible"] and not rail["topVisible"])
        R.record(slug, route, width, "C-rail-scroll", ok2,
                  "ok" if ok2 else "top bar did not appear after scroll>140 "
                  "(before=%s after=%s)" % (rail["topVisible"], ras and ras["topVisible"]))

    if have_ref:
        ref_sections = reference_sections_after_rulings(slug, ref_widths_entry["sections"])
        port_sections = port_widths_entry["sections"]
        box_fails = []
        if len(ref_sections) == len(port_sections):
            for i, (rsec, psec) in enumerate(zip(ref_sections, port_sections)):
                if is_endmatter_section(rsec):
                    continue
                rb, pb = rsec["box"], psec["box"]
                if rb["h"] == 0 and pb["h"] == 0:
                    # A zero-height element is invisible in normal flow on
                    # BOTH sides — usually a `dc-import` mount host. The
                    # runtime wraps these in a `style="display:contents"`
                    # div (shared/ks4-runtime.js) so a child component's own
                    # markup isn't nested inside an extra box; a
                    # `display:contents` element generates no box of its
                    # own at all, so its measured width is 0 regardless of
                    # its (also invisible) content — not a defect, a
                    # consequence of that transparent-host design. Design's
                    # own raw pre-compile DOM had a real (if empty, 0-height)
                    # `<div>` in the same spot instead, which DOES report a
                    # width (block auto-width = the container). Comparing
                    # width here would fail on every dc-import boundary in
                    # every lesson for a difference no reader can see.
                    continue
                dh, dw = abs(rb["h"] - pb["h"]), abs(rb["w"] - pb["w"])
                # the header box legitimately shrinks (R1 removes the select
                # row and, on 3 lessons + non-active routes, R9's badge);
                # tolerate its height only, not other sections'.
                # header height shrinks from BOTH R1 (route selector gone)
                # and a reviewed lesson's draft chip going away — ~83px at
                # 1280, up to ~124px at 360/390 (the same two removed rows
                # wrap onto more lines at a narrow width, so removing them
                # saves proportionally more height there). ⊕ R12 (27 Sep
                # 2026): the two short static chips are ALSO gone now,
                # replaced by one longer "Combined Science · Higher tier"
                # chip, which wraps onto a different number of lines than
                # the two short ones did at 390/360 — measured up to 164px
                # of DELTA on top of the above (chemical-bonds, ionic-
                # compounds, etc., TH route, 390/360 widths). 180 covers the
                # measured range (max seen: 164) with the same margin-not-
                # hiding-a-real-break intent the original 150 had.
                text_differs = (squash(normalize_ws(rsec.get("text", "")))
                                != squash(normalize_ws(psec.get("text", ""))))
                if i == 0:
                    h_tol = 180
                elif text_differs:
                    # The RAW text (before any whitelist substitution) is
                    # not identical — for ANY reason, whether B-text's
                    # whitelist can explain it (most often: a
                    # ks4_science_rulings.py row's `old`/`new` pair matched,
                    # meaning content GENUINELY got longer or shorter) or
                    # not (a logic-level ruling — 71 of the 101 rows change
                    # JS priority/behaviour rather than a literal string, so
                    # a changed word count with no matching `old`->`new`
                    # pair is expected too, per this file's own docstring on
                    # `science_rulings_for()`). Either way, a changed word
                    # count legitimately changes wrap height BY ANY AMOUNT —
                    # unbounded on purpose: this branch only ever fires once
                    # the content difference is independently established,
                    # so it can never hide a genuine layout collapse (an
                    # empty card, a missing figure) — THAT would show with
                    # the text UNCHANGED, which takes the strict branch
                    # below. B-text is the check that still gates whether
                    # the content difference itself is legitimate.
                    continue
                else:
                    h_tol = 2
                if dh > h_tol or dw > 1:
                    box_fails.append("section %r (index %d): dh=%d dw=%d"
                                      % (section_key(rsec), i, dh, dw))
        R.record(slug, route, width, "C-box", not box_fails,
                  "ok" if not box_fails else " | ".join(box_fails[:3]))

        rn, pn = ref_widths_entry["rail"], port_widths_entry["rail"]
        rn_labels = [squash(x) for x in rn["sideNodes"]]
        pn_labels = [squash(x) for x in pn["sideNodes"]]
        ok = (rn["sideNodeCount"] == pn["sideNodeCount"] and rn_labels == pn_labels)
        R.record(slug, route, width, "C-rail-labels", ok,
                  "ok" if ok else "design=%r port=%r" % (rn["sideNodes"], pn["sideNodes"]))

        rl, pl = ref_widths_entry.get("ladder"), port_widths_entry.get("ladder")
        if rl and pl:
            ok = rl["rungCount"] == pl["rungCount"] and rl["hasCommandWords"] == pl["hasCommandWords"]
            R.record(slug, route, width, "C-ladder", ok,
                      "ok" if ok else "design=%s port=%s" % (rl, pl))


def check_console(R, slug, route, width, page):
    errs = [e for e in page.console_errors()
            if "favicon.ico" not in e and BACKEND_HOST not in e]
    R.record(slug, route, width, "H-console", not errs,
              "ok" if not errs else "; ".join(errs[:3]))


def check_keyboard(R, slug, route, page):
    js = """
    (function(){
      var sel = 'a[href], button:not([disabled]), select, textarea, input, [tabindex]';
      var els = Array.from(document.querySelectorAll(sel)).filter(function(el){
        // the shared tutor chat overlay (build_ks3.KS3_CHAT_OVERLAY, reused
        // verbatim by build_ks4.tutor_block() on every one of these 54
        // pages, unmodified) marks itself `inert` while closed
        // (`id="chatOverlay" inert data-inert-when-closed`) — inert
        // correctly removes its whole subtree from the focus order until a
        // real click opens it, which genuinely toggles `inert` off. That
        // is not a port defect, and driving it open is out of this pilot's
        // scope (it is site-wide, pre-existing, and unowned by the pilot).
        if (el.closest('[inert]')) { return false; }
        // ⊕ Stage B (phone run, 28 Sep 2026) — the content of a CLOSED
        // <details> is the same case as `inert` above: Chrome lays it out
        // (content-visibility:hidden keeps its box) but it cannot take focus
        // until its <summary> opens it, and the summary itself stays in this
        // list and is asserted reachable. The one top bar's compact theme
        // control is such a menu (its three popup radios). An element whose
        // OWN summary is the thing being tested is not exempt: only the
        // details' content below the summary is.
        var d = el.closest('details:not([open])');
        if (d && !el.closest('summary')) { return false; }
        var r = el.getBoundingClientRect();
        return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden';
      });
      var unreachable = [];
      var noName = [];
      els.forEach(function(el){
        try { el.focus(); } catch (e) {}
        if (document.activeElement !== el) {
          unreachable.push(el.tagName + (el.id ? '#' + el.id : ''));
        }
        var name = (el.getAttribute('aria-label') || '') || (el.textContent || '').trim()
          || el.getAttribute('title') || el.getAttribute('placeholder')
          || (el.tagName === 'INPUT' && el.value) || '';
        if (!name) {
          var labelled = el.id && document.querySelector('label[for="' + el.id + '"]');
          if (!labelled) { noName.push(el.tagName + (el.id ? '#' + el.id : '') + '.' + (el.className||'')); }
        }
      });
      return {count: els.length, unreachable: unreachable, noName: noName};
    })();
    """
    try:
        res = page.eval(js)
    except Exception as e:
        R.record(slug, route, 1280, "G-keyboard", False, "eval failed: %s" % e)
        return
    ok = not res["unreachable"] and not res["noName"]
    detail = "count=%d" % res["count"]
    if res["unreachable"]:
        detail += "; unreachable=%s" % res["unreachable"][:5]
    if res["noName"]:
        detail += "; no-accessible-name=%s" % res["noName"][:5]
    R.record(slug, route, 1280, "G-keyboard", ok, detail)


def _route_switch_probe(page):
    """The Enter/Space-open, Esc-close, focus-return sequence against
    whatever `.ks3-route-switch` is on the currently loaded page. Shared by
    `check_route_switch_keyboard()` (light, once per page, the original
    R12 gate) and `check_theme()`'s (e) (both themes, THEME_SAMPLE_SLUGS
    only)."""
    js = """
    (function(){
      var d = document.querySelector('.ks3-route-switch');
      if (!d) { return {error: 'no .ks3-route-switch found'}; }
      var summary = d.querySelector('summary');
      if (!summary) { return {error: 'no <summary> found'}; }
      var before = {open: d.open, aria: summary.getAttribute('aria-expanded')};
      summary.focus();
      summary.click();
      var afterOpen = {open: d.open, aria: summary.getAttribute('aria-expanded')};
      document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Escape', bubbles: true}));
      var afterEsc = {open: d.open, aria: summary.getAttribute('aria-expanded'),
                       focusReturned: document.activeElement === summary};
      return {before: before, afterOpen: afterOpen, afterEsc: afterEsc};
    })();
    """
    try:
        return page.eval(js)
    except Exception as e:
        return {"error": "eval failed: %s" % e}


def _route_switch_ok(res):
    if res.get("error"):
        return False
    return (res["before"]["open"] is False and res["before"]["aria"] == "false"
            and res["afterOpen"]["open"] is True and res["afterOpen"]["aria"] == "true"
            and res["afterEsc"]["open"] is False and res["afterEsc"]["aria"] == "false"
            and res["afterEsc"]["focusReturned"])


def check_route_switch_keyboard(R, slug, route, page):
    """R12: the header route switcher opens/closes by keyboard alone —
    Enter/Space on the chip (native <details>/<summary>, so a plain
    `.click()` on the summary proves the same activation a real Enter/
    Space keypress triggers per the HTML spec), Esc closes it and returns
    focus to the chip, and aria-expanded tracks the open state throughout —
    the one R12 assertion that genuinely needs a real browser (ks4_pilot_
    check.py proves the chip/menu/links exist and are correct; this proves
    they OPERATE)."""
    res = _route_switch_probe(page)
    if res.get("error"):
        R.record(slug, route, 1280, "G-route-switch", False, res["error"])
        return
    ok = _route_switch_ok(res)
    R.record(slug, route, 1280, "G-route-switch", ok, "ok" if ok else repr(res))


# ═══════════════════════════════════════════════════════════════════════
# THEME (Mide's ruling, 26 Sep 2026; THEME-CONTRACT.md item 4) — the site-
# wide Light/Dark/System control. theme_wiring_check.py already proves
# THEME_HEAD/theme.js/the slot are present on every one of the 54 pages
# byte-identically; what is left to prove here is BEHAVIOUR, which is a
# property of the shared control (shared/theme.js) and this family's own
# markup around it, not of any one lesson's content — so this runs on a
# SAMPLE chosen to between them cover all four routes (chemical-bonds and
# resistors carry all four; nanoparticles is TF/TH-only, the one lesson
# whose route switcher menu has just ONE other entry rather than three),
# at both 1280 and 360.
# ═══════════════════════════════════════════════════════════════════════
THEME_SAMPLE_SLUGS = ["chemical-bonds", "resistors", "nanoparticles", "polymers"]
THEME_WIDTHS = [1280, 360]


def _cdp_key(page, key, code, vk):
    """A REAL keypress via CDP's Input domain, not a synthetic DOM event —
    load-bearing here specifically: a native <input type=radio> group's
    arrow-key behaviour (move selection, fire 'change') is implemented by
    the browser itself and is never invoked by `dispatchEvent(new
    KeyboardEvent(...))` from page script, only by an actual input event
    reaching Chrome's own input pipeline."""
    for t in ("rawKeyDown", "keyUp"):
        page.send("Input.dispatchKeyEvent", {
            "type": t, "key": key, "code": code,
            "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk,
        })


def check_theme(R, slug, route, url):
    """(a) exactly one theme control in the header, keyboard-operable (Tab
    reaches it, arrow keys change the theme, a visible focus ring); (b)
    light is the default with no stored choice, even under emulated OS
    dark; (c) choosing Dark persists across reload and across navigation to
    another pilot page (via the R12 route switcher), and System follows
    emulated media live; (d) no flash — THEME_HEAD precedes every
    stylesheet in the served bytes, and data-theme is already correct at
    DOMContentLoaded; (e) the route switcher still opens/closes correctly
    in both themes; (f) zero console errors."""
    for w in THEME_WIDTHS:
        # (d, static half) — no browser needed: read the SERVED bytes
        # directly and confirm THEME_HEAD precedes the first stylesheet.
        try:
            raw = urllib.request.urlopen(url, timeout=10).read().decode("utf-8", "replace")
        except Exception as e:
            R.record(slug, route, w, "THEME-d-head-order", False, "fetch failed: %s" % e)
            raw = ""
        head_end = raw.lower().find("</head>")
        head = raw[: head_end if head_end >= 0 else len(raw)]
        i_theme = head.find(THEME_HEAD)
        m_style = re.search(r"<link[^>]+rel=[\"']?stylesheet", head, re.I)
        i_style = m_style.start() if m_style else None
        d1_ok = i_theme >= 0 and (i_style is None or i_theme < i_style)
        R.record(slug, route, w, "THEME-d-head-order", d1_ok,
                  "ok" if d1_ok else "THEME_HEAD at %r, first stylesheet at %r"
                  % (i_theme, i_style))

        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(w, 1000)

            # a paint-independent record of data-theme at DOMContentLoaded,
            # from a script that runs on EVERY subsequent navigation in this
            # page/tab (Page.addScriptToEvaluateOnNewDocument), so the flash
            # check below reads what the page itself saw, not what settled
            # after this test's own JS ran.
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": (
                "window.__mrbThemeAtDCL=null;"
                "document.addEventListener('DOMContentLoaded',function(){"
                "window.__mrbThemeAtDCL=document.documentElement.getAttribute('data-theme');"
                "});")})

            # (b) light default, no stored choice, OS dark emulated — no
            # stored choice is guaranteed here for free: cdp.Browser() gives
            # every check_theme() width iteration a brand-new, empty
            # profile directory (ks3_browser.py), so localStorage has never
            # held 'mrb-theme' at this point.
            # ⊕ 9 Oct 2026: briefly THEME-b-system-default (48f2dd4d0); restored
            # to Light on Mide's ruling — an OS-dark fresh device opens Light.
            MD.set_media(page, scheme="dark")
            page.goto(url, settle=0.8)
            MD.wait_mounted(page)
            theme_b = page.eval("document.documentElement.getAttribute('data-theme')")
            dcl_theme = page.eval("window.__mrbThemeAtDCL")
            ok_b = theme_b == "light" and dcl_theme == "light"
            R.record(slug, route, w, "THEME-b-light-default", ok_b,
                      "data-theme=%r at-DOMContentLoaded=%r (expected light, "
                      "no stored choice, OS dark)" % (theme_b, dcl_theme))

            # (a) exactly one control; reachable; arrow keys change it (a
            # REAL keypress, see _cdp_key); a visible focus ring
            # ⊕ Stage B (phone run, 28 Sep 2026) — the header is the ONE
            # pupil top bar, whose slot is theme.js's `compact` variant (the
            # class page's): at ≥600px one inline radio group; below 600px a
            # single 32px button that opens the SAME group. A compact slot
            # therefore holds TWO `.mrb-theme` fieldsets in the DOM (inline +
            # popup) and exactly one is ever RENDERED. The count is of
            # rendered controls — still exactly one — and on a phone the
            # button is pressed first, so the arrow-key and focus-ring
            # assertions below run on the control a pupil actually uses.
            page.eval(
                "(function(){var s=document.querySelector('.mrb-theme-menu > summary');"
                "if(s&&s.getClientRects().length&&!s.parentNode.open){s.click();}})();")
            time.sleep(0.1)
            n_controls = page.eval(
                "[].filter.call(document.querySelectorAll('.mrb-theme'),"
                "function(f){return f.getClientRects().length>0;}).length")
            n_slots = page.eval("document.querySelectorAll('[data-mrb-theme]').length")
            if n_slots != 1:
                n_controls = "%s (in %s slots)" % (n_controls, n_slots)
            page.eval(
                "(function(){var gs=[].filter.call(document.querySelectorAll('.mrb-theme'),"
                "function(f){return f.getClientRects().length>0;});var g=gs[0];"
                "var el=g&&(g.querySelector('input:checked')||g.querySelector('input'));"
                "if(el)el.focus();})();")
            reached = page.eval(
                "!!(document.activeElement && document.activeElement.closest "
                "&& document.activeElement.closest('.mrb-theme'))")
            pref_before = page.eval("document.documentElement.getAttribute('data-theme-pref')")
            _cdp_key(page, "ArrowRight", "ArrowRight", 39)
            time.sleep(0.15)
            pref_after = page.eval("document.documentElement.getAttribute('data-theme-pref')")
            arrow_ok = pref_after != pref_before
            ring = page.eval(
                "(function(){var l=document.activeElement&&document.activeElement.closest"
                "('label');if(!l)return null;var cs=getComputedStyle(l);"
                "return cs.outlineStyle+':'+cs.outlineWidth;})();")
            ring_ok = bool(ring) and ring not in ("none:0px", "none:0")
            ok_a = (n_controls == 1) and reached and arrow_ok and ring_ok
            R.record(slug, route, w, "THEME-a-control", ok_a,
                      "controls=%s reached=%s arrow(%r->%r) ring=%r"
                      % (n_controls, reached, pref_before, pref_after, ring))

            # (c) choosing Dark persists across reload
            page.eval("window.MRBTheme && window.MRBTheme.set('dark')")
            time.sleep(0.1)
            page.goto(url, settle=0.8)
            MD.wait_mounted(page)
            theme_reload = page.eval("document.documentElement.getAttribute('data-theme')")
            ok_c1 = theme_reload == "dark"
            R.record(slug, route, w, "THEME-c-persist-reload", ok_c1,
                      "data-theme=%r after reload (expected dark)" % theme_reload)

            # (c) and across navigation to ANOTHER pilot page, via the R12
            # route switcher's own link (a real click-driven navigation).
            other_href = page.eval(
                "(function(){var a=document.querySelector('.ks3-route-menu a');"
                "return a?a.getAttribute('href'):null;})();")
            if other_href:
                page.eval(
                    "(function(){var d=document.querySelector('.ks3-route-switch');"
                    "var s=d&&d.querySelector('summary');if(s)s.click();"
                    "var a=document.querySelector('.ks3-route-menu a');if(a)a.click();})();")
                time.sleep(1.0)
                MD.wait_mounted(page)
                theme_nav = page.eval("document.documentElement.getAttribute('data-theme')")
                landed = page.eval("location.pathname")
                ok_c2 = (theme_nav == "dark" and landed == other_href)
                detail_c2 = ("data-theme=%r landed=%r (expected dark, %r)"
                              % (theme_nav, landed, other_href))
            else:
                ok_c2, detail_c2 = True, "no other route on this lesson to navigate to"
            R.record(slug, route, w, "THEME-c-persist-nav", ok_c2, detail_c2)

            # back on the original url for the rest of this width's checks
            page.goto(url, settle=0.8)
            MD.wait_mounted(page)

            # (c) System follows emulated media live
            page.eval("window.MRBTheme && window.MRBTheme.set('system')")
            MD.set_media(page, scheme="light")
            time.sleep(0.2)
            sys_light = page.eval("document.documentElement.getAttribute('data-theme')")
            MD.set_media(page, scheme="dark")
            time.sleep(0.2)
            sys_dark = page.eval("document.documentElement.getAttribute('data-theme')")
            ok_sys = sys_light == "light" and sys_dark == "dark"
            R.record(slug, route, w, "THEME-c-system-live", ok_sys,
                      "system under OS-light=%r, under OS-dark=%r" % (sys_light, sys_dark))

            # (e) the route switcher still works, in both themes
            for scheme_name in ("light", "dark"):
                page.eval("window.MRBTheme && window.MRBTheme.set('%s')" % scheme_name)
                MD.set_media(page, scheme=scheme_name)
                time.sleep(0.15)
                res = _route_switch_probe(page)
                ok_e = _route_switch_ok(res)
                R.record(slug, route, w, "THEME-e-switch-%s" % scheme_name, ok_e,
                          "ok" if ok_e else repr(res))

            # (f) zero console errors, across everything this check did
            errs = [e for e in page.console_errors()
                    if "favicon.ico" not in e and BACKEND_HOST not in e]
            R.record(slug, route, w, "THEME-f-console", not errs,
                      "ok" if not errs else "; ".join(errs[:3]))

            # tidy back to light — courtesy only (this Browser() closes at
            # the end of this `with`), so a screenshot taken right after
            # this gate is never mistaken for showing an unintended default.
            page.eval("try{window.MRBTheme && window.MRBTheme.set('light')}catch(e){}")
            MD.set_media(page, scheme="light")


# ⊕ R12 — `STYLE_TARGETS["badge_pill"]` is a GENERIC probe (`[style*=
# 'border-radius: 99px']`, `measure_design.py`), not a probe for any one
# named element — when reference.json was captured it happened to match
# Design's static header chips (removed by R12; the new route chip is
# styled by a STYLESHEET class, not an inline style, so the selector no
# longer finds it). On a lesson that carries a LATER inline-styled pill
# (an R9 "Contains …" badge, a "Required practical" badge, the R6 "Not on
# the sheet" chip) the same query now matches THAT element instead — an
# apples-to-oranges comparison against Design's chip, forever, by
# construction, regardless of anything this port could style. Exempting
# the comparison, not the floor: only this ONE named component is skipped;
# every other STYLE_TARGETS entry on the same page still compares and
# still gates.
D_STYLES_EXEMPT_COMPONENTS = {"badge_pill"}


def check_styles(R, slug, page, ref_entry):
    # ⊕ THEME RUN (26 Sep 2026, THEME-CONTRACT.md item 4) — the "dark"
    # comparison used to force `prefers-color-scheme: dark` via CDP media
    # emulation, which worked because the port's own dark tokens fired from
    # that same OS setting. Since dark is now keyed on html[data-theme=
    # "dark"] ONLY (THEME-CONTRACT.md rule 3), emulated OS dark no longer
    # darkens the page on its own — this must drive the SITE'S OWN theme
    # control instead, while still comparing against the SAME Design dark
    # reference (reference.json is untouched; only how the PORT side is put
    # into dark mode changes).
    for scheme, ref_key in (("light", "styles_light"), ("dark", "styles_dark")):
        if scheme == "dark":
            page.eval("window.MRBTheme && window.MRBTheme.set('dark')")
        else:
            page.eval("window.MRBTheme && window.MRBTheme.set('light')")
            MD.set_media(page, scheme=scheme)
        time.sleep(0.3)
        ref_styles = ref_entry.get(ref_key) or {}
        fails = []
        for comp, sel in MD.STYLE_TARGETS.items():
            if comp in D_STYLES_EXEMPT_COMPONENTS:
                continue
            ref_cs = ref_styles.get(comp)
            if ref_cs is None:
                continue
            if comp == "check_button" and slug in R18_SLUGS:
                # ⊕ R18 — `sel` is a bare "button": on Design's page the first
                # button was her hook's Ks4Choice option. R18 replaced that hook
                # with Ks4Guess's cards (Design's own batch-4 styling), so measure
                # the same element kind Design's reference did: the first
                # Ks4Choice option button, which every pilot lesson still has.
                sel = "button.ks3-option"
            port_cs = MD.cs(page, sel)
            if port_cs is None:
                fails.append("%s: port element missing (%s)" % (comp, sel))
                continue
            for prop in STYLE_PROPS:
                if not style_value_matches(prop, ref_cs.get(prop), port_cs.get(prop)):
                    fails.append("%s.%s: design=%r port=%r"
                                  % (comp, prop, ref_cs.get(prop), port_cs.get(prop)))
        R.record(slug, DEEP_ROUTE, 1280, "D-styles-%s" % scheme, not fails,
                  "ok" if not fails else " | ".join(fails[:5]))
    page.eval("window.MRBTheme && window.MRBTheme.set('light')")
    MD.set_media(page, scheme="light")


def check_reduced_motion(R, slug, url):
    """Mirrors measure_design.main()'s own reduced-motion proof: commit the
    hook under normal motion, read the reveal's animation-name; reload,
    force reduced motion, commit again, read it again. Also checks that NO
    [data-arrive] element anywhere on the page is left mid-animation once
    reduced motion is forced (broader than the single-element proof)."""
    with cdp.Browser() as b:
        page = b.attach()
        page.set_viewport(1280, 1000)
        page.goto(url, settle=0.8)
        MD.set_media(page, scheme="light")
        MD.wait_mounted(page)
        page.eval("(function(){var el=document.querySelector('#s-hook button');"
                  "if(el){el.scrollIntoView();el.click();}})()")
        time.sleep(0.5)
        anim_normal = page.eval(
            "(()=>{const e=document.querySelector('#s-hook [data-arrive]'); "
            "return e?getComputedStyle(e).animationName:null;})()")

        page.goto(url, settle=0.8)
        MD.set_media(page, scheme="light", motion="reduce")
        MD.wait_mounted(page)
        page.eval("(function(){var el=document.querySelector('#s-hook button');"
                  "if(el){el.scrollIntoView();el.click();}})()")
        time.sleep(0.5)
        anim_reduced = page.eval(
            "(()=>{const e=document.querySelector('#s-hook [data-arrive]'); "
            "return e?getComputedStyle(e).animationName:null;})()")
        running = page.eval(
            "Array.from(document.querySelectorAll('[data-arrive]')).filter(function(e){"
            "var s = getComputedStyle(e); return s.animationPlayState === 'running' && "
            "s.animationName !== 'none';}).length")
    ok = (anim_reduced == "none") and (anim_normal not in (None, "none")) and running == 0
    R.record(slug, DEEP_ROUTE, 1280, "F-reduced-motion", ok,
              "ok" if ok else "normal=%r reduced=%r stillRunning=%s"
              % (anim_normal, anim_reduced, running))


def check_interactions(R, slug, url, ref_entry):
    with cdp.Browser() as b:
        page = b.attach()
        page.goto(url, settle=0.8)
        MD.set_media(page, scheme="light")
        MD.wait_mounted(page)
        page.eval(MD.JS_HELPERS)
        got = MD.measure_interactions(page, 1280)

        # ── best-score persistence: MECHANISM proof, not a live full-score
        # drive. `Ks4Ladder.dc.html`'s `componentDidUpdate` only calls
        # `KS4.save('ks4-best-'+slug, n)` once ALL FOUR rungs are resolved
        # (`score().done`), including rung 4 (Ks4Write, self-marked against
        # a revealed mark scheme) and rung 2's kind-specific grading
        # (calc/text/data, different per lesson). Faithfully automating
        # "answer all 4 rungs, including typing >= the mark-scheme's
        # unlock-word count and clicking the self-mark buttons" per lesson
        # is exactly the gap measure_design.py's own README documents as
        # NOT reliably measurable for the Write rung's unlock (§"Known
        # measurement limitations"). Rather than a live drive that would be
        # exactly as unreliable here, this checks that the save call itself
        # SHIPPED, verbatim, in this page's own compiled block script — the
        # same static assertion `ks4_rulings.check_r4_storage_key()` makes
        # against Design's source, run here against the PORTED page.
        has_mechanism = page.eval(
            "Array.from(document.scripts).some(function(s){"
            "return (s.textContent||'').indexOf("
            "\"'ks4-best-' + (this.props.slug\") !== -1;})")
    ref = ref_entry.get("interactions") or {}
    bool_keys = ["hook_option_clicked", "misconception_option_clicked",
                 "ladder_rung_clicked", "keynote_toggle_clicked"]
    fails = []
    for k in bool_keys:
        if k in ref and bool(ref[k]) and not got.get(k):
            fails.append("%s: design=%r port=%r" % (k, ref[k], got.get(k)))
    if ref.get("sort_button_count") and got.get("sort_button_count") != ref.get("sort_button_count"):
        fails.append("sort_button_count: design=%r port=%r"
                      % (ref.get("sort_button_count"), got.get("sort_button_count")))
    R.record(slug, DEEP_ROUTE, 1280, "E-interactions", not fails,
              "ok" if not fails else " | ".join(fails[:5]))
    R.record(slug, DEEP_ROUTE, 1280, "E-best-score-mechanism", bool(has_mechanism),
              "ok (KS4.save call present)" if has_mechanism
              else "the ks4-best-<slug> save call is missing from this page's "
                   "compiled Ks4Ladder script — LIVE full-ladder scoring and "
                   "reload persistence not separately drilled here (see "
                   "docstring: same documented gap as measure_design.py's "
                   "Write-rung limitation)")


def check_prev_next(R, slug, route, url, lesson, data):
    prev, nxt = build_ks4.compute_prev_next(data, lesson, route)
    with cdp.Browser() as b:
        page = b.attach()
        page.set_viewport(1280, 1000)
        page.goto(url, settle=0.8)
        MD.wait_mounted(page)
        got = page.eval(
            "(function(){var sec=document.querySelector('.ks3-endmatter section');"
            "if(!sec) return [];"
            "return Array.from(sec.querySelectorAll('a')).map(function(a){"
            "return {href:a.getAttribute('href'), text:(a.textContent||'').trim()};});})();")
        connects = page.eval(
            "(function(){var secs=document.querySelectorAll('.ks3-endmatter section');"
            "if(secs.length<2) return [];"
            "return Array.from(secs[1].querySelectorAll('a')).map(function(a){"
            "return a.getAttribute('href');});})();")

    expected = []
    if prev:
        expected.append(prev["href"])
    if nxt:
        expected.append(nxt["href"])
    got_hrefs = [g["href"] for g in (got or [])]
    ok = got_hrefs == expected
    R.record(slug, route, 1280, "B-prevnext", ok,
              "ok" if ok else "expected(from all_subtopics)=%r port=%r" % (expected, got_hrefs))

    bad_connects = [c for c in (connects or [])
                    if not c or c.endswith(".dc.html") or c == "#"
                    or not os.path.exists(os.path.join(REPO_ROOT, c.lstrip("/")))]
    R.record(slug, route, 1280, "B-connects", not bad_connects,
              "ok" if not bad_connects else "bad hrefs: %s" % bad_connects)


# ═══════════════════════════════════════════════════════════════════════
# the sweep
# ═══════════════════════════════════════════════════════════════════════
def measure_port_widths(page, url, widths):
    page.goto(url, settle=0.8)
    MD.set_media(page, scheme="light")
    MD.wait_mounted(page)
    page.eval(MD.JS_HELPERS)
    out = {}
    for w in widths:
        page.set_viewport(w, 1000)
        time.sleep(0.5)
        rail_top = MD.measure_sections(page), MD.measure_overflow(page)
        entry = {
            "sections": rail_top[0],
            "overflow": rail_top[1],
            "rail": MD.measure_rail(page),
            "rail_after_scroll": MD.measure_rail_scrolled(page) if w < 1340 else None,
            "ladder": MD.measure_ladder(page),
            "focusables": MD.measure_focusables(page) if w == 1280 else None,
        }
        out[str(w)] = entry
    return out


def run(only_slug=None, only_width=None):
    reference = json.load(open(REFERENCE_PATH, encoding="utf-8"))
    R = Results()

    lessons = ks4_lessons.LESSONS
    if only_slug:
        lessons = [L for L in lessons if L["slug"] == only_slug]
        if not lessons:
            raise SystemExit("ks4_parity: no lesson %r" % only_slug)
    widths = [only_width] if only_width else WIDTHS

    data = build_ks4.load_subtopics_by_route()

    server, port = cdp.serve(REPO_ROOT)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for lesson in lessons:
                slug = lesson["slug"]
                ref_entry = reference["lessons"].get(slug)
                if ref_entry is None:
                    R.record(slug, "-", None, "A-struct", False,
                              "no reference.json entry for this slug")
                    continue

                for route in lesson["routes"]:
                    is_deep = (route == DEEP_ROUTE)
                    route_widths = widths if is_deep else [w for w in widths if w == 1280]
                    if not route_widths:
                        continue
                    url_path = ks4_lessons.site_url(slug, route)
                    url = "http://127.0.0.1:%d%s" % (port, url_path)
                    ref_route_widths = (ref_entry["routes"].get(ROUTE_LABEL[route], {})
                                        .get("widths", {}))

                    port_widths = measure_port_widths(page, url, route_widths)

                    for w in route_widths:
                        ref_w = ref_route_widths.get(str(w))
                        have_ref = ref_w is not None
                        port_w = port_widths[str(w)]
                        if have_ref:
                            check_structure_and_text(R, slug, route, w, ref_w, port_w["sections"])
                        check_layout(R, slug, route, w, ref_w, port_w, have_ref)
                        check_console(R, slug, route, w, page)

                    check_keyboard(R, slug, route, page)
                    check_route_switch_keyboard(R, slug, route, page)
                    check_prev_next(R, slug, route, url, lesson, data)

                    if slug in THEME_SAMPLE_SLUGS and (not only_width or only_width in THEME_WIDTHS):
                        # check_theme opens its OWN cdp.Browser() session(s)
                        # per width (it needs Page.addScriptToEvaluateOn
                        # NewDocument wired before goto(), and repeated
                        # reloads/navigations) — independent of the `page`
                        # this loop otherwise shares across checks.
                        check_theme(R, slug, route, url)

                if not only_width or only_width == 1280:
                    th_url = "http://127.0.0.1:%d%s" % (port, ks4_lessons.site_url(slug, DEEP_ROUTE))
                    page.goto(th_url, settle=0.8)
                    MD.set_media(page, scheme="light")
                    MD.wait_mounted(page)
                    page.set_viewport(1280, 1000)
                    time.sleep(0.3)
                    page.eval(MD.JS_HELPERS)
                    check_styles(R, slug, page, ref_entry)
                    check_reduced_motion(R, slug, th_url)
                    check_interactions(R, slug, th_url, ref_entry)
    finally:
        server.shutdown()

    return R


# ═══════════════════════════════════════════════════════════════════════
# BATCH ENGINE (1 Oct 2026, docs/ks4/batch-engine.md) — `--batch <name>`
# for anything OTHER than the pilot. There is no Design reference page for
# an authored lesson, so this is NOT `run()` with a different lesson list —
# it is a separate, simpler sweep: zero console errors, no horizontal
# scroll, every block/section type registered, the prerendered text is
# present without JS, a `data-route`-tagged element renders ONLY on its
# routes with its badge, and every interactive control is keyboard-
# reachable. `run()` above, and everything it calls, is untouched — this
# function shares only the genuinely generic helpers (`Results`,
# `check_console`, `check_keyboard`, `measure_design`'s media/overflow/
# mounted helpers), never `reference.json` or the rulings whitelist.
# ═══════════════════════════════════════════════════════════════════════
BATCH_WIDTHS = [1280, 820, 390]
_ROUTE_BADGE_RE = re.compile(r'data-route-badge="([a-z-]+)"')


def _route_layer_expected(kind, route):
    is_higher, is_triple = ROUTE_FLAGS[route]
    if kind == "higher":
        return is_higher
    if kind == "triple":
        return is_triple
    if kind == "triple-higher":
        return is_higher and is_triple
    return None


def check_batch_no_react(R, slug, route, page):
    bad = ["unpkg.com", "React.", "ReactDOM", "Babel", "support.js",
           "createElement(", "dangerouslySetInnerHTML"]
    html = page.eval("document.documentElement.outerHTML")
    hits = [b for b in bad if b in html]
    R.record(slug, route, 1280, "no-react", not hits,
              "ok" if not hits else "found %s" % hits)


def check_batch_overflow(R, slug, route, width, page):
    o = MD.measure_overflow(page)
    R.record(slug, route, width, "no-h-scroll", not o["overflow"],
              "ok" if not o["overflow"] else "scrollWidth=%d innerWidth=%d offender=%s"
              % (o["scrollWidth"], o["innerWidth"], o["offender"]))


def check_batch_prerendered_text(R, slug, route, raw_html):
    """The page carries its text WITHOUT JS — read straight from the file
    on disk (no browser, no script execution), the same property
    `ks4_pilot_check.py` proves for the pilot by a different route (its
    freeze mechanism). A bare, un-prerendered page would show an empty
    `<div id="ks4-mount"></div>`."""
    start = raw_html.find('<div id="ks4-mount">')
    ok = start != -1 and not raw_html[start:start + 400].startswith(
        '<div id="ks4-mount"></div>')
    R.record(slug, route, None, "prerendered-text", ok,
              "ok" if ok else "ks4-mount is empty in the raw, un-executed HTML")


def check_batch_route_layers(R, slug, route, raw_html, lesson_kinds):
    """Every `data-route-badge="<kind>"` found anywhere in the page's RAW,
    un-executed HTML (the prerendered bake — see `check_batch_prerendered_
    text`) must be a kind that genuinely applies to this route, and every
    kind this LESSON uses anywhere (`lesson_kinds`, the union across all
    its routes — not every registered kind; a lesson is not required to
    use all three) must appear on a route where it should. A false
    positive (badge present on a route it should not be) or a false
    negative (badge absent on a route it should apply to) is each its own
    FAIL."""
    found = set(_ROUTE_BADGE_RE.findall(raw_html))
    problems = []
    for kind in found:
        if kind not in ROUTE_LAYER_EXPR_BATCH:
            problems.append("unknown data-route kind %r" % kind)
            continue
        if not _route_layer_expected(kind, route):
            problems.append("%r badge present but should not apply on %s" % (kind, route))
    for kind in lesson_kinds:
        if _route_layer_expected(kind, route) and kind not in found:
            problems.append("%r badge missing but should apply on %s" % (kind, route))
    R.record(slug, route, None, "route-layers", not problems, "; ".join(problems) or "ok")


ROUTE_LAYER_EXPR_BATCH = {"higher", "triple", "triple-higher"}


def check_batch_registry(R, slug, route, raw_html):
    import ks4_pilot_check as KPC
    problems = []
    for m in KPC._DCIMPORT_RE.finditer(raw_html):
        if m.group(1) not in ks4_blocks.COMPONENTS:
            problems.append("unregistered dc-import %r" % m.group(1))
    for m in KPC._DATABLOCK_RE.finditer(raw_html):
        if m.group(1) not in ks4_blocks.SECTION_TYPES:
            problems.append("unregistered data-block %r" % m.group(1))
    R.record(slug, route, None, "registry", not problems, "; ".join(problems) or "ok")


def run_batch(name, only_slug=None):
    if name == "pilot":
        raise SystemExit("ks4_parity --batch pilot: use no flag, or omit "
                          "--batch entirely — the pilot keeps its own run().")
    if name not in ks4_lessons.batch_names():
        raise SystemExit("ks4_parity --batch %r is not registered. Known "
                          "batches: %s" % (name, ", ".join(ks4_lessons.batch_names())))
    lessons = ks4_lessons.lessons_for_batch(name)
    if only_slug:
        lessons = [L for L in lessons if L["slug"] == only_slug]
    manifest_path = build_ks4.batch_manifest_path(name)
    if not os.path.exists(manifest_path):
        raise SystemExit("ks4_parity --batch %s: %s does not exist — run "
                          "`python3 build_ks4.py --batch %s` first."
                          % (name, manifest_path, name))

    R = Results()
    server, port = cdp.serve(REPO_ROOT)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for lesson in lessons:
                slug = lesson["slug"]
                raw_by_route = {}
                for route in lesson["routes"]:
                    url_path = ks4_lessons.site_url(slug, route)
                    out_path = os.path.join(build_ks4.OUT_ROOT, url_path.lstrip("/"))
                    if os.path.exists(out_path):
                        raw_by_route[route] = open(out_path, encoding="utf-8").read()
                lesson_kinds = set()
                for html in raw_by_route.values():
                    lesson_kinds |= set(_ROUTE_BADGE_RE.findall(html))

                for route in lesson["routes"]:
                    url_path = ks4_lessons.site_url(slug, route)
                    out_path = os.path.join(build_ks4.OUT_ROOT, url_path.lstrip("/"))
                    if route not in raw_by_route:
                        R.record(slug, route, None, "exists", False, "%s missing" % out_path)
                        continue
                    raw_html = raw_by_route[route]
                    check_batch_prerendered_text(R, slug, route, raw_html)
                    check_batch_route_layers(R, slug, route, raw_html, lesson_kinds)
                    check_batch_registry(R, slug, route, raw_html)

                    url = "http://127.0.0.1:%d%s" % (port, url_path)
                    for theme in ("light", "dark"):
                        page.goto(url, settle=0.8)
                        MD.set_media(page, scheme=theme)
                        if not MD.wait_mounted(page):
                            R.record(slug, route, None, "mounted-%s" % theme, False,
                                      "page never mounted (.ks3-lesson/[id^=s-])")
                            continue
                        for w in BATCH_WIDTHS:
                            page.set_viewport(w, 1000)
                            time.sleep(0.4)
                            check_batch_overflow(R, slug, route, w, page)
                            if theme == "light":
                                check_console(R, slug, route, w, page)
                        if theme == "light":
                            check_batch_no_react(R, slug, route, page)
                            page.set_viewport(1280, 1000)
                            check_keyboard(R, slug, route, page)
    finally:
        server.shutdown()
    return R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson", default=None, help="restrict to one site slug")
    ap.add_argument("--width", type=int, default=None, help="restrict to one width")
    ap.add_argument("--json", default=None, help="write full results to this path")
    ap.add_argument("--batch", default=None,
                     help="'pilot' (default — the full Design-fidelity run "
                          "below) or another registered batch name (a "
                          "simpler, reference-free sweep — see run_batch())")
    args = ap.parse_args()

    if args.batch and args.batch != "pilot":
        R = run_batch(args.batch, only_slug=args.lesson)
        print("\n" + R.summary())
        return 1 if R.fail_count else 0

    R = run(only_slug=args.lesson, only_width=args.width)

    print("\n" + R.summary())
    print("\nTEXT_EXEMPTIONS exercised this run (job 1, "
          "docs/ks4/pilot-build-contract.md):")
    if not APPLIED_EXEMPTIONS:
        print("  (none — no section hit a whitelisted exemption)")
    else:
        seen = sorted(set(APPLIED_EXEMPTIONS))
        for lesson, key, route, rulings in seen:
            print("  %-28s %-24s %-4s -> %s" % (lesson, key, route, ", ".join(rulings)))
        declared = sum(len(v) for v in TEXT_EXEMPTIONS.values())
        print("  %d exemption row(s) declared in TEXT_EXEMPTIONS, %d distinct "
              "(lesson, section, route) hit(s) this run"
              % (declared, len(seen)))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(R.rows, fh, indent=2)
        print("wrote %s" % args.json)

    return 1 if R.fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
