#!/usr/bin/env python3
"""student_rulings.py — Mide's MRB-275 rulings, as source rather than as an edit.

⚠️ WHY THIS FILE EXISTS, AND WHAT IT IS RECOVERING FROM.

The three rulings of 21 Aug 2026 were applied on 20 Aug in commit 895f34766 —
correctly, carefully, and IN THE WRONG PLACE. That commit touched four files:

    mrbadmus_site/student/class-ported.html
    mrbadmus_site/student/assignment-ported.html
    student/class-ported.html
    student/assignment-ported.html

Every one of those is GENERATED OUTPUT. `build_student_port.py` writes all four
from `student_templates.json`, and its own banner says "GENERATED — do not
edit". So the rulings held for exactly as long as nobody re-ran the build. The
next run — this one — silently reverted all three, and the behaviour gate went
red in thirteen places naming a divergence that had been correct that morning.

That commit's own message diagnosed the neighbouring version of this mistake
("it drove last night's file and reported 28 healthy drives about code that no
longer existed") and then made this one, because `student/class-ported.html`
sits in the repo root and reads like source. It is not. It is the mirror.

So the rulings live HERE now, as transformations applied to Design's logic and
Design's template at build time, and a rebuild carries them rather than
destroying them. The content of every one is unchanged — each `new` below is
byte-for-byte what 895f34766 wrote, extracted from that commit rather than
retyped, and the build asserts that each `old` appears EXACTLY ONCE in Design's
delivery before touching it. If Design redraws that span, the build stops
rather than applying a ruling to a line that has moved.

── THE THREE RULINGS ─────────────────────────────────────────────────────

1a  The right answer's feedback line is dropped for v1, and the slot CLOSES
    rather than standing empty. (`assignment`, six replacements.)
1b  The leaderboard bar shows the TOTAL; the ON TIME / SCORE / RECALL split is
    omitted entirely, along with the leader's hero bar, the three-column
    figures and the static "40 / 40 / 20" legend. (`class view`, four
    replacements plus seven pruned template nodes.)

Both are also asserted from the other side, in `student_behaviour.py`'s
RULED_DIVERGENCE and in `student_parity.py`: present in Design's own delivery,
absent from the port. Those gates are what catch this file rotting.
"""

# ── template nodes the ruling removes, by `data-dc-tpl` index ────────────
#
# Each is the ROOT of a subtree; its descendants go with it. Measured against
# 895f34766, not guessed: pruning exactly these seven reproduces that commit's
# template node-for-node, and the build re-checks the count it removed.
#
#   275, 279   the leader's three-column ON TIME / SCORE / RECALL figures
#   297, 298   the leader's hero split bar
#   322 … 330  the static "ON TIME · 40 / SCORE · 40 / RECALL · 20" legend
PRUNE = {
    # ⊕ RULED 22 Aug 2026 — P7. SETTINGS IS A DEAD CONTROL, SO IT GOES.
    # ⊕ RETIRED 23 Aug 2026 — PHASE 1b. THE CONDITION P7 NAMED HAS BEEN MET.
    #
    # P7 pruned two nodes and stated its own retirement condition in the same
    # breath: *"It comes back when Design's theme picker gives it a job."*
    #
    #   26   the wide header's "Settings" link
    #   30   the same item inside the narrow account menu
    #
    # Both were `<a href="#top">` with no handler, which scrolls the page to
    # the top and is read by a student as the app ignoring them.
    #
    # ⚑ DESIGN'S AMENDED DELIVERY SETTLES IT LITERALLY, not by analogy.
    # Donor node 22 — the same "Settings" in Design's amended header — is a
    # `<button>` carrying `onClick={{ openAccount }}`, and `openAccount` is
    # what opens the account sheet the theme picker lives in. So the job P7
    # was waiting for is the exact job Design gave this exact control.
    #
    # The two indices therefore leave `PRUNE` and arrive in `SET_ON` below,
    # wired to `openAccount`. Their twin registrations in
    # `student_behaviour.RULED_DIVERGENCE` and `.RULED_CONTROLS` come out in
    # the SAME commit: the port renders `Settings` again, exactly as Design's
    # original delivery does, so there is no divergence left to declare and a
    # registration that outlived its ruling would go red for being satisfied.
    #
    # ⚠️ THE AVATAR BUTTON (node 21) IS NOT REWIRED, and this was checked
    # rather than assumed. Design's amended header gives node 19 — its avatar —
    # `openAccount` too, because Design's amended header has NO dropdown menu:
    # the sheet replaces it. Ours still has one, at node 28 (`if menuOpen`),
    # and at NARROW width that dropdown is the only route to `Sign out` — node
    # 25's inline Settings/Sign out pair is inside `if wide`. Rewiring node 21
    # to `openAccount` would therefore sign a phone user out of the ability to
    # sign out. It keeps `toggleMenu`; the route into the sheet on a phone is
    # avatar → menu → Settings, which is two presses and no dead ones.
    # (`SET_ON` would have refused the rewrite anyway — node 21 already
    # carries a handler and the build stops rather than overwrite one.)
    #
    # ── the MRB-275 prunes, unchanged ────────────────────────────────────
    #
    # ⚠️ CLASS VIEW ONLY, AND THAT WAS CHECKED RATHER THAN ASSUMED. The first
    # draft of the P7 ruling pruned 26 and 30 on BOTH pages, because both pages
    # obviously have a header. They do not have the same one: node indices are
    # per-page, and on the assignment page 26/27/30/31 are the `sc-if` around
    # the deadline chip, the LATE chip, the HANDED IN chip and a chevron.
    # Pruning them would have silently deleted a student's "LATE" and
    # "HANDED IN" badges — a far worse defect than the one being fixed, shipped
    # in the same commit that claimed to fix it. The assignment page has no
    # account menu at all: no Settings, no Sign out, no environment badge.
    "class view": [275, 279, 297, 298, 322, 325, 328],
}

# ── template nodes that need a CLICK HANDLER Design never gave them ───────
#
# ⊕ RULED 22 Aug 2026 — P5. SIGN OUT DID NOT SIGN OUT — IT SCROLLED.
#
#   27   the wide header's "Sign out" button
#   31   the same item inside the narrow account sheet
#
# Both are `<a href="#top">Sign out</a>` with no handler at all, in Design's
# delivery and therefore in the port. Pressing it scrolled the page to the top
# and left the student signed in — on a shared school machine, that is the
# next child seeing this one's marks.
#
# ⚑ WHY A THIRD MECHANISM. `LOGIC` rewrites Design's logic and `PRUNE` removes
# template subtrees; neither can put a handler on a node that has none.
# `BINDINGS` can only change a node's TEXT. Adding one more mechanism was the
# alternative to hand-editing the built page, which is the mistake this whole
# file exists to recover from.
#
# `{node index: handler name}`. The name is resolved out of the same scope
# every `onClick="{{ … }}"` in Design's template resolves from, so a handler
# added here is reached exactly as one Design drew — see `node.on` in
# `shared/student-runtime.js`. The build asserts each node exists and does not
# already carry a handler, so this can never silently replace one of Design's.
SET_ON = {
    # Class view only — see the note on PRUNE above. The assignment page has
    # no account menu, so there is no Sign out on it to wire.
    #
    # 231 is the lesson card inside "Lessons in this topic" — Design's
    # `<a href="#top">`, which scrolled instead of opening the lesson. Its
    # handler is `l.open`, resolved out of the `sc-for`'s own loop scope, so
    # each card opens ITS lesson rather than a shared one.
    #
    # ⊕ 23 Aug 2026 — PHASE 1b. 26 and 30 are the two "Settings" controls,
    # back from `PRUNE` with the job Design gave them: they OPEN THE ACCOUNT
    # SHEET, which is where the bench theme picker lives. See the retirement
    # note on `PRUNE` above, and the graft of donor node 243 below.
    #
    # Both, not one. 26 is the wide header's inline link and 30 is the same
    # item inside the narrow dropdown, and a phone only ever sees 30 — wiring
    # the one that reads first in the file would have left every phone with a
    # picker it could not reach and a gate that never noticed, because the
    # behaviour gate drives at 1460.
    "class view": {26: "openAccount", 30: "openAccount",
                   27: "signOut", 31: "signOut", 231: "l.open"},
}

