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

    dict(name="answer_lengths",
         cmd=["python3", "verify_answer_lengths.py"],
         speed="fast",
         why="MRB-297 — the tell POSITION cannot see. The row above "
             "watches WHERE the correct answer sits; nothing watched HOW "
             "LONG it is. The physics audit measured the cost: a student "
             "who ignored the physics and always picked the longest option "
             "scored 35% against 25% by chance, and 56% in P11. Every "
             "P1-P12 question file claimed in its own docstring that "
             "distractors were written to the correct answer's length — "
             "the claim was written and never gated, and 191 questions "
             "failed it. This row is the gate that claim needed. "
             "⚠️ TWO FIGURES, AND THEY COUNT DIFFERENT THINGS: 840 is how "
             "many physics questions `ks3_assignment_bank` holds, and it "
             "is the denominator of every rate below; 271 is how many of "
             "those sets have a VISIBLY longest option at MARGIN 6, which "
             "is the smaller population the printed margin table reports "
             "on. A rate over 271 and a rate over 840 are not comparable "
             "and must never be quoted against each other. "
             "WHAT GATES: two checks, neither tunable by a threshold. "
             "`report_ranks_all` takes the rank distribution over EVERY "
             "set with no margin filter, so the denominator is the whole "
             "corpus — 840 physics bank questions, 140 ladder rungs — and "
             "a rate means the same thing before and after a change. "
             "`report_sweep` takes the worst rate at any rank at any "
             "margin from 3 to 10, so there is no single margin left to "
             "sit on. Both are baselined at this run\'s branch point "
             "834624da7 (`RANK_ALL_BASELINE`, `SWEEP_BASELINE`) and \"no "
             "worse\" is a ONE-SIDED BINOMIAL against the baseline rate, "
             "not a strict inequality — a strict inequality on a "
             "proportion fires on two sets out of 95. Measured: physics "
             "bank rank 1 went 37.7% to 31.9% over the whole corpus and "
             "53.4% to 43.8% at its worst margin; physics ladder rank 2 "
             "went 30.7% to 32.9% and 34.8% to 36.8%, neither detectably "
             "worse than the baseline it carries. "
             "WHAT DOES NOT GATE, DELIBERATELY: the single-MARGIN rank "
             "table now PRINTS, with ‼️ on hot cells, and returns no "
             "failures — it was green in a two-value window of `MARGIN` "
             "and red on either side, which is a coincidence with a "
             "constant rather than a measurement. And the HOOK corpus is "
             "measured and printed with `HOOK_GATES = False`: it is "
             "UNGRADED, because `r_activity_options` in `ks3_art/kit.py` "
             "is design law R3 — chosen, never correct — and the built "
             "markup carries only `data-i` and `aria-pressed`, so the "
             "`answer` index never reaches the page at all. ⚠️ An earlier "
             "pass of this run claimed a giveaway on eight live pages "
             "from that corpus. That claim was WRONG and is retracted "
             "here rather than quietly dropped. "
             "The pass line says what the gate can honestly promise — "
             "\"nothing new, and no scope worse than the state it "
             "inherited\" — and prints the count of baselined scopes that "
             "DO still let length answer the question. All three checks "
             "are mutation-tested and the results are recorded in the "
             "file."),

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

    dict(name="today_drive",
         cmd=["python3", "today_drive.py"],
         speed="slow",
         needs="mrbadmus_site/teacher/today.html",
         why="MRB-306's Today screen, DRIVEN through its four states. Today "
             "is the one teacher page whose whole job is to be HONEST about a "
             "day, and every way it can lie is a state rather than a value: "
             "a weekend that renders Monday as though it were today, a "
             "weekday with no lessons that says nothing, an empty timetable "
             "that invents one, a class whose read failed showing '0 to "
             "chase' instead of blank. Text assertions alone cannot catch "
             "those, so this drives weekday / weekend / empty-weekday / "
             "no-timetable / 390px against fixture rows. "
             "⚠️ IT ASSERTS THE PAGE IS PAINTED, and that is not belt-and-"
             "braces: the first run of this drive passed all twenty-one text "
             "checks against a page that rendered COMPLETELY BLANK — `body` "
             "was display:none and `getComputedStyle` on a child of a hidden "
             "parent still reports its own display:block. The visibility "
             "check is the finding, not the feature. "
             "It needs a browser but NO network and NO credentials: the "
             "client is stubbed, the clock is frozen per case, and the pages "
             "are served from mrbadmus_site/ over a local port — which is "
             "why it is a push gate and admin_view_drive.py, which signs in "
             "for real, is not. The RLS behind it (timetable_entries_own_all) "
             "is proved separately in SQL under real roles.",
         ),

    dict(name="import_year_drive",
         cmd=["python3", "import_year_drive.py"],
         speed="slow",
         needs="teacher/import.html",
         why="MRB-307 — WHICH SCHOOL YEAR A ROSTER IMPORT LANDS IN. On "
             "1 September 2026 a real import enrolled 14 real students into "
             "LAST YEAR's 7h/Sc5 and left this year's empty. The page sent "
             "`academicYearName: null`, the roster-import edge function fell "
             "back to `academic_years.is_current`, and that flag is moved BY "
             "HAND on 1 September — so on the one morning it mattered it "
             "still said 2025-26. Nothing on screen had ever named a year, "
             "so nothing on screen could have looked wrong. "
             "⚠️ THE FIXTURE HOLDS TWO YEARS AND `is_current` POINTS AT THE "
             "WRONG ONE, and that is the whole gate. Against a single-year "
             "fixture this defect is INVISIBLE: resolving the year properly, "
             "reading is_current, and sending null all lead to the only row "
             "there is, so every check passes on the broken page. Anyone "
             "tempted to tidy the fixture down to one year is removing the "
             "gate while leaving its name. "
             "It drives the real page — real class-entry.js, real rendering "
             "— with a stubbed client, a stubbed guard, a stubbed PapaParse "
             "and the clock frozen to 2026-09-04, because "
             "`workingAcademicYear()` is date-based and an unfrozen drive "
             "asserts a different fact every day and none at all after "
             "Aug 2027. "
             "THE CENTRAL ASSERTION IS NOT A RENDERED STRING: it captures "
             "the body actually handed to `functions.invoke('roster-import')` "
             "by both the dry run and the confirmed write. A page can name "
             "the right year in its note and still send null a screen later "
             "— the note is what the teacher reads, the body is what enrols "
             "the children. The screen checks are there so the two can never "
             "disagree. "
             "IT ALSO WATCHES THE SUCCESS SCREEN'S DEEP LINK, which is the "
             "same defect one surface later. The button goes straight to the "
             "class just filled, and the class ids come from roster-import "
             "only on the NEW deployment — on the one live today the page "
             "looks the id up itself, scoped to school + working year + name. "
             "So the fixture holds TWIN CLASSES: two rows called 7h/Sc5 "
             "differing only by academic year. Drop the year filter and the "
             "lookup matches both, refuses to guess, and falls back to the "
             "class list; filter on the wrong year and it opens last year's "
             "empty twin, which is the original defect wearing a different "
             "coat. Both response shapes are driven, because a deep link "
             "that works on only one of two live deployments is a deep link "
             "nobody can trust. "
             "It also runs its OWN NEGATIVE CONTROL: a second pass with the "
             "predicate forced to return 2025-26, which demands the payload "
             "follow it. A drive that stubs this much can go vacuously green, "
             "and a gate that cannot fail is not a gate — if the forced pass "
             "still yields 2026-27 the payload is not reading the working "
             "year at all and the whole file exits non-zero. The control "
             "carries the deep link too — forced onto the stale year it must "
             "open the STALE twin, which is what proves the year filter is "
             "choosing between the twins rather than the fixture's row order. "
             "⚠️ SLOW BY CATEGORY, NOT BY DURATION — it finishes in about "
             "seven seconds, but it needs headless Chrome, and every browser "
             "gate here is a receipt gate rather than a hook gate so that a "
             "machine without Chrome cannot turn every push red. It needs NO "
             "network and NO credentials: the three CDN hosts are blocked at "
             "the protocol level and the pages are served from the repo root "
             "over a local port. `needs` names teacher/import.html — the "
             "hand-written import wizard, `_REFUSED` by build_teacher_port.py "
             "— because the repo copy is the source of truth for it and the "
             "built copy is only a restamped duplicate.",
         ),

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

    # ── ⊕ MRB-306 Phase 3 · in the document is not the same as reachable ─

    dict(name="teacher_reach",
         cmd=["python3", "teacher_reach.py"],
         speed="slow",
         needs="teacher_fixtures/classes-fixture.html",
         why="Mide's Phase 3 ruling, 4 Sep 2026: assert REACHABILITY of "
             "every teacher control at a real phone width, not the absence "
             "of document overflow. The two are different, and the "
             "difference shipped: on 3 Sep the feedback sheet's \"Save "
             "changes\" sat off the right-hand edge of a panel that is "
             "`overflow:auto`, so it overflowed the PANEL, nothing "
             "overflowed the DOCUMENT, the overflow probe of the day was "
             "green, and a teacher could type a paragraph with nowhere to "
             "press. Found by photographing the page. This gate drives the "
             "same derived fixture set as teacher_behaviour at 390 and 360, "
             "presses every control, and after every press SCROLLS EACH "
             "CONTROL THROUGH EVERY SCROLLABLE ANCESTOR and hit-tests it at "
             "its own centre with elementFromPoint — naming what covers it "
             "when something does. ⚠️ It is NOT a second dead-control gate: "
             "teacher_behaviour asserts that a press changes something, at "
             "1460 where the page is roomy, and duplicating that here would "
             "mean two gates red for one defect. This one asserts what "
             "WIDTH decides — every control revealed by a press is itself "
             "reachable, no computed value reaches the copy on the narrow "
             "branch, and the page never scrolls sideways. Its first run "
             "found the top bar dragging every screen 500px wide on a "
             "phone; the fix is the `[data-port-region=\"topbar\"]` rule in "
             "build_teacher_port.py. ⚠️ It does not cover today.html, "
             "timetable.html or admin.html — those are hand-written and "
             "have no fixtures; today_drive covers Today's four states "
             "(including no-timetable) at 390 for OVERFLOW but not for "
             "reach, and admin_view_drive is EXCLUDED because it signs in "
             "for real. That gap is stated in this gate's own docstring "
             "rather than left to be discovered."),

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

    # ── ⊕ MRB-301 · the KS4 chrome port ─────────────────────────────────

    dict(name="ks4_chrome_tells",
         cmd=["python3", "ks4_chrome_tells.py"],
         speed="fast",
         needs="docs/ks3/design-reference/chrome/MrBadmusAI Redesign.dc.html",
         why="Design's click-through must not reach a student. The chrome "
             "delivery is a SAMPLE in the same way the teacher and "
             "leaderboard deliveries were: template tokens ({{ subjectName }}, "
             "{{ goHome }}), directive elements (<sc-if>, <sc-for>, "
             "<x-import>, style-hover=, onClick=), every href a bare '#', and "
             "invented numbers — 68%, 80%, 76%, '14th of 212', '3 of 7 done', "
             "'21/62' — plus two students who do not exist. The numbers are "
             "the dangerous half: an unsubstituted token is visible to anyone "
             "who looks, and 'Your best 68%' is not. Its corpus is DERIVED "
             "from the vendored delivery on every run rather than typed, for "
             "the reason student_page_drive records about its own list. CSS "
             "is excluded from both sides — the first run failed all 118 "
             "pages on `width:100%`, and a gate that cries wolf gets switched "
             "off. It also resolves EVERY internal href on every chrome page "
             "against the built tree (Design's controls all pointed at '#', "
             "so 'no dead controls' has to be measured, not asserted), and "
             "polices the scope wall in both directions: every chrome page "
             "wears data-chrome=\"ks4\", and NOTHING else in the built tree "
             "does — which is what keeps the ~865 lesson pages out. "
             "Mutation-tested: five separate probes each turn it red. "
             "`needs` the vendored delivery, because a gate whose corpus is "
             "missing would pass everything, which is worse than no gate."),

    dict(name="ks4_chrome_drive",
         cmd=["python3", "ks4_chrome_drive.py"],
         speed="slow",
         needs="mrbadmus_site/ks4.html",
         why="the KS4 chrome DRIVEN, and the twin of ks4_chrome_tells the way "
             "teacher_behaviour is the twin of teacher_tells: `tells` reads "
             "the built bytes and would pass just as happily on a page that "
             "renders blank. This walks the whole journey — landing, KS3 "
             "entry, GCSE hub, both pathways, both tiers, all three sciences, "
             "a topic page and the LESSON behind it — at 1440/820/390/360, "
             "signed out AND signed in, on load and again after a reload. It "
             "asserts every view mounts wearing Design's DOUBLE-chevron mark "
             "in Bricolage; that nothing scrolls sideways (the "
             "header-overflow class, and it names the widest element when it "
             "does); that the console stays quiet apart from the backend "
             "calls a static harness cannot serve; that no progress is "
             "CLAIMED IN RENDERED TEXT — which is where `tells` cannot look, "
             "because a string assembled by JS never appears in the built "
             "bytes; and that KS3 and the lesson page still carry the CLASSIC "
             "nav and never `data-chrome`, which is the scope wall driven "
             "rather than remembered. Signed-in is a seeded localStorage "
             "session; ⚠️ its access_token has to be a properly encoded JWT, "
             "because every page loads the Supabase SDK and the SDK DELETES a "
             "stored session whose token it cannot decode — that cost a round "
             "of 88 identical failures misdiagnosed as localStorage not "
             "persisting. ⚠️ Its screenshots default OUTSIDE the repo: they were "
             "written into the committed docs/redesign/ set at first, a "
             "screenshot is not byte-deterministic, and recording this gate's "
             "receipt therefore dirtied the tree and refused the eight gates "
             "behind it. A gate must not modify what it attests. ⚠️ It proves "
             "nothing about the live endpoints: the harness serves static "
             "files, so the two leaderboard surfaces are exercised in their "
             "EMPTY state here and their populated state was driven by hand "
             "with a stubbed fetch."),

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

    dict(name="seating_tells",
         cmd=["python3", "seating_tells.py"],
         speed="fast",
         why="MRB-322 seating plans, static. Five checks, and the two that "
             "matter most cross a repo boundary. (a) THE ROOM LIST IS ONE "
             "LIST: the eleven room codes are written in the dropdown, in a "
             "CHECK constraint, and in the gate — nobody types a room name, "
             "and a room quietly dropped from the dropdown is indis"
             "tinguishable from a room nobody has drawn yet. (b) THE PHOTO IS "
             "NEVER PERSISTED: /api/room-scan holds a photograph of a real "
             "classroom, in memory, and discards it. This walks that handler "
             "AND the room-scan.js module it delegates to — in the backend "
             "repo, by absolute path, as pool_ownership does — and fails on "
             "any fs write, storage upload, or log line that could carry "
             "image bytes. (c) the honest degrade: `photo_scan_unconfigured` "
             "is one string spanning two repos with no shared type, and if "
             "the two halves drift the 'Photo scan isn't switched on yet' "
             "branch becomes unreachable rather than wrong-looking. Plus: no "
             "harness or RLS-rehearsal fixture data in anything shipped, and "
             "every watched file exists — a gate that goes green because its "
             "subject is missing is worse than no gate."),

    dict(name="seating_drive",
         cmd=["python3", "seating_drive.py"],
         speed="slow",
         needs="mrbadmus_site/teacher/seating.html",
         why="MRB-322 seating plans, driven. The canvas is the product — a "
             "layout that cannot be dragged is not a layout — and nothing "
             "else in the estate presses it: teacher_behaviour drives a "
             "FIXED `SCREENS` list and seating.html is not on it, by design, "
             "because that lane's generator does not own this page. Drives "
             "the real page in headless Chrome at 1280 and 390 with pointer "
             "events (the same code path a trackpad and an iPad take), and "
             "asserts the things a screenshot cannot: that a drag moves a "
             "desk and costs exactly one undo, that view mode renders no "
             "handles AT ALL rather than disabled ones, and that the "
             "unseated count is drawn even when it is inconvenient."),

    dict(name="consumer_flag_off",
         cmd=["python3", "night3_selfreview.py",
              "--site", "mrbadmus_site", "--api", "http://localhost:3120"],
         speed="slow",
         needs="mrbadmus_site/parents/index.html",
         why="MRB-317/321. The consumer estate ships to production with "
             "CONSUMER_SIGNUP_ENABLED off, so 21 pages sit in "
             "mrbadmus_site/ that NOBODY MAY SEE YET, and the only thing "
             "standing between a paying-customer front door and 135 "
             "students is one boot() branch on each of them. This drives "
             "the BUILT tree with the Network domain recording every "
             "request and asserts all 21 render 'Not found' having asked "
             "for nothing — not the API, not Supabase, not a CDN. A static "
             "grep cannot do it: the page ships the real markup and the "
             "flag decides at runtime, so the bytes look identical either "
             "way. It also carries the RAINFORD REGRESSION (teacher "
             "landing, today, admin with the consumer card absent, the "
             "student class page, the leaderboard) and the brand greps, "
             "which is why it is here rather than scoped to one lane. "
             "⚠️ Needs a backend on :3120; it signs in as the hz_* TEST "
             "fixtures and skips, loudly, without their passwords."),
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
    "admin_view_drive.py":
        "drives MRB-303 J2's read-only school view (teacher/admin.html). Two "
        "halves, and BOTH are unsuitable for a push gate. The negative half "
        "signs in as real TEST teachers over the network to prove hod and a "
        "plain teacher get no Admin entry and an honest refusal; the "
        "positive half stubs the client, because hz_admin/hz_slt carry NO "
        "PASSWORD on the TEST project and MRB-303 bans setting one. Needs "
        "the network, real sign-ins and a browser; a push must not depend on "
        "any of the three. Run it by hand when the admin view changes.",
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

    # ── MRB-308…321 · the B2C nights' two generators ────────────────────
    #
    # Both arrived with the consumer work and neither was registered, which
    # is the gap this registry exists to make loud. They are EXCLUDED for
    # the reason every other generator here is: writing is the job, and the
    # gate on their output is somewhere else.
    "ks4_seed_sow.py":
        "a GENERATOR of one tracked seed file "
        "(supabase/seeds/20260902001000_ks4_default_sequence.sql), which it "
        "rewrites whole from generate_site_v5.PATHWAY_TOPIC_MAP and the "
        "all_subtopics_* modules. Exactly the shape of ks3_seed_sow.py "
        "above. What its output must satisfy is asserted by the database "
        "itself — scheme_of_work_entries_academic_week_check, which MRB-310 "
        "had to widen to 52 for KS4 precisely because the seed ran into it.",
    "export_ks3_extended.py":
        "an EXPORTER: the KS3 ladder's `explain` and `produce` rungs as "
        "JSON on stdout, feeding the exam_questions seed. It asserts "
        "nothing about the estate and writes no tracked file. Its sibling "
        "export_ks3_questions.py is a gate because it MIRRORS three pools "
        "and can drift from them; this one has no mirror to drift from.",

    # ── MRB-317/321 · the two consumer drives that assert and are STILL
    # excluded, on exactly the P1 reasoning above. The third one,
    # night3_selfreview.py, IS registered (`consumer_flag_off`), because it
    # is estate-wide and it is what stands between a customer front door and
    # 135 students. These two are not.
    "night3_flagon_smoke.py":
        "the flag-ON pass. It asserts plenty, and it is excluded because it "
        "CREATES A REAL FAMILY on the shared TEST project through the API "
        "— a parent, two children, a subscription — and tears them down "
        "again. As a push gate it would have every lane writing fixtures "
        "into one database at once, which is the collision Night 3 already "
        "hit twice (two lanes marking each other's answers through the "
        "platform-wide mb-queue). A gate that corrupts other lanes' runs to "
        "prove a page renders is worse than no gate.",
    "night4_laneC_drive.py":
        "Lane C's public-surface drive — the nine /parents/ pages at 390 "
        "and 1280, the reset-password flow against a real Supabase "
        "recovery link, the org dashboard, and the price/brand cold greps. "
        "Lane-scoped and needs Chrome plus a backend; its flag-off "
        "assertions are a SUBSET of consumer_flag_off's, which is "
        "registered. Same trade as p1_drive.py above: real value, run "
        "deliberately, not a cost every push from every lane pays.",
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
