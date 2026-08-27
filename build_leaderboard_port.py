"""build_leaderboard_port.py — Design's KS4 Weekly Leaderboard, ported.

MRB-290.  Emits `leaderboard.html` into BOTH trees (`mrbadmus_site/` and the
repo root mirror), plus a driveable fixture set into `leaderboard_fixtures/`.

⚑ THE DELIVERY IS A SAMPLE, AND THE EVIDENCE IS IN ITS OWN CONSTANTS.

`docs/ks3/design-reference/leaderboard/source/KS4 Weekly Leaderboard.dc.html`
carries `FIRST` (30 tokens) and `LAST` (20), and derives sixty invented
handles from them with `FIRST[i] + LAST[(i*7+off)%20] + (21+((i*13+off)%58))`.
`VIEWER` is `'AmberYew12'`, typed. Every mark is `rng(hash(week|tier|subject|
name))`, every rank a sort over those, every week nine of them counted back
from the device clock. There is no data layer, no fetch, no empty state driven
by anything but a literal.

So the pre-ruled SAMPLE branch applies: Design's presentation grafted onto
real reads, and NOTHING Design invented as data ships.

⚠️ THE SAMPLE HANDLES ARE NOT SAFELY DISTINGUISHABLE BY SHAPE, and that is
this delivery's version of MRB-287's "Design's sample classes are not named
fictionally". Real MrBadmusAI usernames are generator-built from the SAME
vocabulary — `FoxWave36`, `WolfSummit53`, `FalconGlide41` are real students
and `FoxWave21`, `WolfCrest86`, `FalconSpark34` are Design's. A gate that
looked for "a capitalised word, a capitalised word and two digits" would fire
on every real student on the board. `leaderboard_tells.py` therefore derives
the sixty-one EXACT strings from the delivery's own constants at run time and
pins those. (Checked 25 Aug 2026: zero collisions between the derived
sixty-one and the live board.)

── What is replaced, and what is Design's, verbatim ──────────────────────

REPLACED — the fabricators:  `FIRST`, `LAST`, `VIEWER`, `WEEKS`, `LIVE`,
`roster`, `entered`, `seed`, `streak`, `raw`, `board`, `weekDates`.

VERBATIM — the presentation:  `deco()` in full, the podium, the rail, the
row grid, the expanded breakdown, `PAPERS`, `KEYS`, `SUBJ_KEY`, `CONFETTI`,
`MON`, `clamp`, `initialsOf`, `fmtTime`, `isoWeek`, and the whole of
`renderVals` apart from the ruled expressions listed in `RULINGS` below.

`hash` and `rng` are KEPT — and only because Design's confetti is the sole
remaining caller. That is the same allowance `teacher_tells` makes for
`seed(` in `hueFor`, for the same reason: banning it outright would force the
port to re-implement an identical PRNG under another name to pass a gate.
`leaderboard_tells.py` asserts the caller count is one.

── The seam ──────────────────────────────────────────────────────────────

`shared/leaderboard-live.js`, and nothing else. It fetches
`GET /api/weekly-leaderboard/board` and returns real rows in Design's own
ten-field shape — {name, rank, pct, marks, total, secs, per, done, move,
streak} — so Design's arithmetic runs unmodified on top of them.

⚠️ THE ENDPOINT IS NARROW ON PURPOSE. It returns the top ten plus the
viewer's own row, and precomputes `entries`, `median_pct`, `fastest_secs`,
`biggest_climb` and `cut_pct` over the FULL board server-side. The client
never sees the cohort. Design's aggregate block computes all five FROM
`board`, which here is at most eleven rows — so every one of them is ruled
out and read from the payload instead. See R20/R21.

── Order ─────────────────────────────────────────────────────────────────

AFTER `generate_site_v5.py`, exactly as the two student steps and the teacher
step are, and for the same reason: the KS4 generator rmtree's
`mrbadmus_site/` on the way in. It also copies the root `leaderboard.html`
into `mrbadmus_site/` through its own `_auth_file` list — so this build must
run afterwards and overwrite BOTH trees, which is what it does.
"""

import base64
import hashlib
import html
import json
import os
import re
import subprocess
import sys

# One stamping scheme, four writers. See build_teacher_port.py's note.
from build_ks3 import stamp_versions

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "leaderboard")
SRC = os.path.join(REF, "source", "KS4 Weekly Leaderboard.dc.html")

DS = os.path.join(REF, "source", "_ds",
                  "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")

# ⚠️ THE PAGE IS AT THE SITE ROOT, not in a subdirectory, because that is the
# URL students already have — `/leaderboard.html` is linked from the nav of
# every page on the site and from the KS4 index. Moving it to give the port a
# tidier home would break every one of those links and every bookmark.
SITE_OUT = "mrbadmus_site"
MIRROR_OUT = "."
OUT_NAME = "leaderboard.html"

# ⚑ OUTSIDE EVERY PUBLISHED TREE, AND THIS IS THE §7 LESSON OF MRB-287.
#
# The fixtures carry Design's sixty-one invented handles. `generate_site_v5`
# publishes and ROUND-TRIPS `shared/`, `teacher/` and `student/`; the teacher
# port learned the hard way that withholding files from one of those either
# fails at the next generator run or — worse — deletes them from source. A
# directory the generator has never heard of is neither published nor
# round-tripped, so nothing has to be excluded, ignored or silenced.
#
# ⛔ NEVER ADD AN IGNORE RULE TO A COPYTREE TO MAKE THIS WORK. That is what
# went wrong twice on 24 Aug 2026, and the second attempt silenced the guard
# that would have reported the first.
FIXTURE_OUT = "leaderboard_fixtures"
SHARED_OUT = os.path.join("mrbadmus_site", "shared")
SHARED_SRC = "shared"
RETIRED = os.path.join("docs", "ks3", "retired")
RETIRED_NAME = "leaderboard-2026-08-25-retired.html"

TEMPLATES = "student_templates.json"
TPL_KEY = "leaderboard"

DS_CSS_NAME = "leaderboard-ds.css"
DS_CSS_URL = "/shared/" + DS_CSS_NAME
SERVED_FONTS = "/shared/fonts/"

RUNTIME_JS_NAME = "student-runtime.js"
LIVE_JS_NAME = "leaderboard-live.js"
LIVE_JS_URL = "/shared/" + LIVE_JS_NAME

# The nav's own dependencies, loaded exactly as the retired page loaded them.
# ⚠️ `class-entry.js` BEFORE anything that uses it (CLAUDE.md, MRB-267).
NAV_DEPS = ("tokens.css", "nav.css", "search-index.js", "search.js",
            "nav.js", "class-entry.js")

STAMPED_DEPS = NAV_DEPS + (LIVE_JS_NAME,)

# Design's four editor props, pinned. R27.
PINNED_PROPS = dict(density="comfortable", topCount=10,
                    showPodium=True, showWeekTops=True)


def asset_hash(text):
    if isinstance(text, str):
        text = text.encode("utf-8")
    return hashlib.md5(text).hexdigest()[:8]


# ══════════════════════════════════════════════════════════════════════════
#  THE RULINGS REGISTER
#
#  Every edit this build makes to Design's delivery, with its reason. Nothing
#  is changed that is not on this list, and every entry is APPLIED AND
#  COUNTED — a ruling that matches nothing stops the build, because a seam
#  that silently matched nothing leaves the page reading its marks from
#  Design's imagination while every gate stays green.
# ══════════════════════════════════════════════════════════════════════════

RULINGS = []


def rule(rid, what, why):
    RULINGS.append(dict(id=rid, what=what, why=why))
    return rid


rule("R1", "Design's whole <nav> (source lines 38-57) is removed at compile "
           "time and the live landing page's nav is emitted as static page "
           "shell instead.",
     "MIDE'S OVERRIDE, 25 Aug 2026. Design drew a 1180px-inset nav with a "
     "'My class' link and her own brand mark; the live nav is full-bleed, has "
     "a search control, an auth area and a burger drawer. Two further facts "
     "make the replacement structural rather than cosmetic: (a) the mark in "
     "Design's nav is `MrBadmusDS.BrandMark`, the STUDENT-surface chevron, "
     "and `/leaderboard.html` is an external/public root page, which "
     "CLAUDE.md's four brand presentations say takes the gold-to-rust "
     "two-chevron + wordmark; (b) the runtime EMPTIES ITS HOST on every draw "
     "(`host.textContent = ''` in student-runtime.js), so a nav inside the "
     "host would be destroyed and rebuilt on every tier press — and nav.js "
     "binds its drawer, its auth area and its outside-click handler ONCE. "
     "The nav therefore lives outside the mount point entirely. This also "
     "removes the delivery's only <x-import>, which is what lets "
     "`capture_imports` succeed against a delivery that ships no standalone."),

rule("R2", "Every text node whose value is exactly 'AY' becomes the "
           "expression `me.initials`. Exactly two are expected once the nav "
           "has gone (Design's standing card, source line 70; her pinned "
           "row, line 291).",
     "'AY' is the ONLY hard-typed identity left in the markup — the monogram "
     "of `VIEWER = 'AmberYew12'`. Left literal it ships one invented "
     "student's initials to every real viewer, inside a card headed YOUR "
     "STANDING. Bound to `me.initials` it is reactive and uses Design's own "
     "`initialsOf`, so nothing is retyped."),

rule("R3", "`const VIEWER` is dropped; its three use sites become "
           "`MRB_IS_YOU(x.name)` (deco), `MRB_ME()` (the me-row lookup) and "
           "`MRB_VIEWER_NAME()` (the not-entered fallback).",
     "A module const is evaluated when the script parses, which is BEFORE "
     "the Supabase session resolves — so `const VIEWER = MRB_VIEWER_NAME()` "
     "would be the empty string on every load, for ever, and silently. The "
     "three call sites are evaluated at render time and are correct. "
     "`MRB_IS_YOU` also guards truthiness: signed out the viewer name is '', "
     "and `'' === x.name` would badge an unnamed row as YOU."),

rule("R4", "`WEEKS` and `LIVE` are dropped. The live week list is whatever "
           "the payload carries and `LIVE` is the index whose `is_current` "
           "is true.",
     "MEASURED, NOT ASSUMED, 25 Aug 2026: the backend returned TEN weeks for "
     "Higher/Overall, six for Foundation/Overall, four for "
     "Foundation/Biology and three for Foundation/Physics — and the Higher "
     "list has a two-month hole between 8 May and 3 July. A fixed nine and a "
     "`LIVE = WEEKS - 1` are both false, and the second is false in the "
     "direction that looks fine: it would point at the last week in the "
     "array, which usually IS the current one."),

rule("R5", "`FIRST` and `LAST` are dropped.",
     "The sixty-handle sample roster. This is the data inventor."),

rule("R6", "`roster`, `entered`, `seed` and `streak` are dropped.",
     "`roster` fabricates the cohort, `entered` and `seed` fabricate who sat "
     "and what they scored, `streak` walks backwards through `entered` to "
     "invent a run. Every one of them is replaced by a real column: `streak` "
     "arrives per row on the payload."),

rule("R7", "`raw(w)` returns the mapped rows for the SELECTED week and `[]` "
           "for any other; `board(w)` returns those rows unchanged.",
     "Design's `board` decorated `raw` with `move`/`was`/`streak` computed "
     "by diffing against the previous week's `raw`. All three arrive on the "
     "payload — the backend has the whole cohort and can rank it; the client "
     "has ten rows and cannot. `raw` is only ever called for the selected "
     "week because its one other caller is ruled out at R9."),

rule("R8", "`weekDates()` is replaced: ranges are derived from each week's "
           "`week_start` (+6 days), and the ISO week number from that same "
           "Friday.",
     "REAL WEEKS RUN FRIDAY → THURSDAY and `week_start` is always the "
     "Friday (verified across every week the backend returns). Design counts "
     "back from the device's current MONDAY, which is wrong by four days, "
     "wrong about which weeks exist, and derived from a clock the student "
     "controls. The 'W34' label survives and is honest: the ISO week of a "
     "Friday is the ISO week that Friday falls in."),

rule("R9", "In the week strip, `const top = this.raw(i)[0]` becomes "
           "`MRB_TOP(i)`, reading that week's `top_pct`.",
     "Only the selected week's board is ever fetched. Design's version needs "
     "every week's full board to draw ten mini-bars; `top_pct` arrives on "
     "every week of every payload for exactly this purpose, and is null on a "
     "week nobody has sat — which Design's own `top ? … : '\\u2014'` already "
     "handles."),

rule("R10", "`const s = this.state` becomes `const s = MRB_STATE(this)`.",
      "ONE LINE, AND IT FIXES A WHOLE CLASS OF BUG. Design addresses a week "
      "by INDEX into a fixed nine. The real weeks array CHANGES WITH THE "
      "SUBJECT (R4), so an index is not stable across a subject press: index "
      "3 is 17 July before the press and 24 July after it, and the board "
      "would quietly show a different week than the one highlighted. "
      "Selection is therefore held in the seam as a DATE and the index Design "
      "wants is derived per payload. Every downstream `s.tier`, `s.subject` "
      "and `s.wk` in `renderVals` is then correct with no further edit."),

rule("R11", "The three `onSelect` closures call `MRB_SET({...})` for the "
            "axis they change, and keep Design's own `flip`/`open` setState.",
      "The counterpart to R10: selection lives in the seam, so the presses "
      "that change it must reach the seam. `flip` and `open` are genuinely "
      "the component's and stay there."),

rule("R12", "`componentDidMount`'s countdown interval is guarded on "
            "`MRB_IS_CURRENT()` rather than `this.state.wk === LIVE`. "
            "Design's rail scroll-snap is kept verbatim.",
      "`LIVE` is gone (R4). `is_current` is the payload's own answer and "
      "survives a subject change that reindexes the array."),

rule("R13", "The aggregate block (source lines 519-529: `cut`, `pcts`, "
            "`median`, `fastest`, `climb`, `live`, `ms`, `d`, `h`, `mi`, "
            "`sec`) is replaced wholesale, and additionally defines "
            "`entries`. It reads `cut_pct`, `median_pct`, `fastest_secs`, "
            "`biggest_climb`, `entries`, `is_current` and `closes_at`.",
      "THE CLIENT NEVER SEES THE COHORT. The endpoint returns the top ten "
      "plus the viewer, and precomputes all five statistics over the full "
      "board server-side — so every one of Design's five, computed FROM "
      "`board`, would be computed over at most eleven rows. A median of ten "
      "top scorers is not the cohort's median and would read as one. The "
      "countdown is additionally re-anchored: `closes_at` minus a "
      "SERVER-anchored now, not `dates[LIVE].end` at 23:59 local, because "
      "the real round closes at 09:15 UTC on the following Friday and a "
      "device clock a day fast must not be able to close it early."),

rule("R14", "The three remaining `board.length` in `renderVals` become "
            "`entries`. Exactly three, asserted.",
      "The same fact as R13 seen at the three places a student reads it: the "
      "ENTRIES tile, the 'N SAT THIS WEEK' cut line, and the percentile in "
      "the standing card. `board.length` is at most eleven, so a week eighty "
      "students sat would have printed ENTRIES 10."),

rule("R15", "The MEDIAN SCORE tile's `value: median + '%'` gains a null "
            "branch and renders an em dash.",
      "`median_pct` IS NULL ON AN EMPTY WEEK, and this is the live landing "
      "state today: on 25 Aug 2026 Higher/Overall's current week had zero "
      "entries. `null + '%'` renders the string 'null%' — one of the exact "
      "tells `leaderboard_behaviour.py` fails on. Blanks over invented "
      "numbers."),

