#!/usr/bin/env python3
"""ks4_batch_check.py — FAST gate for a non-pilot KS4 batch's pages. No
browser (docs/ks4/batch-engine.md). The generalised, non-pilot sibling of
`ks4_pilot_check.py` — that script stays pilot-only (its checks 7-9 are
pilot-specific: the R9/R12/R13/R14 rulings, `build_ks4.SPEC_TEXT`, the two
physics lessons' approved exam tip), because none of that generalises to
an authored batch. This file keeps only what DOES generalise:

    python3 ks4_batch_check.py --batch batch-2

  1. Every path in the batch's manifest (`ks4_<batch>_manifest.json`)
     exists under `mrbadmus_site/` and its sha256 matches — catches a
     `generate_site_v5.py`-only run putting the OLD page back.
  2. None of the batch's pages reference unpkg, React, Babel or
     support.js.
  3. Every `dc-import` name and every classified `data-block` section type
     on the batch's pages is in the closed registry (`ks4_lessons.blocks`).
  4. Every `/shared/ks4-*` `?v=` stamp on the batch's pages — both the
     shared pilot assets AND this batch's own `ks4-source-<batch>.js` /
     `ks4-lesson-<batch>.css` / `ks4-ext-<batch>.js` — equals the md5[:8]
     of that file as it stands on disk right now.
  5. For every lesson whose `review_state` is 'examiner-reviewed' or
     'frozen', the compiled template + logic + served source record still
     hash to the value `ks4_lessons/frozen_<batch>.json` recorded at the
     last `python3 build_ks4.py --batch <name> --freeze`.
"""
import argparse
import hashlib
import json
import os
import re
import sys

import build_ks4
import ks4_lessons
from ks4_lessons import blocks as ks4_blocks

OUT_ROOT = build_ks4.OUT_ROOT
_DCIMPORT_RE = re.compile(r'"comp"\s*:\s*"([^"]+)"')
_DATABLOCK_RE = re.compile(r'"data-block"\s*:\s*"([^"]+)"')
BAD_STRINGS = ["unpkg.com", "React.", "ReactDOM", "Babel", "support.js",
               "createElement(", "dangerouslySetInnerHTML"]


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
                "manifest. Re-run build_ks4.py --batch." % path)
        root_path = path[len(OUT_ROOT):].lstrip("/") if path.startswith(OUT_ROOT) else None
        if root_path and os.path.exists(root_path):
            got_root = sha256_of(root_path)
            if got_root != want:
                errors.append("STALE root mirror %s — does not match %s." % (root_path, path))
    for path, want in manifest["assets"].items():
        if not os.path.exists(path):
            errors.append("MISSING asset %s (in manifest, not on disk)" % path)
            continue
        got = sha256_of(path)
        if got != want:
            errors.append("STALE asset %s — sha256 on disk does not match "
                           "the manifest." % path)


def check_no_react(manifest, errors):
    for path in manifest["pages"]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for bad in BAD_STRINGS:
            if bad in text:
                errors.append("%s still references %r." % (path, bad))


def check_registry(manifest, errors):
    for path in manifest["pages"]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        for m in _DCIMPORT_RE.finditer(text):
            if m.group(1) not in ks4_blocks.COMPONENTS:
                errors.append("%s: unregistered dc-import %r" % (path, m.group(1)))
        for m in _DATABLOCK_RE.finditer(text):
            if m.group(1) not in ks4_blocks.SECTION_TYPES:
                errors.append("%s: unregistered data-block %r" % (path, m.group(1)))


_VMATCH_RE = re.compile(r"/shared/(ks4-[\w.\-]+)\?v=([a-f0-9]+)")


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
                continue
            if stamped != want:
                errors.append("%s: ?v=%s for %s does not match its current "
                               "md5[:8] %s" % (path, stamped, name, want))


