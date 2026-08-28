"""gate_registry.py — THE list of gates. One place, so a gate cannot be orphaned.

    "The gate was working; it was not run."
        — ks3_data/c7/questions_03_endothermic_reactions.py, on the defect
          that reached `main` in PR #8

⊕ MRB-277, 21 Aug 2026.

── WHY THIS FILE EXISTS ────────────────────────────────────────────────

`verify_questions.py` was written under MRB-269, works correctly, and was
referenced by NOTHING. Not by `verify_ks3.py`, not by a shell script, not by
a hook, not by CI. Grep the repo before this file existed and the only hits
are its own source, one comment in `ks3_data/c7/`, and two lines of prose in
`docs/`. It could only ever run if a human remembered it by name.

On 21 Aug 2026 nobody did, and `c7-03-e04` — a bank question restating its
apply rung verbatim, which `verify_questions` check 6 refuses — shipped to
`main` in PR #8. The run that shipped it reported "verify_ks3.py exit 0, all
automated gates" and that sentence was TRUE. The gate simply was not inside
the umbrella the sentence described.

So the defect was never "somebody ignored a red gate". It was that the set of
gates existed only in people's heads, and a set that exists only in heads
loses a member silently. This file is that set, written down, and
`prepush_gate.py` refuses a push against it.

── THE RULE FOR ADDING A GATE ──────────────────────────────────────────

A new gate script is not finished until it has a row here. A row costs one
line; the absence of one cost a defect on production and two runs to find it
by accident.

`speed`:
    "fast"  — no browser, runs in seconds. `prepush_gate.py` RUNS these
              itself on every push, so they can never be skipped.
    "slow"  — drives headless Chrome, takes minutes. Running these inside a
              hook would make the hook intolerable and an intolerable hook
              gets disabled, which is how a gate stops watching. Instead the
              guard requires a RECEIPT proving the gate passed against the
              exact tree being pushed. That turns "did you run it?" from a
              question of memory into a checkable fact.

`needs`:
    An optional path that must exist for the gate to be meaningful. A gate
    whose precondition is absent is reported as SKIPPED, by name, with the
    reason — never silently, and never as a pass.

`needs_env`:
    The same idea for a credential. `export_ks3_questions.py --verify` reads
    production over the network and cannot run without a password; the guard
    reports it as SKIPPED BY NAME rather than letting the gate decide for
    itself to exit 0 having measured nothing.

── ⊕ MRB-282, 23 Aug 2026 · THE REGISTRY COULD ITSELF LOSE A MEMBER ────

The paragraphs above describe a set that cannot silently lose a gate. Two days
later it had lost four: `ks3_key_audit`, `ks3_rail_manifest`,
`ks3_instrument_liveness` and `ks3_statutory` all existed, all worked, and
none had a row. It was not hypothetical — `ks3_rail_manifest` was RED on
`origin/main` when the chemistry lane merged, because `c8-07` had been checked
in without its manifest row and the guard does not run a gate it has never
heard of.

That is the SAME defect one level up. A hand-maintained list that nothing
compares against reality is a list that drifts, whether it lists gates or
lists lessons — and the previous version of this file said exactly that about
`verify_questions` in its own opening quotation.

So the list is now CHECKED. `EXCLUDED` below names every other executable
script in the repo root and says why it is not a gate, and `coverage()`
asserts that the two sets together account for all of them. A new script is a
red gate until somebody classifies it:

    python3 gate_registry.py --check

which is itself registered as the `gate_coverage` gate, so the assertion runs
on every push. A registry that can silently omit a member has the same shape
as the problem it was built to solve; this is the fix for the shape, not for
the four instances of it.
"""