rule("R16", "`const listStart = podiumOn ? 3 : 0` becomes "
            "`const listStart = podium.length >= 3 ? 3 : 0`.",
      "A DEFECT, FOUND WITH REAL DATA AND NOT BY ANY GATE. Design's podium "
      "`sc-if` is `podiumOn && podium.length >= 3`, but `listStart` consults "
      "the PROP alone. With one or two entrants the podium is correctly "
      "hidden and the list still starts at index 3 — so `qualified.slice(3)` "
      "is empty and THE BOARD DRAWS NO ROWS AT ALL. Foundation's current "
      "week has exactly one entry today, so this is not a corner: it is what "
      "a Foundation student would have seen on the day this shipped."),

rule("R17", "`cutValue` gains a middle branch: a cut line when there is one, "
            "'ALL n LISTED' when everybody who sat is on the board, and "
            "Design's 'NO ENTRIES' only when nobody sat.",
      "`cut_pct` is null whenever FEWER THAN `topCount` sat, not only when "
      "nobody did — measured: Foundation's current week, one entry, "
      "`cut_pct` null. Design's two-branch version would print 'NO ENTRIES' "
      "on a week somebody entered, under a row bearing that person's name."),

rule("R18", "The not-entered `me` fallback object takes "
            "`name: MRB_VIEWER_NAME()` and gains `initials: ''`.",
      "`name: VIEWER` is R3. The `initials` key is new because R2 binds two "
      "monograms to `me.initials` and Design's fallback has no such key — a "
      "signed-out visitor would have read 'undefined' in the YOUR STANDING "
      "card and again in the pinned row."),

rule("R19", "LOADING is a state: until the first payload for a selection "
            "arrives, the rows are empty, the four tiles read an em dash and "
            "the cut line reads 'LOADING'.",
      "Design's component is synchronous and a sample never waits. A real "
      "fetch does — against a cold Render dyno, for tens of seconds. Design's "
      "own README says empty states are states, not blanks, and a page that "
      "silently draws zero entries while it is still asking is a blank that "
      "claims to be an answer."),

rule("R20", "ERROR is a state: the cut line reads 'COULD NOT LOAD', the "
            "tiles read an em dash, and every control stays live.",
      "Same reason as R19, and the controls stay live deliberately — a "
      "press re-selects, which re-fetches, so the retry is the page rather "
      "than a reload."),

rule("R21", "A subject is in `done` only if its `per` value is non-null.",
      "Applied in the seam. Design's `breakdown` renders `x.per[k] + '%'` "
      "for every key in `done` and has no null branch, and the endpoint can "
      "return that pairing — which would put the literal 'null%' in the "
      "copy."),

rule("R22", "`density`, `topCount`, `showPodium` and `showWeekTops` are "
            "pinned as constants and no control renders them.",
      "They are Design's EDITOR props, not user controls — the delivery's "
      "`data-props` blob types them as an enum, an int and two booleans for "
      "the canvas's properties panel. Shipping them as controls would be "
      "four dead switches; shipping them as props with no control is what "
      "Design's own `?? ` defaults already do."),

rule("R31", "The body container's `max-width: 1180px` is removed. The "
            "gutters Design drew (`padding: 30px 28px 96px`) and her "
            "`margin: 0 auto` both stay.",
      "MIDE'S OVERRIDE OF DESIGN, RULED 25 AUG 2026 after using the live "
      "page signed in as WolfBeam — the same class of ruling as the nav "
      "(R1), and recorded the same way. His words: \"fill the whole page, "
      "or at least leave very little space by the two sides.\" On a wide "
      "monitor Design's cap left the board floating in the middle of the "
      "screen with the table columns squeezed. Everything inside is grid or "
      "flex — the podium is a three-column grid, the stats a four-column "
      "grid, the rail a flex row that scrolls, the table rows a grid keyed "
      "off `grid` — so all four stretch on their own once the cap is gone. "
      "⚠️ THE CAP IS REMOVED AND NOTHING IS ADDED: no new max-width, no new "
      "breakpoint, no re-tuned column list. `margin: 0 auto` is kept "
      "deliberately, so if anyone ever reinstates a cap the block still "
      "centres rather than sticking to the left edge."),

rule("R34", "The PODIUM FRAME ALONE is capped at 1140px and centred "
            "(`max-width` + `margin-left/right: auto` on the element R31's "
            "cap used to sit above), and the type inside it scales up ~1.25x: "
            "rank numerals 86/56/48 → 108/70/60, percentages 32/24 → 40/30, "
            "marks lines 15/14 → 17/16, names 30/22 → 32/24, step min-heights "
            "212/148/116 → 265/185/145. Nothing outside the frame is touched: "
            "the stats grid, the week rail and the ranked table keep R31's "
            "full-bleed width.",
      "MIDE'S RULING, 27 AUG 2026, AND IT RULES BOTH PREVIOUS STATES WRONG. "
      "Design centred the WHOLE page at 1180px with small type; R31 removed "
      "that cap outright on his instruction to fill the screen. Both readings "
      "were right about the table and wrong about the podium. The table wants "
      "the width — nine columns of rank, name, papers, move, score, marks and "
      "time are what got squeezed at 1180px and what R31 was for. The podium "
      "does not: it is three columns of one number each, so on a 2560px "
      "monitor R31 stretched a champion's step to nearly a metre of empty "
      "gradient with 86px of numeral marooned in the middle of it. A frame "
      "is a frame — it should look like an object on the page, not like the "
      "page. ⚠️ R31 IS NOT REVERSED AND MUST NOT BE. The cap added here is on "
      "the podium's own border-radius frame (source line 137), which is "
      "INSIDE the body container R31 uncapped; re-capping the body would "
      "squeeze the table again and this ruling would have traded one of "
      "Mide's complaints for the other. "
      "⊕ The type is the second half of one ruling, not a separate one. "
      "Design's sizes were drawn for a 1180px page and read small; capping "
      "the frame without enlarging them would have left the same small type "
      "in a narrower box, which is Design's original state with extra steps. "
      "1.25x is the factor at which the champion's numeral reads at arm's "
      "length from a classroom board without the three steps crowding. "
      "⊕ THE STEP HEIGHTS ARE SCALED BY THE SAME FACTOR, and that is "
      "load-bearing rather than taste: `min-height` is a MINIMUM, so the "
      "enlarged content overflows it — place 2's contents measure ~152px "
      "against Design's 148 and place 3's ~139 against her 116. Left alone, "
      "the steps would have re-sorted themselves to their content and "
      "Design's deliberate 1-2-3 staircase would have flattened to 212/152/"
      "139. Scaling all three keeps her ratio exactly, and it is her ratio "
      "that says which place won."),

rule("R32", "When a podium student is the viewer, Design's OWN `YOU` chip "
            "is cloned out of her table row and inserted after the podium "
            "name, guarded by that place's `isYou`. Three insertions, one "
            "per podium slot.",
      "MIDE'S RULING, 25 AUG 2026, FROM USING THE PAGE: he was rank 2 and "
      "nothing on the board said so. Design's chip exists only on table "
      "rows and the pinned row — and the pinned row only renders when the "
      "viewer is OUTSIDE the top ten — so a viewer who reaches the podium "
      "loses their marker at exactly the moment it is most worth having. "
      "⚠️ THE CHIP IS CLONED FROM HER TREE, NOT RETYPED. It is a deep copy "
      "of the `sc-if r.isYou` subtree with the expression rewritten to "
      "`p1/p2/p3.isYou`, so the mono face, the letter-spacing, the accent "
      "ground and the 4px radius are literally the same bytes. Retyping a "
      "style string is how two things that must match stop matching, "
      "quietly, six months later. `deco` already computes `isYou` for every "
      "row it decorates and the podium is `board.slice(0,3).map(deco)`, so "
      "no new logic is needed at all — only the markup Design already drew, "
      "in one more place."),

rule("R33", "The week rail follows the SELECTION: when the selected week "
            "changes, the rail scrolls the selected chip into view; when it "
            "has not changed, R28's preserve-the-scroll behaviour stands.",
      "MIDE'S RULING, 25 AUG 2026: clicking a past week loaded that week's "
      "board but left the rail scrolled to the oldest end, so he had to "
      "hunt back for where he was. "
      "⚠️ R28 WAS AIMING AT THE WRONG TARGET AND THIS SUPERSEDES ITS "
      "BEHAVIOUR WITHOUT DELETING IT. Preserving the previous `scrollLeft` "
      "is right for a redraw that does not move the selection — a countdown "
      "tick, a filter press that keeps the week, a student browsing the "
      "strip who must not be yanked back. It is wrong for a redraw that "
      "DOES move it, where the honest answer is to show what was just "
      "chosen. The two cases are now distinguished by tracking the "
      "last-snapped `week_start`, so both behaviours coexist instead of one "
      "overwriting the other. "
      "⊕ The initial load is the same code path and needs no special case: "
      "the selected week IS the current week, its chip is the rightmost, "
      "and scrolling it into view lands exactly where Design's mount snap "
      "put it. And it scrolls only when the chip is actually out of view, "
      "so a selection change that is already visible moves nothing."),

rule("R30", "While the payload is not `ok`, the board footer's left label "
            "drops its '· N SAT THIS WEEK' clause entirely, and the "
            "countdown pill renders an em dash instead of LOCKED or "
            "CLOSES IN.",
      "TWO DEFECTS FOUND BY SCREENSHOTTING THE LIVE PAGE MID-LOAD against a "
      "cold Render dyno — a window that lasts seconds in the wild and that "
      "NO FIXTURE COVERED, because every fixture hands the seam a settled "
      "payload. "
      "(1) `cutLabel` interpolated `entries` unconditionally, so while the "
      "payload was null a student read 'TOP 10 ONLY · null SAT THIS "
      "WEEK' — the literal string `null` as body copy. The clause is DROPPED "
      "rather than dashed: a clause whose only content is a fact we do not "
      "have has no place in the sentence, and 'ALL — SAT THIS WEEK' "
      "would be the same defect wearing a nicer character. "
      "(2) `closeLabel`'s not-live branch fires whenever `is_current` is "
      "false, which an empty payload also satisfies — so the pill told a "
      "student the week was LOCKED when it was merely loading. That is "
      "MRB-287's 'ON TIME 0' exactly: unknown rendered as one of the two "
      "real answers. Unknown is neither, and an em dash is what neither "
      "looks like everywhere else on this page. "
      "⚠️ The pill's colours already read correctly for this state and are "
      "NOT touched: `live` is false while loading, so Design's own muted "
      "locked palette (crumb ground, rule border, no pulse) is already the "
      "neutral presentation. Only the label lied."),

rule("R29", "The Node evaluation environment pins a fixed reference date "
            "(`2026-08-25T12:00:00Z`, TZ=UTC) before Design's unmodified "
            "logic runs.",
      "THE CLOCK BELONGS TO THE HARNESS, NOT TO HER LOGIC — a harness "
      "property like the viewport, not an edit to the delivery. Design's "
      "`weekDates()` counts nine weeks back from the device's current "
      "Monday, so evaluating her sample on Tuesday produced different "
      "`week_start` values from evaluating it on Wednesday, and all eight "
      "fixtures plus their eight data files churned every single day. That "
      "is noise in every diff for ever, and it makes the fixtures unusable "
      "as a tracked artefact. Freezing the clock leaves her logic BYTE-FOR-"
      "BYTE UNTOUCHED and makes the output byte-deterministic on any day. "
      "TZ is pinned too, and separately: the frozen instant is absolute but "
      "`getFullYear`/`getMonth`/`getDate` are LOCAL, so without TZ=UTC a "
      "machine far enough east or west would still derive a different "
      "Monday from the same instant. "
      "⚠️ The fixture week_starts are therefore MONDAYS, and that is "
      "correct: they are Design's own sample reproduced faithfully. Do not "
      "read them as evidence about the real product's Friday→Thursday weeks "
      "— that is a property of the endpoint, handled by R8."),

rule("R28", "A `componentDidUpdate` is ADDED to Design's class, restoring the "
            "week rail's horizontal scroll position after every redraw; "
            "`renderVals` records that position while the old rail is still "
            "in the DOM.",
      "A REAL DEFECT, USER-FACING, FOUND BY THE BEHAVIOUR GATE — and it is "
      "the same defect MRB-287 §7 lists first, in the same component family. "
      "`student-runtime.draw()` does `host.textContent = ''` and rebuilds, "
      "and it preserves focus, field values and WINDOW scroll — but not an "
      "element's `scrollLeft`. So the rail was rebuilt at scroll 0 on every "
      "single state change: `componentDidMount` snaps it to the right-hand "
      "end so the current week is visible, and the first tier, subject or "
      "week press threw that away and jumped the student back to the oldest "
      "week on the rail. "
      "⚠️ HOW IT PRESENTED IS WORTH RECORDING, because it looked like a gate "
      "bug and I nearly treated it as one. The gate reported the 'scroll "
      "back' button dead and the 'scroll forward' button alive, on every "
      "scrollable fixture. That asymmetry IS the diagnosis: at scroll 0, "
      "back is clamped and does nothing while forward moves — so the pair of "
      "results could only mean the rail was at 0 at press time, which it "
      "should never have been after the mount snap. A gate that had merely "
      "been given a longer settle would have gone green and the defect would "
      "have shipped."),

rule("R27", "The two remaining readers of `LIVE` inside `renderVals`: the "
            "week strip's `const live = i === LIVE` becomes a read of that "
            "week's own `is_current`, and `goLive`'s `setState({wk: LIVE})` "
            "becomes `MRB_SET({week: <the current week's start>})`.",
      "FOUND BY SWEEPING THE BUILT PAGE FOR EVERY DROPPED NAME after R26, "
      "rather than by a gate — and the sweep is the lesson. R26 fixed the "
      "one reader that threw in the CONSTRUCTOR, which is loud: nothing "
      "renders. These two throw inside `renderVals` instead, which is loud "
      "in exactly the same way, so the behaviour gate would have caught them "
      "on the next run — but only after another full cycle. `drop_const` "
      "verifies a declaration exists and says nothing about who reads the "
      "name, so a grep of the BUILT page for each dropped identifier is now "
      "part of finishing the job. `goLive` matters twice over: it is the "
      "'This week' button, and a dead press there is the control a student "
      "reaches for after browsing history."),

rule("R26", "Design's `state` class field drops `wk`, `tier` and `subject` "
            "and keeps only `open`, `flip` and `now`.",
      "FOUND BY `leaderboard_behaviour`, WITH THE BUILD ALREADY GREEN, and "
      "it is the same shape as the trap R3 was written to avoid — I simply "
      "did not look for it twice. `state = { wk: LIVE, … }` is a CLASS FIELD "
      "INITIALISER: it runs inside the constructor, referencing a module "
      "const that R4 had deleted, so `new Component()` threw "
      "`ReferenceError: LIVE is not defined` before a single node was drawn. "
      "All eight fixtures rendered zero characters. ⚠️ NOTE WHAT DID NOT "
      "CATCH IT: `drop_const` verifies the DECLARATION exists before "
      "removing it and says nothing about who still reads the name, and the "
      "tells gate passed because a page that throws at mount carries no "
      "invented handles either. The three dropped keys are exactly the three "
      "R10 moved into the seam, so `MRB_STATE` was already ignoring them — "
      "and dropping `tier: 'Higher'` also removes Design's hardcoded tier "
      "default, which the profile-tier landing overrides anyway."),