def check_freeze(name, errors):
    frozen_path = build_ks4.batch_frozen_path(name)
    if not os.path.exists(frozen_path):
        print("ks4_batch_check: NOTE — %s does not exist yet (run "
              "`python3 build_ks4.py --batch %s --freeze`); freeze check "
              "skipped." % (frozen_path, name))
        return
    with open(frozen_path, encoding="utf-8") as fh:
        frozen = json.load(fh)

    lessons = ks4_lessons.lessons_for_batch(name)
    reviewed = [L for L in lessons if L["review_state"] in ("examiner-reviewed", "frozen")]
    if not reviewed:
        return

    source_name = "ks4-source-%s.js" % name
    source_js_path = os.path.join("shared", source_name)
    if not os.path.exists(source_js_path):
        errors.append("FREEZE: %s missing — cannot verify any frozen lesson." % source_js_path)
        return
    source_js_text = open(source_js_path, encoding="utf-8").read()

    for lesson in reviewed:
        slug = lesson["slug"]
        frozen_row = frozen.get(slug)
        if frozen_row is None:
            errors.append(
                "FREEZE: %s is %r but has never been frozen — run "
                "`python3 build_ks4.py --batch %s --freeze`."
                % (slug, lesson["review_state"], name))
            continue
        route = lesson["routes"][0]
        url = ks4_lessons.site_url(slug, route)
        page_path = os.path.join(OUT_ROOT, url.lstrip("/"))
        if not os.path.exists(page_path):
            errors.append("FREEZE: %s missing — cannot verify frozen lesson %s." % (page_path, slug))
            continue
        page_text = open(page_path, encoding="utf-8").read()
        try:
            template_json, logic, source_json = build_ks4.extract_freeze_pieces(
                page_text, source_js_text, slug)
        except ValueError as e:
            errors.append("FREEZE: %s: could not extract compiled content to verify — %s" % (slug, e))
            continue
        current_hash = build_ks4.compute_freeze_hash(template_json, logic, source_json)
        if current_hash != frozen_row.get("hash"):
            errors.append(
                "FREEZE: %s content has changed since it was last frozen "
                "(review_state=%r). Re-run the examination, then "
                "`python3 build_ks4.py --batch %s --freeze`."
                % (slug, lesson["review_state"], name))


def check_one(name):
    manifest_path = build_ks4.batch_manifest_path(name)
    if not os.path.exists(manifest_path):
        print("ks4_batch_check: SKIPPED batch %r — %s does not exist "
              "(build_ks4.py --batch %s has not run yet)." % (name, manifest_path, name))
        return []
    with open(manifest_path, encoding="utf-8") as fh:
        manifest = json.load(fh)

    errors = []
    check_manifest_matches_disk(manifest, errors)
    check_no_react(manifest, errors)
    check_registry(manifest, errors)
    check_version_stamps(manifest, errors)
    check_freeze(name, errors)

    if errors:
        print("\n❌ ks4_batch_check --batch %s: %d problem(s)" % (name, len(errors)))
        for e in errors:
            print("  - %s" % e)
    else:
        print("✅ ks4_batch_check --batch %s: %d page(s), %d asset(s) — all clean."
              % (name, len(manifest["pages"]), len(manifest["assets"])))
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", default=None,
                     help="one registered non-pilot batch name; omit to "
                          "check every registered non-pilot batch (the "
                          "pre-push gate's own invocation — SKIPPED with "
                          "no problems when none are registered yet)")
    args = ap.parse_args()

    os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
    if args.batch == "pilot":
        raise SystemExit("ks4_batch_check: use ks4_pilot_check.py for the pilot.")

    if args.batch:
        names = [args.batch]
    else:
        names = [n for n in ks4_lessons.batch_names() if n != "pilot"]
        if not names:
            print("ks4_batch_check: SKIPPED — no non-pilot batch is registered yet.")
            return 0

    all_errors = []
    for name in names:
        all_errors.extend(check_one(name))
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
