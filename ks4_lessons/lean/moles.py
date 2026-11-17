# -*- coding: utf-8 -*-
"""Moles, in the lean shape. Spec table: ks4-moles.md.

LEGACY (batch 11). Routes CH and TH only (8464 5.3.2.1 / 8462 4.3.2.1, both HT only).
The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the same five on
both routes) stay from the Design page. The practice set does not read the subtopic `quiz`
list, so its fixes are logic_edits and there is no quiz-moles.json.

The legacy page splits its worked examples into two Ks4Cfifa blocks (cf1Examples for mass,
cf2Examples for particles), so the `cfifa` slot has no `cfExamples` to reuse. The record
therefore carries its own `cfifa`: the same five examples and five questions, with the
question ids kept (mol-q1..q3, mol-p1, mol-p2). The record's equations EQ_N and EQ_P are the
legacy page's own two triangles.

Batch-11 logic returns `Object.assign(c, {`. The last logic_edit rewrites it into the
`Object.assign({}, R, {` shape the pilot builder needs for LEAN_PROPS (the eco builder accepts
either shape). `c` is common()'s result, so behaviour is unchanged.
"""

LOGIC_EDITS = [
    # Rung 2 calc 2 (moles#r2-2): "Convert mol to g" is arguably what the whole calculation does,
    # so it was not definitely wrong as a Convert choice. Same index (0 credited), same answer.
    ("['Nothing to convert', 'Convert mol to g', 'Convert 0.2 mol to 200 mol']",
     "['Nothing to convert', 'Convert g to kg', 'Convert 0.2 mol to 200 mol']"),
    # Practice Q1 (9.8 g H2SO4): explanations shouted and used a dash. Stem and options kept.
    ('"1": "Dividing the WRONG way: n = mass ÷ Mr not Mr ÷ mass. n = 9.8 ÷ 98 = 0.1 mol."',
     '"1": "That divides the wrong way. n = mass ÷ Mr, so n = 9.8 ÷ 98 = 0.1 mol."'),
    ('"2": "Multiplying mass and Mr gives a meaningless large number — always DIVIDE mass by Mr."',
     '"2": "Do not multiply the mass by Mr. Divide: n = 9.8 ÷ 98 = 0.1 mol."'),
    # Practice Q2 (CaCO3 from 3.01 × 10²³): same fault in explanations 1 and 3. Stem and options kept.
    ('"1": "3.01 × 10²³ is HALF the Avogadro constant — so this represents 0.5 mol. Mass = 0.5 × 100 = 50 g."',
     '"1": "3.01 × 10²³ is half the Avogadro constant, so it is 0.5 mol. Mass = 0.5 × 100 = 50 g."'),
    ('"3": "0.5 is the number of moles — multiply by Mr (100) to get mass: 0.5 × 100 = 50 g."',
     '"3": "0.5 is the number of moles. Multiply by Mr to get the mass: 0.5 × 100 = 50 g."'),
    # Practice Q3 (2.7 kg Al): credited option was visibly the longest (46 against 18). Stem kept.
    ("'100 mol: 2.7 kg = 2700 g, and 2700 ÷ 27 = 100'",
     "'100 mol: 2700 ÷ 27'"),
    # Practice Q4 (molecules in 36 g water): credited option visibly the longest (48 against 11).
    ("'1.204 × 10²⁴: 36 ÷ 18 = 2 mol, then 2 × 6.02 × 10²³'",
     "'1.204 × 10²⁴'"),
    # Practice Q5 (atoms in a mole of water): credited option visibly the longest (61 against 15).
    ("'3 × 6.02 × 10²³ = 1.806 × 10²⁴: each molecule has three atoms'",
     "'3 × 6.02 × 10²³'"),
    # Builder seam for the record's equations and cfifa (see the docstring).
    ("return Object.assign(c, {",
     "const R = c;\n    return Object.assign({}, R, {"),
    # Examiner SHOULD FIX (13 Nov), exactly as in EXAMINER.md / _exam/proposed.py. Practice Q2 '30100 g' feedback. Keys unchanged.
    ('"2": "A particle count must be turned into moles first (÷ 6.02 × 10²³), and only then multiplied by Mr. Multiplying the count by Mr skips the mole and gives a meaningless number."',
     '"2": "No correct step gives 30100 g. Turn the count into moles first: 3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5 mol. Then 0.5 × 100 = 50 g."'),
]