rule("R25", "A student's `avatar_url` renders as an image INSIDE Design's "
            "own disc — as a bound `background-image` appended to the disc's "
            "style — with Design's initials monogram as the fallback when "
            "there is none. Six discs: the three podium places, the row "
            "avatar, and the viewer's own in both the standing card and the "
            "pinned row.",
      "RULED BY MIDE, 25 Aug 2026, AND IT IS THE ONE PLACE PIXEL FIDELITY "
      "GIVES WAY. Identity is frozen: a student appears under the same "
      "display name AND the same avatar as on the leaderboard they use "
      "today, and the live page renders avatar images. Design drew monogram "
      "circles and no <img> anywhere, so reporting `avatar_url` as "
      "'arrives, nothing renders it' would have shipped a redesign that "
      "silently took every student's face away. The narrowest fix that "
      "honours both: Design's disc geometry, border, size and font are "
      "untouched and no element is added — the image arrives through the "
      "`background` property the disc already has, and `initials` goes empty "
      "only when there is a face to put there. "
      "⚠️ THE URL IS SANITISED AT THE SEAM, not here: it lands in a CSS "
      "`background` shorthand, so `shared/leaderboard-live.js` REJECTS "
      "(never escapes) anything that is not a plain http(s) URL free of "
      "quotes, whitespace, parentheses and semicolons, and such a row falls "
      "back to initials. Escaping would have to be correct for the CSS "
      "tokeniser, the url() grammar and the HTML attribute at once; a "
      "missing face is a cosmetic loss and a CSS injection on a page 135+ "
      "students load is not."),

rule("R24", "`dates[s.wk]` (three reads: the week title twice, the LOCKED "
            "label once) is taken through a guarded `_wk` local, and the "
            "week title renders as empty rather than as a lone separator "
            "when there is no week to name.",
      "ANOTHER CONSEQUENCE OF R19, AND IT THROWS. Design's `dates` is nine "
      "entries counted off the device clock and can never be empty; the real "
      "one is the payload's weeks array, which is EMPTY until the first "
      "payload lands and on any failed fetch. `dates[s.wk].no` on an empty "
      "array is a TypeError thrown from inside `renderVals` — the page paints "
      "its nav and its heading and then stops, with the error in the console "
      "and nothing on screen to say so. (Design's other three `dates[LIVE]` "
      "reads are inside the aggregate block and are removed by R13.)"),

rule("R23", "`hash` and `rng` are KEPT.",
      "Their only remaining caller is Design's confetti, which is "
      "presentation and which Mide's first ruling preserves. This is the "
      "same allowance `teacher_tells` makes for `seed(` in `hueFor`: banning "
      "the primitive outright would force the port to re-implement an "
      "identical PRNG under another name purely to pass a gate. "
      "`leaderboard_tells.py` asserts the caller count is one."),


# ══════════════════════════════════════════════════════════════════════════
#  Balanced-literal surgery on Design's logic
# ══════════════════════════════════════════════════════════════════════════

def _balanced(src, start, opener, closer):
    """Index just past the `closer` matching the `opener` at `start`.

    A balanced scan and not a regex, for the reason build_teacher_port.py
    gives at length: every literal here contains its own terminator. `PAPERS`
    holds braces inside braces; `renderVals` holds four hundred characters of
    nested object literal inside a `.map()`.
    """
    depth, i, n = 0, start, len(src)
    while i < n:
        ch = src[i]
        if ch in "'\"`":
            q, i = ch, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == q:
                    break
                i += 1
            i += 1
            continue
        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if src.startswith("/*", i):
            j = src.find("*/", i)
            i = n if j < 0 else j + 2
            continue
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise SystemExit("build_leaderboard_port.py: unbalanced %r from offset "
                     "%d in Design's logic." % (opener, start))


# ⚠️ THE FABRICATORS ARE AT COLUMN ZERO, OUTSIDE THE CLASS, AND THAT IS WHY
# THIS FUNCTION EXISTS.
#
# `build_teacher_port.drop_field` anchors on `\n  NAME\s*=\s*` — TWO spaces
# of indentation, because on the teacher delivery every invented dataset is a
# CLASS FIELD (`  CLASSES = [...]`). This delivery puts all ten of its
# constants at module scope: `const FIRST = [...]` at column zero, above
# `class Component`. The teacher scanner reaches none of them, and its failure
# mode is a `SystemExit` naming a ruling that "is not in Design's logic",
# which would read as Design having renamed something rather than as the
# scanner looking in the wrong place. Two scopes, two anchors, one balanced
# scan underneath.
def drop_const(logic, name, why):
    """Delete a module-level `const NAME = …;`, found by balanced scan."""
    m = re.search(r"^const %s\s*=\s*" % re.escape(name), logic, re.M)
    if not m:
        raise SystemExit(
            "build_leaderboard_port.py: the MRB-290 seam deletes the "
            "module-level const `%s`, and Design's logic has no such "
            "declaration.\n"
            "  The ruling stands (%s). Re-anchor it: a deletion that deletes "
            "nothing is invisible, and this list is the only thing between a "
            "real student and a hashed number."
            % (name, why))
    i = m.end()
    while logic[i] in " \t\r\n":
        i += 1
    if logic[i] in "[{":
        end = _balanced(logic, i, logic[i], "]" if logic[i] == "[" else "}")
    else:
        end = i
    end = logic.index(";", end - 1 if end > i else i) + 1
    while end < len(logic) and logic[end] == "\n":
        end += 1
    return logic[:m.start()] + logic[end:]


def replace_method(logic, name, body, why):
    """Replace a class method's whole body, found by balanced-brace scan."""
    m = re.search(r"\n  %s\s*\(" % re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_leaderboard_port.py: the MRB-290 seam replaces the body "
            "of `%s()`, and Design's logic has no such method.\n"
            "  The ruling stands (%s). Skipping is not available: a seam "
            "that silently matched nothing leaves the page reading its marks "
            "from Design's imagination while every gate stays green."
            % (name, why))
    args_open = logic.index("(", m.start())
    args_end = _balanced(logic, args_open, "(", ")")
    brace = logic.index("{", args_end - 1)
    end = _balanced(logic, brace, "{", "}")
    return logic[:brace] + "{\n" + body + "\n  }" + logic[end:]


def drop_method(logic, name, why):
    """Delete a class method whole."""
    m = re.search(r"\n  %s\s*\(" % re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_leaderboard_port.py: the MRB-290 seam deletes `%s()`, and "
            "it is not in Design's logic.\n  The ruling stands (%s)."
            % (name, why))
    args_open = logic.index("(", m.start())
    args_end = _balanced(logic, args_open, "(", ")")
    brace = logic.index("{", args_end - 1)
    end = _balanced(logic, brace, "{", "}")
    while end < len(logic) and logic[end] == "\n":
        end += 1
    return logic[:m.start() + 1] + logic[end:]


def swap(logic, old, new, why, count=1):
    """Replace an exact expression, asserting how many times it occurs.

    ⚠️ THE COUNT IS THE POINT. A `str.replace` that matched nothing is the
    silent-green failure this whole file is written against, and one that
    matched four things where three were meant is worse: it edits a line
    nobody reviewed. Every expression ruling states its arity and is refused
    if the delivery does not match it.
    """
    got = logic.count(old)
    if got != count:
        raise SystemExit(
            "build_leaderboard_port.py: the MRB-290 seam expects %d "
            "occurrence(s) of\n    %s\n  in Design's logic and found %d.\n"
            "  The ruling stands (%s). Re-anchor it rather than widening the "
            "match." % (count, old.strip()[:160], got, why))
    return logic.replace(old, new)


# ══════════════════════════════════════════════════════════════════════════
#  The seam's JavaScript
# ══════════════════════════════════════════════════════════════════════════

_SEAM = """/* No number reaches this page except through here, and there is no
   fallback that invents one. Design's delivery is a SAMPLE — sixty-one
   invented handles and a hashed mark for each — so the alternative to a
   blank is a real student shown a rank that is not theirs. */
function MRB_LB(){var L=window.MrBadmusLeaderboardLive;
  if(!L)throw new Error('leaderboard: shared/leaderboard-live.js has not '
    +'loaded; there is no data source and nothing may be drawn.');
  return L;}
function MRB_STATE(c){return MRB_LB().stateFor(c);}
function MRB_D(){return MRB_LB().payload();}
function MRB_STATUS(){return MRB_LB().status();}
function MRB_ROWS(){return MRB_LB().rows();}
function MRB_ME(){return MRB_LB().me();}
function MRB_WEEKS(){return MRB_LB().weeks();}
function MRB_TOP(i){return MRB_LB().topFor(i);}
function MRB_IS_CURRENT(){return MRB_LB().isCurrent();}
function MRB_SET(p){return MRB_LB().select(p);}
function MRB_VIEWER_NAME(){return MRB_LB().viewerName();}
function MRB_VIEWER_INITIALS(){return MRB_LB().viewerInitials();}
function MRB_IS_YOU(n){return MRB_LB().isYou(n);}
/* ⚠️ SERVER-ANCHORED. `server_now` arrives with every payload and the offset
   from `Date.now()` is captured once, at first load. A device clock a day
   fast must not be able to close the round early, nor a slow one hold it
   open. */
function MRB_NOW(){return MRB_LB().now();}
function MRB_CLOSES(){return MRB_LB().closesAt();}
/* The three states a payload can be in, as the ONE label the cut line
   already had a slot for. Design drew neither loading nor error, because a
   sample never waits and never fails. */
function MRB_CUT_STATE(){var s=MRB_STATUS();
  return s==='ok'?null:(s==='error'?'COULD NOT LOAD':'LOADING');}
"""


# The four statistic tiles, rebuilt from the payload. Design's own labels and
# hues, verbatim; only the values are ruled.
_AGGREGATE = """    /* ⊕ MRB-290 R13 — Design's five aggregates computed from `board`,
       replaced by the payload's own. The client is served the top ten plus
       the viewer and never sees the cohort, so a median taken here would be
       the median of ten top scorers and would read as the median of the
       year group. */
    var D = MRB_D();
    const entries = D && D.entries != null ? D.entries : null;
    const cut = (D && D.cut_pct != null) ? {pct: D.cut_pct} : null;
    const median = D && D.median_pct != null ? D.median_pct : null;
    const fastest = (D && D.fastest_secs != null)
      ? {secs: D.fastest_secs} : null;
    const climb = (D && D.biggest_climb != null)
      ? {move: D.biggest_climb} : null;
    const live = MRB_IS_CURRENT();
    /* R13, second half — the countdown. `closes_at` is 09:15 UTC on the
       Friday AFTER the week's Thursday end, which is not derivable from the
       week at all, and `MRB_NOW()` is the server's clock, not the device's. */
    const _closes = MRB_CLOSES();
    const ms = _closes == null ? 0 : _closes - MRB_NOW();
    const d = Math.max(0, Math.floor(ms / 864e5));
    const h = Math.max(0, Math.floor(ms / 36e5) % 24);
    const mi = Math.max(0, Math.floor(ms / 6e4) % 60);
    const sec = Math.max(0, Math.floor(ms / 1000) % 60);"""


