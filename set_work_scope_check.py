#!/usr/bin/env python3
"""set_work_scope_check.py — every node a teacher can pick can be filled.

    python3 set_work_scope_check.py            # measure the authored Python
    python3 set_work_scope_check.py --db       # measure what TEST actually holds
    python3 set_work_scope_check.py --quiet    # totals and failures only

── WHAT THIS PROVES, AND WHY IT IS A DIFFERENT QUESTION FROM ks4_pool_check ──

`ks4_pool_check.py` asks whether each ROW is flagged correctly — whether a
Foundation Combined child could be handed a Higher or a Triple-only question.
It is a statement about the pool.

This asks the question Set work v2 created, which the pool has never had to
answer before: **for every node the sheet will OFFER, and every tier it will
offer it at, is there anything there.** v1 offered scheme-of-work rows, so the
only nodes a teacher could reach were ones somebody had already written a row
for. v2 offers the whole curriculum — 264 KS4 subtopics and 185 KS3 lessons,
each at two or three tiers, filtered four ways by cohort — and a node with an
empty pool is a topic a teacher taps, waits for, and gets nothing from.

⚠️ AN EMPTY CELL IS INVISIBLE FROM EVERY OTHER GATE. The counts the sheet
renders come from the same read as the questions, so a zero renders as `0`,
disables the row, and looks exactly like a deliberate "not authored yet".
Nothing else in the estate walks the CROSS PRODUCT of (cohort × node × tier),
which is where the holes are: `energy-changes` has rows, and
`energy-changes × combined × foundation` may still have none.

The four cohorts, from PLAN §1:

    KS3                      easy / medium / hard   (band easier/standard/harder)
    KS4 combined             foundation / higher    (triple_only rows excluded)
    KS4 triple biology       foundation / higher    (that subject only)
    KS4 triple chemistry     "
    KS4 triple physics       "

── THE FOUR PROPERTIES ────────────────────────────────────────────────

  1. NON-EMPTY — every (cohort, node, tier) cell has at least one question,
     with ONE derived exception, which is a rule and not a list: a KS4 subtopic
     that `ks4_data.classify()` puts at `tier = 'higher'` holds no foundation
     rows at all, so its FOUNDATION cell is empty by construction. Measured:
     30 subtopics are classified higher and not one of them carries a
     foundation row, so the exception is exactly co-extensive with the
     classification rather than an allowance for missing content.

     ⚠️ THAT IS THE DESIGNED BEHAVIOUR, NOT A HOLE, and the reason is
     `treeForClass()`: the tree is filtered by pathway and subject and NEVER by
     tier, deliberately, because a tree that changed shape when the tier chip
     moved would be a different tree and the teacher would lose their place in
     it (RISKS C12). So a Foundation class DOES see `moles` in its list, with
     the count `0` beside it and the row disabled (RISKS A5). This gate counts
     those cells and asserts every one of them fills at HIGHER — a subtopic
     empty at BOTH tiers would be unreachable by anybody, which is a hole, and
     is the failure this exception must not be allowed to hide.
  2. MCQ-ONLY (RISKS C10) — every row in every cell has exactly four options
     and exactly one of them correct. Neither bank has a type column, so "is
     this a multiple-choice question" is answered by its SHAPE; a three-option
     row would render a fourth blank button in the sheet and a fourth blank
     button to the child.
  3. PATHWAY-PURE (RISKS C5/C6) — a combined cell contains no `triple_only`
     row, and a separate-sciences cell contains only that science's rows. This
     is asserted on the CELL, after the filter, which is the only place the
     mistake could show: the flags themselves are ks4_pool_check's business.
  4. NO DUPLICATE STEM WITHIN A CELL (RISKS A7) — two questions whose stems
     differ only in case, whitespace or trailing punctuation are one question
     to a child reading them one after the other. The backend's `pickRoundRobin`
     de-duplicates on exactly this normalisation, so a duplicate does not reach
     a set — it silently shrinks the pool instead, and a scope reporting 20
     available then hands back 19.

  5. THE FIFTY FLOOR, on the cells a teacher actually sets from. A teacher may
     ask for twenty questions on one node, and asking for twenty out of twenty
     hands the class the whole pool — so the same topic set twice running is
     the same paper twice running, and a swap has nothing to swap to. Fifty is
     the number the content lanes built to.

     ⚠️ IT IS FLOORED ON TOPICS AND UNITS, NOT ON SUBTOPICS AND LESSONS, and
     that distinction is the whole of it. A KS4 SUBTOPIC holds twelve to
     forty; a KS3 LESSON holds four to sixteen. Flooring those at fifty would
     demand four times the content that exists and would be a red on every
     run — and it would be demanding the wrong thing, because a teacher
     setting twenty on one subtopic is deliberately narrowing, and a narrow
     pool is what narrow means. The TOPIC is the unit of "set them something
     on Energy Changes", and it is the topic that has to be deep.

     Floored per AUDIENCE, not per topic: `(topic, combined-foundation)`,
     `(topic, combined-higher)`, `(topic, triple-foundation)`,
     `(topic, triple-higher)` are four different pools and a topic can be deep
     for one and thin for another. KS3 is floored per `(unit, tier)`.

Plus: the SMALLEST CELL per key stage, which is the number that says whether
the content lanes are finished. It is reported whether or not anything failed,
because "the smallest KS4 cell is 4" is the fact a reader wants.

── WHERE THE RULES COME FROM ──────────────────────────────────────────

The tree comes from `tools/export_curriculum_tree.build_tree()` — the same
function that writes the backend's mirror, so this gate and the sheet are
looking at the same curriculum by construction, and `--check` on that exporter
is what proves the backend's copy has not drifted.

⚠️ THE COHORT FILTER AND THE POOL SPEC ARE RE-DERIVED FROM PLAN §1, NOT READ
OUT OF THE BACKEND. That is deliberate and it is the same posture
`ks4_pool_check.py` takes: asserting that `set-work-scope.js` *contains* the
right `.eq()` calls is a spelling test that passes a filter which is correct in
shape and wrong in effect. So this states the rule independently and measures
the DATA against it. The JS's own copy is proved against the same rule by
`test_set_work_v2.js` (`poolRowMatches` against a synthetic bank), and the
serving path is proved end to end by `set_work_drive.py`. Three readings of one
rule, none of them reading each other.
"""

