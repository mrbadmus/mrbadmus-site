#!/usr/bin/env python3
"""export_curriculum_tree.py — the curriculum, as a file the backend can read.

    python3 tools/export_curriculum_tree.py            # write curriculum-tree.json
    python3 tools/export_curriculum_tree.py --check    # exit 1 if it has drifted
    python3 tools/export_curriculum_tree.py --out DIR  # write it somewhere else
    python3 tools/export_curriculum_tree.py --stdout   # print it and write nothing

WHY THIS FILE EXISTS
────────────────────
Set work v2 (MRB-335) lets a teacher pick a node of the curriculum — a KS4
topic or subtopic, a KS3 unit or lesson — instead of a scheme-of-work row. The
curriculum is authored in THIS repo, in Python: `generate_site_v5`'s
`PATHWAY_TOPIC_MAP` orders the topics, `ks4_data.classify()` says which tier and
pathway each subtopic belongs to, `ks4_seed_sow.topic_titles()` holds the titles
AQA actually uses, and `ks3_data` holds the 33 units and 185 lessons.

The backend is Node. It cannot import any of that, and it must not re-type it:
a second hand-maintained list of 264 subtopics is a second list that goes wrong,
and the way it would go wrong is a teacher being offered a topic their class is
not taught. So the tree is EXPORTED, once, into a JSON file that is committed in
the backend repo and read at boot.

⚠️ `--check` IS THE POINT, not a convenience. It rebuilds the tree from the
Python and compares it byte for byte with the committed backend file, so a gate
can prove the mirror has not drifted. Content lanes add questions, not
subtopics — but a spec revision that adds one, or a renamed topic, would
otherwise leave the sheet offering something the pool cannot fill, and nothing
would say so.

THE SHAPE
─────────
    { "ks4": { "<subject>": [ { "id", "name", "paper",
                                "subtopics": [ { "slug", "name", "tier",
                                                 "triple_only" } ] } ] },
      "ks3": { "<subject>": [ { "code", "slug", "name",
                                "lessons": [ { "slug", "name" } ] } ] } }

Both key stages are exported WHOLE — every subtopic of every KS4 topic, at both
tiers and both pathways. The backend filters per class (`treeForClass()` in
`set-work-scope.js`), because filtering is a per-request question and the file
is not per-request. A combined class is served the topics minus the
`triple_only` subtopics, and minus any topic all of whose subtopics are
triple-only — which today is exactly `space`.

⚠️ ORDER IS DATA. KS4 topics come out in `PATHWAY_TOPIC_MAP[("triple","higher")]`
order, which is teaching order and is what the site itself lists; subtopics come
out in the authored order inside the module, which is the order the topic page
renders them in. KS3 units come out in `structure.UNITS` declaration order and
lessons in default teaching order. A sheet that reordered them would be showing
a teacher a curriculum nobody teaches.
"""

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

OUT_NAME = "curriculum-tree.json"

# ── the paper map (RISKS C8), and it is a CONSTANT here on purpose ──────
#
# AQA puts each KS4 topic on exactly one of the two papers, and nothing in the
# site's data says which — the topic pages do not carry it and neither does the
# scheme seed. So it is written out, keyed by (subject, topic id), and asserted
# COMPLETE against the tree below: a topic the map does not name fails this
# script rather than exporting a null the sheet would then have to render as a
# missing chip.
#
# ⚠️ KEYED BY (SUBJECT, TOPIC), NEVER BY TOPIC ALONE. `atomic-structure` is a
# topic id in BOTH chemistry (paper 1) and physics (paper 1), and the day one of
# them moves, a topic-only map would move both.
#
# `space` is physics paper 2 and is triple-only at topic level: every one of its
# five subtopics is `triple_only`, so it never appears on a combined tree at all.
KS4_PAPER = {
    "biology": {
        "cell-biology": 1, "organisation": 1, "infection-response": 1,
        "bioenergetics": 1,
        "homeostasis": 2, "inheritance": 2, "ecology": 2,
    },
    "chemistry": {
        "atomic-structure": 1, "bonding": 1, "quantitative": 1,
        "chemical-changes": 1, "energy-changes": 1,
        "rates-equilibrium": 2, "organic": 2, "analysis": 2,
        "atmosphere": 2, "resources": 2,
    },
    "physics": {
        "energy": 1, "electricity": 1, "particle-model": 1,
        "atomic-structure": 1,
        "forces": 2, "waves": 2, "magnetism": 2, "space": 2,
    },
}