def seam_logic(logic):
    """Design's logic class with every MRB-290 ruling applied."""
    n = {}

    # ── R5 / R4 / R3 / R6 — the fabricators ──────────────────────────────
    #
    # ⚠️ R3 BEFORE the const is dropped: the three use sites must be rewritten
    # while `VIEWER` is still there to be found, or `drop_const` removes the
    # declaration and leaves three references to a name that no longer exists
    # — a ReferenceError at first render, on a page that has already painted
    # its nav and its heading.
    logic = swap(
        logic,
        "const isYou = x.name === VIEWER;",
        "const isYou = MRB_IS_YOU(x.name);", "R3")
    logic = swap(
        logic,
        "const meRow = board.find(x => x.name === VIEWER);",
        "const meRow = MRB_ME();", "R3")
    logic = swap(logic, "name: VIEWER,", "name: MRB_VIEWER_NAME(), "
                        "initials: '', avImg: 'none',", "R3/R18/R25")

    # ── R25 — the avatar, inside Design's disc ───────────────────────────
    #
    # ⚠️ TWO KEYS ADDED TO `deco` AND NOT ONE EXISTING KEY ALTERED. The brief
    # freezes `deco` as pure presentation over the ten-field record, and this
    # is the single exception Mide ruled: identity — name AND avatar — is
    # frozen to what the live page shows today, and the live page shows
    # faces. `initials` goes empty ONLY when there is an image to put in its
    # place, so Design's monogram remains the fallback rather than being
    # replaced by one.
    logic = swap(
        logic,
        "        name: x.name, initials: initialsOf(x.name), rank: x.rank,",
        "        name: x.name,\n"
        "        /* ⊕ MRB-290 R25 — Design's monogram, or the student's own\n"
        "           face in the same disc. The URL is sanitised at the seam\n"
        "           (shared/leaderboard-live.js), never here. */\n"
        "        initials: x.avatar_url ? '' : initialsOf(x.name),\n"
        "        avImg: x.avatar_url ? 'url(\"' + x.avatar_url + '\")' : 'none',\n"
        "        rank: x.rank,", "R25")

    # Design's `blank` podium placeholder is unreachable — the podium's own
    # `sc-if` is `podiumOn && podium.length >= 3`, so a blank place can never
    # be drawn. It still gains the key: an absent binding is a render MISS,
    # and the behaviour gate reads `data-mrb-misses`. A dead branch that
    # would fail a gate if it ever woke up is not worth the saving.
    logic = swap(
        logic,
        "const blank = { name: '\\u2014', initials: '--', "
        "pctLabel: '\\u2014', score: '\\u2014' };",
        "const blank = { name: '\\u2014', initials: '--', avImg: 'none', "
        "isYou: false, pctLabel: '\\u2014', score: '\\u2014' };", "R25")

    # ⚠️ R26 BEFORE the consts go, for exactly the reason R3's three swaps
    # are: this is a CLASS FIELD INITIALISER and it reads `LIVE`. Dropped
    # first, `new Component()` throws `ReferenceError: LIVE is not defined`
    # in the constructor and the page renders nothing at all — which is how
    # it shipped past a green build and was caught by the behaviour gate.
    logic = swap(
        logic,
        "  state = { wk: LIVE, tier: 'Higher', subject: 'Overall', "
        "open: null, flip: false, now: Date.now() };",
        "  /* ⊕ MRB-290 R26. `wk`, `tier` and `subject` live in the seam\n"
        "     (R10) — the weeks array changes with the subject, so an index\n"
        "     is not stable across a press. `LIVE` is gone (R4), and\n"
        "     Design's 'Higher' default is overridden by the signed-in\n"
        "     student's own profile tier. What is left is genuinely this\n"
        "     component's: which row is open, the animation flip, and the\n"
        "     countdown tick. */\n"
        "  state = { open: null, flip: false, now: Date.now() };", "R26")

    for name in ("FIRST", "LAST", "VIEWER", "WEEKS", "LIVE"):
        logic = drop_const(logic, name, "R3/R4/R5")
    for name in ("roster", "entered", "seed", "streak"):
        logic = drop_method(logic, name, "R6")

    # ── R7 — the two board reads ─────────────────────────────────────────
    logic = replace_method(logic, "raw", """    /* ⊕ MRB-290 R7. Design hashed a cohort out of a week and a name.
       These are the real rows, already ranked by the backend — which has the
       whole cohort to rank and the client, by design, does not. `w` is only
       ever the selected week: the strip's other-week read is R9. */
    if (w !== MRB_STATE(this).wk) { return []; }
    return MRB_ROWS();""", "R7")

    logic = replace_method(logic, "board", """    /* ⊕ MRB-290 R7. Design derived `move`/`was`/`streak` by diffing this
       week's fabricated board against last week's. All three arrive on the
       payload: `move` null means NEW and 0 means HELD, and those are
       different facts. */
    return this.raw(w);""", "R7")

    # ── R8 — the week ranges ─────────────────────────────────────────────
    logic = replace_method(logic, "weekDates", """    /* ⊕ MRB-290 R8. Weeks run FRIDAY → THURSDAY and `week_start` is
       always the Friday. Design counted back from the device's current
       Monday, which is wrong by four days, wrong about which weeks exist,
       and derived from a clock the student sets. `isoWeek` is Design's own
       and is kept: the ISO week of a Friday is the week that Friday is in. */
    return MRB_WEEKS().map(function (w) {
      const p = String(w.week_start).split('-');
      const s = new Date(+p[0], +p[1] - 1, +p[2]);
      const e = new Date(s.getFullYear(), s.getMonth(), s.getDate() + 6);
      const range = s.getMonth() === e.getMonth()
        ? s.getDate() + '\\u2013' + e.getDate() + ' ' + MON[e.getMonth()]
        : s.getDate() + ' ' + MON[s.getMonth()] + '\\u2013'
          + e.getDate() + ' ' + MON[e.getMonth()];
      return {
        start: s, end: e, range: range, no: 'W' + isoWeek(s),
        week_start: w.week_start,
        long: s.getDate() + ' ' + MON[s.getMonth()].charAt(0)
              + MON[s.getMonth()].slice(1).toLowerCase()
      };
    });""", "R8")

    # ── R12 — the countdown interval and the rail snap ───────────────────
    logic = replace_method(logic, "componentDidMount", """    /* ⊕ MRB-290 R12. `LIVE` is gone (R4); `is_current` is the payload's
       own answer and survives a subject press that reindexes the array.
       Design's rail scroll-snap below is kept exactly as drawn. */
    this._t = setInterval(() => {
      if (MRB_IS_CURRENT()) { this.setState({ now: Date.now() }); }
    }, 1000);
    const snap = () => {
      const el = this.rail();
      if (el && el.scrollWidth > el.clientWidth) { el.scrollLeft = el.scrollWidth; }
      else { setTimeout(snap, 120); }
    };
    setTimeout(snap, 60);""", "R12")

    # ── R10 — selection lives in the seam ────────────────────────────────
    #
    # ⊕ R28 rides on the same line. `renderVals` runs BEFORE the runtime
    # empties the host, so this is the last moment the OLD rail is still in
    # the DOM and its scroll position can be read.
    logic = swap(
        logic, "    const s = this.state;",
        "    const s = MRB_STATE(this);\n"
        "    /* ⊕ MRB-290 R28. The runtime rebuilds the host on every draw\n"
        "       and restores focus, field values and window scroll — but not\n"
        "       an element's scrollLeft. Read it here, while the old rail is\n"
        "       still mounted; componentDidUpdate puts it back. */\n"
        "    { const _r0 = this.rail();\n"
        "      if (_r0) { this._railWant = _r0.scrollLeft; } }", "R10/R28")

    # ── R28 — put the rail back where the student left it ────────────────
    logic = swap(
        logic,
        "  componentWillUnmount() { clearInterval(this._t); }",
        "  componentWillUnmount() { clearInterval(this._t); }\n"
        "\n"
        "  /* ⊕ MRB-290 R28 — ADDED. Design's class has no\n"
        "     componentDidUpdate, because her prototype never re-rendered\n"
        "     into a fresh host. Without this the week rail returns to scroll\n"
        "     0 on every tier, subject or week press, throwing away the\n"
        "     right-hand snap componentDidMount performs and jumping the\n"
        "     student back to the oldest week on the rail.\n"
        "\n"
        "     ⊕ MRB-290 R33 SUPERSEDES ITS BEHAVIOUR WHEN THE SELECTION\n"
        "     MOVES. Preserving the old scrollLeft is right for a redraw\n"
        "     that does NOT move the week — a countdown tick, a filter press\n"
        "     that keeps the week, a student browsing the strip who must not\n"
        "     be yanked back. It is wrong for one that DOES: Mide clicked a\n"
        "     past week and the rail stayed parked at the oldest end, so he\n"
        "     had to hunt back for what he had just chosen. The two cases\n"
        "     are told apart by the last-snapped week_start. */\n"
        "  componentDidUpdate() {\n"
        "    const el = this.rail();\n"
        "    if (!el) { return; }\n"
        "    const idx = MRB_STATE(this).wk;\n"
        "    const wks = MRB_WEEKS();\n"
        "    const sel = wks[idx] ? wks[idx].week_start : null;\n"
        "    if (sel !== this._railWeek) {\n"
        "      this._railWeek = sel;\n"
        "      const chip = el.children[idx];\n"
        "      /* Only when it is actually out of view: a selection change\n"
        "         to a chip already on screen moves nothing. */\n"
        "      if (chip) {\n"
        "        const l = chip.offsetLeft, r = l + chip.offsetWidth;\n"
        "        if (l < el.scrollLeft) {\n"
        "          el.scrollLeft = Math.max(0, l - 16);\n"
        "        } else if (r > el.scrollLeft + el.clientWidth) {\n"
        "          el.scrollLeft = r - el.clientWidth + 16;\n"
        "        }\n"
        "      }\n"
        "      this._railWant = el.scrollLeft;\n"
        "      return;\n"
        "    }\n"
        "    if (this._railWant != null && el.scrollWidth > el.clientWidth) {\n"
        "      el.scrollLeft = this._railWant;\n"
        "    }\n"
        "  }", "R28/R33")

    # ── R24 — the week the payload may not have yet ──────────────────────
    logic = swap(
        logic, "    const dates = this.weekDates();",
        "    const dates = this.weekDates();\n"
        "    /* ⊕ MRB-290 R24. Design's `dates` is nine entries off the\n"
        "       device clock and can never be empty; the real one is empty\n"
        "       until the first payload lands and on any failed fetch, and\n"
        "       `dates[s.wk].no` on an empty array throws from inside\n"
        "       renderVals — a page that paints its nav and then stops. */\n"
        "    const _wk = dates[s.wk] || { no: '', range: '', long: '\\u2014' };",
        "R24")
    logic = swap(
        logic,
        "      weekTitle: dates[s.wk].no + ' \\u00B7 ' + dates[s.wk].range,",
        "      weekTitle: _wk.range ? (_wk.no + ' \\u00B7 ' + _wk.range) : '',",
        "R24")
    logic = swap(logic, "dates[s.wk].long.toUpperCase()",
                 "_wk.long.toUpperCase()", "R24")

    # ── R9 — the strip's mini-bar ────────────────────────────────────────
    logic = swap(logic, "      const top = this.raw(i)[0];",
                 "      const top = MRB_TOP(i);", "R9")

    # ── R27 — the last two readers of the deleted `LIVE` ─────────────────
    logic = swap(
        logic, "      const live = i === LIVE;",
        "      /* ⊕ MRB-290 R27. Each week carries its own `is_current`;\n"
        "         `LIVE` was an index into a fixed nine (R4). */\n"
        "      const live = !!(MRB_WEEKS()[i] || {}).is_current;", "R27")
    logic = swap(
        logic,
        "goLive: () => { const el = this.rail(); if (el) el.scrollTo({ left: "
        "el.scrollWidth, behavior: 'smooth' }); this.setState(p => ({ wk: "
        "LIVE, flip: !p.flip, open: null })); }",
        "goLive: () => { const el = this.rail();\n"
        "        if (el) el.scrollTo({ left: el.scrollWidth, "
        "behavior: 'smooth' });\n"
        "        /* ⊕ MRB-290 R27. 'This week' selects the week the payload\n"
        "           calls current, not the last index in the array. */\n"
        "        const _c = MRB_WEEKS().filter(w => w.is_current)[0];\n"
        "        if (_c) { MRB_SET({ week: _c.week_start }); }\n"
        "        this.setState(p => ({ flip: !p.flip, open: null })); }",
        "R27")

    # ── R11 — the three onSelect closures ────────────────────────────────
    logic = swap(
        logic,
        "        onSelect: () => this.setState(p => ({ wk: i, flip: !p.flip, "
        "open: null }))",
        "        onSelect: () => { const _w = MRB_WEEKS()[i];\n"
        "          if (_w) { MRB_SET({ week: _w.week_start }); }\n"
        "          this.setState(p => ({ flip: !p.flip, open: null })); }",
        "R11")
    logic = swap(
        logic,
        "      onSelect: () => this.setState(p => ({ tier: t, flip: !p.flip, "
        "open: null }))",
        "      onSelect: () => { MRB_SET({ tier: t });\n"
        "        this.setState(p => ({ flip: !p.flip, open: null })); }",
        "R11")
    logic = swap(
        logic,
        "        onSelect: () => this.setState(p => ({ subject: k, flip: "
        "!p.flip, open: null }))",
        "        onSelect: () => { MRB_SET({ subject: k });\n"
        "          this.setState(p => ({ flip: !p.flip, open: null })); }",
        "R11")

    # ── R13 — the aggregate block, replaced whole ────────────────────────
    #
    # It is CONTIGUOUS in Design's source (lines 519-529), which is why this
    # is one ruling and not eleven: the eleven locals it defines are read by
    # `stats`, `closeLabel`, `cutValue` and `closeBg`/`closeBd`/`closeDot`/
    # `closeFg`/`closeAnim` further down, and every one of those reads is left
    # exactly as Design wrote it.
    start = logic.index(
        "    const cut = qualified.length ? qualified[qualified.length - 1] "
        ": null;")
    end = logic.index("    const sec = Math.max(0, Math.floor(ms / 1000) % 60);")
    end = logic.index("\n", end) + 1
    logic = logic[:start] + _AGGREGATE + "\n" + logic[end:]

    # ── R14 — the three remaining board.length ───────────────────────────
    logic = swap(logic, "board.length", "entries", "R14", count=3)

    # ── R15 — a null median is an em dash, not 'null%' ───────────────────
    logic = swap(logic,
                 "{ label: 'MEDIAN SCORE', value: median + '%', "
                 "hue: 'var(--biology)' }",
                 "{ label: 'MEDIAN SCORE', "
                 "value: median == null ? '\\u2014' : median + '%', "
                 "hue: 'var(--biology)' }", "R15")

    # ── R14 knock-on — the ENTRIES tile now reads a nullable number ──────
    logic = swap(logic,
                 "{ label: 'ENTRIES', value: String(entries), "
                 "hue: 'var(--st-accent)' }",
                 "{ label: 'ENTRIES', "
                 "value: entries == null ? '\\u2014' : String(entries), "
                 "hue: 'var(--st-accent)' }", "R15/R19")

    # ── R16 — the one- and two-entrant board that drew nothing ───────────
    logic = swap(logic, "    const listStart = podiumOn ? 3 : 0;",
                 "    /* ⊕ MRB-290 R16. Design consults the PROP here and the\n"
                 "       podium's own `sc-if` consults `podium.length >= 3`.\n"
                 "       With one or two entrants those disagree, the podium\n"
                 "       hides, the list still starts at 3, and the board\n"
                 "       draws NO ROWS AT ALL. Foundation's current week has\n"
                 "       exactly one entry. */\n"
                 "    const listStart = podium.length >= 3 ? 3 : 0;", "R16")

    # ── R30 — the loading state must not put a fact where it has none ────
    #
    # ⚠️ ANCHORED ON THE POST-SWAP TEXT, and the ordering is why this block
    # sits here rather than beside R13. `board.length` became `entries` at
    # R14 and `dates[s.wk].long` became `_wk.long` at R24, so both of these
    # anchors only exist once those have run. Anchored on Design's original
    # text they would match nothing, and `swap` would stop the build — which
    # is the good failure, but pointlessly.
    logic = swap(
        logic,
        "cutLabel: 'TOP ' + topCount + ' ONLY \\u00B7 ' + entries "
        "+ ' SAT THIS WEEK',",
        "cutLabel: MRB_STATUS() !== 'ok'\n"
        "        /* ⊕ MRB-290 R30. The clause is DROPPED, not dashed: while\n"
        "           the payload is null this read 'TOP 10 ONLY \\u00B7 null\n"
        "           SAT THIS WEEK' on the live page. A clause whose only\n"
        "           content is a fact we do not have does not belong in the\n"
        "           sentence at all. */\n"
        "        ? ('TOP ' + topCount + ' ONLY')\n"
        "        : ('TOP ' + topCount + ' ONLY \\u00B7 ' + entries\n"
        "           + ' SAT THIS WEEK'),", "R30")

    logic = swap(
        logic,
        "closeLabel: live ? 'CLOSES IN ' + d + 'D ' + String(h).padStart(2, "
        "'0') + 'H ' + String(mi).padStart(2, '0') + 'M ' + "
        "String(sec).padStart(2, '0') + 'S' : 'LOCKED ' "
        "+ _wk.long.toUpperCase(),",
        "closeLabel: MRB_STATUS() !== 'ok'\n"
        "        /* ⊕ MRB-290 R30. Design's not-live branch fires on an\n"
        "           empty payload too, so this pill told a student the week\n"
        "           was LOCKED while it was merely loading — unknown\n"
        "           rendered as one of the two real answers, which is\n"
        "           MRB-287's 'ON TIME 0' again. Unknown is neither. */\n"
        "        ? '\\u2014'\n"
        "        : (live ? 'CLOSES IN ' + d + 'D ' + String(h).padStart(2, '0')\n"
        "            + 'H ' + String(mi).padStart(2, '0') + 'M '\n"
        "            + String(sec).padStart(2, '0') + 'S'\n"
        "          : 'LOCKED ' + _wk.long.toUpperCase()),", "R30")

    # ── R17 / R19 / R20 — the cut line says which state it is in ─────────
    logic = swap(
        logic,
        "cutValue: cut ? 'CUT LINE ' + cut.pct + '%' : 'NO ENTRIES',",
        "cutValue: MRB_CUT_STATE() || (cut ? 'CUT LINE ' + cut.pct + '%'\n"
        "        : (entries ? 'ALL ' + entries + ' LISTED' : 'NO ENTRIES')),",
        "R17/R19/R20")

    n["rulings"] = len(RULINGS)
    return logic, n


# ══════════════════════════════════════════════════════════════════════════
#  R2 — the 'AY' monograms
# ══════════════════════════════════════════════════════════════════════════

def bind_initials(roots):
    """Rewrite every text node reading exactly 'AY' to `{{ me.initials }}`.

    ⚑ ANCHORED ON THE LITERAL, NOT ON A NODE INDEX, and that is deliberate.
    `teacher_rulings.BINDINGS_AT` binds by index because three DIFFERENT
    import counts on that delivery all read `2`, so a literal key would bind
    every text node reading `2` on the page. Here the opposite holds: 'AY' is
    one person's initials, typed in the two places the viewer's own monogram
    is drawn, and both mean the same thing. A literal key binds both for free
    and — unlike an index — survives Design moving them.

    Returns (roots, count). The caller asserts the count.
    """
    out = json.loads(json.dumps(roots))
    hits = [0]

    def walk(n):
        if not isinstance(n, dict):
            return
        if n.get("t") == "#" and n.get("v") == "AY":
            n["v"] = {"parts": [{"e": "me.initials"}]}
            hits[0] += 1
            return
        for c in (n.get("c") or []):
            walk(c)

    for r in out:
        walk(r)
    return out, hits[0]


AY_EXPECTED = 2


# ══════════════════════════════════════════════════════════════════════════
#  R25 — the avatar, into the disc Design already drew
# ══════════════════════════════════════════════════════════════════════════

# What is appended to a monogram disc's `style`. `background-image` comes
# AFTER Design's `background:` shorthand deliberately — the shorthand resets
# `background-image` to `none`, so an earlier declaration would be wiped by
# Design's own. `cover` + `center` fill a circular disc from any aspect ratio
# without distorting a face.
_AV_SUFFIX = ";background-size:cover;background-position:center;" \
             "background-repeat:no-repeat"