GATES = [
    dict(name="verify_questions",
         cmd=["python3", "verify_questions.py"],
         speed="fast",
         why="the KS3 question bank (MRB-269) — nine checks over every "
             "lesson's ladder and bank. THE ORPHAN: this is the gate that "
             "was red at push time in PR #8 and was not run."),

    dict(name="ks3_smoke_static",
         cmd=["python3", "ks3_smoke.py", "--static"],
         speed="fast",
         why="garbage strings in the built key stage — unsubstituted "
             "placeholders, stray markup, `undefined` reaching a page."),

    dict(name="answer_positions",
         cmd=["python3", "verify_answer_positions.py"],
         speed="fast",
         why="MRB-278 made permanent and cross-key-stage: no fixed-position "
             "MCQ corpus — KS3 authored (served verbatim) or KS4 built "
             "(served post-shuffle) — lets one option position hold more "
             "than half the answers or never be the answer. KS3's bank once "
             "never landed on D; nothing watched KS4 until this row."),

    dict(name="3d_isolation",
         cmd=["python3", "3d_isolation_check.py"],
         speed="fast",
         needs="3d-studio/dist",
         why="spec §10 / MRB-194 — the published studio survives a generator "
             "run. Needs a build to publish; skipped, by name, without one."),

    dict(name="verify_ks3",
         cmd=["python3", "verify_ks3.py"],
         speed="slow",
         why="the §9 slice gates — the umbrella. Rebuilds the key stage and "
             "drives every lesson in headless Chrome."),

    dict(name="student_parity",
         cmd=["python3", "student_parity.py"],
         speed="slow",
         needs="student_parity.py",
         why="the generated student previews against Design's own file, "
             "layers A-H at 360/390/820/1460."),

    dict(name="student_behaviour",
         cmd=["python3", "student_behaviour.py"],
         speed="slow",
         needs="student_behaviour.py",
         why="the ported student pages driven against Design's own — 30 "
             "drives, visible text identical."),

    dict(name="student_themes",
         cmd=["python3", "student_themes.py"],
         speed="slow",
         needs="mrbadmus_site/student/class-fixture.html",
         why="the ported class page's COLOUR — six bench themes plus the "
             "attribute absent, grounds, tokens and every contrast ratio "
             "against the AA floor. The only gate that watches the port's "
             "palette: parity drives the PREVIEW pair and behaviour compares "
             "text, so a colour change ships unwatched without this."),

    # ── ⊕ MRB-287 · the teacher dashboard port ─────────────────────────

    dict(name="teacher_tells",
         cmd=["python3", "teacher_tells.py"],
         speed="fast",
         needs="teacher/insights.html",
         why="Design's invented school must not reach a teacher. The teacher "
             "delivery is a SAMPLE — twelve classes, fifty-four students and "
             "a score for every one of them, all FNV-seeded and all "
             "PLAUSIBLE, which is what makes it dangerous: a teacher cannot "
             "tell by looking. Checks the built LIVE pages (never the "
             "fixtures, which are supposed to carry Design's values) for any "
             "sample identity, any surviving literal count, and for `rnd(` "
             "— the wrapper whose only use is to make a value up. `seed(` is "
             "allowed for hueFor's avatar colour and nothing else, because "
             "the live product already hashes a name to a colour the same "
             "way (shoutouts.js getStudentColour); banning it outright would "
             "have forced the port to re-implement the identical hash under "
             "another name to pass a gate. Its corpus is "
             "DERIVED from the delivery on every run rather than typed, "
             "because the hand-written ancestor of that list in "
             "student_page_drive.py records what a typed one costs: 'THIS "
             "LIST WAS TOO SHORT AND THE DRIVE PASSED BECAUSE OF IT.' "
             "⚠️ `needs` names insights.html — a page that exists only once "
             "the port has run — so this SKIPS BY NAME until then rather "
             "than failing on three pages nobody has built yet."),

    dict(name="teacher_behaviour",
         cmd=["python3", "teacher_behaviour.py"],
         speed="slow",
         # ⚠️ `teacher_fixtures/`, NOT `teacher/`. The fixtures moved out of
         # the published directory (they render Design's invented school and
         # /teacher/* has no edge auth). This row kept the old path for one
         # commit and the gate SKIPPED — by name, which is how it was caught,
         # and exactly the "a gate stopped watching" failure this file exists
         # to prevent. A `needs` path is part of the move.
         needs="teacher_fixtures/classes-fixture.html",
         why="the ported teacher pages, DRIVEN — the teacher-side twin of "
             "ks3_instrument_liveness, and the only teacher gate that presses "
             "the buttons. teacher_tells reads the built bytes and would pass "
             "on a page that is blank; this one asserts every screen mounts, "
             "every binding resolves, every control moves something, no "
             "computed value (null%, NaN, -Infinity) reaches the copy, and "
             "the console stays quiet — on load AND after a reload. Fourteen "
             "fixtures: seven screens x {populated, EMPTY}, because empty "
             "states are the half of the product that ships broken and the "
             "empty half found two crashes on its first run. ⚠️ It drives the "
             "FIXTURES, not the live pages: a live teacher page starts with "
             "requireTeacherRole, so driving one needs a credential and a "
             "waking Render — the same reason student_page_drive and "
             "student_controls_drive are EXCLUDED. It therefore proves "
             "everything between the data arriving and the pixels, and "
             "nothing about whether the seam returned the right rows."),

    # ── ⊕ MRB-288 · one bank per surface ────────────────────────────────

    dict(name="pool_ownership",
         cmd=["python3", "pool_ownership.py"],
         speed="fast",
         needs="/Users/midebadmus/Documents/GitHub/mrbadmus---backend/server.js",
         why="Mide's 24 Aug 2026 ruling: three question pools, one per "
             "surface, and no surface SERVES from a pool it does not own. "
             "Composition fed assignments from BOTH the ladder and the bank "
             "before this existed — verified in the production rows, not "
             "inferred. Asserts composition reads ks3_assignment_bank and "
             "nothing else, the lesson ladder stays baked from ks3_data, the "
             "flashcard deck serves from ks3_cards alone, the composed row "
             "shape is {band, rung: null}, and the ONE frozen exception (the "
             "practice round serving recall+apply from ks3_ladder_questions, "
             "awaiting Mide's ruling) stays bounded to exactly one serving "
             "read per layer. Distinguishes SERVING from ref→lesson "
             "resolution and from reading attempt history — the FROM YOUR "
             "WORK targeting is pedagogy, not a cross-feed. `needs` the "
             "backend checkout because composition lives there; on a machine "
             "without it the gate SKIPS BY NAME rather than asserting half "
             "the contract."),

    # ── ⊕ MRB-290 · the KS4 weekly leaderboard port ─────────────────────

    dict(name="leaderboard_tells",
         cmd=["python3", "leaderboard_tells.py"],
         speed="fast",
         why="no student Design invented reaches the live leaderboard. The "
             "corpus is DERIVED from the vendored delivery on every run — "
             "FIRST, LAST and VIEWER parsed out of its own source and "
             "Design's roster formula re-run — because a typed list is how "
             "student_page_drive passed while covering nothing. It pins the "
             "61 EXACT handles rather than their shape: real usernames come "
             "from the same generator vocabulary (FoxWave36 is a real "
             "student, FoxWave21 is Design's), so a shape match would fire "
             "on every real student on the board. Also asserts the "
             "fabricators are gone, that no unbound 'AY' monogram survives, "
             "and that hash/rng have exactly two callers each — the "
             "declaration and Design's confetti."),

    dict(name="leaderboard_seam",
         cmd=["python3", "leaderboard_seam.py"],
         speed="fast",
         needs="shared/leaderboard-live.js",
         why="the leaderboard's DATA LAYER, driven directly — 31 checks "
             "against the real shared/leaderboard-live.js under Node with a "
             "stubbed fetch and a stubbed Supabase client. ⚑ IT EXISTS "
             "BECAUSE leaderboard_behaviour CANNOT REACH ANY OF THIS: all "
             "eight of its fixtures replace the seam wholesale, which is "
             "what lets them run with no network and no credential, so not "
             "one line of load(), boot(), mapRow() or safeAvatar() was "
             "executed by any gate. Covers the warm-up ping, the "
             "error-key refetch (an error is the absence of an answer, not a "
             "cached one), cache honouring, the row mapping including R21's "
             "done-intersect-per guard against the literal 'null%' reaching "
             "the copy, move null-vs-0 (NEW vs HELD), R25's reject-never-"
             "escape URL rule, the profile-tier landing, the signed-out path "
             "and the server-anchored clock. Mutation-tested: reverting each "
             "of four behaviours turns it red. Skips BY NAME where node is "
             "absent — such a machine cannot run build_leaderboard_port.py "
             "either, so there is no built page for it to be silent about. "
             "⚠️ fetch is stubbed: this proves the data layer maps and "
             "caches correctly and NOTHING about the live endpoint's "
             "contract."),

    dict(name="leaderboard_behaviour",
         cmd=["python3", "leaderboard_behaviour.py"],
         speed="slow",
         why="TEN leaderboard fixtures driven headless, on load and again "
             "after a reload: every control pressed (tier, four subjects, "
             "the week rail's prev/next/This week and every chip, every row "
             "expand), no press leaves the page blank, no computed value "
             "reaches the copy — checked as substrings AND word-bounded, "
             "because the live page's 'TOP 10 ONLY · null SAT THIS "
             "WEEK' was a bare `null` that no substring in the list matched "
             "— at most ONE 'YOU' chip renders anywhere, and the console "
             "stays quiet, and the week rail FOLLOWS the selection (R33) "
             "without yanking a redraw that did not move it. Seven of the "
             "ten are states Design never drew: an empty week (the LIVE "
             "state of Higher/Overall on 25 Aug 2026), one entrant, week "
             "one, a viewer below the cut, a failed fetch, LOADING — the "
             "seconds-long cold-Render window that held two student-visible "
             "defects (R30) precisely because every other fixture starts "
             "from a settled payload — and a viewer ON THE PODIUM, the "
             "state Mide was in when he found that Design's YOU chip stops "
             "at rank 4 (R32). Plus the avatar fixture holding R25's "
             "never-both property. YOU chips are counted EXACTLY, not "
             "merely capped: a missing marker passes any at-most-one check. "
             "⚠️ FIXTURE-DRIVEN: the live page "
             "needs a Supabase session and a warm Render dyno, so this "
             "proves everything between the data arriving and the pixels "
             "and nothing about whether the seam asks for the right rows."),

    # ── ⊕ MRB-282 · THE FOUR THAT WERE OUTSIDE THE REGISTRY ────────────

    dict(name="gate_coverage",
         cmd=["python3", "gate_registry.py", "--check"],
         speed="fast",
         why="the registry against the repo — every executable script at the "
             "root is a gate here or an entry in EXCLUDED with a reason. "
             "Without this the registry is a hand-maintained list nothing "
             "checks, which is the defect it exists to stop."),

    dict(name="ks3_statutory",
         cmd=["python3", "ks3_statutory.py", "--check-only"],
         speed="fast",
         why="the 155 statutory statements, and docs/ks3/statutory-register.md "
             "against the module that renders it. --check-only IS REQUIRED: a "
             "bare run used to REWRITE the register, which destroyed MRB-232's "
             "KS3.B.NUT.02 ruling while reporting PASS, and would dirty the "
             "tree the guard is checking."),

    dict(name="ks3_key_audit",
         cmd=["python3", "ks3_key_audit.py"],
         speed="fast",
         why="every authored data key against the code that reads it. An "
             "authored key nothing reads is teaching that was written and "
             "never rendered — invisible in a screenshot, because what is "
             "missing does not draw."),

    dict(name="ks3_rail_manifest",
         cmd=["python3", "ks3_rail_manifest.py"],
         speed="fast",
         why="the rail Design DREW against the rail the manifest records. "
             "THIS ONE HAS ALREADY FIRED: it was red on origin/main when the "
             "chemistry lane merged c8-07 without a manifest row, and nothing "
             "caught it because the guard did not run it. A bare run checks; "
             "only --write writes."),

    dict(name="ks3_instrument_liveness",
         cmd=["python3", "ks3_instrument_liveness.py"],
         speed="slow",
         why="the only gate that PRESSES THE BUTTONS. Every other KS3 gate "
             "measures the page at rest, so a dead instrument passes parity, "
             "overflow and contrast and does nothing when a student touches "
             "it."),

    # ── ⊕ MRB-282 · found by the sweep that added the four above ────────

    dict(name="student_switches",
         cmd=["python3", "student_switches.py", "--check"],
         speed="slow",
         needs="student_switches.json",
         why="Design's discrete breakpoint switches, measured in a browser "
             "against the recorded table. --check IS REQUIRED: a bare run "
             "OVERWRITES student_switches.json, which is tracked, so the "
             "gate would adopt the drift it is supposed to report."),

    dict(name="student_controls_drive",
         cmd=["python3", "student_controls_drive.py"],
         speed="slow",
         needs_env=("MRB_DRIVE_PASSWORD", "MRB_TEST_STUDENT_PASSWORD"),
         why="presses every control on the student pages and fails on one "
             "that does nothing. The student-side twin of "
             "ks3_instrument_liveness. Signs in to production, so it is "
             "SKIPPED BY NAME without a credential. ⚠️ Its --fixture mode "
             "needs none and is NOT what this row runs: the file's own header "
             "says the whole EXPECT table is invalid under it, and "
             "registering the weaker sweep as though it were the real one is "
             "the overstated-scope defect this registry exists to stop."),

    dict(name="export_ks3_questions_verify",
         cmd=["python3", "export_ks3_questions.py", "--verify"],
         speed="fast",
         needs_env="MRB_TEST_STUDENT_PASSWORD",
         why="the KS3 question mirror in Postgres against these files. The "
             "only check that the tables a student is actually served still "
             "match the authored questions. Reads production over the "
             "network, so it needs a password and is SKIPPED BY NAME without "
             "one."),

    dict(name="3d_parity",
         cmd=["python3", "3d_parity.py"],
         speed="slow",
         needs="3d-studio/dist",
         why="the studio shell against Design's screens (MRB-186). Needs a "
             "built studio; skipped, by name, without one."),

    dict(name="3d_render_check",
         cmd=["python3", "3d_render_check.py"],
         speed="slow",
         needs="3d-studio/dist",
         why="the mesh renderer in a real browser (MRB-187) — including that "
             "a missing GLB routes to the flat stage. Needs a built studio."),
]


