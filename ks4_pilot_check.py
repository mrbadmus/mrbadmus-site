#!/usr/bin/env python3
"""ks4_pilot_check.py — FAST gate for the KS4 pilot's 54 pages. No browser.

    python3 ks4_pilot_check.py

Asserts, purely by reading files already on disk:

  1. Every path in `ks4_pilot_manifest.json` exists under `mrbadmus_site/`
     and its sha256 matches the manifest. This is what catches a
     `generate_site_v5.py`-only run: that generator writes the OLD design
     back onto these 54 paths (build_all.py's step-1b comment explains why),
     and the bytes on disk would then no longer match what build_ks4.py
     last produced.
  2. No page OUTSIDE the manifest, under mrbadmus_site/combined/** or
     mrbadmus_site/triple/**, references ks4-runtime.js — the 250 other
     KS4 lesson pages must never load it.
  3. None of the 54 pages reference unpkg, React, Babel or support.js —
     Design's runtime ships nowhere.
  4. Every `dc-import` name and every classified section type on the 54
     pages is in the closed registry (`ks4_lessons.blocks`).
  5. Every `/shared/ks4-*` `?v=` stamp on the 54 pages equals the md5[:8]
     of that file as it stands on disk right now.
  6. For every lesson whose `review_state` is 'examiner-reviewed' or
     'frozen', the compiled template + logic + served source record still
     hash to the value `ks4_lessons/frozen.json` recorded at the last
     `python3 build_ks4.py --freeze` — a content edit with no
     re-examination is a red, not a silent pass (see `check_freeze()`).

⊕ Mide's ruling (27 Sep 2026, ks4_rulings.py R11–R14) adds three more,
still no browser (see `ks4_parity.py`'s `check_route_switch_keyboard()` for
the one assertion that genuinely needs one — Enter/Space/Esc):

  7. Every one of the 54 pages carries EXACTLY ONE route chip
     (`.ks3-route-chip`) naming that page's own route in words
     (`build_ks4.ROUTE_WORDS`), and its switcher (`.ks3-route-menu`) lists
     EXACTLY the lesson's other existing routes — no more, no fewer — each
     at the real URL `ks4_lessons.site_url()` computes, and every one of
     those URLs exists on disk (see `check_route_chip()`).
  8. `series-parallel-circuits` and `resistors` carry the FINAL, approved
     exam tip byte-exact, on every route each ships on — read straight from
     `all_subtopics_physics_triple_higher.py`'s `examiner_tip` field, the
     same record the page itself is built from, never a second hand-copied
     literal (see `check_exam_tips()`).
  9. Every page's eyebrow + `Ks4KeyNote` `spec` citation matches
     `build_ks4.SPEC_TEXT`: a Triple route (TF/TH) shows the separate
     science's own number, a Combined route (CF/CH) shows 8464's — verified
     against `docs/theme/spec-numbers.md`'s citation table (see
     `check_spec_numbers()`).
"""

import hashlib
import json
import os
import re
import sys

import build_ks4
import ks4_lessons
from ks4_lessons import blocks as ks4_blocks

MANIFEST_PATH = "ks4_pilot_manifest.json"
FREEZE_PATH = build_ks4.FREEZE_PATH
OUT_ROOT = "mrbadmus_site"

BAD_STRINGS = ["unpkg.com", "React.", "ReactDOM", "Babel", "support.js",
               "createElement(", "dangerouslySetInnerHTML"]

_VMATCH_RE = re.compile(r"/shared/(ks4-[\w.\-]+)\?v=([a-f0-9]+)")
_DCIMPORT_RE = re.compile(r'"comp"\s*:\s*"([^"]+)"')
_DATABLOCK_RE = re.compile(r'"data-block"\s*:\s*"([^"]+)"')