def _as_parts(v):
    """A compiled attribute value as a parts list, whatever form it is in."""
    if isinstance(v, dict) and "parts" in v:
        return list(v["parts"])
    return [v] if v else []


def bind_avatars(roots):
    """Give every monogram disc a bound `background-image` from `*.avImg`.

    ⚑ FOUND BY WHAT THE DISC RENDERS, NOT BY AN INDEX OR A STYLE STRING.
    A monogram disc is precisely "an element whose only child is a text node
    interpolating something-dot-initials" — which is true of all six and of
    nothing else on the page. Matching on the style string instead would have
    matched three different strings (Design binds the row disc's background
    to `r.avBg` and hardcodes the other five), and matching on an index would
    break the first time Design moved a disc.

    ⚠️ MUST RUN AFTER `bind_initials`. Two of the six discs are Design's
    typed 'AY' monograms and are not `*.initials` interpolations until R2 has
    rewritten them. Run first, this finds four discs and reports success.

    Returns (roots, count). The caller asserts the count is six.
    """
    out = json.loads(json.dumps(roots))
    hits = [0]

    def walk(n):
        if not isinstance(n, dict):
            return
        kids = n.get("c") or []
        if len(kids) == 1 and isinstance(kids[0], dict) \
                and kids[0].get("t") == "#":
            v = kids[0].get("v")
            parts = v.get("parts") if isinstance(v, dict) else None
            if parts and len(parts) == 1 and isinstance(parts[0], dict):
                expr = parts[0].get("e") or ""
                if expr.endswith(".initials"):
                    prefix = expr[:-len(".initials")]
                    a = n.setdefault("a", {})
                    style = _as_parts(a.get("style"))
                    style.append(";background-image:")
                    style.append({"e": prefix + ".avImg"})
                    style.append(_AV_SUFFIX)
                    a["style"] = {"parts": style}
                    hits[0] += 1
        for c in kids:
            walk(c)

    for r in out:
        walk(r)
    return out, hits[0]


# Three podium places, the row avatar, and the viewer's own disc twice — the
# standing card and the sticky pinned row.
AVATAR_DISCS_EXPECTED = 6


# ══════════════════════════════════════════════════════════════════════════
#  R31 — the page fills the screen
# ══════════════════════════════════════════════════════════════════════════

WIDTH_CAP = "max-width: 1180px; "


def unwidth(roots):
    """Drop the body container's width cap, keeping Design's gutters.

    ⚠️ EXACTLY ONE ELEMENT, ASSERTED. Design's delivery had two 1180px
    containers — the nav's and the body's — and R1 removed the nav with the
    first. If a second ever reappears here it is a new container Design has
    drawn and it needs its own decision, not a silent widening.
    """
    out = json.loads(json.dumps(roots))
    hits = [0]

    def walk(n):
        if not isinstance(n, dict):
            return
        a = n.get("a") or {}
        st = a.get("style")
        if isinstance(st, str) and WIDTH_CAP in st:
            a["style"] = st.replace(WIDTH_CAP, "", 1)
            hits[0] += 1
        for c in (n.get("c") or []):
            walk(c)

    for r in out:
        walk(r)
    return out, hits[0]


WIDTH_CAPS_EXPECTED = 1


# ══════════════════════════════════════════════════════════════════════════
#  R34 — the podium is an object on the page, and its numbers are readable
# ══════════════════════════════════════════════════════════════════════════

# The podium's outer frame: Design's source line 137, the element carrying the
# border-radius, the gradient and the drop shadow. Anchored on the HEAD of its
# style string rather than the whole of it, so that a change to her gradient
# or her shadow does not silently un-anchor the cap.
PODIUM_FRAME_HEAD = ("margin-top: 24px; position: relative; "
                     "border-radius: var(--st-r-frame); overflow: hidden;")

# ⚠️ PREPENDED, NOT APPENDED. Design's own string ends with `box-shadow: …;`
# and her `margin-top: 24px` opens it — putting the cap first keeps her
# declarations in the order she wrote them and keeps `margin-top` next to the
# two margin declarations added here, where anyone reading the built page can
# see all three at once. `margin-left/right` and not the `margin` shorthand,
# which would silently reset her top margin to zero.
PODIUM_CAP = "max-width: 1140px; margin-left: auto; margin-right: auto; "

# Every type size inside the frame, as (what it is, Design's fragment, the
# ported fragment, how many times it must occur INSIDE THE PODIUM SUBTREE).
#
# ⚑ FRAGMENTS, NOT WHOLE STYLE STRINGS, AND SCOPED TO THE FRAME. Two of these
# fragments are genuinely shared by places 2 and 3 — Design drew both silver
# and bronze at 24px percentages and 14px marks — so a whole-string match
# would need two identical entries and a count of one each, which is a lie
# about the drawing. And `font: 600 24px/1 var(--st-display)` occurs elsewhere
# on the page outside the podium, which is exactly why the walk starts at the
# frame rather than at the roots.
PODIUM_TYPE = (
    ("place 1 numeral", "font: 600 86px/0.95", "font: 600 108px/0.95", 1),
    ("place 2 numeral", "font: 600 56px/1 ", "font: 600 70px/1 ", 1),
    ("place 3 numeral", "font: 600 48px/1 ", "font: 600 60px/1 ", 1),
    ("place 1 percentage", "font: 600 32px/1 var(--st-display)",
     "font: 600 40px/1 var(--st-display)", 1),
    ("place 2/3 percentage", "font: 600 24px/1 var(--st-display)",
     "font: 600 30px/1 var(--st-display)", 2),
    ("place 1 marks line", "font: 400 15px/1 var(--st-mono)",
     "font: 400 17px/1 var(--st-mono)", 1),
    ("place 2/3 marks line", "font: 400 14px/1 var(--st-mono)",
     "font: 400 16px/1 var(--st-mono)", 2),
    ("place 1 name", "font: 600 30px/1.08", "font: 600 32px/1.08", 1),
    ("place 2/3 name", "font: 600 22px/1.15", "font: 600 24px/1.15", 2),
    ("place 1 step height", "min-height: 212px", "min-height: 265px", 1),
    ("place 2 step height", "min-height: 148px", "min-height: 185px", 1),
    ("place 3 step height", "min-height: 116px", "min-height: 145px", 1),
)


def repodium(roots):
    """Cap the podium frame and scale the type inside it. R34.

    ⚠️ THE STEP HEIGHTS LIVE IN AN INTERPOLATED STYLE and the numerals do
    not. Design binds `animation: {{ riseA }}` into the same attribute as
    `min-height: 212px`, so that one attribute compiles to a `{"parts": […]}`
    object while the numeral's compiles to a plain string. A rewrite that
    tested `isinstance(style, str)` would find every font size and silently
    miss all three heights — the repo's known compiled-`parts` gotcha, and the
    one that would have flattened Design's staircase while reporting success.
    Both forms are rewritten here, and the counts below are what proves it.

    Returns (roots, hits) where `hits` is keyed by the labels in
    `PODIUM_TYPE`. The caller asserts every one against its expected count.
    """
    out = json.loads(json.dumps(roots))
    frames = []

    def find(n):
        if not isinstance(n, dict):
            return
        st = (n.get("a") or {}).get("style")
        if isinstance(st, str) and st.startswith(PODIUM_FRAME_HEAD):
            frames.append(n)
        for c in (n.get("c") or []):
            find(c)

    for r in out:
        find(r)
    if len(frames) != 1:
        raise SystemExit(
            "build_leaderboard_port.py: R34 caps Design's podium frame — the "
            "element at source line 137 — and the tree holds %d element(s) "
            "whose style opens with it rather than one.\n"
            "  Mide ruled the podium is capped and centred while the table "
            "stays full-bleed; capping the wrong element would either squeeze "
            "the table again (R31's complaint) or do nothing at all."
            % len(frames))

    frame = frames[0]
    frame.setdefault("a", {})["style"] = PODIUM_CAP + frame["a"]["style"]

    hits = {label: 0 for label, _, _, _ in PODIUM_TYPE}

    def rewrite(text):
        for label, old, new, _ in PODIUM_TYPE:
            if old in text:
                hits[label] += text.count(old)
                text = text.replace(old, new)
        return text

    def walk(n):
        if not isinstance(n, dict):
            return
        a = n.get("a") or {}
        st = a.get("style")
        if isinstance(st, str):
            a["style"] = rewrite(st)
        elif isinstance(st, dict) and "parts" in st:
            a["style"] = {"parts": [rewrite(p) if isinstance(p, str) else p
                                    for p in st["parts"]]}
        for c in (n.get("c") or []):
            walk(c)

    walk(frame)
    return out, hits


# ══════════════════════════════════════════════════════════════════════════
#  R32 — the YOU chip reaches the podium
# ══════════════════════════════════════════════════════════════════════════

PODIUM_PLACES = ("p1", "p2", "p3")


def _find_you_chip(roots):
    """Design's own `sc-if r.isYou` chip subtree, found not retyped."""
    found = []

    def walk(n):
        if not isinstance(n, dict):
            return
        if n.get("t") == "if" and n.get("e") == "r.isYou":
            found.append(n)
        for c in (n.get("c") or []):
            walk(c)

    for r in roots:
        walk(r)
    if len(found) != 1:
        raise SystemExit(
            "build_leaderboard_port.py: R32 clones Design's own YOU chip out "
            "of her table row, and the tree holds %d `sc-if r.isYou` node(s) "
            "rather than one.\n"
            "  It is cloned rather than retyped so the two chips cannot "
            "drift apart. If Design has moved or duplicated it, re-anchor "
            "here — do not hand-write a replacement span." % len(found))
    return found[0]


def bind_podium_you(roots):
    """Put Design's YOU chip on a podium place when it is the viewer's.

    ⚑ MIDE'S R32. Inserted as a SIBLING immediately after the podium name,
    inside Design's own column flex — so it sits under the name, centred,
    with no new styling language and no change to any element she drew.
    """
    out = json.loads(json.dumps(roots))
    chip = _find_you_chip(out)
    hits = [0]

    def place_of(kid):
        """The podium place this element names, or None."""
        if not isinstance(kid, dict):
            return None
        only = kid.get("c") or []
        if len(only) != 1 or not isinstance(only[0], dict) \
                or only[0].get("t") != "#":
            return None
        v = only[0].get("v")
        parts = v.get("parts") if isinstance(v, dict) else None
        if not parts or len(parts) != 1 or not isinstance(parts[0], dict):
            return None
        expr = parts[0].get("e") or ""
        if not expr.endswith(".name"):
            return None
        p = expr[:-len(".name")]
        return p if p in PODIUM_PLACES else None

    # ⚠️ REBUILT IN ONE PASS, NOT MUTATED IN PLACE. The first version
    # inserted the chip and then re-walked the same parent to pick up the
    # shifted indices — which found the very same podium name again and
    # recursed until the stack gave out (984 frames). Building a fresh
    # children list means each child is considered exactly once and the
    # inserted node is never a candidate.
    def walk(n):
        if not isinstance(n, dict):
            return
        kids = n.get("c")
        if not kids:
            return
        rebuilt = []
        for kid in kids:
            rebuilt.append(kid)
            place = place_of(kid)
            if place:
                node = json.loads(json.dumps(chip))
                node["e"] = place + ".isYou"
                rebuilt.append(node)
                hits[0] += 1
            else:
                walk(kid)
        n["c"] = rebuilt

    for r in out:
        walk(r)
    return out, hits[0]


PODIUM_YOU_EXPECTED = 3


# ══════════════════════════════════════════════════════════════════════════
#  The nav — READ from the landing page, never retyped
# ══════════════════════════════════════════════════════════════════════════

def live_nav():
    """The landing page's own `<nav class="nav">…</nav>`, lifted verbatim.

    ⚑ READ, NOT COPIED, for the same reason `capture_imports` reads the brand
    SVG out of Design's standalone rather than retyping it: hand-copying
    twenty lines of markup with a gradient definition in the middle of it is
    exactly the transcription that goes wrong quietly and is then defended as
    "it looks the same". Read from `index.html`, the nav on this page IS the
    nav on the landing page, permanently, including the day somebody adds a
    link to it.
    """
    src = open("index.html", encoding="utf-8").read()
    m = re.search(r'<nav class="nav">.*?</nav>', src, re.S)
    if not m:
        raise SystemExit(
            "build_leaderboard_port.py: index.html has no "
            "`<nav class=\"nav\">…</nav>` to lift.\n"
            "  Mide's 25 Aug 2026 ruling (R1) is that this page carries the "
            "LANDING PAGE's nav, so that is where it is read from. Retyping "
            "it here would make the two drift the first time either changed.")
    nav = m.group(0)
    for want, why in (
            ('class="nav-brand"', "the gold-to-rust two-chevron + wordmark "
                                  "CLAUDE.md requires on an external root page"),
            ('id="nav-auth-area"', "nav.js's sign-in slot"),
            ('class="nav-burger"', "the drawer trigger"),
            ('class="nav-cluster"', "the right-hand cluster")):
        if want not in nav:
            raise SystemExit(
                "build_leaderboard_port.py: the nav lifted from index.html "
                "has no `%s` — %s.\n  Either index.html's nav has been "
                "restructured, or the wrong element matched." % (want, why))
    if "octopus" in nav or "⚗" in nav:
        raise SystemExit(
            "build_leaderboard_port.py: the nav lifted from index.html "
            "carries a retired placeholder (the octopus logo or the alembic "
            "emoji). CLAUDE.md calls that brand drift — fix index.html "
            "rather than propagating it here.")
    return nav


# ══════════════════════════════════════════════════════════════════════════
#  The retired original
# ══════════════════════════════════════════════════════════════════════════

def retire_original():
    """Move the hand-written leaderboard.html out of the repo root.

    ⛔ AND REFUSE THE BUILD IF IT IS NEITHER THERE NOR ALREADY RETIRED, the
    same guard `build_teacher_port.retire_originals` carries. A hand-written
    source file sitting beside its generated replacement is a file somebody
    will edit, and the edit survives exactly until the next build — which is
    how the MRB-275 rulings were destroyed once already.
    """
    os.makedirs(RETIRED, exist_ok=True)
    dest = os.path.join(RETIRED, RETIRED_NAME)
    live = os.path.join(MIRROR_OUT, OUT_NAME)
    if os.path.exists(dest):
        return open(dest, encoding="utf-8").read()
    if not os.path.exists(live):
        raise SystemExit(
            "build_leaderboard_port.py: %s is neither at the repo root nor "
            "retired at %s.\n  This build replaces a page 135+ students use. "
            "Refusing rather than writing over an absence: restore the "
            "hand-written original from git first." % (OUT_NAME, dest))
    text = open(live, encoding="utf-8").read()
    if "GENERATED — do not edit" in text[:4000]:
        raise SystemExit(
            "build_leaderboard_port.py: %s is already this build's own "
            "output and there is no retired copy at %s. Restore the "
            "hand-written original from git before rebuilding."
            % (live, dest))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.remove(live)
    print("     ⊕ retired  %-22s → %s" % (OUT_NAME, dest))
    return text


# ══════════════════════════════════════════════════════════════════════════
#  The page
# ══════════════════════════════════════════════════════════════════════════

