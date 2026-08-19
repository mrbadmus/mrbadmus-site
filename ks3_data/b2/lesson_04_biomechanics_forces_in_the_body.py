"""B2 L4 — Biomechanics: forces in the body (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b2/b2-04-biomechanics-forces-in-the-body.dc.html` (1,028 lines),
read in full. Every student-facing string below is lifted from it character for
character unless a `⊕ CORRECTION` says otherwise and says why.

── Owned by BIOLOGY, and that is the statutory register's ruling ─────────

The 2014 KS3 programme of study names biomechanics inside the biology section,
under the skeletal and muscular systems, *"including the measurement of force
exerted by different muscles"*. `ks3_data/structure.py` declares this slot as
B2's fourth lesson with family `QUANTITATIVE`; `covers` takes `KS3.B.SKEL.02`,
the one statement left in the unit once B2's other three lessons have taken
SKEL.01a, SKEL.01b and SKEL.03.

The clause that statement makes load-bearing is the **measurement** one, and
it is `#s-meters`: three muscle groups, three readings each, a mean for each.
That block is why this is a biology lesson rather than a physics lesson
wearing an arm.

── The word `moment` does not appear on a student page but once ──────────

Ruled for this build. The relationship is taught as **turning effect = force ×
distance from the joint**; the vocabulary is P4's, where it is assessed. The
one permitted occurrence is the endmatter's forward reference — *"At GCSE this
becomes: Moments, levers and gears…"* — which is Design's line, is correct,
and stays exactly as drawn.

Design's hook prompt breaks the rule once, in the everyday sense of the word
("at that moment"), and that is corrected below. A student who meets the word
here and again in P4 as a quantity has been handed a collision for nothing.

⚠️ **One occurrence is still unreachable from this file** — the middle
endmatter card. See the `references` key: `lesson_page` prints the TARGET
lesson's own title, which is "Moments: the turning effect". `label` is
authored here to override it and `lesson_page` does not read it yet. One line
fixes it and the line is in the report.

── b2-04 stands alone. Zero assumed prior teaching of forces ─────────────

A school may run P4 in Year 8 and B2 in Year 9, so a sentence like "as you saw
in physics" would break silently on half the schools using this. The P4
relationship is therefore a `references` EDGE — data the graph carries — and
never prose. Nothing in the body of this lesson assumes a force lesson has
happened.

── MRB-204, in Design's own order, with none of the five collapsed ───────

    the formula alone  →  the triangle  →  the staged worked example  →  the
    student's own four steps, on the student's own rig  →  the ladder

`T = F × d` is a PRODUCT, so it takes the TRIANGLE. A balance beam is the sum's
figure (c2-06's, for conservation of mass) and drawing a product as a beam — or
a sum as a triangle — teaches a false relationship to make a rule fit.

── Three instruments, and one that widens ───────────────────────────────

`arm-lever` (#s-bench), `lever-steps` (#s-build) and `meter-compare`
(#s-meters) are new kinds; their renderer, CSS, wiring and parity rows ship as
fragments in `docs/ks3/b2-inventory/instrument-fragments/`. `cover-triangle`
already exists — c2-06 ships its BAR variant and b1-02 ships the narrow
triangle — and its TRIANGLE variant widens by four opt-in keys. See
`cover-triangle.renderer.py`; nothing is forked and neither shipped page moves.

Everything else is reuse. `_head_counter`, `r_bench_gate`, `r_fifa`'s staged
chipped steps, the two-paragraph `reveal`, `r_confrontation`, `r_key_fact` and
`r_ladder` are all called rather than re-implemented.
"""

