#!/usr/bin/env python3
"""teacher_rulings.py — MRB-287's rulings, as source rather than as an edit.

⚠️ WHY THIS FILE EXISTS.

`student_rulings.py` exists because three of Mide's rulings were hand-edited
into GENERATED pages and the next build silently ate all three. This file is
the same mechanism for the teacher dashboard, written before that can happen
rather than after: `teacher/classes.html`, `teacher/class-detail.html` and
`teacher/student-detail.html` become build output under MRB-287, and from that
moment a fix typed into one of them survives exactly until the next
`python3 build_all.py`.

⊕ 24 Aug 2026 — `teacher/import.html` WAS ON THAT LIST AND IS NOT ANY MORE.
See `IMPORT_NOT_PORTED` below. It is hand-written source again, and the
sentence above used to name it.

Everything here is DATA. `build_teacher_port.py` reads it and applies it on the
way from Claude Design's delivery to the seven emitted pages. Nothing in this
file runs.

── WHAT DESIGN DELIVERED, AND WHY IT NEEDS RULINGS AT ALL ────────────────

Design's teacher delivery is ONE FILE holding SEVEN SCREENS behind a top-level
`sc-if` on `s.screen`, plus four overlays. Every number in it is invented — the
class list, the roster, the marks, the charts and the digest are all derived
from `seed()`, an FNV hash, so the sample is internally consistent and entirely
fictional. A port that shipped it unchanged would show a teacher twelve classes
they do not teach and fifty-four children who do not exist.

So the rulings do three separable things:

  1. SPLIT the one file into seven URLs, and rewire every screen-changing
     handler to a real navigation (`NAV`).
  2. CUT the invented data out and put the seam in its place (`METHODS`,
     `DROP_FIELDS`, `LOGIC`, `BINDINGS_AT`).
  3. REMOVE the controls that cannot work (`DEAD`), because a button that
     looks pressable and does nothing is worse than no button.

── THE MECHANISMS, AND WHICH ONE REACHES WHAT ───────────────────────────

    SCREENS/OVERLAYS  the seven `<if>` nodes and the four overlay `<if>`s.
                      Every page keeps its own and prunes the rest.
    DEAD              controls pruned on EVERY page, with the reason.
    SET_ON            a handler attached to a node Design left inert.
    NAV               a handler Design DID write, redefined to navigate, and
                      anchored on the nodes that carry it so a redraw stops
                      the build.
    SET_ATTR          `data-port-region` on every screen and overlay, so the
                      gates have an anchor that is not a node index.
    BIND_ATTR         an attribute whose VALUE is sample data, replaced by an
                      interpolation of a `renderVals` key.
    BINDINGS_AT       a text node whose literal is sample data, bound to a
                      data key at mount. Index-anchored AND literal-asserted.
    INSERT_AT         markup ADDED where Design drew no counterpart at all.
                      The last resort, and the only mechanism here that does
                      not work on something Design already drew.
    METHODS           a whole method body replaced, by balanced-brace scan.
    DROP_FIELDS       a class field deleted, by balanced-literal scan.
    DROP_KEYS         a `renderVals` return key deleted, by balanced scan.
    LOGIC             a guarded exactly-once source replacement for the rest.

Every one of them REFUSES THE BUILD when what it names is not there. That is
the whole point: a ruling that silently matched nothing is the same failure as
the hand-edit it replaces — the build goes green and the ruling is not in the
page.
"""

# ── the seven screens, by the flag they hang on ──────────────────────────
#
# Each is an `<if>` whose single child is the screen's own root `<div>`. The
# child is what carries `data-port-region`, because `student-runtime` renders
# an `<if>` as a BRANCH and never as an element — an attribute set on the `if`
# would be dropped, silently, and the gate anchoring on it would find nothing.
SCREENS = {
    "classes":  30,
    "class":    87,
    "student":  222,
    "marking":  258,
    "digest":   312,
    "import":   346,
    "insights": 401,
}

# ── the four overlays ────────────────────────────────────────────────────
#
# `setWorkOpen` is on this list so the build can PRUNE it by name on every
# page rather than by an index typed in seven places. It is kept by none of
# them; see `DEAD`.
OVERLAYS = {
    "setWorkOpen": 466,
    "bulkOpen":    513,
    "searchOpen":  538,
    "hasToast":    554,
}

# ── ⊕ RULED, MRB-287 · THE IMPORT WIZARD IS NOT PORTED ───────────────────
#
# ⛔ `teacher/import.html` IS HAND-WRITTEN SOURCE AND STAYS HAND-WRITTEN.
# It is NOT in `build_teacher_port.PAGES`, it IS in that build's `_REFUSED`
# guard, and it carries no "GENERATED — do not edit" banner because it is not
# generated. This constant exists so the decision is a recorded ruling rather
# than a gap somebody fills in by adding the row back.
#
# ── WHAT HAPPENED ───────────────────────────────────────────────────────
#
# The port emitted `import.html` for about half a day on 24 Aug 2026. Every
# gate was green. A teacher could not import students.
#
# Design's import screen (node 346) is a MOCK, and Design's own README says
# so: real CSV parsing is listed as not built. It draws three steps, a
# "Choose file" button wired to `impNext` — which advances the step WITHOUT
# taking a file, because the prototype has no file to take — a five-row
# mapping table with no controls in it, four invented children on the confirm
# step, and a button that toasts "26 students imported into 8r/Sc4".
#
# The hand-written page behind it is ~2,000 lines of working engine:
# papaparse and SheetJS, header detection, column mapping the teacher can
# CORRECT, per-class settings Design drew no counterpart for at all — year
# group, Combined/Triple, Foundation/Higher, teacher, subject — a dry run
# against the `roster-import` edge function, a per-row issues list, the
# confirm POST and a success summary. `roster-import` is one of only three
# write paths the whole teacher surface has.
#
# The port carried the wizard's ELEMENTS across as live regions — `#dropzone`,
# `#file-input`, `#screen-2`, `#success-panel` and five more — inside the
# hidden `#mrb-teacher-live-regions` wrapper. It did not, and could not, carry
# the engine: the engine is a 2,000-line inline script bound to those elements
# by id, and `live_regions()` lifts markup and deliberately leaves the
# original's stylesheet and scripts behind.
#
# ── WHY IT IS NOT REBUILT AGAINST DESIGN'S MARKUP ───────────────────────
#
# Because a third of the controls are not there to bind to. Design drew no
# per-class settings block, so a rebind would either drop year group, pathway,
# tier, teacher and subject — every one of which the import needs — or invent
# markup for them, which is a bigger act of design than porting. And the
# thing being risked is a feature that WORKS today and onboards whole schools.
#
# MRB-287's own words: "the live page's conditionals, loops and empty states
# survive the port intact. A wholesale file replacement is a failure of this
# run." The ported import page was a wholesale file replacement. Restoring it
# is the ticket being obeyed, not an exception to it.
#
# ── WHAT IS STILL TRUE OF THE OTHER SIX PAGES ───────────────────────────
#
#   · `SCREENS["import"] = 346` STAYS. Every other page must still PRUNE
#     Design's import screen, and that entry is how. It is the one screen in
#     Design's file that is never the screen a page keeps.
#   · Design's "Import students" (node 40) and the empty-class card (node 78 /
#     `c.open`, `act`) still navigate to `/teacher/import.html`. Those links
#     are CORRECT and must keep working — they now land on the real wizard
#     rather than on a picture of one.
#   · `RETEXT_AT` and the `data-import-slot` entries in `SET_ATTR` are KEPT
#     rather than deleted. They apply to no emitted page today — both loops
#     skip a node that is not on the page — and they are the anchoring work
#     that a future re-port of Design's screen would otherwise have to redo.
#     Stated here because a ruling that applies to nothing, unremarked, is
#     exactly the drift this file exists to prevent.
#   · The `impDone` and `mapRows`/`previewRows` entries in `LOGIC` are LOAD-
#     BEARING and must not be removed. They are source replacements on the
#     shared logic class, which every one of the six pages ships: take them
#     out and Design's four invented children and the "26 students imported
#     into 8r/Sc4" toast are back in the bytes of all six.
IMPORT_NOT_PORTED = dict(
    page="teacher/import.html",
    restored_from="docs/ks3/retired/teacher-import-2026-08-24-retired.html",
    screen_node=346,
    why="Design's import screen is a mock — its own README lists real CSV "
        "parsing as not built — and it draws no counterpart for the "
        "per-class settings the import needs. The hand-written wizard is the "
        "working feature; the port replaced it with its presentation.",
)


# ── ⊕ RULED, MRB-287 · THE SET-WORK FLOW IS A DEAD CONTROL, SO IT GOES ────
#
# Creating an assignment HAS NO WRITE PATH. Measured, not assumed: the only
# teacher-side writes that exist anywhere in the data layer are
# `insertClassShoutout` and `softDeleteClassShoutout` in
# `shared/teacher-data.js`, plus the `roster-import` edge function.
# Assignments are AUTO-GENERATED from `scheme_of_work_entries`; nothing in the
# client can create one and nothing in the schema is waiting for it to try.
#
# So Design's three-step "Set work" sheet is a sheet that would collect a
# topic, a question count, a due day and a class list, press a button, show a
# toast saying the work had been set, and set nothing. That is not an
# unfinished feature — it is a control that LIES, and MRB-287 forbids it
# outright.
#
# ⚠️ NODE 74 GOES AND NODE 78 STAYS, AND THE DIFFERENCE WAS CHECKED RATHER
# THAN ASSUMED. Both carry `c.act`, the class card's action link, and Design's
# `act` handler forks on the class's state:
#
#     act: (e) => { if (c.state === 'empty') → import
#                   else                     → the Set-work sheet }
#
# They are not one button in two states. They are TWO buttons in two different
# branches of the card: node 74 reads "Set work" inside `<if c.noWork>`, node
# 78 reads "Import" inside `<if c.empty>`. Only node 74 can ever reach the
# Set-work arm, and only node 78 can ever reach the import arm — so pruning 74
# removes the whole dead route and leaves the REAL one, which the ticket
# explicitly asks to preserve, exactly as Design drew it.
#
# ⊕ CORRECTED 24 Aug 2026. This paragraph used to end "`act` itself is
# rewritten to import-only in `METHODS`, so the sheet is unreachable from
# the logic as well as from the markup." It was not rewritten anywhere, and
# the sentence is kept rather than deleted because believing it is what let
# the defect ship: `act` set `screen: 'import'` on a page whose import screen
# had just been pruned, and the class list went blank. It is rewritten now —
# in `NAV`, under the key `c.act`, because it is a loop-scoped closure and
# `METHODS` cannot reach one.
DEAD = (
    (466, "the Set-work sheet itself. Three steps, a summary line and a "
          "confirm button, in front of a write path that does not exist."),
    (38,  "\"Set work\" — the primary action on the classes screen."),
    (103, "\"Set work\" — the primary action on the class screen."),
    (193, "\"Set work\" — the empty-state prompt on a class with no "
          "assignments. The emptiest possible dead control: it is the only "
          "thing on screen and it does nothing."),
    (267, "\"Set work\" — the marking screen's header action."),
    (74,  "\"Set work\" on a class card that has students but no work set. "
          "See the note above for why its twin at node 78 survives."),
)


# ── a handler Design never attached ──────────────────────────────────────
#
# ⚑ NODE 29 IS A DEAD CONTROL DESIGN DREW BY ACCIDENT. It is a `<button>`
# reading "Sign out", in the sticky top bar, on every one of the seven
# screens, with NO `onClick` at all — in a single-file prototype there is
# nowhere to sign out to. Shipped as drawn it is a button a teacher presses to
# leave a page holding live student data, that does nothing.
#
# `MrBadmusTeacherGuard.signOut()` is the real one, and it is the same call
# the four hand-written teacher pages already make. `teacher-guard.js`
# documents it in its own header (`<button onclick="MrBadmusTeacherGuard
# .signOut()">Sign out</button>`), so this is the port catching up with the
# live pages rather than inventing anything.
#
# `SET_ON` REFUSES a node that already carries a handler, exactly as it does
# in `student_rulings`: silently replacing an `onClick` Design drew would swap
# one working control's behaviour for another's, and the page would still look
# and gate exactly right.
SET_ON = {
    29: "signOut",
}




# ── ⊕ RULED, MRB-287 · SEVEN URLS, SO EVERY SCREEN CHANGE IS A NAVIGATION ─
#
# Design's file is a prototype: its buttons move `s.screen` and the browser
# never leaves the page. Ours are seven separate URLs, so every one of those
# handlers has to become a real navigation or become a dead control.
#
# ⚠️ THIS IS NOT `student_rulings.SET_ON`, AND IT CANNOT BE. `SET_ON` attaches
# a handler to a node that has NONE. Every node below already carries one of
# Design's own — and half of them are LOOP-SCOPED (`c.open`, `s.open`,
# `a.open`, `h.open`, `r.open`, `d.open`), where the destination depends on the
# ROW that was clicked and therefore cannot be expressed as a different handler
# NAME at all. The only place a per-row destination can be written is the
# closure that builds the row.
#
# So the rewiring happens in the LOGIC, and the NODES are used as an
# ASSERTION: each index below must exist AND must still carry the named
# handler. That is the half `SET_ON` gives for free and a bare source
# replacement would lose — if Design redraws the class card and its `onClick`
# moves, the build stops instead of rewriting a handler nothing calls.
#
# ── THE QUERY STRING IS teacher-live.js's, NOT THIS FILE'S ────────────────
#
# ⚠️ AND IT WAS NEARLY WRONG. `shared/teacher-live.js` reads its parameters in
# `run()`:
#
#     load(q.get("screen") || "classes", { classId:  q.get("class"),
#                                          studentId: q.get("student"),
#                                          paperIdx:  q.get("paper") })
#
# Three consequences, each of which would have shipped as a page that looked
# right and held the wrong data:
#
#   · the names are `class`, `student`, `paper`, `screen`. Not `assignment`.
#   · `paper` is an INDEX into the class's own paper list, not an id. The
#     first draft of these rulings sent `?assignment=<p.id>`, which
#     `teacher-live` would have read as no paper at all, prefetched no grid,
#     and drawn a marking screen with an empty question table.
#   · `screen` is what decides WHICH GRIDS ARE PREFETCHED. The filename does
#     not tell `teacher-live` anything, so every link carries it. It is
#     redundant with the URL to a reader and load-bearing to the seam.
#
# `env` threading is preserved throughout. The live pages already do it
# (`teacher/classes.html`: `const env = …environment === 'test' ? '&env=test'
# : ''`), and dropping it would send a teacher testing in the sandbox back
# into production data one click later.
#
# ── ⊕ MRB-287 E1 · AND `year`, ON EXACTLY TWO OF THEM ────────────────────
#
# `c.open` (a card into its class) and `goClasses` (Back, out of one) carry
# `year: MRB_DATA('yearParam')`. Those two and no others, for two reasons:
#
#   · `yearParam` is EMPTY on the working year and `MRB_GO` drops an empty
#     param, so the ordinary URL is unchanged byte-for-byte and the bookmark
#     a teacher keeps never pins a year they will have left by September.
#   · every OTHER navigation already carries `?class=`, and `teacher-live.js`
#     resolves a class's own academic year when it is not the one in view.
#     Threading `year` through them as well would put a redundant uuid in
#     five more URLs to answer a question the class id already answers.
#
# The pair matters because they are the two that would otherwise LOSE the
# year: a card press from a 2025-26 grid, and the Back out of the class it
# opened. Without it a teacher browsing last year is silently returned to
# this one, which is the dead end MRB-261 exists to remove.
#
# ── nodes whose role differed from the brief, and were rewired to what
#    they ACTUALLY are ──────────────────────────────────────────────────
#
#   304  the brief calls it "digest row -> class detail". It is not: node 304
#        sits inside `<for paper.grid>` inside `<if isMarking>` — it is a ROW
#        OF THE QUESTION GRID on the marking screen, and Design's own closure
#        reads `open: () => this.setState({ screen: 'student', studentId:
#        r.id })`. Wired to the STUDENT page, which is what it is.
#   338  the brief calls it "d.open … /teacher/digest.html (verify)". Verified:
#        node 338 sits inside `<for digestRows>` inside `<if isDigest>` — it is
#        a row OF the digest, and it opens the class that row is about. Wired
#        to CLASS DETAIL. Wiring it to digest.html would have been a row on the
#        digest that reloads the digest.
NAV = {
    "goClasses": dict(
        # ⊕ NODE 348 WAS HERE AND HAD TO GO, 24 Aug 2026. It is the import
        # screen's Back button, and the import screen is no longer emitted on
        # any page (`IMPORT_NOT_PORTED`), so the build's closing sweep —
        # which refuses a NAV node that was never checked on ANY page —
        # refused it. The handler rewrite itself is unaffected: 11 and 89
        # still carry it and are still asserted.
        nodes=(11, 89),
        frm="      goClasses: () => this.setState({ screen: 'classes', "
            "modal: null }),",
        to="      goClasses: () => MRB_GO('classes', "
           "{ year: MRB_DATA('yearParam') }),",
        why="the brand mark in the top bar (11) and the class screen's Back "
            "(89). Design's node 348 — the import screen's Back — is drawn by "
            "the same handler and is not emitted; see the note above."),
    "goClass": dict(
        nodes=(224, 260),
        frm="      goClass: () => this.setState({ screen: 'class', modal: "
            "null }, () => this.snapWeekRail()),",
        to="      goClass: () => MRB_GO('class', { 'class': k && k.id }),",
        why="the student screen's Back (224) and the marking screen's Back "
            "(260). `snapWeekRail` was a scroll fix for a rail that had never "
            "left the DOM; there is no rail to restore across a navigation."),
    "goDigest": dict(
        nodes=(39,),
        frm="      goDigest: () => this.setState({ screen: 'digest', "
            "digestScope: 'all' }),",
        to="      goDigest: () => MRB_GO('digest', {}),",
        why="\"Weekly digest\". No `class` parameter IS `digestScope: 'all'` "
            "— see the state initialiser, which derives the scope from the "
            "presence of the parameter so a reload cannot lose it."),
    "goReport": dict(
        nodes=(106,),
        frm="      goReport: () => this.setState({ screen: 'digest', "
            "digestScope: 'class' }),",
        to="      goReport: () => MRB_GO('digest', { 'class': k && k.id }),",
        why="\"Class report\" — the same page as the digest, scoped to one "
            "class, which is what `digestScope: 'class'` meant in the "
            "prototype."),
    "goImport": dict(
        nodes=(40,),
        frm="      goImport: () => this.setState({ screen: 'import', "
            "importStep: 1 }),",
        to="      goImport: () => MRB_GO('import', {}),",
        why="\"Import students\" on the classes screen."),
    "openInsights": dict(
        nodes=(22, 105),
        frm="      openInsights: () => this.setState({\n"
            "        screen: 'insights',\n"
            "        insFrom: s.screen === 'class' ? 'class' : 'classes',\n"
            "        chartScope: s.screen === 'class' ? k.id : chartScope\n"
            "      }),",
        to="      openInsights: () => MRB_GO('insights', s.screen === "
           "'class' ? { 'class': k && k.id } : {}),",
        why="the chart icon in the top bar (22) and \"Charts\" on the class "
            "screen (105). Design's handler carried the scope with it — from "
            "a class it opened scoped to that class, from anywhere else to "
            "all classes — and that fork survives as the presence or absence "
            "of `?class=`. `insFrom` goes: the browser's history is the back "
            "stack now."),
    "goBackFromDigest": dict(
        nodes=(314,),
        frm="      goBackFromDigest: () => this.setState({ screen: "
            "s.digestScope === 'class' ? 'class' : 'classes' }, () => { if "
            "(s.digestScope === 'class') this.snapWeekRail(); }),",
        to="      goBackFromDigest: () => MRB_BACK(),",
        why="the digest's Back. Design chose between two destinations from "
            "state; the browser knows the real answer, and a digest opened "
            "from a bookmark has no state to consult. `MRB_BACK` falls "
            "through to the class list when there is no history, so it is "
            "never a dead press."),
    "goBackFromInsights": dict(
        nodes=(403,),
        frm="      goBackFromInsights: () => this.setState({ screen: "
            "s.insFrom || 'classes' }, () => { if ((s.insFrom || 'classes') "
            "=== 'class') this.snapWeekRail(); }),",
        to="      goBackFromInsights: () => MRB_BACK(),",
        why="the charts screen's Back. Same reasoning as the digest's."),

    # ── the loop-scoped six ─────────────────────────────────────────────
    "c.open": dict(
        nodes=(52,),
        frm="      open: () => c.n > 0\n"
            "        ? this.openClass({ classId: c.id })\n"
            "        : this.setState({ screen: 'import', importStep: 1 }),",
        to="      open: () => MRB_GO(c.n > 0 ? 'class' : 'import', "
           "{ 'class': c.id, year: MRB_DATA('yearParam') }),",
        why="the class card. ⚠️ DESIGN'S FORK IS KEPT: a card with no "
            "students opens the IMPORT screen, not an empty class page. That "
            "route is real — `roster-import` is one of the three writes that "
            "exist — and the brief's one-line version of this rewiring would "
            "have sent a teacher with an empty class to a page with nothing "
            "on it."),
    "s.open": dict(
        nodes=(140,),
        frm="        open: () => this.setState({ screen: 'student', "
            "studentId: r.id })\n      };\n    });\n\n    const paperRow",
        to="        open: () => MRB_GO('student', { student: r.id, 'class': "
           "k && k.id })\n      };\n    });\n\n    const paperRow",
        why="a roster row on the class screen. ⚠️ ANCHORED ON THE FIVE LINES "
            "THAT FOLLOW IT, because the closure's own text is BYTE-IDENTICAL "
            "to the marking grid's at node 304, and an exactly-once "
            "replacement would refuse the build on a count of two."),
    "a.open": dict(
        nodes=(166, 181),
        frm="      open: () => this.setState({ screen: 'marking', paperId: "
            "p.id })\n    });\n\n    const flagged",
        to="      open: () => MRB_GO('marking', { 'class': k && k.id, paper: "
           "p.idx })\n    });\n\n    const flagged",
        why="the upcoming (166) and marked (181) assignment rows. Both are "
            "drawn by the one `paperRow` closure, so one rewrite serves both "
            "nodes — which is why both are asserted here."),
    "h.open": dict(
        nodes=(250,),
        frm="        open: () => this.setState({ screen: 'marking', paperId: "
            "p.id })\n      };\n    }) : [];",
        to="        open: () => MRB_GO('marking', { 'class': k && k.id, "
           "paper: p.idx })\n      };\n    }) : [];",
        why="a row of the student's assignment history. Anchored on its "
            "trailing `}) : [];` for the same reason `s.open` is."),
    "r.open (marking grid)": dict(
        nodes=(304,),
        frm="      open: () => this.setState({ screen: 'student', studentId: "
            "r.id })\n    })) : [];",
        to="      open: () => MRB_GO('student', { student: r.id, 'class': "
           "k && k.id })\n    })) : [];",
        why="a row of the marking screen's question grid — NOT a digest row."),
    "d.open": dict(
        nodes=(338,),
        frm="        open: () => c.n > 0 ? this.openClass({ classId: c.id, "
            "digestScope: 'all' }) : this.ping('No students in ' + c.code + "
            "' yet')",
        to="        open: () => c.n > 0 ? MRB_GO('class', { 'class': c.id }) "
           ": this.ping('No students in ' + c.code + ' yet')",
        why="a row of the weekly digest. Design's empty-class arm is KEPT as "
            "a toast: it is not a navigation and never was, and silently "
            "doing nothing would be the dead control the toast avoids."),
    # ⊕ RULED 24 Aug 2026 — AND IT WAS SHIPPING BLANK. This file's own note
    # above `DEAD` said "`act` itself is rewritten to import-only in
    # `METHODS`". It was not: `act` is a LOOP-SCOPED closure inside the
    # `cards` map, not a method, and no ruling touched it. So the "Import"
    # link on an empty class card ran `this.setState({ screen: 'import' })` —
    # on a page where `s.screen` is fixed to `'classes'` and Design's import
    # screen has been PRUNED. Every screen `<if>` evaluated false and the page
    # rendered NOTHING. Green on every gate, because `teacher_behaviour`
    # measures "did the press change something" and a page going blank is a
    # change, and it photographs the page BEFORE the sweep.
    #
    # The else-arm goes with it: it opens the Set-work sheet, and the only
    # node that could ever reach it is node 74, which `DEAD` prunes. `act` is
    # import-only now, which is what the note above `DEAD` always claimed.
    #
    # ⚠️ ANCHORED ON NODE 78 ALONE, not on 74 as well. `DEAD` prunes 74 from
    # every page, and the build's closing sweep refuses a NAV node that was
    # never present on ANY page — 74 would fail it. That node's existence is
    # asserted by `DEAD` instead, which is the right owner.
    "c.act": dict(
        nodes=(78,),
        frm="      act: (e) => {\n"
            "        e.stopPropagation();\n"
            "        if (c.state === 'empty') this.setState({ screen: "
            "'import', importStep: 1 });\n"
            "        else this.setState({ modal: 'setwork', swStep: 1, "
            "swClasses: [c.id] });\n"
            "      }",
        to="      act: (e) => { e.stopPropagation(); "
           "MRB_GO('import', { 'class': c.id }); }",
        why="\"Import\" on a class card with no students. The one route into "
            "the roster importer from the class list, and it was rendering a "
            "blank page."),

    "r.open (search)": dict(
        nodes=(548,),
        frm="      open: () => this.setState({ screen: 'student', classId: "
            "p.classId, studentId: p.id, modal: null })",
        to="      open: () => MRB_GO('student', { student: p.id, 'class': "
           "p.classId })",
        why="a result row in the search overlay. It is the one navigation "
            "that changes CLASS as well as student, which is why it reads "
            "`p.classId` rather than the page's own `k.id`."),
}