_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_leaderboard_port.py`

  Markup and view-model: Design's KS4 Weekly Leaderboard delivery.
  Data: shared/%s, and nothing else.
  Every edit to the delivery is in build_leaderboard_port.RULINGS, with why.
  A fix typed into this file survives until the next build. Behaviour goes in
  the rulings register; what renders goes in the seam; the markup is Design's.
  ══════════════════════════════════════════════════════════════════════════
-->
"""

_BANNER_FIXTURE = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED FIXTURE — not the live page, and NOT PUBLISHED.

  It carries Design's OWN sample: sixty-one invented handles derived from the
  delivery's constants and evaluated rather than retyped. That is the point —
  it is what lets leaderboard_behaviour.py drive every control with no
  network and no credential.

  ⛔ It lives in %s/ precisely so that it is outside every tree
  generate_site_v5.py publishes or round-trips. Do not move it into shared/,
  student/ or teacher/, and never add an ignore rule to a copytree to hold it
  back — that is the MRB-287 §7 defect, and the second attempt at it deleted
  the fixtures from source.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def page_html(roots, imports, logic, nav, fixture, versions):
    """`fixture` is the fixture JS filename, or None for the live page."""
    tail = (
        "<script src=\"%s\"></script>\n"
        "<script>window.__MRB_MOUNT__();</script>\n" % fixture
    ) if fixture else (
        # ⚠️ THE SUPABASE SDK BEFORE THE SEAM. `leaderboard-live.js` reads the
        # session to land the viewer on their own profile tier, exactly as the
        # retired page did. Loaded from the same CDN the retired page used.
        "<script src=\"https://cdn.jsdelivr.net/npm/@supabase/"
        "supabase-js@2/dist/umd/supabase.min.js\"></script>\n"
        "<script src=\"%s\"></script>\n" % LIVE_JS_URL
    )

    dep_map = ("<script>window.__MRB_ASSET_V__=%s;</script>\n"
               % json.dumps({k: v for k, v in sorted(versions.items())
                             if k in STAMPED_DEPS},
                            separators=(",", ":")))

    head_links = "".join(
        ("<link rel=\"stylesheet\" href=\"/shared/%s\">\n" % d)
        if d.endswith(".css") else
        ("<script src=\"/shared/%s\" defer></script>\n" % d)
        for d in NAV_DEPS)

    return stamp_versions((
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<meta name=\"theme-color\" content=\"#F7F1E5\">\n"
        # ⚑ THE <title> NAMES NO STUDENT AND NO WEEK. The runtime renders into
        # `#mrb-leaderboard` and never touches <head>, so no binding can reach
        # it — which on the student pages once meant a real class name shipped
        # in a file whose own banner said it held no data.
        "<title>Leaderboard | MrBadmusAI</title>\n"
        "%s"
        "<link rel=\"preload\" href=\"/shared/fonts/fraunces-var-latin.woff2\" "
        "as=\"font\" type=\"font/woff2\" crossorigin>\n"
        "%s"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<style>body{margin:0;background:var(--st-ground,#FBF3E6)}"
        "a{color:var(--st-accent-text);text-decoration:none}"
        "a:hover{color:var(--st-accent-hover)}"
        "button{font-family:inherit}"
        "</style>\n"
        "</head>\n<body>\n"
        # ⚑ THE NAV IS OUTSIDE THE MOUNT POINT, AND THAT IS LOAD-BEARING (R1).
        # student-runtime's `draw()` does `host.textContent = ''` and rebuilds
        # from the template on every state change. nav.js binds its drawer,
        # its auth area and its outside-click handler once, at DOMContentLoaded
        # — inside the host, all three would be detached by the first tier
        # press and the burger would stop opening, silently.
        "%s\n"
        "<div id=\"mrb-leaderboard\" style=\"background:var(--st-ground);"
        "min-height:100vh\"></div>\n"
        "<script src=\"/shared/student-runtime.js\"></script>\n"
        "<script>window.__MRB_TPL__=%s;</script>\n"
        "<script>\n%s\n</script>\n"
        "<script>\n%s\n</script>\n"
        "%s"
        "%s"
        "</body>\n</html>\n"
        % ((_BANNER_FIXTURE % FIXTURE_OUT) if fixture
           else (_BANNER % LIVE_JS_NAME),
           head_links,
           DS_CSS_URL,
           nav,
           json.dumps({"roots": roots, "imports": imports},
                      separators=(",", ":")).replace("<", "\\u003c"),
           _SEAM
           + "var DCLogic = window.MrBadmusStudentRuntime.MrbLogic;\n"
           + "var StreamableLogic = DCLogic;\n" + logic,
           # ⚠️ DECLARED, NOT CALLED. Whoever supplies the data calls it,
           # which is what makes "this page cannot mount without a data
           # source" a property of the file rather than a promise about it.
           "window.__MRB_MOUNT__ = function () {\n"
           "  var R = window.MrBadmusStudentRuntime;\n"
           "  var tpl = window.__MRB_TPL__;\n"
           "  return R.mount({\n"
           "    into: '#mrb-leaderboard',\n"
           "    template: tpl,\n"
           "    imports: tpl.imports,\n"
           "    Component: Component,\n"
           "    props: %s\n"
           "  });\n"
           "};" % json.dumps(PINNED_PROPS, separators=(",", ":")),
           dep_map,
           tail)),
        versions)


def _refuse(path):
    """Nothing but this page is this build's to write."""
    name = os.path.basename(path)
    if path.startswith(FIXTURE_OUT):
        return
    if name != OUT_NAME and not name.endswith(".css"):
        raise SystemExit(
            "build_leaderboard_port.py: refusing to write %s. This build "
            "owns `leaderboard.html` and its design-system stylesheet, and "
            "writing generated output over a hand-written source file is the "
            "trap that ate the MRB-275 rulings." % path)


def write(path, body):
    _refuse(path)
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def _verify_stamps(stamped):
    """Re-read from disk and refuse to finish if any stamp names other bytes.

    A `?v=` naming content that is NOT what will be served is worse than no
    `?v=` at all: the page looks fixed, the browser caches the wrong bytes
    under a URL that will never change again, and every gate stays green.
    """
    bad = []
    for name, want in sorted(stamped.items()):
        for tree in (SHARED_OUT, SHARED_SRC):
            path = os.path.join(tree, name)
            if not os.path.exists(path):
                if tree == SHARED_OUT:
                    print("        ⚠️  %s/%s is missing — "
                          "generate_site_v5.py has not run here, so the stamp "
                          "could not be checked against the deployed copy"
                          % (tree, name))
                    continue
                bad.append("%s/%s does not exist, but the page stamps it "
                           "?v=%s" % (tree, name, want))
                continue
            with open(path, "rb") as fh:
                got = asset_hash(fh.read())
            if got != want:
                bad.append(
                    "%s hashes %s but the page shipped ?v=%s — the stamp "
                    "names content that is not what will be served. Run "
                    "`python3 build_all.py`, which publishes shared/ before "
                    "this build stamps it." % (path, got, want))

    # An optional group, not a negative lookahead: `(?!\?v=)` is satisfied by
    # backtracking one character and reports a perfectly stamped page as
    # unstamped. build_student_port.py records that it did exactly that.
    linked = re.compile(r"/shared/[A-Za-z0-9._/-]+(\?v=[0-9a-f]+)?")
    for tree in (SITE_OUT, MIRROR_OUT):
        path = os.path.join(tree, OUT_NAME)
        if not os.path.exists(path):
            continue
        page = open(path, encoding="utf-8").read()
        for m in linked.finditer(page):
            if m.group(1) or m.group(0).startswith("/shared/fonts/"):
                continue
            bad.append(
                "%s links %s with no cache-bust stamp, at offset %d."
                % (path, m.group(0), m.start()))
    if bad:
        raise SystemExit("build_leaderboard_port.py: the cache-bust stamps "
                         "are not honest.\n  " + "\n  ".join(bad))
    print("     ✅ cache-bust: %d asset(s) stamped from their own "
          "content, each re-hashed from disk" % len(stamped))


# ══════════════════════════════════════════════════════════════════════════
#  Design's own sample, EVALUATED rather than retyped
# ══════════════════════════════════════════════════════════════════════════
#
# The fixture drives Design's UNMODIFIED logic under Node — `roster`,
# `entered`, `raw`, `board`, `weekDates`, all of it — and captures the result
# as payloads in the endpoint's shape. So the fixture asserts the port against
# Design's OWN numbers rather than against numbers this file invented, and
# nothing about the sample is transcribed.
#
# ⚠️ THE THIN STATES ARE NOT DESIGN'S. An empty week, week one, a viewer
# outside the top ten and a signed-out visitor are shapes Design never drew,
# so they are constructed here — from the same evaluated rows where they have
# rows at all. Each is labelled in the fixture list with what it represents.

_SAMPLE_RUNNER = r"""
/* Written and run by build_leaderboard_port.py. Not checked in.

   ⚑ DESIGN'S LOGIC, UNMODIFIED, EVALUATED — not retyped, and not the ported
   copy either. This runs the delivery's own `roster`, `entered`, `raw`,
   `board`, `streak` and `weekDates` exactly as she wrote them and captures
   what they produce, reshaped into the ENDPOINT's envelope. So the fixtures
   carry Design's own numbers, and the behaviour gate measures the port
   against them rather than against numbers this build invented. */

/* ⊕ MRB-290 R29 — THE CLOCK IS PINNED BEFORE HER LOGIC RUNS.
   A harness property, like the viewport, and NOT an edit to the delivery:
   every byte of Design's logic below is still exactly as she wrote it.
   `weekDates()` counts nine weeks back from the device's current Monday, so
   without this the sample — and therefore all eight fixtures and their eight
   data files — changed on every day the build ran.
   ⚠️ TZ IS PINNED SEPARATELY, in the subprocess environment. The frozen
   instant is absolute, but `getFullYear`/`getMonth`/`getDate` are LOCAL, so
   a machine far enough east or west would derive a different Monday from the
   very same instant. Both halves are needed for determinism. */
(function (g) {
  var R = g.Date;
  var FIXED = R.parse('2026-08-25T12:00:00Z');
  function D(a, b, c, d, e, f, h) {
    if (!(this instanceof D)) { return new R(FIXED).toString(); }
    switch (arguments.length) {
      case 0: return new R(FIXED);
      case 1: return new R(a);
      case 2: return new R(a, b);
      case 3: return new R(a, b, c);
      case 4: return new R(a, b, c, d);
      case 5: return new R(a, b, c, d, e);
      case 6: return new R(a, b, c, d, e, f);
      default: return new R(a, b, c, d, e, f, h);
    }
  }
  D.now = function () { return FIXED; };
  D.parse = R.parse;
  D.UTC = R.UTC;
  /* Shared prototype, so `instanceof Date` and date arithmetic (`t - f` in
     Design's own `isoWeek`) keep working on the objects this hands back. */
  D.prototype = R.prototype;
  g.Date = D;
})(globalThis);

%(consts)s
class DCLogic { constructor(){ this.props = {}; } setState(){} }
%(logic)s

function iso(d){ return d.getFullYear() + '-'
  + String(d.getMonth() + 1).padStart(2, '0') + '-'
  + String(d.getDate()).padStart(2, '0'); }

var LONGNAME = {B: 'biology', C: 'chemistry', P: 'physics'};
function row(x){
  var per = {biology: null, chemistry: null, physics: null};
  x.done.forEach(function (k) { per[LONGNAME[k]] = x.per[k]; });
  return {name: x.name, school: '', avatar_url: null, rank: x.rank,
          pct: x.pct, marks: x.marks, total: x.total, secs: x.secs,
          per: per, done: x.done.map(function (k) { return LONGNAME[k]; }),
          move: x.move === undefined ? null : x.move,
          was: x.was === undefined ? null : x.was, streak: x.streak};
}

var c = new Component({});
c.props = %(props)s;
var out = {};

['Foundation', 'Higher'].forEach(function (tier) {
  ['Overall', 'Biology', 'Chemistry', 'Physics'].forEach(function (subject) {
    c.state = {wk: LIVE, tier: tier, subject: subject, open: null,
               flip: false, now: Date.parse('2026-08-25T09:00:00Z')};
    c._cache = new Map();
    var dates = c.weekDates();
    /* ⚠️ EVERY WEEK, not a sample of three. The week rail offers all nine,
       and `leaderboard_behaviour` presses every chip on it — a fixture that
       held three would have three live chips and six that looked dead, and
       the gate would report six dead controls that are really six missing
       fixtures. */
    var weeks = dates.map(function (d, i) {
      var rows = c.raw(i);
      return {week_start: iso(d.start), attempts: rows.length,
              is_current: i === LIVE,
              top_pct: rows[0] ? rows[0].pct : null};
    });
    for (var wk = 0; wk < WEEKS; wk++) {
      c.state.wk = wk;
      var b = c.board(wk);
      var pcts = b.map(function (x) { return x.pct; })
                  .sort(function (a, z) { return a - z; });
      var fastest = b.slice().sort(function (a, z) {
        return a.secs - z.secs; })[0];
      var climb = b.filter(function (x) { return x.move !== null; })
                   .sort(function (a, z) { return z.move - a.move; })[0];
      var top10 = b.slice(0, 10);
      var me = b.filter(function (x) { return x.name === VIEWER; })[0] || null;
      out[[tier, subject, iso(dates[wk].start)].join('|')] = {
        server_now: '2026-08-25T09:00:00.000Z',
        closes_at: '2026-08-28T09:15:00.000Z',
        current_week: iso(dates[LIVE].start),
        week_start: iso(dates[wk].start),
        is_current: wk === LIVE,
        tier: tier.toLowerCase(),
        subject: subject.toLowerCase(),
        weeks: weeks,
        entries: b.length,
        median_pct: pcts.length ? pcts[Math.floor(pcts.length / 2)] : null,
        fastest_secs: fastest ? fastest.secs : null,
        biggest_climb: climb && climb.move > 0 ? climb.move : null,
        cut_pct: top10.length >= 10 ? top10[top10.length - 1].pct : null,
        board: top10.map(row),
        me: me ? row(me) : null
      };
    }
  });
});
process.stdout.write(JSON.stringify({viewer: VIEWER, payloads: out}));
"""


