# -*- coding: utf-8 -*-
"""Concentration of solutions, in the lean shape. Spec table: ks4-concentration-of-solutions.md.

LEGACY (batch 2). The ladder (Ks4Ladder, r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank), so its fixes are in
quiz-concentration-of-solutions.json. The CFIFA examples and questions (`cfifa` slot) are the
page's own. The record adds one equation, EQ_CONC, so the page gets a formula triangle (the old
page wrote the three arrangements out but had none). This logic returns
`Object.assign({}, R, {` once, so the builder can add LEAN_PROPS without a seam edit.
"""

LOGIC_EDITS = [
    # Rung 3, Foundation version (chain). Links 1 and 2 could be read in either order (the rule,
    # then the student's slip, or the slip, then the rule). Mide's rule: one right order only.
    # Link 2 now starts "So" from link 1, and link 3 uses the 0.6 that link 2 works out.
    # Position kept (id kept).
    ("links: ['Concentration in g/dm³ needs the volume of solution in dm³.', '600 cm³ ÷ 1000 = "
     "0.6 dm³, but the student divided by 600.', 'So the concentration is 18 ÷ 0.6 = 30 g/dm³, "
     "1000 times bigger than the student’s answer.'],",
     "links: ['Concentration in g/dm³ needs the volume of solution in dm³.', 'So the 600 cm³ "
     "must be divided by 1000 to give 0.6 dm³. The student divided by 600 instead.', 'The "
     "correct concentration is 18 ÷ 0.6 = 30 g/dm³, 1000 times bigger than the student’s "
     "answer.'],"),
]

LESSON = {
    "slug": "concentration-of-solutions",
    "start": {
        "setup": "A sports drink has 60 g of sugar dissolved in every 1000 cm³.",
        "question": "If you had to guess, how much sugar is in a 250 cm³ glass of it: about 15 g, "
                    "or about 240 g?",
        "options": [
            ("About 15 g",
             "About 15 g. 250 cm³ is a quarter of 1000 cm³, so the glass holds a quarter of the "
             "sugar."),
            ("About 240 g",
             "About 15 g. 250 cm³ is a quarter of 1000 cm³, so the glass holds a quarter of the "
             "sugar."),
        ],
        "answer": 0,
    },
    "words": ["solute", "solution", "concentration", "dm³ (decimetre cubed)"],
    "knowledge": [
        {"kind": "card", "title": "What concentration means",
         "body": ["Many chemical reactions take place in solutions.",
                  "The solute is the substance that dissolves. The solvent is the liquid it "
                  "dissolves in, often water. Together they make a solution.",
                  "The concentration of a solution can be measured in mass per given volume of "
                  "solution, for example grams per dm³ (g/dm³)."]},
        {"kind": "card", "title": "cm³ and dm³",
         "body": ["1 dm³ = 1000 cm³. A dm³ is the same as a litre.",
                  "To change cm³ into dm³, divide by 1000.",
                  {"points": ["250 cm³ = 0.25 dm³", "500 cm³ = 0.5 dm³", "25 cm³ = 0.025 dm³"]}]},
        {"kind": "card", "title": "The equation",
         "body": [{"slot": "triangle:EQ_CONC"},
                  "Rearranged: mass of solute = concentration × volume of solution."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Mass, volume and concentration", "routes": ["CH", "TH"],
         "body": [{"points": [
             "More mass of solute in the same volume of solution gives a higher concentration.",
             "The same mass of solute in a bigger volume of solution gives a lower concentration.",
             "Double the mass in the same volume and the concentration doubles. Double the "
             "volume for the same mass and the concentration halves.",
         ]}]},
        {"kind": "reveal", "title": "Salt solutions", "routes": ["CH", "TH"],
         "cols": ["Concentration"],
         "rows": [
             ("2 g in 0.050 dm³", "40 g/dm³"),
             ("8 g in 0.200 dm³", "40 g/dm³"),
             ("2 g in 0.200 dm³", "10 g/dm³"),
         ]},
        {"kind": "card", "title": "Concentration in mol/dm³", "routes": ["TH"],
         "body": ["The concentration of a solution can also be measured in mol/dm³: the amount of "
                  "solute, in moles, in each dm³ of solution.",
                  "concentration (mol/dm³) = amount of solute (mol) ÷ volume of solution (dm³)",
                  "To go from a mass to mol/dm³, first turn the mass into moles: amount = mass ÷ "
                  "M<sub>r</sub>.",
                  "4.0 g of sodium hydroxide, NaOH (M<sub>r</sub> = 40), is dissolved to make "
                  "250 cm³ of solution. Amount = 4.0 ÷ 40 = 0.10 mol. Volume = 0.250 dm³. "
                  "Concentration = 0.10 ÷ 0.250 = 0.40 mol/dm³.",
                  "To find the amount of solute in a given volume, turn the equation round: "
                  "amount (mol) = concentration (mol/dm³) × volume of solution (dm³). For the "
                  "mass in grams, multiply the amount by M<sub>r</sub>."]},
        {"kind": "card", "title": "Volume of solution, not of water",
         "body": ["Concentration uses the volume of the whole solution.",
                  "To make 250 cm³ of solution, dissolve the solute in less water first. Then add "
                  "water until the total volume of solution is 250 cm³."]},
        {"kind": "card", "title": "Making up a solution",
         "body": [{"points": [
             "Work out the mass needed: 20 g/dm³ × 0.25 dm³ = 5.0 g for 250 cm³.",
             "Weigh out the solute.",
             "Dissolve it in a smaller volume of distilled water in a beaker.",
             "Pour it into a container that measures the volume, rinsing the beaker into it.",
             "Add distilled water until the volume of solution is 250 cm³, then mix.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("5.0 g in 250 cm³: 5.0 ÷ 250 = 0.02 g/dm³.",
              "Convert first: 250 cm³ = 0.25 dm³, so 5.0 ÷ 0.25 = 20 g/dm³."),
             ("To change cm³ into dm³, multiply by 1000.",
              "Divide by 1000. A dm³ is bigger than a cm³, so there are fewer of them."),
             ("The bigger beaker holds more salt, so it is more concentrated.",
              "Concentration is the mass in each dm³, not the total mass."),
         ]}]},
    ],
    "key_fact": "Concentration is the mass of solute in a given volume of solution, measured in "
                "g/dm³: concentration = mass of solute (g) ÷ volume of solution (dm³). To change "
                "cm³ into dm³, divide by 1000.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: convert the volume to dm³, write the equation, then "
             "give the answer with its unit.",
             "<strong>Explain</strong>: say how the mass of solute or the volume of solution "
             "changes, and what that does to the concentration.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
    "equations": {
        "EQ_CONC": {"name": "Concentration",
                    "written": "concentration = mass of solute ÷ volume of solution",
                    "source": "none",
                    "top": {"s": "m", "name": "mass of solute", "unit": "g"},
                    "bottom": [{"s": "c", "name": "concentration", "unit": "g/dm³"},
                               {"s": "V", "name": "volume of solution", "unit": "dm³"}]},
    },
}
