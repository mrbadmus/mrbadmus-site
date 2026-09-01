"""P5 L1 — Pressure = force ÷ area (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p5/p5-01-pressure-force-over-area.dc.html`.

Her page wins outright. The drawing pin, the block on sand, both worked
examples and all four rungs are hers.

── ⚖️ MRB-204 · A TRIANGLE, AND THE PAGE SAYS WHY IT IS ALLOWED ──────

The lesson's own relationship is `pressure = force ÷ area`, which is a
DIVISION — and a division alone does not earn a triangle. What earns it
is that the division is a genuine product rearranged: the triangle asserts
`force = pressure × area`, which is TRUE, so `A = B × C` holds and the
figure encodes a relationship that exists. Force sits at the apex;
pressure and area sit below it.

**This is the only triangle in P5.** `p5-02` and `p5-04` are sums of
layers and `p5-03` is a difference; none of the three takes one.

── ⚖️ RULED · "AT RIGHT ANGLES TO THE SURFACE" IS LOAD-BEARING ───────

It is the statutory clause — *acting normal to any surface* — it is the
reason the second misconception block exists, and without it the formula
is WRONG rather than simplified. It rides in the symbol key, in the
explainer and in the key note.

── ⚖️ RULED · THE SAND'S 6000 Pa IS A TEACHING THRESHOLD ─────────────

Fixed so that failure is something a student can reach, and the foot line
declares it. Real ground has no single failure pressure — it varies with
grain size, packing and how wet it is, and it gives way gradually.
`r_block_on_sand` asserts that some (face, mass) pair clears the limit
and some pair does not, so neither half of the bench is a dead state.

── ⚖️ RULED · THE THREE FACES ARE ONE SOLID, AND THE AREAS ARE CHECKED

0.20 × 0.10 × 0.05 m gives 0.020, 0.010 and 0.005 m². The renderer
multiplies each face's own stated dimensions and refuses a mismatch,
because the whole claim is that the AREA is what changed.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel.

── ⚖️ THE `PRESS` FAMILY OPENS HERE ──────────────────────────────────

    PRESS-01  a sharp point pushes harder than a blunt one
    PRESS-02  pressure only pushes downwards
    PRESS-03  pressure is a force, so it is measured in newtons
    PRESS-04  more contact area means more pressure on the floor

`PRESS-02` has no `elicited_by`, which §5.3 allows: nothing on the page
asks the student to commit to it, and it is confronted because it sits
underneath the first. `PRESS-04` is not in Design's table — it arrived
with rung 2's third option, and it is separate from `PRESS-01`: a student
can have given up "sharp pushes harder" and still think that more contact
means more pressure.
"""

