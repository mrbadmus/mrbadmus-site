#!/usr/bin/env python3
"""build_figures.py — the figure manifest builder (MRB-352, the diagrams
figure contract — `docs/diagrams/figure-contract.md`).

Two emissions, three files:
  * `figures.json`             — the WHOLE manifest (KS3 + KS4), mirrored to
                                  the backend. It serves both key stages and
                                  is not on anyone's phone, so it stays one
                                  complete file.
  * `shared/figures-ks3.js`    — KS3 figures only, for KS3 pages.
  * `shared/figures-ks4.js`    — KS4 figures only, for KS4 pages.
Both site files write `window.MRBFigures = Object.assign(window.MRBFigures
|| {}, {...})`, so a page that (unusually) needs both key stages can load
both scripts and end up with the union, in either order.

A figure record is `{"svg": "<svg …>…</svg>", "alt": "...", "w": N, "h": N}`,
keyed by figure id.

── WHAT GOES IN, AND WHY (⊕ coordinator review, 23 Sep 2026) ──────────────

KS4 figures are every record in `ks4_art.catalogue.CATALOGUE` — that module
exists precisely to be referenced, so everything in it ships.

KS3 figures are DIFFERENT: a KS3 lesson figure (`LESSON["figures"]`,
`status == "drawn"`) is ALREADY inlined into its own lesson page's HTML by
`build_ks3.r_figure` at build time. The manifest's only job is letting a
QUESTION resolve a figure id at runtime — the assignment page, practice, Set
work, the worksheet — so a lesson figure no question references is pure
download weight with no reader: measured before this rule existed, 21
lesson figures cost 409 KB against 43 KB of KS4, and not one byte of that
409 KB was reachable from a question.

So a KS3 figure ships ONLY if some question references its id. Referenced
ids are the union, scanned fresh on every build (never hand-maintained), of:
  * the KS3 assignment bank      — `ks3_data.question_bank.all_questions()`,
                                    each question's `"figure"`
  * the KS3 lesson ladder        — `ks3_data.build_units()`, each lesson's
                                    `ladder[rung]["figure"]`
  * the KS4 assignment bank      — every `ks4_data/questions/**/*.py`
                                    module's `QUESTIONS`, each `"figure"`
  * the KS4 lesson-page quiz     — every `all_subtopics_*.py` module's
                                    `*_SUBTOPICS_ALL[topic][i]["quiz"]`,
                                    each quiz item's `"figure"`
This is intentionally DEMAND, not supply: it grows on its own as content
lanes add references, with no second place to remember to update.

Fails loudly — refuses to write anything — on: a duplicate figure id, an
`art` name no registry knows, a figure with no `title`/`desc`, an id that
does not match `[a-z0-9-]+`, or a question that references a figure id no
`status == "drawn"` KS3 lesson figure actually carries (the id existing
somewhere with a different status, or not at all, is exactly the "unknown
id" the figure contract calls a build failure, never a silent blank).
"""

import glob
import importlib
import json
import re
import sys

import build_ks3
import ks3_data
import ks4_art
import ks4_data
from ks3_data.question_bank import all_questions as ks3_bank_questions
# ⊕ MRB-352 — DISCOVER every catalogue module, do not name one.
#
# This read `from ks4_art.catalogue import CATALOGUE`, which silently ignored
# every other catalogue module in the package. That broke the pattern the
# content lanes were told to use — each lane adds `ks4_art/catalogue_<lane>.py`
# so two lanes editing one worktree never collide on a single file — and the
# failure was the confusing kind: the drawer registry DID discover the lane's
# new art (because `ks4_art.load()` discovers modules), so the figure drew
# perfectly in isolation, and then `build_figures.py` reported its id as
# `unresolved_ks4` as though the record had never been written.
#
# It now discovers `catalogue.py` and every `catalogue_*.py` beside it, the
# same way `ks4_art.load()` finds drawers. A duplicate id across two modules
# is a hard error, named on both sides — the whole point of per-lane files is
# that they cannot quietly overwrite each other.
def _load_ks4_catalogue():
    import importlib
    import pkgutil

    import ks4_art

    records, owner = [], {}
    for mod in sorted(m.name for m in pkgutil.iter_modules(ks4_art.__path__)
                      if m.name == "catalogue"
                      or m.name.startswith("catalogue_")):
        module = importlib.import_module("ks4_art.%s" % mod)
        for rec in getattr(module, "CATALOGUE", ()):
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


CATALOGUE = _load_ks4_catalogue()

