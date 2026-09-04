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
    RETARGET_ON       a node moved from one of Design's handlers to ANOTHER,
                      asserting the one it is moving off. The mechanism for
                      the case `NAV` structurally cannot serve: two nodes
                      sharing one handler name, where only one of them should
                      still go where that handler goes.
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — RE-ANCHORED ON v3, AND TWO ROWS ADDED.
#
# ⛔ THE DEFECT THIS TABLE CARRIED. The v3 port re-indexed `NAV` and stopped.
# Every other node-indexed ruling in this file — this one included — was still
# holding Design's v2 numbering, and v2's numbering is not wrong in a way any
# gate could see: `28` is a real node in v3 too. It is the wrong one.
#
# ⚠️ AND THE ROW THAT WAS NOT HERE AT ALL WAS THE DANGEROUS ONE. v3 opens with
# TWO NEW SCREENS — `isToday` (node 32) and `isTimetable` (node 96) — and this
# dict is what makes each page prune the screens it is not. A screen that is
# not named here is not pruned by anybody, so all six pages would have shipped
# Today AND Timetable stacked on top of their own content, and every gate
# would have stayed green: the build asserts that what it names is present,
# never that what it does not name is absent.
#
# They are named here for exactly the reason `import` still is — every OTHER
# page has to prune it — and for no other. Today and Timetable are hand-written
# pages today (`teacher/today.html`, `teacher/timetable.html`); bringing them
# into the generator is a later unit, and this row does not do it.
#
#   key          v2 (as ruled)     v3 (this table)
#   today        — absent —        32
#   timetable    — absent —        96
#   classes      28                157
#   class        80                207
#   student      209               329
#   marking      245               369
#   digest       299               427
#   import       333               461
#   insights     388               516
SCREENS = {
    "today":     32,
    "timetable": 96,
    "classes":  157,
    "class":    207,
    "student":  329,
    "marking":  369,
    "digest":   427,
    "import":   461,
    "insights": 516,
}


# ── ⊕ RULED BY MIDE, 1 Sep 2026 · THE CLASS-DETAIL WEEK BAR STAYS ────────
#
# ⛔ DESIGN'S v3 DELETED IT. The class screen's week rail — twelve chips, a
# chevron either side, and every figure below scoped to the chip you pressed
# — is gone from the v3 delivery, replaced by a dated assignment table and a
# `glance` block. Mide overrode that on 1 Sep 2026: the bar stays.
#
# This constant exists so that the decision is a RECORDED RULING rather than
# a gap somebody closes by reading the drawing. The next port reads Design's
# file, finds no week bar, and — without this — deletes it again as drift.
# `IMPORT_NOT_PORTED` is here for the same reason and was written for the
# same failure.
#
# ── WHAT IS DELIBERATELY DIFFERENT FROM v2 ──────────────────────────────
#
# ⚠️ **v2's RAIL WAS INDEXED BY ASSIGNMENT. THIS ONE IS INDEXED BY TEACHING
# WEEK.** That is the whole of the difference and it is invisible in Design's
# file, because her sample class has exactly one assignment per week for
# twelve weeks — so "week 3" and "the third paper" are the same object and
# nothing can tell them apart. `8r/Sc1`, the only class in the working year
# with any assignments, has TWO against a thirty-nine-week year. Copied
# forward, the bar would have drawn two chips and called them the term.
#
#   · `weeks()` is the academic year's teaching weeks (seam: `buildWeeks`),
#     newest first, at most twelve, and NEVER a week from before the year
#     began — on the first day of term that is one chip, marked "This week",
#     and that is correct rather than broken.
#   · `weekIdxFor` clamps to `weeks().length`, not to `papersFor(k).length`.
#   · Papers map ONTO weeks by the week they were SET in (seam:
#     `assignPaperWeeks`) — v2's own embedded rule, kept: "a week's range is
#     the teaching week it was set in, not the week its deadline falls in".
#   · A week with NO assignment is a real, drawable state. v2 could not
#     produce one, so Design never drew one; it says "No work set in this
#     week" in words and invents no date.
#   · The chips' second line is filled on every chip — "This week", or the
#     term-relative label. v2 left eleven of twelve blank because its ranges
#     were self-identifying inside its own fiction.
#
# ── WHAT IS UNCHANGED FROM v2, DELIBERATELY ─────────────────────────────
#
#   · `rail()`, `snapWeekRail()` and `pickWeek()` are v2 verbatim (LOGIC #36).
#   · The markup is v2's, style string for style string, with ONE structural
#     change: the chip's `sc-if w.now` wrapper is gone, because that line now
#     carries text on every chip and an always-true `if` is a control nobody
#     can tell from a broken one.
#   · `weekIdx: 0` is the CURRENT week and the list counts backwards, so
#     `wPast = wi > 0`, back is `wi + 1` and forward is `wi - 1` — Design's
#     own directions, and every consumer still reads them that way.
#
# ── THE ONE APPROXIMATION, STATED ───────────────────────────────────────
#
# ⚠️ THERE IS NO `terms` TABLE. Checked, not assumed: `academic_years` holds
# a start date and an end date and nothing else. So "Autumn Week 6" is
# derived — the term from the week's own Monday against `seasonFor`'s
# Sep-Dec / Jan-Mar / Apr-Aug boundaries, the number by counting weeks since
# the year began. Half terms and a moving Easter are not in the data, so the
# count runs straight through the holidays and the week after Christmas reads
# "Autumn Week 18". A `terms` table would make it exact. That is Mide's call,
# and it is in the handover.
WEEK_BAR_RESTORED = dict(
    screen="teacher/class-detail.html",
    ruled_by="Mide",
    ruled_on="2026-09-01",
    against="Design's v3 delivery, which removed the rail",
    logic=("#6 the roster column, #13 the week scope and everything it "
           "reaches, #36 the four methods and the cold-load hooks, plus the "
           "week-bar entries appended at the end of LOGIC"),
    markup="INSERT_AT[(208, 218)]",
    seam="shared/teacher-live.js — buildWeeks / assignPaperWeeks",
    indexed_by="teaching week, NOT assignment",
    approximation="term boundaries and the within-term week number are "
                  "derived from the year's start and end dates; there is no "
                  "`terms` table, so half terms are counted as teaching "
                  "weeks. Open on Mide.",
)

# ── the four overlays ────────────────────────────────────────────────────
#
# `setWorkOpen` is on this list so the build can PRUNE it by name on every
# page rather than by an index typed in seven places. It is kept by none of
# them; see `DEAD`.
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3. 453→581, 500→628,
# 525→655, 541→671. The four overlays survive v3 unchanged in shape; only
# their numbering moved, behind the two screens Design added above them.
OVERLAYS = {
    "setWorkOpen": 581,
    "bulkOpen":    628,
    "searchOpen":  655,
    "hasToast":    671,
}

# ── ⊕ RULED BY MIDE, 3 Sep 2026 · THE SHOUTOUT SURFACE COMES BACK ───────
#
# **THIS SUPERSEDES `SHOUTOUT_COMPOSER_DROPPED` AND `SHOUTOUT_MARKUP_PARKED`,
# which stood here from 2 Sep 2026 to 3 Sep 2026 and recorded the deletion as
# accepted-and-open.** Both names are written out in full here so that a
# reader who greps for either lands on this ruling rather than on nothing.
# They are GONE, not renamed: leaving them in place would have left the file
# saying two contradictory things about the same markup, which is the exact
# failure mode this file exists to prevent.
#
# ── WHAT THEY SAID, AND WHY IT IS NO LONGER TRUE ────────────────────────
#
# `SHOUTOUT_COMPOSER_DROPPED` recorded that Design's v3 deleted v2's nodes
# 181-208 — the "Shoutouts" heading, the single-student composer and the
# whole feed — and listed three ways the port could go, of which it took
# none, because the choice was Mide's and he had not made it. It named three
# rulings left without a surface:
#
#     Mide 2026-08-24 — a teacher who can post a shoutout can remove one
#     MRB-287       — the recipient is an id, not a name
#     MRB-261       — a past academic year is read-only
#
# `SHOUTOUT_MARKUP_PARKED` held the two `INSERT_AT` subtrees for the Remove
# control and its confirm sheet, verbatim, against the day the feed came back.
#
# **Mide ruled on 3 Sep 2026: RESTORE, as a deliberate divergence from v3.**
# His 1 Sep free-text ruling — that a teacher may write their own words to a
# child, alongside the six templates — POSTDATES Design's deletion and
# supersedes it. A composer that can only be reached through a bulk sheet,
# with no feed to read back, is not the surface that ruling describes.
#
# ⚠️ SO THIS IS DIVERGENCE-BY-RULING, NOT A DESIGN OMISSION, and the
# distinction is the whole reason this constant exists. v3 IS DRAWN WITHOUT A
# COMPOSER AND WITHOUT A FEED. A future port that reads the drawing, finds no
# composer on the page and removes one will be helping, carefully, and will be
# destroying a ruling. `WEEK_BAR_RESTORED` is the precedent and this follows
# it exactly: the drawing is not the authority here, Mide is.
#
# ── WHAT IS RESTORED, AND WHERE ─────────────────────────────────────────
#
#   `INSERT_AT[(208, 306)]`   the "Shoutouts" section — heading, the composer
#                             card and the feed column — placed AFTER the
#                             assignments table (node 306), which is where v2
#                             drew it: below the work, at the foot of the
#                             class.
#   `INSERT_AT[(208, None)]`  the confirm sheet in front of the removal.
#                             Re-anchored from the parked `(81, None)`; 81 was
#                             v2's class-screen root and 208 is v3's. The
#                             markup itself is unchanged.
#
# ── IT IS DRAWN IN v3'S LANGUAGE, NOT TRANSPLANTED FROM v2 ──────────────
#
# ⚑ v3 HAS ITS OWN SHOUTOUT COMPOSER AND THIS IS BUILT OUT OF IT. The bulk
# sheet (nodes 646-651) is Design's v3 drawing of exactly this control —
# a `.16em` mono caption at `margin-top:22px`, a template grid at
# `repeat(auto-fit,minmax(240px,1fr))` with `gap:8px;margin-top:12px`, her
# template button at `padding:12px 13px;font:600 16.5px/1.25`, and a
# free-text `<textarea>` at `min-height:70px` under "Or write a message"
# that v2 did not have at all. Every one of those strings is read off v3
# rather than off v2. The section heading is node 283's (`margin:26px 0 12px`,
# a 33px display `h2`), the cards are the roster and assignments cards'
# (`border-radius:11px`), and the feed row's avatar is `glance.praise`'s
# (node 271, `font:600 11.5px/1 var(--st-mono)`) rather than v2's 12px one.
#
# What is v2's, deliberately, is the SHAPE: a composer beside a feed in a
# two-column auto-fit grid, because that is the arrangement Mide is restoring
# and there is no v3 counterpart to read it off.
#
# ⚠️ THE RECIPIENT IS A `<select>`, AND v3 CONTAINS NO OTHER ONE. Checked
# rather than assumed: v3's only form controls are the bulk textarea (651)
# and the search input (662). The select is Design's own, from v2's node 187,
# and three things make it the right restoration rather than the lazy one —
# Design's SURVIVING handler `pickRecipient: (e) => this.setState({recipient:
# e.target.value})` reads `e.target.value` and so needs a valued field;
# `MRB_COMPOSE_RESET` clears `[data-compose-field]` by `.value` for the same
# reason; and v3's own student picker is a MULTI-select chip row, which is a
# different control answering a different question. A chip row here would
# have meant rewriting a handler Design kept.
#
# ── THE THREE RULINGS THAT GET THEIR SURFACE BACK ───────────────────────
#
#   · **Mide, 24 Aug 2026 — a teacher who can post a shoutout can remove
#     one.** `softDeleteClassShoutout` has existed since MRB-46 and has been
#     reachable from nowhere in the ported estate since 2 Sep. The feed row
#     carries the Remove control again and `MRB_DELETE_SHOUTOUT` is live.
#   · **MRB-287 — the recipient is an id, not a name.** v2 needed `BIND_ATTR`
#     to fix Design's `value="{{ s.name }}"`; the restored option is written
#     with `{"e": "s.id"}` from the start, so there is nothing to correct
#     after the fact. `insertClassShoutout` needs `recipient_id`, RLS checks
#     the recipient is a CURRENT member of the class, and two children in one
#     class can share a name.
#   · **MRB-261 — a past academic year is read-only.** See below; it is the
#     one that had to be built differently rather than merely restored.
#
# ── ⛔ THE READ-ONLY YEAR, AND WHY `WRAP` COULD NOT DO IT ───────────────
#
# `WRAP` is keyed by DESIGN'S node index, and every node in this restoration
# is inserted markup carrying no `i` at all — that is `INSERT_AT`'s own rule,
# so that Design's numbering never moves. There is no index to wrap.
#
# So the gate is an `<if>` on `canWrite` INSIDE the inserted subtree, at the
# composer card, and it is the same predicate `WRAP` puts on nodes 215 and
# 276. Three write surfaces, one key, and they cannot disagree.
#
# ⚠️ THE FEED IS NOT INSIDE THAT `if`, AND MUST NOT BE. MRB-261 makes a
# finished year READ-ONLY, not invisible: what a teacher wrote about a child
# last year is still theirs to read. The DELETE control inside the feed is
# separately gated — `f.canDelete` already reads `MRB_DATA('canWrite')` (see
# the `feed:` entry in LOGIC), so the destructive half goes with the composer
# and the readable half stays.
#
# ⚠️ AND IT IS ASSERTED NOW, NOT MERELY DESCRIBED. `teacher_behaviour`'s own
# docstring records what the previous shape of this cost: it DESCRIBED the
# read-only guarantee and asserted nothing, so when v3's deletion took the
# wrapped nodes away the guarantee quietly stopped holding and every gate
# stayed green. The `needs_write` flag on the four composer additions is the
# fix — on a read-only fixture the gate now requires those markers to be
# ABSENT from the DOM, and says so by name when they are not.
#
# ── THE GUARDRAILS, AND WHERE EACH ONE ACTUALLY LIVES ───────────────────
#
#   auditable          the feed is on the class page for every teacher of the
#                      class, and Mide's ruling 2 of 3 Sep widened
#                      `class_shoutouts` RLS so a school admin reads
#                      school-wide. Nothing here is private to its author.
#   one-way            THERE IS NO STUDENT REPLY PATH AND NONE IS ADDED. The
#                      student surface (`student/class.html`) renders
#                      shoutouts through `shoutouts.js` READ-ONLY; there is
#                      no student INSERT policy on `class_shoutouts` and this
#                      restoration adds no control, no field and no write
#                      that a student can reach.
#   context-bound      every row is `(class_id, recipient_id)`. There is no
#                      general inbox and no way to compose one from here: the
#                      composer's recipient list IS this class's roster.
#   attributed         the feed row says who wrote it — `f.by`, added to
#                      `buildFeed` in `shared/teacher-live.js` off the RPC's
#                      own author join. Before this it carried `author_id`
#                      and no name, so a colleague's shoutout was unsigned.
#   retained           removal is a SOFT delete (`deleted_at`); the body is
#                      never overwritten and there is no edit path at all, so
#                      there is no prior body to keep. Stated rather than
#                      implied: the retention guardrail is satisfied by the
#                      absence of an editor, not by a column.
#   plain text         `student-runtime` writes every interpolation with
#                      `document.createTextNode` (student-runtime.js:138).
#                      There is no `innerHTML` on this path, no markdown pass
#                      and no linkifier anywhere in the estate.
#   links inert        follows from the line above and is checked rather than
#                      assumed: a body of "see https://example.com" renders
#                      as those characters inside a `<span class="sc-interp">`
#                      and produces no `<a>`. ⛔ DO NOT ADD ONE. A teacher's
#                      shoutout is read by a child; an anchor in it is a
#                      link an adult put in front of a child that nobody
#                      reviewed.
#   length cap         500 characters, which is `class_shoutouts_message_
#                      length_chk` in the database. `noteCount` renders
#                      "N / 500" and `sendShoutout` refuses above it. ⚠️ NOT
#                      2000 — that is `submission_feedback`, a different
#                      table with a different cap.
SHOUTOUT_SURFACE_RESTORED = dict(
    screen="teacher/class-detail.html",
    ruled_by="Mide",
    ruled_on="2026-09-03",
    against="Design's v3 delivery, which deleted the composer and the feed",
    supersedes=("SHOUTOUT_COMPOSER_DROPPED", "SHOUTOUT_MARKUP_PARKED"),
    markup="INSERT_AT[(208, 306)] the section; INSERT_AT[(208, None)] the "
           "confirm sheet",
    logic="the `feed:` entry and the `sendShoutout` / `closeModal` entries in "
          "LOGIC, all of which already applied — Design kept the HANDLERS in "
          "v3 and deleted only the markup",
    seam="shared/teacher-live.js — buildFeed, which now carries `by`",
    read_only="an `<if>` on `canWrite` inside the inserted subtree, because "
              "WRAP is keyed by Design's node indices and inserted markup "
              "has none; asserted by teacher_behaviour's `needs_write`",
    rulings_given_a_surface_again=(
        "Mide 2026-08-24 — a teacher who can post a shoutout can remove one",
        "MRB-287 — the recipient is an id, not a name",
        "MRB-261 — a past academic year is read-only",
    ),
)


# ── ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK IS A NEW SURFACE ──────
#
# ⛔ DESIGN DREW NO PER-SUBMISSION FEEDBACK UI, ANYWHERE, IN ANY VERSION.
# This is not a control she drew and removed — the way the week bar and the
# shoutout composer were — and there is therefore no drawing to be faithful
# to and none to check this against. `WEEK_BAR_RESTORED` and
# `SHOUTOUT_SURFACE_RESTORED` are RESTORATIONS; this is an ADDITION, and it
# is written down here for exactly the reason those two are: the next port
# reads Design's delivery, finds no feedback surface, and — without this —
# removes it as drift.
#
# ⚑ MIDE'S BRIEF: feedback is "authored from student detail or marking,
# attached to that submission", and the student reads it under their
# automated marking with the teacher's display name.
#
# ── THE GUARDRAILS, AND WHERE EACH ONE IS ACTUALLY ENFORCED ─────────────
#
# These are Mide's defaults. He may loosen them; this build may not. Two of
# the six are not enforceable in a browser at all, which is why they are in
# the database and not here:
#
#   auditable ...... `submission_feedback_select` admits school admins and
#                    (ruling 3, 3 Sep) `slt`, school-wide. DATABASE.
#   ONE-WAY ........ there is no student INSERT policy. DATABASE — and
#                    nothing in this port offers a reply either, not a
#                    disabled one and not one behind a flag. See below.
#   context-bound .. `submission_id` NOT NULL and no second binding, so
#                    there is no inbox this can be reached from. DATABASE.
#   attributed ..... `teacher_id`. The TEACHER side renders "You" or
#                    "Another teacher"; the STUDENT side renders the
#                    teacher's display name where it can prove one. See the
#                    limitation below — it is real and it is reported.
#   retained ....... `CHECK ((edited_at IS NULL) = (prior_body IS NULL))`.
#                    DATABASE, and it is the good kind: the client cannot
#                    forget to keep the prior body, because a write that
#                    forgot is refused.
#   plain text ..... every render is a text node. `student-runtime` writes
#                    interpolations with `createTextNode`; there is no
#                    `innerHTML` on this path, no markdown and no linkifier,
#                    so a URL a teacher types renders as characters. PROVEN
#                    BY INJECTION on this surface rather than carried over
#                    from the shoutout unit.
#   length cap ..... 2000 (`submission_feedback_body_length_chk`), on the
#                    textarea's `maxlength`, in the counter and in front of
#                    the write. NOT 500 — that is `class_shoutouts`.
#
# ── ⛔ ONE-WAY MEANS ONE-WAY, AND IT IS A PROPERTY RATHER THAN A CHOICE ──
#
# There is no reply control on the student side. Not a disabled one, not a
# hidden one, and not a field that a flag could turn on later: the student
# read is a READ — `shared/student-live.js` fetches the row and draws text —
# and there is no student write path in `student-data.js` for one to be
# wired to. A control a child could see and could not use would be a promise
# the RLS refuses, and it would be a promise made to a child.
#
# ── ⚠️ THE ONE THING THIS SURFACE CANNOT DO, STATED ─────────────────────
#
# A TEACHER cannot be shown a COLLEAGUE's NAME on this screen, and a STUDENT
# cannot be shown the author's name on a CO-TAUGHT class. Both have the same
# cause, measured rather than assumed: neither role has a SELECT policy on
# another teacher's `profiles` row, so a `teacher:profiles(display_name)`
# join comes back NULL with no error at all.
#
# The estate already has the answer and has used it twice — a SECURITY
# DEFINER RPC (`class_teachers_for_viewer`, `student_reminders_for_viewer`)
# — and a third of the same shape would close this. It is not written here
# because it is a change to a LIVE database and this unit was scoped to
# build to a store that already exists. So:
#
#   teacher side ... "You" / "Another teacher". Both true, neither invented.
#   student side ... the class's teacher's display name, taken from
#                    `class_teachers_for_viewer`, WHERE THE CLASS HAS EXACTLY
#                    ONE TEACHER — which is unambiguous. Where it is
#                    co-taught, "Your teacher", the same restraint
#                    `teacherName` already takes on the class page. A name
#                    that might be the wrong teacher's is worse than no name.
#
# ⚠️ DO NOT "FIX" THIS BY PICKING THE FIRST TEACHER IN THE LIST. The RPC
# returns names WITHOUT ids, ordered by subject then name; there is no
# mapping from `teacher_id` to any of them, and guessing would attribute one
# teacher's words to another in front of a child.
#
# ── ⊕ 4 Sep 2026 — HALF OF THAT IS NOW CLOSED, AND THE OTHER HALF IS NOT ─
#
# Mide approved the third RPC. `submission_feedback_authors_for_viewer` is
# LIVE ON PROD (migration `20260904214520`): it returns
# `{teacher_id: display_name}` for exactly the feedback rows the CALLING
# STUDENT may already read on one assignment, and nothing else. So the
# STUDENT side names the author on a co-taught class now.
#
# ⚠️ THE FALLBACK ABOVE IS NOT DELETED AND MUST NOT BE. It is what the page
# does when the mapping is empty — an older database, a failed request, an
# author whose profile has gone — and the "never guess" rule is unchanged.
#
# ⚠️ THE TEACHER SIDE IS STILL "Another teacher", DELIBERATELY. The new RPC
# is scoped to `s.student_id = auth.uid()`, which a teacher session cannot
# satisfy; naming a colleague from a teacher session is a different scope and
# a different ruling, and it is left open rather than quietly widened.
#
# ⊕ AND ONE MEASURED CORRECTION TO THE PARAGRAPH ABOVE, kept because the
# paragraph is what a future reader will act on: "neither role has a SELECT
# policy on another teacher's `profiles` row" is true, but it was NOT the
# whole picture. `public.display_name_for(uuid)` has been on prod all along —
# STABLE SECURITY DEFINER, it returns the display name of any teacher who
# teaches a class the CALLER IS A MEMBER OF. So the student half of this
# limitation was always soluble with no new DDL at all, one id at a time, and
# nobody had noticed. It was found on 4 Sep 2026 by the TEST proof of the new
# function, not by reading. The new RPC is still the one wired up (feedback
# AUTHORS only rather than every teacher of the class; one round trip rather
# than N; and it still names someone who has since left the class) — but the
# claim "there is no mapping" was too strong, and a future limitation note
# should be checked against `pg_proc` before it is believed.
FEEDBACK_SURFACE_ADDED = dict(
    screens=("teacher/student-detail.html", "teacher/assignment.html",
             "student/assignment.html"),
    ruled_by="Mide",
    ruled_on="2026-09-03",
    against="Design's v3 delivery, which draws no feedback surface at all",
    store="submission_feedback — migration 20260902221216, widened for `slt` "
          "by 20260903200007. LIVE ON PRODUCTION.",
    markup="INSERT_AT[(366, 367)] and [(420, 422)] the row controls; "
           "INSERT_AT[(330, None)] and [(370, None)] the sheet, from one "
           "builder",
    logic="the three feedback entries at the end of LOGIC, plus the six "
          "`fb*` keys in the state initialiser",
    seam="shared/teacher-live.js — buildFeedback and the `subId` arrays on "
         "the matrix and the grid; shared/teacher-data.js — four functions",
    student_read="shared/student-live.js — drawFeedback, after the mount, "
                 "under the automated marking. ⊕ 4 Sep 2026: AND on the "
                 "IN-PROGRESS screen, `student_rulings.INSERT_AT[(106, "
                 "251)]` — Mide ruled that a teacher MAY comment on "
                 "started-but-not-handed-in work, so a child has to be able "
                 "to read it while the work is still open. Same four keys, "
                 "one read, two screens. A READ and nothing else on both: "
                 "no save path, no offline queue, no submission write.",
    one_way="no reply control exists on the student side, disabled or "
            "otherwise, and there is no student INSERT policy to wire one to",
    limitation="⊕ 4 Sep 2026 — HALF CLOSED. The author's name IS reachable "
               "from a student session now, on a co-taught class, through "
               "`submission_feedback_authors_for_viewer` (prod migration "
               "20260904214520) — with the single-teacher/'your teacher' "
               "fallback KEPT for when the mapping is empty. Still open: a "
               "colleague's NAME from a TEACHER session, which renders "
               "\"Another teacher\". That is a different scope (the new RPC "
               "is scoped to the caller's own submissions) and a different "
               "ruling, and it is left open rather than quietly widened.",
)


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
    screen_node=333,
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3. Every row was still
# holding a v2 index; each moved to the node carrying the SAME tag and the
# SAME handler in v3, verified by structural diff of the two compiled trees
# rather than by reading the drawing:
#
#   453 → 581  the Set-work sheet          (`if setWorkOpen`)
#    36 → 165  classes screen "Set work"   (`button openSetWork`)
#    87 → 214  class screen "Set work"     (`button openSetWork`)
#   180 → 282  the no-work empty state     (`button openSetWork`)
#   254 → 382  the marking header action   (`button openSetWork`)
#    67 → 194  the class card's "Set work" (`button c.act`)
#
# ⚠️ v3 draws a SIXTH `openSetWork` at node 40, on the new Today screen. It is
# not listed: `SCREENS` prunes Today whole on all six pages, and the build's
# own sweep refuses a DEAD node that survives on no page.
DEAD = (
    (581, "the Set-work sheet itself. Three steps, a summary line and a "
          "confirm button, in front of a write path that does not exist."),
    (165, "\"Set work\" — the primary action on the classes screen."),
    (214, "\"Set work\" — the primary action on the class screen."),
    (282, "\"Set work\" — the empty-state prompt on a class with no "
          "assignments. The emptiest possible dead control: it is the only "
          "thing on screen and it does nothing."),
    (382, "\"Reteach and reset\" — the marking screen's header action. It "
          "is drawn by `openSetWork` and opens the same sheet."),
    (194, "\"Set work\" on a class card that has students but no work set. "
          "See the note above for why its twin at node 198 survives."),

    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — AND ONE THAT LIES RATHER THAN DOES
    # NOTHING, WHICH IS WORSE. Node 236 is v3's "Remind all N" in the class
    # glance, and Design's handler is
    # `remind: () => this.ping('Reminder sent to N students in 8r/Sc1')` — a
    # toast asserting a send, in front of no write at all. A teacher presses
    # it, reads that N children were reminded, and nothing was.
    #
    # ⚠️ THIS IS NOT A LOST AFFORDANCE. `shared/teacher-live.js` INJECTS a
    # real reminder control onto this same page after mount
    # (`drawRemindControl`, MRB-306 WS-3), backed by `remindersForClass` and
    # a unique index that stops a second reminder the same day. Its own
    # comment already anticipates this exact moment: "Her v3 delivery DOES
    # draw 'Send reminders' and 'Remind all N'; when that port lands this
    # injection is deleted and the real control takes over." Swapping the two
    # is that port's job — a one-line deletion in the seam plus a NAV entry
    # here. Until then the page carries ONE remind control and it is the one
    # that works.
    (236, "\"Remind all N\" in the class glance. It toasts \"Reminder sent "
          "to N students\" and sends nothing. The working reminder control "
          "on this page is the one teacher-live.js injects; this is its "
          "duplicate, and it lies."),
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — 27 → 31. Design's v3 top bar grows a tab
# strip and a `hasCrumb` wrapper ahead of it, so the "Sign out" button (still a
# `<button>` with no handler at all, still on every screen) moved four places.
SET_ON = {
    31: "signOut",
}


# ── ⊕ RULED, MRB-304 · THE BRAND MARK GOES HOME ──────────────────────────
#
# ⛔ THE DEFECT. Design's top bar hangs `goClasses` on the brand mark (node
# 11), and `NAV["goClasses"]` rewires that handler to `MRB_GO('classes', …)`.
# On five of the six pages that reads as "the brand takes me to my classes",
# which is at least a destination. On `teacher/classes.html` — the page a
# teacher lands on and spends most of their time on — pressing "MrBadmusAI"
# navigates to the page they are already on. It looks like a broken refresh,
# and that is what Mide reported, with a screenshot.
#
# ⚑ MIDE'S INSTRUCTION, 31 Aug 2026: the wordmark goes to the PUBLIC HOMEPAGE
# from every teacher page, unconditionally, and there is a separate, always
# visible way back to the class list. That is what the two hand-written
# teacher pages (`import.html`, `admin.html`) have always done — a brand
# anchor to `/index.html` plus a "My classes" link beside it — so this is the
# ported pages catching up with the hand-written ones rather than a new idea.
# The second half is `INSERT_AT[(10, 13)]` / `AMENDED_ADDITIONS["nav-classes"]`.
#
# ── WHY THIS IS A NEW MECHANISM AND NOT A NAV ENTRY ─────────────────────
#
# ⚠️ `NAV` REDEFINES A HANDLER BY NAME, ONCE, IN THE LOGIC. Every node that
# carries that name gets the new behaviour — there is no per-node arm. And
# `goClasses` is carried by TWO nodes that want DIFFERENT destinations now:
#
#     node 11   the brand mark, on all six pages   → the public homepage
#     node 83   the class screen's "Back"          → the class list  ⟵ correct
#
# Node 83 is right as it stands and must not move: it is the only way out of a
# class detail page, and MRB-287 E1 threads `year` through it so a teacher
# browsing 2025–26 comes back to 2025–26. Rewriting `goClasses` itself would
# take that Back button to the homepage.
#
# `BIND_ATTR` cannot reach this either, and that was checked rather than
# assumed: `student_template` lifts `onClick` OUT of the attribute bag into
# the node's own `on` key (`if (name === 'onclick') { out.on = …; continue; }`),
# so there is no `onClick` attribute for an attribute rewrite to replace.
# `SET_ON` is the right shape and refuses on purpose — it exists to stop a
# ruling silently overwriting a handler Design drew.
#
# So: `{node: (the handler it must be carrying, the handler it moves to,
# why)}`. The `expect` half is the whole safety property. It is the same
# assertion `SET_ON` makes for free, kept rather than dropped: if Design
# redraws the top bar and node 11 becomes something else, the build stops
# instead of pointing an unrelated control at the homepage.
#
# ⚠️ `goHome` IS ADDED IN `LOGIC`, beside the handler it is replacing, and the
# build asserts the name exists in the emitted logic before it will retarget
# anything onto it. Without that check a typo here would leave node 11 calling
# a key `renderVals` does not have — which `student-runtime` records as a
# missed binding, so `teacher_behaviour` would catch it, but only after a page
# had shipped with a brand mark that did nothing.
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · RULED BY MIDE — THE `expect` HALF MOVES
# FROM `goClasses` TO `goToday`, AND THE NODE DOES NOT MOVE AT ALL.
#
# Design's v3 top bar still hangs a handler on node 11, the brand mark, and it
# is no longer `goClasses`: v3 puts a Today screen first and the wordmark now
# carries `goToday`. The DESTINATION this ruling asserts against changed; the
# defect it fixes did not. Pressing "MrBadmusAI" would now be a press that
# takes a teacher to Today rather than a press that reloaded the class list —
# a different wrong answer to the same question.
#
# ⚑ MIDE, 1 Sep 2026: re-anchor it to `goToday` and keep the ruling. His
# reading is that v3 putting Today first IS MRB-304's "the brand mark goes
# home" arriving on its own — Design reached for the same conclusion (the
# wordmark should leave the page you are on) and stopped one step short of
# leaving the teacher portal. The ruling completes it.
#
# ⚠️ THE ASSERTION IS THE WHOLE SAFETY PROPERTY AND IT IS WHAT CAUGHT THIS.
# Had `expect` been dropped rather than re-anchored, the port would have moved
# node 11 off a handler it was no longer carrying and the build would have
# stayed green. `goToday` itself is NOT left dangling: it is still carried by
# node 210 ("Back to today", class screen) and given a real destination in
# `NAV["goToday"]`.
# ⊕ 3 Sep 2026 (MRB-306 Phase 2b) — THE VALUE NAMES ITS SLOT.
#
# `(slot, expected handler, new handler, why)`. `slot` is the key on the
# compiled node — `"on"` for Design's `onClick`, `"onch"` for her `onChange`.
#
# ⚠️ IT IS NOT A DEFAULT, ON PURPOSE. A table that assumed `"on"` would have
# read node 651's missing `on` as "no handler at all" and refused a correct
# ruling — or, if it had written into `on` instead, would have wired a second
# handler onto the node and left `onch` pointing exactly where it did before:
# a green build, a control that still discards what a teacher typed, and
# nothing anywhere saying so.
RETARGET_ON = {
    11: ("on", "goToday", "goHome",
         "the brand mark in the sticky top bar, on all six pages. In v2 "
         "Design shared `goClasses` between it and the class screen's Back; "
         "in v3 she hangs `goToday` on it and shares that with the class "
         "screen's \"Back to today\" (210). Either way only the brand moves. "
         "\"MrBadmusAI\" is the site's name, not the dashboard's, and on "
         "classes.html it was a press that reloaded the page a teacher was "
         "already on."),

    # ══ ⊕ 3 Sep 2026 (MRB-306 Phase 2b) · THE BULK SHEET'S OWN NOTE ══════
    #
    # ⛔ A TEACHER TYPED A MESSAGE, PRESSED SEND, AND THE WORDS VANISHED.
    # Design's v3 draws a free-text textarea in the bulk sheet (node 651)
    # under her own caption "Or write a message", wires it to `setNote`, and
    # the port's `sendBulk` sends `message: null`. Nothing errored; nothing
    # in the UI said the message had been dropped; the six children got a
    # template and no words. That is directly against Mide's free-text ruling
    # of 1 Sep 2026, and there is no reading in which it is intended.
    #
    # ⚠️ THE FIX IS A SEPARATE STATE KEY, AND THE PREVIOUS UNIT WAS RIGHT TO
    # STOP RATHER THAN REACH FOR `s.note`. `note` is the SINGLE-STUDENT
    # composer's field: it is what `noteCount` counts, what `setNote` writes
    # and what `sendShoutout` sends. Picking it up in `sendBulk` would have
    # sent, to a class-sized list of children, text typed into a composer the
    # sheet is not showing — a sheet that is a modal ON TOP of that composer,
    # so the teacher cannot even see what they are about to broadcast.
    #
    # ⚠️ EVERY READER OF `s.note` WAS CHECKED BEFORE THIS KEY WAS ADDED, not
    # after — that omission is how the composer's own template bug happened.
    # There are exactly three in the shipped logic, and this ruling touches
    # none of them:
    #
    #     noteCount     `(s.note || '').length + ' / 500'`   composer counter
    #     setNote       writes `note`                        composer field
    #     sendShoutout  reads `s.note`                       composer send
    #
    # plus `MRB_COMPOSE_RESET`, which clears by the DOM attribute
    # `data-compose-field` and NOT by state name — node 651 carried no such
    # attribute, so it was never in that sweep either. It gets one now
    # (`SET_ATTR`), under its own name `bulk-note`, and `MRB_COMPOSE_RESET`
    # takes a list so that a successful bulk send clears the sheet's field
    # WITHOUT wiping a half-written single shoutout underneath it.
    651: ("onch", "setNote", "setBulkNote",
          "the bulk sheet's free-text message. It was writing into the "
          "single-student composer's state key, which `sendBulk` never "
          "read — so the words were discarded in silence. Now its own key "
          "(`boNote`), its own reset name, and actually sent."),
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
        # ⊕ NODE 11 WAS HERE AND MOVED OUT, 31 Aug 2026 (MRB-304). It is the
        # BRAND MARK, and Mide's ruling is that the wordmark goes to the
        # public homepage from every teacher page. It is not deleted from the
        # rulings — it is asserted in `RETARGET_ON`, which checks it is still
        # carrying `goClasses` BEFORE moving it onto `goHome`, so the
        # anchoring this row used to provide is not lost. Removing it from
        # this tuple without that entry would drop the assertion silently.
        # `goClasses` itself is unchanged: node 83, the class screen's Back,
        # still goes to the class list carrying its academic year.
        # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — `nodes` IS EMPTY, AND THAT IS
        # THE FINDING, not a loosened assertion. The 1 Sep note below says
        # node 463 is "the class screen's Back". It is not: node 463's
        # ancestors are 9 → 461 → 462 → 463, and 461 is `<if isImport>`. It
        # is the IMPORT screen's Back — the same control the 24 Aug note two
        # paragraphs down removed as node 348, back under a new number — and
        # the import screen is not emitted on any page, so the build's
        # closing sweep refused it exactly as it refused 348.
        #
        # ⚠️ v3'S CLASS SCREEN HAS NO "BACK TO MY CLASSES" AT ALL. Node 210
        # is its only Back and it reads "Back to today", carrying `goToday`.
        # So `goClasses` is carried by nothing this port emits.
        #
        # The REWRITE is kept anyway, and it is not dead: it is what makes
        # `goClasses` a real navigation the moment the import screen or any
        # other Back is emitted, and removing it would leave that control
        # calling `setState` on a page where every other screen is pruned —
        # a blank page. What is gone is the ANCHOR, because there is no
        # emitted node left to anchor on. The way back to the class list on
        # all six pages is now the top bar's "My classes" tab (`LOGIC`,
        # `navTabs`), which carries `yearParam` for the same reason this
        # entry does.
        nodes=(),
        anchor=dict(key="goClasses"),
        to="      goClasses: () => MRB_GO('classes', "
           "{ year: MRB_DATA('yearParam') }),",
        why="the class screen's Back (463), and the \"My classes\" link this "
            "port adds to the top bar (`INSERT_AT[(10, 13)]`). Design's node 348 — "
            "the import screen's Back — is drawn by the same handler and is "
            "not emitted; see the note above. Node 11, the brand mark, used "
            "to be on this list and is now in `RETARGET_ON`. "
            "⊕ 1 Sep 2026 (MRB-306): v3 renumbered it — the class screen's "
            "Back is node 463, reading \"Back to my classes\", and it is now "
            "the ONLY node carrying `goClasses`. The import screen's 348 is "
            "gone from the delivery entirely, so the note above describes a "
            "node that no longer exists rather than one merely unemitted."),
    "goClass": dict(
        nodes=(331, 371),
        anchor=dict(key="goClass"),
        to="      goClass: () => MRB_GO('class', { 'class': k && k.id }),",
        why="the student screen's Back (331) and the marking screen's Back "
            "(371). `snapWeekRail` was a scroll fix for a rail that had never "
            "left the DOM; there is no rail to restore across a navigation. "
            "⊕ 1 Sep 2026 (MRB-306): v3 dropped the `snapWeekRail` callback "
            "itself, so Design's handler now agrees with this ruling on that "
            "point; the rewiring to a real URL is unchanged."),
    "goDigest": dict(
        # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — node 41 removed. It is the Today
        # screen's "Weekly digest" and `SCREENS` now prunes Today on all six
        # pages, so it is present on none of them and the closing sweep
        # refuses an anchor that was never checked. Node 166, the classes
        # screen's, is unchanged and still asserted. One rewrite still serves
        # both, so 41 becomes real the day Today is ported.
        nodes=(166,),
        anchor=dict(key="goDigest"),
        to="      goDigest: () => MRB_GO('digest', {}),",
        why="\"Weekly digest\". No `class` parameter IS `digestScope: 'all'` "
            "— see the state initialiser, which derives the scope from the "
            "presence of the parameter so a reload cannot lose it. "
            "⊕ 1 Sep 2026 (MRB-306): v3 draws it TWICE — node 41 on the new "
            "Today screen and node 166 on the classes screen — and adds a "
            "`digestFrom` to Design's setState so her prototype can find its "
            "way back. Both are dropped by the same rewrite: `digestFrom` is "
            "a back stack, and ours is the browser's."),
    "goReport": dict(
        nodes=(217,),
        anchor=dict(key="goReport"),
        to="      goReport: () => MRB_GO('digest', { 'class': k && k.id }),",
        why="\"Class report\" — the same page as the digest, scoped to one "
            "class, which is what `digestScope: 'class'` meant in the "
            "prototype. "
            "⊕ 1 Sep 2026 (MRB-306): v3 relabels the control \"Print report\" "
            "and adds `digestFrom: 'class'`; neither changes where it goes."),
    "goImport": dict(
        nodes=(167,),
        anchor=dict(key="goImport"),
        to="      goImport: () => MRB_GO('import', {}),",
        why="\"Import students\" on the classes screen."),
    "openInsights": dict(
        nodes=(25, 216),
        anchor=dict(key="openInsights"),
        to="      openInsights: () => MRB_GO('insights', s.screen === "
           "'class' ? { 'class': k && k.id } : {}),",
        why="the chart icon in the top bar (25) and \"Charts\" on the class "
            "screen (216). Design's handler carried the scope with it — from "
            "a class it opened scoped to that class, from anywhere else to "
            "all classes — and that fork survives as the presence or absence "
            "of `?class=`. `insFrom` goes: the browser's history is the back "
            "stack now. "
            "⊕ 1 Sep 2026 (MRB-306): v3 widens `insFrom` to three screens "
            "and defaults it to the new `today`. That is the same back stack "
            "this ruling already replaces, so the rewrite is unchanged."),
    "goBackFromDigest": dict(
        nodes=(429,),
        anchor=dict(key="goBackFromDigest"),
        to="      goBackFromDigest: () => MRB_BACK(),",
        why="the digest's Back. Design chose between two destinations from "
            "state; the browser knows the real answer, and a digest opened "
            "from a bookmark has no state to consult. `MRB_BACK` falls "
            "through to the class list when there is no history, so it is "
            "never a dead press. "
            "⊕ 1 Sep 2026 (MRB-306): v3 chooses between THREE now, off the "
            "new `digestFrom`, and one of them is `today`. Design needing a "
            "third is the argument for the ruling rather than against it."),
    "goBackFromInsights": dict(
        nodes=(518,),
        anchor=dict(key="goBackFromInsights"),
        to="      goBackFromInsights: () => MRB_BACK(),",
        why="the charts screen's Back. Same reasoning as the digest's. "
            "⊕ 1 Sep 2026 (MRB-306): v3 dropped the `snapWeekRail` callback "
            "and now falls back to `today` rather than `classes`."),

    # ── the loop-scoped six ─────────────────────────────────────────────
    "c.open": dict(
        nodes=(179,),
        anchor=dict(builder="cards", key="open"),
        to="      open: () => MRB_GO(c.n > 0 ? 'class' : 'import', "
           "{ 'class': c.id, year: MRB_DATA('yearParam') }),",
        why="the class card. ⚠️ DESIGN'S FORK IS KEPT: a card with no "
            "students opens the IMPORT screen, not an empty class page. That "
            "route is real — `roster-import` is one of the three writes that "
            "exist — and the brief's one-line version of this rewiring would "
            "have sent a teacher with an empty class to a page with nothing "
            "on it. "
            "⊕ 1 Sep 2026 (MRB-306): v3 stopped routing the live arm through "
            "`openClass()` and calls `setState` directly; the fork itself is "
            "unchanged. ⚠️ AND `c.open` IS NOW THREE DIFFERENT CONTROLS — the "
            "class card (179), the Today screen's chase list (69, built by "
            "`chaseTop`) and the class glance's chase chips (234, built by "
            "`glance.chase`). Only the card is this ruling's, which is why "
            "the anchor names the `cards` builder and `nodes` names 179 "
            "alone. The other two are unported dead controls on the Today "
            "screen; they are a finding for MRB-306, not for this table."),
    "s.open": dict(
        nodes=(294,),
        anchor=dict(builder="roster", key="open"),
        to="        open: () => MRB_GO('student', { student: r.id, 'class': "
           "k && k.id })",
        why="a roster row on the class screen. ⚠️ ANCHORED ON THE FIVE LINES "
            "THAT FOLLOW IT, because the closure's own text is BYTE-IDENTICAL "
            "to the marking grid's at node 304, and an exactly-once "
            "replacement would refuse the build on a count of two. "
            "⊕ 1 Sep 2026 (MRB-306): that sentence describes the mechanism "
            "this entry no longer uses, and it is kept because it is the "
            "reason the trailing context was ever there. The closure is still "
            "byte-identical to three others; it is now told apart by the "
            "BUILDER it lives in (`roster`), which is a name Design chose, "
            "rather than by the lines that happen to follow it, which she "
            "moved. The trailing `};\\n});\\n\\nconst paperRow` came out of "
            "`to` with it — `paperRow` does not exist in v3, and re-emitting "
            "it would have written v2 source into the middle of a v3 "
            "builder."),
    "a.open": dict(
        nodes=(320,),
        anchor=dict(builder="assignments", key="open"),
        to="      open: () => MRB_GO('marking', { 'class': k && k.id, paper: "
           "p.idx })",
        why="the upcoming (166) and marked (181) assignment rows. Both are "
            "drawn by the one `paperRow` closure, so one rewrite serves both "
            "nodes — which is why both are asserted here. "
            "⊕ 1 Sep 2026 (MRB-306): v3 draws the assignment table ONCE, as "
            "node 320 over `assignments as a`, so there is one node to assert "
            "rather than two, and `paperRow` is gone — the closure is inline "
            "in the `assignments` builder. Its trailing context came out of "
            "`to` for the reason given under `s.open`."),
    "h.open": dict(
        nodes=(361,),
        anchor=dict(builder="stHistory", key="open"),
        to="        open: () => MRB_GO('marking', { 'class': k && k.id, "
           "paper: p.idx })",
        why="a row of the student's assignment history. Anchored on its "
            "trailing `}) : [];` for the same reason `s.open` is. "
            "⊕ 1 Sep 2026 (MRB-306): anchored on the `stHistory` builder "
            "now, for the reason given under `s.open`."),
    "r.open (marking grid)": dict(
        nodes=(419,),
        anchor=dict(builder="grid", key="open"),
        to="      open: () => MRB_GO('student', { student: r.id, 'class': "
           "k && k.id })",
        why="a row of the marking screen's question grid — NOT a digest row. "
            "⊕ 1 Sep 2026 (MRB-306): the control survives v3 unchanged, as "
            "node 419 over `paper.grid as r`, still built by `grid`."),
    "d.open": dict(
        nodes=(453,),
        anchor=dict(builder="digestRows", key="open"),
        to="        open: () => c.n > 0 ? MRB_GO('class', { 'class': c.id }) "
           ": this.ping('No students in ' + c.code + ' yet')",
        why="a row of the weekly digest. Design's empty-class arm is KEPT as "
            "a toast: it is not a navigation and never was, and silently "
            "doing nothing would be the dead control the toast avoids. "
            "⊕ 2 Sep 2026 (MRB-306 Phase 1c): node 453 is fed by TWO "
            "builders — `digestRows` on the whole-school digest and "
            "`classReportRows` when `digestScope` is `class` — and this "
            "entry reaches only the first. The second is now the entry "
            "below, on Mide's ruling. The `builder=` anchor is what makes "
            "two entries on one node possible at all: the handler NAME is "
            "the same on both rows and only the closure they live in tells "
            "them apart."),

    # ── ⊕ RULED BY MIDE, 1 Sep 2026 · A v2 DEFECT CLOSED IN PASSING ──────
    #
    # ⛔ THE CLASS REPORT'S ROWS WERE NEVER REWIRED, IN v2 OR IN v3. Node 453
    # is ONE row markup — `<for digestRows as d>` — and `digestRows` is
    # `isClassReport ? classReportRows : digestRows`, so the SAME row is
    # drawn by two different closures depending on whether the digest is
    # scoped to a class. The entry above rewires `digestRows`. Nothing
    # rewired `classReportRows`, so on `digest.html?class=<id>` — the CLASS
    # REPORT, which is where a teacher goes to look at one class's papers —
    # every row still ran Design's `this.setState({ screen: 'marking',
    # paperId: p.id })`.
    #
    # On a six-URL port that press sets a screen the page does not carry, so
    # every screen `<if>` goes false and THE PAGE RENDERS NOTHING. It is the
    # `c.act` blank page again, on a row a teacher presses to open marking.
    #
    # ⚠️ AND `paperId` WOULD HAVE BEEN WRONG EVEN IF THE SCREEN EXISTED.
    # Design keys a paper by a made-up string (`'8rsc1:p1'`);
    # `teacher-live.js` reads `?paper=` as an INDEX into the class's own
    # paper list. `p.idx` is the index, and it is already in scope — the
    # same closure reads `kMx.colSub[p.idx]` two lines up.
    #
    # ⚑ MIDE, 1 Sep 2026: fix it now. It was reported as pre-existing and
    # out of scope on 1 Sep; this closes it.
    "d.open (class report)": dict(
        nodes=(453,),
        anchor=dict(builder="classReportRows", key="open"),
        to="        open: () => MRB_GO('marking', { 'class': k && k.id, "
           "paper: p.idx })",
        why="a row of the CLASS REPORT — `digest.html?class=<id>` — which "
            "draws the same node 453 as the whole-school digest through a "
            "different builder. It opens the marking screen for that paper, "
            "which is what Design's own closure meant; it went by a paper id "
            "the seam cannot read, to a screen this page does not carry."),
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
        nodes=(198,),
        anchor=dict(builder="cards", key="act"),
        to="      act: (e) => { e.stopPropagation(); "
           "MRB_GO('import', { 'class': c.id }); }",
        why="\"Import\" on a class card with no students. The one route into "
            "the roster importer from the class list, and it was rendering a "
            "blank page. "
            "⊕ 1 Sep 2026 (MRB-306): v3 renumbers the pair — the \"Import\" "
            "arm is node 198 and the \"Set work\" arm `DEAD` prunes is node "
            "194 (they were 71 and 74). The note above still applies "
            "unchanged: only the kept node is asserted here, because the "
            "build's closing sweep refuses a NAV node that appears on no "
            "page. ⚠️ v3 also grows a SECOND control with this shape — "
            "`setupRows.act` at node 95 on the Today screen, drawing the same "
            "Import/Set-work fork — which no ruling touches. A finding for "
            "MRB-306, not a change to make here."),

    # ══ ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · v3'S NEW CLASS-SCREEN CONTROLS ══
    #
    # ⛔ FIVE CONTROLS DESIGN ADDED IN v3 THAT NO RULING TOUCHED, ALL FIVE ON
    # `class-detail.html`, ALL FIVE SETTING `s.screen`. On a six-URL port that
    # is not a navigation, it is a page that renders nothing: `s.screen` is
    # fixed by the build and every other screen `<if>` has been pruned, so the
    # press makes every branch false. It is the `c.act` blank page of 24 Aug,
    # five times over, on the page a teacher spends most of their day on.
    #
    # They were flagged as findings on 1 Sep and left; they are closed here
    # because a screen-setting control on an emitted page is the same defect
    # class as the `TODAY_LESSONS` throw this unit was sent to fix, and
    # leaving a class page whose "glance" block is five dead presses does not
    # serve a teacher looking at a real class.
    "goToday": dict(
        nodes=(210,),
        anchor=dict(key="goToday"),
        to="      goToday: () => MRB_GO('today', {}),",
        why="the class screen's Back (210), which v3 relabels \"Back to "
            "today\" — v2's was \"Back to my classes\" and carried "
            "`goClasses`. It goes to `teacher/today.html`, the hand-written "
            "Today page, which is real and live; when Design's Today screen "
            "is ported it emits that same filename, so this link does not "
            "become a rename. ⚠️ Node 11, the brand mark, ALSO carries "
            "`goToday` in v3 and is moved OFF it by `RETARGET_ON` before this "
            "rewrite is asserted — the brand goes to the public homepage, "
            "which is Mide's MRB-304 ruling and is not weakened by v3 giving "
            "the wordmark a nicer wrong destination."),

    "glance.openMarking": dict(
        nodes=(253,),
        anchor=dict(key="openMarking"),
        to="      openMarking: () => MRB_GO('marking', { 'class': k && k.id, "
           "paper: MRB_NEWEST_MARKED(MRB_PICK('PAPERS', k && k.id)) }),",
        why="\"Open the full breakdown\" under the class glance's two "
            "weakest questions. Design's own destination is the marking "
            "screen for `lastP`, the last MARKED paper — but by `paperId`, a "
            "made-up string the seam cannot read. `MRB_NEWEST_MARKED` is the "
            "port's existing answer to \"which paper is the newest marked "
            "one\", taken from `teacher-live.js` rather than reimplemented, "
            "and it is the same function every other marking link already "
            "uses. Design's `if (lastP)` guard is not needed: the whole "
            "glance block is inside `<if klass.hasWork>`."),

    "w.open (keep an eye on)": dict(
        nodes=(259,),
        anchor=dict(builder="watch", key="open"),
        to="      open: () => MRB_GO('student', { student: r.id, 'class': "
           "k && k.id })",
        why="a student chip in the class glance's \"Keep an eye on\" list "
            "(259). ⚠️ ANCHORED ON THE `watch` BUILDER, not on the line, "
            "because v3 draws a byte-identical closure on the Today screen "
            "as well and an exactly-once source replacement would refuse on "
            "a count of two. It gains `'class'` — Design's version sets only "
            "`studentId`, and a student page needs the class it is being "
            "read in."),

    "r.open (search)": dict(
        nodes=(665,),
        anchor=dict(builder="results", key="open"),
        to="      open: () => MRB_GO('student', { student: p.id, 'class': "
           "p.classId })",
        why="a result row in the search overlay. It is the one navigation "
            "that changes CLASS as well as student, which is why it reads "
            "`p.classId` rather than the page's own `k.id`. "
            "⊕ 1 Sep 2026 (MRB-306): the control survives v3 unchanged, as "
            "node 665 over `searchResults as r`, still built by `results`."),
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3, every row:
#   10→10 · 29→158 · 81→208 · 210→330 · 246→370 · 300→428 · 334→462
#   389→517 · 501→629 · 526→656 · 542→672
#   355→483 · 356→484 · 371→499 · 374→502 · 377→505 · 387→515
# and the two composer rows (187, 196) are GONE — see the note where they
# were, below.
SET_ATTR = {
    10:  {"data-port-region": "topbar"},
    158: {"data-port-region": "classes"},
    208: {"data-port-region": "class"},
    330: {"data-port-region": "student"},
    370: {"data-port-region": "marking"},
    428: {"data-port-region": "digest"},
    462: {"data-port-region": "import"},
    517: {"data-port-region": "insights"},
    629: {"data-port-region": "overlay-bulk"},
    656: {"data-port-region": "overlay-search"},
    672: {"data-port-region": "toast"},
    # ⊕ THE TWO COMPOSER FIELDS, so the send can CLEAR them. Design's select
    # and textarea are uncontrolled — neither carries a `value` — and
    # `student-runtime` deliberately carries field values across a redraw, so
    # clearing `s.recipient` and `s.note` clears the state and leaves the
    # typed text on screen. `MRB_COMPOSE_RESET` empties the DOM first, and
    # this is how it finds them without an id Design did not write.
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — RETIRED. They were nodes 187 and 196
    # and there is nothing in v3 to re-anchor them onto: Design's v3 DELETED
    # the class screen's single-student shoutout composer and the shoutout
    # feed under it (v2 nodes 181–208) outright, and replaced them with the
    # `glance` block.
    # ⊕ 3 Sep 2026 — AND THEY DO NOT COME BACK HERE. Mide ruled the composer
    # restored (`SHOUTOUT_SURFACE_RESTORED`), but the restored fields are
    # INSERTED markup and carry no `i`, so `SET_ATTR` — which is keyed by
    # Design's node index — cannot reach them. `data-compose-field` is
    # written directly into the subtree in `INSERT_AT[(208, 306)]` instead,
    # and `MRB_COMPOSE_RESET` finds both fields again.

    # ⚠️ THE FIVE `data-import-slot` ROWS BELOW APPLY TO NO EMITTED PAGE. They
    # are the import screen's nodes and the import screen is not ported (see
    # `IMPORT_NOT_PORTED`); both loops that read this table skip a node that
    # is not on the page. Kept, not deleted, because they are the anchoring
    # work a future re-port would otherwise redo — and said out loud here,
    # because a ruling that quietly applies to nothing is the drift this file
    # exists to stop.
    483: {"data-import-slot": "fileName"},
    484: {"data-import-slot": "fileSummary"},
    499: {"data-import-slot": "newCount"},
    502: {"data-import-slot": "matchedCount"},
    505: {"data-import-slot": "attentionCount"},
    515: {"data-import-slot": "confirm"},

    # ── ⊕ 3 Sep 2026 (MRB-306 Phase 2b) · THE BULK SHEET'S TEXTAREA ──────
    #
    # It is now SENT (see `RETARGET_ON[651]`), so it needs the two things
    # every other sending field on this screen has and it did not:
    #
    #   · `data-compose-field`, so `MRB_COMPOSE_RESET(['bulk-note'])` can
    #     empty it after a successful send. Design's fields are uncontrolled
    #     and `student-runtime` carries their values across a redraw on
    #     purpose, so clearing `s.boNote` alone would leave the sent words
    #     sitting in the box looking unsent. Its OWN name, not `note`: the
    #     single-student composer is underneath this modal and its half-typed
    #     text must survive an action about other children.
    #   · `maxlength`, which is the DATABASE's number
    #     (`class_shoutouts_message_length_chk`, 500). A cap a teacher
    #     discovers by being refused after writing is not a cap, it is a
    #     rejection — the same sentence the composer's own textarea carries,
    #     and Design gave this one no cap at all.
    651: {"data-compose-field": "bulk-note", "maxlength": "500"},
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
    #
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — RETIRED, and the note above is kept
    # because it is the reasoning, not the anchor. The ruling was on node 190,
    # the `<option>` inside the class screen's recipient `<select>`, and v3
    # has no such node: Design deleted the whole single-student composer. The
    # id-not-name principle survives where the write still happens — the bulk
    # overlay's `bulkStudents` rows carry `s.id` and `MRB_SEND_SHOUTOUTS`
    # takes ids — so nothing regressed to sending a name.
    # ⊕ 3 Sep 2026 — THE SELECT IS BACK AND THIS ROW STILL DOES NOT RETURN.
    # Mide ruled the composer restored (`SHOUTOUT_SURFACE_RESTORED`) and its
    # `<option>` is written with `{"e": "s.id"}` FROM THE START, in
    # `INSERT_AT[(208, 306)]`. There is no Design attribute left to correct,
    # which is the better place for the ruling to live: v2 needed this table
    # because Design wrote `value="{{ s.name }}"` and the port had to
    # overwrite it after the fact.
    # ── "NOT MARKED" DOES NOT FIT IN DESIGN'S PERCENTAGE COLUMN ────────
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a screen 5). The question-breakdown
    # row's last track is 90px, which is exactly right for the only thing
    # Design ever puts in it: `q.pct + '%'`, four characters, measured at
    # 43.2px. The port's `qpct == null` ruling puts "Not marked" there
    # instead — the label for a question nothing was machine-marked on — and
    # that measures 108px in the same 18px mono. Measured, not guessed, on
    # `assignment-written-fixture.html` at 1280px: the cell was 90px wide and
    # 43px TALL where every other cell in the table was 22px, i.e. wrapped
    # onto two lines, and it wrapped mid-phrase ("Not / marked") in a column
    # of right-aligned numerals.
    #
    # ⚠️ THE COLUMN WIDENS RATHER THAN THE TEXT SHORTENING. "Not marked" is
    # the honest label and it is a COMMON state, not a rare one: a paper
    # nobody has answered yet shows it on every row (see
    # `assignment-empty-fixture.html`, where all eight wrapped). 112px fits
    # it with four pixels to spare; nothing else in the row moves, because
    # the flexible track is the `1fr` stem column.
    #
    # ⚠️ AND IT WIDENS ONLY WHEN THE PAPER NEEDS IT — `paper.labelCol` is
    # 112px when any question is unmarked and Design's own 90px otherwise.
    # Two reasons, and the second is the one that decided it. Design's
    # geometry is right for Design's content, and a fully-marked paper has
    # nothing in that column but "54%". And the row template is ALREADY
    # over-constrained at a 390px viewport — `56 + 180 + 90` plus three 14px
    # gaps exceeds the available width, so the `1fr` stem column collapses
    # and the bar paints over the question text — which is the known missing
    # `@media` on these six pages and is not this unit's to solve. Pinning
    # 112px unconditionally would have added 22px to that overflow on every
    # paper in the estate, including the ones that never show the long label.
    #
    # ⛔ `auto` WAS THE OBVIOUS ANSWER AND IT IS WRONG HERE. The template
    # sits on the ROW, not on a shared table, so each row is its own grid
    # container: `auto` would size the last track per row, and a column of
    # right-aligned numerals would have a ragged right edge.
    392: ("style",
          "display:grid;grid-template-columns:56px 1fr 180px 90px;"
          "align-items:center;gap:14px;padding:13px 18px;"
          "border-top:1px solid var(--st-rule-fact)",
          {"parts": ["display:grid;grid-template-columns:56px 1fr 180px ",
                     {"e": "paper.labelCol"},
                     ";align-items:center;gap:14px;padding:13px 18px;"
                     "border-top:1px solid var(--st-rule-fact)"]},
          "the question-breakdown row, widened only on a paper that carries "
          "the port's own \"Not marked\" label."),

    # ── THE CLASS-BY-QUESTION TABLE IS EIGHT COLUMNS WIDE ──────────────
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a screen 5). Both halves of the
    # marking grid — Design's header row (413) and her student row (419) —
    # hardcode `repeat(8,1fr)`. The reasoning is with the `paper.cols` entry
    # in `LOGIC`; in short, eight is `STEMS.length` and real papers are not
    # eight questions (the only TEST assignment with question rows has four).
    #
    # ⚠️ THE TWO MUST NEVER DISAGREE, which is why they interpolate one key
    # rather than computing the same string twice. A header on eight tracks
    # over rows on four is worse than both being wrong together: the column
    # headings would name questions the cells underneath are not.
    413: ("style",
          "display:grid;grid-template-columns:225px repeat(8,1fr) 92px;"
          "background:var(--st-num-well);"
          "border-bottom:1px solid var(--st-rule-soft)",
          {"parts": ["display:grid;grid-template-columns:",
                     {"e": "paper.cols"},
                     ";background:var(--st-num-well);"
                     "border-bottom:1px solid var(--st-rule-soft)"]},
          "the marking grid's header row: one track per question the paper "
          "actually has."),
    419: ("style",
          "display:grid;grid-template-columns:225px repeat(8,1fr) 92px;"
          "align-items:center;border-top:1px solid var(--st-rule-fact);"
          "cursor:pointer",
          {"parts": ["display:grid;grid-template-columns:",
                     {"e": "paper.cols"},
                     ";align-items:center;"
                     "border-top:1px solid var(--st-rule-fact);"
                     "cursor:pointer"]},
          "the marking grid's student row. `paper.cols` resolves through the "
          "loop scope's prototype chain — `student-runtime`'s `for` builds "
          "each iteration with `Object.create(scope)` — so the row inside "
          "`<for paper.grid>` reads the same key the header does."),

    662: ("placeholder",
          "Search students across all 12 classes",
          {"parts": [{"e": "searchPlaceholder"}]},
          "the 12 is this teacher's real class count. Design drew a teacher "
          "with twelve classes; a teacher with three would be invited to "
          "search across twelve. teacher-live.js computes the whole sentence "
          "— including the singular form for a teacher with one class."),

    # ── THE CLASS CARD'S META LINE MUST BE ALLOWED TO WRAP ──────────────
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a). Design's node 182 is the caption
    # under the class code, and she gives it `white-space:nowrap` and no
    # overflow treatment at all. A nowrap child inside an `auto-fit,
    # minmax(310px,1fr)` grid does not truncate and does not ellipsise — it
    # widens its own column until the document overflows the window, and the
    # text is then clipped at the WINDOW edge rather than the card's.
    #
    # ⚠️ THIS WAS ALREADY BROKEN BEFORE PHASE 2a TOUCHED THE LINE. Measured
    # on `classes-fixture.html` at a 1280px viewport, 2 Sep: the meta of
    # `11r/Sc1` ("No students yet · Combined Science · 2026–27") laid out
    # from x=870 to x=1293 and `document.scrollWidth` was 1293 against a
    # 1280 client width — the last five characters of the academic year were
    # off-screen, on the fixture the gates have been driving for a week. It
    # is the longest of Design's twelve; the shorter eleven hid it.
    #
    # Mide's Phase 2a brief adds the year group and key stage to that same
    # line (see the `cards`/`meta` ruling in LOGIC), which takes the worst
    # case from 40 characters to 56 and would clip most of the estate rather
    # than one card. So the two are one change: the line gains the pair, and
    # the caption is allowed to wrap.
    #
    # WHY WRAP RATHER THAN TRUNCATE. Every part of this line is identifying
    # — which year group, which key stage, how many children, which subject,
    # which academic year — and E1's whole reason for the academic year is
    # that `10h/Ph1` and `11h/Ph1` are the same children a year apart. An
    # ellipsis eats the trailing part first, which is precisely the part
    # that ruling exists to keep. A second line is cheap; a wrong card is
    # not.
    #
    # ONLY TWO PROPERTIES CHANGE, and nothing else in the string is
    # touched: `white-space:nowrap` is dropped, and the line-height goes
    # 1.2 → 1.5 so a wrapped uppercase mono caption has room to breathe.
    # Design's margin, font, tracking, transform and colour are hers.
    182: ("style",
          "margin-top:8px;font:400 13px/1.2 var(--st-mono);"
          "letter-spacing:.14em;text-transform:uppercase;"
          "color:var(--st-caption);white-space:nowrap",
          "margin-top:8px;font:400 13px/1.5 var(--st-mono);"
          "letter-spacing:.14em;text-transform:uppercase;"
          "color:var(--st-caption)",
          "the class card's meta caption. nowrap on a grid child does not "
          "truncate — it widens the column and clips at the window edge, "
          "which it already did on the longest of Design's own twelve "
          "cards. The line is identifying end to end, so it wraps rather "
          "than being cut."),
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3: 32→161 · 77→204 ·
# 79→206 · 306→434 · 395→523.
#
# ⚠️ TWO OF THE ASSERTED LITERALS CHANGED AS WELL AS THE INDEX, and that is
# the reason this table asserts the literal at all. Design moved her sample
# forward one week between deliveries: the digest heading now reads
# "Mon 24 – Fri 28 Aug 2026" and the charts heading "Week of Mon 24 Aug 2026".
# Re-anchoring the index alone would have left the build asserting a date
# Design no longer types, which refuses loudly — the right failure. What it
# must NOT become is a literal loosened to make it pass: the literal is what
# proves the node is still the heading and not its neighbour.
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
    #
    # ⊕ MOVED, 26 Aug 2026 — Design's v2 REMOVED the badge node, so this
    # binding has nothing to bind. The safety rationale above still stands,
    # and both are honoured at once: `envBadge()` now returns "" on the live
    # production origin (so prod looks exactly as v2 draws it), and the badge
    # markup returns as a conditional insertion — INSERT_AT node 10 — that
    # renders only when there is something to warn about (TEST, LOCAL). The
    # sandbox warning survives; the permanent "PROD" chip Design deleted does
    # not come back.

    # ── the classes screen ──────────────────────────────────────────────
    161: ("Autumn term · 2026–27", "termLabel"),
    204: ("Viewing 2026–27", "viewingYearLabel"),
    # ⊕ MRB-287 E1 — the year toggle's own label. "Previous years" is right
    # only while the WORKING year is in view; opened FROM a past year the same
    # list leads forward as well, and the retired hand-written page said
    # "other years" for exactly that case
    # (teacher-classes-2026-08-24-retired.html:677). It is `pastYearsLabel`,
    # computed in the seam, and it is the reason that key is no longer dead.
    206: ("Previous years", "pastYearsLabel"),

    # ── the digest ──────────────────────────────────────────────────────
    434: ("Mon 24 – Fri 28 Aug 2026", "weekRangeLabel"),

    # ── the charts screen ───────────────────────────────────────────────
    523: ("Week of Mon 24 Aug 2026", "weekOfLabel"),
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
    # ── ⊕ MIDE, 1 Sep 2026 · THE ROSTER COLUMN IS THE SELECTED WEEK ─────
    #
    # ⚠️ AND THIS ONE IS A BINDING, NOT A LITERAL, WHICH IS WHY IT IS HERE
    # AND NOT IN `BINDINGS_AT`. `BINDINGS_AT` keys are `MRB_DATA` keys, read
    # out of `teacher-live.js`'s payload at mount; `rosterWeekCol` is a
    # `renderVals` key, because it changes every time a teacher presses a
    # chip and the payload does not. A text node's `v` takes a `parts`
    # expression exactly as an attribute's does — Design writes one herself
    # on node 309 — so the assertion this table already makes (the node still
    # reads what the ruling thinks it reads) is the guard that matters.
    #
    # Left as the literal "This week" it is simply false the moment a past
    # week is selected: the column would be headed "This week" over marks
    # from October.
    289: ("This week",
          {"parts": [{"e": "rosterWeekCol"}]},
          "the roster table's second column heading. Under the week bar the "
          "column is the SELECTED week, and it says which one."),

    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — the six import rows re-anchored on
    # v3: 355→483 · 356→484 · 371→499 · 374→502 · 377→505 · 387→515. Every
    # literal is unchanged, which is what says these are the same six nodes.
    # ⚠️ Node 289 above is NOT remapped — it was written against v3 by the
    # week-bar unit and v3's node 289 is the roster's second column heading.
    483: ("year8-autumn.csv", "",
          "a file nobody uploaded."),
    484: ("27 rows · 5 columns", "",
          "counts of a file nobody parsed."),
    499: ("24", "",
          "\"New students\" — a dry-run nobody ran."),
    502: ("2", "",
          "\"Matched existing\" — same."),
    505: ("1", "",
          "\"Needs attention\" — same, and the one a teacher would act on."),
    515: ("Import 26 students", "Import students",
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
# `{(parent node, insert after this child node — or None to append):
#   (subtree, why)}`. Nothing inserted carries an `i`: Design's numbering is
# what every other ruling in this file is anchored on and it must not move.
#
# ⊕ THE KEY USED TO BE THE PARENT NODE ALONE, 31 Aug 2026 (MRB-304). It could
# not stay that way: node 10 — the sticky top bar — now takes TWO insertions,
# the environment badge and the "My classes" link, and a dict keyed by parent
# would have silently kept the LAST one written and dropped the other. A
# ruling that vanishes because two entries share a key is precisely the
# quiet failure every mechanism in this file refuses loudly, so the key
# became the pair that actually identifies an insertion: where it goes, and
# what it goes after.

# ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 5) — 12px → 13px. Design's three
# legend keys are `font:400 13px/1.2 var(--st-mono)` (source lines 621-623),
# and the ruling that uses this constant says the fourth key stands "in the
# register of the three keys beside it". It did not: measured on
# `assignment-empty-fixture.html` at 1280px, the three read 13px/15.6px and
# the fourth read 12px/14.4px, so the one key a teacher has never seen before
# was also the smallest thing in the row.
_LEGEND_KEY = ("display:flex;align-items:center;gap:6px;"
               "font:400 13px/1.2 var(--st-mono);letter-spacing:.12em;"
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

# ── ⊕ MRB-304 · the top bar's way back to the class list ─────────────────
#
# Design's own low-emphasis text button, and not a new register: it is the
# `_DEL_TEXT_BTN` string above, which is itself node 213's "Back to <class>"
# treatment copied verbatim — `font:600 14.5px/1.2 var(--st-ui)` in
# `--st-muted`, no border, no ground, hovering to `--st-ink`. That is the
# treatment Design uses for every in-chrome text navigation in this delivery,
# and the top bar already holds two controls in exactly that weight class.
#
# ⚠️ IT DOES NOT COPY THE CRUMB'S REGISTER, and the difference is deliberate.
# Node 14 is a 13px uppercase mono CAPTION — it says where you are. This says
# where you can go. Painting them the same would make a label look pressable
# and a control look like a label, eight pixels apart.
_NAV_BACK_BTN = _DEL_TEXT_BTN


# ── ⊕ MIDE, 1 Sep 2026 · the week bar's style strings ────────────────────
#
# Read out of the v2 delivery, character for character, not retyped from a
# description: `docs/…/teacher/source/Teacher Dashboard.dc.html` at commit
# 3ee8172f6, lines 157-177. Design drew this bar and then removed it; the
# ruling is that it comes back, not that it gets redesigned.
_WK_BAR = ("display:flex;align-items:center;gap:12px;margin-top:18px;"
           "padding:12px;background:var(--st-paper);"
           "border:1px solid var(--st-rule-soft);border-radius:12px")
_WK_CAPTION = ("flex:none;padding-left:4px;font:500 13px/1.2 var(--st-mono);"
               "letter-spacing:.16em;text-transform:uppercase;"
               "color:var(--st-caption)")
_WK_CHEV = ("flex:none;display:flex;align-items:center;justify-content:center;"
            "width:36px;height:52px;background:var(--st-paper);"
            "border:1px solid var(--st-rule-soft);border-radius:9px;color:")
_WK_RAIL = ("display:flex;align-items:stretch;overflow-x:auto;padding:1px;"
            "scrollbar-width:none")
_WK_CHIP = ("flex:none;display:flex;flex-direction:column;align-items:center;"
            "justify-content:center;gap:5px;min-height:52px;padding:8px 17px;"
            "background:")
_WK_RANGE = "font:500 18px/1.15 var(--st-mono);color:"
_WK_SUB = ("font:500 11.5px/1 var(--st-mono);letter-spacing:.14em;"
           "text-transform:uppercase;white-space:nowrap;color:")
_WK_NOTE = "margin-top:14px;font:400 15.5px/1.4 var(--st-ui);color:var(--st-muted)"


def _wk_chevron(handler, label, path, colour, cursor, marker):
    """One of the two week chevrons, in v2's own drawing.

    ⚠️ `data-mrb-added` IS NOT DECORATION. Inserted markup carries no `i` —
    Design's numbering is what every other ruling is anchored on — so it also
    carries no `data-dc-tpl`, and `teacher_behaviour`'s control sweep finds
    an inserted control ONLY by this attribute. Without it the two chevrons
    would be markup no gate can see, which is the hole that comment records.
    """
    return {
        "t": "button",
        "a": {"type": "button", "aria-label": label,
              "data-mrb-added": marker,
              "style": {"parts": [_WK_CHEV, {"e": colour},
                                  ";cursor:", {"e": cursor}]}},
        "hov": "border-color:var(--st-edge)",
        "on": handler,
        "c": [{"t": "svg",
               "a": {"width": "15", "height": "15", "viewBox": "0 0 14 14",
                     "fill": "none", "aria-hidden": "true"},
               "c": [{"t": "path",
                      "a": {"d": path, "stroke": "currentColor",
                            "stroke-width": "1.7", "stroke-linecap": "round",
                            "stroke-linejoin": "round"}}]}]}


# ── ⊕ MIDE, 3 Sep 2026 · the restored shoutout surface's style strings ───
#
# See `SHOUTOUT_SURFACE_RESTORED` at the top of this file for the ruling.
# ⚑ EVERY STRING HERE IS READ OFF A v3 NODE, and the node is named. That is
# the difference between "restored in v3's language" and "pasted back from
# v2": v3 draws this exact control in the bulk sheet (nodes 638-654) and
# draws this exact card, heading and avatar elsewhere on the same screen.
# Only the two-column SHAPE is v2's, because v3 deleted the arrangement and
# there is nothing of hers left to read it off.
_SO_HEAD = ("display:flex;align-items:baseline;justify-content:space-between;"
            "gap:12px;margin:26px 0 12px")                       # node 283
_SO_H2 = ("margin:0;font:600 33px/1 var(--st-display);"
          "letter-spacing:-0.03em;color:var(--st-ink)")          # node 284
# ⚠️ ONE DECLARATION DIFFERENT FROM NODE 285, AND IT IS A DEFECT NOT
# COPIED. Design's caption carries `white-space:nowrap`, and hers is "16
# STUDENTS · NOT SUBMITTED SHOWN FIRST" — 375px of it — beside a 33px
# heading in a 310px content box at 390px wide. Measured: it overflows the
# page by 171px. This one says "2 SHOUTOUTS · NEWEST FIRST" and would do the
# same thing 80px smaller. It wraps instead, right-aligned so the ragged edge
# is the one against the heading. Design's node is hers and is left alone;
# repeating its one bad declaration on new markup is not fidelity.
_SO_COUNT = ("font:500 13px/1.2 var(--st-mono);letter-spacing:.14em;"
             "text-transform:uppercase;color:var(--st-caption);"
             "text-align:right")                                 # node 285

# ⚠️ `390px` AND NOT v3'S 330px. Node 223's glance grid is three tiles and
# wants three columns; this is two panels and must be two — at 330px the
# 1460px page would fit four and the composer would sit in a quarter-width
# column beside three empty ones. 390 is v2's own figure for this
# arrangement.
#
# ⛔ `min(100%, 390px)` AND NOT A BARE `390px`, AND THIS WAS MEASURED RATHER
# THAN REASONED. A bare `minmax(390px,1fr)` makes the TRACK at least 390px
# wide however narrow the page is — and node 208's own padding is
# `20px 40px 40px`, so at a 390px viewport the content box is 310px and every
# card in this section hung 80px off the right-hand edge of the page.
# Photographed: fifteen elements over the edge, the composer card, all six
# template buttons and both feed cards among them.
#
# ⚠️ AND DESIGN'S OWN GRIDS DO EXACTLY THIS, which is why it is worth
# spelling out. Node 223's `minmax(330px,1fr)` overflows the same 310px box
# by 20px, and the roster table's five fixed tracks force 896px on their own,
# so this screen already scrolls sideways at 390px. That is Design's and it
# is reported, not silently patched here. What is NOT acceptable is adding a
# sixteenth, seventeenth and eighteenth reason for the same scrollbar on
# markup this port wrote.
_SO_GRID = ("display:grid;grid-template-columns:repeat(auto-fit,"
            "minmax(min(100%,390px),1fr));gap:16px;align-items:start")
_SO_CARD = ("padding:20px;background:var(--st-paper);"
            "border:1px solid var(--st-rule-soft);border-radius:11px")
_SO_CAP = ("font:500 13px/1.2 var(--st-mono);letter-spacing:.16em;"
           "text-transform:uppercase;color:var(--st-caption)")   # node 640
_SO_CAP2 = "margin-top:22px;" + _SO_CAP                          # node 646

# ⚠️ THE ONE STRING WITH NO v3 COUNTERPART, and it is Design's from v2 (node
# 187). v3 contains exactly two form controls — the bulk textarea and the
# search input — and neither is a select. See the ruling for why this stays a
# select rather than becoming a chip row.
_SO_SELECT = ("width:100%;margin-top:10px;height:42px;padding:0 12px;"
              "font:600 17px/1.2 var(--st-ui);color:var(--st-ink);"
              "background:var(--st-paper);border:1px solid "
              "var(--st-btn-border);border-radius:10px")
_SO_TPL_GRID = ("display:grid;grid-template-columns:repeat(auto-fit,"
                "minmax(240px,1fr));gap:8px;margin-top:12px")     # node 647
_SO_TPL_BTN = ("text-align:left;white-space:normal;padding:12px 13px;"
               "font:600 16.5px/1.25 var(--st-ui);border-radius:10px;"
               "cursor:pointer;color:")                           # node 649
_SO_NOTE = ("width:100%;margin-top:10px;min-height:70px;padding:12px;"
            "font:400 17px/1.5 var(--st-ui);color:var(--st-ink);"
            "background:var(--st-paper);border:1px solid "
            "var(--st-btn-border);border-radius:10px;resize:vertical")  # 651
_SO_FOOT = ("display:flex;align-items:center;justify-content:space-between;"
            "gap:10px;margin-top:14px")
_SO_COUNTER = ("font:400 13px/1.2 var(--st-mono);letter-spacing:.12em;"
               "text-transform:uppercase;color:var(--st-ghost)")
_SO_SEND = ("flex:none;height:38px;padding:0 18px;"
            "font:600 16.5px/1.2 var(--st-ui);color:var(--st-paper);"
            "background:var(--st-accent-text);border:none;"
            "border-radius:9px;cursor:pointer")                   # node 654

_SO_FEED_COL = "display:flex;flex-direction:column;gap:12px"
_SO_FEED_CARD = ("padding:16px 18px;background:var(--st-paper);"
                 "border:1px solid var(--st-rule-soft);border-radius:11px")
_SO_FEED_TOP = "display:flex;align-items:center;gap:10px"
_SO_AVATAR = ("flex:none;width:26px;height:26px;border-radius:50%;"
              "display:flex;align-items:center;justify-content:center;"
              "font:600 11.5px/1 var(--st-mono);color:var(--st-paper);"
              "background:")                                      # node 271
_SO_FEED_NAME = "font:600 16px/1.2 var(--st-ui);color:var(--st-ink)"   # 273
# ⊕ THE ATTRIBUTION LINE. Design drew no counterpart on a feed card at all —
# v2's card says who it is ABOUT and never who WROTE it — so the treatment is
# node 274's, the second line of a `glance.praise` row, in `--st-muted`
# because it is a byline rather than a verdict.
# ⊕ AND THE TIME IS ON IT, WHICH IS A CHANGE FROM v2 AND WAS FORCED BY
# LOOKING AT 390px. v2 put the relative time in a third element on the top
# row, `margin-left:auto`, in uppercase mono — three items competing for one
# line. Photographed at 390px with the Remove control present: "Hana
# Pretorius" broke across two lines, "2 DAYS AGO" sat against the second of
# them, and "by Mr Badmus" fell to a third. Folded into the byline the row is
# avatar + two lines + control, which is EXACTLY node 270's shape — the
# `glance.praise` row this treatment already came from — and it holds at
# every width.
_SO_FEED_BY = ("margin-top:2px;font:400 13.5px/1.3 var(--st-ui);"
               "color:var(--st-muted)")                           # node 274
_SO_FEED_TPL = ("margin-top:11px;font:500 16.5px/1.45 var(--st-ui);"
                "color:var(--st-accent-text)")
# ⚠️ `pre-wrap` AND `overflow-wrap:anywhere` ARE BOTH LOAD-BEARING, and
# neither is decoration.
#   · `pre-wrap` — this is FREE TEXT a teacher typed into a textarea, and a
#     textarea takes newlines. Collapsed, a three-line note about a child
#     runs together into one paragraph that the teacher did not write.
#   · `overflow-wrap:anywhere` — a pasted URL is one unbroken 80-character
#     token. Links render as INERT TEXT here (see the ruling), and inert text
#     still has to wrap: without this it pushes the card wider than its
#     column and takes the page's horizontal scroll with it. Photographed at
#     390px with a long URL in the body before this was added.
_SO_FEED_BODY = ("margin-top:6px;font:400 17px/1.55 var(--st-ui);"
                 "color:var(--st-body);white-space:pre-wrap;"
                 "overflow-wrap:anywhere")
_SO_FEED_EMPTY = ("padding:26px 18px;background:var(--st-paper);"
                  "border:1px dashed var(--st-rule-soft);border-radius:11px;"
                  "font:400 17px/1.45 var(--st-ui);color:var(--st-muted)")

# ══ ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK — THE STYLE STRINGS ══
#
# See `FEEDBACK_SURFACE_ADDED` at the top of this file for the ruling.
#
# ⚑ DESIGN DREW NO PER-SUBMISSION FEEDBACK UI AT ALL. Her only `<textarea>`
# in the whole v3 delivery is the bulk sheet's, and there is no comment
# affordance on the student screen, the marking grid or anywhere else. So —
# unlike `WEEK_BAR_RESTORED` and `SHOUTOUT_SURFACE_RESTORED`, both of which
# put back something Design had drawn and removed — there is no drawing to be
# faithful to here.
#
# ⚠️ THAT IS NOT A LICENCE TO INVENT A REGISTER. Every string below is read
# off a v3 node and the node is named, exactly as the shoutout strings are:
# the sheet is Design's bulk-sheet chrome (629-654, already extracted as the
# `_DEL_*` family), the caption is her mono caption (640), the textarea is her
# textarea (651) with a taller minimum because 2000 characters is a paragraph
# and 500 is a sentence, and the row control is her own low-emphasis text
# button (the "Back to <class>" control, already extracted as `_DEL_TEXT_BTN`).
# Nothing here is a new idiom; this port has ONE dialog and this is it.

# The row control, on the student screen's history table and on the marking
# grid. `_DEL_TEXT_BTN`'s register, with the colour bound so a row that
# already HAS a comment reads in the ink Design uses for a live value and an
# empty one in the muted register she uses for an action.
# ⚠️ `display:block`, WHICH IT DID NOT HAVE AND WHICH THE SCREENSHOT
# SETTLED. Design's status chip (367) is `display:inline-flex`, so an inline
# button after it sat ON THE SAME LINE — "LATE Edit feedback", two different
# things reading as one phrase — and `margin-top` on an inline element does
# nothing at all, so the declaration that was supposed to separate them was
# inert. Block, and the margin then works.
_FB_ROW_BTN = ("display:block;margin-top:7px;font:600 14.5px/1.2 var(--st-ui);"
               "background:none;border:none;padding:0;cursor:pointer;"
               "text-align:left;white-space:nowrap;color:")

# ⛔ THE MARKING GRID GETS A GLYPH AND NOT A WORD, AND THAT IS A MEASUREMENT
# RATHER THAN A PREFERENCE. Design's student cell (420) sits in a HARD 225px
# track — `225px repeat(8,1fr) 92px`, declared on the header (413) and on the
# row (419) — holding a 30px avatar, a 10px gap and a name that already
# carries `text-overflow:ellipsis`. Photographed with a text button in it,
# every name with a comment beside it was cut to "Clara…" and "Kale…" while
# the rows WITHOUT one still read in full: the control was eating the one
# thing a teacher reads the column for, and only on the rows that mattered
# most.
#
# The alternatives were all worse. The mark cell (426) is 92px and would have
# to grow, which means rewriting a track list Design declares twice. Wrapping
# inside 420 needs `flex-wrap` on one of Design's own style strings, and
# `SET_ATTR` refuses to overwrite one — correctly.
#
# So it is a 22px speech mark, `flex:none`, with the full sentence in
# `aria-label` and in `title`. It costs the name 32px instead of ~110px, it
# is TINTED where a comment exists and ghosted where it does not — which
# makes "who has been written to" scannable down the column in a way a
# repeated word never is — and it is the same builder, the same handler and
# the same sheet as the student screen's. One implementation, two
# affordances, because the two cells are different sizes.
_FB_CELL_BTN = ("flex:none;margin-left:auto;width:22px;height:22px;"
                "display:flex;align-items:center;justify-content:center;"
                "background:none;border:none;padding:0;cursor:pointer;"
                "color:")

# The sheet's own body. `_DEL_BODY` is the pad; these are what sits in it.
_FB_CAP = _SO_CAP                                                # node 640
_FB_CAP2 = "margin-top:20px;" + _SO_CAP

_FB_ON = ("font:400 15.5px/1.5 var(--st-ui);color:var(--st-body)")

# ⚠️ TALLER THAN THE COMPOSER'S, AND THE NUMBER IS THE DATABASE'S REASON.
# `submission_feedback_body_length_chk` allows 2000 characters where
# `class_shoutouts_message_length_chk` allows 500 — feedback on a piece of
# work is a paragraph, a shoutout is a sentence — and a 70px box for 2000
# characters is a control that hides most of what has been written in it.
# Every other declaration is node 651's, verbatim.
_FB_NOTE = ("width:100%;margin-top:10px;min-height:150px;padding:12px;"
            "font:400 17px/1.5 var(--st-ui);color:var(--st-ink);"
            "background:var(--st-paper);border:1px solid var(--st-btn-border);"
            "border-radius:10px;resize:vertical")

# A colleague's comment, which this teacher may read and may not change (RLS:
# `submission_feedback_update` is `teacher_id = auth.uid()`). Design's own
# note ground, and `white-space:pre-wrap` + `overflow-wrap:anywhere` for the
# same two reasons the shoutout feed's body carries them: a teacher's
# paragraph has newlines in it, and an INERT url has to wrap rather than push
# the sheet sideways.
_FB_READ = ("margin-top:10px;padding:14px;background:var(--st-note-bg);"
            "border:1px solid var(--st-rule-soft);border-radius:10px;"
            "font:400 17px/1.55 var(--st-ui);color:var(--st-body);"
            "white-space:pre-wrap;overflow-wrap:anywhere")

_FB_BY = ("margin-top:10px;font:400 13px/1.4 var(--st-mono);"
          "letter-spacing:.12em;text-transform:uppercase;"
          "color:var(--st-caption)")

# The validation line. `--st-accent-text` is Design's own colour for anything
# that needs attention on this surface (the overdue chips, the reteach note).
_FB_ERR = ("margin-top:10px;font:400 15.5px/1.45 var(--st-ui);"
           "color:var(--st-accent-text)")

_FB_COUNTER = _SO_COUNTER

# ⛔ THE FOOTER WRAPS, AND A 390px SCREENSHOT IS WHAT SAID SO. `_DEL_FOOT` is
# Design's bulk-sheet footer and it is `justify-content:space-between` with no
# wrap — correct for the shoutout confirm, whose note is the four words "This
# cannot be undone". This sheet's note is a whole sentence, and a flex item's
# default `min-width:auto` will not shrink below its content: at 390 the note
# took its min-content width, the Remove/Save pair was pushed off the panel's
# right edge, and "Save changes" was reachable only by scrolling the panel
# SIDEWAYS.
#
# ⚠️ AND NO GATE COULD SEE IT. The overflow probe counts elements whose right
# edge passes the DOCUMENT's width; this one passed the PANEL's, and the panel
# is `overflow:auto`, so nothing overflowed the page and every measurement
# came back clean. It was found by looking at the picture.
#
# `_DEL_FOOT` itself is NOT changed — it is shared with the shoutout confirm,
# which does not have the problem and has already been photographed without
# it. This sheet gets its own, wrapping, with the actions pushed right on
# whichever line they end up on.
_FB_FOOT = _DEL_FOOT + ";flex-wrap:wrap"
_FB_ACTIONS = "display:flex;align-items:center;gap:12px;margin-left:auto"


def _fb_open_button(row, style, glyph=False):
    """The control that opens the feedback sheet, for one row of one table.

    ⚑ ONE BUILDER, TWO SURFACES, WHICH IS THE POINT. Mide's brief is that
    feedback is authored "from student detail or marking" — both, and one
    implementation. The row scope differs (`h` on the student screen's
    submission history, `r` on the marking screen's class-by-question grid)
    and nothing else does: the same label, the same handler shape, the same
    sheet behind it, and the same `data-mrb-added` marker so
    `teacher_behaviour` presses it on both pages.

    ⚠️ IT IS INSIDE AN `<if>` ON `<row>.fbCan`. A row with no submission has
    nothing to attach a comment to — `submission_feedback.submission_id` is
    NOT NULL and there is no other binding — so the control is ABSENT rather
    than present-and-refusing. That is the same reading MRB-261's read-only
    rule takes, and the retired page's `applyWriteControls` states the
    standard: absent, not disabled.

    ⚠️ AND IT IS NOT A WRITE CONTROL, which is why it carries no `canWrite`
    gate and no `needs_write` in the register. On a finished academic year a
    teacher may still READ what was written about a child — MRB-261 makes a
    past year read-only, not invisible — and the two controls inside the sheet
    that would CHANGE anything are the ones that go.
    """
    return {
        "t": "if", "e": row + ".fbCan",
        "c": [{
            "t": "button",
            "a": {"type": "button",
                  "data-mrb-added": "feedback-open",
                  "aria-label": {"parts": [{"e": row + ".fbAria"}]},
                  "title": {"parts": [{"e": row + ".fbAria"}]},
                  "style": {"parts": [style, {"e": row + ".fbFg"}]}},
            "hov": "color:var(--st-ink)",
            # ⚠️ STOPS THE PRESS FROM REACHING THE ROW. Both rows Design drew
            # are themselves clickable — the history row navigates to the
            # marking screen, the grid row to the student screen — so without
            # `stopPropagation` inside the closure, opening a comment would
            # simultaneously navigate away from the page the sheet just opened
            # on. The closure does it (see the `fbOpen` entries in LOGIC)
            # rather than Design's `stop` handler, because `stop` alone would
            # swallow the press and open nothing.
            "on": row + ".openFb",
            # ⚠️ THE GLYPH CARRIES THE SAME `aria-label` THE WORDS WOULD
            # HAVE. `title` as well, because a mouse user gets no accessible
            # name read to them and "what is this button" must not need a
            # screen reader to answer.
            "c": ([{"t": "svg",
                    "a": {"width": "16", "height": "16",
                          "viewBox": "0 0 16 16", "fill": "none",
                          "aria-hidden": "true"},
                    "c": [{"t": "path",
                           "a": {"d": "M2.6 3.2h10.8v7.2H7.4L4.4 13v-2.6H2.6z",
                                 "stroke": "currentColor",
                                 "stroke-width": "1.4",
                                 "stroke-linejoin": "round",
                                 "fill": {"parts": [{"e": row + ".fbFill"}]}}}]}]
                  if glyph else
                  [{"t": "#", "v": {"parts": [{"e": row + ".fbLabel"}]}}]),
        }]}


def _fb_sheet():
    """The one feedback sheet, emitted on the student screen and on marking.

    ⚠️ EMITTED TWICE, WRITTEN ONCE. `INSERT_AT` is keyed by the parent node
    and the two screens have different roots (330 and 370), so there are two
    entries — but they are two calls to this function, not two subtrees, and a
    change to the sheet cannot land on one screen and miss the other.

    ⚠️ NOT APPENDED TO NODE 9. Design's own four overlays live there and node
    9 is on all six pages; a feedback sheet hung off it would be markup on
    four pages that can never open it. The shoutout confirm was moved off node
    9 for exactly this and the reasoning is recorded at `INSERT_AT[(208,
    None)]`.

    ── ⛔ THERE IS NO REPLY PATH, AND THERE IS NOT A DISABLED ONE ─────────
    #
    Mide's guardrail is that v1 is ONE-WAY. `submission_feedback` has no
    student INSERT policy at all, so a reply control — even greyed out, even
    behind a flag — would be a promise to a child that the database will
    refuse. The footer says so in words instead, to the TEACHER, because the
    person who needs to know the child cannot answer is the person writing.

    ── the three states this sheet has ──────────────────────────────────
      · nothing written yet ......... caption, empty textarea, Save
      · this teacher's own comment .. byline, the text in the textarea to
                                      edit, Save, and Remove behind a
                                      second press
      · a colleague's comment ....... byline, the text as READ-ONLY prose,
                                      and neither Save nor Remove — RLS's
                                      update policy is `teacher_id =
                                      auth.uid()`, so offering either would
                                      be offering a refusal
    A past year removes the writing half of all three (`canWrite`), and
    leaves the reading half, for the reason above.
    """
    return {
        "t": "if", "e": "fbOpen",
        "c": [{
            "t": "div", "a": {"style": _DEL_SCRIM}, "on": "closeFeedback",
            "c": [{
                "t": "div", "a": {"style": _DEL_PANEL}, "on": "stop",
                "c": [
                    {"t": "div", "a": {"style": _DEL_HEAD}, "c": [
                        {"t": "div", "c": [
                            {"t": "div", "a": {"style": _DEL_KICKER}, "c": [
                                {"t": "#", "v": {"parts": [
                                    {"e": "fbKicker"}]}}]},
                            {"t": "div", "a": {"style": _DEL_TITLE}, "c": [
                                {"t": "#", "v": {"parts": [
                                    {"e": "fbTitle"}]}}]},
                        ]},
                        {"t": "button",
                         "a": {"type": "button",
                               "data-mrb-added": "feedback-close",
                               "aria-label": "Close without saving",
                               "style": _DEL_CLOSE},
                         "on": "closeFeedback",
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
                        # Which piece of work this is about. The binding is
                        # the whole of "context-bound": there is no inbox
                        # here, and the sheet says which submission it is
                        # attached to rather than leaving a teacher to
                        # remember which row they pressed.
                        {"t": "div", "a": {"style": _FB_ON},
                         "c": [{"t": "#", "v": {"parts": [{"e": "fbOn"}]}}]},

                        # ATTRIBUTED. "You", or "Another teacher" — see
                        # `buildFeedback` in teacher-live.js for why a
                        # colleague's NAME is not reachable from a teacher
                        # session and why a blank byline was not an option.
                        {"t": "if", "e": "fbByLine", "c": [
                            {"t": "div", "a": {"style": _FB_BY},
                             "c": [{"t": "#", "v": {"parts": [
                                 {"e": "fbByLine"}]}}]},
                        ]},

                        # ⛔ THE WORDS, WHEREVER THEY CANNOT BE EDITED — and
                        # the condition is NOT "somebody else wrote it",
                        # which is what it said until a read-only fixture was
                        # driven. A teacher opening their OWN comment on a
                        # FINISHED academic year got the byline, the footer
                        # and no text at all: `fbTheirs` was false (it is
                        # theirs) and `fbCanEdit` was false (`canWrite` is),
                        # so neither branch drew and the sheet said who wrote
                        # it and not what they wrote.
                        #
                        # MRB-261 is READ-ONLY, NOT INVISIBLE. The predicate
                        # is therefore "there is a comment and there is no
                        # editor for it", which covers both ways that
                        # happens: a colleague's (RLS's update policy is
                        # `teacher_id = auth.uid()`) and a finished year.
                        #
                        # It renders through a TEXT NODE — `student-runtime`
                        # writes every interpolation with `createTextNode` —
                        # so a URL a teacher typed is inert here as well.
                        {"t": "if", "e": "fbReadBody", "c": [
                            {"t": "div", "a": {"style": _FB_READ},
                             "c": [{"t": "#", "v": {"parts": [
                                 {"e": "fbBodyText"}]}}]},
                        ]},

                        {"t": "if", "e": "fbCanEdit", "c": [
                            {"t": "div", "c": [
                                {"t": "div", "a": {"style": _FB_CAP2},
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "fbFieldCap"}]}}]},
                                # ⛔ THE EXISTING TEXT IS PUT IN BY
                                # `MRB_FB_FILL`, NOT BY AN INTERPOLATION, AND
                                # THIS WAS FOUND BY LOOKING RATHER THAN BY
                                # READING. The first version rendered
                                # `{{ fbBody }}` as the textarea's child —
                                # correct for HTML, where a textarea's content
                                # IS its value — and the box came up EMPTY on
                                # every existing comment, under a caption
                                # reading "YOUR FEEDBACK". A teacher would
                                # have pressed Save on an empty box and
                                # replaced what they wrote.
                                #
                                # The cause is `student-runtime.build`: an
                                # INTERPOLATION in text position is wrapped in
                                # `<span class="sc-interp">` (Design's own
                                # compiler does it, and the parity gate counts
                                # those spans), so the textarea's child was an
                                # ELEMENT, and a textarea's default value
                                # comes only from child TEXT. `textContent`
                                # read correctly and `value` was "".
                                #
                                # So the field is uncontrolled, like Design's
                                # other three, and `openFb` fills it in
                                # `setState`'s completion callback — which
                                # runs AFTER the draw that creates it.
                                # `restoreFields` carries it over every later
                                # redraw, which is the same mechanism the
                                # shoutout composer relies on.
                                # ⚠️ `maxlength` IS THE DATABASE'S NUMBER —
                                # `submission_feedback_body_length_chk`, 2000.
                                # A cap a teacher discovers by being refused
                                # after writing a paragraph is not a cap.
                                {"t": "textarea",
                                 "a": {"data-mrb-added": "feedback-body",
                                       "data-compose-field": "feedback",
                                       "maxlength": "2000",
                                       "aria-label": "Write feedback",
                                       "placeholder": "What they did well, "
                                                      "and the one thing to "
                                                      "work on next",
                                       "style": _FB_NOTE},
                                 "onch": "setFbBody"},
                            ]},
                        ]},

                        {"t": "if", "e": "fbErr", "c": [
                            {"t": "div", "a": {"style": _FB_ERR,
                                               "role": "alert"},
                             "c": [{"t": "#", "v": {"parts": [
                                 {"e": "fbErr"}]}}]},
                        ]},
                    ]},
                    {"t": "div", "a": {"style": _FB_FOOT}, "c": [
                        {"t": "div", "a": {"style": _DEL_FOOT_NOTE},
                         "c": [{"t": "#", "v": {"parts": [
                             {"e": "fbFootNote"}]}}]},
                        {"t": "div", "a": {"style": _FB_ACTIONS}, "c": [
                            {"t": "if", "e": "fbCanRemove", "c": [
                                # ⚠️ TWO PRESSES, NOT A SECOND SHEET. The
                                # shoutout delete gets a confirm dialog
                                # because it sits eight pixels from a child's
                                # name in a feed. This one is already inside a
                                # sheet the teacher deliberately opened, with
                                # the words they are about to remove on screen
                                # above it — so the protection is the button
                                # changing to say what it will do, and a
                                # dialog on top of a dialog would be a second
                                # idiom for the same job.
                                {"t": "button",
                                 "a": {"type": "button",
                                       "data-mrb-added": "feedback-remove",
                                       "style": _DEL_TEXT_BTN},
                                 "hov": "color:var(--st-ink)",
                                 "on": "removeFeedback",
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "fbRemoveLabel"}]}}]},
                            ]},
                            {"t": "if", "e": "fbCanEdit", "c": [
                                {"t": "button",
                                 "a": {"type": "button",
                                       "data-mrb-added": "feedback-save",
                                       "style": _DEL_PRIMARY},
                                 "hov": "background:var(--st-accent-hover)",
                                 "on": "saveFeedback",
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "fbSaveLabel"}]}}]},
                            ]},
                        ]},
                    ]},
                ]}]}]}


