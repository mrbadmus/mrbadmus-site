"""B2 L4 — Biomechanics: forces in the body (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b2/b2-04-biomechanics-forces-in-the-body.dc.html`
(1,028 lines), and its measured specification,
`docs/ks3/b2-inventory/PAYLOAD-MAP.md` §4 and §C1–C9.

── Owned by BIOLOGY, and that is a ruling, not a convenience ─────────────

Ruled by Mide, 16 Aug 2026 (NOTES flag 1, closed). The 2014 KS3 programme of
study names biomechanics inside the biology section, under the skeletal and
muscular systems, *"including the measurement of force exerted by different
muscles"*. `docs/ks3/statutory-register.md` line 67 records `KS3.B.SKEL.02`
against B2, and `ks3_data/structure.py` line 74 declares this slot as a plain
three-tuple with no `owned_by` — so the slot was already B2's and nothing in
either file needed changing. Verified, not assumed.

The clause the statement makes load-bearing is the measurement one, and it is
`#s-meters`: three muscle groups, three readings each, a mean for each. That
block is the reason this lesson is a biology lesson rather than a physics
lesson wearing an arm.

── The word `moment` does not appear, and two occurrences were removed ───

Also Mide's ruling. The relationship is taught as **turning effect = force ×
distance from the joint**; *moment* is introduced in P4, where it is assessed.
Design's own NOTES claim the word is absent from the page; it is not, twice,
and both are corrected here — see `⊕ CORRECTION` at the hook prompt and at
`ks4_becomes`.

The P4 relationship is therefore a `references` EDGE (data), never prose, and
this lesson assumes **no prior physics teaching whatsoever**: a school may run
P4 in Year 8 and B2 in Year 9, so a sentence like "as you saw in physics"
would break silently on half the schools using it. Nothing here says it.

── MRB-204 as amended, in Design's own order ────────────────────────────

    formula alone  →  triangle  →  staged worked example  →  the student's own
    four steps, from the student's own rig  →  and only then the ladder

This lesson is a PRODUCT, so it takes the TRIANGLE (payload map §4.3 row 5).
The balance beam is for sums and conservation statements and is not drawn
here. Inside the formula and the FIFA steps the arrows are drawn by the
component; in running prose a `→` is typed and read aloud by `t()`'s mark
substitution. No prose here needs one.

── Three new instruments, and one that widens ───────────────────────────

`arm-lever` (#s-bench, canvas, static), `lever-steps` (#s-build) and
`meter-compare` (#s-meters) are new kinds; their renderer, CSS, wiring and
parity rows ship as fragments in `scratchpad/b2/frag/`. `cover-triangle`
already exists as `r_formula_triangle` and its PAYLOAD WIDENS — a `result`
slot per cell, three closing blocks instead of one, and Design's button order
with `F` pre-covered. That widening is `cover-triangle.widening.md`; it is not
edited into `build_ks3.py` from here.

Everything else is reuse: `job-sort` is not needed on this page, but
`_head_counter`, `r_bench_gate`, the two-paragraph reveal, `r_fifa`'s chipped
staged steps and `r_ladder` all are, and none of them is re-implemented.
"""