# ── the logic, transformed ───────────────────────────────────────────────
#
# (old, new). `old` must occur exactly once in Design's logic class, or the
# build stops — see `apply_rulings` in build_student_port.py. Order matters
# only in that each is applied to the result of the last.
LOGIC = {
    'class view': [
        # ── ⊕ RULED 22 Aug 2026 — THE LESSON CARDS SCROLLED ───────────────
        #
        # Found by `student_controls_drive.py` on its first run, on the first
        # screen, and not by the brief: every card in "Lessons in this topic"
        # is an `<a href="#top">`, so tapping the lesson a student had just
        # been told they were being tested on scrolled them to the top of the
        # page. The fifth control tonight whose only effect was a scroll.
        #
        # `open` is a function per card, so the `sc-for`'s loop scope gives
        # each one its own lesson — see `SET_ON` above. A card with no known
        # page keeps Design's inert anchor rather than pointing at a 404,
        # which is the same rule the work row's primary button follows.
        (
            "    const lessons = this.lessonDefs.map((l) => ({\n      num: l.num, name: l.name, meta: l.meta,",
            "    const lessons = this.lessonDefs.map((l) => ({\n"
            "      /* ⊕ RULED 22 Aug 2026 — the card opens its lesson. */\n"
            "      open: (e) => {\n"
            "        if (!l.href) { return; }\n"
            "        if (e && e.preventDefault) { e.preventDefault(); }\n"
            "        window.location.href = l.href;\n"
            "      },\n"
            "      num: l.num, name: l.name, meta: l.meta,",
        ),
        # ── ⊕ RULED 22 Aug 2026 — P4. THE BENCH HAD NO DONE STATE ─────────
        #
        # A student who had finished the week was still shown the open-work
        # bench, checklist and all, telling them to open it and answer the
        # questions — while the work list six inches below correctly said
        # COMPLETED. The page contradicted itself on one screen.
        #
        # ⚑ THE WHOLE DONE STATE IS DATA. NOT ONE NEW TEMPLATE NODE.
        #
        # That is not restraint for its own sake — it is what "arranging, not
        # designing" turns out to mean here, because Design had already drawn
        # every part of it:
        #
        #     the eyebrow      carries the congratulation and the date
        #     the heading      is already the assignment's title
        #     the paragraph    already exists (wide only, Design's choice)
        #     the checklist    is an sc-for, so an EMPTY LIST renders nothing
        #     "Practise recall" IS ALREADY THERE, beside the primary button
        #     the meter        is already a percentage and a caption
        #
        # So the interim needs exactly two edits to Design's logic — this one,
        # and the button label binding — and the rest is `student-live.js`
        # putting different words in slots that already exist. When Design's
        # redraw is ported (it landed mid-run; see the run log) it replaces
        # markup, not logic, which is what the ruling asked for.
        #
        # `benchDone` is false in the fixture, so both branches below evaluate
        # to Design's own expression and the behaviour gate sees no change.
        (
            "      benchTasks: benchTasks, benchPct: Math.round((doneCount / 3) * 100) + '%', benchDoneText: doneCount + ' / 3 DONE',",
            "      benchTasks: benchTasks,\n"
            "      /* ⊕ RULED 22 Aug 2026 — P4. */\n"
            "      benchPct: MRB_DATA('benchDone') ? MRB_DATA('benchPct')\n"
            "        : Math.round((doneCount / 3) * 100) + '%',\n"
            "      benchDoneText: MRB_DATA('benchDone') ? MRB_DATA('benchDoneText')\n"
            "        : doneCount + ' / 3 DONE',",
        ),
        # ── ⊕ RULED 22 Aug 2026 — P2. "STREAK BROKEN" BEFORE A STREAK ─────
        #
        #     streakText: st.streak > 0 ? 'STREAK ' + pad(st.streak)
        #                                : 'STREAK BROKEN',
        #
        # The streak opens at 0 — correctly, since nothing records a recall
        # streak between sessions — and 0 rendered as STREAK BROKEN. So the
        # first thing the round said to a student who had not yet answered a
        # single question was that they had broken something.
        #
        # RULED: the label appears only after a streak ACTUALLY BREAKS. Zero
        # is now two different states and the page has to tell them apart:
        #
        #     no streak yet      nothing is said
        #     a streak, running  STREAK 03
        #     a streak, broken   STREAK BROKEN
        #
        # ⚠️ A FIRST WRONG ANSWER IS NOT A BROKEN STREAK EITHER, and that is
        # the case the obvious fix ("say nothing until they have answered
        # one") gets wrong. Nothing was built, so nothing broke. `broke` is
        # therefore set only on the transition FROM a streak TO none —
        # `s.streak > 0` at the moment it is zeroed — and not on reaching
        # zero, which is where it starts.
        #
        # It rides with `streak` rather than with the round: `newRound` does
        # not reset either, because a student's best run is theirs across the
        # sitting and Design already kept the streak across rounds.
        (
            "  state = {",
            "  /* ⊕ RULED 22 Aug 2026 — P2. `broke` — see streakText below. */\n"
            "  state = {\n    broke: false,",
        ),
        (
            "  skipQuestion = () => this.setState((s) => ({ qi: s.qi + 1, pick: null, checked: false, streak: 0 }));",
            "  skipQuestion = () => this.setState((s) => ({ qi: s.qi + 1, pick: null, checked: false, streak: 0, broke: s.broke || s.streak > 0 }));",
        ),
        (
            "      return { checked: true, right: s.right + (ok ? 1 : 0), streak: ok ? s.streak + 1 : 0 };",
            "      /* ⊕ RULED 22 Aug 2026 — P2. A streak BREAKS only when there\n"
            "         was one: wrong on the first question of a round zeroes a\n"
            "         streak that was already zero, and nothing was broken. */\n"
            "      return { checked: true, right: s.right + (ok ? 1 : 0), streak: ok ? s.streak + 1 : 0, broke: s.broke || (!ok && s.streak > 0) };",
        ),
        (
            "      streakText: st.streak > 0 ? 'STREAK ' + pad(st.streak) : 'STREAK BROKEN',",
            "      /* ⊕ RULED 22 Aug 2026 — P2. Silent until a streak breaks. */\n"
            "      streakText: st.streak > 0 ? 'STREAK ' + pad(st.streak) : (st.broke ? 'STREAK BROKEN' : ''),",
        ),
        # ── ⊕ RULED 22 Aug 2026 — P5. SIGN OUT NOW SIGNS OUT ──────────────
        #
        # The handler `SET_ON` attaches to the two "Sign out" nodes. It is
        # exposed here, in `renderVals()`, beside `goClass` and `goRecall`,
        # because that is the scope `node.on` resolves against.
        #
        # It does three things, in this order, and the order matters:
        #
        #   1  CLEAR THIS DEVICE'S CACHES FIRST. The assignment page keeps a
        #      draft under `mrbadmusai.assignment.<class>.<id>.v1`. On a shared
        #      school machine — which is most of them — leaving that behind
        #      hands the next child this child's answers, already filled in.
        #      Done before the session ends, so it happens even if the network
        #      call is slow or fails.
        #   2  END THE SUPABASE SESSION, through the guard the rest of the
        #      student pages already use, so there is one sign-out and not two.
        #      It redirects to /auth.html and carries ?env=test when the page
        #      is on the test project.
        #   3  FALL BACK TO /auth.html. Reached when the guard is not loaded —
        #      which is exactly the fixture page. Design's file navigates
        #      nowhere and the behaviour gate does not press this control, so
        #      the fallback is never taken in anger; it is here so that a
        #      signed-in student on a page with a broken script still LEAVES
        #      rather than silently staying signed in.
        (
            "      goClass: () => this.go('class'), goRecall: () => this.go('recall'),",
            "      goClass: () => this.go('class'), goRecall: () => this.go('recall'),\n"
            "      /* ⊕ RULED 22 Aug 2026 — P5. */\n"
            "      signOut: (e) => {\n"
            "        if (e && e.preventDefault) { e.preventDefault(); }\n"
            "        try {\n"
            "          Object.keys(window.localStorage)\n"
            "            .filter((k) => k.indexOf('mrbadmusai.') === 0)\n"
            "            .forEach((k) => window.localStorage.removeItem(k));\n"
            "        } catch (err) { /* a private window has no storage to clear */ }\n"
            "        const g = window.MrBadmusStudentGuard;\n"
            "        if (g && g.signOut) { g.signOut(); return; }\n"
            "        window.location.href = '/auth.html';\n"
            "      },",
        ),
        # ── ⊕ RULED 22 Aug 2026 — P1. THE PRIMARY BUTTON ON THE BENCH ─────
        #
        # "Open the assignment" — the single most important control on the
        # page — did not open the assignment. It ticked a checklist item:
        #
        #     openAssignment = () => this.setState((s) =>
        #       ({ bench: Object.assign({}, s.bench, { t1: true }) }));
        #
        # That is not a bug in Design's file. Design drew ONE page, and in one
        # page "open it" is a state change — the checklist's first item going
        # green. It became a defect at the moment there was a second page to
        # open, and nothing in the port had told it so.
        #
        # It now navigates when it has somewhere to navigate to, and ticks
        # otherwise. The tick is kept rather than replaced: with an empty
        # `assignmentHref` this is Design's own line, byte for byte in effect,
        # so the fixture still ticks and the behaviour gate needs no
        # divergence registered.
        (
            "  openAssignment = () => this.setState((s) => ({ bench: Object.assign({}, s.bench, { t1: true }) }));",
            "  openAssignment = () => {\n"
            "    /* ⊕ RULED 22 Aug 2026 — P1, extended by P4. The bench's\n"
            "       primary button. It opens the assignment while there is one\n"
            "       open, and revisits the lessons once the week is done — one\n"
            "       button, one destination, both named by the data. */\n"
            "    const href = MRB_DATA('benchPrimaryHref');\n"
            "    if (href) { window.location.href = href; return; }\n"
            "    this.setState((s) => ({ bench: Object.assign({}, s.bench, { t1: true }) }));\n"
            "  };",
        ),
        # ── ⊕ RULED 22 Aug 2026 — P3. "OPEN THE LESSON" OPENED RECALL ──────
        #
        #     primary: w.status === 'open' || w.retake
        #       ? this.openAssignment : () => this.go('recall'),
        #
        # One expression serves five labels, and only two of them are the
        # assignment. Everything else fell into `go('recall')` — so a student
        # whose marked work said "Open the lesson" got the recall round, and a
        # student asking for an extension got the recall round too.
        #
        # The row now routes by what its button SAYS:
        #
        #   open / retake   the assignment      (P1's destination)
        #   marked          the lesson it drew on, when the build knows where
        #                   that lesson lives
        #   anything else   Design's own fallback, unchanged
        #
        # ⚠️ THE FALLBACK IS DELIBERATE AND IS NOT A SHRUG. `r.lessonHref` is
        # empty when the work draws on a lesson this build has no page for —
        # a retired slug, or a question bank that has moved on. Sending that
        # student to a 404 with their name on it is worse than sending them
        # somewhere that exists, and the recall round is at least about the
        # same class. The button that is genuinely wrong here is "Ask for an
        # extension", which does not do that either; it is out of tonight's
        # scope and is on the report as such rather than being quietly
        # rewired.
        (
            "        primary: w.status === 'open' || w.retake ? this.openAssignment : () => this.go('recall'),",
            "        primary: (w.status === 'open' || w.retake)\n"
            "          ? this.openAssignment\n"
            "          : (isMarked && w.lessonHref)\n"
            "            ? () => { window.location.href = w.lessonHref; }\n"
            "            : () => this.go('recall'),",
        ),
        (
            "        monoBorder: r.me ? 'var(--st-accent)' : 'var(--st-edge)',\n        barWidth: Math.round((r.pts / maxPts) * 100) + '%',",
            '        monoBorder: r.me ? \'var(--st-accent)\' : \'var(--st-edge)\',\n        /* ⊕ RULED 21 Aug 2026 — the bar shows the TOTAL, and the ON TIME /\n           SCORE / RECALL split is omitted entirely. `barWidth` is the total:\n           this student\'s points against the class maximum, which is a real\n           comparison and stays. The three sub-widths that used to fill it are\n           gone, along with the leader\'s hero bar, the leader\'s three-column\n           figures and the static "ON TIME · 40 / SCORE · 40 / RECALL · 20"\n           legend (template nodes 275-283, 295-298, 322-330).\n\n           ON TIME and SCORE are both computable — due_at against the submission\n           timestamp, and score against max_score. RECALL is not: nothing\n           anywhere records a recall round, `quiz_scores` carries neither a\n           class nor a teaching week, and `quiz_question_attempts` has no\n           question_ref to resolve an answer back to a rung. A bar showing two\n           of three components is a different lie from one showing three\n           fabricated ones, and it is still one.\n\n           What it would take to make the split honest is measured and costed on\n           MRB-275. Do not restore any of this until that lands — student_parity\n           layer F already fails the build if Design\'s 0.4 / 0.19 drawing\n           constants reappear. */\n        barWidth: Math.round((r.pts / maxPts) * 100) + \'%\',',
        ),
        (
            "        wOnTime: Math.round((r.onT / r.pts) * 100) + '%',\n        wScore: Math.round((r.sc / r.pts) * 100) + '%',\n        wRecall: Math.round((r.rec / r.pts) * 100) + '%',",
            '',
        ),
        (
            "      deltaText: top.me ? 'THAT IS YOU' : pad(top.pts - (table[1] ? table[1].pts : 0)) + ' POINTS CLEAR',\n      wOnTime: Math.round((top.onT / top.pts) * 100) + '%',\n      wScore: Math.round((top.sc / top.pts) * 100) + '%',\n      wRecall: Math.round((top.rec / top.pts) * 100) + '%',\n      parts: [{ label: 'ON TIME', value: top.onT }, { label: 'SCORE', value: top.sc }, { label: 'RECALL', value: top.rec }].map((p, i) => Object.assign(p, { edge: i < 2 ? '1px solid var(--st-room-line)' : 'none' }))",
            "      deltaText: top.me ? 'THAT IS YOU' : pad(top.pts - (table[1] ? table[1].pts : 0)) + ' POINTS CLEAR'\n      /* the leader's split bar and its three-column figures are gone — see the\n         ruling note on `barWidth` above. `leader.points` directly above them is\n         the total, so nothing is lost by removing the bar: at 100% of the\n         leader's own points it was always full and said nothing anyway. */",
        ),
        (
            "        barWidth: Math.round((r.pts / maxPts) * 100) + '%',\n\n        up: d.up, down: d.down, flat: d.flat",
            "        barWidth: Math.round((r.pts / maxPts) * 100) + '%',\n        up: d.up, down: d.down, flat: d.flat",
        ),
        # ── ⊕ RULED 23 Aug 2026 — THE TERM SPINE DID NOT MOVE WITH THE PAGE ─
        #
        # Design's amendment: *"The week-selection tile, the leaderboard card
        # and its week chips take the bench theme, so the whole page moves
        # together."* The bench does, through the token bridge. The leaderboard
        # card does. THE SPINE DID NOT — so on Chalk a light bench sat above a
        # graphite spine, and the page did not move together at all.
        #
        # The spine is not reachable from the bridge and never will be: it is
        # painted by computed colour strings, and it sits on the PAGE ground,
        # not on a themed one. `SET_ATTR` gives it `data-port-region` and
        # deliberately no `data-bench-surface` for exactly that reason — a
        # surface attribute there would remap `--st-cream` and `--st-ink` over
        # cream page chrome. So this is the LOGIC rewrite that note deferred.
        #
        # ⚑ ONE LINE, AND ONLY THE SELECTED TILE. Design's own amended CSS is
        #
        #     .wk[data-sel="1"]{--wk-fill:var(--b-ground);--wk-edge:var(--b-ground);}
        #     .wk[data-sel="1"] .wkline{--wk-line:var(--b-ink);}
        #
        # — a selected tile made of the bench's own material, and nothing else
        # in the spine re-tokened. `trough`, `nowDot` and the unselected `num`
        # are page chrome; Design left them on page tokens and so does this.
        #
        # Mapping Design's two properties onto the live tile, which is node 129
        # (`background:w.trough`, `box-shadow:w.ring`) with the number at 133
        # BELOW it:
        #
        #   --wk-edge  → `ring`.  Adopted. The ring IS the live tile's edge.
        #   --wk-fill  → `trough`. REFUSED. The live trough is not empty the
        #                way Design's tile is — it carries the week's work as
        #                stacked `segs`, and those segs are `--st-ink` for done
        #                and `--st-accent` for open. Filling it with
        #                `--b-ground` would sink the done segments into a dark
        #                ground on five themes and destroy the data the tile
        #                exists to show. Design's tile has no data in it; this
        #                one does, and fidelity to a drawing is not worth a
        #                week's work becoming invisible.
        #   --wk-line  → no counterpart. Design's `.wkline` is a mark drawn
        #                INSIDE the filled tile. With no fill there is nothing
        #                for it to be drawn on.
        #
        # ⚠️ `numColor` STAYS `var(--st-ink)`, AND THAT IS THE SAFETY MARGIN,
        # not an omission. The number sits below the tile on the CREAM PAGE
        # GROUND, not on the bench — the same position as Design's own `w.label`,
        # which Design also leaves on page tokens (`--pg-accent-text` /
        # `--pg-muted`) rather than theming. Theming it would be actively
        # wrong: on Chalk `--b-ground` is #EFE2CB, and #EFE2CB on the cream page
        # measures about 1.1:1 — this unit's other defect, rebuilt in a new
        # place by the fix for it.
        #
        # Keeping it also means SELECTION IS NEVER LOST. The selected tile
        # carries TWO cues — the ring, and the number going from `--st-ghost` to
        # `--st-ink`. The ring now tints with the theme and on Chalk it is a
        # pale edge on a pale page; the number is still full-strength ink on
        # every one of the six, so the student can always see which week is
        # picked. One cue takes the theme, the other guarantees the state.
        #
        # ⚠️ `n === 4` IS UNTOUCHED THROUGHOUT. It is a hardcoded "this week"
        # in Design's pre-ruling logic and it is wrong, but correcting it is a
        # different unit and doing it here would hide it inside a colour change.
        (
            "        ring: sel ? '0 0 0 1.5px var(--st-ink)' : 'none',",
            "        /* ⊕ RULED 23 Aug 2026 — the selected week takes the bench\n"
            "           theme, per Design's `--wk-edge:var(--b-ground)`. The\n"
            "           trough, the nowDot and `numColor` do not move; see the\n"
            "           note above this entry for why each one stays. */\n"
            "        ring: sel ? '0 0 0 1.5px var(--b-ground)' : 'none',",
        ),
        # ── ⊕ RULED 23 Aug 2026 — THE WEEK TILE'S *DONE* SEGMENT IS ESPRESSO ──
        #
        # Design's amendment 1 opens: *"no page chrome is near-black any more.
        # Page-chrome dark is now espresso #4A3728 (10.4:1 on cream) — top
        # rule, work-row and legend DONE dots."* The two DONE dots it names are
        # template nodes and move through `SET_ATTR` + the page-chrome rule in
        # build_student_port.py. This one is a COMPUTED COLOUR STRING, so it is
        # a LOGIC rewrite — the same shape, and for the same reason, as `ring`
        # directly above.
        #
        # ⚠ DESIGN DOES NOT NAME THIS ELEMENT, AND IT MOVES ANYWAY. The reason
        # is the element three lines up from it in the same section: node 118,
        # the legend's DONE dot, which Design DOES name. That legend is a KEY,
        # and what it keys is these segments — `● DONE` beside a stack of
        # `--st-ink` blocks is one statement, not two. Moving the key to
        # espresso and leaving its referent near-black would leave the legend
        # telling a student that a colour they can see means something, in a
        # colour that is no longer on the page. Faithfulness to Design's list,
        # read literally, would have produced a page that contradicts itself.
        #
        # ⚑ AND THIS IS NOT THE REFUSAL THE `ring` NOTE RECORDS. That note
        # refuses `--wk-fill → var(--b-ground)` because the trough carries the
        # week's work as stacked segments and a THEMED fill would sink them into
        # it on five themes. Every word of that stands — and none of it applies
        # here, because espresso is a FIXED PAGE COLOUR, not a themed one. The
        # segment is #4A3728 on all six themes and on none of them does it move
        # with the ground behind it. Measured, on the two troughs the tile
        # actually uses: #4A3728 on `--st-rule-fact` #F0E6D3 and on
        # `--st-crumb-bg` #F7EDDC, both well clear of any confusion, and still
        # plainly distinct from the OPEN segment (`--st-accent`) and the MISSED
        # segment (`--err`) beside it.
        #
        # ⚠ ONLY THE DONE BRANCH MOVES. `'open'` stays `--st-accent` and
        # `'missed'` stays `--err`, byte-identical, because Design's amendment
        # is about page-chrome DARK and neither of those is dark. The anchor is
        # the whole line rather than the token: bare `var(--st-ink)` occurs
        # SEVEN times in Design's logic and anchoring on it would have matched
        # the wrong one — verified by counting, before this was written.
        (
            "        segs: items.map((w) => ({ bg: w.status === 'open' ? "
            "'var(--st-accent)' : w.status === 'missed' ? 'var(--err)' : "
            "'var(--st-ink)' })),",
            "        /* ⊕ RULED 23 Aug 2026 — the DONE segment is espresso, so\n"
            "           the legend's DONE dot above it still keys something\n"
            "           that is on the page. Open and missed are unchanged. */\n"
            "        segs: items.map((w) => ({ bg: w.status === 'open' ? "
            "'var(--st-accent)' : w.status === 'missed' ? 'var(--err)' : "
            "'var(--pg-strong)' })),",
        ),
        # ══════════════════════════════════════════════════════════════════
        # ⊕ 23 Aug 2026 — PHASE 1b. THE LOGIC HALF OF THE THEME PICKER.
        # ══════════════════════════════════════════════════════════════════
        #
        # ⚠️ `GRAFT` COPIES MARKUP AND NOTHING ELSE. It deep-copies a donor
        # SUBTREE and renumbers it; it never touches the logic class. Design's
        # account sheet is `if accountOpen` wrapped around six buttons carrying
        # `onClick={{ pickClay }}` … `{{ pickGraphite }}` and
        # `data-on={{ isClay }}` … `{{ isGraphite }}`, and the LIVE logic class
        # has none of those thirteen names.
        #
        # What that costs if it is forgotten is not an error. `build` resolves
        # an `if` with `lookup(node.e, scope, null)` — miss list deliberately
        # null — so an absent `accountOpen` reads `undefined`, the branch is
        # skipped, and the sheet RENDERS NOTHING, silently, on a page whose
        # build printed a graft and whose gates would all stay green. Every one
        # of the thirteen is therefore written here, by hand, against the live
        # page's own state rather than copied out of Design's self-contained
        # sample (whose `week`/`filter`/`lbweek`/`bench` state would collide
        # with ours).
        #
        # Design's NAMES are kept exactly, because Design's markup is what
        # resolves them. Design's VALUES are kept where they are pure
        # presentation — the `'1'`/`'0'` strings below are Design's, and they
        # have to be strings; see the note beside them.
        (
            'class Component extends DCLogic {',
            "/* ⊕ 23 Aug 2026 — PHASE 1b. WHERE A STUDENT'S THEME ACTUALLY GOES.\n"
            "\n"
            "   The same seam the assignment page already uses for answers, and the\n"
            "   same two rules: `window.__MRB_SINK__` is a WRITER and never a data\n"
            "   source, and it is read LAZILY on every call. The logic script runs\n"
            "   before `student-live.js` has loaded, so a reference captured at\n"
            "   evaluation time would be null forever and every theme a student\n"
            "   chose would be dropped on the floor without a word.\n"
            "\n"
            "   On the fixture page there is no sink, every call is a no-op\n"
            "   returning null, and the picker behaves exactly as Design's own file\n"
            "   does — it paints and it ticks. That is deliberate: the gates drive\n"
            "   the fixture, and a gate that had to reach a network would not be a\n"
            "   gate. */\n"
            "function _sink() {\n"
            "  return (typeof window !== 'undefined' && window.__MRB_SINK__) || null;\n"
            "}\n"
            "function _sinkCall(name, arg) {\n"
            "  var s = _sink();\n"
            "  if (!s || typeof s[name] !== 'function') { return null; }\n"
            "  try { return s[name](arg); } catch (e) { return null; }\n"
            "}\n"
            "class Component extends DCLogic {",
        ),
        (
            "    view: 'class', w: 1200, menu: false,",
            "    /* ⊕ 23 Aug 2026 — PHASE 1b. Two keys, and both are read by\n"
            "       Design's grafted markup rather than by anything of ours.\n"
            "\n"
            "       `theme` is SEEDED FROM THE PAGE, not from a constant.\n"
            "       `student-live.js` writes `data-bench-theme` onto\n"
            "       documentElement in `buildClass`, BEFORE `__MRB_MOUNT__()` is\n"
            "       called, so by the time this initialiser runs the student's\n"
            "       saved preference is already on the page and reading it back is\n"
            "       reading the one value that is true. Seeding it with a literal\n"
            "       'harbour' instead would have opened every sheet with the\n"
            "       harbour swatch ticked for a student sitting on damson — the\n"
            "       page correct and the picker lying about it.\n"
            "\n"
            "       NO ATTRIBUTE IS HARBOUR, which is the column's own contract:\n"
            "       NULL means no preference, `:root` carries harbour's values, and\n"
            "       the fallback here says the same thing in the same words. */\n"
            "    account: false,\n"
            "    theme: (typeof document !== 'undefined' && document.documentElement\n"
            "      && document.documentElement.getAttribute('data-bench-theme'))\n"
            "      || 'harbour',\n"
            "    view: 'class', w: 1200, menu: false,",
        ),
        (
            "  toggleMenu = () => this.setState((s) => ({ menu: !s.menu }));",
            "  toggleMenu = () => this.setState((s) => ({ menu: !s.menu }));\n"
            "\n"
            "  /* ⊕ 23 Aug 2026 — PHASE 1b. THE BENCH THEME PICKER. */\n"
            "  benchThemes = ['clay', 'chalk', 'moss', 'harbour', 'damson', 'graphite'];\n"
            "\n"
            "  /* Both Settings controls are Design's `<a href=\"#top\">`, and the\n"
            "     href is still on them — `SET_ON` adds a handler, it does not\n"
            "     rewrite markup. Without `preventDefault` the sheet would open and\n"
            "     the page behind it would jump to the top at the same moment, which\n"
            "     is the half of P7's original complaint that has nothing to do with\n"
            "     the handler. `menu: false` closes the dropdown the phone opened to\n"
            "     get here, so the student is not left with a menu behind a sheet. */\n"
            "  openAccount = (e) => {\n"
            "    if (e && e.preventDefault) { e.preventDefault(); }\n"
            "    this.setState({ account: true, menu: false });\n"
            "  };\n"
            "  closeAccount = () => this.setState({ account: false });\n"
            "\n"
            "  /* PAINT AND TICK IN ONE PLACE, deliberately. The attribute on\n"
            "     documentElement is what the six `[data-bench-theme]` rules key on;\n"
            "     `state.theme` is what the six `data-on` values key on. They are\n"
            "     two statements about one preference, and anything that moves one\n"
            "     without the other leaves a page wearing damson with harbour\n"
            "     ticked. This is also the path a FAILED WRITE takes back. */\n"
            "  showBenchTheme = (t) => {\n"
            "    if (typeof document !== 'undefined' && document.documentElement) {\n"
            "      document.documentElement.setAttribute('data-bench-theme', t);\n"
            "    }\n"
            "    this.setState({ theme: t });\n"
            "  };\n"
            "\n"
            "  /* OPTIMISTIC, AND HONEST ABOUT FAILING.\n"
            "\n"
            "     The paint happens first and the network is never waited on: a\n"
            "     colour a student asked for has to arrive under their finger, not\n"
            "     after a round trip to Frankfurt on a school wifi.\n"
            "\n"
            "     ⚠️ WHAT HAPPENS WHEN THE WRITE FAILS IS A RULING, not an\n"
            "     oversight. The tick is not decoration — it is the page saying\n"
            "     THIS IS YOUR SAVED PREFERENCE. If the write did not land, that\n"
            "     sentence is false, and it stays false until the student reloads\n"
            "     tomorrow on a different machine and finds their theme gone with no\n"
            "     idea when it went. So a failure puts the previous theme back —\n"
            "     visibly, under their eye, in the moment they can simply press it\n"
            "     again — and the page never claims a preference the database does\n"
            "     not hold. The alternative (keep the colour, log the error) is the\n"
            "     hand-in stamp defect this port already removed once: a false\n"
            "     confirmation is worse than a visible failure, because it stops the\n"
            "     student worrying about it.\n"
            "\n"
            "     ⚠️ THERE IS DELIBERATELY NO \"same theme, do nothing\" SHORTCUT,\n"
            "     and the first draft had one. It looks free and it is not, because\n"
            "     the page's theme and the DATABASE's theme are not the same fact.\n"
            "     A student who has never chosen sits on harbour with `bench_theme`\n"
            "     NULL — no preference. Pressing HARBOUR is that student CHOOSING\n"
            "     harbour, and with the shortcut in place it wrote nothing at all,\n"
            "     so the row stayed NULL and their choice would silently follow the\n"
            "     default the day the default moved. NULL means 'never chose'; it\n"
            "     cannot also mean 'chose the thing that is currently default'.\n"
            "     The cost of dropping it is one redundant PATCH of a few dozen\n"
            "     bytes when a student presses the swatch they are already on.\n"
            "\n"
            "     `ok === false` rather than a throw is the sink's own vocabulary:\n"
            "     `_sinkCall` swallows exceptions by design, so the writer reports a\n"
            "     refusal by RESOLVING false. A null return (no sink at all, which is\n"
            "     every fixture and every gate) takes neither branch and the picker\n"
            "     behaves exactly as Design's file does. */\n"
            "  pickBenchTheme = (t) => {\n"
            "    if (this.benchThemes.indexOf(t) < 0) { return; }\n"
            "    const was = this.state.theme;\n"
            "    this.showBenchTheme(t);\n"
            "    const out = _sinkCall('saveBenchTheme', t);\n"
            "    if (out && typeof out.then === 'function') {\n"
            "      const back = () => this.showBenchTheme(was);\n"
            "      out.then(function (ok) { if (ok === false) { back(); } }, back);\n"
            "    }\n"
            "  };",
        ),
        (
            "      nav: nav, menuOpen: st.menu, toggleMenu: this.toggleMenu,",
            "      nav: nav, menuOpen: st.menu, toggleMenu: this.toggleMenu,\n"
            "      /* ⊕ 23 Aug 2026 — PHASE 1b. Thirteen names Design's grafted\n"
            "         markup resolves out of this object. The spellings are\n"
            "         Design's and are not negotiable: one letter out and the\n"
            "         swatch is a dead control on a page that still builds. */\n"
            "      openAccount: this.openAccount,\n"
            "      closeAll: this.closeAccount,\n"
            "      accountOpen: st.account,\n"
            "      pickClay: () => this.pickBenchTheme('clay'),\n"
            "      pickChalk: () => this.pickBenchTheme('chalk'),\n"
            "      pickMoss: () => this.pickBenchTheme('moss'),\n"
            "      pickHarbour: () => this.pickBenchTheme('harbour'),\n"
            "      pickDamson: () => this.pickBenchTheme('damson'),\n"
            "      pickGraphite: () => this.pickBenchTheme('graphite'),\n"
            "      /* '1' AND '0' AS STRINGS, WHICH IS DESIGN'S OWN CHOICE AND IS\n"
            "         LOAD-BEARING TWICE. The selected treatment is\n"
            "         `.sw[data-on=\"1\"]`, an attribute-VALUE match, so a boolean\n"
            "         true would write `data-on=\"true\"` and no swatch would ever\n"
            "         tick. And the runtime SKIPS an attribute whose resolved value\n"
            "         is `false`, so the unselected five would lose the attribute\n"
            "         altogether rather than carrying '0'. Both failures look like\n"
            "         a CSS problem and neither is. */\n"
            "      isClay: st.theme === 'clay' ? '1' : '0',\n"
            "      isChalk: st.theme === 'chalk' ? '1' : '0',\n"
            "      isMoss: st.theme === 'moss' ? '1' : '0',\n"
            "      isHarbour: st.theme === 'harbour' ? '1' : '0',\n"
            "      isDamson: st.theme === 'damson' ? '1' : '0',\n"
            "      isGraphite: st.theme === 'graphite' ? '1' : '0',",
        ),
    ],
    'assignment': [
        (
            '    const n = Math.round(this.props.questionCount ?? 15);\n    return Math.max(6, Math.min(this.questions.length, n));',
            '    /* ⊕ RULED 22 Aug 2026 — THE FLOOR OF SIX IS THE BUG. THE CAP IS NOT.\n\n       Design\'s own assignment note requires the marker strip to read the real\n       length — "it does not assume fifteen" — and the floor of SIX broke that\n       in the direction that mattered: with four real questions this returned\n       6, the page then indexed `questions[4]` and `questions[5]`, found\n       undefined, and refused to open. The refusal was honest. The floor was\n       wrong. It drops to 1, which is the only number that is not an\n       assumption.\n\n       ⚠️ THE `?? 15` STAYS, and the first draft of this ruling removed it and\n       went red. It reads like an inert default — nothing passes\n       `questionCount`; the mount emits `props: {}` — but Design\'s own fixture\n       array is SIXTEEN questions long and Design renders fifteen, so the 15 is\n       a working CAP that `Math.min` applies, not a fallback that never fires.\n       Taking it out made the fixture render "16 QUESTIONS" and diverged nine\n       behaviour drives at the same character.\n\n       And 15 is the right cap, independently: `ASSIGNMENT_SIZE` in\n       `assignment-compose.js` is 15, so the producer never composes more. A\n       real assignment SHORTER than 15 now shows its real length, which is the\n       whole point; a longer one cannot exist. Proved at 4, 6, 12 and 15. */\n    const n = Math.round(this.props.questionCount ?? 15);\n    return Math.max(1, Math.min(this.questions.length, n));',
        ),
        (
            'class Component extends DCLogic {',
            "/* ⊕ RULED 22 Aug 2026 — WHERE A STUDENT'S WORK ACTUALLY GOES.\n\n   `window.__MRB_SINK__` is set by `shared/student-live.js` immediately before\n   it mounts, and by nothing else. It is a WRITER, not a data source: the page\n   still reads everything it renders through `MRB_DATA`, and the rule that the\n   production page has no code path to Design's example data is untouched.\n\n   It is read LAZILY, on every call, and never captured at script-evaluation\n   time — the logic script runs before `student-live.js` has loaded, so a\n   captured reference would be null forever and every answer would be silently\n   dropped. That is precisely the failure this whole unit exists to remove, and\n   it would have been invisible.\n\n   On the fixture page there is no sink, every call is a no-op returning null,\n   and Design's behaviour is exactly what it was. That is deliberate: the gates\n   drive the fixture, and a gate that had to reach a network would not be a\n   gate. */\nfunction _sink() {\n  return (typeof window !== 'undefined' && window.__MRB_SINK__) || null;\n}\nfunction _sinkCall(name, arg) {\n  var s = _sink();\n  if (!s || typeof s[name] !== 'function') { return null; }\n  /* A save that throws must never take the answer off the screen with it. The\n     student answered; what happens to the network afterwards is not their\n     problem and is not their feedback. */\n  try { return s[name](arg); } catch (e) { return null; }\n}\nclass Component extends DCLogic {",
        ),
        (
            '    const off = this.isOffline();\n    this.lastAct = Date.now();\n    this.setState((p) => {\n      const a = Object.assign({}, p.answers); a[p.idx] = oi;\n      const h = Object.assign({}, p.held); if (off) h[p.idx] = 1;\n      return { answers: a, held: h, resumed: false, paused: false };\n    }, () => this.saveLive());',
            "    /* \u2295 RULED 23 Aug 2026 \u2014 THE HELD MARK IS A FACT, NOT AN INTENTION.\n\n       \u26d4 What this replaces set `held[idx]` from `isOffline()` alone, before\n       anything had been written anywhere. The page told the student\n       HELD ON THIS DEVICE about an answer that was in a variable and would die\n       with the tab \u2014 a reload, a closed tab, a phone locking itself, and the\n       tick they had already seen was all that was ever left of it.\n\n       So the sink is asked FIRST, synchronously, and the claim is made out of\n       what it reports: `held` is set only when the answer is genuinely on the\n       device and will still be there after the tab is closed. When it is not\n       \u2014 a store that is full, disabled, or private \u2014 nothing is marked held,\n       and `notKept` records it instead so the header can say the true thing\n       rather than the comfortable one.\n\n       \u26a0\ufe0f Without a sink \u2014 the fixture, and only the fixture \u2014 `kept` falls\n       back to `off` and Design's behaviour is byte for byte what it was. */\n    const off = this.isOffline();\n    const at = s.idx;\n    this.lastAct = Date.now();\n    /* W1. THE ANSWER GOES TO THE SERVER HERE, NOW. Not batched, not held until\n       the end: the submission row is created by the first of these and the\n       work is safe from question one. The call is idempotent per\n       (submission, question) at the database, so changing an answer updates\n       that row rather than adding a second \u2014 which is why re-confirming is\n       harmless and why no bookkeeping is needed here.\n\n       It runs BEFORE the setState rather than inside its callback, and that is\n       deliberate twice over: the state is not its input (it is handed the\n       index and the option), and its answer decides what the state is allowed\n       to say. Asking afterwards would mean claiming first and checking second,\n       which is the defect this ruling removes. */\n    const r = _sinkCall('saveAnswer', { index: at, option: oi, offline: off });\n    const kept = r ? !!r.held : off;\n    this.setState((p) => {\n      const a = Object.assign({}, p.answers); a[at] = oi;\n      const h = Object.assign({}, p.held); if (kept) h[at] = 1;\n      const nk = Object.assign({}, p.notKept || {});\n      if (off && !kept) nk[at] = 1; else delete nk[at];\n      return { answers: a, held: h, notKept: nk, resumed: false, paused: false };\n    }, () => this.saveLive());",
        ),
        (
            "  /* answers made offline are held on the device, then sent one at a time */\n  drain() {\n    const ids = Object.keys(this.state.held);\n    this.setState({ net: 'sent', sentN: ids.length });\n    let i = 0;\n    clearInterval(this.drainT);\n    this.drainT = setInterval(() => {\n      if (i >= ids.length) {\n        clearInterval(this.drainT);\n        setTimeout(() => this.setState({ net: null }), 1100);\n        return;\n      }\n      const k = ids[i++];\n      this.setState((s) => { const h = Object.assign({}, s.held); delete h[k]; return { held: h }; }, () => this.saveLive());\n    }, 130);\n  }",
            "  /* \u2295 RULED 23 Aug 2026 \u2014 A HATCH CLEARS WHEN THE ANSWER HAS ACTUALLY GONE.\n\n     \u26d4 What this replaces ran a 130ms timer and deleted one held key per\n     tick, whatever was happening on the wire, and headed it\n     `BACK ONLINE \u00b7 03 SENT`. On Design's own page that is honest \u2014 nothing\n     is being sent, it is a DRAWING of sending. On a real one it is the\n     hand-in stamp again: three answers announced as sent while the request\n     carrying them was failing.\n\n     With a sink, `held` is a PROJECTION of what is still on the device. Each\n     tick asks the sink what is left and removes exactly what has left; what is\n     still waiting stays hatched, because it is still waiting. `sentN` counts\n     what actually went.\n\n     Without a sink \u2014 the fixture, and only the fixture \u2014 Design's animation\n     is untouched, which is why it is copied out whole rather than adapted. */\n  drain() {\n    const ids = Object.keys(this.state.held);\n    if (!_sink()) {\n      this.setState({ net: 'sent', sentN: ids.length });\n      let i = 0;\n      clearInterval(this.drainT);\n      this.drainT = setInterval(() => {\n        if (i >= ids.length) {\n          clearInterval(this.drainT);\n          setTimeout(() => this.setState({ net: null }), 1100);\n          return;\n        }\n        const k = ids[i++];\n        this.setState((s) => { const h = Object.assign({}, s.held); delete h[k]; return { held: h }; }, () => this.saveLive());\n      }, 130);\n      return;\n    }\n    this.setState({ net: 'sent', sentN: 0 });\n    let ticks = 0;\n    clearInterval(this.drainT);\n    this.drainT = setInterval(() => {\n      const still = _sinkCall('pending', null) || {};\n      this.setState((s) => {\n        const h = {};\n        Object.keys(s.held).forEach((k) => { if (still[k]) h[k] = 1; });\n        return { held: h, sentN: ids.length - Object.keys(h).length };\n      }, () => this.saveLive());\n      ticks += 1;\n      /* It stops when there is nothing left, and it stops anyway. An answer\n         the backend will not take stays hatched rather than keeping a banner\n         alive for the rest of the lesson \u2014 the hatch is the truth about it. */\n      if (!Object.keys(this.state.held).length || ticks >= 60) {\n        clearInterval(this.drainT);\n        setTimeout(() => this.setState({ net: null }), 1100);\n      }\n    }, 130);\n  }",
        ),
        (
            "    const netNote = st.net === 'sent'\n      ? 'BACK ONLINE \\u00B7 ' + pad(st.sentN || 0) + ' SENT'\n      : offline ? 'OFFLINE \\u00B7 ' + pad(heldKeys.length) + ' HELD ON THIS DEVICE' : '';",
            "    /* \u2295 RULED 23 Aug 2026 \u2014 AND WHAT IT SAYS WHEN THE ANSWER IS NOT HELD.\n\n       An answer given offline that the device would not keep is not held, so\n       the page may not print the held count at it. It prints that sentence's\n       literal negation, in Design's own grammar, with a real number:\n\n           OFFLINE \u00b7 01 NOT HELD ON THIS DEVICE\n\n       \u00a78.10: it says something true about the student's WORK \u2014 their answer,\n       counted \u2014 and nothing whatever about storage, quotas, private browsing,\n       or the platform. There is no hatch legend beside it, because there is\n       nothing hatched.\n\n       When both exist the NOT-HELD count wins, because it is the fact that\n       changes what the student should do next. In practice a store either\n       works from the first answer or from none, so both is close to\n       unreachable.\n\n       `st.notKept` is undefined on the fixture, which reads as none, which\n       leaves Design's line exactly as drawn. */\n    const notKept = Object.keys(st.notKept || {});\n    const netNote = st.net === 'sent'\n      ? 'BACK ONLINE \\u00B7 ' + pad(st.sentN || 0) + ' SENT'\n      : offline\n        ? (notKept.length\n            ? 'OFFLINE \\u00B7 ' + pad(notKept.length) + ' NOT HELD ON THIS DEVICE'\n            : 'OFFLINE \\u00B7 ' + pad(heldKeys.length) + ' HELD ON THIS DEVICE')\n        : '';",
        ),
        (
            "  handIn = () => {\n    const stamp = this.state.late ? '20 SEP, 19:07' : '17 SEP, 20:41';\n    this.setState({ handing: true, handedAt: stamp, sheet: false, zoom: false }, () => this.saveLive());\n    clearTimeout(this.handT);\n    this.handT = setTimeout(() => this.setState({ handing: false, view: 'done' }, () => this.saveLive()), 1350);\n  };",
            "  /* ⊕ RULED 22 Aug 2026 — W3. THIS BUTTON MARKS THE WORK FINISHED.\n     IT DOES NOT SAVE IT. Saving already happened, one answer at a time.\n\n     ⛔ WHAT THIS REPLACES, because it is the worst defect the page had and the\n     reason the swap was refused twice:\n\n         const stamp = this.state.late ? '20 SEP, 19:07' : '17 SEP, 20:41';\n\n     A HARDCODED DATE, posted to NO ENDPOINT. A student pressing it was told\n     they handed in on 17 September, whatever today was, and their work never\n     reached their teacher. A false confirmation is worse than a visible\n     failure, because the student stops worrying about it.\n\n     Now the stamp comes back from the server or it does not appear at all.\n     `is_late` comes back with it — lateness is a fact about the clock decided\n     once, at the database, and never a guess made on the device. Nothing here\n     checks the due date, because nothing is locked by it (ruling 5).\n\n     Idempotent at both ends: this returns early if a completion is already in\n     flight or done, and the route returns the first press's row if it is not. */\n  handIn = () => {\n    if (this.state.handedAt || this.state.handing) return;\n    this.setState({ handing: true, sheet: false, zoom: false }, () => this.saveLive());\n    clearTimeout(this.handT);\n    const settle = (r) => {\n      this.setState((p) => ({\n        handing: false, view: 'done',\n        handedAt: (r && r.stamp) || '',\n        late: r && r.late != null ? !!r.late : p.late\n      }), () => this.saveLive());\n    };\n    const out = _sinkCall('complete', this.state.elapsed);\n    if (out && typeof out.then === 'function') {\n      /* The catch settles rather than rethrowing: a student who has finished\n         must reach the end screen even if the confirmation does not arrive.\n         Their answers are already saved, and the completion is retried by the\n         next visit, which reads its state from the server. */\n      out.then(settle, function () { settle(null); });\n      return;\n    }\n    this.handT = setTimeout(() => settle(out), 1350);\n  };",
        ),
        (
            "  loadLive() {\n    const empty = { answers: {}, sels: {}, held: {}, idx: 0, elapsed: 0, view: 'q', handedAt: null, resumed: false, late: false, sheet: false, zoom: false, handing: false, net: null };\n    try {",
            "  loadLive() {\n    const empty = { answers: {}, sels: {}, held: {}, idx: 0, elapsed: 0, view: 'q', handedAt: null, resumed: false, late: false, sheet: false, zoom: false, handing: false, net: null };\n    /* ⊕ RULED 22 Aug 2026 — W2. THE SERVER IS THE TRUTH; THE BROWSER IS A CACHE.\n       A student on the school computer on Monday and their phone on Thursday\n       must see the same state, and localStorage cannot do that — it is per\n       device and it is per browser profile. So when there is a sink, its\n       resume state wins outright and the local copy is not even consulted.\n       Without one (the fixture, and only the fixture) Design's localStorage\n       behaviour is exactly what it was. */\n    const fromServer = _sinkCall('resume', null);\n    if (fromServer) { return Object.assign(empty, fromServer); }\n    try {",
        ),
        (
            "  applyScenario(scn) {\n    const live = scn === 'Live, saved';",
            "  applyScenario(scn) {\n    /* ⊕ RULED 22 Aug 2026 — DEMO SCENARIOS ARE NOT REACHABLE IN PRODUCTION.\n       Design routes the scenario off the URL hash and falls back to 'Mid-way',\n       which pre-fills six answers with three deliberately wrong. On a real\n       student's assignment that is not a default, it is a lie — and worse, the\n       'Handed in' scenarios would show a child a completion that never\n       happened. A live page must not be able to reach any of them by hash.\n\n       When a sink is present there is exactly one scenario and it is the\n       student's own saved state. This replaces the `#live` history rewrite\n       `student-live.js` was doing from outside, which the last run recorded as\n       a workaround belonging in the page. It now is in the page. */\n    if (_sink()) { scn = 'Live, saved'; }\n    const live = scn === 'Live, saved';",
        ),
        (
            "      screenLabel: onDone ? (st.late ? 'Handed in late' : 'Handed in') : handed ? 'Review' : 'Question ' + pad(idx + 1),",
            "      /* ⊕ RULED 22 Aug 2026 — W5. “Complete” replaces the old wording everywhere.\n         The button marks the work finished; it does not transfer it, because\n         the transfer happened one answer at a time all week. Design's\n         typography and placement are untouched — only the words change. */\n      screenLabel: onDone ? (st.late ? 'Completed late' : 'Complete') : handed ? 'Review' : 'Question ' + pad(idx + 1),",
        ),
        (
            "      doneEyebrow: 'Handed in ' + (st.handedAt || '') + (st.late ? ' \\u00B7 2 days late' : ''),",
            '      /* The stamp is whatever the server said, and nothing when it said\n         nothing — never a manufactured date. The separator goes with it, so an\n         absent stamp leaves "Completed" rather than "Completed ·". */\n      doneEyebrow: \'Completed\' + (st.handedAt ? \' \' + st.handedAt : \'\') + (st.late ? \' \\u00B7 \' + MRB_DATA(\'lateText\') : \'\'),',
        ),
        (
            "      doneKicker: st.late ? 'Marked \\u00B7 handed in late' : 'Marked \\u00B7 week 04',",
            "      doneKicker: st.late ? 'Marked \\u00B7 completed late' : (MRB_DATA('weekLabel') ? 'Marked \\u00B7 ' + MRB_DATA('weekLabel').toLowerCase() : 'Marked'),",
        ),
        (
            "      headMeta: 'WEEK 04 \\u00B7 ' + total + ' QUESTIONS',\n      dueLead: 'CELLS & MICROSCOPY \\u00B7 ' + this.DUE,\n      dueFlag: st.late ? '\\u00B7 2 DAYS LATE' : '',",
            '      /* ⊕ RULED 22 Aug 2026 — three welded values in one line of Design\'s.\n         The week was 04 for every class in every week of every year; the topic\n         was one real class\'s; and "2 DAYS LATE" was a fixed number of days\n         printed over whatever the real overdue period happened to be.\n         `topicTitle` is already bound from the markup, so nothing new is\n         carried for it — the same key, upper-cased for this position. */\n      headMeta: (MRB_DATA(\'weekLabel\') ? MRB_DATA(\'weekLabel\') + \' \\u00B7 \' : \'\') + total + \' QUESTIONS\',\n      dueLead: MRB_DATA(\'topicTitle\').toUpperCase() + \' \\u00B7 \' + this.DUE,\n      dueFlag: st.late ? \'\\u00B7 \' + MRB_DATA(\'lateText\').toUpperCase() : \'\',',
        ),
        (
            'class Component extends DCLogic {',
            '\n/* One definition of "is this feedback line actually authored", used by both the\n   places a line surfaces: the option card while answering, and the review screen\n   at the end. See the ⊕ RULED 21 Aug note above `noteBlock` for why the right\n   answer\'s line is absent and why the slot must close rather than blank.\n   Returns \'\' — never undefined — so a missing line renders as the same closed\n   slot the idle and off states already produce, not as the string "undefined". */\nfunction _line(q, i) {\n  var s = q && q.f && q.f[i];\n  return (typeof s === \'string\' && s.trim()) ? s : \'\';\n}\nclass Component extends DCLogic {',
        ),
        (
            '    const sel = st.sels[idx];\n    const options = q.o.map((t, i) => {',
            '    const sel = st.sels[idx];\n    /* ⊕ RULED 21 Aug 2026 — the right answer\'s explanation line is DROPPED for v1,\n       and the slot must CLOSE rather than stand empty.\n\n       Design\'s §2 asks for four feedback strings per question so the pair reads\n       "why not that / why this". Measured across both content sources — 140 ladder\n       recall/apply rungs and 840 bank questions — the three that exist are always\n       the DISTRACTORS, and "why this" is authored nowhere. Authoring 980 pieces of\n       science prose is a term\'s work and it is Mide\'s gate, not the build\'s.\n\n       Ruled: v1 ships with three. The right answer is marked correct by the tick\n       and the word, with no line beneath it. The reasoning, recorded rather than\n       just obeyed: the teaching in a multiple-choice question lands on the MISTAKE.\n       A student who chose correctly does not need a paragraph confirming it, and\n       the lesson page is where the real explanation lives.\n\n       ⚠️ NOT a blanket suppression, and this is the one place the ruling is read\n       less than literally. `noteBlock` renders a line that IS authored and closes\n       the slot when one is not — because the same ruling says authored lines are\n       "content and welcome", and Design\'s own example data carries all four (its\n       right-answer lines open "Right. …"). Once the pages are wired to the real\n       content sources in phase 2, no correct option has a line anywhere, so both\n       readings ship exactly the same v1. This one just does not destroy the slot\n       on the way, and a fallback string appearing in 840 places is the thing\n       Design forbade — gated separately in student_parity.py.\n\n       Closing means dropping noteRule and noteColor too, not just blanking `note`.\n       Those carry the rule above the line and its padding; leaving them behind is\n       precisely the gap the ruling says must not appear. `idle` and `off` already\n       close it this way, which is the shape being matched. */\n    const noteBlock = (i, rule, color) => {\n      const s = _line(q, i);\n      return s ? { note: s, noteRule: rule, noteColor: color } : { note: \'\' };\n    };\n\n    const options = q.o.map((t, i) => {',
        ),
        (
            "        markColor: 'var(--ks3-ok-text)', status: 'RIGHT', statusColor: 'var(--ks3-ok-text)',\n        note: q.f[i], noteRule: 'var(--ok-border)', noteColor: 'var(--st-body)'\n      });",
            "        markColor: 'var(--ks3-ok-text)', status: 'RIGHT', statusColor: 'var(--ks3-ok-text)'\n      }, noteBlock(i, 'var(--ok-border)', 'var(--st-body)'));",
        ),
        (
            "        markColor: 'var(--err)', status: 'NOT THIS ONE', statusColor: 'var(--err)',\n        note: q.f[i], noteRule: 'var(--err-border)', noteColor: 'var(--st-body)'\n      });",
            "        markColor: 'var(--err)', status: 'NOT THIS ONE', statusColor: 'var(--err)'\n      }, noteBlock(i, 'var(--err-border)', 'var(--st-body)'));",
        ),
        (
            "        markColor: 'var(--ks3-ok)', status: 'THE ANSWER', statusColor: 'var(--ks3-ok-text)',\n        note: q.f[i], noteRule: 'var(--st-rule-soft)', noteColor: 'var(--st-muted)'\n      });",
            "        markColor: 'var(--ks3-ok)', status: 'THE ANSWER', statusColor: 'var(--ks3-ok-text)'\n      }, noteBlock(i, 'var(--st-rule-soft)', 'var(--st-muted)'));",
        ),
        (
            '        yourKey: keys[a], yourText: qq.o[a], yourNote: qq.f[a],\n        ansKey: keys[qq.a], ansText: qq.o[qq.a], ansNote: qq.f[qq.a],',
            "        yourKey: keys[a], yourText: qq.o[a], yourNote: _line(qq, a),\n        /* the correct option's line, closed when unauthored — see noteBlock above.\n           The review screen is the SECOND place it surfaces, and it was missed on\n           the first pass: closing it only on the question card would have left the\n           end-of-assignment review showing an empty rule under every right answer. */\n        ansKey: keys[qq.a], ansText: qq.o[qq.a], ansNote: _line(qq, qq.a),",
        ),
        (
            "    else window.location.href = 'Class View.dc.html';",
            '    else {\n      /* ⊕ RULED 22 Aug 2026 — THE FALLBACK WAS A DEAD LINK.\n         `Class View.dc.html` is DESIGN\'S OWN FILENAME inside Design\'s own\n         delivery, and it has never existed on this site. `history.back()`\n         above covers the ordinary path — a student who came from their class\n         page goes back to it — so this only bites the student who opened the\n         assignment directly, from a bookmark or a link in a message, and they\n         are exactly the student with no history to go back to. For them "Back\n         to 8r/Sc1" was a 404.\n\n         Nothing caught it because nothing drives navigation ACROSS pages: the\n         behaviour gate drives one page\'s states, and a href is not a state.\n\n         `?class=` is carried over when it is there. A student has one class\n         and does not need it; a teacher previewing does, and dropping a\n         parameter on the way back is how a preview quietly becomes somebody\n         else\'s page. */\n      var cls = new URLSearchParams(window.location.search).get(\'class\');\n      window.location.href = \'/student/class.html\'\n        + (cls ? \'?class=\' + encodeURIComponent(cls) : \'\');\n    }',
        ),
    ],
}