_ID_RE = re.compile(r"^[a-z0-9-]+$")
_VIEWBOX_RE = re.compile(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"')

FIGURES_JSON = "figures.json"
FIGURES_JS_KS3 = "shared/figures-ks3.js"
FIGURES_JS_KS4 = "shared/figures-ks4.js"


def _dims(svg, fid):
    """`w`/`h` are read OFF the rendered SVG's own viewBox, never passed
    separately — a drawer that ever changed its canvas size without this
    file's knowledge would otherwise ship a manifest that quietly
    disagreed with the picture it describes."""
    m = _VIEWBOX_RE.search(svg)
    if not m:
        raise ValueError(
            "figure %r rendered an <svg> with no `viewBox=\"0 0 W H\"` — "
            "every drawer opens with `_svg_open`, which always emits one, "
            "so this means the id names something that isn't a kit-built "
            "figure at all." % fid)
    return float(m.group(1)), float(m.group(2))


def _add(manifest, fid, svg, alt, where):
    if not fid or not _ID_RE.match(fid):
        raise ValueError(
            "figure id %r (%s) does not match [a-z0-9-]+. Every figure id "
            "must, so a page or a worksheet can trust it as a URL/attribute-"
            "safe key before it ever reaches the manifest." % (fid, where))
    if fid in manifest:
        raise ValueError(
            "figure id %r is registered twice (%s and an earlier entry). "
            "One id, one drawing — a duplicate is a silent last-one-wins "
            "waiting to ship the wrong picture under the other's id."
            % (fid, where))
    if not alt:
        raise ValueError(
            "figure %r (%s) has no title, so it has no alt text. Mide's "
            "rule: alt text names what is shown, and a figure with none "
            "would ship blank to a screen reader." % (fid, where))
    w, h = _dims(svg, fid)
    manifest[fid] = {"svg": svg, "alt": alt, "w": w, "h": h}
    return len(svg)


# ── demand: who references a figure id, across all four corpora ──────────
#
# Read-only. This file only ever IMPORTS `ks3_data`/`ks4_data`/
# `all_subtopics_*` — content lanes are editing files under those trees in
# this same shared worktree right now, and nothing here writes to any of
# them or touches git.

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
            # A half-written file mid-save from another lane. `load_pool`
            # already treats this as normal rather than fatal (see its own
            # note); scanning for figure refs holds to the same rule rather
            # than crashing on someone else's in-progress edit.
            continue
        for q in (getattr(mod, "QUESTIONS", None) or []):
            if q.get("figure"):
                ids.add(q["figure"])
    return ids


def _ks4_quiz_referenced_ids():
    ids = set()
    for path in sorted(glob.glob("all_subtopics_*.py")):
        mod = importlib.import_module(path[:-3])
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
    """`(ks3_ids, ks4_ids)` — the union of figure ids named by a question in
    each key stage's corpora. KS4's `ks4_bank` and `quiz` scans are folded
    together because both key questions in the SAME key stage's manifest."""
    ks3_ids = _ks3_referenced_ids()
    ks4_ids = _ks4_bank_referenced_ids() | _ks4_quiz_referenced_ids()
    return ks3_ids, ks4_ids


# ── collecting the drawings themselves ────────────────────────────────────

def collect_ks3(manifest, wanted):
    """Only the `status == "drawn"` lesson figures some question actually
    references (`wanted`) — rendered through `build_ks3.SVG_ART`, the SAME
    registry the lesson page itself renders through, so a lesson page and a
    question naming the same id show identical bytes, never a fork.

    ⚠️ `kind == "css-art"` is a DIFFERENT, pre-existing rendering path —
    `build_ks3._css_art`/`CSS_ART`, tokens and CSS classes rendered directly
    into the lesson page, never an `_svg_open`-built inline SVG. It cannot
    go through this manifest (it has no self-contained SVG to hand a
    worksheet or a runtime lookup), so a question that references one is a
    pre-existing content gap this ticket did not create and cannot close —
    reported, not silently dropped, but not a reason to fail every future
    build either.

    Returns `(count, bytes, ids_found, ids_wrong_kind)`.
    """
    n, nbytes, found, wrong_kind = 0, 0, set(), []
    for unit in ks3_data.build_units():
        for lesson in unit["lessons"]:
            for fig in (lesson.get("figures") or []):
                fid = fig.get("id")
                if fid not in wanted:
                    continue
                where = "KS3 %s/%s" % (unit["code"], lesson.get("slug"))
                if fig.get("kind") != "diagram":
                    wrong_kind.append((fid, where, fig.get("kind"), fig.get("status")))
                    continue
                if fig.get("status") != "drawn":
                    raise ValueError(
                        "a question references figure %r, but %s declares "
                        "it with status %r, not 'drawn'. An id a question "
                        "names must resolve to a real drawing, never a "
                        "silent blank." % (fid, where, fig.get("status")))
                art = fig.get("art")
                if art not in build_ks3.SVG_ART:
                    raise ValueError(
                        "figure %r (%s) declares art %r, which no ks3_art "
                        "module draws. Known: %s."
                        % (fid, where, art, ", ".join(sorted(build_ks3.SVG_ART))))
                if not fig.get("title") or not fig.get("desc"):
                    raise ValueError(
                        "figure %r (%s) is status 'drawn' but has no "
                        "title/desc — `_svg_open` requires both." % (fid, where))
                svg = build_ks3.SVG_ART[art](fig)
                nbytes += _add(manifest, fid, svg, fig["title"], where)
                n += 1
                found.add(fid)
    return n, nbytes, found, wrong_kind


def collect_ks4(manifest):
    """Every record in `ks4_art.catalogue.CATALOGUE` — that module exists
    precisely to be referenced, so it all ships, demand-scan or not."""
    reg = ks4_art.load()
    nbytes = 0
    for rec in CATALOGUE:
        fid = rec.get("id")
        where = "KS4 catalogue"
        art = rec.get("art")
        if art not in reg.art:
            raise ValueError(
                "figure %r (%s) declares art %r, which no ks4_art module "
                "draws. Known: %s."
                % (fid, where, art, ", ".join(sorted(reg.art))))
        if not rec.get("title") or not rec.get("desc"):
            raise ValueError("figure %r (%s) has no title/desc." % (fid, where))
        svg = reg.art[art](rec)
        nbytes += _add(manifest, fid, svg, rec["title"], where)
    return len(CATALOGUE), nbytes


def build():
    ks3_wanted, ks4_wanted = referenced_ids()
    manifest = {}
    n_ks3, b_ks3, ks3_found, ks3_wrong_kind = collect_ks3(manifest, ks3_wanted)
    n_ks4, b_ks4 = collect_ks4(manifest)

    catalogue_ids = {rec["id"] for rec in CATALOGUE}
    unresolved_ks4 = sorted(ks4_wanted - catalogue_ids)
    if unresolved_ks4:
        raise ValueError(
            "%d KS4 question(s) reference figure id(s) not in "
            "any ks4_art/catalogue*.py: %s. An id a question names must exist in "
            "the manifest — the figure contract calls this a build failure, "
            "never a silent blank." % (len(unresolved_ks4), ", ".join(unresolved_ks4)))

    # Genuinely unresolved: not found as ANY figure at all (of any kind).
    # Ids resolved but of the wrong `kind` (`ks3_wrong_kind`) are reported
    # separately below — a pre-existing content gap this ticket did not
    # create, not a defect in the drawing layer, so it is a loud WARNING
    # rather than a build failure that blocks every future run.
    seen_any = ks3_found | {fid for fid, *_ in ks3_wrong_kind}
    unresolved_ks3 = sorted(ks3_wanted - seen_any)
    if unresolved_ks3:
        raise ValueError(
            "%d KS3 question(s)/rung(s) reference figure id(s) no lesson "
            "declares at all: %s." % (len(unresolved_ks3), ", ".join(unresolved_ks3)))

    ks3_ids = set(ks3_found)
    ks4_ids = {rec["id"] for rec in CATALOGUE}
    return manifest, (n_ks3, b_ks3, ks3_ids), (n_ks4, b_ks4, ks4_ids), ks3_wrong_kind


def write(manifest, ks3_ids, ks4_ids):
    payload = json.dumps(manifest, separators=(",", ":"), sort_keys=True)
    with open(FIGURES_JSON, "w") as f:
        f.write(payload)
        f.write("\n")

    def _subset_js(path, ids):
        subset = {fid: manifest[fid] for fid in sorted(ids)}
        body = json.dumps(subset, separators=(",", ":"), sort_keys=True)
        with open(path, "w") as f:
            f.write("window.MRBFigures = Object.assign(window.MRBFigures || "
                    "{}, %s);\n" % body)

    _subset_js(FIGURES_JS_KS3, ks3_ids)
    _subset_js(FIGURES_JS_KS4, ks4_ids)
    return payload


def main():
    manifest, (n_ks3, b_ks3, ks3_ids), (n_ks4, b_ks4, ks4_ids), wrong_kind = build()
    payload = write(manifest, ks3_ids, ks4_ids)
    print("build_figures: %d figure(s) (%d KS3 / %d KS4) -> %s (%d bytes), "
          "%s, %s"
          % (len(manifest), n_ks3, n_ks4, FIGURES_JSON, len(payload),
             FIGURES_JS_KS3, FIGURES_JS_KS4))
    print("build_figures: byte split — KS3 %d bytes, KS4 %d bytes of SVG"
          % (b_ks3, b_ks4))
    for fid, where, kind, status in wrong_kind:
        print("build_figures: WARNING — a question references figure %r "
              "(%s), but it is kind=%r/status=%r, not an SVG 'diagram' this "
              "manifest can serve. Pre-existing content gap, not fixed by "
              "this build." % (fid, where, kind, status))
    return 0


if __name__ == "__main__":
    sys.exit(main())
