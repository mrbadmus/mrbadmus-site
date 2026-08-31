"""P5 L4 — Atmospheric pressure (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p5/p5-04-atmospheric-pressure.dc.html`.

Her page wins outright. The crushed can, the mountain bench, the stack of
bands, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A STACK, THE SAME SHAPE AS `p5-02`, WITH ONE CHANGE ──

`air pressure = weight of the air above ÷ the area it presses on` is the
same relationship and the same figure as pressure in a liquid. The one
difference is that **the bands are unequal**, because air is squashable
and most of its mass is packed into the lowest few kilometres. `p5-02`'s
rule line carries a proportionality clause — twice the depth, twice the
pressure — and this one drops it, because air is not linear with height.
`_stack` refuses equal bands here for exactly that reason.

⚖️ **NO COVER BUTTONS**, for the same reason as `p5-02`: covering a band
of atmosphere means nothing.

── ⚖️ RULED · "NOTHING SUCKS: AIR PUSHES" IS THE WHOLE LESSON ────────

`PRESS-13` is *a vacuum sucks things in*, and it is the belief the hook,
the key fact, both misconception quotes and rung 4 are all built around.
Every case that looks like sucking is rewritten as *what is pushing, and
from where?* — the straw, the plunger, the can. A vacuum is nothing, and
nothing cannot pull.

── ⚖️ RULED · THE PRESSURES ARE STANDARD-ATMOSPHERE VALUES ───────────

101, 90, 75, 50, 31 and 23 kPa at 0, 1000, 2500, 5500, 8850 and 11 000 m
— each within a kilopascal of the international standard atmosphere. The
boiling points (100, 97, 92, 82, 71, 65 °C) follow from them. Real
pressure moves several kilopascals with the weather, which is what makes
a barometer useful at all, and the foot line says so. `r_altitude_column`
asserts that the pressure FALLS at every step, because that is the
statement this lesson owns.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    PRESS-13  a vacuum sucks things in
    PRESS-14  if air pressed that hard we would feel it
    PRESS-15  a sealed bag swells at altitude because gravity is weaker
    PRESS-16  the air runs out at a definite height, and above it there is
              none at all

`PRESS-14` has no `elicited_by`: nothing asks the student to commit to
it, and it is confronted by the second quote. `PRESS-16` is not in
Design's table — it arrived with her own six-band stack, which thins
upwards without ever reaching zero, and with the bench's `share` readout
that never gets to 0 per cent. It is a genuinely separate belief from
`PRESS-15`: a student can have accepted that gravity is unchanged and
still think there is a ceiling.
"""