import argparse
import collections
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

SUBJECTS = ("biology", "chemistry", "physics")
KS4_TIERS = ("foundation", "higher")
KS3_TIERS = ("easy", "medium", "hard")
KS3_BAND_BY_TIER = {"easy": "easier", "medium": "standard", "hard": "harder"}

# PLAN §5's threshold: a teacher may draw twenty from one node, and twenty out
# of twenty is the whole pool.
POOL_FLOOR = 50

failures = []
notes = []


def fail(where, msg):
    failures.append((where, msg))


# ── the pool spec, PLAN §1 ─────────────────────────────────────────────
#
# KS4 Foundation — `tier='foundation'` rows, all three bands.
# KS4 Higher     — `tier='higher'` rows (all bands) ∪ `tier='foundation'` rows
#                  in `standard|harder`.
#
# ⚠️ THE SECOND HALF IS THE PART TO READ TWICE, and it is why a Higher cell is
# never simply "the higher rows". A Higher class is not a class that skips the
# foundation material; it is a class that meets it at the harder end. Only 30 of
# 264 subtopics are classified `higher`, so excluding foundation rows would
# leave Higher unable to set most of the specification — and including their
# `easier` band would hand a Higher group the four gentlest questions in the
# topic.
def ks4_row_in_tier(row, tier):
    if tier == "foundation":
        return row["tier"] == "foundation"
    if row["tier"] == "higher":
        return True
    return row["tier"] == "foundation" and row["band"] in ("standard", "harder")


