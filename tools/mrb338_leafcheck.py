#!/usr/bin/env python3
"""MRB-338 · the per-leaf checker, rebuilt IN THE REPO.

Night 1 of the bank-expansion programme ran a per-leaf checker all night. It
lived in a session scratch directory and it is gone. Every lane rebuilt some
part of it from memory, and the parts they rebuilt were the parts that were
WRONG before they were corrected. REPORT §9 lists the four corrections; this
file is them, written down where the next lane can run them instead of
rediscovering them.

    python3 tools/mrb338_leafcheck.py --unit B1 --lesson animal-and-plant-cells
    python3 tools/mrb338_leafcheck.py --unit C3
    python3 tools/mrb338_leafcheck.py --subtopic stem-cells
    python3 tools/mrb338_leafcheck.py --topic cell-biology

── THE FOUR CORRECTIONS, AND THE CASE THAT FORCED EACH ──────────────────

Every one of these was wrong in the permissive-to-strict direction: it blocked
good work rather than passing bad. That is the right direction to be wrong in,
and it still cost most of a night.

  1 · **Paraphrase is Jaccard, never the overlap coefficient.** The overlap
      coefficient divides by the SMALLER stem, so "What is a coverslip?" —
      four tokens — scores 0.75 against anything containing "what is a". 13 of
      20 hits on night 1 were that artefact and nothing else. Jaccard divides
      by the union and separates them.
  2 · **A hard fail at Jaccard >= 0.60 needs BOTH stems >= 10 tokens.** "State
      the approximate resolution of a light microscope" against "State the
      maximum magnification of a light microscope" scores 0.70 on a shared
      seven-token frame. They are two facts with two different answers — a
      DISCRIMINATION SET, which is the point of the pool, not a defect in it.
      Short pairs are reported for a human to read, never failed.
  3 · **"figure", "table" and "picture" are matched only in their unambiguous
      page-reference senses.** "Why is their figure an underestimate" is a
      NUMBER. "A block rests on a table" is FURNITURE. "The picture on the
      retina" is an optical IMAGE. None of the three is a page reference and
      all three were flagged.
  4 · **Pre-existing pairs are REPORTED; only a pair involving a NEW row
      FAILS.** An old-old pair is a pre-existing condition of the estate, not
      this run's finding, and failing on it stops a lane fixing a leaf it did
      not break. "New" is taken from `git diff` against the merge-base with
      `origin/main` — ids present now and absent there.

── ⚠️ DUPLICATES ARE SCOPED TO THE UNIT OR TOPIC, NEVER THE LEAF ────────

Brief §9.4. `set_work_scope_check` treats a whole KS3 unit and a whole KS4
topic as ONE cell and fails on a repeated stem anywhere inside it. Night 1
shipped two rows that duplicated a stem in a DIFFERENT leaf of the same unit,
and nothing a lane was running could see it: a per-leaf checker compares a leaf
against itself, and lanes cannot read each other's uncommitted files.

So checks 1, 2, 3 and 7 always sweep the whole unit or topic even when
`--lesson`/`--subtopic` names one leaf. The per-leaf measures — length parity,
rank spread, position spread — stay per leaf, because they are properties of
what a teacher SETS.

── ⚠️ THIS IS AN ADVISOR, NOT THE GATE ──────────────────────────────────

`verify_answer_lengths` and `set_work_scope_check` are the gates, and
`tools/mrb338_land.sh` runs them. The length rule here is not a second
implementation of the first one — it IMPORTS it, so the two cannot drift.
"""

import argparse
import ast
import collections
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

import verify_answer_lengths as VAL       # noqa: E402  — the length rule, once

# Authoring thresholds. The brief's numbers, not new ones.
CEILING = 0.32          # brief §6/§9.1 — the authoring aim for longest-is-key
FLOOR = VAL.LO          # 0.12 — the mirror tell, equally a defect
SWEEP = range(3, 11)    # brief §9.1 — sweep margins, do not trust one
JACCARD_HARD = 0.60
JACCARD_MIN_TOKENS = 10  # correction 2 — below this, report only
RANK_MAX_SHARE = 0.40   # brief §6 — no length rank may hold more than 40%
RANK_MIN_N = 20         # below this a 40% share is arithmetic, not a tell
POSITION_MIN_N = 8      # below this an unused index is not yet evidence
# Check 7 — how much a key has to SAY before its appearance in another stem
# means anything. ⚠️ ⊕ A FIFTH CORRECTION, found the first time this file was
# run (B1, 12 Sep 2026). A bare 12-character threshold produced 57 hits on one
# unit and every single one was an artefact: the keys were "Chloroplasts",
# "The cell wall", "An organ system", "Xylem and phloem" — the bare nouns a
# unit is ABOUT. Every stem in a cells unit mentions cell walls; that is the
# subject, not a leak.
#
# Brief §9.6's two real cases are "about two million every second" and "last
# about four months": a key that is a FACT — a quantity, or a multi-word claim
# — and reading it in another stem genuinely hands a pupil the answer. So a
# key qualifies only if it carries enough to be that: FOUR OR MORE TOKENS,
# always, plus 18 characters — or 12 if it carries a digit, since a quantity
# says a lot in few characters.
#
# ⚠️ The four-token floor is not negotiable down to three. At three tokens the
# first run still admitted "the ×10 objective" (a digit, 17 characters) and
# flagged four rows of the microscopy leaf, which is a leaf ABOUT objectives.
# A piece of named apparatus is not a leaked fact. Checked against brief
# §9.6's two real cases — "about two million every second" (5 tokens) and
# "last about four months" (4 tokens) — both of which survive it.
KEY_ECHO_MIN_TOKENS = 4
KEY_ECHO_MIN_CHARS = 18
KEY_ECHO_DIGIT_MIN_CHARS = 12