SUBJECTS = ("biology", "chemistry", "physics")


# ── KS4 ────────────────────────────────────────────────────────────────

def _ks4_subtopic_titles(subject):
    """slug → authored title, from the Triple Higher module.

    Triple Higher is the SUPERSET — `ks4_data.classify()` asserts the twelve
    blocks nest and walks that block precisely because it visits every subtopic
    in the subject exactly once — so one module holds every title. Reading the
    other three would add nothing but a chance for two of them to disagree.
    """
    import importlib
    mod = importlib.import_module("all_subtopics_%s_triple_higher" % subject)
    pages = getattr(mod, "%s_SUBTOPICS_ALL" % subject.upper())
    titles = {}
    for topic_id, subtopics in pages.items():
        for st in subtopics:
            titles[st["id"]] = st.get("title") or st["id"]
    return titles


def build_ks4():
    import generate_site_v5 as site
    import ks4_seed_sow as sow
    import ks4_data

    classify = ks4_data.classify()
    out = {}

    for subject in SUBJECTS:
        topic_titles = sow.topic_titles(subject)
        sub_titles = _ks4_subtopic_titles(subject)

        # Teaching order, from the ordering authority. Triple Higher is the
        # superset of topics as well as of subtopics.
        topic_ids = site.PATHWAY_TOPIC_MAP[("triple", "higher")][subject]

        # Subtopics grouped under their topic, in the order `subtopics_for`
        # returns them — the order the topic page itself renders.
        grouped = {}
        for topic_id, _title, slug in sow.subtopics_for("triple", "higher", subject):
            grouped.setdefault(topic_id, []).append(slug)

        topics = []
        for topic_id in topic_ids:
            paper = KS4_PAPER.get(subject, {}).get(topic_id)
            if paper is None:
                raise SystemExit(
                    "export_curriculum_tree: %s topic %r is not in KS4_PAPER. "
                    "Every KS4 topic sits on paper 1 or paper 2 and the sheet "
                    "renders a chip for it; add it to the map (RISKS C8) rather "
                    "than letting it export as null."
                    % (subject, topic_id))
            subtopics = []
            for slug in grouped.get(topic_id, []):
                c = classify.get(slug)
                if c is None:
                    raise SystemExit(
                        "export_curriculum_tree: subtopic %r is taught by "
                        "%s/%s but ks4_data.classify() does not know it. The "
                        "pool joins on this slug; exporting it unclassified "
                        "would offer a teacher a node with no audience."
                        % (slug, subject, topic_id))
                subtopics.append({
                    "slug": slug,
                    "name": sub_titles.get(slug, slug),
                    "tier": c["tier"],
                    "triple_only": bool(c["triple_only"]),
                })
            topics.append({
                "id": topic_id,
                "name": topic_titles.get(topic_id, topic_id),
                "paper": paper,
                "subtopics": subtopics,
            })
        out[subject] = topics

    return out


# ── KS3 ────────────────────────────────────────────────────────────────

def build_ks3():
    import ks3_data

    out = {s: [] for s in SUBJECTS}
    for unit in ks3_data.build_units():
        lessons = []
        for lesson in unit["lessons"]:
            # §4.6 single-source: a referenced slot is a cross-link to a lesson
            # owned by another unit, not a second copy of it. It has no rows in
            # `ks3_assignment_bank` — the bank keys on the OWNING unit's slug —
            # so offering it would be offering an empty node. (Measured today:
            # zero referenced slots exist, so this drops nothing. It is here
            # because the structure allows them and one would be silent.)
            if lesson.get("reference_to"):
                continue
            lessons.append({
                "slug": lesson["slug"],
                "name": lesson.get("title") or lesson["slug"],
            })
        out[unit["discipline"]].append({
            "code": unit["code"],
            "slug": unit["slug"],
            "name": unit["title"],
            "lessons": lessons,
        })
    return out