# ⚠️ AN INCLUSION, NEVER AN EXCLUSION (RISKS C6). "not triple_only" would admit
# a third content flag silently, to every class in the school, on the day it was
# added.
def ks4_row_in_pathway(row, pathway):
    return row["triple_only"] in ((False, True) if pathway == "triple" else (False,))


def normalise_stem(s):
    return re.sub(r"[.?!\s]+$", "", re.sub(r"\s+", " ", str(s or "").lower())).strip()


# ── loading the two pools into ONE row shape ───────────────────────────
#
# The banks disagree about where the answer lives — KS4 stores `options: [str]`
# plus a `correct_index`, KS3 stores `[{text, correct, why}]` — exactly as they
# disagree for the backend, which normalises them in `swShapeKs4`/`swShapeKs3`.
# The conversion happens once, here, so every check below reads one shape.

def load_python():
    import ks4_data
    import ks3_data.question_bank as qb

    ks4 = []
    for r in ks4_data.load_pool():
        opts = list(r.get("options") or [])
        ks4.append({
            "id": r["id"], "slug": r["subtopic_slug"], "subject": r.get("subject"),
            "band": r["band"], "tier": r["tier"],
            "triple_only": bool(r.get("triple_only")),
            "text": r.get("text"), "n_options": len(opts),
            "n_correct": (1 if isinstance(r.get("correct_index"), int)
                          and 0 <= r["correct_index"] < len(opts) else 0),
        })

    ks3 = []
    for entry in qb.load_bank():
        for q in entry["questions"]:
            opts = list(q.get("options") or [])
            ks3.append({
                "id": q["id"], "slug": entry["lesson"], "unit": entry["unit"],
                "band": q["band"], "tier": None, "triple_only": False,
                "text": q.get("text"), "n_options": len(opts),
                "n_correct": sum(1 for o in opts if o and o.get("correct")),
            })
    return ks4, ks3, "the authored Python"


def load_db():
    """The same two pools as TEST actually holds them.

    ⚠️ SERVICE ROLE, AND ONLY BECAUSE THIS IS A CONTENT CHECK. Both banks are
    `authenticated`-SELECT, so an anon read returns nothing and would report
    every cell empty — a red that says nothing about the content. Nothing here
    is a claim about what a USER can reach; that is `set_work_drive.py`'s job,
    and it carries no service key at all.
    """
    env_path = os.environ.get(
        "MRB_BACKEND_ENV",
        "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env")
    conf = {}
    for line in open(env_path, encoding="utf-8"):
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            conf[k.strip()] = v.strip()
    url, key = conf["SUPABASE_URL"], conf["SUPABASE_SERVICE_ROLE_KEY"]
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

    def page(table, cols):
        out, frm = [], 0
        while True:
            req = urllib.request.Request(
                "%s/rest/v1/%s?select=%s&order=id" % (url, table, cols),
                headers={"apikey": key, "Authorization": "Bearer " + key,
                         "Range": "%d-%d" % (frm, frm + 999)})
            with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
                rows = json.loads(r.read().decode())
            out.extend(rows)
            if len(rows) < 1000:
                return out
            frm += 1000

    ks4 = []
    for r in page("ks4_assignment_bank",
                  "id,subtopic_slug,subject,band,tier,triple_only,text,options,correct_index"):
        opts = list(r.get("options") or [])
        ks4.append({
            "id": r["id"], "slug": r["subtopic_slug"], "subject": r.get("subject"),
            "band": r["band"], "tier": r["tier"],
            "triple_only": bool(r.get("triple_only")),
            "text": r.get("text"), "n_options": len(opts),
            "n_correct": (1 if isinstance(r.get("correct_index"), int)
                          and 0 <= r["correct_index"] < len(opts) else 0),
        })
    ks3 = []
    for r in page("ks3_assignment_bank", "id,lesson_slug,unit_code,band,text,options"):
        opts = list(r.get("options") or [])
        ks3.append({
            "id": r["id"], "slug": r["lesson_slug"], "unit": r.get("unit_code"),
            "band": r["band"], "tier": None, "triple_only": False,
            "text": r.get("text"), "n_options": len(opts),
            "n_correct": sum(1 for o in opts if isinstance(o, dict) and o.get("correct")),
        })
    # ⊕ MRB-338, 9 Sep 2026. This said "the TEST database" unconditionally,
    # and `--db` honours $MRB_BACKEND_ENV — so pointing it at production
    # printed a production measurement under the word TEST. A gate that
    # misnames which database it read is a gate whose green means nothing, and
    # on 9 Sep the two projects held identical row counts, so the label was the
    # only thing distinguishing them on screen. Name the project from the URL
    # actually used.
    import re as _re
    _m = _re.search(r"https://([a-z0-9]+)\.supabase\.co", url)
    _ref = _m.group(1) if _m else "?"
    _name = {"urklkrwevjtlfbwnipjn": "the PRODUCTION database",
             "qeppkiswvclkkwbxmlok": "the TEST database"}.get(
                 _ref, "the database at %s" % _ref)
    return ks4, ks3, _name


