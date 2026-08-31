"""P5 L2 — Pressure in liquids (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p5/p5-02-pressure-in-liquids.dc.html`.

Her page wins outright. The three holes in the can, the probe in the tank,
the stack of layers, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A STACK, NOT A TRIANGLE, AND NOT A BAR ───────────────

The new content here is WHERE THE FORCE COMES FROM — a sum of layers —
and the arithmetic is `p5-01`'s division. So the figure is a stack and it
carries a running total, and the relationship line is the same `P = W ÷ A`
it always was. A triangle would be the wrong shape twice over: this is a
sum, and the division it feeds is already drawn one lesson back.

⚖️ **NO COVER BUTTONS, AND DESIGN'S FLAG 0a IS RIGHT ABOUT WHY.** Covering
a layer of water means nothing. A part–whole bar keeps its buttons because
covering a part asks a real question; a stack does not.

── ⚖️ RULED · THE PROBE READS GAUGE PRESSURE, AND THE PAGE SAYS SO ───

The reading counts the liquid ONLY. The atmosphere is pressing on the
surface as well and adds about 100 000 Pa everywhere in the tank. Without
that line a student takes the surface reading of 0 Pa as an absolute
vacuum, which is the one way this bench can actively mislead — so the
zero branch says *"the reading counts the liquid only, and the air is
still pressing on the surface the whole time"*, and the foot line repeats
it.

── ⚖️ RULED · EVERY BRANCH NAMES THE SAME DEPTH IN ANOTHER LIQUID ────

Design's rule for this bench, and it is a real one: a student who moves
the probe AND swaps the liquid otherwise has two variables and no way to
tell which did what. `r_depth_probe` refuses a payload with fewer than two
densities for exactly that reason.

── ⚖️ THE WEIGHT ABOVE IS DERIVED, AND IT COMES OUT RIGHT ────────────

`weight above = pressure × face area`. A 2 m column of water over a
0.02 m² face is 0.04 m³, which is 40 kg, which is 400 N — and
`20 000 Pa × 0.02 m²` is 400 N. The tile and the reading cannot disagree
because one is computed from the other.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    PRESS-05  more liquid in total means more pressure at the bottom
    PRESS-06  water is heavier, or packed tighter, deeper down
    PRESS-07  pressure in a liquid acts downwards only
    PRESS-08  a wider container gives a bigger pressure at its base

`PRESS-07` has no `elicited_by`: nothing asks the student to commit to it,
and it is confronted by the explainer and by the four-way rosette on the
probe face. `PRESS-08` is not in Design's table — it arrived with rung 2's
third option, and it is `PRESS-05` from the other side: not "more water"
but "a narrower tube concentrates it", which is a `p5-01` idea being
misapplied.
"""

