#!/usr/bin/env python3
"""export_curriculum_tree.py — the curriculum, as a file the backend can read.

    python3 tools/export_curriculum_tree.py            # write curriculum-tree.json
    python3 tools/export_curriculum_tree.py --check    # exit 1 if it has drifted
    python3 tools/export_curriculum_tree.py --out DIR  # write it somewhere else
    python3 tools/export_curriculum_tree.py --stdout   # print it and write nothing

    Every run that writes also writes consumer/curriculum-index.json (the
    browser index below), and --check also checks it.

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


# ── the browser index (B2C onboarding repair, 3 Oct 2026) ──────────────
#
# The parent's topic picker (consumer/topic-picker.js) offers EVERY KS3 unit
# and lesson and EVERY GCSE topic and subtopic, and greys out the ones a child's
# year does not teach with "taught in Year N". N has to come from data, so the
# browser needs the curriculum AND the year each node is taught in — which is
# the same Python the backend tree above is built from, plus the year split
# `ks4_seed_sow.build_block()` makes for each (pathway, tier) block.
#
# It is a SEPARATE file from curriculum-tree.json on purpose: that file is the
# backend's and must stay byte-identical to what the backend already holds
# (`curriculum_tree_mirror`). This one lives in consumer/ — never shared/,
# which school pages load — and `--check` compares it with a fresh build, so
# it cannot drift either.
#
# Shape (compact; it is fetched by a phone):
#   { "v": 1,
#     "ks3": [ { "s": subject, "c": unit code, "n": title, "y": year,
#                "l": [ [lesson slug, lesson title], … ] }, … ],
#     "ks4": [ { "s": subject, "id": topic id, "n": title,
#                "l": [ [subtopic slug, title, { block: year, … }], … ] }, … ] }
# A KS4 block key is pathway initial + tier initial: cf, ch, tf, th. A
# subtopic a block does not teach has no key for it. KS3 lessons carry no
# year of their own: a lesson is taught when its unit is, and the scheme of
# work places units, not loose lessons.

INDEX_NAME = os.path.join("consumer", "curriculum-index.json")


def build_index(tree=None):
    import ks4_seed_sow as sow
    tree = tree or build_tree()

    # (subject, slug) -> {block: year}. Omitted rows (past a year's week
    # ceiling) are still TAUGHT in that year by the sequence — the database
    # simply cannot hold them — so they count.
    years = {}
    for pathway in ("combined", "triple"):
        for tier in ("foundation", "higher"):
            key = pathway[0] + tier[0]
            for subject in SUBJECTS:
                rows, omitted = sow.build_block(pathway, tier, subject)
                for r in rows + omitted:
                    years.setdefault((subject, r["subtopic"]), {})[key] = r["year_group"]

    import ks3_data
    unit_year = {u["code"]: u["typical_year"] for u in ks3_data.build_units()}

    ks3 = []
    for subject in SUBJECTS:
        for u in tree["ks3"][subject]:
            ks3.append({"s": subject, "c": u["code"], "n": u["name"],
                        "y": unit_year[u["code"]],
                        "l": [[l["slug"], l["name"]] for l in u["lessons"]]})
    ks4 = []
    for subject in SUBJECTS:
        for t in tree["ks4"][subject]:
            ks4.append({"s": subject, "id": t["id"], "n": t["name"],
                        "l": [[st["slug"], st["name"],
                               {k: v for k, v in sorted(years.get((subject, st["slug"]), {}).items())}]
                              for st in t["subtopics"]]})
    return {"v": 1, "ks3": ks3, "ks4": ks4}


def serialise_index(index):
    return json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n"


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
    ap.add_argument("--index-only", action="store_true",
                    help="write only %s (no backend checkout needed)" % INDEX_NAME)
    ap.add_argument("--stdout", action="store_true",
                    help="print the JSON and write nothing")
    args = ap.parse_args()

    tree = build_tree()
    text = serialise(tree)
    index_text = serialise_index(build_index(tree))
    index_path = os.path.join(REPO, INDEX_NAME)
    ks4_t, ks4_s, ks3_u, ks3_l = counts(tree)
    summary = ("KS4 %d topics / %d subtopics · KS3 %d units / %d lessons"
               % (ks4_t, ks4_s, ks3_u, ks3_l))

    if args.stdout:
        sys.stdout.write(text)
        return 0

    # The browser index is checked FIRST and independently of the backend
    # file: a drifted index is a picker labelling a topic with the wrong year,
    # and it must fail --check even when the backend mirror is fine.
    if args.check:
        have_index = None
        if os.path.isfile(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                have_index = f.read()
        if have_index != index_text:
            print("❌ %s is missing or has DRIFTED from the Python. "
                  "Rebuild: python3 tools/export_curriculum_tree.py" % INDEX_NAME)
            return 1
        print("✅ %s matches the Python (%d bytes)" % (INDEX_NAME, len(index_text.encode("utf-8"))))
    else:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_text)
        print("wrote %s — %d bytes" % (INDEX_NAME, len(index_text.encode("utf-8"))))
        if args.index_only:
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