LESSON = {
    "slug":  "pressure-force-over-area",
    "title": "Pressure = force ÷ area",
    "discipline": "physics",
    "unit": "Pressure",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.PRES.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["non-contact-forces"],
    "assumes": [],
    "references": ["what-a-force-is", "gas-pressure", "how-breathing-works"],
    "ks4_links": [],

    "meta_description": "A drawing pin is squeezed between finger and thumb "
                        "with equal forces. One end goes into the wood and "
                        "the other does not go into your thumb. The "
                        "difference is the area.",

    "big_question": "A drawing pin is squeezed between one finger and one "
                    "thumb. The two forces are equal — they have to be. One "
                    "end goes into the wood and the other does not go into "
                    "your thumb.",

    "rail": [
        {"anchor": "s-hook",    "short": "PIN",
         "label": "The pin and the point", "done_when": "committed"},
        {"anchor": "s-bench",   "short": "SAND",
         "label": "Block on sand",   "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",  "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Press the flat head into your thumb. Now turn it round.",
        "prompt": "Hold a drawing pin between finger and thumb and squeeze, "
                  "gently. The head does nothing to your thumb. The point, "
                  "under the same squeeze, goes straight into the wood.",
        "commit": "Your finger and your thumb push on the pin with the same "
                  "force. So why does only one end go in?",
        "options": [
            "The point is sharper, so the push it gives out is bigger",
            "The same force is acting on a much smaller area at the point",
            "The metal is stronger at the point than it is at the head",
            "Your thumb pushes harder on the pin than your finger does",
        ],
        "answer": 1,
        "reveal": "Nothing about the force is different. What is different "
                  "is the <em>area</em> each end acts on. The head spreads "
                  "its force across a few square millimetres of thumb; the "
                  "point concentrates the same force onto a tiny fraction of "
                  "one. <strong>Force divided by the area it is spread over "
                  "has its own name and its own unit: that is "
                  "pressure.</strong>",
    },

    "misconceptions": [
        {"id": "PRESS-01",
         "statement": "A sharp point pushes harder than a blunt one.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "PRESS-02",
         "statement": "Pressure only pushes downwards.",
         "confronted_by": "s-think"},
        {"id": "PRESS-03",
         "statement": "Pressure is a force, so it is measured in newtons.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "PRESS-04",
         "statement": "More of the sole touching the floor means more "
                      "pressure on it.",
         "elicited_by": "s-ladder",
         "confronted_by": "sand"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Pressure</strong> says how concentrated a force is "
                 "on the surface it meets: the force acting at right angles "
                 "to that surface, divided by the area it is spread over. It "
                 "is measured in <strong>pascals, Pa</strong>, and one "
                 "pascal is one newton spread over one square metre — "
                 "<strong>1 Pa = 1 N/m²</strong>. Pressure acts at right "
                 "angles to whatever surface it meets, whichever way that "
                 "surface happens to face."},

        # ── #s-bench · one block, three faces, a tray of sand ──────────
        {"type": "block-on-sand",
         "id": "sand",
         "anchor": "s-bench",
         "eyebrow": "At the bench · one block, three faces, a tray of sand",
         "heading": "Same weight. Different face. Different hole in the "
                    "sand.",
         "progress": "Change a control to begin",
         "lead": "The block measures 0.20 m by 0.10 m by 0.05 m, so it has "
                 "three different faces to stand on. This sand gives way at "
                 "{limit}. Choose a face. Choose the mass resting on it.",
         "limit": 6000,
         "g": 10,
         "scale": 1400,
         "w_scale": 1.6,
         "base_y": 470,
         "cx": 420,
         "start_face": 0,
         "face_label": "Face on the sand",
         "gate": {
             "prompt": "Commit first. You stand the same block on its "
                       "smallest face instead of its largest one. The weight "
                       "has not changed. What happens to the pressure under "
                       "it?",
             "options": [
                 "It goes up — the same force now pressing on a quarter of "
                 "the area",
                 "It stays the same — the weight has not changed, so the "
                 "pressure has not changed",
                 "It goes down — the force is concentrated, so less of it "
                 "reaches the sand",
                 "It goes up — standing a block on its end makes it heavier",
             ],
             "answer": 0,
         },
         "mass": {"label": "Mass on the sand", "min": 1, "max": 10,
                  "step": 1, "start": 4},
         # ⚖️ THE AREAS ARE CHECKED AGAINST THE DIMENSIONS by the renderer.
         # One solid, three faces, and the arithmetic has to close.
         "faces": [
             {"id": "flat", "label": "Flat · 0.020 m²", "area": 0.02,
              "area_label": "0.020 m²", "m_w": 0.20, "m_h": 0.10,
              "draw_w": 0.20, "draw_h": 0.05,
              "dims": "0.20 m × 0.10 m", "name": "largest"},
             {"id": "edge", "label": "On edge · 0.010 m²", "area": 0.01,
              "area_label": "0.010 m²", "m_w": 0.20, "m_h": 0.05,
              "draw_w": 0.20, "draw_h": 0.10,
              "dims": "0.20 m × 0.05 m", "name": "middle"},
             {"id": "end", "label": "On end · 0.005 m²", "area": 0.005,
              "area_label": "0.005 m²", "m_w": 0.10, "m_h": 0.05,
              "draw_w": 0.10, "draw_h": 0.20,
              "dims": "0.10 m × 0.05 m", "name": "smallest"},
         ],
         "branches": {
             "sinks": "{weight} on {area} is {pressure}, and this sand gives "
                      "way at {limit}, so the block sinks in. Two ways to "
                      "stop it, and neither of them takes any weight off the "
                      "sand in total: spread the same {weight} over more "
                      "than {needarea} m², or keep this face and bring the "
                      "mass down to {holdmass}.",
             "holds_any": "{weight} on {area} is only {pressure}, well under "
                          "the {limit} this sand gives way at, so the "
                          "surface holds. At this mass no face will sink it: "
                          "even standing the block on end, on its "
                          "{smallestarea} face, the same weight makes just "
                          "{onsmallest}. Add mass, or find a narrower foot.",
             "holds_for_now": "{weight} on {area} gives {pressure}, under "
                              "the {limit} this sand gives way at, so it "
                              "holds — for now. Nothing about the weight "
                              "needs to change to break it: stand this same "
                              "block on its {smallestname} face and the same "
                              "{weight} makes {onsmallest}. On this face you "
                              "would have to reach {needmass} instead.",
         },
         "readouts": [
             {"id": "weight", "label": "Weight pressing down", "sub": True},
             {"id": "area", "label": "Area under it", "sub": True},
             {"id": "pressure", "label": "Pressure"},
             {"id": "verdict", "label": "The sand"},
         ]},

        {"type": "formula",
         "id": "pressure-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Pressure = force ÷ area",
         "support": ["N with m² gives Pa · never N with cm²"],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Force F sits above a "
                           "dividing line; pressure P and area A sit below "
                           "it, multiplied together. Covering one letter "
                           "leaves the way to work it out.",
             # ⚠️ NO PROSE PER COVER — Design's 19 Aug re-specification.
             "order": ["left", "top", "right"],
             "covered": "left",
             "top":   {"label": "F", "button": "Cover F",
                       "result": "F = P × A", "text": ""},
             "left":  {"label": "P", "button": "Cover P",
                       "result": "P = F ÷ A", "text": ""},
             "right": {"label": "A", "button": "Cover A",
                       "result": "A = F ÷ P", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["F · force, at right angles to the surface · N",
                           "P · pressure · Pa",
                           "A · area it acts on · m²"],
             },
         }},

        {"type": "worked-example", "id": "cfifa-pressure-plain"},
        {"type": "worked-example", "id": "cfifa-pressure-convert"},
        {"type": "check", "id": "your-turn-pressure", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "pressure-is-force-over-area"},

        {"type": "misconception", "id": "think-sharp-pushes-harder",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-pressure-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A stack of bricks presses down with 24 N on a base of "
                    "0.008 m². What is the pressure on the ground?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "24 N stays 24 N · 0.008 m² stays 0.008 m²",
              "note": "The force is already in newtons and the area already "
                      "in square metres, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "pressure = force ÷ area",
              "note": "The force is the one at right angles to the ground, "
                      "which here is the weight."},
             {"letter": "I", "label": "Insert",
              "line": "pressure = 24 N ÷ 0.008 m²",
              "note": "The area is the part actually touching, not the size "
                      "of the whole stack."},
             {"letter": "F", "label": "Fine-tune",
              "line": "24 ÷ 0.008 = 3000",
              "note": "Newtons divided by square metres leaves newtons per "
                      "square metre."},
             {"letter": "A", "label": "Answer",
              "line": "pressure = 3000 Pa",
              "note": "Three thousand pascals, because 1 Pa is 1 N spread "
                      "over 1 m²."},
         ]},

        {"id": "cfifa-pressure-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A brick presses down with 30 N on a face of 200 cm². "
                    "What is the pressure?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own block."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "200 cm² ÷ 10 000 = 0.0200 m²",
              "note": "A pascal is a newton per square metre, and there are "
                      "10 000 square centimetres in a square metre."},
             {"letter": "F", "label": "Formula",
              "line": "pressure = force ÷ area",
              "note": "Force shared out over the area it presses on."},
             {"letter": "I", "label": "Insert",
              "line": "pressure = 30 N ÷ 0.0200 m²",
              "note": "The converted area goes in. The 200 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "30 ÷ 0.0200 = 1500",
              "note": "Newtons divided by square metres leaves newtons per "
                      "square metre."},
             {"letter": "A", "label": "Answer",
              "line": "pressure = 1500 Pa",
              "note": "Insert 200 instead of 0.0200 and the answer comes out "
                      "0.15 Pa — ten thousand times too small."},
         ]},

        {"id": "your-turn-pressure",
         "kind": "p5-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"weight": "40 N", "area": "0.020 m²", "mass": 4,
                  "wnum": 40, "anum": "0.020", "pnum": "2000",
                  "pressure": "2000 Pa", "dims": "0.20 m × 0.10 m",
                  "verdictnote": "Under the 6000 Pa this sand gives way at, "
                                 "so the surface holds."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your block: {weight} standing on {area}.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{weight} stays {weight} · {area} stays {area}",
                   "note": "The weight is already in newtons and the face is "
                           "already in square metres, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "pressure = force ÷ area",
                   "note": "The product force = pressure × area, rearranged "
                           "for the quantity you want."},
                  {"letter": "I", "label": "Insert",
                   "line": "pressure = {weight} ÷ {area}",
                   "note": "The weight is {mass} kg × 10 N/kg; the area is "
                           "the face you chose."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{wnum} ÷ {anum} = {pnum}",
                   "note": "Newtons divided by square metres leaves newtons "
                           "per square metre."},
                  {"letter": "A", "label": "Answer",
                   "line": "pressure = {pressure}",
                   "note": "{verdictnote}"},
              ],
              "close": "The five lines give {pressure}, and the footprint on "
                       "the bench is drawn {dims} to match."},
             {"id": "q2", "tab": "Question 2",
              "head": "A tin of paint presses down with 12 N on a base of "
                      "50 cm². What is the pressure on the shelf?",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "50 cm² ÷ 10 000 = 0.0050 m²",
                   "note": "A pascal needs square metres, and there are "
                           "10 000 square centimetres in one."},
                  {"letter": "F", "label": "Formula",
                   "line": "pressure = force ÷ area",
                   "note": "Force shared out over the area it presses on."},
                  {"letter": "I", "label": "Insert",
                   "line": "pressure = 12 N ÷ 0.0050 m²",
                   "note": "The converted area goes in. The 50 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "12 ÷ 0.0050 = 2400",
                   "note": "Newtons divided by square metres leaves newtons "
                           "per square metre."},
                  {"letter": "A", "label": "Answer",
                   "line": "pressure = 2400 Pa",
                   "note": "Insert 50 instead of 0.0050 and the answer comes "
                           "out 0.24 Pa."},
              ],
              "close": "The five lines give 2400 Pa. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-sharp-pushes-harder",
         "kind": "predict",
         "demand": "explain",
         "targets": "PRESS-01",
         "statements": [
             {"quote": "A sharp point pushes harder than a blunt one.",
              "targets": "PRESS-01",
              "body": [
                  "It does not push harder at all. Put a force meter behind "
                  "a sharp pin and a blunt one and press each into a board "
                  "until it stops: the meter reads the same. "
                  "<strong>Sharpening something changes no force anywhere "
                  "— it changes the area that force has to act "
                  "through</strong>, and pressure is force divided by area. "
                  "That is also why sharpening a knife makes cutting easier "
                  "without making you stronger, and why a blunt knife needs "
                  "you to lean on it: you are having to supply extra force "
                  "to make up for the extra area.",
              ]},
             {"quote": "Pressure pushes downwards.",
              "targets": "PRESS-02",
              "body": [
                  "Downwards is only where this lesson's examples happen to "
                  "point, because a weight on sand is the easiest case to "
                  "draw. Pressure acts at right angles to whatever surface "
                  "it meets, whichever way that surface faces: a drawing pin "
                  "pressed sideways into a noticeboard presses sideways, "
                  "water presses outwards on the walls of a tank as well as "
                  "down on its base, and the air presses on every side of "
                  "your body at once. <strong>The rule is <em>at right "
                  "angles to the surface</em>, not <em>towards the "
                  "floor</em>.</strong>",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "pressure-is-force-over-area",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Pressure is the force acting at right angles to a surface "
                 "divided by the area it acts on, measured in pascals: 1 Pa "
                 "is 1 N spread over 1 m². Put the same force on a quarter "
                 "of the area and the pressure is four times as big — which "
                 "is what a point, a blade and a stiletto heel are all for."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. P5 has eight rungs across four
    # lessons; they cycle 0,1 / 2,3 / 0,1 / 2,3 for a flat [2,2,2,2].
    "ladder": {
        "recall": {
            "q": "A crate presses down on the floor with its weight of "
                 "600 N. Its base measures 0.30 m². What is the pressure on "
                 "the floor?",
            "options": [
                "2000 Pa — 600 N shared over 0.30 m²",
                "180 Pa — multiply the force by the area",
                "2000 N — a press on the floor is a force, so it is in "
                "newtons",
                "0.0005 Pa — divide the area by the force",
            ],
            "answer": 0,
            "feedback": {
                1: "Multiplying gives you a force back when you already know "
                   "the pressure. To find the pressure you share the force "
                   "out over the area, so you divide.",
                2: "The arithmetic is right and the unit is wrong. Force "
                   "divided by area gives newtons per square metre, which is "
                   "the pascal.",
                3: "That is the calculation upside down. Pressure is how "
                   "much force each square metre carries, so the force is "
                   "the one being shared out.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "Two students both weigh 500 N. One is in flat boots, "
                 "touching the floor over 0.025 m². The other is in heels, "
                 "touching it over 0.0005 m². Which statement is right?",
            "options": [
                "They press on the floor with the same pressure, because "
                "they weigh the same.",
                "The heels give 1 000 000 Pa against 20 000 Pa — fifty "
                "times the pressure for exactly the same weight.",
                "The boots give the higher pressure, because more of the "
                "sole is in contact with the floor, so more of the weight "
                "reaches it.",
                "The heels give the higher pressure, because walking in "
                "heels makes you push down harder.",
            ],
            "answer": 1,
            "feedback": {
                0: "Same force, but not the same area. The weight decides "
                   "the force; the area decides how concentrated it is.",
                2: "More contact area is what lowers the pressure. The same "
                   "500 N shared over fifty times the area is fifty times "
                   "gentler on the floor.",
                3: "The verdict is right and the reason is wrong. Both "
                   "students weigh 500 N, and that is the whole force in "
                   "either case — it is the area that has changed.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A drawing pin has a wide flat head and a very sharp point. "
                 "Explain why it is made that way, using the words force, "
                 "area and pressure.",
            "field_label": "Your explanation",
            "placeholder": "The force pushing on the head is…",
            "success": [
                "Says the force at the head and the force at the point are "
                "the same.",
                "Says the head has a large area and the point a very small "
                "one.",
                "Says pressure is the force divided by the area it acts on.",
                "Says the pressure under the point is therefore very high, "
                "which is why it goes into the wood.",
                "Says the pressure under the head is low, which is why it "
                "does not go into your thumb.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A tracked machine weighs 12 000 N and must not press on "
                 "soft ground with more than 30 000 Pa. Work out the "
                 "smallest total track area it can have, and explain why the "
                 "same machine on wheels touching half that area would sink "
                 "where the tracks do not.",
            "field_label": "Your answer",
            "placeholder": "Rearranging the formula gives…",
            "success": [
                "Rearranges to area = force ÷ pressure.",
                "Works out 12 000 ÷ 30 000 = 0.4 m², and gives the unit as "
                "square metres.",
                "Says halving the area doubles the pressure for the same "
                "weight.",
                "Gives that pressure as 60 000 Pa, which is over the "
                "30 000 Pa limit.",
                "Says the weight has not changed — the wheels change the "
                "area, not the force.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Pressure is the force acting at right angles to a surface "
                "divided by the area it is spread over: pressure in pascals "
                "= force in newtons ÷ area in square metres, and 1 Pa = "
                "1 N/m². The same force on a smaller area gives a higher "
                "pressure, and on a larger area a lower one. Pressure is not "
                "a force and is not measured in newtons, and it acts at "
                "right angles to whichever surface it meets.",

    "stretch": [
        {"id": "in-or-on",
         "type": "explainer",
         "text": "Once you can see pressure as force over area, a lot of "
                 "design stops looking arbitrary. Anything meant to go "
                 "<em>into</em> something else concentrates a force into "
                 "almost no area: nails, needles, studs, chisels, teeth, "
                 "claws. Anything meant to stay <em>on top of</em> something "
                 "soft spreads it: snowshoes, tractor tyres, tank tracks, "
                 "the flat splayed feet of a camel, and the wide concrete "
                 "footings under a building, which exist only to hand the "
                 "whole weight of the house to the ground over enough square "
                 "metres that the ground can take it. <strong>Both are the "
                 "same equation, read in opposite directions.</strong>"},
        # ⚖️ DESIGN'S FLAG 9 — the hydraulic jack, with the distance traded
        # explicitly against the force. The belief it confronts is `ENER-19`,
        # owned by `p1-08`; this re-confronts it and mints nothing.
        {"id": "the-hydraulic-trade",
         "type": "explainer",
         "text": "Liquids give the idea a second life. Because a liquid "
                 "cannot be squashed much, pressure applied at one place is "
                 "felt everywhere in it, so a small force on a small piston "
                 "can hold up a car on a big one — the pressure is the same "
                 "in both cylinders, and the big piston simply has more "
                 "square metres for it to act on. That is a hydraulic jack, "
                 "and it is worth being careful about what it does and does "
                 "not give you: the big piston pushes with more force, but "
                 "it moves a much shorter distance, and the two multiply out "
                 "to the same energy transferred. <strong>Force can be "
                 "multiplied. Energy cannot</strong>, which is the same "
                 "trade you get from a long spanner in the lesson on "
                 "moments."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "pressure",
         "definition": "The force acting at right angles to a surface, "
                       "divided by the area it is spread over. Not a force."},
        {"term": "pascal",
         "definition": "The unit of pressure, written Pa. One pascal is one "
                       "newton spread over one square metre."},
        {"term": "square metre",
         "definition": "The unit of area a pascal needs. There are 10 000 "
                       "square centimetres in one, not 100."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a pressure of your own to work out — a shoe, a tyre, a "
                "knife?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Pressure in pascals and kilopascals, pressure in fluids "
                   "and its increase with depth, upthrust and floating, and "
                   "pressure–volume work on gases.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Press the pin against your fingertip firmly, but never "
                   "hard enough to break the skin. You are feeling the "
                   "difference, not testing how much you can stand.",

    "convention_note": "The sand tray is a teaching model. Its giving-way "
                       "pressure is fixed at 6000 Pa so that failure is "
                       "something you can reach; real ground varies with "
                       "grain size, packing and how wet it is, and gives way "
                       "gradually rather than at one number. The mass you "
                       "set is the whole mass resting on the sand, block "
                       "included, and weight is taken as mass in kilograms × "
                       "10 N/kg. The block is drawn to scale in "
                       "cross-section; the weight arrow uses its own "
                       "separate scale, and the depth it sinks is drawn as a "
                       "fixed amount rather than calculated.",

    "ws": [],
}