# ── the cohorts, and the nodes each of them can reach ──────────────────
#
# A cohort is (key_stage, pathway, subject) — PLAN §1 — and it is the ONLY
# thing that decides which nodes exist for a class. Tier is chosen per set and
# never changes the shape of the tree, only the counts on it (RISKS C12).

def ks4_nodes(tree, pathway, subject):
    """(kind, ref, label, [slugs], all_higher) for every node this cohort sees.

    RISKS C7 lives in the `if not slugs: continue` — a topic all of whose
    subtopics are triple-only is not an empty topic on a combined tree, it is a
    topic that is not on it. Today that is exactly `space`.
    """
    out = []
    subjects = [subject] if subject else list(SUBJECTS)
    for subj in subjects:
        for topic in tree["ks4"][subj]:
            slugs = [st["slug"] for st in topic["subtopics"]
                     if pathway == "triple" or not st["triple_only"]]
            if not slugs:
                continue
            kept = [st for st in topic["subtopics"] if st["slug"] in slugs]
            out.append(("topic", topic["id"], "%s/%s" % (subj, topic["id"]), slugs,
                        all(st["tier"] == "higher" for st in kept)))
            for st in kept:
                out.append(("subtopic", st["slug"],
                            "%s/%s/%s" % (subj, topic["id"], st["slug"]),
                            [st["slug"]], st["tier"] == "higher"))
    return out


# ── ⊕ MRB-336, 8 Sep 2026 — THE PAPER CHIP IS A FILTER, AND A FILTER CAN
#    BE A DEAD END ──────────────────────────────────────────────────────
#
# ⛔ THERE WAS NO PAPER DIMENSION IN THIS GATE AT ALL BEFORE TODAY, and until
# today that was defensible: `papersFor` returned `[1, 2]` for combined and
# `null` for triple, so on the only cohort that had chips the paper split was
# a re-partition of a tree this gate already walked node by node, and the
# exporter refuses a topic with no paper (`export_curriculum_tree.py:146`) so
# the map cannot be incomplete.
#
# MRB-336 gave every KS4 cohort the chips, and that adds a question none of
# the four properties above asks: **is anything left after the chip.** The
# cells this gate measures are (cohort, node, tier); a paper chip is a fifth
# axis over the COHORT, and a cohort × paper with no topics in it is a chip a
# teacher taps and gets an empty list from — the same failure as an empty
# cell, one level up, and invisible from every other angle. `space` is the
# case that makes it real rather than theoretical: it is physics paper 2 and
# triple-only, so it exists under one cohort's paper 2 chip and under no
# other's, and it is the topic most likely to be dropped by a future filter
# written for combined.
#
# ⚠️ IT IS A REACHABILITY CHECK, NOT A SECOND FLOOR. The fifty floor already
# applies per topic, and a paper is not a thing a teacher sets work ON — they
# tap it to narrow the list and then pick a topic inside it. So what is
# asserted is that the narrowing leaves something, at every tier, on every
# cohort; the depth of what it leaves is the topic floor's business.
def ks4_paper_cells(tree, pathway, subject):
    """{paper: [(topic_id, [slugs], all_higher)]} for one cohort."""
    cells = {1: [], 2: []}
    subjects = [subject] if subject else list(SUBJECTS)
    for subj in subjects:
        for topic in tree["ks4"][subj]:
            paper = topic.get("paper")
            slugs = [st["slug"] for st in topic["subtopics"]
                     if pathway == "triple" or not st["triple_only"]]
            if not slugs:
                continue
            if paper not in cells:
                fail("papers", "%s/%s carries paper %r, which is neither 1 "
                               "nor 2 — the chip rail cannot partition a tree "
                               "with a topic outside it" % (subj, topic["id"],
                                                            paper))
                continue
            kept = [st for st in topic["subtopics"] if st["slug"] in slugs]
            cells[paper].append((topic["id"], slugs,
                                 all(st["tier"] == "higher" for st in kept)))
    return cells


