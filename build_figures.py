#!/usr/bin/env python3
"""build_figures.py — the figure manifest builder (MRB-352; the diagrams
figure contract, `docs/diagrams/figure-contract.md`).

⊕ MRB-352 run 2 — EVERY figure now comes from ONE place: `figlib/`, Mide's
diagram library brought into the repo. The KS3 question figures used to be
borrowed from the lesson pages' drawers and the KS4 ones came from a
separate set of drawers in `ks4_art/`; both painted through stylesheet
classes, which is how the same drawing came out as a black disc, black
bands and black-on-black letters on every surface without `ks3.css`.

Three emissions:
  * `figures.json`          — the whole manifest (KS3 + KS4), mirrored to the
                               backend for the worksheet renderer.
  * `shared/figures-ks3.js` — KS3 figures only, for KS3 pages.
  * `shared/figures-ks4.js` — KS4 figures only, for KS4 pages.
Both site files write `window.MRBFigures = Object.assign(window.MRBFigures
|| {}, {...})`, so a page that needs both key stages gets the union.

A record is `{"svg": "<svg …>…</svg>", "alt": "...", "w": N, "h": N}`,
keyed by figure id.

── WHERE THE DRAWINGS ARE DECLARED ────────────────────────────────────────
  * KS3: `figlib/catalogue_ks3.py`. A KS3 figure ships only if some question
    references it (demand — see `referenced_ids()`); a lesson page draws its
    own figures and never reads this manifest.
  * KS4: `ks4_art/catalogue.py` and every `ks4_art/catalogue_*.py`. All of
    it ships.

── WHAT MUST HOLD, OR NOTHING IS WRITTEN ──────────────────────────────────
Every catalogue record — shipped or not, so a figure cannot sit broken in
the catalogue until the day a question first points at it — is drawn,
passed through `figlib.web.to_manifest_svg` (scalable, named, flat,
prefixed, on its paper card) and then through `figlib.checks`:
self-painting (no class, no style, no var()), the worksheet's element and
attribute subset, WCAG AA contrast against what each label actually sits
on, no text on a dark fill, legible at 360px (>= 11px text, >= 1px
strokes), AQA symbols only (no motor, no d.c. box), Georgia first.
Plus: an id is unique and `[a-z0-9-]+`, a record has title and desc, and
every id any question references resolves.

    python3 build_figures.py            build and write
    python3 build_figures.py --check    build in memory; exit 1 if any
                                        committed output differs (writes
                                        nothing)
    python3 build_figures.py --mirror   exit 1 if the backend's figures.json
                                        differs from this build (writes
                                        nothing)
    python3 build_figures.py --catalogue-json PATH
                                        also write EVERY catalogue figure
                                        (shipped or not) to PATH, for review
"""

import argparse
import glob
import importlib
import json
import os
import re
import sys

import figlib
import ks3_data
import ks4_art
import ks4_data
from figlib import checks as figchecks
from figlib import web as figweb
from figlib.catalogue_ks3 import CATALOGUE as KS3_CATALOGUE
from ks3_data.question_bank import all_questions as ks3_bank_questions

