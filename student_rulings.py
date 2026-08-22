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
    # ⊕ 23 Aug 2026 — PHASE 3. 335 IS DESIGN'S ORIGINAL RECALL ROUND.
    #
    # The whole `if onRecall` subtree — from the band at 336 to the "Open the
    # assignment instead" link at 403. Design's AMENDED delivery replaces it
    # wholesale with the themed overlay at donor 366, which is grafted below,
    # and there must not end up being two reachable rounds.
    #
    # ⚠️ PRUNING THE MARKUP IS THE SMALLEST PART OF RETIRING IT. Five other
    # things reached this subtree, and every one of them is dealt with in
    # `LOGIC` above — the data, the locals, the methods, the state, and the
    # three ROUTES into `go('recall')`, which after this prune would each have
    # rendered an empty page with a perfectly green build. See the PHASE 3
    # banner in LOGIC['class view'] for the list.
    #
    # ⚑ IT IS THE `if`, NOT THE `<div>` INSIDE IT — the same reading as the
    # flashcards overlay's graft. Pruning node 336 alone would leave a bare
    # `<if onRecall>` with no children: harmless today, and a place for a
    # future edit to put something back into a branch nothing else can see.
    "class view": [275, 279, 297, 298, 322, 325, 328, 335],
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
        # ── ⊕ RETIRED 23 Aug 2026 — PHASE 3. THE SURFACE P2 RULED IS GONE. ──
        #
        # P2's ruling stands, word for word. Its four TRANSFORMATIONS do not,
        # because every line they anchored on has been removed with Design's
        # ORIGINAL recall round — see the Phase 3 entries at the end of this
        # list, and the `PRUNE` of live node 335. `apply_rulings` asserts each
        # `old` occurs EXACTLY ONCE, so leaving them here would stop the build
        # naming four lines that no longer exist, which is that check working.
        #
        # They are quoted rather than deleted, because deleting them would
        # hide a ruling of Mide's rather than move it:
        #
        #     ("  state = {",
        #      "  state = {\n    broke: false,")
        #     ("  skipQuestion = () => this.setState((s) => ({ qi: s.qi + 1,
        #       pick: null, checked: false, streak: 0 }));",
        #      "  … streak: 0, broke: s.broke || s.streak > 0 }));")
        #     ("      return { checked: true, right: s.right + (ok ? 1 : 0),
        #       streak: ok ? s.streak + 1 : 0 };",
        #      "      … broke: s.broke || (!ok && s.streak > 0) };")
        #     ("      streakText: st.streak > 0 ? 'STREAK ' + pad(st.streak)
        #       : 'STREAK BROKEN',",
        #      "      … : (st.broke ? 'STREAK BROKEN' : ''),")
        #
        # ⚑ THE RULING IS CARRIED, NOT DROPPED, and it is carried into a
        # drawing that would otherwise have re-created the exact defect it
        # names. Design's AMENDED round writes
        #
        #     streakLabel: s.streak > 0 ? 'STREAK ' + pad(s.streak) : 'STREAK 00',
        #
        # and resets `streak` to 0 on every `anotherRound` — so a student who
        # had never answered anything would be shown `STREAK 00`, and P2's
        # three states would be back down to two. `recallVals` below reproduces
        # P2 exactly: nothing said before a streak exists, `STREAK 03` while one
        # runs, `STREAK BROKEN` only on the transition FROM a streak TO none.
        #
        # ⚠️ AND `rbroke` IS RESET BY `anotherRound`, WHICH P2's `broke` WAS
        # NOT. That is not a departure from the ruling; it is the ruling read
        # against a different reset. Design's ORIGINAL `newRound` did not touch
        # `streak`, so a streak survived a round and so did the fact it had
        # broken. Design's AMENDED `anotherRound` zeroes the streak — and a
        # `rbroke` that outlived it would open the new round with
        # `STREAK BROKEN` over a student who had not yet answered a question,
        # which is P2's defect verbatim, in a new place.
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
        # ══════════════════════════════════════════════════════════════════
        # ⊕ 23 Aug 2026 — PHASE 2. THE LOGIC HALF OF THE FLASHCARD SURFACE.
        # ══════════════════════════════════════════════════════════════════
        #
        # ⚠️ THE SAME LESSON AS THE PICKER, AND IT IS WORTH RESTATING BECAUSE
        # IT FAILS SILENTLY. `GRAFT` copies MARKUP. Design's two flashcard
        # regions reference twelve names — `cardCount`, `stackPos`, `topFront`,
        # `topMine`, `card`, `pips`, `flipOn`, `flipLabel`, `flip`, `next`,
        # `openCards`, `cardsOpen` — and the live logic class has none of them.
        # `build` resolves an `if` with `lookup(node.e, scope, null)`, miss list
        # deliberately null, so an absent `cardsOpen` reads `undefined`, the
        # overlay renders NOTHING, and the build and every gate stay green.
        #
        # Design's NAMES are kept exactly; Design's VALUES are kept wherever
        # they are pure presentation (the `'1'`/`'0'` strings, `Reveal`/`Hide`,
        # the wrap-around index). What is OURS is where the deck comes from and
        # what order it is in — see `shared/student-live.js`.
        (
            "    tab: 'all', week: null, open: null,",
            "    /* ⊕ 23 Aug 2026 — PHASE 2. Design's own three state keys for\n"
            "       the flashcards, spelled Design's way. None of them collides\n"
            "       with the live page's own state — checked before it was\n"
            "       written: the live initialiser carries view, w, menu, tab,\n"
            "       week, open, bench, boardWeek, boardSize, qi, pick, checked,\n"
            "       right, streak, and Phase 1b's account and theme.\n"
            "\n"
            "       `idx` IS DELIBERATELY NOT PERSISTED, and that is a ruling\n"
            "       rather than an omission. It survives closing and reopening\n"
            "       the overlay — Design's `closeAll` does not touch it — which\n"
            "       is the resume the sidebar card is for. It does NOT survive a\n"
            "       reload, because the deck is RE-RANKED on every load (the\n"
            "       wrongly-answered set moves, the seen counts move), so a\n"
            "       stored index would name a DIFFERENT card and the marker\n"
            "       would be lying about where the student was. Storing the card\n"
            "       id instead would be honest and would fight the ranking: the\n"
            "       point of least-seen-first is that a fresh load opens on what\n"
            "       the student most needs, not on the one they just finished. */\n"
            "    cards: false, idx: 0, flipped: false,\n"
            "    tab: 'all', week: null, open: null,",
        ),
        (
            "  closeAccount = () => this.setState({ account: false });\n",
            "  closeAccount = () => this.setState({ account: false });\n"
            "\n"
            "  /* ⊕ 23 Aug 2026 — PHASE 2. THE FLASHCARDS.\n"
            "\n"
            "     `closeAll` closes BOTH surfaces, which is Design's own\n"
            "     definition of it (`closeAll: () => this.setState({ account:\n"
            "     false, cards: false })`) and is why the name is plural. It is\n"
            "     wired to the sheet's close button AND to the overlay's, and the\n"
            "     two are mutually exclusive by construction — `openCards` clears\n"
            "     `account` and `openAccount` clears `cards` — so closing both is\n"
            "     never closing something the student wanted left open. */\n"
            "  closeAll = () => this.setState({ account: false, cards: false });\n"
            "\n"
            "  /* THE DECK IS DATA AND IS READ THROUGH `MRB_DATA` LIKE EVERYTHING\n"
            "     ELSE. Design's `deck()` returns six authored sample cards; ours\n"
            "     returns whatever `shared/student-live.js` built from the lessons\n"
            "     this class has covered, already ranked. There is no length cap\n"
            "     anywhere in here: a class that has covered twenty lessons gets\n"
            "     every card those lessons carry. */\n"
            "  benchDeck() {\n"
            "    var d = MRB_DATA('cards');\n"
            "    return (d && d.length) ? d : [];\n"
            "  }\n"
            "\n"
            "  /* ⚠️ AN EMPTY DECK MUST NOT OPEN AN EMPTY OVERLAY. A surface with\n"
            "     a counter reading 00 / 00 and a Reveal button over nothing is\n"
            "     worse than a card that says what is true and waits. */\n"
            "  openCards = (e) => {\n"
            "    if (e && e.preventDefault) { e.preventDefault(); }\n"
            "    if (!this.benchDeck().length) { return; }\n"
            "    this.setState({ cards: true, account: false, flipped: false });\n"
            "  };\n"
            "\n"
            "  /* REVEALING A CARD IS WHAT COUNTS AS SEEING IT, and flipping past\n"
            "     one is not. The count feeds the least-seen half of the ranking\n"
            "     (see `rankForPractice` in shared/student-live.js), so counting a\n"
            "     card the student never turned over would push a card they have\n"
            "     not practised to the back of tomorrow's deck.\n"
            "\n"
            "     Through the sink, lazily, like every other write: on the fixture\n"
            "     there is no sink, `_sinkCall` returns null, and Design's file\n"
            "     behaves exactly as drawn. */\n"
            "  flipCard = () => {\n"
            "    const deck = this.benchDeck();\n"
            "    if (!deck.length) { return; }\n"
            "    const showing = !this.state.flipped;\n"
            "    this.setState({ flipped: showing });\n"
            "    if (!showing) { return; }\n"
            "    const n = deck.length;\n"
            "    const at = deck[((this.state.idx % n) + n) % n];\n"
            "    if (at && at.id) { _sinkCall('cardSeen', at.id); }\n"
            "  };\n"
            "\n"
            "  /* Design's own `next`: forward one, face down. The modulo lives in\n"
            "     `cardVals` below, so this can add without bound and the deck\n"
            "     wraps — which is what Design drew and what a revision stack\n"
            "     should do. */\n"
            "  nextCard = () => this.setState((p) => ({ idx: p.idx + 1, flipped: false }));\n"
            "\n"
            "  /* ⚠️ THE PIP ROW DROPS PAST TWENTY-FOUR CARDS, AND THE COUNTER DOES\n"
            "     NOT. Design's row is `display:flex;gap:6px` inside a 390px panel\n"
            "     with 18px of padding either side, so N pips are each\n"
            "     (354 - 6(N-1)) / N pixels wide against a fixed height of 3px. At\n"
            "     24 that is 9px — three times its own height, still legibly a bar\n"
            "     with a 2px radius on each end. At 25 it goes under 3:1 and keeps\n"
            "     shrinking; by 40 it is 3px, a square, and the row has stopped\n"
            "     being a position and become texture.\n"
            "\n"
            "     So past 24 the row is emitted EMPTY and disappears — the `<for>`\n"
            "     renders nothing, the container has no children, and\n"
            "     `[data-pip-row]:empty{display:none}` in build_student_port.py\n"
            "     takes the 16px flex gap with it. `stackPos` is untouched at any\n"
            "     length, so the student always knows where they are; what goes is\n"
            "     the graphic that could no longer say it. */\n"
            "  PIP_MAX = 24;\n"
            "\n"
            "  cardVals() {\n"
            "    const s = this.state;\n"
            "    const deck = this.benchDeck();\n"
            "    const n = deck.length;\n"
            "    const pad = (x) => (x < 10 ? '0' + x : '' + x);\n"
            "    const idx = n ? (((s.idx % n) + n) % n) : 0;\n"
            "    /* The empty card carries no tag, no topic and no back — nothing\n"
            "       that would read as a card with content missing from it. Its\n"
            "       front is the one honest sentence, supplied as data. */\n"
            "    const card = n ? deck[idx]\n"
            "      : { tag: '', topic: '', front: MRB_DATA('cardsEmpty'),\n"
            "          back: '', mine: false };\n"
            "    return {\n"
            "      cardCount: pad(n),\n"
            "      stackPos: n ? (pad(idx + 1) + ' / ' + pad(n)) : '',\n"
            "      topFront: card.front,\n"
            "      topMine: card.mine,\n"
            "      card: card,\n"
            "      /* ⚠️ `cardPips`, NOT Design's `pips` — the live recall\n"
            "         round already owns that name in this same scope object,\n"
            "         and it won. The grafted `<for>` is renamed to match by\n"
            "         `SET_EXPR`; see the note beside it for what the collision\n"
            "         actually rendered. */\n"
            "      cardPips: (n && n <= this.PIP_MAX)\n"
            "        ? deck.map((_, i) => ({ on: i <= idx ? '1' : '0' })) : [],\n"
            "      flipOn: s.flipped ? '1' : '0',\n"
            "      flipLabel: s.flipped ? 'Hide' : 'Reveal',\n"
            "      flip: this.flipCard,\n"
            "      next: this.nextCard,\n"
            "      openCards: this.openCards,\n"
            "      cardsOpen: s.cards\n"
            "    };\n"
            "  }\n",
        ),
        (
            "    this.setState({ account: true, menu: false });\n",
            "    /* ⊕ 23 Aug 2026 — PHASE 2. `cards: false`, so the sheet and the\n"
            "       overlay can never be open at once. Design's own\n"
            "       `openAccount` says the same thing. */\n"
            "    this.setState({ account: true, menu: false, cards: false });\n",
        ),
        (
            "      openAccount: this.openAccount,\n      closeAll: this.closeAccount,\n",
            "      openAccount: this.openAccount,\n"
            "      /* ⊕ 23 Aug 2026 — PHASE 2. It closes BOTH now; the overlay's\n"
            "         close button is wired to the same name. */\n"
            "      closeAll: this.closeAll,\n"
            "      /* ⊕ 23 Aug 2026 — PHASE 2. The twelve names Design's two\n"
            "         grafted flashcard regions resolve out of this object. */\n"
            "      ...this.cardVals(),\n",
        ),
        # ══════════════════════════════════════════════════════════════════
        # ⊕ 23 Aug 2026 — PHASE 3. THE RECALL ROUND.
        # ══════════════════════════════════════════════════════════════════
        #
        # ⚠️ THE SURFACE DECISION, MADE DELIBERATELY AND MADE ONCE.
        #
        # The live page ALREADY HAD a recall round — Design's original, drawn
        # months before the amendments: a `view` switch at template node 335,
        # `choose`/`advance`/`skipQuestion`/`newRound` over `this.questions`,
        # painted in `--st-room` / `--st-cream` page-chrome dark. Design's
        # AMENDED round (donor 366) is a themed OVERLAY in `--b-*`, and it is
        # the richer surface: a round number, a best streak, a rounds count, a
        # round score, a progress bar, a per-question verdict, a
        # Finish-the-round label and an Another-round exit.
        #
        # RULED: GRAFT THE AMENDED ROUND AND RETIRE THE ORIGINAL. Re-skinning
        # the original was considered and refused for a mechanical reason, not
        # a taste one: its colours are LITERAL `var(--st-room)` / `--st-cream`
        # strings inside inline `style` attributes on some thirty template
        # nodes. `LOGIC` cannot reach an inline literal — that is the whole
        # reason `SET_ATTR` and `_PAGE_STRONG` exist — so re-skinning meant
        # thirty attribute registrations against a drawing Design had already
        # replaced, and it would still have been the poorer surface.
        #
        # ⚠️ THERE MUST NOT END UP BEING TWO REACHABLE ROUNDS, and "retired"
        # here means REMOVED, in five places, each of which was a live part of
        # the old one:
        #
        #   1  the DATA          the renderVals block below, removed entire
        #   2  the LOCALS        qi / q / options / pickIdx / rightPick / pips
        #   3  the METHODS       choose / advance / skipQuestion / newRound
        #   4  the STATE         qi / pick / checked / right / streak
        #   5  the ROUTES        the nav's `Recall` tab, `goRecall` on the two
        #                        bench buttons, and P3's work-row fallback
        #
        # plus the MARKUP, which is `PRUNE` 335 — the whole `if onRecall`
        # subtree — because a prune is not a LOGIC transformation.
        #
        # ⚠️ 5 IS THE ONE THAT WOULD HAVE SHIPPED A BLANK PAGE. `go('recall')`
        # sets `view: 'recall'`, and with node 335 pruned there is NOTHING
        # rendered for that view — the class view is `if onClass` and the round
        # was the only other branch. So every surviving caller of `go('recall')`
        # becomes a control that blanks the page, and the build would have been
        # green. There were three: the nav tab, `goRecall` (nodes 77 and 88),
        # and the marked-work row's fallback from ruling P3.
        (
            "      recallMeter: 'QUESTION ' + pad(Math.min(st.qi + 1, 6)) + ' / 06',\n"
            "      recallMeterPct: Math.round((Math.min(st.qi, 6) / 6) * 100) + '%',\n"
            "      roundLive: st.qi < 6, roundDone: st.qi >= 6,\n"
            "      qCounter: 'QUESTION ' + pad(Math.min(st.qi + 1, 6)) + ' / 06 \\u00B7 ' + q.topic,\n"
            "      question: q.q, options: options, pips: pips,\n"
            "      showFeedback: st.checked && pickIdx > -1,\n"
            "      fbLabel: rightPick ? 'CORRECT' : 'NOT THIS ONE',\n"
            "      fbEdge: rightPick ? 'var(--st-ok-room)' : 'var(--st-ember)',\n"
            "      // ⊕ MRB-270 phase 3, RULED 20 Aug 2026: the LABEL is text, and\n"
            "      // --st-ok-room is graphic-only. The 3px edge above keeps it.\n"
            "      fbLabelColor: rightPick ? 'var(--ks3-ok-dark)' : 'var(--st-ember)',\n"
            "      fbText: pickIdx > -1 ? q.f[pickIdx] : '',\n"
            "      primaryRecall: this.advance, skipQuestion: this.skipQuestion, newRound: this.newRound,\n"
            "      recallBtnLabel: st.checked ? 'Next question' : 'Check',\n"
            "      recallBtnBg: st.pick || st.checked ? 'var(--ks3-accent-text)' : 'transparent',\n"
            "      recallBtnColor: st.pick || st.checked ? 'var(--st-paper)' : 'var(--st-room-muted)',\n"
            "      recallBtnBorder: st.pick || st.checked ? 'var(--ks3-accent-text)' : 'var(--st-room-line)',\n"
            "      streakText: st.streak > 0 ? 'STREAK ' + pad(st.streak) : 'STREAK BROKEN',\n"
            "      roundScore: pad(st.right),\n"
            "      roundNote: 'Six answers logged against Week 04. Recall is worth 20 of the 100 points on the leaderboard.',\n"
            "      recallStats: [{ label: 'BEST STREAK', value: pad(Math.max(9, st.streak)) }, { label: 'ROUNDS', value: '08' }],\n"
            "\n",
            "      /* ⊕ 23 Aug 2026 — PHASE 3, part 1 of 5. The old round's DATA.\n"
            "\n"
            "         Twenty keys, and pruned node 335 was the only reader of\n"
            "         every one of them. Removed rather than left dead, for a\n"
            "         reason that is not tidiness: TWO of them — `roundDone` and\n"
            "         `roundScore` — are names Design's AMENDED round needs, in\n"
            "         this same scope object. Leaving them would put the port back\n"
            "         in exactly the position the `pips` collision put it in one\n"
            "         phase ago: one scope, one name, two lists, and whichever key\n"
            "         was written later silently winning. That defect shipped with\n"
            "         a green build and all three gates green, and the fix for it\n"
            "         is not to rely on ordering a second time.\n"
            "\n"
            "         `roundNote` goes with them, and it is the sentence that has\n"
            "         to stay gone: *'Recall is worth 20 of the 100 points on the\n"
            "         leaderboard'* states an apportionment the platform cannot\n"
            "         compute — the same fault the 21 Aug ruling took out of the\n"
            "         split bar and its static 40/40/20 legend — and it is\n"
            "         platform self-explanation on a student page. Design's\n"
            "         AMENDED delivery draws it AGAIN, at donor node 439, and that\n"
            "         node is omitted on the way in; see the graft.\n"
            "\n"
            "         `recallStats` goes with them for the reason student-live.js\n"
            "         already records against `recallAnswered` / `recallPct` /\n"
            "         `recallRounds`: BEST STREAK 09 and ROUNDS 08 were a drawing.\n"
            "         Nothing anywhere records a recall round. */\n",
        ),
        (
            "    const qi = Math.min(st.qi, 5);\n"
            "    const q = this.questions[qi];\n"
            "    const keys = ['A', 'B', 'C', 'D'];\n"
            "    const options = q.o.map((t, i) => {\n"
            "      const k = keys[i];\n"
            "      const chosen = st.pick === k;\n"
            "      const isAns = q.a === k;\n"
            "      const ok = st.checked && isAns;\n"
            "      const bad = st.checked && chosen && !isAns;\n"
            "      return {\n"
            "        key: k, text: t, onClick: () => this.choose(k), ok: ok, bad: bad,\n"
            "        bg: ok ? 'rgba(85,179,106,0.12)' : chosen ? '#241E17' : 'transparent',\n"
            "        border: bad ? 'var(--err)' : ok ? 'var(--st-ok-room)' : chosen ? 'var(--st-room-line-strong)' : 'var(--st-room-line)',\n"
            "        keyBg: chosen || ok ? 'var(--st-ember)' : 'transparent',\n"
            "        keyBorder: chosen || ok ? 'var(--st-ember)' : 'var(--st-room-line-strong)',\n"
            "        keyColor: chosen || ok ? '#15110C' : 'var(--st-room-muted)',\n"
            "        color: ok || chosen ? 'var(--st-cream)' : 'var(--st-room-text)'\n"
            "      };\n"
            "    });\n"
            "    const pickIdx = keys.indexOf(st.pick);\n"
            "    const rightPick = st.checked && st.pick === q.a;\n"
            "    const pips = this.questions.map((x, i) => ({\n"
            "      w: i === st.qi ? '26px' : '12px',\n"
            "      bg: i < st.qi ? 'var(--st-ember)' : i === st.qi ? 'var(--st-cream)' : 'var(--st-room-line)'\n"
            "    }));\n",
            "    /* ⊕ 23 Aug 2026 — PHASE 3, part 2 of 5. The old round's LOCALS.\n"
            "\n"
            "       ⚠️ THIS BLOCK IS WHY AN EMPTY BANK USED TO TAKE THE WHOLE\n"
            "       PAGE DOWN. `const q = this.questions[qi]` ran on EVERY render\n"
            "       of the class view — the round was a VIEW, not an overlay, and\n"
            "       `renderVals` computes both — so a class with no ladder rungs\n"
            "       behind its lessons hit `q.o.map` of undefined during the first\n"
            "       paint and drew nothing at all. That is what the `throw` in\n"
            "       student-live.js was defending against, and removing this block\n"
            "       is what let the throw go.\n"
            "\n"
            "       `pips` LEAVES HERE TOO, and it is the name the flashcards\n"
            "       overlay collided with in Phase 2. `SET_EXPR`'s rename of the\n"
            "       grafted loop to `cardPips` is DELIBERATELY KEPT rather than\n"
            "       retired with it: the rename costs nothing, it is asserted at\n"
            "       build time against the expected old value, and unwinding it\n"
            "       would put the overlay back on a name this file has already\n"
            "       proved two surfaces can want. */\n",
        ),
        (
            "  choose = (k) => { if (!this.state.checked) this.setState({ pick: k }); };\n"
            "  advance = () => this.setState((s) => {\n"
            "    if (!s.checked) {\n"
            "      if (!s.pick) return {};\n"
            "      const ok = s.pick === this.questions[s.qi].a;\n"
            "      return { checked: true, right: s.right + (ok ? 1 : 0), streak: ok ? s.streak + 1 : 0 };\n"
            "    }\n"
            "    return { qi: s.qi + 1, pick: null, checked: false };\n"
            "  });\n"
            "  skipQuestion = () => this.setState((s) => ({ qi: s.qi + 1, pick: null, checked: false, streak: 0 }));\n"
            "  newRound = () => this.setState({ qi: 0, pick: null, checked: false, right: 0 });\n",
            "  /* ⊕ 23 Aug 2026 — PHASE 3, part 3 of 5. The old round's METHODS,\n"
            "     replaced by the amended round's. Every name below is Design's\n"
            "     own, spelled Design's way, because Design's grafted markup is\n"
            "     what resolves them: `build` looks an `if` up with a null miss\n"
            "     list, so one letter out is a branch that renders NOTHING,\n"
            "     silently, on a page whose build printed a graft and whose gates\n"
            "     all stay green.\n"
            "\n"
            "     ⚠️ AND NO GATE OPENS THIS SURFACE. `student_behaviour` requires\n"
            "     every step of a drive to be performable on Design's ORIGINAL\n"
            "     file, and pressing `Practise recall` there opens the round this\n"
            "     unit retires — so the two files would diverge by a whole screen\n"
            "     and the drive cannot be kept. The seven `Recall` drives are\n"
            "     retired with it. `student_themes` is extended instead: it drives\n"
            "     the port alone, needs no oracle, and is the one gate that CAN\n"
            "     open the round. */\n"
            "\n"
            "  /* THE ROUND IS min(6, POOL) — ruling P2 — and the number is\n"
            "     computed in ONE place so nothing can state a size it will not\n"
            "     show. `recallBank` arrives from student-live.js already ranked\n"
            "     by `rankForPractice`; this file neither sorts it nor chooses\n"
            "     from it, which is what keeps one definition of 'what should this\n"
            "     student practise next' in one file. */\n"
            "  RECALL_MAX = 6;\n"
            "\n"
            "  recallBank() {\n"
            "    var b = MRB_DATA('recallBank');\n"
            "    return (b && b.length) ? b : [];\n"
            "  }\n"
            "\n"
            "  recallSize() {\n"
            "    return Math.min(this.RECALL_MAX, this.recallBank().length);\n"
            "  }\n"
            "\n"
            "  /* NO REPEAT WITHIN A ROUND, STRUCTURALLY RATHER THAN BY CHECKING.\n"
            "     A round is `size` CONSECUTIVE items of a bank of `length`, and\n"
            "     `size` is `min(6, length)` — so the modulo can never come back\n"
            "     round to an index it has already handed out. Design's own\n"
            "     arithmetic, with the real size in place of Design's literal 6:\n"
            "     Design writes `length: 6` over a bank of 8, which would repeat\n"
            "     two questions in every round the moment a real bank was shorter\n"
            "     than six. Round two starts where round one stopped, so a student\n"
            "     with a long bank works THROUGH it rather than round the same\n"
            "     six; with a bank of exactly `size` the same questions come back,\n"
            "     which is the honest answer rather than a defect. */\n"
            "  recallRound() {\n"
            "    const bank = this.recallBank();\n"
            "    const size = this.recallSize();\n"
            "    if (!size) { return []; }\n"
            "    const start = ((this.state.rno - 1) * size) % bank.length;\n"
            "    const out = [];\n"
            "    for (var i = 0; i < size; i += 1) {\n"
            "      out.push(bank[(start + i) % bank.length]);\n"
            "    }\n"
            "    return out;\n"
            "  }\n"
            "\n"
            "  /* ⚠️ AN EMPTY BANK MUST NOT OPEN AN EMPTY ROUND — the same rule\n"
            "     `openCards` follows one surface over. It cannot normally be\n"
            "     reached at all: `recallLabel` is empty with no bank and its\n"
            "     binding is marked `drop`, so the button is not on the page. This\n"
            "     is the second lock, because the first one lives in another\n"
            "     file. */\n"
            "  openRecall = (e) => {\n"
            "    if (e && e.preventDefault) { e.preventDefault(); }\n"
            "    if (!this.recallSize()) { return; }\n"
            "    this.setState({ recall: true, cards: false, account: false, menu: false });\n"
            "  };\n"
            "  closeRecall = () => this.setState({ recall: false });\n"
            "\n"
            "  /* ⛔ NOTHING IS HANDED IN, AND THIS METHOD IS WHERE THAT IS TRUE\n"
            "     OR NOT. There is no submission, no attempt row, no score and no\n"
            "     network call of any kind anywhere in the round. The one thing a\n"
            "     round writes is a per-device SEEN COUNT, in localStorage, which\n"
            "     feeds the least-seen half of the ordering and is read by nothing\n"
            "     a student or a teacher ever sees. */\n"
            "  recallAdvance = (scored) => {\n"
            "    const size = this.recallSize();\n"
            "    this.setState((s) => {\n"
            "      const last = s.rqi >= size - 1;\n"
            "      const streak = scored ? s.rstreak + 1 : 0;\n"
            "      return {\n"
            "        rstreak: streak,\n"
            "        /* ⊕ P2, CARRIED. A streak BREAKS only when there was one:\n"
            "           getting the first question of a round wrong zeroes a\n"
            "           streak that was already zero, and nothing was broken. */\n"
            "        rbroke: s.rbroke || (!scored && s.rstreak > 0),\n"
            "        rbest: Math.max(s.rbest, streak),\n"
            "        rright: s.rright + (scored ? 1 : 0),\n"
            "        rpick: null, rchecked: false,\n"
            "        rqi: last ? s.rqi : s.rqi + 1,\n"
            "        rdone: last,\n"
            "        rrounds: last ? s.rrounds + 1 : s.rrounds\n"
            "      };\n"
            "    });\n"
            "  };\n"
            "\n"
            "  nextRecall = () => {\n"
            "    const at = this.recallRound()[this.state.rqi];\n"
            "    this.recallAdvance(!!at && this.state.rpick === at.answer);\n"
            "  };\n"
            "  skipRecall = () => this.recallAdvance(false);\n"
            "\n"
            "  /* CHECKING IS WHAT COUNTS AS SEEING A QUESTION, and moving past\n"
            "     one is not — the same distinction `flipCard` draws between\n"
            "     revealing a card and flicking past it. Through the sink, lazily:\n"
            "     on the fixture there is none, `_sinkCall` returns null, and\n"
            "     Design's file behaves exactly as drawn. */\n"
            "  checkRecall = () => {\n"
            "    if (this.state.rchecked || this.state.rpick === null) { return; }\n"
            "    this.setState({ rchecked: true });\n"
            "    const at = this.recallRound()[this.state.rqi];\n"
            "    if (at && at.id) { _sinkCall('questionSeen', at.id); }\n"
            "  };\n"
            "\n"
            "  /* Design's own `anotherRound`, with `rbroke` reset alongside the\n"
            "     streak it belongs to — see the retired P2 note above for why\n"
            "     that is the ruling being kept rather than bent. `rbest` and\n"
            "     `rrounds` survive it: a student's best run, and how many rounds\n"
            "     they have done, are facts about the sitting and not about a\n"
            "     round. */\n"
            "  anotherRound = () => this.setState((s) => ({\n"
            "    rno: s.rno + 1, rqi: 0, rpick: null, rchecked: false,\n"
            "    rright: 0, rdone: false, rstreak: 0, rbroke: false\n"
            "  }));\n"
            "\n"
            "  recallVals() {\n"
            "    const s = this.state;\n"
            "    const pad = (x) => (x < 10 ? '0' + x : '' + x);\n"
            "    const size = this.recallSize();\n"
            "    const round = this.recallRound();\n"
            "    const at = Math.min(s.rqi, Math.max(0, size - 1));\n"
            "    const qq = round[at];\n"
            "    /* With no bank there is no surface: `openRecall` refuses and the\n"
            "       button is not on the page. This is what stops a state reached\n"
            "       some other way from indexing an empty array. */\n"
            "    if (!size || !qq) {\n"
            "      return {\n"
            "        recallOpen: false, inRound: false, roundDone: false,\n"
            "        q: { topic: '', q: '', note: '' }, opts: [], qpips: [],\n"
            "        checked: false, canCheck: false, verdict: '',\n"
            "        nextLabel: '', streakLabel: '', roundLabel: '',\n"
            "        roundScore: '', qPos: '', qStep: '0',\n"
            "        check: this.checkRecall, nextQ: this.nextRecall,\n"
            "        skipQ: this.skipRecall, anotherRound: this.anotherRound,\n"
            "        openRecall: this.openRecall, closeRecall: this.closeRecall\n"
            "      };\n"
            "    }\n"
            "    const gotIt = s.rchecked && s.rpick === qq.answer;\n"
            "    const optState = (i) => {\n"
            "      if (!s.rchecked) { return s.rpick === i ? 'picked' : 'idle'; }\n"
            "      if (i === qq.answer) { return 'correct'; }\n"
            "      return s.rpick === i ? 'wrong' : 'idle';\n"
            "    };\n"
            "    const opts = (qq.options || []).map((label, i) => ({\n"
            "      label: label, letter: 'ABCD'[i], st: optState(i),\n"
            "      right: s.rchecked && i === qq.answer,\n"
            "      pick: () => { if (!this.state.rchecked) { this.setState({ rpick: i }); } }\n"
            "    }));\n"
            "    /* ⚠️ THE LINE UNDER THE VERDICT IS THE ONE WRITTEN AGAINST THE\n"
            "       ANSWER THE STUDENT GAVE, and it is empty when they were right.\n"
            "       Design's amended sample carries ONE note per question and\n"
            "       prints it whatever was picked; the real corpus carries a `why`\n"
            "       per OPTION, and — measured across both content sources, and\n"
            "       recorded in the 21 Aug ruling — the ones that exist are always\n"
            "       the DISTRACTORS. The teaching in a multiple-choice question\n"
            "       lands on the MISTAKE. A correct answer gets the verdict word\n"
            "       and nothing beneath it, which is that ruling exactly, and the\n"
            "       slot does not stand open because the verdict is in it. Both\n"
            "       shapes are read, so the fixture keeps Design's behaviour byte\n"
            "       for byte. */\n"
            "    const note = Array.isArray(qq.notes)\n"
            "      ? (s.rpick === null ? '' : (qq.notes[s.rpick] || ''))\n"
            "      : (qq.note || '');\n"
            "    /* ⚠️⚠️ THE PROGRESS BAR ASSUMES SIX, AND THE POOL DOES NOT.\n"
            "       Design's grafted CSS carries `.rprog[data-w=\"0\"]` … `[\"6\"]` at\n"
            "       0/17/33/50/67/83/100%, and Design's own logic feeds it the RAW\n"
            "       step index — right for a round of six and wrong for every\n"
            "       other length. With the real pool of FOUR on 8r/Sc1, a student\n"
            "       who had answered all four would have seen a bar at 67%: the\n"
            "       round complete, and the graphic saying it was not.\n"
            "\n"
            "       The step is scaled onto Design's six buckets instead, so no\n"
            "       CSS is added and Design's stylesheet is not touched: a round of\n"
            "       six is unchanged (the scale is the identity), a round of four\n"
            "       reads 0 / 33 / 50 / 83(*) / 100 and a round of two reads\n"
            "       0 / 50 / 100 — both measured in the browser, not derived on\n"
            "       paper. (*) 3 of 4 is 75%, which falls exactly between the 67%\n"
            "       and 83% buckets, and `Math.round` takes the half upward. The\n"
            "       buckets are 17 points apart and a 3px bar is not a readout;\n"
            "       what matters is that the bar MOVES on every question and is\n"
            "       FULL when the round is done, and both hold at every length.\n"
            "\n"
            "       ⚑ AND IT NOW REACHES 100%, WHICH DESIGN'S NEVER DID. Design\n"
            "       pins `qi` at the last question when the round ends, so the bar\n"
            "       stopped at 83% over a finished round. The step here is the\n"
            "       number of questions COMPLETED, which is the size once the\n"
            "       round is done. */\n"
            "    const step = s.rdone ? size : s.rqi;\n"
            "    return {\n"
            "      recallOpen: s.recall,\n"
            "      inRound: s.recall && !s.rdone,\n"
            "      roundDone: s.rdone,\n"
            "      roundLabel: 'ROUND ' + pad(s.rno),\n"
            "      /* Both of these STATE THE REAL SIZE, which is ruling P2's whole\n"
            "         requirement. The two text nodes that used to spell it out in\n"
            "         a WORD — `SIX QUESTIONS · UNLIMITED ROUNDS` and `OF SIX` —\n"
            "         are retired with the old round's markup, so there is no\n"
            "         wording left on the page that CAN be wrong about it. */\n"
            "      roundScore: s.rright + ' / ' + size,\n"
            "      qPos: pad(Math.min(s.rqi + 1, size)) + ' / ' + pad(size),\n"
            "      qStep: String(Math.round((step / size) * 6)),\n"
            "      qpips: round.map((_, i) => ({ on: i <= s.rqi ? '1' : '0' })),\n"
            "      q: { topic: qq.topic, q: qq.q, note: note },\n"
            "      opts: opts,\n"
            "      checked: s.rchecked,\n"
            "      canCheck: !s.rchecked,\n"
            "      verdict: gotIt ? 'Correct.' : 'Not this time.',\n"
            "      nextLabel: s.rqi >= size - 1 ? 'Finish the round' : 'Next question',\n"
            "      /* ⊕ P2, CARRIED WHOLE. Three states and not two: nothing said\n"
            "         before a streak exists, the count while one runs, and the\n"
            "         word only once one has actually broken. Design's amended line\n"
            "         prints `STREAK 00` in the first state, which is P2's defect\n"
            "         in a politer font. */\n"
            "      streakLabel: s.rstreak > 0 ? 'STREAK ' + pad(s.rstreak)\n"
            "        : (s.rbroke ? 'STREAK BROKEN' : ''),\n"
            "      check: this.checkRecall,\n"
            "      nextQ: this.nextRecall,\n"
            "      skipQ: this.skipRecall,\n"
            "      anotherRound: this.anotherRound,\n"
            "      openRecall: this.openRecall,\n"
            "      closeRecall: this.closeRecall\n"
            "    };\n"
            "  }\n",
        ),
        (
            "    qi: 0, pick: null, checked: false, right: 0, streak: 3\n  };",
            "    /* ⊕ 23 Aug 2026 — PHASE 3, part 4 of 5. The old round's STATE,\n"
            "       replaced by the amended round's. Every key is prefixed `r` and\n"
            "       that is not a style choice: `checked`, `pick` and `right` are\n"
            "       words other surfaces in this codebase also use, and this port\n"
            "       has already shipped one defect that was two surfaces wanting\n"
            "       one name in one scope.\n"
            "\n"
            "       Design's own amended state is `qi, picked, checked, roundNo,\n"
            "       answered, streak, best, rounds, roundScore, roundDone`.\n"
            "       `answered` is NOT carried: it is Design's THIS WEEK figure, and\n"
            "       nothing anywhere records a recall round, so the panel it lives\n"
            "       in is omitted on the way in rather than filled with a session\n"
            "       count wearing a week's label. See the graft.\n"
            "\n"
            "       Nothing here is persisted, and that is deliberate in the same\n"
            "       way the flashcards' `idx` is: a round is a sitting, the bank is\n"
            "       re-ranked on every load, and a restored `rqi` would name a\n"
            "       DIFFERENT question. */\n"
            "    recall: false, rqi: 0, rpick: null, rchecked: false,\n"
            "    rright: 0, rstreak: 0, rbest: 0, rbroke: false,\n"
            "    rno: 1, rrounds: 0, rdone: false\n  };",
        ),
        (
            "      goClass: () => this.go('class'), goRecall: () => this.go('recall'),\n"
            "      /* ⊕ RULED 22 Aug 2026 — P5. */",
            "      goClass: () => this.go('class'),\n"
            "      /* ⊕ 23 Aug 2026 — PHASE 3, part 5 of 5. THE ROUTES.\n"
            "\n"
            "         ⛔ `goRecall: () => this.go('recall')` is what this replaces,\n"
            "         and after the prune of node 335 it was a control that blanked\n"
            "         the page: `view: 'recall'` has no branch left to render. Two\n"
            "         live buttons resolve this name — `Practise recall` on the\n"
            "         bench (node 77) and `Start recall` on the empty-class bench\n"
            "         (node 88) — and Design's AMENDED delivery wires its own\n"
            "         `Practise recall` (donor 76, and donor 116 on the done bench)\n"
            "         to `openRecall`. So the NAME is repointed rather than the\n"
            "         nodes rewired: `SET_ON` refuses a node that already carries a\n"
            "         handler, and one line here reaches every caller there will\n"
            "         ever be — including the done bench's copy when Phase 4\n"
            "         lands.\n"
            "\n"
            "         The name stays `goRecall` because Design's markup resolves\n"
            "         that spelling on both nodes. What it means has changed; where\n"
            "         it is written has not. */\n"
            "      goRecall: this.openRecall,\n"
            "      /* ⊕ RULED 22 Aug 2026 — P5. */",
        ),
        (
            "            : () => this.go('recall'),",
            "            /* ⊕ 23 Aug 2026 — PHASE 3. P3's fallback, repointed. It\n"
            "               sent a marked row with no known lesson page to the\n"
            "               recall round, deliberately — \"at least about the same\n"
            "               class\". That destination is an overlay now rather than\n"
            "               a view, and `go('recall')` would have blanked the page.\n"
            "               Same destination, reached the way it is reached now. */\n"
            "            : this.openRecall,",
        ),
        (
            "    const nav = [\n"
            "      { label: 'My class', onClick: () => this.go('class'), on: onClass },\n"
            "      { label: 'Recall', onClick: () => this.go('recall'), on: !onClass }\n"
            "    ].map((n) => ({",
            "    /* ⊕ 23 Aug 2026 — PHASE 3. THE NAV'S `Recall` TAB IS GONE.\n"
            "\n"
            "       It was the third route into `go('recall')`, and the only one\n"
            "       that could not simply be repointed: the nav is a VIEW SWITCH —\n"
            "       its `on` state is `!onClass` and its underline says which view\n"
            "       you are in — and the round is no longer a view. Wiring the tab\n"
            "       to `openRecall` would have left a tab that opens an overlay and\n"
            "       can never look selected, which is a control lying about what\n"
            "       kind of thing it is.\n"
            "\n"
            "       ⚑ NO DESTINATION IS LOST. `Practise recall` sits on the bench\n"
            "       at the top of the same page, and Design's amended delivery puts\n"
            "       it there in BOTH bench states — donor 76 open, donor 116 done —\n"
            "       which is Design saying in the file that the bench is where the\n"
            "       round is reached from.\n"
            "\n"
            "       Registered from the other end in student_behaviour.py:\n"
            "       `RULED_DIVERGENCE` for the text and `RULED_CONTROLS` for the\n"
            "       census, because the two are compared separately and a ruling\n"
            "       that reaches only one of them reads as a broken port. */\n"
            "    const nav = [\n"
            "      { label: 'My class', onClick: () => this.go('class'), on: onClass }\n"
            "    ].map((n) => ({",
        ),
        (
            "    this.setState({ account: true, menu: false, cards: false });\n",
            "    /* ⊕ 23 Aug 2026 — PHASE 3. `recall: false` joins them: three\n"
            "       surfaces, one at a time, and each opener closes the other\n"
            "       two. */\n"
            "    this.setState({ account: true, menu: false, cards: false, recall: false });\n",
        ),
        (
            "    this.setState({ cards: true, account: false, flipped: false });\n",
            "    this.setState({ cards: true, account: false, flipped: false, recall: false });\n",
        ),
        # ── ⊕ 23 Aug 2026 — PHASE 3. A DEAD PRIMARY BUTTON, FOUND IN PASSING ──
        #
        # ⚠️ THIS IS LIVE TODAY, and it is not Phase 4's. Ruling P4 gives the
        # bench's primary button a second job once the week is done, and its
        # own label says which:
        #
        #     benchPrimaryLabel: benchDone
        #       ? (benchLessons.length ? 'Revisit the lesson' : 'Practise recall')
        #       : 'Open the assignment'
        #     benchPrimaryHref:  benchDone
        #       ? (benchLessons.length ? benchLessons[0].href : '')
        #       : (current ? assignmentHref() : '')
        #
        # So a student who finishes work drawn on a lesson this build has NO
        # PAGE for — a retired slug, or a bank that has moved on — gets a
        # primary button reading `Practise recall` with an EMPTY href, and P1's
        # fallback ticks checklist item one. `benchDone` also empties
        # `benchTasks`, so the checklist is not rendered at all: the tick is
        # invisible and the press does nothing a student can see. The biggest
        # control on the page, saying the name of a surface, going nowhere.
        #
        # It could not be fixed before this phase, because until this phase
        # there was nothing for it to open that would not have blanked the
        # page. Now `openRecall` exists and it is one line.
        #
        # ⚠️ GUARDED ON `benchDone` AND NOT ON THE EMPTY HREF, and the
        # difference matters: `benchPrimaryHref` is ALSO empty in the OPEN
        # state when no assignment is set, and there the label reads `Open the
        # assignment`. Sending that student to the recall round would be a
        # second button naming a destination it does not go to — this ruling's
        # own complaint, committed in the act of fixing it.
        #
        # `openRecall` refuses an empty bank, so a class with no rungs presses
        # a button that still does nothing. That is not this ruling's to fix:
        # it is P4's done-bench markup, which Phase 4 grafts (donor 101), and
        # Design draws `Practise recall` there as its own separate control
        # (donor 116) rather than as the primary.
        (
            "    const href = MRB_DATA('benchPrimaryHref');\n"
            "    if (href) { window.location.href = href; return; }\n",
            "    const href = MRB_DATA('benchPrimaryHref');\n"
            "    if (href) { window.location.href = href; return; }\n"
            "    /* ⊕ 23 Aug 2026 — PHASE 3. The done bench with no lesson page\n"
            "       labels this button `Practise recall`, and until this phase\n"
            "       it had nowhere to send them. Now it does. */\n"
            "    if (MRB_DATA('benchDone')) { this.openRecall(); return; }\n",
        ),
        (
            "      ...this.cardVals(),\n",
            "      ...this.cardVals(),\n"
            "      /* ⊕ 23 Aug 2026 — PHASE 3. The twenty-one names Design's\n"
            "         grafted recall round resolves out of this object. It is\n"
            "         spread LAST, and there is deliberately nothing riding on\n"
            "         that: every name it emits was checked against the whole\n"
            "         object first, and the two that DID collide — `roundDone` and\n"
            "         `roundScore` — were removed at source rather than shadowed.\n"
            "         Ordering is what the `pips` defect relied on, and relying on\n"
            "         it twice is how a lesson stops being one. */\n"
            "      ...this.recallVals(),\n",
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
    # ⊕ 23 Aug 2026 — PHASE 2. TWO MORE, ON THE GRAFTED FLASHCARD CARD.
    #
    #   10204  the flashcards card Design's C2 puts where the dark RECALL card
    #          was. It is painted `background:var(--b-ground)` — a THEME token,
    #          used DIRECTLY, with no `--st-*` anywhere in the whole subtree
    #          (measured: the two regions reference only `--b-*` and `--pg-*`).
    #          So the token bridge has nothing to do here and the attribute is
    #          inert as CSS.
    #
    #          ⚠️ IT IS NOT INERT TO THE GATE, AND THAT IS WHY IT IS HERE.
    #          `student_themes.check_page_chrome` sweeps every element OUTSIDE
    #          `[data-bench-surface]` for a near-black background, because
    #          Design's amendment says no page CHROME is near-black any more.
    #          `--b-ground` is near-black on four of the six themes (harbour
    #          #20363F, moss #294036, damson #38243A, graphite #1A1512 — every
    #          channel under 70), so without this the card would be reported as
    #          four unregistered strays on a page where it is doing exactly what
    #          Design drew. Registering it as an EXCEPTION would be the wrong
    #          shape: an exception says "near-black chrome that has not moved to
    #          espresso yet". This is not chrome. It is a themed surface, and
    #          `data-bench-surface` is this build's word for one.
    #
    #   10329  the overlay's pip row. It is `display:flex;gap:6px` with a single
    #          `<for>` inside it; past 24 cards the loop is handed an empty list
    #          and renders nothing, and an empty flex child still costs its
    #          parent's 16px gap. `[data-pip-row]:empty{display:none}` in
    #          build_student_port.py collapses it. An attribute plus a scoped
    #          rule, for the same reason `data-page-strong` is one: the row's
    #          `display` is a LITERAL inside Design's inline `style`, so there
    #          is no string in the logic for a `LOGIC` ruling to anchor on.
    #
    # ⊕ 23 Aug 2026 — PHASE 3. ONE MORE, ON THE GRAFTED RECALL ROUND.
    #
    #   10384  the round's question panel — `background:var(--b-ground)`, a
    #          THEME token used directly, exactly as the flashcards card at
    #          10204 is. So the token bridge has nothing to do here and the
    #          attribute is inert as CSS.
    #
    #          ⚠️ IT IS NOT INERT TO THE GATE. `--b-ground` is near-black on
    #          four of the six themes, and `student_themes.check_page_chrome`
    #          sweeps every element OUTSIDE `[data-bench-surface]` for a
    #          near-black background. Without this the panel would be reported
    #          as four unregistered strays the moment anything opens the round —
    #          which `student_themes` now does, deliberately, because it is the
    #          only gate that can.
    #
    #          The ROUND ROOT at 10367 takes no surface attribute and needs
    #          none: it is `background:var(--pg-ground)`, the cream page, and it
    #          already carries Design's own `data-port-region="recall-round"`
    #          through the graft. The sidebar panel Design draws beside this one
    #          — donor 425, also `--b-ground` — is omitted on the way in, so
    #          there is no second surface to name.
    "class view": {
        55:  {"data-bench-surface": "bench", "data-port-region": "bench"},
        10204: {"data-bench-surface": "cards"},
        10329: {"data-pip-row": "1"},
        10384: {"data-bench-surface": "recall"},
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


# ── the ONE loop name that two of Design's surfaces both wanted ──────────
#
# ⊕ 23 Aug 2026 — PHASE 2, AND IT WAS FOUND BY DRIVING THE PAGE, NOT BY
# READING IT. This is the sixth mechanism and it exists for one node.
#
# Design's flashcards overlay draws its position pips from `<for e="pips">`
# (donor node 330). The live page's RECALL ROUND does too — Design drew that
# months earlier, and `renderVals` line 673 reads `pips: pips`, built from
# `this.questions`. One scope object, one name, two lists.
#
# ⚠️ WHAT THAT LOOKED LIKE, WHICH IS WHY NOTHING CAUGHT IT. The class-view
# spread of `cardVals()` sits EARLIER in the returned object literal than the
# recall round's own key, so the LATER key won. The flashcards overlay rendered
# TWO pips for an eleven-card deck — the recall round's two questions — each
# with no `data-on` at all, because a recall pip's shape is not a card pip's.
# The build was green, all three gates were green (none of them can open the
# overlay), and the row simply drew the wrong thing. It was measured in the
# drive: `n: 2, w: 174, on: ''`.
#
# ⚠️ AND ORDERING IS NOT THE FIX, because the two surfaces are NOT mutually
# exclusive. The recall round is `if onRecall` inside the page; the overlay is
# grafted at the design root, outside both views, and `goRecall` does not clear
# `cards`. A student who opens the cards and then the round has both, so
# whichever list won would be wrong for one of them.
#
# So the GRAFTED loop is renamed to `cardPips` and the live one is untouched.
# It is a BINDING NAME and not a drawing — nothing Design drew changes — and
# `cardVals` in LOGIC above emits `cardPips` to match. The expected old value
# is asserted at build time, so an index that drifts stops the build instead of
# repointing some other loop at a list that is not its own.
SET_EXPR = {
    "class view": {
        10330: ("pips", "cardPips"),
    },
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

        # ⊕ 23 Aug 2026 — PHASE 2. THE FLASHCARD SURFACE, IN TWO GRAFTS.
        #
        # ── 1. THE SIDEBAR CARD, AND IT IS A `replace` ────────────────────
        #
        # Design's own marker says what to do with it, in Design's own words:
        # donor 204 carries `data-port-change="C2 replaces the dark RECALL
        # card"`. Live node 136 IS that card — `background:var(--st-room)`,
        # #15110C, the one near-black slab in the sidebar — and it is the node
        # `student_themes.PAGE_CHROME_EXCEPTIONS` registered as a survivor with
        # the note "Design's C2 replaces this card wholesale … it stops
        # existing". That registration is retired in this same commit, from the
        # other end: an exception that cannot go stale is a hole.
        #
        # ⚠️ WHAT THE REPLACEMENT TAKES WITH IT, counted rather than assumed:
        #
        #   · `Start a round` — the card's `goRecall` button. The recall round
        #     is still reachable from the bench (`Practise recall` at node 77,
        #     `Start recall` at node 88) and from the nav, so no destination is
        #     lost. It is registered in `student_behaviour.RULED_CONTROLS`.
        #   · `retrievalCount` and its ANSWERED / THIS WEEK caption. The same
        #     count is drawn a second time inside the recall room (node 395),
        #     so the seam that carries it still has an anchor and still has a
        #     reader.
        #   · the `recallBlurb` sentence, whose ONLY text node on the whole page
        #     was node 142 inside this card. Its `BINDINGS` entry comes out in
        #     the same commit — measured, not guessed: `text_paths` finds it at
        #     exactly one path, and leaving the entry would stop the build with
        #     "the literal is not a text node in Design's template", which is
        #     that check doing its job.
        #
        # ── 2. THE OVERLAY, AND WHY IT IS THE `<if>` AND NOT THE `<div>` ──
        #
        # Donor 318 is `<if cardsOpen>`; donor 319 is the surface inside it.
        # Grafting 319 alone would put a `position:fixed;inset:0` scrim over
        # every student's class page, permanently, with no way to close it —
        # the graft would look like it worked and the page would be unusable.
        # The conditional IS the feature.
        #
        # `at=10, mode="append"`, for the two reasons the account sheet's graft
        # already records and one more:
        #
        #   · INSIDE `.rd[data-mode="ks3"]` (node 10), because every gate opens
        #     with `document.querySelector('.rd[data-mode="ks3"]')` and a
        #     surface grafted onto node 9 is one no gate can see.
        #   · LAST, and AFTER the sheet, because it is `z-index:50` against the
        #     sheet's 40 and painting order breaks ties. The sheet and the
        #     overlay are mutually exclusive in the logic, so this is belt and
        #     braces rather than load-bearing — which is the right amount of
        #     care for a scrim.
        #   · `append` and not `after`: `after` inserts into the PARENT, which
        #     would put the overlay outside `.rd` again.
        dict(at=136, mode="replace", donor=204,
             why="Design's C2, in Design's own words on the donor node: the "
                 "flashcards card replaces the dark RECALL card. It is the "
                 "deck's front door and its resume marker — the top card's "
                 "front, the stack position, and the FROM YOUR WORK chip when "
                 "that card comes from a lesson the student got something "
                 "wrong in."),
        dict(at=10, mode="append", donor=318,
             why="Design's C2 flashcards overlay, grafted as the `if cardsOpen` "
                 "rather than as the surface inside it, so it exists only when "
                 "a student has opened it. Header, pip row, the 460ms flip card "
                 "with its two faces, and the Reveal / Next pair."),

        # ⊕ 23 Aug 2026 — PHASE 3. THE RECALL ROUND.
        #
        # Donor 366 is `<if recallOpen>`; donor 367 is the surface inside it,
        # and it is the node Design marked
        # `data-port-change="C2b bench 'Practise recall' lands here"`.
        #
        # `at=10, mode="append"` for the three reasons the two grafts above
        # already record, and they hold here identically:
        #
        #   · INSIDE `.rd[data-mode="ks3"]` (node 10), because every gate opens
        #     with `document.querySelector('.rd[data-mode="ks3"]')` and a
        #     surface grafted onto node 9 is one no gate can see. This surface
        #     needs that more than either of the others: it is the one
        #     `student_themes` is being extended to open.
        #   · LAST, and after the sheet and the overlay. This is
        #     `position:fixed;inset:0;z-index:45` — between the sheet's 40 and
        #     the overlay's 50 — and painting order breaks ties. All three are
        #     mutually exclusive in the logic (each opener clears the other
        #     two), so this is belt and braces rather than load-bearing.
        #   · `append` and not `after`: `after` inserts into the PARENT, which
        #     would put the round outside `.rd` again.
        #
        # ⚠️ IT IS THE `<if>` AND NOT THE `<div>`, for the reason the overlay's
        # graft spells out: grafting 367 alone would put a `position:fixed`
        # full-screen panel over every student's class page, permanently, with
        # no way to close it. The conditional IS the feature.
        #
        # ── THE `THIS WEEK` PANEL IS OMITTED — donor 425 ──────────────────
        #
        # Design's round has a sidebar beside the question panel. It contains
        # exactly five things, and NOT ONE of them can ship:
        #
        #   ANSWERED       Design's `answered`, a THIS WEEK count. Nothing
        #                  anywhere records a recall round — `/api/class/recall`
        #                  only reads, and no table carries a class, a teaching
        #                  week and a rung together. `student-live.js` has
        #                  emitted `recallAnswered: ""` since the day the figure
        #                  was found to be a drawing, and it still does.
        #   BEST STREAK    a SESSION value under a WEEK heading. The number is
        #                  real inside one sitting and false the next morning,
        #                  when the student comes back to `00` having answered
        #                  thirty the day before. The round shows the streak
        #                  where it is honest — `streakLabel`, live, inside the
        #                  round itself.
        #   ROUNDS         `recallRounds`, the same unrecorded fact as ANSWERED.
        #   the sentence   *"Recall counts for 20 of the 100 points on the
        #                  leaderboard."* This is the SAME apportionment the
        #                  21 Aug ruling took out of the leaderboard's split bar
        #                  and its static 40 / 40 / 20 legend, because the
        #                  platform cannot compute it — and it is platform
        #                  self-explanation on a student page (§8.10).
        #   the button    `Open the assignment instead`, wired by Design to
        #                  `closeRecall`. It does not open the assignment. It
        #                  closes the round, which is what the two other
        #                  controls already do and say so.
        #
        # So the panel is three unsourceable figures, one sentence that is
        # ruled out twice over, and a button that names the wrong destination.
        # Keeping the frame and emptying the figures would have left a heading
        # over three blanks, which is the "empty bordered box" the `drop` flag
        # exists to prevent. It goes whole.
        #
        # ⚠️ NOTHING A STUDENT CAN DO IS LOST WITH IT. `closeRecall` is on TWO
        # surviving controls — the `8r/Sc1` button in the round's own bar
        # (donor 373) and `Back to my class` on the round-done card (donor 424).
        # Counted before this was written.
        #
        # `omit` and not `PRUNE`, for the reason the account sheet's EMAIL row
        # records: PRUNE walks the LIVE template and asserts every index was
        # found, and at that moment the donor has not been copied in yet. It
        # runs on the donor's own numbering, before the renumber, and asserts
        # 425 is present — so if Design redraws the sidebar, the build stops
        # rather than omitting nothing and shipping the sentence.
        #
        # Registered from the other end in `student_behaviour.AMENDED_OMISSIONS`.
        dict(at=10, mode="append", donor=366, omit=[425],
             why="Design's C2b recall round, grafted as the `if recallOpen` "
                 "rather than as the surface inside it, so it exists only once "
                 "a student has opened it from the bench. It REPLACES Design's "
                 "original round, which is pruned at live node 335 — the port "
                 "must not end up with two reachable recall surfaces. The THIS "
                 "WEEK sidebar is omitted: its three figures are facts nothing "
                 "records, and its one sentence states the 20-of-100 "
                 "apportionment the 21 Aug ruling already removed from the "
                 "leaderboard."),
    ],
    "assignment": [],
}