def report_papers(label, tree, pathway, subject, index, keep):
    """Every (cohort, paper, tier) leaves a teacher something to pick."""
    cells = ks4_paper_cells(tree, pathway, subject)
    smallest = None
    for paper in (1, 2):
        topics = cells[paper]
        if not topics:
            fail(label, "paper %d offers NO topic at all — the chip is a dead "
                        "end on this cohort" % paper)
            continue
        for tier in KS4_TIERS:
            # The derived exception from property 1 applies unchanged: a topic
            # every subtopic of which is classified `higher` holds no
            # foundation row by construction, so it is not counted against the
            # foundation cell. The PAPER cell only fails if EVERY topic under
            # it is empty at that tier, which is a chip with nothing behind it.
            total = 0
            for _tid, slugs, all_higher in topics:
                if tier == "foundation" and all_higher:
                    continue
                for slug in slugs:
                    total += sum(1 for r in index.get(slug, []) if keep(r, tier))
            if not total:
                fail(label, "paper %d at %s has NO question behind any of its "
                            "%d topic(s) — tapping the chip and then the tier "
                            "leaves the teacher nothing"
                     % (paper, tier, len(topics)))
            elif smallest is None or total < smallest[0]:
                smallest = (total, "%s paper %d %s" % (label, paper, tier))
    if smallest:
        notes.append("%s: thinnest paper cell %d questions (%s)"
                     % (label, smallest[0], smallest[1]))
    return smallest


def ks3_nodes(tree):
    out = []
    for subj in SUBJECTS:
        for unit in tree["ks3"][subj]:
            slugs = [l["slug"] for l in unit["lessons"]]
            if not slugs:
                continue
            out.append(("unit", unit["code"], "%s/%s" % (subj, unit["code"]),
                        slugs, False))
            for slug in slugs:
                out.append(("lesson", slug, "%s/%s/%s" % (subj, unit["code"], slug),
                            [slug], False))
    return out


def by_slug(rows):
    m = collections.defaultdict(list)
    for r in rows:
        m[r["slug"]].append(r)
    return m


# ── one cohort, measured ───────────────────────────────────────────────

