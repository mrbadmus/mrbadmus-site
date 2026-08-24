#!/usr/bin/env python3
"""pool_ownership.py — one bank per surface. MRB-288, ruled by Mide 24 Aug 2026.

── THE CONTRACT THIS GATE ENFORCES ─────────────────────────────────────

Three question pools, one per surface. No surface SERVES questions from a
pool it does not own:

    lesson-page ladder   → the authored ladder (mirrored as ks3_ladder_questions)
    weekly assignment    → ks3_assignment_bank
    dashboard flashcards → ks3_cards

SERVING is reading a pool to put its questions or cards in front of a user.
It is NOT the same thing as resolving a ref to a lesson slug, and it is NOT
reading attempt history: the FROM YOUR WORK targeting reads assignment
attempts to weight practice toward weaknesses, and that is intended pedagogy
which survives untouched. This gate polices where questions COME FROM, never
what may be LEARNED from how they were answered.

── WHY IT EXISTS ───────────────────────────────────────────────────────

composition fed assignments from BOTH the ladder and the bank — verified in
production: assignment 282f2277… (18 Aug) is 100% ladder rows, 72a5b315…
(20 Aug) is 100% bank rows. The seam was `assignment_questions.rung`. The
database now refuses the seam (`one_pool_per_assignment`, 20260824214711);
this gate refuses the code paths, so the next cross-feed fails a build
instead of shipping and being found in the rows.

── THE FROZEN EXCEPTION (report item 6 — awaiting Mide's ruling) ───────

The class page's PRACTICE ROUND serves multiple-choice questions, and the
only pool holding scored MCQs for covered lessons is the ladder mirror. Its
ruled owner pool (ks3_cards) holds flashcards — front/back pairs with no
options and no answer — and cannot supply a scored round. Per MRB-288's
pre-ruling, a working surface is never broken mid-run to satisfy a table, so
the round is FROZEN exactly as it reads today:

    FROZEN MRB-288 · shared/student-live.js — the practice round reads
    ks3_ladder_questions (rungs recall+apply, filtered by the covered-lesson
    set) and /api/class/practice (backend) reads the same table for the same
    round. Both are named below, both are bounded to exactly one serving
    read each, and any NEW serving read of the ladder outside them is a
    failure.

Everything here is static and fast: it reads the two repos' source files.
The database-level truth (the constraint, the live rows) is proven by
`one_pool_per_assignment` itself and re-checked whenever
`export_ks3_questions.py --verify` runs.
"""

import os
import re
import sys

SITE = os.path.dirname(os.path.abspath(__file__))
BACKEND = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"

POOLS = ("ks3_assignment_bank", "ks3_ladder_questions", "ks3_cards")
RETIRED_NAME = "ks3_bank_questions"   # must never come back into live code

failures = []


def fail(what, detail):
    failures.append("%s — %s" % (what, detail))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ── 1 · the class page (shared/student-live.js) ─────────────────────────
#
# Serving reads select question/card CONTENT (`options` for questions,
# `front`/`back` for cards). Resolution reads select identity columns only.
def check_student_live():
    src = read(os.path.join(SITE, "shared", "student-live.js"))

    if RETIRED_NAME in src:
        fail("student-live.js", "references the retired name %s" % RETIRED_NAME)

    # every from("<pool>") call, with the FULL select argument that follows it
    # (the round's column list spans concatenated string literals, so this
    # captures everything up to the closing paren, not just the first segment)
    reads = re.findall(
        r'from\("(%s)"\)\s*\.select\((.*?)\)' % "|".join(POOLS), src, re.S)

    bank_reads = [sel for t, sel in reads if t == "ks3_assignment_bank"]
    ladder_reads = [sel for t, sel in reads if t == "ks3_ladder_questions"]
    card_reads = [sel for t, sel in reads if t == "ks3_cards"]

    # the assignment pool: the page RESOLVES refs against it and never serves
    # from it (its questions reach the page through the backend's payload).
    for sel in bank_reads:
        if "options" in sel or "text" in sel:
            fail("student-live.js", "serves question content straight from "
                 "ks3_assignment_bank (select %r); the assignment pool is "
                 "served by composition only" % sel)
    if not any("lesson_slug" in sel for sel in bank_reads):
        fail("student-live.js", "the ref→lesson resolution read of "
             "ks3_assignment_bank is gone; 'Open the lesson', deck scope and "
             "FROM YOUR WORK all hang off it")

    # the cards pool: exactly one serving read, and it is the flashcard deck.
    serving_cards = [sel for sel in card_reads if "front" in sel]
    if len(serving_cards) != 1:
        fail("student-live.js", "expected exactly 1 flashcard serving read of "
             "ks3_cards, found %d" % len(serving_cards))

    # the ladder pool: one resolution read + ONE frozen serving read (the
    # practice round). A second serving read is a new cross-feed.
    serving_ladder = [sel for sel in ladder_reads if "options" in sel]
    if len(serving_ladder) != 1:
        fail("student-live.js", "expected exactly 1 ladder serving read (the "
             "FROZEN MRB-288 practice round), found %d — a new one is a new "
             "cross-feed, and removing the frozen one is Mide's ruling to "
             "make, not a build's" % len(serving_ladder))
    resolution_ladder = [sel for sel in ladder_reads
                         if "options" not in sel and "lesson_slug" in sel]
    if len(resolution_ladder) != 1:
        fail("student-live.js", "expected exactly 1 ladder resolution read "
             "(ref→lesson), found %d" % len(resolution_ladder))