# ── the rig's defaults, in one place ────────────────────────────────────
#
# `lever-steps` computes its own option text from these through the live
# instrument, and the RESTING render (before any JS runs) is computed from
# them at build time by `r_lever_steps`, which reads this activity by id.
# They are written once, here, because two copies of "4 cm" is two places for
# the arithmetic to stop agreeing with the drawing.
_LOAD_KG, _INS_CM, _HAND_CM, _G = 2.0, 4.0, 32, 10

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 74 character for character.
    "slug":        "biomechanics-forces-in-the-body",
    "title":       "Biomechanics: forces in the body",
    "discipline":  "biology",
    "unit":        "movement-skeleton-and-muscles",
    "family":      "QUANTITATIVE",

    # `KS3.B.SKEL.02` — "biomechanics – the interaction between skeleton and
    # muscles, including the measurement of force exerted by different
    # muscles" (statutory register line 67, attributed to B2). B2's other
    # three lessons take SKEL.01a, SKEL.01b and SKEL.03, so this is the one
    # remaining statement in the unit and the key stage keeps exactly-once
    # coverage. Nothing else in KS3 claims it.
    "covers":      ["KS3.B.SKEL.02"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    "requires":    ["antagonistic-muscle-pairs"],
    "assumes":     [],

    # ⚖️ THE P4 RELATIONSHIP IS AN EDGE, NEVER PROSE (Mide, 16 Aug).
    #
    # Design drew endmatter card 2 as a prose paragraph — *"Physics: Forces —
    # where the turning effect of a force is developed on its own, away from
    # the body."* Prose asserts a sequence, and the sequence is not ours to
    # assert: a school can teach P4 in Year 8 and B2 in Year 9. As data, the
    # graph carries the relationship and the card renders the honest
    # "coming soon" treatment `lesson_page` already has for a unit that is not
    # authored yet, so no prose-only endmatter card is needed and payload map
    # §4.6 note 6 closes without a new card shape.
    #
    # ⚠️ `label` OVERRIDES THE RESOLVED TITLE, and here that is the ruling
    # rather than a preference: P4's slot is titled "Moments: the turning
    # effect", and rendering the target's own title would print the one word
    # this unit may not contain. See `lesson-page.deltas.md`.
    "references":  [{"unit": "P4", "lesson": "moments",
                     "label": "Physics: Forces",
                     "why": "Where the turning effect of a force is developed "
                            "on its own, away from the body."}],
    "connects_heading": "Taught in full in",
    "ks4_links":   [],

    "big_question": "Holding a 2 kg dumbbell, your biceps pulls with about "
                    "160 newtons. Why is it working eight times harder than "
                    "the weight it is holding?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # SIX stops, not five: b2-01/02/03 have five, and NOTES §6 says of this
    # page "six in b2-04 — the extra one is the force-meter comparison the
    # statutory statement asks for". Page lines 517–524; tick conditions
    # 794–802. Every anchor below names a section this lesson emits, and each
    # of those sections carries a completion signal `doneByDom()` reads.
    #
    # The triangle (block 5) and the worked example (block 6) are deliberately
    # NOT stops. Both are read rather than done, and MRB-208 says the rail
    # carries only sections that require the student to do something.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Eight times harder", "done_when": "committed"},
        # ⚠️ A SET, never a press count: two DIFFERENT controls moved, and the
        # meter fitted. Design's own predicate (`Object.keys(touched).length
        # >= 2 && meterShown`) is already a set, and it is reproduced as a set.
        {"anchor": "s-bench",  "short": "RIG",
         "label": "The forearm rig", "done_when": "rig_measured"},
        {"anchor": "s-build",  "short": "STEPS",
         "label": "Your own four steps", "done_when": "steps_opened"},
        {"anchor": "s-meters", "short": "METERS",
         "label": "Three force meters", "done_when": "ranked"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What levers buy", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "The muscle is losing, badly, and it is built that way on "
                 "purpose.",
        # ⊕ CORRECTION 1 of 2 (Mide's ruling, 16 Aug). Design's line reads
        # "Your biceps, at that moment, is pulling with about 80 N". That is
        # the everyday word for an instant and not the physical quantity — but
        # the ruling is that the word does not appear anywhere in B2, and a
        # student who meets *moment* here and again in P4 as a quantity has
        # been given a collision for nothing. "at that instant" says the same
        # thing and costs nothing.
        "prompt": "Hold a bag of sugar on your flat hand. It weighs 10 N. "
                  "Your biceps, at that instant, is pulling with about 80 N — "
                  "and it is attached only about 4 cm from your elbow, while "
                  "the bag sits about 32 cm away.",
        "commit": "Something about that arrangement is doing the damage. What?",
        "options": [
            "Muscles are simply weak for their size",
            "The two distances from the elbow are very different",
            "The bag is heavier than it looks",
            "The forearm bones get in the way of the pull",
        ],
        "reveal": "The two distances. A force that acts a long way from a "
                  "joint has far more turning effect than the same force "
                  "acting close to it — and your muscles are all attached "
                  "close in. That is the trade this whole lesson is about, "
                  "and it can be worked out to the newton.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # NOTES §5's proposed `BODY` family, continued from b2-01/02/03, which
    # already write BODY-01…BODY-09. The statement is the line the PAGE
    # quotes wherever the page quotes one — `r_confrontation` renders
    # `misconceptions[].statement` as the “…” at the top of `#s-think`, so a
    # statement that differed from Design's quote would silently replace it.
    "misconceptions": [
        {"id": "BODY-10",
         "statement": "A muscle pulls with the same force as the weight it is "
                      "holding.",
         "elicited_by": "forearm-rig",
         "confronted_by": "forearm-rig"},
        {"id": "BODY-11",
         "statement": "Your arm is a lever, and levers make things easier — "
                      "so the muscle pulls less than the weight.",
         "elicited_by": "think-commit-lever",
         "confronted_by": "think-commit-lever"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    # Fifteen direct children of `.ks3-lesson` on the page; eleven authored
    # blocks here, because the header, the stretch layer, the endmatter and
    # the convention line are emitted by `lesson_page` rather than by `core`.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every force acting on a bone is trying to turn it about a "
                 "joint. How much turning it does depends on two things: how "
                 "big the force is, and how far from the joint it acts."},

        # ── #s-bench — ink-dark `practical` shell (page lines 113–195) ──────
        #
        # ⚖️ THE MUSCLE-FORCE TILE IS THE GATE, AND IT IS THE LESSON.
        # NOTES §3.4: *"the meter exists so the student can check their own
        # arithmetic, not skip it. If Code makes the meter reading available
        # before the calculation, the lesson is gone."* The tile reads
        # `not measured — you work it out` until the meter is fitted, and the
        # muscle arrow on the canvas is never labelled with its magnitude
        # either — the same gate reached by the other route.
        {"type": "arm-lever", "id": "forearm-rig", "anchor": "s-bench",
         "eyebrow": "At the bench · the forearm rig",
         "heading": "Three measurements. The fourth number is yours.",
         # The two-state variant of the block-head counter, not a count: this
         # block has one thing to report and it is a boolean.
         "head_counter": {"off": "Meter not fitted yet", "on": "Meter fitted"},
         "demand": "investigate",
         "targets": "BODY-10",
         "prompt": "The rig gives you the load, and the two distances from "
                   "the elbow. It does not tell you the force in the muscle, "
                   "because that is the thing worth working out.",
         "gate": {
             "prompt": "Commit first. You move the load from 32 cm out to "
                       "16 cm — half the distance. What happens to the force "
                       "the muscle needs?",
             "options": [
                 "It halves",
                 "It doubles",
                 "It stays the same — the load has not changed",
                 "It falls to a quarter",
             ]},
         # Three controls; TWO of them moved, plus the meter, is the rail
         # stop. Authored so the predicate is data rather than a number in a
         # wire function.
         "done_at": 2,
         "load": {"min": 0.5, "max": 5, "step": 0.5, "default": _LOAD_KG,
                  "label": "Mass in the hand"},
         "ins":  {"min": 3, "max": 6, "step": 0.5, "default": _INS_CM,
                  "label": "Muscle attached at"},
         "hand": {"options": [32, 16], "default": _HAND_CM,
                  "label": "Hand distance"},
         # The KS3 convention, stated once on the page in the line at the
         # bottom edge and used here. NOTES flag 2.
         "g": _G,
         # Decimals are DERIVED from each control's `step`, not authored: a
         # step of 0.5 needs one decimal and an integer set needs none, so a
         # `decimals` key would be a second statement of the same fact.
         "formats": {"load": "{n} kg", "ins": "{n} cm", "hand": "{n} cm",
                     "weight": "{n} N", "force": "{n} N"},
         "tiles": {"weight": "Weight of the load",
                   "load_distance": "Load, from the elbow",
                   "muscle_distance": "Muscle, from the elbow",
                   "muscle_force": "Force in the muscle"},
         "unmeasured": "not measured — you work it out",
         "meter": {
             "label": "Fit a force meter to the tendon",
             "label_done": "Meter reading shown",
             "note": "Work it out first. Then fit the meter and see whether "
                     "the rig agrees with you.",
             "note_done": "The meter agrees with the arithmetic, because the "
                          "arithmetic is what the tendon is obeying."},
         # Drawn on the canvas. `load_arrow` takes the computed weight; the
         # muscle arrow takes a bare word, and deliberately no number.
         "canvas": {"title": "THE FOREARM RIG · SIDE VIEW",
                    "joint": "ELBOW",
                    "muscle_arrow": "muscle",
                    "load_arrow": "{n} N"},
         # Composed from the three live values, in Python for the resting
         # render and in JS for every state after it — an authored string
         # would be a fourth copy of the state and would go stale on the
         # first drag.
         "alt": "A side view of a forearm held level. A load of {load} "
                "kilograms hangs from the hand {hand} centimetres from the "
                "elbow, and the muscle pulls upwards {ins} centimetres from "
                "the elbow on the other side of the joint."},

        # ── the formula, alone in its own block (MRB-204 part 1) ────────────
        #
        # ⊕ ADDITION inside a drawn component. Design's section carries the
        # triangle, the three prose lines and no statement line — the
        # relationship is written out only in the KEY FACT and the key note,
        # both of which come later. MRB-204 step 1 is a ruling ("a student
        # flicking back through the lesson to find the formula must be able to
        # see it from the scroll position"), and this is the block that
        # ruling names, so the relationship is stated here in display type.
        # It is the ruled wording, in the ruled place, and it contradicts
        # nothing on the page.
        {"type": "formula", "id": "turning-effect",
         "statement": "Turning effect = force × distance from the joint",
         # MRB-204 part 2 — the cover interaction, on the shape the
         # relationship has. A PRODUCT takes the triangle; the balance beam
         # is the sum's figure and is not drawn here.
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle: turning effect on top, force "
                           "and distance from the joint underneath, "
                           "multiplied together.",
             # ⊕ WIDENED PAYLOAD (payload map §4.6 note 2). Each cell gains a
             # `result` — the arrangement, in display type — beside the
             # sentence that says why. Folding the two into one note loses the
             # line a student actually reads.
             "top":   {"label": "T", "button": "Cover T",
                       "result": "T = F × d",
                       "text": "T is on its own at the top, with the other "
                               "two side by side underneath. Cover it and you "
                               "are left with F × d — multiply."},
             "left":  {"label": "F", "button": "Cover F",
                       "result": "F = T ÷ d",
                       "text": "F sits underneath, with T above it. Cover it "
                               "and you are left with T over d — divide."},
             "right": {"label": "d", "button": "Cover d",
                       "result": "d = T ÷ F",
                       "text": "d sits underneath, with T above it. Cover it "
                               "and you are left with T over F — divide."},
             # Design's own order and default: F, T, d, with F already
             # covered on load — which is the arrangement this lesson needs,
             # because every question on the page solves for the muscle force.
             "order": ["left", "top", "right"],
             "covered": "left",
             # Three trailing blocks, not one paragraph: a prose rule, a mono
             # unit legend, and the balanced condition in display type.
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["T — turning effect, in N m",
                           "F — force, in N",
                           "d — distance from the joint, in m"],
                 # Reworded by Design from a fourth arrangement into the
                 # CONDITION it actually is (NOTES change-log, b2-04).
                 "condition": "Nothing moving: F₁ × d₁ = F₂ × d₂"}}},

        # ── the worked example (MRB-204 part 3) — read, not done ────────────
        {"type": "worked-example", "id": "dumbbell-worked"},

        # ── #s-build (MRB-204 part 4) — the same four steps, on the student's
        # own rig. Light block on the inset ground.
        {"type": "lever-steps", "id": "your-four-steps", "anchor": "s-build",
         "ground": "inset",
         "eyebrow": "Your turn · the same four steps",
         # ⚠️ LIVE. The heading quotes the rig the student left set, so the
         # two blocks are visibly the same problem. Filled at build time from
         # the rig's defaults and repainted whenever a control moves.
         "heading": "Your rig: {load} kg at {hand} cm, muscle at {ins} cm.",
         "demand": "construct",
         "prompt": "Commit to each line, then open the worked version and "
                   "compare it with yours.",
         # The instrument this one reads. A build-time error if it is missing
         # or is not an `arm-lever`, rather than a panel of empty templates.
         "rig": "forearm-rig",
         "picks": [
             {"label": "Step 1 · Formula",
              "question": "Nothing is moving, so the two turning effects are "
                          "equal. Which line says that?",
              "options": [
                  "F × d(muscle) = W × d(load)",
                  "F × d(load) = W × d(muscle)",
                  "F = W × d(muscle) × d(load)",
              ]},
             # ⚖️ The distractors are GENERATED, not authored: they are this
             # student's own numbers arranged three ways. Authoring them would
             # fix the rig at 2 kg and make every other setting unanswerable.
             {"label": "Step 2 · Insert",
              "question": "Put your rig's numbers in, with the distances in "
                          "metres.",
              "options": [
                  "F × {dM} = {W} × {dL}",
                  "F × {dL} = {W} × {dM}",
                  "F = {W} × {dM} × {dL}",
              ]},
         ],
         "field": {"label": "Steps 3 and 4 · Work it out, then answer",
                   "question": "Divide, round to the nearest newton, and "
                               "choose the unit.",
                   "hint": "Your answer as a number",
                   "placeholder": "0",
                   "unit_hint": "Unit",
                   # ⚠️ Empty value on the placeholder option, or the open
                   # button unlocks for a student who never chose a unit.
                   "unit_placeholder": "choose a unit",
                   "units": ["N", "kg", "m", "N m"]},
         "button": "Show the four steps",
         "progress": {"format": "{n} of 3 lines committed", "done": "Opened"},
         "reveal_head": "Your rig, done four ways",
         # The second full FIFA set on the page, and distinct from the worked
         # example's: same four letters and labels (C4), the student's own
         # numbers, and the alert-on-ink badge rather than the accent-on-inset
         # one.
         "steps": [
             {"letter": "F", "label": "Formula",
              "line": "F × d(muscle) = W × d(load)",
              "note": "Nothing moves, so the two turning effects are equal."},
             {"letter": "I", "label": "Insert",
              "line": "F × {dM} m = {W} N × {dL} m",
              "note": "Weight is mass × 10, and both distances go into "
                      "metres."},
             {"letter": "F", "label": "Fine-tune",
              "line": "F × {dM} = {TE}, so F = {TE} ÷ {dM}",
              "note": "Right-hand side first, then rearrange so F is on its "
                      "own."},
             {"letter": "A", "label": "Answer",
              "line": "F = {F} N",
              "note": "That is {ratio} times the weight of the load, because "
                      "the load acts {ratio} times further from the joint."},
         ],
         # ⚖️ Quotes the student's own answer back beside the worked one, and
         # hands them to the meter on the rig. A comparison they make, never a
         # mark the page makes (R3 / MRB-196 R10).
         "close": {"template": "You wrote {answer} {unit}. The worked answer "
                               "is {F} N. Fit the force meter on the rig and "
                               "it reads the same.",
                   "blank": "—"}},

        # The QUANTITATIVE placement (C3): the law is stated once the student
        # has used it, so this box lands after the student's own calculation
        # rather than after the rig.
        {"type": "key-fact", "ref": "force-times-distance"},

        # ── #s-meters — the statutory measurement clause ────────────────────
        #
        # ⚖️ THIS BLOCK IS WHY THE LESSON IS BIOLOGY'S. `KS3.B.SKEL.02` asks
        # for "the measurement of force exerted by different muscles" in as
        # many words. Three groups, three readings each, a mean each — and
        # the closing band says why one pull would have told you nothing.
        {"type": "meter-compare", "id": "three-meters", "anchor": "s-meters",
         "eyebrow": "Measured, not guessed · three force meters",
         "heading": "Which muscle group pulls hardest?",
         "head_counter": {"off": "Not ranked yet", "on": "Ranked"},
         "demand": "classify",
         "prompt": "Three groups of muscles, each measured three times on a "
                   "force meter by the same person. Put them in order before "
                   "you look.",
         # One commitment, three options, and no per-option feedback: the
         # cards ARE the answer and they arrive whichever order was chosen.
         "options": [
             "Leg press, then hand grip, then biceps",
             "Biceps, then hand grip, then leg press",
             "Hand grip, then leg press, then biceps",
         ],
         # NOTES flag 16: plausible adult values, not measured ones. If Mide
         # wants real figures from a school dynamometer they become
         # `pending-data` and these three rows change; nothing else does.
         "rows": [
             {"name": "Hand grip",
              "readings": "312 N · 298 N · 305 N", "mean": "305 N"},
             {"name": "Biceps, pulling up",
              "readings": "196 N · 210 N · 203 N", "mean": "203 N"},
             {"name": "Leg press, both legs",
              "readings": "1450 N · 1390 N · 1425 N", "mean": "1422 N"},
         ],
         "mean_label": "mean of three",
         "close": "The bigger the muscle, the bigger the force — and the "
                  "three readings for each are never identical, so each one "
                  "is reported as a mean. A single pull tells you almost "
                  "nothing."},

        {"type": "misconception", "id": "think-commit-lever",
         "anchor": "s-think", "targets": "BODY-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "force-times-distance",
         "text": "A force turns a bone about a joint by force × distance from "
                 "the joint. Muscles attach close in, so they must pull many "
                 "times harder than the load they hold.",
         "placement": "top-level",
         # The unit-wide choice on all four B2 pages, and it differs from the
         # shipped `band` default (C3).
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The three instruments are authored inline in `core` and lifted here by
    # `ks3_data/b2/__init__.py::_normalise`, which also leaves the right shell
    # behind them — `practical` (ink-dark) for the rig, `check` (light) for
    # the other two, measured from Design's markup.
    "activities": [
        # MRB-204 part 3 — STAGED, one step at a time, on tap, one-way.
        # A worked example a student can read straight through is one they
        # watch happen to somebody else.
        {"id": "dumbbell-worked",
         "kind": "worked-example",
         "demand": "explain",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 2 kg dumbbell, 32 cm out. The biceps attaches at 4 cm.",
         "head_counter": {"format": "Step {n} of 4", "total": 4},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All four shown",
                     "done_note": "Now the same four steps on your own rig."},
         # `label` on each step takes Design's chipped treatment — a rounded
         # badge holding the bare letter, a mono label, a display line and a
         # note — rather than the shipped `letter · name` concatenation. Step
         # three is **Fine-tune**, which is what the second F stands for
         # (NOTES change-log item 1).
         "fifa": [
             {"letter": "F", "label": "Formula",
              "line": "F × d(muscle) = W × d(load)",
              "note": "Nothing is moving, so the turning effect of the muscle equals the turning effect of the load."},
             {"letter": "I", "label": "Insert",
              "line": "F × 0.04 m = 20 N × 0.32 m",
              "note": "The 2 kg dumbbell weighs 2 × 10 = 20 N. Both distances go into metres."},
             {"letter": "F", "label": "Fine-tune",
              "line": "F × 0.04 = 6.4, so F = 6.4 ÷ 0.04",
              "note": "Right-hand side first, then rearrange so F is on its own."},
             {"letter": "A", "label": "Answer",
              "line": "F = 160 N",
              "note": "Eight times the weight of the dumbbell — because 0.32 is eight times 0.04."},
         ]},

        # ── #s-think · commit, then two paragraphs (contract R1) ────────────
        # The quote itself comes from the register entry `BODY-11` names, so
        # the wrong idea lives in exactly one place.
        {"id": "think-commit-lever",
         "kind": "predict",
         "demand": "explain",
         "targets": "BODY-11",
         "prompt": "You have just calculated the opposite. Commit to what the "
                   "body is getting out of the deal before you read on.",
         "options": [
             "Nothing — it is simply a bad design",
             "Speed and distance: the hand moves much further and faster than "
             "the muscle shortens",
             "It saves energy",
             "It protects the joint from damage",
         ],
         "reveal": [
             "<strong>Speed and distance.</strong> The biceps shortens by "
             "about 4 cm and your hand travels about 32 cm — eight times as "
             "far, in the same time, so eight times as fast. A muscle can "
             "only shorten by a fraction of its own length and it cannot do "
             "it quickly. Attaching it close to the joint converts a small, "
             "slow, powerful pull into a long, fast movement.",
             "You pay for it in force, every single time. That is not a "
             "design fault; it is the price of a hand that can throw "
             "something. A body built the other way round would be immensely "
             "strong and would move like a crane.",
         ]},
    ],

    # ── the mastery ladder (C2) ─────────────────────────────────────────────
    # Four rungs, two page-marked and two self-marked, five criteria on each
    # self rung — the same instrument on all four B2 pages. Rung 1's title is
    # overridden because this lesson's first rung is a calculation; rungs 2, 3
    # and 4 take the engine's Design-worded defaults unchanged.
    "ladder": {
        "recall": {
            "title": "Calculate",
            "q": "A load of 30 N is held 30 cm from the elbow. The muscle "
                 "attaches 5 cm from the elbow. What force must the muscle "
                 "pull with?",
            "options": [
                "180 N",
                "30 N",
                "6 N",
                "900 N",
            ],
            "answer": 0,
            "feedback": {
                1: "That would only be true if both distances were the same. "
                   "The load acts six times further out than the muscle.",
                2: "That is 30 ÷ 5. Dividing the force by a distance does not "
                   "give a force.",
                3: "That is 30 × 30 — the turning effect of the load in N cm, "
                   "not the muscle force. It still has to be divided by the "
                   "muscle distance.",
            }},
        "apply": {
            "q": "Why does the biceps have to pull so much harder than the "
                 "weight it is holding?",
            "options": [
                "It attaches very close to the joint, so it has a much "
                "smaller distance to work with",
                "Muscles are inefficient and waste most of their force",
                "Because the forearm itself is heavy",
                "Because muscles can only pull and never push",
            ],
            "answer": 0,
            "feedback": {
                1: "Nothing is being wasted. Every newton is doing exactly "
                   "what the arithmetic says it must.",
                # NOTES flag 4: the forearm's own weight is ignored throughout,
                # and this is the one place the page says so out loud.
                2: "The forearm does add to it, but even a weightless forearm "
                   "would need the same eight-times pull.",
                3: "True, and it is why there are two of them — but it is not "
                   "what makes this one big number big.",
            }},
        "explain": {
            "q": "The arrangement in your arm costs a lot of force. Explain "
                 "what the body gets in return, using the two distances.",
            "field_label": "Your explanation",
            "placeholder": "The muscle shortens by only…",
            "success": [
                "Says the muscle attaches close to the joint and the hand is "
                "much further out.",
                "Says a small shortening of the muscle moves the hand a much "
                "larger distance.",
                "Says the hand therefore moves faster than the muscle "
                "shortens.",
                "Says the price is force: the muscle must pull many times "
                "harder than the load.",
                "Gives a pair of numbers from the rig or the worked example "
                "to back it up.",
            ]},
        "produce": {
            "q": "Someone carries a 5 kg bag. Held against the chest, its "
                 "weight acts about 10 cm from the shoulder joint; held out "
                 "at arm’s length, about 60 cm. Explain, with a calculation, "
                 "why the second one is so much harder — and say what that "
                 "means for how you should lift a box.",
            "field_label": "Your answer",
            "placeholder": "The bag weighs…",
            "success": [
                "Gives the weight of the bag as 50 N.",
                "Works out both turning effects: 50 × 0.1 = 5 N m, and "
                "50 × 0.6 = 30 N m.",
                "Says the far one is six times the turning effect of the near "
                "one.",
                "Says the muscle force needed goes up in the same proportion, "
                "because the muscle distance has not changed.",
                "Draws the practical conclusion: keep the load close to the "
                "joint, or close to the body, when lifting.",
            ]},
    },

    "key_note": "Turning effect = force × distance from the joint. When "
                "nothing is moving, the two turning effects are equal, so a "
                "muscle attached 4 cm from the elbow must pull eight times "
                "harder than a load held 32 cm out. Force is bought with "
                "distance, and speed is bought with force.",

    # ── going further ───────────────────────────────────────────────────────
    # MRB-225: the elite-sprinter finding is evidence about the world and
    # belongs here, not in the body, and nothing in the lesson is retracted by
    # it — the Achilles is the same trade tuned differently, not an exception
    # to the rule the lesson just taught.
    "stretch": [
        {"type": "explainer", "id": "achilles",
         "text": "Your Achilles tendon is the exception that proves the rule. "
                 "It attaches behind the ankle joint, well back from it, "
                 "which is a long way as body attachments go — and that is "
                 "exactly why you can push off the ground hard enough to run "
                 "and jump. Elite sprinters tend to have a slightly shorter "
                 "heel bone than average, giving the tendon a <em>smaller</em> "
                 "distance to work with, and a bigger force is needed for "
                 "every stride. What they get in return is speed: a small "
                 "shortening of the calf muscle throws the foot down faster. "
                 "The trade is the same one your elbow makes, tuned "
                 "differently."},
    ],

    "support": [],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Stuck on which distance goes where?",
              "cta": "Ask about this lesson",
              "anchor": "s-build"},

    # ⊕ CORRECTION 2 of 2 (Mide's ruling, 16 Aug). Design's line reads
    # "Moments, levers and gears, and the mechanics of the musculoskeletal
    # system." — the GCSE topic's own name, and the second occurrence of the
    # word the ruling bars from this unit. The science is unchanged: at GCSE
    # this becomes the turning effect of a force, under the name it is
    # assessed by, which P4 introduces first.
    "ks4_becomes": "The turning effect of a force, levers and gears, and the "
                   "mechanics of the musculoskeletal system.",

    # ⚠️ NOT `safety_note`. Design's line at the bottom edge of the page is
    # the g-convention, and shipping it through `safety_note` would print it
    # under a class named `ks3-safety` — a convention is not a hazard. Payload
    # map §4.6 note 8; the slot is in `lesson-page.deltas.md`.
    "convention_note": "Weight in newtons is taken as mass in kilograms × "
                       "10 N/kg throughout.",

    "ws": ["measurement", "analysis-and-evaluation"],

    "review_state": "draft",
}
