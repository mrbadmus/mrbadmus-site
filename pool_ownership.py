#!/usr/bin/env python3
"""pool_ownership.py — one bank per surface. MRB-288, ruled by Mide 24 Aug 2026.
⊕ Extended to KS4 by MRB-332, 6 Sep 2026.

── THE CONTRACT THIS GATE ENFORCES ─────────────────────────────────────

FOUR question pools, one per surface. No surface SERVES questions from a
pool it does not own:

  KS3 (MRB-288)
    lesson-page ladder      → the authored ladder (mirrored as
                              ks3_ladder_questions)
    weekly assignment       → ks3_assignment_bank
    dashboard flashcards    → ks3_cards

  KS4 (MRB-332)
    lesson-page "Test yourself" → the `quiz` entries in all_subtopics_*.py,
                              baked into the page by generate_site_v5. There
                              is NO runtime pool read: the questions are in
                              the HTML the student is already looking at.
    weekly assignment       → ks4_assignment_bank (from ks4_data/, backend
                              composition only — exactly like KS3's)

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

── WHY KS4 IS TWO POOLS AND TWO TABLES (MRB-332) ───────────────────────

At KS4 the cross-feed the contract forbids has a different shape and a
worse consequence. The lesson pages' "Test yourself" questions are PRINTED
ON A PAGE THE CHILD CAN OPEN WHENEVER THEY LIKE. Serving one of them as
homework is not merely a pool mix-up: it publishes the answers in advance,
and it does so invisibly, because every individual question is correct,
on-spec and reviewed. So check 8 below does not check a table NAME — it
measures the CONTENT, comparing every authored assignment stem against
every lesson-page stem and failing on a match.

The second reason is the slug collision. `ks3_assignment_bank` has no
key-stage column and is joined on `lesson_slug` alone, and eight KS4
subtopic slugs are byte-identical to KS3 lesson slugs —

    aerobic-respiration    catalysts             changes-of-state
    chromatography         conservation-of-mass  distance-time-graphs
    electric-fields        magnetic-fields

— so a KS4 lookup against KS3's table returns twelve KS3 questions: real
science, correct, and three years too easy, with nothing anywhere saying
so. MRB-331 held that off with `bankFor(keyStage, …)`, a guard that works
only while every future call site remembers its first argument. MRB-332
ends it structurally with a second table, and check 7 below asserts the two
branches of `bankFor` cannot reach each other's table.

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

import collections
import difflib
import glob
import os
import re
import sys

SITE = os.path.dirname(os.path.abspath(__file__))

# ⚠️ WHICH BACKEND CHECKOUT, AND WHY IT IS NOT SIMPLY THE SIBLING REPO
# (⊕ MRB-331, 7 Sep 2026).
#
# This read used to be hardwired to the main backend checkout. That is fine on
# a machine with one branch checked out and actively wrong on this one: the
# main checkout is a shared working copy and any session can leave it on any
# branch. On 7 September it was sitting on a colleague's `feat/mrb332-ks4-pool`,
# and this gate went RED on `bankFor() no longer reads ks3_assignment_bank` —
# a true statement about a branch that has nothing to do with the tree being
# pushed, reported as if it were about it.
#
# ⚠️ THE FAILURE DIRECTION IS THE DANGEROUS ONE. Red-for-the-wrong-reason is
# survivable because somebody investigates. The same wiring can just as easily
# read a colleague's branch that HAPPENS to satisfy the contract and report
# green about a backend nobody is shipping — a gate that has stopped watching
# while still printing PASS.
#
# So it takes an explicit path, exactly as `verify_week_truth.py` does and for
# exactly that file's reason: point it at the backend actually being shipped.
# The sibling repo remains the default, because that is what an ordinary
# machine has.
BACKEND = (
    (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None)
    or os.environ.get("MRB_BACKEND")
    or "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
)

POOLS = ("ks3_assignment_bank", "ks3_ladder_questions", "ks3_cards")
RETIRED_NAME = "ks3_bank_questions"   # must never come back into live code

# The KS4 assignment pool (MRB-332). Deliberately NOT added to POOLS: the KS3
# checks above are tuned to KS3's shape and read patterns, and widening their
# tuple would change what they measure. The KS4 pool gets its own checks.
KS4_POOL = "ks4_assignment_bank"

# How near is "near" for the info-only similarity report in check 8. An exact
# match after normalisation is a FAILURE; this is the eyeballing band beneath
# it, for a stem that has been reworded rather than copied.
NEAR_DUPLICATE_RATIO = 0.88

failures = []
notes = []


def fail(what, detail):
    failures.append("%s — %s" % (what, detail))


def note(what, detail):
    """Something a reader must see that is not (yet) a failure.

    Printed on a green run as well as a red one. A gate that quietly declines
    to measure something is a gate that has stopped watching, so anything
    this gate skips says so out loud.
    """
    notes.append("%s — %s" % (what, detail))


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
def _other_surfaces():
    """The frontend files that own no pool at all.

    Factored out so check 6 sweeps exactly the same set for the KS4 pool and
    the two can never drift apart. `student-live.js` is absent here because it
    DOES own reads (checked in 1); check 6 adds it back, because it owns no
    KS4 read.
    """
    others = [os.path.join("shared", f) for f in
              ("teacher-live.js", "teacher-data.js", "student-data.js",
               "class-entry.js", "mrbadmus.v2.js")]
    others += [f for f in os.listdir(SITE) if f.endswith(".html")]
    return others


def check_other_surfaces():
    others = _other_surfaces()
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
        # ⊕ MRB-332 moved the two table NAMES into `BANK_TABLES` in
        # assignment-compose.js, because there are now two of them and the
        # key stage picks between them. `BANK_TABLES.KS3` is the same read
        # this line has always asserted, spelled through the map; the literal
        # is still accepted so this check does not depend on which spelling
        # the backend happens to be using.
        if "ks3_assignment_bank" not in body and "BANK_TABLES.KS3" not in body:
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

    # ── ⊕ MRB-331 · EVERY BANK READ SITS IN A NAMED PLACE ──────────────
    #
    # Until Set work there was exactly one way into `ks3_assignment_bank` from
    # the backend — `bankFor()` — and this gate policed its BODY without ever
    # asking whether anything else was reading the table. That was a real hole
    # and the gate's own closing note said so: "a bank read outside bankFor()
    # is currently unconstrained by this gate".
    #
    # MRB-331 gave three surfaces a reason to want the bank (the topics sheet,
    # its question preview, and the write that validates the chosen ids), so
    # the hole became a live risk rather than a theoretical one. It is closed
    # the way the ladder's was: an allowlist of named spans, each justified,
    # and anything outside them fails.
    #
    # ⚠️ THE ALLOWLIST IS SHORT ON PURPOSE. Two of the three new surfaces do
    # NOT appear in it, because they were built to go through `bankFor()` with
    # a different column list rather than to open a read of their own. If a
    # future change gives one its own `.from('ks3_assignment_bank')`, this gate
    # fails and the author has to come here and say why — which is the entire
    # point.
    BANK_HOMES = (
        (r"async function bankFor.*?\n}",
         "composition's pool read, the ruled owner path — every SERVING read "
         "of the bank goes through it, including the Set work sheet's topic "
         "counts and its question preview, which pass a column list rather "
         "than opening a read of their own"),
        (r"async function readAssignmentWithQuestions.*?\n}",
         "hydrating an assignment's stored source_refs back into questions. "
         "Serving, and of the pool the assignment owns"),
        (r"app\.post\('/api/teacher/set-work'.*?\n\}\);",
         "the write-side seal (MRB-331): it re-reads the chosen ids to prove "
         "every one belongs to the lesson the teacher picked. ⚠️ It selects "
         "`id, lesson_slug, band` and MUST NOT select `text` or `options` — "
         "it is validating provenance, not serving questions"),
    )
    spans = []
    for pattern, why in BANK_HOMES:
        m3 = re.search(pattern, server, re.S)
        if not m3:
            fail("server.js", "the bank home for %r is gone — re-point this "
                 "gate at it before the allowlist quietly stops covering "
                 "anything" % why[:48])
        else:
            spans.append((m3.span(), why))

    for m4 in re.finditer(r"ks3_assignment_bank", server):
        if any(a <= m4.start() < b for (a, b), _why in spans):
            continue
        line_start = server.rfind("\n", 0, m4.start()) + 1
        line = server[line_start:m4.start()]
        if "//" in line or line.strip()[:1] == "*":
            continue          # prose about the bank, not a read of it
        fail("server.js", "ks3_assignment_bank read outside every named home "
             "(offset %d) — a new way into the assignment pool. Add it to "
             "BANK_HOMES with a reason, or route it through bankFor()"
             % m4.start())

    # the write-side seal must not become a serving read
    seal = re.search(r"app\.post\('/api/teacher/set-work'.*?\n\}\);",
                     server, re.S)
    if seal:
        body = seal.group(0)
        m5 = re.search(r"from\('ks3_assignment_bank'\)\s*\.select\((.*?)\)",
                       body, re.S)
        if m5:
            for banned in ("text", "options"):
                if banned in m5.group(1):
                    fail("server.js", "/api/teacher/set-work selects %r from "
                         "the bank — it validates provenance and must not "
                         "serve question content" % banned)

    # ── the key stage is a precondition, not a filter ───────────────────
    #
    # `ks3_assignment_bank` has NO key_stage column; only its name says KS3.
    # Eight KS4 subtopic slugs are byte-identical to KS3 lesson slugs, so a
    # join on `lesson_slug` alone hands a Year 11 class Year 8 questions.
    # `bankFor` takes the key stage as its FIRST argument so no caller can
    # reach the table without having said which key stage it is asking for.
    sig = re.search(r"async function bankFor\(([^)]*)\)", server)
    if not sig:
        fail("server.js", "bankFor's signature is gone")
    elif "keyStage" not in sig.group(1).replace("key_stage", "keyStage"):
        fail("server.js", "bankFor no longer takes a key stage as an "
             "argument — the KS3/KS4 slug collision is unguarded and a KS4 "
             "class can be served KS3 questions on eight lessons")

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


# ── 6 · no frontend surface names the KS4 assignment pool ───────────────
#
# The KS4 pool is served by backend composition ONLY, exactly like KS3's: its
# questions reach a student inside the assignment payload, never by the page
# reading the table. So unlike the KS3 pools — where student-live.js has ruled
# resolution reads — there is no legitimate frontend mention of this name at
# all, which makes the check a flat prohibition rather than a shape check.
def check_ks4_frontend():
    for rel in _other_surfaces() + [os.path.join("shared", "student-live.js")]:
        path = os.path.join(SITE, rel)
        if not os.path.isfile(path):
            continue
        if KS4_POOL in read(path):
            fail(rel, "references %s — the KS4 assignment pool is served by "
                      "backend composition only, and a page that reads it is "
                      "a page serving from a pool it does not own" % KS4_POOL)


# ── 7 · composition: bankFor() is the only door, and it has two rooms ────
def _uncommented(src, needle):
    """Offsets of `needle` in `src`, skipping lines that only discuss it.

    Same allowance the ladder sweep in check 5 makes: the comments above
    `bankFor` explain the two-table split at length, and explaining a rule is
    not breaking it.
    """
    out = []
    for m in re.finditer(re.escape(needle), src):
        line_start = src.rfind("\n", 0, m.start()) + 1
        line = src[line_start:m.start()]
        if "//" in line or line.strip()[:1] == "*":
            continue
        out.append(m.start())
    return out


def _js_function(src, name):
    """(start, end) of `function name(…) { … }`, brace-matched.

    Not a parser. It is enough for these bodies — plain object literals and
    no template strings carrying braces — and it fails loudly rather than
    quietly if the shape it assumes stops holding.
    """
    m = re.search(r"\b(?:async\s+)?function\s+%s\s*\(" % re.escape(name), src)
    if not m:
        return None
    return _brace_block(src, src.index("{", m.end()), m.start())


def _brace_block(src, open_at, start=None):
    """(start, end) of the `{ … }` beginning at `open_at`, brace-matched.

    `start` widens the span leftwards to include the header that opened the
    block — `function foo(…)`, `if (…)` — so a caller can quote it.
    """
    depth = 0
    for j in range(open_at, len(src)):
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                return (open_at if start is None else start, j + 1)
    return None


# The functions allowed to reach a bank table. ⚠️ AN ALLOWLIST, and adding to
# it is a ruling, not a refactor.
#
# MRB-332's brief named `bankFor` alone. The backend landed the pool with the
# read split in two, because "what could this class be SET?" (by slug, filtered
# by the content rule) and "what IS in this assignment?" (by id, deliberately
# unfiltered — see the comment above `bankRowsByIds`) are different questions
# and were already two code paths at KS3. Both are composition; both take the
# key stage as their first argument and refuse on it before touching anything.
# The contract — one pool per surface, and no call site reaching a table
# without naming a key stage — is unchanged by there being two doors, as long
# as the list of doors is written down. This is that list.
BANK_READERS = ("bankFor", "bankRowsByIds")


def check_ks4_backend():
    server = read(os.path.join(BACKEND, "server.js"))
    compose = read(os.path.join(BACKEND, "assignment-compose.js"))

    live = [("server.js", o) for o in _uncommented(server, KS4_POOL)]
    live += [("assignment-compose.js", o)
             for o in _uncommented(compose, KS4_POOL)]

    if not live:
        note("backend", "the KS4 branch has NOT LANDED yet — no live line in "
                        "server.js or assignment-compose.js names %s. Checks "
                        "6 and 8 are enforced regardless; this one starts "
                        "biting the moment the branch appears, and it is not "
                        "skipped for any other reason." % KS4_POOL)
        return

    # a) ONE PLACE NAMES THE TABLE. MRB-332's brief said "only bankFor may name
    #    it"; the backend went one better and let NO function name it — the
    #    two table names live in a single `BANK_TABLES` map that the key stage
    #    indexes. That is the same rule, harder: a new call site cannot even
    #    type the table, only a key stage.
    tables = re.search(r"const BANK_TABLES\s*=\s*\{.*?\};", compose, re.S)
    if not tables:
        fail("assignment-compose.js",
             "BANK_TABLES is gone — it is the single place either bank is "
             "named, and the thing that stops a call site typing a table "
             "instead of a key stage; re-point this gate at whatever replaced "
             "it")
        return
    if not re.search(r"KS3:\s*'ks3_assignment_bank'", tables.group(0)) or \
       not re.search(r"KS4:\s*'%s'" % KS4_POOL, tables.group(0)):
        fail("assignment-compose.js",
             "BANK_TABLES no longer maps KS3→ks3_assignment_bank and "
             "KS4→%s:\n       %s" % (KS4_POOL, tables.group(0)))
    for name, off in live:
        if name != "assignment-compose.js" or \
           not (tables.start() <= off < tables.end()):
            fail(name, "names %s outside the BANK_TABLES map (offset %d) — "
                       "the KS4 pool is reached through the key stage or not "
                       "at all, so that no call site can read it without "
                       "having said which key stage it is asking on behalf of"
                 % (KS4_POOL, off))

    # b) only the allowlisted composition functions dereference it.
    spans = {}
    for fn in BANK_READERS:
        sp = _js_function(server, fn)
        if not sp:
            fail("server.js", "%s() not found — composition's bank read has "
                              "moved; re-point this gate at it" % fn)
            return
        spans[fn] = sp
    for m in re.finditer(r"BANK_TABLES\.KS4", server):
        if any(a <= m.start() < b for a, b in spans.values()):
            continue
        line_start = server.rfind("\n", 0, m.start()) + 1
        if "//" in server[line_start:m.start()] or \
           "require(" in server[line_start:server.find("\n", m.start())] or \
           re.match(r"\s*BANK_TABLES,", server[line_start:]):
            continue
        fail("server.js", "BANK_TABLES.KS4 is dereferenced outside %s (offset "
                          "%d). Reaching the KS4 assignment pool is composition"
                          "'s job and nobody else's; adding a reader is a "
                          "ruling, not a refactor"
             % (" / ".join("%s()" % f for f in BANK_READERS), m.start()))

    # c) inside each reader: the key stage CHOOSES the table, and neither
    #    branch can reach the other's. Measured by brace-matching the
    #    `keyStage === 'KS4'` block and asserting the two tables' reads fall
    #    on opposite sides of it — not by looking for the words near each
    #    other, which a single unbranched body would also satisfy.
    for fn, (a, b) in spans.items():
        body = server[a:b]
        if "bankRefusalFor" not in body:
            fail("server.js", "%s() no longer refuses on key stage first. The "
                              "refusal is a PRECONDITION of touching a bank "
                              "(MRB-331), not a filter on the result" % fn)
        br = re.search(r"if\s*\(\s*keyStage\s*===\s*'KS4'\s*\)\s*\{", body)
        if not br:
            fail("server.js", "%s() reaches both banks but has no "
                              "`keyStage === 'KS4'` branch — the table is "
                              "being chosen on something other than the key "
                              "stage, or not chosen at all" % fn)
            continue
        blk = _brace_block(body, br.end() - 1)
        if not blk:
            fail("server.js", "%s()'s KS4 branch has unbalanced braces — this "
                              "gate cannot bound it" % fn)
            continue
        lo, hi = blk
        ks4_reads = [m.start() for m in
                     re.finditer(r"\.from\(BANK_TABLES\.KS4\)", body)]
        ks3_reads = [m.start() for m in
                     re.finditer(r"\.from\(BANK_TABLES\.KS3\)", body)]
        if not ks4_reads or not ks3_reads:
            fail("server.js", "%s() does not read both banks (KS4 reads: %d, "
                              "KS3 reads: %d)"
                 % (fn, len(ks4_reads), len(ks3_reads)))
            continue
        outside = [o for o in ks4_reads if not lo <= o < hi]
        if outside:
            fail("server.js", "%s() reads the KS4 bank OUTSIDE its "
                              "`keyStage === 'KS4'` branch (offset(s) %s) — a "
                              "KS3 class can reach the KS4 table"
                 % (fn, outside))
        inside = [o for o in ks3_reads if lo <= o < hi]
        if inside:
            fail("server.js", "%s() reads the KS3 bank INSIDE its "
                              "`keyStage === 'KS4'` branch (offset(s) %s) — "
                              "this is the eight-slug collision, back" % (fn, inside))

        # d) the join column is the structural half of "neither branch can
        #    reach the other's table": KS3's key is `lesson_slug` and the KS4
        #    table has no such column; KS4's is `subtopic_slug` and the KS3
        #    table has no such column. A branch filtering on the other's key
        #    is not reading the table it thinks it is.
        ks4_blk, rest = body[lo:hi], body[:lo] + body[hi:]
        if re.search(r"\.(?:in|eq)\(\s*'lesson_slug'", ks4_blk):
            fail("server.js", "%s()'s KS4 branch filters on lesson_slug — %s "
                              "is joined on subtopic_slug and has no "
                              "lesson_slug column" % (fn, KS4_POOL))
        if re.search(r"\.(?:in|eq)\(\s*'subtopic_slug'", rest):
            fail("server.js", "%s() filters on subtopic_slug outside its KS4 "
                              "branch — ks3_assignment_bank has no such "
                              "column" % fn)
        if ks4_reads and not re.search(
                r"\.(?:in|eq)\(\s*'(?:subtopic_slug|id)'", ks4_blk):
            fail("server.js", "%s()'s KS4 branch reads %s without filtering on "
                              "subtopic_slug or id — it is not joining on the "
                              "KS4 table's key" % (fn, KS4_POOL))

    # e) the KS4 branch must be REACHABLE. Every reader's first line is a
    #    `bankRefusalFor` precondition (MRB-331), which used to answer
    #    'no_ks4_bank' for every key stage but KS3. If that is still true,
    #    everything above is dead code behind an early return — the most
    #    expensive way there is for a gate to pass.
    rm = re.search(r"function bankRefusalFor.*?\n}", compose, re.S)
    if not rm:
        fail("assignment-compose.js",
             "bankRefusalFor() not found, but the readers still guard on it — "
             "re-point this gate at the precondition")
    elif "KS4" not in rm.group(0) and "BANK_KEY_STAGES" not in rm.group(0):
        fail("assignment-compose.js",
             "the readers have a KS4 branch, but bankRefusalFor() still "
             "refuses every key stage but KS3 — the branch is unreachable "
             "dead code behind an early return:\n       %s"
             % rm.group(0).strip())


# ── 8 · ⚠️ the KS4 pools do not share CONTENT ───────────────────────────
#
# THE ONE THAT MATTERS. Checks 1–7 are about which table a line of code names;
# this one is about what a child is actually asked. A KS4 assignment question
# that restates a lesson page's "Test yourself" stem is homework with the
# answers already printed on a page the child can open in one tap, and no name
# check anywhere can see it — the code is correct, the table is right, and the
# question is the same question.
#
# So it is a MEASUREMENT. Every `quiz` stem in the twelve all_subtopics_*.py
# modules, against every `text` in ks4_data.load_pool(), normalised, exact
# match = failure. Near matches are counted and listed as information, because
# a reworded stem is a judgement call a reviewer makes, not one a ratio makes.
_PUNCT = " \t\r\n?.!:;,-–—…'\"’”)"


def _norm_stem(s):
    return re.sub(r"\s+", " ", s).strip().casefold().rstrip(_PUNCT)


def _lesson_quiz_stems():
    """(normalised stem, subtopic id, where) for every KS4 lesson-page quiz.

    The twelve modules overlap heavily by design — a Combined Foundation
    subtopic reappears in the Higher and Triple corpora — so the same stem is
    reached many times. Keyed by normalised text, first provenance wins.
    """
    import importlib
    stems = {}
    for path in sorted(glob.glob(os.path.join(SITE, "all_subtopics_*.py"))):
        name = os.path.basename(path)[:-3]
        mod = importlib.import_module(name)
        const = [k for k in dir(mod) if k.endswith("_SUBTOPICS_ALL")]
        if not const:
            fail(name + ".py", "has no *_SUBTOPICS_ALL dict — the KS4 lesson "
                               "quiz corpus this gate compares against cannot "
                               "be read, so the duplicate check is blind")
            continue
        for topic, subs in sorted(getattr(mod, const[0]).items()):
            for st in subs:
                # ⚠️ THREE KINDS OF PUBLISHED ITEM, NOT ONE (MRB-332).
                #
                # This originally collected `quiz` alone, and that made the
                # gate blind to two thirds of what the lesson page actually
                # prints. A `fifas` entry is a worked example shown WITH ITS
                # FULL SOLUTION; a `matching` block is shown ALREADY PAIRED.
                # Both are published to the same child on the same page, and
                # an assignment question that restates one is homework whose
                # answer is already on the page the child is sent to read.
                #
                # Four cold reviewers found ~90 such collisions between them
                # once they were shown these lists by hand. Collecting them
                # here is what stops the next one needing a human to notice.
                #
                # ⚖️ The TASK/FACT line (docs/ks4/pool-authoring.md §2) rules
                # that a matching PAIR may legitimately be examined where the
                # lesson has published a subtopic's whole core — so pairs are
                # collected into a SEPARATE bucket and reported, never failed.
                # quiz and fifas are TASKS and stay hard failures.
                for q in (st.get("quiz") or []):
                    text = q.get("q")
                    if isinstance(text, str) and text.strip():
                        stems.setdefault(
                            _norm_stem(text),
                            (st.get("id"), "%s %s" % (name, topic), "quiz"))
                for fz in (st.get("fifas") or []):
                    text = (fz.get("q") or fz.get("question")
                            or fz.get("title")) if isinstance(fz, dict) else fz
                    if isinstance(text, str) and text.strip():
                        stems.setdefault(
                            _norm_stem(text),
                            (st.get("id"), "%s %s" % (name, topic), "FIFA"))
    return stems


def _lesson_answers():
    """(subtopic id) -> {normalised correct answer: printed stem}.

    ⚠️ WHY THIS EXISTS, ON TOP OF THE STEM COMPARISON.
    Stem similarity is a STRING measure, so a task that is semantically
    identical but worded differently scores low and passes. Measured in the
    wild by a cold reviewer: "Name the two elements that bronze is made from"
    against the printed "name the two metals mixed together to make bronze"
    scores 0.59 — plainly the same question, comfortably under any threshold
    that is not also full of false positives.

    What those pairs share is not their wording but their ANSWER. So this
    indexes what each published question's correct option actually says, and
    the check below flags a pool question in the same subtopic whose keyed
    answer matches one. Two questions with the same answer in the same
    subtopic are usually the same question wearing different words.

    Reported, never failed: a short answer ("copper and tin") can legitimately
    be the answer to two genuinely different questions, so this needs a human
    eye rather than a build break.
    """
    import importlib
    out = collections.defaultdict(dict)
    for path in sorted(glob.glob(os.path.join(SITE, "all_subtopics_*.py"))):
        name = os.path.basename(path)[:-3]
        mod = importlib.import_module(name)
        const = [k for k in dir(mod) if k.endswith("_SUBTOPICS_ALL")]
        if not const:
            continue
        for _topic, subs in sorted(getattr(mod, const[0]).items()):
            for st in subs:
                sid = st.get("id")
                for q in (st.get("quiz") or []):
                    for o in (q.get("opts") or []):
                        if not isinstance(o, (list, tuple)) or len(o) < 2:
                            continue
                        if o[1] and isinstance(o[0], str) and o[0].strip():
                            out[sid].setdefault(_norm_stem(o[0]),
                                                q.get("q") or "")
    return out


def _lesson_matching_pairs():
    """(normalised pair text, subtopic id, where) for every matching block.

    Reported, never failed — see the TASK/FACT ruling above. A pair is a FACT
    the page publishes, and where the matching block IS the spec point,
    examining it is correct; inventing an off-spec question to dodge it is the
    worse defect. One reviewer proved that by reverting six of its own
    rewrites once the line was drawn.
    """
    import importlib
    pairs = {}
    for path in sorted(glob.glob(os.path.join(SITE, "all_subtopics_*.py"))):
        name = os.path.basename(path)[:-3]
        mod = importlib.import_module(name)
        const = [k for k in dir(mod) if k.endswith("_SUBTOPICS_ALL")]
        if not const:
            continue
        for topic, subs in sorted(getattr(mod, const[0]).items()):
            for st in subs:
                m = st.get("matching") or {}
                if not isinstance(m, dict):
                    continue
                for pair in (m.get("pairs") or []):
                    try:
                        a, b = pair[0], pair[1]
                    except (TypeError, IndexError, KeyError):
                        continue
                    if not isinstance(b, str) or not b.strip():
                        continue
                    pairs.setdefault(
                        _norm_stem("%s %s" % (a, b)),
                        (st.get("id"), "%s %s" % (name, topic)))
    return pairs


def check_ks4_pool_collision():
    try:
        import ks4_data
        # strict=False: 264 subtopics are authored by many hands and a
        # part-written pool must still be measurable. Completeness is the
        # export's gate, not this one's.
        pool = ks4_data.load_pool(strict=False)
    except SystemExit as exc:
        fail("ks4_data", "the pool does not load, so its content cannot be "
                         "compared against the lesson pages:\n       %s"
             % str(exc).replace("\n", "\n       "))
        return
    except Exception as exc:                       # noqa: BLE001 — reported
        fail("ks4_data", "the pool could not be loaded (%s: %s)"
             % (type(exc).__name__, exc))
        return

    lesson = _lesson_quiz_stems()
    if not lesson:
        return                                     # already failed above

    if not pool:
        note("ks4_data", "the KS4 assignment pool is EMPTY — nothing to "
                         "compare against the %d lesson-page stems yet. The "
                         "check is not skipped for any other reason: one "
                         "authored question is enough to make it measure."
             % len(lesson))
        return

    # exact collisions — a failure, named by both sides
    hits = []
    for row in pool:
        norm = _norm_stem(row["text"])
        if norm in lesson:
            sid, where, kind = lesson[norm]
            hits.append("%s (%s) == lesson %s on %s [%s]"
                        % (row["id"], row["subtopic_slug"], kind, sid, where))
    if hits:
        fail("ks4_data vs all_subtopics_*", (
            "%d assignment question(s) restate a TASK the lesson page already "
            "publishes with its answer — a 'Test yourself' stem or a worked "
            "FIFA example. That page is one tap away from the student sitting "
            "the homework, so this hands over the answer in advance:"
            "\n       · %s") % (len(hits), "\n       · ".join(hits[:40])))

    # ── matching pairs: REPORTED, never failed ─────────────────────────
    #
    # The TASK/FACT ruling (docs/ks4/pool-authoring.md §2). A pair is a fact
    # the page publishes, not a task, and in the saturated subtopics the
    # matching block IS the spec point — `properties-of-waves` pairs all five
    # wave quantities with their definitions, which is the whole of 6.6.1.2.
    # Failing on those would force off-spec questions, which is the worse
    # defect and was measured happening: one reviewer reverted six of its own
    # rewrites once the line was drawn.
    #
    # So this counts them and names the saturated subtopics, because a
    # subtopic whose entire core is published is a LESSON-PAGE finding worth
    # Mide's eye — not a question defect to fix in the pool.
    # ⚠️ MEASURED ON THE ANSWER HALF, NOT ON THE WHOLE PAIR.
    #
    # The first version of this compared a question's STEM against the
    # concatenated pair ("elastic potential | a compressed spring") and could
    # therefore never match anything — a check that always passes, which is
    # worse than no check, because it reads as coverage. (That is the same
    # trap documented in docs/ks4/merge-notes.md §2, met from the other side.)
    #
    # What a pairing actually leaks is its ANSWER half: the page prints
    # "Elastic potential ↔ a compressed spring", and the question that leans
    # on it has "a compressed spring" in the stem and "elastic potential" as
    # the correct option. So the comparison is the pair's two halves against
    # the question's stem AND its keyed option, on a similarity threshold.
    pairs = _lesson_matching_pairs()
    paired = collections.Counter()
    for row in pool:
        blob = _norm_stem("%s %s" % (row["text"],
                                     row["options"][row["correct_index"]]))
        words = set(re.findall(r"[a-z]{4,}", blob))
        if not words:
            continue
        for pnorm in pairs:
            pw = set(re.findall(r"[a-z]{4,}", pnorm))
            if not pw:
                continue
            # both halves of the pair substantially present in the question
            if len(pw & words) >= max(2, int(0.75 * len(pw))):
                paired[row["subtopic_slug"]] += 1
                break
    if paired:
        note("ks4_data vs matching blocks",
             "%d question(s) across %d subtopic(s) examine a fact the lesson "
             "page prints already paired. ALLOWED by the TASK/FACT ruling — "
             "reported so a saturated subtopic stays visible.\n       "
             "Worst: %s"
             % (sum(paired.values()), len(paired),
                ", ".join("%s %d" % kv for kv in paired.most_common(8))))

    # ── same subtopic, same keyed answer: the semantic-duplicate channel ──
    answers = _lesson_answers()
    same_answer = []
    for row in pool:
        printed = answers.get(row["subtopic_slug"])
        if not printed:
            continue
        key = _norm_stem(row["options"][row["correct_index"]])
        if key in printed:
            same_answer.append(
                "%s (%s) keys the same answer as a printed quiz question "
                "on the same page" % (row["id"], row["subtopic_slug"]))
    if same_answer:
        note("ks4_data vs all_subtopics_* (same answer)",
             "%d assignment question(s) key an answer identical to a "
             "published question's answer, in the SAME subtopic. Stem "
             "similarity does not catch these — a reworded task scores low. "
             "A reviewer's call, not a failure:\n       · %s"
             % (len(same_answer), "\n       · ".join(same_answer[:20])))

    # near-duplicates — information only. An inverted word index keeps this
    # linear-ish: comparing 3,168 pool stems against 2,434 lesson stems pair
    # by pair is 7.7M ratios and turns a fast gate into a slow one.
    index = collections.defaultdict(list)
    keys = list(lesson)
    for i, norm in enumerate(keys):
        for w in set(re.findall(r"[a-z]{4,}", norm)):
            index[w].append(i)
    near = []
    for row in pool:
        norm = _norm_stem(row["text"])
        if norm in lesson:
            continue                               # already a failure
        words = set(re.findall(r"[a-z]{4,}", norm))
        if not words:
            continue
        shared = collections.Counter()
        for w in words:
            shared.update(index.get(w, ()))
        floor = max(3, int(0.4 * len(words)))
        best, best_i = 0.0, None
        for i, n in shared.items():
            if n < floor:
                continue
            r = difflib.SequenceMatcher(None, norm, keys[i]).ratio()
            if r > best:
                best, best_i = r, i
        if best >= NEAR_DUPLICATE_RATIO:
            sid, where, kind = lesson[keys[best_i]]
            near.append("%.2f  %s (%s) ~ lesson %s on %s [%s]"
                        % (best, row["id"], row["subtopic_slug"], kind, sid,
                           where))
    if near:
        note("ks4_data vs all_subtopics_*",
             "%d assignment stem(s) are %.0f%%+ similar to a lesson-page stem "
             "without being identical. Not a failure — a reviewer's call. "
             "Nearest first:\n       · %s"
             % (len(near), 100 * NEAR_DUPLICATE_RATIO,
                "\n       · ".join(sorted(near, reverse=True)[:20])))
    elif not hits:
        note("ks4_data vs all_subtopics_*",
             "%d authored assignment stem(s) measured against %d distinct "
             "lesson-page stems: no exact matches, no near-duplicates at "
             "%.0f%%." % (len(pool), len(lesson), 100 * NEAR_DUPLICATE_RATIO))


def main():
    check_student_live()
    check_lesson_ladder()
    check_other_surfaces()
    check_constraint_migration()
    check_backend()
    check_ks4_frontend()
    check_ks4_backend()
    check_ks4_pool_collision()

    def show_notes():
        for n in notes:
            print("   ℹ️  %s" % n)
        if notes:
            print()

    if failures:
        print("❌ pool_ownership: %d failure(s)\n" % len(failures))
        for f in failures:
            print("   · %s" % f)
        print()
        show_notes()
        return 1

    print("✅ pool_ownership: one bank per surface")
    print("   KS3 ladder page  ← authored ladder (ks3_data, baked at build)")
    print("   KS3 assignment   ← ks3_assignment_bank (backend composition only)")
    print("   KS3 flashcards   ← ks3_cards (class page, one serving read)")
    print("   KS4 lesson page  ← all_subtopics_*.py `quiz` (baked at build, "
          "no runtime read)")
    print("   KS4 assignment   ← ks4_assignment_bank / ks4_data (backend "
          "composition only)")
    print("   FROZEN MRB-288: the practice round serves recall+apply from "
          "ks3_ladder_questions\n   (student-live.js + /api/class/practice) "
          "— bounded to one serving read each,\n   awaiting Mide's ruling.")
    print()
    show_notes()
    return 0


if __name__ == "__main__":
    sys.exit(main())
