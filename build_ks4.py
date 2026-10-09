#!/usr/bin/env python3
"""build_ks4.py — the KS4 pilot generator (docs/ks4/pilot-build-contract.md).

    python3 build_ks4.py

Compiles Design's 14 lesson `.dc.html` files and 11 shared block `.dc.html`
files (docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and
Electricity/) into 54 static pages under `mrbadmus_site/{combined,triple}/
{foundation,higher}/{chemistry,physics}/{bonding,electricity}/<slug>.html` —
the SAME URLs the old (pre-port) KS4 generator already serves for these 14
subtopics. `generate_site_v5.py` writes the old design there first (it
always runs); this script OVERWRITES those 54 paths with the ported design
immediately after — see the note next to its `build_all.py` step.

No React, no Babel, no `support.js`: `shared/ks4-runtime.js` renders
Design's compiled templates and her (verbatim, ruling-corrected) logic
classes without them. See that file's own docstring for the runtime; see
`ks4_rulings.py` for every correction applied to Design's delivery and why.

⚠️ `ks4_data/` (the KS4 question-pool package) is NEVER imported or touched
here — a hard line (contract §2). This script reads `all_subtopics_*.py`
only, the same files `generate_site_v5.py` reads.
"""

import hashlib
import importlib
import json
import os
import re
import sys
import time

import brand
import ks4_lessons
from ks4_lessons import blocks as ks4_blocks
import ks4_batch_rulings
import ks4_rulings
import ks4_science_rulings
from theme_head import THEME_HEAD, theme_script

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DESIGN_DIR = ks4_lessons.DESIGN_DIR
DS_DIR = os.path.join("docs", "ks4", "design-reference", "pilot", "_ds",
                       "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")
OUT_ROOT = "mrbadmus_site"
INVENTORY_DIR = os.path.join("docs", "ks4", "pilot-inventory")
MANIFEST_PATH = "ks4_pilot_manifest.json"
AUTHORED_ROOT = ks4_lessons.AUTHORED_ROOT  # ks4_lessons/authored


def batch_manifest_path(name):
    return "ks4_pilot_manifest.json" if name == "pilot" else "ks4_%s_manifest.json" % name


def batch_frozen_path(name):
    return FREEZE_PATH if name == "pilot" else os.path.join("ks4_lessons", "frozen_%s.json" % name)

BLOCK_NAMES = ["Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write",
               "Ks4Cfifa", "Ks4Ladder", "Ks4KeyNote", "Ks4QuizBank", "Ks4End",
               "Ks4Video"]

# ⊕ Mide's rule 1 (2 Oct 2026, docs/ks4/START-HERE-REWRITE.md) — every KS4
# lesson opens on Design's two-option `Ks4Guess`. Batch 4 carries it in its own
# block set; the pilot and batches 2-3 do not, so it is compiled from batch 4's
# lessons dir and registered on a page ONLY when that lesson's template uses it
# (a lesson that does not is byte-identical to before). It is deliberately NOT
# in BLOCK_NAMES, and its (already-shipped) <style> is not added to any CSS.
GUESS_BLOCK_DIR = os.path.join(REPO_ROOT, "docs", "ks4", "design-reference",
                               "batch-4", "lessons")
GUESS_IMPORT = 'name="Ks4Guess"'

ROUTE_CODES = ["CF", "CH", "TF", "TH"]
ROUTE_LABEL = ks4_lessons.ROUTE_LABELS
ROUTE_URL = ks4_lessons.ROUTE_URL

# ⊕ Mide's ruling (27 Sep 2026, the KS4 polish run) — the header route chip
# now states the page's route IN WORDS rather than the review-tool label
# ("Triple Higher"). Same four routes, a reader-facing phrasing.
ROUTE_WORDS = {
    "CF": "Combined Science · Foundation tier",
    "CH": "Combined Science · Higher tier",
    "TF": "Triple Science · Foundation tier",
    "TH": "Triple Science · Higher tier",
}


def compute_route_switch(lesson):
    """One dict per route this lesson ships on: `{route_code: {"words":
    ..., "options": [{"href", "label"}, ...]}}` — the OTHER routes this
    SAME lesson exists on, from `ks4_lessons.LESSONS`'s own `routes` list
    (the same ground truth `shared/ks4-lib.js`'s NAV/hrefFor mirrors for
    prev/next/connects) via `ks4_lessons.site_url()`. Computed once per
    lesson (not per route) since every route's option list is a subset of
    the same `lesson["routes"]`; `ks4_rulings.R11` reads it per (lesson,
    route) at mount time."""
    out = {}
    for route in lesson["routes"]:
        others = [{"href": ks4_lessons.site_url(lesson["slug"], other),
                   "label": ROUTE_WORDS[other]}
                  for other in lesson["routes"] if other != route]
        out[route] = {"words": ROUTE_WORDS[route], "options": others}
    return out


# ⊕ Mide's ruling (27 Sep 2026) — every route used to show the Combined
# Science (8464) AQA spec section number, even on a Triple/separate-science
# route. `docs/theme/spec-numbers.md` is the citation table (verified
# against the real AQA-8462/8463-SP-2016.PDF spec PDFs, section by section,
# never assumed by numeric pattern) this dict is the machine copy of. Every
# lesson but `nanoparticles` gets an entry — nanoparticles has NO Combined
# route at all (8462 §4.2.4 is chemistry-only content), and its eyebrow/
# key-note already show the correct, verified 8462 number with nothing to
# swap, so `ks4_rulings.apply_r14_spec_number` is never called for it.
#
# ⊕ D13 (theme-run audit, 27 Sep 2026) — the COMBINED side of every entry
# below used to show only the bare section number ("AQA Chemistry 5.2.1.1"),
# with no "(8464)" — inconsistent with the TRIPLE side of the very same
# entry, which has always named its own spec ("AQA Chemistry (8462)
# 4.2.1.1"). A Combined pupil reading the eyebrow could not tell which of
# the three AQA GCSE Science specs the number belonged to; a Triple pupil
# always could. Every "combined" eyebrow now carries "(8464)" in the exact
# position its "triple" sibling carries "(8462)"/"(8463)" (right after the
# subject name), and every "combined" keynote carries it where the sibling
# does (right after the number, before any trailing "· RP"/"· <word>"
# annotation). `apply_r14_spec_number` itself is untouched: it swaps the
# template's literal text for a `{{ specEyebrow }}`/`{{ specNote }}`
# placeholder and does not care what the replacement text says, so this
# is a content-only change, verified with `extract_freeze_pieces()` (see
# docs/theme/spec-numbers.md) to move nothing else on any of the 54 pages.
# The tutor's own context string (`tutor_block()`, below) reads THIS dict
# via `compute_spec_note()` and already regexes "AQA <num> (<code>)" into
# "AQA <code> <num>" for the tutor — that conversion previously never fired
# for Combined (nothing to convert) and now fires identically to Triple's,
# so the tutor is consistent with the page for free; no separate edit.
SPEC_TEXT = {
    "chemical-bonds": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.1.1 · Classify", "keynote": "AQA 5.2.1.1 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.1.1 · Classify", "keynote": "AQA 4.2.1.1 (8462)"}},
    "ionic-bonding": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.1.2 · Process", "keynote": "AQA 5.2.1.2 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.1.2 · Process", "keynote": "AQA 4.2.1.2 (8462)"}},
    "ionic-compounds": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.1.3 · Model", "keynote": "AQA 5.2.1.3 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.1.3 · Model", "keynote": "AQA 4.2.1.3 (8462)"}},
    "covalent-bonding": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.1.4 · Process", "keynote": "AQA 5.2.1.4 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.1.4 · Process", "keynote": "AQA 4.2.1.4 (8462)"}},
    "metallic-bonding": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.1.5 · Model", "keynote": "AQA 5.2.1.5 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.1.5 · Model", "keynote": "AQA 4.2.1.5 (8462)"}},
    "states-of-matter": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.1–5.2.2.2 · Investigation", "keynote": "AQA 5.2.2.1–5.2.2.2 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.1–4.2.2.2 · Investigation", "keynote": "AQA 4.2.2.1–4.2.2.2 (8462)"}},
    "properties-ionic-compounds": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.3 · Contrast", "keynote": "AQA 5.2.2.3 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.3 · Contrast", "keynote": "AQA 4.2.2.3 (8462)"}},
    "properties-small-molecules": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.4 · Model", "keynote": "AQA 5.2.2.4 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.4 · Model", "keynote": "AQA 4.2.2.4 (8462)"}},
    "polymers": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.5 · Classify", "keynote": "AQA 5.2.2.5 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.5 · Classify", "keynote": "AQA 4.2.2.5 (8462)"}},
    "giant-covalent-structures": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.6 · 5.2.3.1–5.2.3.3 · Contrast", "keynote": "AQA 5.2.2.6, 5.2.3 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.6 · 4.2.3.1–4.2.3.3 · Contrast", "keynote": "AQA 4.2.2.6, 4.2.3 (8462)"}},
    "metals-alloys": {
        "combined": {"eyebrow": "AQA Chemistry (8464) 5.2.2.7–5.2.2.8 · Contrast", "keynote": "AQA 5.2.2.7–5.2.2.8 (8464)"},
        "triple": {"eyebrow": "AQA Chemistry (8462) 4.2.2.7–4.2.2.8 · Contrast", "keynote": "AQA 4.2.2.7–4.2.2.8 (8462)"}},
    "series-parallel-circuits": {
        "combined": {"eyebrow": "AQA Physics (8464) 6.2.2 · System", "keynote": "AQA 6.2.2 (8464)"},
        "triple": {"eyebrow": "AQA Physics (8463) 4.2.2 · System", "keynote": "AQA 4.2.2 (8463)"}},
    "resistors": {
        "combined": {"eyebrow": "AQA Physics (8464) 6.2.1.4 · Required practical", "keynote": "AQA 6.2.1.4 (8464) · RP"},
        "triple": {"eyebrow": "AQA Physics (8463) 4.2.1.4 · Required practical", "keynote": "AQA 4.2.1.4 (8463) · RP"}},
}


def compute_spec_note(slug, route):
    entry = SPEC_TEXT.get(slug)
    if entry is None:
        return None
    return entry["triple" if route in ("TF", "TH") else "combined"]


def old_combined_spec_text(slug):
    """⊕ D13 (theme-run audit, 27 Sep 2026) — `SPEC_TEXT[slug]["combined"]`
    is the RENDER-TIME value (with "(8464)"); Design's ORIGINAL template
    file on disk, and `ks4_parity`'s `reference.json` snapshot of it, both
    still carry the pre-D13 literal with no spec code at all. Three
    consumers need that exact pre-D13 string — `compile_lesson()`'s call to
    `ks4_rulings.apply_r14_spec_number` (finds it in the template to swap
    in the placeholder), and `ks4_parity.apply_text_whitelist()` (finds it
    in Design's reference text to reconcile against the port, on EVERY
    route: CF/CH now show the new combined text, TF/TH show triple's) — so
    this is the one place the stripping happens, not three. "(8464) "/"
    (8464)" appear nowhere else in either string, so removing them
    reproduces the exact original, byte for byte. Returns None for a slug
    not in SPEC_TEXT (nanoparticles)."""
    entry = SPEC_TEXT.get(slug)
    if entry is None:
        return None
    return {
        "eyebrow": entry["combined"]["eyebrow"].replace("(8464) ", "", 1),
        "keynote": entry["combined"]["keynote"].replace(" (8464)", "", 1),
    }

# ⊕ D3 fix (26 Sep 2026, docs/ks4/pilot-live-audit.md) — the pilot pages
# shipped no `<link rel="icon">` at all, so every one of the 54 pages 404'd
# on the browser's `/favicon.ico` fallback (the ONLY console error the audit
# found). The old (pre-pilot, generate_site_v5.py-built) KS4 lesson pages
# already carry this exact icon — confirmed byte-identical via
# `git show 0741525aa:mrbadmus_site/combined/foundation/chemistry/bonding/
# metallic-bonding.html`, which decodes to this same `<svg>` — and it is the
# same one `build_ks3.FAVICON_LINK` and `generate_site_v5.KS4_FAVICON_LINK`
# each already define, independently, as their own literal (this codebase's
# standing preference for independent generators over cross-module coupling
# — see generate_site_v5.py's comment by KS4_FAVICON_LINK). Kept here as
# ITS OWN literal for the same reason, not imported.
# ⊕ ONE-MARK RULING (Mide, 13 Sep 2026; one-mark run 27 Sep 2026) — the
# upward-chevron data: favicon literal this comment describes is RETIRED.
# The pages carry the ONE mark's head tags from brand.py instead (the kit's
# favicon, apple-touch icon and the lockup stylesheet), stamped by the same
# stamp_versions() pass as every /shared/ks4-* asset (KS4_VERSIONED). The
# D3 property is unchanged: every page has a real <link rel="icon">, so no
# favicon.ico 404.
KS4_PILOT_FAVICON_LINK = brand.brand_head()

# ⊕ these are OUR OWN new assets, a SEPARATE list from build_ks3.py's
# VERSIONED_ASSETS tuple (contract §1: "add a KS4 list in build_ks4.py — do
# not edit build_ks3.py's tuple in place"). mrbadmus.v2.js is included
# because our pages load it too, even though we never write it ourselves.
# theme.js (THEME RUN, 26 Sep 2026) is the same situation: the ONE shared
# theme control every lane loads, never written by this script, still
# stamped like every other /shared/ks4-* asset on these pages.
KS4_VERSIONED = ("ks4-ds.css", "ks4-theme.css", "ks4-lesson.css",
                  "ks4-source.js", "ks4-lib.js", "ks4-diagrams.js",
                  "ks4-runtime.js", "mrbadmus.v2.js", "theme.js",
                  # ⊕ one-mark run (27 Sep 2026) — brand.brand_head()'s assets.
                  "brand/brand.css", "brand/mrbadmus-favicon.svg",
                  "brand/mrbadmus-icon-light-512.png",
                  # ⊕ Stage B (phone run, 28 Sep 2026) — the one top bar and
                  # what its right-hand group needs (config.js for ?env=test,
                  # class-entry.js for who is looking, the bell).
                  "topbar.css", "topbar.js", "config.js", "class-entry.js",
                  "student-bell.js")

# The subset of KS4_VERSIONED this script itself WRITES (excludes
# mrbadmus.v2.js, which it only reads — that one is generate_site_v5.py's,
# already synced by its own round-trip). Cloudflare serves from
# mrbadmus_site/, not the repo root, so a page linking /shared/ks4-lib.js
# 404s unless the file is copied there too — the same reason build_ks3.py
# copies ks3.css/ks3.js/tokens.css into mrbadmus_site/shared/ itself rather
# than trusting generate_site_v5.py to have done it: generate_site_v5.py's
# copy of shared/ happens BEFORE this script runs (build_all.py's step
# order), so anything this script writes into shared/ AFTER that has to be
# synced here, not assumed.
KS4_OWN_ASSETS = ("ks4-ds.css", "ks4-theme.css", "ks4-lesson.css",
                   "ks4-source.js", "ks4-lib.js", "ks4-diagrams.js",
                   "ks4-runtime.js")


def _shared(name):
    return os.path.join("shared", name)


# ═══════════════════════════════════════════════════════════════════════
# FREEZE — the re-freeze mechanism (docs/ks4/pilot-build-contract.md /
# the run brief's item 4). `ks4_lessons/frozen.json` (written by
# `python3 build_ks4.py --freeze`) records, per lesson, a sha256 of exactly
# three things concatenated: the compiled TEMPLATE json blob, the rulings-
# applied LOGIC source, and the lesson's served SOURCE record (the quiz/
# rp/key_note copy for every route). All three are byte-identical to what
# ends up embedded on disk — the template/logic strings are the very ones
# `lesson_mount_script()` interpolates into the page's mount `<script>`, and
# the source-record string is the very one `build_source_js()` interpolates
# into `shared/ks4-source.js` — so a fast, browser-free gate (ks4_pilot_
# check.py) can recompute the SAME hash by lifting the same three
# substrings back out of what's already on disk, with no recompilation and
# no Chrome. `extract_freeze_pieces()` is that reverse operation; it MUST
# stay byte-for-byte in step with how `lesson_mount_script()` and
# `build_source_js()` assemble those strings, or a green freeze will not
# reproduce.
# ═══════════════════════════════════════════════════════════════════════
FREEZE_PATH = os.path.join("ks4_lessons", "frozen.json")
_FREEZE_SEP = "\x1f"  # ASCII unit separator — cannot appear in JSON or in
                       # Design's JS source, so it cannot be forged by content


def compute_freeze_hash(template_json_str, logic_str, source_json_str):
    blob = _FREEZE_SEP.join([template_json_str, logic_str, source_json_str])
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


_MOUNT_MARKER = ("\nwindow.MrBadmusKS4Runtime.mount({\n"
                 "  into: '#ks4-mount', Component: Component,\n"
                 "  props: ")