_CFQ_PH = ["anything to convert?", "written out", "numbers in", "work it out", "with unit"]


def _q(lines, conv_ph=None):
    """A Ks4Cfifa question's five lines, in the legacy CFQ shape."""
    letters = [("C", "Convert"), ("F", "Formula"), ("I", "Insert"), ("F", "Fine-tune"), ("A", "Answer")]
    ph = list(_CFQ_PH)
    if conv_ph:
        ph[0] = conv_ph
    return [{"letter": l, "label": lab, "placeholder": p, "line": ln}
            for (l, lab), p, ln in zip(letters, ph, lines)]


LESSON = {
    "slug": "moles",
    "start": {
        "setup": None,
        "question": "If you had to guess, what do one mole of carbon and one mole of water have "
                    "in common?",
        "options": [
            ("The same mass",
             "The same number of particles: 6.02 × 10²³. Their masses are different: 12 g and "
             "18 g."),
            ("The same number of particles",
             "The same number of particles: 6.02 × 10²³. Their masses are different: 12 g and "
             "18 g."),
        ],
        "answer": 1,
    },
    "words": ["mole", "Avogadro constant", "relative formula mass"],
    "knowledge": [
        {"kind": "card", "title": "The mole",
         "body": ["Chemical amounts are measured in moles. The symbol for the unit mole is mol.",
                  "The mass of one mole of a substance in grams is numerically equal to its "
                  "relative formula mass (M<sub>r</sub>). For an element, use its relative atomic "
                  "mass (A<sub>r</sub>).",
                  {"points": ["One mole of carbon, C (A<sub>r</sub> 12), has a mass of 12 g.",
                              "One mole of water, H₂O (M<sub>r</sub> 18), has a mass of 18 g.",
                              "One mole of sodium chloride, NaCl (M<sub>r</sub> 58.5), has a mass "
                              "of 58.5 g."]},
                  {"slot": "fig:one-mole-masses"}]},
        {"kind": "card", "title": "The Avogadro constant",
         "body": ["One mole of a substance contains the same number of the stated particles, "
                  "atoms, molecules or ions as one mole of any other substance.",
                  "The number of atoms, molecules or ions in a mole of a given substance is the "
                  "Avogadro constant. The value of the Avogadro constant is 6.02 × 10²³ per mole.",
                  "Moles can count atoms, molecules, ions, electrons, formulae and equations. In "
                  "one mole of carbon (C) the number of atoms is the same as the number of "
                  "molecules in one mole of carbon dioxide (CO₂)."]},
        {"kind": "card", "title": "Say which particle you are counting",
         "body": ["One mole of water contains 6.02 × 10²³ molecules.",
                  "Each water molecule has three atoms: two hydrogen and one oxygen.",
                  "So one mole of water contains 3 × 6.02 × 10²³ = 1.806 × 10²⁴ atoms."]},
        {"kind": "card", "title": "Moles from mass",
         "body": [{"slot": "triangle:EQ_N"},
                  "n = m ÷ M<sub>r</sub>",
                  "The mass must be in grams. Convert kilograms first: 1 kg = 1000 g.",
                  "You need to remember this equation."]},
        {"kind": "card", "title": "Particles from moles",
         "body": [{"slot": "triangle:EQ_P"},
                  "N = n × 6.02 × 10²³",
                  "The Avogadro constant is a fixed number, so it is never the thing you find."]},
        {"kind": "card", "title": "Standard form",
         "body": ["6.02 × 10²³ is 602 followed by 21 zeros.",
                  "To multiply, multiply the front number: 2 × 6.02 × 10²³ = 12.04 × 10²³.",
                  "Then keep the front number between 1 and 10: 12.04 × 10²³ = 1.204 × 10²⁴.",
                  "To divide two numbers with the same power of ten, divide the front numbers: "
                  "3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Between a mass and a number of particles",
         "body": ["Always go through moles.",
                  {"points": ["Particles to mass: n = particles ÷ 6.02 × 10²³, then "
                              "m = n × M<sub>r</sub>.",
                              "Mass to particles: n = m ÷ M<sub>r</sub>, then "
                              "particles = n × 6.02 × 10²³."]},
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A mole of anything has the same mass.",
              "A mole of anything has the same number of particles. Its mass in grams is its "
              "M<sub>r</sub>."),
             ("2.7 kg of aluminium is 2.7 ÷ 27 = 0.1 mol.",
              "Convert to grams first: 2700 ÷ 27 = 100 mol."),
             ("n = M<sub>r</sub> ÷ mass.",
              "n = mass ÷ M<sub>r</sub>."),
             ("One mole of water contains 6.02 × 10²³ atoms.",
              "It contains 6.02 × 10²³ molecules, which is 3 × 6.02 × 10²³ atoms."),
         ]}]},
    ],
    "key_fact": "Chemical amounts are measured in moles (mol). One mole of any substance contains "
                "6.02 × 10²³ particles (the Avogadro constant), and its mass in grams equals its "
                "relative formula mass, so number of moles = mass (g) ÷ M<sub>r</sub>.",
    "deeper": [
        {"kind": "card", "title": "Finding M<sub>r</sub> from moles",
         "body": ["Rearrange the equation: M<sub>r</sub> = mass ÷ number of moles.",
                  "0.5 mol of a substance has a mass of 20 g, so its M<sub>r</sub> is "
                  "20 ÷ 0.5 = 40."]},
        {"kind": "card", "title": "Where this goes next",
         "body": ["Percentage by mass of an element in a compound is in Relative formula mass.",
                  "Using moles to work out reacting masses is in Amounts of substances in "
                  "equations."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>State</strong>: give the fact, such as the Avogadro constant.",
             "<strong>Calculate</strong>: show each line, with the mass in grams.",
             "<strong>Give your answer in standard form</strong>: front number between 1 and 10.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
    "equations": {
        "EQ_N": {"name": "Moles from mass", "written": "number of moles = mass (g) ÷ Mr",
                 "source": "none",
                 "top": {"s": "m", "name": "mass", "unit": "g"},
                 "bottom": [{"s": "n", "name": "number of moles", "unit": "mol"},
                            {"s": "Mr", "name": "relative formula mass (Ar for an element)",
                             "unit": "no unit"}]},
        "EQ_P": {"name": "Particles from moles",
                 "written": "number of particles = number of moles × Avogadro constant",
                 "source": "none",
                 "top": {"s": "N", "name": "number of particles", "unit": "no unit"},
                 "bottom": [{"s": "n", "name": "number of moles", "unit": "mol"},
                            {"s": "Nₐ", "name": "Avogadro constant, 6.02 × 10²³",
                             "unit": "per mol", "fixed": True}]},
    },
    "cfifa": {
        "examples": [
            {"tab": "Moles from mass", "eq": "EQ_N", "find": "n", "next": "Now one in kilograms.",
             "head": "Calculate the number of moles in 27 g of aluminium (Ar = 27).",
             "steps": [["C", "Convert", "Nothing to convert: the mass is in grams.",
                        "Ar has no unit."],
                       ["F", "Formula", "n = m ÷ Ar"],
                       ["I", "Insert", "n = 27 ÷ 27"],
                       ["F", "Fine-tune", "n = 1"],
                       ["A", "Answer", "1 mol of aluminium"]]},
            {"tab": "Convert kg to g", "eq": "EQ_N", "find": "n",
             "next": "Now the triangle the other way.",
             "head": "Calculate the number of moles of aluminium atoms in 2.7 kg of aluminium "
                     "(Ar = 27).",
             "steps": [["C", "Convert", "2.7 kg × 1000 = 2700 g",
                        "Grams first: 2.7 ÷ 27 would give 0.1 mol, a thousand times too small."],
                       ["F", "Formula", "n = m ÷ Ar"],
                       ["I", "Insert", "n = 2700 ÷ 27"],
                       ["F", "Fine-tune", "n = 100"],
                       ["A", "Answer", "100 mol"]]},
            {"tab": "Mass from moles", "eq": "EQ_N", "find": "m",
             "next": "Now particles from moles.",
             "head": "Calculate the mass of 0.25 mol of calcium carbonate, CaCO₃ (Mr = 100).",
             "steps": [["C", "Convert", "Nothing to convert."],
                       ["F", "Formula", "m = n × Mr"],
                       ["I", "Insert", "m = 0.25 × 100"],
                       ["F", "Fine-tune", "m = 25"],
                       ["A", "Answer", "25 g"]]},
            {"tab": "Particles from moles", "eq": "EQ_P", "find": "N",
             "next": "Now the triangle the other way.",
             "head": "How many molecules are there in 2 mol of water?",
             "steps": [["C", "Convert", "Nothing to convert."],
                       ["F", "Formula", "particles = n × Nₐ"],
                       ["I", "Insert", "particles = 2 × 6.02 × 10²³"],
                       ["F", "Fine-tune", "particles = 12.04 × 10²³ = 1.204 × 10²⁴",
                        "In standard form the front number is between 1 and 10."],
                       ["A", "Answer", "1.204 × 10²⁴ molecules"]]},
            {"tab": "Moles from particles", "eq": "EQ_P", "find": "n", "next": "Now yours, below.",
             "head": "How many moles is 3.01 × 10²³ formula units of sodium chloride?",
             "steps": [["C", "Convert", "Nothing to convert."],
                       ["F", "Formula", "n = particles ÷ Nₐ"],
                       ["I", "Insert", "n = 3.01 × 10²³ ÷ 6.02 × 10²³"],
                       ["F", "Fine-tune", "n = 0.5",
                        "Same power of ten top and bottom, so divide the front numbers."],
                       ["A", "Answer", "0.5 mol"]]},
        ],
        "questions": [
            {"tab": "Question 1", "id": "mol-q1",
             "head": "Calculate the number of moles in 9 g of water, H₂O (Mr = 18).",
             "close": "n = m ÷ Mr, so 9 ÷ 18, not 18 ÷ 9.",
             "steps": _q(["Nothing to convert: grams.", "n = m ÷ Mr", "n = 9 ÷ 18", "n = 0.5",
                          "0.5 mol"])},
            {"tab": "Question 2", "id": "mol-q2",
             "head": "Calculate the number of moles in 0.5 kg of calcium carbonate, CaCO₃ "
                     "(Mr = 100).",
             "close": "0.5 ÷ 100 uses kilograms. Convert: 0.5 kg = 500 g.",
             "steps": _q(["0.5 kg = 500 g", "n = m ÷ Mr", "n = 500 ÷ 100", "n = 5", "5 mol"],
                         "kg to g?")},
            {"tab": "Question 3", "id": "mol-q3",
             "head": "Calculate the mass of 2 mol of carbon dioxide, CO₂ (Mr = 44).",
             "close": "Cover m: m = n × Mr.",
             "steps": _q(["Nothing to convert.", "m = n × Mr", "m = 2 × 44", "m = 88", "88 g"])},
            {"tab": "Question 4", "id": "mol-p1",
             "head": "How many atoms are there in 0.1 mol of iron?",
             "close": "Multiply the front number: 0.1 × 6.02 = 0.602, so 6.02 × 10²².",
             "steps": _q(["Nothing to convert.", "particles = n × Nₐ",
                          "particles = 0.1 × 6.02 × 10²³",
                          "particles = 0.602 × 10²³ = 6.02 × 10²²", "6.02 × 10²² atoms"])},
            {"tab": "Question 5", "id": "mol-p2",
             "head": "How many moles is 1.204 × 10²⁴ molecules of carbon dioxide?",
             "close": "Write both with the same power: 12.04 × 10²³ ÷ 6.02 × 10²³ = 2.",
             "steps": _q(["1.204 × 10²⁴ = 12.04 × 10²³", "n = particles ÷ Nₐ",
                          "n = 12.04 × 10²³ ÷ 6.02 × 10²³", "n = 2", "2 mol"],
                         "same power of ten?")},
        ],
    },
}