# ── 2 · the lesson-page ladder serves from the authored source ──────────
def check_lesson_ladder():
    for rel in (os.path.join("shared", "ks3.js"), "build_ks3.py"):
        src = read(os.path.join(SITE, rel))
        for pool in ("ks3_assignment_bank", "ks3_cards", RETIRED_NAME):
            if pool in src:
                fail(rel, "references %s; the lesson ladder is baked from "
                     "ks3_data and touches no other surface's pool" % pool)


# ── 3 · no OTHER surface reads any pool ─────────────────────────────────
def check_other_surfaces():
    others = [os.path.join("shared", f) for f in
              ("teacher-live.js", "teacher-data.js", "student-data.js",
               "class-entry.js", "mrbadmus.v2.js")]
    others += [f for f in os.listdir(SITE) if f.endswith(".html")]
    for rel in others:
        path = os.path.join(SITE, rel)
        if not os.path.isfile(path):
            continue
        src = read(path)
        for pool in POOLS + (RETIRED_NAME,):
            if pool in src:
                fail(rel, "references %s — a surface serving from a pool it "
                     "does not own, or a stale name" % pool)


# ── 4 · the composed row cannot carry a rung — the migration is present ─
def check_constraint_migration():
    path = os.path.join(SITE, "supabase", "migrations",
                        "20260824214711_mrb288_one_pool_per_assignment.sql")
    if not os.path.isfile(path):
        fail("migrations", "20260824214711_mrb288_one_pool_per_assignment.sql "
             "is missing")
        return
    src = read(path)
    if "one_pool_per_assignment" not in src or \
       "band is not null and rung is null" not in src:
        fail("migrations", "the one_pool_per_assignment definition has "
             "drifted from the ruling")


# ── 5 · composition (the Node backend) ──────────────────────────────────
def check_backend():
    server = read(os.path.join(BACKEND, "server.js"))
    compose = read(os.path.join(BACKEND, "assignment-compose.js"))

    for name, src in (("server.js", server), ("assignment-compose.js", compose)):
        if RETIRED_NAME in src:
            fail(name, "references the retired name %s" % RETIRED_NAME)

    # composition reads the assignment pool and nothing else
    m = re.search(r"async function bankFor.*?\n}", server, re.S)
    if not m:
        fail("server.js", "bankFor() not found — composition's pool read has "
             "moved; re-point this gate at it")
    else:
        body = m.group(0)
        if "ks3_assignment_bank" not in body:
            fail("server.js", "bankFor() no longer reads ks3_assignment_bank")
        for other in ("ks3_ladder_questions", "ks3_cards"):
            if other in body:
                fail("server.js", "bankFor() reads %s — composition serving "
                     "from a pool it does not own" % other)

    if "ks3_cards" in server:
        fail("server.js", "reads ks3_cards; the flashcard deck is served "
             "client-side from its owner pool and the backend has no business "
             "in it")

    # a composed row carries band, never rung
    if not re.search(r"rung:\s*null,\s*\n\s*band:\s*q\.band", server):
        fail("server.js", "the composition insert no longer writes "
             "{rung: null, band: q.band} — the one-pool row shape has "
             "changed; prove the new shape against one_pool_per_assignment "
             "and update this gate")

    # every ladder reference sits inside the FROZEN practice route
    route = re.search(
        r"app\.get\('/api/class/practice'.*?\n\}\);", server, re.S)
    if not route:
        fail("server.js", "/api/class/practice route not found")
    else:
        span = route.span()
        for m2 in re.finditer(r"ks3_ladder_questions", server):
            if not (span[0] <= m2.start() < span[1]):
                # comments above the route explain it; allow only comment
                # lines ("//" before it on the same line)
                line_start = server.rfind("\n", 0, m2.start()) + 1
                line = server[line_start:m2.start()]
                if "//" in line or "*" in line.strip()[:1]:
                    continue
                fail("server.js", "ks3_ladder_questions read outside the "
                     "FROZEN /api/class/practice route (offset %d) — a new "
                     "cross-feed" % m2.start())


def main():
    check_student_live()
    check_lesson_ladder()
    check_other_surfaces()
    check_constraint_migration()
    check_backend()

    if failures:
        print("❌ pool_ownership: %d failure(s)\n" % len(failures))
        for f in failures:
            print("   · %s" % f)
        print()
        return 1

    print("✅ pool_ownership: one bank per surface")
    print("   ladder page  ← authored ladder (ks3_data, baked at build)")
    print("   assignment   ← ks3_assignment_bank (backend composition only)")
    print("   flashcards   ← ks3_cards (class page, one serving read)")
    print("   FROZEN MRB-288: the practice round serves recall+apply from "
          "ks3_ladder_questions\n   (student-live.js + /api/class/practice) "
          "— bounded to one serving read each,\n   awaiting Mide's ruling.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