# ── attributes the ruling SETS on a template node, by `data-dc-tpl` ───────
#
# ⊕ 22 Aug 2026 — THE FOURTH MECHANISM, and it exists for the bench themes.
#
# Design's six themes are driven by one attribute on the page root and a token
# block scoped under it. The tokens they override — `--b-ground`, `--b-ink`,
# `--b-muted` — are Design's own namespace, and the live page does not use it:
# the live bench's ground is `--st-room-panel`, its title `--st-cream`, its
# accent `--st-ember`.
#
# ⚠️ REMAPPING THE `--st-*` FAMILY AT THE ROOT IS NOT SAFE, and the reason is
# one line of the live markup. `--st-cream` is declared "cream as used ON dark
# surfaces" and is a text colour eleven times — but it is also a BACKGROUND
# once, on the leaderboard's leader avatar, a cream disc carrying `--st-ink`
# text. Remap it globally and CHALK — the light theme, where `--b-ink` is
# #221E1B — turns that disc near-black under its near-black initials. The five
# dark themes would have looked perfect.
#
# So the theme override is scoped to the three surfaces that take it, and those
# surfaces are bare inline-styled `<section>`s with nothing to scope to. This
# gives them something. `SET_ON` attaches handlers; this attaches attributes,
# and refuses to overwrite one Design already wrote.
SET_ATTR = {
    # ⊕ 22 Aug 2026 — PHASE 2a. Six nodes, and every one is either the token
    # bridge's anchor or a handle for a gate. Read out of the COMPILED tree
    # node by node rather than off the markup — see MERGE-2026-08-23.md,
    # "Phase 2a — the theme bridge, MEASURED before it was written".
    #
    #   55   the bench `<section>`, `background:var(--st-room-panel)`. It
    #        takes BOTH names because they answer to different readers:
    #        `data-bench-surface` is what the token bridge in
    #        build_student_port.py scopes its ten declarations to, and
    #        `data-port-region` is DESIGN'S OWN marker name, which is how the
    #        behaviour gate's AMENDED_ADDITIONS machinery finds a region.
    #        Spelling one of them the other way would silently detach one of
    #        the two from the node it is about.
    #   91   the docket — the one PAPER card inside the dark bench,
    #        `background:var(--st-paper)`. Named so the ruling "the docket
    #        stays paper and ink on all six themes" has something to hold on
    #        to; see the bridge for why that is not free.
    #   107  the term spine, 249 the leaderboard — regions ONLY, no surface.
    #        Neither is painted by the bridge: the spine takes the theme
    #        through Design's own computed colour strings (`ring`, `numColor`,
    #        `trough`, `nowDot`), which is a LOGIC rewrite and a later unit.
    #        ⊕ 23 Aug 2026 — THAT LATER UNIT LANDED, and the sentence above is
    #        kept rather than corrected because it names all four strings and
    #        only ONE of them moved. `ring` now takes `var(--b-ground)`; see
    #        the RULED 23 Aug entry at the end of LOGIC['class view'] for why
    #        `trough`, `nowDot` and `numColor` are deliberately still page
    #        chrome, and why theming `numColor` would have been a new defect
    #        rather than a completion. The spine still takes NO surface
    #        attribute: it sits on the cream page ground, and a bridge scope
    #        there would remap `--st-ink` and `--st-cream` over page chrome.
    #   260  the leaderboard CARD, `background:var(--st-room-panel)` — the
    #        second surface the bridge paints, inside the region at 249.
    #   266  the leader's avatar disc. `background:var(--st-cream)`, and it is
    #        the ONE place in the class view where `--st-cream` is a
    #        background rather than text. That single line is why the bridge
    #        INVERTS this node instead of exempting it.
    #
    # ⊕ 23 Aug 2026 — PHASE 1a. TWO MORE, AND THEY ARE NOT SURFACES.
    #
    #   118  the term spine's legend DONE dot — a 9px disc,
    #        `background:var(--st-ink)`, sitting beside the word DONE.
    #   166  the work row's MARKED dot — the same disc at 13px, inside
    #        `if r.isMarked`. Its three siblings are `--st-accent` (open),
    #        `--err` (missed) and `--st-rule-strong` (pending); this is the
    #        only near-black one, which is the whole reason it is the only one
    #        named.
    #
    # Both are Design's OWN named page chrome — README change 1: *"no page
    # chrome is near-black any more. Page-chrome dark is now espresso #4A3728
    # … top rule, work-row and legend DONE dots."* — and both are drawn in the
    # amended delivery as `background:var(--pg-strong)`, at donor nodes 171 and
    # 142 respectively. So this adopts Design's own value for Design's own
    # element rather than inferring one.
    #
    # ⚑ WHY AN ATTRIBUTE AND A CSS RULE RATHER THAN A `LOGIC` REWRITE. The
    # colour is not computed — it is a LITERAL `var(--st-ink)` inside an inline
    # `style` attribute on a template node, so there is no string in Design's
    # logic to anchor on and `LOGIC` has nothing to bite. `SET_ATTR` plus a
    # scoped rule is the mechanism that reaches an inline declaration, and it
    # is the one `[data-bench-avatar]` already uses for exactly this shape.
    # See `_PAGE_STRONG` in build_student_port.py for the rule, and for why it
    # carries `!important`.
    #
    # ⚠ THE THIRD ELEMENT DESIGN NAMES — THE TOP RULE — IS NOT HERE, BECAUSE
    # THE LIVE PAGE DOES NOT HAVE ONE. Design's amended delivery draws a 5px
    # `var(--pg-strong)` bar above the topbar (donor node 10); Design's
    # ORIGINAL delivery, which the live page is ported from, has no such node
    # and neither does the port — measured in a browser, not inferred: there is
    # no element of any colour in the top 40px of the page under 10px tall.
    # So the top rule is not a near-black element that needs moving; it is
    # markup that would have to be ADDED, by a `GRAFT` of donor node 10, and
    # that node carries neither `data-port-region` nor `data-port-change` —
    # Design's own signal that it is not a declared amendment to an existing
    # region. Adding a visible bar to the top of every student's class page on
    # the strength of a README noun is a design decision, not a colour port.
    # Mapped here so it is one line of work whenever it is ruled; deliberately
    # not taken.
    "class view": {
        55:  {"data-bench-surface": "bench", "data-port-region": "bench"},
        91:  {"data-bench-docket": "1"},
        107: {"data-port-region": "term-spine"},
        118: {"data-page-strong": "legend-done"},
        166: {"data-page-strong": "work-row-done"},
        249: {"data-port-region": "leaderboard"},
        260: {"data-bench-surface": "board"},
        266: {"data-bench-avatar": "1"},
    },
    # The assignment page has no bench, no spine and no leaderboard. Nothing
    # to name, and naming it anyway would move that page's bytes for nothing.
    "assignment": {},
}