def measure(label, nodes, index, tiers, keep, want_subject=None):
    """`keep(row, tier)` is the pool spec for this cohort. Returns
    (smallest, empties, shape_bad, purity_bad, dup_bad, cells, higher_only)."""
    smallest = None
    empties, shape_bad, purity_bad, dup_bad, thin = [], [], [], [], []
    cells = 0
    higher_only = 0
    floored = 0
    for kind, ref, where, slugs, all_higher in nodes:
        for tier in tiers:
            cells += 1
            pool = [r for slug in slugs for r in index.get(slug, []) if keep(r, tier)]
            n = len(pool)
            if n == 0:
                # The one derived exception, and the assertion that keeps it
                # honest is three lines below: a node empty at foundation
                # BECAUSE it is classified higher must fill at higher, or it is
                # reachable by nobody and the exception has hidden a hole.
                if all_higher and tier == "foundation":
                    higher_only += 1
                    other = [r for slug in slugs for r in index.get(slug, [])
                             if keep(r, "higher")]
                    if not other:
                        empties.append("%s %s is empty at BOTH tiers — nobody "
                                       "can reach it" % (kind, where))
                    continue
                empties.append("%s %s @ %s" % (kind, where, tier))
                continue
            if smallest is None or n < smallest[0]:
                smallest = (n, "%s %s @ %s" % (kind, where, tier))

            # ── 5 · the fifty floor, on TOPICS and UNITS only ─────────
            if kind in ("topic", "unit"):
                floored += 1
                if n < POOL_FLOOR:
                    thin.append("%s @ %s holds %d" % (where, tier, n))

            # 2 · MCQ shape
            for r in pool:
                if r["n_options"] != 4 or r["n_correct"] != 1:
                    shape_bad.append("%s (%s): %d option(s), %d correct"
                                     % (r["id"], where, r["n_options"], r["n_correct"]))
            # 3 · purity
            for r in pool:
                if want_subject is None and r.get("triple_only"):
                    purity_bad.append("%s is triple_only and reached %s"
                                      % (r["id"], where))
                if want_subject and r.get("subject") and r["subject"] != want_subject:
                    purity_bad.append("%s is %s and reached the %s tree"
                                      % (r["id"], r["subject"], want_subject))
            # 4 · duplicate stems
            seen = {}
            for r in pool:
                k = normalise_stem(r["text"])
                if k in seen:
                    dup_bad.append("%s == %s (%s @ %s)"
                                   % (r["id"], seen[k], where, tier))
                else:
                    seen[k] = r["id"]
    return (smallest, empties, shape_bad, purity_bad, dup_bad, cells,
            higher_only, thin, floored)


def report(cohort, res, quiet):
    (smallest, empties, shape_bad, purity_bad, dup_bad, cells, higher_only,
     thin, floored) = res
    ok = not (empties or shape_bad or purity_bad or dup_bad or thin)
    print("   %s %-26s %5d cells   smallest %s"
          % ("✅" if ok else "❌", cohort, cells,
             ("%d  (%s)" % smallest) if smallest else "— nothing at all"))
    if higher_only:
        print("        %d Higher-only node(s) render 0 at Foundation and fill "
              "at Higher — RISKS A5" % higher_only)
    if floored:
        print("        %d topic/unit pool(s) floored at %d — %s"
              % (floored, POOL_FLOOR,
                 "all clear" if not thin else "%d BELOW IT" % len(thin)))
    for name, bad in (("EMPTY", empties), ("not a four-option MCQ", shape_bad),
                      ("out of pathway", purity_bad), ("duplicate stem", dup_bad),
                      ("below the %d floor" % POOL_FLOOR, thin)):
        if not bad:
            continue
        fail(cohort, "%d %s" % (len(bad), name))
        head = bad if quiet else bad[:12]
        for b in head:
            print("        · %s" % b)
        if len(bad) > len(head):
            print("        · … and %d more" % (len(bad) - len(head)))
    return smallest