# ── the rig's defaults, in one place ────────────────────────────────────
#
# `lever-steps` reads the rig it names (`rig: "forearm-rig"`) and computes its
# RESTING render from that instrument's own control defaults at build time, and
# every state after it from the live DOM. The numbers are written once, here,
# because two copies of "4 cm" is two places for the arithmetic to stop
# agreeing with the drawing.
#
# `_G` is the KS3 convention: weight in newtons is mass in kilograms × 10 N/kg.
# Design states it in a line at the bottom edge of the page; see the report —
# `lesson_page` has no slot for it and it survives here only inside the two
# `Insert` notes, which is where a student actually meets it.
_LOAD_KG, _INS_CM, _HAND_CM, _G = 2.0, 4.0, 32, 10

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py character for character.
    "slug":        "biomechanics-forces-in-the-body",
    "title":       "Biomechanics: forces in the body",
    "discipline":  "biology",
    "unit":        "movement-skeleton-and-muscles",
    "family":      "QUANTITATIVE",

    # `KS3.B.SKEL.02` — "biomechanics – the interaction between skeleton and
    # muscles, including the measurement of force exerted by different
    # muscles". B2's other three lessons take SKEL.01a, SKEL.01b and SKEL.03,
    # so the unit keeps exactly-once coverage and nothing else in KS3 claims
    # this statement.
    "covers":      ["KS3.B.SKEL.02"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    "requires":    ["antagonistic-muscle-pairs"],
    "assumes":     [],

    # ⚖️ THE P4 RELATIONSHIP IS AN EDGE, NEVER PROSE.
    #
    # Design drew endmatter card 2 as prose — *"Physics: Forces — where the
    # turning effect of a force is developed on its own, away from the body."*
    # Prose asserts a teaching sequence, and the sequence is not ours to
    # assert. As data the graph carries the relationship, and the card renders
    # the honest coming-soon treatment `lesson_page` already has for a unit
    # that is not authored yet.
    #
    # ⚠️ BLOCKED, AND IT PRINTS THE ONE BARRED WORD. `lesson_page` composes the
    # card's label as `tgt["title"] if tgt else r["lesson"]`, and P4's slot is
    # titled "Moments: the turning effect". So this card currently renders
    # BOTH the wrong label (Design wrote "Physics: Forces") and the word this
    # unit may not contain. `label` below is the override and nothing reads it.
    # The fix is one line, in `lesson_page`, beside the existing composition:
    #
    #     label = r.get("label") or (tgt["title"] if tgt else r["lesson"])
    #
    # It is in the report as a required same-pass splice.
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
    # SIX stops, not the five b2-01/02/03 carry — the extra one is the
    # force-meter comparison the statutory statement asks for. Page lines
    # 517–524 for the anchors, shorts and labels; 794–802 for Design's own
    # tick conditions, one of which is corrected below.
    #
    # The triangle block and the worked example are deliberately NOT stops.
    # Both are read rather than done, and MRB-208 has the rail carrying only
    # sections that require the student to do something.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Eight times harder", "done_when": "committed"},
        # ⚠️ A SET, never a press count: two DIFFERENT controls moved, and the
        # meter fitted. Design's own predicate is already a set
        # (`Object.keys(touched).length >= 2 && meterShown`) and it is
        # reproduced as one — `wireArmLever` counts distinct control keys.
        {"anchor": "s-bench",  "short": "RIG",
         "label": "The forearm rig", "done_when": "rig_measured"},
        # ⊕ CORRECTION 2 of 3 — see the header of `lever-steps` below.
        # Design ticks this stop on `buildOpen`, i.e. on the student pressing
        # "Show the four steps". Opening an answer is not a demand. The stop
        # now requires the three commitments the block asks for.
        {"anchor": "s-build",  "short": "STEPS",
         "label": "Your own four steps",
         "done_when": "three_lines_committed"},
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
        # ⊕ CORRECTION 1 of 3. Design's line reads "Your biceps, at that
        # moment, is pulling with about 80 N". That is the everyday word for an
        # instant rather than the physical quantity — but the ruling is that
        # the word does not appear in this unit's teaching, and "at that
        # instant" says the same thing at the same length.
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
    # Continues the BODY family b2-01/02/03 write (BODY-01…BODY-09).
    #
    # ⚠️ `statement` IS the quoted line at the top of `#s-think`.
    # `r_confrontation` renders the register entry rather than a second copy,
    # so a statement that drifted from Design's quote would silently replace
    # it. BODY-11 below is page line 377, character for character.
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
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every force acting on a bone is trying to turn it about a "
                 "joint. How much turning it does depends on two things: how "
                 "big the force is, and how far from the joint it acts."},

        # ── #s-bench — ink-dark `practical` shell (page lines 113–195) ──────
        #
        # ⚖️ THE MUSCLE-FORCE TILE IS THE GATE, AND IT IS THE LESSON. The rig
        # hands over the load and both distances and refuses the fourth
        # number: the tile reads `not measured — you work it out` until the
        # meter is fitted, and the muscle arrow on the canvas carries the word
        # `muscle` and deliberately no magnitude. The same gate, reached by
        # both routes a student has.
        {"type": "arm-lever", "id": "forearm-rig", "anchor": "s-bench",
         "eyebrow": "At the bench · the forearm rig",
         "heading": "Three measurements. The fourth number is yours.",
         # The two-state variant of the block-head readout, not a count: this
         # block has one thing to report and it is a boolean.
         "head_counter": {"off": "Meter not fitted yet", "on": "Meter fitted"},
         "demand": "investigate",
         "targets": "BODY-10",
         "prompt": "",
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
         # Three controls; TWO of them moved, plus the meter, is the rail stop.
         # Authored so the predicate is data rather than a number buried in a
         # wire function.
         "done_at": 2,
         # The KS3 convention, in the one place the arithmetic uses it.
         "g": _G,
         # ⚠️ Decimals are DERIVED from each control's `step` — a step of 0.5
         # needs one decimal place, an integer set needs none — so there is no
         # `decimals` key. A second statement of the same fact is a second
         # place for it to go wrong.
         "controls": [
             {"key": "load", "label": "Mass in the hand", "format": "{n} kg",
              "min": 0.5, "max": 5, "step": 0.5, "start": _LOAD_KG},
             {"key": "ins", "label": "Muscle attached at", "format": "{n} cm",
              "min": 3, "max": 6, "step": 0.5, "start": _INS_CM},
             # A two-tab set rather than a slider, because Design draws the
             # halving as a comparison a student makes on purpose and not as
             # a value they slide past.
             {"key": "hand", "label": "Hand distance", "format": "{n} cm",
              "options": [32, 16], "start": _HAND_CM},
         ],
         # `mono` is Design's own split: the three measured tiles are mono
         # 25px, and the fourth is 19px/700 because until the meter is fitted
         # it holds a sentence rather than a number.
         "tiles": [
             {"key": "weight", "label": "Weight of the load",
              "format": "{n} N", "mono": True},
             {"key": "hand", "label": "Load, from the elbow",
              "format": "{n} cm", "mono": True},
             {"key": "ins", "label": "Muscle, from the elbow",
              "format": "{n} cm", "mono": True},
             {"key": "force", "label": "Force in the muscle",
              "format": "{n} N"},
         ],
         "unmeasured": "not measured — you work it out",
         "meter": {
             "label": "Fit a force meter to the tendon",
             "label_done": "Meter reading shown",
             "note": "Work it out first. Then fit the meter and see whether "
                     "the rig agrees with you.",
             "note_done": "The meter agrees with the arithmetic, because the "
                          "arithmetic is what the tendon is obeying."},
         # Drawn on the canvas. The load arrow takes the computed weight; the
         # muscle arrow takes a bare word and deliberately no number.
         "canvas": {"title": "THE FOREARM RIG · SIDE VIEW",
                    "joint": "ELBOW",
                    "muscle": "muscle",
                    "load": "{n} N"},
         # ⚠️ COMPOSED, never authored per state: it quotes three live values,
         # so a fixed string would be a fourth copy of the state and would go
         # stale on the first drag. Python renders the resting label at build
         # time, JS renders every state after it, and both use the same
         # composition.
         #
         # ⊕ ADDITION: `measured` is appended once the meter is fitted, so the
         # muscle force is IN the label — but only once it is on screen. The
         # canvas is the whole drawing for a screen reader and must carry
         # every number a sighted student can see; it must not carry the one
         # the block exists to withhold.
         "alt": {
             "template": "A side view of a forearm held level. A load of "
                         "{load} kilograms hangs from the hand {hand} "
                         "centimetres from the elbow, and the muscle pulls "
                         "upwards {ins} centimetres from the elbow on the "
                         "other side of the joint.",
             "measured": " The force meter fitted to the tendon reads {force} "
                         "newtons."}},

        # ── the formula, alone in its own block, then the triangle ──────────
        # MRB-204 steps 1 and 2. `r_formula` puts the statement panel and the
        # figure in ONE block on purpose: both are the formula, and a student
        # flicking back through the lesson wants them together.
        #
        # ⊕ ADDITION inside a drawn component. Design's section carries the
        # triangle, the three prose lines and NO statement line — the
        # relationship is written out only in the key fact and the key note,
        # both of which come later. MRB-204 step 1 is a ruling ("a student
        # flicking back through the lesson to find the formula must be able to
        # see it from the scroll position"), this is the block that ruling
        # names, and `r_formula` renders an empty statement panel without one.
        # The sentence is Design's own — it is the first clause of the key
        # note, line 471 — relocated, not written.
        #
        # No `eyebrow` on the block: Design draws exactly one, "The triangle",
        # and it belongs to the figure. Two would be two.
        {"type": "formula", "id": "turning-effect",
         "statement": "Turning effect = force × distance from the joint",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle: turning effect on top, force "
                           "and distance from the joint underneath, "
                           "multiplied together.",
             # ⊕ WIDENED: each cell gains a `result` — the arrangement, in
             # display type — beside the sentence that says why. Folding the
             # two into one note loses the line a student actually reads off
             # the page.
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
             # ⊕ WIDENED: Design's own button order and default — F, T, d,
             # with F already covered on load. That is the arrangement this
             # lesson needs, because every question on the page solves for the
             # muscle force. Declaring `covered` also makes the control a
             # RADIO rather than b1-02's toggle: there is no uncovered state
             # here, so the triangle is only ever taught covered.
             "order": ["left", "top", "right"],
             "covered": "left",
             # ⊕ WIDENED: three trailing blocks rather than b1-02's one
             # paragraph — a prose rule, a mono unit legend, and the balanced
             # condition in display type. The condition is not a fourth
             # arrangement of T, F and d; it is the statement that makes the
             # rest of the lesson solvable, and it is why it is set apart.
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["T — turning effect, in N m",
                           "F — force, in N",
                           "d — distance from the joint, in m"],
                 "condition": "Nothing moving: F₁ × d₁ = F₂ × d₂"}}},

        # ── the worked example (MRB-204 step 3) — read, not done ────────────
        {"type": "worked-example", "id": "dumbbell-worked"},

        # ── #s-build (MRB-204 step 4) — the same four steps, on the student's
        # own rig. A light `check` block on the inset ground.
        {"type": "lever-steps", "id": "your-four-steps", "anchor": "s-build",
         "ground": "inset",
         "eyebrow": "Your turn · the same four steps",
         # ⚠️ LIVE. The heading quotes the rig the student left set, so the two
         # blocks are visibly the same problem. Filled at build time from the
         # rig's own defaults and repainted whenever a control moves.
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
             # ⚖️ These three are GENERATED from the student's own rig, not
             # authored. Authoring them would fix the rig at 2 kg and make
             # every other setting of the sliders unanswerable.
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
                   # ⚠️ The placeholder option carries an EMPTY value, or the
                   # open button unlocks for a student who never chose a unit.
                   "unit_placeholder": "choose a unit",
                   "units": ["N", "kg", "m", "N m"]},
         "button": "Show the four steps",
         "progress": {"format": "{n} of 3 lines committed", "done": "Opened"},
         "reveal_head": "Your rig, done four ways",
         # The second full FIFA set on the page and distinct from the worked
         # example's: the same four letters and labels, the student's own
         # numbers, and the alert-on-ink badge rather than the accent-on-inset
         # one. Step three is **Fine-tune**, which is what the second F stands
         # for in Design's own wording.
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
         # ⚖️ Quotes the student's own answer back beside the worked one and
         # hands them to the meter on the rig. A comparison the student makes,
         # never a mark the page makes (R3).
         "close": {"template": "You wrote {answer} {unit}. The worked answer "
                               "is {F} N. Fit the force meter on the rig and "
                               "it reads the same.",
                   "blank": "—"}},

        # The QUANTITATIVE placement: the law is stated once the student has
        # used it, so this box lands after their own calculation rather than
        # after the rig.
        {"type": "key-fact", "ref": "force-times-distance"},

        # ── #s-meters — the statutory measurement clause ────────────────────
        #
        # ⚖️ THIS BLOCK IS WHY THE LESSON IS BIOLOGY'S. `KS3.B.SKEL.02` asks
        # for "the measurement of force exerted by different muscles" in as
        # many words. Three groups, three readings each, a mean each — and the
        # closing band says why one pull would have told you nothing.
        #
        # ⚠️ NO `ground`. Design paints this on the DEFAULT card ground while
        # `#s-build` above it takes the inset one. Two light blocks, two
        # different grounds, measured off the markup rather than assumed.
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
         # ⚠️ R3 — read at BUILD TIME ONLY, exactly as `keyed-commit` reads
         # its own. It names, for the examiner, the order the data supports
         # (1422 > 305 > 203) and it reaches no attribute, no class and no
         # student. If a `rows` edit ever reordered the means, the build says
         # so instead of the page quietly arguing for the wrong option.
         "answer_index": 0,
         # Plausible adult values, not measured ones. If real figures from a
         # school dynamometer arrive, these three rows change and nothing else
         # does.
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
         # The unit-wide choice on all four B2 pages; it differs from the
         # engine's shipped `band` default.
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The three instruments are authored inline in `core` and lifted here by
    # `ks3_data/b2/__init__.py::_normalise`, which also leaves the right shell
    # behind them — `practical` (ink-dark) for the rig, `check` (light) for the
    # other two, measured from Design's own markup.
    "activities": [
        # MRB-204 step 3 — STAGED, one step at a time, on tap, one-way. A
        # worked example a student can read straight through is one they watch
        # happen to somebody else.
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
         # note — rather than the shipped `letter · name` concatenation.
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

        # ── #s-think · commit, then two paragraphs ──────────────────────────
        # The quoted wrong idea comes from the register entry `BODY-11`, so it
        # lives in exactly one place.
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

    # ── the mastery ladder ──────────────────────────────────────────────────
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
            # ⚠️ ALL FOUR ARE TWO WORDS, AND THAT IS CORRECT — leave it alone.
            # MRB-177's length-parity gate flags a correct option that is
            # STRICTLY the longest; four equal-length options cannot be a
            # length tell, and shortening or padding a numeric answer to make
            # a set "look" balanced would be tampering with a calculation.
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
            # ⚖️ **CORRECTED FROM DESIGN — the distractors were too short
            # (MRB-177 length parity, ⊕ CORRECTION 3 of 3).**
            #
            # Design's set ran 17 / 9 / 6 / 8 words. The correct answer beat
            # the longest distractor by eight words and by 1.9×, which fails
            # the gate on both thresholds — and a student who has worked out
            # that the long one is usually right, which a class works out
            # early, could take this rung without reading it. A question you
            # can score without knowing the science measures nothing.
            #
            # Each distractor keeps its misconception EXACTLY: waste,
            # forearm weight, pull-not-push. Only the sentence is completed,
            # so all four now read as full claims at 15–17 words. The correct
            # option is unchanged, because it is the science.
            "options": [
                "It attaches very close to the joint, so it has a much "
                "smaller distance to work with",
                "Muscles are inefficient and waste most of their force, so a "
                "lot of the pull is lost",
                "Because the forearm itself is heavy, and the muscle has to "
                "lift the arm as well",
                "Because muscles can only pull and never push, so pulling is "
                "the only option left",
            ],
            "answer": 0,
            "feedback": {
                1: "Nothing is being wasted. Every newton is doing exactly "
                   "what the arithmetic says it must.",
                # The forearm's own weight is ignored throughout this lesson,
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
    # The elite-sprinter finding is evidence about the world and belongs in
    # the chosen layer, not the body. Nothing in the lesson is retracted by
    # it: the Achilles is the same trade tuned differently, not an exception
    # to the rule the lesson has just taught.
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

    # ⚠️ THE ONE PERMITTED OCCURRENCE, and it is Design's line unchanged. The
    # endmatter's forward reference names the GCSE topic by the name it is
    # assessed under; renaming it here would leave a student unable to find
    # the thing they were told they were heading towards.
    "ks4_becomes": "Moments, levers and gears, and the mechanics of the "
                   "musculoskeletal system.",

    "ws": ["measurement", "analysis-and-evaluation"],

    # ⊕ Design's foot line, lifted byte-identical from the approved page
    # (line 506). It had nowhere to go until `convention_note` landed in
    # `lesson_page` (MRB-228): the only lesson-level foot slot was
    # `safety_note`, and a units convention is not a hazard — shipping it under
    # `class="ks3-safety"` would spend the safety treatment on a sentence about
    # arithmetic.
    #
    # It is load-bearing rather than decorative. g = 10 N/kg is stated inside
    # two worked steps, and "throughout" is the word that tells a student the
    # same assumption still holds in the rung they are about to attempt.
    "convention_note": "Weight in newtons is taken as mass in kilograms × "
                       "10 N/kg throughout.",

    "review_state": "draft",
}