# ── the fixture's data source ─────────────────────────────────────────────
#
# ⚑ IT IMPLEMENTS THE SAME API AS `shared/leaderboard-live.js` AND SHARES NO
# CODE WITH IT, on purpose. The seam's job is to turn a network response into
# Design's shapes; the fixture's job is to hand over shapes that are already
# right, with no network at all. Sharing an implementation would mean the
# behaviour gate exercised the fixture's copy of the mapper and told you
# nothing about the live one — and the live one is where the mapping bugs
# are. What IS shared is the interface, and that is what the gate measures.
_FIXTURE_API = r"""
/* GENERATED FIXTURE DATA — not checked in, not published. */
(function () {
  var D = %(payloads)s;
  var VIEWER = %(viewer)s;
  var START = %(start)s;
  var sel = {tier: START.tier, subject: START.subject, week: START.week};
  var redraw = function () {};
  var mounted = null;

  function initialsOf(n) {
    if (!n) { return ''; }
    var m = n.match(/^([A-Z])[a-z]*([A-Z])/);
    return m ? m[1] + m[2] : n.slice(0, 2).toUpperCase();
  }
  function key() { return [sel.tier, sel.subject, sel.week].join('|'); }
  function cur() { return D[key()] || null; }

  var TO_KEY = {biology: 'B', chemistry: 'C', physics: 'P'};
  function safeAvatar(u) {
    if (typeof u !== 'string' || !u) { return null; }
    if (!/^(https?:\/\/|\/)/i.test(u)) { return null; }
    if (/["'\\\s()<>;]/.test(u)) { return null; }
    return u;
  }
  function mapRow(r) {
    if (!r) { return null; }
    var p = r.per || {};
    var per = {B: p.biology == null ? null : p.biology,
               C: p.chemistry == null ? null : p.chemistry,
               P: p.physics == null ? null : p.physics};
    var done = [];
    (r.done || []).forEach(function (s) {
      var k = TO_KEY[s];
      if (k && per[k] != null && done.indexOf(k) < 0) { done.push(k); }
    });
    return {name: r.name, rank: r.rank, pct: r.pct, marks: r.marks,
            total: r.total, secs: r.secs, per: per, done: done,
            avatar_url: safeAvatar(r.avatar_url),
            move: (r.move === undefined ? null : r.move),
            was: (r.was === undefined ? null : r.was),
            streak: r.streak || 0};
  }

  var api = {
    status: function () { return %(status)s; },
    payload: cur,
    stateFor: function (cmp) {
      var st = (cmp && cmp.state) || {};
      return {wk: api.weekIndex(), tier: sel.tier, subject: sel.subject,
              open: st.open == null ? null : st.open,
              flip: !!st.flip, now: st.now || Date.now()};
    },
    weeks: function () { var d = cur(); return (d && d.weeks) || []; },
    weekIndex: function () {
      var w = api.weeks();
      for (var i = 0; i < w.length; i++) {
        if (w[i].week_start === sel.week) { return i; }
      }
      return api.liveIndex();
    },
    liveIndex: function () {
      var w = api.weeks();
      for (var i = 0; i < w.length; i++) { if (w[i].is_current) { return i; } }
      return Math.max(0, w.length - 1);
    },
    topFor: function (i) {
      var w = api.weeks()[i];
      return (w && w.top_pct != null) ? {pct: w.top_pct} : null;
    },
    rows: function () {
      var d = cur();
      return (d && d.board) ? d.board.map(mapRow) : [];
    },
    me: function () { var d = cur(); return (d && d.me) ? mapRow(d.me) : null; },
    isCurrent: function () { var d = cur(); return !!(d && d.is_current); },
    now: function () { return Date.parse('2026-08-25T09:00:00Z'); },
    closesAt: function () {
      var d = cur();
      return d && d.closes_at ? Date.parse(d.closes_at) : null;
    },
    viewerName: function () { return VIEWER; },
    viewerInitials: function () { return initialsOf(VIEWER); },
    isYou: function (n) { return !!VIEWER && n === VIEWER; },
    select: function (p) {
      if (p.tier) { sel.tier = p.tier; }
      if (p.subject) { sel.subject = p.subject; }
      if ('week' in p) { sel.week = p.week; }
      /* ⚠️ THE SAME FALLBACK THE SEAM HAS. A tier or subject press keeps the
         DATE; if the new axis has no such week the index falls back to that
         axis's current week. Without this the fixture would resolve to a
         missing key and render an empty board — which would look exactly
         like the empty-week state and pass. */
      if (!D[key()]) {
        var w = api.weeks();
        for (var i = 0; i < w.length; i++) {
          if (w[i].is_current) { sel.week = w[i].week_start; break; }
        }
      }
      redraw();
    }
  };
  window.MrBadmusLeaderboardLive = api;

  var boot = window.__MRB_MOUNT__;
  window.__MRB_MOUNT__ = function () {
    mounted = boot();
    redraw = function () { if (mounted) { mounted.schedule(); } };
    return mounted;
  };
})();
"""


def _clone(p):
    return json.loads(json.dumps(p))


def _shape_empty(p):
    """A week nobody sat. ⚠️ The live state of Higher/Overall on 25 Aug."""
    p["entries"] = 0
    p["board"] = []
    p["me"] = None
    for k in ("median_pct", "fastest_secs", "biggest_climb", "cut_pct"):
        p[k] = None
    for w in p["weeks"]:
        if w["week_start"] == p["week_start"]:
            w["attempts"], w["top_pct"] = 0, None
    return p


def _shape_thin(p):
    """ONE entrant — the state that found R16."""
    p["board"] = p["board"][:1]
    p["board"][0]["rank"] = 1
    p["entries"] = 1
    p["median_pct"] = p["board"][0]["pct"]
    p["fastest_secs"] = p["board"][0]["secs"]
    # ⚠️ cut_pct NULL WITH entries 1, which is exactly what the live backend
    # returned for Foundation's current week. Design would print NO ENTRIES.
    p["cut_pct"] = None
    p["biggest_climb"] = None
    p["me"] = None
    return p


def _shape_weekone(p):
    """The first week of a year — nothing to have moved from."""
    for r in p["board"]:
        r["move"] = None
        r["was"] = None
        r["streak"] = 1
    if p.get("me"):
        p["me"]["move"] = None
        p["me"]["was"] = None
        p["me"]["streak"] = 1
    p["biggest_climb"] = None
    p["weeks"] = p["weeks"][:1]
    p["weeks"][0]["is_current"] = True
    p["weeks"][0]["week_start"] = p["week_start"]
    p["is_current"] = True
    p["current_week"] = p["week_start"]
    return p


# ⚠️ THE OUTSIDE FIXTURE'S VIEWER IS THIS PERSON, AND THE SPEC BELOW MUST SAY
# SO TOO. `me` and the viewer are THE SAME PERSON by construction in the real
# seam — `me` arrives on a payload keyed by the authenticated user, and the
# viewer name comes from that same user's profile. The first version of this
# fixture renamed the `me` row to TestViewer99 and left VIEWER as Design's
# AmberYew12, so the page rendered TWO "YOU" chips: one on board row 09 via
# `deco`'s `isYou`, and one on the pinned row. A state the product cannot
# reach, shipped as the fixture that documents what the product looks like.
# Found by LOOKING at the screenshot; no gate was watching. One now is.
OUTSIDE_VIEWER = "TestViewer99"


def _shape_outside(p):
    """A viewer below the cut: in `me`, absent from `board`."""
    me = _clone(p["board"][-1])
    me["name"] = OUTSIDE_VIEWER
    me["rank"] = 27
    me["pct"] = 41
    me["move"] = -6
    me["was"] = 21
    me["streak"] = 2
    p["me"] = me
    p["entries"] = 34
    return p


def _post_outside(shaped, key):
    """One viewer across the WHOLE fixture, not just its headline week.

    ⚠️ THE SHAPE FUNCTION ONLY EVER SEES ONE PAYLOAD, and that was not
    enough. Fixing the headline week left the other seventy-one carrying
    Design's `me` (AmberYew12) while VIEWER said TestViewer99 — two
    identities in one file. It happened not to render two YOU chips, because
    AmberYew12 is inside the top ten on those weeks and so is never pinned —
    but "happens not to" is not a property, and the drive presses every week
    chip and every subject.

    ⚑ DEEP-CLONED BEFORE MUTATION. `shaped` starts as a SHALLOW copy of the
    shared payload map, so mutating a payload here would reach into every
    OTHER fixture built afterwards. That is a cross-fixture corruption that
    would show up as an unrelated gate failing later.
    """
    for k, p in list(shaped.items()):
        if k == key or not p or not p.get("me"):
            continue
        q = _clone(p)
        q["me"]["name"] = OUTSIDE_VIEWER
        # Outside the top ten on every week, so the pinned row is the only
        # place the viewer ever appears — which is what this fixture is for.
        q["me"]["rank"] = max(int(q["me"].get("rank") or 1), 11) + 16
        shaped[k] = q
    return shaped


def _shape_signedout(p):
    """No session. The board is public; the viewer's own row is not."""
    p["me"] = None
    return p


def _shape_avatars(p):
    """R25 — faces, monograms, and one hostile URL the seam must reject."""
    # ⚠️ A REAL, SAME-ORIGIN, SERVED FILE — not a placeholder host. Pointing
    # at `https://example.test/...` made the browser attempt four DNS lookups
    # that fail, and `leaderboard_behaviour` correctly reported four console
    # errors. Silencing them with a filter would have blinded the gate to a
    # genuinely missing asset; serving a real 1x1 PNG from the fixture
    # directory removes the noise by removing its cause.
    urls = ["/leaderboard_fixtures/av.png"] * 4
    for i, r in enumerate(p["board"]):
        if i < len(urls):
            r["avatar_url"] = urls[i]
        elif i == len(urls):
            # ⚠️ THE HOSTILE ONE. A quote and a semicolon would close the CSS
            # declaration if the seam escaped instead of rejecting. It must
            # come back as Design's monogram.
            r["avatar_url"] = '/leaderboard_fixtures/av.png");color:red;a("'
        else:
            r["avatar_url"] = None
    if p.get("me"):
        p["me"]["avatar_url"] = urls[0]
    return p


def _shape_podium(p):
    """The viewer is ON the podium — R32, and the state Mide was in.

    ⚠️ NO OTHER FIXTURE COULD REACH IT. Design's sample viewer sits around
    rank 9, the outside fixture puts them at 27, and the rest have no `me`
    at all — so a viewer in the top three, which is precisely where her chip
    stopped rendering, was never once drawn by a gate. The viewer here is
    the rank-2 student, which is where Mide was when he reported it.
    """
    p["me"] = _clone(p["board"][1])
    return p


def _viewer_rank2(p):
    return p["board"][1]["name"]


def _shape_loading(p):
    """No payload has arrived yet. ⚠️ THE STATE R30's TWO DEFECTS LIVED IN.

    Every other fixture hands the seam a settled payload, which is why a
    window that is on screen for SECONDS against a cold Render dyno had no
    coverage at all: the footer read "TOP 10 ONLY \u00b7 null SAT THIS WEEK"
    and the pill read "LOCKED \u2014", and eight green fixtures said nothing.
    """
    return None


def _shape_error(p):
    """The fetch failed. No payload at all — status drives the page."""
    return None


FIXTURES = [
    dict(out="leaderboard-fixture.html", js="leaderboard-fixture.js",
         axis=("Higher", "Overall"), week="live", shape=None, status="ok",
         what="Design's own sample, Higher/Overall — a full board, a podium, "
              "a cut line, movement and streaks"),
    dict(out="leaderboard-empty-fixture.html",
         js="leaderboard-fixture-empty.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_empty,
         status="ok",
         what="a week nobody sat. ⚠️ THE LIVE LANDING STATE of "
              "Higher/Overall on 25 Aug 2026 — not a corner case"),
    dict(out="leaderboard-thin-fixture.html",
         js="leaderboard-fixture-thin.js",
         axis=("Foundation", "Overall"), week="live", shape=_shape_thin,
         status="ok",
         what="ONE entrant — the podium hides and R16's list-start defect "
              "would draw an entirely empty board. Foundation's current "
              "week, live, today"),
    dict(out="leaderboard-weekone-fixture.html",
         js="leaderboard-fixture-weekone.js",
         axis=("Higher", "Overall"), week="first", shape=_shape_weekone,
         status="ok",
         what="the first week of a year — every move NEW, every streak 1, "
              "no previous week to have climbed from"),
    dict(out="leaderboard-outside-fixture.html",
         js="leaderboard-fixture-outside.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_outside,
         status="ok", viewer=OUTSIDE_VIEWER, post=_post_outside,
         what="a viewer ranked below the cut — present in `me`, absent from "
              "`board`, so the sticky pinned row is the only place they "
              "appear"),
    dict(out="leaderboard-signedout-fixture.html",
         js="leaderboard-fixture-signedout.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_signedout,
         status="ok", viewer="",
         what="no session — `me` null, no pinned row, no YOU badge, and the "
              "board still renders because it is public"),
    dict(out="leaderboard-avatars-fixture.html",
         js="leaderboard-fixture-avatars.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_avatars,
         status="ok",
         what="rows carrying a real avatar_url — R25. The face renders "
              "inside Design's disc, a row without one keeps her monogram, "
              "no disc shows both, and a hostile URL falls back to initials"),
    dict(out="leaderboard-podium-fixture.html",
         js="leaderboard-fixture-podium.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_podium,
         status="ok", viewer_fn=_viewer_rank2,
         what="the viewer is RANK 2, on the podium — R32. Mide's own state "
              "when he reported that nothing on the board said so"),
    dict(out="leaderboard-loading-fixture.html",
         js="leaderboard-fixture-loading.js",
         axis=("Foundation", "Overall"), week="live", shape=_shape_loading,
         status="loading",
         what="no payload yet — R30. The seconds-long window a student "
              "actually sees against a cold Render dyno, and the one state "
              "no other fixture could reach because they all start settled"),
    dict(out="leaderboard-error-fixture.html",
         js="leaderboard-fixture-error.js",
         axis=("Higher", "Overall"), week="live", shape=_shape_error,
         status="error",
         what="the fetch failed — R20. Every control stays live, because "
              "the press IS the retry"),
]


# ⊕ MRB-290 R29 — the nine weeks Design's own `weekDates()` produces from the
# frozen instant (2026-08-25T12:00:00Z, TZ=UTC → Tuesday 25 Aug, whose Monday
# is the 24th), counted eight weeks back.
#
# ⚠️ THEY ARE MONDAYS, AND THAT IS CORRECT. This is Design's sample
# reproduced faithfully, not the product's calendar. Real weeks run
# FRIDAY→THURSDAY and `week_start` is the Friday — a property of the
# endpoint, handled by R8. Do not "fix" these to Fridays: it would mean
# editing her logic, which is precisely what the freeze exists to avoid.
FROZEN_WEEK_STARTS = (
    "2026-06-29", "2026-07-06", "2026-07-13", "2026-07-20", "2026-07-27",
    "2026-08-03", "2026-08-10", "2026-08-17", "2026-08-24",
)


def design_sample(logic_src, consts_src):
    """Design's own numbers, by running Design's own code under Node."""
    scratch = os.path.join(FIXTURE_OUT, "_sample.js")
    os.makedirs(FIXTURE_OUT, exist_ok=True)
    with open(scratch, "w", encoding="utf-8") as fh:
        fh.write(_SAMPLE_RUNNER % dict(
            consts=consts_src, logic=logic_src,
            props=json.dumps(PINNED_PROPS)))
    # ⊕ MRB-290 R29, second half. The frozen instant is absolute; the getters
    # Design calls on it are LOCAL. Node reads TZ from the environment, so
    # this is pinned at the process boundary rather than inside her logic —
    # which is the same reason the clock itself is pinned in the runner's
    # preamble and not by touching `weekDates()`.
    env = dict(os.environ, TZ="UTC")
    r = subprocess.run(["node", scratch], capture_output=True, text=True,
                       env=env)
    if r.returncode != 0:
        raise SystemExit(
            "build_leaderboard_port.py: could not evaluate Design's sample "
            "under Node.\n  %s\n"
            "  The fixtures carry Design's OWN numbers rather than numbers "
            "this build invented, which is what makes the behaviour gate an "
            "assertion about the port. Retyping them is not the fallback."
            % (r.stderr or "").strip()[:900])
    os.remove(scratch)
    got = json.loads(r.stdout)

    # ⚑ R29 ASSERTED, NOT ASSUMED. The whole point of freezing the clock is
    # that these fixtures are byte-identical whatever day the build runs, and
    # the only way to know the freeze is still working is to check the dates
    # it should have produced. A build on a different day with the freeze
    # broken would otherwise regenerate all sixteen files silently and the
    # gates would still pass — they measure the fixtures against themselves.
    starts = sorted({w["week_start"] for p in got["payloads"].values()
                     for w in p["weeks"]})
    if starts != list(FROZEN_WEEK_STARTS):
        raise SystemExit(
            "build_leaderboard_port.py: the fixture clock is not frozen "
            "where R29 says it is.\n"
            "  expected %s\n  got      %s\n"
            "  Design's `weekDates()` counts back from the device's current "
            "Monday, so this is what changing dates look like. Either the "
            "`Date` freeze in the runner's preamble has stopped applying, or "
            "TZ is no longer pinned to UTC at the subprocess boundary. Do "
            "NOT update the expected list to today's dates: that is the "
            "daily churn this ruling exists to remove."
            % (list(FROZEN_WEEK_STARTS), starts))
    return got


