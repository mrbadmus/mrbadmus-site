#!/usr/bin/env python3
"""build_student_port.py — the PORTED student pages: Design's markup and logic,
rendered by our own vanilla runtime with no React and no `support.js`.

    python3 build_student_port.py

Writes:

    mrbadmus_site/shared/student-ds.css        Design's six stylesheets, once
    mrbadmus_site/shared/student-fixture-class.js       Design's example data
    mrbadmus_site/shared/student-fixture-assignment.js  Design's example data
    mrbadmus_site/student/class-ported.html        production — NO data in it
    mrbadmus_site/student/assignment-ported.html  production — NO data in it
    mrbadmus_site/student/class-fixture.html       the gates' page
    mrbadmus_site/student/assignment-fixture.html  the gates' page
    student/*.html, shared/*.js                (mirror)

── TWO PAGES, BECAUSE ONE CANNOT BE BOTH ────────────────────────────────

A single page that renders Design's example data when the database is quiet
is a page that shows one child's marks to another the first time a fetch
fails. So the split is structural rather than conditional:

  *-ported.html   Design's markup and Design's logic with every data literal
                  lifted out. It defines `window.__MRB_MOUNT__` and DOES NOT
                  CALL IT, and it ends by loading `shared/student-live.js`.
                  There is no fixture in this file to fall back to, so there
                  is no code path that could fall back to one.
  *-fixture.html  the same file but for its banner comment and its last two
                  script tags, which load Design's extracted values and mount.
                  This is what `student_behaviour.py` drives.

Design's data is lifted BY SOURCE TRANSFORMATION, never retyped — the five
class-view fields and the five assignment fields by balanced-literal scan out
of the logic class, the eleven identity strings by exact match against the
compiled template. Anything on either list that cannot be found stops the
build; see `find_field` and `bindings_for`.

⛔ It writes no live page. `_REFUSED` in `build_student.py` is the same list and
the same reason: swapping a preview onto a live path is a separate, deliberate
change, gated on the whole Phase 5 checklist.

── Why this exists beside build_student.py rather than replacing it ──────

`build_student.py` photographs Design's rendered DOM. That was the right first
move — it made parity a property rather than an effort — and it has two limits
that no amount of care removes:

  * IT IS ONE STATE. 52 nodes Design renders below desktop are simply not in a
    desktop photograph, and no runtime shim can conjure them. Neither is the
    recall round, the expanded work row, the marker sheet or the end screen.
  * IT IS 558 KB, of which 306 KB is Chrome's longhand expansion of `all:
    unset` on 25 buttons and 223 KB is CSS inlined once per page.

This renders from Design's TEMPLATE instead, so every state exists, `all:unset`
stays two words, and the stylesheets are linked and cached. The two builds are
kept side by side until the ported pages pass the same parity gate the
snapshots do — at which point the snapshot build retires, with a note, rather
than being deleted.

── What is Design's ─────────────────────────────────────────────────────

The markup (Design's template, compiled by `student_template.py`, not retyped),
the behaviour (Design's logic class, extracted verbatim), the styling (Design's
own six stylesheets, concatenated in Design's own link order), and the brand
mark (captured from Design's render). What is ours is `shared/student-runtime.js`
— a 30-line base class and a renderer for three constructs.
"""

import hashlib
import html
import json
import os
import re
import sys

# ⊕ 23 Aug 2026 — the cache-bust stamp. `stamp_versions` is IMPORTED, not
# retyped: build_ks3.py already owns the one substitution that gets this right
# (idempotent against a stale `?v=`, anchored on the trailing quote so a short
# name cannot match inside a longer one, and agnostic about whether the path
# sits in a `src` or an `href`). generate_site_v5.py carries a second inline
# copy of the same regex; a third one here would be the copy that drifts.
# Importing build_ks3 is cheap and side-effect-free — it loads the KS3 art
# registry and writes nothing — measured at ~0.26s.
from build_ks3 import stamp_versions

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "student")
DS = os.path.join(REF, "source", "_ds",
                  "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")
SITE_OUT = os.path.join("mrbadmus_site", "student")
MIRROR_OUT = "student"
SHARED_OUT = os.path.join("mrbadmus_site", "shared")

TEMPLATES = "student_templates.json"

# ⊕ 22 Aug 2026. Design's class-view amendments, compiled by
# `student_template.py` as a page that is never emitted. `apply_rulings` grafts
# regions out of its tree; nothing else reads it, and nothing renders it.
DONOR_PAGE = "class view amendments"
DS_CSS_NAME = "student-ds.css"
DS_CSS_URL = "/shared/" + DS_CSS_NAME
SERVED_FONTS = "/shared/fonts/"

# ⊕ THE SWAP, 22 Aug 2026. `class.html` and `assignment.html` are OFF this
# list, and this build now writes them directly.
#
# ⚠️ THE ALTERNATIVE WAS A TRAP, AND IT IS THE TRAP THAT COST THE LAST RUN A
# RED GATE. Copying the built `-ported.html` over `student/class.html` would
# have put GENERATED OUTPUT AT A SOURCE PATH — which is exactly what happened
# to the MRB-275 rulings, hand-edited into `-ported.html`, silently eaten by
# the next build, and recovered only by inventing `student_rulings.py`. Doing
# it that way would have set the same trap one file along: the live page would
# look hand-editable, somebody would hand-edit it, and the next rebuild would
# revert a student-facing fix without a word.
#
# So the build owns the live path outright. A rebuild now KEEPS the live page
# correct instead of reverting it, and nothing about these two pages is ever
# edited by hand again. The hand-written originals are retired to
# `docs/ks3/retired/` with tonight's date — out of `student/`, so the
# generator does not publish them, and git holds them regardless.
#
# `classes.html`, `settings.html` and `claim-confirm.html` STAY refused. They
# are still hand-written source and this build has nothing to say about them.
_REFUSED = {"classes.html", "settings.html", "claim-confirm.html"}

LESSON_INDEX_NAME = "ks3-lesson-urls.js"
RUNTIME_JS_NAME = "student-runtime.js"
LIVE_JS_NAME = "student-live.js"
LIVE_JS_URL = "/shared/" + LIVE_JS_NAME

# ── Cache-bust stamps ────────────────────────────────────────────────────
#
# ⚑ THIS CLOSED A DEFECT THAT WAS HITTING STUDENTS, and it is worth writing
# down exactly, because a 200 with the right HTML is the failure mode that
# looks like success.
#
# Measured on mrbadmus.com: `/student/class` is served
# `max-age=0, must-revalidate` — always fresh — while every asset under
# `/shared/` is served `max-age=14400, must-revalidate`, four hours. These two
# pages loaded `student-runtime.js`, `student-live.js` and `student-ds.css`
# with NO version query, so for up to four hours after every deploy a student
# arriving by bookmark, typed URL or the "My class" nav got TODAY's HTML with
# YESTERDAY's JavaScript. The compiled binding table then demanded a key the
# old file never emitted:
#
#     [student-live] Error: student page: no data for "accountClassLine"
#
# and the catch in `student-live.js` fell through to "We could not load your
# class just now. Try again in a moment." — a TRANSIENT sentence for a
# condition that persists for four hours. Reload cures it (a reload
# revalidates); NAVIGATION does not, which is why it looked intermittent.
#
# The stamp makes the skew impossible rather than unlikely: the URL names the
# CONTENT, so a browser holding the old bytes is holding them under a
# different URL and has no cached answer for the one the page asks for.
#
# ── the four the pages themselves link ───────────────────────────────────
# `student-fixture-*.js` is per page and is added to the map inside the loop.
#
# ── AND THE FIVE THE RUNTIME LOADS, which is the half the brief did not see ──
# `student-live.js` loads five more shared scripts itself, from its `DEPS`
# list, and every one of them was unstamped:
#
#     config.js · class-entry.js · student-guard.js · student-data.js
#     ks3-lesson-urls.js
#
# Stamping only the three tags in the HTML would have left `student-data.js`
# — which carries `saveBenchTheme` and the `workingAcademicYear()` scoping —
# on the same four-hour skew, reached through a `<script>` element this build
# never writes. They cannot be stamped by rewriting `student-live.js` (it is a
# hand-written source file, and rewriting the published copy would make the
# deployed bytes differ from the repo's). So the BUILD publishes the map and
# the RUNTIME reads it: `window.__MRB_ASSET_V__`, bare name → hash.
#
# ⚠️ THE MAP IS KEYED ON THE BARE NAME, ON PURPOSE. Keyed on the full
# `/shared/<name>` URL it would be rewritten by generate_site_v5.py's own
# cache-bust pass — that regex matches `/shared/student-data.js"` wherever it
# occurs, including inside a JSON key — turning the key into
# `"/shared/student-data.js?v=…"`, which `student-live.js` would then fail to
# look up. Silent, and it would look like the stamp simply had no effect.
STAMPED_DEPS = ("config.js", "class-entry.js", "student-guard.js",
                "student-data.js")


def asset_hash(text):
    """The repo's one stamping scheme: md5 of the bytes, first 8 hex chars.

    Identical to `build_ks3.asset_versions` and to generate_site_v5.py's
    inline pass, which is what makes `class-entry.js?v=8be18391` read the same
    on `student/classes.html` (stamped by the KS4 generator) and in this
    build's `__MRB_ASSET_V__` map. Two writers, one number.
    """
    if isinstance(text, str):
        text = text.encode("utf-8")
    return hashlib.md5(text).hexdigest()[:8]

PAGES = [
    dict(page="class view", out="class.html",
         fixture_out="class-fixture.html",
         fixture_js="student-fixture-class.js",
         title="My class · MrBadmusAI",
         title_expr="MRB_DATA('className') + "
                    "' \\u00B7 My class \\u00B7 MrBadmusAI'",
         fields=["work", "roster", "weekPts", "lessonDefs", "questions"],
         # ⊕ 22 Aug 2026 — `boardWeek` joins `streak`. Design opens the
         # leaderboard on WEEK 04 because that is the week Design drew, and a
         # DEFAULT is student-visible data just as surely as a string is: on a
         # real class in week 1 the board headed itself "TOP OF WEEK 04" and
         # its scope note read "WEEK 04 · FINAL" — a final result for a week
         # that has not happened. Found by photographing the page; no grep for
         # a welded string would have found it, because there is no welded
         # string. The fixture still carries 4, so Design's render is unchanged.
         # ⊕ 23 Aug 2026 — PHASE 3. `streak` LEAVES THIS LIST, and the build
         # stopping is what found it: *"`streak` is not a property of the
         # `state` initialiser in Design's logic"*. It is not, any more.
         # Design's original recall round is retired — its state went with its
         # markup, its methods and its data (see PHASE 3 in
         # student_rulings.LOGIC) — and the amended round's streak is `rstreak`,
         # which opens at 0 and is a fact about the SITTING rather than a
         # student's record. There is nothing for a data source to seed.
         state_fields=["boardWeek"],
         # ── constants ────────────────────────────────────────────────────
         # ⊕ RULED 22 Aug 2026 — P1 and P3. Two destinations Design's file has
         # no opinion about, because Design's file has nowhere to go: it is one
         # page, and its buttons move state rather than navigating.
         #
         # EMPTY IS DESIGN'S OWN BEHAVIOUR, not a placeholder. Both rulings
         # below are written as "navigate if there is somewhere to navigate to,
         # otherwise do exactly what Design did", so with these two empty the
         # fixture ticks its checklist and opens its recall panel precisely as
         # the delivery does — and the behaviour gate compares the two without
         # a divergence to register. The live page supplies real URLs.
         # `benchDone` false is Design's own state — the delivery draws the
         # bench with work still on it — so every ruling below falls back to
         # exactly what Design computed and the fixture is untouched.
         # ⊕ 23 Aug 2026 — PHASE 2. `cardsEmpty` is the sentence the
         # flashcards card shows when the deck has nothing in it. EMPTY on
         # the fixture, deliberately: Design's amended delivery draws no
         # empty state for this card, so there is nothing of Design's to
         # carry, and Design's own six-card deck never reaches the branch
         # that reads it. The live source supplies the real sentence.
         # ⊕ 23 Aug 2026 — PHASE 4. `benchPct` and `benchDoneText` LEAVE THIS
         # LIST. Both were here for the interim done state's two overrides on
         # Design's bench line; Design's done bench is drawn now, the open
         # bench does not render beside it, and those two overrides came off in
         # the same commit — so nothing reads either key through `MRB_DATA` any
         # more, and a constant nothing reads cannot go stale loudly.
         #
         # FOUR JOIN IT, and all four are FALSE-ISH ON PURPOSE, because the
         # fixture is Design's own delivery and Design's bench has work still
         # on it. `benchOpen` true and `benchDone` false is exactly the state
         # Design drew, so the behaviour gate sees the same page it always saw
         # and there is no divergence to register. The other three gate parts
         # of a bench the fixture never reaches; they are here because
         # `MRB_DATA` THROWS on a missing key and `renderVals` reads all four
         # unconditionally — a page that mounts is not evidence they were
         # optional.
         constants=dict(benchPrimaryHref="''", benchDone="false",
                        benchOpen="true", benchDoneMarked="false",
                        benchDoneLessons="false", benchDoneFeedback="''",
                        cardsEmpty="''")),
    dict(page="assignment", out="assignment.html",
         fixture_out="assignment-fixture.html",
         fixture_js="student-fixture-assignment.js",
         title="Assignment · MrBadmusAI",
         title_expr="'Assignment \\u00B7 ' + MRB_DATA('className') + "
                    "' \\u00B7 MrBadmusAI'",
         fields=["questions", "wrongPlan", "figCaptions", "KEY", "DUE"],
         state_fields=[],
         # ── constants ────────────────────────────────────────────────────
         # ⊕ 22 Aug 2026. Two values a RULING introduced rather than lifted.
         #
         # `lift_literals` and `rewrite_seams` both carry Design's own bytes
         # out of Design's own logic, which is what makes the fixture's render
         # provably identical. These two have no such source: `student_rulings`
         # REPLACED the expressions that held them, so there is nothing left in
         # Design's file to lift from. They are therefore written here, beside
         # the ruling that needs them, with EXACTLY the value Design's line
         # produced — `'WEEK 04 \u00B7 '` and `' \u00B7 2 days late'` — so the
         # fixture still renders byte-for-byte what Design drew.
         #
         # ⚠️ This is the one place in the build a value is typed rather than
         # extracted, and it is deliberately small and deliberately named. If
         # it ever grows past a handful, the seam has stopped being a seam.
         #
         # ⊕ QUICKFIX-2026-08-24 — a third value, same reason. Design's file
         # never had an `assignmentLessonHref`; the ruling that reads it
         # (node 348's `<if>`, see WRAP in student_rulings.py) is new, and
         # `MRB_DATA` throws on a key the fixture was never given — found by
         # `student_behaviour.py` refusing to mount at all, not by reading
         # the diff. A real-shaped lesson URL, not a placeholder string, so
         # the fixture keeps exercising a PRESSABLE "Open lesson" — matching
         # Design's own always-visible button — rather than silently gating
         # it off on every gate run.
         constants=dict(weekLabel="'WEEK 04'", lateText="'2 days late'",
                        assignmentLessonHref=
                        "'/ks3/biology/breathing-and-gas-exchange/"
                        "the-gas-exchange-system.html'")),
]