LESSON = {
    "slug":  "pressure-in-liquids",
    "title": "Pressure in liquids",
    "discipline": "physics",
    "unit": "Pressure",
    "family": "MODEL",

    "covers": ["KS3.P.PRES.02a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["pressure-force-over-area"],
    "assumes": [],
    "references": ["upthrust-floating-and-sinking", "what-a-force-is"],
    "ks4_links": [],

    "meta_description": "Punch three holes down the side of a full can and "
                        "the bottom jet shoots furthest, every time. Lower a "
                        "probe into a tank and find out why depth is the "
                        "only thing that matters.",

    "big_question": "Punch three holes down the side of a full can — near "
                    "the top, halfway, near the bottom. The bottom jet "
                    "shoots out furthest, every single time.",

    "rail": [
        {"anchor": "s-hook",    "short": "CAN",
         "label": "Three holes in a can", "done_when": "committed"},
        {"anchor": "s-bench",   "short": "TANK",
         "label": "Probe in the tank",    "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "The stack and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Three holes, one can, three different jets.",
        "prompt": "The top hole dribbles. The middle one arches out. The "
                  "bottom one throws water most of the way across the sink. "
                  "Same can, same water, holes the same size.",
        "commit": "Why does the bottom jet travel furthest?",
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
            "The can is narrower at the bottom, so the water is squeezed "
            "out faster there",
            "The water from the bottom hole has further to fall, so it "
            "lands further out",
            "There is more water stacked above the bottom hole, so it "
            "presses harder there",
            "Water gets heavier as it sinks, so the lowest water pushes "
            "hardest of all",
        ],
        "answer": 2,
        "reveal": "Nothing about the water changes as it sinks. A litre near "
                  "the bottom weighs exactly what a litre near the top "
                  "weighs. What changes is how much water is <em>stacked "
                  "above the hole</em>: at the bottom hole the whole depth "
                  "of water is pressing, and at the top hole only a few "
                  "centimetres are. <strong>More weight above, on the same "
                  "area, means more pressure</strong> — and a faster jet.",
    },

    "misconceptions": [
        {"id": "PRESS-05",
         "statement": "More liquid in total means more pressure at the "
                      "bottom.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "PRESS-06",
         "statement": "Water is heavier, or packed tighter, deeper down.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "PRESS-07",
         "statement": "Pressure in a liquid acts downwards only.",
         "confronted_by": "probe"},
        {"id": "PRESS-08",
         "statement": "A narrow container concentrates the pressure, so its "
                      "base takes more than a wide one at the same depth.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A liquid presses on everything it touches. Go deeper and "
                 "there is more liquid stacked above you, so more weight is "
                 "pressing on each square metre and the pressure is higher. "
                 "At any one depth a liquid presses <strong>equally in every "
                 "direction</strong> — down on the bottom, sideways on the "
                 "walls, and upwards on anything underneath — which is why "
                 "water comes out sideways through a hole in the side of a "
                 "can rather than just running down the inside."},

        # ── #s-bench · a pressure probe on a cable ─────────────────────
        {"type": "depth-probe",
         "id": "probe",
         "anchor": "s-bench",
         "eyebrow": "At the bench · a pressure probe on a cable",
         "heading": "Same probe. Same liquid. Just lower.",
         "progress": "Change a control to begin",
         "lead": "The probe has a face of {face}, and it reads the pressure "
                 "of the liquid alone. Lower it, and change what the tank is "
                 "filled with.",
         "face": 0.02,
         "px_per_m": 90,
         "surface_y": 90,
         "start_liquid": 0,
         "liquid_label": "What the tank holds",
         "surface_label": "SURFACE",
         "gate": {
             "prompt": "Commit first. You lower the probe from 1 m down to "
                       "2 m down in the same tank. What happens to the "
                       "reading?",
             "options": [
                 "It doubles — twice the depth means twice the liquid above "
                 "the face",
                 "It stays the same — it is the same tank and the same "
                 "liquid",
                 "It halves — the deeper water is out of the way of the "
                 "surface",
                 "It goes up a little — the water down there is packed "
                 "tighter",
             ],
             "answer": 0,
         },
         "depth": {"label": "Depth of the probe", "min": 0, "max": 10,
                   "step": 1, "start": 6, "per_step": 0.5},
         "liquids": [
             {"id": "water", "label": "Water", "name": "fresh water",
              "rho": 1000},
             {"id": "sea", "label": "Sea water", "name": "sea water",
              "rho": 1025},
             {"id": "paraffin", "label": "Paraffin", "name": "paraffin",
              "rho": 800},
         ],
         # ⚖️ THE SURFACE IS ITS OWN BRANCH. It is the honest zero of the
         # experiment and the one place the gauge/absolute distinction can
         # mislead, not a shallow reading with a small number.
         "branches": {
             "surface": "The probe is sitting at the surface with no {name} "
                        "above it at all, so the liquid presses on it with "
                        "{pressure}. This is the honest zero of the "
                        "experiment: the reading counts the liquid only, and "
                        "the air is still pressing on the surface the whole "
                        "time.",
             "shallow": "{depth} down in {name}, and the {weight} sitting on "
                        "the face gives {pressure}. Halve the depth to "
                        "{half} and it falls to {halfp} — the depth and the "
                        "pressure rise and fall together. In {othername} the "
                        "same {depth} would read {otherp} instead.",
             "deep": "Down at {depth} the column above the face weighs "
                     "{weight}, which is {pressure} on the face — and it "
                     "does not matter how wide the tank is, only how far "
                     "down you are. Compare it with {half}, where the same "
                     "probe read {halfp}. In {othername} this depth would "
                     "give {otherp}, because a cubic metre of it weighs a "
                     "different amount.",
         },
         "readouts": [
             {"id": "depth", "label": "Depth"},
             {"id": "weight", "label": "Liquid above the face", "sub": True},
             {"id": "pressure", "label": "Pressure on the face"},
             {"id": "same", "label": "Turn the face over"},
         ]},

        {"type": "formula",
         "id": "depth-rule",
         "eyebrow": "The relationship · a stack, not a triangle",
         "statement": "Pressure at a depth = weight of the liquid above ÷ "
                      "the area it presses on",
         "support": [
             "P = W ÷ A",
             "Every layer adds its weight to what is below it.",
             "Twice the depth, twice the weight above, twice the pressure.",
         ],
         "figure": {
             "art": "p5-stack",
             "aria_label": "A stack of five layers of water, each one metre "
                           "deep. Each layer adds ten thousand newtons to "
                           "every square metre below it, so the running "
                           "total goes 10 000, 20 000, 30 000, 40 000 and "
                           "50 000 pascals at five metres down.",
             "equal": True,
             "height_px": 400,
             "total_fmt": "%s Pa",
             "foot": "1 m² OF FLOOR",
             "layers": [
                 {"label": "1 m · 10 000 N", "weight": 10000, "depth": 1},
                 {"label": "1 m · 10 000 N", "weight": 10000, "depth": 1},
                 {"label": "1 m · 10 000 N", "weight": 10000, "depth": 1},
                 {"label": "1 m · 10 000 N", "weight": 10000, "depth": 1},
                 {"label": "1 m · 10 000 N", "weight": 10000, "depth": 1},
             ],
         }},

        {"type": "worked-example", "id": "cfifa-depth-plain"},
        {"type": "worked-example", "id": "cfifa-depth-convert"},
        {"type": "check", "id": "your-turn-depth", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "depth-decides-the-pressure"},

        {"type": "misconception", "id": "think-more-water-more-pressure",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-depth-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A probe with a 0.05 m² face sits 2 m down. The water "
                    "above its face weighs 1000 N. What is the pressure on "
                    "it?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1000 N stays 1000 N · 0.05 m² stays 0.05 m²",
              "note": "The weight is already in newtons and the face already "
                      "in square metres, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "pressure = weight of the liquid above ÷ area",
              "note": "The same relationship as any other pressure. Only the "
                      "force has a new name."},
             {"letter": "I", "label": "Insert",
              "line": "pressure = 1000 N ÷ 0.05 m²",
              "note": "The area is the probe face, not the area of the whole "
                      "tank."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1000 ÷ 0.05 = 20 000",
              "note": "Newtons divided by square metres leaves newtons per "
                      "square metre."},
             {"letter": "A", "label": "Answer",
              "line": "pressure = 20 000 Pa",
              "note": "Twenty thousand pascals, which is what 2 m of water "
                      "comes to."},
         ]},

        {"id": "cfifa-depth-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A probe face of 250 cm² has 600 N of water above it. "
                    "What is the pressure on the face?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own probe."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "250 cm² ÷ 10 000 = 0.0250 m²",
              "note": "A pascal is a newton per square metre, and there are "
                      "10 000 square centimetres in a square metre."},
             {"letter": "F", "label": "Formula",
              "line": "pressure = weight of the liquid above ÷ area",
              "note": "Force shared out over the face it presses on."},
             {"letter": "I", "label": "Insert",
              "line": "pressure = 600 N ÷ 0.0250 m²",
              "note": "The converted area goes in. The 250 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "600 ÷ 0.0250 = 24 000",
              "note": "Newtons divided by square metres leaves newtons per "
                      "square metre."},
             {"letter": "A", "label": "Answer",
              "line": "pressure = 24 000 Pa",
              "note": "Insert 250 instead of 0.0250 and the answer comes out "
                      "2.4 Pa."},
         ]},

        {"id": "your-turn-depth",
         "kind": "p5-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"weight": "600 N", "name": "fresh water",
                  "face": "0.02 m²", "depth": "3.0 m",
                  "wnum": 600, "fnum": 0.02, "pnum": "30 000",
                  "pressure": "30 000 Pa"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your probe: {weight} of {name} above a {face} face, "
                      "{depth} down.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own tank is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{weight} stays {weight} · {face} stays {face}",
                   "note": "The weight is already in newtons and the face "
                           "already in square metres, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "pressure = weight of the liquid above ÷ area",
                   "note": "Force over area, with the weight of the column "
                           "as the force."},
                  {"letter": "I", "label": "Insert",
                   "line": "pressure = {weight} ÷ {face}",
                   "note": "Both figures come off the bench above."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{wnum} ÷ {fnum} = {pnum}",
                   "note": "Newtons divided by square metres leaves newtons "
                           "per square metre."},
                  {"letter": "A", "label": "Answer",
                   "line": "pressure = {pressure}",
                   "note": "At {depth} down in {name}, pressing equally in "
                           "every direction."},
              ],
              "close": "The five lines give {pressure}, and the shaded "
                       "column on the bench is the {weight} those lines "
                       "used."},
             {"id": "q2", "tab": "Question 2",
              "head": "A hatch of 400 cm² in the side of a tank has 1600 N "
                      "of water above it. What is the pressure on the "
                      "hatch?",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "400 cm² ÷ 10 000 = 0.0400 m²",
                   "note": "A pascal needs square metres, and there are "
                           "10 000 square centimetres in one."},
                  {"letter": "F", "label": "Formula",
                   "line": "pressure = weight of the liquid above ÷ area",
                   "note": "Force shared out over the area it presses on."},
                  {"letter": "I", "label": "Insert",
                   "line": "pressure = 1600 N ÷ 0.0400 m²",
                   "note": "The converted area goes in. The 400 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "1600 ÷ 0.0400 = 40 000",
                   "note": "Newtons divided by square metres leaves newtons "
                           "per square metre."},
                  {"letter": "A", "label": "Answer",
                   "line": "pressure = 40 000 Pa",
                   "note": "Insert 400 instead of 0.0400 and the answer "
                           "comes out 4 Pa."},
              ],
              "close": "The five lines give 40 000 Pa. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-more-water-more-pressure",
         "kind": "predict",
         "demand": "explain",
         "targets": "PRESS-05",
         "statements": [
             {"quote": "More water means more pressure, so a lake presses "
                       "harder than a bucket.",
              "targets": "PRESS-05",
              "body": [
                  "Only if it is deeper. Stand a narrow tube of water 2 m "
                  "tall next to a swimming pool 2 m deep and the pressure at "
                  "the bottom of each is the same, to the pascal. What sits "
                  "above your square metre of floor is a column 2 m tall in "
                  "both cases, and <strong>the water off to the sides in the "
                  "pool is not resting on your square metre — it is resting "
                  "on its own.</strong> This is why a water tower works: "
                  "what matters for the pressure at your tap is how high the "
                  "water is above it, not how many litres the tower holds.",
              ]},
             {"quote": "Water is heavier at the bottom.",
              "targets": "PRESS-06",
              "body": [
                  "It is not. A litre from the bottom of the tank and a "
                  "litre from the top balance each other exactly — and a "
                  "liquid is very nearly impossible to squash, so the water "
                  "down there is not even packed tighter. <strong>Nothing "
                  "about the water changes with depth. What changes is how "
                  "much of it is above you</strong>, which is a fact about "
                  "your position, not about the water.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "depth-decides-the-pressure",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         # ⊕ PHASE 3 REVERT, 25 Aug 2026. This had been paraphrased. The
         # paraphrase is not wrong — it even adds "and on the liquid",
         # which is true — but under Mide's standing ruling "mine is
         # clearer" is not a defect, and Design's own sentence is what the
         # page is meant to leave a student with. Hers, verbatim.
         "text": "Pressure in a liquid increases with depth, because the "
                 "deeper you go the more liquid is stacked above you. At "
                 "any one depth the liquid presses equally in every "
                 "direction, and it is the depth that decides the "
                 "pressure — not how much liquid there is in total."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A pressure probe has a face of 0.05 m². At the depth it is "
                 "hanging, the water above its face weighs 1500 N. What is "
                 "the pressure on the face?",
            "options": [
                "75 Pa — multiply the weight by the area",
                "30 000 N — the probe is measuring a push, so it reads in "
                "newtons",
                "30 000 Pa — 1500 N shared over 0.05 m²",
                "0.000033 Pa — divide the area by the weight",
            ],
            "answer": 2,
            "feedback": {
                0: "Multiplying gives a force back from a pressure you "
                   "already know. To find the pressure, the weight is shared "
                   "out over the area, so you divide.",
                1: "The arithmetic is right and the unit is wrong. Newtons "
                   "divided by square metres gives pascals.",
                3: "That is the division upside down. Pressure asks how much "
                   "force each square metre is carrying.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A swimming pool is filled to 2 m deep. Beside it stands a "
                 "thin pipe of water, also 2 m tall, open at the top. Where "
                 "is the pressure greater at the bottom?",
            "options": [
                "The pool, because it holds thousands of times more water.",
                "The pipe, because the same push is concentrated into a "
                "narrow tube, and a narrower column always presses harder at "
                "the bottom.",
                "The same in both, because water always presses the same "
                "everywhere.",
                "The same in both — the depth is the same, and depth is "
                "what decides it.",
            ],
            "answer": 3,
            "feedback": {
                0: "The extra water in the pool is sitting on its own patch "
                   "of floor, not on yours. Above any one square metre there "
                   "is 2 m of water in both cases.",
                1: "Nothing is being concentrated. Each square metre of the "
                   "pipe’s base carries the water directly above it, "
                   "exactly as in the pool.",
                2: "The verdict is right and the reason is wrong. Water does "
                   "not press the same everywhere — it presses harder "
                   "deeper down. These two match because their depths "
                   "match.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A concrete dam is thin at the top and much thicker at the "
                 "base. Explain why, using depth, pressure and the water "
                 "above.",
            "field_label": "Your explanation",
            "placeholder": "Near the top of the dam there is…",
            "success": [
                "Says the pressure on the dam increases with depth.",
                "Says that is because there is more water stacked above the "
                "deeper parts.",
                "Says the water presses sideways on the wall, not only "
                "downwards.",
                "Says the base therefore has to withstand a much greater "
                "pressure than the top.",
                "Says the extra thickness is there to take that larger push.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "You punch three holes down the side of a full can and "
                 "watch the jets. Predict what the three jets look like, "
                 "then say what happens to all three as the can empties, and "
                 "explain both using pressure.",
            "field_label": "Your answer",
            "placeholder": "The bottom hole…",
            "success": [
                "Says the lowest hole gives the fastest, furthest jet.",
                "Explains it as the greatest depth of water above that hole.",
                "Says the jets come out sideways because a liquid presses in "
                "every direction.",
                "Says every jet weakens as the can empties.",
                "Explains that as the depth of water above each hole "
                "falling, and notes each hole stops when the surface reaches "
                "it.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "The pressure in a liquid rises with depth, because each "
                "layer of liquid adds its weight to everything below it. "
                "Work it out the same way as any other pressure: the weight "
                "of the liquid above, divided by the area it presses on. At "
                "a given depth the push is the same in every direction, and "
                "it depends on the depth and the liquid — not on how much "
                "liquid there is or how wide the container is.",

    "stretch": [
        {"id": "dams-and-hulls",
         "type": "explainer",
         "text": "Every dam in the world is built to this fact. The pressure "
                 "at the top of the wall is almost nothing and the pressure "
                 "at the base is enormous, so a dam is thin at the top and "
                 "thick at the bottom — <strong>the shape is a drawing of "
                 "the pressure it has to hold.</strong> Submarines are the "
                 "same story from the inside: a hull that is comfortable at "
                 "100 m is in serious trouble at 500 m, and the deep-sea "
                 "vehicles that visit the bottom of the Mariana Trench sit "
                 "inside spheres with walls several centimetres thick, "
                 "because a sphere is the only shape that has no flat side "
                 "for the water to work on."},
        {"id": "the-height-of-the-tower",
         "type": "explainer",
         "text": "The same idea runs your taps. Water is pumped up into a "
                 "tower or a reservoir on high ground, and the pressure at "
                 "your kitchen sink comes from the height of that water "
                 "above it — nothing else. That is why the top flat in a "
                 "block often has feeble water pressure and the ground floor "
                 "does not, and why a hosepipe on a hill runs harder than "
                 "the same hose at the top of the slope. Turn it round and "
                 "you get a way to measure: a column of liquid whose height "
                 "tells you a pressure, which is what a manometer is, and "
                 "which is why blood pressure is still quoted as millimetres "
                 "of mercury."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "depth",
         "definition": "How far below the surface you are. It is the only "
                       "thing besides the liquid itself that sets the "
                       "pressure."},
        {"term": "gauge pressure",
         "definition": "A reading that counts the liquid alone and leaves "
                       "out the atmosphere pressing on the surface. The "
                       "probe on this bench reads one."},
        {"term": "manometer",
         "definition": "A column of liquid whose height tells you a "
                       "pressure. The idea of this lesson, used backwards."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a depth of your own in mind — a pool, a dam, a dive?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Pressure in a column of liquid as height × density × "
                   "gravitational field strength, pressure differences in "
                   "fluids, and how those give upthrust.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Ask your teacher before making holes in a can. Cut edges "
                   "are sharp.",

    "convention_note": "The tank is a teaching model. Water is taken as "
                       "1000 kg in every cubic metre, sea water as 1025 and "
                       "paraffin as 800, and weight as mass × 10 N/kg; real "
                       "values shift with temperature and, for sea water, "
                       "with saltiness. The probe reads the pressure of the "
                       "liquid alone — the atmosphere is pressing on the "
                       "surface as well, and adds about 100 000 Pa "
                       "everywhere in the tank. The tank is drawn to scale "
                       "in depth; the probe face is drawn larger than "
                       "0.02 m² would be so that it can be seen.",

    "ws": [],
}