# ── EVERYTHING ELSE AT THE REPO ROOT, AND WHY IT IS NOT A GATE ──────────
#
# One row per executable script that is NOT in GATES. A REASON, not a
# category: "it is a generator, and writing is the job" is a reason; "not a
# gate" is not.
#
# `coverage()` asserts GATES + EXCLUDED account for every *.py and *.sh at the
# repo root, so a new script cannot be quietly neither.

EXCLUDED = {
    # ── generators · they WRITE the site, by design ─────────────────────
    "build_all.py":
        "the entry point — runs the four generators in their load-bearing "
        "order. Writing is the job.",
    "build_ks3.py":
        "the KS3 generator. Its output is what the gates measure.",
    "build_student.py":
        "the student PREVIEW generator, gated by student_parity.",
    "build_student_port.py":
        "the LIVE student page generator, gated by student_behaviour.",
    "build_teacher_port.py":
        "the LIVE teacher page generator, gated by teacher_behaviour.",
    "build_leaderboard_port.py":
        "the LIVE KS4 leaderboard generator, gated by leaderboard_tells "
        "(fast) and leaderboard_behaviour (slow).",
    "generate_site_v5.py":
        "the KS4 generator.",
    "ks3_seed_sow.py":
        "a GENERATOR of two tracked seed files (supabase/seeds/"
        "*_ks3_default_sequence.sql and *_ks3_school_schemes.sql), which it "
        "rewrites whole on every successful run with no check mode — the "
        "same shape as the ks3_statutory defect MRB-282 fixed. NOT "
        "registered and NOT fixed here on purpose: the 183 -> 185 "
        "scheme_of_work rewrite is parked by Mide, and giving this a "
        "--check-only would turn a parked disagreement into a red gate.",

    # ── MRB-223 · P1's port harnesses ───────────────────────────────────
    #
    # ⚠️ THESE ASSERT, AND THEY ARE STILL EXCLUDED. The registry's rule is
    # "a gate if it asserts something, EXCLUDED with a reason if not", and
    # the honest answer here is a third thing: they assert, they pass, and
    # they are scoped to ONE unit and need a headless browser. Registering
    # them would run a P1-only Chrome sweep on every push from every lane
    # for the rest of the repo's life, which is a cost the whole team pays
    # for one unit's port.
    #
    # ⊕ WORTH GENERALISING, THOUGH, AND THAT IS A RECOMMENDATION RATHER THAN
    # A CHANGE. `p1_complete.py` caught something all seventeen registered
    # gates missed: eight instruments that called `setCount` and never
    # `markStage`, so every control worked and no rail stop could ever tick.
    # MRB-208's R2 gate passed them because it reads the BYTES — the page
    # DECLARES a `done_when` and ships `data-stage-done="0"`, and nothing
    # static is wrong with a page whose JS never fires. A key-stage-wide
    # version of "drive each instrument and assert its stop actually ticks"
    # would close that, and it is Mide's call whether the runtime is worth
    # it.
    "p1_drive.py":
        "P1's control sweep — presses every control on all eight pages and "
        "asserts each changes its own section. Run 1's design, re-pointed. "
        "Unit-scoped and needs Chrome; see the note above.",
    "p1_complete.py":
        "P1's completion drive — drives each instrument as a student would "
        "and asserts its rail stop ticks AND was not ticked beforehand. "
        "Unit-scoped and needs Chrome; see the note above.",
    "phase3_audit.py":
        "MRB-223's Phase 3 second pass — twelve checks of the BUILT P1 "
        "pages against Design's delivered `.dc.html`. Unit-scoped: it names "
        "eight slugs and one design-reference folder, so it asserts nothing "
        "about the other twenty units.",

    # ── libraries · imported, never the thing you run ───────────────────
    # gate_registry.py is NOT here: it is the `gate_coverage` gate above, and
    # a script cannot be both — coverage() reports that as a contradiction.
    "prepush_gate.py":
        "the guard that RUNS the registry. Gating the guard with the guard "
        "is the same circularity.",
    "ks3_browser.py":
        "the headless-Chrome harness every driven gate is built on. A "
        "library with no assertions of its own.",
    "ks3_parity.py":
        "the MRB-183 parity assertions. Imported and run by verify_ks3 "
        "(verify_ks3.py:1366), which IS registered.",
    "student_rulings.py":
        "Mide's MRB-275 rulings as source. Data, consumed by "
        "build_student_port.",
    "teacher_rulings.py":
        "Mide's MRB-287 rulings as source. Data, consumed by "
        "build_teacher_port.",
    "student_template.py":
        "Design's template, compiled. A library consumed by "
        "build_student_port.",

    # ── run INSIDE verify_ks3, which is registered ──────────────────────
    "ks3_canvas.py":
        "does the canvas redraw when you touch it — invoked by verify_ks3 "
        "(verify_ks3.py:2158). A second row would run it twice.",
    "ks3_figure_sweep.py":
        "every drawn figure at three widths — invoked by verify_ks3 "
        "(verify_ks3.py:432).",
    "ks3_overflow.py":
        "the 390px sideways-scroll gate — invoked by verify_ks3 "
        "(verify_ks3.py:2175).",

    # ── diagnostics · they REPORT, and a human reads the report ─────────
    "ks3_mutation.py":
        "source-level mutation testing of the parity assertions. Its "
        "valuable output is the supplying-selector column a human reads, it "
        "defaults to one unit (B3), and a full sweep is hours. Run it by "
        "hand when a parity row is suspect.",
    "student_diff.py":
        "what changes for a student between two built KS3 trees. A "
        "comparison tool with no correct answer to assert.",
    "student_shots.py":
        "photographs the wired student pages so a human can look. Produces "
        "images, asserts nothing.",
    "student_theme_shots.py":
        "photographs the six bench themes for the same reason. The "
        "assertions about those colours live in student_themes, which IS "
        "registered.",
    "audit_content.py":
        "the KS4 Phase 1 content audit. Rewrites 15 tracked files under "
        "docs/audit/ on every run, has no pass/fail verdict, and covers the "
        "KS4 subtopic data rather than anything KS3.",

    # ── they rewrite tracked source, on purpose ─────────────────────────
    "ks3_prose_swap.py":
        "an APPLY tool: it edits the authored .py source, rebuilds, checks "
        "the page moved, and reverts if it did not. Running it as a gate "
        "would rewrite the tree the gate is measuring.",
    "splice_instruments.py":
        "disarmed. Kept only as the record of what ks3_art/ replaced.",
    "bonding_redesign.py":
        "a one-off KS4 theory-block decomposition (MRB-113 Phase B).",

    # ── they drive PRODUCTION, with real credentials ────────────────────
    "student_api_drive.py":
        "drives the weekly assignment producer against PRODUCTION as a real "
        "student. Needs credentials and the network; a push must not depend "
        "on Render being awake.",
    "student_page_drive.py":
        "drives the wired student pages against production data. Same "
        "reason.",
    "teacher_landing_drive.py":
        "drives the teacher landing as three real signed-in teachers against "
        "the TEST project, to prove MRB-293's self-filter: a teacher holding "
        "a school-wide read scope sees only their OWN classes, and a "
        "CO-TAUGHT class still shows for BOTH its teachers. Needs the "
        "network, real sign-ins and a browser; a push must not depend on "
        "any of the three.",
    "student_submit_drive.py":
        "drives POST /api/assignment-submit against production. Same "
        "reason, and it WRITES rows.",
    "check_ks3_live.sh":
        "verifies mrbadmus.com AFTER a push, including the cache-bust "
        "stamps. It cannot run before the thing it checks exists.",
    "check_b1_live.sh":
        "the same, for B1's lessons.",
    "check_ks4_live.sh":
        "verifies mrbadmus.com's KS4 and root pages AFTER a push, including "
        "the cache-bust stamps (MRB-290). It cannot run before the thing it "
        "checks exists.",
}