_SCRIPT_OPEN_MARKER = "<script>\n(function () {\n"
_PROPS_TEMPLATE_SEP = ",\n  template: "
_MOUNT_TAIL_MARKER = "\n});\n})();\n</script>"


def extract_freeze_pieces(page_text, source_js_text, slug):
    """Reverse of `lesson_mount_script()` + `build_source_js()`'s string
    assembly: pulls the exact LOGIC and TEMPLATE-JSON substrings back out of
    an already-built page, and the exact SOURCE-record JSON substring back
    out of `shared/ks4-source.js`, with no parsing beyond string search
    (both embedded blobs are single-line — `json.dumps` never emits a raw
    newline — so a literal marker search is exact, not a heuristic)."""
    idx_mount = page_text.index(_MOUNT_MARKER)
    idx_open = page_text.rindex(_SCRIPT_OPEN_MARKER, 0, idx_mount)
    logic = page_text[idx_open + len(_SCRIPT_OPEN_MARKER):idx_mount]

    template_start = page_text.index(
        _PROPS_TEMPLATE_SEP, idx_mount + len(_MOUNT_MARKER)) + len(_PROPS_TEMPLATE_SEP)
    template_end = page_text.index(_MOUNT_TAIL_MARKER, template_start)
    template_json = page_text[template_start:template_end]

    src_marker = 'window.KS4SRC["%s"] = ' % slug
    src_start = source_js_text.index(src_marker) + len(src_marker)
    src_end = source_js_text.index(";\n", src_start)
    source_json = source_js_text[src_start:src_end]

    return template_json, logic, source_json


# ═══════════════════════════════════════════════════════════════════════
# STEP A — shared/ks4-source.js, GENERATED from all_subtopics_*.py
# ═══════════════════════════════════════════════════════════════════════
SOURCE_MODULES = {
    "chemistry": {"CF": "all_subtopics_chemistry",
                  "CH": "all_subtopics_chemistry_higher",
                  "TF": "all_subtopics_chemistry_triple_foundation",
                  "TH": "all_subtopics_chemistry_triple_higher"},
    "physics": {"CF": "all_subtopics_physics",
                "CH": "all_subtopics_physics_higher",
                "TF": "all_subtopics_physics_triple_foundation",
                "TH": "all_subtopics_physics_triple_higher"},
    # ⊕ batch engine (1 Oct 2026) — the pilot never needed biology (it is
    # chemistry/bonding + physics/electricity only); the first batch of
    # Code-authored lessons may be any of the three sciences.
    "biology": {"CF": "all_subtopics_biology",
                "CH": "all_subtopics_biology_higher",
                "TF": "all_subtopics_biology_triple_foundation",
                "TH": "all_subtopics_biology_triple_higher"},
}
SOURCE_ATTR = {"chemistry": "CHEMISTRY_SUBTOPICS_ALL", "physics": "PHYSICS_SUBTOPICS_ALL",
               "biology": "BIOLOGY_SUBTOPICS_ALL"}

# The non-quiz fields Design's ks4-source.js carries. `quiz` is handled
# separately below because it is the one field that genuinely varies by
# route; every other field is taken from ONE canonical record (see
# `build_source_record`).
NONQUIZ_FIELDS = ["summary", "theory", "common_mistake", "examiner_tip",
                   "key_note", "matching", "fifas", "equations", "rp",
                   "variables", "higher"]


def load_subtopics_by_route():
    """{subject: {route_code: SUBTOPICS_ALL dict}} — the same four files per
    subject `generate_site_v5.py` imports, aliased the same way it does."""
    out = {}
    for subject, routes in SOURCE_MODULES.items():
        out[subject] = {}
        for route, modname in routes.items():
            mod = importlib.import_module(modname)
            out[subject][route] = getattr(mod, SOURCE_ATTR[subject])
    return out


def find_subtopic(data, subject, route, topic_id, slug):
    lst = data[subject][route].get(topic_id, [])
    return next((s for s in lst if s["id"] == slug), None)


def build_source_record(data, lesson):
    """One lesson's record for shared/ks4-source.js. Non-quiz fields are
    taken from the TRIPLE HIGHER file — always present for all 14 lessons
    (it is the "everything" tier) — so there is exactly one canonical
    theory/summary/key_note/examiner_tip/common_mistake per lesson, the way
    Design's own file has one. `quiz` is the one field built per route."""
    slug, subject, topic = lesson["slug"], lesson["subject"], lesson["topic_id"]
    canon = find_subtopic(data, subject, "TH", topic, slug)
    if canon is None:
        raise SystemExit("build_ks4.build_source_record: no TH record for %r" % slug)
    rec = {}
    for f in NONQUIZ_FIELDS:
        v = canon.get(f)
        if v:
            rec[f] = v
    quiz = {}
    for route in lesson["routes"]:
        st = find_subtopic(data, subject, route, topic, slug)
        if st and st.get("quiz"):
            quiz[route] = st["quiz"]
    rec["quiz"] = quiz
    return rec


def apply_withhold(lesson, rec):
    """Batch lessons only. `withhold` on a lesson record names frozen quiz
    items the batch examiner found scientifically wrong, or wrong for a
    route, so the page does not serve them (practice bank, K.find). The
    frozen all_subtopics_*.py rows are never edited — this only selects
    what the generated batch source carries. Each entry is
    {"needle": <substring of the question>, "routes": [codes] | None,
    "dep": <DEPARTURES id>}; a needle that matches nothing on a named
    route fails the build, so a withheld item cannot silently come back
    or silently stop being withheld."""
    for w in lesson.get("withhold", []):
        routes = w.get("routes") or list(rec["quiz"].keys())
        for r in routes:
            items = rec["quiz"].get(r, [])
            keep = [q for q in items if w["needle"] not in q.get("q", "")]
            if len(keep) == len(items):
                raise SystemExit(
                    "build_ks4.apply_withhold: %s %s: needle %r (%s) matches "
                    "no quiz item" % (lesson["slug"], r, w["needle"], w.get("dep")))
            rec["quiz"][r] = keep


def build_source_js(data, lessons=None, out_name=None):
    """`lessons=None` (the pilot's own call) keeps the exact header this
    function always had, byte for byte. A batch passes its own `lessons`
    list and `out_name` (e.g. 'ks4-source-batch-2.js') for a header that
    names itself correctly — the ONLY difference; the body format (one
    `window.KS4SRC[slug] = {...}` line per lesson, merging into the SAME
    global every other ks4-source*.js file writes to) is identical, so a
    pilot page and a batch page can load both scripts in either order."""
    if lessons is None:
        lessons = ks4_lessons.LESSONS
        lines = [
            "/* shared/ks4-source.js — GENERATED by build_ks4.py from "
            "all_subtopics_chemistry*.py / all_subtopics_physics*.py.",
            "   Never hand-edit — re-run build_ks4.py. Keyed by SITE slug "
            "(see ks4_rulings.py R-SLUG for the three lessons whose OWN",
            "   `const slug` differs from it). A build check diffs this against "
            "Design's own ks4-source.js field by field —",
            "   docs/ks4/pilot-inventory/source-diff.md. */",
            "window.KS4SRC = window.KS4SRC || {};",
        ]
    else:
        lines = [
            "/* shared/%s — GENERATED by build_ks4.py --batch from the "
            "repo's own all_subtopics_*.py files (docs/ks4/batch-engine.md)."
            % out_name,
            "   Never hand-edit — re-run build_ks4.py. Merges into the SAME "
            "window.KS4SRC the pilot's shared/ks4-source.js writes to, so "
            "both",
            "   may be loaded on the same page in either order. */",
            "window.KS4SRC = window.KS4SRC || {};",
        ]
    per_slug = {}
    for lesson in lessons:
        per_slug[lesson["slug"]] = build_source_record(data, lesson)

    per_slug = ks4_science_rulings.apply_source(per_slug)
    if lessons is not ks4_lessons.LESSONS:
        for lesson in lessons:
            apply_withhold(lesson, per_slug[lesson["slug"]])

    for lesson in lessons:
        slug = lesson["slug"]
        rec = per_slug[slug]
        ks4_science_rulings.expect_present("source", slug, rec)
        lines.append('window.KS4SRC["%s"] = %s;'
                      % (slug, json.dumps(rec, sort_keys=True)))
    return "\n".join(lines) + "\n", per_slug


_KS4SRC_LINE_RE = re.compile(r'window\.KS4SRC\["([^"]+)"\]\s*=\s*(\{.*?\});', re.S)


def load_design_source_js():
    path = os.path.join(DESIGN_DIR, "ks4-source.js")
    text = open(path, encoding="utf-8").read()
    out = {}
    for m in _KS4SRC_LINE_RE.finditer(text):
        out[m.group(1)] = json.loads(m.group(2))
    return out