# ── every ported region gets a name the gates can anchor on ──────────────
#
# A node index is the wrong thing for a gate to hold: it is Design's
# numbering, it moves whenever Design redraws, and a gate asserting on one
# reports a redraw as a missing region. `data-port-region` is ours, stable
# across a redraw, and says what the region IS.
#
# Set on the screen's own root `<div>` rather than on the `<if>` above it — an
# `<if>` is a branch and carries no element, so an attribute on one is
# silently dropped and the gate would find nothing.
#
# `data-import-slot` is the same idea for a different job: see `RETEXT_AT`.
SET_ATTR = {
    10:  {"data-port-region": "topbar"},
    31:  {"data-port-region": "classes"},
    88:  {"data-port-region": "class"},
    223: {"data-port-region": "student"},
    259: {"data-port-region": "marking"},
    313: {"data-port-region": "digest"},
    347: {"data-port-region": "import"},
    402: {"data-port-region": "insights"},
    514: {"data-port-region": "overlay-bulk"},
    539: {"data-port-region": "overlay-search"},
    555: {"data-port-region": "toast"},
    # ⊕ THE TWO COMPOSER FIELDS, so the send can CLEAR them. Design's select
    # and textarea are uncontrolled — neither carries a `value` — and
    # `student-runtime` deliberately carries field values across a redraw, so
    # clearing `s.recipient` and `s.note` clears the state and leaves the
    # typed text on screen. `MRB_COMPOSE_RESET` empties the DOM first, and
    # this is how it finds them without an id Design did not write.
    200: {"data-compose-field": "recipient"},
    209: {"data-compose-field": "note"},

    # ⚠️ THE FIVE `data-import-slot` ROWS BELOW APPLY TO NO EMITTED PAGE. They
    # are the import screen's nodes and the import screen is not ported (see
    # `IMPORT_NOT_PORTED`); both loops that read this table skip a node that
    # is not on the page. Kept, not deleted, because they are the anchoring
    # work a future re-port would otherwise redo — and said out loud here,
    # because a ruling that quietly applies to nothing is the drift this file
    # exists to stop.
    368: {"data-import-slot": "fileName"},
    369: {"data-import-slot": "fileSummary"},
    384: {"data-import-slot": "newCount"},
    387: {"data-import-slot": "matchedCount"},
    390: {"data-import-slot": "attentionCount"},
    400: {"data-import-slot": "confirm"},
}


# ── an ATTRIBUTE whose value is sample data ──────────────────────────────
#
# ⚠️ `BINDINGS_AT` CANNOT REACH THIS ONE, and that was checked rather than
# assumed. `student-runtime.applyBindings` walks to a node and refuses unless
# it lands on a TEXT node (`node.t !== "#"` throws by name). The search box's
# sample count is not text — it is `placeholder="Search students across all 12
# classes"`, an attribute on node 545 — so there is no text node for a binding
# path to land on.
#
# What the compiled template DOES support in an attribute is an interpolation:
# `{"parts": [...]}`, the same shape Design's own `style` attributes use forty
# times over. So the attribute becomes an interpolation of a `renderVals` key,
# computed beside `searchFoot` — Design's own idiom for exactly this sentence
# one line further down the same overlay.
BIND_ATTR = {
    # ⊕ RULED, 24 Aug 2026 — THE RECIPIENT SELECT SENDS AN ID, NOT A NAME.
    # Design models the recipient as `pickRecipient: (e) => this.setState({
    # recipient: e.target.value })` over a `<select>` whose options are
    # `value="{{ s.name }}"`, and its `sendShoutout` then toasts "Shoutout
    # sent to " + that name. A name is not a key: `insertClassShoutout` needs
    # `recipient_id`, RLS checks that the recipient is an active member of
    # this class, and two children in one class can share a first name and a
    # surname. So the OPTION carries the roster row's real id, and the roster
    # row gained an `id` field in `LOGIC` to put there.
    #
    # ⚠️ THIS IS AN ATTRIBUTE AND NOT A TEXT NODE, so `BINDINGS_AT` cannot
    # reach it — the same reason the search placeholder is here. The visible
    # LABEL stays `s.name`; only the value changes.
    203: ("value",
          {"parts": [{"e": "s.name"}]},
          {"parts": [{"e": "s.id"}]},
          "the shoutout recipient. Design's option value is the child's "
          "NAME; the write path needs the id, and the id is what identifies "
          "a child."),
    545: ("placeholder",
          "Search students across all 12 classes",
          {"parts": [{"e": "searchPlaceholder"}]},
          "the 12 is this teacher's real class count. Design drew a teacher "
          "with twelve classes; a teacher with three would be invited to "
          "search across twelve. teacher-live.js computes the whole sentence "
          "— including the singular form for a teacher with one class."),
}


# ── text nodes Design typed that are SAMPLE DATA, not copy ───────────────
#
# `{node: (exact literal, seam key)}` — INDEX-anchored and LITERAL-asserted,
# both. `student_rulings` binds by literal alone, which is right there because
# one value (`8r/Sc1`) is typed in several places and all of them mean the
# same class. Here the opposite is true, and the import counts are why: `24`,
# `2` and `1` are three DIFFERENT figures, and a literal-keyed table would
# bind every text node reading `2` anywhere on the page.
#
# ⚠️ EVERY KEY BELOW IS ONE `shared/teacher-live.js` ACTUALLY EXPORTS. A key
# one side emits and the other never supplies is a thrown error on a real
# page, so the names are taken from that file's own `load()` return rather
# than chosen here.
BINDINGS_AT = {
    # ── the top bar, on every page ──────────────────────────────────────
    #
    # ⊕ AND IT IS **NOT** DROPPED WHEN EMPTY, WHICH IS THE OPPOSITE OF THE
    # RULING ON THE STUDENT PAGE, DELIBERATELY. P6 pruned the student's `PROD`
    # chip because a developer's instrument had wandered onto a product a
    # child reads. A teacher dashboard is a working instrument for an adult,
    # and the four hand-written teacher pages ALREADY carry this badge, PROD
    # included, styled `.pill.env-prod` — it is the thing that stops somebody
    # driving the wrong database.
    27:  ("PROD", "envBadge"),

    # ── the classes screen ──────────────────────────────────────────────
    34:  ("Autumn term · 2026–27", "termLabel"),
    84:  ("Viewing 2026–27", "viewingYearLabel"),
    # ⊕ MRB-287 E1 — the year toggle's own label. "Previous years" is right
    # only while the WORKING year is in view; opened FROM a past year the same
    # list leads forward as well, and the retired hand-written page said
    # "other years" for exactly that case
    # (teacher-classes-2026-08-24-retired.html:677). It is `pastYearsLabel`,
    # computed in the seam, and it is the reason that key is no longer dead.
    86:  ("Previous years", "pastYearsLabel"),

    # ── the digest ──────────────────────────────────────────────────────
    319: ("Mon 17 – Fri 21 Aug 2026", "weekRangeLabel"),

    # ── the charts screen ───────────────────────────────────────────────
    408: ("Week of Mon 17 Aug 2026", "weekOfLabel"),
}


# ── text nodes that are sample data with NO seam key, on purpose ─────────
#
# ⚑ THE IMPORT WIZARD IS THE ONE PLACE WHERE "LIVE LOGIC WINS" MEANS THE SEAM
# MUST STAY OUT OF IT. `teacher-live.js` returns `IMPORT_MAP_ROWS: []`,
# `IMPORT_PREVIEW_ROWS: []` and `importCountLabel: ""` and says why in its own
# comment: the CSV mapping, the row preview and the count are all things the
# LIVE wizard already computes — it parses the file, counts the rows and the
# columns, runs a dry-run against `roster-import` and counts what came back.
# Filling them from the data layer would be a second implementation of a
# wizard that works.
#
# So these five figures cannot be bound to a key, and they cannot be left
# either: `year8-autumn.csv`, `27 rows · 5 columns`, `24`, `2` and `1` are a
# file nobody uploaded and counts of rows nobody parsed. They are BLANKED at
# build time and their elements carry `data-import-slot` (see `SET_ATTR`), so
# the live wizard writes into Design's own presentation.
#
# ⚠️ THE SIXTH IS DIFFERENT AND IS NOT BLANKED. `Import 26 students` is a
# BUTTON, and an empty button is not a smaller button — it is an unpressable
# rectangle. Its count is fiction and its verb is not, so the count goes and
# the verb stays. The slot is still there for the wizard to put the number
# back once it has one.
#
# `{node: (exact literal, replacement text, why)}`.
RETEXT_AT = {
    368: ("year8-autumn.csv", "",
          "a file nobody uploaded."),
    369: ("27 rows · 5 columns", "",
          "counts of a file nobody parsed."),
    384: ("24", "",
          "\"New students\" — a dry-run nobody ran."),
    387: ("2", "",
          "\"Matched existing\" — same."),
    390: ("1", "",
          "\"Needs attention\" — same, and the one a teacher would act on."),
    400: ("Import 26 students", "Import students",
          "the button. 26 is fiction; \"Import\" is not. An empty button is "
          "an unpressable rectangle, so the count goes and the verb stays."),
}


# ── markup Design drew no counterpart for ────────────────────────────────
#
# ⚑ THE LAST RESORT, AND THE ONLY MECHANISM IN THIS FILE THAT ADDS MARKUP.
# Everything else here works on something Design drew. These two states cannot,
# because Design's sample cannot reach either of them: its class list always
# holds both key stages, and its question grid has three cell states where the
# seam can now produce four.
#
# Design's README states the rule both of them break: "Empty states are
# states, not blanks", and "every state a teacher can reach has a name on the
# page". Finishing a control Design added is not new scope; shipping it
# unfinished is.
#
# ⚠️ EACH ONE COPIES ITS TYPE TREATMENT OFF A NODE DESIGN DID DRAW, verbatim,
# rather than inventing a register — the filtered-empty card off Design's own
# "No work set for this class" panel (node 189), the legend key off its three
# siblings inside node 288. If Design redraws either, the copy here will look
# wrong before it reads wrong, which is the failure mode to want.
#
# `{parent node: (insert after this child node or None to append, subtree,
#   why)}`. Nothing inserted carries an `i`: Design's numbering is what every
# other ruling in this file is anchored on and it must not move.

_LEGEND_KEY = ("display:flex;align-items:center;gap:6px;"
               "font:400 12px/1.2 var(--st-mono);letter-spacing:.12em;"
               "text-transform:uppercase;color:var(--st-caption)")

# ── ⊕ MRB-287 E1 · the year selector's two treatments ────────────────────
#
# Both are Design's own, copied off nodes she DID draw rather than invented:
#
#   `_YEAR_OPTION` is node 86's exact style string — the "Previous years"
#   toggle it sits under — with one substitution: `--st-caption` becomes
#   `--st-accent-text`, which is the token Design uses on every other
#   in-place ACTION link in this delivery (node 78's "Import", node 196's
#   "Send to several students"). The toggle is chrome and the options are
#   actions, and those are Design's two colours for exactly that difference.
#
#   `_READONLY_CHIP` is node 96's pill — the subject-dots chip beside the
#   class code in the same header row — at Design's own measurements, with
#   node 84's mono caption register for the text inside it.
_YEAR_OPTION = ("font:400 12px/1.4 var(--st-mono);letter-spacing:.14em;"
                "text-transform:uppercase;color:var(--st-accent-text);"
                "background:none;border:none;padding:2px 0;cursor:pointer;"
                "text-decoration:underline;text-underline-offset:3px")

_YEAR_LIST = "display:flex;align-items:center;gap:8px;flex-wrap:wrap"

_READONLY_CHIP = ("display:flex;align-items:center;gap:6px;padding:6px 9px;"
                  "border:1px solid var(--st-rule);border-radius:9px")

_READONLY_TEXT = ("font:400 12px/1.4 var(--st-mono);letter-spacing:.14em;"
                  "text-transform:uppercase;color:var(--st-caption)")


# ── ⊕ RULED, MRB-287 · A THIRD CATEGORY: MARKUP MIDE ASKED FOR ───────────
#
# The two entries above FINISH a control Design drew. The shoutout delete
# control does not — Design's feed card (nodes 215–221) has no delete
# affordance of any kind, and her delivery is not incomplete in drawing none.
#
# ⚑ MIDE'S INSTRUCTION, 24 Aug 2026: *"The shoutout is already part of
# Design's build. The delete control may not be in her delivery; Mide's
# instruction is to add it. A teacher who can post a shoutout can remove one.
# Treat it as an AMENDED_ADDITION against her delivery, not a departure."*
#
# So it is registered as one — see `AMENDED_ADDITIONS` below, which the build
# asserts against the emitted bytes. This file has never before added a
# control that Design did not draw, and a category that is not written down is
# a category the next reader has to infer from two entries that do not fit it.
#
# ⚠️ EVERY STYLE BELOW IS COPIED OFF A NODE DESIGN DID DRAW, verbatim, which
# is the rule the two entries above already keep:
#
#   the "Remove" button   Design's own low-emphasis text button — the
#                         "Back to <class>" control on the student screen:
#                         `font:600 14.5px/1.2 var(--st-ui);color:
#                         var(--st-muted);background:none;border:none;
#                         padding:0;cursor:pointer` with `style-hover`
#                         `color:var(--st-ink)`. It rests in the same
#                         register as the timestamp beside it (node 219) and
#                         the CONFIRM carries the weight.
#   the confirm sheet     Design's bulk-shoutout sheet (nodes 513–537): the
#                         scrim, the panel, the header row, the close X and
#                         its 12x12 path, the body pad, the footer bar and
#                         the primary button, all at her measurements. This
#                         port has ONE dialog idiom and this is it; a second
#                         one invented here is how a page starts disagreeing
#                         with itself about what a dialog looks like.
#
# ⚠️ AND IT IS A SHEET AND NOT A `window.confirm`. Two reasons, and the
# second is not the aesthetic one. Design drew three overlays and the page has
# a dialog idiom, so a browser dialog would be the odd surface out — and
# `teacher_behaviour.py` PRESSES every control on the fixtures in headless
# Chrome, where a `window.confirm` blocks the sweep on a dialog nothing
# answers. The gate would hang rather than fail, which is the worse of the
# two.
#
# ⚠️ `data-mrb-added` IS NOT DECORATION. `teacher_behaviour.clickable()`
# collects `[data-dc-tpl]`, and `data-dc-tpl` is written from a node's `i` —
# which INSERT_AT deliberately does not give an inserted node, so that
# Design's numbering cannot move. The consequence, found on this run and
# stated rather than left implied: **markup inserted by INSERT_AT was
# invisible to the drive gate.** Neither existing insertion holds a control,
# so nothing was going unpressed; this one is four controls, and a delete
# button no gate can press is exactly the dead control this whole port is
# trying not to ship. The attribute is a STRING, so it can never collide with
# Design's integer indices, and `teacher_behaviour` now sweeps it too.
_DEL_TEXT_BTN = ("flex:none;font:600 14.5px/1.2 var(--st-ui);"
                 "color:var(--st-muted);background:none;border:none;"
                 "padding:0;cursor:pointer")

