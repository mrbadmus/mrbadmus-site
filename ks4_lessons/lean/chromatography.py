# -*- coding: utf-8 -*-
"""Chromatography, in the lean shape. New record, no legacy page (it replaces the old
generate_site_v5 page). Spec table: ks4-chromatography.md (AQA 8464 5.8.1.3 / 8462 4.8.1.3, word for
word the same, Rf included on every route; no HT-only or chemistry-only lines).

The only route difference is the required practical's number: Required practical activity 12 in
8464 (CF CH, `notTriple`), Required practical 6 in 8462 (TF TH, `isTriple`). The method is the same.

The record carries one equation, EQ_RF (Rf = distance moved by substance ÷ distance moved by
solvent). The spec gives no symbols; d₁ and d₂ are named in full wherever they appear. Figure wanted:
fig:chromatogram (BRIEF-AN.md). The practice set reads the route's `quiz` list (K.bank):
quiz-chromatography.json, five per route, both old stems kept."""

_CFQ_PH = ["anything to convert?", "written out", "numbers in", "work it out", "with unit"]


def _q(lines, conv_ph=None):
    """A Ks4Cfifa question's five lines, in the shape gas_volumes.py uses."""
    letters = [("C", "Convert"), ("F", "Formula"), ("I", "Insert"), ("F", "Fine-tune"), ("A", "Answer")]
    ph = list(_CFQ_PH)
    if conv_ph:
        ph[0] = conv_ph
    return [{"letter": l, "label": lab, "placeholder": p, "line": ln}
            for (l, lab), p, ln in zip(letters, ph, lines)]


_METHOD = [
    "Investigate how paper chromatography can be used to separate and tell the difference between "
    "coloured substances. Calculate Rf values.",
    {"points": [
        "1. Draw a start line in pencil about 2\u00a0cm from the bottom of the chromatography paper.",
        "2. Put a small spot of each ink or food colouring on the start line.",
        "3. Stand the paper in a beaker with a little solvent, such as water. The solvent must be "
        "below the start line.",
        "4. Put a lid on the beaker. Leave it until the solvent has moved most of the way up the "
        "paper.",
        "5. Take the paper out and mark the solvent front in pencil straight away. Let it dry.",
        "6. Measure the distance from the start line to the solvent front, and to the centre of "
        "each spot. Calculate each Rf value.",
    ]},
]