def _first_diff_note(a, b, path=""):
    """STRUCTURE-AWARE: walks matching dict keys / list indices rather than
    comparing two serialized strings character-by-character, which drifts
    out of alignment the moment the two sides serialize ONE field with a
    different length (whitespace, key order, unicode-escaping) and then
    "diffs" a hundred unrelated characters later. Returns the first leaf
    value that genuinely differs, with its path."""
    if a is None and b is None:
        return ""
    if a is None:
        return " — design has no value at %s; ours: %s" % (path or "(root)", json.dumps(b)[:160])
    if b is None:
        return " — ours has no value at %s; design's: %s" % (path or "(root)", json.dumps(a)[:160])
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                return " — design is missing key %r (at %s)" % (k, path)
            if k not in b:
                return " — ours is missing key %r (at %s)" % (k, path)
            if a[k] != b[k]:
                return _first_diff_note(a[k], b[k], "%s.%s" % (path, k) if path else k)
        return ""
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return (" — length differs at %s: design has %d, ours has %d"
                    % (path or "(root)", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                return _first_diff_note(x, y, "%s[%d]" % (path, i))
        return ""
    return (" — at %s: design=%r vs ours=%r"
            % (path or "(root)", _shorten(a), _shorten(b)))


def _shorten(v):
    s = v if isinstance(v, str) else json.dumps(v)
    return s if len(s) <= 140 else s[:140] + "…"


def _json_normalize(v):
    """Round-trip through JSON so a Python tuple (`[('Ionic', '…'), …]` is
    how every `opts`/`matching.pairs`/`fifas` list is AUTHORED in
    all_subtopics_*.py) compares equal to the JSON array it is semantically
    identical to. Without this, `[('a', True)] == [['a', True]]` is FALSE in
    Python — tuple vs list — and every quiz/matching field in this diff
    reported DIFFERS for a reason that had nothing to do with content."""
    return json.loads(json.dumps(v, sort_keys=True))


def write_source_diff(per_slug):
    design = load_design_source_js()
    per_slug = {slug: _json_normalize(rec) for slug, rec in per_slug.items()}
    lines = [
        "# KS4 pilot — shared/ks4-source.js vs Design's ks4-source.js",
        "",
        "Generated by build_ks4.py's `write_source_diff()`. Byte equality is "
        "the expectation for every field except where a ruling documents a "
        "departure; a difference below is a FINDING for the inventory "
        "executor / examiners, not something this script papers over.",
        "",
    ]
    equal_count = diff_count = 0
    for lesson in ks4_lessons.LESSONS:
        slug = lesson["slug"]
        design_key = ks4_rulings.SLUG_MISMATCHES.get(slug, slug)
        d = design.get(design_key)
        ours = per_slug[slug]
        lines.append("## `%s` (Design's key: `%s`)" % (slug, design_key))
        if d is None:
            lines.append("- Design's ks4-source.js has no entry under this key. SKIPPED.")
            lines.append("")
            continue
        fields = sorted(set(list(d.keys()) + list(ours.keys()) + ["quiz"]))
        for f in fields:
            if f == "file":
                continue  # Design's authoring-markdown filename; we never had one
            if f == "quiz":
                for route in ROUTE_CODES:
                    dq = (d.get("quiz") or {}).get(route)
                    oq = (ours.get("quiz") or {}).get(route)
                    if dq is None and oq is None:
                        continue
                    if dq == oq:
                        lines.append("- quiz.%s: EQUAL (%d questions)" % (route, len(oq or [])))
                        equal_count += 1
                    else:
                        lines.append("- quiz.%s: DIFFERS%s" % (route, _first_diff_note(dq, oq)))
                        diff_count += 1
                continue
            dv, ov = d.get(f), ours.get(f)
            if dv == ov:
                if dv is not None:
                    lines.append("- %s: EQUAL" % f)
                    equal_count += 1
                continue
            lines.append("- %s: DIFFERS%s" % (f, _first_diff_note(dv, ov)))
            diff_count += 1
        lines.append("")
    lines.insert(4, "Summary: %d field/route comparisons EQUAL, %d DIFFER.\n"
                 % (equal_count, diff_count))
    os.makedirs(INVENTORY_DIR, exist_ok=True)
    out_path = os.path.join(INVENTORY_DIR, "source-diff.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return out_path, equal_count, diff_count


# ═══════════════════════════════════════════════════════════════════════
# STEP B — the small shared assets: ks4-ds.css (generated), ks4-theme.css
# and ks4-diagrams.js (copied verbatim), ks4-lib.js (ported: R2's fig
# marker + the hrefFor/NAV addition).
# ═══════════════════════════════════════════════════════════════════════
_FONT_URL_RE = re.compile(r"url\('(?:\.\./fonts/|\./)?([A-Za-z0-9_-]+\.woff2)'\)")

_DS_CSS_HEADER = """/* shared/ks4-ds.css — GENERATED by build_ks4.py from Design's own
   delivered bundle (docs/ks4/design-reference/pilot/_ds/.../styles.css and
   its @import chain), concatenated in her own import order:
     tokens/src-styles-tokens.css, tokens/shared-tokens.css,
     tokens/shared-ks3.css, fonts/fonts.css, _ds_bundle.css

   WHY A NEW FILE rather than shared/tokens.css + shared/ks3.css (which the
   rest of the site already loads): neither is byte-identical to what
   Design's page was built against — shared/ks3.css alone is ~29,850
   lines against her 1,403 (the diff has real content on BOTH sides, not
   just a subset), and shared/tokens.css differs beyond its font paths.
   Loading the site's evolved stylesheets here would risk months of OTHER
   KS3 unit CSS cascading onto a page Design never tested against it. The
   contract's "the page wins" rule settles this: ship what she built
   against, verbatim, as one new asset. shared/fonts/*.woff2 IS reused
   as-is — confirmed byte-identical to the seven fonts this bundle needs.

   The ONLY bytes changed from Design's originals are the font url() paths,
   rewritten to /shared/fonts/X.woff2. Never hand-edit; re-run build_ks4.py. */

"""


_DS_CSS_DARK_MARKER = '[data-theme="dark"] {'


def build_ds_css():
    parts = []
    for rel in ("tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
                "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css"):
        parts.append(open(os.path.join(DS_DIR, rel), encoding="utf-8").read())
    body = "\n\n".join(parts)
    body = _FONT_URL_RE.sub(lambda m: "url('/shared/fonts/%s')" % m.group(1), body)
    # ⊕ D8 (theme-run audit, 27 Sep 2026). This bundle's ONE `[data-theme=
    # "dark"] { ... }` block (from tokens/shared-tokens.css, byte-identical
    # to shared/tokens.css's own — same reasoning as that file's D8 fix) is
    # unconditional: `data-theme="dark"` is written by THEME_HEAD/theme.js
    # on every load, in every medium, so un-guarded it printed the dark
    # ground and cream ink on every one of the 54 pilot pages regardless of
    # the viewed theme. `body.count(...) == 1` is checked because this is a
    # build-time transform of Design's frozen concatenation, never a
    # hand-edit of her source files — if a future delivery changes the
    # bundle so this marker no longer appears exactly once, the build must
    # stop rather than silently wrap the wrong text (or nothing at all). */
    if body.count(_DS_CSS_DARK_MARKER) != 1:
        raise SystemExit(
            "build_ks4: ks4-ds.css bundle's [data-theme=\"dark\"] block "
            "moved, is missing, or is no longer unique (found %d) — the D8 "
            "@media screen wrap in build_ds_css() needs to be re-read "
            "against the new bundle before this can be re-run."
            % body.count(_DS_CSS_DARK_MARKER))
    start = body.index(_DS_CSS_DARK_MARKER)
    depth = 0
    end = None
    for i in range(start, len(body)):
        if body[i] == "{":
            depth += 1
        elif body[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        raise SystemExit(
            "build_ks4: ks4-ds.css bundle's [data-theme=\"dark\"] block "
            "has no matching closing brace — re-read before this can be "
            "re-run.")
    body = (body[:start] + "@media screen {\n" + body[start:end]
            + "\n} /* @media screen — D8 */" + body[end:])
    return _DS_CSS_HEADER + body


def build_ks4_lib_js():
    text = open(os.path.join(DESIGN_DIR, "ks4-lib.js"), encoding="utf-8").read()
    text = ks4_rulings.apply_r2_ks4lib(text)
    text = ks4_rulings.apply_r11_route_lib(text)

    # ⊕ batch engine fix (docs/ks4/batch-engine.md §7b, 1 Oct 2026) — this
    # USED to build NAV from `ks4_lessons.all_lessons()` (every registered
    # batch, not just the pilot), reasoning that it stayed byte-identical
    # until a second batch actually shipped. That reasoning was wrong the
    # moment a batch WAS registered: `shared/ks4-lib.js` is one of the 17
    # shared assets whose `?v=<md5>` stamp is baked into all 54 pilot pages'
    # own bytes (`KS4_VERSIONED`, `build_pilot()`'s `versions` dict) — so
    # registering `ks4_lessons/batch_2.py` moved this file's content, moved
    # its stamp, and moved all 54 pilot pages by those bytes, breaking the
    # one rule this engine exists to keep ("the pilot's 54 pages … must
    # never change by a byte because a batch was added"). NAV is pinned to
    # the pilot's OWN 14 lessons, forever — it cannot depend on which
    # batches are registered. A connects/prev/next link that needs to reach
    # a NON-pilot lesson (or any other KS4 subtopic on the site) is
    # `shared/ks4-nav.js`'s job instead (`build_ks4_nav_js()`, below) — a
    # SEPARATE asset, loaded by batch pages only, never by the pilot's.
    nav = {L["slug"]: {"subject": L["subject"], "topic": L["topic_id"],
                        "routes": L["routes"]} for L in ks4_lessons.LESSONS}
    addition = (
        "\n  /* ⊕ ENGINE ADDITION — not in Design's delivery. Her page "
        "never needed a\n"
        "     real href (Route was a review selector, and her prev/next/"
        "connects\n"
        "     hrefs were sibling .dc.html filenames for local review). NAV "
        "is\n"
        "     generated from ks4_lessons.LESSONS by build_ks4.py.\n"
        "     ⊕ D2 fix (26 Sep 2026, docs/ks4/pilot-live-audit.md): this "
        "used to\n"
        "     fall back to the Triple pathway at the same tier when the "
        "target did\n"
        "     not ship on the current pathway (nanoparticles is "
        "Triple-only), which\n"
        "     sent a Combined pupil into chemistry-only content. It now "
        "returns\n"
        "     null instead — ks4_rulings.py's R-CONNECTS wraps every "
        "endConnects\n"
        "     array with a .filter() that drops a null-href entry, so the "
        "link is\n"
        "     simply absent on a route where the target has no page. */\n"
        "  var NAV = %s;\n"
        "  function hrefFor(slug, R) {\n"
        "    var n = NAV[slug];\n"
        "    if (!n) { return null; }\n"
        "    var pathway = (R && R.isTriple) ? 'triple' : 'combined';\n"
        "    var tier = (R && R.isHigher) ? 'higher' : 'foundation';\n"
        "    var code = (pathway === 'triple' ? 'T' : 'C') + (tier === "
        "'higher' ? 'H' : 'F');\n"
        "    if (n.routes.indexOf(code) === -1) { return null; }\n"
        "    return '/' + pathway + '/' + tier + '/' + n.subject + '/' + "
        "n.topic + '/' + slug + '.html';\n"
        "  }\n"
    ) % json.dumps(nav, sort_keys=True)

    marker = "  return { rail: rail,"
    if text.count(marker) != 1:
        raise SystemExit("build_ks4_lib_js: expected exactly one %r" % marker)
    idx = text.index(marker)
    text = text[:idx] + addition + text[idx:]

    tail_from = "commonMistake: commonMistake, cfifa: cfifa, fifas: fifas, load: load, save: save, hash: hash };"
    tail_to = "commonMistake: commonMistake, cfifa: cfifa, fifas: fifas, load: load, save: save, hash: hash, hrefFor: hrefFor };"
    if text.count(tail_from) != 1:
        raise SystemExit("build_ks4_lib_js: expected exactly one %r" % tail_from)
    text = text.replace(tail_from, tail_to, 1)
    return text


# ═══════════════════════════════════════════════════════════════════════
# shared/ks4-nav.js — the batch engine's fix for the leak above
# (docs/ks4/batch-engine.md §7b). `shared/ks4-lib.js`'s NAV is pinned to the
# pilot's 14 lessons forever, so a batch page that needs to resolve a
# connects/prev/next link against a lesson OUTSIDE those 14 — a sibling in
# its own batch, a lesson in a different batch, or any other KS4 subtopic
# that merely has a page on the site (an old, unported design page is a
# real page at a real URL too) — needs a bigger table. This is that table.
#
# Loaded by BATCH pages ONLY, after `ks4-lib.js`, and it wraps
# `KS4.hrefFor` rather than replacing it: the pilot's own lookups keep
# resolving exactly as they always have (NAV first), and only a miss falls
# through to this file's FULL_NAV.
#
# ⚠️ Content depends ONLY on `all_subtopics_*.py` (via
# `load_subtopics_by_route()` — the SAME data `generate_site_v5.py` itself
# reads to decide which pages exist) — NEVER on `ks4_lessons.LESSONS`,
# `all_lessons()`, or which batches are registered. That is what makes this
# file safe for a batch to depend on: adding, building or removing a batch
# never moves ITS bytes either, so batch 2's pages do not move when batch 3
# is registered.
# ═══════════════════════════════════════════════════════════════════════
def build_ks4_nav_js():
    data = load_subtopics_by_route()
    nav = {}
    for subject, by_route in data.items():
        for route, subtopics_all in by_route.items():
            for topic_id, lst in subtopics_all.items():
                for s in lst:
                    slug = s["id"]
                    entry = nav.setdefault(
                        slug, {"subject": subject, "topic": topic_id, "routes": []})
                    if entry["subject"] != subject or entry["topic"] != topic_id:
                        raise SystemExit(
                            "build_ks4_nav_js: slug %r appears under more than one "
                            "(subject, topic) — (%r, %r) vs (%r, %r). ks4-nav.js "
                            "cannot key purely by slug if that happens."
                            % (slug, entry["subject"], entry["topic"], subject, topic_id))
                    if route not in entry["routes"]:
                        entry["routes"].append(route)
    for entry in nav.values():
        entry["routes"].sort()

    return (
        "/* shared/ks4-nav.js — GENERATED by build_ks4.py (docs/ks4/"
        "batch-engine.md §7b).\n"
        "   Loaded by BATCH pages only, after ks4-lib.js — the pilot's 54 "
        "pages never\n"
        "   load this file and never will; their own hrefFor lookups stay "
        "pinned to\n"
        "   ks4-lib.js's own NAV (the pilot's 14 lessons) regardless of "
        "what this\n"
        "   file contains. FULL_NAV covers EVERY KS4 subtopic on the site "
        "— every\n"
        "   slug in all_subtopics_*.py has a real page at that URL, "
        "whether that\n"
        "   page is an authored batch lesson, a ported pilot lesson, or "
        "the old\n"
        "   (pre-port) generated design — so a connects link may target "
        "any of\n"
        "   them. Content depends ONLY on all_subtopics_*.py, NEVER on "
        "which\n"
        "   batches are registered. Never hand-edit; re-run build_ks4.py "
        "--batch. */\n"
        "(function () {\n"
        "  var FULL_NAV = %s;\n"
        "  function fullNavHref(slug, R) {\n"
        "    var n = FULL_NAV[slug];\n"
        "    if (!n) { return null; }\n"
        "    var pathway = (R && R.isTriple) ? 'triple' : 'combined';\n"
        "    var tier = (R && R.isHigher) ? 'higher' : 'foundation';\n"
        "    var code = (pathway === 'triple' ? 'T' : 'C') + (tier === "
        "'higher' ? 'H' : 'F');\n"
        "    if (n.routes.indexOf(code) === -1) { return null; }\n"
        "    return '/' + pathway + '/' + tier + '/' + n.subject + '/' + "
        "n.topic + '/' + slug + '.html';\n"
        "  }\n"
        "  var base = KS4.hrefFor;\n"
        "  KS4.hrefFor = function (slug, R) { return base(slug, R) || "
        "fullNavHref(slug, R); };\n"
        "})();\n"
    ) % json.dumps(nav, sort_keys=True)


def build_ks4_diagrams_js():
    text = open(os.path.join(DESIGN_DIR, "ks4-diagrams.js"), encoding="utf-8").read()
    text = ks4_science_rulings.apply("asset", "ks4-diagrams.js", text)
    ks4_science_rulings.expect_present("asset", "ks4-diagrams.js", text)
    return text


# ⊕ THEME RUN (26 Sep 2026, THEME-CONTRACT.md rule 3) — shared/ks4-theme.css
# is copied VERBATIM from Design's own delivery (DESIGN_DIR), which is
# frozen and MD5-verified (contract §0); this is NOT a hand-edit of that
# file, it is a build-time transform of the COPY, same as KS4_DARK_MODE_
# FIXES above and for the identical reason: the `@media (prefers-color-
# scheme: dark)` block guards on `.rd[data-mode="ks3"]:not([data-theme=
# "light"])` — the `.rd` element's OWN attribute, which these pages never
# set (their mount prop is always `theme:"auto"`) — so it fired from the
# OS setting regardless of the site's own stored theme choice. The
# surviving `[data-theme="dark"] .rd[data-mode="ks3"]` selector (an
# ancestor match on `<html>`, which THEME_HEAD/theme.js DO always set)
# covers every case the media block used to, including System mode.
_KS4_THEME_CSS_DARK_BLOCK = """.rd[data-mode="ks3"][data-theme="dark"],
[data-theme="dark"] .rd[data-mode="ks3"] {
  --ks3-ground: #16120E; --ks3-card: #1F1A15; --ks3-band: #2A231C; --ks3-inset: #231D17; --ks3-row-dim: #1B1611;
  --ks3-rule: #3E352C; --ks3-rule-strong: #5E5246; --ks3-option-border: #4F443A; --ks3-option-spent: #2B241D;
  --ks3-ink: #F3ECE0; --ks3-ink-body: #E3D9CA; --ks3-ink-muted: #C2B6A6; --ks3-ink-faint: #B0A493; --ks3-ink-ghost: #8A7F72;
  --ks3-accent: #F07A4E; --ks3-accent-text: #FF9E78; --ks3-accent-tint: #3A2218; --ks3-accent-hover: #FFC2A8;
  --ks3-ok: #3CC477; --ks3-ok-text: #86E6AC; --ks3-ok-tint: #15301F;
  --ks3-alert: #FFC53D; --ks3-alert-text: #FFDC85; --ks3-alert-tint: #33290F; --ks3-alert-border: #D9821A;
  --ks3-stretch: #9C7BFF; --ks3-stretch-text: #C2ADFF; --ks3-stretch-tint: #261D3D; --ks3-stretch-rule: #44386A;
  --ks3-blue: #6C8EFF; --ks3-blue-text: #A8C0FF; --ks3-blue-tint: #1B2440;
  --ks3-on-dark: #16120E; /* ink-filled controls (reveal, check, retry) flip to light fills in dark mode, so their label flips dark */
  color-scheme: dark;
}"""

_KS4_THEME_CSS_MEDIA_BLOCK = """@media (prefers-color-scheme: dark) {
  .rd[data-mode="ks3"]:not([data-theme="light"]):not([data-theme="light"] .rd) {
    --ks3-ground: #16120E; --ks3-card: #1F1A15; --ks3-band: #2A231C; --ks3-inset: #231D17; --ks3-row-dim: #1B1611;
    --ks3-rule: #3E352C; --ks3-rule-strong: #5E5246; --ks3-option-border: #4F443A; --ks3-option-spent: #2B241D;
    --ks3-ink: #F3ECE0; --ks3-ink-body: #E3D9CA; --ks3-ink-muted: #C2B6A6; --ks3-ink-faint: #B0A493; --ks3-ink-ghost: #8A7F72;
    --ks3-accent: #F07A4E; --ks3-accent-text: #FF9E78; --ks3-accent-tint: #3A2218; --ks3-accent-hover: #FFC2A8;
    --ks3-ok: #3CC477; --ks3-ok-text: #86E6AC; --ks3-ok-tint: #15301F;
    --ks3-alert: #FFC53D; --ks3-alert-text: #FFDC85; --ks3-alert-tint: #33290F; --ks3-alert-border: #D9821A;
    --ks3-stretch: #9C7BFF; --ks3-stretch-text: #C2ADFF; --ks3-stretch-tint: #261D3D; --ks3-stretch-rule: #44386A;
    --ks3-blue: #6C8EFF; --ks3-blue-text: #A8C0FF; --ks3-blue-tint: #1B2440;
    --ks3-on-dark: #16120E; /* ink-filled controls (reveal, check, retry) flip to light fills in dark mode, so their label flips dark */
  color-scheme: dark;
  }
}
"""


def build_ks4_theme_css():
    text = open(os.path.join(DESIGN_DIR, "ks4-theme.css"), encoding="utf-8").read()
    if _KS4_THEME_CSS_MEDIA_BLOCK not in text:
        raise SystemExit(
            "build_ks4: ks4-theme.css's @media (prefers-color-scheme: dark) "
            "block moved or is missing — the THEME RUN strip in "
            "build_ks4_theme_css() needs to be re-read against the new "
            "text before this can be re-run.")
    text = text.replace(_KS4_THEME_CSS_MEDIA_BLOCK, "", 1)
    # ⊕ D8 (theme-run audit, 27 Sep 2026). The surviving non-media block
    # (`.rd[data-mode="ks3"][data-theme="dark"], [data-theme="dark"]
    # .rd[data-mode="ks3"] { ... color-scheme: dark; }`) is unconditional —
    # `data-theme="dark"` is written by THEME_HEAD/theme.js on every load,
    # in every medium — so printing one of these 54 pages in dark mode
    # printed the dark ground and cream ink verbatim (rule 7: print is
    # always light text on white). Same build-time transform this function
    # already applies to the OS-media block above, for the same reason:
    # never a hand-edit of Design's frozen file, only a wrap of the copy.
    if _KS4_THEME_CSS_DARK_BLOCK not in text:
        raise SystemExit(
            "build_ks4: ks4-theme.css's surviving [data-theme=\"dark\"] "
            "block moved or is missing — the D8 @media screen wrap in "
            "build_ks4_theme_css() needs to be re-read against the new "
            "text before this can be re-run.")
    text = text.replace(
        _KS4_THEME_CSS_DARK_BLOCK,
        "@media screen {\n" + _KS4_THEME_CSS_DARK_BLOCK + "\n} /* @media screen — D8 */",
        1)
    text += (
        "\n/* ⊕ THEME RUN (26 Sep 2026) — the @media (prefers-color-scheme: "
        "dark) block Design's own ks4-theme.css carried here has been "
        "stripped by build_ks4.build_ks4_theme_css() at build time (never "
        "hand-edited in Design's frozen source under docs/ks4/design-"
        "reference/pilot/). See THEME-CONTRACT.md rule 3 and the comment "
        "above KS4_DARK_MODE_FIXES in build_ks4.py for why: it guarded on "
        "the .rd element's own (always-unset) data-theme attribute, not on "
        "html[data-theme], so it fired from the OS setting regardless of "
        "the site's own stored theme choice. The surviving non-media block "
        "above (both its own-attribute and [data-theme=\"dark\"] ancestor "
        "selector forms) is unchanged and covers every case this did. */\n"
    )
    return text


def build_shared_assets():
    written = {}
    for name, content in (
        ("ks4-ds.css", build_ds_css()),
        ("ks4-theme.css", build_ks4_theme_css()),
        ("ks4-diagrams.js", build_ks4_diagrams_js()),
        ("ks4-lib.js", build_ks4_lib_js()),
    ):
        path = _shared(name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        written[name] = path
    return written


# ═══════════════════════════════════════════════════════════════════════
# STEP C — shared/ks4-lesson.css: every per-page <style> block, deduplicated
# ═══════════════════════════════════════════════════════════════════════
_STYLE_RE = re.compile(r"<style>(.*?)</style>", re.S)


def collect_lesson_css(all_files):
    seen = set()
    chunks = []
    for fname in all_files:
        text = open(os.path.join(DESIGN_DIR, fname), encoding="utf-8").read()
        helmet_end = text.find("</helmet>")
        helmet = text[:helmet_end] if helmet_end != -1 else text
        for m in _STYLE_RE.finditer(helmet):
            block = m.group(1).strip()
            if not block or block in seen:
                continue
            seen.add(block)
            chunks.append("/* from %s */\n%s" % (fname, block))
    header = ("/* shared/ks4-lesson.css — GENERATED by build_ks4.py: every "
               "distinct <style> block found in the\n"
               "   <helmet> of the 14 lessons + 11 blocks, deduplicated "
               "(exact text match), first-seen order.\n"
               "   Never hand-edit; re-run build_ks4.py. */\n\n")
    return header + "\n\n".join(chunks) + "\n" + KS4_DARK_MODE_FIXES + KS4_CHIP_CSS


def collect_batch_lesson_css(base_dir, files, out_name):
    """The batch-engine equivalent of `collect_lesson_css()` above, for a
    non-pilot batch's OWN `ks4-lesson-<batch>.css` (docs/ks4/batch-engine.md
    requirement 2): every distinct `<style>` block in that batch's own
    lesson files, deduplicated against EACH OTHER only — not against the
    pilot's `ks4-lesson.css` or the 11 shared blocks' styles, which every
    KS4 page (pilot or batch) already loads separately. No dark-mode-fix /
    route-chip CSS is appended here — both are already shipped once, in the
    pilot's shared file, and every batch page loads that file too."""
    seen = set()
    chunks = []
    for fname in files:
        text = open(os.path.join(base_dir, fname), encoding="utf-8").read()
        helmet_end = text.find("</helmet>")
        helmet = text[:helmet_end] if helmet_end != -1 else text
        for m in _STYLE_RE.finditer(helmet):
            block = m.group(1).strip()
            if not block or block in seen:
                continue
            seen.add(block)
            chunks.append("/* from %s */\n%s" % (fname, block))
    header = ("/* shared/%s — GENERATED by build_ks4.py --batch: every "
              "distinct <style> block found in the\n"
              "   <helmet> of this batch's own lesson files, deduplicated "
              "(exact text match), first-seen order.\n"
              "   Never hand-edit; re-run build_ks4.py --batch. */\n\n"
              % out_name)
    if not chunks:
        return header
    return header + "\n\n".join(chunks) + "\n"


# ── Dark-mode legibility fixes (Mide's ruling, Experience run item 13;
# ⊕ 26 Sep 2026, KS4 pilot job 3, docs/ks4/pilot-build-contract.md).
# ADDITIVE ONLY — never edits Design's shared/ks4-theme.css or
# shared/ks4-ds.css in place; appended here because ks4-lesson.css is the
# LAST <link> on every pilot page, so an equal-specificity rule here wins by
# source order alone. All three reuse EXISTING dark-palette tokens already
# defined in shared/ks4-theme.css; nothing new is minted.
#
# ⊕ THEME RUN (26 Sep 2026, THEME-CONTRACT.md rule 3) — each of these three
# USED to carry a `@media (prefers-color-scheme: dark)` block (guarded
# `.rd[data-mode="ks3"]:not([data-theme="light"])`) alongside the plain
# `[data-theme="dark"]` selector. That guard checks the `.rd` element's OWN
# `data-theme` attribute — bound to `{{ theme }}`, a per-lesson mount prop
# that is always `"auto"` in production and so never actually written — so
# `:not([data-theme="light"])` was always true, and the OS media query fired
# regardless of the SITE'S OWN stored theme choice: a student who chose
# Light, on a phone set to dark, still got these dark-mode overrides.
# THEME-CONTRACT.md rule 3 is explicit that a `@media (prefers-color-scheme:
# dark)` block "must NEVER apply on its own any more" once a page always
# carries `data-theme` on `<html>` (these pages do, via THEME_HEAD) — so the
# media-query path is removed outright, not merely re-guarded. The surviving
# selector, `[data-theme="dark"] .rd[data-mode="ks3"]`, matches whenever the
# ANCESTOR `<html>` carries `data-theme="dark"` — which is exactly and only
# what theme.js/THEME_HEAD ever write — so System mode (which theme.js
# resolves from the OS media query itself, once, into that same attribute)
# still reaches these three fixes; only the double-application through the
# `.rd`'s own dead attribute is gone.
KS4_DARK_MODE_FIXES = """
/* ⊕ D8 (theme-run audit, 27 Sep 2026) — every rule below is guarded inside
   `@media screen`. All five fixes key off `[data-theme="dark"]` (directly,
   or via `html[data-theme="dark"] body`'s inherited colour), and the
   attribute is unconditional — it is written by THEME_HEAD/theme.js on
   every load of every one of these 54 pages, in EVERY medium, including
   print. Un-guarded, printing a pilot page in dark mode printed the dark
   ground (`html[data-theme="dark"] body`'s own rule a few lines down being
   the clearest case: it sets print's own text colour to the dark-mode
   cream) with "print background graphics" on, or faint low-contrast text
   without it — both wrong; rule 7 is print stays light text on white
   regardless of the viewed theme. Matches the guard `shared/ks3-theme.css`
   already uses for the identical reason. */
@media screen {
/* ⊕ KS4-DARK-1 (DEPARTURES-PILOT.md) — disabled .ks3-reveal-btn/.ks3-retry
   measured 2.01:1 in dark mode (contrast_audit.py, disabled-control floor
   3.0). Design's own compiled Component sets `style="opacity:.45"` inline
   per instance when a control is disabled; that inline opacity fades an
   (in dark mode) light-cream fill and a near-black label toward the same
   dark page ground by the SAME factor, collapsing their mutual contrast
   from ~16:1 down to ~2:1. Only `!important` in a stylesheet can outrank
   an inline style, so this raises that one number. .7 keeps the control
   visibly duller than its enabled (opacity 1) state — still reads as
   "disabled" — while composited contrast clears the floor: measured
   4.57:1.

   ⊕ THEME RUN (26 Sep 2026) — UNGATED from dark-only, having measured the
   IDENTICAL collapse in LIGHT mode (1.60:1, same floor 3.0) the first time
   this run's `contrast_audit.py --themes light,dark` actually reached a
   disabled control on these 54 pages. The mechanism is symmetric, not
   theme-specific: these buttons' filled/label pair is (fill=--ks3-ink,
   label=--ks3-ground) in EITHER theme — a near-black fill under
   cream-coloured label text — and `--ks3-ground` in light mode IS the
   page's own cream ground, so opacity-fading the label toward that same
   page ground converges label-onto-page just as catastrophically as the
   dark-mode case converges it onto the dark ground. This was not
   introduced by the theme run; it is a pre-existing defect this run's
   dual-theme, real-disabled-state measurement was the first thing to
   surface (Decisions/Deviations, ks4-pilot theme-run report). One
   unconditional rule now covers both floors: measured 4.57:1 dark,
   3.03:1 light.

   `.ks3-check-btn:disabled` joins the same rule for the same reason,
   found by the same sweep — a ghost-style button (cream fill, ink label,
   ~12:1 apart) whose SAME opacity:.45 fade collapses it to 2.76:1 in
   LIGHT mode only (its dark pairing already cleared the floor at .45,
   so raising it here only widens that margin, never regresses it). */
.ks3-reveal-btn:disabled,
.ks3-retry:disabled,
.ks3-check-btn:disabled {
  opacity: .7 !important;
}

/* ⊕ KS4-DARK-2 (DEPARTURES-PILOT.md) — the end-matter `.ks3-tutor` card's
   h2/p measured 2.35:1 in dark mode (floor 3.0, both text large enough to
   qualify — see ks4-ds.css's own comment on the 19px/700 reclassification
   for the light-mode equivalent of this exact defect). `--ks3-ink` (light
   cream, #F3ECE0) and `--ks3-accent` (#F07A4E) BOTH flip light under the
   dark remap, so ink-on-accent — dark text on a mid orange in light mode —
   becomes light-on-light in dark mode. `--ks3-on-dark` (#16120E) is
   Design's own token for precisely this situation ("ink-filled controls
   ...flip to light fills in dark mode, so their label flips dark",
   shared/ks4-theme.css) — the accent card is exactly such a filled, bright
   surface. Measured 6.74:1. Nothing minted. */
.rd[data-mode="ks3"][data-theme="dark"] .ks3-endmatter .ks3-tutor h2,
.rd[data-mode="ks3"][data-theme="dark"] .ks3-endmatter .ks3-tutor p,
[data-theme="dark"] .rd[data-mode="ks3"] .ks3-endmatter .ks3-tutor h2,
[data-theme="dark"] .rd[data-mode="ks3"] .ks3-endmatter .ks3-tutor p {
  color: var(--ks3-on-dark);
}

/* ⊕ KS4-DARK-3 (DEPARTURES-PILOT.md) — the Ks4Write rung's bare
   `<textarea>` AND the FIFA-method calc rungs' bare `<input>` fields
   (Ks4Choice/Ks4Cfifa's per-line numeric/formula inputs, e.g.
   `#np-q1-line0`, `#<slug>-r2n`) carry no `::placeholder` rule anywhere in
   ks4-ds.css or ks4-theme.css, so both fall through to Chrome's own
   UA-default placeholder grey (~#757575) — measured 3.75:1 on
   `--ks3-card` (textarea) and 4.04:1 on `--ks3-ground` (input) in dark
   mode, both under the 4.5 floor for ordinary text (placeholders are real
   informational text a student reads, per this gate's own docstring).
   Found on all 14 lessons, not just the one this job's contrast_audit
   --only run first measured — contrast_audit.py --quick --gate --only
   "ks4 pilot" (job 4's full-pilot sweep) is what surfaced the `<input>`
   half of this; the fix is the SAME defect, same cause, one extra
   selector. `--ks3-ink-muted` is the SAME token the Write rung's own
   "Your answer" label immediately above its textarea already uses, so
   reusing it here gives every placeholder a properly
   de-emphasized-but-legible tone consistent with that label. Measured
   8.66:1 on --ks3-card, 9.35:1 on --ks3-ground. Nothing minted.

   ⊕ THEME RUN (26 Sep 2026) — UNGATED from dark-only, having measured the
   SAME UA-default placeholder grey failing in LIGHT mode too (4.18:1 on
   --ks3-ground, 4.50:1 on --ks3-card — both under the 4.5 floor; not
   introduced by this run, the same pre-existing gap KS4-DARK-1 above
   turned out to have). `--ks3-ink-muted` already carries its OWN correct
   value in EITHER theme (5.6:1 on light --ks3-ground per its own token
   comment, 8.66/9.35:1 in dark per this rule's original measurement), so
   ONE unconditional rule — not two theme-gated copies — is both correct
   and sufficient: the token resolves per-theme on its own. */
.rd[data-mode="ks3"] input::placeholder,
.rd[data-mode="ks3"] textarea::placeholder {
  color: var(--ks3-ink-muted);
  opacity: 1;
}

/* ⊕ KS4-DARK-4 (THEME RUN, 26 Sep 2026) — the tutor chat overlay
   (#chatOverlay, build_ks3.KS3_CHAT_OVERLAY, mounted verbatim by every one
   of these 54 pages' tutor_block()) ships with NO stylesheet of its own —
   its rules (`.chat-head-info h3`, `.chat-modal`, …) live only in
   shared/styles.css, which these pages do not load (a pre-existing,
   unrelated gap: KS3 lesson pages load it, KS4 pilot pages never have).
   So every one of those rules is a no-op here, and the overlay's h3/p
   render with NO explicit colour of their own — they simply INHERIT
   `body`'s, which ks4-ds.css sets, unscoped, to `--st-ink` (a 3D-Studio
   token bundled in from Design's concatenated tokens export, landing here
   only because build_ds_css() ships her whole chain). `--st-ink` carries
   no dark remap anywhere in this file, so in dark mode the overlay's text
   stayed the SAME near-black (#1A1714) while its background — composited
   straight through, since every layer between it and `body` is
   transparent — correctly followed body's OWN dark ground (#16120E, this
   file's own `html,body` rule below): 1.04:1. `#chatOverlay` sits OUTSIDE
   `.rd[data-mode="ks3"]` (a sibling of #ks4-mount, both direct children of
   `body`), so it cannot see `--ks3-ink`'s `.rd`-scoped dark remap by
   inheritance — CSS custom properties cascade down a subtree, never
   sideways to a sibling — so the value below is that SAME dark ink
   (#F3ECE0, shared/ks4-theme.css) written literally, because the custom
   property itself is out of scope at `body`. Nothing else lives directly
   under `body` outside `.rd` (`.rd` sets its own inline `color`, which
   always wins there regardless of body's), so this cannot touch lesson
   content. Measured 15.98:1. */
html[data-theme="dark"] body {
  color: #F3ECE0;
}

/* ⊕ KS4-DARK-5 (THEME RUN, 26 Sep 2026) — same unstyled-overlay cause as
   KS4-DARK-4, one door down: `#chatOverlay`'s `<input id="ci">` (the chat
   text box) carries no background/border of its own either (again,
   because shared/styles.css never loads here), so it renders as a bare
   NATIVE form control — and `html.style.colorScheme` (set by theme.js/
   THEME_HEAD, needed everywhere else on the page so the OS's own chrome —
   scrollbars, native pickers — matches the site's choice) makes Chrome
   skin that native control with its OWN dark widget theme: a dark grey
   fill (#3B3B3B) under Chrome's OWN placeholder grey (#757575, the exact
   value KS4-DARK-3's docstring already names as the UA default) — 2.43:1,
   under the 4.5 floor. In light mode the same native pairing (white fill,
   #757575 placeholder) already clears it, which is exactly why this
   never needed fixing before: the overlay predates dark mode entirely and
   has no design of its own to give it. Rather than invent one, `color-
   scheme: light` pins the overlay's native controls to the SAME
   appearance they have always had, in either theme — the accurate
   "unchanged" for a component nothing here has redesigned. */
#chatOverlay {
  color-scheme: light;
}
} /* @media screen — D8 */
"""


# ── the header route chip/switcher (Mide's ruling, 27 Sep 2026;
# ks4_rulings.py R12). Every colour is a `--ks3-*` token, so light and dark
# both "just work" the same way the rest of the page does — no separate
# dark-mode block is needed here the way KS4-DARK-1..3 above needed one:
# those three fought an INLINE style Design's own compiled Component sets
# per instance (only `!important` in a stylesheet can outrank an inline
# style); this chip carries no inline colour at all. `summary` is added to
# the page's own focus-visible selector list (html,body's own `<style>`
# block only names button/a/select/input/textarea) so the chip gets the
# SAME outline every other interactive control on the page does. `list-
# style: none` on a `<ul>` is a known VoiceOver/Safari gotcha (it can drop
# the element's implicit list semantics) — `role="list"` on the markup
# restores it explicitly, matching the templates rather than duplicated
# here.
KS4_CHIP_CSS = """
/* ⊕ KS4-CHIP-1 (Mide's ruling, 27 Sep 2026) — replaces the two static
   "Combined · Triple" / "Foundation · Higher" header chips with one
   chip stating the page's own route in words, as a native disclosure.
   Enter/Space toggles a native <details>/<summary> with no script; Tab
   reaches the menu's links (already static <a> elements in the prerendered
   HTML, not a runtime fetch). shared/ks4-runtime.js adds only Esc-to-close
   plus keeping aria-expanded in sync with the open state. */
.ks3-route-switch { position: relative; }
.ks3-route-chip {
  display: inline-flex; align-items: center; gap: 6px; cursor: pointer;
  font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500;
  letter-spacing: .06em; text-transform: uppercase;
  padding: 4px 11px; border-radius: 99px; border: 2px solid var(--ks3-ink);
  color: var(--ks3-ink); background: var(--ks3-card);
  -webkit-tap-highlight-color: transparent;
}
.ks3-route-chip::-webkit-details-marker { display: none; }
.ks3-route-chip::marker { content: ""; }
.ks3-route-chip:hover { border-color: var(--ks3-accent-text); }
.ks3-route-chip:focus-visible { outline: 3px solid var(--ks3-accent-text); outline-offset: 2px; }
.ks3-route-chip svg { flex: 0 0 auto; transition: transform .15s ease; }
.ks3-route-switch[open] > .ks3-route-chip svg { transform: rotate(180deg); }
.ks3-route-menu {
  /* ⚠️ `display: none` here is LOAD-BEARING, not a default this selector
     happens to start from. The browser's own UA stylesheet already hides a
     closed <details>'s non-summary content (`details:not([open]) >
     *:not(summary) { display: none }`), but an AUTHOR stylesheet's rule
     beats a UA rule at equal-or-lower specificity regardless of source
     order — an unconditional `display: flex` here would force the menu
     visible EVEN WHILE CLOSED (found live via ks4_parity's G-keyboard
     layer: 3 always-focusable <a> with non-zero rects). `[open] >` below
     is the ONLY rule that may ever show it. */
  display: none;
  list-style: none; margin: 6px 0 0; padding: 6px;
  flex-direction: column; gap: 2px;
  position: absolute; top: 100%; left: 0; z-index: 5;
  min-width: 15rem; max-width: min(20rem, calc(100vw - 32px));
  background: var(--ks3-card); border: 2px solid var(--ks3-option-border);
  border-radius: var(--ks3-r-panel); box-shadow: 0 8px 24px rgba(0, 0, 0, .18);
}
.ks3-route-switch[open] > .ks3-route-menu { display: flex; }
.ks3-route-menu a {
  display: block; padding: 9px 10px; border-radius: 8px; min-height: 44px;
  font-family: var(--ks3-font-body); font-size: 15px; font-weight: 500;
  line-height: 1.3; color: var(--ks3-ink); text-decoration: none;
}
.ks3-route-menu a:hover { background: var(--ks3-band); }
.ks3-route-menu a:focus-visible { outline: 3px solid var(--ks3-accent-text); outline-offset: -3px; background: var(--ks3-band); }
@media (max-width: 400px) {
  .ks3-route-menu { left: 0; right: auto; }
}
"""


# ── the header route chip/switcher (Mide's ruling, 27 Sep 2026;
# ks4_rulings.py R12). Every colour is a `--ks3-*` token, so light and dark
# both "just work" the same way the rest of the page does — no separate
# dark-mode block is needed here the way KS4-DARK-1..3 above needed one:
# those three fought an INLINE style Design's own compiled Component sets
# per instance (only `!important` in a stylesheet can outrank an inline
# style); this chip carries no inline colour at all. `summary` is added to
# the page's own focus-visible selector list (html,body's own `<style>`
# block only names button/a/select/input/textarea) so the chip gets the
# SAME outline every other interactive control on the page does. `list-
# style: none` on a `<ul>` is a known VoiceOver/Safari gotcha (it can drop
# the element's implicit list semantics) — `role="list"` on the markup
# restores it explicitly, matching the templates rather than duplicated
# here.
KS4_CHIP_CSS = """
/* ⊕ KS4-CHIP-1 (Mide's ruling, 27 Sep 2026) — replaces the two static
   "Combined · Triple" / "Foundation · Higher" header chips with one
   chip stating the page's own route in words, as a native disclosure.
   Enter/Space toggles a native <details>/<summary> with no script; Tab
   reaches the menu's links (already static <a> elements in the prerendered
   HTML, not a runtime fetch). shared/ks4-runtime.js adds only Esc-to-close
   plus keeping aria-expanded in sync with the open state. */
.ks3-route-switch { position: relative; }
.ks3-route-chip {
  display: inline-flex; align-items: center; gap: 6px; cursor: pointer;
  font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500;
  letter-spacing: .06em; text-transform: uppercase;
  padding: 4px 11px; border-radius: 99px; border: 2px solid var(--ks3-ink);
  color: var(--ks3-ink); background: var(--ks3-card);
  -webkit-tap-highlight-color: transparent;
}
.ks3-route-chip::-webkit-details-marker { display: none; }
.ks3-route-chip::marker { content: ""; }
.ks3-route-chip:hover { border-color: var(--ks3-accent-text); }
.ks3-route-chip:focus-visible { outline: 3px solid var(--ks3-accent-text); outline-offset: 2px; }
.ks3-route-chip svg { flex: 0 0 auto; transition: transform .15s ease; }
.ks3-route-switch[open] > .ks3-route-chip svg { transform: rotate(180deg); }
.ks3-route-menu {
  /* ⚠️ `display: none` here is LOAD-BEARING, not a default this selector
     happens to start from. The browser's own UA stylesheet already hides a
     closed <details>'s non-summary content (`details:not([open]) >
     *:not(summary) { display: none }`), but an AUTHOR stylesheet's rule
     beats a UA rule at equal-or-lower specificity regardless of source
     order — an unconditional `display: flex` here would force the menu
     visible EVEN WHILE CLOSED (found live via ks4_parity's G-keyboard
     layer: 3 always-focusable <a> with non-zero rects). `[open] >` below
     is the ONLY rule that may ever show it. */
  display: none;
  list-style: none; margin: 6px 0 0; padding: 6px;
  flex-direction: column; gap: 2px;
  position: absolute; top: 100%; left: 0; z-index: 5;
  min-width: 15rem; max-width: min(20rem, calc(100vw - 32px));
  background: var(--ks3-card); border: 2px solid var(--ks3-option-border);
  border-radius: var(--ks3-r-panel); box-shadow: 0 8px 24px rgba(0, 0, 0, .18);
}
.ks3-route-switch[open] > .ks3-route-menu { display: flex; }
.ks3-route-menu a {
  display: block; padding: 9px 10px; border-radius: 8px; min-height: 44px;
  font-family: var(--ks3-font-body); font-size: 15px; font-weight: 500;
  line-height: 1.3; color: var(--ks3-ink); text-decoration: none;
}
.ks3-route-menu a:hover { background: var(--ks3-band); }
.ks3-route-menu a:focus-visible { outline: 3px solid var(--ks3-accent-text); outline-offset: -3px; background: var(--ks3-band); }
@media (max-width: 400px) {
  .ks3-route-menu { left: 0; right: auto; }
}
"""


# ═══════════════════════════════════════════════════════════════════════
# STEP D — the browser-side template compiler (extends student_template.py's
# _COMPILE_JS with `dc-import` → `t: 'child'`).
# ═══════════════════════════════════════════════════════════════════════
_COMPILE_JS = r"""
(function (html) {
  var t = document.createElement('template');
  t.innerHTML = html;

  function interp(s) {
    if (s.indexOf('{{') === -1) { return s; }
    var parts = [], re = /\{\{\s*([^}]+?)\s*\}\}/g, last = 0, m;
    while ((m = re.exec(s)) !== null) {
      if (m.index > last) { parts.push(s.slice(last, m.index)); }
      parts.push({e: m[1]});
      last = m.index + m[0].length;
    }
    if (last < s.length) { parts.push(s.slice(last)); }
    return {parts: parts};
  }

  var n = 0;
  function walk(node) {
    if (node.nodeType === 3) {
      var v = node.nodeValue;
      if (!v.trim()) { return null; }
      return {t: '#', v: interp(v)};
    }
    if (node.nodeType !== 1) { return null; }

    var tag = node.tagName.toLowerCase();
    var idx = n++;

    if (tag === 'sc-if') {
      return {t: 'if', i: idx, e: (node.getAttribute('value') || '')
                .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              c: kids(node)};
    }
    if (tag === 'sc-for') {
      return {t: 'for', i: idx,
              e: (node.getAttribute('list') || '')
                 .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              as: node.getAttribute('as') || 'it', c: kids(node)};
    }
    if (tag === 'x-import') {
      return {t: 'import', i: idx,
              from: node.getAttribute('component-from-global-scope') || '',
              size: node.getAttribute('size') || ''};
    }
    if (tag === 'dc-import') {
      var comp = node.getAttribute('name') || '';
      var attrs = {};
      for (var k2 = 0; k2 < node.attributes.length; k2++) {
        var at2 = node.attributes[k2], name2 = at2.name, val2 = at2.value;
        if (name2 === 'name' || name2 === 'hint-placeholder-count' ||
            name2 === 'hint-placeholder-val' || name2 === 'hint-size' ||
            name2 === 'sc-name') { continue; }
        attrs[name2] = interp(val2);
      }
      return {t: 'child', i: idx, comp: comp, a: attrs};
    }

    var out = {t: tag, i: idx, a: {}, c: kids(node)};
    for (var k = 0; k < node.attributes.length; k++) {
      var at = node.attributes[k], name = at.name, val = at.value;
      if (name === 'hint-placeholder-count' || name === 'hint-placeholder-val' ||
          name === 'hint-size' || name === 'sc-name') { continue; }
      if (name === 'onclick') { out.on = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'onchange' || name === 'oninput') {
        out.onch = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue;
      }
      if (name === 'ref') { out.ref = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'style-hover') { out.hov = val; continue; }
      out.a[name] = interp(val);
    }
    if (!Object.keys(out.a).length) { delete out.a; }
    if (!out.c.length) { delete out.c; }
    return out;
  }

  function kids(node) {
    var out = [];
    for (var i = 0; i < node.childNodes.length; i++) {
      var c = walk(node.childNodes[i]);
      if (c) { out.push(c); }
    }
    return out;
  }

  var roots = [];
  for (var i = 0; i < t.content.childNodes.length; i++) {
    var r = walk(t.content.childNodes[i]);
    if (r) { roots.push(r); }
  }
  return JSON.stringify({n: n, roots: roots});
})(%s)
"""


def template_and_logic(path):
    """Split a `.dc.html` into (template markup, logic-class source). Same
    slicing rule as student_template.py's — the template starts at
    `<helmet`, NOT after it, because `data-dc-tpl` numbering (and every
    node index this build relies on) is stamped from zero across the whole
    document, helmet included."""
    src = open(path, encoding="utf-8").read()
    a = src.index("<helmet")
    m = re.search(r'<script[^>]*data-dc-script[^>]*>', src)
    if not m:
        raise SystemExit("build_ks4: %s has no <script data-dc-script>" % path)
    tpl = src[a:m.start()]
    logic = src[m.end():]
    logic = logic[:logic.rindex("</script>")]
    return tpl.strip(), logic.strip()


def compile_template_text(page, tpl_text):
    got = json.loads(page.eval(_COMPILE_JS % json.dumps(tpl_text)))
    return {"n": got["n"], "roots": got["roots"]}


# ═══════════════════════════════════════════════════════════════════════
# STEP E — compile the 11 blocks
# ═══════════════════════════════════════════════════════════════════════
_BLOCK_R2 = {
    "Ks4Choice": ks4_rulings.apply_r2_choice,
    "Ks4Write": ks4_rulings.apply_r2_write,
    "Ks4Ladder": ks4_rulings.apply_r2_ladder,
    # batch 4: Ks4Guess's figure line is byte-identical to Ks4Choice's.
    "Ks4Guess": ks4_rulings.apply_r2_choice,
}


def compile_block(page, name, design_dir=None):
    # `design_dir` is None for the pilot and batches 2/3 (the pilot's own
    # DESIGN_DIR, unchanged). A batch that brings its own shared blocks
    # (batch 4+: ks4_lessons.batch_blocks) passes its own directory.
    path = os.path.join(design_dir or DESIGN_DIR, name + ".dc.html")
    tpl, logic = template_and_logic(path)
    if name == "Ks4Chrome":
        # ⊕ R-TOPBAR (Stage B, phone run 28 Sep 2026) — FIRST, and it
        # replaces the whole header nav with the ONE pupil top bar. It
        # RETIRES the three rulings that used to run here, in this order:
        #     tpl = ks4_rulings.apply_r_breadcrumb(tpl)
        #     tpl = ks4_rulings.apply_r15_theme_slot(name, tpl)
        #     tpl = ks4_rulings.apply_r_brand_chrome(tpl)
        # — their targets (the README.md crumbs, the nav's closing bytes, the
        # old brand anchor) are all inside the nav R-TOPBAR removes, so each
        # would now fail loud on a missing anchor. See ks4_rulings.py.
        tpl = ks4_rulings.apply_r_topbar(tpl)
        logic = ks4_rulings.apply_r_topbar_logic(logic)
    if name == "Ks4End":
        # ⊕ R-BRAND — the footer's sign-off says "MrBadmus".
        tpl = ks4_rulings.apply_r_brand_footer(tpl)
        # ⊕ R10 (ks4_rulings.py) — D1 fix: the "Ask about this lesson" CTA
        # becomes a real button carrying the hook mrbadmus.v2.js binds.
        tpl = ks4_rulings.apply_r10_tutor_cta(tpl)
        # ⊕ D2 fix — drop a connects entry whose target has no page on the
        # current route (see ks4_rulings.py's comment above
        # apply_r_end_connects_filter for why this lives here, on the
        # shared block, rather than on any of the 14 lessons' own logic).
        logic = ks4_rulings.apply_r_end_connects_filter(logic)
    if name in _BLOCK_R2:
        logic = _BLOCK_R2[name](logic)
    if name == "Ks4Ladder":
        # ⊕ R16 (ks4_rulings.py) — the Apply rung reads "63 000"/"63,000".
        logic = ks4_rulings.apply_r16_ladder_parse(logic)
    if name == "Ks4Triangle":
        # ⊕ B4-TRI-TOP (ks4_batch_rulings.py) — batch 4's own block; the pilot has none.
        logic = ks4_batch_rulings.apply_triangle_top_label(logic)
    if name == "Ks4Practice":
        # ⊕ B-PRACTICE-PARSE (ks4_batch_rulings.py) — R16 for the new block.
        logic = ks4_batch_rulings.apply_practice_parse(logic)
    if name == "Ks4Sort":
        # ⊕ R17 (ks4_rulings.py) — report completion so the rail stop ticks.
        logic = ks4_rulings.apply_r17_sort_report(logic)
    template = compile_template_text(page, tpl)
    return {"template": template, "logic": logic}


# ═══════════════════════════════════════════════════════════════════════
# STEP F — compile the 14 lessons
# ═══════════════════════════════════════════════════════════════════════
def compile_lesson(page, lesson, report):
    path = os.path.join(DESIGN_DIR, lesson["design_file"])
    tpl, logic = template_and_logic(path)

    # structural template edits BEFORE the browser compile — removing a node
    # renumbers everything after it (student_template.py's rule, carried
    # over unchanged: R1/R6/R7/R12/R14 all touch the template, so they all
    # run here).
    tpl = ks4_rulings.apply_r1_route_selector(lesson["design_file"], tpl)
    tpl = ks4_rulings.apply_r12_route_chip(lesson["slug"], tpl)
    tpl, r9_fired = ks4_rulings.apply_r9_badge_gate(lesson["slug"], tpl)
    # ⊕ D11 (theme-run audit, 27 Sep 2026): R15 (the theme slot) moved OFF
    # this per-lesson hero row and into the shared Ks4Chrome block's own
    # top header nav — see ks4_rulings.apply_r15_theme_slot's own comment.
    # It is applied once, in compile_block()'s "Ks4Chrome" branch below,
    # not per lesson.
    ks4_rulings.check_r3_ready_unused(logic)
    draft_tip = None
    if lesson["slug"] == "nanoparticles":
        tpl = ks4_rulings.apply_r5_nanoparticles_spec(tpl)
    if lesson["slug"] == "series-parallel-circuits":
        tpl = ks4_rulings.apply_r6_rtotal_chip(tpl)
        tpl = ks4_rulings.apply_r13_approved_exam_tip(lesson["design_file"], tpl)
        logic = ks4_rulings.apply_r13_exam_tip_logic(lesson["design_file"], logic)
    if lesson["slug"] == "resistors":
        tpl = ks4_rulings.apply_r13_approved_exam_tip(lesson["design_file"], tpl)
        logic = ks4_rulings.apply_r13_exam_tip_logic(lesson["design_file"], logic)
    if lesson["slug"] == "metals-alloys":
        logic = ks4_rulings.apply_r8_model_data(logic)
    spec_text = SPEC_TEXT.get(lesson["slug"])
    if spec_text is not None:
        # ⊕ D13 (theme-run audit, 27 Sep 2026): the TEMPLATE FILE on disk
        # still carries Design's original, un-prefixed literal —
        # `apply_r14_spec_number` has to find THAT to swap in the
        # `{{ specEyebrow }}`/`{{ specNote }}` placeholder, not the new
        # (8464)-carrying render value. See `old_combined_spec_text()`.
        old_spec = old_combined_spec_text(lesson["slug"])
        tpl = ks4_rulings.apply_r14_spec_number(
            lesson["slug"], tpl, old_spec["eyebrow"], old_spec["keynote"])

    logic, tpl, slug_renamed = ks4_rulings.apply_r_slug(lesson["slug"], logic, tpl)
    logic, n_prev, n_next = ks4_rulings.apply_r_prevnext(lesson["design_file"], logic)
    logic, connects_targets = ks4_rulings.apply_r_connects(lesson["design_file"], logic)

    tpl = ks4_science_rulings.apply("template", lesson["slug"], tpl)
    ks4_science_rulings.expect_present("template", lesson["slug"], tpl)
    logic = ks4_science_rulings.apply("logic", lesson["slug"], logic)
    ks4_science_rulings.expect_present("logic", lesson["slug"], logic)

    # ⊕ R18 (rule 1) — the two-option "Start here" guess. AFTER the science
    # rulings: several of them correct old-opener text, and must still fire.
    tpl, logic, r18_fired = ks4_rulings.apply_r18_start_here(
        lesson["slug"], lesson["design_file"], tpl, logic)

    template = compile_template_text(page, tpl)

    block_map = lesson.get("block_map", {})
    classified = classify_lesson_sections(template, lesson["slug"], block_map)

    report.append(dict(slug=lesson["slug"], slug_renamed=slug_renamed,
                        r9_fired=r9_fired, r18_fired=r18_fired,
                        has_prev=bool(n_prev), has_next=bool(n_next),
                        connects=connects_targets, draft_tip=draft_tip,
                        sections=classified))
    return {"template": template, "logic": logic, "draft_tip": draft_tip,
            "uses_guess": GUESS_IMPORT in tpl}


def classify_lesson_sections(template, slug, block_map, unwrap_route_if=False):
    def find_lesson_div(nodes):
        for n in nodes:
            if n.get("t") == "div" and ks4_blocks._class_of(n) == "ks3-lesson":
                return n
            found = find_lesson_div(n.get("c") or [])
            if found is not None:
                return found
        return None

    lesson_div = find_lesson_div(template["roots"])
    if lesson_div is None:
        raise SystemExit("build_ks4: %s has no .ks3-lesson div to classify" % slug)
    out = []
    idx = 0
    for child in lesson_div.get("c") or []:
        # ⊕ batch engine (1 Oct 2026) — a `data-route`-tagged top-level
        # section (apply_route_layers, above) is no longer a bare <section>
        # child of .ks3-lesson; it is wrapped in a synthetic `sc-if`. A
        # batch lesson passes `unwrap_route_if=True` so this looks through
        # exactly that one shape (an "if" node with a single child that IS
        # a section/key-fact) and classifies/stamps `data-block` on the
        # INNER node, never on the wrapper (which carries no `a` of its
        # own). ⚠️ Defaults to False and the pilot path never passes True:
        # at least one pilot lesson (states-of-matter's `s-limits`, gated
        # `isHigher`) already has an `sc-if`-wrapped section as a direct
        # `.ks3-lesson` child, and its PRE-EXISTING, already-shipped
        # behaviour is to be silently skipped here (no `data-block`, not
        # counted) — found by trying `unwrap_route_if=True` unconditionally
        # and watching the pilot build fail on it. Changing that gap is out
        # of scope for the batch engine; this flag exists so the batch path
        # gets the new behaviour without moving the pilot's.
        target = child
        if unwrap_route_if and child.get("t") == "if" and len(child.get("c") or []) == 1:
            inner = child["c"][0]
            inner_a = inner.get("a") or {}
            if inner.get("t") == "section" or "data-key-fact" in inner_a:
                target = inner
        a = target.get("a") or {}
        is_section = target.get("t") == "section" or "data-key-fact" in a
        if not is_section:
            continue
        ctype = ks4_blocks.classify_section(target, slug, idx, block_map)
        target.setdefault("a", {})["data-block"] = ctype
        out.append({"index": idx, "id": a.get("id", ""), "type": ctype})
        idx += 1
    return out


# ═══════════════════════════════════════════════════════════════════════
# BATCH ENGINE — the `data-route` template convention (docs/ks4/batch-
# engine.md, requirement 3 of the 1 Oct 2026 batch run). An authored
# lesson's own `.dc.html` may mark ANY element `data-route="higher"` /
# `"triple"` / `"triple-higher"`; at compile time (once per lesson, not
# once per route — the SAME compiled template serves all four routes, with
# the condition evaluated at RUNTIME against the mount's `isHigher`/
# `isTriple` flags, exactly the mechanism `ks4_rulings.apply_r9_badge_gate`
# already uses for the pilot's own three hand-ruled badges) the element is
# wrapped in an `sc-if` on the matching flag and gets a route badge
# inserted as its own first child, reusing the pilot's mono-pill style
# (ks4_rulings.R9_TARGETS's inline-style shape) so a reader sees the exact
# same chip language the pilot already shipped. Pilot lessons never carry
# this attribute, so `apply_route_layers` is called ONLY from the batch
# compile path (`compile_batch_lesson`, below) — never from `compile_lesson`
# — and the pilot's 54 pages cannot be touched by it.
# ═══════════════════════════════════════════════════════════════════════
ROUTE_LAYER_EXPR = {
    "higher": "__rtH",
    "triple": "__rtT",
    "triple-higher": "__rtTH",
}
ROUTE_LAYER_BADGE = {
    "higher": ("Higher",
               "border: 2px solid var(--ks3-stretch); background: var(--ks3-stretch-tint); color: var(--ks3-stretch-text);"),
    "triple": ("Triple",
               "border: 2px solid var(--ks3-blue); background: var(--ks3-blue-tint); color: var(--ks3-blue-text);"),
    "triple-higher": ("Higher · Triple",
                       "border: 2px solid var(--ks3-alert-border); background: var(--ks3-alert-tint); color: var(--ks3-ink);"),
}


def _route_badge_node(kind, next_idx):
    label, style_tail = ROUTE_LAYER_BADGE[kind]
    style = ("display: inline-block; margin: 0 0 8px; font-family: var(--ks3-font-mono); "
             "font-size: 13px; font-weight: 500; letter-spacing: .06em; "
             "text-transform: uppercase; padding: 4px 11px; border-radius: 99px; " + style_tail)
    return {"t": "span", "i": next_idx(),
            "a": {"style": style, "data-route-badge": kind},
            "c": [{"t": "#", "v": label}]}


def apply_route_layers(template):
    """Mutates and returns a compiled `{"n", "roots"}` template: every node
    carrying a `data-route` attribute is replaced by an `sc-if` wrapper on
    the matching runtime flag, holding that SAME node (minus the
    `data-route` attribute, plus a route badge as its new first child).
    Fresh node indices are allocated from `template["n"]` for the synthetic
    if/badge nodes, the same way Chrome's own walker (`_COMPILE_JS`)
    allocates one for every node it visits — so a batch lesson's `dc-import`
    children keep stable, non-colliding indices after this runs."""
    state = {"n": template["n"]}

    def next_idx():
        i = state["n"]
        state["n"] += 1
        return i

    def walk(nodes):
        out = []
        for node in nodes:
            t = node.get("t")
            if t in ("if", "for"):
                if node.get("c"):
                    node["c"] = walk(node["c"])
                out.append(node)
            elif t in ("#", "child"):
                out.append(node)
            else:
                # a regular element node — recurse into children first, so
                # a nested data-route element is handled before this one
                # decides whether to wrap itself.
                if node.get("c"):
                    node["c"] = walk(node["c"])
                a = node.get("a") or {}
                kind = a.pop("data-route", None)
                if a:
                    node["a"] = a
                else:
                    node.pop("a", None)
                if kind is None:
                    out.append(node)
                    continue
                if kind not in ROUTE_LAYER_EXPR:
                    raise SystemExit(
                        "build_ks4.apply_route_layers: unknown "
                        "data-route=%r (expected one of %s)"
                        % (kind, sorted(ROUTE_LAYER_EXPR)))
                badge = _route_badge_node(kind, next_idx)
                node["c"] = [badge] + (node.get("c") or [])
                wrapper = {"t": "if", "i": next_idx(),
                           "e": ROUTE_LAYER_EXPR[kind], "c": [node]}
                out.append(wrapper)
        return out

    template["roots"] = walk(template["roots"])
    template["n"] = state["n"]
    return template


# ═══════════════════════════════════════════════════════════════════════
# BATCH ENGINE — compile ONE authored lesson (docs/ks4/batch-engine.md).
# Deliberately much thinner than `compile_lesson()` above: an authored
# lesson is written DIRECTLY in the final, post-ruling shape (no Route
# <select>, `this.props.mrbPrevNext.prev`/`.next` already in its Component
# class, `KS4.hrefFor('<slug>', R)` already in its own connects array) —
# the whole point of "authors do not hand-write route logic" (contract
# requirement 3) and "authors will simply not include it" (requirement 4)
# is that there is nothing here for a ks4_rulings.py-style fixup pass to
# do. `ks4_science_rulings.apply`/`expect_present` are still called, as
# genuine no-ops today (no row exists for any batch slug) — kept so a
# future batch CAN carry a ruling without this function changing.
# ═══════════════════════════════════════════════════════════════════════
def compile_batch_lesson(page, batch_name, lesson, report):
    path = os.path.join(ks4_lessons.authored_dir(batch_name),
                        lesson.get("source_file", lesson["slug"] + ".dc.html"))
    tpl, logic = template_and_logic(path)
    port_report = {}
    if lesson.get("port_rulings"):
        # Design's own delivery (batch 4): named port rulings, see
        # ks4_batch_rulings.py. Batches 2/3 never carry the flag.
        slug_by_file = {L["source_file"]: L["slug"]
                        for L in ks4_lessons.batch_modules()[batch_name].LESSONS}
        # every other registered lesson, by Design's file name, so a connects link
        # may cross batches (batch 5 -> batch 4) or reach the pilot.
        other_slug_by_file = {}
        for mod in ks4_lessons.batch_modules().values():
            for L in mod.LESSONS:
                other_slug_by_file.setdefault(L["source_file"], L["slug"])
        for L in ks4_lessons.LESSONS:
            other_slug_by_file.setdefault(L.get("design_file", ""), L["slug"])
        tpl, logic, port_report = ks4_batch_rulings.port_lesson(
            lesson, tpl, logic, slug_by_file, other_slug_by_file)

    tpl = ks4_science_rulings.apply("template", lesson["slug"], tpl)
    ks4_science_rulings.expect_present("template", lesson["slug"], tpl)
    logic = ks4_science_rulings.apply("logic", lesson["slug"], logic)
    ks4_science_rulings.expect_present("logic", lesson["slug"], logic)

    template = compile_template_text(page, tpl)
    template = apply_route_layers(template)

    block_map = lesson.get("block_map", {})
    classified = classify_lesson_sections(template, lesson["slug"], block_map,
                                           unwrap_route_if=True)

    report.append(dict(slug=lesson["slug"], sections=classified, **port_report))
    return {"template": template, "logic": logic, "uses_guess": GUESS_IMPORT in tpl}


# ═══════════════════════════════════════════════════════════════════════
# STEP G — prev/next, computed exactly as generate_site_v5.make_pathway_
# subtopic_page does: index neighbours within the ROUTE'S OWN topic list.
# ═══════════════════════════════════════════════════════════════════════
def compute_prev_next(data, lesson, route):
    subject, topic, slug = lesson["subject"], lesson["topic_id"], lesson["slug"]
    lst = data[subject][route].get(topic, [])
    ids = [s["id"] for s in lst]
    if slug not in ids:
        return None, None
    i = ids.index(slug)
    pathway, tier = ROUTE_URL[route]

    def entry(idx):
        if idx < 0 or idx >= len(lst):
            return None
        s = lst[idx]
        return {"href": "/%s/%s/%s/%s/%s.html" % (pathway, tier, subject, topic, s["id"]),
                "label": s["title"]}
    return entry(i - 1), entry(i + 1)


# ═══════════════════════════════════════════════════════════════════════
# STEP H — the rung-1 fallback check (examiner finding, 25 Sep 2026).
# Static analysis only — never changes KS4.find()'s runtime behaviour.
# ═══════════════════════════════════════════════════════════════════════
_FIND_RE = re.compile(r"K\.find\(slug,\s*R\.route,\s*'((?:[^'\\]|\\.)*)'\)")
_JS_UNICODE_RE = re.compile(r"\\u([0-9a-fA-F]{4})")
# ⚠️ SCOPED TO THE r1: LINE, not every K.find in the file. states-of-matter
# has a SECOND, unrelated K.find at its `lim = …` line (feeding an
# isHigher-only widget, not rung 1) — an unscoped regex mislabelled that as
# a "rung1-fallback" in the first version of this check. All 14 lessons
# write `r1: Object.assign(K.find(...) [|| K.find(...)] || {...}, {...}),`
# immediately followed by `r2:` (verified across all 14 by grep before this
# was written), so the text between those two literal keys is exactly
# rung 1's needle(s) and nothing else.
_R1_BLOCK_RE = re.compile(r"r1:\s*(.*?),\s*r2:", re.S)


def _decode_js_string(s):
    s = _JS_UNICODE_RE.sub(lambda m: chr(int(m.group(1), 16)), s)
    return s.replace("\\'", "'")


def extract_rung1_needles(raw_logic_text):
    """Rung 1's needle(s), in the order `K.find(...) || K.find(...)` tries
    them, as WRITTEN in Design's original (pre-ruling) logic text."""
    m = _R1_BLOCK_RE.search(raw_logic_text)
    if not m:
        raise SystemExit(
            "build_ks4.extract_rung1_needles: no `r1: … , r2:` block found "
            "— Design's ladder-rung shape moved; this check needs "
            "re-scoping, not silently returning nothing.")
    return [_decode_js_string(x) for x in _FIND_RE.findall(m.group(1))]


def check_rung1_fallback(data, lesson, needles):
    """For every route this lesson ships on: does the FIRST needle that
    resolves (own-route copy, else TH copy, in K.find's own order) come
    from the route's OWN quiz, or did it fall back to TH? Prints one
    WARNING line per fallback and one per total miss. Returns the count."""
    if not needles:
        return 0
    warnings = 0
    subject, topic, slug = lesson["subject"], lesson["topic_id"], lesson["slug"]
    for route in lesson["routes"]:
        st = find_subtopic(data, subject, route, topic, slug)
        own_qs = [q["q"] for q in (st["quiz"] if st else [])]
        th = find_subtopic(data, subject, "TH", topic, slug)
        th_qs = [q["q"] for q in (th["quiz"] if th else [])]
        resolved = False
        for needle in needles:
            if any(needle in q for q in own_qs):
                resolved = True
                break
            if any(needle in q for q in th_qs):
                print("  WARNING rung1-fallback %s %s needle=%r"
                      % (slug, route, needle))
                warnings += 1
                resolved = True
                break
        if not resolved:
            print("  WARNING rung1-nomatch %s %s — no needle in %r matched "
                  "own-route or TH copy; rung 1 would render with no options"
                  % (slug, route, needles))
            warnings += 1
    return warnings


# ═══════════════════════════════════════════════════════════════════════
# STEP I — page assembly
# ═══════════════════════════════════════════════════════════════════════
def guess_registration_script(compiled_blocks, compiled_lesson):
    """"" unless this lesson mounts Ks4Guess; then its registration script,
    appended after the shared block set (see GUESS_BLOCK_DIR)."""
    if not compiled_lesson.get("uses_guess"):
        return ""
    return "\n" + block_registration_scripts(compiled_blocks, ["Ks4Guess"])


def block_registration_scripts(compiled_blocks, names=None):
    out = []
    for name in (names or BLOCK_NAMES):
        b = compiled_blocks[name]
        out.append(
            "<script>\nwindow.KS4_BLOCKS = window.KS4_BLOCKS || {};\n"
            "(function () {\n%s\n"
            "window.KS4_BLOCKS[%s] = {Component: Component, template: %s};\n"
            "})();\n</script>"
            % (b["logic"], json.dumps(name), json.dumps(b["template"])))
    return "\n".join(out)


def lesson_mount_script(compiled_lesson, route, lesson, prev_next, subject_label):
    prev, nxt = prev_next
    route_switch = compute_route_switch(lesson)
    props = {
        "route": ROUTE_LABEL[route],
        "theme": "auto",
        "showDraft": lesson["review_state"] == "draft",
        "mrbPrevNext": {"prev": prev, "next": nxt},
        "mrbRouteSwitch": route_switch[route],
        "mrbSpecNote": compute_spec_note(lesson["slug"], route),
    }
    if lesson.get("batch", "pilot") != "pilot":
        # Route-layer flags for apply_route_layers()' sc-if wrappers. Passed
        # as mount props (the runtime's scope falls back to props), so a
        # data-route tag works whether or not the lesson's own renderVals
        # exposes isHigher/isTriple. Batch lessons only: pilot props unchanged.
        props["__rtH"] = route in ("CH", "TH")
        props["__rtT"] = route in ("TF", "TH")
        props["__rtTH"] = route == "TH"
    return (
        "<script>\n(function () {\n%s\n"
        "window.MrBadmusKS4Runtime.mount({\n"
        "  into: '#ks4-mount', Component: Component,\n"
        "  props: %s,\n"
        "  template: %s\n"
        "});\n})();\n</script>"
        % (compiled_lesson["logic"], json.dumps(props, sort_keys=True),
           json.dumps(compiled_lesson["template"])))


TUTOR_OVERLAY = None  # filled from build_ks3.KS3_CHAT_OVERLAY in main()


def tutor_block(lesson, route):
    """The tutor overlay, wired like build_ks3.py's `tutor_mount()` — same
    markup, same MrBadmus.init() call shape, same deferred-script /
    DOMContentLoaded ordering. Differs in the subtitle (TUTOR_OVERLAY has
    already had ks4_rulings.apply_r_tutor_label() applied to it in main() —
    D4 fix, "GCSE Science Tutor" not "KS3 Science Tutor") and in the config:
    KS4 pages never pass `keyStage`, matching every OLD KS4 lesson page's own
    `MrBadmus.init({subject, topic})` call (mrbadmus.v2.js reads tier/
    pathway from the STUDENT'S OWN profile for any non-KS3 page, and takes
    no tier/pathway override in its config at all — contract's "supply
    tier/pathway from the route" is honoured by folding the route into
    `topic`, so the tutor has that context even for a student whose own
    profile tier differs from the page they are revising on)."""
    # ⊕ theme run follow-up to R14 (27 Sep 2026): the tutor's context names the
    # section in THIS route's own spec — the same verified SPEC_TEXT the
    # eyebrow and key note read (docs/theme/spec-numbers.md) — so a Triple
    # pupil's tutor is never told the Combined (8464) number.
    note = compute_spec_note(lesson["slug"], route)
    # ⊕ D13 (theme-run audit, 27 Sep 2026) — nanoparticles is the one lesson
    # `compute_spec_note` returns None for (it has no Combined route, so it
    # is deliberately outside SPEC_TEXT — see that dict's own comment), and
    # its fallback used to read `lesson["spec"]` bare ("4.2.4", the same
    # value `ks4_lessons.verify_slugs` checks against the data and which
    # must stay bare there). R5 now puts "(8462)" on the page itself (the
    # eyebrow and the key note); the tutor needs the same code so it is not
    # the one surface still silent about which spec "4.2.4" belongs to.
    spec = (note["keynote"].split(" · ")[0] if note else
            "AQA %s (8462)" % lesson["spec"] if lesson["slug"] == "nanoparticles"
            else "AQA %s" % lesson["spec"])
    # "AQA 4.2.1.4 (8463)" -> "AQA 8463 4.2.1.4", so the context has no nested brackets
    spec = re.sub(r"^AQA (.+) \((\d{4})\)$", r"AQA \2 \1", spec)
    topic = "%s (%s) — %s" % (lesson["title"], spec, ROUTE_LABEL[route])
    cfg = json.dumps({"subject": lesson["subject"], "topic": topic}, sort_keys=True)
    cfg = cfg.replace("<", "\\u003c")
    return (TUTOR_OVERLAY +
            '<script src="/shared/mrbadmus.v2.js" defer fetchpriority="low"></script>\n'
            '<script>document.addEventListener("DOMContentLoaded",'
            'function(){if(window.MrBadmus){MrBadmus.init(%s);}});</script>\n' % cfg)


def render_page(lesson, route, compiled_lesson, block_scripts, prev_next, versions,
                 batch_css="", batch_source_js="", batch_ext_js="", batch_nav_js=""):
    """The four `batch_*` params are the ONLY addition for the batch engine
    (docs/ks4/batch-engine.md) — each is "" by default, and an empty string
    substituted into the template below adds no byte at all (it sits on the
    SAME line as the next fixed tag, never on a line of its own), so the
    pilot's own call site (which never passes them) renders byte-identical
    output to before this parameter existed. A batch call passes e.g.
    `batch_css='<link rel="stylesheet" href="/shared/ks4-lesson-batch-2.css">\\n'`
    — the trailing newline is the caller's to supply, exactly like every
    other multi-line %-substitution in this function. `batch_nav_js` is
    `'<script src="/shared/ks4-nav.js"></script>\\n'` for a batch page and
    "" for the pilot's — see build_ks4_nav_js()'s docstring for why the
    pilot never loads it."""
    url = ks4_lessons.site_url(lesson["slug"], route)
    subject_label = lesson["subject"].capitalize()
    # ⊕ one-mark ruling (13 Sep 2026): "X · MrBadmusAI GCSE Chemistry" →
    # "X | GCSE Chemistry | MrBadmus", brand.title()'s one suffix.
    title = brand.title(lesson["title"], "GCSE %s" % subject_label)
    mount_script = lesson_mount_script(compiled_lesson, route, lesson, prev_next, subject_label)
    # ⊕ THEME RUN (26 Sep 2026, THEME-CONTRACT.md rules 2/3) — THEME_HEAD
    # goes as early as possible (right after <meta charset>, before every
    # stylesheet/blocking script), so no page ever paints the wrong theme
    # even for a flash. The theme script is stamped like every other
    # /shared/ks4-* asset (see KS4_VERSIONED, below). The old hard-coded
    # `background:#FBF3E6` ground (there to avoid a flash before ks4-ds.css
    # loads) becomes token-aware: the light value stays byte-identical, and
    # a dark value (the SAME #16120E `--ks3-ground` shared/ks4-theme.css
    # already uses under [data-theme="dark"]) is keyed on html[data-theme=
    # "dark"] so the ground is right before ANY stylesheet loads, in either
    # theme. theme.js itself is emitted unstamped here, like every other
    # /shared/ks4-* asset on this page — stamp_versions() below rewrites it
    # to /shared/theme.js?v=<hash> using the "theme.js" entry KS4_VERSIONED
    # adds to `versions`.
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
%(theme_head)s
%(theme_script)s
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<link rel="canonical" href="https://mrbadmus.com%(url)s">
%(favicon)s
<link rel="stylesheet" href="/shared/ks4-ds.css">
<link rel="stylesheet" href="/shared/ks4-theme.css">
<link rel="stylesheet" href="/shared/ks4-lesson.css">
%(batch_css)s<link rel="stylesheet" href="/shared/topbar.css">
<style>html,body{margin:0;padding:0;background:#FBF3E6}@media screen{html[data-theme="dark"] body,html[data-theme="dark"]{background:#16120E}}</style>
</head>
<body>
<div id="ks4-mount"></div>
<script src="/shared/ks4-source.js"></script>
%(batch_source_js)s<script src="/shared/ks4-lib.js"></script>
%(batch_nav_js)s<script src="/shared/ks4-diagrams.js"></script>
%(batch_ext_js)s<script src="/shared/ks4-runtime.js"></script>
%(block_scripts)s
%(mount_script)s
<script src="/shared/config.js" defer></script>
%(tutor)s
<script src="/shared/class-entry.js" defer></script>
<script src="/shared/student-bell.js" defer></script>
<script src="/shared/topbar.js" defer></script>
</body>
</html>
""" % dict(title=title, url=url, favicon=KS4_PILOT_FAVICON_LINK,
           theme_head=THEME_HEAD, theme_script=theme_script(),
           block_scripts=block_scripts, mount_script=mount_script,
           tutor=tutor_block(lesson, route),
           batch_css=batch_css, batch_source_js=batch_source_js, batch_ext_js=batch_ext_js,
           batch_nav_js=batch_nav_js)
    import build_ks3
    return build_ks3.stamp_versions(html, versions)


# ═══════════════════════════════════════════════════════════════════════
# STEP J — prerender in headless Chrome: bake the mounted DOM's static text
# into the page, assert zero console errors at 1280 and 360.
# ═══════════════════════════════════════════════════════════════════════
# ⊕ MRB-267 precedent (ks3_smoke.py, ks3_parity.py): `shared/mrbadmus.v2.js`
# pings mrbadmus-backend.onrender.com/api/health on every page load to keep
# Render warm. It is `.catch()`-ed in JS, but Chrome logs the network/CORS
# failure to the console regardless — from a 127.0.0.1 test origin it always
# fails CORS, so this is a property of testing from localhost, not a defect
# in the page. Demoted here exactly as it is in the two gates above.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config_env  # noqa: E402 — shared/config.js's worlds
# The production backend's host, read out of shared/config.js (B2C unit 6).
BACKEND_HOST = config_env.PROD_BACKEND_HOST


def _real_errors(errs):
    # ⊕ D3 fix (26 Sep 2026) — favicon.ico is NO LONGER filtered out here.
    # The pages now carry KS4_PILOT_FAVICON_LINK, so a favicon.ico 404
    # should never occur; if one does, it is a real regression and must
    # fail the build (see the explicit assertion in main(), below), not be
    # silently absorbed the way it was before this fix.
    return [e for e in errs if BACKEND_HOST not in e]


PRERENDER_FREEZE_JS = """
(function () {
  window.setInterval = function () { return 0; };
  window.clearInterval = function () {};
  var seed = 0x9E3779B9;
  Math.random = function () {
    seed = (Math.imul(seed ^ (seed >>> 15), 0x2C1B3C6D) + 0x9E3779B9) | 0;
    return ((seed >>> 0) % 1000000) / 1000000;
  };
})();
"""


# ⊕ R-BRAND (one-mark ruling, 13 Sep 2026) — the baked first paint carries
# brand.py's lockup BYTE FOR BYTE. The runtime draws the same element tree
# from the compiled Ks4Chrome template, but a browser's innerHTML is not
# brand.py's bytes: it adds the runtime's `data-dc-tpl` numbering and
# serialises the boolean `data-mrb-mark` as `data-mrb-mark=""`. The static
# HTML is what brand_one_mark reads (and what a visitor sees before
# ks4-runtime.js runs), so the one serialised anchor is swapped back for the
# exact lockup. Exactly one per page, or the build stops.
_BAKED_BRAND_RE = re.compile(r'<a\b[^>]*\bclass="mrb-brand"[^>]*>.*?</a>', re.S)


def _bake_brand(baked):
    hits = _BAKED_BRAND_RE.findall(baked)
    if len(hits) != 1:
        raise SystemExit("build_ks4 R-BRAND: the baked page carries %d brand "
                         "lockup(s), expected exactly 1" % len(hits))
    return _BAKED_BRAND_RE.sub(lambda m: brand.brand_lockup("/"), baked, count=1)


def prerender_all(cdp, pages):
    """`pages`: [(out_path, url_path)]. Bakes #ks4-mount's innerHTML into
    each file and returns [(url_path, errors_1280, errors_360)]."""
    server, port = cdp.serve(OUT_ROOT)
    results = []
    try:
        with cdp.Browser() as b:
            page = b.attach()
            # ⊕ 26 Sep 2026 — the bake must be DETERMINISTIC. Design's
            # flagships animate on setInterval ticks (L5's electron sea,
            # L8's two-forces model …) and the snapshot used to land on
            # whichever frame the interval had reached, so every rebuild
            # moved a molecule by 0.1 px, dirtied the 54 pages and the
            # manifest, and a receipt-recording gate then refused the tree.
            # For the prerender only, setInterval never fires and
            # Math.random is a fixed-seed PRNG, so the baked frame is frame
            # zero every time. The shipped runtime is untouched: this script
            # exists only inside the build's own headless Chrome.
            page.send("Page.addScriptToEvaluateOnNewDocument", {"source": PRERENDER_FREEZE_JS})
            for out_path, url_path in pages:
                page.set_viewport(1280, 1000)
                page.goto("http://127.0.0.1:%d%s" % (port, url_path))
                # the mount script is a plain synchronous <script>, run by
                # the time `load` fires; poll briefly for belt and braces.
                baked = None
                for _ in range(40):
                    try:
                        renders = page.eval(
                            "document.querySelector('#ks4-mount').getAttribute('data-mrb-renders')")
                    except Exception:
                        renders = None
                    if renders:
                        # ⊕ Stage B — the top bar's "who" slot is emptied in
                        # the SAME eval that reads the mount: what topbar.js
                        # put there depends on who is looking (and on when its
                        # promise settled), so baking it would make the page
                        # nondeterministic and hand every visitor the bake's
                        # signed-out "Sign in" until the runtime redraws.
                        baked = page.eval(
                            "(function(){[].forEach.call(document.querySelectorAll("
                            "'[data-mrb-topbar-who]'),function(s){s.textContent='';});"
                            "return document.querySelector('#ks4-mount').innerHTML;})()")
                        break
                    time.sleep(0.1)
                errors_1280 = _real_errors(page.console_errors())
                page.set_viewport(360, 900)
                time.sleep(0.15)
                errors_360 = _real_errors(page.console_errors())
                results.append((url_path, errors_1280, errors_360))
                if baked is not None:
                    baked = _bake_brand(baked)
                    full = open(out_path, encoding="utf-8").read()
                    full = full.replace('<div id="ks4-mount"></div>',
                                         '<div id="ks4-mount">%s</div>' % baked, 1)
                    with open(out_path, "w", encoding="utf-8") as fh:
                        fh.write(full)
    finally:
        server.shutdown()
    return results


# ═══════════════════════════════════════════════════════════════════════
# BUILD_PILOT — batch 1. This is the EXACT body `main()` always had (the
# whole pilot build, docs/ks4/pilot-build-contract.md), extracted verbatim
# so the batch engine (`main()`, below) can call it as one of N registered
# batches without changing a single byte of what it does. Never add
# anything batch-generic here — add it to `build_batch()` instead, or this
# function (and the pilot's byte-identity) is no longer isolated from the
# rest of the batch engine.
# ═══════════════════════════════════════════════════════════════════════
def build_pilot(freeze=False):
    import ks3_browser as cdp
    import build_ks3

    global TUTOR_OVERLAY
    # ⊕ D4 fix (26 Sep 2026, docs/ks4/pilot-live-audit.md) — the overlay is
    # KS3's own, verbatim, EXCEPT for its subtitle: "KS3 Science Tutor" ->
    # "GCSE Science Tutor" (ks4_rulings.R-TUTOR-LABEL).
    TUTOR_OVERLAY = ks4_rulings.apply_r_tutor_label(build_ks3.KS3_CHAT_OVERLAY)

    print("\n\U0001f9f1  build_ks4 — the KS4 pilot (14 lessons, 54 pages)\n")

    ks4_lessons.verify_slugs()
    print("  ✓ all 14 slugs verified against all_subtopics_*.py")

    ks4_science_rulings.reset_applied()
    data = load_subtopics_by_route()
    source_js, per_slug = build_source_js(data)
    with open(_shared("ks4-source.js"), "w", encoding="utf-8") as fh:
        fh.write(source_js)
    diff_path, n_eq, n_diff = write_source_diff(per_slug)
    print("  ✓ shared/ks4-source.js written; diff vs Design's own: "
          "%d EQUAL, %d DIFFER (%s)" % (n_eq, n_diff, diff_path))

    build_shared_assets()
    print("  ✓ shared/ks4-ds.css, ks4-theme.css, ks4-diagrams.js, ks4-lib.js written")

    all_files = [L["design_file"] for L in ks4_lessons.LESSONS] + \
        [n + ".dc.html" for n in BLOCK_NAMES]
    lesson_css = collect_lesson_css(all_files)
    with open(_shared("ks4-lesson.css"), "w", encoding="utf-8") as fh:
        fh.write(lesson_css)
    print("  ✓ shared/ks4-lesson.css written (%d bytes)" % len(lesson_css))

    # ks4-runtime.js is hand-written engine code (not regenerated here); just
    # confirm it exists before anything tries to load it.
    if not os.path.exists(_shared("ks4-runtime.js")):
        raise SystemExit("build_ks4: shared/ks4-runtime.js is missing")

    import shutil
    dst_shared = os.path.join(OUT_ROOT, "shared")
    os.makedirs(dst_shared, exist_ok=True)
    for name in KS4_OWN_ASSETS:
        src = _shared(name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dst_shared, name))
    print("  ✓ synced %d shared asset(s) into %s (Cloudflare serves "
          "from there, not the repo root)" % (len(KS4_OWN_ASSETS), dst_shared))

    stub_dir = os.path.join(REPO_ROOT, ".ks4_compile_stub")
    os.makedirs(stub_dir, exist_ok=True)
    with open(os.path.join(stub_dir, "stub.html"), "w", encoding="utf-8") as fh:
        fh.write("<!doctype html><html><body></body></html>")

    compiled_blocks = {}
    lesson_report = []
    compiled_lessons = {}
    stub_server, stub_port = cdp.serve(stub_dir)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.goto("http://127.0.0.1:%d/stub.html" % stub_port)
            for name in BLOCK_NAMES:
                compiled_blocks[name] = compile_block(page, name)
            compiled_blocks["Ks4Guess"] = compile_block(page, "Ks4Guess", GUESS_BLOCK_DIR)
            print("  ✓ %d shared blocks compiled" % len(compiled_blocks))

            for lesson in ks4_lessons.LESSONS:
                compiled_lessons[lesson["slug"]] = compile_lesson(page, lesson, lesson_report)
    finally:
        stub_server.shutdown()
    print("  ✓ %d lessons compiled" % len(compiled_lessons))

    for _rid in ks4_science_rulings.applied_ids():
        print("     ks4_science_rulings applied: %s" % _rid)
    print("  ✓ ks4_science_rulings: %d of 101 rows applied (skip_apply rows "
          "and the 2 docs-only rows excluded)"
          % len(ks4_science_rulings.applied_ids()))

    for row in lesson_report:
        if row["slug_renamed"]:
            print("     R-SLUG fired: %s" % row["slug"])
        if row["r9_fired"]:
            print("     R9 fired: %s" % row["slug"])
        if row.get("r18_fired"):
            print("     R18 fired: %s" % row["slug"])

    # ── rung-1 fallback check (examiner finding) ───────────────────────
    fallback_warnings = 0
    for lesson in ks4_lessons.LESSONS:
        raw_tpl, raw_logic = template_and_logic(
            os.path.join(DESIGN_DIR, lesson["design_file"]))
        needles = extract_rung1_needles(raw_logic)
        fallback_warnings += check_rung1_fallback(data, lesson, needles)
    print("  ✓ rung-1 fallback check: %d warning(s) printed above" % fallback_warnings)

    # ── draft exam tips, preserved verbatim ────────────────────────────
    draft_tips = []
    for lesson in ks4_lessons.LESSONS:
        tip = compiled_lessons[lesson["slug"]]["draft_tip"]
        if tip:
            draft_tips.append((lesson["slug"], lesson["title"], tip))
    os.makedirs(INVENTORY_DIR, exist_ok=True)
    with open(os.path.join(INVENTORY_DIR, "draft-exam-tips.md"), "w", encoding="utf-8") as fh:
        fh.write("# Draft examiner tips removed by R7 (not yet approved)\n\n"
                  "Verbatim, for Mide/the examiners to approve or replace. "
                  "Removed from the live page — no draft chip may reach a "
                  "student (pilot-build-contract.md R7).\n\n")
        for slug, title, tip in draft_tips:
            fh.write("## %s (%s)\n\n%s\n\n" % (title, slug, tip))
    print("  ✓ %d draft exam tip(s) preserved in docs/ks4/pilot-inventory/draft-exam-tips.md"
          % len(draft_tips))

    # ── cache-bust: hash our own new assets ────────────────────────────
    versions = {}
    for name in KS4_VERSIONED:
        path = _shared(name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                versions[name] = hashlib.md5(fh.read()).hexdigest()[:8]
    print("  ✓ %d shared asset(s) versioned" % len(versions))

    # ── emit the 54 pages ───────────────────────────────────────────────
    block_scripts = block_registration_scripts(compiled_blocks)
    written_pages = []
    for lesson in ks4_lessons.LESSONS:
        compiled_lesson = compiled_lessons[lesson["slug"]]
        for route in lesson["routes"]:
            prev_next = compute_prev_next(data, lesson, route)
            html = render_page(lesson, route, compiled_lesson,
                                block_scripts + guess_registration_script(
                                    compiled_blocks, compiled_lesson),
                                prev_next, versions)
            url = ks4_lessons.site_url(lesson["slug"], route)
            out_path = os.path.join(OUT_ROOT, url.lstrip("/"))
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            written_pages.append((out_path, url))
    print("  ✓ %d pages written" % len(written_pages))

    # ── prerender + console-error gate ──────────────────────────────────
    results = prerender_all(cdp, written_pages)
    total_errors = 0
    for url, e1280, e360 in results:
        if e1280 or e360:
            total_errors += len(e1280) + len(e360)
            print("  ✗ console errors on %s" % url)
            for e in e1280:
                print("      [1280] %s" % e)
            for e in e360:
                print("      [360]  %s" % e)
    if total_errors:
        raise SystemExit("build_ks4: %d console error(s) across the 54 pages "
                          "— a build failure (see above)." % total_errors)
    print("  ✓ zero console errors across %d pages at 1280 and 360px" % len(results))
    print("  ✓ D3 verified: favicon.ico 404 is gone (KS4_PILOT_FAVICON_LINK "
          "shipped, no favicon.ico error on any of the %d pages)" % len(results))

    # ── root-level mirror ────────────────────────────────────────────────
    # ⚠️ `generate_site_v5.py`'s own "Copy to repo root" step rmtree's and
    # copytree's the WHOLE `combined/`/`triple/` top-level dirs from
    # `mrbadmus_site/` back to the repo root — but it does that BEFORE this
    # script runs (build_all.py's step order), so by the time build_ks4.py
    # has overwritten these 54 pages under mrbadmus_site/, the root mirror
    # still holds the OLD design. `git ls-files combined/` proves the repo
    # DOES track this mirror (424 files), so it has to be kept in step.
    # Mirrors ONLY the 54 files this script itself wrote — never a wholesale
    # rmtree+copytree of the whole tree, which would needlessly re-touch the
    # other ~250 untouched KS4 pages living in the same directories (the
    # bytes would end up identical either way, since nothing else in this
    # run wrote them, but touching 250 files this run has no business
    # touching is exactly the kind of scope creep the hard line — "the
    # other 250 KS4 lesson pages do not change by a byte" — exists to catch).
    for out_path, _url in written_pages:
        root_path = out_path[len(OUT_ROOT):].lstrip(os.sep)
        os.makedirs(os.path.dirname(root_path), exist_ok=True)
        import shutil as _shutil
        _shutil.copy2(out_path, root_path)
    print("  ✓ mirrored %d page(s) to the repo-root combined/triple/ "
          "trees" % len(written_pages))

    # ── manifest ─────────────────────────────────────────────────────────
    manifest = {"pages": {}, "assets": {}}
    for out_path, url in written_pages:
        with open(out_path, "rb") as fh:
            manifest["pages"][out_path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    for name in KS4_VERSIONED:
        path = _shared(name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                manifest["assets"][path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("  ✓ %s written (%d pages, %d assets)"
          % (MANIFEST_PATH, len(manifest["pages"]), len(manifest["assets"])))

    # ── freeze (only with --freeze) ─────────────────────────────────────
    if freeze:
        frozen = {}
        for lesson in ks4_lessons.LESSONS:
            slug = lesson["slug"]
            template_json_str = json.dumps(compiled_lessons[slug]["template"])
            logic_str = compiled_lessons[slug]["logic"]
            source_json_str = json.dumps(per_slug[slug], sort_keys=True)
            frozen[slug] = {
                "hash": compute_freeze_hash(template_json_str, logic_str, source_json_str),
                "review_state": lesson["review_state"],
            }
        with open(FREEZE_PATH, "w", encoding="utf-8") as fh:
            json.dump(frozen, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print("  ✓ %s written (%d lesson(s) frozen)" % (FREEZE_PATH, len(frozen)))

    import shutil
    shutil.rmtree(stub_dir, ignore_errors=True)

    print("\n✅ build_ks4 complete — %d pages, %d fallback warning(s).\n"
          % (len(written_pages), fallback_warnings))
    return 0


# ═══════════════════════════════════════════════════════════════════════
# BUILD_BATCH — any batch OTHER than the pilot (docs/ks4/batch-engine.md).
# Much thinner than `build_pilot()`: no Design reference to diff against,
# no draft-exam-tip preservation, no rung-1 fallback check (both of those
# are about RECOVERING from Design's own React delivery, which an authored
# batch never had) — just compile, apply the data-route convention, render,
# prerender, mirror, manifest, optionally freeze.
# ═══════════════════════════════════════════════════════════════════════
def build_batch(name, freeze=False):
    import ks3_browser as cdp
    import build_ks3
    import shutil

    global TUTOR_OVERLAY
    if TUTOR_OVERLAY is None:
        TUTOR_OVERLAY = ks4_rulings.apply_r_tutor_label(build_ks3.KS3_CHAT_OVERLAY)

    lessons = ks4_lessons.lessons_for_batch(name)
    if not lessons:
        print("  ⚠️  build_ks4 --batch %s: no lessons registered — nothing to build." % name)
        return 0

    print("\n\U0001f9f1  build_ks4 — batch %r (%d lesson(s))\n" % (name, len(lessons)))

    ks4_lessons.verify_batch_slugs(name)
    ks4_lessons.verify_no_slug_collisions()
    print("  ✓ %d slug(s) verified against all_subtopics_*.py, no cross-batch collisions"
          % len(lessons))

    ks4_science_rulings.reset_applied()
    data = load_subtopics_by_route()

    source_name = "ks4-source-%s.js" % name
    source_js, per_slug = build_source_js(data, lessons=lessons, out_name=source_name)
    with open(_shared(source_name), "w", encoding="utf-8") as fh:
        fh.write(source_js)
    print("  ✓ shared/%s written (%d lesson(s))" % (source_name, len(lessons)))

    authored_dir = ks4_lessons.authored_dir(name)
    lesson_files = [lesson.get("source_file", lesson["slug"] + ".dc.html") for lesson in lessons]
    css_name = "ks4-lesson-%s.css" % name
    # A batch that brings its own shared blocks (batch 4+) adds the <style>
    # of the blocks whose styling is new, after the lessons' own.
    own_blocks = ks4_lessons.batch_blocks(name)
    block_names, block_dir = BLOCK_NAMES, None
    if own_blocks:
        block_names, block_dir, own_css_blocks = own_blocks
        lesson_files = lesson_files + [b + ".dc.html" for b in own_css_blocks]
    lesson_css = collect_batch_lesson_css(authored_dir, lesson_files, css_name)
    lesson_css += getattr(ks4_lessons.batch_modules()[name], "EXTRA_CSS", "")
    with open(_shared(css_name), "w", encoding="utf-8") as fh:
        fh.write(lesson_css)
    print("  ✓ shared/%s written (%d bytes)" % (css_name, len(lesson_css)))

    ext_name = "ks4-ext-%s.js" % name
    # a batch may name its own ext source (batch 4 keeps Design's folder
    # byte-identical, so its ext asset lives in ks4_lessons/).
    ext_src_path = getattr(ks4_lessons.batch_modules()[name], "EXT_SRC",
                           os.path.join(authored_dir, "_ext.js"))
    has_ext = os.path.exists(ext_src_path)
    if has_ext:
        ext_text = open(ext_src_path, encoding="utf-8").read()
        with open(_shared(ext_name), "w", encoding="utf-8") as fh:
            fh.write(ext_text)
        print("  ✓ shared/%s written (from %s)" % (ext_name, ext_src_path))

    # ⊕ docs/ks4/batch-engine.md §7b — shared/ks4-nav.js is ONE shared
    # asset (not per-batch-name, unlike source_name/css_name/ext_name
    # above), loaded by EVERY batch page, never the pilot's. Its content
    # depends only on all_subtopics_*.py (build_ks4_nav_js()), so rewriting
    # it on every batch build is idempotent — building batch-2 then
    # batch-3 writes it twice with identical bytes, never once per name.
    nav_name = "ks4-nav.js"
    with open(_shared(nav_name), "w", encoding="utf-8") as fh:
        fh.write(build_ks4_nav_js())
    print("  ✓ shared/%s written" % nav_name)

    # the shared pilot infra (ks4-ds.css/ks4-theme.css/ks4-lib.js/
    # ks4-diagrams.js/ks4-runtime.js) must already exist. `main()` always
    # builds the pilot first in a no-flag run; a bare `--batch <name>` run
    # requires a prior pilot (or full) build on this tree.
    for required in ("ks4-ds.css", "ks4-theme.css", "ks4-lib.js",
                      "ks4-diagrams.js", "ks4-runtime.js"):
        if not os.path.exists(_shared(required)):
            raise SystemExit(
                "build_ks4 --batch %s: shared/%s is missing — run "
                "`python3 build_ks4.py` (no flag, or `--batch pilot`) at "
                "least once first so the shared KS4 infra exists."
                % (name, required))

    dst_shared = os.path.join(OUT_ROOT, "shared")
    os.makedirs(dst_shared, exist_ok=True)
    own_assets = [source_name, css_name, nav_name] + ([ext_name] if has_ext else [])
    for asset_name in own_assets:
        shutil.copy2(_shared(asset_name), os.path.join(dst_shared, asset_name))
    print("  ✓ synced %d batch asset(s) into %s" % (len(own_assets), dst_shared))

    stub_dir = os.path.join(REPO_ROOT, ".ks4_compile_stub_%s" % name)
    os.makedirs(stub_dir, exist_ok=True)
    with open(os.path.join(stub_dir, "stub.html"), "w", encoding="utf-8") as fh:
        fh.write("<!doctype html><html><body></body></html>")

    compiled_blocks = {}
    lesson_report = []
    compiled_lessons = {}
    stub_server, stub_port = cdp.serve(stub_dir)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.goto("http://127.0.0.1:%d/stub.html" % stub_port)
            for block_name in block_names:
                compiled_blocks[block_name] = compile_block(page, block_name, block_dir)
            if not own_blocks:
                # rule 1: Ks4Guess for batches 2/3 (registered per page, below)
                compiled_blocks["Ks4Guess"] = compile_block(page, "Ks4Guess", GUESS_BLOCK_DIR)
            for lesson in lessons:
                compiled_lessons[lesson["slug"]] = compile_batch_lesson(
                    page, name, lesson, lesson_report)
    finally:
        stub_server.shutdown()
    print("  ✓ %d shared block(s) + %d lesson(s) compiled"
          % (len(compiled_blocks), len(compiled_lessons)))

    versions = {}
    for asset_name in list(KS4_VERSIONED) + own_assets:
        path = _shared(asset_name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                versions[asset_name] = hashlib.md5(fh.read()).hexdigest()[:8]
    print("  ✓ %d shared+own asset(s) versioned" % len(versions))

    batch_css_link = '<link rel="stylesheet" href="/shared/%s">\n' % css_name
    batch_source_tag = '<script src="/shared/%s"></script>\n' % source_name
    batch_ext_tag = ('<script src="/shared/%s"></script>\n' % ext_name) if has_ext else ""
    batch_nav_tag = '<script src="/shared/%s"></script>\n' % nav_name

    block_scripts = block_registration_scripts(compiled_blocks, block_names)
    written_pages = []
    for lesson in lessons:
        compiled_lesson = compiled_lessons[lesson["slug"]]
        for route in lesson["routes"]:
            prev_next = compute_prev_next(data, lesson, route)
            html = render_page(lesson, route, compiled_lesson,
                                block_scripts + ("" if own_blocks else guess_registration_script(
                                    compiled_blocks, compiled_lesson)),
                                prev_next, versions,
                                batch_css=batch_css_link,
                                batch_source_js=batch_source_tag,
                                batch_ext_js=batch_ext_tag,
                                batch_nav_js=batch_nav_tag)
            url = ks4_lessons.site_url(lesson["slug"], route)
            out_path = os.path.join(OUT_ROOT, url.lstrip("/"))
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            written_pages.append((out_path, url))
    print("  ✓ %d page(s) written" % len(written_pages))

    results = prerender_all(cdp, written_pages)
    total_errors = 0
    for url, e1280, e360 in results:
        if e1280 or e360:
            total_errors += len(e1280) + len(e360)
            print("  ✗ console errors on %s" % url)
            for e in e1280:
                print("      [1280] %s" % e)
            for e in e360:
                print("      [360]  %s" % e)
    if total_errors:
        raise SystemExit("build_ks4 --batch %s: %d console error(s) across "
                          "%d page(s) — a build failure." % (name, total_errors, len(results)))
    print("  ✓ zero console errors across %d page(s) at 1280 and 360px" % len(results))

    for out_path, _url in written_pages:
        root_path = out_path[len(OUT_ROOT):].lstrip(os.sep)
        os.makedirs(os.path.dirname(root_path), exist_ok=True)
        shutil.copy2(out_path, root_path)
    print("  ✓ mirrored %d page(s) to the repo-root combined/triple/ trees" % len(written_pages))

    manifest = {"pages": {}, "assets": {}}
    for out_path, url in written_pages:
        with open(out_path, "rb") as fh:
            manifest["pages"][out_path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    for asset_name in list(KS4_VERSIONED) + own_assets:
        path = _shared(asset_name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                manifest["assets"][path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    manifest_path = batch_manifest_path(name)
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("  ✓ %s written (%d pages, %d assets)"
          % (manifest_path, len(manifest["pages"]), len(manifest["assets"])))

    if freeze:
        frozen = {}
        for lesson in lessons:
            slug = lesson["slug"]
            template_json_str = json.dumps(compiled_lessons[slug]["template"])
            logic_str = compiled_lessons[slug]["logic"]
            source_json_str = json.dumps(per_slug[slug], sort_keys=True)
            frozen[slug] = {
                "hash": compute_freeze_hash(template_json_str, logic_str, source_json_str),
                "review_state": lesson["review_state"],
            }
        frozen_path = batch_frozen_path(name)
        with open(frozen_path, "w", encoding="utf-8") as fh:
            json.dump(frozen, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print("  ✓ %s written (%d lesson(s) frozen)" % (frozen_path, len(frozen)))

    shutil.rmtree(stub_dir, ignore_errors=True)

    print("\n✅ build_ks4 --batch %s complete — %d page(s).\n" % (name, len(written_pages)))
    return 0


# ═══════════════════════════════════════════════════════════════════════
# MAIN — dispatches to build_pilot() / build_batch() per the batch
# registry (docs/ks4/batch-engine.md). No flag builds EVERY registered
# batch, pilot first (ks4_lessons.batch_names()'s own order) — this is
# what keeps build_all.py's step 1b (which calls this script with no flag)
# rebuilding every live batch on every full site build.
# ═══════════════════════════════════════════════════════════════════════
def main():
    os.chdir(REPO_ROOT)
    sys.path.insert(0, REPO_ROOT)

    argv = sys.argv[1:]
    freeze = "--freeze" in argv
    batch_arg = None
    if "--batch" in argv:
        i = argv.index("--batch")
        if i + 1 >= len(argv):
            raise SystemExit("build_ks4: --batch needs a name, e.g. --batch pilot")
        batch_arg = argv[i + 1]

    registered = ks4_lessons.batch_names()
    if batch_arg is not None:
        if batch_arg not in registered:
            raise SystemExit(
                "build_ks4: --batch %r is not registered. Known batches: %s"
                % (batch_arg, ", ".join(registered)))
        targets = [batch_arg]
    else:
        targets = registered

    rc = 0
    for name in targets:
        if name == "pilot":
            rc = build_pilot(freeze=freeze) or rc
        else:
            rc = build_batch(name, freeze=freeze) or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
