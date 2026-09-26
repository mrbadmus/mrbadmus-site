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
    manifest_pages = set(manifest["pages"].keys())
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