LESSON = {
    "slug": "chromatography",
    "start": {
        "setup": "A spot of black felt-tip ink is put on a strip of paper. The bottom of the strip "
                 "stands in water, and the water soaks up past the spot.",
        "question": "If you had to guess, what happens to the black spot?",
        "options": [
            ("It stays as one black spot",
             "It splits into coloured spots. The black ink is a mixture of dyes, and each dye moves "
             "a different distance up the paper."),
            ("It splits into coloured spots",
             "It splits into coloured spots. The black ink is a mixture of dyes, and each dye moves "
             "a different distance up the paper."),
        ],
        "answer": 1,
    },
    "words": ["stationary phase", "mobile phase", "chromatogram", "Rf value"],
    "knowledge": [
        {"kind": "card", "title": "What chromatography does",
         "body": ["Chromatography can be used to separate mixtures and can give information to "
                  "help identify substances.",
                  "Paper chromatography separates the coloured substances in inks and food "
                  "colourings."]},
        {"kind": "card", "title": "Two phases",
         "body": ["Chromatography involves a stationary phase and a mobile phase.",
                  {"points": [
                      "The <strong>stationary phase</strong> does not move. In paper "
                      "chromatography it is the paper.",
                      "The <strong>mobile phase</strong> moves. In paper chromatography it is the "
                      "solvent, which soaks up the paper.",
                  ]},
                  "Separation depends on the distribution of substances between the phases."]},
        {"kind": "card", "title": "How paper chromatography separates a mixture",
         "body": [{"points": [
             "The solvent moves up the paper and dissolves the substances in the spot.",
             "Each substance is distributed differently between the paper and the solvent.",
             "A substance that spends more time dissolved in the solvent moves further up the "
             "paper.",
             "A substance that is more attracted to the paper moves a shorter distance.",
             "So the substances move different distances and separate into different spots.",
         ]}]},
        {"kind": "card", "title": "Reading a chromatogram",
         "body": ["The paper after the solvent has moved is called a chromatogram.",
                  {"slot": "fig:chromatogram"},
                  {"points": [
                      "The <strong>start line</strong> (origin) is where the spots were put.",
                      "The <strong>solvent front</strong> is how far the solvent moved.",
                      "Each spot is a different substance.",
                  ]}]},
        {"kind": "card", "title": "Rf value",
         "body": ["The ratio of the distance moved by a compound (centre of spot from origin) to "
                  "the distance moved by the solvent is its Rf value.",
                  {"slot": "triangle:EQ_RF"},
                  {"points": [
                      "Measure both distances from the start line, in the same unit.",
                      "Measure to the centre of the spot.",
                      "An Rf value has no unit. It is always less than 1, because a substance "
                      "cannot move further than the solvent.",
                      "Give the answer to a sensible number of significant figures: usually two, "
                      "like the distances you measured.",
                  ]}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Identifying a substance",
         "body": ["Different compounds have different Rf values in different solvents, which can "
                  "be used to help identify the compounds.",
                  "Run the unknown next to known substances on the same paper, in the same solvent. "
                  "A spot with the same Rf value and colour as a known substance is probably that "
                  "substance."]},
        {"kind": "card", "title": "Pure or a mixture",
         "body": ["The compounds in a mixture may separate into different spots depending on the "
                  "solvent, but a pure compound will produce a single spot in all solvents.",
                  "One spot in one solvent does not prove a substance is pure. Run it in two or "
                  "three different solvents. A single spot in every solvent suggests it is pure."]},
        {"kind": "card", "title": "Required practical 12", "routes": ["CF", "CH"],
         "body": _METHOD},
        {"kind": "card", "title": "Required practical 6", "routes": ["TF", "TH"],
         "body": _METHOD},
        {"kind": "reveal", "title": "Why each step is done",
         "cols": ["Reason"],
         "rows": [
             ("Start line in pencil", "Pencil does not dissolve in the solvent, so it does not "
                                      "run up the paper"),
             ("Solvent below the start line", "Otherwise the spots dissolve into the solvent in "
                                              "the beaker"),
             ("Lid on the beaker", "It stops the solvent evaporating"),
             ("Mark the solvent front at once", "The solvent evaporates, and then the front "
                                                "cannot be seen"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Rf = distance moved by solvent ÷ distance moved by substance.",
              "Rf = distance moved by substance ÷ distance moved by solvent. The answer is "
              "less than 1."),
             ("Measure to the top of the spot.",
              "Measure from the start line to the centre of the spot."),
             ("Draw the start line in ink.",
              "Draw it in pencil. Ink would dissolve and run up the paper."),
             ("One spot in one solvent proves a substance is pure.",
              "A pure compound gives a single spot in all solvents. Test it in more than one."),
         ]}]},
    ],
    "key_fact": "Chromatography separates a mixture because its substances are distributed "
                "differently between the stationary phase and the mobile phase, so they move "
                "different distances. Rf = distance moved by substance ÷ distance moved by "
                "solvent, and a pure compound produces a single spot in all solvents.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Pure substances shows another test for purity: melting and boiling points.",
                  "Formulations are mixtures, and chromatography can separate their coloured "
                  "components."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: write Rf = distance moved by substance ÷ distance "
             "moved by solvent, then the numbers, then the answer with no unit.",
             "<strong>Explain</strong> how it separates: the phases, the different distances, "
             "the different spots.",
             "<strong>Suggest</strong> how to show a substance is pure: run it in several "
             "solvents and look for one spot in each.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_RF": {"name": "Rf value",
                  "written": "Rf = distance moved by substance ÷ distance moved by solvent",
                  "source": "none",
                  "top": {"s": "d₁", "name": "distance moved by substance", "unit": "cm"},
                  "bottom": [{"s": "Rf", "name": "Rf value", "unit": "no unit"},
                             {"s": "d₂", "name": "distance moved by solvent", "unit": "cm"}]},
    },
    "cfifa": {
        "examples": [
            {"tab": "Rf from two distances", "eq": "EQ_RF", "find": "Rf",
             "next": "Now one with two different units.",
             "head": "A spot moves 3.6\u00a0cm from the start line. The solvent front is 8.0\u00a0cm from the "
                     "start line. Calculate the Rf value.",
             "steps": [["C", "Convert", "Nothing to convert: both distances are in cm."],
                       ["F", "Formula", "Rf = d₁ ÷ d₂"],
                       ["I", "Insert", "Rf = 3.6 ÷ 8.0"],
                       ["F", "Fine-tune", "Rf = 0.45"],
                       ["A", "Answer", "Rf = 0.45 (no unit)"]]},
            {"tab": "Convert first", "eq": "EQ_RF", "find": "Rf",
             "next": "Now the triangle the other way.",
             "head": "A spot moves 27\u00a0mm from the start line. The solvent front is 6.0\u00a0cm from the "
                     "start line. Calculate the Rf value.",
             "steps": [["C", "Convert", "6.0\u00a0cm × 10 = 60\u00a0mm",
                        "Both distances must be in the same unit."],
                       ["F", "Formula", "Rf = d₁ ÷ d₂"],
                       ["I", "Insert", "Rf = 27 ÷ 60"],
                       ["F", "Fine-tune", "Rf = 0.45"],
                       ["A", "Answer", "Rf = 0.45 (no unit)"]]},
            {"tab": "Distance from Rf", "eq": "EQ_RF", "find": "d₁",
             "next": "Now yours, below.",
             "head": "A dye has an Rf value of 0.60 in water. The solvent front moves 7.5\u00a0cm. "
                     "Calculate how far the dye moves.",
             "steps": [["C", "Convert", "Nothing to convert: the distance is in cm."],
                       ["F", "Formula", "d₁ = Rf × d₂"],
                       ["I", "Insert", "d₁ = 0.60 × 7.5"],
                       ["F", "Fine-tune", "d₁ = 4.5"],
                       ["A", "Answer", "The dye moves 4.5\u00a0cm"]]},
        ],
        "questions": [
            {"tab": "Question 1", "id": "rf-q1",
             "head": "A spot moves 2.4\u00a0cm from the start line. The solvent front is 6.0\u00a0cm from the "
                     "start line. Calculate the Rf value.",
             "close": "Substance over solvent: 2.4 ÷ 6.0 = 0.40.",
             "steps": _q(["Nothing to convert: both are in cm.", "Rf = d₁ ÷ d₂",
                          "Rf = 2.4 ÷ 6.0", "Rf = 0.40", "0.40 (no unit)"])},
            {"tab": "Question 2", "id": "rf-q2",
             "head": "A spot moves 45\u00a0mm from the start line. The solvent front is 9.0\u00a0cm from the "
                     "start line. Calculate the Rf value.",
             "close": "Same unit first: 9.0\u00a0cm = 90\u00a0mm. Then 45 ÷ 90 = 0.50.",
             "steps": _q(["9.0\u00a0cm × 10 = 90\u00a0mm", "Rf = d₁ ÷ d₂",
                          "Rf = 45 ÷ 90", "Rf = 0.50", "0.50 (no unit)"],
                         "same unit first?")},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "In paper chromatography, what is the mobile phase?",
             "why": "The mobile phase is the solvent, which moves up the paper.",
             "options": [
                 {"text": "The paper", "correct": False,
                  "reply": "The paper does not move: it is the stationary phase."},
                 {"text": "The solvent", "correct": True},
                 {"text": "The start line", "correct": False,
                  "reply": "The start line is where the spots go. The solvent is the mobile "
                           "phase."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the equation for an Rf value.",
             "why": "Rf = distance moved by substance ÷ distance moved by solvent.",
             "options": [
                 {"text": "distance moved by solvent ÷ distance moved by substance",
                  "correct": False,
                  "reply": "This is upside down. It would give an answer bigger than 1."},
                 {"text": "distance moved by substance ÷ distance moved by solvent",
                  "correct": True},
                 {"text": "distance moved by substance × distance moved by solvent",
                  "correct": False,
                  "reply": "Rf is a ratio: divide the two distances."},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A spot moves 4.2\u00a0cm from the start line. The solvent front is 6.0\u00a0cm from "
                       "the start line. Calculate the Rf value.",
             "convOptions": ["Nothing to convert: both are in cm", "Convert cm to mm: multiply by 10",
                             "Convert only 4.2\u00a0cm to mm"],
             "convAnswer": 0, "answer": 0.7, "tol": 0.005, "unit": "no unit",
             "units": ["no unit", "cm", "mm", "cm²"],
             "right": "4.2 ÷ 6.0 = 0.70. An Rf value has no unit.",
             "wrong": "Rf = distance moved by substance ÷ distance moved by solvent = 4.2 ÷ "
                      "6.0 = 0.70, with no unit.",
             "model": ["C · Nothing to convert", "F · Rf = d₁ ÷ d₂",
                       "I · Rf = 4.2 ÷ 6.0", "F · Rf = 0.70",
                       "A · 0.70 (no unit)"]},
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A spot moves 18\u00a0mm from the start line. The solvent front is 6.0\u00a0cm from the "
                       "start line. Calculate the Rf value.",
             "convOptions": ["Nothing to convert", "Convert 6.0\u00a0cm to mm: multiply by 10",
                             "Convert 18\u00a0mm to cm: multiply by 10"],
             "convAnswer": 1, "answer": 0.3, "tol": 0.005, "unit": "no unit",
             "units": ["no unit", "cm", "mm", "cm²"],
             "right": "6.0\u00a0cm = 60\u00a0mm, and 18 ÷ 60 = 0.30.",
             "wrong": "Put both distances in the same unit first: 6.0\u00a0cm = 60\u00a0mm. Then Rf = 18 "
                      "÷ 60 = 0.30.",
             "model": ["C · 6.0\u00a0cm × 10 = 60\u00a0mm", "F · Rf = d₁ ÷ d₂",
                       "I · Rf = 18 ÷ 60", "F · Rf = 0.30",
                       "A · 0.30 (no unit)"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how paper chromatography separates the dyes in an ink. Put the "
                       "links in order.",
             "links": ["The solvent moves up the paper and dissolves the dyes in the ink spot.",
                       "The dissolved dyes are carried up the paper, but each dye is attracted to "
                       "the paper by a different amount.",
                       "So each dye moves a different distance, and the dyes separate into "
                       "different spots."],
             "herrings": [{"text": "The heaviest dye always moves furthest up the paper.",
                           "why": "Separation depends on how each dye is distributed between the "
                                  "paper and the solvent."},
                          {"text": "The paper moves up through the solvent.",
                           "why": "The paper is the stationary phase. The solvent moves."}]},
            {"kind": "chain", "command": "Suggest", "marks": 3,
             "prompt": "A food colouring gives one spot in water. Suggest how a student could find "
                       "out whether it is a pure substance. Put the links in order.",
             "links": ["One spot in water is not enough: two dyes could move the same distance in "
                       "that solvent.",
                       "So run the food colouring again in a different solvent, and then in a "
                       "third.",
                       "If it gives a single spot in every solvent, it is probably a pure substance."],
             "herrings": [{"text": "One spot in water already proves that it is pure.",
                           "why": "A pure compound gives a single spot in all solvents, not just "
                                  "one."},
                          {"text": "Use a longer strip of paper to make the spot pure.",
                           "why": "The length of the paper cannot change what is in the food "
                                  "colouring."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe how to use paper chromatography to find the Rf value of a dye in "
                       "an ink.",
             "points": ["Draw a start line in pencil near the bottom of the paper.",
                        "Put a small spot of the ink on the start line.",
                        "Stand the paper in a solvent, with the solvent below the start line.",
                        "When the solvent has nearly reached the top, mark the solvent front.",
                        "Measure from the start line to the centre of the spot and to the solvent "
                        "front, then Rf = distance moved by dye ÷ distance moved by "
                        "solvent."],
             "reject": ["“Draw the start line in pen.” Ink would run up the paper with "
                        "the dyes.",
                        "“Pour the solvent above the start line.” The spots would "
                        "dissolve into the solvent in the beaker."]},
        ],
    },
}