# Design's own sheet, node for node: 514 scrim, 515 panel, 516 header bar,
# 518 kicker, 519 title, 520 close, 523 body pad, 535 footer bar, 536 footer
# caption, 537 primary button.
_DEL_SCRIM = ("position:fixed;inset:0;z-index:60;background:rgba(26,23,20,.45);"
              "display:flex;align-items:center;justify-content:center;"
              "padding:40px 20px")
_DEL_PANEL = ("width:720px;max-width:100%;max-height:86vh;overflow:auto;"
              "background:var(--st-paper);border:1px solid var(--st-edge);"
              "border-radius:14px;box-shadow:var(--st-shadow-frame)")
_DEL_HEAD = ("display:flex;align-items:center;justify-content:space-between;"
             "gap:12px;padding:20px 24px;"
             "border-bottom:1px solid var(--st-rule-soft)")
_DEL_KICKER = ("font:500 12px/1.2 var(--st-mono);letter-spacing:.18em;"
               "text-transform:uppercase;color:var(--st-caption)")
_DEL_TITLE = ("margin-top:9px;font:600 27px/1 var(--st-display);"
              "letter-spacing:-0.03em;color:var(--st-ink)")
_DEL_CLOSE = ("flex:none;width:32px;height:32px;display:flex;"
              "align-items:center;justify-content:center;"
              "background:transparent;border:1px solid var(--st-btn-border);"
              "border-radius:9px;cursor:pointer;color:var(--st-muted)")
_DEL_BODY = "padding:22px 24px"
_DEL_PROSE = "font:400 15.5px/1.55 var(--st-ui);color:var(--st-body)"
_DEL_FOOT = ("display:flex;align-items:center;justify-content:space-between;"
             "gap:14px;padding:16px 24px;"
             "border-top:1px solid var(--st-rule-soft);"
             "background:var(--st-crumb-bg)")
_DEL_FOOT_NOTE = ("font:400 12.5px/1.4 var(--st-mono);letter-spacing:.1em;"
                  "text-transform:uppercase;color:var(--st-caption)")
_DEL_PRIMARY = ("flex:none;height:38px;padding:0 18px;"
                "font:600 15px/1.2 var(--st-ui);color:var(--st-paper);"
                "background:var(--st-accent-text);border:none;"
                "border-radius:9px;cursor:pointer")

INSERT_AT = {
    # ── the fourth glyph gets a name ────────────────────────────────────
    #
    # ⛔ THE GRID DRAWS FOUR STATES AND THE LEGEND NAMED THREE. `cellStyle(3)`
    # was added for `is_correct IS NULL` — answered, and self-marked or
    # written, so the platform holds no correctness claim — and it draws a
    # filled square, distinct from the dot, the ring and the dash. Nothing on
    # the page said what it meant. A teacher reading eight unexplained squares
    # against one child's name has no way to know they are not a failure.
    #
    # ⚠️ THE WORDING SAYS WHAT THE STATE IS. "Not machine-marked" and "No
    # mark" both describe an absence, and an absence beside CORRECT and
    # INCORRECT reads as a third kind of wrong. It is neither: the child
    # answered, and the answer is one a machine cannot mark. Hence
    # "Self-marked or written" — the two things the state actually is, in
    # Design's own uppercase mono, in the register of the three keys beside
    # it.
    288: (293, {
        "t": "span", "a": {"style": _LEGEND_KEY},
        "c": [
            {"t": "span", "a": {"style": "width:9px;height:9px;"
                                         "border-radius:2px;"
                                         "background:var(--st-hatch-b)"}},
            {"t": "#", "v": "Self-marked or written"},
        ]},
        "the fourth key on the class-by-question legend. The swatch is "
        "`cellStyle(3)`'s own geometry and colour, read off that ruling "
        "rather than retyped as a guess."),

    # ── a filter that matches nothing is still a state ──────────────────
    #
    # ⛔ FILTER TO A KEY STAGE THE TEACHER DOES NOT TEACH AND THE GRID GOES
    # BLANK. The chrome above it still reads "0 SHOWN" and the sort controls
    # stay live, so the page looks like it failed rather than like it
    # answered. Reachable by any teacher who teaches one key stage and presses
    # the other, which is most of them.
    #
    # ⚠️ IT NAMES THE FILTER, NOT THE TEACHER'S CLASS LIST. "No classes yet"
    # here would be a lie — they have classes, they filtered them out — and it
    # would also COMPETE with the seam's own no-classes sentence, which
    # `teacher-live.js` throws before mount (`SAY.noClasses`) so that the
    # truly-empty case never reaches this grid at all. Two sentences for one
    # condition is how a page ends up disagreeing with itself.
    31: (50, {
        "t": "if", "e": "noneShown",
        "c": [{
            "t": "div",
            "a": {"style": "display:flex;align-items:center;"
                           "justify-content:space-between;gap:16px;"
                           "padding:26px;background:var(--st-note-bg);"
                           "border:1px dashed var(--st-rule-strong);"
                           "border-radius:11px"},
            "c": [{
                "t": "div",
                "a": {"style": "font:600 20px/1.3 var(--st-display);"
                               "letter-spacing:-0.02em;color:var(--st-ink)"},
                "c": [{"t": "#", "v": {"parts": [{"e": "noneShownLine"}]}}],
            }],
        }]},
        "the classes grid, filtered to nothing. Design's own empty-state "
        "panel (node 189) supplies the dashed border, the note ground and "
        "the 20px display line; the action button is dropped because there "
        "is nothing to do but change the filter that is already on screen."),

    # ── ⊕ MRB-287 E1 · THE LIST BEHIND "PREVIOUS YEARS" ────────────────
    #
    # ⛔ THE CONTROL WAS A DEAD END, AND THE HISTORY IS THE POINT. Design
    # drew the strip at the foot of the class grid as "VIEWING 2026–27 ·
    # Previous years" and gave the button a handler that pings
    # "2025–26 is read-only" — it names a year and offers no way to open it.
    # `LIVE_REGIONS["classes.html"]["year-switch"]` already records the
    # diagnosis: "Design drew HALF of it … but drew no LIST behind the
    # button. The list is what makes it a control."
    #
    # MRB-261 is the reason it matters: a teacher's past classes are not
    # clutter, they are the record, and until now the only way to reach one
    # was to already know its uuid.
    #
    # ⚠️ THE OPTIONS EXCLUDE THE YEAR ALREADY IN VIEW, AND THAT IS LOAD-
    # BEARING RATHER THAN TIDY. Included, the current year would have to
    # render as a disabled row with no handler — and `student-runtime.js`
    # looks a handler up THROUGH the miss recorder (`lookup(node.on, scope,
    # ctx.miss)`), so a looped button with no `on` writes `data-mrb-misses`
    # and fails `teacher_behaviour`'s own binding check. Node 84 names the
    # year in view; this list is the years you can go TO. Every option
    # rendered is therefore pressable, which is also what lets the drive
    # gate press one.
    #
    # ⚠️ NO READ-ONLY CHIP HERE. It would print the year a second time
    # eight pixels from node 84, which already says it. The statement rides
    # on `viewingYearLabel` instead — "Viewing 2025–26 · read-only" — one
    # binding, one sentence, and no literal year anywhere near it.
    83: (86, {
        "t": "if", "e": "yearsOpen",
        "c": [{
            "t": "span",
            "a": {"style": _YEAR_LIST},
            "c": [{
                "t": "for", "e": "yearOptions", "as": "y",
                "c": [{
                    "t": "button",
                    "a": {"type": "button",
                          "data-mrb-added": "year-open",
                          "style": _YEAR_OPTION},
                    "hov": "color:var(--st-ink)",
                    "on": "y.open",
                    "c": [{"t": "#", "v": {"parts": [{"e": "y.name"}]}}],
                }],
            }],
        }]},
        "the academic years a teacher can switch into, behind Design's own "
        "\"Previous years\" toggle. The treatment is node 86's exact style "
        "string in Design's action colour — see _YEAR_OPTION."),

    # ── ⊕ MRB-287 E1 · A PAST YEAR SAYS SO, ON THE CLASS PAGE ──────────
    #
    # ⛔ MRB-261: "a past year is read-only and must SAY so." It did not.
    # `is_past_year` has been computed in `teacher-data.js` since MRB-261 and
    # read by nothing — MRB-287's own report lists it under "Found and NOT
    # fixed, deliberately" — so the class page let a teacher open a class
    # that finished in July, compose a shoutout against it, and never told
    # them which year they were looking at.
    #
    # This is the half that TELLS them. The half that stops them is `WRAP`,
    # which takes the composer off the page entirely; the two ship together
    # on purpose, because a page that suppresses a control and does not say
    # why reads as broken rather than as read-only.
    #
    # ⊕ MRB-291, 26 Aug 2026 — `is_past_year` IS STILL DEAD, AND STAYS DEAD.
    # The paragraph above reads as an argument for wiring it up. It is not.
    # MRB-291 re-checked every reader and confirmed `teacher-data.js`'s
    # `is_past_year` (loadClassDetail) is consumed by nothing: the ported
    # pages take the YEARS-LIST path instead — `teacher-live.js` derives
    # `viewingIsPast` from `viewing.is_past` and exports `canWrite` /
    # `readOnlyLine` from it, and every ruling on this page reads THOSE. That
    # is the live path and the only one. Wiring the second computation in
    # would give one page two answers to "is this year history", which is the
    # exact shape of the drift MRB-267 removed from `workingAcademicYear`.
    # The note is recorded rather than the field deleted — `loadClassDetail`
    # is also called from hand-written teacher surfaces. See the matching
    # supersede note at the field in `shared/teacher-data.js`.
    #
    # ⚠️ APPENDED TO NODE 94 — Design's `<h1>` row, which already holds the
    # class code and the subject-dots pill and is `flex-wrap`ped for exactly
    # this. Not to node 92: that row is `justify-content:space-between` and
    # a third child there would push the header actions off their edge.
    94: (None, {
        "t": "if", "e": "readOnlyLine",
        "c": [{
            "t": "span",
            "a": {"style": _READONLY_CHIP},
            "c": [{
                "t": "span",
                "a": {"style": _READONLY_TEXT},
                "c": [{"t": "#", "v": {"parts": [{"e": "readOnlyLine"}]}}],
            }],
        }]},
        "the read-only statement on a past-year class, in Design's own "
        "header pill (node 96) at her own measurements. The year is a "
        "BINDING: `teacher_tells` fails the build on a typed academic year, "
        "and it is right to — Design's \"2025–26 is read-only\" was wrong "
        "from 1 September and wrong on day one for any school whose "
        "previous year is not 2025-26."),

    # ── ⊕ AMENDED ADDITION · the shoutout a teacher wrote, removable ────
    #
    # ⛔ ONLY ON A SHOUTOUT THIS TEACHER WROTE. The RLS UPDATE policy on
    # `class_shoutouts` is `author_id = auth.uid() AND
    # auth_user_teaches_class(class_id)`, so a control offered on anybody
    # else's shoutout would look pressable, be pressed, and be refused by the
    # database. `f.canDelete` compares the row's `author_id` — which
    # `buildFeed` in teacher-live.js already carries on every entry — against
    # `MRB_ME()`, the signed-in teacher's own id, which now travels through
    # the seam like everything else on this page.
    #
    # ⚠️ THE WORD IS "REMOVE", NOT "DELETE", and it is not a euphemism. The
    # write is a soft delete (`deleted_at`), and the read RPC
    # `class_shoutouts_for_viewer` filters `deleted_at IS NULL` — so the row
    # leaves the feed for EVERYONE, the author included. What a teacher sees
    # is a real removal, which is what the word says; "delete" would promise
    # something about the database that the database does not do.
    216: (219, {
        "t": "if", "e": "f.canDelete",
        "c": [{
            "t": "button",
            "a": {"type": "button",
                  "data-mrb-added": "shoutout-delete",
                  "aria-label": "Remove this shoutout",
                  "style": _DEL_TEXT_BTN},
            "hov": "color:var(--st-ink)",
            "on": "f.del",
            "c": [{"t": "#", "v": "Remove"}],
        }]},
        "the delete control on a shoutout the signed-in teacher wrote. "
        "Design drew no delete affordance anywhere in the feed; this is "
        "Mide's instruction of 24 Aug 2026, registered in "
        "AMENDED_ADDITIONS. The treatment is Design's own low-emphasis "
        "text button, copied verbatim off the \"Back to <class>\" control."),

    # ── ⊕ AMENDED ADDITION · the confirm step ──────────────────────────
    #
    # ⚑ THE CONFIRM IS THE CONTROL. A one-press delete on a card in a feed,
    # eight pixels from a child's name, is the shape of an accident — and the
    # thing being destroyed is a teacher's own sentence about a child, which
    # nothing on this platform can give back.
    #
    # ⚠️ IT SAYS WHAT REMOVAL ACTUALLY DOES. "It disappears from the feed for
    # everyone, including you" is the read RPC's own behaviour stated
    # plainly, and "This cannot be undone" is true: there is no UPDATE path
    # that clears `deleted_at` anywhere in this codebase.
    #
    # ⚠️ APPENDED TO THE CLASS SCREEN'S ROOT (node 88) AND NOT TO NODE 9,
    # where Design's own four overlays live. Node 9 is on all six pages;
    # node 88 is pruned everywhere but class-detail, which is the only page
    # with a feed. An inert overlay on five pages that can never open it is
    # markup a teacher can never reach, which is what LIVE_REGIONS just had
    # one of removed for.
    88: (None, {
        "t": "if", "e": "delOpen",
        "c": [{
            "t": "div", "a": {"style": _DEL_SCRIM}, "on": "cancelDelete",
            "c": [{
                "t": "div", "a": {"style": _DEL_PANEL}, "on": "stop",
                "c": [
                    {"t": "div", "a": {"style": _DEL_HEAD}, "c": [
                        {"t": "div", "c": [
                            {"t": "div", "a": {"style": _DEL_KICKER}, "c": [
                                {"t": "#", "v": {"parts": [
                                    {"e": "klass.code"}, " \u00b7 Shoutouts"]}}]},
                            {"t": "div", "a": {"style": _DEL_TITLE}, "c": [
                                {"t": "#", "v": "Remove this shoutout?"}]},
                        ]},
                        {"t": "button",
                         "a": {"type": "button",
                               "data-mrb-added": "shoutout-delete-close",
                               "aria-label": "Keep the shoutout",
                               "style": _DEL_CLOSE},
                         "on": "cancelDelete",
                         "c": [{"t": "svg",
                                "a": {"width": "12", "height": "12",
                                      "viewBox": "0 0 12 12", "fill": "none",
                                      "aria-hidden": "true"},
                                "c": [{"t": "path",
                                       "a": {"d": "M2.5 2.5l7 7M9.5 2.5l-7 7",
                                             "stroke": "currentColor",
                                             "stroke-width": "1.6",
                                             "stroke-linecap": "round"}}]}]},
                    ]},
                    {"t": "div", "a": {"style": _DEL_BODY}, "c": [
                        {"t": "div", "a": {"style": _DEL_PROSE}, "c": [
                            {"t": "#", "v": {"parts": [
                                "This removes the shoutout to ",
                                {"e": "delName"},
                                ". It disappears from the feed for everyone, "
                                "including you."]}}]},
                    ]},
                    {"t": "div", "a": {"style": _DEL_FOOT}, "c": [
                        {"t": "div", "a": {"style": _DEL_FOOT_NOTE}, "c": [
                            {"t": "#", "v": "This cannot be undone"}]},
                        {"t": "div",
                         "a": {"style": "display:flex;align-items:center;"
                                        "gap:12px"},
                         "c": [
                            {"t": "button",
                             "a": {"type": "button",
                                   "data-mrb-added": "shoutout-delete-cancel",
                                   "style": _DEL_TEXT_BTN},
                             "hov": "color:var(--st-ink)",
                             "on": "cancelDelete",
                             "c": [{"t": "#", "v": "Keep it"}]},
                            {"t": "button",
                             "a": {"type": "button",
                                   "data-mrb-added": "shoutout-delete-confirm",
                                   "style": _DEL_PRIMARY},
                             "hov": "background:var(--st-accent-hover)",
                             "on": "confirmDelete",
                             "c": [{"t": "#", "v": "Remove shoutout"}]},
                         ]},
                    ]},
                ]}]}]},
        "the confirm step in front of the shoutout delete. Design's bulk "
        "sheet (nodes 513-537) supplies the scrim, the panel, the header, "
        "the close X, the body pad, the footer bar and the primary button, "
        "at her own measurements. Registered in AMENDED_ADDITIONS."),
}


# ── ⊕ MRB-287 E1 · ONE OF DESIGN'S NODES, MADE CONDITIONAL ──────────────
#
# ⚑ THE MECHANISM THIS FILE WAS MISSING. `DEAD` deletes a node on every page,
# `INSERT_AT` adds one; neither can say "draw the thing Design drew, but only
# when the data says so". Every conditional the port needed until now happened
# to be inside a `renderVals` string, so this gap did not show. Two rulings in
# E1 need it and cannot be expressed any other way:
#
#   · a control the data cannot power must not ship — the year toggle on a
#     school with one academic year leads nowhere; and
#   · MRB-261's read-only rule, which is about ABSENCE. The retired page's
#     `applyWriteControls` (teacher-classes-2026-08-24-retired.html:648-657)
#     states the standard: the write controls are ABSENT, not present-and-
#     disabled, because "setting homework against a class that no longer runs
#     is not a mistake worth leaving available."
#
# The implementation is `build_student_port.py`'s, ported rather than
# reinvented: the node is REPLACED IN ITS PARENT by an `<if>` whose single
# child is the node itself, so its subtree, its index, its handlers and its
# bindings are all untouched. The wrapper carries no `i` — `student-runtime`
# renders an `<if>` as a branch and never as an element, so there is nothing
# to hang a `data-dc-tpl` on, and Design's numbering does not move.
#
# ⛔ EVERY EXPRESSION HERE MUST BE A `renderVals` KEY, AND THE BUILD CHECKS.
# `student-runtime.js:146` evaluates an `<if>` with `lookup(node.e, scope,
# null)` — WITHOUT the miss recorder — so a key that does not exist is not an
# error, it is silently FALSE. A typo here would take the shoutout composer
# off every class page with every gate green and nothing in the console.
# `build_teacher_port` asserts each name into the emitted logic for that
# reason; see the guard beside the wrap step.
#
# `{page: {node index: renderVals key}}`.
WRAP = {
    "classes.html": {
        # The year strip's separator and its toggle. A school in its first
        # year has no other year to reach, and Design's unconditional button
        # would answer "there are none" — which is a control that exists to
        # tell you it should not.
        85: "hasOtherYears",
        86: "hasOtherYears",
        # The two import routes. `roster-import` is one of only three write
        # paths on the whole teacher surface, and importing children into a
        # class that finished in July is not an action worth offering.
        # Node 40 is the header action; node 78 is the same route from an
        # empty class card (the one node 74's pruning deliberately spared).
        40: "canWrite",
        78: "canWrite",
    },
    "class-detail.html": {
        # The bulk sheet's opener and the composer card. Node 198 is the
        # WHOLE composer — its label (199), the recipient select (200), the
        # six template buttons (206/207), the textarea (209) and the footer
        # holding "Send shoutout" (212) are all inside it — so one wrap takes
        # the write surface off the page without touching Design's grid.
        #
        # ⚠️ NODE 213, THE FEED, STAYS. A past year is READ-only, not
        # invisible: what a teacher wrote about a child last year is exactly
        # the record MRB-261 exists to keep reachable.
        196: "canWrite",
        198: "canWrite",
    },
}