# ══════════════════════════════════════════════════════════════════════════
#  The design system, and every token it must resolve
# ══════════════════════════════════════════════════════════════════════════

def ds_css():
    """Design's six stylesheets, in Design's own link order, as one file.

    ⚠️ NOT the site's own `shared/tokens.css` and NOT `teacher-ds.css`. The
    site's copies have grown past the versions in Design's bundle, and
    sharing a file with another delivery means one design-system bump
    silently restyles a surface nobody was looking at. Three deliveries,
    three bundles, three stylesheets.
    """
    order = ["tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
             "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css",
             "styles.css"]
    out, sizes = [], []
    for rel in order:
        path = os.path.join(DS, rel)
        if not os.path.exists(path):
            raise SystemExit("build_leaderboard_port.py: missing %s" % path)
        css = open(path, encoding="utf-8").read()
        if rel.endswith("fonts.css"):
            css = css.replace("./", SERVED_FONTS)
        out.append("/* ── %s ── */\n%s" % (rel, css))
        sizes.append((rel, len(css)))
    return "\n\n".join(out), sizes


_VAR_RE = re.compile(r"var\(\s*(--[A-Za-z0-9_-]+)")
_DEF_RE = re.compile(r"(--[A-Za-z0-9_-]+)\s*:")


def check_tokens(css, tpl_json, logic):
    """Every `var(--…)` the page names must resolve, or top up by name.

    ⚑ THIS EXISTS BECAUSE ONE DID NOT RESOLVE ON THE STUDENT PAGES AND THE
    PAGE STILL LOOKED FINE. An undefined custom property is the quietest
    failure CSS has: it falls back to the inherited value and nothing
    anywhere says so. Topped up BY NAME out of the site's own tokens.css,
    never retyped; anything still unresolved stops the build.
    """
    wanted = set(_VAR_RE.findall(tpl_json)) | set(_VAR_RE.findall(logic))
    have = set(_DEF_RE.findall(css))
    missing = sorted(wanted - have)
    if not missing:
        return css, []
    site = os.path.join("shared", "tokens.css")
    lines, topped = [], []
    if os.path.exists(site):
        text = open(site, encoding="utf-8").read()
        for name in missing:
            m = re.search(re.escape(name) + r"\s*:\s*([^;}]+)[;}]", text)
            if m:
                lines.append("  %s: %s;" % (name, m.group(1).strip()))
                topped.append(name)
    still = sorted(set(missing) - set(topped))
    if still:
        raise SystemExit(
            "build_leaderboard_port.py: %d custom propert(ies) the page "
            "names are defined nowhere — not in Design's bundle and not in "
            "shared/tokens.css: %s\n"
            "  An undefined `var(--…)` renders as the inherited value with "
            "no error, so this cannot be waved through: the page would look "
            "broadly right and be wrong in a way no gate would see."
            % (len(still), ", ".join(still)))
    return css + "\n\n/* ── topped up by name from shared/tokens.css " \
                 "── */\n:root {\n%s\n}\n" % "\n".join(lines), topped


# ══════════════════════════════════════════════════════════════════════════
#  build
# ══════════════════════════════════════════════════════════════════════════

def build():
    if not os.path.exists(TEMPLATES):
        raise SystemExit(
            "build_leaderboard_port.py: %s is missing. Run `python3 "
            "student_template.py` — the template and the logic are compiled "
            "out of Design's delivery, never typed." % TEMPLATES)
    tpls = json.load(open(TEMPLATES, encoding="utf-8"))
    tpl = tpls.get(TPL_KEY)
    if not tpl:
        raise SystemExit(
            "build_leaderboard_port.py: %s has no %r entry. Add the PAGES "
            "row to student_template.py and recompile."
            % (TEMPLATES, TPL_KEY))

    print("\n\U0001F3C6  build_leaderboard_port — Design's KS4 weekly "
          "leaderboard\n")
    print("     %d ruling(s) in the register, each applied and counted."
          % len(RULINGS))

    if tpl.get("imports"):
        raise SystemExit(
            "build_leaderboard_port.py: the compiled template carries %d "
            "`x-import`(s) and this delivery ships no standalone to capture "
            "one from. `strip_nav` should have removed the only one with "
            "Design's nav." % len(tpl["imports"]))
    if not tpl.get("navStripped"):
        raise SystemExit(
            "build_leaderboard_port.py: the compiled template was not "
            "nav-stripped. R1 replaces Design's nav with the landing page's, "
            "and a page carrying BOTH would put the student-surface chevron "
            "on a public root page — which CLAUDE.md forbids — and "
            "would rebuild the nav inside the runtime host on every press.")

    # ── Design's logic, seamed once ──────────────────────────────────────
    logic, counts = seam_logic(tpl["logic"])
    print("     ⊕ logic: %d ruled edit(s) applied, every one counted"
          % counts["rulings"])

    # ── the two compiled-tree rulings, in the order that matters ─────────
    roots, n_ay = bind_initials(tpl["roots"])
    if n_ay != AY_EXPECTED:
        raise SystemExit(
            "build_leaderboard_port.py: R2 expected %d 'AY' text node(s) in "
            "the compiled template and found %d.\n"
            "  'AY' is the monogram of Design's `VIEWER = 'AmberYew12'` and "
            "is the only hard-typed identity left in the markup. Too few "
            "means the binding is not reaching them; too many means Design "
            "has drawn another and it would ship one invented student's "
            "initials to every real viewer." % (AY_EXPECTED, n_ay))

    roots, n_av = bind_avatars(roots)
    if n_av != AVATAR_DISCS_EXPECTED:
        raise SystemExit(
            "build_leaderboard_port.py: R25 expected %d monogram disc(s) and "
            "bound %d.\n"
            "  The six are the three podium places, the row avatar, and the "
            "viewer's own in both the standing card and the pinned row. Note "
            "the ORDER: `bind_avatars` must run AFTER `bind_initials`, "
            "because two of the six are Design's typed 'AY' and are not "
            "`*.initials` interpolations until R2 has rewritten them — "
            "run first it finds four and reports success."
            % (AVATAR_DISCS_EXPECTED, n_av))
    roots, n_cap = unwidth(roots)
    if n_cap != WIDTH_CAPS_EXPECTED:
        raise SystemExit(
            "build_leaderboard_port.py: R31 expected %d width-capped "
            "container and found %d.\n"
            "  Mide ruled the page fills the screen; a second capped "
            "container is one Design has newly drawn and needs its own "
            "decision, not a silent widening."
            % (WIDTH_CAPS_EXPECTED, n_cap))

    # ⚠️ BEFORE R32, DELIBERATELY. `bind_podium_you` deep-copies Design's own
    # YOU chip out of her table row, and R32's whole point is that the two
    # chips are literally the same bytes. Run after this, the clone would be
    # taken from a subtree this walk had already been over — and any future
    # fragment added to PODIUM_TYPE that matched the chip would rewrite the
    # podium's copy and not the table's, which is the drift R32 forbids.
    roots, pod_hits = repodium(roots)
    wrong = [(label, exp, pod_hits[label])
             for label, _, _, exp in PODIUM_TYPE if pod_hits[label] != exp]
    if wrong:
        raise SystemExit(
            "build_leaderboard_port.py: R34 rescales the podium's type and "
            "these size(s) did not occur the expected number of times inside "
            "the podium frame:\n%s\n"
            "  Too few means Design has redrawn that element and the size is "
            "no longer being scaled — the podium would ship half-enlarged, "
            "which looks like a design decision and is not one. Too many "
            "means the fragment now matches something else in the frame. "
            "Re-anchor against her source rather than relaxing the count."
            % "\n".join("    %-22s expected %d, rewrote %d" % (l, e, g)
                        for l, e, g in wrong))

    roots, n_you = bind_podium_you(roots)
    if n_you != PODIUM_YOU_EXPECTED:
        raise SystemExit(
            "build_leaderboard_port.py: R32 expected %d podium place(s) and "
            "gave the YOU chip to %d.\n"
            "  The three are p1, p2 and p3. Fewer means a podium name is no "
            "longer a bare `pN.name` interpolation and a viewer on that "
            "place would silently lose their marker again — which is the "
            "defect Mide reported."
            % (PODIUM_YOU_EXPECTED, n_you))

    print("     ⊕ tree:  %d monogram(s) bound to me.initials, "
          "%d disc(s) given a bound avatar,\n"
          "              %d width cap removed (R31), %d podium place(s) can "
          "wear YOU (R32),\n              podium frame capped + %d type "
          "size(s) rescaled (R34)"
          % (n_ay, n_av, n_cap, n_you, sum(pod_hits.values())))

    # ── the nav, read from the landing page ──────────────────────────────
    nav = live_nav()
    print("     ⊕ nav:   %d bytes lifted from index.html (R1)" % len(nav))

    # ── the design system ────────────────────────────────────────────────
    css, sizes = ds_css()
    tpl_json = json.dumps(roots)
    css, topped = check_tokens(css, tpl_json, logic)
    print("     ✅ tokens: every var(--…) resolves%s"
          % ((" (%d topped up from shared/tokens.css: %s)"
              % (len(topped), ", ".join(topped))) if topped else ""))

    for out_dir in (SHARED_OUT, SHARED_SRC):
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, DS_CSS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(css)
    print("     ✅ %-22s %7d bytes, %d sheet(s), linked and cached once"
          % (DS_CSS_NAME, len(css), len(sizes)))

    # ⚑ EVERY ASSET PUBLISHED BEFORE THE PAGE THAT NAMES IT IS WRITTEN, and
    # the version map built from CONTENT. `_verify_stamps` re-reads all of it
    # from disk afterwards and refuses to finish if any hash disagrees.
    versions = {DS_CSS_NAME: asset_hash(css)}

    src = os.path.join(SHARED_SRC, RUNTIME_JS_NAME)
    if not os.path.exists(src):
        raise SystemExit(
            "build_leaderboard_port.py: shared/%s does not exist and the "
            "page loads it. Without it the page mounts nothing at all."
            % RUNTIME_JS_NAME)
    runtime = open(src, encoding="utf-8").read()
    os.makedirs(SHARED_OUT, exist_ok=True)
    with open(os.path.join(SHARED_OUT, RUNTIME_JS_NAME), "w",
              encoding="utf-8") as fh:
        fh.write(runtime)
    # ⚠️ THE RUNTIME IS STAMPED TOO, and it was not on the first pass. The
    # page links `/shared/student-runtime.js` directly, so a name absent from
    # `versions` is a tag `stamp_versions` walks straight past — and
    # `_verify_stamps`'s unstamped-link sweep caught it on both trees. Every
    # asset under /shared/ is served `max-age=14400`, so an unstamped runtime
    # is today's HTML with yesterday's renderer for up to four hours after a
    # deploy.
    versions[RUNTIME_JS_NAME] = asset_hash(runtime)

    for name in STAMPED_DEPS:
        dep = os.path.join(SHARED_SRC, name)
        if not os.path.exists(dep):
            raise SystemExit(
                "build_leaderboard_port.py: shared/%s does not exist, and "
                "the leaderboard names it. A missing dependency here is a "
                "blank page or a nav that never binds." % name)
        body = open(dep, "rb").read()
        versions[name] = asset_hash(body)
        # ⚠️ ALWAYS OVERWRITE, NEVER "only if absent". A previous generator
        # run can leave a STALE copy in the published tree — one did, for
        # `leaderboard-live.js`, and publish-if-absent kept it while this
        # build stamped the hash of the CURRENT source. That is the exact
        # dishonest-stamp case `_verify_stamps` exists to catch: a `?v=`
        # naming bytes that are not the bytes being served, cached under a
        # URL that will never change again.
        with open(os.path.join(SHARED_OUT, name), "wb") as fh:
            fh.write(body)

    # ── retire the hand-written original ─────────────────────────────────
    retire_original()

    # ── the live page, into BOTH trees ───────────────────────────────────
    body = page_html(roots, tpl.get("imports") or {}, logic, nav, None,
                     versions)
    write(os.path.join(SITE_OUT, OUT_NAME), body)
    write(os.path.join(MIRROR_OUT, OUT_NAME), body)
    print("     ✅ %-22s %7d bytes → %s/ and ./ (mirror)"
          % (OUT_NAME, len(body), SITE_OUT))

    # ── the fixtures ─────────────────────────────────────────────────────
    # ⚠️ SPLIT, NOT BOTH. Design's module consts and her class live in one
    # blob; the runner emits `DCLogic` BETWEEN them, so it needs the two
    # halves separately. Passing the whole blob as the second half declared
    # `FIRST` twice and Node refused the file outright — which is the good
    # failure, but only because `const` is not `var`.
    _split = tpl["logic"].index("class Component")
    consts = tpl["logic"][:_split]
    sample = design_sample(tpl["logic"][_split:], consts)
    payloads, viewer = sample["payloads"], sample["viewer"]

    def pick(axis, when):
        tier, subject = axis
        keys = [k for k in payloads if k.startswith("%s|%s|" % (tier, subject))]
        keys.sort()
        if not keys:
            raise SystemExit(
                "build_leaderboard_port.py: Design's sample produced no "
                "payload for %s/%s." % axis)
        hit = keys[-1] if when == "live" else keys[0]
        return hit, payloads[hit]

    os.makedirs(FIXTURE_OUT, exist_ok=True)
    # A real 1x1 PNG for the avatars fixture to point at. Same origin, served
    # by the gate's own root server, so no DNS lookup and no console noise.
    with open(os.path.join(FIXTURE_OUT, "av.png"), "wb") as fh:
        fh.write(base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8"
            "z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="))
    for spec in FIXTURES:
        key, base = pick(spec["axis"], spec["week"])
        shaped = dict(payloads)
        if spec["shape"] is not None:
            one = spec["shape"](_clone(base))
            shaped[key] = one
            if one is None:
                shaped = {}
        elif spec["shape"] is None and spec["status"] == "error":
            shaped = {}
        if spec.get("post") and shaped:
            shaped = spec["post"](shaped, key)
        tier, subject = spec["axis"]
        # ⊕ R32's fixture names its viewer FROM THE DATA rather than from a
        # literal: the podium fixture's viewer must BE the rank-2 student,
        # and hardcoding a name would silently stop being that student the
        # day the frozen sample shifts.
        who = spec.get("viewer", viewer)
        if spec.get("viewer_fn"):
            who = spec["viewer_fn"](shaped[key])
        start = dict(tier=tier, subject=subject, week=key.split("|")[2])
        js = _FIXTURE_API % dict(
            payloads=json.dumps(shaped, separators=(",", ":")),
            viewer=json.dumps(who),
            start=json.dumps(start),
            status=json.dumps(spec["status"]))
        with open(os.path.join(FIXTURE_OUT, spec["js"]), "w",
                  encoding="utf-8") as fh:
            fh.write(js)
        fix = page_html(roots, tpl.get("imports") or {}, logic, nav,
                        spec["js"], versions)
        write(os.path.join(FIXTURE_OUT, spec["out"]), fix)
    print("     ✅ %d fixture(s) → %s/  (Design's own numbers, "
          "evaluated;\n        outside every tree generate_site_v5 publishes "
          "or round-trips)" % (len(FIXTURES), FIXTURE_OUT))

    _verify_stamps(versions)

    print("\n     → %s/%s  and  ./%s  (mirror)\n"
          % (SITE_OUT, OUT_NAME, OUT_NAME))
    return 0


def main():
    os.chdir(REPO)
    return build()


if __name__ == "__main__":
    raise SystemExit(main())
