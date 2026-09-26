#!/usr/bin/env python3
"""ks4_lessons — the 14 KS4 pilot lesson records (docs/ks4/pilot-build-contract.md §0).

One dict per lesson in `LESSONS`. Every `slug` here was verified against the
site's own subtopic data (`all_subtopics_chemistry*.py` / `all_subtopics_physics*.py`)
by `verify_slugs()` below — not copied from the contract table on trust, because
the contract itself says that table "was read from the data by a scout, not
proven." `build_ks4.py` calls `verify_slugs()` before it does anything else and
stops the build if a single slug is wrong.

Fields
------
slug        — the site slug: the subtopic `id` in all_subtopics_*.py, and the
              filename stem the generator writes (`<slug>.html`).
design_file — the delivered `.dc.html` this lesson compiles from, under
              `docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and
              Electricity/`.
subject     — `chemistry` | `physics`. Matches the key into
              all_subtopics_<subject>*.py and the URL segment.
topic_id    — the topic key inside that subject's subtopic dict
              (`bonding` for all 12 chemistry lessons, `electricity` for the
              2 physics lessons) — also the URL segment before the slug.
title       — the lesson title, for the manifest/report only (the page's own
              `<h1>` comes from Design's template, not from here).
spec        — the AQA spec point shown in the contract table. Nanoparticles is
              deliberately `4.2.4` here even though the design FILENAME still
              says `5.2.3.3` — see flag 2 in NOTES-KS4-pilot.md §9: the page
              itself already shows 4.2.4 (verified, R5 is a no-op check, not a
              rewrite) and the filename is frozen because renaming it would
              break every cross-reference the delivery makes to it by name.
family      — Design's pedagogical family label (README.txt), carried for the
              inventory; not read by the compiler.
routes      — the route labels this lesson ships on. 4 for every lesson except
              nanoparticles (Triple only — the whole lesson is 8462 4.2.4,
              chemistry-only content, so it has no Combined route at all).
review_state — 'examiner-reviewed' for all 14 as of 26 Sep 2026 (the science
              examination is complete for all 14 lessons and every required
              change is applied and proven by `ks4_science_rulings.expect_
              present`; see the freeze mechanism in `ks4_lessons/frozen.json`
              and `build_ks4.py --freeze`). Was 'draft' before the
              examination landed. Feeds `showDraft` at mount: 'draft' -> true,
              'examiner-reviewed' / 'frozen' -> false.
design_slug — the string literal `const slug = '...'` and the `Ks4Ladder
              slug="..."` attribute carry INSIDE Design's verbatim component,
              when it differs from the site slug. `None` when they already
              match. ks4_rulings.py rewrites these three lessons' internal
              slug constant to the site slug (examiner finding, 25 Sep 2026)
              so `KS4.find`/`KS4.bank`/`KS4.tip` resolve against
              `shared/ks4-source.js`, which is generated keyed by SITE slug.
block_map   — only present when a lesson's own `<section>` ids/classes are not
              enough for `ks4_lessons.blocks.classify_section()` to infer a
              type; maps a section's `id` (or a 0-based section index when it
              has none) to one of the registered block types.
"""

import os
import sys