# ── subtrees GRAFTED from Design's amended delivery ───────────────────────
#
# ⊕ 22 Aug 2026 — THE FIFTH MECHANISM, and the keystone of the amendments port.
#
# Every mechanism above this one REMOVES or REBINDS something Design already
# drew, because until now every ruling did. None of them can ADD MARKUP.
#
# Design's class-view amendments need markup added: a theme picker of six
# swatches, a flashcard overlay, a recall round and a done bench, none of which
# exist on the live page. And they must NOT be added by replacing the live
# template with Design's file — see PORT2-2026-08-22.md. Design's delivery is a
# self-contained SAMPLE: 18 conditional branches against the live page's 45, 7
# loops against 14. Adopting it wholesale would delete every empty state, every
# work-row status, the entire `wide`/`narrow` responsive treatment, the
# leaderboard movement arrows, and would flatten the lessons list to Design's
# four literal cards.
#
# So the port MERGES BY REGION. Design's README declares which regions changed
# and marks them `data-port-change`; the four that carry only `data-port-region`
# — crumbs, hero, work-list, lessons-panel — are left exactly as they are.
#
# Each entry:
#     at     `data-dc-tpl` of the LIVE node to anchor on
#     mode   "replace" | "append" | "prepend" | "after"
#     donor  `data-dc-tpl` of the node in `class view amendments` whose
#            SUBTREE is copied
#     why    a sentence. Required — a graft with no stated reason is a
#            redesign nobody signed off.
#
# ⚠️ GRAFTED NODES ARE RENUMBERED into a reserved range (`GRAFT_BASE` +
# Design's own index) rather than keeping Design's numbers. `data-dc-tpl` has
# to stay unique — PRUNE, SET_ON, SET_ATTR, the parity gate and the binding
# index paths are all keyed on it, and the donor's 0..449 overlap the live
# page's 0..403 almost exactly. Adding a fixed base keeps them unique AND
# keeps them readable: node 10312 on the built page is Design's node 312, and
# subtracting is how you find it in the delivery.
GRAFT_BASE = 10000