# ── ⊕ RULED, MRB-287 · what this port ADDED to Design's delivery ─────────
#
# ⚑ THE REGISTER THAT MAKES AN ADDITION VISIBLE. `student_behaviour.py` has
# an `AMENDED_ADDITIONS` of the same name and it does a different job — it
# tolerates text the port renders that Design's own file does not, for a gate
# that diffs the two. `teacher_behaviour.py` diffs nothing against Design's
# file, so a copy of that mechanism here would be a register with no gate
# behind it.
#
# What this one does instead: it NAMES every control this port put on a
# teacher's screen that Design did not draw, says which page it is on and
# which of her nodes it hangs off, and `build_teacher_port.build()` asserts
# each marker is in the EMITTED bytes of that page and in no other. So the
# register cannot drift from the pages, and an addition cannot be made
# without appearing here.
#
# ⚠️ THE MARKERS ARE ALSO WHAT `teacher_behaviour.py` SWEEPS. Inserted
# markup carries no `i`, so it carries no `data-dc-tpl`, so the drive gate
# could not see it. Both facts are one attribute now.
#
# ⚠️ `needs_data` IS NOT A GET-OUT, IT IS THE SHAPE OF THE CONTROL. All four
# of these live on the shoutout feed, and the EMPTY class-detail fixture is a
# class with no roster and therefore no shoutouts — `FEED[cid]` is `[]`. There
# is nothing to remove, so there is correctly nothing to press, and a gate
# demanding the control on that fixture would be demanding a delete button on
# an empty feed. `teacher_behaviour` skips them there and says so; on the
# POPULATED fixture every one of them is pressed by name and must move
# something. ⛔ A future addition that is pure chrome must NOT carry this flag
# — chrome is on screen in every state, and claiming otherwise would excuse it
# from the only gate that presses it.
AMENDED_ADDITIONS = (
    # ⊕ MRB-287 E1 — the academic year a teacher is switching TO.
    #
    # ⚠️ `needs_data` IS DELIBERATELY NOT SET, per the warning above. This is
    # CHROME: the year strip is on screen in every state the classes page can
    # be in, including the one with no classes at all — which is precisely the
    # state it matters most in, because a teacher whose classes are ALL last
    # year's arrives at an empty grid and this is their only way out of it.
    #
    # ⚠️ `opener_tpl` IS DESIGN'S NODE, NOT AN ADDITION, AND THE GATE NEEDED
    # TEACHING THAT. `teacher_behaviour`'s reveal loop presses earlier
    # ADDITIONS to uncover a later one; this is the first addition on its page
    # and the thing that opens it is node 86, one of Design's own. Without the
    # opener the marker is reported unreachable — correctly, because it would
    # be, to that gate.
    dict(marker="year-open", page="classes.html", node=83, opener_tpl=86,
         label="<the year's name>",
         # ⚠️ WHERE IT GOES, NOT JUST THAT IT MOVES. A control whose entire
         # job is to navigate proves nothing by re-rendering, and `MRB_GO`
         # DROPS an empty parameter — so a year link that computed no id
         # would navigate to the working year and be indistinguishable from
         # one that works. `teacher_behaviour` compares the recorded nav.
         expect_nav=dict(screen="classes", param="year"),
         why="the list behind Design's \"Previous years\" toggle. Design "
             "drew the toggle and no list, so `pastYears` could only toast a "
             "hardcoded \"2025–26 is read-only\" — a control that names a "
             "year and cannot open it. MRB-261 is explicit that the history "
             "stays reachable; this is what makes the strip a control "
             "instead of a caption."),
    dict(marker="shoutout-delete", page="class-detail.html", node=216,
         label="Remove", needs_data=True,
         why="Mide, 24 Aug 2026: \"A teacher who can post a shoutout can "
             "remove one.\" Design's feed card has no delete affordance. "
             "Shown only where `f.canDelete` — the row's `author_id` is the "
             "signed-in teacher's — because the RLS UPDATE policy is "
             "author-only and a control that fails RLS is a control that "
             "lied."),
    dict(marker="shoutout-delete-close", page="class-detail.html", node=88,
         label="Keep the shoutout", needs_data=True,
         why="the confirm sheet's close X, off Design's node 520."),
    dict(marker="shoutout-delete-cancel", page="class-detail.html", node=88,
         label="Keep it", needs_data=True,
         why="the confirm sheet's decline. The wording is the SAFE choice "
             "stated as an action, so the two footer buttons read as a "
             "choice rather than as one button and an escape hatch."),
    dict(marker="shoutout-delete-confirm", page="class-detail.html", node=88,
         label="Remove shoutout", needs_data=True,
         why="the press that actually writes. `confirmDelete` calls "
             "`MRB_DELETE_SHOUTOUT`, which is "
             "`MrBadmusTeacherData.softDeleteClassShoutout` — the function "
             "that has existed since MRB-46 — and then re-reads the feed "
             "through `MRB_REFRESH_FEED`. On failure it writes "
             "`#compose-error` and toasts, which is the composer's own "
             "failure idiom and not a second one."),
)


# ── class fields that are pure invention ─────────────────────────────────
#
# Deleted by BALANCED-LITERAL SCAN, never by regex: `NAMES` holds apostrophes,
# `TITLES` holds em dashes and nested braces, and a scan that stopped at the
# first `;` would truncate a list in the middle of a string and produce a
# syntax error four hundred lines later.
#
# `rnd` is here and `seed` IS NOT — see `SEED_GUARD` at the foot of this file.
DROP_FIELDS = (
    ("NAMES", "fifty-four invented children. The roster supplies real names."),
    ("LASTS", "eleven invented \"last seen\" strings. The roster supplies "
              "`last`, computed from the newest real submission stamp."),
    ("HOURS", "the numeric twin of LASTS. The roster supplies `hours`, "
              "measured between two real timestamps."),
    ("TITLES", "thirty-six invented assignment titles, three subjects deep. "
               "Real titles come from `scheme_of_work_entries`."),
    ("STEMS", "eight invented question stems, held as a CLASS field — the "
              "same eight for every paper in every subject. A paper's "
              "questions belong to the paper: they arrive on "
              "`GRID[key].stems`, and their LENGTH is the real question "
              "count, which Design also has no way to vary."),
    ("TOPICS", "five invented topics. Only the Set-work sheet read them, and "
               "it is pruned; `teacher-live.js` returns `TOPICS: []` and "
               "says why."),
    ("POOL_CLASSES", "five class ids the search overlay drew its results "
                     "from — three students each, fifteen names, so a "
                     "teacher typing a real child's surname found nothing."),
    ("BANDS", "the five score bands. Only `chartFor`'s spread chart reads "
              "them and it still does; they are NOT deleted — this row is "
              "here to record that they were CHECKED and kept, because they "
              "are a scale and not a sample. See below: the tuple is "
              "consulted, not this sentence."),
    ("rnd", "THE HASH THAT INVENTS EVERY NUMBER ON THE PAGE. Every mark, "
            "percentage, submission count and chart column in Design's "
            "delivery comes out of this function."),
)
# BANDS is kept. Recorded above so the decision is written down, removed here
# so the build does not act on it — a comment that contradicts the code is
# worse than no comment.
DROP_FIELDS = tuple(r for r in DROP_FIELDS if r[0] != "BANDS")


# ── `renderVals` keys that go with the Set-work sheet ────────────────────
#
# `renderVals` is Design's DERIVATION and stays verbatim — except for the
# fifteen keys that exist only to drive a sheet that is no longer on the page.
# They are not harmless: `topics` and `swSummary` read `this.TOPICS`, which is
# deleted, so leaving them would throw at mount on all seven pages rather than
# merely computing something nobody looks at.
# ⚠️ `sw1` IS NOT HERE, AND THE BUILD STOPPING IS WHAT FOUND IT. `sw1`, `sw2`
# and `sw3` share one physical line, and `LOGIC` deletes that line whole
# (`DROP_KEYS` works one balanced key at a time and cannot take the other
# two). Listing `sw1` here as well asked for a key that was already gone.
# ⊕ `sampleCsv` IS ON THIS LIST TOO, AND IT IS NOT A SET-WORK KEY. It is
# `() => this.ping('Template CSV downloaded')` — a toast that states a fact
# about the teacher's own computer, in front of nothing. No file is built, no
# Blob, no anchor, no download; the browser's downloads list stays empty and
# the teacher goes looking for a file that was never written.
#
# It is DROPPED rather than implemented, and the reason is `IMPORT_NOT_PORTED`
# above: the only node that carried it is Design's node 364, on the import
# screen, and that screen is no longer emitted. Implementing a download for a
# button nobody can press would be dead code that reads as a feature; leaving
# the toast would be a lie nobody can hear. The hand-written wizard has never
# offered a template CSV and still does not — that is a real gap, it is in the
# report, and it belongs to whoever next opens `teacher/import.html`.
DROP_KEYS = (
    "setWorkOpen", "swEyebrow", "topics", "swCounts", "swDays",
    "swRelease", "swClassList", "swSummary", "swBackLabel", "swNextLabel",
    "swBack", "swNext", "openSetWork",
    "sampleCsv",
)


# ── whole method bodies, replaced ────────────────────────────────────────
#
# ⚠️ `chartFor` IS **NOT** ON THIS LIST, AND THE FIRST DRAFT PUT IT HERE. It
# looked like the same shape as `matrixFor` — four hundred lines of numbers —
# and it is not: it is four hundred lines of DERIVATION over `matrixFor`,
# `rosterFor`, `papersFor` and `gridFor`, all four of which are seamed below.
# Replace it with a lookup and the insights screen needs a `CHARTS` key that
# `teacher-live.js` does not export and should not: the charts are computed
# FROM the primitives, on the page, exactly as Design wrote them. What it
# needs instead is the five crash guards and the four `STEMS` reads, which are
# in `LOGIC`.
METHODS = {
    "matrixFor": (
        "    if (!k || !k.id) return MRB_EMPTY_MATRIX();\n"
        "    return MRB_PICK('MATRIX', k.id);",
        "ONE score matrix per class — Design's README calls it the single "
        "source every average on every screen derives from, and Design's is "
        "seeded from an FNV hash of the class id. The seam keeps the shape "
        "and fills it from real submissions, and ADDS what Design's could not "
        "carry: `pct[]` and `max[]` per cell (real papers are not out of 8), "
        "`stampShort[]` (when the work actually arrived) and `markedIdx` "
        "(which columns are closed, because real classes do not have exactly "
        "one open paper at index 0)."),
    "rosterFor": (
        "    if (!k || !k.id) return [];\n"
        "    return MRB_PICK('ROSTER', k.id);",
        "the class roster."),
    "papersFor": (
        "    if (!k || !k.id) return [];\n"
        "    return MRB_PICK('PAPERS', k.id);",
        "the term's assignments, newest first, already carrying `sub`, "
        "`mean`, `due`, `range` and `when` in Design's own shape."),
    "weeks": (
        "    const k = this.klass();\n"
        "    return (k && k.id) ? MRB_PICK('WEEKS', k.id) : [];",
        "⚠️ PER CLASS, WHICH DESIGN'S IS NOT. Design derives twelve weeks "
        "from `new Date(2026, 7, 26)` — one hardcoded term start for every "
        "school in the country. A class's weeks are its OWN assignments' "
        "weeks, so there is one list per class and a class with no work set "
        "has no week bar at all, which is Design's own documented rule and is "
        "now a consequence of the data rather than a special case."),
    "gridFor": (
        "    if (!k || !k.id) return null;\n"
        "    var g = MRB_PICK('GRID', k.id + ':' + pIdx);\n"
        "    return g || null;",
        "the per-paper question grid, from what each student actually "
        "answered rather than from a hash of their total. ⚠️ IT CAN BE NULL, "
        "DELIBERATELY: `teacher-live.js` prefetches only the grids a screen "
        "will draw, and a key that is present and null means NOT FETCHED "
        "YET. Design's `renderVals` already writes `pGrid ? … : []` "
        "everywhere it reads it, so a null renders an empty grid rather than "
        "a grid of zeros — which is the one thing it must never be."),
    "klass": (
        "    const found = this.klassById(this.state.classId);\n"
        "    if (found) return found;\n"
        "    if (this.state.classId) {\n"
        "      throw new Error('teacher page: class \"' + this.state.classId "
        "+ '\" is not one of this teacher\\'s classes');\n"
        "    }\n"
        "    return this.CLASSES[0] || MRB_NO_CLASS();",
        "⊕ DEVIATION FROM THE BRIEF, AND IT IS DELIBERATE. The brief lists "
        "`klass` among the methods that stay verbatim. Verbatim it reads "
        "`this.klassById(this.state.classId) || this.CLASSES[3]` — a class id "
        "that does not resolve falls back to THE FOURTH CLASS IN THE LIST. In "
        "a prototype where every class is fictional that is a harmless "
        "default; on `class-detail.html?class=<uuid>` it is one teacher's "
        "class shown under another teacher's URL, silently. That is the exact "
        "failure `MRB_DATA` throws to prevent, one level up.\n"
        "\n"
        "        The empty case is NOT a throw, and that was checked rather "
        "than assumed: `renderVals` calls `this.klass()` unconditionally on "
        "every screen, and a teacher with no classes at all reaches it. "
        "Set-but-missing throws; absent returns null.\n"
        "\n"
        "        ⚠️ AND A NULL CLASS HAS TO SURVIVE THE WHOLE OF `renderVals`, "
        "which calls `rosterFor`, `papersFor`, `matrixFor` and `weeks` "
        "unconditionally on every screen. Each therefore opens with a null "
        "guard — an empty roster, no papers, no weeks and an empty matrix — "
        "because a teacher with no classes at all is a real first day and "
        "not an error. Found by the empty fixture crashing on "
        "`MRB_PICK('ROSTER', k.id)`, which is the empty fixture doing its "
        "job."),
    "paper": (
        "    const list = this.papersFor(this.klass());\n"
        "    const i = this.state.paperIdx;\n"
        "    if (i == null || i === '') {\n"
        "      const n = window.MrBadmusTeacherLive\n"
        "        ? window.MrBadmusTeacherLive.newestMarkedIdx(list) : -1;\n"
        "      return n >= 0 ? list[n] : (list[0] || null);\n"
        "    }\n"
        "    if (!list[Number(i)]) {\n"
        "      throw new Error('teacher page: assignment ' + i + ' is not in "
        "this class');\n"
        "    }\n"
        "    return list[Number(i)];",
        "⊕ TWO DEVIATIONS, AND BOTH ARE THE SAME DEFECT. (1) Design keys on "
        "`state.paperId`; `teacher-live.js` takes `?paper=` as an INDEX, "
        "because a paper's identity to this page is its position in the "
        "class's own list. (2) Design falls back to `list[1] || list[0]` — "
        "THE SECOND PAPER OF THE TERM — which is index 1 only when there is "
        "exactly one open paper, a property of the sample. Real classes have "
        "none open, or three. Unasked-for now means the newest MARKED paper, "
        "via the seam's own `newestMarkedIdx`, so the page and the data layer "
        "cannot disagree about which one that is; asked-for and missing "
        "throws, rather than marking up a different paper under the "
        "requested one's URL."),
    "student": (
        "    const rows = this.rosterFor(this.klass());\n"
        "    const found = rows.filter(r => r.id === this.state.studentId)"
        "[0];\n"
        "    if (found) return found;\n"
        "    if (this.state.studentId) {\n"
        "      throw new Error('teacher page: student \"' + "
        "this.state.studentId + '\" is not on this class\\'s roster');\n"
        "    }\n"
        "    return null;",
        "the same deviation, and the sharpest of the three. Verbatim it falls "
        "back to `rows[0]` — THE FIRST CHILD ON THE ROSTER — so a student id "
        "that does not resolve shows one child's marks, attendance and "
        "history under another child's URL. A page that is confidently wrong "
        "about a child is worse than a page that is plainly broken."),
    "rosterFor_noop": ("", ""),
    "cellStyle": (
        "    if (v === 1) return { w: 9, h: 9, r: '50%', bg: 'var(--ks3-ok)',"
        " bd: 'none' };\n"
        "    if (v === 0) return { w: 9, h: 9, r: '50%', bg: 'transparent', "
        "bd: '1.5px solid var(--st-rule-strong)' };\n"
        "    if (v === 3) return { w: 9, h: 9, r: '2px', bg: "
        "'var(--st-hatch-b)', bd: '1.5px solid var(--st-hatch-b)' };\n"
        "    return { w: 9, h: 2, r: '1px', bg: 'var(--st-rule-strong)', bd: "
        "'none' };",
        "⊕ THE FOURTH GRID STATE. Design's grid has three: 1 correct, 0 "
        "incorrect, 2 not attempted — and its final `return` catches "
        "EVERYTHING ELSE, so the new 3 currently draws as the DASH, which "
        "says \"not attempted\" about a child who answered. That is precisely "
        "the misreading the state was added to prevent.\n"
        "\n"
        "        3 is `is_correct IS NULL`: answered, and self-marked or "
        "written, so the platform records no correctness claim. The column's "
        "NOT NULL was dropped on 20 Aug 2026 so that an honest row could "
        "exist.\n"
        "\n"
        "        ⚠️ IT MUST READ AS NONE OF THE OTHER THREE, and all three "
        "wrong answers were available: a RING is Design's incorrect, a DOT is "
        "Design's correct, a DASH is Design's not-attempted. So it is a "
        "filled SQUARE — the same 9x9 footprint as the two circles so the "
        "grid keeps its rhythm, 2px corners rather than 50% so it differs in "
        "SHAPE and not only in colour, and `--st-hatch-b` rather than green "
        "or the rule ink so it reads as present-but-neutral. Distinguishable "
        "without colour, which the ring/dot pair already is not."),
}
del METHODS["rosterFor_noop"]