# ── the identity strings, which are NOT in the logic ──────────────────────
#
# Design's example data lives in two places and only one of them is a field.
# `8r/Sc1`, `Ayo`, `Mr Badmus`, `28 students` are TEXT NODES in Design's
# template — typed into the markup, not computed — so seaming the logic class
# alone leaves a page that reads its work from the database and still greets
# every student as Ayo.
#
# ⚠️ THEY ARE BOUND AS LITERALS AND MUST STAY LITERALS. Design's compiler wraps
# every `{{ }}` in text position in `<span class="sc-interp">`; rewriting these
# nodes into interpolations would therefore ADD one element per binding and the
# parity gate counts elements. So the binding happens to the compiled template
# at mount time — the node's `v` is replaced with a different plain string —
# and the node count is untouched. See `applyBindings` in student-runtime.js.
#
# Each entry is (exact literal, data key). EVERY node whose text is exactly
# that literal is bound, which is deliberate: `8r/Sc1` appears twice in the
# class view's markup and both are the same class. Whitespace is part of the
# match, which is why the padded third occurrence is a separate key rather than
# a third match — binding it to `className` would silently eat its indentation.
BINDINGS = {
    "class view": [
        ("8r/Sc1", "className"),
        # ⊕ 23 Aug 2026 — PHASE 3. `classNamePadded` IS RETIRED, and it was
        # found by the build stopping rather than by reading — which is the
        # check working. Quoted rather than deleted:
        #
        #     ("8r/Sc1\n        ", "classNamePadded"),
        #
        # Its ONE text node on the whole class view was node 338, the back
        # button of Design's ORIGINAL recall round, and Phase 3 prunes that
        # subtree. Measured both ways before this was written: the literal
        # occurs at exactly one path in Design's original template and at NO
        # path in the amended delivery — Design's amended round draws the same
        # button (donor 373) with the text node `8r/Sc1`, no trailing
        # indentation, which binds to `className` for free.
        #
        # So the padded twin exists because Design's compiler kept the markup's
        # indentation inside that one text node, and it stops existing with the
        # node. `student-live.js` still computes it, like `recallBlurb` and
        # `recallEyebrow`; it is in `_MUST_NOT_LEAK`, which is an assertion
        # about a key's VALUE never reaching the page and is unaffected by the
        # key having no reader.
        # ⊕ 23 Aug 2026 — RETIRED, and quoted rather than deleted for the same
        # reason `recallBlurb` and `classNamePadded` above are — deleting it
        # would hide WHY the student's name stopped being in the header:
        #
        #     ("Ayo", "studentFirstName"),
        #
        # Its ONE text node on the whole class view was node 24, inside the
        # `<if wide>` beside the avatar disc — measured with `text_paths`, one
        # path, not assumed — and the 23 Aug header ruling prunes that `<if>`
        # (see `PRUNE` 23 in student_rulings.py: the header drew the name here,
        # again inside the account sheet it opens, and again in the hero).
        # Leaving the entry would stop the build with "the literal is not a
        # text node in Design's template", which is that check working.
        #
        # ⚑ THE KEY IS NOT ORPHANED. `BINDINGS_AT` 10254 binds the account
        # sheet's name to `studentFirstName`, and it is the reason that entry
        # exists at all — Design's amended sample writes `AY` there, so the
        # sheet needs the NAME bound where Design drew the monogram twice.
        ("Welcome back, Ayo · your class", "welcomeLine"),
        ("AY", "studentInitials"),
        ("Mr Badmus", "teacherName"),
        ("MB", "teacherInitials"),
        # ⊕ RULED 23 Aug 2026 — `drop`, and it is P6's ruling applied to the
        # case P6 missed. `classSize` is a deliberate COULD-NOT-SOURCE empty
        # string (`shared/student-live.js`: "class_members_self_read shows a
        # student their own membership row and no one else's, so the size of
        # the class cannot be counted from the client"). Without the flag the
        # empty string blanks the TEXT and leaves Design's CHIP: measured on
        # the live page, an 18x14 bordered pill, `border-radius:9px`, sitting
        # in the hero beside SCIENCE and YOUR TEACHER, on every student's page
        # on every load. That is word for word the thing P6 already ruled
        # against for the environment badge —
        #
        #     "blanking its text leaves a small empty box in the header —
        #      visible, meaningless, and worse than either showing the badge
        #      or not having one"
        #
        # — and the mechanism P6 built for it needed one word here.
        #
        # ⚠️ Safe against the stale-path hazard the `drop` note below records:
        # the other two drops (`envBadge`, `recallLabel`) are in different
        # parents, so no two drops share a parent's child list.
        #
        # The FIXTURE is unmoved — Design supplies "28 students" there, the
        # value is non-empty, and the chip stays exactly as Design drew it.
        ("28 students", "classSize", "drop"),
        ("Biology", "subjectLabel"),
        ("Cells & microscopy", "topicTitle"),
        ("AUTUMN TERM", "termLabel"),
        # ── ⊕ RULED 22 Aug 2026 — P6. THE PROD BADGE SHIPPED TO STUDENTS ──
        #
        # Design drew an environment chip in the header — a bordered `PROD`
        # pill — and it rendered on mrbadmus.com, to children, at phone width
        # where it sits directly under the class name. It is a developer's
        # instrument that had wandered onto the product.
        #
        # RULED: the badge renders only when the environment is NOT
        # production. On mrbadmus.com, nothing at all.
        #
        # ⚠️ IT IS NOT PRUNED, AND THAT IS THE POINT OF THE `drop` FLAG.
        # Pruning would take the badge away from localhost and the test
        # project too, where it is the thing that stops somebody driving the
        # wrong database. So the chip's TEXT becomes data, and the element is
        # dropped when that data is empty — because an empty chip is not
        # nothing, it is a small bordered box with nothing in it, which is
        # worse than either state. `student-live.js` supplies "" on
        # production and the environment's name everywhere else.
        #
        # Design's fixture value is `PROD`, so the fixture and every gate that
        # drives it render exactly what Design drew.
        ("PROD", "envBadge", "drop"),
        # ── ⊕ RULED 22 Aug 2026 — P2. THE ROUND IS min(6, POOL), AND THE
        #    PAGE HAS TO SAY THE SIZE IT IS ACTUALLY GOING TO SHOW ──────────
        #
        # The header announced "SIX QUESTIONS · UNLIMITED ROUNDS" over a
        # counter reading 01/02, because `8r/Sc1` has one covered lesson and
        # therefore two recall rungs. The COUNTER was already right — it reads
        # `this.questions.length` — so the page was not inconsistent by
        # accident; it was consistent everywhere except the three places that
        # spell the number out in a WORD, which is why no search for a digit
        # found them.
        #
        # All three are text nodes Design typed, so they bind. The round size
        # itself needs no change at all: `student-live.js` already stops
        # filling the pool at six, so the round IS min(6, pool) and grows back
        # to six by itself when the Physics and C4+ banks land — with no code
        # change, which is the ruling's own test.
        # ⊕ 23 Aug 2026 — PHASE 2. THE `recallBlurb` ENTRY IS RETIRED, and it
        # is kept here as a comment rather than deleted because deleting it
        # would hide WHY the sentence stopped being on the page.
        #
        #     ("Questions from the lessons this class has covered. Six a
        #       round, unlimited rounds.", "recallBlurb"),
        #
        # Its only text node on the whole class view was node 142, inside the
        # dark sidebar RECALL card — and Design's C2 replaces that card
        # wholesale with the flashcards card (see the graft on live node 136 in
        # student_rulings.py). `text_paths` finds the literal at exactly one
        # path, measured, so with the card gone the literal is gone, and
        # leaving this entry in place would stop the build with "the literal is
        # not a text node in Design's template" — that check working, not
        # failing. `student-live.js` still computes the key; it is unread until
        # a later unit gives the sentence a new home, which is cheaper than
        # deleting a computation that is correct.
        # ⊕ 23 Aug 2026 — PHASE 3. BOTH ENTRIES ARE RETIRED, and they are
        # quoted here rather than deleted for the same reason `recallBlurb`
        # above is — deleting them would hide WHY two sentences stopped being
        # on the page:
        #
        #     ("SIX QUESTIONS · UNLIMITED ROUNDS", "recallEyebrow"),
        #     ("OF SIX", "recallOutOf"),
        #
        # Their only text nodes on the whole class view were 343 and 387, both
        # inside Design's ORIGINAL recall round — and Phase 3 prunes that whole
        # subtree and grafts Design's amended round in its place (see `PRUNE`
        # 335 and the graft of donor 366 in student_rulings.py). `text_paths`
        # finds each literal at exactly one path, measured, so with the round
        # gone the literals are gone, and leaving these entries would stop the
        # build with "the literal is not a text node in Design's template" —
        # that check doing its job.
        #
        # ⚑ P2 IS NOT WEAKENED BY THEIR GOING; IT IS FINISHED BY IT. P2 exists
        # because those two sentences spelled the round size out in a WORD and
        # went on saying SIX over a round of two. What states the size now is
        # `qPos` ("QUESTION 01 / 04") and `roundScore` ("2 / 4"), both computed
        # from `min(6, pool)` in one place in `recallVals`. There is no wording
        # left on the page that CAN be wrong about it.
        #
        # `student-live.js` still computes both keys, and `recallCrumb` with
        # them, exactly as it still computes `recallBlurb` — a correct
        # computation costs nothing and is cheaper than deleting it and
        # rediscovering it.
        #
        # ── ⊕ 23 Aug 2026 — PHASE 3. THE ROUND'S BAND, AND ITS BENCH BUTTON ──
        #
        # ⚠️ THE NON-BREAKING-SPACE TRAP, FOR THE THIRD TIME, and it would have
        # failed the same silent way as `accountClassLine` and
        # `flashcardsTitle`. Design's round opens with
        # `8r/Sc1 \u00a0·\u00a0 RECALL` as ONE text node. `8r/Sc1` is on this
        # list already, but `text_paths` matches the WHOLE node value and
        # nothing less, so this node would not have bound and every student's
        # recall round would have been headed with one real class's name.
        # Composed in student-live.js from the class name it already holds; the
        # separator is Design's typography and is carried verbatim.
        #
        # (The `8r/Sc1` on the round's own back button — donor 373 — is its own
        # text node and binds to `className` for free, which is exactly why the
        # binding table is keyed on the literal rather than on an index.)
        ("8r/Sc1 \u00a0\u00b7\u00a0 RECALL", "recallTitle"),
        # ⛔ AND THE BENCH BUTTON GOES WHEN THERE IS NOTHING TO PRACTISE.
        #
        # `Practise recall` is live node 77, the bench's route into the round,
        # and it is a real control. A class whose covered lessons carry no
        # ladder rungs has an empty bank, and the button would open nothing —
        # the dead control P7 exists to prevent, and `openRecall` refusing to
        # open an empty round is what makes it dead rather than broken.
        #
        # Marked `drop`, so an empty value takes the BUTTON with it rather than
        # leaving a bordered box with nothing in it. That is the `envBadge`
        # shape exactly, and the same reasoning: an empty control is not
        # nothing, it is worse than either state.
        #
        # Design's fixture value is `Practise recall`, and Design's own bank is
        # eight questions long, so the fixture and every gate that drives it
        # render exactly what Design drew.
        #
        # ⚑ `Start recall` (node 88) IS DELIBERATELY NOT GIVEN THE SAME
        # TREATMENT, and that was checked rather than assumed. It lives inside
        # `if fresh`, and `fresh` is `this.props.classState === 'Fresh class'` —
        # the mount emits `props: {}`, so it is false on every ported page and
        # node 88 never renders there at all. Binding it would have added a key
        # nothing can reach, and a `drop` on a node that never draws is a
        # registration that can never be checked.
        ("Practise recall", "recallLabel", "drop"),
        # ── ⊕ RULED 22 Aug 2026 — P4. THE BENCH'S PRIMARY BUTTON ──────────
        # In the OPEN state it opens the assignment. In the DONE state the
        # assignment is finished, and the two actions the ruling asks for are
        # "Revisit the lessons" and "Practise recall" — the second of which
        # Design already drew, sitting right beside this one. So only this
        # label changes, and the bench needs no new markup at all.
        # ⊕ 23 Aug 2026 — PHASE 4. THE THREE SENTENCES ABOVE ARE THE INTERIM,
        # AND THEY ARE KEPT RATHER THAN CORRECTED because they are the reason
        # this binding exists and the reason it now does nothing.
        #
        # Design has DRAWN the done bench (donor 101), it is grafted, and the
        # grid this button lives in no longer renders once the week is
        # finished. So `benchPrimaryLabel` has exactly one value again —
        # Design's own — and `student-live.js` supplies that literal rather
        # than the interim's `Revisit the lesson` / `Practise recall` fork.
        #
        # The binding STAYS. It costs one row in a table and it is the seam a
        # future ruling would need; removing it would mean re-deriving the path
        # to this node the next time the label has an opinion. What came out is
        # the fork, not the join.
        ("Open the assignment", "benchPrimaryLabel"),
        # ── ⊕ 23 Aug 2026 — PHASE 4. DESIGN'S DONE BENCH, DONOR 101 ────────
        #
        # Seven values, and every one of them comes out of the student's own
        # `assignment_submissions` row. Each literal below is Design's amended
        # sample, and each occurs at EXACTLY ONE path in the port after the
        # graft — measured, not assumed: none of the seven is a text node in
        # the live template at all, and the donor's own duplicates (`50%` at
        # donor 48, `Breathing and gas exchange` at donor 63, `COMPLETED` at
        # donor 37, `THIS WEEK'S ASSIGNMENT` at donor 82) all sit in the OPEN
        # branch, which is not grafted.
        #
        # ⚠️ `benchDoneTitle` IS A SECOND KEY FOR THE SAME FACT, AND IT HAS TO
        # BE. The open bench's heading already binds `Cells & microscopy` to
        # `topicTitle`; Design's done bench draws `Breathing and gas exchange`
        # in the same slot. `bindings_for` refuses one key claimed by two
        # different literals — correctly, because a key IS its value and the
        # fixture would then render whichever literal was registered last in a
        # place Design drew the other. So the port carries two names for the
        # topic, each holding its own delivery's sample, and `student-live.js`
        # fills both from the same `current.assignment.topic`. One fact, one
        # source, two fixture values, which is what the amendments' whole
        # sample-data problem looks like whenever it reaches a bound literal.
        #
        # ⚠️ `Practise recall` (donor 116) IS NOT BOUND, and that is not an
        # oversight. It is the same literal as live node 77's own button, it
        # says the same thing in both places, and it has no data behind it in
        # either. `recallLabel` above already claims that literal, and binding
        # a second node to it would be correct but pointless; leaving it is
        # what Design drew. `THE WEEK'S WORK`, `OPENED · ANSWERED ·
        # COMPLETED`, `THIS WEEK'S ASSIGNMENT`, `SCORE`, `RIGHT`, `COMPLETED`,
        # `Revisit this week's lessons` and `Read the feedback` are chrome for
        # the same reason: they are labels, not values.
        ("Breathing and gas exchange", "benchDoneTitle"),
        ("Good week, AY.", "benchDoneLead"),
        ("3 / 3", "benchDoneSteps"),
        ("MARKED", "benchDoneFlag"),
        ("50%", "benchDoneScore"),
        ("2 of 4", "benchDoneRight"),
        ("Wed 20 Aug, 19:42", "benchDoneAt"),
        # ⊕ RULED 22 Aug 2026 — ANOTHER "04", AND ANOTHER ONE THE SCREENSHOT
        # FOUND. The "Lessons in this topic" badge is the literal text `04`,
        # sitting above an `sc-for` over the real list. This class's current
        # assignment draws on ONE lesson, so the page counted four and then
        # listed one, directly underneath itself.
        #
        # It is the same shape as the leaderboard's WEEK 04 and the spine's
        # now-dot: a number Design chose to draw four of something, left
        # standing over real data. Three of them tonight. The count is now the
        # length of the list it counts, which is the only definition that
        # cannot drift — the same fix `shoutCount` already got.
        ("04", "lessonCount"),
        # ⊕ 22 Aug 2026 — TWO SENTENCES A SCREENSHOT CAUGHT AND NO GREP COULD.
        #
        # Both are text nodes in Design's markup, and both are written in
        # SENTENCE CASE and upper-cased by CSS. So the rendered page read
        # "ON THE BENCH NOW · DUE THU 18:00" while the source said
        # "due Thu 18:00" — and every grep for the rendered form, in the page
        # and in the fixture and in the live source, came back empty. The tell
        # list has to be matched against `innerText`, and the seam has to be
        # written against the source; they are not the same bytes.
        #
        # The blurb is worse than a wrong time: it states the question count in
        # WORDS, tells the student to "hand it in" (which W5 retires), and
        # names Thursday as the deadline for every class in every week.
        ('On the bench now · due Thu 18:00', "benchLead"),
        ("Eight questions, set from this week's lessons. Open it, answer them, hand it in before Thursday.", "benchBlurb"),
        # ── ⊕ 23 Aug 2026 — PHASE 1b. THE ACCOUNT SHEET'S TWO REAL ROWS ───
        #
        # Design's sheet carries three hardcoded facts about one sample class:
        # `Mr Badmus`, `8r/Sc1 · SCIENCE` and `Summer · Week 01 / 39`. (The
        # fourth, `ay@school.uk`, is not here because it is not on the page —
        # see `omit` on the graft in student_rulings.py.)
        #
        # `Mr Badmus` needs nothing: it is already on this list, bound to
        # `teacherName`, and `text_paths` binds EVERY node whose text is
        # exactly that literal — so the grafted row binds for free, the moment
        # the graft lands. That is not luck; it is why the binding table is
        # keyed on the literal rather than on an index.
        #
        # ⚠️ THE OTHER TWO ARE NOT EXACT MATCHES FOR ANYTHING ALREADY HERE,
        # and `8r/Sc1 · SCIENCE` is the trap. `8r/Sc1` IS on this list — but
        # the donor's text node is `8r/Sc1\u00a0·\u00a0 SCIENCE`, one string,
        # with NON-BREAKING SPACES around the separator. `text_paths` matches
        # the whole node value and nothing less, so it would not bind, and the
        # sheet would have shipped one real class's name and one real subject
        # under a heading that said the student's own class.
        #
        # Both therefore become their own keys, composed in student-live.js
        # from values it already holds — the class name and the subject pill,
        # the term label and the teaching week. The separator is carried
        # through verbatim, non-breaking spaces and all, because it is Design's
        # typography and not data.
        ("8r/Sc1 \u00a0\u00b7\u00a0 SCIENCE", "accountClassLine"),
        ("Summer \u00a0\u00b7\u00a0 Week 01 / 39", "accountTerm"),
        # ── ⊕ 23 Aug 2026 — PHASE 2. THE FLASHCARD OVERLAY'S HEADING ──────
        #
        # ⚠️ THE SAME TRAP `accountClassLine` DOCUMENTS, ONE FLOOR UP, AND IT
        # WOULD HAVE FAILED THE SAME SILENT WAY. Design's overlay header reads
        # `FLASHCARDS \u00a0·\u00a0 8r/Sc1` — ONE text node, with NON-BREAKING
        # spaces around the separator. `8r/Sc1` is on this list already, but
        # `text_paths` matches the WHOLE node value and nothing less, so this
        # node would not have bound and every student's flashcards would have
        # been headed with one real class's name.
        #
        # Composed in student-live.js from the class name it already holds, so
        # the overlay is not a second opinion about which class this is. The
        # separator is carried through verbatim, non-breaking spaces and all:
        # it is Design's typography, and it is what stops the class name
        # wrapping under the word FLASHCARDS on a 360px phone.
        ("FLASHCARDS \u00a0\u00b7\u00a0 8r/Sc1", "flashcardsTitle"),
    ],
    "assignment": [
        ("8r/Sc1", "className"),
        ("Back to 8r/Sc1", "backToClass"),
        ("Cells & microscopy", "topicTitle"),
        # ── W5, RULED 22 Aug 2026 — "Complete" replaces "Hand it in" ───────
        #
        # The button marks the work FINISHED. It does not transfer it: every
        # answer was already saved the moment it was given, so "hand it in" now
        # describes something that does not happen. Design's typography and
        # placement are untouched; only the words change.
        #
        # ⚑ WHY THESE THREE GO THROUGH BINDINGS AND THE OTHERS THROUGH RULINGS.
        # It is not a preference — it is which mechanism can reach them. These
        # are TEXT NODES in Design's markup, and `student_rulings.LOGIC` only
        # transforms the logic class. Their siblings (`screenLabel`,
        # `doneEyebrow`, `doneKicker`) are computed in `renderVals()`, where
        # BINDINGS cannot reach. Each word is changed by the one mechanism that
        # can see it.
        #
        # ⚠️ THE TRAILING WHITESPACE IS PART OF THE MATCH. Design's compiler
        # keeps the markup's indentation inside the text node, and binding
        # "Hand it in" without it would find nothing and stop the build. That
        # is why the padding is carried through to the replacement too — the
        # same reason `classNamePadded` exists.
        ("Hand it in\n          ", "completeLabel"),
        ("HANDED IN\n          ", "completeChip"),
        ("Handed in", "completeHeading"),
        # ── QUICKFIX-2026-08-24 — "Open lesson 02" NAMED A LESSON THAT IS NOT
        # A NUMBER. Design's sample happened to draw its second lesson; a real
        # assignment's lesson has a slug, never a position, and the digits were
        # never true of anything a student could see. The destination is fixed
        # by SET_ON (node 348, `openLesson`, WRAP-gated on `assignmentLessonHref`
        # — see student_rulings.py); this is only the word.
        ("Open lesson 02", "assignmentLessonLabel"),
    ],
}

# ── one node, one key, where the LITERAL cannot tell two nodes apart ──────
#
# ⊕ 23 Aug 2026 — PHASE 1b, and it exists for exactly one node.
#
# `BINDINGS` is keyed on the literal, which is what lets it bind every copy of
# a value wherever Design typed it. Design's account sheet contains two text
# nodes reading `AY` and they are NOT the same fact:
#
#     donor 252   the 52px avatar disc          → the student's INITIALS
#     donor 254   the 26px name line beside it  → the student's NAME
#
# In Design's amended sample they read alike because that sample's student is
# called `AY`. On a real class they do not: `studentInitials` is `MB` where
# `studentFirstName` is `Mide`, and binding both to the initials would print
# a student's initials twice, in two sizes, where Design drew a monogram and a
# name. The header directly above already says the name — so the sheet would
# have contradicted the page it opened from.
#
# The literal cannot separate them, so this does, by NODE INDEX — the same way
# `SET_ATTR` and `SET_ON` address a node, and asserted the same way.
#
# `{node index: (expected literal, key)}`. The literal is stated and CHECKED,
# not decorative: an index that has drifted onto a different node fails loudly
# instead of binding the class name into the avatar. The key must already be
# claimed by a literal in `BINDINGS`, because that literal is what supplies the
# FIXTURE's value — this table repoints a node at an existing key and never
# invents one.
#
# ⚠️ ONE CONSEQUENCE, STATED RATHER THAN DISCOVERED LATER. The fixture now
# renders `Ayo` in the sheet's name line where Design's amended delivery
# renders `AY`. That is the same class of difference the whole
# `AMENDED_ADDITIONS` mechanism exists to tolerate — the two deliveries carry
# different sample data — and the registration in `student_behaviour.py`
# matches the name as `\S+` for precisely this reason, with a note saying so.
BINDINGS_AT = {
    "class view": {
        10254: ("AY", "studentFirstName"),
    },
    "assignment": {},
}


# ── Design's data welded into METHOD BODIES, not into initialisers ────────
#
# ⚑ THE HALF THE FIRST SEAM COULD NOT REACH, AND WHY IT NEEDED A SECOND ONE.
#
# `seam_logic` lifts class FIELDS (`work = […];`) because a field is a whole
# statement: it can be found by its `^  name =` and cut at its terminating
# `;`. Design's remaining example data is not shaped like that. It is welded
# into `renderVals()` — one value inside a returned object literal, interleaved
# with computation:
#
#     crumbRight: onClass ? (wide ? 'AUTUMN TERM · WEEK 04 / 12' : …) : …,
#     shoutouts: fresh ? [] : [ { who: 'MB', text: 'Best score in the …' } ],
#     boardScopeNote: wk === 'term' ? 'WHOLE AUTUMN TERM' : wk === 4 ? …,
#
# There is no statement to cut and no field to rename, so the previous unit
# named them, counted them and left them — and they shipped in
# `class-ported.html`, which is the one file that must contain no example data
# at all. A production page that reads the work list from the database and
# still tells the class that MB said "best score on digestion this week" is
# the same failure as greeting every student as Ayo; it just took two more
# lines of Design's file to find.
#
# TWO MECHANISMS, both the same discipline as `apply_rulings`: the anchor must
# match EXACTLY ONCE or the build stops naming it. Neither retypes a value —
# each carries Design's own bytes out to the fixture.
#
#   LIFTS     an array or object literal welded into a method body. Anchored on
#             the text immediately before it; the literal itself is taken by
#             BALANCED SCAN (`balanced_group`), so apostrophes, commas and
#             nested braces inside it are just text. The literal becomes
#             `MRB_DATA(key)` and the surrounding expression is untouched —
#             `fresh ? [] : […]` stays a conditional, with only its second arm
#             seamed.
#
#   REWRITES  a value SPLICED INTO a string, where there is no literal to lift
#             because the datum is three characters in the middle of a
#             sentence. The pattern captures Design's value into a named group
#             and the replacement rebuilds the same string from `MRB_DATA`, so
#             the rendered bytes are unchanged when the fixture supplies
#             Design's own value. That equality is not a hope: the fixture IS
#             what the pattern captured.
#
# ⚠️ A capture group whose name is already a BINDING key is not written to the
# fixture — it is CHECKED against it. `termLabel` is bound from the markup
# (`AUTUMN TERM` is a text node in Design's template as well as a substring of
# two of these strings), and one key holding two different values is the bug
# `bindings_for` already refuses. See `rewrite_seams`.

LIFTS = {
    "class view": [
        # The shout-outs. `who`/`meta` name the teacher, `text` is one child's
        # week — every byte of it is one real class's, which is precisely why
        # it cannot ship. The `fresh ? [] : …` conditional stays: an empty
        # class still shows no shout-outs, and that is behaviour, not data.
        dict(key="shoutouts", anchor="      shoutouts: fresh ? [] : "),
        # ⊕ 22 Aug 2026 — THE BENCH CHECKLIST, and it carries two faults at once.
        #
        #     { key: 't2', label: 'Answer the eight questions' },
        #     { key: 't3', label: 'Hand it in' }
        #
        # The first hard-codes the assignment's length IN WORDS, which is why
        # no grep for a digit ever found it, and it sits on the same screen as
        # the docket — so once the docket became data the two contradicted each
        # other in front of the student. The second is W5: the button no longer
        # says that, and neither should the checklist item that names it.
        #
        # Lifted whole rather than patched in place: a three-item checklist
        # about THIS assignment is data about this assignment, and there is no
        # local variable inside it for `balanced_group` to strand.
        dict(key="benchTasks", anchor="    const benchTasks = "),
    ],
}