# ── the 14 lessons, in the contract's unit order ──────────────────────────
LESSONS = [
    dict(slug="chemical-bonds", design_file="ks4-chemistry-5.2.1.1-chemical-bonds.dc.html",
         subject="chemistry", topic_id="bonding", title="Chemical bonds",
         spec="5.2.1.1", family="Classify", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="ionic-bonding", design_file="ks4-chemistry-5.2.1.2-ionic-bonding.dc.html",
         subject="chemistry", topic_id="bonding", title="Ionic bonding",
         spec="5.2.1.2", family="Process", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None,
         # 's-forge' — "Formula forge": Al2O3/Li2S/Ca3N2 worked interactively
         # with a live charge meter (NOTES-KS4-pilot.md §7.2). A guided
         # construction exercise, not a check-your-understanding activity.
         block_map={"s-forge": "worked-example"}),
    dict(slug="ionic-compounds", design_file="ks4-chemistry-5.2.1.3-ionic-compounds.dc.html",
         subject="chemistry", topic_id="bonding", title="Ionic compounds",
         spec="5.2.1.3", family="Model", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="covalent-bonding", design_file="ks4-chemistry-5.2.1.4-covalent-bonding.dc.html",
         subject="chemistry", topic_id="bonding", title="Covalent bonding",
         spec="5.2.1.4", family="Process", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="metallic-bonding", design_file="ks4-chemistry-5.2.1.5-metallic-bonding.dc.html",
         subject="chemistry", topic_id="bonding", title="Metallic bonding",
         spec="5.2.1.5", family="Model", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="states-of-matter", design_file="ks4-chemistry-5.2.2.1-states-of-matter.dc.html",
         subject="chemistry", topic_id="bonding", title="States of matter",
         spec="5.2.2.1", family="Investigation", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="properties-ionic-compounds",
         design_file="ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html",
         subject="chemistry", topic_id="bonding", title="Properties of ionic compounds",
         spec="5.2.2.3", family="Contrast", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None,
         # 's-bench' — the side-by-side solid/molten/solution conductivity
         # simulation (NOTES §7.7): a practical, simulated on screen.
         # 's-examiner' — "Be the examiner": mark a sample 1/3 answer
         # (NOTES §7.7) — a self-check activity.
         block_map={"s-bench": "practical", "s-examiner": "check"}),
    dict(slug="properties-small-molecules",
         design_file="ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html",
         subject="chemistry", topic_id="bonding", title="Properties of small molecules",
         spec="5.2.2.4", family="Model", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="polymers", design_file="ks4-chemistry-5.2.2.5-polymers.dc.html",
         subject="chemistry", topic_id="bonding", title="Polymers",
         spec="5.2.2.5", family="Classify", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="giant-covalent-structures",
         design_file="ks4-chemistry-5.2.2.6-giant-covalent-structures.dc.html",
         subject="chemistry", topic_id="bonding", title="Giant covalent structures",
         spec="5.2.2.6", family="Contrast", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="metals-alloys", design_file="ks4-chemistry-5.2.2.7-metals-alloys.dc.html",
         subject="chemistry", topic_id="bonding", title="Metals and alloys",
         spec="5.2.2.7", family="Contrast", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug="metals-and-alloys"),
    # ⊕ flag 2 (NOTES §9): the delivered FILENAME still says 5.2.3.3 (which is
    # graphene/fullerenes, L10's content) but the PAGE ITSELF already shows
    # "AQA Chemistry 4.2.4 (chemistry only)" in its eyebrow — verified by
    # reading the compiled markup, not assumed. `spec` here is the true one;
    # R5 in ks4_rulings.py asserts the page already says it rather than
    # rewriting anything.
    dict(slug="nanoparticles", design_file="ks4-chemistry-5.2.3.3-nanoparticles.dc.html",
         subject="chemistry", topic_id="bonding", title="Nanoparticles",
         spec="4.2.4", family="Quantitative", routes=["TF", "TH"],
         review_state="examiner-reviewed", design_slug=None),
    dict(slug="series-parallel-circuits",
         design_file="ks4-physics-6.2.2-series-parallel-circuits.dc.html",
         subject="physics", topic_id="electricity", title="Series and parallel circuits",
         spec="6.2.2", family="System", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug="series-and-parallel"),
    dict(slug="resistors",
         design_file="ks4-physics-6.2.1.4-resistors-iv-required-practical.dc.html",
         subject="physics", topic_id="electricity", title="Resistors and I-V characteristics",
         spec="6.2.1.4", family="Required practical", routes=["CF", "CH", "TF", "TH"],
         review_state="examiner-reviewed", design_slug="resistors-iv"),
]

LESSON_BY_SLUG = {L["slug"]: L for L in LESSONS}
LESSON_BY_DESIGN_FILE = {L["design_file"]: L for L in LESSONS}