# ── the rest, as guarded exactly-once source replacements ────────────────
#
# `(from, to, why)`. Applied with `str.replace(from, to, 1)` and the build
# REFUSES if `from` does not occur EXACTLY ONCE. Not zero — a ruling that
# matched nothing is invisible. Not twice — a ruling that matched twice was
# aimed at one of them.
#
# ⚑ HALF OF THESE ARE ONE DEFECT WITH SIX ADDRESSES. Design's sample has
# properties real data does not, and its derivation reads those properties as
# facts:
#
#     every paper is out of 8              → every `/ 8` and every `'/8'`
#     exactly one paper is open, at 0      → every `.slice(1)`, `[1]`,
#                                            `length - 1`
#     every answer is marked right or wrong→ `qpct[i]` is never null
#     every submission's lateness is known → `!late[p]` means on time
#     the roster is the denominator        → `colSub[i] + '/' + k.n`
#
# None of them is a bug in Design's file, where all five are true. Every one
# of them is a wrong number on a real dashboard.
LOGIC = (
    # ══ the state initialiser ═══════════════════════════════════════════
    #
    # `screen` is per-page and written by the build; `MRB_SCREEN` is the token
    # it substitutes.
    #
    # ⚠️ `paperId` BECOMES `paperIdx`, AND THAT IS NOT A RENAME. Design keys a
    # paper by a made-up string id (`'8rsc1:p1'`); `teacher-live.js` takes
    # `?paper=` as an INDEX into the class's own paper list, because that is
    # what identifies a paper to this page. Left as an id, `paper()` would
    # match nothing on every real class.
    #
    # ⚠️ `digestScope` AND `chartScope` COME OFF THE URL, WHICH THE BRIEF SAID
    # TO LEAVE ALONE. They were UI state in a prototype where the digest was a
    # screen you switched to; they are URL state now, because
    # `digest.html?class=<id>` IS the class report and has to survive a reload,
    # a bookmark and a Back. Reading them off the query is the only place that
    # knowledge exists once the pages are separate. Deviation, stated.
    #
    # `boTpl` reads the FIRST TEMPLATE'S KEY rather than Design's `3`. The six
    # templates are the DB enum now (`class_shoutouts_template_key_chk`) and
    # their ids are strings; `3` matches nothing, so Design's composer would
    # open with no template selected and no way to tell that from a bug.
    ("""  state = {
    screen: 'classes', classId: '8rsc1', studentId: '8rsc1-3', paperId: '8rsc1:p1', weekIdx: 0,
    ks: 'All', sort: 'code', modal: null, toast: '',
    swStep: 1, swTopic: 't1', swQ: 10, swDay: 'Wed', swRel: 'now', swClasses: ['8rsc1'],
    boSel: [], boTpl: 3, note: '', search: '', importStep: 1, digestScope: 'all', recipient: '',
    chartKind: 'submissions', chartScope: 'all', insFrom: 'classes'
  };""",
     """  state = {
    screen: 'MRB_SCREEN',
    classId: MRB_DATA('classId'), studentId: MRB_DATA('studentId'),
    paperIdx: MRB_DATA('paperIdx'), weekIdx: 0,
    ks: 'All', sort: 'code', modal: null, toast: '',
    boSel: [], boTpl: MRB_FIRST_TEMPLATE(), note: '', search: '',
    importStep: 1, digestScope: MRB_Q('class') ? 'class' : 'all', recipient: '',
    chartKind: 'submissions', chartScope: MRB_Q('class') || 'all',
    yearsOpen: false
  };""",
     "the state initialiser. See the block comment above."),

    # ══ the class list, the templates, the teacher ══════════════════════
    ("""  CLASSES = [
    { id: '7hsc5', code: '7h/Sc5', year: 7, ks: 'KS3', subject: 'Science', n: 28, week: [24, 28], last: '18 min ago', state: 'live' },
    { id: '7rsc3', code: '7r/Sc3', year: 7, ks: 'KS3', subject: 'Science', n: 30, week: [27, 30], last: '42 min ago', state: 'live' },
    { id: '8hsc2', code: '8h/Sc2', year: 8, ks: 'KS3', subject: 'Science', n: 29, week: [11, 29], last: '3 hours ago', state: 'live' },
    { id: '8rsc1', code: '8r/Sc1', year: 8, ks: 'KS3', subject: 'Science', n: 16, week: [11, 16], last: '9 min ago', state: 'live' },
    { id: '8rsc4', code: '8r/Sc4', year: 8, ks: 'KS3', subject: 'Science', n: 0, week: [0, 0], last: 'No activity yet', state: 'empty' },
    { id: '9hsc5', code: '9h/Sc5', year: 9, ks: 'KS3', subject: 'Science', n: 31, week: [19, 31], last: '1 hour ago', state: 'live' },
    { id: '9rsc5', code: '9r/Sc5', year: 9, ks: 'KS3', subject: 'Science', n: 0, week: [0, 0], last: 'No activity yet', state: 'empty' },
    { id: '10hph1', code: '10h/Ph1', year: 10, ks: 'KS4', subject: 'Physics', n: 24, week: [22, 24], last: '26 min ago', state: 'live' },
    { id: '10hsc2', code: '10h/Sc2', year: 10, ks: 'KS4', subject: 'Combined Science', n: 27, week: [9, 27], last: '5 hours ago', state: 'live' },
    { id: '11hph1', code: '11h/Ph1', year: 11, ks: 'KS4', subject: 'Physics', n: 17, week: [17, 17], last: '34 min ago', state: 'live' },
    { id: '11hsc5', code: '11h/Sc5', year: 11, ks: 'KS4', subject: 'Combined Science', n: 25, week: [0, 25], last: '2 days ago', state: 'nowork' },
    { id: '11rsc1', code: '11r/Sc1', year: 11, ks: 'KS4', subject: 'Combined Science', n: 0, week: [0, 0], last: 'No activity yet', state: 'empty' }
  ];""",
     "  CLASSES = MRB_DATA('CLASSES');",
     "twelve invented classes. ⚠️ THEY LOOK REAL, which is why this is worth "
     "a note: `7h/Sc5`, `10h/Ph1` and `11r/Sc1` are correctly-formed MRB-263 "
     "class codes and three of them are codes the school actually uses. "
     "Design did the naming convention properly and the numbers behind them "
     "are still fiction."),

    ("""  TEMPLATES = [
    { id: 1, label: 'Top of the class this week' },
    { id: 2, label: 'Brilliant improvement' },
    { id: 3, label: 'Every assignment on time' },
    { id: 4, label: 'Smashed a tough topic' },
    { id: 5, label: 'Bounced back strong' },
    { id: 6, label: 'Helped a classmate' }
  ];""",
     "  TEMPLATES = MRB_DATA('TEMPLATES');",
     "the shoutout templates. Design copied the six LABELS accurately and "
     "invented numeric ids; the id is what an insert stores, and it is the "
     "DB enum key. `teacher-live.js` maps the locked list in shoutouts.js — "
     "which mirrors `class_shoutouts_template_key_chk` — into Design's shape."),

    ("    const teacher = this.props.teacherName ?? 'Ayomide';",
     "    const teacher = MRB_DATA('teacherName');",
     "the name in the top bar and in `classLine`. `props` is `{}` on every "
     "ported page — the mount emits it empty — so the `??` fallback was not a "
     "default, it was the value, and every teacher was greeted as Ayomide."),

    # ══ THE ACADEMIC YEAR, WELDED INTO TWO COMPUTED STRINGS ═════════════
    #
    # Not a text node, so no binding reaches it: `2026–27` is concatenated
    # inside `renderVals` and would have gone on reading 2026–27 in 2028.
    #
    # ⊕ CORRECTED, MRB-287 E1 — AND THE FIRST FIX WAS THE WRONG ONE.
    # This ruling used to read `MRB_DATA('yearLabel')`, which is the WORKING
    # year: right while the working year is the only one you can see, and
    # wrong the moment a past year opens — twelve cards from 2025-26 each
    # confidently stating 2026-27. Binding a literal to the nearest key is not
    # the same as binding it to the RIGHT key, and this is what that looks
    # like when it ships.
    #
    # The card states ITS OWN year, off the class's `academic_year_name`,
    # which `teacher-data.js:610` has always returned and `teacher-live.js`
    # was dropping. The retired hand-written page did this correctly and
    # recorded why (teacher-classes-2026-08-24-retired.html:497-506): "The
    # academic year is on EVERY card regardless of which year is selected, so
    # 10H/Ph1 and 11h/Ph1 — the same 17 students a year apart — can never read
    # as a duplicate again."
    #
    # ⚠️ EMPTY PARTS ARE DROPPED, NOT PRINTED. `year_group` is nullable and
    # `academic_year_name` can be null on a year nobody named; the retired
    # page's `buildMetaLine` filtered for exactly that reason. Blanks over
    # invented values — "Year null · KS3 · undefined" is worse than "KS3".
    ("      meta: 'Year ' + c.year + ' · ' + c.ks + ' · 2026–27',",
     "      meta: [c.year == null ? '' : 'Year ' + c.year, c.ks, c.yearName]\n"
     "        .filter(Boolean).join(' · '),",
     "the class card's meta line — the card's OWN academic year, not the "
     "dashboard's. See the block comment: the first port bound this to the "
     "working year, which is a different question."),

    # ══ THE ROSTER ROW: /8, AND \"on time\" FOR AN UNKNOWN ══════════════
    #
    # THREE defects in five lines, and all three show a teacher a number that
    # is not true of the child in front of them:
    #
    #   · `sc / 8` — real papers are out of `max[]`, and the matrix already
    #     carries `pct[]` so nothing downstream has to divide by anything.
    #   · `late ? 'late' : 'on time'` — `late[p]` is TRI-STATE now (true /
    #     false / null, where null is "no stamp and no deadline, genuinely
    #     unknown"). Rendering the unknown as "on time" is the same lie as
    #     rendering `is_correct IS NULL` as wrong, and it is forbidden for the
    #     same reason. Pre-22-Aug-2026 rows have no `is_late` at all, so this
    #     is not a rare path.
    #   · `'1/1 on time'` — the OPEN week's label, over `r.inWeek`, which
    #     means SUBMITTED and says nothing about lateness. The words claimed a
    #     punctuality the number never measured.
    ("""      const scPct = sc == null ? 0 : Math.round((sc / 8) * 100);
      return {
        name: r.name,
        initials: this.initials(r.name),
        hue: this.hueFor(r.name),
        hasWork: kPapers.length > 0,
        pct: wPast ? scPct : (r.inWeek ? 100 : 0),
        weekLabel: kPapers.length === 0 ? 'No work set'
          : (wPast
            ? (sc == null ? 'Not submitted' : scPct + '% · ' + (late ? 'late' : 'on time'))
            : (r.inWeek ? '1/1 on time' : '0/1 in')),""",
     """      const scPct = mrow && mrow.pct[wi] != null ? mrow.pct[wi] : null;
      const lateState = mrow ? mrow.late[wi] : null;
      return {
        id: r.id,
        name: r.name,
        initials: this.initials(r.name),
        hue: this.hueFor(r.name),
        hasWork: kPapers.length > 0,
        pct: wPast ? (scPct == null ? 0 : scPct) : (r.inWeek ? 100 : 0),
        weekLabel: kPapers.length === 0 ? 'No work set'
          : (wPast
            ? (scPct == null ? 'Not submitted'
              : scPct + '% · ' + (lateState === true ? 'late'
                : (lateState === false ? 'on time' : 'timing unknown')))
            : (r.inWeek ? 'Submitted' : 'Not in')),""",
     "the roster row. See the block comment: three defects, five lines. "
     "⊕ AND `id`, ADDED 24 Aug 2026: the shoutout composer's `<select>` is "
     "built from this list, and its option values have to be the child's real "
     "id rather than their name — `insertClassShoutout` writes "
     "`recipient_id`, RLS checks the recipient is a member of this class, and "
     "two children in one class can share a name. See `BIND_ATTR` 203."),

    # ══ THE QUESTION LIST: STEMS WAS A CLASS FIELD, AND qpct CAN BE NULL ═
    #
    # `STEMS` held eight stems for every paper in every subject. A paper's
    # questions belong to the paper, and their COUNT is the paper's too —
    # `pGrid.stems.length` is the real number of questions, which Design has
    # no way to vary at all.
    #
    # `qpct[i]` is null where NOTHING at that question was machine-marked
    # (every answer written or self-marked). `null + '%'` renders the string
    # `"null%"`, and `null < 50` is TRUE, so an unmarked question would also
    # have been painted as the worst one on the paper.
    ("    const questions = pGrid ? this.STEMS.map((q, qi) => ({ id: q.id, "
     "text: q.text, pct: pGrid.qpct[qi] })) : [];\n"
     "    const worst = questions.length ? questions.reduce((a, q) => "
     "(q.pct < a.pct ? q : a), questions[0]) : null;",
     "    const questions = pGrid ? pGrid.stems.map((q, qi) => ({ id: q.id, "
     "text: q.text, pct: pGrid.qpct[qi] })) : [];\n"
     "    const scored = questions.filter(q => q.pct != null);\n"
     "    const worst = scored.length ? scored.reduce((a, q) => "
     "(q.pct < a.pct ? q : a), scored[0]) : null;",
     "the marking screen's question list."),

    # ══ THE GRID'S TEN-ROW CAP ══════════════════════════════════════════
    ("    const grid = pGrid ? pGrid.rows.slice(0, 10).map(r => ({",
     "    const grid = pGrid ? pGrid.rows.map(r => ({",
     "Design shows the first TEN students of a class and no more, with no "
     "\"and 21 others\" and nothing to press. On a 31-student class that is "
     "two thirds of the children hidden on the screen a teacher opens to find "
     "the ones who are struggling. The cap is Design's sample being 16 "
     "students deep; the grid scrolls."),

    # ══ THE PAPER TILES: '8 questions, 1 mark each' AND A null% LABEL ═══
    ("          { label: 'Class mean', value: pp.mean, sub: '8 questions, "
     "1 mark each' },",
     "          { label: 'Class mean', value: pp.mean, sub: pGrid ? "
     "pGrid.qLine : '' },",
     "Design's paper is eight questions worth one mark each. A real one is "
     "whatever it is, and `teacher-live.js` builds the sentence from the "
     "paper's own question count and max score — blank where it does not know "
     "rather than a guess."),

    ("        questions: questions.map(qq => ({\n"
     "          id: qq.id, text: qq.text, pct: qq.pct, label: qq.pct + '%',\n"
     "          worst: worst && qq.id === worst.id,\n"
     "          fill: qq.pct < 50 ? 'var(--st-accent)' : (qq.pct < 70 ? "
     "'var(--st-hatch-b)' : 'var(--ks3-ok)')\n"
     "        })),",
     "        questions: questions.map(qq => ({\n"
     "          id: qq.id, text: qq.text, pct: qq.pct == null ? 0 : qq.pct,\n"
     "          label: qq.pct == null ? 'Not marked' : qq.pct + '%',\n"
     "          worst: !!(worst && qq.pct != null && qq.id === worst.id),\n"
     "          fill: qq.pct == null ? 'var(--st-rule-soft)'\n"
     "            : (qq.pct < 50 ? 'var(--st-accent)' : (qq.pct < 70 ? "
     "'var(--st-hatch-b)' : 'var(--ks3-ok)'))\n"
     "        })),",
     "the per-question bars. `null + '%'` is the string `\"null%\"` and "
     "`null < 50` is true, so an unmarked question rendered as \"null%\" in "
     "the accent colour reserved for the WORST question on the paper. The bar "
     "goes to zero width and the label says why."),

    # ══ THE STUDENT'S HISTORY: /8, AND A FABRICATED SUBMISSION DATE ═════
    #
    # ⚑ `submitted` IS THE WORST LINE IN DESIGN'S FILE, and it is easy to
    # read past. It renders `p.dueShort` when the work was on time and
    # `p.lateShort` when it was late — the DEADLINE and the END OF THE WEEK.
    # Neither is when anybody submitted anything. A teacher reading a column
    # headed "Submitted" is being shown a date the child had nothing to do
    # with, and on a parents' evening it would be quoted.
    #
    # The matrix carries `stampShort[]`, which is `completed_at` or
    # `submitted_at` formatted — the real thing, blank where there is none.
    ("""      const pct = sc == null ? null : Math.round((sc / 8) * 100);
      const tone = open ? 'neutral' : (sc == null || late ? 'warn' : 'ok');
      return {
        marked: !open && sc != null,
        missing: !open && sc == null,
        late: late,
        pct: open ? null : pct,
        title: p.title,
        due: p.due.replace('Due ', ''),
        submitted: open ? (sc != null ? st.last : 'Not yet') : (sc == null ? '—' : (late ? p.lateShort : p.dueShort)),
        score: open || sc == null ? '—' : sc + '/8 · ' + pct + '%',""",
     """      const pct = stRow ? stRow.pct[i] : null;
      const stampS = stRow ? stRow.stampShort[i] : null;
      const tone = open ? 'neutral' : (sc == null || late ? 'warn' : 'ok');
      return {
        marked: !open && sc != null,
        missing: !open && sc == null,
        late: late,
        pct: open ? null : pct,
        title: p.title,
        due: p.due.replace('Due ', ''),
        submitted: open ? (sc != null ? st.last : 'Not yet') : (stampS || '—'),
        score: open || sc == null || stRow.max[i] == null ? '—'
          : sc + '/' + stRow.max[i] + (pct == null ? '' : ' · ' + pct + '%'),""",
     "the student's assignment history. `/ 8` twice and a fabricated date; "
     "see the block comment above."),

    ("      const late = !open && sc != null && stRow.late[i];",
     "      const late = !open && sc != null && stRow.late[i] === true;",
     "`late[]` is tri-state. `null` is unknown, and `sc != null && null` is "
     "`null`, which is falsy — so an unknown already rendered as \"On time\" "
     "in the status column. Pinned to an explicit `=== true` so the only "
     "thing that reads as late is a stamped late."),

    # ══ THE CLASS TILES: THE ROSTER AS A DENOMINATOR, AND THREE CAPTIONS ═
    #
    # ⚑ `k.n` IS NOT WHO WAS ASKED. Departed students are counted in a
    # column's aggregates — MRB-38's locked rule: an assignment's mean must
    # not move because a pupil left in February — so `colSub[i]` can exceed
    # the CURRENT roster and `colSub + '/' + k.n` renders "31/29". The matrix
    # carries `colAsked[]` for exactly this.
    #
    # `wLate = colSub - colOnTime` overstates late for the same reason the
    # roster row did: the unknowns fall into the subtraction. `colLate[]` is
    # the real count and `colLateUnknown[]` is the gap, which is SHOWN rather
    # than hidden — a hidden unknown is a number a teacher reads as a zero.
    #
    # And three captions say more than their figure knows:
    #   "Nothing in for two weeks" over a flag that tests missing work OR an
    #   average under 50, with no two weeks anywhere in it;
    #   "Across N marked assignments" over `kPapers.length - 1`, which assumes
    #   exactly one open paper;
    #   "Revision, not homework" over `k.last`, which is the newest SUBMISSION
    #   stamp — homework, precisely.
    ("""          { label: 'Submitted', value: kMx.colSub[wi] + '/' + k.n, sub: wPaper.title },
          { label: 'Week mean', value: wMean == null ? '—' : wMean + '%', sub: wGap == null ? 'Nothing marked' : (wGap === 0 ? 'Level with the term average' : Math.abs(wGap) + (Math.abs(wGap) === 1 ? ' point ' : ' points ') + (wGap > 0 ? 'above' : 'below') + ' the term average') },
          { label: 'On time', value: kMx.colSub[wi] ? Math.round((kMx.colOnTime[wi] / kMx.colSub[wi]) * 100) + '%' : '—', sub: wLate + ' late of ' + kMx.colSub[wi] + ' submitted' },
          { label: 'Not submitted', value: String(k.n - kMx.colSub[wi]), sub: 'Of ' + k.n + ' students' }
        ] : [
          { label: 'This week', value: kMx.colSub[0] + '/' + k.n, sub: upcomingPaper ? upcomingPaper.title : '' },
          { label: 'Class mean', value: kMean == null ? '—' : kMean + '%', sub: 'Across ' + (kPapers.length - 1) + ' marked assignments' },
          { label: 'On time', value: kMx.markedPct == null ? '—' : kMx.markedPct + '%', sub: Math.max(0, kMx.markedSub - kMx.markedOnTime) + ' late of ' + kMx.markedSub + ' marked' },
          { label: 'Needs a look', value: String(flagged), sub: flagged ? 'Nothing in for two weeks' : 'Everyone accounted for' }
        ]) : [
          { label: 'This week', value: '—', sub: 'No work set' },
          { label: 'Class mean', value: '—', sub: 'Nothing marked yet' },
          { label: 'Students', value: String(k.n), sub: 'Roster imported' },
          { label: 'Last activity', value: k.last, sub: 'Revision, not homework' }
        ]""",
     """          { label: 'Submitted', value: kAsked(wi), sub: wPaper.title },
          { label: 'Week mean', value: wMean == null ? '—' : wMean + '%', sub: wGap == null ? 'Nothing marked' : (wGap === 0 ? 'Level with the term average' : Math.abs(wGap) + (Math.abs(wGap) === 1 ? ' point ' : ' points ') + (wGap > 0 ? 'above' : 'below') + ' the term average') },
          { label: 'On time', value: kOnTimePct(wi), sub: MRB_LATE_LINE(kMx.colLate[wi], kMx.colLateUnknown[wi], kMx.colSub[wi], 'submitted') },
          { label: 'Not submitted', value: String(Math.max(0, (kMx.colAsked[wi] || 0) - kMx.colSub[wi])), sub: 'Of ' + (kMx.colAsked[wi] || 0) + ' asked' }
        ] : [
          { label: 'This week', value: kAsked(0), sub: upcomingPaper ? upcomingPaper.title : '' },
          { label: 'Class mean', value: kMean == null ? '—' : kMean + '%', sub: 'Across ' + kMx.markedIdx.length + (kMx.markedIdx.length === 1 ? ' marked assignment' : ' marked assignments') },
          { label: 'On time', value: kMx.markedPct == null ? '—' : kMx.markedPct + '%', sub: MRB_LATE_LINE(kMx.markedLate, kMx.markedLateUnknown, kMx.markedSub, 'marked') },
          { label: 'Needs a look', value: String(flagged), sub: flagged ? 'Nothing in this week, and behind' : 'Everyone accounted for' }
        ]) : [
          { label: 'This week', value: '—', sub: 'No work set' },
          { label: 'Class mean', value: '—', sub: 'Nothing marked yet' },
          { label: 'Students', value: String(k.n), sub: 'On the roster' },
          { label: 'Last activity', value: k.last, sub: 'Newest submission' }
        ]""",
     "the class screen's four tiles. See the block comment: the roster as a "
     "denominator, lateness by subtraction, and three captions that overstate "
     "their own figure."),

    # the two helpers those tiles now call, defined beside them
    ("    const flagged = kRoster.filter(r => r.flag).length;",
     "    const kAsked = (i) => kMx.colSub[i] + '/' + (kMx.colAsked[i] || 0);\n"
     "    const kOnTimePct = (i) => {\n"
     "      const known = kMx.colOnTime[i] + kMx.colLate[i];\n"
     "      return known ? Math.round((kMx.colOnTime[i] / known) * 100) + '%' "
     ": '—';\n"
     "    };\n"
     "    const flagged = kRoster.filter(r => r.flag).length;",
     "`kAsked` is `submitted/asked` — the denominator MRB-38 locked. "
     "`kOnTimePct` divides by the population whose lateness is KNOWN rather "
     "than by everyone who submitted, which is the same correction "
     "`markedPct` already carries in the seam."),

    ("        longMeta: 'Year ' + k.year + ' · ' + k.ks + ' · 2026–27 · ' + "
     "k.n + ' students · ' + (kPapers.length ? kPapers.length + "
     "' assignments' : 'no assignments'),",
     "        longMeta: [k.year == null ? '' : 'Year ' + k.year, k.ks, "
     "k.yearName,\n"
     "          k.n + ' students',\n"
     "          kPapers.length ? kPapers.length + (kPapers.length === 1 ? "
     "' assignment' : ' assignments') : 'no assignments'\n"
     "        ].filter(Boolean).join(' · '),",
     "the class header's long meta line. The year, and a plural that said "
     "\"1 assignments\".\n"
     "\n"
     "        ⊕ CORRECTED AGAIN, MRB-287 E1 — IT WAS THE SAME DEFECT AS THE "
     "CARD META, on the same class, one screen along. `MRB_DATA('yearLabel')` "
     "is the WORKING year, so a class opened out of 2025-26 read 2026-27 in "
     "its own header. Fixed here rather than left for later because two "
     "statements of one class's year that can disagree is worse than the "
     "line of scope it costs — and the class page is exactly where a teacher "
     "goes to check WHICH 11h/Ph1 they are looking at."),

    # ══ THE DIGEST ══════════════════════════════════════════════════════
    ("          : (c.state === 'nowork' ? 'No work set for two weeks' : (fl ? "
     "(fl === 1 ? '1 student to chase' : fl + ' students to chase') : "
     "'Nothing outstanding')),",
     "          : (c.state === 'nowork' ? 'No work set' : (fl ? "
     "(fl === 1 ? '1 student to chase' : fl + ' students to chase') : "
     "'Nothing outstanding')),",
     "`nowork` tests whether the class has ANY assignments, not for how long "
     "it has had none. A class set up yesterday read \"No work set for two "
     "weeks\"."),

    ("""      digestTiles: isClassReport ? [
        { label: 'Submissions', value: kMx.colSub[0] + '/' + k.n, sub: 'This week' },
        { label: 'Class mean', value: kMean == null ? '—' : kMean + '%', sub: 'Across ' + Math.max(0, kPapers.length - 1) + ' marked assignments' },
        { label: 'On time', value: kMx.markedPct == null ? '—' : kMx.markedPct + '%', sub: Math.max(0, kMx.markedSub - kMx.markedOnTime) + ' late of ' + kMx.markedSub + ' marked' },
        { label: 'Needs a look', value: String(kFlagged), sub: kFlagged ? 'Nothing in for two weeks' : 'Everyone accounted for' }
      ] : [
        { label: 'Submissions', value: String(totalSubs), sub: 'Across ' + liveClasses.length + ' active classes' },
        { label: 'Mean score', value: Math.round(liveClasses.reduce((a, c) => a + (this.meanOf(c) || 0), 0) / liveClasses.length) + '%', sub: 'Mean of ' + liveClasses.length + ' class means' },""",
     """      digestTiles: isClassReport ? [
        { label: 'Submissions', value: kAsked(0), sub: 'This week' },
        { label: 'Class mean', value: kMean == null ? '—' : kMean + '%', sub: 'Across ' + kMx.markedIdx.length + (kMx.markedIdx.length === 1 ? ' marked assignment' : ' marked assignments') },
        { label: 'On time', value: kMx.markedPct == null ? '—' : kMx.markedPct + '%', sub: MRB_LATE_LINE(kMx.markedLate, kMx.markedLateUnknown, kMx.markedSub, 'marked') },
        { label: 'Needs a look', value: String(kFlagged), sub: kFlagged ? 'Nothing in this week, and behind' : 'Everyone accounted for' }
      ] : [
        { label: 'Submissions', value: String(totalSubs), sub: 'Across ' + liveClasses.length + (liveClasses.length === 1 ? ' active class' : ' active classes') },
        { label: 'Mean score', value: liveClasses.length ? Math.round(liveClasses.reduce((a, c) => a + (this.meanOf(c) || 0), 0) / liveClasses.length) + '%' : '—', sub: 'Mean of ' + liveClasses.length + (liveClasses.length === 1 ? ' class mean' : ' class means') },""",
     "the digest's four tiles. The same three corrections as the class "
     "screen's, plus the division by `liveClasses.length` — which is ZERO for "
     "a teacher whose classes have no work set yet, and `NaN%` was what a "
     "teacher saw on their first day."),

    ("""      const missing = k.n - kMx.colSub[p.idx];""",
     """      const missing = Math.max(0, (kMx.colAsked[p.idx] || 0) - kMx.colSub[p.idx]);""",
     "`classReportRows`. Same denominator defect: `k.n` is the CURRENT "
     "roster, and a departed student who submitted makes this negative."),

    # ══ chartFor: FIVE CRASH PATHS AND FOUR READS OF A DELETED FIELD ════
    #
    # ⚑ EVERY ONE OF THESE IS REACHABLE ON A TEACHER'S FIRST DAY, which is
    # exactly when nobody is watching. Design's sample always has live
    # classes, always has marked papers and always has eight marked questions,
    # so none of them can fire in the delivery.
    ("""      if (all) {
        const raw = live.map(c => ({ code: c.code, ks: c.ks, mean: mx(c).classMean || 0 }));
        const cohort = Math.round(raw.reduce((a, r) => a + r.mean, 0) / (raw.length || 1));""",
     """      if (all) {
        const raw = live.map(c => ({ code: c.code, ks: c.ks, mean: mx(c).classMean || 0 }));
        if (!raw.length) { return { ...base, title: 'Class means, marked work', note: 'No class has marked work yet' }; }
        const cohort = Math.round(raw.reduce((a, r) => a + r.mean, 0) / (raw.length || 1));""",
     "`means / all` reads `sorted[0]` and `sorted[sorted.length - 1]` "
     "immediately afterwards. With no live classes both are `undefined` and "
     "the chart throws, taking the whole page with it."),

    ("""      const means = ps.map(p => m.colMean[p.idx]);
      const best = ps[means.indexOf(Math.max.apply(null, means))];
      const worst = ps[means.indexOf(Math.min.apply(null, means))];""",
     """      const means = ps.map(p => m.colMean[p.idx]);
      if (!ps.length) { return { ...base, title: k.code + ' — mean by assignment', note: 'Nothing marked yet' }; }
      const best = ps[means.indexOf(Math.max.apply(null, means))];
      const worst = ps[means.indexOf(Math.min.apply(null, means))];""",
     "`means / class`. `Math.max.apply(null, [])` is `-Infinity`, "
     "`indexOf(-Infinity)` is `-1`, and `ps[-1].idx` throws. A class with no "
     "marked work is not an edge case — it is every class in September."),

    ("""        const rows = live.map(c => {
          const g = this.gridFor(c, 1);
          const min = Math.min.apply(null, g.qpct);
          const qi = g.qpct.indexOf(min);
          return { label: c.code, sub: this.STEMS[qi].id + ' · ' + this.STEMS[qi].text, value: min + '%', pct: min, fill: min < 50 ? 'var(--st-accent)' : 'var(--st-hatch-b)', qi };
        });""",
     """        const rows = live.map(c => {
          const gi = MRB_NEWEST_MARKED(this.papersFor(c));
          const g = gi < 0 ? null : this.gridFor(c, gi);
          const scored = g ? g.qpct.filter(v => v != null) : [];
          if (!scored.length) { return null; }
          const min = Math.min.apply(null, scored);
          const qi = g.qpct.indexOf(min);
          const st = g.stems[qi] || { id: '—', text: '' };
          return { label: c.code, sub: st.id + ' · ' + st.text, value: min + '%', pct: min, fill: min < 50 ? 'var(--st-accent)' : 'var(--st-hatch-b)', qi };
        }).filter(r => r);
        if (!rows.length) { return { ...base, title: 'Weakest question per class, last marked set', note: 'No class has a marked paper yet' }; }""",
     "`questions / all`. FOUR defects in five lines: `gridFor(c, 1)` assumes "
     "paper 1 is the newest marked one; the grid can be `null` (not "
     "prefetched); `qpct` can hold nulls, and `Math.min` over `[null]` is 0 "
     "so an unmarked paper became a 0% weakest question; and `STEMS[-1]` "
     "throws when `indexOf` misses."),

    ("""      const g = this.gridFor(k, 1);
      const p = this.papersFor(k)[1];
      const min = Math.min.apply(null, g.qpct);
      const max = Math.max.apply(null, g.qpct);
      const qi = g.qpct.indexOf(min);
      return { ...base, type: 'cols', title: k.code + ' — ' + p.title,
        cols: this.colsFrom(this.STEMS.map((q, i) => ({ label: q.id, value: g.qpct[i] + '%', raw: g.qpct[i], flag: g.qpct[i] === min })), 100),
        tiles: [tile('Paper mean', mx(k).colMean[1] + '%', g.submitted + ' of ' + k.n + ' submitted'),
          tile('Lowest', this.STEMS[qi].id + ' · ' + min + '%', this.STEMS[qi].text), tile('Highest', max + '%', 'Best answered question')],
        note: 'Reteach ' + this.STEMS[qi].text.toLowerCase() + ' — ' + min + '% of the class got it' };""",
     """      const gi = MRB_NEWEST_MARKED(this.papersFor(k));
      const g = gi < 0 ? null : this.gridFor(k, gi);
      const p = gi < 0 ? null : this.papersFor(k)[gi];
      const scored = g ? g.qpct.filter(v => v != null) : [];
      if (!g || !p || !scored.length) {
        return { ...base, type: 'cols', title: k.code + ' — question difficulty', note: g ? 'Nothing on this paper was machine-marked' : 'No marked paper yet' };
      }
      const min = Math.min.apply(null, scored);
      const max = Math.max.apply(null, scored);
      const qi = g.qpct.indexOf(min);
      const lowest = g.stems[qi] || { id: '—', text: '' };
      return { ...base, type: 'cols', title: k.code + ' — ' + p.title,
        cols: this.colsFrom(g.stems.map((q, i) => ({ label: q.id, value: g.qpct[i] == null ? 'Not marked' : g.qpct[i] + '%', raw: g.qpct[i] == null ? 0 : g.qpct[i], flag: g.qpct[i] != null && g.qpct[i] === min })), 100),
        tiles: [tile('Paper mean', mx(k).colMean[gi] == null ? '—' : mx(k).colMean[gi] + '%', g.submitted + ' of ' + (mx(k).colAsked[gi] || 0) + ' submitted'),
          tile('Lowest', lowest.id + ' · ' + min + '%', lowest.text), tile('Highest', max + '%', 'Best answered question')],
        note: lowest.text ? 'Reteach ' + lowest.text.toLowerCase() + ' — ' + min + '% of the class got it' : '' };""",
     "`questions / class`. The same four, plus `papersFor(k)[1].title` on a "
     "one-paper class, plus `k.n` as the submitted denominator, plus "
     "`STEMS[qi].text.toLowerCase()` on a stem that no longer exists."),

    ("""      const rows = live.map(c => {
        const m = mx(c);
        const pct = c.n ? Math.round((m.colSub[0] / c.n) * 100) : 0;
        return { label: c.code, sub: c.ks, value: m.colSub[0] + '/' + c.n, pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
      });""",
     """      const rows = live.map(c => {
        const m = mx(c);
        const asked = m.colAsked[0] || 0;
        const pct = asked ? Math.round((m.colSub[0] / asked) * 100) : 0;
        return { label: c.code, sub: c.ks, value: m.colSub[0] + '/' + asked, pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
      });""",
     "`submissions / all`. `c.n` is the current roster; a class where two "
     "pupils left after submitting read \"31/29\"."),

    ("""    const rows = this.papersFor(k).map(p => {
      const pct = k.n ? Math.round((m.colSub[p.idx] / k.n) * 100) : 0;
      return { label: p.title, sub: (p.when === 'upcoming' ? 'Open · due ' + p.due.replace('Due ', '') : 'Marked · due ' + p.due), value: m.colSub[p.idx] + '/' + k.n, pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
    });""",
     """    const rows = this.papersFor(k).map(p => {
      const asked = m.colAsked[p.idx] || 0;
      const pct = asked ? Math.round((m.colSub[p.idx] / asked) * 100) : 0;
      return { label: p.title, sub: (p.when === 'upcoming' ? 'Open · due ' + p.due.replace('Due ', '') : 'Marked · due ' + p.due), value: p.sub, pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
    });""",
     "`submissions / class`. Same denominator, and the value string is "
     "`p.sub`, which the seam has already built as `colSub/colAsked` — one "
     "answer rather than two."),

    ("""        ? live.map(c => ({ label: c.code, sub: c.ks, on: mx(c).markedOnTime, tot: mx(c).markedSub }))
        : this.papersFor(k).filter(p => p.when === 'marked').map(p => ({ label: p.title, sub: 'Due ' + p.due, on: mx(k).colOnTime[p.idx], tot: mx(k).colSub[p.idx] }));""",
     """        ? live.map(c => ({ label: c.code, sub: c.ks, on: mx(c).markedOnTime, tot: mx(c).markedOnTime + mx(c).markedLate }))
        : this.papersFor(k).filter(p => p.when === 'marked').map(p => ({ label: p.title, sub: 'Due ' + p.due, on: mx(k).colOnTime[p.idx], tot: mx(k).colOnTime[p.idx] + mx(k).colLate[p.idx] }));""",
     "the on-time chart. `markedSub` includes the submissions whose lateness "
     "is UNKNOWN, so the bar counted every unknown as late — the same error "
     "as the roster row's, in a graph, where it is harder to see."),

    # ══ the shoutout feed, the search pool, the import wizard ═══════════
    ("""      feed: [
        {
          name: kRoster.length ? kRoster[Math.min(9, kRoster.length - 1)].name : '—',
          when: '2 days ago',
          template: 'Top of the class this week',
          body: 'Highest mean in ' + k.code + ' on the last set — and showed working on every question.'
        },
        {
          name: kRoster.length ? kRoster[Math.min(12, kRoster.length - 1)].name : '—',
          when: '1 week ago',
          template: 'Bounced back strong',
          body: 'Went from 38% to 74% after one reteach of the lowest-scoring question.'
        }
      ].map(f => ({ ...f, initials: this.initials(f.name), hue: this.hueFor(f.name) })),""",
     "      feed: (MRB_DATA('FEED')[k && k.id] || []).map((f) => ({\n"
     "        ...f,\n"
     "        /* ⊕ MRB-287 — THE DELETE AFFORDANCE, AUTHOR-ONLY. The RLS\n"
     "           UPDATE policy is `author_id = auth.uid() AND\n"
     "           auth_user_teaches_class(class_id)`, so this asks the same\n"
     "           question the database will ask, BEFORE the control is drawn\n"
     "           rather than after it is pressed. */\n"
     "        /* ⊕ MRB-287 E1 — AND NOT ON A PAST YEAR. Removing a shoutout\n"
     "           is a WRITE, and MRB-261 makes a finished year read-only.\n"
     "           Without this the E1 wrap would take the composer off the\n"
     "           page and leave the destructive half of the feed live, which\n"
     "           is the worse half to leave. `canWrite` is the same key that\n"
     "           gates the composer, so the two cannot disagree.\n"
     "           ⚠️ READ THROUGH `MRB_DATA`, NOT AS A BARE NAME: `canWrite`\n"
     "           is a KEY of the object being built here, not a local, so\n"
     "           the identifier is not in scope inside this map. */\n"
     "        canDelete: !!(MRB_DATA('canWrite') && f.id && f.author_id &&\n"
     "                      f.author_id === MRB_ME()),\n"
     "        del: () => this.setState({ delId: f.id, delName: f.name }),\n"
     "      })),",
     "⚑ TWO COMPLETE FABRICATED SHOUTOUTS, and they are NOT in the template "
     "so no literal sweep finds them: a real child's name off the roster, a "
     "relative time, a template label and a written body — \"Went from 38% to "
     "74% after one reteach\" — rendered on the class screen under the "
     "heading a real feed uses, with words put in a teacher's mouth. "
     "`teacher-live.js` reads the real ones and already computes `initials` "
     "and `hue`, so Design's `.map` goes with the sample rather than being "
     "kept: two derivations of one avatar is two answers.\n"
     "\n"
     "        `FEED` is keyed by class and is populated only on the class and "
     "student screens — the seam's own scoping — so this reads through the "
     "map rather than `MRB_PICK`, which would throw on the five screens that "
     "have no feed to show.\n"
     "\n"
     "        ⊕ AND THE `.map` IS BACK, FOR A DIFFERENT REASON — 24 Aug 2026. "
     "Design's map computed `initials` and `hue`; that half stays deleted, "
     "and neither is recomputed here. What this map adds is the DELETE "
     "AFFORDANCE Mide asked for: a per-row `canDelete` and a per-row `del`, "
     "which is Design's own idiom for a control inside a list (`t.pick` on "
     "the template buttons, `s.toggle` on the bulk chips). See "
     "AMENDED_ADDITIONS."),

    ("""    const pool = [];
    this.POOL_CLASSES.forEach(id => {
      const kk = this.klassById(id);
      this.rosterFor(kk).slice(0, 3).forEach(r => {
        pool.push({ name: r.name, klass: kk.code, classId: kk.id, id: r.id, avg: r.avg == null ? '—' : r.avg + '%' });
      });
    });""",
     "    const pool = MRB_DATA('searchPool');",
     "what the top bar's search searches. Design's pool is the first three "
     "children of five hand-picked classes — fifteen names, so a teacher "
     "typing a real child's surname found nothing. The real pool is every "
     "student on every class the teacher holds this year, which is what the "
     "box says it is."),

    ("""      mapRows: [
        { col: 'first_name', field: 'First name', note: 'Matched', noteFg: 'var(--ks3-ok-text)' },
        { col: 'surname', field: 'Last name', note: 'Matched', noteFg: 'var(--ks3-ok-text)' },
        { col: 'school_email', field: 'Email', note: 'Matched', noteFg: 'var(--ks3-ok-text)' },
        { col: 'yr', field: 'Year group', note: 'Guessed from header', noteFg: 'var(--st-muted)' },
        { col: 'form', field: 'Ignored', note: 'Not used by Mr Badmus AI', noteFg: 'var(--st-ghost)' }
      ],
      previewRows: [
        { name: 'Aisha Bello', email: 'a.bello@school.uk', klass: '8r/Sc4', status: 'New', stFg: 'var(--ks3-ok-text)' },
        { name: 'Tom Okri', email: 't.okri@school.uk', klass: '8r/Sc4', status: 'New', stFg: 'var(--ks3-ok-text)' },
        { name: 'Daisy Fairhurst', email: 'd.fairhurst@school.uk', klass: '8r/Sc1', status: 'Already enrolled', stFg: 'var(--st-muted)' },
        { name: 'J. Smith', email: 'missing', klass: '8r/Sc4', status: 'Email missing', stFg: 'var(--st-accent-text)' }
      ],""",
     "      mapRows: MRB_DATA('IMPORT_MAP_ROWS'),\n"
     "      previewRows: MRB_DATA('IMPORT_PREVIEW_ROWS'),",
     "⚑ FOUR INVENTED CHILDREN WITH INVENTED SCHOOL EMAIL ADDRESSES, on the "
     "confirm step, under the heading a teacher reads before pressing Import. "
     "Of everything in this delivery this is the one a teacher would most "
     "plausibly have believed.\n"
     "\n"
     "        Both keys come back EMPTY from the seam, on purpose: the live "
     "wizard already parses the file and already runs the dry-run, and a "
     "second implementation in the data layer would be a second answer. The "
     "empty arrays render Design's tables with no rows until the live "
     "wizard fills them through `data-import-slot`."),

    # ══ ⊕ 24 Aug 2026 · A CAP SIZED TO A FIFTEEN-NAME SAMPLE ═══════════
    #
    # ⛔ THE THIRD SILENT CAP, AND THE ONE THAT SURVIVED. This port has
    # already taken two out of Design's delivery for the same reason — the
    # marking grid's `.slice(0, 10)`, which hid two thirds of a class on the
    # screen a teacher opens to find who is struggling, and the fifteen-name
    # search POOL, which meant a teacher typing a real child's surname found
    # nothing. This one is `.slice(0, 12)` on the search RESULTS, and it is
    # on all six pages.
    #
    # Design's cap was sized to her own sample: fifteen invented names, so
    # twelve was almost all of them and the cap almost never bit. The pool
    # behind it is now REAL — every student on every class the teacher holds
    # this year — and at a secondary school a common letter matches far more
    # than twelve. A teacher types "s", sees twelve, and has no way to know
    # there are thirty-one.
    #
    # ⚑ THE FIX IS A COUNT, NOT PAGINATION, and that is a judgement about
    # what the control IS. A search dropdown is refined by TYPING; a "load
    # more" inside it would be a second way to do the thing the box already
    # does, and the shoutout feed's `shoutouts-loadmore` region exists
    # because a FEED is the opposite case. So the cap stays and the
    # truncation is DECLARED.
    #
    # ⊕ AND IT IS DESIGN'S OWN CAPTION, CORRECTED — NOT A NEW ONE. Node 553
    # already sits directly under the results list, in the mono/caption/
    # uppercase register, bound to `searchFoot`, on every page that keeps the
    # overlay. What it SAID was `results.length + ' of ' + pool.length +
    # ' students'`, which is wrong twice over on a real pool: `results.length`
    # is the POST-CAP number, so it reads "12" no matter how many matched,
    # and `pool.length` is every student the teacher has rather than every
    # student who matched. On a query matching thirty-one of sixty it read
    # "12 OF 60 STUDENTS" — a sentence in which neither number is the one a
    # teacher wants and nothing says anything was withheld.
    #
    # ⚠️ SO THERE IS NO `INSERT_AT` ENTRY FOR THIS, deliberately. Inserting a
    # second caption under the first would put two sentences about one
    # condition on one strip, which is the failure `INSERT_AT[31]`'s own note
    # rules against — and `INSERT_AT` is documented here as the LAST RESORT,
    # for states Design drew no counterpart for. She drew this one.
    ("""    const results = pool.filter(p => !q || p.name.toLowerCase().indexOf(q) > -1).slice(0, 12).map(p => ({""",
     "    /* ⊕ MRB-287 — MATCHED, BEFORE THE CAP. The count a teacher needs "
     "is\n"
     "       how many matched, not how many exist and not how many fit. */\n"
     "    const matched = pool.filter(p => !q || "
     "p.name.toLowerCase().indexOf(q) > -1);\n"
     "    const results = matched.slice(0, 12).map(p => ({",
     "the search results, so the number withheld by the cap can be known. "
     "The cap itself is unchanged: twelve rows is a dropdown, and the answer "
     "to more than twelve matches is to keep typing."),

    ("      searchFoot: results.length + ' of ' + pool.length + ' students "
     "· type to narrow',",
     "      searchFoot: MRB_SEARCH_FOOT(matched.length, results.length,\n"
     "                                  pool.length, q),",
     "Design's own footer caption, saying what it is under. It named the "
     "post-cap row count and the whole roster and never the match total, so "
     "a truncated search was indistinguishable from a complete one."),

    # ══ the two keys the rulings introduce ══════════════════════════════
    ("      searchResults: results,",
     "      searchPlaceholder: MRB_DATA('searchPlaceholder'),\n"
     "      searchResults: results,",
     "the key `BIND_ATTR` 545 interpolates. Placed beside `searchFoot`, "
     "Design's own computed sentence about the same overlay, so the two "
     "cannot drift apart."),

    # ══ ⊕ MRB-287 E1 · THE ACADEMIC YEAR IN VIEW, ON EVERY SCREEN ═══════
    #
    # ⚠️ AT THE HEAD OF THE RETURN OBJECT, NOT IN THE CLASSES BLOCK, AND THAT
    # IS DELIBERATE. `hasOtherYears` and `yearOptions` are only ever read on
    # the classes screen, but `canWrite` gates the shoutout composer on
    # class-detail and `readOnlyLine` is drawn in its header. One key with two
    # derivations is how two screens end up disagreeing about whether a year
    # is writable — so there is ONE derivation, in the seam, and one placement
    # here that every screen can see.
    #
    # A `<for>` scope reaches these through the prototype chain
    # (`student-runtime.js:158`, `Object.create(scope)`), which is what lets
    # `WRAP` gate node 78 — a control inside the class-card loop — on
    # `canWrite`.
    ("    return {\n      teacher,",
     "    return {\n      teacher,\n"
     "      /* ⊕ MRB-287 E1 — the year in view. See teacher_rulings. */\n"
     "      yearsOpen: s.yearsOpen,\n"
     "      hasOtherYears: MRB_DATA('hasOtherYears'),\n"
     "      canWrite: MRB_DATA('canWrite'),\n"
     "      readOnlyLine: MRB_DATA('readOnlyLine'),\n"
     "      yearOptions: MRB_DATA('yearOptions').map((y) => ({\n"
     "        name: y.name,\n"
     "        open: () => MRB_GO('classes', { year: y.id })\n"
     "      })),",
     "the five keys the year selector and the read-only rule need. "
     "`yearOptions` is mapped into Design's own row idiom — a `name` and an "
     "`open`, the same shape as `t.pick` on the template buttons — so the "
     "inserted list is a list of Design's rows rather than a new pattern. "
     "Switching year always returns to the GRID, which is the retired page's "
     "behaviour and the only destination that is certainly valid in the year "
     "being opened."),

    ("      goClasses: () =>",
     "      signOut: () => window.MrBadmusTeacherGuard.signOut(),\n"
     "      goClasses: () =>",
     "the real sign-out, for node 29 — a \"Sign out\" button Design drew with "
     "no handler at all. Deliberately NOT guarded with a `&&`: if the guard "
     "has not loaded, the page has no business being on screen and a thrown "
     "error is the correct outcome."),

    # ══ TWO TOASTS THAT STATE A FACT, AND KNOW NOTHING ══════════════════
    #
    # ⚑ NEITHER IS IN THE TEMPLATE, so no literal sweep of the markup finds
    # them, and both are shown to a teacher as a CONFIRMATION — the one kind
    # of copy a person reads as a statement about what just happened to their
    # own data.
    ("      pastYears: () => this.ping('2025–26 is read-only')",
     "      pastYears: () => this.setState({ yearsOpen: "
     "!this.state.yearsOpen }),",
     "'2025-26 is read-only'. TWO defects in one line, and the second is the "
     "one that mattered.\n"
     "\n"
     "        · A hardcoded academic year in user-visible copy: wrong from "
     "1 September, and wrong on day one for any school whose previous year "
     "is not 2025-26.\n"
     "        · A DEAD END DRESSED AS AN ANSWER. It named a year and offered "
     "no way to open it, on the one screen whose whole point (MRB-261) is "
     "that a teacher's past classes stay reachable. An earlier pass replaced "
     "the literal with the real list and kept it a toast, which fixed the "
     "copy and left the dead end exactly where it was.\n"
     "\n"
     "        It is the disclosure half of a real control now: the list it "
     "opens is `INSERT_AT[83]`, the years come from the seam as "
     "`yearOptions`, and node 86 does not render at all when there is no "
     "other year to reach (`WRAP`, `hasOtherYears`) — so the state Design's "
     "version answered with a toast is now a control that is simply not "
     "there."),

    ("      impDone: () => { this.setState({ screen: 'classes', importStep: "
     "1 }); this.ping('26 students imported into 8r/Sc4'); },",
     "      impDone: () => {\n"
     "        /* The REAL import is the live wizard's `#confirm-import`, "
     "which is carried\n"
     "           into this page as a live region. Design's button is its "
     "PRESENTATION;\n"
     "           this is the only seam a generated page can offer it. */\n"
     "        window.dispatchEvent(new CustomEvent('mrb-import-confirm'));\n"
     "        const line = MRB_DATA('importCountLabel');\n"
     "        if (line) { this.ping(line); }\n"
     "      },",
     "⛔ THE WORST TOAST ON THE DASHBOARD: '26 students imported into "
     "8r/Sc4' — a hardcoded count AND a hardcoded class code, shown as "
     "confirmation of something that did not happen, on a screen whose whole "
     "job is to change a school's roster. A teacher reads that sentence as a "
     "fact about their own file.\n"
     "\n"
     "        It makes NO CLAIM now unless the seam gives it one to make. "
     "`importCountLabel` comes back empty from `teacher-live.js` on purpose "
     "— the live wizard is what knows the count, and a second implementation "
     "in the data layer would be a second answer — so the button dispatches "
     "an event the wizard can listen for and says nothing until something "
     "real has a number. Design's `setState({ screen: 'classes' })` also "
     "goes: the screens are pages now, and navigating away is the one thing "
     "this button must NOT do before the import has run."),

    # ══ ⊕ 24 Aug 2026 · THE COLD LOAD ═══════════════════════════════════
    #
    # ⛔ THE WEEK RAIL OPENED PARKED ON JUNE. Measured on class-detail:
    # `scrollLeft: 0`, `maxScroll: 360`, and the selected chip — "17-21 Aug ·
    # THIS WEEK" — is the LAST of the twelve. A teacher lands on a class page
    # looking at a week eleven weeks in the past.
    #
    # Design drew this correctly and the PORT lost it, and the mechanism is
    # the whole single-page-to-many-URLs seam in one line: `snapWeekRail()` is
    # called from exactly one place, `openClass`'s `setState` callback, and in
    # Design's prototype you always reached the class screen by pressing a
    # class card, so `openClass` always ran. With seven URLs you arrive COLD —
    # from a bookmark, a link, a reload, or `MRB_GO` from another page — and
    # nothing calls it. `componentDidMount` was not defined at all.
    #
    # ⚠️ NO SECOND GUARD, AND THAT WAS VERIFIED RATHER THAN ASSUMED. `rail()`
    # is `document.querySelector('[data-rail="weeks"]')` and the rail is drawn
    # only on the class screen; `snapWeekRail`'s inner `snap` opens
    # `if (!el) return;`. On the five other pages this is two no-ops on a
    # frame.
    #
    # ⊕ AND `componentDidUpdate`, WHICH IS THE SAME DEFECT ONE PRESS LATER.
    # `student-runtime.draw()` empties the host and rebuilds it, so EVERY
    # `setState` resets the rail's `scrollLeft` to 0 — press a sort tab, open
    # the search overlay, dismiss a toast, and the rail is back on June. It
    # re-snaps only when the rail is scrolled hard left AND has somewhere to
    # scroll, which is exactly the state a rebuild leaves behind; a teacher
    # who has scrolled the rail themselves and then presses something else
    # loses that scroll either way, because the element they scrolled no
    # longer exists.
    ("  openClass(patch) { this.setState({ screen: 'class', weekIdx: 0, "
     "...patch }, () => this.snapWeekRail()); }",
     "  /* ⊕ MRB-287 — THE COLD LOAD. Seven URLs mean the class page is\n"
     "     reached without `openClass` ever running. See teacher_rulings. */\n"
     "  componentDidMount() { this.snapWeekRail(); }\n"
     "  componentDidUpdate() {\n"
     "    const el = this.rail();\n"
     "    if (el && !el.scrollLeft && el.scrollWidth > el.clientWidth) {\n"
     "      this.snapWeekRail();\n"
     "    }\n"
     "  }\n"
     "  openClass(patch) { this.setState({ screen: 'class', weekIdx: 0, "
     "...patch }, () => this.snapWeekRail()); }",
     "the week rail's scroll position, on a page opened directly. Design's "
     "only caller was a screen-change handler and there are no screen "
     "changes any more."),

    # ══ ⊕ 24 Aug 2026 · A FILTER THAT MATCHES NOTHING ═══════════════════
    #
    # The two keys `INSERT_AT[31]` renders. `s.ks` is the filter that is ON,
    # so the sentence names the FILTER — "No KS4 classes" — and never claims
    # the teacher has no classes: they have classes, they filtered them out,
    # and the genuinely-empty case never reaches this grid because
    # `teacher-live.js` throws `SAY.noClasses` before mount.
    ("      shownLine: cards.length + ' shown',",
     "      shownLine: cards.length + ' shown',\n"
     "      noneShown: !cards.length,\n"
     "      noneShownLine: s.ks === 'All' ? 'No classes'\n"
     "        : 'No ' + s.ks + ' classes',",
     "the classes grid's empty state. Design drew none because Design's "
     "sample always has both key stages in it."),

    # ══ ⊕ 24 Aug 2026 · THE SHOUTOUT COMPOSER, WIRED ════════════════════
    #
    # ⛔ A COMPOSER THAT LOOKS LIKE IT SENDS AND DOES NOT IS WORSE THAN NO
    # COMPOSER. Design's `sendShoutout` is one `ping`: it picks between
    # "Shoutout sent to <name>" and "Pick a student first" and writes nothing
    # either way. The teacher believes a child has been told; the child never
    # hears; and there is no error anywhere to notice.
    #
    # The write path existed the whole time —
    # `MrBadmusTeacherData.insertClassShoutout({classId, authorId,
    # recipientId, templateKey, message})` — and the hand-written
    # `class-detail.html` has driven it since MRB-46. This is that flow,
    # reused rather than reinvented: the same validation (a recipient, and at
    # least one of template/message), the same 500-character cap, the same
    # two error branches, and the same re-fetch of the feed on success.
    #
    # ⚠️ THE WRITE IS ASYNC AND `renderVals` IS NOT, and that is fine: the
    # promise is fired and the state is set on settle. What must NOT happen is
    # a rejection escaping into a synchronous closure, which is why
    # `MRB_SEND_SHOUTOUTS` resolves on every path.
    #
    # ⚠️ NO SUCCESS TOAST. The proof that a shoutout sent is the shoutout
    # appearing at the top of the feed, which `MRB_REFRESH_FEED` fetches. A
    # toast saying "sent" is the exact sentence Design shipped without a
    # write behind it, and it would be indistinguishable from it.
    ("      sendShoutout: () => this.ping(s.recipient ? 'Shoutout sent to ' "
     "+ s.recipient : 'Pick a student first'),",
     "      sendShoutout: () => {\n"
     "        const rid = s.recipient;\n"
     "        const body = String(s.note || '').trim();\n"
     "        if (!rid) { return this.ping('Pick a student first'); }\n"
     "        if (!s.boTpl && !body) {\n"
     "          return this.ping('Pick a template, or write a message'); }\n"
     "        if (body.length > 500) {\n"
     "          MRB_COMPOSE_ERROR('Message too long — 500 characters "
     "at most.');\n"
     "          return this.ping('Message too long — 500 characters at "
     "most'); }\n"
     "        MRB_COMPOSE_ERROR('');\n"
     "        this.ping('Sending…');\n"
     "        const cid = k && k.id;\n"
     "        MRB_SEND_SHOUTOUTS(cid, [rid], s.boTpl, body || null)\n"
     "          .then((r) => {\n"
     "            if (!r.ok) {\n"
     "              const why = MRB_SHOUTOUT_WHY(r.error);\n"
     "              MRB_COMPOSE_ERROR(why);\n"
     "              return this.ping(why);\n"
     "            }\n"
     "            /* Design's fields are uncontrolled and the runtime carries\n"
     "               their values over a redraw, so the DOM is cleared before\n"
     "               the state is. */\n"
     "            MRB_COMPOSE_RESET();\n"
     "            MRB_REFRESH_FEED(cid).then(() => {\n"
     "              this.setState({ recipient: '', note: '', toast: '' });\n"
     "            });\n"
     "          });\n"
     "      },",
     "the shoutout composer. Design's version toasts a confirmation of a "
     "write that does not happen."),

    # ⛔ AND THE BULK SHEET, WHICH IS THE SAME LIE MULTIPLIED. Design's
    # `sendBulk` closes the sheet, empties the selection and toasts "Shoutout
    # sent to 6 students". Six children, none of whom were told anything.
    #
    # ⚠️ IT REPORTS PARTIAL FAILURE AND NEVER A BARE SUCCESS. N inserts can
    # settle N ways — one recipient may have left the class between the roster
    # being read and the button being pressed, and RLS refuses that one row
    # and no others. "Sent to 4 of 6" is the only honest sentence there, and
    # the sheet stays OPEN with the selection intact when anything failed, so
    # the teacher can see who was chosen and try again.
    ("""      sendBulk: () => {
        const n = s.boSel.length;
        this.setState({ modal: null, boSel: [] });
        this.ping(n ? 'Shoutout sent to ' + n + ' students' : 'Pick at least one student');
      },""",
     "      sendBulk: () => {\n"
     "        const ids = (s.boSel || []).slice();\n"
     "        if (!ids.length) {\n"
     "          return this.ping('Pick at least one student'); }\n"
     "        this.ping('Sending to ' + ids.length + '…');\n"
     "        const cid = k && k.id;\n"
     "        MRB_SEND_SHOUTOUTS(cid, ids, s.boTpl, null).then((r) => {\n"
     "          if (!r.ok) {\n"
     "            return this.ping(MRB_SHOUTOUT_WHY(r.error)); }\n"
     "          if (r.fail) {\n"
     "            /* The sheet stays open and the selection stays put: some "
     "of\n"
     "               these children were told and some were not, and the "
     "teacher\n"
     "               is the only one who can decide what to do about it. */\n"
     "            return this.ping('Sent to ' + r.ok + ' of ' + ids.length +\n"
     "              ' — ' + MRB_SHOUTOUT_WHY(r.error)); }\n"
     "          MRB_REFRESH_FEED(cid).then(() => {\n"
     "            this.setState({ modal: null, boSel: [],\n"
     "              toast: 'Shoutout sent to ' + r.ok +\n"
     "                (r.ok === 1 ? ' student' : ' students') });\n"
     "          });\n"
     "        });\n"
     "      },",
     "the bulk shoutout sheet. Same defect as the composer, N times over."),

    # ══ ⊕ 24 Aug 2026 · \"ON TIME\" WHERE THE TIMING IS UNKNOWN ═══════════
    #
    # ⚑ THE STANDING RULING, APPLIED TO THE FOUR PLACES THAT STILL BROKE IT.
    # `is_late` is NULL on every submission written before 22 Aug 2026 and on
    # any submission with no deadline, so "unknown" is a real population and
    # not a rounding error. It must not render as late (an accusation), and it
    # must not render as on time (a flattery), and a count of the on-time ones
    # must not be printed as a bare number when NOTHING is known — because
    # that number is 0, and 0 reads as "nobody was on time".
    #
    # The roster line, the two class tiles and the on-time chart were already
    # routed through `MRB_LATE_LINE`. These four were missed.
    ("          { label: 'On time', value: pp.when === 'upcoming' ? '—' "
     ": String(kMx.colOnTime[pp.idx]), sub: pp.when === 'upcoming' ? 'Not due "
     "yet' : 'Late submissions still marked' },",
     "          { label: 'On time',\n"
     "            value: pp.when === 'upcoming' ? '—'\n"
     "              : MRB_ONTIME_VALUE(kMx.colOnTime[pp.idx], "
     "kMx.colLate[pp.idx]),\n"
     "            sub: pp.when === 'upcoming' ? 'Not due yet'\n"
     "              : MRB_ONTIME_SUB(kMx.colOnTime[pp.idx], "
     "kMx.colLate[pp.idx],\n"
     "                               kMx.colLateUnknown[pp.idx], "
     "'submitted') },",
     "the marking screen's On-time tile. It printed `colOnTime` raw, so a "
     "paper with thirteen submissions and no recorded deadlines read ON TIME "
     "0 under a SUBMITTED tile reading 13/16, over a caption saying \"Late "
     "submissions still marked\"."),

    ("      const late = !open && sc != null && stRow.late[i] === true;",
     "      const lateState = (!open && sc != null) ? stRow.late[i] : null;\n"
     "      const late = lateState === true;",
     "⊕ THE OTHER HALF OF THE `=== true` PIN. Making `late` strict stopped an "
     "unknown being CALLED late and did nothing about it being called ON "
     "TIME, which is what the status chip did — the previous ruling's own "
     "note claimed otherwise and was wrong. The tri-state is carried on the "
     "row now, so the chip and the tile can both see it."),

    ("      const tone = open ? 'neutral' : (sc == null || late ? 'warn' : "
     "'ok');",
     "      const tone = open ? 'neutral'\n"
     "        : (sc == null || late ? 'warn'\n"
     "          : (lateState === false ? 'ok' : 'neutral'));",
     "the status chip's colour. Green is Design's \"on time\"; an unknown is "
     "not a claim and takes the neutral tone."),

    ("        status: open ? (sc != null ? 'In progress' : 'Nothing in') : "
     "(sc == null ? 'Nothing in' : (late ? 'Late' : 'On time')),",
     "        status: open ? (sc != null ? 'In progress' : 'Nothing in')\n"
     "          : (sc == null ? 'Nothing in'\n"
     "            : (lateState === true ? 'Late'\n"
     "              : (lateState === false ? 'On time' : 'Submitted'))),",
     "the status chip on a row of the student's assignment history. It read "
     "\"On time\" for every submission whose timing is not recorded, which is "
     "every submission older than 22 Aug 2026."),

    # ══ ⊕ 24 Aug 2026 · THE SHOUTOUT DELETE, CONFIRMED AND WIRED ═══════
    #
    # Mide's instruction: a teacher who can post a shoutout can remove one.
    # Design drew no delete affordance at all, so these four keys and the
    # sheet in `INSERT_AT[88]` are an AMENDED ADDITION against her delivery
    # rather than a correction of it — see `AMENDED_ADDITIONS`.
    #
    # ⚠️ THE CONFIRM HOLDS AN ID, NOT A BOOLEAN. `delId` is the shoutout the
    # sheet is asking about, so the press that confirms cannot act on a
    # different row from the press that opened it — `renderVals` runs again
    # on every `setState` and the feed is re-read each time.
    #
    # ⚠️ IT DOES NOT REUSE DESIGN'S `modal`. `closeModal` sets `modal: null`
    # and nothing else, and the bulk sheet's close depends on that; a fourth
    # value in the same slot would mean one handler closing two different
    # things by luck of what happened to be open.
    #
    # ⚠️ NOTHING HERE REJECTS, for the reason `MRB_SEND_SHOUTOUTS` gives:
    # these are Design's SYNCHRONOUS `renderVals` closures, and a rejection
    # escaping one is a console error a teacher never sees, in front of a
    # feed that still shows the shoutout they believe they removed.
    #
    # ⚠️ NO SUCCESS TOAST, the same ruling as the composer's. The proof that
    # a shoutout was removed is that it is GONE from the feed, which
    # `MRB_REFRESH_FEED` re-reads. The failure path is the composer's own and
    # not a second one: `#compose-error` for the live region, and the toast
    # for the surface a teacher actually looks at.
    ("      closeModal: () => this.setState({ modal: null }),",
     "      closeModal: () => this.setState({ modal: null }),\n"
     "      delOpen: !!s.delId,\n"
     "      delName: s.delName || '',\n"
     "      cancelDelete: () => this.setState({ delId: '', delName: '' }),\n"
     "      confirmDelete: () => {\n"
     "        const sid = s.delId, cid = k && k.id;\n"
     "        this.setState({ delId: '', delName: '' });\n"
     "        if (!sid) { return; }\n"
     "        this.ping('Removing…');\n"
     "        MRB_DELETE_SHOUTOUT(sid).then((r) => {\n"
     "          if (!r.ok) {\n"
     "            const why = MRB_DELETE_WHY(r.error);\n"
     "            MRB_COMPOSE_ERROR(why);\n"
     "            return this.ping(why);\n"
     "          }\n"
     "          MRB_COMPOSE_ERROR('');\n"
     "          MRB_REFRESH_FEED(cid).then(() => {\n"
     "            this.setState({ toast: '' });\n"
     "          });\n"
     "        });\n"
     "      },",
     "the shoutout delete's state and its two handlers. Design has no "
     "counterpart at all: her feed card cannot be acted on."),

    ("""    const stOnTime = stMarked.filter(h => !h.late).length;
    const stLate = stMarked.filter(h => h.late).length;
    const stMissing = stHistory.filter(h => h.missing).length;
    const stTimeSub = (stLate === 0 && stMissing === 0)
      ? 'Every deadline met'
      : [stLate ? (stLate === 1 ? '1 late' : stLate + ' late') : null, stMissing ? stMissing + ' not submitted' : null].filter(x => x).join(' · ');""",
     "    const stOnTime = stMarked.filter(h => h.lateState === false).length;\n"
     "    const stLate = stMarked.filter(h => h.lateState === true).length;\n"
     "    const stUnknown = stMarked.length - stOnTime - stLate;\n"
     "    const stMissing = stHistory.filter(h => h.missing).length;\n"
     "    const stTimeSub = (function () {\n"
     "      const bits = [];\n"
     "      if (stLate) { bits.push(stLate === 1 ? '1 late'\n"
     "        : stLate + ' late'); }\n"
     "      if (stUnknown) { bits.push(stUnknown + ' timing unknown'); }\n"
     "      if (stMissing) { bits.push(stMissing + ' not submitted'); }\n"
     "      if (bits.length) { return bits.join(' · '); }\n"
     "      return stOnTime ? 'Every deadline met' : 'Nothing submitted yet';\n"
     "    })();",
     "the student's on-time counts. `!h.late` counted every unknown as on "
     "time, and \"Every deadline met\" was then printed over a history in "
     "which no deadline was recorded at all."),

    ("          { label: 'On time', value: String(stOnTime), sub: stTimeSub "
     "},",
     "          { label: 'On time', value: MRB_ONTIME_VALUE(stOnTime, "
     "stLate),\n"
     "            sub: stTimeSub },",
     "the student screen's On-time tile. Same shape as the marking screen's: "
     "a bare count that is 0 when nothing is known."),

    ("""    const dgLate = Math.max(0, dgMarkedSub - dgOnTime);
    const dgOnPct = dgMarkedSub ? Math.round((dgOnTime / dgMarkedSub) * 100) : 0;""",
     "    const dgLate = liveClasses.reduce((a, c) => a + "
     "this.matrixFor(c).markedLate, 0);\n"
     "    const dgUnknown = liveClasses.reduce((a, c) => a + "
     "this.matrixFor(c).markedLateUnknown, 0);\n"
     "    const dgKnown = dgOnTime + dgLate;\n"
     "    const dgOnPct = dgKnown ? Math.round((dgOnTime / dgKnown) * 100) "
     ": null;",
     "the digest's cross-class lateness. `markedSub - markedOnTime` folds "
     "every unknown into LATE, and dividing by `markedSub` counts them "
     "against the on-time percentage as well — the same population "
     "mis-stated twice in one line, in the number a head of department "
     "reads first."),

    ("        { label: 'On time', value: dgOnPct + '%', sub: dgLate + ' late "
     "of ' + dgMarkedSub + ' marked submissions' },",
     "        { label: 'On time',\n"
     "          value: dgOnPct == null ? '—' : dgOnPct + '%',\n"
     "          sub: MRB_ONTIME_SUB(dgOnTime, dgLate, dgUnknown,\n"
     "                              'marked submissions') },",
     "the digest's On-time tile, over the corrected counts."),

    ("""        stacks: src.map(x => {
          const pct = x.tot ? Math.round((x.on / x.tot) * 100) : 0;
          return { label: x.label, sub: x.sub, right: pct + '% · ' + (x.tot - x.on) + ' late',
            segs: [{ pct, fill: 'var(--ks3-ok)' }, { pct: 100 - pct, fill: 'var(--st-accent)' }] };
        }),""",
     "        stacks: src.map(x => {\n"
     "          /* No known deadline anywhere in this row is not 0% on time.\n"
     "             Left as Design drew it the bar renders 100% accent, which\n"
     "             is the bar for a class where everybody was late. */\n"
     "          if (!x.tot) {\n"
     "            return { label: x.label, sub: x.sub,\n"
     "              right: '— · timing not recorded',\n"
     "              segs: [{ pct: 100, fill: 'var(--st-rule-soft)' }] };\n"
     "          }\n"
     "          const pct = Math.round((x.on / x.tot) * 100);\n"
     "          return { label: x.label, sub: x.sub, right: pct + '% · "
     "' + (x.tot - x.on) + ' late',\n"
     "            segs: [{ pct, fill: 'var(--ks3-ok)' }, { pct: 100 - pct, "
     "fill: 'var(--st-accent)' }] };\n"
     "        }),",
     "a row of the on-time chart with no recorded deadlines. `tot` is the "
     "KNOWN population since the earlier ruling, so a row of unknowns is "
     "`tot === 0` and drew a full late bar labelled 0%."),

    ("        tiles: [tile('On time', (tot ? Math.round((on / tot) * 100) : "
     "0) + '%', 'Of ' + tot + ' marked submissions'), tile('Late', tot - on, "
     "'Still marked'), tile('Open work', 'Excluded', 'Not due yet')],",
     "        tiles: [tile('On time', tot ? Math.round((on / tot) * 100) + "
     "'%' : '—',\n"
     "                     tot ? 'Of ' + tot + ' with a recorded deadline'\n"
     "                         : 'No marked submission has a recorded "
     "deadline'),\n"
     "                tile('Late', tot ? tot - on : '—', 'Still "
     "marked'),\n"
     "                tile('Open work', 'Excluded', 'Not due yet')],",
     "the on-time chart's own tiles. `0%` of `0 marked submissions` when "
     "nothing is known, and a Late count of 0 beside it."),

    ("        note: worst ? 'Weakest: ' + worst.label + ' at ' + (worst.tot ? "
     "Math.round((worst.on / worst.tot) * 100) : 0) + '% on time' : '' };",
     "        note: (worst && worst.tot) ? 'Weakest: ' + worst.label + ' at "
     "' + Math.round((worst.on / worst.tot) * 100) + '% on time' : '' };",
     "the on-time chart's caption. With no recorded deadlines anywhere it "
     "named a class and said it was at 0% on time."),

    # ══ the Set-work sheet's leftovers ══════════════════════════════════
    ("""    const swSel = s.swClasses;
    const swStudents = this.CLASSES.filter(c => swSel.indexOf(c.id) > -1).reduce((a, c) => a + c.n, 0);
    const topic = this.TOPICS.filter(t => t.id === s.swTopic)[0] || this.TOPICS[0];

""",
     "",
     "three locals only the Set-work keys read. `topic` reads `this.TOPICS`, "
     "which is deleted, so this is not tidying — left in place it throws at "
     "mount on all seven pages."),

    ("      sw1: s.swStep === 1, sw2: s.swStep === 2, sw3: s.swStep === 3,\n",
     "",
     "`sw2` and `sw3`, on the same physical line as `sw1`, so `DROP_KEYS` — "
     "which works one balanced key at a time — cannot take them."),
)