# ── ⊕ 23 Aug 2026 — PHASE 2. LIFTING A LITERAL OUT OF THE *DONOR* ────────
#
# The graft brings Design's markup across. The FIXTURE then has to render that
# markup, and Design's amended delivery renders it against Design's own six
# sample flashcards — six cards of authored science prose, in a method body:
#
#     deck() {
#       return [ { tag: 'DEFINITION', … }, … ];
#     }
#
# ⚠️ THE OBVIOUS PLACE FOR IT IS `constants`, AND `constants` SAYS IN ITS OWN
# COMMENT WHY NOT. It is "the one place in the build a value is TYPED rather
# than extracted, and it is deliberately small … if it ever grows past a
# handful, the seam has stopped being a seam." Six authored cards is not a
# handful, and retyping them would put a copy of Design's prose in this file
# that drifts from the delivery the first time Design rewrites a card.
#
# So it is lifted, by the same balanced scan `LIFTS` uses, from the DONOR's
# logic instead of the page's. Nothing about the donor's logic is otherwise
# read or shipped — `apply_rulings` takes its TREE and never its behaviour —
# so this is a read of one literal and not a second logic source.
#
# Entry shape: `key` (the fixture key), `anchor` (text immediately before the
# literal, which must occur EXACTLY ONCE), `why`.
DONOR_LIFTS = {
    "class view": [
        dict(key="cards",
             anchor="  deck() {\n    return ",
             why="Design's six sample flashcards, so `class-fixture.html` "
                 "renders the grafted card and overlay exactly as the amended "
                 "delivery draws them. The live page reads a real deck built "
                 "from the lessons the class has covered."),
        # ⊕ 23 Aug 2026 — PHASE 3. Design's eight sample recall questions.
        #
        # The same shape and the same reason as the deck above: the fixture has
        # to render the grafted round exactly as Design's amended delivery
        # draws it, and the value is CARRIED rather than retyped so Design's
        # apostrophes and its `p = F / A` survive unchanged.
        #
        # ⚠️ ALL EIGHT ARE FIXTURE TELLS, registered in
        # `student_page_drive.FIXTURE_TELLS`. If any of them reaches the screen
        # on a page that is supposed to be showing real data, the bank has
        # fallen back to Design's sample and a student is revising one
        # drawing's science. The live bank is every recall and apply rung of
        # every lesson the class has covered, read from `ks3_ladder_questions`.
        dict(key="recallBank",
             anchor="  bank() {\n    return ",
             why="Design's eight sample recall questions, so "
                 "`class-fixture.html` renders the grafted round exactly as "
                 "the amended delivery draws it. The live page reads the real "
                 "recall and apply rungs of the lessons the class has "
                 "covered."),
    ],
}


def donor_lifts(page, donor_logic, fixture):
    """Design's own literals, lifted out of the AMENDED delivery's logic.

    Returns the number lifted. Same discipline as `lift_literals`: the anchor
    must match exactly once or the build stops naming it, and the literal is
    carried as SOURCE so Design's `\u00B7` and apostrophes survive unchanged.
    """
    lifts = DONOR_LIFTS.get(page, ())
    if not lifts:
        return 0
    if donor_logic is None:
        raise SystemExit(
            "build_student_port.py: %r lifts %d literal(s) out of the amended "
            "delivery's logic and there is no %r entry in %s to lift from. "
            "Recompile the templates; a graft whose fixture value is missing "
            "renders an empty surface with a green build."
            % (page, len(lifts), DONOR_PAGE, TEMPLATES))
    for spec in lifts:
        anchor, key = spec["anchor"], spec["key"]
        n = donor_logic.count(anchor)
        if n != 1:
            raise SystemExit(
                "build_student_port.py: %s — the donor seam anchor for %r "
                "occurs %d times in Design's AMENDED logic, not once:\n    %s\n"
                "Design has redrawn it. Re-anchor it in DONOR_LIFTS rather "
                "than dropping it: without the value the fixture renders an "
                "empty version of a surface the gates are asserting against."
                % (page, key, n, anchor.strip()))
        at = donor_logic.index(anchor) + len(anchor)
        lit, _end = balanced_group(donor_logic, at, key)
        if key in fixture:
            raise SystemExit(
                "build_student_port.py: %s — %r is supplied both by the "
                "donor lift and by the page's own seam. One key is one value."
                % (page, key))
        fixture[key] = lit
    return len(lifts)


# (name, pattern, replacement, {capture: "str"|"num"}). `name` appears in the
# failure message; the pattern is matched against Design's logic AFTER the
# rulings and must match exactly once.
REWRITES = {
    "class view": [
        # The crumb rail. Design writes the pair twice — once wide, once
        # narrow — from the same three data: the term, this week, the last
        # week of term. ⊕ 22 Aug 2026 — P2: `SIX A ROUND` USED TO BE LEFT
        # HERE, as "the recall view's own label and not data". That was true
        # while a round was always six. It stopped being true the moment the
        # round became min(6, pool), and it is carried as data now.
        dict(name="crumbRight",
             pat=r"crumbRight: onClass \? \(wide \? "
                 r"'(?P<termLabel>[A-Z][A-Z ]*) \\u00B7 WEEK "
                 r"(?P<weekNumber>\d+) / (?P<weekTotal>\d+)' : "
                 r"'WK (?P=weekNumber) / (?P=weekTotal)'\) : "
                 r"'(?P<recallCrumb>SIX A ROUND)'",
             new="crumbRight: onClass ? (wide ? MRB_DATA('termLabel')"
                 " + ' \\u00B7 WEEK ' + MRB_DATA('weekNumber')"
                 " + ' / ' + MRB_DATA('weekTotal') : "
                 "'WK ' + MRB_DATA('weekNumber')"
                 " + ' / ' + MRB_DATA('weekTotal')) : "
                 "MRB_DATA('recallCrumb')",
             # ⊕ RULED 22 Aug 2026 — P2. `SIX A ROUND` is the RECALL view's
             # own crumb, and the previous seam deliberately left it alone as
             # "the recall view's own label and not data". That was right when
             # a round was six. It is data now, for the same reason the header
             # eyebrow is.
             keys=dict(weekNumber="str", weekTotal="str",
                       recallCrumb="str")),
        # The leaderboard's scope note. `'WHOLE AUTUMN TERM'` embeds the term
        # name; `wk === 4` embeds which week is the current one — a NUMBER,
        # compared with `===`, so it is carried as a number and not as the
        # padded string. `'WEEK ' + pad(wk)` is computed from the week the
        # student picked and stays as Design wrote it.
        dict(name="boardScopeNote",
             pat=r"boardScopeNote: wk === 'term' \? "
                 r"'WHOLE (?P<termLabel>[A-Z][A-Z ]*)' : "
                 r"wk === (?P<currentWeek>\d+) \?",
             new="boardScopeNote: wk === 'term' ? "
                 "'WHOLE ' + MRB_DATA('termLabel') : "
                 "wk === MRB_DATA('currentWeek') ?",
             keys=dict(currentWeek="num")),
        # ⊕ 22 Aug 2026 — the shout-out BADGE, which the array beside it
        # outgrew. `shoutouts` has been data since the first method-body seam,
        # so a class with three shout-outs rendered three cards under a badge
        # reading `02`. It needs no key of its own: the count is the length of
        # the list it is counting, which is the only definition that cannot
        # drift. Design's fixture has two, so `pad(2)` is `02` and the render
        # is unchanged.
        dict(name="shoutCount",
             # No capture group at all: nothing here becomes data, so there is
             # nothing to carry to the fixture and nothing to check against a
             # binding. A named group would be read as one or the other.
             pat=r"shoutCount: fresh \? '00' : '\d+'",
             new="shoutCount: pad(fresh ? 0 : MRB_DATA('shoutouts').length)",
             keys={}),
        # ⚑ NOT ON THE BRIEF, AND NOT OPTIONAL. Two more copies of the current
        # week number, both spliced mid-sentence, neither anywhere near the
        # crumb rail: the readings strip's `ANSWERED · WK 04` and the work
        # row's `COUNTS TOWARDS WEEK 04`. They were found by grepping the
        # BUILT page for the week rather than by reading the brief, which is
        # the only way either would have been found — a datum that appears in
        # four places is a datum that looks closed after you fix three.
        # ⊕ RULED 22 Aug 2026 — P9. THE TERM SPINE'S "NOW" IS THREE FOURS,
        # NOT ONE, AND NOT ONE OF THEM IS A STRING.
        #
        #     trough:   n <= 4 ? 'var(--st-rule-fact)' : 'var(--st-crumb-bg)'
        #     numColor: … n === 4 ? 'var(--ks3-accent-text)' : …
        #     nowDot:   n === 4 ? 'var(--st-accent)' : 'transparent'
        #
        # The same shape of defect as the leaderboard's WEEK 04 default, and it
        # hid the same way: there is no "04" anywhere to grep for, only the
        # numeral 4 in three comparisons. Every text search over the built page
        # came back clean while the picture showed the marker four weeks into a
        # term that is one week old. A screenshot caught it; no tell could.
        #
        # ⚑ THE FIRST OF THE THREE WAS NOT ON THE BRIEF. The brief names the
        # dot. But `trough` shades weeks 1-4 as ALREADY ELAPSED, so a class in
        # week 1 drew three weeks of school that have not happened yet in the
        # "done" tone — a wrong statement about the past sitting directly under
        # a wrong statement about the present. Found by reading the whole block
        # rather than the line the brief pointed at.
        #
        # Two seams rather than one because the three are not contiguous:
        # `stackH`, `segs` and `ring` sit between them, and `rewrite_seams`
        # splices the replacement in literally — it does not run `re.sub`, so a
        # pattern spanning the gap could not put back what it matched.
        #
        # `currentWeek` is already captured as 4 by `boardScopeNote` above, so
        # both of these are CHECKED against it rather than written twice. If
        # Design ever redraws the spine around a different week, the build
        # stops instead of shipping two "now"s.
        dict(name="spine — trough (weeks drawn as elapsed)",
             pat=r"trough: n <= (?P<currentWeek>\d+) \? "
                 r"'var\(--st-rule-fact\)' : 'var\(--st-crumb-bg\)'",
             new="trough: n <= MRB_DATA('currentWeek') ? "
                 "'var(--st-rule-fact)' : 'var(--st-crumb-bg)'",
             keys=dict(currentWeek="num")),
        dict(name="spine — numColor / nowDot (the NOW marker)",
             pat=r"numColor: sel \? 'var\(--st-ink\)' : "
                 r"n === (?P<currentWeek>\d+) \? "
                 r"'var\(--ks3-accent-text\)' : 'var\(--st-ghost\)',\n"
                 r"        nowDot: n === (?P=currentWeek) \? "
                 r"'var\(--st-accent\)' : 'transparent'",
             new="numColor: sel ? 'var(--st-ink)' : "
                 "n === MRB_DATA('currentWeek') ? "
                 "'var(--ks3-accent-text)' : 'var(--st-ghost)',\n"
                 "        nowDot: n === MRB_DATA('currentWeek') ? "
                 "'var(--st-accent)' : 'transparent'",
             keys=dict(currentWeek="num")),
        dict(name="readings — ANSWERED · WK nn",
             pat=r"caption: 'ANSWERED \\u00B7 WK (?P<weekNumber>\d+)'",
             new="caption: 'ANSWERED \\u00B7 WK ' + MRB_DATA('weekNumber')",
             keys=dict(weekNumber="str")),
        dict(name="work row — COUNTS TOWARDS WEEK nn",
             pat=r"'COUNTS TOWARDS WEEK (?P<weekNumber>\d+)'",
             new="'COUNTS TOWARDS WEEK ' + MRB_DATA('weekNumber')",
             keys=dict(weekNumber="str")),
        # ⚑ ALSO NOT ON THE BRIEF, AND A NAME RATHER THAN A FIGURE. A piece of
        # work awaiting marking reads `WITH MR BADMUS` — the teacher's real
        # name, upper-cased, welded into a status word where no grep for
        # `Mr Badmus` would ever find it. `teacherName` is already bound from
        # the markup, so nothing new is carried: the capture is CHECKED
        # against that binding through the same `upper` transform the label
        # applies, which is why the two cannot drift apart.
        # ⊕ 22 Aug 2026 — W5, in the readings strip. `label: 'Handed in'` and
        # `caption: 'OF HANDED IN'` are computed in a method, so BINDINGS
        # cannot see them and the words have to travel as data. The fixture
        # carries Design's own two strings, so Design's render is unchanged and
        # nothing has to be registered as a divergence; the live source supplies
        # "Completed" and "OF COMPLETED".
        dict(name="readings — Handed in",
             pat=r"\{ label: '(?P<handedLabel>Handed in)', value: all\.length",
             new="{ label: MRB_DATA('handedLabel'), value: all.length",
             keys=dict(handedLabel="str")),
        dict(name="readings — OF HANDED IN",
             pat=r"caption: '(?P<handedCaption>OF HANDED IN)'",
             new="caption: MRB_DATA('handedCaption')",
             keys=dict(handedCaption="str")),
        dict(name="work row — WITH <teacher>",
             pat=r"w\.status === 'pending' \? "
                 r"'WITH (?P<teacherName>[A-Z][A-Z ]*)'",
             new="w.status === 'pending' ? "
                 "'WITH ' + MRB_DATA('teacherName').toUpperCase()",
             keys={}, check=dict(teacherName="upper")),

        # ── THE FIGURES ──────────────────────────────────────────────────
        #
        # Everything below this line is a NUMBER rather than a name, which is
        # why none of it was caught by the greps that gate the identity
        # strings and why the previous unit could name it, count it and leave
        # it. It is example data all the same: `46` is one child's answered
        # count, `2 days left` is one Thursday, `Using a microscope` is one
        # week's lesson. On the production page every one of them is not
        # merely stale but WRONG, and wrong in the direction a student would
        # believe — a page that says the deadline is two days away is not
        # obviously broken the way a page greeting them as Ayo is.
        #
        # ⚠️ ORDER MATTERS FOR ONE OF THEM. The readings strip's `caption` is
        # already rewritten by `readings — ANSWERED · WK nn` above, so the two
        # seams below are written against the line AS IT IS BY THEN: they
        # anchor on `value:` and on `pct:` and never on the caption between
        # them. A pattern spanning all three would match Design's delivery and
        # not the logic these run on.
        dict(name="readings — recall answered",
             pat=r"\{ label: 'Recall', value: fresh \? '0' : "
                 r"'(?P<recallAnswered>\d+)'",
             new="{ label: 'Recall', value: fresh ? '0' : "
                 "MRB_DATA('recallAnswered')",
             keys=dict(recallAnswered="str")),
        dict(name="readings — recall percentage",
             pat=r"pct: fresh \? '0%' : '(?P<recallPct>\d+%)' \}",
             new="pct: fresh ? '0%' : MRB_DATA('recallPct') }",
             keys=dict(recallPct="str")),
        # The same 46, spliced a second time 280 lines further down as the
        # retrieval room's own count. ONE KEY, TWO USES — deliberately: if the
        # strip and the room ever disagreed about how many questions a student
        # has answered, one of them would be lying, and `rewrite_seams`
        # refuses a key captured as two different values.
        dict(name="retrievalCount",
             pat=r"retrievalCount: fresh \? '0' : '(?P<recallAnswered>\d+)'",
             new="retrievalCount: fresh ? '0' : MRB_DATA('recallAnswered')",
             keys=dict(recallAnswered="str")),

        # The docket — this week's assignment, four facts about it. ⚠️ ONLY
        # THE `value:` IS TAKEN. `font:` on three of these four reads
        # `'500 ' + bigVal + '/1.3 …'`, and `bigVal` is a LOCAL CONST of
        # `renderVals()`. Lifting the objects whole would carry that
        # expression into the fixture, where `bigVal` is not in scope, and the
        # page would throw on mount. The typography is Design's and stays
        # exactly where Design put it; only the four data go.
        dict(name="docket — QUESTIONS",
             pat=r"\{ label: 'QUESTIONS', value: '(?P<docketQuestions>\d+)'",
             new="{ label: 'QUESTIONS', value: MRB_DATA('docketQuestions')",
             keys=dict(docketQuestions="str")),
        dict(name="docket — DRAWS ON",
             pat=r"\{ label: 'DRAWS ON', value: '(?P<docketDrawsOn>[^']*)'",
             new="{ label: 'DRAWS ON', value: MRB_DATA('docketDrawsOn')",
             keys=dict(docketDrawsOn="str")),
        dict(name="docket — SET",
             pat=r"\{ label: 'SET', value: '(?P<docketSet>[^']*)'",
             new="{ label: 'SET', value: MRB_DATA('docketSet')",
             keys=dict(docketSet="str")),
        dict(name="docket — DUE",
             pat=r"\{ label: 'DUE', value: '(?P<docketDue>[^']*)'",
             new="{ label: 'DUE', value: MRB_DATA('docketDue')",
             keys=dict(docketDue="str")),
        # The docket's countdown strip. `fresh ?` keeps its empty-class arm —
        # `No deadline` and `—` are what a class with nothing set says, which
        # is behaviour rather than data.
        # ⊕ RULED 22 Aug 2026 — P4, FOUND IN THE SCREENSHOT AND NOT IN ANY
        # CHECK. The docket sits directly above the bench, and while the bench
        # was being taught a done state the docket went on saying `OPEN` and
        # `14 days left` over a piece of work the student had finished. Two
        # statements about the same assignment, contradicting each other, two
        # inches apart — the exact fault P4 exists to remove, in the panel
        # above the one the brief names.
        #
        # No text check could have caught it: `OPEN` is a correct word for an
        # open assignment, and every drive that had a docket had an open one.
        # A picture caught it, on the first look, which is the second time
        # tonight that has happened.
        dict(name="docketFlag",
             pat=r"docketFlag: fresh \? 'BENCH CLEAR' : '(?P<docketFlag>OPEN)'",
             new="docketFlag: fresh ? 'BENCH CLEAR' : MRB_DATA('docketFlag')",
             keys=dict(docketFlag="str")),
        dict(name="docketLeft",
             pat=r"docketLeft: fresh \? 'No deadline' : "
                 r"'(?P<docketLeft>[^']*)'",
             new="docketLeft: fresh ? 'No deadline' : MRB_DATA('docketLeft')",
             keys=dict(docketLeft="str")),
        dict(name="docketWorth",
             pat=r"docketWorth: fresh \? '\\u2014' : "
                 r"'(?P<docketWorth>[^']*)'",
             new="docketWorth: fresh ? '\\u2014' : MRB_DATA('docketWorth')",
             keys=dict(docketWorth="str")),
        dict(name="docketElapsed",
             pat=r"docketElapsed: fresh \? '0%' : "
                 r"'(?P<docketElapsed>\d+%)'",
             new="docketElapsed: fresh ? '0%' : MRB_DATA('docketElapsed')",
             keys=dict(docketElapsed="str")),

        # The work row's status words for a piece of work still open. `DUE THU
        # 18:00` is one assignment's deadline written into a status vocabulary
        # — every open assignment in the class reads it, whatever its own due
        # date. The wide and narrow forms are two different strings and so two
        # different keys; the `pending` / `missed` / `marked` arms are status
        # words rather than data and stay.
        dict(name="work row — DUE (wide)",
             pat=r"const longWord = w\.status === 'open' \? "
                 r"'(?P<dueWordLong>DUE [A-Z]{3} \d{2}:\d{2})' :",
             new="const longWord = w.status === 'open' ? "
                 "MRB_DATA('dueWordLong') :",
             keys=dict(dueWordLong="str")),
        dict(name="work row — DUE (narrow)",
             pat=r"const shortWord = w\.status === 'open' \? "
                 r"'(?P<dueWordShort>DUE [A-Z]{3})' :",
             new="const shortWord = w.status === 'open' ? "
                 "MRB_DATA('dueWordShort') :",
             keys=dict(dueWordShort="str")),

        # The round's closing line. LIFTED WHOLE, not spliced: `Six` and
        # `Week 04` are the two figures in it, and rebuilding the sentence
        # around them would fix the sentence in place — on real data it is a
        # different sentence ("One answer logged…", and nothing says the
        # weighting stays 20 of 100). One string, one key.
        # ⊕ 23 Aug 2026 — PHASE 3. RETIRED WITH THE LINE IT SEAMED. Quoted
        # rather than deleted, because it is the seam that made the sentence
        # removable in the first place:
        #
        #     dict(name="roundNote",
        #          pat=r"roundNote: '(?P<roundNote>[A-Z][a-z]+ answers? logged
        #              against Week \d+\. Recall is worth \d+ of the \d+
        #              points on the leaderboard\.)'", …)
        #
        # `roundNote` was removed from Design's logic entirely by the Phase 3
        # ruling, along with the other nineteen keys only the pruned round read.
        # The sentence it carried — *"Recall is worth 20 of the 100 points on
        # the leaderboard"* — stays gone, and it is now refused in TWO places
        # rather than emptied in one: the original's key does not exist, and
        # Design's amended delivery draws the same sentence again at donor node
        # 439, which the graft omits. Registered in `AMENDED_OMISSIONS`.

        # ⚑ `Math.max(9, st.streak)` IS NOT A DEFAULT — IT IS A FLOOR ON A
        # REAL CHILD'S RECORD. Design needed the example streak to read `09`
        # and wrote the nine into the max. Shipped, it tells a student whose
        # best run is three that their best run is nine, and it does it in the
        # one place on the page that is purely their own achievement. The
        # floor now comes from data: the fixture carries Design's 9 as a
        # NUMBER so Design's own render is byte-identical, and the live source
        # supplies 0, which makes the `Math.max` a no-op and lets the real
        # streak — however small — through.
        # ⊕ 23 Aug 2026 — PHASE 3. RETIRED WITH THE LINE IT SEAMED, and the
        # note above it is kept because it is the reasoning, not the mechanism:
        #
        #     dict(name="recallStats",
        #          pat=r"recallStats: \[\{ label: 'BEST STREAK', value:
        #              pad\(Math\.max\((?P<bestStreakFloor>\d+), st\.streak\)\)
        #              \}, \{ label: 'ROUNDS', value: '(?P<recallRounds>\d+)' \}\]", …)
        #
        # `recallStats` is one of the twenty keys removed with Design's original
        # round. BEST STREAK and ROUNDS are drawn again in Design's AMENDED
        # delivery — in the THIS WEEK panel at donor 425 — and that panel is
        # omitted on the way in, because both figures are facts nothing records
        # and the third one beside them, ANSWERED, is the same. `bestStreakFloor`
        # therefore has no floor left to lift: there is no `Math.max` on the page.

        # ── THE SIX-QUESTION ROUND, WHICH IS NOT DATA AND NOT A KEY ───────
        #
        # These two carry NOTHING to the fixture. Design's recall round is six
        # questions long and the six is written into the meter, the counter,
        # the percentage, the live/done test and the index clamp — five places,
        # none of which reads the array it is counting. A seven-question round
        # would stop at six with `QUESTION 06 / 06` on the screen and a
        # question still unanswered; a five-question round would run off the
        # end of the array. So the length comes from `this.questions.length`,
        # which is the round itself, and there is no key because there is
        # nothing here a data source should get to decide.
        #
        # The division is guarded: an empty round is `0%` and not `NaN%`.
        # Design's own round has six questions, so every string below renders
        # the same bytes it did — that equality is the check on this one.
        # ⊕ 23 Aug 2026 — PHASE 3. BOTH ARE RETIRED, and the paragraph above
        # is kept because its REASONING is what Phase 3 finishes rather than
        # abandons: "the length comes from the round itself, and there is no
        # key because there is nothing here a data source should get to decide".
        #
        #     dict(name="recall round — length from this.questions", …)
        #     dict(name="recall round — index clamp",
        #          pat=r"const qi = Math\.min\(st\.qi, 5\);", …)
        #
        # Every line either of them anchored on — `recallMeter`,
        # `recallMeterPct`, `roundLive`, `qCounter`, `const qi` — is removed
        # with Design's original round. The amended round computes its own
        # length ONCE, in `recallSize()`, as `min(6, bank.length)`, and every
        # number the surface prints is derived from it: `qPos`, `roundScore`,
        # `qpips`, `nextLabel`, the round's last-question test and the progress
        # bar's scale. Still no key, and still for the same reason.

    ],
}


