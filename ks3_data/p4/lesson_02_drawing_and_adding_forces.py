"""P4 L2 — Drawing and adding forces (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-02-drawing-and-adding-forces.dc.html`.

Her page wins outright. The tug of war, the sledge on ice, the three-bar
beam, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A BEAM, AND THE ARITHMETIC IS CHECKED ────────────────

`resultant = bigger pull − smaller pull` is a DIFFERENCE. `A = B × C`
does not hold, so there is no triangle here and putting one over it would
teach a relationship that does not exist. Design draws three aligned bars
and says so on the face of the block: *"That is why this relationship gets
a beam and not a triangle: nothing here is being multiplied."*

The bars are 700 px for 40 N, 437 px for 25 N and 263 px for 15 N, and
**437 + 263 = 700 exactly**. `_resultant_beam` derives the widths from the
authored newtons at one scale and REFUSES a payload whose parts do not sum
to the whole, so a bar model that lies cannot be authored here.

── ⚖️ RULED · ONE PX-PER-NEWTON SCALE ACROSS THE WHOLE BENCH ─────────

Design's `SCALE` is `380 / 60` — 6.33 px per newton — and the resultant
arrow is drawn on the SAME scale as the two pulls, on its own baseline.
This is not a drawing convenience: the lesson's own second misconception
is *"arrows should be drawn the same length so it looks tidy"*, and a
bench that scaled its arrows to fit would be committing the error the
block below it marks wrong.

── ⚖️ RULED · THE EQUAL STATE DRAWS NO ARROW AND PRINTS `0 N` ────────

A zero-length arrow is not a small arrow. Set both ropes to 30 N — which
is exactly what the commit gate asks about — and Design draws nothing on
the resultant baseline and writes *"no arrow to draw · 0 N"*. The tile
reads *"0 N — nothing left over"*, and the note is careful to add that
both ropes are still under 30 N of tension: a resultant of 0 N and no
forces at all look identical from outside, which is `p4-03`'s whole hook.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

⚠️ **MRB-208 · THE `s-formula` ID GOES ON THE ATTEMPT PANEL, NOT ON THE
FORMULA.** Design's `DONE` reads `if (id === 's-formula') return
s.buildOpen`, and `buildOpen` is set by the CFIFA's *Check my five lines*.
A `formula` block carries no demand and emits no `data-stage-done`, so
anchoring the stop there would make a stop that can never become true.

── ⚖️ FIVE MISCONCEPTIONS FROM FOUR OF DESIGN'S ──────────────────────

    FORCE-16  the bigger arrow wins, so it moves at the bigger force
    FORCE-17  arrows should all be drawn the same length
    FORCE-18  forces along a line always add up
    FORCE-19  equal opposite forces cancel out and stop existing

`FORCE-19` is not in Design's proposed table. It arrived with rung 2's
fourth option — *"the two forces cancel out and stop existing"* — and it
is genuinely separate from `FORCE-18`: a student can be perfectly sound
that opposite forces subtract and still think the forces themselves have
gone. The correction says both are still acting and both would still break
something.

── ⚠️ THE HEDGE IN `#s-think` IS LOAD-BEARING ───────────────────────

*"Change the sledge for a heavier one and the same 15 N produces less of a
change"* is a hint about `p4-04`, and it is phrased as a hint rather than
a claim because mass is not taught in this unit. Tidying it into a rule
would import `F = ma` into a lesson that does not have it.
"""