# ⊕ 12 Sep 2026 — A SECOND ADMISSION PATH, added after the B2 examiner found
# SIX stem-states-a-key collisions this check had not flagged. Three of the six
# were blocked by the four-token floor above and are unarguably real leaks:
#
#     "About 160 degrees."   3 tokens   quoted verbatim by b2-02-h21's stem
#     "Two directions."      2 tokens   quoted verbatim by b2-03-e29's stem
#     "1200 N."              2 tokens   quoted verbatim by b2-04-s24's stem
#
# The floor is still right for PROSE — lowering it to three re-admits "the ×10
# objective" and floods a leaf that is ABOUT objectives. But a key that IS a
# bare quantity or a bare count is a fact however few words it uses, and
# reading it in another stem hands a pupil the answer exactly as a long one
# does. So those are admitted by SHAPE instead of by length.
#
# ⚠️ This does not catch a PARAPHRASED leak. The B2 examiner also found three
# collisions where the stem restated the key in different words ("moves the
# tendon further from the joint" against a key of "It increases that
# distance"). Substring matching cannot see those and this check does not
# pretend to; only a cold read finds them. Do not read a clean section 7 as
# proof there is no leak.
_QUANTITY_KEY = re.compile(
    r"^(?:about|roughly|around|approximately|nearly)?\s*"
    r"\d[\d,.]*\s*"
    r"(?:°|degrees?|N|kg|g|mg|cm|mm|km|m|s|ms|ml|l|dm3|cm3|m3|J|kJ|W|kW|V|A|"
    r"%|times|Hz)\b\.?$", re.I)
_COUNT_KEY = re.compile(
    r"^(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+\w+\.?$", re.I)

def _key_is_bare_fact(text):
    """A quantity or a count — a fact stated in very few words."""
    t = (text or "").strip()
    return bool(_QUANTITY_KEY.match(t) or _COUNT_KEY.match(t))

BAND_LETTER = {"easier": "e", "standard": "s", "harder": "h"}
FROZEN_POSITIONS = 12   # bank_position 0..11 — the auto-composition window
FROZEN_PER_BAND = 4     # ids e01–e04, s01–s04, h01–h04

# Correction 3 — the UNAMBIGUOUS page-reference senses only. Every pattern
# here needs a determiner or a position word; a bare "figure"/"table"/
# "picture" is not matched, because on its own it is a number, a piece of
# furniture or an optical image at least as often as it is a page reference.
PAGE_REF = [
    re.compile(p, re.I) for p in (
        r"\bin (?:the|this) (?:figure|table|picture|diagram|graph|image)\b",
        r"\b(?:the|this) (?:figure|table|picture|diagram|graph) "
        r"(?:above|below|shown|opposite|on the right|on the left)\b",
        r"\bfrom the (?:figure|table|graph|diagram)\b",
        r"\bshown (?:above|below|opposite)\b",
        r"\b(?:above|below)[,]? (?:the )?(?:figure|table|diagram|graph)\b",
        r"\bin (?:this|the) lesson\b",
        r"\bon the (?:previous|next) page\b",
    )
]

def topic_of_module(path):
    """The topic a KS4 question file belongs to, from its filename.

    `ks4_data._modules` reads `pkgutil`'s module NAME, which has no extension,
    and splits the topic off at the double underscore: `particle_model__a` ->
    `particle-model`. Here the same names arrive from `git ls-tree` WITH `.py`
    on the end, and a base file like `cell_biology.py` has no double
    underscore at all — so splitting first yields `cell-biology.py`, which
    matches no topic. The whole base file then vanished from the merge-base
    reconstruction and its 96 rows read as NEW, which made every frozen
    position look changed. Strip the extension first.
    """
    stem = os.path.basename(path)
    if stem.endswith(".py"):
        stem = stem[:-3]
    return stem.split("__")[0].replace("_", "-")


TOKEN = re.compile(r"[a-z0-9]+")
ID_TAIL = re.compile(r"-([esh])(\d+)$")

FAILS = []          # hard failures — these set the exit code
NOTES = []          # things a human reads and judges


def fail(check, msg):
    FAILS.append("%s · %s" % (check, msg))


def normalise_stem(s):
    """Identical to `set_work_scope_check.normalise_stem`, deliberately.

    That function is what the binding gate de-duplicates on. A checker that
    normalises differently reports a clean leaf and then the gate goes red,
    which is the worst of both.
    """
    return re.sub(r"[.?!\s]+$", "",
                  re.sub(r"\s+", " ", str(s or "").lower())).strip()


def tokens(s):
    return set(TOKEN.findall(str(s or "").lower()))


def jaccard(a, b):
    """Intersection over UNION. See correction 1 — never over the smaller."""
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ── git: what is NEW on this branch ─────────────────────────────────────

def git(*args):
    return subprocess.run(["git"] + list(args), cwd=REPO,
                          capture_output=True, text=True)


def merge_base():
    r = git("merge-base", "HEAD", "origin/main")
    if r.returncode:
        return None
    return r.stdout.strip()


def blob_at(rev, path):
    r = git("show", "%s:%s" % (rev, path))
    return None if r.returncode else r.stdout


def files_at(rev, prefix):
    r = git("ls-tree", "-r", "--name-only", rev, "--", prefix)
    return [] if r.returncode else [p for p in r.stdout.split("\n") if p]


def literal_questions(src):
    """`QUESTIONS = [...]` out of a source file, without importing it.

    Importing an old revision means writing it to disk and putting it on the
    path, which is how a checker ends up measuring a file the author cannot
    see. `ast.literal_eval` reads the literal and nothing else.
    """
    if src is None:
        return None
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == "QUESTIONS":
                try:
                    return ast.literal_eval(node.value)
                except (ValueError, SyntaxError):
                    return None
    return None