def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        return None
    with open(MANIFEST_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def sha256_of(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def check_manifest_matches_disk(manifest, errors):
    for path, want in manifest["pages"].items():
        if not os.path.exists(path):
            errors.append("MISSING page %s (in manifest, not on disk)" % path)
            continue
        got = sha256_of(path)
        if got != want:
            errors.append(
                "STALE page %s — sha256 on disk does not match the "
                "manifest. A generate_site_v5.py-only run (or something "
                "else) has overwritten it since build_ks4.py last ran; "
                "re-run build_ks4.py (or build_all.py)." % path)
        # the repo-root combined/triple mirror (git ls-files combined/ shows
        # the repo tracks it) — generate_site_v5.py's own round-trip runs
        # BEFORE build_ks4.py, so build_ks4.py has to keep this in step
        # itself; a stale mirror here means that copy step did not run.
        root_path = path[len(OUT_ROOT):].lstrip("/") if path.startswith(OUT_ROOT) else None
        if root_path and os.path.exists(root_path):
            got_root = sha256_of(root_path)
            if got_root != want:
                errors.append(
                    "STALE root mirror %s — does not match %s. build_ks4.py's "
                    "root-mirror copy did not run, or something touched it "
                    "since." % (root_path, path))
    for path, want in manifest["assets"].items():
        if not os.path.exists(path):
            errors.append("MISSING asset %s (in manifest, not on disk)" % path)
            continue
        got = sha256_of(path)
        if got != want:
            errors.append("STALE asset %s — sha256 on disk does not match "
                           "the manifest." % path)


def check_no_leakage(manifest, errors):
    # ⊕ batch engine fix (docs/ks4/batch-engine.md §7b, 1 Oct 2026) — this
    # check predates `build_ks4.py --batch`, back when the pilot's own
    # manifest was the only KS4-ported content that could legitimately load
    # ks4-runtime.js. A registered batch's OWN pages do too, by design, and
    # are never in the pilot's manifest — so without this, registering ANY
    # second batch (e.g. batch-2) would permanently fail this gate for a
    # page that is not a leak at all. A page is only flagged now if it is
    # outside the pilot's manifest AND outside every OTHER registered
    # batch's own manifest too — a real orphan is still caught.
    manifest_pages = set(manifest["pages"].keys())
    for name in ks4_lessons.batch_names():
        if name == "pilot":
            continue
        other_path = build_ks4.batch_manifest_path(name)
        if not os.path.exists(other_path):
            continue
        with open(other_path, encoding="utf-8") as fh:
            other_manifest = json.load(fh)
        manifest_pages |= set(other_manifest["pages"].keys())
    for tree in ("combined", "triple"):
        base = os.path.join(OUT_ROOT, tree)
        if not os.path.isdir(base):
            continue
        for root, _dirs, files in os.walk(base):
            for fname in files:
                if not fname.endswith(".html"):
                    continue
                path = os.path.join(root, fname).replace(os.sep, "/")
                if path in manifest_pages:
                    continue
                try:
                    text = open(path, encoding="utf-8").read()
                except (OSError, UnicodeDecodeError):
                    continue
                if "ks4-runtime.js" in text:
                    errors.append(
                        "LEAK: %s is outside the KS4 pilot manifest but "
                        "references ks4-runtime.js — one of the other 250 "
                        "KS4 lesson pages must never load it." % path)


def check_no_react(manifest, errors):
    for path in manifest["pages"]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for bad in BAD_STRINGS:
            if bad in text:
                errors.append("%s still references %r — Design's runtime "
                               "must ship nowhere." % (path, bad))


def check_registry(manifest, errors):
    known_comps = ks4_blocks.COMPONENTS
    known_sections = ks4_blocks.SECTION_TYPES
    for path in manifest["pages"]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in _DCIMPORT_RE.finditer(text):
            if m.group(1) not in known_comps:
                errors.append("%s: unregistered dc-import %r" % (path, m.group(1)))
        for m in _DATABLOCK_RE.finditer(text):
            if m.group(1) not in known_sections:
                errors.append("%s: unregistered data-block %r" % (path, m.group(1)))


def check_version_stamps(manifest, errors):
    hashes = {}
    for path in manifest["assets"]:
        name = os.path.basename(path)
        with open(path, "rb") as fh:
            hashes[name] = hashlib.md5(fh.read()).hexdigest()[:8]
    for path in manifest["pages"]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in _VMATCH_RE.finditer(text):
            name, stamped = m.group(1), m.group(2)
            want = hashes.get(name)
            if want is None:
                continue  # asset not tracked here (e.g. ks4-runtime.js, still fine to skip)
            if stamped != want:
                errors.append("%s: ?v=%s for %s does not match its current "
                               "md5[:8] %s" % (path, stamped, name, want))


def check_freeze(errors):
    """For every lesson whose `review_state` is 'examiner-reviewed' or
    'frozen', the CURRENT build (the compiled template + logic embedded in
    its own page, and its served source record in shared/ks4-source.js)
    must hash to the same value `ks4_lessons/frozen.json` recorded at the
    last `build_ks4.py --freeze`. A mismatch means the content moved after
    the science examination signed it off — the examination, not the code,
    is what is now stale."""
    if not os.path.exists(FREEZE_PATH):
        print("ks4_pilot_check: NOTE — %s does not exist yet "
              "(run `python3 build_ks4.py --freeze`); freeze check skipped."
              % FREEZE_PATH)
        return
    with open(FREEZE_PATH, encoding="utf-8") as fh:
        frozen = json.load(fh)

    reviewed = [L for L in ks4_lessons.LESSONS
                if L["review_state"] in ("examiner-reviewed", "frozen")]
    if not reviewed:
        return

    source_js_path = os.path.join("shared", "ks4-source.js")
    if not os.path.exists(source_js_path):
        errors.append("FREEZE: %s missing — cannot verify any frozen lesson."
                       % source_js_path)
        return
    source_js_text = open(source_js_path, encoding="utf-8").read()

    for lesson in reviewed:
        slug = lesson["slug"]
        frozen_row = frozen.get(slug)
        if frozen_row is None:
            errors.append(
                "FREEZE: %s is %r but has never been frozen — run "
                "`python3 build_ks4.py --freeze` after re-running the "
                "examination." % (slug, lesson["review_state"]))
            continue
        route = lesson["routes"][0]
        url = ks4_lessons.site_url(slug, route)
        page_path = os.path.join(OUT_ROOT, url.lstrip("/"))
        if not os.path.exists(page_path):
            errors.append("FREEZE: %s missing — cannot verify frozen lesson %s."
                           % (page_path, slug))
            continue
        page_text = open(page_path, encoding="utf-8").read()
        try:
            template_json, logic, source_json = build_ks4.extract_freeze_pieces(
                page_text, source_js_text, slug)
        except ValueError as e:
            errors.append("FREEZE: %s: could not extract compiled content "
                           "to verify — %s" % (slug, e))
            continue
        current_hash = build_ks4.compute_freeze_hash(template_json, logic, source_json)
        if current_hash != frozen_row.get("hash"):
            errors.append(
                "FREEZE: %s content has changed since it was last frozen "
                "(review_state=%r). A science examination signed off the "
                "PREVIOUS content; this content has not been re-examined. "
                "Re-run the examination, then `python3 build_ks4.py "
                "--freeze` once the examiner's changes are applied."
                % (slug, lesson["review_state"]))


# ═══════════════════════════════════════════════════════════════════════
# R11–R14 (Mide's ruling, 27 Sep 2026) — three fast, browser-free checks
# ═══════════════════════════════════════════════════════════════════════
_CHIP_RE = re.compile(
    r'class="ks3-route-chip"[^>]*>.*?class="sc-interp">([^<]*)</span>', re.S)
_MENU_RE = re.compile(r'class="ks3-route-menu"[^>]*>(.*?)</ul>', re.S)
_MENU_ITEM_RE = re.compile(
    r'<a[^>]*href="([^"]+)"[^>]*>(?:<span[^>]*class="sc-interp">)?([^<]*)', re.S)


def _page_path(slug, route):
    return os.path.join(OUT_ROOT, ks4_lessons.site_url(slug, route).lstrip("/"))


def check_route_chip(errors):
    """R12: exactly one `.ks3-route-chip` per page, its text is
    `build_ks4.ROUTE_WORDS[route]`, and its switcher's `<a href>`s are
    EXACTLY the lesson's other existing routes at their real URL — a
    missing option, an extra option, or a wrong URL is each its own error,
    never silently tolerated by only checking set membership one way."""
    for lesson in ks4_lessons.LESSONS:
        route_switch = build_ks4.compute_route_switch(lesson)
        for route in lesson["routes"]:
            path = _page_path(lesson["slug"], route)
            if not os.path.exists(path):
                errors.append("ROUTE-CHIP: %s missing" % path)
                continue
            text = open(path, encoding="utf-8").read()
            chips = _CHIP_RE.findall(text)
            if len(chips) != 1:
                errors.append(
                    "ROUTE-CHIP: %s carries %d .ks3-route-chip element(s), "
                    "expected exactly 1" % (path, len(chips)))
                continue
            want_words = build_ks4.ROUTE_WORDS[route]
            if chips[0] != want_words:
                errors.append(
                    "ROUTE-CHIP: %s chip reads %r, expected %r (this "
                    "page's own route, in words)" % (path, chips[0], want_words))
            menus = _MENU_RE.findall(text)
            if len(menus) != 1:
                errors.append(
                    "ROUTE-CHIP: %s carries %d .ks3-route-menu element(s), "
                    "expected exactly 1" % (path, len(menus)))
                continue
            got_options = sorted(_MENU_ITEM_RE.findall(menus[0]))
            want_options = sorted(
                (o["href"], o["label"]) for o in route_switch[route]["options"])
            if got_options != want_options:
                errors.append(
                    "ROUTE-CHIP: %s switcher options %r != expected %r"
                    % (path, got_options, want_options))
                continue
            for href, _label in got_options:
                target = os.path.join(OUT_ROOT, href.lstrip("/"))
                if not os.path.exists(target):
                    errors.append(
                        "ROUTE-CHIP: %s switcher links to %s, which does "
                        "not exist under %s/" % (path, href, OUT_ROOT))


def check_exam_tips(errors):
    """R13: the two physics lessons' approved exam tip ships BYTE-EXACT —
    read from the SAME `examiner_tip` field the page is built from (never a
    second, hand-copied literal that could drift from it) — and every one
    of their routes' pages carries the `{{ examTip }}` binding that serves
    it.

    ⚠️ Cannot check the RENDERED text here: `examTip: ready ? K.tip(slug) :
    ''` is a runtime read of `window.KS4SRC` gated on `ready` (component
    state that only becomes true client-side), so the prerendered, static
    HTML this fast/no-Chrome gate reads always shows it blank — true of all
    14 lessons' tips, not just these two (confirmed against an
    already-shipped lesson before writing this check). The RENDERED-text
    proof, in a real browser where `ready` genuinely becomes true, is
    `ks4_parity.py`'s `compare_section_text()` R13 branch."""
    import all_subtopics_physics_triple_higher as phys_th

    def approved_tip(slug):
        for topic_list in phys_th.PHYSICS_SUBTOPICS_ALL.values():
            for st in topic_list:
                if st.get("id") == slug:
                    return st.get("examiner_tip") or ""
        return ""

    source_js_path = os.path.join("shared", "ks4-source.js")
    source_text = open(source_js_path, encoding="utf-8").read() if os.path.exists(source_js_path) else ""
    if not source_text:
        errors.append("EXAM-TIP: %s missing — cannot verify the served tip" % source_js_path)

    for slug in ("series-parallel-circuits", "resistors"):
        want = approved_tip(slug)
        if not want:
            errors.append(
                "EXAM-TIP: no examiner_tip found for %r in "
                "all_subtopics_physics_triple_higher.py" % slug)
            continue
        if source_text and want not in source_text:
            errors.append(
                "EXAM-TIP: %s does not carry the approved tip byte-exact "
                "for %r — window.KS4SRC[%r].examiner_tip has drifted from "
                "the all_subtopics_*.py field it is generated from"
                % (source_js_path, slug, slug))
        lesson = ks4_lessons.LESSON_BY_SLUG[slug]
        for route in lesson["routes"]:
            path = _page_path(slug, route)
            if not os.path.exists(path):
                errors.append("EXAM-TIP: %s missing" % path)
                continue
            text = open(path, encoding="utf-8").read()
            if "Examiner tip</p>" not in text:
                errors.append("EXAM-TIP: %s has no 'Examiner tip' slot at all" % path)
            if '"examTip"' not in text:
                errors.append(
                    "EXAM-TIP: %s carries no {{ examTip }} binding in its "
                    "compiled logic — the R13 slot did not wire up" % path)


def check_spec_numbers(errors):
    """R14: a Triple route (TF/TH) shows the separate science's own AQA
    spec number (8462/8463); a Combined route (CF/CH) shows 8464's — and,
    ⊕ D13 (theme-run audit, 27 Sep 2026), NAMES it: every "combined" value
    in `build_ks4.SPEC_TEXT` now carries "(8464)" the same way every
    "triple" value has always carried "(8462)"/"(8463)", so this check's
    own `want["eyebrow"]`/`want["keynote"]` already read the D13 text —
    nothing else here needed to change for the 12 Combined-route lessons.
    `nanoparticles` is excluded from THIS loop (it has no Combined route at
    all, so it is not in `SPEC_TEXT`, and R14 was never applied to it — see
    DEPARTURES-PILOT.md) but is checked separately below, by R5, which now
    also carries "(8462)"."""
    for lesson in ks4_lessons.LESSONS:
        slug = lesson["slug"]
        entry = build_ks4.SPEC_TEXT.get(slug)
        if entry is None:
            continue
        for route in lesson["routes"]:
            path = _page_path(slug, route)
            if not os.path.exists(path):
                errors.append("SPEC-NUMBER: %s missing" % path)
                continue
            text = open(path, encoding="utf-8").read()
            want = entry["triple" if route in ("TF", "TH") else "combined"]
            for field, needle in (("eyebrow", want["eyebrow"]),
                                   ("keynote", want["keynote"])):
                if needle not in text:
                    errors.append(
                        "SPEC-NUMBER: %s (%s) does not contain the expected "
                        "%s citation %r" % (path, route, field, needle))


def check_r5_nanoparticles_spec(errors):
    """⊕ D13 (theme-run audit, 27 Sep 2026) — nanoparticles sits outside
    `check_spec_numbers()` (it is not in `SPEC_TEXT`), so its own R5 fix
    (`ks4_rulings.apply_r5_nanoparticles_spec`) had no gate at all watching
    it. Asserts both literals it writes are on both of nanoparticles' two
    routes (TF, TH)."""
    for route in ("TF", "TH"):
        path = _page_path("nanoparticles", route)
        if not os.path.exists(path):
            errors.append("SPEC-NUMBER: %s missing" % path)
            continue
        text = open(path, encoding="utf-8").read()
        # ⊕ bare substrings, matching check_spec_numbers()'s own convention
        # just above — the compiled page carries these as JSON string
        # values ("spec": "AQA ..."), not the source template's HTML
        # attribute syntax (spec="AQA ..."), so a needle wrapped in that
        # syntax never matches the built output.
        for needle in ("AQA Chemistry (8462) 4.2.4 (chemistry only) · Quantitative",
                       "AQA 4.2.4 (8462) (chemistry only)"):
            if needle not in text:
                errors.append(
                    "SPEC-NUMBER: %s (%s) does not contain the expected "
                    "R5 citation %r" % (path, route, needle))


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
    manifest = load_manifest()
    if manifest is None:
        print("ks4_pilot_check: SKIPPED — %s does not exist (build_ks4.py "
              "has not run yet)." % MANIFEST_PATH)
        return 0

    errors = []
    check_manifest_matches_disk(manifest, errors)
    check_no_leakage(manifest, errors)
    check_no_react(manifest, errors)
    check_registry(manifest, errors)
    check_version_stamps(manifest, errors)
    check_freeze(errors)
    check_route_chip(errors)
    check_exam_tips(errors)
    check_spec_numbers(errors)
    check_r5_nanoparticles_spec(errors)

    if errors:
        print("\n❌ ks4_pilot_check: %d problem(s)\n" % len(errors))
        for e in errors:
            print("  - %s" % e)
        return 1

    print("✅ ks4_pilot_check: %d page(s), %d asset(s) — all clean."
          % (len(manifest["pages"]), len(manifest["assets"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
