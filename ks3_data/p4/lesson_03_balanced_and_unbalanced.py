"""P4 L3 — Balanced and unbalanced (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-03-balanced-and-unbalanced.dc.html`.

Her page wins outright. The two identical books, the support rig, the two
panels, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A BEAM, AND THE PAGE SAYS WHY ────────────────────────

`upward force = weight` is an EQUALITY and `resultant = weight − upward
force` is a DIFFERENCE. Neither is a product, so neither takes a triangle,
and Design writes the reason into the block: *"This is a beam and not a
triangle, because the two forces are being subtracted from one another,
never multiplied."*

── ⚖️ RULED · THE SHEET OF PAPER'S 2 N BREAKING POINT IS MADE UP ─────

Design's flag 4 asks for a ruling and it is hers. The number is invented,
it is declared invented in the foot line, and it exists so that
UNBALANCED is a state a student can reach on a support that is not simply
absent. Without it the only route to a leftover force is removing the
support entirely, which teaches that unbalanced means unsupported — the
exact opposite of the lesson. A real sheet of 80 gsm A4 held at two edges
has no single failure figure, and putting one on the page would turn a
teaching threshold into a claim about paper.

── ⚖️ RULED · "AT REST AND STAYING AT REST" IS NOT TIDIED ────────────

Design's hedge, and it is load-bearing. *At rest* alone is not enough: an
object momentarily at rest at the top of a throw is at rest and the forces
on it are NOT balanced — which is exactly `p4-04` rung 2. The full phrase
is in the formula step and stays there.

── ⚖️ RULED · "mass in kilograms × 10 N/kg", WRITTEN OUT, FOUR TIMES ─

In the hook, in the formula block, in the key note and in the foot line.
The misconception it exists to kill is that the weight in newtons is the
same number as the mass in kilograms, and a symbol would not kill it.
`FORCE-22` is that belief and rung 1's second option is it.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel, which is
what Design's `s.buildOpen` is set by.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-20  if something is not moving, there are no forces on it
    FORCE-21  balanced forces mean the object is stopped
    FORCE-22  weight in newtons is the same number as the mass in kilograms
    FORCE-23  a support pushes back only as hard as it is able to, not as
              hard as it needs to

`FORCE-23` is not in Design's proposed table. It arrived with rung 1's
fourth option — an 80 N upward force under a 40 N box — and it is the
belief the *Going further* layer answers: a surface stops squashing at the
point where the two are equal, which is why the answer is EXACTLY the
weight rather than approximately or generously.
"""