# ── ⊕ MRB-338, 9 Sep 2026 — THE LEAF TABLE ─────────────────────────────
#
# The floor above is on TOPICS and UNITS, and the long comment at property 5
# says why: a KS4 subtopic held twelve to forty and a KS3 lesson four to
# sixteen, so flooring the leaves would have been a red on every run.
#
# ⚠️ THAT WAS A STATEMENT ABOUT THE CONTENT, NOT ABOUT THE PRODUCT. Mide's
# ruling of 8 Sep is that the leaf is what a teacher actually taps — "teachers
# will most likely set assignment on each topic, but these topics don't have
# enough questions" — so the leaf has to be deep too, and MRB-338 is the
# programme that makes it so. Until that programme finishes, this REPORTS and
# does not gate: `--leaf` prints the per-leaf gap, `--leaf --strict` turns the
# gap red, and only the finishing night runs it strict.
#
# The KS4 leaf floor is stated per (subtopic, tier) under the MRB-335 pool
# spec, re-using `ks4_row_in_tier` rather than restating it — a leaf table
# that measured the pool differently from the cell table would be measuring a
# pool the sheet never serves. Pathway is not an axis here on purpose: a
# subtopic's rows carry ONE triple_only flag, so `triple_only` decides whether
# a cohort sees the leaf at all and never how many rows it sees.
KS4_LEAF_FLOOR = 50

# ⚠️ ONE CONSTANT, deliberately — Mide may raise 30 to 50, and when he does it
# is this line that moves and nothing else.
KS3_LEAF_FLOOR = 30


def leaf_cells(tree, ks4_index, ks3_index):
    """(stage, subject, where, tier, have, floor) for every leaf a teacher taps."""
    out = []
    for subj in SUBJECTS:
        for topic in tree["ks4"][subj]:
            for st in topic["subtopics"]:
                rows = ks4_index.get(st["slug"], [])
                where = "%s/%s" % (topic["id"], st["slug"])
                for tier in KS4_TIERS:
                    # Property 1's derived exception, unchanged: a subtopic
                    # `classify()` puts at `higher` holds no foundation row by
                    # construction, so its foundation cell is not a gap.
                    if tier == "foundation" and st["tier"] == "higher":
                        continue
                    have = sum(1 for r in rows if ks4_row_in_tier(r, tier))
                    out.append(("ks4", subj, where, tier, have, KS4_LEAF_FLOOR))
    for subj in SUBJECTS:
        for unit in tree["ks3"][subj]:
            for lesson in unit["lessons"]:
                rows = ks3_index.get(lesson["slug"], [])
                where = "%s/%s" % (unit["code"], lesson["slug"])
                for tier in KS3_TIERS:
                    have = sum(1 for r in rows
                               if r["band"] == KS3_BAND_BY_TIER[tier])
                    out.append(("ks3", subj, where, tier, have, KS3_LEAF_FLOOR))
    return out