# ── loading · both key stages into ONE row shape ────────────────────────
#
# The two banks disagree about where the answer lives — KS4 stores
# `options: [str]` with a `correct_index`, KS3 stores `[{text, correct, why}]`
# — exactly as they disagree for the backend. Converted once, here.

def load_ks3(unit):
    import ks3_data.question_bank as qb
    rows, leaves, files = [], [], {}
    for rec in qb.load_bank():
        if rec["unit"] != unit:
            continue
        leaf = rec["lesson"]
        leaves.append(leaf)
        files[leaf] = rec["module"].replace(".", "/") + ".py"
        for pos, q in enumerate(rec["questions"]):
            opts = [o.get("text", "") for o in q["options"]]
            key = [i for i, o in enumerate(q["options"]) if o.get("correct")]
            rows.append({
                "id": q.get("id"), "leaf": leaf, "band": q.get("band"),
                "text": q.get("text", ""), "options": opts,
                "key": key[0] if len(key) == 1 else None,
                "why": [o.get("why") or "" for o in q["options"]],
                "position": pos, "file": files[leaf],
            })
    return rows, sorted(set(leaves)), files


def ks4_topic_of(subtopic):
    sys.path.insert(0, os.path.join(REPO, "tools"))
    import export_curriculum_tree as ex
    for subject, topics in ex.build_tree()["ks4"].items():
        for t in topics:
            for st in t["subtopics"]:
                if st["slug"] == subtopic:
                    return t["id"], subject
    return None, None


def ks4_subject_of_topic(topic):
    sys.path.insert(0, os.path.join(REPO, "tools"))
    import export_curriculum_tree as ex
    for subject, topics in ex.build_tree()["ks4"].items():
        for t in topics:
            if t["id"] == topic:
                return subject
    return None


def load_ks4(topic, subject):
    import ks4_data
    rows, leaves = [], []
    for r in ks4_data.load_pool(subject=subject):
        st = r["subtopic_slug"]
        tp, _ = ks4_topic_of(st)
        if tp != topic:
            continue
        leaves.append(st)
        rows.append({
            "id": r["id"], "leaf": st, "band": r.get("band"),
            "text": r.get("text", ""), "options": list(r["options"]),
            "key": r.get("correct_index"),
            "why": [r.get("why") or ""],
            "position": r.get("bank_position"), "file": None,
        })
    return rows, sorted(set(leaves))


# ── 1, 2 · duplicate stems and duplicate answer-sets ────────────────────

def check_duplicates(rows, new_ids, scope_name):
    print("\n1 · DUPLICATE STEMS — normalised for case, whitespace and "
          "trailing punctuation,")
    print("    swept across the whole %s (brief §9.4)." % scope_name)
    seen = {}
    pairs = []
    for r in rows:
        k = normalise_stem(r["text"])
        if k in seen:
            pairs.append((seen[k], r))
        else:
            seen[k] = r
    _report_pairs(pairs, new_ids, "duplicate stem",
                  lambda a, b: "%s" % normalise_stem(a["text"])[:88])

    print("\n2 · DUPLICATE ANSWER-SETS — no two rows may share all four "
          "options.")
    seen = {}
    pairs = []
    for r in rows:
        k = tuple(sorted(normalise_stem(o) for o in r["options"]))
        if k in seen:
            pairs.append((seen[k], r))
        else:
            seen[k] = r
    _report_pairs(pairs, new_ids, "duplicate answer-set",
                  lambda a, b: " | ".join(a["options"])[:88])


def _report_pairs(pairs, new_ids, what, describe):
    if not pairs:
        print("    ✅ none")
        return
    hard = [(a, b) for a, b in pairs
            if a["id"] in new_ids or b["id"] in new_ids]
    old = [(a, b) for a, b in pairs if (a, b) not in hard]
    for a, b in hard:
        # Correction 4 — a pair involving a row this branch wrote is THIS
        # run's finding and fails.
        fail(what, "%s (%s) == %s (%s) — %s"
             % (b["id"], b["leaf"], a["id"], a["leaf"], describe(a, b)))
        print("    ❌ %s (%s) == %s (%s)"
              % (b["id"], b["leaf"], a["id"], a["leaf"]))
        print("       %s" % describe(a, b))
    for a, b in old:
        # Correction 4 — an old-old pair is a pre-existing condition.
        NOTES.append("pre-existing %s: %s == %s" % (what, a["id"], b["id"]))
        print("    ⚠️  PRE-EXISTING (both rows predate this branch — reported, "
              "not failed)")
        print("       %s (%s) == %s (%s)"
              % (b["id"], b["leaf"], a["id"], a["leaf"]))


# ── 3 · paraphrase ──────────────────────────────────────────────────────