GRAFT = {
    "class view": [
        # ⊕ 22 Aug 2026 — PHASE 2a, and the first graft the port has ever
        # applied. Design's node 7 is a single `<style>`: the `--pg-*`, `--t-*`
        # and `--b-*` families on `:root` with HARBOUR as the default, the six
        # `[data-bench-theme="…"]` rules, and the state classes.
        #
        # It is PREPENDED into the live page root (node 9) rather than typed
        # into the `<style>` build_student_port.py emits, for the same reason
        # the brand SVG is captured rather than retyped: it is Design's
        # stylesheet, and a copy of it would drift the first time somebody
        # tidied one of the six themes.
        #
        # ⚠️ MEASURED SAFE BEFORE IT WAS WRITTEN, not assumed. The live page
        # references ZERO `--pg-*` tokens and `shared/student-ds.css` defines
        # none, so the whole `:root` block is purely additive — it cannot
        # re-point anything already on the page. The state classes are inert
        # for the same reason: the live class view carries exactly three class
        # names (`rd`, `eyebrow`, `kchip`) and Design's rules key on `wk`,
        # `tab`, `lbchip`, `sw`, `stbtn`, `pip`, `opt`, `rprog` and `fcflip`,
        # none of which exist on it yet. They arrive with the subtrees that
        # use them, in later units.
        #
        # The two rules that DO reach the rest of the page are `body{}` and
        # `a{}`/`a:hover{}`, which sit in the same block and land after the
        # emitted `<style>` in document order, so they win. MEASURED in a
        # browser, before and after, rather than reasoned about:
        #
        #   body background       rgb(251,243,230) → rgb(251,243,230)  same
        #   -webkit-font-smoothing  antialiased → antialiased          same
        #   link colour           rgb(169,52,17) → rgb(169,52,17)      same
        #   link :hover colour    rgb(127,36,8)  → rgb(127,36,8)       same
        #   body text-wrap        wrap → PRETTY                        NEW
        #   link :hover           no underline → UNDERLINE             NEW
        #
        # `var(--pg-ground)` is the same #FBF3E6 the emitted rule already
        # carried, `--pg-accent-text`/`-hover` are the same values as
        # `--ks3-accent-text`/`-hover`, and student-ds.css's own `body` rule
        # was already antialiasing. So exactly two things change outside the
        # bench, both of them Design's own treatment of a page Design drew:
        # links underline on hover, and the body balances its last lines. They
        # are adopted rather than stripped — but adopted KNOWINGLY, which is
        # what this paragraph is for.
        dict(at=9, mode="prepend", donor=7,
             why="Design's six-theme token block — the --pg-/--t-/--b- "
                 "families with harbour as :root's default, the six "
                 "[data-bench-theme] rules and the state classes. Every "
                 "themed surface on the page resolves a --b-* token, so the "
                 "block has to be ON the page before any of them can paint, "
                 "and it is grafted from Design's file rather than retyped "
                 "so the six themes cannot drift from the delivery."),

        # ⊕ 23 Aug 2026 — PHASE 1b + 1c. THE ACCOUNT SHEET AND ITS PICKER.
        #
        # Donor 243 is Design's `<if accountOpen>`; its subtree is the whole
        # sheet — the scrim, the 460px panel, the close button, the identity
        # block, the TEACHER / TERM / EMAIL rows, and the BENCH THEME block
        # with the six `class="sw"` swatches at donor 270/278/286/294/302/310.
        #
        # ── WHY node 10, and WHY append ──────────────────────────────────
        #
        # Node 10 is `.rd[data-mode="ks3"]` — the DESIGN ROOT, and the direct
        # counterpart of the donor's own node 8, which is the `.rd` Design's
        # sheet is drawn inside. The sheet goes at the END of it.
        #
        #   INSIDE `.rd`, and this is not a preference. Everything that reads
        #   this page reads it through `.rd[data-mode="ks3"]`:
        #   `student_behaviour`'s text and control census and
        #   `student_controls_drive`'s press sweep both open with
        #   `document.querySelector('.rd[data-mode="ks3"]')`. Node 9 — the
        #   outer `<div>` the token block was prepended into — is its PARENT,
        #   and a sheet grafted there is a control surface no gate can see
        #   while being perfectly visible to a student. That was tried first
        #   and the drive found it: six live swatches, and every gate reading
        #   an empty sheet.
        #
        #   LAST, because it is `position:fixed;inset:0;z-index:40` and it has
        #   to paint over the page. z-index alone does not settle it — the
        #   header at node 11 carries `z-index:20` inside a `position:relative`
        #   context of its own, and painting order breaks ties. Last child and
        #   higher z-index, both.
        #
        # `append` and not `after`: `after` needs a parent to insert into, and
        # would put the sheet outside `.rd` again.
        #
        # ⚠️ ONE THING HERE WAS MEASURED RATHER THAN REASONED, AND THE
        # REASONING WOULD HAVE BEEN WRONG. Node 10 carries
        # `container-type:inline-size`, and CSS containment makes an element a
        # containing block for its `position:fixed` descendants — which would
        # have anchored this sheet to the top of a 3597px-tall document
        # instead of to the viewport, so scrolling would have slid the scrim
        # off the screen. Driven at 1460 and at 390, at scrollY 0 and 1200:
        # the scrim measures exactly the viewport (1460×1200 and 390×844) and
        # stays at top:0 through the scroll. Chrome does not apply
        # fixed-position containment for `inline-size`. The graft stays where
        # the gates can see it, and it behaves as Design drew it.
        #
        # ── ⊕ 1c — THE EMAIL ROW IS OMITTED ──────────────────────────────
        #
        # RULED: no student surface shows an email address. A class page is
        # opened on a shared classroom machine and on a projector; a school
        # email is a real identifier and a real contact route, and it is on
        # screen for whoever is standing behind the student. Nothing else on
        # the student surface shows one, and the sheet showing one would make
        # it the first place on the site that does.
        #
        # ⚠️ IT CANNOT BE DONE WITH `PRUNE`, and the reason is the order of
        # `apply_rulings`: PRUNE walks the LIVE template first and asserts
        # every index it was given was found, and only THEN does the graft
        # copy the donor in. Listing the renumbered 10263 would therefore
        # raise "they are not in Design's template" — correctly, because at
        # that moment they are not. Hence `omit`, which runs inside the graft,
        # on the donor's own numbering, before the renumber.
        #
        # ⚠️ `omit` IS NOT `BINDINGS`' `drop`, AND THEY ARE DELIBERATELY NOT
        # SPELLED ALIKE. `drop` is a RUNTIME rule about a bound value — the
        # element goes when its text turns out to be empty, and it comes back
        # when the value is not (the environment badge on localhost). `omit`
        # is a BUILD-TIME rule about Design's markup — the subtree is never
        # copied at all, so there is nothing on the page in any state and no
        # value could bring it back.
        #
        # Each index is asserted PRESENT in the donor subtree before it is
        # removed, so an entry that goes stale — Design redraws the sheet, the
        # row moves, the number means something else — stops the build instead
        # of silently omitting nothing and shipping the email.
        dict(at=10, mode="append", donor=243, omit=[263],
             why="Design's account sheet, which is where change C1 puts the "
                 "bench theme control. Six swatches, one tick, and the two "
                 "Settings controls P7 pruned come back wired to it. The "
                 "EMAIL row is omitted: no student surface shows an email "
                 "address, and a class page is read on shared classroom "
                 "machines."),
    ],
    "assignment": [],
}