def build_tree():
    return {"ks4": build_ks4(), "ks3": build_ks3()}


def serialise(tree):
    """One canonical rendering, so `--check` compares content and not whitespace.

    `sort_keys` is deliberately NOT set: the LISTS carry teaching order and JSON
    objects here are small and fixed. `ensure_ascii=False` keeps AQA's own
    punctuation readable in the committed file.
    """
    return json.dumps(tree, indent=2, ensure_ascii=False) + "\n"


# ── where the backend lives ────────────────────────────────────────────

def default_out_dir():
    """The backend checkout beside this one, found rather than hardcoded.

    This script runs from a worktree during a build (`set-work-v2` beside
    `set-work-v2-backend`) and from the main checkout at merge
    (`mrbadmus-site` beside `mrbadmus---backend`). An absolute path would be
    right in exactly one of those. `MRB_BACKEND_DIR` overrides everything.
    """
    env = os.environ.get("MRB_BACKEND_DIR")
    if env:
        return env
    parent = os.path.dirname(REPO)
    here = os.path.basename(REPO)
    candidates = [
        os.path.join(parent, here + "-backend"),
        os.path.join(parent, "mrbadmus---backend"),
        os.path.expanduser("~/Documents/GitHub/mrbadmus---backend"),
    ]
    for c in candidates:
        if os.path.isfile(os.path.join(c, "server.js")):
            return c
    raise SystemExit(
        "export_curriculum_tree: could not find the backend checkout. Tried:\n"
        + "\n".join("  " + c for c in candidates)
        + "\nSet MRB_BACKEND_DIR, or pass --out.")


def counts(tree):
    ks4_t = sum(len(v) for v in tree["ks4"].values())
    ks4_s = sum(len(t["subtopics"]) for v in tree["ks4"].values() for t in v)
    ks3_u = sum(len(v) for v in tree["ks3"].values())
    ks3_l = sum(len(u["lessons"]) for v in tree["ks3"].values() for u in v)
    return ks4_t, ks4_s, ks3_u, ks3_l


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="compare the backend's file with a fresh build; "
                         "exit 1 on drift")
    ap.add_argument("--out", default=None,
                    help="directory to write %s into" % OUT_NAME)
    ap.add_argument("--stdout", action="store_true",
                    help="print the JSON and write nothing")
    args = ap.parse_args()

    tree = build_tree()
    text = serialise(tree)
    ks4_t, ks4_s, ks3_u, ks3_l = counts(tree)
    summary = ("KS4 %d topics / %d subtopics · KS3 %d units / %d lessons"
               % (ks4_t, ks4_s, ks3_u, ks3_l))

    if args.stdout:
        sys.stdout.write(text)
        return 0

    out_dir = args.out or default_out_dir()
    path = os.path.join(out_dir, OUT_NAME)

    if args.check:
        if not os.path.isfile(path):
            print("❌ %s does not exist — the backend has no curriculum "
                  "mirror at all." % path)
            return 1
        with open(path, "r", encoding="utf-8") as f:
            have = f.read()
        if have == text:
            print("✅ %s matches the Python — %s" % (path, summary))
            return 0
        # Say WHAT drifted, not merely that something did. A diff of a
        # 6,000-line JSON file is not an answer anybody can act on.
        try:
            old = json.loads(have)
        except ValueError:
            print("❌ %s is not valid JSON — rebuild it." % path)
            return 1
        old_c = counts(old)
        if old_c != (ks4_t, ks4_s, ks3_u, ks3_l):
            print("❌ %s has DRIFTED.\n   file:   KS4 %d/%d · KS3 %d/%d"
                  "\n   python: KS4 %d/%d · KS3 %d/%d"
                  % ((path,) + old_c + (ks4_t, ks4_s, ks3_u, ks3_l)))
        else:
            print("❌ %s has DRIFTED — the same counts, different content "
                  "(a renamed topic, a moved paper, a changed tier flag).\n"
                  "   %s" % (path, summary))
        print("   Rebuild: python3 tools/export_curriculum_tree.py")
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s — %s" % (path, summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