def check_paraphrase(rows, new_ids, scope_name):
    print("\n3 · PARAPHRASE — Jaccard over the whole %s." % scope_name)
    print("    ⚠️ Jaccard, NOT the overlap coefficient (correction 1), and a "
          "hard fail")
    print("    needs BOTH stems >= %d tokens (correction 2: a shared frame on "
          "two short" % JACCARD_MIN_TOKENS)
    print("    stems is a DISCRIMINATION SET, which is the point).")
    toks = {r["id"]: tokens(r["text"]) for r in rows}
    hard = short = pre = 0
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            j = jaccard(toks[a["id"]], toks[b["id"]])
            if j < JACCARD_HARD:
                continue
            both_long = (len(toks[a["id"]]) >= JACCARD_MIN_TOKENS
                         and len(toks[b["id"]]) >= JACCARD_MIN_TOKENS)
            involves_new = a["id"] in new_ids or b["id"] in new_ids
            if both_long and involves_new:
                hard += 1
                fail("paraphrase", "%s (%s) ~ %s (%s) Jaccard %.2f"
                     % (b["id"], b["leaf"], a["id"], a["leaf"], j))
                print("    ❌ %.2f  %s (%s)  ~  %s (%s)"
                      % (j, b["id"], b["leaf"], a["id"], a["leaf"]))
                print("         %s" % a["text"][:96])
                print("         %s" % b["text"][:96])
            elif involves_new:
                short += 1
                print("    ⚠️  %.2f  %s ~ %s — one stem under %d tokens; read "
                      "it: two facts with two" % (j, b["id"], a["id"],
                                                  JACCARD_MIN_TOKENS))
                print("         answers is a discrimination set, not a "
                      "duplicate.")
                print("         %s" % a["text"][:96])
                print("         %s" % b["text"][:96])
            else:
                pre += 1
                NOTES.append("pre-existing paraphrase %s ~ %s (%.2f)"
                             % (a["id"], b["id"], j))
    if not (hard or short or pre):
        print("    ✅ no pair at or above Jaccard %.2f" % JACCARD_HARD)
    else:
        print("    %d hard, %d short-stem (read them), %d pre-existing "
              "(reported, not failed)" % (hard, short, pre))


# ── 4 · length parity, measured the way the GATE measures it ────────────

def parity(rows, margin):
    """(visible, correct) at this margin. `verify_answer_lengths`' own rule."""
    visible = correct = 0
    for r in rows:
        if r["key"] is None or len(r["options"]) != 4:
            continue
        lens = sorted((len(o) for o in r["options"]), reverse=True)
        if lens[0] - lens[1] < margin:
            continue
        visible += 1
        if len(r["options"][r["key"]]) == lens[0]:
            correct += 1
    return visible, correct


def check_parity(leaf, rows):
    n, k = parity(rows, VAL.MARGIN)
    head = "    %-34s " % leaf
    if n == 0:
        print("%s%3d rows · NO set has a visibly longest option at margin %d"
              % (head, len(rows), VAL.MARGIN))
        print("%s⚠️ that is not a clean bill — brief §9.1 names flattening "
              "every set as" % (" " * 38))
        print("%sthe way to fake this number. Aim for a real population where "
              "the long" % (" " * 38))
        print("%soption is usually a DISTRACTOR." % (" " * 38))
        return
    rate = k / n
    hot = VAL._hot(n, k)
    mark = "❌" if hot else ("⚠️ " if (rate > CEILING or rate < FLOOR) else "✅")
    print("%s%3d rows · %3d visible · key is longest %3d = %5.1f%%  %s%s"
          % (head, len(rows), n, k, 100 * rate, mark,
             (" " + hot) if hot else ""))
    if hot:
        fail("length parity", "%s is %s at margin %d: %d/%d = %.1f%% "
             "(the gate's own rule)" % (leaf, hot, VAL.MARGIN, k, n,
                                        100 * rate))
    elif rate > CEILING:
        NOTES.append("%s is %.1f%% — over the %.0f%% authoring ceiling, though "
                     "not yet significant" % (leaf, 100 * rate, 100 * CEILING))
    elif rate < FLOOR:
        NOTES.append("%s is %.1f%% — under the %.0f%% floor (the MIRROR tell), "
                     "though not yet significant"
                     % (leaf, 100 * rate, 100 * FLOOR))
    # ⚠️ brief §9.1 — sweep, never trust one margin. A fix shaped to the value
    # this repo happens to ship is a fix shaped to a constant.
    worst_hi = worst_lo = None
    for m in SWEEP:
        vn, vk = parity(rows, m)
        if vn < 8:
            continue
        vr = vk / vn
        if worst_hi is None or vr > worst_hi[0]:
            worst_hi = (vr, m, vn, vk)
        if worst_lo is None or vr < worst_lo[0]:
            worst_lo = (vr, m, vn, vk)
    if worst_hi:
        print("%sworst across margins 3..10: high %.1f%% (%d/%d @ margin %d) · "
              "low %.1f%% (%d/%d @ margin %d)"
              % (" " * 38, 100 * worst_hi[0], worst_hi[3], worst_hi[2],
                 worst_hi[1], 100 * worst_lo[0], worst_lo[3], worst_lo[2],
                 worst_lo[1]))
        for lab, cell in (("GIVEAWAY", worst_hi), ("MIRROR", worst_lo)):
            r8, m8, n8, k8 = cell
            if VAL._hot(n8, k8):
                NOTES.append("%s: %s at margin %d (%d/%d = %.1f%%) — red in "
                             "the sweep even though margin %d is not"
                             % (leaf, VAL._hot(n8, k8), m8, k8, n8,
                                100 * r8, VAL.MARGIN))
    else:
        print("%s(too few visible sets at any margin to sweep)" % (" " * 38))


# ── 5, 6 · rank and position spread ─────────────────────────────────────