LESSON = {
    "slug":  "drawing-and-adding-forces",
    "title": "Drawing and adding forces",
    "discipline": "physics",
    "unit": "Forces",
    "family": "MODEL",

    # ⚠️ FORCES.02 is split at the clause across p4-02 and p4-03. See the
    # package docstring: the register has no sub-index for a clause and
    # nothing here invents one.
    "covers": ["KS3.P.FORCES.02a", "KS3.P.FORCES.02b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["what-a-force-is"],
    "assumes": [],
    "references": ["moments", "pressure-force-over-area"],
    "ks4_links": [],

    "meta_description": "A sledge pulled 40 N one way and 25 N the other. "
                        "One single arrow does the job of both — 15 N to the "
                        "right. Set two pulls on the bench and read the "
                        "arrow the sledge actually responds to.",

    "big_question": "A sledge is pulled one way with 40 N and the other way "
                    "with 25 N. One single arrow does the job of both. How "
                    "long is it, and which way does it point?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Tug of war",         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "SLEDGE",
         "label": "Sledge on ice",      "done_when": "gate_and_a_slider"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Beam and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two pulls, one rope, and the winner is a subtraction.",
        "prompt": "In a tug of war the rope does not care how many people "
                  "are holding it. It moves according to one number: how "
                  "much more one side is pulling than the other.",
        "commit": "A sledge is pulled right with 40 N and left with 25 N. "
                  "What single force would have exactly the same effect?",
        "options": [
            "65 N to the right",
            "15 N to the right",
            "15 N to the left",
            "40 N to the right",
        ],
        "answer": 1,
        "reveal": "15 N to the right. The 25 N pull cancels 25 N of the 40 N "
                  "pull, and what is left over is the only thing the sledge "
                  "responds to. That leftover has a name: the "
                  "<strong>resultant force</strong>.",
    },

    "misconceptions": [
        {"id": "FORCE-16",
         "statement": "The bigger arrow wins, so the object moves at the "
                      "bigger force.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-17",
         "statement": "Force arrows should all be drawn the same length.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "FORCE-18",
         "statement": "Forces along a line always add up.",
         "elicited_by": "sledge",
         "confronted_by": "sledge"},
        {"id": "FORCE-19",
         "statement": "Equal and opposite forces cancel out and stop "
                      "existing.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An arrow is how a force gets written down. Where it starts "
                 "says which object is being pushed or pulled, which way it "
                 "points says the direction, and its length says the size "
                 "— so <strong>two arrows drawn the same length are "
                 "claiming two forces are equal</strong>."},

        # ── #s-bench · the sledge on ice ───────────────────────────────
        {"type": "resultant-bench",
         "id": "sledge",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the sledge on ice",
         "heading": "Set two pulls. Read one arrow.",
         "progress": "Set a pull to begin",
         # 380 px for the largest 60 N reading, exactly as Design draws it.
         "scale": 380.0 / 60.0,
         "body_label": "Sledge",
         "base_label": "ONE ARROW INSTEAD OF TWO",
         "zero_label": "no arrow to draw · 0 N",
         "gate": {
             "prompt": "Commit first. You set both pulls to 30 N. What does "
                       "the single arrow look like?",
             "options": [
                 "A 60 N arrow, because the pulls add up",
                 "No arrow at all — the resultant is 0 N",
                 "A 30 N arrow, because one of them wins",
                 "Two arrows, because there is no single one",
             ],
             "answer": 1,
         },
         "sliders": [
             {"id": "right", "label": "Pull to the right",
              "min": 0, "max": 60, "step": 5, "start": 40},
             {"id": "left", "label": "Pull to the left",
              "min": 0, "max": 60, "step": 5, "start": 25},
         ],
         "readouts": [
             {"id": "right", "label": "Pull to the right"},
             {"id": "left", "label": "Pull to the left"},
             {"id": "res", "label": "Resultant force"},
         ],
         # ⚖️ FIVE BRANCHES, KEYED TO WHICH SLIDER IS NON-ZERO. Not to the
         # numbers: the both-zero state and the equal state are different
         # facts, and both are states a student will leave the bench in.
         "branches": {
             "both_zero": "Both ropes are slack, so there is nothing to draw "
                          "and nothing to work out. A resultant of 0 N and "
                          "no forces at all look identical from the outside "
                          "— which is exactly why the next lesson exists.",
             "right_only": "One rope only, so the single arrow is that "
                           "arrow: {right} N to the right. With nothing "
                           "pulling back, there is nothing to subtract.",
             "left_only": "One rope only, so the single arrow is that arrow: "
                          "{left} N to the left. With nothing pulling back, "
                          "there is nothing to subtract.",
             "equal": "The two arrows are the same length and point opposite "
                      "ways, so the single arrow has no length at all. The "
                      "resultant is 0 N, and both ropes are still under "
                      "{right} N of tension.",
             "unequal": "The longer arrow is {big} N and the shorter one is "
                        "{small} N, so {small} N of the bigger pull is "
                        "cancelled. The single arrow is {diff} N to the "
                        "{dir}.",
         }},

        # ── #s-formula · the beam, then CFIFA, then the student's turn ──
        # ⚠️ NO ANCHOR ON THE FORMULA — MRB-208. See the module note.
        {"type": "formula",
         "id": "resultant-rule",
         "eyebrow": "The relationship · a beam, not a triangle",
         "statement": "Along one line, opposite ways: resultant = bigger "
                      "force − smaller force, pointing the way of the "
                      "bigger one.",
         "support": [
             "Same way along the line: add them.",
             "Opposite ways along the line: subtract.",
             "Every force, and the resultant, is in newtons (N).",
         ],
         "figure": {
             "art": "p4-resultant-beam",
             # ⊕ PHASE 3, 25 Aug 2026. Design writes one line above the beam
             # and one below it, and both were being dropped: the drawer
             # took no `caption` or `note` and `r_formula_figure` emitted
             # only the SVG. The lower one is MRB-204's own argument — the
             # page asserted a beam and never said why.
             "caption": "Two pulls the opposite way: one cancels part of "
                        "the other.",
             "note": "The two lower bars fill the top one exactly, because "
                     "25 N and 15 N make 40 N. That is why this "
                     "relationship gets a beam and not a triangle: nothing "
                     "here is being multiplied.",
             "aria_label": "Three bars, drawn to the same scale. The top bar "
                           "is a 40 newton pull to the right. Under it a 25 "
                           "newton bar points left and reaches only part of "
                           "the way, and the remaining length is a 15 newton "
                           "bar pointing right. The two lower bars together "
                           "make the length of the top one.",
             "whole": {"label": "PULL RIGHT", "newtons": 40, "dir": "right"},
             "parts": [
                 {"label": "PULL LEFT", "newtons": 25, "dir": "left"},
                 {"label": "LEFT OVER", "newtons": 15, "dir": "right"},
             ],
         }},

        {"type": "worked-example", "id": "cfifa-resultant-plain"},
        {"type": "worked-example", "id": "cfifa-resultant-convert"},
        # ⚠️ MRB-208 — THE RAIL STOP LANDS HERE, on the block that carries
        # the demand. Design's `s-formula` done-expression is `s.buildOpen`,
        # which is set by this panel's Check button and by nothing else.
        {"type": "check", "id": "your-turn-resultant",
         "anchor": "s-formula"},

        {"type": "key-fact", "ref": "arrow-length-is-the-size"},

        {"type": "misconception", "id": "think-bigger-pull-wins",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-resultant-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "40 N right, 25 N left. Find the resultant.",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "40 N stays 40 N · 25 N stays 25 N",
              "note": "Both pulls are already in newtons, so there is "
                      "nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "resultant = bigger pull − smaller pull",
              "note": "The two pulls are along one line and point opposite "
                      "ways."},
             {"letter": "I", "label": "Insert",
              "line": "resultant = 40 N − 25 N",
              "note": "Bigger first, so the subtraction cannot come out "
                      "negative."},
             {"letter": "F", "label": "Fine-tune",
              "line": "40 − 25 = 15",
              "note": "Subtract, and keep the direction of the bigger pull."},
             {"letter": "A", "label": "Answer",
              "line": "resultant = 15 N to the right",
              "note": "Size, unit and direction. Fifteen on its own is not "
                      "an answer."},
         ]},

        {"id": "cfifa-resultant-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A tug pulls right with 1.2 kN. A second pulls left with "
                    "400 N.",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own bench."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.2 kN × 1000 = 1200 N",
              "note": "A kilonewton is a thousand newtons, and two pulls "
                      "cannot be compared until they share a unit."},
             {"letter": "F", "label": "Formula",
              "line": "resultant = bigger pull − smaller pull",
              "note": "Still one line, still opposite ways."},
             {"letter": "I", "label": "Insert",
              "line": "resultant = 1200 N − 400 N",
              "note": "The converted pull goes in. The 1.2 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1200 − 400 = 800",
              "note": "Newtons take away newtons, so the answer is in "
                      "newtons."},
             {"letter": "A", "label": "Answer",
              "line": "resultant = 800 N to the right",
              "note": "Subtract 400 from 1.2 and the resultant comes out "
                      "pointing the wrong way."},
         ]},

        # ⚖️ Question 1 is LIVE on the bench. `{right}`, `{left}`, `{big}`,
        # `{small}`, `{diff}` and `{dir}` are filled by `wireResultantBench`
        # from the same state the readouts use, so the five lines can never
        # contradict the arrows above them.
        {"id": "your-turn-resultant",
         "kind": "p4-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The sledge opens at 40 N right against 25 N left, so the resting
         # bytes read 15 N to the right — which is also the hook's answer.
         "rest": {"right": 40, "left": 25, "big": 40, "small": 25,
                  "diff": 15, "dir": "to the right"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your bench: {right} N to the right, {left} N to the "
                      "left.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own sledge is showing.",
              "blocked_lead": "Both ropes are slack. Set a pull above zero "
                              "and the five lines come back.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{right} N stays {right} N · {left} N stays "
                           "{left} N",
                   "note": "Both pulls are already in newtons, so there is "
                           "nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "resultant = bigger pull − smaller pull",
                   "note": "Opposite ways along one line, so subtract."},
                  {"letter": "I", "label": "Insert",
                   "line": "resultant = {big} N − {small} N",
                   "note": "Both pulls are in newtons already."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{big} − {small} = {diff}",
                   "note": "Keep the direction of the bigger pull."},
                  {"letter": "A", "label": "Answer",
                   "line": "resultant = {diff} N {dir}",
                   "note": "Size, unit and direction, all three."},
              ],
              "close": "The five lines give {diff} N {dir}, and the arrow on "
                       "the bench is drawn that length."},
             {"id": "q2", "tab": "Question 2",
              "head": "A trolley is pushed right with 2.5 kN while a rope "
                      "drags it left with 900 N.",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "2.5 kN × 1000 = 2500 N",
                   "note": "A kilonewton is a thousand newtons, so multiply "
                           "by 1000 before comparing the two."},
                  {"letter": "F", "label": "Formula",
                   "line": "resultant = bigger pull − smaller pull",
                   "note": "One line, two opposite directions."},
                  {"letter": "I", "label": "Insert",
                   "line": "resultant = 2500 N − 900 N",
                   "note": "The converted push goes in. The 2.5 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "2500 − 900 = 1600",
                   "note": "Newtons take away newtons, so the answer is in "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "resultant = 1600 N to the right",
                   "note": "Work with 2.5 instead of 2500 and the resultant "
                           "comes out pointing left."},
              ],
              "close": "The five lines give 1600 N to the right. The whole "
                       "question turned on the first one."},
         ]},

        {"id": "think-bigger-pull-wins",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-16",
         "statements": [
             {"quote": "The bigger pull wins, so the sledge goes at 40 N.",
              "targets": "FORCE-16",
              "body": [
                  "Two different things are being run together here. The "
                  "40 N pull does win, in the sense that the sledge ends up "
                  "going that way — but the sledge does not respond to "
                  "40 N, it responds to 15 N, because 25 N of that pull is "
                  "being cancelled by the other rope. And a force is not a "
                  "speed: 15 N does not tell you how fast the sledge goes, "
                  "only how hard it is being pushed along. Change the sledge "
                  "for a heavier one and the same 15 N produces less of a "
                  "change, which is a hint about the next lesson.",
              ]},
             {"quote": "Arrows on a diagram should be drawn the same length "
                       "so it looks tidy.",
              "targets": "FORCE-17",
              "body": [
                  "A force arrow is a measurement, not a decoration. Two "
                  "arrows of the same length are a claim that the two forces "
                  "are equal, and if they are not equal you have drawn "
                  "something false — the diagram now says the sledge is "
                  "going nowhere. <strong>Draw the bigger force longer, "
                  "always, and label both with their size in newtons</strong> "
                  "so the reader is not left estimating from your drawing. "
                  "This is why examiners can mark a diagram wrong even when "
                  "the words beside it are right.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "arrow-length-is-the-size",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An arrow's length is the size of the force and its "
                 "direction is the direction of the force. Forces along one "
                 "line add if they point the same way and subtract if they "
                 "point opposite ways, and the single force left over — "
                 "the resultant — is in newtons with a direction."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A box is pushed forwards with 90 N while friction pushes "
                 "backwards with 34 N. What is the resultant force?",
            "options": [
                "124 N forwards",
                "56 N backwards",
                "56 N forwards",
                "90 N forwards",
            ],
            "answer": 2,
            "feedback": {
                0: "That is 90 + 34. Adding is for forces pointing the same "
                   "way; these point opposite ways, so they subtract.",
                1: "The size is right and the direction is not. The "
                   "resultant always points the way of the bigger force, "
                   "which here is the 90 N push.",
                3: "The 34 N of friction does not disappear because it is "
                   "smaller. It cancels 34 N of the push before anything is "
                   "left over.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "Two arrows on a diagram are drawn the same length, one "
                 "pointing left and one pointing right. What does the "
                 "diagram say?",
            "options": [
                "The two forces are equal, so the object moves steadily in "
                "the direction of the right-hand arrow.",
                "Arrow length is just for tidiness, so the sizes could be "
                "anything.",
                "The two forces cancel out and stop existing.",
                "The two forces are equal in size, so the resultant force is "
                "0 N.",
            ],
            "answer": 3,
            "feedback": {
                0: "Nothing is left over to move it. Equal opposite arrows "
                   "mean a resultant of 0 N, and the arrow on the right is "
                   "fully cancelled.",
                1: "Length is the measurement. Drawing two unequal forces "
                   "the same length makes the diagram say something false.",
                2: "Both are still acting, and both would still break "
                   "something. It is the resultant that is 0 N, not the "
                   "forces.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A trolley is pulled forwards with 60 N and dragged "
                 "backwards by 20 N of friction. Describe the arrow diagram "
                 "you would draw for it, then give the resultant force.",
            "field_label": "Your description and answer",
            "placeholder": "I would draw an arrow…",
            "success": [
                "Both arrows start on the trolley.",
                "The forward arrow points forwards and the friction arrow "
                "points backwards.",
                "The forward arrow is drawn three times as long as the "
                "friction arrow.",
                "Both arrows are labelled with their size in newtons.",
                "Gives the resultant as 40 N forwards, with the unit and the "
                "direction.",
            ],
            "title": "Rung 3 · Draw and explain"},
        "produce": {
            "q": "A parachutist is falling. Gravity pulls down with 700 N "
                 "and the parachute pushes up with 700 N. Then the "
                 "parachutist pulls a cord and the parachute pushes up with "
                 "760 N instead. Work out the resultant force in each case "
                 "and say what changed.",
            "field_label": "Your answer",
            "placeholder": "In the first case the resultant is…",
            "success": [
                "First case: resultant = 700 − 700 = 0 N.",
                "Second case: resultant = 760 − 700 = 60 N upwards.",
                "Says the direction of the resultant is upwards in the "
                "second case, using the direction of the bigger force.",
                "Says the parachutist is still falling in the second case, "
                "and slowing down.",
                "Does not claim a resultant of 0 N means no forces are "
                "acting.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Draw a force as an arrow: it starts on the object being "
                "pushed or pulled, points the way the force acts, and its "
                "length is the size in newtons. Along a single line, forces "
                "pointing the same way add and forces pointing opposite ways "
                "subtract. What is left over is the resultant force, and it "
                "is the only force the object responds to.",

    "stretch": [
        {"id": "three-forces-on-one-line",
         "type": "explainer",
         "text": "Three forces along one line are no harder than two: take "
                 "everything pointing right as positive, everything pointing "
                 "left as negative, and add them all up. A cyclist with "
                 "120 N of pedalling, 30 N of air resistance and 15 N of "
                 "friction has 120 − 30 − 15 = 75 N left over, forwards. "
                 "The same trick handles four forces, or ten. What it will "
                 "not handle is forces that are not along the same line — "
                 "a rope pulling upwards at an angle while gravity pulls "
                 "straight down. Adding those needs a method that is not "
                 "subtraction, and that method is GCSE work; at this stage "
                 "the honest answer is that the arrows tell you the answer "
                 "is somewhere between the two, and you leave it there."},
        {"id": "where-the-arrow-starts",
         "type": "explainer",
         "text": "One thing the arrow says that this lesson has not used: "
                 "<em>where</em> it starts. Two equal and opposite forces on "
                 "the same object, drawn at the same point, do nothing at "
                 "all. Draw the same two forces at opposite ends of a "
                 "steering wheel and the wheel turns, even though the "
                 "resultant is still zero. That is a second effect a force "
                 "can have, and it is why the arrow's starting point is part "
                 "of the diagram and not just a place to begin drawing."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "resultant force",
         "definition": "The single force that would have exactly the same "
                       "effect as all the forces acting. It is what is left "
                       "over once they have been added up."},
        {"term": "force arrow",
         "definition": "A drawn measurement. It starts on the object, points "
                       "the way the force acts, and its length is the size."},
        {"term": "kilonewton",
         "definition": "A thousand newtons, written kN. Two forces cannot be "
                       "compared until they are in the same unit."},
    ],

    "tutor": {
        "anchor": "s-formula",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check a diagram you have drawn?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Free-body diagrams, scale drawings and resolving forces "
                   "that are not along one line.",

    "convention_note": "The sledge on the bench is on ice: friction and air "
                       "resistance are left out so that only the two pulls "
                       "you set are acting along the line. The bars in the "
                       "beam are drawn to one scale, so equal lengths mean "
                       "equal newtons.",

    "ws": [],
}
