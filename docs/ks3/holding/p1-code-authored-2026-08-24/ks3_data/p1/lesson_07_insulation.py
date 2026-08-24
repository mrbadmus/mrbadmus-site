"""P1 L7 — Keeping energy in: insulation (INVESTIGATION).

The last of the four thermal lessons and the one that turns them into a design
problem. p1-04 said what drives a transfer, p1-05 and p1-06 gave it two
routes; this one asks how you slow both of them down, and makes the student
answer it with a fair test rather than an opinion.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**An insulator does nothing. That is the whole trick.** `ENER-15` is the
misconception — that a jumper, a duvet or a layer of lagging is a source of
warmth — and it is held by almost everyone because the everyday sentence is
"a jumper keeps you warm", which sounds like the jumper is doing something.
It is not. Your own thermal store is the only source in the room, and the
jumper's entire job is to be bad at passing it on. Wrap a jumper round a bottle
of cold water and the water stays cold, which is the experiment that settles it
and is what `#s-think` asks for.

**Trapped air is the insulator; the material is mostly a way of trapping it.**
Wool, foam, feathers, bubble wrap and fibreglass are all the same idea — a
structure that holds air still. Still air is a very poor conductor (p1-05's
bench: air is almost nothing) and holding it still stops it carrying warmth
away by moving. This is why a thick loose duvet beats a thin packed one made
of the same stuff, and why the bench's thickness dial does what it does.

── The bench is the fair test, not a demonstration of one ──────────────

The INVESTIGATION family's demand is that the student runs a comparison and
can say why it is fair. So the bench has TWO dials — material and thickness —
and both are modelled, because MRB-257 §5A.1 is explicit that a dial which is
drawn and not modelled marks a student's own prediction correct while showing
them nothing.

Two dials is the point. With eight cells on the bench, the only way to answer
"which material is best" is to hold the thickness, and the only way to answer
"does thickness matter" is to hold the material. The closing panel says so;
the bench is what makes it obvious first.

⚠️ **The bare beaker is a CONTROL and is shown at all times**, next to
whatever cell is selected. Without it every reading is a number with nothing
to be better than, and "kept it at 62.7 degrees" means nothing until you know
that nothing at all leaves it at 37.9.
"""