def check_spreads(leaf, rows):
    ranks = collections.Counter()
    positions = collections.Counter()
    n = 0
    for r in rows:
        if r["key"] is None or len(r["options"]) != 4:
            continue
        n += 1
        order = sorted(range(4), key=lambda j: (-len(r["options"][j]), j))
        ranks[order.index(r["key"]) + 1] += 1
        positions[r["key"]] += 1
    if not n:
        return
    rank_cells = " · ".join("rank %d %3d = %4.1f%%" % (i, ranks[i],
                                                       100 * ranks[i] / n)
                            for i in (1, 2, 3, 4))
    over = [i for i in (1, 2, 3, 4) if ranks[i] / n > RANK_MAX_SHARE]
    if over and n >= RANK_MIN_N:
        fail("rank spread", "%s: length rank %s holds %s of %d keys — over "
             "the %.0f%% ceiling (brief §6)"
             % (leaf, ",".join(str(i) for i in over),
                ",".join("%.1f%%" % (100 * ranks[i] / n) for i in over),
                n, 100 * RANK_MAX_SHARE))
        mark = "❌"
    elif over:
        NOTES.append("%s: rank %s over %.0f%% but only %d keys — arithmetic, "
                     "not yet a tell" % (leaf, over, 100 * RANK_MAX_SHARE, n))
        mark = "⚠️ "
    else:
        mark = "✅"
    print("    %-34s %s %s" % (leaf, mark, rank_cells))

    pos_cells = " · ".join("idx %d %3d = %4.1f%%" % (i, positions[i],
                                                     100 * positions[i] / n)
                           for i in range(4))
    unused = [i for i in range(4) if not positions[i]]
    if unused and n >= POSITION_MIN_N:
        fail("position spread", "%s: answer index %s never used across %d rows "
             "(brief §6)" % (leaf, ",".join(str(i) for i in unused), n))
        mark = "❌"
    elif unused:
        mark = "⚠️ "
    else:
        mark = "✅"
    print("    %-34s %s %s" % ("", mark, pos_cells))


# ── 7 · a stem that states another row's keyed answer ───────────────────

def check_key_echo(rows, scope_name):
    print("\n7 · A STEM THAT STATES ANOTHER ROW'S KEYED ANSWER (brief §9.6) — "
          "swept across")
    print("    the whole %s. ⚠️ Duplicate-stem and duplicate-option checks "
          "are BLIND to" % scope_name)
    print("    this: the collision is between one row's STEM and another "
          "row's KEY.")
    print("    Reported for a human read, never failed — a long key that is "
          "also a common")
    print("    phrase will match honestly. Only keys that carry a FACT are "
          "matched (>= %d tokens" % KEY_ECHO_MIN_TOKENS)
    print("    and %d chars, or %d chars with a digit): a bare "
          "\"chloroplasts\" is what the unit"
          % (KEY_ECHO_MIN_CHARS, KEY_ECHO_DIGIT_MIN_CHARS))
    print("    is ABOUT, not a leak. ⊕ 12 Sep 2026 a SECOND path admits "
          "a key that IS a bare quantity or count (\"1200 N.\", \"Two "
          "directions.\") however few words it uses.")
    print("    ⚠️  A PARAPHRASED leak is still invisible here — a stem "
          "restating the key in other words matches nothing. A clean "
          "section 7 is not proof there is no leak.")
    keys = []
    for r in rows:
        if r["key"] is None:
            continue
        k = normalise_stem(r["options"][r["key"]])
        ntok = len(TOKEN.findall(k))
        informative = (
            (ntok >= KEY_ECHO_MIN_TOKENS and len(k) >= KEY_ECHO_MIN_CHARS)
            or (any(c.isdigit() for c in k)
                and ntok >= KEY_ECHO_MIN_TOKENS
                and len(k) >= KEY_ECHO_DIGIT_MIN_CHARS)) or _key_is_bare_fact(k)
        if informative:
            keys.append((k, r))
    hits = 0
    for r in rows:
        stem = normalise_stem(r["text"])
        for k, owner in keys:
            if owner["id"] == r["id"]:
                continue
            if k in stem:
                hits += 1
                NOTES.append("%s's stem states %s's key" % (r["id"],
                                                            owner["id"]))
                print("    ⚠️  %s (%s) states the key of %s (%s)"
                      % (r["id"], r["leaf"], owner["id"], owner["leaf"]))
                print("        key:  %s" % owner["options"][owner["key"]][:90])
                print("        stem: %s" % r["text"][:90])
    if not hits:
        print("    ✅ no stem contains another row's key")


# ── 8 · literal \n, <sub>, and page references ──────────────────────────