# ── the assertion that proves no invented number survived ────────────────
#
# ⚑ THIS IS THE CHECK THE WHOLE PORT TURNS ON. Every mark, percentage,
# submission count and chart column in Design's delivery comes out of `rnd()`,
# which comes out of `seed()`. If either is still being called after the
# rewrites, a real teacher's dashboard is showing at least one hashed number,
# and nothing about the page would look wrong.
#
# ⚠️ `seed` IS NOT DELETED, AND THE BRIEF SAYS IT SHOULD BE. Deleting it breaks
# `hueFor`:
#
#     hueFor(name) { return this.HUE[this.seed(name) % this.HUE.length]; }
#
# — which the brief ALSO lists, correctly, among the methods that are Design's
# derivation and stay verbatim. The two instructions cannot both be followed,
# and the reason they conflict is that `seed` does two different jobs: it
# invents NUMBERS (through `rnd`) and it picks a stable AVATAR COLOUR from a
# name. The first is fiction; the second is a hash of a real string and is
# what stops a child's avatar changing colour between two screens.
#
# So `rnd` is deleted outright and `seed` survives with exactly one caller.
# Asserted rather than trusted: `rnd(` must appear NOWHERE, and `this.seed(`
# exactly once. A second caller means somebody has started inventing numbers
# again.
SEED_GUARD = dict(
    forbidden=("this.rnd(", "  rnd(key, lo, hi)"),
    seed_callers=1,
    why="`rnd` invents every number in Design's delivery; `seed` also backs "
        "`hueFor`, which is derivation and stays.",
)