LESSON = {
    "slug":        "insulation",
    "title":       "Keeping energy in: insulation",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "INVESTIGATION",

    "covers":      ["KS3.P.ECT.02d"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["radiation"],
    "assumes":     ["conduction"],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "Four materials, two thicknesses and a bare beaker. An "
                        "insulator adds nothing and stops nothing — it only makes "
                        "the route out a bad one.",

    "big_question": "A jumper has no power supply, no fuel and no moving "
                    "parts, and it keeps you warm. Wrap the same jumper "
                    "round a bottle of cold water and the water stays cold. "
                    "Both of those are the same fact.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two identical beakers", "done_when": "committed"},
        {"anchor": "s-lag",    "short": "TEST",
         "label": "Four materials, two thicknesses",
         "done_when": "all_cells_run"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What a jumper actually does", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Same water, same starting temperature, same room. One is "
                 "wrapped and one is not.",
        "prompt": "Two identical beakers, each with 200 cm³ of water at 80 "
                  "degrees, left in a room at 20 degrees for twenty minutes. "
                  "One is bare. One is wrapped in a centimetre of foam. The "
                  "bare one comes out at 38 degrees and the wrapped one at "
                  "63.",
        "commit": "What did the foam do?",
        "options": [
            "It added warmth to the water",
            "It stopped the cold from getting in",
            "It was bad at passing the transfer on, so less got out",
            "It reflected the water's own warmth back into it",
        ],
        "reveal": "It was bad at passing the transfer on. The foam has no "
                  "energy of its own to give and does not add a single joule "
                  "— both beakers cooled. The wrapped one just cooled more "
                  "slowly, because the route out of it was a poor one. Leave "
                  "them both overnight and they will both be at 20 degrees.",
    },

    "misconceptions": [
        {"id": "ENER-15",
         "statement": "Insulation makes heat, which is why a jumper warms "
                      "you up.",
         "elicited_by": "think-commit-jumper",
         "confronted_by": "think-commit-jumper"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An insulator is a material that carries a thermal transfer "
                 "badly. That is its whole job, and it is a job done by doing "
                 "nothing. Most good insulators work the same way: they hold "
                 "a lot of air still, in small pockets, and still air is "
                 "close to the worst conductor there is."},

        # #s-lag — the flagship. Ink-dark practical, two dials.
        {"type": "lagging-bench", "id": "four-materials", "anchor": "s-lag",
         "eyebrow": "The test · 200 cm³ at 80 °C, twenty minutes, room at "
                    "20 °C",
         "heading": "Four materials, two thicknesses, one bare beaker",
         "head_counter": {"format": "{n} of 8 combinations run", "total": 8},
         "demand": "investigate",
         "targets": "ENER-15",
         "prompt": "Pick a material and a thickness, then run it. The bare "
                   "beaker is on the bench the whole time so every reading "
                   "has something to be compared with.",
         "gate": {"prompt": "Commit first. To compare the four materials "
                            "fairly, which of these matters most?",
                  "options": ["Using the same thickness for all four",
                              "Starting each one at whatever temperature it "
                              "happens to be",
                              "Using the cheapest material for each test",
                              "Running the best one for longer to be sure"]},
         "resting": "Pick a material and a thickness, then run it.",
         "start_temp": 80,
         "room_temp": 20,
         "minutes": 20,
         "unit": "°C",
         "labels": {"material": "Material", "thickness": "Thickness",
                    "after": "After 20 minutes", "drop": "Temperature drop",
                    "control": "Bare beaker (no lagging)",
                    "better": "kept above the bare beaker"},
         "run_labels": {"idle": "Run this combination",
                        "done": "Run finished"},
         # The control, shown at all times. Everything else is compared with it.
         "control_after": 37.9,
         "thicknesses": [
             {"id": "thin", "label": "1 layer"},
             {"id": "thick", "label": "3 layers"},
         ],
         # ⚖️ `rank` IS THE ORDER, at the SAME thickness. The closing claim is
         # derived from these ranks and checked against the readings — at both
         # thicknesses — in `ks3_art/p1.py`.
         "materials": [
             {"id": "newspaper", "name": "Newspaper", "rank": 3,
              "after": {"thin": 48.6, "thick": 59.1},
              "note": "The worst of the four and still far better than "
                      "nothing. Paper holds some air between its fibres, and "
                      "three layers hold three times as many pockets."},
             {"id": "cotton", "name": "Cotton wool", "rank": 2,
              "after": {"thin": 55.1, "thick": 64.4},
              "note": "Loose fibres with a lot of air between them. Squash "
                      "it flat and it works far worse, which is the clue to "
                      "what is really doing the insulating."},
             {"id": "bubble", "name": "Bubble wrap", "rank": 1,
              "after": {"thin": 59.4, "thick": 67.6},
              "note": "Air in sealed pockets, so it cannot even drift about "
                      "inside the wrap. The plastic itself is a poor "
                      "insulator; the bubbles are the material."},
             {"id": "foam", "name": "Polystyrene foam", "rank": 0,
              "after": {"thin": 62.7, "thick": 70.3},
              "note": "The best on the bench at both thicknesses. "
                      "Polystyrene foam is about 95 per cent trapped air by "
                      "volume, which is why a foam cup weighs nothing and a "
                      "solid plastic one weighs something."},
         ],
         "order_claim": ["foam", "bubble", "cotton", "newspaper"],
         "close": [
             "Four materials, and the same order at one layer and at three. "
             "Foam, bubble wrap, cotton wool, newspaper — the more air a "
             "material holds still, the better it does.",
             "Now look at what the thickness dial did. Every material "
             "improved when it went from one layer to three, and no material "
             "changed places. Those are two separate findings and you could "
             "only get either of them by holding the other dial still — "
             "which is what makes this a fair test rather than eight "
             "unrelated readings.",
             "And every single beaker cooled. The best combination on the "
             "bench still lost nearly ten degrees in twenty minutes. "
             "Insulation slows a transfer down; nothing here stopped one.",
         ]},

        {"type": "key-fact", "ref": "slows-never-stops"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Insulation", "Trapped air", "Fair test", "Control"]},

        {"type": "misconception", "id": "think-commit-jumper",
         "anchor": "s-think", "targets": "ENER-15"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "slows-never-stops",
         "text": "An insulator adds no energy at all. It slows a transfer "
                 "down by being bad at carrying it, and almost every good "
                 "one works by holding a lot of air still. Nothing on the "
                 "bench stopped a transfer — every beaker cooled.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Insulation",
         "definition": "A material used to slow a thermal transfer down.",
         "note": "It adds nothing and it stops nothing. It only makes the "
                 "route out a bad one."},
        {"term": "Trapped air",
         "definition": "Air held still in small pockets inside a material.",
         "note": "The real insulator in wool, foam, feathers, bubble wrap "
                 "and a double-glazed window. Let the air move and it works "
                 "far worse."},
        {"term": "Fair test",
         "definition": "A test in which you change one thing and keep "
                       "everything else the same.",
         "note": "Change two and you cannot say which of them caused the "
                 "difference."},
        {"term": "Control",
         "definition": "The run with nothing done to it, kept for "
                       "comparison.",
         "note": "The bare beaker. Without it, 62.7 degrees is a number "
                 "with nothing to be better than."},
    ],

    "activities": [
        {"id": "think-commit-jumper",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-15",
         "prompt": "You wrap a jumper tightly round a bottle of water "
                   "straight out of the fridge and leave it on the table for "
                   "an hour. Commit before you read on.",
         "options": [
             "The water will be warmer than it would have been without the "
             "jumper",
             "The water will be cooler, because the jumper takes warmth away",
             "The water will be colder than it would have been without the "
             "jumper",
             "The water will still be cold, because the jumper slows the "
             "transfer both ways",
         ],
         "reveal": [
             "It will still be cold. The jumper has no warmth of its own to "
             "give — it is at room temperature and nothing about it is a "
             "source. What it does is make the route between the room and "
             "the bottle a bad one, and a bad route is a bad route in both "
             "directions.",
             "This is what \"a jumper keeps you warm\" is actually saying, "
             "and the sentence hides it. You are the source. Your own "
             "thermal store is being topped up all day by the food you have "
             "eaten, and the jumper's only job is to be bad at letting it "
             "out. Put the same jumper on a snowman and the snowman lasts "
             "<em>longer</em> — which is the experiment that settles it, and "
             "which surprises almost everyone.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "What does most of the insulating in a woollen jumper?",
            "options": [
                "The wool fibres themselves",
                "The dye, which reflects warmth back",
                "The air trapped between the fibres",
                "The thickness of the thread",
            ],
            "answer": 2,
            "feedback": {
                0: "The fibres hold the air in place, but the air is what "
                   "carries the transfer badly. Squash the same wool flat "
                   "and it insulates far worse with the same fibres in it.",
                1: "Dye makes no measurable difference. A white jumper and a "
                   "black one of the same thickness keep you equally warm.",
                3: "A thicker thread packed tight can hold LESS air than a "
                   "fine one loosely knitted, and it insulates worse.",
            }},
        "apply": {
            "q": "In the bench test, cotton wool at 3 layers finished at "
                 "64.4 °C and bubble wrap at 1 layer finished at 59.4 °C. "
                 "What can you conclude from that pair on its own?",
            "options": [
                "Cotton wool is a better insulator than bubble wrap",
                "Nothing about which material is better, because two things "
                "were different",
                "Bubble wrap is a better insulator than cotton wool",
                "Thickness makes no difference to either material",
            ],
            "answer": 1,
            "feedback": {
                0: "The cotton wool was also three times as thick. You "
                   "cannot tell whether the material or the thickness caused "
                   "the difference.",
                2: "It is the right answer to a different comparison — at "
                   "the SAME thickness bubble wrap does beat cotton wool. "
                   "This pair cannot show it.",
                3: "Every material on the bench improved with thickness, and "
                   "this pair does not test that at all.",
            }},
        "explain": {
            "q": "A student says the foam lagging \"kept the heat in\". "
                 "Rewrite that as an accurate sentence, and explain why the "
                 "bare beaker had to be on the bench at the same time.",
            "field_label": "Your rewrite, then the control",
            "placeholder": "The foam did not keep anything in; it…",
            "success": [
                "Says the foam slowed the transfer rather than stopping it.",
                "Says the wrapped beaker still cooled — by about 17 degrees.",
                "Says the foam adds no energy of its own.",
                "Says the bare beaker shows what happens with no lagging at "
                "all.",
                "Says that without the control there is nothing to compare "
                "the reading with.",
            ]},
        "produce": {
            "q": "A company claims its new lagging \"keeps a hot water tank "
                 "hot for ever\". Design a test that would show whether the "
                 "claim is true, say what result would prove it false, and "
                 "explain why you already know what the result will be.",
            "field_label": "Your test and your prediction",
            "placeholder": "I would fill two identical tanks…",
            "success": [
                "Uses identical tanks, the same starting temperature and the "
                "same room.",
                "Includes an unlagged control.",
                "Measures temperature repeatedly over a long time, not once.",
                "Says the claim is false as soon as the lagged tank's "
                "temperature falls at all.",
                "Explains that a transfer runs whenever there is a "
                "temperature difference, so it can only stop when the tank "
                "reaches room temperature.",
            ]},
    },

    "key_note": "An insulator adds nothing and stops nothing. It slows a "
                "thermal transfer by being bad at carrying it, usually by "
                "holding air still in small pockets — and it works in both "
                "directions, which is why a jumper keeps a snowman as well "
                "as it keeps you.",

    "stretch": [
        {"type": "explainer", "id": "the-three-at-once",
         "text": "A real vacuum flask has to beat all the routes at once, "
                 "and it uses a different trick for each. Two glass walls "
                 "with the air pumped out between them: conduction has no "
                 "particles to work with, so it is zero. Both facing "
                 "surfaces silvered: radiation is reflected back rather than "
                 "given off, which is p1-06's polished-silver face doing its "
                 "job. A plastic stopper: the hot liquid itself cannot get "
                 "out, and plastic conducts badly where the two walls have "
                 "to meet. Three problems, three answers, and the flask "
                 "still goes cold eventually — because the glass rim has to "
                 "join somewhere, and no route is ever quite zero."},
    ],

    "support": [],

    "safety_note": "Water at 80 °C will scald. Beakers of it are carried one "
                   "at a time and never over anyone's hands.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a jumper keeps a snowman cold?",
              "cta": "Ask about this lesson",
              "anchor": "s-lag"},

    "ks4_becomes": "Thermal conductivity and thickness used quantitatively, "
                   "and the design of buildings for low energy use.",

    "ws": ["experimental-skills-and-investigations", "measurement",
           "analysis-and-evaluation"],

    "review_state": "draft",
}