INSERT_AT = {
    # ── ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 5) · NOTHING TO BREAK DOWN ─
    #
    # ⛔ THE ONE STATE THIS SCREEN IS REQUIRED TO SURVIVE HAD NO WORDS. When
    # `gridFor` returns null — a grid key that is absent, which is what
    # happens whenever a class's papers are all still open and `load()`
    # therefore prefetched nothing — `questions` is `[]` and Design's
    # `sc-for` renders zero rows. Nothing throws. What a teacher gets is the
    # heading "Question breakdown", a hairline, and empty space.
    #
    # ⚠️ THE SENTENCE DOES NOT SAY "NOT FETCHED", and that is deliberate.
    # Which of the two causes produced the empty list is a fact about the
    # prefetch policy, not about the class: on this screen a null grid is
    # only ever reachable when nothing on the paper has been marked, so
    # "no marks yet" is true in both cases and is the half a teacher can act
    # on. It also stays true if the policy changes.
    #
    # ⚠️ IT IS INSIDE THE CARD, AFTER THE `sc-for` (node 391), so it cannot
    # appear beside rows: the `if` and the `for` are exclusive by
    # construction — `noQuestions` is `questions.length === 0` and the `for`
    # is over the same list.
    (390, 391): ({
        "t": "if", "e": "paper.noQuestions",
        "c": [{
            "t": "div",
            "a": {"style": "padding:26px 18px;"
                           "font:400 17px/1.45 var(--st-ui);"
                           "color:var(--st-muted)"},
            "c": [{"t": "#",
                   "v": "No question-by-question marks for this paper yet."}],
        }]},
        "the marking screen's question breakdown, with no grid. Design drew "
        "no empty state here because her sample always has eight marked "
        "questions."),

    # ── ⊕ RULED BY MIDE, 1 Sep 2026 · THE WEEK BAR ─────────────────────
    #
    # See `WEEK_BAR_RESTORED` at the top of this file for the ruling and for
    # what is deliberately different from v2. This is the markup half; the
    # logic half is LOGIC #6, #13, #36 and the week-bar entries at the end of
    # LOGIC, and the data half is `buildWeeks` / `assignPaperWeeks` in
    # `shared/teacher-live.js`.
    #
    # ⚠️ THE MARKUP AND THE KEYS SHIP TOGETHER OR NEITHER SHIPS. `weekTabs`
    # with nowhere to render is invisible — the page builds, every gate is
    # green, and the bar Mide ruled is simply not there. `weekBack` with no
    # button is the opposite failure and the one `teacher_behaviour` catches:
    # a handler nothing calls.
    #
    # ⚑ IT IS AN ADDITION AGAINST DESIGN'S v3 and is registered in
    # `AMENDED_ADDITIONS` for that reason — but it is not new design. Every
    # style string is v2's, read out of the delivery rather than retyped, and
    # Design drew all of it. What changed is that she removed it and Mide put
    # it back.
    #
    # ⚠️ PLACED AFTER NODE 218 — the class header (code, meta, stat line),
    # which owns the rule under it — and therefore before node 222, v3's
    # `glance` grid. That is exactly where v2 drew it: under the header,
    # above everything the week scopes.
    #
    # ⚠️ GATED ON `klass.hasWork`, WHICH IS DESIGN'S OWN RULE AND SURVIVES THE
    # RE-INDEXING. The weeks now come from the academic year rather than from
    # the class's assignments, so a class with no work set HAS twelve weeks —
    # and a bar over a class with nothing to scope is a control that does
    # nothing whichever chip you press. The seam's `weeks()` ruling says the
    # same thing from the other side.
    #
    # ⚠️ THE CHIP'S SECOND LINE HAS NO `if` ANY MORE. v2 wrapped it in
    # `sc-if w.now` and rendered "This week" on one chip out of twelve,
    # because its ranges identified the weeks inside its own fiction. Dated
    # from a real academic year they do not — "5–9 Oct" says nothing about
    # which teaching week it is — so the line carries "This week" or the
    # term-relative label on every chip, in Design's own type. An
    # always-true `if` was the alternative, and a dead conditional cannot be
    # told from a broken one.
    (208, 218): ({
        "t": "if", "e": "klass.hasWork",
        "c": [
            {"t": "div",
             "a": {"class": "noprint", "style": _WK_BAR},
             "c": [
                 {"t": "span", "a": {"style": _WK_CAPTION},
                  "c": [{"t": "#", "v": "Week"}]},
                 _wk_chevron("weekBack", "Previous week", "M9 3L5 7l4 4",
                             "weekBackColor", "weekBackCursor", "week-back"),
                 {"t": "div",
                  "a": {"data-rail": "weeks", "style": _WK_RAIL},
                  "c": [{
                      "t": "for", "e": "weekTabs", "as": "w",
                      "c": [{
                          "t": "button",
                          "a": {"type": "button",
                                "data-mrb-added": "week-chip",
                                "data-week": {"parts": [{"e": "w.idx"}]},
                                "aria-pressed": {"parts": [{"e": "w.on"}]},
                                "style": {"parts": [
                                    _WK_CHIP, {"e": "w.bg"},
                                    ";border:none;border-left:1px solid ",
                                    {"e": "w.divider"},
                                    ";box-shadow:", {"e": "w.ring"},
                                    ";border-radius:9px;cursor:pointer"]}},
                          "hov": "background:var(--st-note-bg)",
                          "on": "w.pick",
                          "c": [
                              {"t": "span",
                               "a": {"style": {"parts": [
                                   _WK_RANGE, {"e": "w.dateColor"},
                                   ";white-space:nowrap"]}},
                               "c": [{"t": "#",
                                      "v": {"parts": [{"e": "w.range"}]}}]},
                              {"t": "span",
                               "a": {"style": {"parts": [
                                   _WK_SUB, {"e": "w.subFg"}]}},
                               "c": [{"t": "#",
                                      "v": {"parts": [{"e": "w.sub"}]}}]}
                          ]}]}]},
                 _wk_chevron("weekFwd", "Next week", "M5 3l4 4-4 4",
                             "weekFwdColor", "weekFwdCursor", "week-fwd")
             ]},
            {"t": "div", "a": {"style": _WK_NOTE},
             "c": [{"t": "#", "v": {"parts": [{"e": "weekNote"}]}}]}
        ]},
        "the class screen's week bar — Mide's ruling of 1 Sep 2026, against "
        "Design's v3, which deleted it. Twelve teaching weeks of the "
        "academic year, newest first; pressing one re-scopes the glance "
        "block, the roster column and the assignment table. v2's markup, "
        "style string for style string."),

    # ── ⊕ RULED, MRB-304 · A PERSISTENT WAY BACK TO THE CLASS LIST ──────
    #
    # ⛔ THE BRAND MARK WAS DOING THIS JOB AND HAS STOPPED. See `RETARGET_ON`:
    # node 11 now goes to the public homepage, on Mide's instruction, which
    # takes the only always-on route to `teacher/classes.html` off five of the
    # six screens. A brand that goes home and no other way back would be a
    # regression dressed as a fix.
    #
    # ⚑ MIDE'S INSTRUCTION, 31 Aug 2026: "every page in the teacher portal
    # should present the same header affordances — brand to home, and a
    # separate My classes control to the dashboard, present and working
    # identically everywhere." The two hand-written teacher pages already do
    # exactly this, and their markup is the pattern being mirrored:
    #
    #     <a href="/index.html" …>MrBadmusAI</a>
    #     <div class="nav-right">
    #       <a href="/teacher/classes.html" …>My classes</a>
    #
    # So this is an AMENDED ADDITION against Design's delivery — registered in
    # `AMENDED_ADDITIONS`, which is how it becomes visible to the drive gate —
    # and not a correction of it. Design drew one file with one screen at a
    # time and a brand mark that switched between them; the six-URL port is
    # what makes a second control necessary, and the port is this file's doing
    # rather than hers.
    #
    # ⚠️ IT REUSES `goClasses` RATHER THAN INVENTING A HANDLER. That is the
    # handler node 11 has just stopped calling and node 83 still does — it
    # carries `year: MRB_DATA('yearParam')`, so a teacher browsing 2025–26
    # comes back to 2025–26 from any of the six screens rather than being
    # silently returned to the working year. A fresh `goClassList` would have
    # been a second answer to a question MRB-287 E1 already answered.
    #
    # ⚠️ IT WAS ON ALL SIX PAGES INCLUDING classes.html, where it re-entered
    # the page it was on. That was deliberate: the header is chrome, chrome
    # is identical everywhere, and a control that appears and disappears
    # depending on which screen you are on is a harder thing for a teacher
    # to learn than one that is always there.
    #
    # ⊕ SUPERSEDED, Mide, 4 Sep 2026. On classes.html the crumb beside it
    # (node 14) ALREADY reads "My classes" — that screen's `crumb` value is
    # literally the string "My classes" — so the always-there argument above
    # bought consistency at the cost of two controls saying the same thing
    # in the same breath, one of them a press that reloads the page you are
    # already reading. Wrapped in an `if` on `showClassesLink`
    # (shared/teacher-live.js), true on every screen except classes.html, so
    # the button still appears identically on the other five and the crumb
    # alone answers "where am I" on the one screen where the two would have
    # agreed.
    #
    # ⚠️ STILL COMPILED INTO ALL SIX. The `if` is a RUNTIME condition, not a
    # build-time one — this node carries no `i` (INSERT_AT never gives one)
    # and is inserted once into the shared template tree the six pages all
    # emit from, so `"data-mrb-added":"nav-classes"` is in classes.html's
    # bytes exactly as it always was; build_teacher_port.py's own byte check
    # would refuse the build otherwise. `AMENDED_ADDITIONS`'s `nav-classes`
    # entry keeps `pages` naming all six for that reason, and adds
    # `runtime_hidden_on=("classes.html",)` instead — the field
    # `teacher_behaviour.py` reads to stop expecting a PRESS there without
    # claiming the markup is gone.
    #
    # Placed AFTER node 13 — Design's crumb block, with its own left rule —
    # and before node 15, the search button that carries `margin-left:auto`.
    # So it sits in the left-hand group with the brand and the crumb, and the
    # right-hand group Design drew is untouched.
    #
    # ── ⊕ 4 Sep 2026, ON THE v3 MERGE — READ THE TWO NOTES IN ORDER ──────
    #
    # ⚠️ THE PARAGRAPHS ABOVE AND THE ONE BELOW LOOK LIKE THEY DISAGREE, AND
    # THEY DO NOT — they are two dates. `main` shipped the `if
    # showClassesLink` wrap TODAY, against the v2-based pages, to stop the
    # button and the crumb both saying "My classes" on the classes screen.
    # This branch had already RETIRED the whole insertion, because v3's top
    # bar draws the control itself. Merging the two would have put the
    # button back beside Design's own tab — the duplicate `main` had just
    # removed, in a new place. The retirement below wins on the merged tree,
    # and it satisfies `main`'s fix as well as MRB-304's ruling.
    #
    # ⚠️ WHAT SURVIVES THE RETIREMENT, AND IS NOW READ BY NOTHING:
    # `showClassesLink` is still computed in `shared/teacher-live.js`'s
    # `load()`, still written into the fixture payload by
    # `build_teacher_port.py`, and still exposed by the `LOGIC` entry below.
    # With the insertion gone no `<if>` reads it. It is KEPT rather than
    # unpicked across three files during a merge — it is an inert boolean
    # that cannot reach a screen — and it is named HERE so that a future
    # reader finds the answer instead of the puzzle. Deleting the three is a
    # tidy-up, not a fix, and it belongs in a run of its own.
    #
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — RETIRED, BECAUSE DESIGN DREW IT.
    #
    # The insertion that was here put a "My classes" button into the top bar
    # after Design's crumb. v3's top bar opens with a TAB STRIP of her own —
    # node 13 holding `<for navTabs>`, whose two tabs are literally "Today"
    # and "My classes", present on every screen, with the active one lit.
    # That is Mide's 31 Aug requirement — "a separate My classes control to
    # the dashboard, present and working identically everywhere" — arriving
    # in Design's own hand, exactly as v3 independently arrived at the other
    # half of MRB-304 (`RETARGET_ON`, where the wordmark had already stopped
    # pointing at the class list).
    #
    # ⚠️ SO THE RULING IS SATISFIED, NOT DROPPED. Keeping the insertion as
    # well would put TWO "My classes" controls eight pixels apart in a 62px
    # bar, one lit and one not.
    #
    # ⚠️ AND IT ONLY COUNTS BECAUSE THE TAB WAS REWIRED. Design's `t.pick` is
    # `this.setState({ screen: t.id })`, and on a page where every screen but
    # one is pruned that press renders NOTHING — the same blank-page failure
    # `c.act` shipped with in August. See the `navTabs` entry in `LOGIC`: both
    # tabs are real navigations now, and the "My classes" one carries
    # `yearParam` exactly as this insertion's `goClasses` did, so a teacher
    # browsing 2025-26 still comes back to 2025-26.

    # ── the environment badge, conditional now ──────────────────────────
    #
    # ⊕ MRB-287, 26 Aug 2026 — Design's v2 deleted the nav's `PROD` chip, so
    # the old `BINDINGS_AT` row (26: "PROD" → envBadge) lost its node. The
    # chip's reason to exist was never "say PROD on prod": it is the thing
    # that stops somebody driving the wrong database. Both rulings hold at
    # once by making it conditional — `envBadge()` returns "" on the live
    # production origin, so this `if` renders nothing there (v2's exact
    # drawing) and renders TEST / LOCAL anywhere it would matter. Styling is
    # v1's own chip, at v2's 12px nav scale.
    (10, 25): ({
        "t": "if", "e": "envBadge",
        "c": [{
            "t": "span",
            "a": {"style": "flex:none;padding:5px 8px;"
                           "font:500 12px/1.2 var(--st-mono);"
                           "letter-spacing:.16em;color:var(--st-caption);"
                           "background:var(--st-num-well);border-radius:6px"},
            "c": [{"t": "#", "v": {"parts": [{"e": "envBadge"}]}}],
        }]},
        "the environment badge, off the page on production and on it "
        "anywhere a teacher could be driving the wrong database."),

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
    #
    # ⊕ RECOLOURED 2 Sep 2026 (MRB-306 Phase 2a screen 5) — AND THE COLOUR WAS
    # THE WHOLE POINT OF THE STATE.
    #
    # ⛔ IT WAS `--st-hatch-b`, CHOSEN AS "PRESENT-BUT-NEUTRAL". It is not
    # neutral. `--st-hatch-b: #B33E1C` is declared INSIDE the accent block of
    # `src-styles-tokens.css`, between `--st-accent: #E4572E` and
    # `--st-accent-text: #A93411`, and on this very page that hue is the
    # vocabulary of alarm: the "Reteach next lesson" banner, the RETEACH tag,
    # the chase line, the late chip, the flagged child.
    #
    # ⚠️ FOUND BY LOOKING, NOT BY READING. On
    # `assignment-empty-fixture.html` the fourth state rendered as a row of
    # eight rust squares against one child's name, and it reads louder than
    # the hollow ring that actually MEANS incorrect. The state exists to stop
    # a written answer being reported as a wrong one; drawn in the accent it
    # reported it as something worse.
    #
    # `--st-caption` (#7A6E5F) is a neutral warm grey from the cream block —
    # the legend row's own ink, so the swatch reads as a marker rather than as
    # a status — and it stays plainly distinct from the dash's much lighter
    # `--st-rule-strong` (#D6C6A8). Geometry is unchanged: still the 9x9
    # square with 2px corners, so the state is still told apart by SHAPE and
    # not only by colour.
    (403, 408): ({
        "t": "span", "a": {"style": _LEGEND_KEY},
        "c": [
            {"t": "span", "a": {"style": "width:9px;height:9px;"
                                         "border-radius:2px;"
                                         "background:var(--st-caption)"}},
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
    (158, 177): ({
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
    (203, 206): ({
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
    # ⚠️ APPENDED TO NODE 91 — v2's header identity block, the bordered
    # `padding-bottom` div holding the class-code `<h1>` (92) and the
    # `longMeta` line (93). v1 tucked this chip beside a subject-dots pill in
    # a flex-wrapped h1 row; v2 deleted that pill and flattened the header,
    # so the chip now lands as a full-width band under the meta line — which
    # reads MORE loudly, and read-only is a state worth reading loudly.
    # Not into node 82's action row: that is `space-between` and a third
    # child there would push the header actions off their edge.
    (218, None): ({
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

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · THE SHOUTOUT SECTION ══════════════
    #
    # ⛔ THIS IS A DELIBERATE DIVERGENCE FROM DESIGN'S v3, NOT A GAP BEING
    # FILLED. v3 IS DRAWN WITH NO COMPOSER AND NO FEED. Read
    # `SHOUTOUT_SURFACE_RESTORED` at the top of this file BEFORE removing any
    # of this as drift — it is the ruling, and the drawing is not the
    # authority for this section. The same treatment `WEEK_BAR_RESTORED` got,
    # for the same reason.
    #
    # ⚠️ PLACED AFTER NODE 306 — the assignments table — so it is the LAST
    # thing on the class screen. That is where v2 drew it (below the work),
    # and it is where it belongs against v3's reorganisation: the glance
    # tiles are what a teacher opens this page to act on, and node 267's
    # "Worth a shoutout" list ends with node 276's "Send a shoutout". A
    # teacher who follows that reads down into this section rather than
    # scrolling back up past the roster.
    #
    # ⚠️ THE COMPOSER IS INSIDE AN `if canWrite` AND THE FEED IS NOT. MRB-261
    # makes a finished academic year READ-ONLY, not invisible: what was
    # written about a child last year is still readable, and the two controls
    # that could CHANGE it — this composer and the feed's Remove — are the
    # ones that go. `canWrite` is the same key `WRAP` puts on nodes 215 and
    # 276, so the three write surfaces on this screen cannot disagree.
    # ⛔ THE `if` CANNOT BE A `WRAP` ROW. `WRAP` is keyed by Design's node
    # index and every node here is inserted markup with no `i` — that is
    # `INSERT_AT`'s own rule, so Design's numbering never moves — so there is
    # no index to key on. The conditional has to be in the subtree.
    #
    # ⚠️ THE RIGHT-HAND SIDE OF THE HEADING IS A CAPTION, NOT A THIRD BULK
    # OPENER. v2 put "Send to several students" there (its node 183). v3
    # already opens the bulk sheet from node 215 in the header AND node 276
    # at the foot of the watch tile; a third would be the same control three
    # times on one screen. The count is what the heading has to say instead,
    # in node 285's treatment.
    (208, 306): ({
        "t": "div",
        "c": [
            {"t": "div", "a": {"style": _SO_HEAD}, "c": [
                {"t": "h2", "a": {"style": _SO_H2},
                 "c": [{"t": "#", "v": "Shoutouts"}]},
                {"t": "span", "a": {"style": _SO_COUNT},
                 "c": [{"t": "#", "v": {"parts": [{"e": "feedCount"}]}}]},
            ]},
            {"t": "div", "a": {"style": _SO_GRID}, "c": [

                # ── the composer, on a year that can be written to ──────
                {"t": "if", "e": "canWrite", "c": [
                    {"t": "div", "a": {"class": "noprint",
                                       "style": _SO_CARD}, "c": [
                        {"t": "div", "a": {"style": _SO_CAP},
                         "c": [{"t": "#", "v": "Send a shoutout to"}]},
                        # ⚠️ THE OPTION CARRIES `s.id`, NOT `s.name`.
                        # MRB-287's ruling, written in from the start rather
                        # than corrected afterwards by `BIND_ATTR` the way
                        # v2's had to be: `insertClassShoutout` stores
                        # `recipient_id`, RLS checks the recipient is a
                        # CURRENT member of this class, and two children in
                        # one class can share a first name and a surname.
                        # The visible LABEL is still `s.name`.
                        # ⚠️ `data-compose-field` IS WHAT `MRB_COMPOSE_RESET`
                        # QUERIES. Design's fields are uncontrolled and
                        # `student-runtime` carries field values across a
                        # redraw on purpose, so clearing the state alone
                        # leaves the typed text on screen.
                        {"t": "select",
                         "a": {"data-mrb-added": "shoutout-recipient",
                               "data-compose-field": "recipient",
                               "aria-label": "Send a shoutout to",
                               "style": _SO_SELECT},
                         "onch": "pickRecipient",
                         "c": [
                             {"t": "option", "a": {"value": ""},
                              "c": [{"t": "#", "v": "Select a student"}]},
                             {"t": "for", "e": "roster", "as": "s", "c": [
                                 {"t": "option",
                                  "a": {"value": {"parts": [{"e": "s.id"}]}},
                                  "c": [{"t": "#", "v": {"parts": [
                                      {"e": "s.name"}]}}]},
                             ]},
                         ]},
                        {"t": "div", "a": {"style": _SO_CAP2},
                         "c": [{"t": "#", "v": "Pick a template"}]},
                        {"t": "div", "a": {"style": _SO_TPL_GRID}, "c": [
                            {"t": "for", "e": "templates", "as": "t", "c": [
                                {"t": "button",
                                 "a": {"type": "button",
                                       "data-mrb-added": "shoutout-template",
                                       "style": {"parts": [
                                           _SO_TPL_BTN, {"e": "t.fg"},
                                           ";background:", {"e": "t.bg"},
                                           ";border:1px solid ",
                                           {"e": "t.bc"}]}},
                                 "on": "t.pick",
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "t.label"}]}}]},
                            ]},
                        ]},
                        {"t": "div", "a": {"style": _SO_CAP2},
                         "c": [{"t": "#", "v": "Or write a message"}]},
                        # ⚠️ `maxlength` IS THE DATABASE'S NUMBER. 500 is
                        # `class_shoutouts_message_length_chk`, and it is
                        # here as well as in `sendShoutout` because a cap a
                        # teacher discovers by being refused after writing
                        # is not a cap, it is a rejection. `noteCount`
                        # counts up to it in Design's own foot.
                        {"t": "textarea",
                         "a": {"data-mrb-added": "shoutout-note",
                               "data-compose-field": "note",
                               "maxlength": "500",
                               "aria-label": "Write a message",
                               "placeholder": "Something specific you want "
                                              "to recognise",
                               "style": _SO_NOTE},
                         "onch": "setNote"},
                        {"t": "div", "a": {"style": _SO_FOOT}, "c": [
                            {"t": "span", "a": {"style": _SO_COUNTER},
                             "c": [{"t": "#", "v": {"parts": [
                                 {"e": "noteCount"}]}}]},
                            {"t": "button",
                             "a": {"type": "button",
                                   "data-mrb-added": "shoutout-send",
                                   "style": _SO_SEND},
                             "hov": "background:var(--st-accent-hover)",
                             "on": "sendShoutout",
                             "c": [{"t": "#", "v": "Send shoutout"}]},
                        ]},
                    ]},
                ]},

                # ── the feed, on every year ─────────────────────────────
                {"t": "div", "a": {"style": _SO_FEED_COL}, "c": [
                    {"t": "for", "e": "feed", "as": "f", "c": [
                        {"t": "div", "a": {"style": _SO_FEED_CARD}, "c": [
                            {"t": "div", "a": {"style": _SO_FEED_TOP}, "c": [
                                {"t": "div",
                                 "a": {"style": {"parts": [
                                     _SO_AVATAR, {"e": "f.hue"}]}},
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "f.initials"}]}}]},
                                {"t": "div",
                                 "a": {"style": "min-width:0;flex:1 1 auto"},
                                 "c": [
                                     {"t": "div",
                                      "a": {"style": _SO_FEED_NAME},
                                      "c": [{"t": "#", "v": {"parts": [
                                          {"e": "f.name"}]}}]},
                                     # ⊕ ATTRIBUTED. See the guardrail table
                                     # in SHOUTOUT_SURFACE_RESTORED: a feed
                                     # a teacher shares with colleagues has
                                     # to say whose sentence each one is.
                                     {"t": "div",
                                      "a": {"style": _SO_FEED_BY},
                                      "c": [{"t": "#", "v": {"parts": [
                                          {"e": "f.by"}, " \u00b7 ",
                                          {"e": "f.when"}]}}]},
                                 ]},
                                # ⛔ ONLY ON A SHOUTOUT THIS TEACHER WROTE,
                                # AND ONLY ON A YEAR THAT CAN BE WRITTEN TO.
                                # `f.canDelete` is both halves at once — see
                                # the `feed:` entry in LOGIC, which reads
                                # `MRB_DATA('canWrite')` and compares
                                # `f.author_id` to `MRB_ME()` — so the
                                # control is offered exactly where RLS would
                                # allow it, rather than looking pressable
                                # and being refused.
                                # ⚠️ THE WORD IS "REMOVE", NOT "DELETE". The
                                # write is a soft delete (`deleted_at`) and
                                # the read RPC filters it out, so the row
                                # leaves the feed for EVERYONE including its
                                # author. That is a real removal, which is
                                # what the word says.
                                {"t": "if", "e": "f.canDelete", "c": [
                                    {"t": "button",
                                     "a": {"type": "button",
                                           "class": "noprint",
                                           "data-mrb-added": "shoutout-"
                                                             "delete",
                                           "aria-label": "Remove this "
                                                         "shoutout",
                                           "style": "flex:none;margin-left:"
                                                    "auto;" + _DEL_TEXT_BTN},
                                     "hov": "color:var(--st-ink)",
                                     "on": "f.del",
                                     "c": [{"t": "#", "v": "Remove"}]},
                                ]},
                            ]},
                            {"t": "if", "e": "f.template", "c": [
                                {"t": "div", "a": {"style": _SO_FEED_TPL},
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "f.template"}]}}]},
                            ]},
                            # ⚠️ THE BODY IS INSIDE AN `if` AND v2'S WAS NOT.
                            # `class_shoutouts_content_chk` requires a
                            # template OR a message, so a template-only
                            # shoutout is a real and common row — and v2
                            # drew its empty body div regardless, which is
                            # eleven pixels of margin under a card that has
                            # nothing more to say. The same `if` is on the
                            # template line for the mirror-image row.
                            {"t": "if", "e": "f.body", "c": [
                                {"t": "div", "a": {"style": _SO_FEED_BODY},
                                 "c": [{"t": "#", "v": {"parts": [
                                     {"e": "f.body"}]}}]},
                            ]},
                        ]},
                    ]},
                    # ⚠️ THE EMPTY STATE'S SENTENCE DEPENDS ON `canWrite`,
                    # and that is not decoration. "No shoutouts yet" invites
                    # an action; on a finished year there is no action to
                    # take and the composer above it is gone. `feedEmptyLine`
                    # is computed in LOGIC for that reason.
                    {"t": "if", "e": "feedNone", "c": [
                        {"t": "div", "a": {"style": _SO_FEED_EMPTY},
                         "c": [{"t": "#", "v": {"parts": [
                             {"e": "feedEmptyLine"}]}}]},
                    ]},
                ]},
            ]},
        ]},
        "the shoutout composer and the feed, restored by Mide's ruling of "
        "3 Sep 2026 against Design's v3, which deleted both. See "
        "SHOUTOUT_SURFACE_RESTORED."),

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
    # ⚠️ APPENDED TO THE CLASS SCREEN'S ROOT AND NOT TO NODE 9, where
    # Design's own four overlays live. Node 9 is on all six pages; the class
    # screen's root is pruned everywhere but class-detail, which is the only
    # page with a feed. An inert overlay on five pages that can never open it
    # is markup a teacher can never reach, which is what LIVE_REGIONS had one
    # of removed for.
    #
    # ⊕ 3 Sep 2026 — RE-ANCHORED FROM `(81, None)` TO `(208, None)`, and
    # NOTHING ELSE CHANGED. 81 was v2's class-screen root and 208 is v3's;
    # this markup came out of `INSERT_AT` on 2 Sep when v3's deletion left it
    # hanging off a feed that was not on the page, was parked verbatim, and
    # is back verbatim. That parking is why the restoration cost one index.
    (208, None): ({
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

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK ══════════════════
    #
    # ⛔ THIS IS NOT A GAP BEING FILLED AND IT IS NOT DRIFT. Design's v3
    # contains no per-submission feedback UI of any kind — no comment
    # control, no sheet, and her only `<textarea>` in the file is the bulk
    # shoutout sheet's. Read `FEEDBACK_SURFACE_ADDED` at the top of this file
    # BEFORE removing any of this: the drawing is not the authority here,
    # Mide is, and the store it writes to is live on production.
    #
    # ⚠️ FOUR ENTRIES, ONE SURFACE. Two row controls (one per authoring
    # screen) and the sheet, twice, because `INSERT_AT` is keyed by parent
    # node and the two screens have different roots. All four come out of two
    # builders — `_fb_open_button` and `_fb_sheet` — so the two screens
    # cannot drift apart.
    #
    # ⚠️ WHERE EACH ROW CONTROL GOES, AND WHY IT IS NOT A NEW COLUMN. The
    # student screen's history table is a five-track CSS grid declared twice
    # (the header at 354 and the row at 361); a sixth cell would need both
    # track lists rewritten and would push a five-column table past 390px in
    # a place Design sized. So the control goes INSIDE the Status cell (366,
    # after her chip at 367), where there is vertical room and where "was
    # this marked, and did anyone say anything" reads as one column. On the
    # marking screen it goes inside her student cell (420, after the name at
    # 422), pushed right by `margin-left:auto` — the cell is already a flex
    # row and already has the space.
    (366, 367): (_fb_open_button("h", _FB_ROW_BTN),
                 "the feedback control on one row of the student screen's "
                 "submission history. Design drew no comment affordance "
                 "anywhere; this is Mide's ruling of 3 Sep 2026, and it is "
                 "inside her Status cell rather than in a sixth column "
                 "because her table's track list is declared twice and sized "
                 "for five."),
    (420, 422): (_fb_open_button("r", _FB_CELL_BTN, glyph=True),
                 "the same control on one row of the marking screen's "
                 "class-by-question grid — the second of Mide's two "
                 "authoring surfaces, the same builder, the same handler and "
                 "the same sheet. A GLYPH rather than words: Design's "
                 "student cell is a hard 225px track and a text button in it "
                 "cut every name that had a comment beside it. See "
                 "`_FB_CELL_BTN`."),
    (330, None): (_fb_sheet(),
                  "the feedback sheet, on the student screen. Design's "
                  "bulk-sheet chrome at her own measurements; this port has "
                  "one dialog idiom and this is it. Appended to the SCREEN "
                  "root rather than to node 9, so it is not markup on four "
                  "pages that can never open it."),
    (370, None): (_fb_sheet(),
                  "the same sheet on the marking screen. One builder, two "
                  "parents, because INSERT_AT is keyed by parent node."),
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
# ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3: 78→205, 79→206,
# 38→167, 71→198. And `class-detail.html` LOST BOTH OF ITS ROWS, which is a
# change in what the page does and not only in its numbering — see the note
# where they were.
WRAP = {
    "classes.html": {
        # The year strip's separator and its toggle. A school in its first
        # year has no other year to reach, and Design's unconditional button
        # would answer "there are none" — which is a control that exists to
        # tell you it should not.
        205: "hasOtherYears",
        206: "hasOtherYears",
        # The two import routes. `roster-import` is one of only three write
        # paths on the whole teacher surface, and importing children into a
        # class that finished in July is not an action worth offering.
        # Node 167 is the header action; node 198 is the same route from an
        # empty class card (the one node 194's pruning deliberately spared).
        167: "canWrite",
        198: "canWrite",
    },
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — `class-detail.html` HAD TWO ROWS HERE
    # AND HAS NONE. They were nodes 183 ("Send to several students") and 185
    # (the whole single-student composer), wrapped in `canWrite` so a PAST
    # academic year could not be written to. Design's v3 deleted both nodes.
    #
    # ⚠️ SO MRB-261'S READ-ONLY GUARANTEE HAD A HOLE ON THIS PAGE. The
    # shoutout write surface that survives v3 is the BULK OVERLAY, opened
    # from node 215 ("Shoutouts") and node 276 ("Send a shoutout"), and
    # NEITHER WAS WRAPPED. On a past year a teacher could still open the
    # sheet and press Send. The insert is refused further down —
    # `insertClassShoutout` writes against the class's own academic year and
    # the year is what the page is scoped by — so it was a control that LIED
    # rather than one that corrupted, which is the lesser of the two and
    # still not right.
    #
    # ⊕ CLOSED 2 Sep 2026 (MRB-306 Phase 2a screen 2). Both are wrapped on
    # `canWrite` below, and the two rows carry the same predicate as the four
    # on `classes.html` above.
    #
    # ⚠️ THIS IS NOT A RESTORATION OF THE DELETED COMPOSER AND MUST NOT BE
    # READ AS ONE. Whether v3's deletion of nodes 183/185 is accepted or
    # reversed was Mide's open call when this was written.
    # ⊕ 3 Sep 2026 — HE MADE IT: RESTORE. See `SHOUTOUT_SURFACE_RESTORED`.
    # These two rows are UNAFFECTED and stay exactly as they are — they gate
    # the two openers of Design's own BULK sheet, which v3 kept and which
    # were never part of the deletion. The restored composer carries its own
    # `canWrite` gate inside the inserted subtree, because `WRAP` is keyed by
    # Design's node indices and inserted markup has none. Three write
    # surfaces on this screen, one predicate.
    # This row changes nothing about WHICH
    # controls exist — it applies MRB-261's EXISTING read-only rule to the
    # two openers that survived, exactly as that rule already applies to
    # every other write path on the teacher surface. A past year offers no
    # write controls; these were write controls; they were missed because
    # the nodes they used to hang off were deleted underneath the ruling.
    #
    # ⚠️ WHAT DRIVING SHOWED, and why this was not merely theoretical: on
    # `class-detail-empty-fixture.html` — which IS the past-year read-only
    # shape, `canWrite: false`, `readOnlyLine: "2025–26 is read-only"` — the
    # rendered page carried a live "Shoutouts" button in its header. The
    # docstring of `teacher_behaviour.py` asserted the opposite ("the
    # shoutout composer and the bulk opener absent"); that sentence was
    # written against v2 and had silently stopped being true. It is
    # corrected there in the same change.
    "class-detail.html": {
        215: "canWrite",
        276: "canWrite",
    },
    # ── ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 5) ────────────────────────
    #
    # ⛔ THE CLASS-BY-QUESTION SECTION DRAWS ITS CHROME WHETHER OR NOT IT HAS
    # A GRID. With no grid — the key-absent state this screen must survive,
    # reachable whenever a class's papers are all still open — node 401 still
    # renders the heading and the whole four-key legend, and node 410 still
    # renders the card with its STUDENT / MARK header strip, over nothing.
    # Seen on `assignment-gridmissing-fixture.html`: a legend explaining four
    # glyphs none of which are on the page, above an empty box.
    #
    # ⚠️ THE HEADING GOES WITH IT, WHICH IS THE POINT. Leaving "Class by
    # question" up over a hidden table is the same claim the empty table
    # makes. The Question-breakdown card above keeps ITS heading because the
    # `INSERT_AT` note lands inside it and answers for it; this section has
    # no such note and would be a heading with nothing underneath.
    "assignment.html": {
        401: "paper.hasQuestions",
        410: "paper.hasQuestions",
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
#
# ⊕ 31 Aug 2026 (MRB-304) — THE FIELD IS `pages` AND IT IS ALWAYS A TUPLE. It
# used to be `page`, one filename, because every addition so far lived on one
# screen. The "My classes" link is CHROME in the strictest sense: Mide's
# instruction is that the header presents the same affordances on every
# teacher page, so it is on all six.
#
# ⚠️ THE PLURAL IS THE POINT, AND SO IS THE UNIFORM SHAPE. Naming one page and
# letting the other five carry it anyway would have tripped the build's own
# absent-elsewhere check — and softening THAT check to let it through would
# have retired the register's best property, which is that an addition cannot
# drift onto a screen it was never ruled onto. Both halves still hold exactly
# as written: present on every page it names, absent on every page it does
# not. A single-page addition is a one-tuple, so there is no second shape for
# a reader — or a consumer — to remember.
AMENDED_ADDITIONS = (
    # ⊕ RULED, MRB-304 — the top bar's way back to the class list.
    #
    # ⚠️ `needs_data` IS DELIBERATELY NOT SET. This is chrome in the strictest
    # sense: it is in the sticky top bar, on all six screens, in every state
    # including the empty ones. The warning above applies exactly — a chrome
    # control that claimed `needs_data` would be excusing itself from the only
    # gate that presses it.
    #
    # ⚠️ NO `opener_tpl`. Nothing reveals it, because nothing hides it; the
    # reveal loop is for controls behind a sheet or a toggle, and this one is
    # on screen the moment the page mounts.
    #
    # `expect_nav` names the destination and NOT a parameter. `goClasses`
    # carries `year: MRB_DATA('yearParam')`, and `yearParam` is EMPTY on the
    # working year by design — `MRB_GO` drops an empty param so the ordinary
    # URL stays byte-identical — so demanding a value there would fail on
    # every fixture that is in the year it is supposed to be in.
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — the `nav-classes` row was here and is
    # RETIRED: Design's v3 top bar draws the control itself, as the "My
    # classes" tab of her own `navTabs` strip, so the port no longer adds one.
    # The full reasoning is at the retired `INSERT_AT[(10, 13)]` entry. This
    # register names markup the port ADDS; a control Design drew is asserted
    # by `NAV`/`LOGIC` instead, which is where the rewired tab is asserted.
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — re-anchored on v3: 76→203, 79→206.
    dict(marker="year-open", pages=("classes.html",), node=203, opener_tpl=206,
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
    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · THE SHOUTOUT SURFACE, REGISTERED ══
    #
    # ⊕ 3 Sep 2026 — THESE ROWS REPLACE A RETIRAL. From 2 Sep to 3 Sep this
    # spot held a comment recording that the four `shoutout-delete` rows had
    # been retired because Design's v3 deleted the feed they hung off, and
    # that Mide's 24 Aug ruling was "a product regression, not a numbering
    # change". He has now ruled: the surface comes back. The four delete rows
    # are below, unchanged, and four composer rows are new. See
    # `SHOUTOUT_SURFACE_RESTORED`.
    #
    # ── ⊕ `needs_write`, AND WHY IT IS NOT `needs_data` ─────────────────
    #
    # ⚑ A NEW FLAG, BECAUSE THE EXISTING ONE WOULD HAVE BEEN A LIE THAT
    # PASSED. `needs_data` means "there is legitimately nothing to press on
    # an empty fixture", and `teacher_behaviour` SKIPS such a row there. The
    # composer is not absent for want of data — it is absent because MRB-261
    # makes a finished academic year READ-ONLY, and it is absent on a
    # populated past-year class exactly as much as on an empty one.
    #
    # ⚠️ AND THE DIFFERENCE IS THAT `needs_write` ASSERTS. A skip proves
    # nothing; `teacher_behaviour` requires a `needs_write` marker to be
    # PRESENT and pressable wherever `canWrite` is true, and to be ABSENT
    # from the DOM wherever it is false — by name, on both passes. That is
    # the guarantee this gate previously only DESCRIBED, and its own
    # docstring records what describing it cost: v3 deleted the two wrapped
    # nodes, the read-only rule quietly stopped holding on this screen, and
    # every gate stayed green until somebody opened the page and read it.
    #
    # ⚠️ `shoutout-delete` CARRIES BOTH FLAGS, and needs both. It hangs off a
    # feed row (so there is nothing to press on an empty feed) AND it is a
    # write (so it must be gone on a finished year). `f.canDelete` is
    # literally the conjunction — see the `feed:` entry in LOGIC.
    #
    # ⛔ AND THEY CARRY NO `opener_tpl` EITHER. That field names one of
    # DESIGN'S nodes by template index, and `teacher_behaviour` presses it
    # with `[data-dc-tpl="<index>"]`. Nothing of Design's reveals this sheet —
    # the thing that opens it is `shoutout-delete`, which is an ADDITION, and
    # the probe's reveal loop already presses earlier additions in register
    # order until the wanted control appears. Naming a marker in a field that
    # takes an index would query a selector that matches nothing, fall
    # through to the loop that was going to work anyway, and read like
    # coverage.
    #
    # ⛔ THE CONFIRM SHEET'S THREE BUTTONS DELIBERATELY DO NOT CARRY
    # `needs_write`. They live inside `if delOpen`, which is false at rest on
    # every fixture in the set, so an absence assertion on them would pass
    # everywhere and prove nothing — a green check that measures nothing is
    # worse than no check, because it reads like coverage. They keep
    # `needs_data` and `opener_tpl`, which is the mechanism that actually
    # reveals and presses them.
    dict(marker="shoutout-recipient", pages=("class-detail.html",),
         node=306, needs_write=True,
         label="Send a shoutout to",
         why="the composer's recipient select. Design's v3 deleted the "
             "single-student composer outright and Mide ruled it back on "
             "3 Sep 2026; the OPTION carries the roster row's real id "
             "because `insertClassShoutout` stores `recipient_id` and two "
             "children in one class can share a name."),
    dict(marker="shoutout-template", pages=("class-detail.html",),
         node=306, needs_write=True,
         label="<one of the six templates>",
         why="the six template quick-picks, read from the locked enum in "
             "shared/shoutouts.js that mirrors the DB CHECK "
             "`class_shoutouts_template_key_chk`. Never retyped here: a "
             "seventh key or a stale one would gate green and fail on "
             "insert."),
    dict(marker="shoutout-note", pages=("class-detail.html",),
         node=306, needs_write=True,
         label="Something specific you want to recognise",
         why="the free-text field. Mide's ruling of 1 Sep 2026 is that a "
             "teacher may write their own words alongside the templates, and "
             "that ruling POSTDATES Design's deletion of this control, which "
             "is what makes the restoration a divergence-by-ruling. Capped "
             "at 500 characters, which is the database's own "
             "`class_shoutouts_message_length_chk`."),
    dict(marker="shoutout-send", pages=("class-detail.html",),
         node=306, needs_write=True,
         label="Send shoutout",
         why="the send. `sendShoutout` reaches `MRB_SEND_SHOUTOUTS` and a "
             "real INSERT; Design's own handler was a toast in front of no "
             "write at all."),
    dict(marker="shoutout-delete", pages=("class-detail.html",),
         node=306, needs_data=True, needs_write=True,
         label="Remove",
         why="the delete control on a shoutout the signed-in teacher wrote. "
             "Design drew no delete affordance anywhere in the feed; this is "
             "Mide's instruction of 24 Aug 2026. The treatment is Design's "
             "own low-emphasis text button, copied verbatim off the \"Back "
             "to <class>\" control."),
    dict(marker="shoutout-delete-close", pages=("class-detail.html",),
         node=208, needs_data=True,
         label="Keep the shoutout",
         why="the confirm sheet's close X. The sheet is Design's bulk-sheet "
             "chrome at her own measurements; the confirm itself is the "
             "control, because a one-press delete eight pixels from a "
             "child's name is the shape of an accident."),
    dict(marker="shoutout-delete-cancel", pages=("class-detail.html",),
         node=208, needs_data=True,
         label="Keep it",
         why="the confirm sheet's cancel. It clears `delId` and writes "
             "nothing."),
    dict(marker="shoutout-delete-confirm", pages=("class-detail.html",),
         node=208, needs_data=True,
         label="Remove shoutout",
         why="the confirm sheet's primary. It reaches "
             "`softDeleteClassShoutout`, which sets `deleted_at` and forces "
             "RETURNING so an RLS refusal cannot come back looking like a "
             "success."),

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK, REGISTERED ══════
    #
    # See `FEEDBACK_SURFACE_ADDED`. Design drew NONE of this — not a comment
    # control, not a sheet, not a textarea outside her bulk sheet — so every
    # row here is an addition against her delivery and this register is what
    # makes the build assert them against the emitted bytes.
    #
    # ⚠️ ORDER MATTERS AND IT IS NOT COSMETIC. `feedback-open` is registered
    # FIRST because it is what reveals the other three: the probe's reveal
    # loop presses earlier additions in REGISTER ORDER until the control it
    # wants appears, and the sheet is `<if fbOpen>` — nothing of Design's
    # opens it, so `opener_tpl` (which takes one of DESIGN's node indices)
    # has nothing to name.
    #
    # ⚠️ `needs_write` IS ON THE OPENER AND ON NEITHER OF THE WRITES, which
    # looks backwards and is not. The flag asserts a marker is PRESENT where
    # `canWrite` is true and ABSENT where it is false, at rest. The three
    # controls inside the sheet are inside `<if fbOpen>`, which is false at
    # rest on every fixture in the set, so an absence assertion on them would
    # pass everywhere and measure nothing — the same reasoning the shoutout
    # confirm sheet's three buttons carry. And the OPENER is not a write
    # either: MRB-261 makes a past year read-only, not unreadable, and a
    # teacher may still open a comment written last year. So it carries
    # `needs_data` alone, and the read-only behaviour of the WRITE halves is
    # asserted by `fbCanEdit`/`fbCanRemove` reading `MRB_DATA('canWrite')`
    # and by the drive in the report, which is where a state behind an `if`
    # can honestly be measured.
    dict(marker="feedback-open",
         pages=("student-detail.html", "assignment.html"),
         node=330, needs_data=True,
         label="Add feedback / Edit feedback / Read feedback",
         why="the control that opens the feedback sheet, on a submission "
             "history row and on a marking grid row. Two surfaces, ONE "
             "builder (`_fb_open_button`), because Mide's brief asks for "
             "both and a second implementation is how they come to "
             "disagree. Absent on a row with no submission: "
             "`submission_feedback.submission_id` is NOT NULL and there is "
             "nothing to attach a comment to."),
    dict(marker="feedback-close",
         pages=("student-detail.html", "assignment.html"),
         node=330, needs_data=True,
         label="Close without saving",
         why="the sheet's close X, in Design's own bulk-sheet chrome. It "
             "writes nothing and clears the draft."),
    dict(marker="feedback-body",
         pages=("student-detail.html", "assignment.html"),
         node=330, needs_data=True,
         label="What they did well, and the one thing to work on next",
         why="the comment itself. Capped at 2000, which is "
             "`submission_feedback_body_length_chk` — not 500, which is "
             "class_shoutouts. The existing text is the textarea's CHILD "
             "rather than a `value` attribute, because a textarea's content "
             "IS its value and `value=` on one does nothing."),
    dict(marker="feedback-save",
         pages=("student-detail.html", "assignment.html"),
         node=330, needs_data=True,
         label="Save feedback / Save changes",
         why="the write. INSERT where there is nothing yet, UPDATE where "
             "there is — and the UPDATE carries `prior_body`, because the "
             "database refuses an edit that does not keep the wording it "
             "replaced."),
    dict(marker="feedback-remove",
         pages=("student-detail.html", "assignment.html"),
         node=330, needs_data=True,
         label="Remove",
         why="the soft delete, behind a second press that says what it will "
             "do. Drawn only on a comment the signed-in teacher wrote, "
             "because `submission_feedback_update` is `teacher_id = "
             "auth.uid()` and offering it elsewhere would be offering a "
             "refusal."),
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
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — AND THIS ONE WAS THROWING AT MOUNT.
    # `TODAY_LESSONS` is four invented lessons — four class ids, four period
    # numbers, four times and two room names — new in v3 and reached by TWO
    # readers, `const lessons` and `const lessonToday`, BOTH unconditional in
    # `renderVals`. `lessons` opens `this.klassById(t.classId)` and then
    # `c.state`, and on a real class list `klassById('8hsc2')` is undefined:
    # a TypeError at mount, on every one of the six pages, whatever screen
    # they draw. It survived because the Today screen is not emitted and
    # nobody looked at a page that crashes before it paints.
    #
    # ⚠️ THE FABRICATION MATTERS AS MUCH AS THE CRASH. `klass.meta` printed
    # "Next lesson today · P5 · 13:55 · Lab 2" for a real class, and there is
    # no timetable data behind any of those four values. Real timetable data
    # is the Today/Timetable unit's job; this row only stops the invention
    # and the throw. See the two `LOGIC` entries that degrade its readers.
    ("TODAY_LESSONS", "four invented lessons — fake class ids, periods, "
                      "times and room names, new in v3. Both its readers "
                      "run on every page, and the first one throws on any "
                      "real class list."),
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

    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — A SEEDED DATE, NEW IN v3.
    # `todayLine: 'Monday 31 August · Autumn term · 2026–27'` — a literal
    # weekday, a literal date, a literal term and a literal academic year,
    # all four wrong for every school on every day but one. It is read by
    # exactly one node (36, on the Today screen), which `SCREENS` prunes on
    # all six pages, so it renders nowhere — but it SHIPS in the logic of all
    # six, and `teacher_tells` refuses it there, correctly: a sample string in
    # the bytes is one failed guard away from a sample string on the page.
    #
    # Dropped rather than bound, for the reason the Set-work keys above were:
    # binding it needs a `MRB_DATA` key, and inventing one that
    # `teacher-live.js` does not supply is a thrown error at mount. When the
    # Today screen is ported it gets a real date from the seam, in the seam.
    "todayLine",

    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — THE TIMETABLE WIZARD, WHOLE.
    #
    # `ttRows` is the one that matters and the other nine go with it. It is
    # seven invented timetable slots — a weekday and period, a clock time, a
    # source string off an imaginary MIS export, and a match status — WRAPPED
    # AROUND REAL CLASS CODES. `8h/Sc2`, `7r/Sc3`, `9h/Sc5`, `10h/Ph1`,
    # `8r/Sc1` and `11h/Sc5` are this school's actual 2026-27 classes; the
    # days, the times and the rooms beside them are Design's fiction. That
    # mixture is worse than a wholly invented row, because the half a reader
    # can check is true.
    #
    # ⚠️ IT IS DROPPED, NOT SEAMED, AND THAT IS THE SAME CALL `TODAY_LESSONS`
    # GOT. There is no timetable data anywhere in this product — no table, no
    # RPC, nothing on `teacher-live.js` to bind to — so a seam would need a
    # `MRB_DATA` key nobody supplies, which is a throw at mount rather than a
    # blank row. Real timetable data is the Today/Timetable unit's job.
    #
    # The other nine exist only to drive the wizard `SCREENS` prunes:
    #
    #   · `ttSteps`, `tt1`, `tt2`, `tt3` — the three-step chrome. Read by
    #     nodes 104/109/116/141, every one of them inside node 96.
    #   · `ttNext`, `ttBack` — nodes 114/140 and 139/155, also inside 96.
    #   · `ttDone` — node 156, inside 96. It also `ping`s "Timetable linked —
    #     Today now shows your lessons", which is not true of anything.
    #   · `ttSample` — node 115, inside 96, and it is `sampleCsv` again
    #     verbatim: `this.ping('Timetable template downloaded')` in front of
    #     no Blob, no anchor and no download. Dropped for the reason
    #     `sampleCsv` was.
    #   · `goTimetable` — CHECKED BY READING, because the top bar was rewired
    #     by the week-bar unit and a live control must not lose its handler.
    #     Its only two readers are nodes 42 and 49, and BOTH are inside node
    #     32, the Today screen, which `SCREENS` prunes on all six pages.
    #     `navTabs` does NOT reach it: Design's own strip is two tabs,
    #     `today` and `classes`, and the port's rewire dispatches both through
    #     `MRB_GO(t.id, …)`. There is no third tab and never was.
    #
    # ⚠️ `ttStep` IS NOT ON THIS LIST — see the state initialiser in `LOGIC`,
    # where the reason it stays is written down and was corrected by this
    # unit rather than left standing.
    "ttSteps", "tt1", "tt2", "tt3", "ttRows",
    "ttNext", "ttBack", "ttDone", "ttSample", "goTimetable",
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
        "    var m = MRB_DATA('GRID');\n"
        "    var key = k.id + ':' + pIdx;\n"
        "    return (m && (key in m)) ? (m[key] || null) : null;",
        "the per-paper question grid, from what each student actually "
        "answered rather than from a hash of their total. ⚠️ IT CAN BE NULL, "
        "DELIBERATELY: `teacher-live.js` prefetches only the grids a screen "
        "will draw, and a key that is present and null means NOT FETCHED "
        "YET. Design's `renderVals` already writes `pGrid ? … : []` "
        "everywhere it reads it, so a null renders an empty grid rather than "
        "a grid of zeros — which is the one thing it must never be.\n"
        "\n"
        "        ⊕ MRB-287 — AND A MISSING KEY IS THE SAME ANSWER, NOT A "
        "THROW. The first body read `MRB_PICK('GRID', key)`, which throws on "
        "an absent key — but an absent key IS the not-fetched-yet state this "
        "comment already promised to survive: `renderVals` computes the "
        "marking screen's `paper` block on EVERY screen, so opening "
        "class-detail on any class with an assignment asked for a grid only "
        "`assignment.html` prefetches, threw mid-mount, and landed on the "
        "generic error card. The one class a teacher had set work on was the "
        "one class that could not be opened — live, 26 Aug 2026. "
        "`MRB_DATA('GRID')` still throws when the payload carries no GRID "
        "map at all, so a page fed nothing stays loud; only the per-key miss "
        "is the documented null."),
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
        "'var(--st-caption)', bd: '1.5px solid var(--st-caption)' };\n"
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
        "grid keeps its rhythm, and 2px corners rather than 50% so it differs "
        "in SHAPE and not only in colour. Distinguishable without colour, "
        "which the ring/dot pair already is not.\n"
        "\n"
        "        ⊕ RECOLOURED 2 Sep 2026 — `--st-hatch-b` → `--st-caption`. "
        "The first draft picked `--st-hatch-b` and called it "
        "present-but-neutral. It is #B33E1C, declared inside the ACCENT block "
        "of the token sheet between `--st-accent` and `--st-accent-text`, and "
        "on this page that hue means Reteach, late, chase, flagged. Driven "
        "and looked at, one child's eight self-marked answers rendered as a "
        "row of rust squares that reads louder than the ring that actually "
        "means wrong — the exact misreport the state was invented to "
        "prevent, in a different direction. `--st-caption` (#7A6E5F) is the "
        "legend's own neutral ink and is far darker than the dash's "
        "`--st-rule-strong`, so present and unscored is what it says."),
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
    # ⊕ RE-ANCHORED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306). The `frm` was a
    # photograph of v2's seven lines and v3 redrew five of them — `screen`
    # opens on 'today', `weekIdx` is gone, `ttStep`, `insFrom` and
    # `digestFrom` are new. The ruling is not about any of that: it is about
    # WHICH INITIALISER, and there is exactly one `state = {` in the class.
    #
    # ⚠️ THIS IS A MERGE AND NOT A REPLACEMENT, which is the whole care in
    # it. Three kinds of key meet in this object and each is kept for its own
    # reason:
    #
    #   · v3's own keys the port still needs — `insFrom` and `digestFrom`
    #     are the "came from" crumbs. Dropping a key Design's render reads
    #     is a silent `undefined` on screen, never an error.
    #     ⊕ CORRECTED 2 Sep 2026 (MRB-306 Phase 1c). This bullet used to
    #     read "`ttStep` drives the timetable wizard's three steps", and
    #     that sentence stopped being true in the same run that wrote it:
    #     `DROP_KEYS` now takes the whole wizard — `ttSteps`, `tt1`-`tt3`,
    #     `ttRows`, `ttNext`, `ttBack`, `ttDone`, `ttSample`,
    #     `goTimetable` — because `ttRows` is invented timetable data and
    #     the rest only served the screen `SCREENS` prunes. `ttStep: 1`
    #     therefore has NO reader left in the shipped logic.
    #     It stays anyway, on `weekIdx`'s reasoning below: a state key
    #     ahead of its readers is inert, a reader ahead of its state key is
    #     not, and the Timetable screen is a named later unit that will
    #     want the cursor back. It is also not a tell — the value is the
    #     integer 1, not a fact about anybody's school. Left as a comment
    #     that says so rather than a comment that lies.
    #   · the ported keys, all of them — MRB_SCREEN, the three MRB_DATA
    #     reads, MRB_FIRST_TEMPLATE for `boTpl`, `digestScope`/`chartScope`
    #     off the URL via MRB_Q, and `yearsOpen`.
    #   · ⊕ 3 Sep 2026 (Phase 2b) — `boNote` and the six `fb*` keys.
    #     `boNote` is the BULK SHEET's own message, separate from the
    #     composer's `note` (see `RETARGET_ON[651]` for the three readers
    #     that made sharing one key unsafe). The `fb*` six are the feedback
    #     sheet's whole state: which submission is open, the child's name and
    #     the paper's title as they were when it opened, the text being
    #     typed, the validation line, and whether Remove has been pressed
    #     once. Nothing about a person is in any of them beyond what is
    #     already on the screen that opened the sheet.
    #   · `weekIdx: 0`, RESTORED. v3 deleted it with the week rail; Mide
    #     ruled the week bar back in on 1 Sep 2026, so the state key belongs
    #     here even though the rail's own markup lands in a later unit. A
    #     state key that arrives before its readers is inert; a reader that
    #     arrives before its state key reads `undefined` and indexes an
    #     array with it.
    #
    # The Set-work keys (`swStep`, `swTopic`, `swQ`, `swDay`, `swRel`,
    # `swClasses`) stay dropped: Set work is not shipped, and #52 deletes the
    # three locals that read them.
    (dict(key="state = {"),
     """  state = {
    screen: 'MRB_SCREEN',
    classId: MRB_DATA('classId'), studentId: MRB_DATA('studentId'),
    paperIdx: MRB_DATA('paperIdx'), weekIdx: 0,
    ks: 'All', sort: 'code', modal: null, toast: '',
    boSel: [], boTpl: MRB_FIRST_TEMPLATE(), note: '', boNote: '',
    search: '',
    fbSub: null, fbName: '', fbPaper: '', fbBody: '', fbErr: '',
    fbConfirm: false,
    importStep: 1, ttStep: 1,
    digestScope: MRB_Q('class') ? 'class' : 'all', recipient: '',
    chartKind: 'submissions', chartScope: MRB_Q('class') || 'all',
    insFrom: 'today', digestFrom: 'today',
    yearsOpen: false
  };""",
     "the state initialiser. See the block comment above. "
     "⊕ 1 Sep 2026 (MRB-306) — moved off a verbatim `frm` onto "
     "`key=\"state = {\"`, because v3 redrew five of the seven lines the "
     "`frm` had photographed without touching what the ruling is about. "
     "Merged rather than replaced: v3's `ttStep`, `insFrom` and `digestFrom` "
     "are kept, and `weekIdx: 0` is RESTORED under Mide's 1 Sep week-bar "
     "ruling — the rail's markup follows in a later unit, and a state key "
     "that arrives early is inert where a reader that arrives early is not."),

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

    # ⊕ MRB-287, 26 Aug 2026 — the environment badge's key, INTO THE RENDER
    # SCOPE. The INSERT_AT chip at nav node 10 hangs on `if envBadge`, and an
    # `if` resolves through `renderVals` — not through `__MRB_BIND__`, which
    # is where v1's badge got its text. A key the scope does not name never
    # fires and never errors (the student pages' documented seam trap), which
    # is exactly what the first local drive showed: chip in the template,
    # nothing on screen.
    ("      isClasses: s.screen === 'classes',",
     "      envBadge: MRB_DATA('envBadge'),\n"
     "      isClasses: s.screen === 'classes',",
     "the environment badge, exposed where the inserted `if` can see it. "
     "Empty on live production, so the chip renders only where the warning "
     "means something."),

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
    # ⊕ RE-ANCHORED FOR DESIGN'S v2, 26 Aug 2026. v1 drew the meta as
    # `'Year ' + c.year + ' · ' + c.ks + ' · 2026–27'`; v2 redraws it as the
    # student count alone (`c.n ? c.n + ' students' : 'No students yet'`) and
    # states the year group nowhere but the class code itself. The count is
    # Design's v2 presentation and stays; the academic year is Mide's E1
    # ruling and stays too — appended, dropped when the school has not named
    # the year. Year group and key stage do NOT come back: they were v1's
    # drawing, not part of the ruling, and v2's KS filter tabs already answer
    # the key-stage question.
    # ⊕ RE-ANCHORED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306). v3 appends the
    # subject: `(c.n ? … ) + ' · ' + c.subject`. That is Design's drawing and
    # it stays; the academic year is Mide's E1 ruling and it stays too. The
    # anchor names the card builder and the key, so the next time Design
    # appends something to this line the ruling still finds it.
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a) — YEAR GROUP AND KEY STAGE COME BACK,
    # AND THIS REVERSES THE 26 AUG NOTE DIRECTLY ABOVE. That note said "Year
    # group and key stage do NOT come back: they were v1's drawing, not part
    # of the ruling, and v2's KS filter tabs already answer the key-stage
    # question." It is kept above rather than deleted because it is the
    # reasoning a future reader would otherwise re-derive — but it was a
    # PORTER'S reading of what the ruling required, not one of Mide's, and
    # Mide's Phase 2a brief names the card's contents explicitly: "class
    # code, year + key stage, submissions this week, last activity".
    #
    # "Year" there is the YEAR GROUP, not the academic year: the brief pairs
    # it with key stage, lists the academic year separately as ruling 3, and
    # the pair it asks for is v1's own drawing (`'Year ' + c.year + ' · ' +
    # c.ks`) minus the welded literal E1 replaced.
    #
    # ⚠️ AND THE FILTER TABS ARE NOT AN ANSWER TO IT. "All" is the tab a
    # teacher lands on and the one they stay on, so on the default view the
    # tabs say nothing about any individual card.
    #
    # Design's own pair — the student count and the subject — keeps its
    # order and its adjacency; the year group and key stage are prepended and
    # the academic year still trails. Every part is still dropped rather than
    # printed when it is missing: `year_group` and `key_stage` are both
    # nullable, and "Year null · undefined" is worse than a shorter line.
    #
    # ⚠️ THE LINE NO LONGER FITS ON ONE ROW AND MUST NOT TRY TO. It did not
    # fit BEFORE this change either — measured 2 Sep at a 1280px viewport,
    # `11r/Sc1`'s meta ran from x=870 to x=1293 and was clipped at the
    # window edge, because Design's node 182 carries `white-space:nowrap`
    # and nothing else. See the `182` row in `BIND_ATTR`, which is the other
    # half of this ruling: without it, restoring the pair makes a
    # pre-existing clip worse on every card.
    #
    # ⚠️ THE SEPARATOR IS GLUED TO THE PART BEFORE IT — ` · `,
    # a NO-BREAK SPACE then the middot then an ordinary space. Design joins
    # on ` · `, which on a line that never wrapped was the same thing. Now
    # that it wraps, an ordinary space on BOTH sides of the middot lets the
    # break land in front of it, and a line then OPENS with "· 2026–27" —
    # which on a wall of sixty-nine cards reads as a bullet rather than as a
    # separator. Gluing it backwards means every wrapped line ENDS with the
    # middot, which is the convention a reader already knows. The parts
    # themselves keep ordinary spaces, so "Combined Science" and "28
    # students" can still break internally on a narrow card.
    (dict(builder="cards", key="meta"),
     "      meta: [c.year ? 'Year ' + c.year : '', c.ks,\n"
     "        c.n ? c.n + ' students' : 'No students yet',\n"
     "        c.subject, c.yearName].filter(Boolean).join('\\u00A0\\u00B7 '),",
     "the class card's meta line — v2's student count, plus the card's OWN "
     "academic year (Mide's E1 ruling), not the dashboard's. "
     "⊕ 1 Sep 2026 (MRB-306) — moved off `frm` onto "
     "`builder=\"cards\", key=\"meta\"`, and v3's `c.subject` is folded into "
     "the same `.filter(Boolean)` list rather than concatenated, so an "
     "unnamed academic year drops out instead of printing a bare separator. "
     "⊕ 2 Sep 2026 (MRB-306 Phase 2a) — year group and key stage restored "
     "to the front of the same list, per Mide's Phase 2a brief; both are "
     "nullable and both drop rather than print."),

    # ══ "LAST ACTIVITY NO ACTIVITY YET" ═════════════════════════════════
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a). Design wrote the card's activity
    # line as
    #
    #     activity: c.state === 'empty' ? c.last : 'Last activity ' + c.last,
    #
    # which prefixes the string for every class that HAS a roster. But
    # `c.last` is not a date — it is `relativeTime(lastIso)` OR the words
    # "No activity yet", and `teacher-live.js` produces the words whenever
    # `lastIso` is null. `lastIso` is the newest submission across the
    # roster, so it is null for:
    #
    #   · a class with students and no work set (`state: 'nowork'` — no
    #     papers means no matrix columns means no submission stamps), and
    #   · a class with students and work set that nobody has handed in yet
    #     (`state: 'live'`).
    #
    # Both render "Last activity No activity yet". Design's own sample can
    # never show it — her `nowork` class carries an invented "2 days ago",
    # which is a shape the seam cannot produce — so it was invisible to
    # every gate.
    #
    # ⚠️ IT IS THE COMMON CASE ON THE REAL YEAR, NOT AN EDGE. Measured on
    # prod for 2026-27: 69 classes, 3 with any members, 1 with any
    # assignments. That is 66 `empty` (correct today, via the branch below),
    # 2 `nowork` and 1 `live` — i.e. all three classes a teacher can
    # actually do anything with read as broken English.
    #
    # The branch was conditioned on the wrong thing. Whether to prefix is a
    # question about the ACTIVITY, not about the class's state, so it is
    # asked of the activity. Empty classes are unaffected: they have no
    # roster, so `c.last` is the same string and the same branch is taken.
    (dict(builder="cards", key="activity"),
     "      activity: c.last === 'No activity yet'\n"
     "        ? c.last\n"
     "        : 'Last activity ' + c.last,",
     "the class card's last-activity line — the prefix is conditioned on "
     "whether there IS any activity, not on `state === 'empty'`. A class "
     "with a roster and no submissions read \"Last activity No activity "
     "yet\"; on the working year that is every class with members."),

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
    # ⊕ RE-EXPRESSED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306), AND SCOPED TO
    # THE SELECTED WEEK. v3 deleted the whole span this ruling was written
    # against — no `scPct`, no `pct`, no `weekLabel`, and no `sc`/`late`
    # locals at all — and redrew the row as a BINARY `week`/`weekFg`/`dot`
    # triple over `r.inWeek`, which is "did this child hand in THIS week's
    # work" and nothing else.
    #
    # All three defects above survive v3 in a shorter sentence. `'In · on
    # time'` is written over `r.inWeek`, which still means SUBMITTED and
    # still says nothing about lateness, so v3 states a punctuality it has
    # not measured for every child who handed anything in — the third defect,
    # word for word. The `/8` and the two-state `late` are gone from this row
    # only because the row no longer shows a score.
    #
    # ⚑ AND UNDER MIDE'S WEEK BAR THE COLUMN IS NOT "THIS WEEK" ANY MORE. It
    # is the week the teacher has picked, so it reads the SELECTED week's
    # papers out of the matrix rather than the seam's `inWeek` flag, which is
    # hard-wired to the current week window. `wTally` — built beside the week
    # scope, see the tiles ruling — is that count per child.
    #
    # ⚠️ A WEEK NOBODY WAS ASKED ANYTHING IN IS NOT "NOT IN YET". It is
    # "Nothing set", and it has to be, because "Not in yet" beside a child's
    # name in a week their teacher set no work is an accusation the data does
    # not support. That state is unreachable in Design's sample and reachable
    # on nearly every real class.
    (dict(builder="roster", key="week"),
     """      week: !kPapers.length ? '—'
        : (!wTally[r.id].asked ? 'Nothing set'
          : (!wTally[r.id].in ? 'Not in yet'
            : (wTally[r.id].in < wTally[r.id].asked
              ? wTally[r.id].in + ' of ' + wTally[r.id].asked + ' in'
              : (wTally[r.id].late === true ? 'In · late'
                : (wTally[r.id].late === false ? 'In · on time'
                  : 'In · timing unknown'))))),""",
     "the roster row. See the block comment: Design's binary column states a "
     "punctuality it never measured, and under Mide's week bar the column is "
     "the SELECTED week rather than this one. The `id` this row also needs — "
     "the shoutout composer's `<select>` writes `recipient_id` — is its own "
     "entry at the end of this tuple, because a property anchor replaces one "
     "property and `id` is a different one."),

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
    # ⊕ RE-ANCHORED AND SPLIT FOR DESIGN'S v3, 1 Sep 2026 (MRB-306).
    #
    # ⚠️ THE LATENESS HALF OF THIS AREA IS NOT v3's, AND IT IS EASY TO READ IT
    # THAT WAY. The built page carries `lateState`, a three-way tone and a
    # "timing unknown" status, and every one of those is THIS PORT'S — rulings
    # #41, #42, #43 and #45, which all still apply cleanly. Design's v3 file
    # still reads `const late = !open && sc != null && stRow.late[i];` and
    # still writes "On time" over an unknown. Nothing was fixed upstream.
    #
    # What v3 ACTUALLY changed here is one character class: v2 wrote
    # `late: late,` and `pct: open ? null : pct,` on two lines, v3 writes the
    # shorthand `late, pct: open ? null : pct,` on one. That is the entire
    # reason a ten-line `frm` stopped matching, and it is the argument for
    # anchors in a sentence — nine of those ten lines were dragged along only
    # to reach `submitted:` and `score:` at the bottom.
    #
    # So the ruling is now THREE anchors on the three nodes it actually
    # corrects. The other two are at the END of LOGIC rather than here,
    # deliberately: entries are addressed by index in the week-rail unit that
    # follows this one, and inserting two here would silently renumber #13
    # and #36 out from under it. Search `MRB-306 — #11, parts 2 and 3`.
    (dict(builder="stHistory", key="const pct"),
     """      const pct = stRow ? stRow.pct[i] : null;
      const stampS = stRow ? stRow.stampShort[i] : null;""",
     "the student's assignment history. `/ 8` twice and a fabricated date; "
     "see the block comment above. "
     "⊕ 1 Sep 2026 (MRB-306) — SPLIT INTO THREE, and this entry is the "
     "first: the score percentage off `stRow.pct[i]`, and `stampShort` "
     "captured for the date. Moved off a ten-line `frm` onto "
     "`builder=\"stHistory\", key=\"const pct\"`. v3 shortened `late: late,` "
     "to the `late,` shorthand one line below, and that alone killed the "
     "span; the `/ 8` and the fabricated date were never touched. The "
     "`submitted` and `score` halves are two further anchored entries at the "
     "end of LOGIC."),

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
    #
    # ── ⊕ RE-EXPRESSED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306) ─────────────
    #
    # ⛔ THERE ARE NO TILES IN v3. `klass` carries `code`, `meta`, `statLine`,
    # `rosterLine`, `hasWork`, `noWork`, `noWorkLine` and `paperLine`, and
    # nothing else; the four-tile grid is replaced by a `glance` block —
    # this week's assignment with a chase list, the last marked set with its
    # two weakest questions, and a watch list. The brief for this run said
    # this ruling needed one `String(flagged)` corrected. It needed the whole
    # ruling re-read: there is no `String(flagged)` because there is no tile
    # to print it in.
    #
    # ⚑ EVERY DEFECT ABOVE MOVED WITH THE COMPONENT. `glance.openIn` is
    # `kMx.colSub[0] + ' of ' + k.n + ' in'` — the roster denominator, on the
    # same figure, one screen redesign later — and `openPct` divides by `k.n`
    # too. `openP = kPapers[0]` and `lastP = kPapers[1]` are the one-open-
    # paper-at-index-0 assumption, stated as fact. So the ruling is
    # re-expressed onto `glance` rather than dropped, in the same way E1's
    # year statement moved from the deleted `longMeta` onto `klass.meta`.
    #
    # ⚑ AND THIS ENTRY IS WHERE MIDE'S WEEK BAR LANDS, because the two lines
    # it replaces — `const openP` / `const lastP` — ARE the class screen's
    # scope, and the ruling is that the scope is a teaching week rather than
    # a position in the paper list. Everything downstream (`glance`, the
    # roster column, the assignment table) reads the locals declared here.
    #
    # ⚠️ THE FIRST AND LAST CHIPS ARE BUCKETS, DELIBERATELY. The bar shows at
    # most twelve weeks. Work set for a week still AHEAD (teachers plan
    # forward, and `academic_week` can name any week of the year) has a
    # negative index, and work older than the twelfth chip has an index off
    # the end. Filtered strictly, both would simply vanish from the class
    # screen — a teacher would set next week's homework and watch it
    # disappear. So the current-week chip carries everything at or ahead of
    # it and the oldest chip carries everything at or behind it. Nothing a
    # teacher has set is ever unreachable, and each paper still states its
    # own due date.
    #
    # ⚠️ `wMean` IS THE MEAN OF THE WEEK'S COLUMN MEANS, not a pooled
    # sum/sum, because that is the definition `classMean` already uses in the
    # seam and two definitions of one word is how a dashboard starts
    # disagreeing with itself.
    (dict(method="renderVals", key="const openP"),
     """    /* ── ⊕ RULED BY MIDE, 1 Sep 2026 — THE CLASS SCREEN IS SCOPED TO A
        TEACHING WEEK. `weekIdx` 0 is the week the bar opens on and the list
        counts backwards, which is Design's own direction. Papers map onto
        weeks by the week they were SET in; the two end chips are buckets, so
        work set ahead and work older than the bar are both still reachable.
        See `WEEK_BAR_RESTORED`. ── */
    const kWeeks = this.weeks();
    const wi = this.weekIdxFor(k);
    const wWeek = kWeeks[wi] || null;
    const wOldest = wi >= kWeeks.length - 1;
    const wPapers = kPapers.filter(p => wi === 0
      ? (p.weekIdx == null || p.weekIdx <= 0)
      : (wOldest ? p.weekIdx >= wi : p.weekIdx === wi));
    const wIdxs = wPapers.map(p => p.idx);

    /* Per child, for the SELECTED week: how many of that week's papers they
       handed in, and whether any of them was late. `late` stays TRI-STATE —
       true, false, or null for "no stamp and no deadline" — because folding
       the unknown into either answer is a claim about a child that the row
       cannot support. */
    const wTally = {};
    kRoster.forEach(r => {
      const row = kMx.byId[r.id];
      let wIn = 0, wLateOne = null;
      wIdxs.forEach(i => {
        if (!(row && row.submitted[i])) return;
        wIn += 1;
        if (row.late[i] === true) wLateOne = true;
        else if (row.late[i] === false && wLateOne !== true) wLateOne = false;
      });
      wTally[r.id] = { in: wIn, asked: wIdxs.length, late: wLateOne };
    });

    const wSub = wIdxs.reduce((a, i) => a + (kMx.colSub[i] || 0), 0);
    const wAsk = wIdxs.reduce((a, i) => a + (kMx.colAsked[i] || 0), 0);
    const wMeans = wIdxs.map(i => kMx.colMean[i]).filter(v => v != null);
    const wMean = wMeans.length
      ? Math.round(wMeans.reduce((a, v) => a + v, 0) / wMeans.length) : null;
    const openP = wPapers[0] || null;""",
     "the class screen's four tiles, re-expressed onto the block v3 replaced "
     "them with, and scoped to Mide's teaching week. See the block comment: "
     "the roster as a denominator, lateness by subtraction, and three "
     "captions that overstate their own figure — all three survive v3 inside "
     "`glance`, which the locals declared here now scope. The corrections to "
     "`glance`'s own keys are separate entries at the end of this tuple, "
     "because a property anchor replaces one property."),

    # the two helpers those tiles now call, defined beside them
    #
    # ⊕ RE-ANCHORED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306). This entry only
    # ever PREPENDED two helpers; `const flagged` is where they go, not what
    # they are about. v3 dropped `.length` from that line — `flagged` is an
    # array now, `watch` takes `flagged.slice(0, 4)` and `kFlagged =
    # flagged.length` is declared further down — so the line is REPRODUCED AS
    # v3 WROTE IT. Restoring the `.length` would leave `flagged.slice` on a
    # number, which is a TypeError at mount on every class page.
    (dict(method="renderVals", key="const flagged"),
     "    const kAsked = (i) => kMx.colSub[i] + '/' + (kMx.colAsked[i] || 0);\n"
     "    const kOnTimePct = (i) => {\n"
     "      const known = kMx.colOnTime[i] + kMx.colLate[i];\n"
     "      return known ? Math.round((kMx.colOnTime[i] / known) * 100) + '%' "
     ": '—';\n"
     "    };\n"
     "    const flagged = kRoster.filter(r => r.flag);",
     "`kAsked` is `submitted/asked` — the denominator MRB-38 locked. "
     "`kOnTimePct` divides by the population whose lateness is KNOWN rather "
     "than by everyone who submitted, which is the same correction "
     "`markedPct` already carries in the seam. "
     "⊕ 1 Sep 2026 (MRB-306) — moved off `frm` onto "
     "`method=\"renderVals\", key=\"const flagged\"`, and the anchor line is "
     "now emitted in v3's shape (an array, no `.length`) because v3's own "
     "`watch` and `kFlagged` both read it that way."),

    # ⊕ RE-ANCHORED FOR DESIGN'S v2, 26 Aug 2026. v1 drew `'Year ' + k.year +
    # ' · ' + k.ks + ' · 2026–27 · '` ahead of the counts; v2 draws the counts
    # alone. Year group and key stage were v1's drawing and follow it out; the
    # class's OWN academic year is Mide's E1 ruling and stays, leading, so
    # 10h/Ph1 and 11h/Ph1 — the same 17 students a year apart — never share a
    # header. The singular fix ("1 assignment") survives the redraw.
    # ⊕ RE-EXPRESSED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306) — AND THIS ONE IS
    # A RE-EXPRESSION, NOT A RE-ANCHOR. There is no `longMeta` in v3 to point
    # at: Design deleted the key outright and rebuilt the class header as
    # `klass.meta` / `klass.statLine` / `klass.paperLine`. The assignment
    # count moved to `paperLine` and is drawn correctly there, so the plural
    # half of this ruling has been overtaken by Design and is not restated.
    #
    # What has NOT been overtaken is the E1 ruling the entry exists to serve:
    # every class surface states its OWN academic year, off `k.yearName`, and
    # `MRB_DATA('yearLabel')` — the WORKING year — is banned from this
    # expression. v3's `meta` states the year nowhere, so a class opened out
    # of 2025-26 is again indistinguishable from this year's, which is
    # precisely the defect E1 was written about. The line is therefore
    # re-expressed onto `klass.meta`: v3's own three parts, in v3's own
    # order, with `k.yearName` LEADING (as it led in `longMeta` — the card
    # meta trails it, the header leads with it, so a teacher checking WHICH
    # 11h/Ph1 they are on reads the year first).
    #
    # `.filter(Boolean).join(' · ')` rather than concatenation, for the
    # reason it always was: `academic_year_name` is null on a year nobody
    # named and `year_group` is nullable, and a dropped part beats
    # "Year null · undefined". With both present the rendered string is v3's,
    # character for character, plus the year.
    # ══ "MOST MISSING" BURIES THE CLASSES THAT NEED SOMETHING ═══════════
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a). Design ranks the cards by the
    # week's shortfall and gives every non-live class the same `-1`:
    #
    #     const ga = a.state === 'live' ? (a.week[1] - a.week[0]) : -1;
    #
    # A tie keeps class-code order, so `nowork` and `empty` interleave. On
    # Design's twelve that is invisible — three non-live cards at the end of
    # one screen. On the working year it is the whole page: measured on prod
    # for 2026-27, 69 classes, 3 with any members, 1 with any assignments. A
    # sixty-card wall in which `11h/Ph1` (17 children enrolled, no work set)
    # and `11r/Sc1` (33) sit at positions 47 and 55, below fifty-seven
    # classes with nobody in them at all.
    #
    # Both genuinely have nothing MISSING — nobody was asked for anything —
    # so this is not a correction to the arithmetic. It is the tie-break,
    # which Design left to alphabetical order, and the teacher's question
    # under this sort is "where do I need to go". A class with 17 children
    # and no work set is the answer; an empty class is a roster import.
    #
    # Design's own logic already draws that distinction one screen away:
    # `setupRows` splits exactly these two states, offering "Import" for
    # `empty` and "Set work" for `nowork`. The ranking now agrees with it.
    #
    #     live, by shortfall (descending) → nowork → empty
    #
    # ⚠️ A JUDGEMENT CALL AND EASILY REVERSED: put both back to `-1` and the
    # old order returns. Mide's brief names the sort ("code or most missing")
    # and does not rule the tie-break.
    # ⚠️ TWO ENTRIES, ONE FOR EACH SIDE OF THE COMPARATOR, and it has to be
    # two. A statement anchor on `if (s.sort === 'activity')` ends at the
    # first line back at its own depth that terminates with `;` — and an
    # `if` block's closing brace does not — so that anchor runs straight on
    # and swallows the whole `const cards` builder after it. It was tried;
    # the E1 byte guard caught it, which is the guard working. Design writes
    # the same ternary twice, so the ruling mirrors her and each entry is one
    # self-identifying line.
    (dict(method="renderVals", key="const ga"),
     "        const ga = a.state === 'live' ? (a.week[1] - a.week[0])\n"
     "          : (a.state === 'nowork' ? -1 : -2);",
     "the \"most missing\" tie-break, left side. Design gives every non-live "
     "class -1, so a class with 17 children and no work set sorts among "
     "fifty-seven empty ones. Nothing is missing in either, but only one of "
     "them has children waiting."),
    (dict(method="renderVals", key="const gb"),
     "        const gb = b.state === 'live' ? (b.week[1] - b.week[0])\n"
     "          : (b.state === 'nowork' ? -1 : -2);",
     "the \"most missing\" tie-break, right side. Design writes the same "
     "ternary twice; so does the ruling."),

    # ══ "ENROLLED AND WAITING. LAST ACTIVITY NO ACTIVITY YET." ══════════
    #
    # ⊕ RULED 2 Sep 2026 (MRB-306 Phase 2a). THE SAME DEFECT AS THE CARD'S
    # `activity` LINE, one screen along, and this one fires EVERY TIME the
    # line is drawn rather than only on some classes.
    #
    # `noWorkLine` is the class page's empty state for `noWork`, which is
    # `kPapers.length === 0`. With no papers there are no matrix columns, so
    # no submission stamp can be read, so `lastIso` is null for every child
    # on the roster, so `k.last` is the words "No activity yet" — always.
    # Design's sentence welds "Last activity " in front of it, so the state
    # this line exists to explain reads, without exception:
    #
    #     "25 students are enrolled and waiting. Last activity No activity
    #      yet."
    #
    # No fixture could show it: Design's own class is `live`, and her
    # `nowork` sample carries an invented "2 days ago" that the seam cannot
    # produce (see `_no_activity` in build_teacher_port.py).
    #
    # The branch is kept rather than collapsed to the one arm that can fire
    # today. It costs nothing, and it states the rule — say what the stamp
    # says, or say there is none — rather than encoding a coupling between
    # `noWork` and `lastIso` that a later change to `buildRoster` would
    # silently break.
    #
    # ⚠️ THIS IS THE CLASS-DETAIL SCREEN, NOT SCREEN 1, and it is fixed here
    # anyway: it is one line, it is the same sentence, and the alternative is
    # leaving a known fabrication in the tree for the next unit to meet.
    (dict(method="renderVals", key="klass.noWorkLine"),
     "        noWorkLine: k.n + ' students are enrolled and waiting. '\n"
     "          + (k.last === 'No activity yet'\n"
     "            ? 'No activity yet.'\n"
     "            : 'Last activity ' + k.last + '.'),",
     "the class screen's no-work line. `noWork` means no papers, no papers "
     "means no submission stamps, so `k.last` is ALWAYS the words \"No "
     "activity yet\" here and the sentence always read \"Last activity No "
     "activity yet.\""),

    (dict(method="renderVals", key="klass.meta"),
     "        meta: [k.yearName,\n"
     "          k.n + (k.n === 1 ? ' student' : ' students'),\n"
     "          k.year ? 'Year ' + k.year + ' ' + k.subject : k.subject\n"
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
     "goes to check WHICH 11h/Ph1 they are looking at.\n"
     "\n"
     "        ⊕ RE-EXPRESSED, 1 Sep 2026 (MRB-306). v3 DELETED `longMeta` "
     "and rebuilt the header as `klass.meta` + `statLine` + `paperLine`, so "
     "there was nothing left to re-anchor. The assignment plural is now "
     "Design's own job on `paperLine`; the academic year is still Mide's, "
     "and it is stated on `klass.meta` — v3's parts, v3's order, "
     "`k.yearName` leading, dropped rather than printed when the school has "
     "not named the year. `k.year` is guarded for the same reason: "
     "`year_group` is nullable and \"Year null\" is worse than silence.\n"
     "\n"
     "        ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — THE FOURTH PART IS GONE. v3's "
     "own line ended `· Next lesson today · P5 · 13:55 · Lab 2`, off "
     "`TODAY_LESSONS`, which is four invented lessons and is deleted by "
     "`DROP_FIELDS`. The falsy arm is not kept either: \"No lesson today\" "
     "is not the honest empty state, it is a CLAIM — that this class has no "
     "lesson today — and the platform holds no timetable to make it from. A "
     "part that cannot be computed is dropped, which is what "
     "`.filter(Boolean)` is here for. When the Today/Timetable unit lands "
     "real timetable data, this is the part that comes back."),

    # ══ THE DIGEST ══════════════════════════════════════════════════════
    #
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 6) — ONE RENDERING OF THIS WEEK'S
    # RETURN, and the flag count carried rather than counted twice.
    ("""        code: c.code, ks: c.ks,
        sub: live ? c.week[0] + '/' + c.week[1] : '—',""",
     """        code: c.code, ks: c.ks, flagN: fl,
        sub: MRB_WEEK_IN(c),""",
     "the by-class row's Submitted cell. The expression is unchanged in "
     "meaning — `MRB_WEEK_IN` is this line, lifted — and that is the point: "
     "the class report's Submissions tile was computing the same figure a "
     "different way (`colSub[0]`, paper index 0) and the two only agreed "
     "because Design's sample makes them agree. There is one renderer now "
     "and both call it.\n"
     "\n"
     "        `flagN` is the row's own \"students to chase\" count, kept on "
     "the row so the Needs-a-look TILE can sum the rows instead of "
     "re-walking every roster with a second copy of the same filter. Not a "
     "rendered field — the row markup names `code`, `ks`, `sub`, `mean`, "
     "`ontime`, `needs` and `open`, and an extra key is inert."),

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
        { label: 'Submissions', value: MRB_WEEK_IN(k), sub: 'This week' },
        { label: 'Class mean', value: kMean == null ? '—' : kMean + '%', sub: 'Across ' + kMx.markedIdx.length + (kMx.markedIdx.length === 1 ? ' marked assignment' : ' marked assignments') },
        { label: 'On time', value: kMx.markedPct == null ? '—' : kMx.markedPct + '%', sub: MRB_ONTIME_SUB(kMx.markedOnTime, kMx.markedLate, kMx.markedLateUnknown, 'marked') },
        { label: 'Needs a look', value: String(kFlagged), sub: kFlagged ? 'Nothing in this week, and behind' : 'Everyone accounted for' }
      ] : [
        { label: 'Submissions', value: String(totalSubs), sub: 'Across ' + liveClasses.length + (liveClasses.length === 1 ? ' active class' : ' active classes') },
        { label: 'Mean score', value: dgMeans.length ? Math.round(dgMeans.reduce((a, m) => a + m, 0) / dgMeans.length) + '%' : '—', sub: 'Mean of ' + dgMeans.length + (dgMeans.length === 1 ? ' class mean' : ' class means') },""",
     "the digest's four tiles. The same three corrections as the class "
     "screen's, plus the division by `liveClasses.length` — which is ZERO for "
     "a teacher whose classes have no work set yet, and `NaN%` was what a "
     "teacher saw on their first day.\n"
     "\n"
     "        ⊕ 2 Sep 2026 — ON TIME, ON THE CLASS REPORT, takes "
     "`MRB_ONTIME_SUB` rather than `MRB_LATE_LINE` directly. The two differ "
     "only in the case this screen kept hitting: with nothing marked, "
     "`MRB_LATE_LINE(0, 0, 0, 'marked')` printed the words \"0 late of 0 "
     "marked\" underneath an em dash, which reads as a measurement of a "
     "class that has never been set any work. `MRB_ONTIME_SUB` has the arm "
     "for it — \"Nothing submitted yet\" — and the whole-school tile two "
     "lines below was already calling it.\n"
     "\n"
     "        ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 6) — TWO OF THESE FOUR "
     "WERE STILL A SECOND SOURCE.\n"
     "\n"
     "        **Submissions, on the class report.** `kAsked(0)` is "
     "`colSub[0]/colAsked[0]` — PAPER INDEX 0, which `buildPapers` sorts "
     "`due_at DESC NULLS FIRST`. It is the newest paper, not this week's, and "
     "a paper with no deadline at all sorts ahead of every dated one. The "
     "tile is captioned \"This week\" and the digest's own by-class row for "
     "the SAME class reads `c.week`, the seam's real current-teaching-week "
     "count. Two derivations, one caption. They agree on every fixture "
     "because Design's fiction gives every class exactly one paper due this "
     "week at index 0 — which is precisely why nothing caught it. Driven at "
     "A4 the tile read \"11/16 · This week\" directly above a table whose "
     "first row said that 11/16 belonged to \"Particle model — recall and "
     "apply\", an OPEN assignment. Both readers now call `MRB_WEEK_IN`.\n"
     "\n"
     "        **Mean score.** `(this.meanOf(c) || 0)` turns a class with "
     "nothing marked into a 0% class mean and LEAVES IT IN THE DENOMINATOR, "
     "while the by-class row three inches below prints \"—\" for that same "
     "class. The `liveClasses.length ? … : '—'` guard added earlier stops the "
     "NaN and does nothing about this. `dgMeans` is the classes that HAVE a "
     "mean, so the value and the caption's count describe the same "
     "population, and the caption now agrees with the rows a reader can "
     "count."),

    # ── the whole-school Needs-a-look tile: summed off the rows ──────────
    ("        { label: 'Needs a look', value: String(liveClasses.reduce("
     "(a, c) => a + this.rosterFor(c).filter(r => r.flag).length, 0)), "
     "sub: 'Students with nothing in' }",
     "        { label: 'Needs a look', value: String(dgFlagged), "
     "sub: 'Students with nothing in' }",
     "the tile walked every roster and re-applied the flag filter, and the "
     "table under it walked them again with its own copy of the same "
     "expression. They agree today because the two expressions are "
     "character-for-character the same predicate — which is exactly the "
     "arrangement that stops agreeing the day one of them is edited, and "
     "\"57\" over rows that sum to something else is unfalsifiable by any "
     "gate we have. `dgFlagged` sums the rows, so the tile is now a total "
     "OF the table rather than a second opinion about it."),

    # ── the class report's On-time column: a percentage, like every other ──
    ("        ontime: p.when === 'upcoming' ? '—' : "
     "String(kMx.colOnTime[p.idx]),",
     "        ontime: p.when === 'upcoming' ? '—' : kOnTimePct(p.idx),",
     "the same column header — \"ON TIME\" — carried a PERCENTAGE on the "
     "by-class table (`matrixFor(c).markedPct + '%'`) and a BARE COUNT here. "
     "Driven, the by-class table read 80% / 93% / 84% and the by-assignment "
     "table read 11 / 8 / 12 under the identical heading; a reader with the "
     "class report in front of them has no way to tell that \"6\" in the "
     "On-time column of a row whose Submitted cell says 11/16 is six "
     "children rather than six percent.\n"
     "\n"
     "        And the count is the raw `colOnTime`, which is the defect "
     "`MRB_ONTIME_VALUE` exists to prevent: `is_late` is NULL on every "
     "submission written before 22 Aug 2026, so a paper can have thirteen "
     "submissions with nothing known about the timing of any of them and "
     "this cell printed \"0\" — nobody was on time. Every fixture in the set "
     "has `colLateUnknown` all zeros, so no gate could see it.\n"
     "\n"
     "        `kOnTimePct` is not new: it was written beside `kAsked` by the "
     "ruling on `const flagged`, it divides by the population whose lateness "
     "is KNOWN and returns an em dash when that population is empty — the "
     "same definition `markedPct` carries in the seam — and it was DEAD "
     "CODE, called from nowhere. The correct derivation already existed and "
     "the screen was not using it."),

    # ── "this term" is a claim the list cannot support ───────────────────
    ("        ? k.n + ' students · ' + kPapers.length + ' assignments this "
     "term'",
     "        ? k.n + ' students · ' + kPapers.length + (kPapers.length === 1 "
     "? ' assignment' : ' assignments')",
     "`papersFor` returns the class's assignments for the academic year in "
     "view, which `buildPapers` takes from the whole `pack.assignments` list "
     "— there is no term filter anywhere in the chain. In September \"12 "
     "assignments this term\" over a list that spans the year is a number "
     "with the wrong noun on it, and the plural was unguarded besides."),

    # ── one population for the Submissions tile and its own caption ──────
    ("    const totalSubs = this.CLASSES.reduce((a, c) => a + c.week[0], 0);",
     "    const totalSubs = liveClasses.reduce((a, c) => a + c.week[0], 0);",
     "the tile reads `String(totalSubs)` under the caption \"Across N active "
     "classes\", and `totalSubs` was summed over ALL classes. The figure is "
     "unchanged — a class that is not live has an empty roster or no papers, "
     "so no child of it can have `inWeek` set and its `week[0]` is "
     "structurally 0 — but the value and the caption were describing two "
     "different populations and only happened to coincide. An invariant that "
     "holds by accident is one nobody will notice breaking."),

    ("""      const missing = k.n - kMx.colSub[p.idx];""",
     """      const missing = Math.max(0, (kMx.colAsked[p.idx] || 0) - kMx.colSub[p.idx]);""",
     "`classReportRows`. Same denominator defect: `k.n` is the CURRENT "
     "roster, and a departed student who submitted makes this negative."),

    # ── the SECOND copy of the `CLASSES[3]` fallback ────────────────────
    ("""    const k = all ? null : (this.klassById(scope) || this.CLASSES[3]);""",
     """    const k = all ? null : this.klass();""",
     "`chartFor` carried its OWN copy of the fallback the `klass` ruling "
     "exists to remove: a scope that does not resolve falls back to THE "
     "FOURTH CLASS IN THE LIST. The `klass` ruling says why that is not "
     "acceptable — on a real URL it is one teacher's class shown under "
     "another teacher's scope, silently — and it is no better for being in "
     "a chart. It is also a crash on a short list: `CLASSES[3]` is "
     "`undefined` for a teacher with three classes or fewer, and `k.code` "
     "is dereferenced eleven lines later. A teacher with three classes is "
     "the ordinary case in this school, not the edge.\n"
     "\n"
     "        `this.klass()` is the ruled resolver and resolves the SAME "
     "input: `chartScope` is `MRB_Q('class') || 'all'` and `state.classId` "
     "is the seam's `classId`, which `load()` also takes from `?class=`. So "
     "this is not a new answer — it is the existing one, called instead of "
     "copied. Set-but-missing throws with the class id in the message; "
     "absent returns the first class, or `MRB_NO_CLASS()` for a teacher "
     "with none."),

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
          return { label: c.code, sub: st.id + ' · ' + st.text, value: min + '%', pct: min, fill: min < 50 ? 'var(--st-accent)' : 'var(--st-hatch-b)', qi, stem: st, qkey: st.question_ref || st.text || '' };
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

    # ── the tiles and note of `questions / all`: A DELETED FIELD, TWICE ──
    ("""        const tally = {};
        rows.forEach(r => { tally[r.qi] = (tally[r.qi] || 0) + 1; });
        const keys = Object.keys(tally).sort((a, b) => tally[b] - tally[a]);
        const uniqueTop = keys.length === 1 || tally[keys[0]] > tally[keys[1]];
        const worst = rows.slice().sort((a, b) => a.pct - b.pct)[0];
        const under50 = rows.filter(r => r.pct < 50).length;
        return { ...base, title: 'Weakest question per class, last marked set', rows,
          tiles: [tile('Classes', rows.length, 'With marked work'), tile('Lowest', worst.label + ' · ' + worst.value, worst.sub),
            uniqueTop
              ? tile('Most common', this.STEMS[keys[0]].id, this.STEMS[keys[0]].text)
              : tile('Weak points', keys.length + ' questions', 'No single common gap')],
          note: uniqueTop
            ? this.STEMS[keys[0]].text + ' is the weakest question in ' + tally[keys[0]] + ' of ' + rows.length + ' classes'
            : 'No single common gap — ' + keys.length + ' different questions come last, and ' + under50 + ' classes fall below 50% on theirs' };""",
     """        const tally = {};
        rows.forEach(r => { if (r.qkey) { tally[r.qkey] = (tally[r.qkey] || 0) + 1; } });
        const keys = Object.keys(tally).sort((a, b) => tally[b] - tally[a]);
        const top = keys.length ? rows.filter(r => r.qkey === keys[0])[0].stem : null;
        const uniqueTop = !!top && rows.length > 1 &&
          (keys.length === 1 || tally[keys[0]] > tally[keys[1]]);
        const worst = rows.slice().sort((a, b) => a.pct - b.pct)[0];
        const under50 = rows.filter(r => r.pct < 50).length;
        return { ...base, title: 'Weakest question per class, last marked set', rows,
          tiles: [tile('Classes', rows.length, rows.length === 1 ? 'With a marked paper' : 'With marked work'),
            tile('Lowest', worst.label + ' · ' + worst.value, worst.sub),
            uniqueTop
              ? tile('Most common', top.id, top.text)
              : tile('Weak points', keys.length + (keys.length === 1 ? ' question' : ' questions'),
                     rows.length < 2 ? 'Only one class to look at' : 'No single common gap')],
          note: uniqueTop
            ? top.text + ' is the weakest question in ' + tally[keys[0]] + ' of ' + rows.length + ' classes'
            : (rows.length < 2
               ? 'One class has a marked paper — nothing to compare it with yet'
               : 'No single common gap — ' + keys.length + ' different questions come last, and ' + under50 + (under50 === 1 ? ' class falls' : ' classes fall') + ' below 50% on theirs') };""",
     "⛔ THIS ONE KILLED THE PAGE, AND IT WAS SHIPPING. `STEMS` is DELETED "
     "by `DROP_FIELDS` — eight invented question stems held as a class "
     "field. The ruling above replaced the four reads in this branch's ROWS "
     "and the four in the class branch, and left the TWO here. "
     "`this.STEMS[keys[0]]` on `undefined` throws `TypeError: Cannot read "
     "properties of undefined (reading '3')`, `renderVals` never returns, "
     "and the Charts page goes blank the moment a teacher presses Question "
     "difficulty on All classes. Driven on the delivery's OWN POPULATED "
     "FIXTURE on 2 Sep 2026 — the one every gate already had — and "
     "reachable in production the moment one class has one marked paper, "
     "which on the working year is `8r/Sc1` and nothing else.\n"
     "\n"
     "        ⚠️ AND THE TALLY WAS KEYED ON THE WRONG THING. `r.qi` is the "
     "question's INDEX WITHIN ITS OWN PAPER, and every class in this chart "
     "is on a DIFFERENT paper — `MRB_NEWEST_MARKED` picks each class's own "
     "newest marked set. Counting how many classes share index 3 compares "
     "question 4 of a chemistry paper with question 4 of a physics one and "
     "calls the coincidence \"the most common gap\". It reads as a finding "
     "and it is arithmetic on unrelated things. In Design's fiction there "
     "is ONE `STEMS` array behind every paper in the school, so the index "
     "IS the question and the defect cannot exist. The key is now the "
     "question's own identity — `question_ref` where the snapshot carries "
     "one, its text otherwise — and a row with neither is left OUT of the "
     "tally rather than counted as a match with every other blank.\n"
     "\n"
     "        `rows.length > 1` is the third correction. With one class the "
     "top of the tally is unanimous by construction, and \"X is the weakest "
     "question in 1 of 1 classes\" has the shape of a finding and none of "
     "the content. One class is the whole school today."),

    ("""      const rows = live.map(c => {
        const m = mx(c);
        const pct = c.n ? Math.round((m.colSub[0] / c.n) * 100) : 0;
        return { label: c.code, sub: c.ks, value: m.colSub[0] + '/' + c.n, pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
      });""",
     """      const rows = live.map(c => {
        const w = c.week || [0, 0];
        const pct = w[1] ? Math.round((w[0] / w[1]) * 100) : 0;
        return { label: c.code, sub: c.ks, value: MRB_WEEK_IN(c), pct, fill: pct < 60 ? 'var(--st-accent)' : 'var(--st-hatch-b)' };
      });""",
     "`submissions / all`. `c.n` is the current roster; a class where two "
     "pupils left after submitting read \"31/29\".\n"
     "\n"
     "        \u2295 2 Sep 2026 (MRB-306 Phase 2a screen 7) \u2014 AND "
     "`colSub[0]` IS NOT THIS WEEK EITHER. The `colAsked` denominator fixed "
     "the impossible fraction and left the row plotting PAPER INDEX 0 under "
     "a chart titled \"Submissions this week\". Correcting the tiles above "
     "it to `c.week` and leaving the rows on `colSub[0]` would have made a "
     "card whose total disagreed with the bars beneath it \u2014 on "
     "`insights-single` the tile read 0/2 above a row reading 1/2, which is "
     "the two-sources defect reappearing INSIDE one chart. `MRB_WEEK_IN` is "
     "the one renderer of this figure and the rows call it too."),

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

    # ══ THE HANDED-OVER DEFECT: "This week", A THIRD TIME ═══════════════
    ("""      tiles: [tile('This week', m.colSub[0] + '/' + k.n, 'Open assignment'), tile('Outstanding', k.n - m.colSub[0], 'Students yet to submit'), tile('Assignments', rows.length, 'Set this term')],""",
     """      tiles: [tile('Submissions', MRB_WEEK_IN(k), 'This week'),
        tile('Outstanding', k.state === 'live' ? Math.max(0, (k.week[1] || 0) - (k.week[0] || 0)) : '—', 'Students yet to submit'),
        tile('Assignments', rows.length, rows.length === 1 ? 'Set so far this year' : 'Set so far this year')],""",
     "⊕ HANDED OVER BY SCREEN 6, and it is the WORST of the three "
     "renderings of this week's return. Two faults in one expression and a "
     "third in the caption beside it.\n"
     "\n"
     "        **`colSub[0]` is not this week.** `buildPapers` sorts "
     "`due_at DESC NULLS FIRST`, so index 0 is the NEWEST paper — whatever "
     "week it belongs to — and a paper with no deadline at all sorts ahead "
     "of every dated one and so belongs to no week. Design's fiction gives "
     "every class exactly one paper, due this week, at index 0, which is why "
     "three independent derivations of one figure agreed on every fixture in "
     "the set. Driven on `insights-single` — one class, one paper, set in an "
     "EARLIER teaching week — the tile read \"1/2\" under the caption \"This "
     "week\" while the seam's own `week` said 0, and the single row "
     "underneath it said \"Marked · due Wed 26 Aug\".\n"
     "\n"
     "        **`k.n` is the roster denominator MRB-38 ruled against.** It is "
     "the CURRENT roll; `colSub` counts every submission including a "
     "departed student's, so `k.n - colSub[0]` GOES NEGATIVE the moment a "
     "child who submitted has left. \"Outstanding: −1\" tells a teacher "
     "nothing except that the page is wrong. `week[0]` and `week[1]` cannot "
     "do that: `buildRoster` maps over `pack.members`, so `week[0]` counts a "
     "subset of `week[1]` by construction and the subtraction has a floor "
     "whether or not the `Math.max` is there.\n"
     "\n"
     "        **\"Open assignment\" was a claim about paper index 0.** On "
     "`insights-single` the only paper is MARKED and the caption said Open. "
     "The sub is now the word the digest's own Submissions tile carries, so "
     "the two screens read identically.\n"
     "\n"
     "        `MRB_WEEK_IN` is screen 6's helper and this is its third "
     "caller. NOT a fourth derivation — the point of the helper is that "
     "there is one renderer of this figure and every reader of it calls "
     "that renderer.\n"
     "\n"
     "        The tile is LABELLED \"Submissions\" and captioned \"This "
     "week\" \u2014 which is the digest\u2019s class-report tile, word for "
     "word. Design labelled it \"This week\" and captioned it \"Open "
     "assignment\"; with the caption corrected, label and caption both read "
     "\"This week\", which on screen looks like a rendering fault. Two "
     "screens showing one figure now show it under one name.\n"
     "\n"
     "        \"Set this term\" goes for the reason already ruled on the "
     "digest's sub-heading: `papersFor` returns the assignments for the "
     "academic year in view and there is no term filter anywhere in the "
     "chain.\n"
     "\n"
     "        ⚠️ ONE THING THIS DOES NOT FIX, STATED RATHER THAN HIDDEN. "
     "`week[1]` is the whole roster whether or not anything was DUE this "
     "week, so a live class with no paper due this week reads \"0/16\" — "
     "which looks like an accusation and is really \"nobody was asked\". "
     "That is a property of the shared helper and of the seam's `week` "
     "tuple, so it is the same on the class cards and the digest, and "
     "fixing it HERE would put this screen back to disagreeing with the "
     "other two. It belongs to `MRB_WEEK_IN` and is in the screen 7 "
     "report."),

    # ── and the same chart with NOTHING to plot ─────────────────────────
    ("""    const lowP = rows.slice().sort((a, b) => a.pct - b.pct)[0];
    return { ...base, title: k.code + ' — submissions by assignment', rows,""",
     """    const lowP = rows.slice().sort((a, b) => a.pct - b.pct)[0];
    if (!rows.length) {
      return { ...base, title: k.code + ' — submissions by assignment',
        note: k.state === 'empty' ? 'No students on the roster yet'
                                  : 'No work set for this class yet' };
    }
    return { ...base, title: k.code + ' — submissions by assignment', rows,""",
     "`submissions / class` WITH NO PAPERS, which is 68 of the working "
     "year's 69 classes on 2 Sep 2026. `m.colSub[0]` on an empty column "
     "array is `undefined`, so the tile rendered the literal string "
     "**\"undefined/16\"** and the one beside it rendered **\"NaN\"** — both "
     "photographed on `insights-noroster` and `insights-nolive` before this "
     "guard. Three zero-width bars and two nonsense words is not an empty "
     "state; it is the page failing where a teacher cannot tell that it "
     "has."),

    ("""        ? live.map(c => ({ label: c.code, sub: c.ks, on: mx(c).markedOnTime, tot: mx(c).markedSub }))
        : this.papersFor(k).filter(p => p.when === 'marked').map(p => ({ label: p.title, sub: 'Due ' + p.due, on: mx(k).colOnTime[p.idx], tot: mx(k).colSub[p.idx] }));""",
     """        ? live.map(c => ({ label: c.code, sub: c.ks, on: mx(c).markedOnTime, tot: mx(c).markedOnTime + mx(c).markedLate }))
        : this.papersFor(k).filter(p => p.when === 'marked').map(p => ({ label: p.title, sub: 'Due ' + p.due, on: mx(k).colOnTime[p.idx], tot: mx(k).colOnTime[p.idx] + mx(k).colLate[p.idx] }));""",
     "the on-time chart. `markedSub` includes the submissions whose lateness "
     "is UNKNOWN, so the bar counted every unknown as late — the same error "
     "as the roster row's, in a graph, where it is harder to see."),

    ("""      note: lowP ? 'Weakest return: ' + lowP.label + ' at ' + lowP.pct + '%' : '' };""",
     """      note: (rows.length > 1 && lowP) ? 'Weakest return: ' + lowP.label + ' at ' + lowP.pct + '%' : '' };""",
     "the class chart's caption, ON ONE ASSIGNMENT. \"Weakest return: "
     "Energy stores and transfers at 50%\" under a chart with exactly one "
     "bar in it is a ranking with one entrant, and it reads as a judgement "
     "on the only piece of work the class has done. One class with one "
     "paper is the working year's entire assignment history on 2 Sep 2026."),

    # ══ `submissions / all`: THE SAME FIGURE, THE SAME TWO FAULTS ═══════
    ("""      const subs = live.reduce((a, c) => a + mx(c).colSub[0], 0);
      const seats = live.reduce((a, c) => a + c.n, 0);
      const done = live.filter(c => mx(c).colSub[0] === c.n).length;
      const low = rows.slice().sort((a, b) => a.pct - b.pct)[0];
      return { ...base, title: 'Submissions this week', rows,
        tiles: [tile('Submitted', subs + '/' + seats, 'Across ' + live.length + ' classes'), tile('Outstanding', seats - subs, 'Students yet to submit'), tile('Everyone in', done + '/' + live.length, 'Classes complete')],
        note: low ? 'Lowest return: ' + low.label + ' at ' + low.pct + '% (' + low.value + ')' : '' };""",
     """      if (!rows.length) {
        return { ...base, title: 'Submissions this week',
          note: 'No class has work set yet' };
      }
      const subs = live.reduce((a, c) => a + ((c.week || [0, 0])[0]), 0);
      const seats = live.reduce((a, c) => a + ((c.week || [0, 0])[1]), 0);
      const done = live.filter(c => c.week && c.week[1] && c.week[0] === c.week[1]).length;
      const low = rows.slice().sort((a, b) => a.pct - b.pct)[0];
      return { ...base, title: 'Submissions this week', rows,
        tiles: [tile('Submitted', subs + '/' + seats, 'Across ' + live.length + (live.length === 1 ? ' class' : ' classes')),
          tile('Outstanding', Math.max(0, seats - subs), 'Students yet to submit'),
          tile('Everyone in', done + '/' + live.length, 'Classes complete')],
        note: rows.length < 2 ? ''
          : (low ? 'Lowest return: ' + low.label + ' at ' + low.pct + '% (' + low.value + ')' : '') };""",
     "the whole-school half of the same tile, and it had the same two "
     "faults: `colSub[0]` for \"this week\" and `c.n` for the denominator. "
     "Summed over eight classes the negative cannot be SEEN — it is "
     "absorbed by the other seven — which is worse than the class-scoped "
     "one, not better.\n"
     "\n"
     "        Both now read `c.week`, the seam's current-teaching-week "
     "count, which is what the ROWS of this same chart read (see the "
     "ruling below) and what the digest's by-class Submitted column reads. "
     "One question, one answer, four callers.\n"
     "\n"
     "        The empty guard is the September case: with no live class the "
     "tiles read \"0/0 · Across 0 classes\", \"Outstanding 0\" and "
     "\"Everyone in 0/0\" over a blank axis — a school that submitted "
     "nothing, rather than a school that has not been asked. Photographed "
     "on `insights-nolive`.\n"
     "\n"
     "        And \"Lowest return\" is dropped at one class: naming the "
     "only class in the school as the lowest is a ranking with one entrant."),

    # ── spread: five bands of zero is not an empty state ────────────────
    ("""      const bands = this.BANDS.map(b => ({ label: b.label, n: avgs.filter(v => v >= b.lo && v <= b.hi).length, lo: b.lo }));""",
     """      if (!avgs.length) {
        return { ...base, title: (all ? 'Score spread, all classes' : k.code + ' — score spread'),
          note: all ? 'No student has marked work yet'
                    : (k.state === 'empty' ? 'No students on the roster yet'
                                           : 'Nothing marked for this class yet') };
      }
      const bands = this.BANDS.map(b => ({ label: b.label, n: avgs.filter(v => v >= b.lo && v <= b.hi).length, lo: b.lo }));""",
     "`spread`, both scopes. With no marked work anywhere the chart drew "
     "its five bands at zero, three tiles reading 0, and the caption "
     "\"0 of 0 students sit below 55%, 0 at 70% or above\" — a labelled "
     "axis with no series, which reads as a measurement of a school where "
     "nobody scores anything rather than a school that has not marked "
     "anything. Photographed on `insights-nolive` and `insights-noroster`; "
     "reachable on 68 of the working year's 69 classes."),

    # ── on time: an empty legend under an empty chart ───────────────────
    ("""      const on = src.reduce((a, x) => a + x.on, 0);
      const tot = src.reduce((a, x) => a + x.tot, 0);""",
     """      if (!src.length) {
        return { ...base, title: (all ? 'On time vs late, marked work' : k.code + ' — on time by assignment'),
          note: all ? 'No class has marked work yet' : 'Nothing marked for this class yet' };
      }
      const on = src.reduce((a, x) => a + x.on, 0);
      const tot = src.reduce((a, x) => a + x.tot, 0);""",
     "`ontime`, both scopes. The tiles already carried em dashes from the "
     "unknown-lateness ruling, so this looked handled — but the CHART did "
     "not: an On time / Late key still drew under a card with no bars in "
     "it, and \"Late — · Still marked\" describes marked work that does not "
     "exist. A legend for a series that is not there is the chart claiming "
     "to have measured something."),

    # ── engagement: "everyone" when there is nobody ─────────────────────
    ("""      const rows = this.rosterFor(k);
      const b = this.bucketsOf(rows);
      const cold = rows.filter(r => r.hours >= 168).map(r => r.name);""",
     """      const rows = this.rosterFor(k);
      if (!rows.length) {
        return { ...base, title: k.code + ' — last seen',
          note: 'No students on the roster yet' };
      }
      const b = this.bucketsOf(rows);
      const cold = rows.filter(r => r.hours >= 168).map(r => r.name);""",
     "⚑ `engagement / class` ON A CLASS WITH NO ROSTER SAID **\"Everyone "
     "has opened something this week\"** — about nobody — over three "
     "columns of zero and a tile reading \"Students 0 · On the roster\". "
     "Photographed on `insights-noroster`, which is the shape 66 of the "
     "working year's 69 classes are in today. \"Everyone\" over an empty "
     "set is the most confident sentence on the page and the least "
     "supported."),

    ("""      note: cold.length ? 'Not seen for two weeks: ' + cold.slice(0, 3).join(', ') + (cold.length > 3 ? ' and ' + (cold.length - 3) + ' more' : '') : 'Everyone has opened something this week' };""",
     """      note: cold.length ? 'Not seen for two weeks: ' + cold.slice(0, 3).join(', ') + (cold.length > 3 ? ' and ' + (cold.length - 3) + ' more' : '') : 'Nobody in this class has been quiet for two weeks or more' };""",
     "\u201cEveryone has opened something this week\u201d IS NOT WHAT THIS "
     "CHART MEASURED. `bucketsOf` reads `r.hours`, and `buildRoster` sets "
     "`hours` from the newest SUBMISSION stamp \u2014 or, for a child who "
     "has never submitted anything, from how long they have been ON THE "
     "ROLL. So a class whose roster was imported this morning and which has "
     "never been set any work buckets every child as \u201cactive today\u201d "
     "and was told that all of them had opened something. Photographed on "
     "`insights-nolive`, where the class has sixteen children, no "
     "assignments, and therefore not one submission in existence.\n"
     "\n"
     "        The replacement claims exactly what `cold` counts and nothing "
     "more \u2014 `cold` is `hours >= 168`, so an empty `cold` genuinely "
     "means nobody has been quiet for a fortnight, and that stays true for a "
     "never-active child however long they have been on the roll. No new "
     "derivation and no new field: the same number, described honestly.\n"
     "\n"
     "        \u26a0\ufe0f WHAT IS NOT FIXED HERE. The TILE still reads "
     "\u201cActive today\u201d over children who have never opened anything, "
     "because that is the bucket LABELS being wrong for a never-active "
     "student rather than this caption being wrong \u2014 and "
     "`teacher-live.js` already records it as a handover item beside "
     "`hours` (\u201cthe bucket labels still say last seen, which is not "
     "quite what this measures\u201d). Re-deriving it here would be a second "
     "answer to a question the seam has already parked."),

    ("""        return { ...base, type: 'stack', title: 'Last seen, by class', stacks,""",
     """        if (!stacks.length) {
          return { ...base, title: 'Last seen, by class',
            note: 'No class has work set yet' };
        }
        return { ...base, type: 'stack', title: 'Last seen, by class', stacks,""",
     "`engagement / all`. With no live class the card drew a Today / This "
     "week / 2+ weeks key under nothing, three zero tiles, and the caption "
     "\"0 students have not opened anything for two weeks or more\" — which "
     "is a reassurance, and there was nobody it could be about."),

    ("""          tiles: [tile('Active today', totals.today, 'Across ' + live.length + ' classes'), tile('This week', totals.week, ''), tile('2+ weeks', totals.stale, 'Worth chasing')],""",
     """          tiles: [tile('Active today', totals.today, 'Across ' + live.length + (live.length === 1 ? ' class' : ' classes')), tile('This week', totals.week, ''), tile('2+ weeks', totals.stale, 'Worth chasing')],""",
     "\"Across 1 classes\" — the unguarded plural, on the shape the working "
     "year is actually in."),

    # ── means: a cohort of one is not a cohort ──────────────────────────
    ("""        return { ...base, title: 'Class means, marked work', tiles: [
          tile('Cohort mean', cohort + '%', 'Mean of ' + raw.length + ' class means'),
          tile('Highest', sorted[0].code + ' · ' + sorted[0].mean + '%', ''),
          tile('Lowest', sorted[sorted.length - 1].code + ' · ' + sorted[sorted.length - 1].mean + '%', '')
        ], note: below + ' of ' + raw.length + ' classes sit below the ' + cohort + '% cohort mean',""",
     """        return { ...base, title: 'Class means, marked work', tiles: (raw.length < 2 ? [
          tile('Class mean', cohort + '%', sorted[0].code + ' — the only class with marked work')
        ] : [
          tile('Cohort mean', cohort + '%', 'Mean of ' + raw.length + ' class means'),
          tile('Highest', sorted[0].code + ' · ' + sorted[0].mean + '%', ''),
          tile('Lowest', sorted[sorted.length - 1].code + ' · ' + sorted[sorted.length - 1].mean + '%', '')
        ]), note: raw.length < 2 ? '' : below + ' of ' + raw.length + ' classes sit below the ' + cohort + '% cohort mean',""",
     "`means / all` WITH ONE CLASS, which is the whole school today. "
     "`sorted[0]` and `sorted[sorted.length - 1]` are the SAME ROW, so the "
     "card printed **Highest 8r/Sc1 · 63%** and **Lowest 8r/Sc1 · 63%** "
     "side by side, under a \"Cohort mean\" that is that one class's own "
     "mean, over the caption \"0 of 1 classes sit below the 63% cohort "
     "mean\". Photographed on `insights-single`. Four tiles, one number, "
     "and the word \"cohort\" doing all the lying: a mean of one class is "
     "that class."),

    ("""        tiles: [tile('Class mean', (m.classMean == null ? '—' : m.classMean + '%'), 'Across ' + ps.length + ' marked assignments'),
          tile('Strongest', Math.max.apply(null, means) + '%', best.title),
          tile('Weakest', Math.min.apply(null, means) + '%', worst.title),
          tile('Open work', 'Excluded', 'Not marked yet')],
        note: 'Weakest set: ' + worst.title + ' at ' + m.colMean[worst.idx] + '%' };""",
     """        tiles: (ps.length < 2 ? [
          tile('Class mean', (m.classMean == null ? '—' : m.classMean + '%'), 'From one marked assignment'),
          tile('Open work', 'Excluded', 'Not marked yet')
        ] : [
          tile('Class mean', (m.classMean == null ? '—' : m.classMean + '%'), 'Across ' + ps.length + ' marked assignments'),
          tile('Strongest', Math.max.apply(null, means) + '%', best.title),
          tile('Weakest', Math.min.apply(null, means) + '%', worst.title),
          tile('Open work', 'Excluded', 'Not marked yet')
        ]),
        note: ps.length < 2 ? '' : 'Weakest set: ' + worst.title + ' at ' + m.colMean[worst.idx] + '%' };""",
     "`means / class` WITH ONE MARKED PAPER. `best` and `worst` are the "
     "same paper, so the card read **Strongest 63% · Energy stores and "
     "transfers** beside **Weakest 63% · Energy stores and transfers**, and "
     "the caption named it the weakest set of one. \"Across 1 marked "
     "assignments\" was the unguarded plural in the same row. One class, one "
     "marked paper is the entirety of the working year's data."),

    # ── the sub-heading's plurals ───────────────────────────────────────
    ("""      insSub: chartScope === 'all'
        ? liveClasses.length + ' active classes · ' + totalStudents + ' students on roll'
        : k.code + ' · ' + k.n + ' students · ' + kPapers.length + ' assignments',""",
     """      insSub: chartScope === 'all'
        ? liveClasses.length + (liveClasses.length === 1 ? ' active class · ' : ' active classes · ') + totalStudents + (totalStudents === 1 ? ' student on roll' : ' students on roll')
        : [k.code, k.n + (k.n === 1 ? ' student' : ' students'),
           kPapers.length + (kPapers.length === 1 ? ' assignment' : ' assignments')].join(' · '),""",
     "the Charts sub-heading, three unguarded plurals. \"1 active classes · "
     "2 students on roll\" is the working year's real line."),

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
     "      })),\n"
     # ⊕ 3 Sep 2026 — THREE KEYS THE RESTORED FEED NEEDS AND DESIGN HAS
     # NO COUNTERPART FOR, added here rather than as a fourth LOGIC entry
     # because they are derived from the SAME list and a second entry
     # would read `FEED` twice.
     #
     # ⚠️ `feedEmptyLine` BRANCHES ON `canWrite` AND THAT IS THE POINT.
     # "No shoutouts yet" is an invitation, and on a finished academic
     # year there is nothing to accept it with — the composer above it is
     # gone under MRB-261. Read through `MRB_DATA` for the same reason the
     # `canDelete` line above is: `canWrite` is a KEY of the object being
     # built here, not a local in scope.
     "      feedCount: ((MRB_DATA('FEED')[k && k.id] || []).length === 1\n"
     "        ? '1 shoutout' : (MRB_DATA('FEED')[k && k.id] || []).length +\n"
     "          ' shoutouts') + ' \u00b7 newest first',\n"
     "      feedNone: !(MRB_DATA('FEED')[k && k.id] || []).length,\n"
     "      feedEmptyLine: MRB_DATA('canWrite')\n"
     "        ? 'No shoutouts yet \u2014 the first one you send appears here.'\n"
     "        : 'No shoutouts were written for this class.',",
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

    # ⊕ Mide, 4 Sep 2026 — `showClassesLink`, the top bar's "My classes"
    # button (INSERT_AT[(10,13)]). ⚠️ WITHOUT THIS RETURN-OBJECT ENTRY THE
    # KEY IS INVISIBLE, even though `shared/teacher-live.js`'s `load()`
    # already returns it and `build_teacher_port.py`'s fixture payload
    # already carries it: `renderVals()` is the render SCOPE, an explicit
    # object literal, not a pass-through of `window.__MRB_DATA__` — a key
    # absent from here cannot be read by any `{"e":"..."}` in the template,
    # `if` nodes included, no matter how correct the underlying data is.
    # That is the exact shape `hasOtherYears`/`canWrite` just above already
    # solved, so this reuses their anchor rather than inventing a second one.
    ("      canWrite: MRB_DATA('canWrite'),\n",
     "      canWrite: MRB_DATA('canWrite'),\n"
     "      showClassesLink: MRB_DATA('showClassesLink'),\n",
     "the one key INSERT_AT[(10,13)]'s `if` reads. Anchored on `canWrite`'s "
     "own line rather than the `return {` head above: that head is this "
     "same MRB-287 E1 patch's own `to` text, and re-matching it would be a "
     "second ruling assuming a FROM only the first one's replacement ever "
     "produces — LOGIC applies in tuple order and each entry's `frm` must "
     "be unique in the source AT THAT POINT, so this one comes after."),

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
    # ⊕ RE-ANCHORED FOR DESIGN'S v3, 1 Sep 2026 (MRB-306) — AND IT NOW
    # RESTORES THE METHODS AS WELL AS THE HOOK. v3 deleted `openClass`,
    # `rail`, `snapWeekRail`, `pickWeek` and `weekIdxFor` outright along with
    # the rail they served. Mide's ruling of 1 Sep keeps the bar, so the four
    # methods come back — but `weekIdxFor` comes back RE-DERIVED, not copied.
    #
    # ⛔ v2's `weekIdxFor` CLAMPED TO `papersFor(k).length - 1`. One chip per
    # ASSIGNMENT. In Design's fiction one paper is one week so the two never
    # disagree; on the working year `8r/Sc1` has two assignments against a
    # thirty-nine-week year, and a copied-forward clamp would have pinned the
    # whole bar to two positions and called them the term. It clamps to
    # `weeks().length` now, and `weeks()` is the academic year's teaching
    # weeks — see the seam.
    #
    # ⚠️ THE ANCHOR IS THIS PORT'S OWN OUTPUT, ON PURPOSE. `CLASSES =
    # MRB_DATA('CLASSES')` is the first LOGIC ruling's result, so Design
    # cannot break this anchor by redrawing anything — which is precisely the
    # problem for a ruling that RESTORES code Design has deleted: there is no
    # span of hers left to name. A class body takes fields and methods in any
    # order, so they land here, immediately under the field, rather than in
    # the methods block below.
    #
    # ⚑ THE COLD LOAD. Seven URLs mean the class page is reached without any
    # screen-change handler ever running, so the rail's opening scroll
    # position has to come from the lifecycle instead. `setState` resets the
    # rail's `scrollLeft` to 0 — press a sort tab, open the search overlay,
    # dismiss a toast, and the rail is back on the oldest week — so it
    # re-snaps only when the rail is scrolled hard left AND has somewhere to
    # scroll, which is exactly the state a rebuild leaves behind. A teacher
    # who has scrolled the rail themselves and then presses something else
    # loses that scroll either way, because the element they scrolled no
    # longer exists. `student-runtime.js` defines both hooks as no-ops and
    # calls them, and Design defines neither, so there is nothing to shadow.
    (dict(key="CLASSES = MRB_DATA"),
     r"""CLASSES = MRB_DATA('CLASSES');

/* ── ⊕ MIDE, 1 Sep 2026 (MRB-306) · THE WEEK BAR, RESTORED ──────────
   Design's v3 deleted the class-detail week rail in favour of a dated
   assignment table; Mide overrode that and the bar stays. These are the
   four methods it needs, back from v2 — three of them verbatim, and
   `weekIdxFor` re-derived over WEEKS rather than over assignments.
   See `WEEK_BAR_RESTORED` in teacher_rulings.py. ── */
rail() { return document.querySelector('[data-rail="weeks"]'); }

/* The strip runs oldest to newest, so it opens parked on this week. */
snapWeekRail() {
  const snap = () => {
    const el = this.rail();
    if (!el) return;
    if (!this.state.weekIdx) { el.scrollLeft = el.scrollWidth; return; }
    const chip = el.querySelector('[data-week="' + this.state.weekIdx + '"]');
    if (chip) el.scrollLeft = Math.max(0, chip.offsetLeft - (el.clientWidth - chip.offsetWidth) / 2);
  };
  requestAnimationFrame(snap);
  setTimeout(snap, 90);
}

pickWeek(i) {
  this.setState({ weekIdx: i }, () => {
    const el = this.rail();
    if (!el) return;
    const chip = el.querySelector('[data-week="' + i + '"]');
    if (!chip) return;
    const left = chip.offsetLeft, right = left + chip.offsetWidth;
    if (left < el.scrollLeft + 8) el.scrollTo({ left: Math.max(0, left - 14), behavior: 'smooth' });
    else if (right > el.scrollLeft + el.clientWidth - 8) el.scrollTo({ left: right - el.clientWidth + 14, behavior: 'smooth' });
  });
}

/* ⚠️ WEEKS, NOT PAPERS. v2 clamped to `papersFor(k).length - 1`, which
   is one position per assignment. `weeks()` is the academic year's
   teaching weeks, newest first, at most twelve. */
weekIdxFor(k) {
  const n = this.weeks().length;
  if (!n) return 0;
  return Math.min(Math.max(0, this.state.weekIdx || 0), n - 1);
}

/* ⊕ MRB-287 — THE COLD LOAD. Six URLs mean the class page is reached
   without any screen-change handler running. See teacher_rulings. */
componentDidMount() { this.snapWeekRail(); }
componentDidUpdate() {
  const el = this.rail();
  if (el && !el.scrollLeft && el.scrollWidth > el.clientWidth) {
    this.snapWeekRail();
  }
}""",
     "the week rail's scroll position, on a page opened directly, and — "
     "since v3 deleted them — the four methods the rail is made of. "
     "Design's only caller was a screen-change handler and there are no "
     "screen changes any more. `weekIdxFor` is re-derived over weeks; the "
     "other three are v2 verbatim."),

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

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · A TEMPLATE CAN BE UNPICKED ═══════
    #
    # ⛔ WITHOUT THIS, "FREE TEXT ALONGSIDE THE TEMPLATES" CANNOT BE SENT.
    # Design's `pick` only ever SETS: `pick: () => this.setState({ boTpl:
    # t.id })`. There is no value of `boTpl` a teacher can reach that is
    # empty, and the port's own `state` ruling opens the composer with the
    # FIRST template already selected — which was right when the only
    # consumer was the bulk sheet, where a template is what you are sending.
    #
    # ⚠️ SO EVERY FREE-TEXT SHOUTOUT WOULD HAVE CARRIED A TEMPLATE NOBODY
    # CHOSE. Photographed before this ruling on `class-detail-fixture.html`:
    # the composer opens with "Top of the class this week" tinted, and a
    # teacher who ignores the templates and writes their own sentence about a
    # child sends `template_key='top_of_class'` with it. The child then reads
    # 🌟 Top of the class this week above words that say something else — and
    # `class_shoutouts_content_chk` is satisfied, so nothing anywhere
    # complains. Mide's ruling of 1 Sep 2026 is that a teacher may write
    # their OWN words; a template they cannot take off is that ruling not
    # being delivered.
    #
    # ⚠️ A TOGGLE, NOT A CLEARED DEFAULT. The default stays — `boTpl` is
    # shared with Design's bulk sheet, where opening with nothing selected
    # would be the "no template selected and no way to tell that from a bug"
    # state the `state` ruling records — and pressing the SELECTED template
    # unpicks it. Design's own tint is already the read-out: selected is
    # `--st-chip-tint` on `--st-accent-text`, unselected is paper, so the
    # toggle needs no new affordance and no new key.
    #
    # ⚠️ AND `sendBulk` GAINS THE GUARD THAT GOES WITH IT, below. Once a
    # template can be empty, `sendBulk` — which sends `message: null` — can
    # reach `insertClassShoutout` with neither, and
    # `class_shoutouts_content_chk` refuses the row. That would surface as
    # "the message is too long, or the template is not one this school uses",
    # which is true of neither. It is refused in front of the write instead.
    ("        pick: () => this.setState({ boTpl: t.id })",
     "        pick: () => this.setState({ boTpl: s.boTpl === t.id ? '' "
     ": t.id })",
     "the template quick-picks. Design's only ever SET, so with the port's "
     "first-template default there was no way to send a shoutout WITHOUT a "
     "template — and Mide's free-text ruling of 1 Sep 2026 requires one."),

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
     # ⊕ 3 Sep 2026 (Phase 2b) — NAMED, not bare. There are three
     # composing fields in this logic now (`recipient`, `note`, and the
     # bulk sheet's `bulk-note`) and a fourth on two other pages (the
     # feedback sheet's `feedback`). A bare reset clears whatever it
     # finds; naming its own two means this send can never empty
     # somebody else's half-written text, on this page or on a page
     # this handler is not even drawn on.
     "            MRB_COMPOSE_RESET(['recipient', 'note']);\n"
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
     # ⊕ 3 Sep 2026 — THE GUARD THAT COMES WITH THE UNPICKABLE TEMPLATE.
     # With neither a template nor a message there is nothing to send and
     # `class_shoutouts_content_chk` refuses every row — which would surface
     # as "the message is too long, or the template is not one this school
     # uses", true of neither. Refused in front of the write instead.
     #
     # ⊕ 3 Sep 2026 (Phase 2b) — AND THE MESSAGE IS ACTUALLY SENT NOW.
     # This block used to read `if (!s.boTpl) return this.ping('Pick a
     # template')` with a note saying the sheet's own textarea was NOT sent
     # and that saying so would be worse than staying silent. It was not
     # worse: a teacher typed a message, pressed send, and the words were
     # discarded with no error anywhere. `boNote` is the sheet's own state
     # key (see RETARGET_ON[651] for why it is not `s.note`), it is capped
     # at the database's own 500, and the sentence now names both ways of
     # having something to say.
     "        const bulkBody = String(s.boNote || '').trim();\n"
     "        if (!s.boTpl && !bulkBody) {\n"
     "          return this.ping('Pick a template, or write a message'); }\n"
     "        if (bulkBody.length > 500) {\n"
     "          return this.ping('Message too long — 500 characters at "
     "most'); }\n"
     "        this.ping('Sending to ' + ids.length + '…');\n"
     "        const cid = k && k.id;\n"
     "        MRB_SEND_SHOUTOUTS(cid, ids, s.boTpl, bulkBody || null)\n"
     "          .then((r) => {\n"
     "            if (!r.ok) {\n"
     "              return this.ping(MRB_SHOUTOUT_WHY(r.error)); }\n"
     "            if (r.fail) {\n"
     "              /* The sheet stays open and the selection stays put: "
     "some of\n"
     "                 these children were told and some were not, and the "
     "teacher\n"
     "                 is the only one who can decide what to do about "
     "it. */\n"
     "              return this.ping('Sent to ' + r.ok + ' of ' + "
     "ids.length +\n"
     "                ' — ' + MRB_SHOUTOUT_WHY(r.error)); }\n"
     # ⚠️ THE DOM FIELD IS EMPTIED BEFORE THE STATE, and BY NAME. Design's
     # textarea is uncontrolled and `student-runtime` carries field values
     # across a redraw on purpose, so clearing `boNote` alone leaves the
     # sent words on screen looking unsent. `['bulk-note']` and not a bare
     # reset: the single-student composer is UNDERNEATH this modal, and a
     # bulk send must not wipe a half-written shoutout about somebody else.
     "            MRB_COMPOSE_RESET(['bulk-note']);\n"
     "            MRB_REFRESH_FEED(cid).then(() => {\n"
     "              this.setState({ modal: null, boSel: [], boNote: '',\n"
     "                toast: 'Shoutout sent to ' + r.ok +\n"
     "                  (r.ok === 1 ? ' student' : ' students') });\n"
     "            });\n"
     "          });\n"
     "      },",
     "the bulk shoutout sheet. Same defect as the composer, N times over."),

    # ══ ⊕ 3 Sep 2026 (MRB-306 Phase 2b) · THE SHEET'S OWN NOTE HANDLER ══
    #
    # `setNote` stays exactly as Design wrote it and keeps writing `note` —
    # it is the single-student composer's field and three things read it.
    # This is its twin for the bulk sheet, added BESIDE it rather than
    # replacing it, and node 651 is moved onto it by `RETARGET_ON`.
    ("      setNote: (e) => this.setState({ note: e.target.value }),",
     "      setNote: (e) => this.setState({ note: e.target.value }),\n"
     "      setBulkNote: (e) => this.setState({ boNote: e.target.value }),",
     "the bulk sheet's own free-text handler. Design wires her sheet's "
     "textarea to the COMPOSER's `setNote`, so the two surfaces shared one "
     "state key and only one of them sent it."),

    # ⚠️ AND THE SUMMARY LINE HAS TO SAY SO. Design's reads "6 selected · Top
    # of the class this week", which was complete when a template was the
    # only thing being sent. Now that a message goes too, a line that names
    # only the template is the same silence in a smaller font — a teacher
    # would read it as confirmation that the words are not going.
    ("      bulkSummary: s.boSel.length + ' selected · ' + "
     "(this.TEMPLATES.filter(t => t.id === s.boTpl)[0] || "
     "{ label: 'no template' }).label,",
     "      bulkSummary: s.boSel.length + ' selected · ' +\n"
     "        (this.TEMPLATES.filter(t => t.id === s.boTpl)[0] ||\n"
     "          { label: 'no template' }).label +\n"
     "        (String(s.boNote || '').trim() ? ' · and your message' : ''),",
     "the bulk sheet's summary line. It named the template and never the "
     "message, which was accurate only while the message was being thrown "
     "away."),

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK — THE ROWS ═══════
    #
    # See `FEEDBACK_SURFACE_ADDED`. These three entries are the logic half of
    # `INSERT_AT`'s four markup entries; neither half is any use alone, and
    # the failure of shipping only one is silent in both directions — markup
    # with no keys renders an invisible control, keys with no markup are a
    # handler nothing calls.
    #
    # ⚠️ `MRB_FEEDBACK` READS THE PAYLOAD, IT DOES NOT FETCH. It is called
    # once per row of a thirty-child grid inside `renderVals`, which is
    # synchronous; `shared/teacher-live.js` does the reading, once, in
    # `load()`.
    ("      const stampS = stRow ? stRow.stampShort[i] : null;",
     "      const stampS = stRow ? stRow.stampShort[i] : null;\n"
     "      /* ⊕ MRB-306 Phase 2b — the submission this row is about, and\n"
     "         whatever has already been written on it. `subId` is null where\n"
     "         the child has not handed in: there is nothing to attach a\n"
     "         comment to, and the control is not drawn. */\n"
     "      const fbSub = stRow ? stRow.subId[i] : null;\n"
     "      const fbRow = MRB_FEEDBACK(fbSub);",
     "the student screen's history rows, given the submission id and the "
     "comment on it. Design's rows carry neither, because Design's delivery "
     "has no concept of a submission id and no feedback at all."),

    ("        stDotR: tone === 'warn' ? '1px' : '50%',",
     "        stDotR: tone === 'warn' ? '1px' : '50%',\n"
     "        fbCan: !!fbSub,\n"
     "        fbLabel: !fbRow ? 'Add feedback'\n"
     "          : (fbRow.mine ? 'Edit feedback' : 'Read feedback'),\n"
     "        fbFg: fbRow ? 'var(--st-accent-text)' : 'var(--st-muted)',\n"
     "        fbAria: (!fbRow ? 'Add feedback on '\n"
     "          : (fbRow.mine ? 'Edit your feedback on '\n"
     "            : 'Read the feedback on ')) + p.title +\n"
     "          ' for ' + (st ? st.name : 'this student'),\n"
     "        /* ⚠️ `stopPropagation` FIRST. Design's whole row (361) carries\n"
     "           `h.open` and navigates to the marking screen, so without\n"
     "           this the press would open the sheet and leave the page it\n"
     "           opened on in the same gesture. */\n"
     "        openFb: (e) => {\n"
     "          if (e && e.stopPropagation) { e.stopPropagation(); }\n"
     "          if (e && e.preventDefault) { e.preventDefault(); }\n"
     "          const had = (fbRow && fbRow.body) || '';\n"
     "          this.setState({ fbSub: fbSub, fbName: st ? st.name : '',\n"
     "            fbPaper: p.title, fbBody: had,\n"
     "            fbErr: '', fbConfirm: false },\n"
     "            () => MRB_FB_FILL(had));\n"
     "        },",
     "the student screen's feedback control, per history row. Mide's ruling "
     "of 3 Sep 2026: feedback is authored from student detail or from "
     "marking, attached to that submission."),

    # ⚠️ THE SAME KEYS ON THE MARKING GRID, and it is deliberately the same
    # NAMES rather than a second vocabulary: the markup that reads them is
    # one builder (`_fb_open_button`) taking the row alias, so two spellings
    # would mean two subtrees and the two screens drifting apart.
    ("      cells: r.raw.map(v => this.cellStyle(v)),\n"
     "      score: r.score,",
     "      cells: r.raw.map(v => this.cellStyle(v)),\n"
     "      score: r.score,\n"
     "      fbCan: !!r.subId,\n"
     "      fbLabel: !MRB_FEEDBACK(r.subId) ? 'Add feedback'\n"
     "        : (MRB_FEEDBACK(r.subId).mine ? 'Edit feedback'\n"
     "          : 'Read feedback'),\n"
     "      fbFg: MRB_FEEDBACK(r.subId) ? 'var(--st-accent-text)'\n"
     "        : 'var(--st-ghost)',\n"
     # The glyph is FILLED where a comment exists and hollow where it does
     # not, so "who has been written to" is scannable down a thirty-child
     # column. `none` and not `transparent`: an SVG fill of `none` is no
     # paint at all, which is what a hollow speech mark is.
     "      fbFill: MRB_FEEDBACK(r.subId) ? 'currentColor' : 'none',\n"
     "      fbAria: (!MRB_FEEDBACK(r.subId) ? 'Add feedback for '\n"
     "        : (MRB_FEEDBACK(r.subId).mine ? 'Edit your feedback for '\n"
     "          : 'Read the feedback for ')) + r.name,\n"
     "      openFb: (e) => {\n"
     "        if (e && e.stopPropagation) { e.stopPropagation(); }\n"
     "        if (e && e.preventDefault) { e.preventDefault(); }\n"
     "        const row = MRB_FEEDBACK(r.subId);\n"
     "        const had = (row && row.body) || '';\n"
     "        this.setState({ fbSub: r.subId, fbName: r.name,\n"
     "          fbPaper: pp ? pp.title : '', fbBody: had,\n"
     "          fbErr: '', fbConfirm: false },\n"
     "          () => MRB_FB_FILL(had));\n"
     "      },",
     "the marking screen's feedback control, per grid row — the second of "
     "Mide's two authoring surfaces. The grid row already carries `subId` "
     "from `buildGrid`; Design's carries a student id and a mark and "
     "nothing that identifies the submission."),

    # ══ ⊕ RULED BY MIDE, 3 Sep 2026 · WRITTEN FEEDBACK — THE SHEET ══════
    #
    # ⚠️ EVERY KEY BELOW IS READ BY AN `<if>` OR AN INTERPOLATION IN
    # `_fb_sheet()`, and `student-runtime` evaluates an `<if>` with `lookup(…,
    # null)` — WITHOUT the miss recorder — so a key that does not exist is
    # not an error, it is silently FALSE. A typo here takes the sheet off both
    # screens with every gate green and nothing in the console. They are
    # driven rather than trusted; see the report.
    #
    # ⚠️ `canWrite` IS READ THROUGH `MRB_DATA`, NOT AS A BARE NAME, for the
    # reason `f.canDelete` records: inside `renderVals` there is no local
    # called `canWrite` — the renderVals KEY of that name is not in scope
    # while the object is still being built — so a bare reference is
    # `undefined`, which is falsy, which would silently take the composing
    # half of this sheet off every screen including the ones that can write.
    #
    # ⚠️ AND THE READING HALF IS NOT GATED ON IT. MRB-261 makes a finished
    # year READ-ONLY, not invisible: what was written about a child last year
    # is still readable, and only Save and Remove go.
    ("      backToClass: 'Back to ' + k.code,",
     "      backToClass: 'Back to ' + k.code,\n"
     "\n"
     "      /* ── ⊕ MRB-306 Phase 2b · the feedback sheet ──────────────── */\n"
     "      fbOpen: !!s.fbSub,\n"
     "      fbKicker: k.code + ' \\u00b7 Feedback',\n"
     "      fbTitle: 'Feedback for ' + (s.fbName || 'this student'),\n"
     "      fbOn: s.fbPaper ? 'On ' + s.fbPaper : 'On this submission',\n"
     "      fbBody: s.fbBody || '',\n"
     "      fbErr: s.fbErr || '',\n"
     "      /* ATTRIBUTED, in the only terms a teacher session can prove.\n"
     "         `buildFeedback` records why this is \"You\" / \"Another\n"
     "         teacher\" and not a name: a teacher has no read policy on\n"
     "         another teacher's profile row, so a name would either be an\n"
     "         em dash (which reads as a bug) or a guess. */\n"
     "      fbByLine: (function () {\n"
     "        const r = MRB_FEEDBACK(s.fbSub);\n"
     "        if (!r) { return ''; }\n"
     "        return r.by + ' \\u00b7 ' + r.when +\n"
     "          (r.edited ? ' \\u00b7 edited ' + r.editedWhen : '');\n"
     "      })(),\n"
     "      /* ⛔ THE WORDS, WHENEVER THERE IS NO EDITOR FOR THEM — a\n"
     "         colleague's comment (RLS: `submission_feedback_update` is\n"
     "         `teacher_id = auth.uid()`, so offering an editor would be\n"
     "         offering a refusal) OR this teacher's own on a FINISHED year.\n"
     "         ⚠️ IT USED TO READ `!mine` ALONE, and a read-only drive found\n"
     "         what that cost: on a past year a teacher opened their own\n"
     "         comment and saw the byline with no text under it. MRB-261 is\n"
     "         read-only, not invisible. */\n"
     "      fbReadBody: !!(MRB_FEEDBACK(s.fbSub) &&\n"
     "        (!MRB_FEEDBACK(s.fbSub).mine || !MRB_DATA('canWrite'))),\n"
     "      fbBodyText: (MRB_FEEDBACK(s.fbSub) &&\n"
     "        (!MRB_FEEDBACK(s.fbSub).mine || !MRB_DATA('canWrite')))\n"
     "        ? MRB_FEEDBACK(s.fbSub).body : '',\n"
     "      fbCanEdit: !!(MRB_DATA('canWrite') &&\n"
     "        (!MRB_FEEDBACK(s.fbSub) || MRB_FEEDBACK(s.fbSub).mine)),\n"
     "      fbCanRemove: !!(MRB_DATA('canWrite') && MRB_FEEDBACK(s.fbSub) &&\n"
     "        MRB_FEEDBACK(s.fbSub).mine),\n"
     "      fbFieldCap: MRB_FEEDBACK(s.fbSub) ? 'Your feedback'\n"
     "        : 'Write feedback',\n"
     "      fbSaveLabel: MRB_FEEDBACK(s.fbSub) ? 'Save changes'\n"
     "        : 'Save feedback',\n"
     "      /* TWO PRESSES. The first says what the second will do; nothing\n"
     "         is written until the second. There is no undo — there is no\n"
     "         UPDATE path anywhere in this codebase that clears\n"
     "         `deleted_at` — so the label says so rather than a dialog\n"
     "         saying it on top of a dialog. */\n"
     "      fbRemoveLabel: s.fbConfirm\n"
     "        ? 'Remove it \\u2014 this cannot be undone' : 'Remove',\n"
     "      /* ⛔ THE ONE-WAY GUARDRAIL, IN WORDS, TO THE PERSON WRITING.\n"
     "         There is no reply control anywhere on the student side and\n"
     "         there is no student INSERT policy on the table, so a child\n"
     "         cannot answer this — and the teacher composing it is the one\n"
     "         who needs to know that before they phrase a question. */\n"
     "      fbFootNote: MRB_DATA('canWrite')\n"
     "        ? 'They read this under their marking. They cannot reply.'\n"
     "        : 'This year is read-only.',\n"
     "      closeFeedback: () => this.setState({ fbSub: null, fbBody: '',\n"
     "        fbErr: '', fbConfirm: false }),\n"
     "      setFbBody: (e) => this.setState({ fbBody: e.target.value,\n"
     "        fbErr: '' }),\n"
     "      /* INSERT where there is nothing yet, UPDATE where there is — and\n"
     "         the UPDATE carries the body it replaces, because the database\n"
     "         refuses an edit that does not\n"
     "         (`(edited_at IS NULL) = (prior_body IS NULL)`). Retention is\n"
     "         not remembered here; it is unavoidable. */\n"
     "      saveFeedback: () => {\n"
     "        const sub = s.fbSub;\n"
     "        const row = MRB_FEEDBACK(sub);\n"
     "        const body = String(s.fbBody || '').trim();\n"
     "        if (!sub) { return; }\n"
     "        if (!body) {\n"
     "          return this.setState({ fbErr: 'Write something first.' }); }\n"
     "        if (body.length > MRB_FB_MAX()) {\n"
     "          return this.setState({ fbErr: 'Too long \\u2014 ' +\n"
     "            MRB_FB_MAX() + ' characters at most.' }); }\n"
     # ⚠️ AN UNCHANGED SAVE WRITES NOTHING, AND THAT IS ABOUT THE CHILD.
     # An UPDATE stamps `edited_at`, and the student's own read renders
     # "· EDITED" from it — so a teacher who opens their comment, changes
     # their mind, and presses Save anyway would tell a child their
     # feedback had been rewritten when not one character moved. It closes
     # instead, and says so.
     "        if (row && body === String(row.body || '')) {\n"
     "          return this.setState({ fbSub: null, fbBody: '', fbErr: '',\n"
     "            fbConfirm: false, toast: 'No change' }); }\n"
     "        this.ping('Saving\\u2026');\n"
     "        MRB_SAVE_FEEDBACK(sub, body, row).then((res) => {\n"
     "          if (!res.ok) {\n"
     "            const why = MRB_FEEDBACK_WHY(res.error);\n"
     "            this.setState({ fbErr: why });\n"
     "            return this.ping(why);\n"
     "          }\n"
     "          MRB_REFRESH_FEEDBACK(s.screen, { classId: s.classId,\n"
     "            studentId: s.studentId, paperIdx: s.paperIdx }).then(() => {\n"
     "            this.setState({ fbSub: null, fbBody: '', fbErr: '',\n"
     "              fbConfirm: false,\n"
     "              toast: row ? 'Feedback updated' : 'Feedback saved' });\n"
     "          });\n"
     "        });\n"
     "      },\n"
     "      removeFeedback: () => {\n"
     "        const row = MRB_FEEDBACK(s.fbSub);\n"
     "        if (!row || !row.id) { return; }\n"
     "        if (!s.fbConfirm) { return this.setState({ fbConfirm: true }); }\n"
     "        this.ping('Removing\\u2026');\n"
     "        MRB_REMOVE_FEEDBACK(row.id).then((res) => {\n"
     "          if (!res.ok) {\n"
     "            const why = MRB_FEEDBACK_WHY(res.error);\n"
     "            this.setState({ fbErr: why, fbConfirm: false });\n"
     "            return this.ping(why);\n"
     "          }\n"
     "          MRB_REFRESH_FEEDBACK(s.screen, { classId: s.classId,\n"
     "            studentId: s.studentId, paperIdx: s.paperIdx }).then(() => {\n"
     "            this.setState({ fbSub: null, fbBody: '', fbErr: '',\n"
     "              fbConfirm: false, toast: 'Feedback removed' });\n"
     "          });\n"
     "        });\n"
     "      },",
     "the feedback sheet's keys and its four handlers. Design drew no "
     "feedback surface at all, so there is no handler of hers being "
     "replaced here — this is an addition, ruled by Mide on 3 Sep 2026 and "
     "registered in FEEDBACK_SURFACE_ADDED and AMENDED_ADDITIONS."),


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
     ": null;\n"
     "    /* ⊕ MRB-306 screen 6 — the two figures the tiles used to derive\n"
     "       for themselves, derived ONCE here instead. `dgMeans` is the\n"
     "       live classes that actually HAVE a class mean; `dgFlagged` is\n"
     "       summed off `digestRows`, so the tile cannot count a child the\n"
     "       table below it does not. */\n"
     "    const dgMeans = liveClasses.map(c => this.meanOf(c))\n"
     "                               .filter(m => m != null);\n"
     "    const dgFlagged = digestRows.reduce((a, d) => a + d.flagN, 0);",
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
     "        note: (src.length > 1 && worst && worst.tot) ? 'Weakest: ' + "
     "worst.label + ' at ' + Math.round((worst.on / worst.tot) * 100) + "
     "'% on time' : '' };",
     "the on-time chart's caption. With no recorded deadlines anywhere it "
     "named a class and said it was at 0% on time.\n"
     "\n"
     "        ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 7) — AND ON ONE ROW IT "
     "NAMED THE ONLY CLASS IN THE SCHOOL \"Weakest\", at 100% on time. The "
     "arithmetic is real and the superlative is a ranking with one entrant; "
     "photographed on `insights-single`. The guard is `src.length > 1`, the "
     "same correction the Highest/Lowest and Strongest/Weakest pairs take "
     "two rulings above. Amended in place rather than added below, because "
     "`LOGIC` applies IN ORDER and a second ruling on this line would have "
     "had to anchor on this one's output."),

    # ══ the Set-work sheet's leftovers ══════════════════════════════════
    #
    # ⊕ 1 Sep 2026 (MRB-306) — THE THREE STATEMENTS ARE UNCHANGED IN v3 AND
    # THE `frm` STILL DIED, on two trailing blank lines that became one. Left
    # on `frm` deliberately: three complete statements naming three locals is
    # self-identifying text, not disambiguation padding, and converting a
    # ruling that works is risk with no reward. What is trimmed is the blank
    # line — Design's whitespace was never part of the ruling.
    ("""    const swSel = s.swClasses;
    const swStudents = this.CLASSES.filter(c => swSel.indexOf(c.id) > -1).reduce((a, c) => a + c.n, 0);
    const topic = this.TOPICS.filter(t => t.id === s.swTopic)[0] || this.TOPICS[0];
""",
     "",
     "three locals only the Set-work keys read. `topic` reads `this.TOPICS`, "
     "which is deleted, so this is not tidying — left in place it throws at "
     "mount on all seven pages. "
     "⊕ 1 Sep 2026 (MRB-306) — the trailing blank line came out of `frm`; "
     "v3 leaves one blank line here where v2 left two, and the statements "
     "themselves never changed."),

    ("      sw1: s.swStep === 1, sw2: s.swStep === 2, sw3: s.swStep === 3,\n",
     "",
     "`sw2` and `sw3`, on the same physical line as `sw1`, so `DROP_KEYS` — "
     "which works one balanced key at a time — cannot take them."),

    # ══ ⊕ MRB-304 · the handler the brand mark moves ONTO ════════════════
    #
    # ⚠️ THE ANCHOR IS `NAV`'s OUTPUT, NOT DESIGN'S SOURCE, AND THAT IS
    # DELIBERATE RATHER THAN INCIDENTAL. `seam_logic` runs `NAV` first and
    # `LOGIC` second — it says so, and the order is already load-bearing for
    # three other entries. Anchoring on the REWRITTEN line means this ruling
    # cannot land unless the navigation rewire it sits beside landed first:
    # if `NAV["goClasses"]` is ever re-anchored or removed, this refuses on
    # "appears 0 times" instead of quietly defining a method beside a handler
    # that no longer exists.
    #
    # ⚠️ IT IS A SIBLING KEY IN `renderVals`, WHICH IS WHERE IT HAS TO BE.
    # `student-runtime` resolves a node's `on` against the object `renderVals`
    # returns — that is the page's whole render scope — so a method defined
    # anywhere else on the class would be looked up, missed, and recorded in
    # `data-mrb-misses` as a control wired to nothing.
    #
    # `MRB_HOME` is one line in the seam (`build_teacher_port._SEAM`) and not
    # an inline `window.location.href` here, for the reason every other
    # navigation in this port goes through a named helper: `teacher_behaviour`
    # STUBS the helpers so a swept press computes its destination without
    # tearing the page down mid-sweep. An inline assignment would navigate the
    # gate's browser away from the fixture on the first press of the brand.
    ("      goClasses: () => MRB_GO('classes', "
     "{ year: MRB_DATA('yearParam') }),",
     "      goClasses: () => MRB_GO('classes', "
     "{ year: MRB_DATA('yearParam') }),\n"
     "      goHome: () => MRB_HOME(),",
     "`goHome` — the public homepage, which is where the MrBadmusAI wordmark "
     "goes from every teacher page (Mide, 31 Aug 2026). Defined next to the "
     "handler node 11 has just stopped calling, so the pair reads as one "
     "decision. See `RETARGET_ON`."),

    # ══ MRB-306 — #11, PARTS 2 AND 3 ════════════════════════════════════
    #
    # The other two nodes of the student's assignment-history ruling. They
    # belong beside #11 and they are HERE, at the bottom, for one reason: the
    # week-rail unit that follows this one names LOGIC entries by index, and
    # inserting two entries in the middle would renumber every ruling after
    # them without a word of warning. Appending renumbers nothing.
    #
    # Order is safe: both anchor inside `const stHistory`, which no earlier
    # ruling removes, and neither touches a line another entry is looking for.
    (dict(builder="stHistory", key="submitted"),
     "        submitted: open ? (sc != null ? st.last : 'Not yet') "
     ": (stampS || '—'),",
     "the SUBMITTED column, and it is the worst line in Design's file. It "
     "renders `p.dueShort` when the work was on time and `p.lateShort` when "
     "it was late — the DEADLINE and the END OF THE WEEK. Neither is when "
     "anybody submitted anything, and on a parents' evening it would be "
     "quoted. `stampShort[]` is `completed_at` or `submitted_at` formatted, "
     "blank where there is none. "
     "⊕ 1 Sep 2026 (MRB-306) — split out of #11's ten-line `frm` onto its "
     "own anchor; the ruling is unchanged."),

    (dict(builder="stHistory", key="score"),
     "        score: open || sc == null || stRow.max[i] == null ? '—'\n"
     "          : sc + '/' + stRow.max[i] "
     "+ (pct == null ? '' : ' · ' + pct + '%'),",
     "the SCORE column's `/8`. Design's every paper is out of eight; a real "
     "one is out of `max[]`, and a paper whose max is unknown says so rather "
     "than dividing by a number nobody set. "
     "⊕ 1 Sep 2026 (MRB-306) — split out of #11's ten-line `frm` onto its "
     "own anchor; the ruling is unchanged."),

    # ══ MRB-306 · THE WEEK BAR — THE REST OF #6 AND #13 ═════════════════
    #
    # Appended rather than inserted, for the reason the block above gives:
    # LOGIC entries are named by INDEX in every brief written about this
    # port, and inserting in the middle renumbers everything after it in
    # silence. #6 owns the roster row's `week`; #13 owns the week scope
    # itself. Everything those two corrections reach — and there is more of
    # it in v3 than there was in v2, because v3 spread the four tiles across
    # a `glance` block, a `statLine` and an assignments table — lands here.
    #
    # ⚠️ ORDER IS SAFE AND WAS CHECKED, NOT ASSUMED. Every entry below
    # anchors on a line that no earlier ruling removes or rewrites, and none
    # of them contains a span another entry is still looking for.

    # ── the roster row's other two properties ───────────────────────────
    #
    # Design writes these as a binary over `r.inWeek`. Under the bar they are
    # the SELECTED week, and a week nobody was asked anything in reads as the
    # neutral ghost rather than as the accent that means "chase this child".
    (dict(builder="roster", key="weekFg"),
     """      weekFg: (!kPapers.length || !wTally[r.id].asked) ? 'var(--st-ghost)'
        : (wTally[r.id].in >= wTally[r.id].asked
          ? 'var(--st-ink)' : 'var(--st-accent-text)'),""",
     "the roster row's week colour, on the selected week. Part of #6."),

    (dict(builder="roster", key="dot"),
     """      dot: (!kPapers.length || !wTally[r.id].asked) ? 'var(--st-rule-strong)'
        : ((wTally[r.id].in >= wTally[r.id].asked && wTally[r.id].late !== true)
          ? 'var(--ks3-ok)' : 'var(--st-accent)'),""",
     "the roster row's week dot, on the selected week. ⚠️ A LATE SUBMISSION IS NOT GREEN: v3 paints the dot from `inWeek` alone, so a child who handed in a week after the deadline got the same green as one who was on time — the row's own words say \"In · late\" beside it. Part of #6."),

    # ── the id the shoutout composer writes ─────────────────────────────
    #
    # ⊕ 24 Aug 2026, and it is the half of #6 that a property anchor cannot
    # carry: `id` is a different property from `week`, so it is a different
    # entry. The composer's `<select>` is built from this list and its option
    # values have to be the child's real id rather than their name —
    # `insertClassShoutout` writes `recipient_id`, RLS checks the recipient is
    # an active member of this class, and two children in one class can share
    # a name. See `BIND_ATTR` 190.
    (dict(builder="roster", key="name"),
     """      id: r.id,
      name: r.name,""",
     "the roster row's `id`, for the shoutout composer. Part of #6."),

    # ── ⚑ THE TWO CONSUMERS OF `r.inWeek` THE WEEK BAR MISSED ───────────
    #
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 2). The week-bar unit ruled that
    # `r.inWeek` is "hard-wired to the current week window" and re-derived
    # the roster row's `week`, `weekFg` and `dot` off `wTally` — the
    # per-child, per-SELECTED-week count built beside the week scope. It
    # left two OTHER readers of the same flag on this screen, and both are
    # visible defects on any week but the current one. FOUND BY DRIVING, not
    # by reading: every gate on this page was green with both in place.
    #
    # ⚠️ WHAT A TEACHER ACTUALLY SAW, on `class-detail-fixture.html`, with
    # the numbers beside the names:
    #
    #   week 0  (24–28 Aug)  card "11 of 16 in"  chips: Jasmine, Kaleb,
    #                        Leila, Marcus, Nia          — 5 names, correct
    #   week 1  (17–21 Aug)  card "13 of 16 in"  chips: THE SAME FIVE
    #                        roster column says: Chidi, Hana, Idris
    #   week 11 (8–12 Jun)   card "10 of 16 in"  chips: THE SAME FIVE
    #                        roster column says: Jasmine, Kaleb, Marcus,
    #                        Clara, Amara, Farida
    #
    # So on every week but the open one the chase chips CONTRADICT both the
    # count printed directly above them and the roster table printed
    # directly below them, and they name children who did hand the work in.
    # Leila and Nia are chased in week 11 having submitted; Chidi, Hana and
    # Idris are the three who actually owe week 1 and are never named. This
    # is not a cosmetic mismatch — the chips are a chase list, each one is a
    # link into that child's record, and `kChase.length` is what "Remind all
    # N" counts.
    #
    # ⚠️ AND IT IS WHY THE REMINDER CONTROL MUST NOT BE WIRED TO `kChase` AS
    # DESIGN WROTE IT. See DEAD's note on node 236: the working control is
    # the one `shared/teacher-live.js` injects, and it computes its own
    # chase from `papers[0]` — the open week — so it was never exposed to
    # this. Wiring Design's node to `kChase` before this correction would
    # have sent real reminders to the wrong children.
    (dict(method="renderVals", key="const kChase"),
     """    const kChase = (!k || k.state !== 'live' || !wIdxs.length) ? []
      : kRoster.filter(r => wTally[r.id].in < wTally[r.id].asked);""",
     "the class screen's chase list, on the SELECTED week rather than on "
     "`r.inWeek`. `chaseFor()` itself is left alone — the classes screen "
     "calls it too, and there the current week is the right question. Part "
     "of #13."),

    # ⚠️ "NOT SUBMITTED FIRST" HAS TO MEAN THE WEEK BEING LOOKED AT. The
    # sort read `r.inWeek` as well, so on any earlier week the children
    # floated to the top of the table were the ones behind on THIS week's
    # work while the rows actually reading "Not in yet" sat wherever the
    # roster happened to put them. Driving week 1 showed the first row as
    # "In · on time" with all three genuinely-missing children further down.
    #
    # ⚠️ A WEEK NOBODY WAS ASKED ANYTHING IN MUST NOT SORT EVERYONE TO THE
    # TOP, which is why `asked` is tested and not just `in`. That is the
    # same care the `week` property's ruling states: the column reads
    # "Nothing set", not "Not in yet", and the sort has to agree with it or
    # the table is ordered by an accusation the data does not support.
    (dict(method="renderVals", key="const rosterWeight"),
     """    const rosterWeight = (r) => ((wTally[r.id] && wTally[r.id].asked
      && wTally[r.id].in < wTally[r.id].asked) ? 2 : 0) + (r.flag ? 1 : 0);""",
     "the roster sort, on the SELECTED week rather than on `r.inWeek`. Part "
     "of #6 and #13."),

    # ── "the last marked set" stops meaning "the second paper" ──────────
    #
    # ⛔ `kPapers[1]` IS THE ONE-OPEN-PAPER-AT-INDEX-0 ASSUMPTION, and it is
    # the same defect `paper()` was corrected for in METHODS: index 1 is the
    # newest marked paper only when exactly one paper is open, which is a
    # property of Design's sample. A real class has none open, or three. The
    # matrix already publishes `markedIdx` — which columns have closed,
    # newest first — so the answer exists and does not have to be guessed.
    # ⊕ EXTENDED 2 Sep 2026 (MRB-306 Phase 2a screen 2) — AND SOMEBODY HAS
    # TO HAVE SAT IT.
    #
    # ⚠️ `markedIdx` IS NOT "PAPERS THAT WERE MARKED". It is papers whose
    # DEADLINE HAS PASSED — `buildPapers` sets `when = 'marked'` on
    # `due_at <= now` and consults no submission at all — so a paper closes
    # on time whether sixteen children sat it or none did. On the `nosubs`
    # fixture (a live class, work set, nobody in) that produced a card
    # reading:
    #
    #     RETEACH FROM THE LAST SET
    #     Energy stores and transfers
    #     Marked · class mean — · 0/16 submitted
    #
    # with an empty body under it and a live "Open the full breakdown" link.
    # A teacher is told to reteach a topic on the evidence of a paper NOBODY
    # SAT, and the evidence panel is blank because there is none. That is a
    # recommendation manufactured out of an empty column, and a deadline
    # passing with nothing handed in is an ordinary week, not an edge case.
    #
    # So the newest CLOSED paper somebody actually sat is the one there is
    # anything to reteach from. `colSub[i] > 0` is the same submitted count
    # the card itself prints, so the card and its own subtitle cannot
    # disagree.
    #
    # ⚠️ FOUND BY THE THIRTEENTH FIXTURE ON ITS FIRST RUN, and unreachable
    # without it: the populated fixture has marked papers with submissions,
    # and the no-roster fixture has no papers. Neither could express "closed,
    # and empty".
    ("    const lastP = kPapers[1] || null;",
     "    const lastMarked = kMx.markedIdx.filter(i => (kMx.colSub[i] || 0) > 0);\n"
     "    const lastP = lastMarked.length "
     "? (kPapers[lastMarked[0]] || null) : null;",
     "the class screen's \"last marked set\". Part of #13: `kPapers[1]` is "
     "the index-0 assumption, and `markedIdx` is the seam's own answer to "
     "the same question — narrowed to the closed papers somebody actually "
     "sat, because `markedIdx` is a deadline test and not a submission "
     "one."),

    # ⚠️ AND THE CARD NEEDS WORDS FOR THAT STATE. `lastTitle` fell back to a
    # bare em-dash, which under the heading "Reteach from the last set" reads
    # as a value that failed to load rather than as an answer. `openTitle`
    # three lines above already solves the identical problem with a sentence
    # ("No work set in this week"), so this is that pattern applied to its
    # neighbour rather than a new one.
    (dict(method="renderVals", key="lastTitle"),
     """      lastTitle: lastP ? lastP.title : 'Nothing marked yet',""",
     "the reteach card's empty state. A class whose closed papers nobody sat "
     "has nothing to reteach FROM, and must say so rather than render a "
     "dash. Part of #13."),

    ("    const g1 = lastP ? this.gridFor(k, 1) : null;",
     "    const g1 = lastP ? this.gridFor(k, lastP.idx) : null;",
     "the grid behind \"Worth a reteach\". Design asks for the grid of paper "
     "1 rather than the grid of the paper it has just resolved, so on a "
     "class whose newest marked set is anywhere else it reteaches the wrong "
     "assignment. Part of #13."),

    ("    const worstTwo = g1 ? this.STEMS.map((q, qi) => ({ id: q.id, "
     "text: q.text, pct: g1.qpct[qi] })).sort((a, b) => a.pct - b.pct)"
     ".slice(0, 2) : [];",
     "    const worstTwo = g1 ? g1.stems.map((q, qi) => ({ id: q.id, "
     "text: q.text, pct: g1.qpct[qi] })).filter(q => q.pct != null)"
     ".sort((a, b) => a.pct - b.pct).slice(0, 2) : [];",
     "the two weakest questions. `this.STEMS` is DELETED by DROP_FIELDS — "
     "eight invented stems for every paper in every subject — so this line "
     "throws the moment a grid is present; and `qpct[i]` is null where "
     "nothing at that question was machine-marked, which sorts below a real "
     "0%. Same correction as #7, one screen along. Part of #13."),

    # ── `glance`, scoped to the selected week ───────────────────────────
    #
    # This is where the four tiles' defects went. `openIn` is
    # `colSub[0] + ' of ' + k.n` — the roster as a denominator, the first
    # thing #13 was written about — and `openPct` divides by `k.n` too.
    # `colAsked` is who the paper actually went to; both numbers are true and
    # neither can render "31 of 29".
    (dict(method="renderVals", key="openTitle"),
     """      openTitle: openP
        ? (wPapers.length > 1
          ? openP.title + ' · +' + (wPapers.length - 1) + ' more'
          : openP.title)
        : 'No work set in this week',""",
     "the week's assignment. ⚠️ A WEEK WITH NO ASSIGNMENT IS A REAL STATE "
     "AND DESIGN NEVER DREW IT — its rail could not produce one, because its "
     "rail was made of assignments. It says so in words rather than showing "
     "an em dash, which reads as a missing figure. Part of #13."),

    (dict(method="renderVals", key="openDue"),
     "      openDue: openP && openP.due "
     "? openP.due.replace(/^Due /, '') : '',",
     "the week's due date, blank when the assignment has no deadline. "
     "Design's `.replace('Due ', '')` strips the prefix anywhere in the "
     "string; anchored to the front, which is where it is written. "
     "Part of #13."),

    (dict(method="renderVals", key="openIn"),
     "      openIn: wPapers.length ? wSub + ' of ' + wAsk + ' in' : '—',",
     "\"N of M in\", over the week and over `colAsked`. Part of #13: the "
     "roster as a denominator is the defect this ruling has always been "
     "about, and v3 moved it here from the tiles."),

    (dict(method="renderVals", key="openPct"),
     "      openPct: wAsk ? Math.round((wSub / wAsk) * 100) : 0,",
     "the bar under it, over the same denominator. Part of #13."),

    # ── the assignment table, scoped to the week ────────────────────────
    #
    # Mide's ruling: picking a week "re-scopes the tiles, the roster column
    # and the assignment tables". The end chips are buckets — see #13 — so
    # nothing a teacher has set ever becomes unreachable.
    ("    const assignments = kPapers.map(p => {",
     "    const assignments = wPapers.map(p => {",
     "the assignment table, scoped to the selected teaching week. Mide, "
     "1 Sep 2026. Part of #13."),

    # ── ⛔ AND THIS ONE IS A LIVE CRASH, NOT A WEEK-BAR CHANGE ───────────
    #
    # `gridFor` RETURNS NULL FOR A GRID THAT HAS NOT BEEN FETCHED, which is
    # the documented contract in METHODS, and `teacher-live.js` prefetches NO
    # grids for the class screen. So `g.qpct` on the line below is a
    # TypeError on any class with a marked assignment — which is `8r/Sc1`,
    # the only class in the working year that has any assignments at all.
    # This is v3-new (v2 had no weak column here) and no ruling covered it;
    # found while scoping the table to a week, fixed here because the week
    # bar puts that paper on the screen.
    #
    # `this.STEMS` is the second half: it is DELETED by DROP_FIELDS, so even
    # with a grid present the line throws. The grid carries its own stems.
    # And `qpct[i]` is null where nothing at that question was machine-marked
    # — `Math.min` over an array containing null returns 0, which would name
    # a question as the class's weakest at 0% on the strength of no marks at
    # all.
    ("""      let weak = '—', weakFg = 'var(--st-ghost)';
      if (markedRow) {
        const g = this.gridFor(k, p.idx);
        const min = Math.min.apply(null, g.qpct);
        const qi = g.qpct.indexOf(min);
        weak = this.STEMS[qi].id + ' · ' + min + '%';
        weakFg = min < 50 ? 'var(--st-accent-text)' : 'var(--st-muted)';
      }""",
     """      let weak = '—', weakFg = 'var(--st-ghost)';
      const wkG = markedRow ? this.gridFor(k, p.idx) : null;
      const wkPct = (wkG && wkG.qpct) ? wkG.qpct : [];
      let wkMin = null, wkAt = -1;
      wkPct.forEach((v, qi) => {
        if (v != null && (wkMin == null || v < wkMin)) { wkMin = v; wkAt = qi; }
      });
      if (wkMin != null) {
        const wkStem = (wkG.stems || [])[wkAt];
        weak = ((wkStem && wkStem.id) || ('Q' + (wkAt + 1))) + ' · ' + wkMin + '%';
        weakFg = wkMin < 50 ? 'var(--st-accent-text)' : 'var(--st-muted)';
      }""",
     "the assignment table's weakest-question column. A null grid and a "
     "deleted `STEMS` are two separate throws on the one class that has "
     "work set; a null `qpct` entry is a third wrong answer that does not "
     "throw. See the block comment."),

    # ── ⛔ AND THE SAME THREE THROWS AGAIN, IN `weakFor` ─────────────────
    #
    # v3-new, and worse than the one above because `renderVals` builds
    # `reteachRows` UNCONDITIONALLY on every screen: `weakFor` is called for
    # every live class on all six pages, so this is a mount-time TypeError on
    # a real teacher's dashboard, not just on class detail. Found by driving
    # the seamed logic over `8r/Sc1`'s real shape — it threw before it
    # reached the week bar.
    #
    #   · `gridFor(k, 1)` is the index-0 assumption AND an unfetched grid.
    #     The class, Today and insights screens prefetch no grids at all
    #     (`teacher-live.js` prefetches only for `marking` and for the
    #     questions chart), so `g` is null every time.
    #   · `this.STEMS` is deleted by DROP_FIELDS.
    #   · `Math.min` over a `qpct` containing nulls returns 0, which would
    #     name a question as the weakest in the school at 0% on no marks.
    #
    # Fixed here rather than left for the Today-screen unit because it stands
    # between a real teacher and every one of the six pages, and because it
    # is the same defect as the entry above — one ruling, two addresses.
    ("""  weakFor(k) {
    if (k.state !== 'live') return null;
    const g = this.gridFor(k, 1);
    const min = Math.min.apply(null, g.qpct);
    const qi = g.qpct.indexOf(min);
    return { qi, min, id: this.STEMS[qi].id, text: this.STEMS[qi].text, paperId: k.id + ':p1' };
  }""",
     """  weakFor(k) {
    if (!k || k.state !== 'live') return null;
    const papers = this.papersFor(k);
    const pi = MRB_NEWEST_MARKED(papers);
    const p = pi >= 0 ? papers[pi] : null;
    const g = p ? this.gridFor(k, p.idx) : null;
    if (!g || !g.qpct) return null;
    let min = null, qi = -1;
    g.qpct.forEach((v, i) => {
      if (v != null && (min == null || v < min)) { min = v; qi = i; }
    });
    if (min == null) return null;
    const stem = (g.stems || [])[qi] || {};
    return { qi, min, id: stem.id || ('Q' + (qi + 1)),
      text: stem.text || '', paperId: p.id };
  }""",
     "the cross-class \"Worth a reteach\" list. Three throws in five lines, "
     "on every page rather than on one. See the block comment."),

    # ── the assignment section's own count ──────────────────────────────
    (dict(method="renderVals", key="klass.paperLine"),
     """        paperLine: !kPapers.length ? 'None set'
          : (wPapers.length
            ? wPapers.length + (wPapers.length === 1 ? ' assignment' : ' assignments') + ' · ' + kPapers.length + ' this term'
            : 'None in this week · ' + kPapers.length + ' this term')""",
     "the caption over the assignment table. With the table scoped to a "
     "week it has to say how many of the term's assignments it is showing, "
     "or a teacher reads a filtered table as the whole term. Part of #13."),

    # ══ THE WEEK BAR'S OWN KEYS ═════════════════════════════════════════
    #
    # ⚑ v2 had all nine of these and v3 has none. They are restored here, on
    # `backToClass` — a property the class screen has kept and which sits
    # exactly where v2 declared them, immediately after `roster` and
    # `assignments`.
    #
    # ⚠️ `weekTabs` MAPS OVER WEEKS. v2 mapped over `kPapers` and labelled
    # each chip with the week its paper was set in, which is one chip per
    # ASSIGNMENT wearing a week's clothes. That is the single thing about
    # this bar most likely to be got wrong by copying v2 faithfully, and it
    # is the thing real data breaks first.
    #
    # ⚠️ THE SECOND LINE OF EVERY CHIP IS FILLED. Design drew it as an
    # `sc-if w.now` reading "This week" and nothing at all on the other
    # eleven chips, because in her fiction the ranges alone identified the
    # weeks. Dated from a real academic year they do not — "5–9 Oct" says
    # nothing about which teaching week it is — so the line reads "This
    # week" on the current chip and the term-relative label ("Autumn Week 6")
    # on every other, in Design's own uppercase mono at her own size. The
    # conditional is gone rather than left always-true: a dead `if` is a
    # control that cannot be told from a broken one.
    #
    # ⚠️ THE TERM LABEL IS AN APPROXIMATION AND THE SEAM SAYS SO. There is no
    # `terms` table — checked, not assumed — so the term comes from the
    # week's own Monday against `seasonFor`'s Sep–Dec / Jan–Mar / Apr–Aug
    # boundaries and the number counts every week since the year began,
    # holidays included. "Autumn Week 18" for the week after Christmas is
    # what that costs. A `terms` table would make it exact; Mide's call.
    (dict(method="renderVals", key="backToClass"),
     """      backToClass: 'Back to ' + k.code,

      /* ── ⊕ MIDE, 1 Sep 2026 (MRB-306) · THE WEEK BAR ── */
      weekTabs: kWeeks.slice().reverse().map((w, n) => {
        const i = w.idx;
        const on = i === wi;
        return {
          idx: String(i),
          range: w.range,
          sub: w.now ? 'This week' : w.label,
          subFg: w.now ? 'var(--st-accent-text)' : 'var(--st-muted)',
          on,
          now: w.now,
          pick: () => this.pickWeek(i),
          bg: on ? 'var(--st-num-well)' : 'transparent',
          ring: on ? 'inset 0 0 0 1.5px var(--st-accent)' : 'none',
          divider: n === 0 || on ? 'transparent' : 'var(--st-rule-soft)',
          dateColor: on ? 'var(--st-ink)' : 'var(--st-muted)'
        };
      }),
      weekNote: !wWeek ? ''
        : [wWeek.now ? 'This week' : wWeek.label, wWeek.range,
          (!wPapers.length
            ? 'No work set in this week'
            : (wPapers.length === 1
              ? wPapers[0].title
                + (wPapers[0].when === 'upcoming' ? ' · open' : ' · marked')
                + (wPapers[0].due ? ', due ' + wPapers[0].due.replace(/^Due /, '') : '')
              : wPapers.length + ' assignments set')),
          wMean == null ? '' : 'Week mean ' + wMean + '%'
        ].filter(Boolean).join(' · '),
      weekBack: () => { if (wi < kWeeks.length - 1) this.pickWeek(wi + 1); },
      weekFwd: () => { if (wi > 0) this.pickWeek(wi - 1); },
      weekBackColor: wi >= kWeeks.length - 1 ? 'var(--st-rule-strong)' : 'var(--st-ink)',
      weekFwdColor: wi <= 0 ? 'var(--st-rule-strong)' : 'var(--st-ink)',
      weekBackCursor: wi >= kWeeks.length - 1 ? 'default' : 'pointer',
      weekFwdCursor: wi <= 0 ? 'default' : 'pointer',
      rosterWeekCol: wWeek ? (wWeek.now ? 'This week' : wWeek.range) : 'This week',""",
     "the nine keys Mide's week bar renders — the chips, the sentence under "
     "them, the two chevrons with their disabled colours and cursors, and "
     "the roster column's heading. All nine are v2's, `weekTabs` re-derived "
     "over WEEKS rather than over assignments and every chip's second line "
     "now filled. See the block comment."),

    # ══ ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · THE TWO READERS OF TODAY_LESSONS ═
    #
    # ⛔ A GREEN BUILD THAT THREW AT MOUNT. `DROP_FIELDS` deletes the four
    # invented lessons; these two entries are what stops the code that read
    # them from throwing on the way past. BOTH run unconditionally inside
    # `renderVals`, on every one of the six pages, before anything is drawn.
    #
    # `lessons` is the Today screen's list, and the Today screen is pruned on
    # all six pages — so the ONLY thing this expression ever did on an emitted
    # page was throw. It degrades to `[]`, which is the honest answer: the
    # platform holds no timetable, so it knows of no lessons today. Design's
    # own presentation of an empty list is what the Today screen will use when
    # it is ported.
    #
    # ⚠️ `[]` AND NOT A ONE-LINE GUARD INSIDE THE MAP. Guarding
    # `klassById(t.classId)` would have stopped the throw and kept four rows
    # of fiction — periods, times and rooms nobody timetabled — which is the
    # failure this port exists to prevent, wearing the fix's clothes.
    ("""    const lessons = this.TODAY_LESSONS.map(t => {
      const c = this.klassById(t.classId);
      const chase = this.chaseFor(c);
      let ready = '', readyFg = 'var(--st-muted)';
      if (c.state === 'empty') { ready = 'No students yet — import your class list'; }
      else if (c.state === 'nowork') { ready = 'No work set for two weeks · ' + c.n + ' students waiting'; readyFg = 'var(--st-accent-text)'; }
      else if (!chase.length) { ready = 'All ' + c.n + ' homeworks in — nothing to chase'; readyFg = 'var(--ks3-ok-text)'; }
      else {
        ready = (c.n - chase.length) + ' of ' + c.n + ' in — chase ' + chase.slice(0, 2).map(r => this.shortName(r.name)).join(', ') + (chase.length > 2 ? ' +' + (chase.length - 2) + ' more' : '');
        readyFg = 'var(--st-accent-text)';
      }
      return {
        p: t.p, time: t.time, code: c.code,
        meta: t.room + (c.n ? ' · ' + c.n + ' students' : '') + ' · ' + c.subject,
        ready, readyFg,
        open: () => c.n > 0 ? this.setState({ screen: 'class', classId: c.id }) : this.setState({ screen: 'import', importStep: 1 })
      };
    });""",
     """    /* ⊕ MRB-306: `TODAY_LESSONS` was four invented lessons and is deleted.
       This ran on every page and threw on the first real class id. There is
       no timetable behind this dashboard yet, so the honest list is empty. */
    const lessons = [];""",
     "the Today screen's lesson list. It read four fabricated lessons, and "
     "`klassById` on a fabricated class id returns undefined, so `c.state` "
     "threw at mount on all six pages."),

    # `lessonToday` is the CLASS screen's copy of the same fiction, and unlike
    # `lessons` its output reached a page a teacher actually opens:
    # `klass.meta` printed "Next lesson today · P5 · 13:55 · Lab 2" under a
    # real class code. `.filter(...)[0]` on a deleted field would throw; it
    # becomes `null`, and the `klass.meta` ruling above drops the part rather
    # than printing the falsy arm, because "No lesson today" is a claim and
    # not an empty state.
    ("    const lessonToday = this.TODAY_LESSONS.filter(t => t.classId === k.id)[0];",
     "    /* ⊕ MRB-306: no timetable data exists; see DROP_FIELDS. */\n"
     "    const lessonToday = null;",
     "the class header's \"next lesson\" fact. Four invented rooms and "
     "times, printed under a real class's code."),

    # ══ ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · DESIGN'S TOP-BAR TABS BECOME REAL ═
    #
    # ⛔ A BLANK PAGE, ON EVERY PAGE, FROM THE CHROME. v3's top bar is a two-
    # tab strip — "Today" and "My classes" — and both tabs call
    # `this.setState({ screen: t.id })`. On these six pages `s.screen` is
    # fixed by the build and every other screen `<if>` is PRUNED, so setting
    # `screen` to a screen this page does not carry makes every branch false
    # and the page renders nothing at all. It is the `c.act` failure of 24
    # Aug exactly, in the chrome rather than on one card, and therefore on all
    # six pages: every gate green, and a teacher pressing a tab in the header
    # gets a white screen with no error in the console.
    #
    # ⚑ SO THE TABS BECOME NAVIGATIONS, which is what every other screen-
    # changing control in this port already is. `t.pick` is loop-scoped, so
    # the destination has to be written in the closure that builds the row —
    # `NAV`'s builder anchor cannot reach it, because `navTabs` is a key of
    # `renderVals`'s return and not a `const … = ….map(` declaration.
    #
    # ⚠️ "Today" GOES TO THE HAND-WRITTEN `teacher/today.html`, WHICH IS REAL.
    # It is a live page that already loads `teacher-live.js`; it is simply not
    # one of the six this generator emits yet. Porting Design's Today screen
    # is a later unit, and when it lands it emits `teacher/today.html` — the
    # SAME URL — so this link does not become a redirect or a rename. The
    # alternative was pruning Design's strip, which would have thrown away the
    # only always-visible navigation on the dashboard to avoid a link to a
    # page that works.
    #
    # ⚠️ "My classes" CARRIES `yearParam`, because it is now the control that
    # `INSERT_AT[(10, 13)]` used to be, and MRB-287 E1's guarantee travels
    # with it: a teacher browsing 2025-26 comes back to 2025-26 rather than
    # being silently returned to the working year.
    #
    # The `on` computation, the two colours and Design's markup are untouched:
    # only the press changes.
    ("""          pick: () => this.setState({ screen: t.id, modal: null })""",
     """          pick: () => MRB_GO(t.id,
            t.id === 'classes' ? { year: MRB_DATA('yearParam') } : {})""",
     "the top bar's two tabs. Design's press set `s.screen`, which on a "
     "six-URL port is a page that renders nothing; both are real navigations "
     "now, and \"My classes\" carries the academic year the way the control "
     "it replaces did."),

    # ══ ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · THE THREE GLANCE CHIPS `NAV`
    #    CANNOT ANCHOR ═══════════════════════════════════════════════════
    #
    # The other five of v3's new class-screen controls are in `NAV` (see
    # `goToday`, `glance.openMarking`, `w.open (keep an eye on)`). These three
    # are here instead, and the reason is mechanical rather than a preference:
    # `NAV`'s builder anchor requires a `const <name> = ….map(` declaration,
    # and neither of these two lists has one. `chase` is a property INSIDE the
    # `const glance = {` object literal, and `praise` is `const praise = [];`
    # filled by two `.push(` calls. So they are anchored the way this file
    # anchors everything a node cannot reach: on their own source, exactly
    # once, and the build refuses on nought matches or two.
    #
    # ⚠️ STATED PLAINLY — THESE THREE ARE SOURCE-ANCHORED AND NOT
    # NODE-ANCHORED, so nodes 234 and 270 are asserted by nothing. If Design
    # redraws the glance block the source anchors below go red (which is the
    # protection that matters), but a chip that MOVED to a different node
    # would not be noticed. It is the weaker of the two guarantees and it is
    # the one available.
    ("        open: (e) => { e.stopPropagation(); this.setState({ screen: 'student', studentId: r.id }); }",
     "        open: (e) => { e.stopPropagation(); MRB_GO('student', "
     "{ student: r.id, 'class': k && k.id }); }",
     "a name chip in the class glance's \"Not in yet\" chase list (node "
     "234). `e.stopPropagation()` is KEPT — the chip sits inside a card that "
     "has its own press, and dropping it would fire both."),

    ("open: () => this.setState({ screen: 'student', studentId: best.id })",
     "open: () => MRB_GO('student', { student: best.id, 'class': k && k.id })",
     "the \"Worth a shoutout\" chip for the class's top average (node 270)."),

    ("open: () => this.setState({ screen: 'student', studentId: imp.r.id })",
     "open: () => MRB_GO('student', { student: imp.r.id, 'class': "
     "k && k.id })",
     "the \"Worth a shoutout\" chip for the most improved student (the "
     "second row of node 270's loop)."),

    # ══ ⊕ 2 Sep 2026 (MRB-306 Phase 2a, screen 4) ═══════════════════════
    #    THE STUDENT'S TILES DID NOT AGREE WITH THE ROWS UNDER THEM
    #
    # Appended, not inserted, for the reason the two blocks above give: LOGIC
    # entries are named by INDEX in every brief written about this port.
    #
    # ── 1. `lateState` NEVER REACHED THE ROW ────────────────────────────
    #
    # ⚑ FOUND BY LOOKING AT THE PAGE, NOT BY READING IT. Every gate was
    # green. The screenshot showed an ON TIME tile reading "—" over the
    # caption "10 timing unknown · 1 not submitted", sitting directly above
    # eight rows each carrying a green ON TIME chip and two carrying a red
    # LATE chip. The tile and the rows were describing the same eleven
    # submissions and disagreeing about every one of them.
    #
    # The cause is one missing word. The ruling four hundred lines above
    # introduced the tri-state and its note says "the tri-state is carried on
    # the row now, so the chip and the tile can both see it" — but it
    # declares `lateState` as a LOCAL `const` inside `kPapers.map(…)` and
    # never adds it to the object that map RETURNS. The chip can see it,
    # because the chip is computed inside the closure. The tile cannot,
    # because the tile filters the returned rows:
    #
    #     const stOnTime = stMarked.filter(h => h.lateState === false).length;
    #     const stLate   = stMarked.filter(h => h.lateState === true).length;
    #
    # `h.lateState` is `undefined` on every row, so BOTH counts are always 0,
    # `stUnknown` is always the whole of `stMarked`, and `MRB_ONTIME_VALUE(0,
    # 0)` returns an em dash by design. The tile could not have shown a
    # number, for any student, on any data, ever.
    #
    # ⚠️ THE FIXTURE COULD HAVE CAUGHT THIS AND NO GATE ASKED IT TO. Design's
    # sample carries real booleans in `late[]` — nine false, two true — so a
    # working tile reads "8" and "2 late". Nothing compares the tile with the
    # rows, and every check that does exist passed.
    # ⚠️ SOURCE-ANCHORED, AND NOT `dict(builder="stHistory", key="late, pct")`
    # — WHICH WAS TRIED FIRST AND IS A TRAP. v3 writes this line as the
    # shorthand pair `late, pct: …`, so `key="late, pct"` looks like the
    # obvious anchor. `resolve_anchor` accepted it and returned a span of
    # 6,008 CHARACTERS: from `late,` to the end of the enclosing structure,
    # swallowing `submitted`, `score`, `status`, all four tone fields,
    # `stMarked`, `stOnTime`, `stTimeSub` and `stSummary`. Replacing that span
    # with this one line would have DELETED about six kilobytes of Design's
    # logic.
    #
    # ⛔ AND IT WOULD HAVE BUILT GREEN. Nothing measures how much a resolved
    # anchor spans. It was caught only because the NEXT ruling in this block
    # anchors on `stSummary`, which the deletion had just removed, so the
    # build refused with "appears 0 times" — pointing at the innocent entry,
    # not the guilty one. A shorter block here would have shipped it.
    # Reported to Mide as a hazard in the anchor mechanism itself.
    ("        late, pct: open ? null : pct,",
     "        late, lateState, pct: open ? null : pct,",
     "the tri-state, PUT ON THE ROW. `lateState` was a local const the "
     "returned object never carried, so the two tile counts that filter on "
     "it were both permanently 0 and the On-time tile was permanently an em "
     "dash. One word, and it is the difference between a tile that reports "
     "the rows and a tile that contradicts them."),

    # ── 2. "OPEN" WAS A POSITION, NOT A DEADLINE ────────────────────────
    #
    # `const open = i === 0` says the newest paper is the open one. That is
    # true in Design's fiction — her sample is one paper a week with exactly
    # one still running — and `shared/teacher-live.js` warns about it in
    # terms, above `buildMatrix`:
    #
    #     ⚠️ COLUMN 0 IS NOT NECESSARILY THE ONLY OPEN PAPER. Design assumes
    #     exactly one — index 0 open, 1..n marked — and reaches for
    #     `.slice(1)` when it wants "the marked ones". Real classes have none
    #     open, or three.
    #
    # Index 0 is merely the newest by `due_at`; whether it is open is a
    # DEADLINE test, and `buildPapers` already did it — `when` is `upcoming`
    # or `marked`. The `assignments` table on the class screen reads
    # `p.when === 'marked'`; the student's history was the one list left
    # reading a position instead.
    #
    # ⚑ WHAT IT COSTS ON REAL DATA, which is the only place it bites. When
    # the newest paper's deadline HAS passed, row 0 is forced down the open
    # branch: its mark is replaced by an em dash, its chip reads "In
    # progress" or "Nothing in", and — because `stMarked` is built from these
    # rows — it is dropped from Submissions, from On time and from Avg score.
    # A child's most recent marked paper disappears from the page and from
    # every number on it. Today only `8r/Sc1` has assignments at all, and
    # both of them are past their deadline the moment the first one closes.
    (dict(builder="stHistory", key="const open"),
     "      const open = p.when === 'upcoming';",
     "\"open\" is whether the DEADLINE has passed, not whether the paper is "
     "first in the list. Design's `i === 0` is her one-open-paper fiction, "
     "the seam warns about it by name above `buildMatrix`, and `buildPapers` "
     "already answers it as `when`. A real class has none open, or three."),

    # ── 3. AND THE DENOMINATOR THAT ASSUMED THE SAME THING ──────────────
    #
    # `Math.max(0, kPapers.length - 1)` is "all the papers except the open
    # one", spelled as arithmetic. It is the third of the three captions the
    # #11 block lists as saying more than their figure knows, and the class
    # and digest screens were both corrected to `kMx.markedIdx.length` on
    # 24 Aug; the student screen's two occurrences were missed. Same defect,
    # same fix, same key — `markedIdx` is the indices actually closed, so the
    # denominator is counted rather than assumed, and it agrees with the rows
    # because `open` above is now the same test.
    ("          { label: 'Submissions', value: String(stMarked.length), "
     "sub: 'Of ' + Math.max(0, kPapers.length - 1) + ' marked this term' },",
     "          { label: 'Submissions', value: String(stMarked.length),\n"
     "            sub: 'Of ' + kMx.markedIdx.length + ' marked this term' },",
     "the Submissions tile's denominator. `kPapers.length - 1` assumes "
     "exactly one open paper; `markedIdx` counts the closed ones."),

    ("      ? (stMarked.length + ' of ' + Math.max(0, kPapers.length - 1) "
     "+ ' marked sets handed in'",
     "      ? (stMarked.length + ' of ' + kMx.markedIdx.length "
     "+ ' marked sets handed in'",
     "the summary sentence's denominator — the same assumption as the tile "
     "above it, in words. Both now count the closed papers."),

    # ── 4. "SEND A REMINDER" SENT NOTHING ───────────────────────────────
    #
    # Design draws the button (node 341), gates it on `student.flagged`, and
    # hands it `this.ping('Reminder sent to ' + st.name)`. It was pressed on
    # the fixture before this ruling and it said, in a toast, "Reminder sent
    # to Jasmine Okafor". No row was written, no child was told, and the
    # teacher had no way to know.
    #
    # This is the same defect the shoutout composer had — a `ping` standing
    # in for a write — and it is corrected the same way, through a helper
    # beside the six that wired the composer, so the page keeps Design's
    # button and Design's toast surface and gains the write behind them.
    #
    # ⚠️ THE BACKEND ALREADY EXISTED AND IS NOT NEW HERE. `student_notifications`
    # is a live table with an RLS policy (`teacher_send`, gated on
    # `sent_by = auth.uid() AND auth_user_teaches_class(class_id)`) and a
    # unique index `(student_id, assignment_id, sent_on)`.
    # `MrBadmusTeacherData.sendReminders` and `remindersForClass` have driven
    # the class screen's "Remind all N" since MRB-306 WS-3. `MRB_REMIND_STUDENT`
    # calls that same function with a one-element list; it does not
    # reimplement any of it.
    #
    # ⚠️ AND IT DOES NOT ENFORCE THE RATE LIMIT — the database does. A second
    # press upserts with `ignoreDuplicates`, writes nothing, and returns an
    # empty array, which is reported as "already reminded today". A control
    # that claimed to have sent a second reminder would be lying twice.
    ("      remindStudent: () => this.ping('Reminder sent to ' + "
     "(st ? st.name : 'student')),",
     "      remindStudent: () => MRB_REMIND_STUDENT(k && k.id,\n"
     "        kPapers[0] && kPapers[0].id, st && st.id).then((r) => {\n"
     "          if (r.error) { this.ping(MRB_REMIND_WHY(r.error)); return; }\n"
     "          if (r.already) {\n"
     "            this.ping((st ? st.name : 'They')\n"
     "              + ' has already been reminded about this today');\n"
     "            return;\n"
     "          }\n"
     "          this.ping('Reminder sent to ' + (st ? st.name : 'student'));\n"
     "        }),",
     "the per-student reminder. Design's handler toasted a send that never "
     "happened; this writes to `student_notifications` through the same "
     "`sendReminders` the class screen's control uses, and says which of the "
     "three things actually occurred."),

    # ══ ⊕ 2 Sep 2026 · A RETEACH LINE WITH NO QUESTION IN IT ════════════
    #
    # ⛔ `worst.text` CAN BE EMPTY, AND DESIGN'S SENTENCE ASSUMES IT NEVER IS.
    # `assignment_question_attempts.question_text` is NULLABLE — it is a
    # denormalised snapshot of the stem as the child was served it
    # (`20260501212106_schools_layer.sql:325`, `20260818231152:7`) — and
    # `buildGrid` deliberately leaves a column's `text` as `""` when no
    # attempt carried one, because "an unanswered question has no snapshot
    # and so no text — blank, not a placeholder".
    #
    # Design's line then reads:
    #
    #     Q4 — . Only 23% of the class got it right.
    #
    # in 19px on the accent panel at the top of the screen, which is the
    # first thing a teacher sees on the page. The em-dash clause is the part
    # that has nothing to say, so the em-dash clause is what goes; the
    # sentence that survives ("Q4. Only 23% of the class got it right.")
    # still names the question and still gives the number.
    #
    # ⚠️ THE TILE BELOW IT ALREADY HANDLED THIS and that is why it was easy
    # to read past — `{ label: 'Lowest', … sub: worst ? worst.text : '' }`
    # renders an empty sub perfectly well. Only the banner concatenates.
    ("        reteachLine: worst ? worst.id + ' \u2014 ' + "
     "worst.text.toLowerCase() + '. Only ' + worst.pct + '% of the class got "
     "it right.' : '',",
     "        reteachLine: worst ? worst.id\n"
     "          + (worst.text ? ' \u2014 ' + worst.text.toLowerCase() : '')\n"
     "          + '. Only ' + worst.pct + '% of the class got it right.'\n"
     "          : '',",
     "the reteach banner, on a paper whose worst question carries no stem "
     "snapshot."),

    # ══ ⊕ 2 Sep 2026 · THE CLASS-BY-QUESTION GRID IS EIGHT WIDE ═════════
    #
    # ⛔ `grid-template-columns:225px repeat(8,1fr) 92px`, TWICE — Design's
    # header row (node 413) and her student row (node 419). Eight is the
    # length of `STEMS`, the sample's one question list for every paper in
    # every subject, and it is welded into the LAYOUT rather than into the
    # data, so the `pGrid.stems.length` ruling that freed the question COUNT
    # left the table still eight columns wide.
    #
    # ⚠️ REAL PAPERS ARE NOT EIGHT QUESTIONS. Measured on the TEST project,
    # 2 Sep 2026: the only assignment carrying `assignment_questions` rows has
    # FOUR, and every `assignment_submissions.max_score` in the database is
    # TEN. A four-question paper draws four cells into an eight-column
    # template — four empty columns, and "Mark" nowhere near the right-hand
    # edge it is right-aligned to. A twelve-question paper is worse: the
    # extra cells create implicit auto-width columns, so the row and the
    # header disagree about where every column starts and the marks column
    # is pushed off the end of the scroll area.
    #
    # The template is therefore built from the paper, in `renderVals`, and
    # both nodes interpolate it (`BIND_ATTR` 413 and 419). `paper.cols` is a
    # STRING because a grid template is one; `questions.length || 1` because
    # `repeat(0,1fr)` is invalid CSS and an invalid track list drops the whole
    # declaration — which would turn the not-fetched state, the one state
    # this screen must survive, into an unstyled stack.
    #
    # ── AND THE TWO SECTIONS HAVE TO BE ABLE TO SAY THEY ARE EMPTY ──────
    #
    # ⛔ A GRID KEY THAT IS NOT THERE IS THE STATE THIS SCREEN MUST SURVIVE,
    # AND IT SURVIVED IT SILENTLY. `gridFor` returns null, `questions` and
    # `grid` are both `[]`, nothing throws — and the page then draws the
    # heading "Question breakdown" over a hairline and nothing else, and
    # under it "Class by question" with a legend and a STUDENT / MARK header
    # strip over an empty card. Driven on
    # `assignment-gridmissing-fixture.html` and looked at: it reads as a page
    # that failed, not as a page with nothing to show.
    #
    # `hasQuestions` / `noQuestions` are the pair. Both, rather than one and
    # a negation at each site, because `student-runtime` has no `unless`.
    ("        qids: questions.map(qq => ({ id: qq.id })),\n"
     "        grid\n"
     "      } : { title: '\u2014', eyebrow: k.code, hasReteach: false, "
     "reteachLine: '', tiles: [], questions: [], qids: [], grid: [] },",
     "        qids: questions.map(qq => ({ id: qq.id })),\n"
     "        cols: '225px repeat(' + (questions.length || 1) + ',1fr) "
     "92px',\n"
     "        hasQuestions: questions.length > 0,\n"
     "        noQuestions: questions.length === 0,\n"
     "        labelCol: scored.length === questions.length ? '90px' "
     ": '112px',\n"
     "        grid\n"
     "      } : { title: '\u2014', eyebrow: k.code, hasReteach: false, "
     "reteachLine: '', tiles: [], questions: [], qids: [], grid: [],\n"
     "          cols: '225px repeat(1,1fr) 92px',\n"
     "          hasQuestions: false, noQuestions: true, "
     "labelCol: '90px' },",
     "the class-by-question table's column template, and the pair of flags "
     "the two empty states hang on. The no-paper branch carries all three: "
     "every one of the six pages computes this object, so a key that exists "
     "on only one branch is a missing binding on the others."),
)



# ── ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · THE UNGUARDED-RULING SWEEP ─────────
#
# ⛔ THE HOLE THIS CLOSES. `apply_rulings` runs each node-anchored table with
# `if node not in here: continue` — correct per page, because a node pruned
# with somebody else's screen is legitimately absent. But four of those
# tables had NO cross-page sweep behind them, so a node Design had DELETED
# was skipped on all six pages and the ruling was never checked anywhere:
# build green, ruling not in any page. That is exactly the failure this whole
# file exists to prevent, and it was live in `SET_ATTR`, `BIND_ATTR`,
# `RETEXT_AT` and `SET_ON`. `NAV` and `RETARGET_ON` already had the sweep;
# these four now share it.
#
# ⚠️ AND A BARE SWEEP WOULD HAVE BEEN RED ON A CORRECT BUILD, which is why
# this register exists. Twelve rulings BELONG to the import screen, and the
# import screen is deliberately not emitted (`IMPORT_NOT_PORTED`). They are
# kept rather than deleted because they are the anchoring a future re-port
# would otherwise redo. Naming them here is the difference between "we know
# these twelve apply to nothing, and here is why" and silence.
#
# ⚠️ IT IS CHECKED IN BOTH DIRECTIONS. An entry named here that DOES turn up
# on a page fails the build too — otherwise the exemption list rots into a
# way of switching a guard off. `{table: {node: why}}`.
KNOWN_UNAPPLIED = {
    "SET_ATTR": {
        462: "import wizard — the screen's own `data-port-region`. Found by "
             "the sweep on its first run, which is the point of it: nobody "
             "had noticed this row applied to nothing.",
        483: "import wizard — the uploaded file's name",
        484: "import wizard — the row/column summary",
        499: "import wizard — \"New students\"",
        502: "import wizard — \"Matched existing\"",
        505: "import wizard — \"Needs attention\"",
        515: "import wizard — the confirm button",
    },
    "RETEXT_AT": {
        483: "import wizard — a file nobody uploaded",
        484: "import wizard — counts of a file nobody parsed",
        499: "import wizard — a dry-run nobody ran",
        502: "import wizard — same",
        505: "import wizard — same",
        515: "import wizard — the button's fictional count",
    },
    "BIND_ATTR": {},
    "SET_ON": {},
}


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