LESSON = {
    "slug":  "balanced-and-unbalanced",
    "title": "Balanced and unbalanced",
    "discipline": "physics",
    "unit": "Forces",
    "family": "CONTRAST",

    "covers": ["KS3.P.FORCES.02c", "KS3.P.BAL.01"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["drawing-and-adding-forces"],
    "assumes": [],
    "references": ["springs-and-hookes-law", "what-a-force-is"],
    "ks4_links": [],

    "meta_description": "Two identical books have the same weight pulling "
                        "them down. One sits on a table and one is falling. "
                        "The difference is not the weight — it is what is "
                        "pushing back.",

    "big_question": "Two identical books have the same weight pulling them "
                    "down. One is sitting on a table and one is falling. The "
                    "difference is not the weight.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two identical books", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "RIG",
         "label": "The support rig",     "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Beam and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The table is holding up 8 N and nobody notices.",
        "prompt": "A 0.8 kg book weighs about 8 N — mass in kilograms × "
                  "10 N/kg. Rest it on a table and it stays. Hold it out and "
                  "let go and it drops. Its weight was 8 N the whole time.",
        "commit": "So what is different about the forces on the book on the "
                  "table?",
        "options": [
            "The falling book has more weight than the same book resting "
            "on a table",
            "A second force pushes up on the resting book, exactly matching "
            "its weight",
            "The resting book has no forces acting on it at all while it "
            "stays still",
            "Gravity switches off as soon as something rests on a solid "
            "surface",
        ],
        "answer": 1,
        "reveal": "There is a second force. The table is squashed by an "
                  "amount too small to see and pushes back up with 8 N — "
                  "<strong>exactly matching the weight, so the resultant is "
                  "0 N and nothing changes.</strong> Take the table away and "
                  "the 8 N has nothing to cancel it.",
    },

    "misconceptions": [
        {"id": "FORCE-20",
         "statement": "If something is not moving, there are no forces on "
                      "it.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-21",
         "statement": "Balanced forces mean the object is stopped.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "FORCE-22",
         "statement": "Weight in newtons is the same number as the mass in "
                      "kilograms.",
         "elicited_by": "rig",
         "confronted_by": "s-ladder"},
        {"id": "FORCE-23",
         "statement": "A support pushes back as hard as it is able to, "
                      "rather than as hard as it needs to.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Balanced</strong> means the forces along a line add "
                 "up to a resultant of 0 N, so nothing about the motion "
                 "changes. <strong>Unbalanced</strong> means something is "
                 "left over, and whatever is left over is what changes the "
                 "motion."},

        # ── #s-bench · the support rig ─────────────────────────────────
        {"type": "support-rig",
         "id": "rig",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the support rig",
         "heading": "Change what is holding it up",
         "progress": "Change a control to begin",
         "g": 10,
         "scale": 3,
         "support_label": "What is holding it up",
         "start_support": "table",
         "gate": {
             "prompt": "Commit first. A 2 kg mass hangs from a spring and "
                       "stays still. How hard is the spring pulling up?",
             "options": [
                 "20 N — the same as the weight",
                 "More than 20 N, or it would not hold",
                 "2 N — the same as the mass",
                 "0 N — nothing is moving",
             ],
             "answer": 0,
         },
         "mass": {"label": "Mass", "min": 0.5, "max": 5,
                  "step": 0.5, "start": 2},
         # ⚖️ `cap: None` is "no limit within this bench's range", not
         # "infinitely strong" as a claim about tables. The renderer requires
         # the key so that an uncapped support is a decision rather than an
         # omission.
         "supports": [
             {"id": "table", "tab": "A table top", "shape": "solid",
              "word": "RESTING ON A TABLE TOP", "cap": None,
              "note": "The table top is squashed by a fraction of a "
                      "millimetre and pushes back with exactly {up} N. The "
                      "resultant is 0 N, so the load stays exactly where it "
                      "was put."},
             {"id": "spring", "tab": "A spring", "shape": "spring",
              "word": "HANGING FROM A SPRING", "cap": None,
              "note": "The spring stretches until its pull reaches {up} N "
                      "and then stops stretching. The resultant is 0 N, and "
                      "the load hangs in mid-air with nothing underneath "
                      "it."},
             {"id": "paper", "tab": "A sheet of paper", "shape": "sheet",
              "word": "RESTING ON A SHEET OF PAPER", "cap": 2, "tears": True,
              "note": "The paper gives way at about 2 N, so it can only push "
                      "up with {up} N against a weight of {weight} N. That "
                      "leaves {over} N over, downwards, and the load goes "
                      "through.",
              "note_ok": "The paper is bent but holding, pushing up with "
                         "{up} N. The resultant is 0 N — right up to the "
                         "point where the fibres give way."},
             {"id": "none", "tab": "Nothing — dropped", "shape": "none",
              "word": "NOTHING UNDERNEATH IT", "cap": 0,
              "note": "Nothing is pushing up at all, so the whole {weight} N "
                      "is left over, downwards. The resultant is {over} N "
                      "down, and the load falls — faster every second it "
                      "is falling."},
         ],
         "readouts": [
             {"id": "weight", "label": "Weight, pulling down"},
             {"id": "up", "label": "Push or pull, upwards"},
             {"id": "res", "label": "Resultant"},
             {"id": "verdict", "label": "Verdict"},
         ]},

        {"type": "formula",
         "id": "balance-rule",
         "eyebrow": "The relationship · a beam, not a triangle",
         "statement": "At rest and staying at rest: upward force = weight. "
                      "So the upward force is the weight, in newtons.",
         "support": [
             "weight in N = mass in kg × 10 N/kg",
             "balanced: resultant = 0 N",
             "unbalanced: resultant = bigger force − smaller force",
         ],
         "figure": {
             "art": "p4-balance-beam",
             # ⊕ PHASE 3, 25 Aug 2026 — Design's caption and note, restored.
             "caption": "Same length, opposite ways, nothing left over.",
             "note": "This is a beam and not a triangle, because the two "
                     "forces are being subtracted from one another, never "
                     "multiplied. Nothing here has a formula triangle, and "
                     "putting one on it would teach a relationship that "
                     "does not exist.",
             "aria_label": "Two panels drawn to one scale. On the left, an "
                           "upward arrow of 30 newtons and a downward arrow "
                           "of 30 newtons are the same length, and the "
                           "resultant is zero newtons. On the right, an "
                           "upward arrow of 15 newtons is half the length of "
                           "the 30 newton downward arrow, and a third arrow "
                           "shows 15 newtons left over, downwards.",
             "scale": 2.867,
             "panels": [
                 {"title": "BALANCED", "up": 30, "down": 30,
                  "verdict": "resultant 0 N"},
                 {"title": "UNBALANCED", "up": 15, "down": 30,
                  "verdict": "15 N left over, down"},
             ],
         }},

        {"type": "worked-example", "id": "cfifa-support-plain"},
        {"type": "worked-example", "id": "cfifa-support-convert"},
        {"type": "check", "id": "your-turn-support", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "balanced-means-no-change"},

        {"type": "misconception", "id": "think-not-moving-no-forces",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-support-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 3 kg toolbox rests on a shelf. How hard does the "
                    "shelf push up?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "3 kg stays 3 kg",
              "note": "The mass is already in kilograms, which is what × "
                      "10 N/kg needs, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "upward force = weight",
              "note": "It is at rest and staying at rest, so the two forces "
                      "are equal."},
             {"letter": "I", "label": "Insert",
              "line": "upward force = 3 kg × 10 N/kg",
              "note": "Weight in newtons is mass in kilograms × 10 N/kg."},
             {"letter": "F", "label": "Fine-tune",
              "line": "3 × 10 = 30",
              "note": "Kilograms times newtons per kilogram leaves newtons."},
             {"letter": "A", "label": "Answer",
              "line": "upward force = 30 N, upwards",
              "note": "Same size as the weight, opposite direction."},
         ]},

        {"id": "cfifa-support-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 250 g book rests on the same shelf. How hard does the "
                    "shelf push up?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own rig."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "250 g ÷ 1000 = 0.250 kg",
              "note": "× 10 N/kg wants kilograms, and a gram is a thousandth "
                      "of one, so divide by 1000."},
             {"letter": "F", "label": "Formula",
              "line": "upward force = weight",
              "note": "At rest and staying at rest, so the two forces are "
                      "equal."},
             {"letter": "I", "label": "Insert",
              "line": "upward force = 0.250 kg × 10 N/kg",
              "note": "The converted mass goes in. The 250 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "0.250 × 10 = 2.5",
              "note": "Kilograms times newtons per kilogram leaves newtons."},
             {"letter": "A", "label": "Answer",
              "line": "upward force = 2.5 N, upwards",
              "note": "Insert 250 instead of 0.250 and the shelf comes out "
                      "pushing a thousand times too hard."},
         ]},

        {"id": "your-turn-support",
         "kind": "p4-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The rig opens on the table top at 2.0 kg — a balanced state, so
         # the resting five lines are the `upward force = weight` branch.
         "rest": {"mass": "2.0", "supportword": "resting on a table top",
                  "formula": "upward force = weight",
                  "formulanote": "It is at rest and staying at rest, so the "
                                 "two are equal.",
                  "insert": "upward force = 2.0 kg × 10 N/kg",
                  "finetune": "2.0 × 10 = 20",
                  "answer": "upward force = 20 N, upwards",
                  "answernote": "And the resultant is 0 N, which is why "
                                "nothing happens.",
                  "target": 20},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your rig: {mass} kg, {supportword}.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own rig is showing — and which "
                      "relationship you need depends on whether it balances.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{mass} kg stays {mass} kg",
                   "note": "The mass is already in kilograms, which is what "
                           "× 10 N/kg needs, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "{formula}",
                   "note": "{formulanote}"},
                  {"letter": "I", "label": "Insert",
                   "line": "{insert}",
                   "note": "Weight in newtons is mass in kilograms × "
                           "10 N/kg."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{finetune}",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "{answer}",
                   "note": "{answernote}"},
              ],
              "close": "The five lines give {target} N, and the arrows on "
                       "the rig are drawn to match."},
             {"id": "q2", "tab": "Question 2",
              "head": "A 400 g mug sits still on a table. How hard does the "
                      "table push up?",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "400 g ÷ 1000 = 0.400 kg",
                   "note": "× 10 N/kg wants kilograms, so divide the grams "
                           "by 1000."},
                  {"letter": "F", "label": "Formula",
                   "line": "upward force = weight",
                   "note": "Still and staying still, so the two forces are "
                           "equal."},
                  {"letter": "I", "label": "Insert",
                   "line": "upward force = 0.400 kg × 10 N/kg",
                   "note": "The converted mass goes in. The 400 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "0.400 × 10 = 4",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "upward force = 4 N, upwards",
                   "note": "Insert 400 instead of 0.400 and the table comes "
                           "out pushing with 4000 N."},
              ],
              "close": "The five lines give 4 N upwards. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-not-moving-no-forces",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-20",
         "statements": [
             {"quote": "If something is not moving, there are no forces on "
                       "it.",
              "targets": "FORCE-20",
              "body": [
                  "A resultant of 0 N and no forces at all look identical "
                  "from a distance, and they are completely different "
                  "situations. Hang a heavier and heavier load from a rope "
                  "and nothing appears to happen — until the rope snaps, "
                  "which is not something that happens to an object with no "
                  "forces on it. Every bridge, chair and shelf you have ever "
                  "used is holding a load in balance, and every one of them "
                  "has a load it cannot hold. <strong>The forces are there; "
                  "they are cancelling.</strong>",
              ]},
             {"quote": "Balanced forces mean the object is stopped.",
              "targets": "FORCE-21",
              "body": [
                  "Balanced means <em>no change</em>, not <em>no "
                  "motion</em>. A car at a steady 70 miles an hour on a "
                  "motorway has a resultant force of 0 N: the engine's "
                  "forward push exactly matches the air resistance and "
                  "friction pushing back. Take your foot off the accelerator "
                  "and the forces stop being balanced, and the car slows. A "
                  "skydiver at terminal velocity is falling at a constant 55 "
                  "metres per second with balanced forces. <strong>Balanced "
                  "forces are the reason things carry on doing whatever they "
                  "were doing</strong>, which is the whole subject of the "
                  "next lesson.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "balanced-means-no-change",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Balanced forces give a resultant of 0 N, so nothing about "
                 "the motion changes — which is why a stretched spring or "
                 "a squashed surface holding something at rest must be "
                 "pushing back with exactly the weight, in newtons."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A 4 kg box sits still on a bench. What is the upward force "
                 "from the bench?",
            "options": [
                "40 N upwards",
                "4 N upwards",
                "0 N — it is not moving, so no force is needed",
                "80 N upwards",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the mass in kilograms, not the weight. Multiply "
                   "by 10 N/kg to get newtons.",
                2: "The resultant is 0 N, which is not the same as the bench "
                   "doing nothing. Remove the bench and the box falls.",
                3: "That would leave 40 N over, upwards, and the box would "
                   "lift off the bench. The upward force matches the weight "
                   "exactly.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A lorry is driving along a motorway at a steady 25 m/s. "
                 "What can you say about the forces on it?",
            "options": [
                "They are unbalanced forwards, because it is moving "
                "forwards.",
                "They are balanced, because its motion is not changing.",
                "Only the engine is acting, because the lorry is winning.",
                "They must be balanced, because balanced forces always mean "
                "stopped.",
            ],
            "answer": 1,
            "feedback": {
                0: "Movement does not need a resultant force; changing "
                   "movement does. Steady speed in a straight line means "
                   "balanced forces.",
                2: "Air resistance and friction are both acting the whole "
                   "time. At a steady speed the engine’s push matches "
                   "them exactly.",
                3: "The verdict is right and the reason is wrong. Balanced "
                   "means no change, and a lorry at a steady speed is not "
                   "changing.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A 2 kg bag of flour hangs from a spring and does not move. "
                 "Explain, using both forces, why the spring stops "
                 "stretching where it does.",
            "field_label": "Your explanation",
            "placeholder": "The weight of the bag is…",
            "success": [
                "Gives the weight as 20 N, using mass × 10 N/kg.",
                "Says the spring pulls upwards on the bag.",
                "Says the spring stretches further, and pulls harder, as it "
                "stretches.",
                "Says it stops stretching when its pull reaches 20 N.",
                "Says the resultant is then 0 N, so the bag stays where it "
                "is.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A lift with a total mass of 500 kg hangs from a cable. The "
                 "cable can pull with up to 6 000 N. Work out whether the "
                 "lift is safe at rest, and explain what would have to "
                 "happen to the forces for the lift to start moving upwards.",
            "field_label": "Your answer",
            "placeholder": "The weight of the lift is…",
            "success": [
                "Gives the weight as 5 000 N, using 500 × 10 N/kg.",
                "Says the cable only needs to pull with 5 000 N to hold it "
                "at rest, which is within its limit.",
                "Says at rest the resultant is 0 N and the forces are "
                "balanced.",
                "Says the cable would have to pull with more than 5 000 N "
                "for the lift to start moving up.",
                "Says the resultant would then be upwards, and gives a "
                "figure such as 5 200 N giving 200 N upwards.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Forces on an object are balanced when they cancel to a "
                "resultant of 0 N, and unbalanced when something is left "
                "over. Anything held at rest by a spring or a surface is in "
                "balance, so the upward force must equal the weight — mass "
                "in kilograms × 10 N/kg. Balanced does not mean stationary; "
                "it means nothing is changing.",

    "stretch": [
        {"id": "how-a-table-knows",
         "type": "explainer",
         "text": "How does a table know how hard to push? It does not, and "
                 "it does not need to. Every solid is a lattice of particles "
                 "held together by forces that behave like tiny stiff "
                 "springs. Put a book on the table and the top layer of "
                 "particles is pushed a little closer to the layer below "
                 "— a squash far too small to see, but real — and "
                 "squashed springs push back. Add more load and they squash "
                 "further and push back harder, and this continues "
                 "automatically until the push matches the load. "
                 "<strong>That is why the answer is always <em>exactly</em> "
                 "the weight rather than approximately</strong>: the surface "
                 "stops squashing at the point where the two are equal, and "
                 "stays there. It is the same mechanism as the spring in the "
                 "bench above, with a much shorter stretch."},
        {"id": "why-every-support-breaks",
         "type": "explainer",
         "text": "It also explains why every support has a breaking point. "
                 "Squash those particle springs far enough and the lattice "
                 "fails — the paper tears, the shelf snaps, the ice gives "
                 "way — and beyond that point the surface cannot supply "
                 "the force needed, so the forces stop being balanced and "
                 "the load goes through. Engineers do not design a bridge to "
                 "be strong; they design it so that the largest load it will "
                 "ever carry still leaves it in balance, with a margin. A "
                 "structure that is in balance is doing its job, silently, "
                 "and the failure is what happens when the arithmetic runs "
                 "out."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "balanced forces",
         "definition": "Forces that add up to a resultant of 0 N. Nothing "
                       "about the motion changes — which is not the same "
                       "as nothing moving."},
        {"term": "unbalanced forces",
         "definition": "Forces that leave something over. Whatever is left "
                       "over is what changes the motion."},
        {"term": "weight",
         "definition": "The force of gravity on an object, in newtons. At "
                       "KS3 it is taken as mass in kilograms × 10 N/kg."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure whether a situation counts as balanced?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Resultant forces, equilibrium, Newton's first law, and "
                   "terminal velocity.",

    "convention_note": "Weight in newtons is taken as mass in kilograms × "
                       "10 N/kg throughout. The support rig shows only the "
                       "vertical forces, and the sheet of paper is given a "
                       "made-up breaking point of 2 N so that failure is "
                       "something you can reach; a real sheet depends on its "
                       "size, its fibres and how it is held.",

    "ws": [],
}