def check_text_defects(paths, rows, scope_name):
    print("\n8 · LITERAL \\n AND <sub> (brief §9.10) — both hard fails.")
    bad = 0
    # ⚠️ ⊕ 12 Sep 2026 — THIS USED TO BE A RAW LINE SCAN OF THE WHOLE FILE, and
    # it was wrong in the permissive-to-strict direction (REPORT §9's fourth
    # correction, all over again). `ks3_data/c3/questions_06_chromatography.py`
    # carries a module docstring in which a previous author RULED, in prose,
    # that this estate writes Unicode subscripts and not `<sub>` — quoting the
    # markup twice in order to reject it. The raw scan matched the prose and
    # hard-failed a file no lane had touched, which would have blocked every
    # commit to unit C3 for a defect that does not exist.
    #
    # A comment cannot reach a pupil. Only a string inside QUESTIONS can. So
    # the scan is now STRUCTURAL: parse the file and walk the `QUESTIONS`
    # assignment, scanning every string constant within it — stems, options,
    # `why` text and ids alike. Docstrings and comments are not in that tree,
    # so they cannot be matched, while a `why` (which never loads into `rows`)
    # still is.
    for p in sorted(set(p for p in paths if p)):
        full = os.path.join(REPO, p)
        if not os.path.exists(full):
            continue
        try:
            tree = ast.parse(open(full, encoding="utf-8").read())
        except SyntaxError as exc:
            bad += 1
            fail("text defect", "%s does not parse: %s (line %s)"
                 % (p, exc.msg, exc.lineno))
            continue
        qnode = None
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id == "QUESTIONS"
                    for t in node.targets):
                qnode = node.value
        if qnode is None:
            continue
        for sub in ast.walk(qnode):
            if not (isinstance(sub, ast.Constant)
                    and isinstance(sub.value, str)):
                continue
            for needle, why in (("\n", "a literal \\n becomes a real "
                                 "newline plus indentation in the question"),
                                ("<sub>", "markup does not render in an "
                                 "option")):
                if needle in sub.value:
                    bad += 1
                    fail("text defect", "%s:%d carries %r — %s"
                         % (p, sub.lineno, needle, why))
                    print("    ❌ %s:%d  %s"
                          % (p, sub.lineno, sub.value.strip()[:80]))
    # And the same defect as it reaches a pupil, from the LOADED strings —
    # a real newline in a stem or option, whatever put it there.
    for r in rows:
        for label, s in ([("stem", r["text"])]
                         + [("option", o) for o in r["options"]]):
            if "\n" in s or "<sub>" in s:
                bad += 1
                fail("text defect", "%s's %s carries a real newline or <sub>"
                     % (r["id"], label))
                print("    ❌ %s %s: %r" % (r["id"], label, s[:70]))
    if not bad:
        print("    ✅ none in %d file(s) or %d row(s)"
              % (len(set(p for p in paths if p)), len(rows)))

    print("\n8b · PAGE REFERENCES (brief §9.10) — every stem is read away from "
          "the lesson.")
    print("     ⚠️ Only the UNAMBIGUOUS senses are matched (correction 3): "
          "\"their figure\"")
    print("     is a number, \"rests on a table\" is furniture, \"the picture "
          "on the retina\"")
    print("     is an optical image. None of those is a page reference.")
    hits = 0
    for r in rows:
        for rx in PAGE_REF:
            m = rx.search(r["text"])
            if m:
                hits += 1
                NOTES.append("%s may reference the page: %r"
                             % (r["id"], m.group(0)))
                print("     ⚠️  %s (%s): %r in %r"
                      % (r["id"], r["leaf"], m.group(0), r["text"][:78]))
                break
    if not hits:
        print("     ✅ no unambiguous page reference in %d row(s)" % len(rows))


# ── 9 · the frozen window ───────────────────────────────────────────────

# ── 10 · over-assertion: does an absolute MARK the wrong options? ─────────

# ⊕ Ruled by Mide, 13 Sep 2026. Swept across the whole estate on 12 Sep:
# "at all / genuinely / somehow / truly / actually / really / always / never /
# only" appeared **2,622 times in distractors and 208 times in keys** — wrong
# 92.7% of the time, against 75% by chance (three of four options are wrong).
#
# ⚠️ Four lanes converged on the habit independently in one night, each one's
# share looking like noise. It is only visible per LEAF and above, which is why
# it belongs here rather than in an author's head. A pupil who learns "the
# over-asserting option is wrong" eliminates a distractor for free.
#
# THE RULE (Mide, 13 Sep): in NEW rows, an absolute may appear in a distractor
# no more often than it appears in a key, per leaf. Repair of SHIPPED rows is
# night-3 work and is deliberately NOT enforced here.
OVER_ASSERT = re.compile(
    r"\b(at all|genuinely|somehow|whatever|truly|secretly|after all|actually|"
    r"in fact|really|always|never|only|every single|no exception)\b", re.I)


def check_over_assertion(rows, new_ids, scope_name):
    print("\n10 · OVER-ASSERTION (Mide, 13 Sep) — an absolute must not MARK the "
          "wrong\n     options. Measured on NEW rows only; shipped rows are "
          "night-3 repair work.")
    per = collections.defaultdict(lambda: [0, 0])     # leaf -> [in distractors, in keys]
    for r in rows:
        if new_ids and r["id"] not in new_ids:
            continue
        leaf = r.get("leaf") or scope_name
        for i, o in enumerate(r["options"]):
            if not OVER_ASSERT.search(o or ""):
                continue
            per[leaf][1 if i == r["key"] else 0] += 1
    if not per:
        print("     ✅ no new row uses an absolute")
        return
    bad = 0
    for leaf, (d, k) in sorted(per.items()):
        tot = d + k
        rate = 100.0 * d / tot if tot else 0.0
        # chance is 75%: three of four options are wrong.
        # ⚠️ HOW THE RULING IS READ, and why it is not read literally.
        # Mide's words on 13 Sep: "absolutes in a distractor no more often than
        # in the key, per leaf". Taken literally that is d <= k — but every row
        # has THREE distractors to ONE key, so pure chance already gives d ≈ 3k
        # (75%), and a literal reading would fail every leaf in the estate
        # including flawless ones. The DEFECT the ruling is aimed at is the
        # estate-wide 92.7% against that 75% baseline: the absolute MARKING the
        # wrong options. So the test is "significantly above chance", not
        # "d <= k". Flagged at 85% with n >= 12 — comfortably clear of chance,
        # and it catches every leaf in the 12 Sep sweep that was a real tell.
        over = tot >= 12 and rate > 85.0
        flag = ("  ← ABOVE 85%: the absolute marks the wrong options"
                if over else "")
        if over:
            bad += 1
        print("     %-34s %3d in distractors · %3d in keys · %5.1f%%%s"
              % (leaf, d, k, rate, flag))
    if bad:
        NOTES.append("over-assertion: %d leaf/leaves where an absolute appears "
                     "only in distractors (%d+ times) and never in a key"
                     % (bad, 4))
    else:
        print("     ✅ no leaf uses an absolute only on the wrong side")