# ── live regions Design drew no counterpart for ──────────────────────────
#
# ⚑ THE RULE IS "LIVE LOGIC WINS, DESIGN'S PRESENTATION WINS", and these are
# the regions where there is no Design presentation to win. They are lifted
# VERBATIM out of the hand-written page, by element id, and emitted into the
# ported page inside a hidden wrapper, so the port DELETES NOTHING a teacher
# can currently reach.
#
# ⚠️ THEY ARRIVE WITHOUT THE HAND-WRITTEN PAGE'S CSS, AND THAT IS DELIBERATE
# RATHER THAN AN OVERSIGHT. Each original carries a ~600-line `<style>` block
# that opens `* { box-sizing: border-box; margin: 0; padding: 0 }` and
# `body { display: none }`. Emitting it alongside Design's stylesheet would not
# "keep the live styling" — it would reset Design's own page out from under it.
# So the markup is carried and the styling is not, and these regions are a
# SAFETY NET rather than a finished surface: `shared/teacher-live.js` renders
# its own states through Design's presentation and should reach for these only
# where Design drew nothing at all.
#
# `{page: ((element id, why), …)}`. Every id must be found EXACTLY ONCE in the
# original, or the build stops — an id that has been renamed silently carries
# nothing, and a region that silently carries nothing is a deleted error state.
LIVE_REGIONS = {
    "classes.html": (
        ("state-empty", "\"No classes yet\", for a teacher a school admin has "
                        "not added to anything. teacher-live.js has its own "
                        "sentence for this (`SAY.noClasses`); the markup is "
                        "kept because Design drew neither."),
        ("state-error", "\"Couldn't load your classes\", with a Refresh "
                        "button. Design's file cannot fail to load."),
        ("year-band", "the read-only banner shown while a PAST academic year "
                      "is open. MRB-261's ruling: a past year is read-only "
                      "and must SAY so."),
        ("year-switch", "the academic-year switcher. ⚠️ Design drew HALF of "
                        "it — node 84 \"Viewing 2026–27\" and node 86 "
                        "\"Previous years\" are the same control's face — but "
                        "drew no LIST behind the button, so `pastYears` in "
                        "Design's logic only toasts \"2025–26 is read-only\". "
                        "The list is what makes it a control."),
    ),
    "class-detail.html": (
        ("state-not-found", "the class does not exist."),
        ("state-not-authorised", "⛔ THE ONE THAT MATTERS MOST. The class "
                                 "exists and this teacher does not teach it. "
                                 "Design has no concept of a class you may "
                                 "not see."),
        ("state-error", "the load failed."),
        # ── ⊕ RULED, MRB-287 · THE LEADERBOARD IS A STUDENT FEATURE ──
        #
        # `leaderboard-section` WAS AN ENTRY HERE, and it was removed on
        # 24 Aug 2026. It read: "the class leaderboard. Design drew NO
        # counterpart anywhere in the delivery — this is a deletion Design
        # may not have intended, and it is in the report." It went in the
        # report, Mide read it, and ruled the other way: the Stars
        # leaderboard is a STUDENT feature and is never a teacher one.
        # Design's delivery was right to draw no counterpart.
        #
        # ⚠️ WHAT GOES IS AN ORPHANED HIDDEN ELEMENT, NOT A WORKING
        # CONTROL. The section was carried into the port and then never
        # filled: `shared/teacher-live.js` does not contain the word
        # "leaderboard" once, so nothing has ever rendered into it. No
        # teacher could reach it. The rule this whole block exists to
        # protect — "the port DELETES NOTHING a teacher can currently
        # reach" — is therefore not weakened by removing it.
        #
        # The STUDENT leaderboard is untouched and stays exactly where it
        # is: the `class_stars_leaderboard_for_member` RPC, read by
        # `shared/student-data.js`. Nothing student-side changed.
        ("compose-error", "the shoutout composer's validation message. "
                          "Design's composer cannot fail to send."),
        ("shoutouts-loadmore", "pagination on the shoutout feed. Design's "
                               "feed is two entries long and needs none."),
    ),
    "student-detail.html": (
        ("state-not-found", "the student does not exist."),
        ("state-not-authorised", "⛔ the student exists and is not this "
                                 "teacher's to look at."),
        ("state-error", "the load failed."),
    ),
    # ⛔ NO `import.html` ENTRY, AND THAT IS THE RULING RATHER THAN AN
    # OVERSIGHT. This file used to list nine regions for it — `dropzone`,
    # `file-input`, `parse-error`, `preview-card`, `screen-2`,
    # `screen2-validation`, `dryrun-error`, `issues-card`, `success-panel` —
    # and carrying nine elements out of a 2,000-line wizard is what a live
    # region is NOT for: it lifts markup, by id, without the script that
    # drives it. The whole page is hand-written again (see
    # `IMPORT_NOT_PORTED`), so all nine are live in their own file, with
    # their own engine and their own stylesheet.
}