def report_leaves(cells, strict, quiet, only=None):
    """The per-leaf gap table. Reports; fails only under --strict."""
    print("\n📏  leaf floors — KS4 subtopic %d per tier, KS3 lesson %d per band%s"
          % (KS4_LEAF_FLOOR, KS3_LEAF_FLOOR,
             "   [STRICT: gaps are failures]" if strict else "   [reporting only]"))
    if only:
        cells = [c for c in cells if c[2] in only or c[2].split("/")[-1] in only]
        print("    filtered to %d cell(s) by --leaf-only" % len(cells))
    for stage in ("ks4", "ks3"):
        mine = [c for c in cells if c[0] == stage]
        if not mine:
            continue
        short = [c for c in mine if c[4] < c[5]]
        gap = sum(c[5] - c[4] for c in short)
        leaves = len({c[2] for c in mine})
        print("\n   %s — %d leaves, %d cells, %d short, %d row(s) to author"
              % (stage.upper(), leaves, len(mine), len(short), gap))
        if short:
            worst = sorted(short, key=lambda c: (c[5] - c[4]), reverse=True)
            head = worst if quiet or len(worst) <= 40 else worst[:40]
            for _st, subj, where, tier, have, floor in head:
                print("        · %-9s %-46s %-10s %3d/%-3d  +%d"
                      % (subj, where, tier, have, floor, floor - have))
            if len(worst) > len(head):
                print("        · … and %d more" % (len(worst) - len(head)))
            if strict:
                fail("%s leaves" % stage.upper(),
                     "%d leaf cell(s) below the floor, %d rows short"
                     % (len(short), gap))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", action="store_true",
                    help="measure the TEST database instead of the Python source")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--leaf", action="store_true",
                    help="also report the per-leaf gap (MRB-338)")
    ap.add_argument("--strict", action="store_true",
                    help="with --leaf, a leaf below its floor is a FAILURE")
    ap.add_argument("--leaf-only", default=None,
                    help="comma-separated leaf slugs to restrict --leaf to")
    args = ap.parse_args()

    sys.path.insert(0, os.path.join(REPO, "tools"))
    import export_curriculum_tree as ex
    tree = ex.build_tree()

    ks4_rows, ks3_rows, source = load_db() if args.db else load_python()
    ks4_index, ks3_index = by_slug(ks4_rows), by_slug(ks3_rows)

    print("\n🧭  set_work_scope_check — every node a teacher can pick, at every "
          "tier\n    measuring %s: %d KS4 rows, %d KS3 rows\n"
          % (source, len(ks4_rows), len(ks3_rows)))

    ks4_small, ks3_small = [], []

    s = report("KS3 (all three sciences)",
               measure("KS3", ks3_nodes(tree), ks3_index, KS3_TIERS,
                       lambda r, t: r["band"] == KS3_BAND_BY_TIER[t]),
               args.quiet)
    if s:
        ks3_small.append(s)

    s = report("KS4 combined",
               measure("combined", ks4_nodes(tree, "combined", None), ks4_index,
                       KS4_TIERS,
                       lambda r, t: ks4_row_in_tier(r, t)
                       and ks4_row_in_pathway(r, "combined")),
               args.quiet)
    if s:
        ks4_small.append(s)

    # ⊕ MRB-336 — the paper chips, on the cohort that has had them all along
    # and on the three that got them today.
    report_papers("KS4 combined", tree, "combined", None, ks4_index,
                  lambda r, t: ks4_row_in_tier(r, t)
                  and ks4_row_in_pathway(r, "combined"))

    for subject in SUBJECTS:
        report_papers("KS4 triple %s" % subject, tree, "triple", subject,
                      ks4_index,
                      lambda r, t: ks4_row_in_tier(r, t)
                      and ks4_row_in_pathway(r, "triple"))

    for subject in SUBJECTS:
        s = report("KS4 triple %s" % subject,
                   measure("triple %s" % subject,
                           ks4_nodes(tree, "triple", subject), ks4_index,
                           KS4_TIERS,
                           lambda r, t: ks4_row_in_tier(r, t)
                           and ks4_row_in_pathway(r, "triple"),
                           want_subject=subject),
                   args.quiet)
        if s:
            ks4_small.append(s)

    # ⚠️ THE SMALLEST CELL IS PRINTED WHETHER OR NOT ANYTHING FAILED. "Nothing
    # is empty" and "the thinnest node holds four questions" are different
    # facts, and only the second one says whether a teacher can ask for ten.
    print("\n   smallest cell, KS4: %s" % (("%d — %s" % min(ks4_small))
                                           if ks4_small else "—"))
    print("   smallest cell, KS3: %s" % (("%d — %s" % min(ks3_small))
                                         if ks3_small else "—"))

    if args.leaf:
        report_leaves(leaf_cells(tree, ks4_index, ks3_index),
                      args.strict, args.quiet,
                      only=set(filter(None, (args.leaf_only or "").split(","))) or None)

    for n in notes:
        print("   ℹ️  %s" % n)

    if failures:
        print("\n❌ set_work_scope_check: %d cohort(s) with findings" % len(failures))
        for where, msg in failures:
            print("   · %-24s %s" % (where, msg))
        return 1
    print("\n✅ set_work_scope_check: every offered node fills at every tier, "
          "four options and one answer, in pathway, no repeated stem,\n"
          "   and every topic/unit pool is at or above the %d floor"
          % POOL_FLOOR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