REPO = os.path.dirname(os.path.abspath(__file__))
_ID_RE = re.compile(r"^[a-z0-9-]+$")
_VIEWBOX_RE = re.compile(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"')

FIGURES_JSON = "figures.json"
FIGURES_JS_KS3 = "shared/figures-ks3.js"
FIGURES_JS_KS4 = "shared/figures-ks4.js"


def _ks4_catalogue():
    records, owner = [], {}
    for mod, rec in ks4_art.load_catalogue():
        fid = rec.get("id")
        if fid in owner:
            raise SystemExit(
                "build_figures: figure id %r is declared in BOTH "
                "ks4_art/%s.py and ks4_art/%s.py. One id, one owner — "
                "per-lane catalogue files exist so lanes cannot collide, "
                "and a duplicate is exactly the collision they prevent."
                % (fid, owner[fid], mod))
        owner[fid] = mod
        records.append(rec)
    return records


# ── demand: who references a figure id, across all four corpora ──────────

def _ks3_referenced_ids():
    ids = set()
    for q in ks3_bank_questions():
        if q.get("figure"):
            ids.add(q["figure"])
    for unit in ks3_data.build_units():
        for lesson in unit["lessons"]:
            for rung in (lesson.get("ladder") or {}).values():
                if isinstance(rung, dict) and rung.get("figure"):
                    ids.add(rung["figure"])
    return ids


def _ks4_bank_referenced_ids():
    ids = set()
    for _subj, _topic, mod in ks4_data._modules():
        if isinstance(mod, ks4_data._Broken):
            continue    # another lane's half-saved file; load_pool skips it too
        for q in (getattr(mod, "QUESTIONS", None) or []):
            if q.get("figure"):
                ids.add(q["figure"])
    return ids


def _ks4_quiz_referenced_ids():
    ids = set()
    for path in sorted(glob.glob(os.path.join(REPO, "all_subtopics_*.py"))):
        mod = importlib.import_module(os.path.basename(path)[:-3])
        for name in dir(mod):
            if not name.endswith("_SUBTOPICS_ALL"):
                continue
            for subtopics in getattr(mod, name).values():
                for st in subtopics:
                    for item in (st.get("quiz") or []):
                        if item.get("figure"):
                            ids.add(item["figure"])
    return ids


def referenced_ids():
    """`(ks3_ids, ks4_ids)` — every figure id a question names, per key
    stage, scanned fresh on every build (never hand-maintained)."""
    return (_ks3_referenced_ids(),
            _ks4_bank_referenced_ids() | _ks4_quiz_referenced_ids())


# ── drawing ───────────────────────────────────────────────────────────────

def _render(rec, where):
    fid = rec.get("id")
    if not fid or not _ID_RE.match(fid):
        raise ValueError("figure id %r (%s) does not match [a-z0-9-]+" % (fid, where))
    if not rec.get("title") or not rec.get("desc"):
        raise ValueError("figure %r (%s) has no title/desc — the title is the "
                         "alt text, and a figure without one ships blank to a "
                         "screen reader" % (fid, where))
    svg = figweb.to_manifest_svg(figlib.draw(rec), fid, rec["title"], rec["desc"])
    m = _VIEWBOX_RE.search(svg)
    return {"svg": svg, "alt": rec["title"],
            "w": float(m.group(1)), "h": float(m.group(2))}


def build():
    """`(manifest, ks3_ids, ks4_ids, everything, report)`.

    `everything` is every catalogue figure, shipped or not; `manifest` is
    what ships. Raises SystemExit, listing every problem, if anything fails.
    """
    ks3_wanted, ks4_wanted = referenced_ids()
    ks4_records = _ks4_catalogue()
    everything, where = {}, {}
    problems = []
    for label, records in (("figlib/catalogue_ks3.py", KS3_CATALOGUE),
                           ("ks4_art catalogue", ks4_records)):
        for rec in records:
            fid = rec.get("id")
            if fid in everything:
                problems.append("figure id %r is declared twice (%s and %s)"
                                % (fid, where[fid], label))
                continue
            try:
                everything[fid] = _render(rec, label)
                where[fid] = label
            except (ValueError, KeyError, TypeError) as exc:
                problems.append("%s (%s): %s" % (fid, label, exc))
    problems.extend(figchecks.check_manifest(everything))

    ks3_ids = {r["id"] for r in KS3_CATALOGUE}
    ks4_ids = {r["id"] for r in ks4_records}
    for fid in sorted(ks3_wanted - ks3_ids):
        problems.append("a KS3 question references figure %r, which "
                        "figlib/catalogue_ks3.py does not declare" % fid)
    for fid in sorted(ks4_wanted - ks4_ids):
        problems.append("a KS4 question references figure %r, which no "
                        "ks4_art/catalogue*.py declares" % fid)
    if problems:
        raise SystemExit(
            "build_figures: REFUSING TO WRITE — %d problem(s):\n  %s\n"
            "Every one of these is something a pupil would see. Fix the "
            "drawing or the catalogue; never the check."
            % (len(problems), "\n  ".join(problems)))

    ship_ks3 = ks3_wanted & ks3_ids
    manifest = {fid: everything[fid] for fid in sorted(ship_ks3 | ks4_ids)}
    report = {"ks3_unused": sorted(ks3_ids - ks3_wanted),
              "ks4_unused": sorted(ks4_ids - ks4_wanted)}
    return manifest, ship_ks3, ks4_ids, everything, report


def render_outputs(manifest, ks3_ids, ks4_ids):
    """`{path: text}` — exactly the bytes `write()` puts on disk."""
    payload = json.dumps(manifest, separators=(",", ":"), sort_keys=True) + "\n"

    def subset_js(ids):
        subset = {fid: manifest[fid] for fid in sorted(ids)}
        body = json.dumps(subset, separators=(",", ":"), sort_keys=True)
        return ("window.MRBFigures = Object.assign(window.MRBFigures || "
                "{}, %s);\n" % body)

    return {FIGURES_JSON: payload,
            FIGURES_JS_KS3: subset_js(ks3_ids),
            FIGURES_JS_KS4: subset_js(ks4_ids)}


def _backend_dir():
    sys.path.insert(0, os.path.join(REPO, "tools"))
    from export_curriculum_tree import default_out_dir
    return default_out_dir()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--mirror", action="store_true")
    ap.add_argument("--catalogue-json")
    args = ap.parse_args(argv)

    manifest, ks3_ids, ks4_ids, everything, report = build()
    outputs = render_outputs(manifest, ks3_ids, ks4_ids)
    summary = ("%d figure(s) shipped (%d KS3 / %d KS4) of %d in the "
               "catalogues, all passing figlib.checks"
               % (len(manifest), len(ks3_ids), len(ks4_ids), len(everything)))

    if args.catalogue_json:
        with open(args.catalogue_json, "w") as f:
            json.dump(everything, f, sort_keys=True)

    if args.mirror:
        path = os.path.join(_backend_dir(), FIGURES_JSON)
        have = open(path).read() if os.path.isfile(path) else None
        if have == outputs[FIGURES_JSON]:
            print("✅ %s matches this build — %s" % (path, summary))
            return 0
        print("❌ %s %s. Copy this repo's figures.json across (the backend "
              "renders worksheets from it)." % (
                  path, "does not exist" if have is None else "has DRIFTED"))
        return 1

    if args.check:
        drift = [p for p, text in outputs.items()
                 if not os.path.isfile(os.path.join(REPO, p))
                 or open(os.path.join(REPO, p)).read() != text]
        if drift:
            print("❌ committed figure output is stale: %s. Run "
                  "python3 build_figures.py (build_all.py runs it)."
                  % ", ".join(drift))
            return 1
        print("✅ build_figures --check: %s; committed output matches" % summary)
        return 0

    for path, text in outputs.items():
        with open(os.path.join(REPO, path), "w") as f:
            f.write(text)
    print("build_figures: %s -> %s, %s, %s"
          % (summary, FIGURES_JSON, FIGURES_JS_KS3, FIGURES_JS_KS4))
    for key, label in (("ks3_unused", "KS3"), ("ks4_unused", "KS4")):
        if report[key]:
            print("build_figures: %s catalogue ids no question references "
                  "yet (%d): %s" % (label, len(report[key]),
                                     ", ".join(report[key])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