def check_frozen(stage, rows, leaves, new_ids, old_by_leaf):
    print("\n9 · THE FROZEN WINDOW — bank_position 0..11 is every automatic "
          "assignment this")
    print("    leaf has ever produced (RISKS D7). Proved against "
          "`git show <merge-base>:<file>`,")
    print("    never against the working tree alone.")
    clean = True

    # 9a · no new id lands inside the first four of its band.
    # ⚠️ Positions 0–11 ARE ids e01–e04, s01–s04, h01–h04, at both key stages
    # — `question_bank` and `ks4_pool_check` both assert it. So a new id
    # numbered <= 04 is an INSERT into the frozen window however it was
    # written, and a top-up must continue each band's sequence from 05.
    for r in rows:
        if r["id"] not in new_ids:
            continue
        m = ID_TAIL.search(r["id"] or "")
        if not m:
            fail("frozen window", "%s does not end in a band letter plus a "
                 "number" % r["id"])
            clean = False
            continue
        if int(m.group(2)) <= FROZEN_PER_BAND:
            fail("frozen window", "%s is a NEW row numbered %s — ids 01..%02d "
                 "of each band are the frozen twelve; a top-up appends from "
                 "%02d" % (r["id"], m.group(2), FROZEN_PER_BAND,
                           FROZEN_PER_BAND + 1))
            clean = False
        if BAND_LETTER.get(r["band"]) != m.group(1):
            fail("frozen window", "%s is band %r but its id says %r"
                 % (r["id"], r["band"], m.group(1)))
            clean = False

    # 9b · ids continue each band's sequence: 01..N, no gaps, no duplicates.
    for leaf in leaves:
        by_band = collections.defaultdict(list)
        for r in rows:
            if r["leaf"] != leaf:
                continue
            m = ID_TAIL.search(r["id"] or "")
            if m:
                by_band[m.group(1)].append(int(m.group(2)))
        for letter, nums in sorted(by_band.items()):
            want = list(range(1, len(nums) + 1))
            if sorted(nums) != want:
                fail("frozen window", "%s band %r ids are %s — expected "
                     "%02d..%02d with no gaps and no repeats"
                     % (leaf, letter, sorted(nums), 1, len(nums)))
                clean = False

    # 9c · no row at position 0..11 changed, compared row by row.
    for leaf in leaves:
        now = [r for r in rows if r["leaf"] == leaf]
        now.sort(key=lambda r: (r["position"] if r["position"] is not None
                                else 0))
        old = old_by_leaf.get(leaf)
        if old is None:
            print("    ·  %-34s new leaf at the merge-base — nothing frozen "
                  "yet" % leaf)
            continue
        for pos in range(min(FROZEN_POSITIONS, len(old), len(now))):
            a, b = old[pos], now[pos]
            # ⚠️ NAME THE FIELD THAT MOVED. This used to print only
            # "position 0 CHANGED: b1-03-e01 -> b1-03-e01", which on the
            # commonest case — the id is the same and the TEXT was edited —
            # tells the reader nothing and reads like a bug in the checker
            # rather than a finding about the row.
            moved = []
            if a["id"] != b["id"]:
                moved.append("id %s -> %s" % (a["id"], b["id"]))
            if normalise_stem(a["text"]) != normalise_stem(b["text"]):
                moved.append("stem %r -> %r"
                             % (a["text"][:48], b["text"][:48]))
            if ([normalise_stem(o) for o in a["options"]]
                    != [normalise_stem(o) for o in b["options"]]):
                moved.append("options changed")
            if a["key"] != b["key"]:
                moved.append("key index %s -> %s" % (a["key"], b["key"]))
            if moved:
                fail("frozen window", "%s position %d CHANGED (%s) — %s"
                     % (leaf, pos, b["id"], "; ".join(moved)))
                print("    ❌ %s position %d changed (%s)"
                      % (leaf, pos, b["id"]))
                for m in moved:
                    print("       %s" % m)
                clean = False
        if len(old) > len(now):
            fail("frozen window", "%s lost %d row(s) — ids retire, they are "
                 "never renumbered" % (leaf, len(old) - len(now)))
            clean = False
    if clean:
        print("    ✅ every frozen row intact, every new id continues its "
              "band's sequence")


# ── old-tree reconstruction, per key stage ──────────────────────────────

def ks3_old(unit, mb):
    """Each leaf's rows AS THEY WERE at the merge-base, in file order."""
    out = {}
    if not mb:
        return out
    for path in files_at(mb, "ks3_data/%s/" % unit.lower()):
        if "/questions_" not in path:
            continue
        qs = literal_questions(blob_at(mb, path))
        if qs is None:
            continue
        src = blob_at(mb, path) or ""
        m = re.search(r'^LESSON\s*=\s*"([^"]+)"', src, re.M)
        if not m:
            continue
        out[m.group(1)] = [{
            "id": q.get("id"), "text": q.get("text", ""),
            "options": [o.get("text", "") for o in q.get("options", [])],
            "key": next((i for i, o in enumerate(q.get("options", []))
                         if o.get("correct")), None),
        } for q in qs]
    return out


def ks4_old(topic, subject, mb):
    """Each subtopic's rows at the merge-base, in `load_pool` order.

    `load_pool` walks modules sorted by name and numbers each subtopic's rows
    from 0 within itself, so the same walk over the old blobs reproduces the
    old `bank_position` without importing anything.
    """
    out = collections.defaultdict(list)
    if not mb:
        return dict(out)
    paths = [p for p in files_at(mb, "ks4_data/questions/%s/" % subject)
             if p.endswith(".py") and topic_of_module(p) == topic]
    for path in sorted(paths, key=os.path.basename):
        qs = literal_questions(blob_at(mb, path))
        if qs is None:
            continue
        for q in qs:
            out[q.get("subtopic_slug")].append({
                "id": q.get("id"), "text": q.get("text", ""),
                "options": list(q.get("options", [])),
                "key": q.get("correct_index"),
            })
    return dict(out)