LESSON = {
    "slug":  "atmospheric-pressure",
    "title": "Atmospheric pressure",
    "discipline": "physics",
    "unit": "Pressure",
    "family": "SYSTEM",

    "covers": ["KS3.P.PRES.01"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["upthrust-floating-and-sinking"],
    "assumes": [],
    "references": ["pressure-in-liquids", "pressure-force-over-area"],
    "ks4_links": [],

    # ── ⚠️ NO `safety_note` ON THIS LESSON, AND THE ABSENCE IS DELIBERATE ──
    #
    # ⊕ MRB-297, 31 Aug 2026. Mide approved twelve safety notes on 30 Aug and
    # eleven were placed. The twelfth was for THIS lesson and reads
    # "Teacher demonstration only — never try this one yourself. …". It is
    # NOT here, and it is not to be added without his say-so.
    #
    # Why: the note assumes the crushed can is a teacher demonstration, and
    # this lesson's own `meta_description` and `big_question` were written as
    # an INSTRUCTION TO THE STUDENT — "Boil a splash of water in an empty
    # can, seal it, and cool it." A note saying "never try this one
    # yourself" under a page that tells a child to do it would make the page
    # contradict itself on a safety point, so the run's rule applied: where a
    # note's assumption is contradicted by the lesson, the note is not placed
    # and NOT ADAPTED — it goes back to Mide.
    #
    # ⊕ AMENDED 1 Sep 2026, by the cold double-check, which was right that
    # withholding the note ALONE left the worst of the three states: a do-it
    # instruction on a hazard, with nothing beside it. Audit M1's option (c)
    # pairs the two, so the two leading fields are now in the SAME PASSIVE
    # VOICE the lesson's own hook already uses nineteen lines below ("A
    # little water is boiled … The can is sealed and stood in cold water").
    # No new safety wording was written and no claim about who does it was
    # added; an instruction was turned back into a description, in the
    # lesson's own words. **The note itself is still Mide's to rule on.**
    "meta_description": "A little water is boiled in a can, the can is "
                        "sealed and cooled, and it crushes itself flat with "
                        "nothing near it. Take three things up a mountain "
                        "and find out what was pressing all along.",

    "big_question": "A little water is boiled in an empty can, which is then "
                    "sealed and cooled. The can crushes itself flat, and "
                    "nothing goes anywhere near it.",

    "rail": [
        {"anchor": "s-hook",    "short": "CAN",
         "label": "The crushed can", "done_when": "committed"},
        {"anchor": "s-bench",   "short": "CLIMB",
         "label": "Up the mountain", "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "The stack and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",  "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Nothing touched the can.",
        "prompt": "A little water is boiled in a thin metal can until steam "
                  "has driven the air out. The can is sealed and stood in "
                  "cold water. It folds in on itself with a bang, in about a "
                  "second.",
        "commit": "What crushed it?",
        "options": [
            # ⊕ PHASE 3, 25 Aug 2026 — HER four options. These had
            # been invented: her prompt was ported and her answers were
            # not, which the HTML comparison could not see because a
            # `.dc.html` renders them from `{{ opt.text }}`.
            # ⊕ AMENDED MRB-297, 31 Aug 2026 — no longer true of all four,
            # and kept rather than deleted so the provenance is not silently
            # overstated. HER CORRECT OPTION IS UNCHANGED, byte for byte.
            # The distractors were re-authored to the same length and shape:
            # as delivered they were terse beside a reasoned correct answer,
            # so the right one was the visibly longest and the hook could be
            # answered without reading it.
            "The vacuum inside sucked the sides in, because empty space pulls "
            "on what surrounds it",
            "The air outside was always pressing that hard, and the steam "
            "inside had been pushing back",
            "The metal shrank as it cooled, and pulled its own walls inwards "
            "with it",
            "The steam pulled the sides in as it cooled, because a gas "
            "turning to liquid drags things in",
        ],
        "answer": 1,
        "reveal": "The air outside. It was pressing that hard the whole time "
                  "— about 100 000 N on every square metre of that can, "
                  "from every side. Nothing changed outside; what changed "
                  "was inside. Steam filled the can and pushed back just as "
                  "hard, and when the steam cooled it turned back into a few "
                  "drops of water and stopped pushing. With the push from "
                  "inside gone, the outside push had nothing to work "
                  "against. <strong>Nothing sucked the can in.</strong>",
    },

    "misconceptions": [
        {"id": "PRESS-13",
         "statement": "A vacuum sucks things in.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "PRESS-14",
         "statement": "If air really pressed that hard, we would feel it.",
         "confronted_by": "s-think"},
        {"id": "PRESS-15",
         "statement": "A sealed bag swells at altitude because gravity is "
                      "weaker up there.",
         "elicited_by": "climb",
         "confronted_by": "s-ladder"},
        {"id": "PRESS-16",
         "statement": "The air runs out at a definite height, and above it "
                      "there is none at all.",
         "elicited_by": "s-ladder",
         "confronted_by": "climb"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "You are at the bottom of an ocean of air about a hundred "
                 "kilometres deep, and it has weight. All of it presses down "
                 "on you, and — as with any fluid — it presses in every "
                 "direction at once, roughly <strong>100 000 Pa</strong> at "
                 "sea level. Climb, and some of that air is now below you "
                 "instead of above you, so there is less weight pressing and "
                 "the pressure falls. Air is squashable, unlike water, so "
                 "most of its mass is packed into the lowest few kilometres, "
                 "which is why the pressure drops fastest near the ground."},

        # ── #s-bench · take three things up a mountain ─────────────────
        {"type": "altitude-column",
         "id": "climb",
         "anchor": "s-bench",
         "eyebrow": "At the bench · take three things up a mountain",
         "heading": "Same objects. Less air above them.",
         "progress": "Change a control to begin",
         "lead": "A foil bag sealed at sea level, a pan of water on a stove, "
                 "and a barometer. Choose a height, and choose which one to "
                 "watch.",
         "sea_kpa": 101,
         "palm": 0.01,
         "base_y": 560,
         "top": 40,
         "span_m": 12000,
         "start_height": 0,
         "start_case": 0,
         "height_label": "Height above sea level",
         "case_label": "What to watch",
         "gate": {
             "prompt": "Commit first. A foil bag of crisps is sealed at sea "
                       "level and carried up to 5500 m. What happens to it?",
             "options": [
                 "It puffs up tight — the air sealed inside is still at "
                 "sea-level pressure",
                 "It stays exactly as it was — it is sealed, so nothing can "
                 "change",
                 "It is crushed inwards by the thinner air",
                 "It puffs up because there is less gravity up there",
             ],
             "answer": 0,
         },
         # ⚖️ STANDARD-ATMOSPHERE VALUES. The renderer asserts that the
         # pressure falls at every step, because that IS `PRES.01`.
         "heights": [
             {"id": "sea", "label": "Sea level", "name": "a beach",
              "m": 0, "kpa": 101, "boil": 100},
             {"id": "h1000", "label": "1000 m",
              "name": "a Lake District summit", "m": 1000, "kpa": 90,
              "boil": 97},
             {"id": "h2500", "label": "2500 m",
              "name": "an Alpine ski village", "m": 2500, "kpa": 75,
              "boil": 92},
             {"id": "h5500", "label": "5500 m",
              "name": "Everest base camp and a bit higher", "m": 5500,
              "kpa": 50, "boil": 82},
             {"id": "h8850", "label": "8850 m",
              "name": "the summit of Everest", "m": 8850, "kpa": 31,
              "boil": 71},
             {"id": "h11000", "label": "11 000 m",
              "name": "cruising height for an airliner", "m": 11000,
              "kpa": 23, "boil": 65},
         ],
         "cases": [
             {"id": "bag", "label": "Sealed bag", "tile": "The bag",
              "clause_sea": "The bag looks exactly as it did when it was "
                            "sealed, because the air inside and the air "
                            "outside are pressing equally.",
              "clause_above": "The bag is tight, holding about {swell} times "
                              "the volume it had at sea level: the air "
                              "sealed inside is still at {sea} kPa while the "
                              "air outside is down to {kpa} kPa, so the "
                              "inside push wins."},
             {"id": "pan", "label": "Pan of water", "tile": "Water boils at",
              "clause_sea": "The pan boils at 100 °C, which is the number "
                            "everyone learns — and it is a fact about sea "
                            "level, not about water.",
              "clause_above": "The pan boils at {boil} °C. It is not cooler "
                              "because the stove is weaker; water boils when "
                              "its vapour can push the air out of the way, "
                              "and there is less air to push."},
             {"id": "baro", "label": "Barometer", "tile": "The barometer",
              "clause_sea": "The barometer reads {kpa} kPa, which is its "
                            "sea-level reading and the one every other "
                            "height is compared with.",
              "clause_above": "The barometer reads {kpa} kPa, which is "
                              "{share} of its sea-level reading."},
         ],
         "branches": {
             "sea": "At sea level the whole atmosphere is above you and it "
                    "presses with {kpa} kPa, or {pa} — about {palmforce} on "
                    "each palm, which you never notice because it pushes "
                    "from every side at once. ",
             "above": "At {label} — {name} — {share} of the atmosphere is "
                      "still above you, so the pressure is {kpa} kPa instead "
                      "of {sea}. Nothing about the air has changed: you have "
                      "simply climbed above some of it, and what is above "
                      "you is what presses. ",
         },
         "readouts": [
             {"id": "height", "label": "Height", "sub": True},
             {"id": "pressure", "label": "Air pressure", "sub": True},
             {"id": "share", "label": "Air left above you"},
             {"id": "case", "label": "The case"},
         ]},

        {"type": "formula",
         "id": "atmos-rule",
         "eyebrow": "The relationship · a stack, not a triangle",
         "statement": "Air pressure = weight of the air above ÷ the area it "
                      "presses on",
         # ⚠️ NO PROPORTIONALITY CLAUSE HERE. `p5-02`'s rule line says
         # "twice the depth, twice the pressure"; air is squashable and is
         # not linear with height, so this one says only that the layers you
         # have climbed above stop pressing.
         "support": [
             "P = W ÷ A",
             "Every layer adds its weight to what is below it.",
             "Climb, and the layers you pass are no longer pressing on you.",
         ],
         "figure": {
             "art": "p5-stack",
             "aria_label": "A column of air divided into five bands. At "
                           "11 km the pressure is 23 kilopascals, at 8.85 km "
                           "31, at 5.5 km 50, at 2.5 km 75, and at sea level "
                           "101 kilopascals. The bands get thinner and "
                           "heavier towards the ground.",
             "equal": False,
             "height_px": 400,
             "foot": "1 m² OF GROUND",
             # ⚖️ UNEQUAL BANDS, AND THE TOTALS ARE THE STANDARD-ATMOSPHERE
             # PRESSURES. Each band's `weight` is the kPa it adds; the drawn
             # depth thins upwards because air is squashable.
             "layers": [
                 {"label": "thin air", "weight": 23, "depth": 1.9,
                  "total": "11 km · 23 kPa"},
                 {"label": "", "weight": 8, "depth": 1.5,
                  "total": "8.85 km · 31 kPa"},
                 {"label": "", "weight": 19, "depth": 1.3,
                  "total": "5.5 km · 50 kPa"},
                 {"label": "", "weight": 25, "depth": 1.15,
                  "total": "2.5 km · 75 kPa"},
                 {"label": "", "weight": 26, "depth": 1.0,
                  "total": "0 m · 101 kPa"},
             ],
         }},

        {"type": "worked-example", "id": "cfifa-atmos-plain"},
        {"type": "worked-example", "id": "cfifa-atmos-convert"},
        {"type": "check", "id": "your-turn-atmos", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "nothing-sucks-air-pushes"},

        {"type": "misconception", "id": "think-vacuum-sucks",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-atmos-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A window is 2 m². At sea level the air presses on it "
                    "with 101 000 Pa. What force is that?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "101 000 Pa stays 101 000 Pa · 2 m² stays 2 m²",
              "note": "The pressure is already in pascals and the area "
                      "already in square metres, so there is nothing to "
                      "convert."},
             {"letter": "F", "label": "Formula",
              "line": "force = pressure × area",
              "note": "The same relationship as always, rearranged for the "
                      "force."},
             {"letter": "I", "label": "Insert",
              "line": "force = 101 000 Pa × 2 m²",
              "note": "Pascals are newtons per square metre, so this will "
                      "give newtons."},
             {"letter": "F", "label": "Fine-tune",
              "line": "101 000 × 2 = 202 000",
              "note": "Two square metres carry twice the force of one."},
             {"letter": "A", "label": "Answer",
              "line": "force = 202 000 N",
              "note": "Two hundred thousand newtons on one window — and the "
                      "same again from inside, which is why it stays put."},
         ]},

        {"id": "cfifa-atmos-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A skylight is 0.8 m². At a mountain station the air "
                    "presses with 80 kPa. What force is that?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, at your own height."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "80 kPa × 1000 = 80 000 Pa",
              "note": "A kilopascal is a thousand pascals, and only pascals "
                      "times square metres give newtons."},
             {"letter": "F", "label": "Formula",
              "line": "force = pressure × area",
              "note": "Rearranged for the force."},
             {"letter": "I", "label": "Insert",
              "line": "force = 80 000 Pa × 0.8 m²",
              "note": "The converted pressure goes in. The 80 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "80 000 × 0.8 = 64 000",
              "note": "Newtons per square metre times square metres leaves "
                      "newtons."},
             {"letter": "A", "label": "Answer",
              "line": "force = 64 000 N",
              "note": "Insert 80 instead of 80 000 and the answer comes out "
                      "64 N — a thousand times too small."},
         ]},

        {"id": "your-turn-atmos",
         "kind": "p5-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"label": "Sea level", "kpa": 101, "pa": "101 000 Pa",
                  "panum": "101 000", "fnum": "1010",
                  "palmforce": "1010 N"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your height: {label}, where the air presses with "
                      "{pa}. What force is that on one palm, 0.01 m²?",
              "lead": "Write all five lines before you check. The pressure "
                      "is the one your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{kpa} kPa × 1000 = {pa}",
                   "note": "A kilopascal is a thousand pascals, and only "
                           "pascals times square metres give newtons."},
                  {"letter": "F", "label": "Formula",
                   "line": "force = pressure × area",
                   "note": "The same relationship as always, rearranged for "
                           "the force."},
                  {"letter": "I", "label": "Insert",
                   "line": "force = {pa} × 0.01 m²",
                   "note": "The converted pressure goes in. The {kpa} never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{panum} × 0.01 = {fnum}",
                   "note": "Newtons per square metre times square metres "
                           "leaves newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "force = {palmforce}",
                   # ⊕ PHASE 3, 25 Aug 2026 — hers, verbatim. The
                   # paraphrase said the same thing and lost the word
                   # "pushing", which is the one this page spends its
                   # whole length on.
                   "note": "And the same force is pushing back on the "
                           "other side of your hand, which is why you "
                           "feel nothing."},
              ],
              "close": "The five lines give {palmforce} on a palm at "
                       "{label}. At sea level the same palm carries about "
                       "1010 N."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question. A different
              # one with different numbers had been written here;
              # hers lives in her page's JS, which the HTML
              # comparison could not see.
              "head": "A car windscreen is 1.5 m². The air outside presses "
                      "on it with 98 kPa. What force is that?",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "98 kPa × 1000 = 98 000 Pa",
                   "note": "A kilopascal is a thousand pascals, and only "
                           "pascals times square metres give newtons."},
                  {"letter": "F", "label": "Formula",
                   "line": "force = pressure × area",
                   "note": "Rearranged for the force."},
                  {"letter": "I", "label": "Insert",
                   "line": "force = 98 000 Pa × 1.5 m²",
                   "note": "The converted pressure goes in. The 98 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "98 000 × 1.5 = 147 000",
                   "note": "Newtons per square metre times square metres "
                           "leaves newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "force = 147 000 N",
                   "note": "Insert 98 instead of 98 000 and the answer "
                           "comes out 147 N."},
              ],
              "close": "The five lines give 147 000 N — and the same again "
                       "from inside the car, which is why the glass "
                       "survives."},
         ]},

        {"id": "think-vacuum-sucks",
         "kind": "predict",
         "demand": "explain",
         "targets": "PRESS-13",
         "statements": [
             {"quote": "A vacuum sucks things in.",
              "targets": "PRESS-13",
              "body": [
                  "A vacuum is <em>nothing</em>, and nothing cannot pull. "
                  "Every case that looks like sucking is the air on the "
                  "other side pushing. Drinking through a straw: you lower "
                  "the pressure in your mouth, and the atmosphere pressing "
                  "on the surface of the drink pushes it up the straw. A "
                  "sink plunger: you squeeze the air out, and the outside "
                  "air holds it against the surface. The can at the top of "
                  "this lesson: the steam stopped pushing outwards and the "
                  "air outside had a free run. <strong>Rewriting these the "
                  "right way round is the whole skill — <em>what is "
                  "pushing, and from where?</em></strong>",
              ]},
             {"quote": "If air really pressed that hard, we would feel it.",
              "targets": "PRESS-14",
              "body": [
                  "You are pressed by roughly 100 000 Pa right now — about "
                  "1000 N on each palm — and you feel nothing, for two "
                  "reasons. It pushes equally in every direction, so it does "
                  "not squash you in any one direction; and the fluids and "
                  "gases inside your body push out just as hard, so the two "
                  "match. <strong>You only notice when the balance "
                  "changes</strong>, which is exactly what your ears do on a "
                  "plane or a mountain road: for a few seconds the pressure "
                  "inside the eardrum no longer matches the pressure "
                  "outside, and you can feel the difference until it evens "
                  "out.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "nothing-sucks-air-pushes",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Atmospheric pressure is the weight of the air above you, "
                 "spread over the area it presses on — about 100 000 Pa at "
                 "sea level. It falls as you climb, because less air is left "
                 "above you. Nothing sucks: air pushes."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3,
    # closing P5's eight rungs on a flat [2, 2, 2, 2].
    "ladder": {
        "recall": {
            "q": "Atmospheric pressure is 100 000 Pa. What force does the "
                 "air push on a shop window of 1.5 m² with?",
            "options": [
                "66 667 N — divide the pressure by the area",
                "150 000 Pa — the air is pressing, so the answer is a "
                "pressure",
                "150 000 N — 100 000 Pa acting on each of 1.5 m²",
                "0.000015 N — divide the area by the pressure",
            ],
            "answer": 2,
            "feedback": {
                0: "Dividing is how you get a pressure from a force. Here "
                   "the pressure is known and each square metre carries "
                   "100 000 N, so the two multiply.",
                1: "The arithmetic is right and the unit is wrong. Pressure "
                   "× area gives a force, in newtons.",
                3: "That is the calculation upside down, and it gives an "
                   "answer far too small to be a force on a window.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A foil bag of crisps sealed at sea level puffs up tight on "
                 "an aircraft at cruising height. Which statement is right?",
            "options": [
                "There is less gravity that high up, so the air sealed "
                "inside weighs less and spreads out until the bag is full "
                "and tight against the foil.",
                "The cabin heating warms the bag and the air inside expands "
                "until the foil is stretched tight.",
                "The low pressure outside sucks the bag outwards until the "
                "foil can stretch no further.",
                "The air sealed inside is still at sea-level pressure while "
                "the cabin air is lower, so the inside push wins until the "
                "foil stretches.",
            ],
            "answer": 3,
            "feedback": {
                0: "Gravity is essentially unchanged 11 km up. What has "
                   "changed is the pressure of the air outside the bag.",
                1: "A warm bag would swell a little, but a cabin is not much "
                   "warmer than a shop. The big change is the drop in "
                   "outside pressure.",
                2: "The verdict is right and the reason is wrong. Low "
                   "pressure cannot pull — the bag swells because the air "
                   "inside is pushing out harder than the cabin air pushes "
                   "in.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why atmospheric pressure at the top of a mountain "
                 "is lower than at sea level. Use the weight of the air in "
                 "your answer.",
            "field_label": "Your explanation",
            "placeholder": "At sea level the whole depth of the "
                           "atmosphere…",
            "success": [
                "Says air has weight.",
                "Says the pressure comes from the weight of all the air "
                "above, spread over the area it presses on.",
                "Says at the top of a mountain some of that air is now below "
                "you instead of above you.",
                "Says there is therefore less weight pressing on each square "
                "metre.",
                "Concludes that the pressure is lower, and does not claim "
                "the air has become lighter or that gravity has changed.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Explain how a drink comes up a straw, without using the "
                 "word suck. Then say what would happen if you tried it on "
                 "the Moon, and why.",
            "field_label": "Your answer",
            "placeholder": "When you breathe in, the pressure in your "
                           "mouth…",
            "success": [
                "Says you lower the air pressure inside your mouth and the "
                "straw.",
                "Says the atmosphere is pushing down on the surface of the "
                "drink in the glass.",
                "Says the drink is pushed up the straw by that outside "
                "pressure, into the region of lower pressure.",
                "Says on the Moon there is no atmosphere to push on the "
                "drink.",
                "Concludes that nothing would rise up the straw however hard "
                "you breathed in, and does not describe a vacuum as pulling.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's, verbatim. The replacement
    # added a true sentence about where the atmosphere's mass sits, and
    # dropped hers about what suction actually is. Neither move clears the
    # bar: nothing was wrong with what she wrote.
    "key_note": "The atmosphere has weight, and atmospheric pressure is that "
                "weight divided by the area it presses on — about 100 000 Pa "
                "at sea level, in every direction at once. It decreases with "
                "height, because the higher you go the less air there is "
                "above you. Air pushes; nothing sucks. What looks like "
                "suction is always the atmosphere pushing on one side of "
                "something while the push on the other side has been "
                "reduced.",

    # ⊕ PHASE 3 REVERT, 25 Aug 2026. This block had been replaced with two
    # items of its own — a longer Torricelli piece and a "where the air
    # stops" piece about the 100 km boundary. Neither is wrong, and that is
    # exactly the problem: under Mide's standing ruling of 24 Aug, "a
    # different example" and "mine is clearer" are NOT defects, and nothing
    # could be named as wrong with what Design drew. Her three items are
    # restored verbatim. The replacement also carried an internal lesson
    # slug into student prose, which `ks3_smoke --static` caught.
    "stretch": [
        {"id": "the-weather-map-is-a-pressure-map",
         "type": "explainer",
         "text": "Atmospheric pressure does not only change with height — it "
                 "changes with the weather, and that is what a weather map "
                 "is showing. A \u201clow\u201d is a region where the air "
                 "above is lighter and the pressure at the ground is a few "
                 "thousand pascals below normal; a \u201chigh\u201d is the "
                 "opposite. Air flows from high pressure towards low, which "
                 "is what wind is, and the tighter the lines on the map are "
                 "packed the stronger the wind."},
        {"id": "torricelli-and-millimetres-of-mercury",
         "type": "explainer",
         "text": "The first instrument to measure any of this was a tube of "
                 "mercury stood upside down in a dish by Torricelli in "
                 "1643: the atmosphere pushing on the dish held a column of "
                 "mercury about 760 mm high, and when the weather changed "
                 "the height changed with it. Blood pressure is still "
                 "quoted in millimetres of mercury for that reason."},
        {"id": "cabins-summits-and-kitchens",
         "type": "explainer",
         "text": "Aircraft take the same physics seriously. At 11 km the air "
                 "outside a cabin is at about 23 kPa, far too little to keep "
                 "anyone conscious, so cabins are pumped up to roughly the "
                 "pressure you would meet at 2000 to 2400 m — enough to be "
                 "comfortable, low enough that the hull is not fighting a "
                 "full 100 kPa difference. The cost of that difference is "
                 "why a fuselage is a pressure vessel and why a cabin door "
                 "is enormous work to open in flight. Climbers face the raw "
                 "version: at the summit of Everest each breath contains "
                 "about a third of the oxygen molecules it would at sea "
                 "level, which is why bodies acclimatise for weeks and why "
                 "almost everyone still carries gas. And in the kitchen it "
                 "shows up gently — at altitude water boils below 100 °C, "
                 "so an egg genuinely takes longer to cook and rice may "
                 "never soften properly."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "atmospheric pressure",
         "definition": "The weight of the air above you, divided by the area "
                       "it presses on. About 100 000 Pa at sea level."},
        {"term": "kilopascal",
         "definition": "A thousand pascals, written kPa. Sea-level air "
                       "pressure is about 101 kPa."},
        {"term": "barometer",
         "definition": "An instrument that reads atmospheric pressure. Its "
                       "reading moves with the weather as well as with "
                       "height."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a case that looks like sucking and needs rewriting?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Atmospheric pressure from the weight of the air "
                   "column, why the decrease with height is not a straight "
                   "line, and pressure differences in gases.",

    # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's, verbatim. The replacement
    # changed a claim ("rounded to the nearest kilopascal" became "each
    # within a kilopascal of the international standard"), dropped her
    # sentence explaining what the "air left above you" readout is, and
    # added one about the column being drawn to scale. None of that clears
    # the bar.
    "convention_note": "The heights and pressures are standard-atmosphere "
                       "values rounded to the nearest kilopascal: real "
                       "pressure at any height varies with the weather by "
                       "several kilopascals, and with temperature. The "
                       "boiling points are approximate for pure water. "
                       "\u201cAir left above you\u201d is the share of the "
                       "whole atmosphere\u2019s weight still overhead, "
                       "worked out from the pressure itself. The bag is "
                       "drawn swelling in proportion to the pressure drop "
                       "and is clipped once it would leave the panel; a real "
                       "bag stops stretching and then splits.",

    "ws": [],
}