_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED: Claude Design's own template and Design's own logic class,
  rendered by shared/student-runtime.js. No React and none of Design's
  `support.js` ships here — that was ruled on 20 Aug 2026.

  The markup is not retyped and neither is the behaviour. Both are extracted
  from docs/ks3/design-reference/student/ by student_template.py, so the only
  way this can differ from Design's file is if Design's file changed.

  ⊕ THIS IS THE LIVE PAGE, as of 22 Aug 2026. It used to say the opposite —
  "the live pages are student/class.html and student/assignment.html and this
  build never writes them" — and that was true until the swap. The hand-written
  originals are retired in docs/ks3/retired/ under that date.

  It follows that this file is NOT hand-editable, and the warning at the top is
  not a formality: a fix typed in here survives exactly until the next build.
  Changes to Design's logic belong in student_rulings.py, changes to what the
  page renders belong in shared/student-live.js, and changes to the markup
  belong to Design.

  THERE IS NO DATA IN THIS FILE. Design's example values — the work list, the
  roster, the week points, the questions, and the identity strings that were
  typed into the markup — have been lifted out into `window.__MRB_DATA__`, and
  every read of them goes through `MRB_DATA(k)`, which THROWS when the key is
  absent. So this page cannot render one child's homework to a different
  child: with no data source loaded it renders nothing at all and says why.
  The data arrives from %s, and from nowhere else.

  Its twin, %s, is this same file with two differences and no others — this
  comment, and the script tags at the end, where it loads Design's own
  extracted example values and mounts. That twin is what student_parity.py and
  student_behaviour.py drive, which is how Design's data can still be exercised
  in full without being reachable from here.
  ══════════════════════════════════════════════════════════════════════════