DESIGN_DIR = os.path.join(
    "docs", "ks4", "design-reference", "pilot", "KS4 Lessons",
    "Pilot - Bonding and Electricity")

ROUTE_LABELS = {
    "CF": "Combined Foundation", "CH": "Combined Higher",
    "TF": "Triple Foundation", "TH": "Triple Higher",
}
# pathway/tier URL segments per route code
ROUTE_URL = {
    "CF": ("combined", "foundation"), "CH": ("combined", "higher"),
    "TF": ("triple", "foundation"), "TH": ("triple", "higher"),
}


def site_url(slug, route):
    """The live URL path for `slug` at `route` ('CF'/'CH'/'TF'/'TH')."""
    L = LESSON_BY_SLUG[slug]
    pathway, tier = ROUTE_URL[route]
    return "/%s/%s/%s/%s/%s.html" % (pathway, tier, L["subject"], L["topic_id"], slug)


def verify_slugs():
    """Every `slug` above must be a real subtopic id in the site's own data,
    under the stated `subject`/`topic_id`, on at least one of the four
    per-route all_subtopics_* files. Raises SystemExit naming exactly what
    was wrong — this is the check the contract's table itself asks for
    ("verify every slug against all_subtopics_*.py before relying on it").
    """
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    mods = {
        "chemistry": [
            ("all_subtopics_chemistry", "CHEMISTRY_SUBTOPICS_ALL"),
            ("all_subtopics_chemistry_higher", "CHEMISTRY_SUBTOPICS_ALL"),
            ("all_subtopics_chemistry_triple_foundation", "CHEMISTRY_SUBTOPICS_ALL"),
            ("all_subtopics_chemistry_triple_higher", "CHEMISTRY_SUBTOPICS_ALL"),
        ],
        "physics": [
            ("all_subtopics_physics", "PHYSICS_SUBTOPICS_ALL"),
            ("all_subtopics_physics_higher", "PHYSICS_SUBTOPICS_ALL"),
            ("all_subtopics_physics_triple_foundation", "PHYSICS_SUBTOPICS_ALL"),
            ("all_subtopics_physics_triple_higher", "PHYSICS_SUBTOPICS_ALL"),
        ],
    }
    import importlib
    errors = []
    for L in LESSONS:
        found_any = False
        found_specs = set()
        for modname, attr in mods[L["subject"]]:
            mod = importlib.import_module(modname)
            data = getattr(mod, attr)
            topic_list = data.get(L["topic_id"], [])
            hit = next((s for s in topic_list if s["id"] == L["slug"]), None)
            if hit is not None:
                found_any = True
                if hit.get("spec"):
                    found_specs.add(hit["spec"])
        if not found_any:
            errors.append(
                "%s: slug %r not found under topic %r in ANY "
                "all_subtopics_%s*.py file" % (L["design_file"], L["slug"],
                                                L["topic_id"], L["subject"]))
        # nanoparticles is the one deliberate spec-label departure (flag 2).
        # states-of-matter and metals-alloys carry a RANGE in the data
        # ('5.2.2.1–5.2.2.2', '5.2.2.7–5.2.2.8') because flag 10
        # (NOTES §9) folds 5.2.2.2/5.2.2.8 into these two lessons; the
        # contract's single spec point is the lesson's PRIMARY point and must
        # be a PREFIX of the data's range, not an exact match.
        if (L["slug"] != "nanoparticles" and found_specs
                and not any(s == L["spec"] or s.startswith(L["spec"] + "–")
                             for s in found_specs)):
            errors.append(
                "%s: contract spec %r does not match the data's spec %r"
                % (L["design_file"], L["spec"], sorted(found_specs)))
    if errors:
        raise SystemExit(
            "ks4_lessons.verify_slugs: %d problem(s):\n  " % len(errors)
            + "\n  ".join(errors))
    return True


if __name__ == "__main__":
    verify_slugs()
    print("ks4_lessons: all %d slugs verified against all_subtopics_*.py" % len(LESSONS))