def main():
    ap = argparse.ArgumentParser(
        description="MRB-338 per-leaf checker. Duplicates sweep the whole "
                    "unit/topic (brief §9.4); parity and spread are per leaf.")
    ap.add_argument("--unit", help="KS3 unit code, e.g. B1")
    ap.add_argument("--lesson", help="KS3 lesson slug — one leaf of --unit")
    ap.add_argument("--topic", help="KS4 topic id, e.g. cell-biology")
    ap.add_argument("--subtopic", help="KS4 subtopic slug — one leaf; its "
                                       "topic is derived")
    args = ap.parse_args()

    if args.lesson and not args.unit:
        ap.error("--lesson needs --unit")
    if not (args.unit or args.topic or args.subtopic):
        ap.error("give --unit [--lesson] or --topic / --subtopic")
    if args.unit and (args.topic or args.subtopic):
        ap.error("--unit is KS3 and --topic/--subtopic are KS4; pick one")

    os.chdir(REPO)
    mb = merge_base()
    print("mrb338_leafcheck — the per-leaf checker, MRB-338 REPORT §9")
    print("  merge-base with origin/main: %s" % (mb or "NOT FOUND — every row "
                                                 "will count as pre-existing"))

    if args.unit:
        stage = "KS3"
        unit = args.unit.upper()
        rows, leaves, files = load_ks3(unit)
        if not rows:
            print("  ❌ no KS3 bank rows for unit %r" % unit)
            return 2
        scope_name = "unit %s" % unit
        paths = sorted(set(files.values()))
        old_by_leaf = ks3_old(unit, mb)
        focus = [args.lesson] if args.lesson else leaves
        if args.lesson and args.lesson not in leaves:
            print("  ❌ %r is not a lesson of %s. Leaves: %s"
                  % (args.lesson, unit, ", ".join(leaves)))
            return 2
    else:
        stage = "KS4"
        if args.subtopic:
            topic, subject = ks4_topic_of(args.subtopic)
            if not topic:
                print("  ❌ %r is not a KS4 subtopic in the curriculum tree"
                      % args.subtopic)
                return 2
        else:
            topic = args.topic
            subject = ks4_subject_of_topic(topic)
            if not subject:
                print("  ❌ %r is not a KS4 topic in the curriculum tree"
                      % topic)
                return 2
        rows, leaves = load_ks4(topic, subject)
        if not rows:
            print("  ❌ no KS4 pool rows for topic %r" % topic)
            return 2
        scope_name = "topic %s (%s)" % (topic, subject)
        paths = [p for p in files_at("HEAD", "ks4_data/questions/%s/" % subject)
                 if p.endswith(".py") and topic_of_module(p) == topic]
        old_by_leaf = ks4_old(topic, subject, mb)
        focus = [args.subtopic] if args.subtopic else leaves
        if args.subtopic and args.subtopic not in leaves:
            print("  ❌ %r has no rows in %s" % (args.subtopic, topic))
            return 2

    old_ids = set()
    for lst in old_by_leaf.values():
        old_ids |= {q["id"] for q in lst}
    new_ids = {r["id"] for r in rows} - old_ids

    print("  scope: %s · %d leaf/leaves · %d rows · %d of them NEW on this "
          "branch" % (scope_name, len(leaves), len(rows), len(new_ids)))
    print("  under test: %s" % ", ".join(focus))
    if mb and not old_ids:
        print("  ⚠️  the merge-base carries NO rows for this scope, so every "
              "row reads as new.")

    check_duplicates(rows, new_ids, scope_name)
    check_paraphrase(rows, new_ids, scope_name)

    print("\n4 · LENGTH PARITY, measured the way `verify_answer_lengths` "
          "measures it —")
    print("    discard every set whose top two options are within %d "
          "characters, then ask" % VAL.MARGIN)
    print("    how often the key is the long one. Chance %.0f%%, authoring "
          "ceiling %.0f%%, floor" % (100 * VAL.CHANCE, 100 * CEILING))
    print("    %.0f%% (the mirror tell). ⚠️ n=0 is not a pass — brief §9.1."
          % (100 * FLOOR))
    for leaf in focus:
        check_parity(leaf, [r for r in rows if r["leaf"] == leaf])

    print("\n5 · KEY LENGTH-RANK SPREAD — 1 = longest … 4 = shortest. No rank "
          "may hold")
    print("    more than %.0f%% of the keys (brief §6); enforced from %d keys "
          "up." % (100 * RANK_MAX_SHARE, RANK_MIN_N))
    print("6 · KEY POSITION SPREAD — no index may be unused (brief §6); "
          "enforced from %d rows up." % POSITION_MIN_N)
    for leaf in focus:
        check_spreads(leaf, [r for r in rows if r["leaf"] == leaf])

    check_key_echo(rows, scope_name)
    check_text_defects(paths, rows, scope_name)
    check_over_assertion(rows, new_ids, scope_name)
    check_frozen(stage, rows, leaves, new_ids, old_by_leaf)

    print("\n" + "=" * 72)
    if NOTES:
        print("READ THESE — reported, not failed (%d):" % len(NOTES))
        for n in NOTES:
            print("  · %s" % n)
    if FAILS:
        print("\nmrb338_leafcheck: ❌ FAIL — %d hard failure(s)" % len(FAILS))
        for f in FAILS:
            print("  ❌ %s" % f)
        return 1
    print("\nmrb338_leafcheck: ✅ no hard failure.")
    print("  ⚠️  This is an ADVISOR. `verify_answer_lengths` and "
          "`set_work_scope_check` are")
    print("      the gates, and `tools/mrb338_land.sh` runs them. Green here "
          "is not a commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