-->
"""

_BANNER_FIXTURE = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED — THE FIXTURE PAGE. The same file as %s but for this comment and
  the script tags at the end: this one loads Design's own extracted example
  data and mounts, that one loads the live data source and does not.

  ⛔ NOT A CANDIDATE FOR ANY LIVE PATH, and not because it is unfinished — it
  is one real class, hard-coded, for every visitor. It exists so the gates have
  something with known values to drive: `student_parity.py` compares its render
  against Design's own file and `student_behaviour.py` drives both through the
  same 28 journeys. A gate that drove the production page would be asserting
  against whatever the database happened to hold that morning.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def _refuse(path):
    if os.path.basename(path) in _REFUSED:
        raise SystemExit(
            "build_student_port.py REFUSES to write %s — that is a LIVE "
            "student page." % path)


def ds_css():
    """Design's six stylesheets, in Design's own link order, as one file.

    ⚠️ NOT THE SITE'S OWN COPIES. `shared/tokens.css` and `shared/ks3.css` have
    both grown well past the versions in Design's bundle — measured, 31.8 KB
    against 24.5 KB and 548 KB against 42.5 KB — so linking the site's files
    would give the page a cascade Design never drew and never checked. Design's
    are vendored, which is also what makes the parity gate meaningful.

    Reconciling the two is real work and it is NOT this build's: it would
    change what KS3 lesson pages render as well, and it belongs with the
    already-open note about `--ks3-data` being in the engine's tokens and not
    in Design's.
    """
    order = ["tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
             "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css",
             "styles.css"]
    out, sizes = [], []
    for rel in order:
        path = os.path.join(DS, rel)
        if not os.path.exists(path):
            raise SystemExit("build_student_port.py: missing %s" % path)
        css = open(path, encoding="utf-8").read()
        if rel.endswith("fonts.css"):
            # The faces point at `./` inside the bundle; the site self-hosts
            # every one of the seven at /shared/fonts/ and they are
            # byte-identical (verified by sha256 in build_student.py).
            css = css.replace("./", SERVED_FONTS)
        out.append("/* ── %s ── */\n%s" % (rel, css))
        sizes.append((rel, len(css)))
    return "\n\n".join(out), sizes


# ── every token the page references must resolve ──────────────────────────
#
# ⚑ THIS EXISTS BECAUSE ONE DID NOT, AND THE PAGE STILL LOOKED FINE. The ruled
# fix to the recall `CORRECT` label points it at `--ks3-ok-dark`, minted under
# MRB-252 in `shared/tokens.css`. Design's `_ds` bundle predates that mint and
# does not define it, so the label resolved to the INHERITED ink — measured,
# rgb(34,30,27) where #40DD84 was intended. No error, no warning; a green word
# quietly became a black one, and the token-contract gate went green because a
# black word is not a `--st-ok-room` violation either.
#
# An undefined custom property is the quietest failure CSS has. So the build
# collects every `var(--…)` the template and the logic reference, checks each
# against what the stylesheets actually define, and tops up the difference from
# the site's own `shared/tokens.css` — by NAME, read out of that file, never
# retyped. Anything still unresolved stops the build.
_VAR_RE = None


def referenced_tokens(tpl):
    """Every `--custom-property` the template or the logic asks for."""
    import re as _re
    blob = json.dumps(tpl["roots"]) + tpl["logic"] + json.dumps(tpl["imports"])
    return set(_re.findall(r"var\(\s*(--[a-zA-Z0-9-]+)", blob))


def defined_tokens(css, tpl=None):
    """Every custom property the page can resolve — from CSS AND from markup.

    ⚠️ THE MARKUP HALF IS NOT OPTIONAL. Design declares `--st-ok-room` inline on
    the design root (`--st-ink:var(--ks3-ink);--st-ok-room:#55B36A` in the
    root's own style attribute) rather than in a stylesheet, which is exactly
    what the handoff note says it did — "Declared on the design root, not in
    the token files". A scan that read only the stylesheets called it undefined
    and stopped the build on a token that resolves perfectly well.

    (The canonical copy now lives in `3d-studio/src/styles/tokens.css` under the
    20 Aug 2026 ruling. The inline declaration is byte-identical to it and is
    what actually paints, being on the element; the token-file entry is what
    makes Design's NEXT delivery inherit the value instead of re-declaring it.)
    """
    import re as _re
    found = set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", css))
    if tpl:
        blob = json.dumps(tpl["roots"])
        found |= set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", blob))
    return found


def top_up(css, wanted, tpls):
    """Define, from shared/tokens.css, any token the bundle is missing."""
    import re as _re
    have = defined_tokens(css)
    for name, t in tpls.items():
        # ⚠️ THE DONOR DOES NOT COUNT. Its tree defines Design's `--b-*` and
        # `--pg-*` families, and it is not on the page — only the subtrees
        # GRAFTED out of it are. Counting them here would let a token that is
        # referenced by the live page and defined only in the delivery pass as
        # resolved, and an undefined custom property does not error: it falls
        # back to the inherited value and the page looks almost right.
        if name == DONOR_PAGE:
            continue
        have |= defined_tokens("", t)
    missing = sorted(wanted - have)
    if not missing:
        return css, []
    site = open(os.path.join("shared", "tokens.css"), encoding="utf-8").read()
    lines, still = [], []
    for name in missing:
        m = _re.search(r"%s\s*:\s*([^;]+);" % _re.escape(name), site)
        if m:
            lines.append("  %s: %s;" % (name, m.group(1).strip()))
        else:
            still.append(name)
    if still:
        raise SystemExit(
            "build_student_port.py: %d token(s) the page references are "
            "defined NOWHERE — not in Design's bundle and not in "
            "shared/tokens.css: %s.\n"
            "  An undefined custom property does not error; it falls back to "
            "the inherited value and the page looks almost right. Define them "
            "or stop referencing them." % (len(still), ", ".join(still)))
    block = ("\n\n/* ── minted since Design's bundle, read out of "
             "shared/tokens.css ──\n"
             "   Design's `_ds` drop predates MRB-252, which minted the two\n"
             "   body-size greens. Values are COPIED FROM the site's token\n"
             "   file at build time rather than retyped, so they cannot\n"
             "   drift from it. */\n:root,\n.rd[data-mode=\"ks3\"] {\n%s\n}\n"
             % "\n".join(lines))
    return css + block, missing


# ── Mide's rulings, applied to Design's delivery at build time ────────────
#
# ⚑ THESE WERE HAND-EDITED INTO THE GENERATED PAGES ONCE, AND A REBUILD ATE
# THEM. Commit 895f34766 applied three of Mide's rulings to
# `student/class-ported.html` and `student/assignment-ported.html` — files this
# script writes and whose own banner says "GENERATED — do not edit". They
# survived until the next build, which is this one, and the behaviour gate went
# red in thirteen places naming a divergence that had been correctly applied
# hours earlier.
#
# So they are applied HERE now, from `student_rulings.py`, on the way from
# Design's delivery to the page. See that file for what each ruling is and for
# the full account of the recovery. Nothing about their content changed.


def apply_rulings(page, logic, roots, donor=None):
    """Design's logic and template with Mide's rulings applied.

    Returns (logic, roots, replacements, pruned, wired, grafted, attred,
    exprd, wrapped, moved). Every `old` must appear
    EXACTLY ONCE — not zero times, and not twice. A ruling that silently
    matched nothing is the same failure as the hand-edit it replaces: the build
    goes green and the ruling is not in the page.
    """
    import student_rulings

    reps = student_rulings.LOGIC.get(page, ())
    for old, new in reps:
        n = logic.count(old)
        if n != 1:
            raise SystemExit(
                "build_student_port.py: the MRB-275 ruling for %r anchors on a "
                "span that appears %d times in Design's logic, not once:\n"
                "    %s…\n"
                "Design has redrawn that span. The ruling is Mide's and still "
                "stands; re-anchor it in student_rulings.py rather than "
                "dropping it, and do NOT hand-edit the built page — that is "
                "exactly how it was lost the first time."
                % (page, n, old.strip().split("\n")[0][:78]))
        logic = logic.replace(old, new, 1)

    prune = set(student_rulings.PRUNE.get(page, ()))
    removed = [0]

    def walk(node):
        if not isinstance(node, dict) or not node.get("c"):
            return
        kept = []
        for kid in node["c"]:
            if isinstance(kid, dict) and kid.get("i") in prune:
                removed[0] += 1
                prune.discard(kid.get("i"))
                continue
            walk(kid)
            kept.append(kid)
        node["c"] = kept

    roots = json.loads(json.dumps(roots))
    for root in roots:
        walk(root)
    if prune:
        raise SystemExit(
            "build_student_port.py: the MRB-275 ruling for %r prunes template "
            "node(s) %s, and they are not in Design's template. The ruling "
            "stands; re-read the delivery and re-anchor it."
            % (page, sorted(prune)))

    # ── subtrees grafted from Design's amended delivery ──────────────────
    #
    # ⊕ 22 Aug 2026. See `GRAFT` in student_rulings.py for why the amendments
    # are merged by region instead of replacing the live template.
    #
    # Runs BEFORE the handler pass on purpose: a grafted subtree carries
    # Design's own `onClick` expressions, and `SET_ON` must be able to see and
    # refuse to overwrite them like any other.
    grafts = list(student_rulings.GRAFT.get(page, ()))
    grafted = [0]
    if grafts and donor is None:
        raise SystemExit(
            "build_student_port.py: %r has %d graft(s) but no donor tree was "
            "passed. The donor is the compiled 'class view amendments' entry "
            "in %s; without it there is nothing to graft FROM."
            % (page, len(grafts), TEMPLATES))

    def _index(tree):
        found = {}

        def walk(n):
            if isinstance(n, dict):
                if n.get("i") is not None:
                    found[n["i"]] = n
                for kid in n.get("c") or []:
                    walk(kid)

        for r in (tree or []):
            walk(r)
        return found

    def _renumber(node):
        """Design's subtree, deep-copied, with every index moved clear of the
        live page's. Text nodes have no index and keep none."""
        out = json.loads(json.dumps(node))

        def walk(n):
            if isinstance(n, dict):
                if n.get("i") is not None:
                    n["i"] = student_rulings.GRAFT_BASE + n["i"]
                for kid in n.get("c") or []:
                    walk(kid)

        walk(out)
        return out

    def _omit(sub, drop, why):
        """Donor subtrees a graft deliberately does NOT copy.

        ⊕ 23 Aug 2026 — 1c, the EMAIL row. Runs INSIDE the graft, on the
        donor's own numbering, before `_renumber` — which is the only place it
        can run.

        ⚠️ `PRUNE` CANNOT DO THIS, and the order of this function is why:
        `PRUNE` walks the LIVE template near the top of `apply_rulings` and
        asserts every index it was given was found. At that moment the donor
        has not been copied in, so naming a grafted node there raises rather
        than removing anything.

        ⚠️ AND IT IS NOT `BINDINGS`' `drop`, which is a different rule with a
        different lifetime: `drop` removes an element AT RUNTIME when its
        BOUND VALUE turns out to be empty, and puts it back when it is not.
        This removes markup at BUILD TIME, so there is no state in which the
        subtree exists. Two mechanisms, two names, on purpose.

        Every index must be PRESENT in the donor subtree. A stale entry —
        Design redraws, the row moves, the number comes to mean something
        else — stops the build rather than omitting nothing and shipping the
        thing the ruling exists to remove, which is the failure mode that
        looks exactly like success.
        """
        want = set(drop)
        if not want:
            return sub
        seen = set()

        def walk(n):
            if not isinstance(n, dict) or not n.get("c"):
                return
            kept = []
            for kid in n["c"]:
                if isinstance(kid, dict) and kid.get("i") in want:
                    seen.add(kid["i"])
                    continue
                walk(kid)
                kept.append(kid)
            n["c"] = kept

        if sub.get("i") in want:
            raise SystemExit(
                "build_student_port.py: the graft %r omits donor node %s, "
                "which is the grafted subtree's own ROOT. Omitting the root "
                "omits the whole graft; graft something else, or drop the "
                "graft." % (why[:60], sub.get("i")))
        walk(sub)
        missing = sorted(want - seen)
        if missing:
            raise SystemExit(
                "build_student_port.py: the graft %r omits donor node(s) %s, "
                "and they are not in the subtree it copies. The omission is a "
                "RULING and it still stands — Design has redrawn that part of "
                "the delivery, so re-read it and re-anchor the index. Leaving "
                "a stale number here would omit NOTHING and ship exactly what "
                "the ruling exists to remove, with a green build."
                % (why[:60], missing))
        return sub

    if grafts:
        donor_by_i = _index(donor)
        live_by_i = _index(roots)
        parent_of = {}

        def note_parents(n):
            if isinstance(n, dict):
                for kid in n.get("c") or []:
                    if isinstance(kid, dict):
                        parent_of[id(kid)] = n
                    note_parents(kid)

        for r in roots:
            note_parents(r)

        for g in grafts:
            if not g.get("why"):
                raise SystemExit(
                    "build_student_port.py: a graft on %r states no reason. "
                    "`why` is required — a graft with no stated reason is a "
                    "redesign nobody signed off." % page)
            at, mode, src = g["at"], g["mode"], g["donor"]
            if at not in live_by_i:
                raise SystemExit(
                    "build_student_port.py: the graft %r anchors on live "
                    "template node %s, which is not in Design's live "
                    "template. Design has redrawn it; re-anchor the graft "
                    "rather than dropping it." % (g["why"][:60], at))
            if src not in donor_by_i:
                raise SystemExit(
                    "build_student_port.py: the graft %r copies donor node "
                    "%s, which is not in the amended delivery. The delivery "
                    "moved; re-anchor the graft." % (g["why"][:60], src))
            sub = _omit(json.loads(json.dumps(donor_by_i[src])),
                        g.get("omit") or (), g["why"])
            sub = _renumber(sub)
            target = live_by_i[at]
            if mode in ("append", "prepend"):
                kids = target.setdefault("c", [])
                kids.insert(len(kids) if mode == "append" else 0, sub)
            elif mode in ("replace", "after"):
                parent = parent_of.get(id(target))
                if parent is None:
                    raise SystemExit(
                        "build_student_port.py: the graft %r asks to %s live "
                        "node %s, which is a template ROOT and has no parent "
                        "to hold the result." % (g["why"][:60], mode, at))
                kids = parent["c"]
                pos = kids.index(target)
                if mode == "replace":
                    kids[pos] = sub
                else:
                    kids.insert(pos + 1, sub)
            else:
                raise SystemExit(
                    "build_student_port.py: the graft %r has mode %r. It must "
                    "be replace, append, prepend or after."
                    % (g["why"][:60], mode))
            grafted[0] += 1

    # ── the ONE name two of Design's surfaces both want ──────────────────
    #
    # ⊕ 23 Aug 2026 — PHASE 2, and it was found by DRIVING, not by reading.
    #
    # Design's flashcard overlay draws a row of position pips from
    # `<for e="pips">`. So does the live page's RECALL ROUND, which Design drew
    # months earlier — `renderVals` line 673, `pips: pips`, built from
    # `this.questions`. Both loops resolve the same name out of the same scope
    # object, and the class-view spread lands EARLIER in that object literal
    # than the recall round's key, so the recall round's list won: the
    # flashcards overlay rendered TWO pips for an eleven-card deck, each with
    # no `data-on` at all, and nothing errored anywhere.
    #
    # ⚠️ AND THEY ARE NOT MUTUALLY EXCLUSIVE, which is what makes renaming the
    # right fix rather than an ordering tweak. The recall round is
    # `if onRecall` INSIDE the page; the flashcards overlay is grafted at the
    # design root, OUTSIDE both views. `goRecall` does not clear `cards`, so a
    # student who opens the cards and then the round has both on screen, and
    # whichever name won would be wrong for one of them.
    #
    # So the GRAFTED loop is renamed and the live one is left alone. It is a
    # binding NAME, not a drawing: nothing about what Design drew changes, and
    # the alternative is two surfaces silently sharing one variable.
    #
    # `{node index: (expected expression, new expression)}`. The expected value
    # is asserted, exactly as `BINDINGS_AT` asserts its literal: an index that
    # has drifted onto a different node would otherwise repoint some other loop
    # at a list that is not its own, and the page would still build.
    exprs = dict(student_rulings.SET_EXPR.get(page, {}))
    exprd = [0]

    def rename(node):
        if not isinstance(node, dict):
            return
        idx = node.get("i")
        if idx in exprs:
            want, new_e = exprs[idx]
            if node.get("e") != want:
                raise SystemExit(
                    "build_student_port.py: the expression ruling for %r "
                    "renames template node %s from %r, and that node reads "
                    "%r. The index has drifted, or Design has redrawn it. "
                    "Re-anchor it: a silently skipped rename leaves two "
                    "surfaces sharing one name, which is the defect it exists "
                    "to remove and which nothing errors on."
                    % (page, idx, want, node.get("e")))
            node["e"] = new_e
            exprs.pop(idx)
            exprd[0] += 1
        for kid in node.get("c") or []:
            rename(kid)

    for root in roots:
        rename(root)
    if exprs:
        raise SystemExit(
            "build_student_port.py: the expression ruling for %r renames "
            "template node(s) %s, and they are not in the template (or the "
            "graft that brings them in did not run). Re-anchor them."
            % (page, sorted(exprs)))

    # ── attributes Design never wrote ────────────────────────────────────
    #
    # ⊕ 22 Aug 2026. See `SET_ATTR` in student_rulings.py — the bench themes
    # need three surfaces to be nameable in CSS, and they carry no class.
    #
    # Refuses to overwrite an attribute Design already wrote, for the same
    # reason `SET_ON` refuses to overwrite a handler: the page would still look
    # and gate exactly right while one of Design's own values had been
    # silently replaced.
    attrs = dict(student_rulings.SET_ATTR.get(page, {}))
    attred = [0]

    def paint(node):
        if not isinstance(node, dict):
            return
        idx = node.get("i")
        if idx in attrs:
            bag = node.setdefault("a", {})
            for k, v in attrs[idx].items():
                if k in bag:
                    raise SystemExit(
                        "build_student_port.py: the theme ruling for %r sets "
                        "%s=%r on template node %s, and Design already gives "
                        "that node %s=%r. Re-anchor rather than overwriting "
                        "one of Design's own values."
                        % (page, k, v, idx, k, bag[k]))
                bag[k] = v
            attrs.pop(idx)
            attred[0] += 1
        for kid in node.get("c") or []:
            paint(kid)

    for root in roots:
        paint(root)
    if attrs:
        raise SystemExit(
            "build_student_port.py: the theme ruling for %r sets attributes "
            "on template node(s) %s, and they are not in the template. "
            "Re-anchor them." % (page, sorted(attrs)))

    # ── handlers Design never attached ───────────────────────────────────
    #
    # ⊕ RULED 22 Aug 2026 — P5. See `SET_ON` in student_rulings.py.
    #
    # Every node named must EXIST and must NOT already carry a handler. The
    # second check is the load-bearing one: silently replacing an `onClick`
    # Design drew would swap one working control's behaviour for another's,
    # and the page would still look and gate exactly right.
    want = dict(student_rulings.SET_ON.get(page, {}))
    wired = [0]

    def wire(node):
        if not isinstance(node, dict):
            return
        idx = node.get("i")
        if idx in want:
            if node.get("on"):
                raise SystemExit(
                    "build_student_port.py: the P5 ruling for %r attaches "
                    "%r to template node %s, but Design already gives that "
                    "node the handler %r. Design has redrawn it; re-anchor "
                    "the ruling rather than overwriting a live control."
                    % (page, want[idx], idx, node.get("on")))
            node["on"] = want.pop(idx)
            wired[0] += 1
        for kid in node.get("c") or []:
            wire(kid)

    for root in roots:
        wire(root)
    if want:
        raise SystemExit(
            "build_student_port.py: the P5 ruling for %r attaches a handler "
            "to template node(s) %s, and they are not in Design's template "
            "(or were pruned out from under it). The ruling stands; re-read "
            "the delivery and re-anchor it." % (page, sorted(want)))

    # ── a handler Design DID attach, pointed somewhere else ──────────────
    #
    # ⊕ RULED 23 Aug 2026 — THE EIGHTH MECHANISM. See `RETARGET_ON` in
    # student_rulings.py for the ruling and for the seven-caller count that
    # makes it necessary.
    #
    # It is `SET_ON`'s stated counterpart, and the two assertions are mirror
    # images of each other. `SET_ON` refuses a node that ALREADY carries a
    # handler; this one refuses a node that does not carry the EXPECTED one.
    # Neither can quietly repoint a control Design drew — the failure both are
    # written against is the one where the page still looks and gates perfectly
    # while a button does somebody else's job.
    #
    # ⚠️ AND THE DESTINATION IS ASSERTED TOO, WHICH `SET_ON` CANNOT DO. A
    # handler name resolves out of `renderVals`'s returned object at mount, so
    # a typo in `to` is not an error anywhere — it is `undefined`, the runtime
    # attaches nothing, and the brand becomes a mark that draws correctly and
    # does nothing when pressed. No gate in this build can see that: the
    # element is still there, its text is unchanged, and it is still in the
    # control list. So the name is required to APPEAR IN THE LOGIC. That is a
    # cheap check rather than a proof it is a live key, and it catches the
    # whole of the failure it is aimed at, which is a misspelling.
    moves = dict(student_rulings.RETARGET_ON.get(page, {}))
    moved = [0]

    for _idx, (_from, _to) in sorted(moves.items()):
        if _to not in logic:
            raise SystemExit(
                "build_student_port.py: the RETARGET_ON ruling for %r points "
                "template node %s at the handler %r, and that name appears "
                "nowhere in the logic this build is about to ship. It would "
                "resolve to `undefined` at mount and the control would draw "
                "perfectly and do nothing — which no gate here can see. Add "
                "it in LOGIC[%r] beside the handler it replaces."
                % (page, _idx, _to, page))

    def retarget(node):
        if not isinstance(node, dict):
            return
        idx = node.get("i")
        if idx in moves:
            want_from, want_to = moves[idx]
            got = node.get("on")
            if got != want_from:
                raise SystemExit(
                    "build_student_port.py: the RETARGET_ON ruling for %r "
                    "moves template node %s from %r to %r, and Design gives "
                    "that node %r. Design has redrawn it, or the index now "
                    "names a different control. The ruling is Mide's and "
                    "stands; re-anchor it rather than retargeting whatever is "
                    "sitting at that index — that is how the brand's ruling "
                    "would silently land on somebody's Back button."
                    % (page, idx, want_from, want_to,
                       got or "no handler at all"))
            node["on"] = want_to
            moves.pop(idx)
            moved[0] += 1
        for kid in node.get("c") or []:
            retarget(kid)

    for root in roots:
        retarget(root)
    if moves:
        raise SystemExit(
            "build_student_port.py: the RETARGET_ON ruling for %r moves "
            "template node(s) %s onto another handler, and they are not in "
            "the template (or were pruned out from under it). A silently "
            "skipped move leaves the control pointing where it always did "
            "and the build green. Re-anchor it." % (page, sorted(moves)))

    # ── a live node that has to STOP RENDERING in a state Design draws
    #    separately ─────────────────────────────────────────────────────
    #
    # ⊕ 23 Aug 2026 — PHASE 4. THE SEVENTH MECHANISM, and it exists because
    # none of the other six can make an EXISTING node conditional.
    #
    #   PRUNE        removes a subtree, in every state
    #   GRAFT        adds one, in every state
    #   SET_ON       attaches a handler to a node that has none
    #   RETARGET_ON  moves a node off the handler Design gave it, naming that
    #                handler so a redraw stops the build (⊕ 23 Aug 2026)
    #   SET_ATTR     names a node for CSS and for a gate
    #   SET_EXPR     renames a loop's list
    #   BINDINGS   replaces a text node's text (and `drop` can remove the
    #              element that CARRIES that text, when its value is empty —
    #              which is a rule about a VALUE, not about a state)
    #
    # Design's amended bench has TWO branches — `<if benchOpen>` at donor 59
    # and `<if benchDone>` at donor 100 — each with its own left column AND its
    # own docket. The live bench has ONE unconditional grid (node 57) holding
    # the live left column and the live docket, because when Design drew the
    # original there was only one bench state. Grafting the done bench beside
    # it without gating it leaves BOTH on screen: two headings, two dockets,
    # and `[data-bench-docket]` matching two elements, which is the exact
    # reading `student_themes.check_docket` refuses.
    #
    # ⚠️ AND `drop` COULD NOT DO IT, WHICH WAS CHECKED RATHER THAN ASSUMED.
    # `drop` removes the element carrying a bound text node when that value is
    # empty, and it splices from the tree by PATH — so two drops inside one
    # parent make the second path stale, and the removal that should collapse
    # a row either throws or removes the wrong sibling depending on the order
    # they were registered in. A state is not a value, and the mechanism for
    # one is not the mechanism for the other.
    #
    # `{node index: expression}`. The node is REPLACED IN ITS PARENT by an
    # `<if>` whose single child is the node itself, so the subtree, its
    # indices, its handlers and its bindings are all untouched — the only
    # change is that it now renders when the expression is truthy and not
    # otherwise.
    #
    # ⚠️ THE WRAPPER CARRIES NO `i`, AND THAT IS DELIBERATE. `student-runtime`
    # renders an `<if>` as a branch and never as an element (see `build`), so
    # it has nothing to hang a `data-dc-tpl` on; and `count_nodes` counts
    # nodes that HAVE an index, so a wrapper with one would report a node the
    # page does not contain. It is a branch, not a box.
    #
    # ⚠️ IT RUNS LAST, AFTER THE GRAFTS. Two of Phase 4's four entries name
    # GRAFTED nodes (the done docket's SCORE and RIGHT rows), which do not
    # exist until the graft has run; and the graft anchored on the live bench
    # section must not find an `<if>` where it expects the grid. Every index
    # is asserted present, so an entry that goes stale stops the build rather
    # than silently leaving a surface on screen in a state it contradicts.
    wraps = dict(student_rulings.WRAP.get(page, {}))
    wrapped = [0]

    def enclose(node):
        if not isinstance(node, dict) or not node.get("c"):
            return
        kids = node["c"]
        for pos, kid in enumerate(kids):
            if isinstance(kid, dict) and kid.get("i") in wraps:
                expr = wraps.pop(kid["i"])
                kids[pos] = {"t": "if", "e": expr, "c": [kid]}
                wrapped[0] += 1
            enclose(kid)

    for root in roots:
        if isinstance(root, dict) and root.get("i") in wraps:
            raise SystemExit(
                "build_student_port.py: the PHASE 4 ruling for %r wraps "
                "template node %s in `<if %s>`, and that node is a template "
                "ROOT with no parent to hold the wrapper. Wrap something "
                "further in." % (page, root.get("i"), wraps[root["i"]]))
        enclose(root)
    if wraps:
        raise SystemExit(
            "build_student_port.py: the PHASE 4 ruling for %r wraps template "
            "node(s) %s in a conditional, and they are not in the template "
            "(or the graft that brings them in did not run). Re-anchor them: "
            "a silently skipped wrap leaves the OPEN bench on screen "
            "underneath the DONE bench, with two dockets, and the build stays "
            "green." % (page, sorted(wraps)))

    return (logic, roots, len(reps), removed[0], wired[0],
            grafted[0], attred[0], exprd[0], wrapped[0], moved[0])


# ── lifting Design's data out of Design's logic ───────────────────────────
#
# The fields are welded into the class body as initialisers:
#
#     work = [ { id: 'a5', … }, … ];
#
# so the seam is a source transformation and not a hand edit. The literal is
# found by BALANCED SCAN rather than by regex, because every one of these
# contains the terminator: `questions` holds apostrophes, `figCaptions` holds
# semicolons inside strings, and `work` holds braces sixteen deep. A regex that
# stopped at the first `;` would truncate the class view's work list in the
# middle of a note and produce a syntax error four hundred lines later.
#
# ⚠️ A FIELD THAT CANNOT BE FOUND STOPS THE BUILD. The failure this refuses to
# have is the quiet one: a rename in Design's next delivery, a field silently
# left unseamed, and a production page that reads four lists from the database
# and the fifth from Design's imagination. There is no fallback path here on
# purpose — see `MRB_DATA` in the emitted page, which has none either.

def _skip_ws(src, i):
    """Advance past whitespace and both comment forms."""
    while i < len(src):
        ch = src[i]
        if ch in " \t\r\n":
            i += 1
        elif src.startswith("//", i):
            j = src.find("\n", i)
            i = len(src) if j < 0 else j + 1
        elif src.startswith("/*", i):
            j = src.find("*/", i)
            if j < 0:
                raise SystemExit("build_student_port.py: unterminated comment")
            i = j + 2
        else:
            return i
    return i


def balanced_literal(src, start):
    """From `start`, the literal that runs to its terminating top-level `;`.

    Returns (literal_text, index_of_the_semicolon). Strings, escapes and
    comments are all respected, so a `;` or a `}` inside `'…'` is just text.
    """
    depth, i, n = 0, start, len(src)
    while i < n:
        ch = src[i]
        if ch in "'\"`":
            quote, i = ch, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == quote:
                    i += 1
                    break
                i += 1
            continue
        if src.startswith("//", i) or src.startswith("/*", i):
            i = _skip_ws(src, i)
            continue
        if ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
            if depth < 0:
                raise SystemExit(
                    "build_student_port.py: unbalanced %r at offset %d" % (ch, i))
        elif ch == ";" and depth == 0:
            return src[start:i].rstrip(), i
        i += 1
    raise SystemExit(
        "build_student_port.py: no terminating `;` for the literal at offset "
        "%d — Design's logic class does not parse the way this build assumes."
        % start)


def find_field(logic, name):
    """(literal, start, end_of_statement) for `^  <name> = …;`."""
    import re as _re
    m = _re.search(r"(?m)^  %s\s*=\s*" % _re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_student_port.py: the field %r is NOT in Design's logic "
            "class. It is on this build's seam list, which means either "
            "Design has renamed it or it has gone. Seaming four of five data "
            "fields and leaving the fifth welded shut is the failure mode this "
            "refuses to have — reconcile the list against the delivery."
            % name)
    lit, semi = balanced_literal(logic, m.end())
    return lit, m.start(), semi + 1


def balanced_group(src, start, what):
    """The bracket group that OPENS at `start`, as source text.

    `balanced_literal` runs to a top-level `;`, which is right for a class
    field and wrong for a literal welded into a method body: that one has no
    `;` of its own — it is one value in an object literal, and the next `;`
    is four hundred lines down at the end of the return statement.

    Same scanner otherwise. Strings, escapes and comments are respected, so a
    `]` inside `'…'` is text. Returns (group_source, index_just_past_it).
    """
    opens, closes = "[{(", "]})"
    if start >= len(src) or src[start] not in opens:
        raise SystemExit(
            "build_student_port.py: the seam anchor for %r is not followed by "
            "a literal — Design's logic reads %r there. The anchor matched, so "
            "the line still exists; it has been rewritten around the value. "
            "Re-anchor it rather than dropping the seam: a dropped seam ships "
            "Design's example data on the production page."
            % (what, src[start:start + 40]))
    depth, i, n = 0, start, len(src)
    while i < n:
        ch = src[i]
        if ch in "'\"`":
            quote, i = ch, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == quote:
                    i += 1
                    break
                i += 1
            continue
        if src.startswith("//", i) or src.startswith("/*", i):
            i = _skip_ws(src, i)
            continue
        if ch in opens:
            depth += 1
        elif ch in closes:
            depth -= 1
            if depth == 0:
                return src[start:i + 1], i + 1
            if depth < 0:
                raise SystemExit(
                    "build_student_port.py: unbalanced %r at offset %d while "
                    "lifting %r" % (ch, i, what))
        i += 1
    raise SystemExit(
        "build_student_port.py: the literal for %r never closes — Design's "
        "logic class does not parse the way this build assumes." % what)


def lift_literals(page, logic, fixture):
    """Lift each welded literal out to `MRB_DATA(key)`. Returns (logic, n)."""
    lifts = LIFTS.get(page, ())
    for spec in lifts:
        anchor, key = spec["anchor"], spec["key"]
        n = logic.count(anchor)
        if n != 1:
            raise SystemExit(
                "build_student_port.py: %s — the seam anchor for %r occurs %d "
                "times in Design's logic, not once:\n    %s\n"
                "Design has redrawn that line. Re-anchor it in LIFTS; do NOT "
                "drop it, because dropping it puts Design's example data back "
                "into the production page."
                % (page, key, n, anchor.strip()))
        at = logic.index(anchor) + len(anchor)
        lit, end = balanced_group(logic, at, key)
        if key in fixture:
            raise SystemExit(
                "build_student_port.py: %s — %r is lifted twice, once as a "
                "field and once from a method body. One key is one value."
                % (page, key))
        fixture[key] = lit
        logic = logic[:at] + "MRB_DATA(%s)" % _q(key) + logic[end:]
    return logic, len(lifts)


def rewrite_seams(page, logic, fixture, bind_values):
    """Rebuild each spliced-in string from `MRB_DATA`. Returns (logic, n).

    The captured value goes to the fixture, so what the fixture supplies is
    BY CONSTRUCTION what Design wrote — the rendered string is unchanged, not
    approximately unchanged. A capture whose name is already a binding key is
    checked against it instead of written, because the markup and the logic
    naming the same thing differently is a bug that would otherwise render as
    two different term names on one page.
    """
    import re as _re
    seams = REWRITES.get(page, ())
    for spec in seams:
        hits = list(_re.finditer(spec["pat"], logic))
        if len(hits) != 1:
            raise SystemExit(
                "build_student_port.py: %s — the data seam %r matches Design's "
                "logic %d times, not once. Its pattern is:\n    %s\n"
                "Design has redrawn that span. Re-anchor it in REWRITES; do "
                "NOT drop it — the value it is closing is one real class's, "
                "and the page it ships on is the production page."
                % (page, spec["name"], len(hits), spec["pat"]))
        m = hits[0]
        for key, val in m.groupdict().items():
            kind = spec["keys"].get(key)
            if kind is None:
                # Not ours to carry — it must already be bound from the markup.
                # A label that upper-cases what it prints is compared through
                # the same transform, not against the raw binding.
                bound = bind_values.get(key)
                how = spec.get("check", {}).get(key)
                if how == "upper" and bound is not None:
                    bound = bound.upper()
                if bound != val:
                    raise SystemExit(
                        "build_student_port.py: %s — the seam %r reads %r as "
                        "%r, but the markup binds that key to %r. The template "
                        "and the logic disagree about the same datum; one key "
                        "is one value."
                        % (page, spec["name"], key, val, bound))
                continue
            js = _q(val) if kind == "str" else val
            if key in fixture and fixture[key] != js:
                raise SystemExit(
                    "build_student_port.py: %s — %r is captured as %s by the "
                    "seam %r and as %s elsewhere. Design's logic disagrees "
                    "with itself about the same datum; do not pick one."
                    % (page, key, js, spec["name"], fixture[key]))
            fixture[key] = js
        logic = logic[:m.start()] + spec["new"] + logic[m.end():]
    return logic, len(seams)


def seam_logic(spec, logic, page, bind_values):
    """Design's logic with every data literal replaced by a `MRB_DATA` read.

    Returns (seamed_logic, {key: js_literal_source}, n_method_body_seams).
    The literal is carried to
    the fixture as SOURCE, not re-serialised through JSON — Design wrote
    `\\u00B7` and `\\u2019` by hand in a hundred places and a round trip
    through json would rewrite every one of them into a raw character. Same
    bytes in, same bytes out.
    """
    fixture, edits = {}, []
    for name in spec["fields"]:
        lit, start, end = find_field(logic, name)
        fixture[name] = lit
        edits.append((start, end, "  %s = MRB_DATA(%s);" % (name, _q(name))))

    # ── `state` is not lifted; ONE PROPERTY INSIDE IT IS ──────────────────
    #
    # `streak` is a student's recall streak and belongs to the student;
    # everything else in that initialiser is view state — which tab is open,
    # how wide the window is — and belongs to the page. Lifting the whole
    # initialiser would have made the data source responsible for `w: 1200`,
    # which is not data, and would have put a render-time constant behind a
    # throw.
    if spec["state_fields"]:
        lit, start, end = find_field(logic, "state")
        new = lit
        import re as _re
        for name in spec["state_fields"]:
            m = _re.search(r"\b%s\s*:\s*([^,}\s]+)" % _re.escape(name), new)
            if not m:
                raise SystemExit(
                    "build_student_port.py: `%s` is not a property of the "
                    "`state` initialiser in Design's logic. It is on the seam "
                    "list; reconcile it against the delivery." % name)
            fixture[name] = m.group(1)
            new = new[:m.start(1)] + "MRB_DATA(%s)" % _q(name) + new[m.end(1):]
        edits.append((start, end, "  state = %s;" % new))

    for start, end, text in sorted(edits, reverse=True):
        logic = logic[:start] + text + logic[end:]

    # ── and then the half a field-scan cannot reach ───────────────────────
    #
    # These run AFTER the field edits, on the result, because both anchor on
    # text inside `renderVals()` and the field edits change offsets above it.
    logic, n_lift = lift_literals(page, logic, fixture)
    logic, n_rew = rewrite_seams(page, logic, fixture, bind_values)
    return logic, fixture, n_lift + n_rew


def _q(s):
    return json.dumps(s)


# ── binding a literal text node without becoming an interpolation ─────────

def text_paths(roots, literal):
    """Every path to a text node whose value is EXACTLY `literal`.

    A path is [root index, child index, child index, …] into `c`.
    """
    hits = []

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if node.get("t") == "#" and node.get("v") == literal:
            hits.append(path)
        for i, kid in enumerate(node.get("c") or []):
            walk(kid, path + [i])

    for i, root in enumerate(roots):
        walk(root, [i])
    return hits


def bindings_for(page, tpl):
    """The binding table, and the values Design typed, for one page."""
    table, values = [], {}
    for entry in BINDINGS.get(page, ()):
        literal, key = entry[0], entry[1]
        drop = len(entry) > 2 and entry[2] == "drop"
        paths = text_paths(tpl["roots"], literal)
        if not paths:
            raise SystemExit(
                "build_student_port.py: %s — the literal %r is not a text node "
                "in Design's template. It is on the binding list, so either "
                "Design has redrawn that line or the whitespace has moved. "
                "Nothing is guessed here: an approximate match would bind the "
                "wrong node and the page would say the right thing in the "
                "wrong place." % (page, literal))
        if key in values and values[key] != literal:
            raise SystemExit(
                "build_student_port.py: %s — the key %r is claimed by two "
                "different literals, %r and %r. One key is one value; give "
                "them separate keys." % (page, key, values[key], literal))
        values[key] = literal
        for path in paths:
            row = {"p": path, "k": key}
            if drop:
                # ⊕ RULED 22 Aug 2026 — P6. This literal CARRIES ITS OWN
                # ELEMENT: when its value is empty the element goes with it,
                # rather than leaving a bordered box with nothing in it. See
                # `applyBindings` in student-runtime.js.
                # THREE, not two: dropping the element means removing it
                # from ITS OWN parent, so the path must reach a grandparent.
                # At depth 2 the element carrying the text IS a root, and a
                # root has no parent to be removed from — the runtime would
                # silently do nothing and the badge would ship.
                if len(path) < 3:
                    raise SystemExit(
                        "build_student_port.py: %s — %r is marked `drop`, but "
                        "its path is only %d deep, so the element carrying it "
                        "is a template root and has no parent to be removed "
                        "from. Drop something further in, or prune the root."
                        % (page, literal, len(path)))
                row["d"] = 1
            table.append(row)

    # ── the node-indexed overrides ────────────────────────────────────────
    #
    # ⊕ 23 Aug 2026. See `BINDINGS_AT` above for why one node needs addressing
    # by index instead of by literal. Applied AFTER the literal table, and it
    # REPLACES whatever row landed on the same path rather than adding a second
    # — two rows on one path would both fire, in list order, and the page would
    # show whichever happened to be last.
    for idx, (literal, key) in sorted(
            (BINDINGS_AT.get(page) or {}).items()):
        # ⊕ 23 Aug 2026 — THIS NODE'S OWN LITERAL SUPPLIES THE FIXTURE'S VALUE
        # WHEN NOTHING ELSE DOES.
        #
        # ⛔ This used to be fatal:
        #
        #     "BINDINGS_AT repoints template node %s at the key %r, and no
        #      literal in BINDINGS claims that key. The fixture would then have
        #      no value for it and the page would throw at mount."
        #
        # The DIAGNOSIS was right and the REMEDY was too narrow. What must
        # never happen is a key with no fixture value; requiring a second node
        # elsewhere in the template to carry the same literal is one way of
        # guaranteeing that and not the only one. This table already states the
        # literal it expects AND asserts it against the node, three lines
        # below — so the value is in hand, checked, and Design's own.
        #
        # It became load-bearing with the 23 Aug header ruling. `studentFirstName`
        # was claimed by the literal `Ayo` at exactly one node — the name beside
        # the header avatar — and that node is pruned (the header drew the name
        # three times over; see `PRUNE` 23 in student_rulings.py). The account
        # sheet's name line, node 10254, is now the key's only reader, and the
        # rule as written said a key may not be read by the only node that has
        # it.
        #
        # ⚠️ THE FIXTURE'S NAME LINE THEREFORE READS `AY` RATHER THAN `Ayo`,
        # which is Design's amended sample's own value and closer to the
        # delivery than what it replaces. The registration that matches it —
        # `AMENDED_ADDITIONS`' `" ?ACCOUNT AY \\S+ 8r/Sc1 · SCIENCE "` — already
        # matches the name as `\\S+`, deliberately and with a note saying why,
        # so it covers both. The LIVE page is unmoved either way: it binds
        # `studentFirstName` to the real student's real first name.
        if key not in values:
            values[key] = literal
        path = _path_to_text(tpl["roots"], idx)
        if path is None:
            raise SystemExit(
                "build_student_port.py: %s — BINDINGS_AT names template node "
                "%s, and there is no such node carrying a single text child. "
                "It has been pruned, or Design has redrawn it, or the graft "
                "that brings it in is not applied. Re-anchor it; a silently "
                "skipped override binds the wrong value to the wrong place."
                % (page, idx))
        node = tpl["roots"][path[0]]
        for i in path[1:]:
            node = node["c"][i]
        if node.get("v") != literal:
            raise SystemExit(
                "build_student_port.py: %s — BINDINGS_AT expects template node "
                "%s to read %r and it reads %r. The index has drifted onto a "
                "different node. Nothing is guessed here: binding on a drifted "
                "index puts the right value in the wrong place, which is the "
                "one failure that still looks like a working page."
                % (page, idx, literal, node.get("v")))
        table = [r for r in table if r["p"] != path]
        table.append({"p": path, "k": key})
    return table, values


def _path_to_text(roots, index):
    """The path to the single text child of template node `index`, or None."""
    found = []

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if node.get("i") == index:
            kids = [(i, k) for i, k in enumerate(node.get("c") or [])
                    if isinstance(k, dict)]
            texts = [(i, k) for i, k in kids if k.get("t") == "#"]
            if len(kids) == 1 and len(texts) == 1:
                found.append(path + [texts[0][0]])
            return
        for i, kid in enumerate(node.get("c") or []):
            walk(kid, path + [i])

    for i, root in enumerate(roots):
        walk(root, [i])
    return found[0] if len(found) == 1 else None


def count_nodes(roots):
    """Nodes in the compiled template — reported after the ruling, not before.

    `student_templates.json` records Design's count; the class view's ruling
    prunes seven subtrees out of it, so quoting the stored number would report
    404 for a page that ships 384.
    """
    n = [0]

    def walk(node):
        if not isinstance(node, dict):
            return
        # Element nodes only — the same thing `student_templates.json` counts,
        # so the two numbers are comparable. Text nodes carry no `i`.
        if "i" in node:
            n[0] += 1
        for kid in node.get("c") or []:
            walk(kid)

    for root in roots:
        walk(root)
    return n[0]


def scrub_roots(roots, bind_table):
    """Design's template with every bound literal emptied.

    ⚑ THIS IS THE HALF THAT IS EASY TO MISS, and missing it makes the whole
    seam cosmetic. Binding at mount time replaces the text node's value in
    memory — it does NOT remove the value from the compiled template that
    SHIPS. Without this, `class-ported.html` reads its work list from the
    database and still has the string `Ayo` sitting in it, four hundred
    kilobytes down, waiting for the day somebody renders the template without
    the bindings.

    So the shipped template carries an EMPTY string at each bound path and the
    value arrives with the data. Empty rather than a placeholder because a
    placeholder is a thing that can be shipped by accident; empty is not
    mistakable for a real name. The node itself stays — a text node with no
    text is still a text node, and the parity gate counts nodes.
    """
    out = json.loads(json.dumps(roots))
    for b in bind_table:
        node = out[b["p"][0]]
        for i in b["p"][1:]:
            node = node["c"][i]
        if node.get("t") != "#":
            raise SystemExit(
                "build_student_port.py: the binding path for %r does not land "
                "on a text node." % b["k"])
        node["v"] = ""
    return out


# Keys whose value appearing anywhere in the shipped production page is a
# BUILD FAILURE rather than a note. These are the ones that name a person or a
# class: if `Ayo` survives the seam, the seam did not happen.
_MUST_NOT_LEAK = {"className", "classNamePadded", "studentFirstName",
                  "welcomeLine", "studentInitials", "teacherName",
                  "teacherInitials", "classSize", "backToClass"}


def fixture_js(spec, page, data_literals, bind_values):
    """`window.__MRB_DATA__ = {…}` — Design's own values, once, for the gates."""
    rows = []
    named = list(spec["fields"]) + list(spec["state_fields"])
    # The fields, in Design's order, then whatever the method-body seams
    # lifted — sorted, so the file is stable across runs.
    for name in named + sorted(k for k in data_literals if k not in named):
        rows.append("  %s: %s" % (_q(name), data_literals[name]))
    for key in sorted(spec.get("constants") or {}):
        rows.append("  %s: %s" % (_q(key), spec["constants"][key]))
    for key in sorted(bind_values):
        rows.append("  %s: %s" % (_q(key), _q(bind_values[key])))
    return (
        "/* ══════════════════════════════════════════════════════════════\n"
        "   GENERATED — do not edit. `python3 build_student_port.py`\n"
        "   ══════════════════════════════════════════════════════════════\n"
        "\n"
        "   Claude Design's own example data for the %s, lifted out of\n"
        "   Design's logic class and out of Design's template by source\n"
        "   transformation — not retyped, and not re-serialised. Every value\n"
        "   below is the same bytes Design wrote.\n"
        "\n"
        "   ⛔ FOR THE GATES ONLY. This is one real class's homework with one\n"
        "   real child's name on it, frozen. It is loaded by %s and by nothing\n"
        "   that a student can reach: the production page loads %s instead,\n"
        "   and `MRB_DATA` throws rather than falling back to this.\n"
        "   ══════════════════════════════════════════════════════════════ */\n"
        "window.__MRB_DATA__ = {\n%s\n};\n"
        % (page, spec["fixture_out"], LIVE_JS_NAME, ",\n".join(rows)))


# ── the KS3 lesson index: a slug, and where that lesson actually lives ────
#
# ⊕ RULED 22 Aug 2026 — P3. "Open the lesson" has to know where the lesson is,
# and NOTHING THE CLIENT CAN READ KNOWS THAT.
#
# The chain a student can follow is `assignment_questions.source_ref` →
# `ks3_assignment_bank` / `ks3_ladder_questions` → `(unit_code, lesson_slug)`.
# All three are readable under RLS (`aq_student_read`, and both question tables
# are `SELECT true` to any authenticated user), so a student can learn that a
# piece of work draws on `the-gas-exchange-system` in unit `B4`.
#
# What they CANNOT learn is that B4's pages are served from
# `/ks3/biology/breathing-and-gas-exchange/`. The unit's discipline and
# directory slug exist only in `ks3_data`, which is Python and build-time. So
# the map is emitted here, once, as a file the page loads.
#
# ⚠️ IT IS BUILT FROM `ks3_data`, NOT FROM THE `ks3/` TREE, AND THEN CHECKED
# AGAINST THE TREE. Reading the directory listing would produce a map that is
# self-consistent and wrong the moment a lesson is renamed — it would simply
# describe whatever files happened to be there, including stale ones. Reading
# the data and then asserting the file exists catches the rename in the
# direction that matters: the build stops rather than shipping a link to a
# lesson that has moved.
#
# ⚑ WHY IT IS EMITTED HERE AND NOT BY `build_ks3.py`, WHICH OWNS THIS DATA.
# Two reasons, and the first is the honest one: a parallel content session owns
# `build_ks3.py` tonight and this run is not allowed to touch it. The second is
# that it would still belong here afterwards — `build_ks3.py` is not run by a
# KS4-only build, the student pages are, and a page that depends on a file its
# own build does not publish is the hidden prerequisite that cost a red gate
# over `student-runtime.js`. Same lesson, applied before it bites.

def lesson_index():
    """`{lesson_slug: "discipline/unit-slug"}` for every KS3 lesson.

    Returns (js_source, n_lessons). Stops the build on a duplicate slug or on
    a lesson whose page is not on disk.
    """
    import ks3_data

    index, owners = {}, {}
    for unit in ks3_data.KS3_UNITS:
        for lesson in unit["lessons"]:
            slug = lesson["slug"]
            where = unit["discipline"] + "/" + unit["slug"]
            if slug in index and index[slug] != where:
                raise SystemExit(
                    "build_student_port.py: the KS3 lesson slug %r is used by "
                    "BOTH %s and %s. The index is keyed on the slug alone, "
                    "which was safe while all 183 were distinct and is not "
                    "any more. Key it on (unit_code, slug) and carry the unit "
                    "code through from `assignment_questions`."
                    % (slug, owners[slug], unit["code"]))
            index[slug] = where
            owners[slug] = unit["code"]

    missing = [s for s, w in sorted(index.items())
               if not os.path.exists(os.path.join("ks3", w, s + ".html"))]
    if missing:
        raise SystemExit(
            "build_student_port.py: %d KS3 lesson page(s) named in ks3_data "
            "are not built on disk, and the student pages are about to link "
            "to them: %s%s\nRun `python3 build_ks3.py` (or build_all.py) "
            "first — a link to a lesson that is not there is a 404 with a "
            "student's name on it."
            % (len(missing), ", ".join(missing[:5]),
               " …" if len(missing) > 5 else ""))

    rows = ",\n".join('  %s: %s' % (_q(s), _q(index[s]))
                       for s in sorted(index))
    return ("/* ══════════════════════════════════════════════════════════\n"
            "   GENERATED — do not edit. `python3 build_student_port.py`\n"
            "   ══════════════════════════════════════════════════════════\n"
            "\n"
            "   Where each KS3 lesson lives, as `slug: \"discipline/unit\"`,\n"
            "   so a page can turn a lesson slug from the database into the\n"
            "   URL of the lesson itself:\n"
            "\n"
            "       /ks3/ + MRB_KS3_LESSONS[slug] + / + slug + .html\n"
            "\n"
            "   Built from ks3_data and checked against the built tree: every\n"
            "   one of these %d pages existed on disk when this was written.\n"
            "   ══════════════════════════════════════════════════════════ */\n"
            "window.MRB_KS3_LESSONS = {\n%s\n};\n" % (len(index), rows)), len(index)


# ── the token bridge: Design's theme tokens → the live page's ────────────
#
# ⊕ 22 Aug 2026 — PHASE 2a. Design's six themes move `--b-*`; the live bench,
# the leaderboard card and the leader's avatar are painted in `--st-*`. This is
# the join between them, and it is SCOPED to the surfaces `SET_ATTR` names
# rather than declared at the root — see student_rulings.py for why a root-level
# remap of `--st-cream` breaks on Chalk.
#
# ⚠️ THESE TEN ARE A LIST, NOT A FAMILY SWEEP, AND THE DISTINCTION IS THE
# WHOLE POINT OF THE RULE. Measured out of the compiled tree rather than read
# off the markup: inside node 55, excluding the docket subtree at node 91, the
# `--st-*` tokens in use are these ten colours PLUS `--st-ui`, `--st-display`,
# `--st-mono`, `--st-r-btn`, `--st-r-frame`, `--st-r-chip`, `--st-shadow-frame`,
# `--st-accent` and `--st-hatch-b`. The first seven of those are FONTS, RADII
# AND A SHADOW. A rule that swept "the dark `--st-*` family" would have
# re-pointed the bench's typeface and its corner radii at a colour, and half of
# what it caught would not have been a colour at all.
#
# ⊕ 23 Aug 2026 — IT WAS EIGHT, AND EIGHT WAS WRONG. THE NINTH AND TENTH ARE
# `--st-room-text` AND `--st-room-faint`, and the paragraph above used to claim
# the list was complete. It was not, and the way it was incomplete is worth
# recording, because the measurement that produced it was run against the
# MARKUP and these two do not appear there.
#
# The bench checklist — "Open it" / "Answer the eight questions" / "Hand it in"
# — takes its colour from a COMPUTED STRING in Design's logic, not from a style
# attribute the compiler can see:
#
#     color: done ? 'var(--st-room-faint)' : 'var(--st-room-text)',
#
# so a sweep of node 55's compiled attributes finds nothing, and the two tokens
# stayed at their `shared/student-ds.css` defaults on every theme. Those
# defaults are `#B7AA98` and `#7E7263`, declared "readable text on dark" — FIXED
# LIGHT VALUES FOR A DARK BENCH. On the five dark themes that is fine and
# measures 5.55:1 on harbour. On CHALK, the one light theme, the bench ground is
# `#EFE2CB` and the same fixed light ink lands on it at **1.78:1** — three
# labels telling a student what to do, in a colour they cannot read. It shipped
# green because the gate at the time asserted the `--b-*` tokens' own contrast
# and never asked what the bench's rendered text actually did; `student_themes.py`
# now walks every text-bearing leaf inside the bench, which is what closes it.
#
# ⚠️ `--st-room-text` → `--b-ink` IS NOT A JUDGEMENT CALL. Design's amended
# delivery redraws this exact checklist, and draws it
# `color:var(--b-ink)` — `class-view-amendments/source/KS3 Class View.dc.html`,
# lines 138-140, the three `<li>`s. The bridge is adopting Design's own value
# for Design's own element, not inferring one.
#
# `--st-room-faint` → `--b-muted` IS a judgement call, and a small one. It is
# the TICKED state — a task the student has finished and no longer needs to
# read — and Design's amended bench draws no ticked label to copy. `--b-muted`
# is the theme's only de-emphasis tone, it is where the bridge already sends
# `--st-room-muted`, and it is asserted at or above AA on all six themes
# (5.05:1 on chalk, its worst). The alternative — leaving it fixed — reproduces
# the defect above in the one state a student reaches by making progress.
#
# ⚠️ AND THIS IS WHY IT IS A BRIDGE RULE AND NOT A `LOGIC` RULING. The obvious
# fix is to rewrite that computed string in `student_rulings.py`. It is the
# wrong one twice over. First, the inline style declares the PROPERTY but its
# VALUE is a `var()`, so the token resolves from the cascade at the element and
# a scoped redeclaration reaches it with no `!important` and no rewrite — the
# opposite of node 266's avatar, where the inline declared a literal and the
# keyword was load-bearing. Second, `--st-room-text` appears TWICE in that
# logic, and the second is the recall round's option colour
# (`ok || chosen ? 'var(--st-cream)' : 'var(--st-room-text)'`), which must NOT
# move: Design replaces that card wholesale with flashcards in a later unit.
# The bridge cannot touch it even by accident — MEASURED, not assumed: driving
# the fixture into the recall round leaves ZERO `[data-bench-surface]` elements
# on the page, because the round replaces the class view rather than nesting
# inside it. A `LOGIC` ruling would have had to anchor around that collision by
# hand; the scope does it for free.
#
# ⚠️ AND A SWEEP WOULD HAVE TAKEN THE DOCKET WITH IT. `--st-paper` IS in the
# list — it is the CTA ink on nodes 74 and 88 — and it is ALSO the background
# of node 91, the one paper card sitting inside the dark bench. Custom
# properties inherit, so the bridge reaches it whether or not it was aimed
# there. Hence the restore two rules down. Mide's brief for this unit said the
# docket uses none of the eight and that no reset rule was needed; measured, it
# uses exactly one, and without the restore the docket's ground moves from
# #FFFDF8 to #FFF7EC on five themes and to #FBF3E6 on Chalk. Small, real, and
# contrary to the ruling that the docket stays paper and ink on all six.
#
# The restore is written as a CAPTURE, not as a value: `--st-docket-paper` is
# taken from `--st-paper` at the root, OUTSIDE the bench, so the docket follows
# `shared/student-ds.css` if that file ever changes. Retyping #FFFDF8 here is
# exactly the kind of restated constant that rots, which is what the brief was
# guarding against; capturing it is not.
#
# ⚠️ `[data-bench-avatar]` IS NOT AN EXEMPTION — IT IS AN INVERSION. Node 266
# is the leader's avatar disc: `background:var(--st-cream)` carrying `--st-ink`
# initials, and the only place in the class view where `--st-cream` is a
# background rather than text. Bridging `--st-cream → var(--b-ink)` is REQUIRED,
# because on Chalk the card ground goes light #EFE2CB and cream text on it is
# unreadable — but the same bridge would turn the disc near-black under
# near-black initials. Inverting gives a cream disc with dark initials on the
# five dark themes and a dark disc with light initials on Chalk. Legible on all
# six, and it is the relationship Design draws rather than a special case bolted
# on beside it.
#
# ⚠️ AND IT NEEDS `!important`, WHICH IS NOT DECORATION. Node 266 carries its
# colours in an INLINE style — `background:var(--st-cream)` and
# `color:var(--st-ink)` — and an inline declaration outranks any selector.
# Written without the keyword, both declarations parse, match, and lose, and the
# page looks exactly as if the rule were there: measured on Chalk before the
# keyword was added, the disc came out rgb(34,30,27) with rgb(34,30,27)
# initials — the disc and the letters the same colour, which is the precise
# defect this rule exists to prevent, shipped under a rule that claims to
# prevent it. The two declarations are Mide's, verbatim; the keyword is what
# makes them true.
#
# ⚠️ THERE IS DELIBERATELY NO `[data-bench-docket]` RULE BEYOND THE ONE TOKEN IT
# ACTUALLY USES. `SET_ATTR` names node 91 so a gate has a handle to assert "the
# docket stays paper and ink on all six themes" against; that gate is a separate
# unit. Restating the docket's other colours here would pin values it does not
# reference and would rot the moment Design moved one.
#
# CLASS VIEW ONLY. The assignment page has no bench, and emitting these rules
# into it would move that page's bytes to define selectors it can never match.
_THEME_BRIDGE = (
    ":root{--st-docket-paper:var(--st-paper)}"
    "[data-bench-surface]{"
    "--st-room-panel:var(--b-ground);"
    "--st-room-body:var(--b-ink);"
    # ⊕ 23 Aug 2026 — the ninth and tenth. The bench checklist; see above.
    "--st-room-text:var(--b-ink);"
    "--st-room-faint:var(--b-muted);"
    "--st-room-muted:var(--b-muted);"
    # ⊕ 23 Aug 2026 — THE ELEVENTH, and the one that hurt the DEFAULT theme.
    #
    # `--st-room-line-strong` (#4A4036) draws the unticked checkbox outlines
    # beside those three labels, the leader card's streak chip and the recall
    # bar. Measured against the theme grounds it is 1.25:1 on HARBOUR — the new
    # default — 1.79 on graphite and 7.90 on chalk. A checkbox a student cannot
    # see, on the theme every student now gets.
    #
    # ⚠️ IT WAS NEARLY LEFT OUT ON A "PRE-EXISTING" ARGUMENT, and that argument
    # is wrong HERE even though it is right about the docket header. It measured
    # 1.73:1 on the old graphite bench, so the themes did not break it — but
    # Design's amended bench REDRAWS this element, as
    # `border:2px solid var(--b-muted)`, which measures 5.05–6.97 across the
    # six. "Design has not changed it" is what makes a shortfall somebody
    # else's; Design changing it is what makes it ours. Adopting Design's own
    # value is not inventing one.
    #
    # Found twice, independently, by two agents looking at the same page from
    # different ends — one measuring tokens, one looking at a screenshot and
    # asking why the checkboxes were faint.
    "--st-room-line-strong:var(--b-muted);"
    "--st-room-line:var(--b-rule);"
    "--st-room-border:var(--b-edge);"
    "--st-cream:var(--b-ink);"
    "--st-ember:var(--b-ember);"
    "--st-paper:var(--b-cta-ink)}"
    "[data-bench-docket]{--st-paper:var(--st-docket-paper)}"
    "[data-bench-avatar]{background:var(--b-ink)!important;"
    "color:var(--b-ground)!important}"
)


# ── page chrome: espresso, and FIXED on every theme ──────────────────────
#
# ⊕ 23 Aug 2026 — PHASE 1a. Design's amended README, change 1, first sentence:
#
#     "The near-black ground is gone as a default, and no page chrome is
#      near-black any more. Page-chrome dark is now espresso #4A3728
#      (10.4:1 on cream) — top rule, work-row and legend DONE dots."
#
# `--pg-strong: #4A3728` is Design's own NEW page token. It is declared exactly
# once on the built page, in the `:root` block grafted from Design's node 7, so
# this rule is a reference to Design's value and not a second copy of it — if
# Design moves espresso, this follows.
#
# ⚠️ THIS IS A PAGE RULE, NOT A THEME RULE, AND THAT IS THE POINT. The two
# dots it paints sit on the CREAM PAGE GROUND, outside `[data-bench-surface]`,
# which is why they are unreachable from the theme bridge and why they must NOT
# be reachable from it. `--pg-strong` is a fixed hex on `:root` and no
# `[data-bench-theme]` rule touches it, so these read #4A3728 on all six themes
# and on the attribute's absence — asserted, in `student_themes.py`.
#
# That fixedness is the safety margin the term spine's `numColor` note already
# records: page chrome routed through a THEME token would put `--b-ground` on
# the cream page at about 1.1:1 on Chalk. Espresso on cream is 10.20:1
# measured, everywhere, unconditionally.
#
# ⚠️ AND IT NEEDS `!important`, FOR THE REASON NODE 266 DOCUMENTS. Both dots
# carry `background:var(--st-ink)` in an INLINE style attribute of Design's
# own, and an inline declaration outranks any selector. Without the keyword
# this rule parses, matches and loses, and the page looks exactly as if it were
# not here. `background-color` rather than the `background` shorthand, so the
# important-flag covers the one component that is actually being replaced and
# nothing else.
#
# The value the rule REPLACES is `--st-ink`, which the page frame re-points at
# `--ks3-ink` #221E1B — 15.0:1 on cream. Espresso is 10.20:1. Both clear AA by
# a wide margin for a graphic mark; this is a tone change, not a legibility fix,
# and it is Design's tone.
#
# ⚑ WHAT IS DELIBERATELY NOT IN HERE. Three other near-black paints survive
# outside the themed surfaces, and none of them is this unit's:
#
#   · the sidebar RECALL card (#15110C) — Design's C2 REPLACES that card
#     wholesale with the themed flashcards card. It stops existing; it does not
#     turn espresso.
#   · the leaderboard's selected week chip (#221E1B) — Design's change 1 says
#     the week chips take the BENCH THEME, not espresso. That is unfinished
#     theme work, not page chrome.
#   · every near-black `color:` on the page — that is `--pg-ink` #221E1B, which
#     Design's token table lists UNCHANGED at 15.0:1. Body ink is not chrome.
#
# CLASS VIEW ONLY, like the bridge above it: the assignment page has no term
# spine and no work list, so neither selector could ever match there.
_PAGE_STRONG = (
    "[data-page-strong]{background-color:var(--pg-strong)!important}"
)


# ── the pip row, and what happens to it past twenty-four cards ───────────
#
# ⊕ 23 Aug 2026 — PHASE 2. Design's flashcard overlay draws a row of position
# pips, one per card, `display:flex;gap:6px` across a 390px panel with 18px of
# padding either side. Each pip is `flex:1 1 auto` against a FIXED 3px height,
# so N pips are (354 - 6(N-1)) / N pixels wide: 9px at 24 cards, under 3:1 at
# 25, and 3px — a square — by 40. Past two dozen the row has stopped being a
# position and become texture.
#
# `cardVals` in student_rulings.py therefore hands the `<for>` an EMPTY list
# past `PIP_MAX`, and the runtime renders nothing for an empty loop. That is
# not enough on its own: the row's CONTAINER survives, and an empty flex child
# still costs its parent's 16px gap — a band of dead space where a graphic used
# to be, which reads as something that failed to load rather than as something
# deliberately not drawn.
#
# ⚠️ AN ATTRIBUTE AND A SCOPED RULE, FOR THE REASON `data-page-strong` ALREADY
# DOCUMENTS. The row's `display:flex` is a LITERAL inside Design's inline
# `style`, so there is no computed string in Design's logic for a `LOGIC`
# ruling to anchor on, and `SET_ATTR` refuses to overwrite an attribute Design
# already wrote. `:empty` is what makes the rule need no state of its own: it
# is true exactly when the loop drew nothing, so the two can never disagree.
#
# ⚠️ AND IT NEEDS `!important`, FOR THE THIRD TIME IN THIS FILE. Design's row
# carries `display:flex;gap:6px` in an INLINE style attribute, and an inline
# declaration outranks any selector however specific — `:empty` adds a compound
# and changes nothing about that. Without the keyword this rule parses,
# matches, loses, and the page looks exactly as if it were absent: an empty
# 3px-tall flex row still costing its parent's 16px gap. Same failure mode as
# `[data-bench-avatar]`, which shipped broken once for precisely this reason.
#
# CLASS VIEW ONLY, like the two rules above it: the assignment page has no
# flashcards and the selector could never match there.
_PIP_ROW = (
    "[data-pip-row]:empty{display:none!important}"
)


# ── the flip stage, and the two buttons it pushed off a phone ────────────
#
# ⊕ RULED 23 Aug 2026 — PHASE 5. See `data-card-fit` in student_rulings.py for
# the measurement; this is the rule it names, and it is the fourth in this file
# to fight an inline declaration.
#
# Design's overlay card is `height:min(100%,760px)` inside a fixed full-screen
# scrim and is `overflow:hidden`, so under 760px of viewport height the card is
# the viewport and its column has to fit inside it. The column's fixed chrome —
# header, body padding, two gaps, the pip row and the 52px button row — is
# 200px, and the flip stage below it is floored at `min-height:300px`. Under
# roughly 500px of viewport height the sum no longer fits, and what goes over
# the clipped edge is the LAST flex child: Reveal and Next. On a phone held
# sideways (844 × 390) both buttons are entirely off screen, with no scroll to
# reach them — the deck is open and cannot be turned.
#
# `min(300px, calc(100vh - 240px))` yields ONLY when it has to. At 500px of
# viewport height and above it evaluates to Design's own 300px and this rule
# changes nothing whatever; below it the stage gives back exactly the room the
# buttons need. 240px is the 200px of chrome plus 40px of slack, because the
# header's height is content-derived and a narrow viewport can wrap it.
#
# ⚠️ `100vh` IS THE RIGHT UNIT HERE and not a guess at one. The card's `100%`
# resolves against the scrim, and the scrim is `position:fixed;inset:0` — so
# the card's height IS the viewport height wherever the 760px cap is not
# binding, which is precisely the range in which this rule is not the identity.
#
# ⚠️ AND IT NEEDS `!important`, for the reason `_PAGE_STRONG` and `_PIP_ROW`
# both record. `min-height:300px` is a LITERAL inside Design's inline `style`
# attribute, and an inline declaration outranks any selector however specific.
# Written without the keyword this rule parses, matches, loses, and the page
# looks exactly as if it were absent — the failure mode `[data-bench-avatar]`
# shipped once already.
#
# CLASS VIEW ONLY, like the three rules above it: the flashcards overlay is
# grafted onto the class view and the assignment page has no such surface.
_CARD_FIT = (
    ".rd[data-mode=\"ks3\"] [data-card-fit]"
    "{min-height:min(300px,calc(100vh - 240px))!important}"
)


# ── the question counter, which is now the only thing above the question ──
#
# ⊕ RULED 23 Aug 2026 — ASSIGNMENT ONLY, and it is the first emitted rule this
# page has ever needed.
#
# The question screen used to open with three stacked meta lines: the topic and
# the deadline (`dueLead`), a late chip beside them, and then
# `Question 01 of 04 · ANIMAL AND PLANT CELLS`. The first two are pruned
# (`PRUNE` 107 in student_rulings.py) and the third has lost its topic suffix,
# because the topic was already in the crumb bar and in the marker sheet's own
# lead and this was the third telling, in the smallest type on the screen.
#
# What is left is the one thing a student needs at the top of a question — WHICH
# QUESTION THEY ARE ON — still drawn at `.eyebrow`'s 10.5px, a size it was given
# when it was the last of three.
#
# ⚠️ `.eyebrow` ITSELF IS NOT TOUCHED, AND THAT IS THE WHOLE REASON THIS RULE
# EXISTS RATHER THAN A ONE-LINE EDIT TO `shared/student-ds.css`. The class is
# used six more times on this page alone — the marker sheet's lead, the rail's
# heading, the review screen's labels — and every one of them is a caption doing
# the job the class was sized for. Raising the class would raise all seven, and
# that is a redesign of the page rather than a fix to one line of it.
#
# ⚠️ AND `shared/student-ds.css` IS GENERATED, WHICH THE FIRST DRAFT LEARNED THE
# EXPENSIVE WAY. It is Design's six sheets concatenated by this very file, so a
# rule appended to it survives exactly until the next build — the same mistake,
# in a new file, that `student_rulings.py`'s banner exists to recover from. An
# emitted rule beside `_PAGE_STRONG` and `_PIP_ROW` is where a port's own CSS
# goes.
#
# ⚠️ NO `!important` HERE, and that is not an oversight — it is the difference
# between this rule and the three above it. Those fight an INLINE declaration
# (`background`, `display`) and an inline declaration outranks any selector.
# `font-size`, `letter-spacing` and `color` for this span come from the
# `.eyebrow` CLASS; the span's own inline style sets only `display` and
# `margin-top`. A `[data-*]` attribute selector under `.rd[data-mode="ks3"]`
# outranks a bare class, so it wins on specificity, as CSS is supposed to.
#
# The values: 10.5px → 13px is `.eyebrow` at the next step of the ramp, with
# tracking eased from 0.18em to 0.14em because letter-spacing that reads at
# 10.5px is loose at 13px, and colour up one tier of ink from `--st-caption` to
# `--st-body`. Legible from a desk without becoming a heading in its own right:
# the question below it is still twice the size at every viewport.
_Q_EYEBROW = (
    ".rd[data-mode=\"ks3\"] [data-q-eyebrow]"
    "{font-size:13px;letter-spacing:0.14em;color:var(--st-body)}"
)


# ── the six themes' tokens, for a page that has no grafted `:root` ───────
#
# ⊕ RULED 23 Aug 2026 — THE ASSIGNMENT'S SCORECARD FOLLOWS THE BENCH THEME.
#
# The end-of-assignment card — MARKED · WEEK 01, the score, the fraction, the
# RIGHT / WRONG / MISSED / TIME TAKEN row — is painted in exactly the family
# the class page's bench is: `--st-room-panel` for its ground, `--st-cream` for
# its figures, `--st-ember` for its kicker. `_THEME_BRIDGE` already knows how
# to remap all three. It could not be used here for one reason, which was
# MEASURED rather than assumed: `grep -c -- '--b-ground' student/assignment.html`
# returned 0. The bridge maps `--st-*` onto `--b-*`, and on this page `--b-*`
# does not exist — so every one of its declarations would have resolved to
# nothing and the card would have gone from fixed-dark to unpainted.
#
# The tokens exist on the class view because Design's amended delivery carries
# them in a `<style>` at donor node 7, and that node is grafted in whole.
#
# ⚠️ GRAFTING THAT NODE HERE TOO WAS THE FIRST IDEA AND IT IS NOT SAFE. Donor 7
# is not a token block; it is the amended page's entire stylesheet. Alongside
# the `--b-*` and `--pg-*` sets it carries `.wk[data-sel="1"]`, `.tab[data-on]`,
# `.lbchip`, `.sw`, `.stbtn`, `.pip`, `.rprog`, the `.fcflip` keyframes — and
# `.opt[data-st="picked"] { --opt-bg: var(--b-inset); … }`. The assignment page
# is BUILT out of `.opt` elements: every answer a student picks is one. Grafting
# the block to obtain ten custom properties would have quietly restyled the
# question screen of a page 135 students answer homework on.
#
# ⚑ SO THE TOKENS ARE EXTRACTED, AND EXTRACTED RATHER THAN RETYPED. Ten values
# and six themes' worth of overrides is sixty-six numbers; typed out here they
# would be a second copy of Design's palette, correct on the day it was pasted
# and drifting from that day on. This reads Design's own `<style>` out of the
# compiled donor and emits only what it is looking for, so a value Design moves
# moves here too — the same argument `--st-docket-paper` makes for being a
# capture instead of a hex.
#
# ⚠️ WHAT IT REFUSES TO SHIP. `--b-*` ONLY: every other declaration in that
# block, custom property or rule, is dropped. Six theme rules exactly, or the
# build stops — five would ship a picker with a swatch that does nothing, and
# seven would mean Design added a theme nobody has ruled on. And every property
# a theme rule sets must be one `:root` also defines, so a theme can never
# introduce a token that has no default underneath it.
_THEME_NAMES = ("clay", "chalk", "moss", "harbour", "damson", "graphite")


def bench_theme_tokens(donor_roots):
    """Design's `--b-*` defaults and its six theme overrides, and nothing else."""
    import re

    texts = []

    def walk(node):
        if not isinstance(node, dict):
            return
        if node.get("t") == "style":
            for kid in node.get("c") or []:
                if isinstance(kid, dict) and kid.get("t") == "#":
                    texts.append(str(kid.get("v") or ""))
        for kid in node.get("c") or []:
            walk(kid)

    for root in donor_roots or ():
        walk(root)
    src = "\n".join(t for t in texts if "--b-ground" in t)
    if not src:
        raise SystemExit(
            "build_student_port.py: no `<style>` in the compiled 'class view "
            "amendments' declares `--b-ground`. The six bench themes are "
            "Design's and this build reads them out of Design's own delivery "
            "rather than restating them; it will not invent a palette. "
            "Re-compile the templates, or re-anchor bench_theme_tokens().")

    decls = re.compile(r"(--b-[a-z0-9-]+)\s*:\s*([^;}]+)")

    root_match = re.search(r":root\s*\{(.*?)\}", src, re.S)
    if not root_match:
        raise SystemExit(
            "build_student_port.py: Design's amended stylesheet has no `:root` "
            "block to read the bench-theme defaults out of.")
    base = decls.findall(root_match.group(1))
    if not base:
        raise SystemExit(
            "build_student_port.py: Design's `:root` declares no `--b-*` "
            "token. Without the defaults, the attribute being ABSENT would "
            "paint nothing rather than harbour.")
    known = {name for name, _ in base}

    out = [":root{%s}" % "".join(
        "%s:%s;" % (n, v.strip()) for n, v in base)]

    seen = []
    for name, body in re.findall(
            r'\[data-bench-theme="([a-z]+)"\]\s*\{([^}]*)\}', src):
        rule = decls.findall(body)
        stray = sorted({n for n, _ in rule} - known)
        if stray:
            raise SystemExit(
                "build_student_port.py: Design's %r theme sets %s, which "
                "`:root` does not define. A theme token with no default under "
                "it is unpainted on every OTHER theme, silently."
                % (name, ", ".join(stray)))
        seen.append(name)
        out.append('[data-bench-theme="%s"]{%s}' % (
            name, "".join("%s:%s;" % (n, v.strip()) for n, v in rule)))

    if tuple(seen) != _THEME_NAMES:
        raise SystemExit(
            "build_student_port.py: expected Design's six bench themes %s in "
            "that order and read %s out of the amended stylesheet. The picker "
            "offers six; a page that defines a different set has swatches "
            "that do nothing." % (list(_THEME_NAMES), seen))

    return "".join(out)


def page_html(spec, tpl, roots, bind_table, logic, fixture=False,
              versions=None, bench_css=""):
    tail = (
        "<script src=\"/shared/%s\"></script>\n"
        "<script>window.__MRB_MOUNT__();</script>\n" % spec["fixture_js"]
    ) if fixture else (
        "<script src=\"%s\"></script>\n" % LIVE_JS_URL
    )
    # ⚠️ EMITTED ON BOTH PAGES, including the fixture, which never reads it.
    # `student_behaviour.py` and `student_themes.py` both document the fixture
    # as "the same bytes apart from its banner and its last two script tags",
    # and that sentence is why they are allowed to measure the fixture and
    # report on the production page. A tag on one and not the other would make
    # it false — for a JSON blob no student can see. One line of dead weight on
    # the fixture is the cheaper side of that trade.
    dep_map = (
        "<script>window.__MRB_ASSET_V__=%s;</script>\n"
        % json.dumps({k: v for k, v in sorted((versions or {}).items())
                      if k in STAMPED_DEPS or k == LESSON_INDEX_NAME},
                     separators=(",", ":"))
    )
    return stamp_versions((
        # ⚑ THE <title> CARRIES NO CLASS. It used to read
        # `8r/Sc1 · My class · MrBadmusAI` on the production page — one real
        # class's name shipped in a file whose own banner says it holds no
        # data — and it survived the seam for a structural reason rather than
        # an oversight: the runtime renders into `#mrb-student` and never
        # touches `<head>`, so no binding can reach a `<title>`.
        #
        # So the static title says only what is true of every class, and the
        # class's own name is written onto it AT MOUNT, through the same
        # `MRB_DATA` as every other value. A page with no data source
        # therefore gets no class in its title rather than somebody else's,
        # and the fixture page still renders the exact title Design's file
        # carries.
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<style>body{margin:0;background:#FBF3E6}"
        "a{color:var(--ks3-accent-text);text-decoration:none}"
        "a:hover{color:var(--ks3-accent-hover)}"
        "button{font-family:inherit}"
        "%s</style>\n"
        "</head>\n<body>\n"
        "<div id=\"mrb-student\" style=\"background:var(--st-ground);"
        "min-height:100vh\"></div>\n"
        "<script src=\"/shared/student-runtime.js\"></script>\n"
        "<script>window.__MRB_TPL__=%s;</script>\n"
        "<script>window.__MRB_BIND__=%s;</script>\n"
        "<script>\n%s\n</script>\n"
        "<script>\n%s\n</script>\n"
        "%s"
        "%s"
        "</body>\n</html>\n"
        % (html.escape(spec["title"]),
           (_BANNER_FIXTURE % (spec["page"].capitalize(), spec["out"]))
           if fixture else
           (_BANNER % (spec["page"].capitalize(), LIVE_JS_NAME,
                       spec["fixture_out"])),
           DS_CSS_URL,
           # ⊕ 22 Aug 2026 — the theme bridge, class view only. See above.
           # ⊕ 23 Aug 2026 — and the espresso page chrome beside it.
           # ⊕ 23 Aug 2026 — and the assignment has one of its own now, so
           # this is a choice between two pages rather than a class-view flag.
           # Each page emits only rules whose selectors could match ON it: a
           # rule that can never match is a rule nothing can tell is broken.
           # ⊕ 23 Aug 2026 — and the flashcards stage's height ceiling.
           # ⊕ 23 Aug 2026 — and the assignment takes the BRIDGE now too, for
           # its scorecard (node 293), preceded by the `--b-*` tokens the
           # bridge maps onto: the class view is grafted them and this page is
           # not. `_PAGE_STRONG` and `_PIP_ROW` stay class-view-only — checked
           # rather than assumed: there is no `[data-page-strong]` and no
           # `[data-pip-row]` anywhere in the assignment template, so both
           # would be rules nothing could tell were broken.
           ((_THEME_BRIDGE + _PAGE_STRONG + _PIP_ROW + _CARD_FIT)
            if spec["page"] == "class view"
            else (bench_css + _THEME_BRIDGE + _Q_EYEBROW)),
           json.dumps({"roots": roots, "imports": tpl["imports"]},
                      separators=(",", ":")).replace("<", "\\u003c"),
           json.dumps(bind_table, separators=(",", ":")),
           # Design's logic class, with DCLogic bound to our base and with
           # Design's example data lifted out to `MRB_DATA`. Everything else
           # about it is still verbatim.
           "/* No data reaches this page except through here, and there is no\n"
           "   fallback. A missing key is a THROWN ERROR and a blank page,\n"
           "   deliberately: the alternative to a blank page is one child's\n"
           "   marks shown to a different child, and a page that is confidently\n"
           "   wrong about a child's homework is worse than a page that is\n"
           "   plainly broken. */\n"
           "function MRB_DATA(k){var d=window.__MRB_DATA__;"
           "if(!d||!(k in d))throw new Error('student page: no data for \"'"
           "+k+'\"');return d[k];}\n"
           "var DCLogic = window.MrBadmusStudentRuntime.MrbLogic;\n"
           "var StreamableLogic = DCLogic;\n" + logic,
           # ⚠️ DECLARED, NOT CALLED. Whoever loads the data calls it, which is
           # what makes "the production page cannot mount without a data
           # source" a property of the file rather than a promise about it.
           "window.__MRB_MOUNT__ = function () {\n"
           "  /* The <head> is not rendered by the runtime, so the class name\n"
           "     arrives here instead — after the data, through the same throw\n"
           "     as everything else. */\n"
           "  document.title = " + spec["title_expr"] + ";\n"
           "  var R = window.MrBadmusStudentRuntime;\n"
           "  var tpl = window.__MRB_TPL__;\n"
           "  return R.mount({\n"
           "    into: '#mrb-student',\n"
           "    template: {roots: R.applyBindings(tpl.roots, "
           "window.__MRB_BIND__, MRB_DATA), imports: tpl.imports},\n"
           "    imports: tpl.imports,\n"
           "    Component: Component,\n"
           "    props: {}\n"
           "  });\n"
           "};",
           dep_map,
           tail)),
        versions or {})


def write(path, body):
    _refuse(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def _verify_stamps(stamped, pages):
    """Re-read from disk and refuse to finish if any stamp names other bytes.

    ⚑ THE ORDERING IS THE WHOLE UNIT, so it is asserted rather than commented.
    A `?v=` naming content that is not the content being served is worse than
    no `?v=` at all: the page looks fixed, the browser caches the wrong bytes
    under a URL that will never change again, and every gate stays green. The
    only way to know the stamp is honest is to hash the file that will actually
    be deployed, AFTER everything that writes it has run.

    Three checks, and each one has caught a different mistake in rehearsal:

      1. every stamp matches the deployed copy under `mrbadmus_site/shared/`;
      2. every stamp matches the repo-root copy under `shared/`, where one
         exists — the two trees are round-tripped and must not disagree;
      3. no `/shared/…` reference survives in a built page WITHOUT a stamp,
         so adding a fourth asset to `page_html` and forgetting the map is a
         red build rather than a silent hole four hours wide.
    """
    bad = []
    for name, want in sorted(stamped.items()):
        for tree in (SHARED_OUT, "shared"):
            path = os.path.join(tree, name)
            if not os.path.exists(path):
                # Only the deployed copy of a dependency this build does not
                # write can legitimately be absent — a bare `build_student_port`
                # run in a tree where `generate_site_v5.py` has never run.
                if tree == SHARED_OUT and name in STAMPED_DEPS:
                    print("        ⚠️  %s/%s is missing — %s has not run here, "
                          "so the stamp could not be checked against the "
                          "deployed copy" % (tree, name, "generate_site_v5.py"))
                    continue
                bad.append("%s/%s does not exist, but a page stamps it "
                           "?v=%s" % (tree, name, want))
                continue
            with open(path, "rb") as fh:
                got = asset_hash(fh.read())
            if got != want:
                bad.append(
                    "%s hashes %s but the pages shipped ?v=%s — the stamp "
                    "names content that is not what will be served. Run "
                    "`python3 build_all.py`, which publishes shared/ before "
                    "this build stamps it." % (path, got, want))

    # ⚠️ WRITTEN AS AN OPTIONAL GROUP, NOT A NEGATIVE LOOKAHEAD, and the first
    # draft was the lookahead. `/shared/[\w.-]+(?!\?v=)` is satisfied by
    # BACKTRACKING one character: on the correctly stamped
    # `/shared/student-ds.css?v=1a2b3c4d` it matched `/shared/student-ds.cs`,
    # saw that `s` is not `?v=`, and reported a perfectly stamped page as
    # unstamped — twelve times. A check that cannot be trusted when it is red
    # is no better than one that cannot be trusted when it is green.
    #
    # Matching the stamp OPTIONALLY and testing whether it was captured has no
    # such ambiguity: `?` is not in the character class, so the greedy run
    # stops exactly at the end of the filename every time.
    #
    # `finditer` rather than a lookup of the first occurrence: a page linking
    # the same asset twice, once stamped and once not, must report the bad one.
    linked = re.compile(r'/shared/[A-Za-z0-9._/-]+(\?v=[0-9a-f]+)?')
    for tree in (SITE_OUT, MIRROR_OUT):
        for spec in pages:
            for key in ("out", "fixture_out"):
                path = os.path.join(tree, spec[key])
                if not os.path.exists(path):
                    continue
                page = open(path, encoding="utf-8").read()
                for m in linked.finditer(page):
                    if m.group(1):
                        continue
                    bad.append(
                        "%s links %s with no cache-bust stamp, at offset %d. "
                        "Every asset a student page names must be in the "
                        "version map — see STAMPED_DEPS and build()."
                        % (path, m.group(0), m.start()))
    if bad:
        raise SystemExit(
            "build_student_port.py: the cache-bust stamps are not honest.\n  "
            + "\n  ".join(bad))
    print("     ✅ cache-bust: %d asset(s) stamped from their own content, "
          "each re-hashed from disk — %s"
          % (len(stamped), ", ".join("%s=%s" % (n, v)
                                     for n, v in sorted(stamped.items()))))


def build():
    if not os.path.exists(TEMPLATES):
        raise SystemExit(
            "build_student_port.py: %s is missing. Run `python3 "
            "student_template.py` — the template and the logic are compiled "
            "out of Design's delivery, never typed." % TEMPLATES)
    tpls = json.load(open(TEMPLATES, encoding="utf-8"))

    print("\n🎓  build_student_port — Design's template and logic, "
          "on our runtime\n")

    css, sizes = ds_css()

    wanted = set()
    for spec in PAGES:
        t = tpls.get(spec["page"])
        if t:
            wanted |= referenced_tokens(t)
    css, topped = top_up(css, wanted, tpls)
    print("     %d token(s) referenced by the two pages; %d not in Design's "
          "bundle and topped up from shared/tokens.css%s"
          % (len(wanted), len(topped),
             (": " + ", ".join(topped)) if topped else ""))

    for out_dir in (SHARED_OUT, "shared"):
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, DS_CSS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(css)
    print("     ✅ %-24s %7d bytes, %d sheet(s), linked and cached once"
          % (DS_CSS_NAME, len(css), len(sizes)))

    # ⚑ THE VERSION MAP IS BUILT FROM CONTENT, and every asset it names is
    # PUBLISHED BEFORE THE PAGE THAT NAMES IT IS WRITTEN. Both halves matter.
    versions = {DS_CSS_NAME: asset_hash(css)}
    stamped = dict(versions)   # every hash any page shipped — see _verify_stamps

    # ── the runtime is mirrored HERE, not left to the KS4 generator ──────
    #
    # ⚑ THIS COST A RED GATE. Both pages load `/shared/student-runtime.js`, and
    # until now nothing in this build put it there — `generate_site_v5.py`
    # glob-copies `shared/` into the output, so the served copy was whatever
    # the last full site build happened to leave. Editing the runtime and
    # re-running this build therefore produced a page that loaded the OLD
    # runtime, and the failure arrived as `R.applyBindings is not a function`
    # from a file that plainly contained `applyBindings`.
    #
    # A build that emits a page depending on a file it does not publish is a
    # build with a hidden prerequisite. This one publishes it.
    #
    # ⊕ 23 Aug 2026 — MOVED, from the last thing this build did to one of the
    # first, and the move is the whole point of the cache-bust unit rather
    # than tidying.
    #
    # A stamp that names the WRONG content is worse than no stamp, because it
    # looks fixed. Written where it used to be, the runtime, the live source
    # and the lesson index were all published AFTER the pages loop — so a
    # stamp computed inside that loop from `mrbadmus_site/shared/` would have
    # read the PREVIOUS build's copy and pinned the page to bytes this build
    # was about to overwrite. The page would then carry `?v=<yesterday>` and
    # be served today's file under it: the four-hour skew, made permanent and
    # given a green build.
    #
    # `ks3-lesson-urls.js` is the sharpest case, because this build GENERATES
    # it — there is no source file to fall back on, so the only correct hash is
    # of the bytes about to be written.
    #
    # Two independent guards, and neither is a convention:
    #   · publish first, stamp second — the ordering above;
    #   · `_verify_stamps()` at the end of build(), which re-reads every file
    #     from disk and refuses to finish if any hash disagrees with the stamp
    #     that shipped.
    idx_js, n_lessons = lesson_index()
    for out in (os.path.join("shared", LESSON_INDEX_NAME),
                os.path.join(SHARED_OUT, LESSON_INDEX_NAME)):
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(idx_js)
    versions[LESSON_INDEX_NAME] = asset_hash(idx_js)
    print("     ✅ %-24s %7d bytes  (%d KS3 lesson(s), every page checked on "
          "disk)" % (LESSON_INDEX_NAME, len(idx_js), n_lessons))

    for name in (RUNTIME_JS_NAME, LIVE_JS_NAME):
        src = os.path.join("shared", name)
        if not os.path.exists(src):
            raise SystemExit(
                "build_student_port.py: shared/%s does not exist, and both "
                "pages load it. Without it they mount nothing at all — which "
                "is the correct failure and still a failure." % name)
        text = open(src, encoding="utf-8").read()
        with open(os.path.join(SHARED_OUT, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        versions[name] = asset_hash(text)
        print("     ✅ %-24s %7d bytes  (%s)"
              % (name, len(text),
                 "STUB — throws; the live data source is not wired yet"
                 if "not wired yet" in text else "published, not assumed"))

    # The five `student-live.js` loads for itself. These four are published by
    # `generate_site_v5.py`'s glob copy of `shared/`, not by this build, so
    # they are hashed from the SOURCE tree — the one input both generators
    # agree on, and the same choice `build_ks3.asset_versions` documents at
    # length. `_verify_stamps()` then checks the deployed copy really does
    # match, so the agreement is asserted rather than assumed.
    for name in STAMPED_DEPS:
        src = os.path.join("shared", name)
        if not os.path.exists(src):
            raise SystemExit(
                "build_student_port.py: shared/%s does not exist, and "
                "student-live.js loads it on every student page. A missing "
                "dependency is a blank class page." % name)
        with open(src, "rb") as fh:
            versions[name] = asset_hash(fh.read())

    # ⊕ RULED 23 Aug 2026 — Design's six themes' tokens, read out of Design's
    # own amended stylesheet ONCE, for the page that has no grafted `:root` to
    # get them from. See `bench_theme_tokens` for why they are extracted rather
    # than retyped, and why the whole donor block is not grafted instead.
    bench_css = bench_theme_tokens((tpls.get(DONOR_PAGE) or {}).get("roots"))
    print("     %d bench-theme rule(s) read from Design's amended stylesheet, "
          "%d bytes, emitted onto the assignment page only"
          % (len(_THEME_NAMES) + 1, len(bench_css)))

    for spec in PAGES:
        tpl = tpls.get(spec["page"])
        if not tpl:
            raise SystemExit("build_student_port.py: %s has no entry for %r"
                             % (TEMPLATES, spec["page"]))

        # ⚠️ THE RULINGS COME FIRST, and the order is load-bearing in one
        # direction only: the class view's ruling deletes template nodes, and
        # the binding paths are index paths into `c`. Binding against the raw
        # template and then pruning would leave every path after node 275
        # pointing one sibling to the left — the class name would appear where
        # the term label belongs, and it would look like a data bug.
        donor_tpl = tpls.get(DONOR_PAGE)
        (logic, ruled_roots, n_rep, n_pruned, n_wired,
         n_grafted, n_attred, n_exprd, n_wrapped, n_moved) = apply_rulings(
            spec["page"], tpl["logic"], tpl["roots"],
            donor=(donor_tpl or {}).get("roots"))
        ruled_tpl = {"roots": ruled_roots, "imports": tpl["imports"]}

        # ⚠️ THE BINDINGS ARE READ BEFORE THE SEAM, not after. They used to
        # run the other way round and the order did not matter, because the
        # seam only cut fields out of the logic. It matters now: the method-
        # body seams splice `termLabel` back into two of Design's strings, and
        # they are checked against what the markup binds that key to rather
        # than trusting that the two agree. `bindings_for` reads only the
        # template, so moving it earlier changes nothing else.
        bind_table, bind_values = bindings_for(spec["page"], ruled_tpl)
        logic, data_literals, n_welded = seam_logic(
            spec, logic, spec["page"], bind_values)
        # ⊕ 23 Aug 2026 — PHASE 2. Design's own sample deck, lifted out of the
        # AMENDED delivery's logic so the fixture renders the grafted
        # flashcard surfaces exactly as Design draws them. See DONOR_LIFTS.
        n_donor = donor_lifts(spec["page"], (donor_tpl or {}).get("logic"),
                              data_literals)
        roots = scrub_roots(ruled_roots, bind_table)

        # ⚑ THE FIXTURE'S DATA FILE IS WRITTEN BEFORE THE PAGE THAT LINKS IT,
        # for the reason the version map's own comment gives: the fixture page
        # carries `student-fixture-<page>.js?v=<hash>`, and the only honest
        # hash is of the bytes this build is about to write. Computed after,
        # it would name the previous run's example data.
        js = fixture_js(spec, spec["page"], data_literals, bind_values)
        for out_dir in (SHARED_OUT, "shared"):
            with open(os.path.join(out_dir, spec["fixture_js"]), "w",
                      encoding="utf-8") as fh:
                fh.write(js)
        page_versions = dict(versions)
        page_versions[spec["fixture_js"]] = asset_hash(js)
        stamped.update(page_versions)

        body = page_html(spec, tpl, roots, bind_table, logic, fixture=False,
                         versions=page_versions, bench_css=bench_css)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["out"]), body)

        fix_body = page_html(spec, tpl, roots, bind_table, logic, fixture=True,
                             versions=page_versions, bench_css=bench_css)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["fixture_out"]), fix_body)

        # ⚑ ASSERTED, NOT ASSUMED — and precise about what is asserted.
        # ── what this build GUARANTEES, and what it only reports ─────────
        #
        # GUARANTEED, on pain of SystemExit: no bound identity string survives
        # in the template the production page ships. That is the half this
        # unit owns — the binding table and the scrub are both its work, so a
        # leak there is its bug and not a finding about somebody else's.
        #
        # REPORTED, not failed: Design's example data does not live only in
        # the class fields, and this loop is what finds the rest of it. The
        # shout-outs, the crumb rail, the leaderboard scope note, the two
        # stray copies of the week number, the docket's four facts and its
        # countdown, the retrieval count and its percentage, the round note,
        # the rounds tally and the streak floor are ALL closed now, by LIFTS
        # and REWRITES above.
        #
        # ⊕ 22 Aug 2026 — this comment used to end by naming those figures as
        # "still welded … lifting them is the next unit's". They are lifted.
        # What is left, and is reported rather than failed, is named in the
        # findings on that unit: `shoutCount`'s `'02'`, the bench task's
        # "Answer the eight questions", and the leaderboard's 0.4 / 0.19 /
        # 160 / 80 weightings, which are the ruled-and-costed MRB-275 split
        # rather than this build's to close.
        tpl_blob = json.dumps(roots, ensure_ascii=False)
        stuck = []
        for key, val in sorted(bind_values.items()):
            if not val.strip():
                continue
            if json.dumps(val, ensure_ascii=False) in tpl_blob:
                raise SystemExit(
                    "build_student_port.py: %s — the literal %r is STILL a "
                    "text node in the shipped template after the scrub, so "
                    "the binding for %r is cosmetic and the production page "
                    "carries the value anyway. The binding table and the "
                    "scrub disagree." % (spec["out"], val, key))
            for form in ("'%s'" % val.strip(), '"%s"' % val.strip()):
                if form in logic:
                    stuck.append((key, val.strip()))
                    break
        for key, val in stuck:
            print("        ⚠️  %-16s is bound in the markup but Design's logic "
                  "also writes %r inline (not a field — %s)"
                  % (key, val, "renderVals"))
        if stuck:
            print("        ⚠️  those are Design's example data too, welded "
                  "into method bodies rather than into initialisers, and "
                  "still welded — LIFTS/REWRITES close the named ones, not "
                  "every one.")

        if n_rep or n_pruned or n_wired:
            print("        ⊕ rulings: %d ruled edit(s) to Design's logic, "
                  "%d template subtree(s) pruned, %d handler(s) attached, "
                  "%d subtree(s) grafted from the amendments, %d node(s) "
                  "named for the themes, %d loop expression(s) renamed, "
                  "%d node(s) made conditional, %d handler(s) retargeted — "
                  "from student_rulings.py, not from a hand edit to the "
                  "built page"
                  % (n_rep, n_pruned, n_wired, n_grafted, n_attred, n_exprd,
                     n_wrapped, n_moved))
        print("     ✅ %-24s %7d bytes  (%d template node(s), "
              "%d chars of Design's logic, 0 bytes of data)"
              % (spec["out"], len(body), count_nodes(roots), len(logic)))
        print("        %-21s %7d bytes  (+%d binding(s) applied at mount)"
              % (spec["fixture_out"], len(fix_body), len(bind_table)))
        print("        %-21s %7d bytes  (%d field(s) lifted from the logic, "
              "%d identity string(s) from the markup)"
              % (spec["fixture_js"], len(js), len(data_literals),
                 len(bind_values)))
        if n_donor:
            print("        ⊕ %d literal(s) lifted out of the AMENDED "
                  "delivery's own logic for the fixture — see DONOR_LIFTS"
                  % n_donor)
        if n_welded:
            print("        ⊕ %d data seam(s) closed inside METHOD BODIES "
                  "rather than initialisers — see LIFTS and REWRITES"
                  % n_welded)

    _verify_stamps(stamped, PAGES)

    print("\n     → %s/  and  %s/  (mirror)" % (SITE_OUT, MIRROR_OUT))
    print("\n     ⚠️  *-ported.html carry NO data and do not mount themselves; "
          "%s does that.\n         *-fixture.html carry Design's example data "
          "and are what the gates drive.\n         Neither is a candidate to "
          "replace a live page.\n" % LIVE_JS_NAME)


if __name__ == "__main__":
    sys.path.insert(0, REPO)
    build()