# The KS4 subtopic corpora are DATA, not scripts: one module each of AQA spec
# content, imported by generate_site_v5. Listed as a prefix rather than as
# twelve near-identical rows.
EXCLUDED_PREFIXES = {
    "all_subtopics_":
        "AQA KS4 subtopic content data, imported by generate_site_v5. No "
        "entry point; the audit of this content is audit_content.py, and "
        "the served answer-position property over what these build into is "
        "asserted by the answer_positions gate. (The authored files are "
        "deliberately 100%% index-0 — the build-time shuffle is what a "
        "student sees, which is why the gate measures the built tree.)",
}


def gate_scripts():
    """Every repo-root script that a GATES row actually invokes."""
    out = {}
    for g in GATES:
        for token in g["cmd"]:
            if token.endswith(".py") or token.endswith(".sh"):
                out.setdefault(token, []).append(g["name"])
    return out


def coverage(root="."):
    """Problems, as strings. Empty means every root script is accounted for."""
    import os
    problems = []
    gated = gate_scripts()

    present = sorted(f for f in os.listdir(root)
                     if (f.endswith(".py") or f.endswith(".sh"))
                     and os.path.isfile(os.path.join(root, f)))

    for f in present:
        if f in gated or f in EXCLUDED:
            continue
        if any(f.startswith(p) for p in EXCLUDED_PREFIXES):
            continue
        problems.append(
            "%s is neither a gate nor excluded. Add a row to GATES if it "
            "asserts something, or a row to EXCLUDED saying WHY it does not "
            "\u2014 a script that is quietly neither is how verify_questions "
            "spent weeks outside the set." % f)

    # The other direction: a row naming a file that is gone is a row nobody
    # will notice has stopped meaning anything.
    have = set(present)
    for f in sorted(gated):
        if f not in have:
            problems.append(
                "GATES row(s) %s invoke %s, which does not exist at the repo "
                "root." % (", ".join(gated[f]), f))
    for f in sorted(EXCLUDED):
        if f not in have:
            problems.append(
                "EXCLUDED names %s, which no longer exists. Delete the row so "
                "the list stays a description of the repo." % f)
    for pre in sorted(EXCLUDED_PREFIXES):
        if not any(f.startswith(pre) for f in have):
            problems.append(
                "EXCLUDED_PREFIXES names %s*, which now matches nothing." % pre)

    # Both at once is not belt-and-braces, it is two rows disagreeing: one
    # says the script is run on every push, the other says why it never is.
    for f in sorted(set(gated) & set(EXCLUDED)):
        problems.append(
            "%s is BOTH a gate (%s) and excluded. One of those rows is wrong."
            % (f, ", ".join(gated[f])))

    # A row that EXPLAINS a required mode and does not PASS it is the
    # ks3_statutory defect waiting to happen again: the registry says
    # --check-only, the cmd says nothing, and the "gate" rewrites the tree.
    for g in GATES:
        for flag in ("--check-only", "--check"):
            # Longest first, and stop at the first MENTION rather than the
            # first problem: "--check-only" contains "--check", so a row that
            # correctly passes --check-only would otherwise be reported as
            # failing to pass --check.
            if flag in g["why"]:
                if flag not in g["cmd"]:
                    problems.append(
                        "gate %s explains that %s is required and does not "
                        "pass it." % (g["name"], flag))
                break

    for g in GATES:
        if g["speed"] not in ("fast", "slow"):
            problems.append("gate %s has speed %r, which is neither fast nor "
                            "slow." % (g["name"], g["speed"]))
    return problems


def main(argv):
    if "--list" in argv:
        for g in GATES:
            print("  %-28s %-5s %s"
                  % (g["name"], g["speed"], " ".join(g["cmd"])))
        return 0
    if "--check" not in argv:
        print(__doc__)
        return 2
    problems = coverage()
    if problems:
        print("\u274c gate coverage: %d problem(s)\n" % len(problems))
        for p in problems:
            print("   \u00b7 %s" % p)
        print()
        return 1
    import os
    present = [f for f in os.listdir(".")
               if (f.endswith(".py") or f.endswith(".sh")) and os.path.isfile(f)]
    data = [f for f in present if any(f.startswith(p) for p in EXCLUDED_PREFIXES)]
    print("\u2705 gate coverage: %d root script(s) \u2014 %d gate(s) over %d "
          "of them,\n   %d excluded with a reason, %d content-data module(s)."
          % (len(present), len(GATES), len(gate_scripts()), len(EXCLUDED),
             len(data)))
    return 0


def by_name(name):
    for g in GATES:
        if g["name"] == name:
            return g
    raise KeyError("no gate named %r — the registry is %s"
                   % (name, ", ".join(g["name"] for g in GATES)))


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
