# -*- coding: utf-8 -*-
"""Amounts of substances in equations, in the lean shape. Spec table: ks4-amounts-in-equations.md.

LEGACY (batch 11). Routes CH and TH only (8464 5.3.2.2 / 8462 4.3.2.2, both HT only).
The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the same five on
both routes) stay from the Design page. The practice set does not read the subtopic `quiz`
list, so its fixes are logic_edits and there is no quiz-amounts-in-equations.json.

The CFIFA examples and questions (`cfifa`), the worked three-step example (`steps-worked`,
aie-w) and the three-step attempt (`steps-attempt`, aie-a) are the legacy page's own. The
record adds EQ_N (the legacy page's own triangle) so it can be placed with `triangle:EQ_N`;
the last logic_edit rewrites `Object.assign(c, {` into the shape the pilot builder needs
(the eco builder accepts either shape).
"""

LOGIC_EDITS = [
    # Practice Q1 (N2 + 3H2, 0.6 mol): explanations used dashes. Stem and options kept.
    ('"1": "The molar ratio must be used — 3 mol H₂ produces 2 mol NH₃, so 0.6 mol H₂ produces 0.6 × (2/3) = 0.4 mol NH₃."',
     '"1": "Use the mole ratio. 3 mol of H₂ makes 2 mol of NH₃, so 0.6 mol of H₂ makes 0.6 × 2 ÷ 3 = 0.4 mol."'),
    ('"2": "0.6 × (3/2) = 0.9 — this inverts the ratio. H₂:NH₃ = 3:2, so NH₃ = H₂ × (2/3)."',
     '"2": "0.6 × 3 ÷ 2 turns the ratio upside down. Wanted over given: 0.6 × 2 ÷ 3 = 0.4 mol."'),
    ('"3": "Doubling would only apply if the ratio were 1:2 — but H₂:NH₃ = 3:2."',
     '"3": "Doubling only works for a 1 : 2 ratio. Here H₂ : NH₃ is 3 : 2."'),
    # Practice Q3 (4.8 g Mg to MgO): credited option visibly the longest (71 against 24). Stem kept.
    ("'8.0 g: n(Mg) = 0.2 mol; ratio 2 : 2 gives 0.2 mol MgO; 0.2 × 40 = 8.0 g'",
     "'8.0 g: 0.2 × 40'"),
    # Practice Q4 (Mr of hydrogen gas): credited option visibly the longest (21 against 4). Stem kept.
    ("'2: hydrogen gas is H₂'",
     "'2'"),
    # Practice Q5 (CaO from 10 g CaCO3): credited option visibly the longest (95 against 51). Stem kept.
    ("'Mass to moles (10 ÷ 100 = 0.1), ratio 1 : 1 (0.1 mol CaO), moles to mass (0.1 × 56 = 5.6 g)'",
     "'Mass to moles, then the ratio, then moles to mass'"),
    # Worked three-step example (steps-worked slot): the Convert line had a dash aside.
    ("'Nothing to convert — the mass of magnesium is already in grams throughout the calculation.'",
     "'Nothing to convert: the mass is in grams.'"),
    # Builder seam for the record's equation (see the docstring).
    ("return Object.assign(c, {",
     "const R = c;\n    return Object.assign({}, R, {"),
    # Examiner NOTE taken as a fix: Steps-attempt answer from 2 s.f. data (8.0 g) is 3.5 g, not 3.52 g.
    ("'m(CO₂) = 3.52', '3.52 g of carbon dioxide'",
     "'m(CO₂) = 3.52', '3.5 g of carbon dioxide'"),
    # Blind fix (a): practice Q4 named a 'Step 3' the item does not show. Self-contained now. NEW ID.
    ("Q('Mg + 2HCl → MgCl₂ + H₂. What is the Mr of hydrogen gas used in Step 3?'",
     "Q('Mg + 2HCl → MgCl₂ + H₂. What is the Mr of hydrogen gas, H₂? Ar: H = 1.'"),
    # Ladder rung 2 (Mide, 16 Nov 2026): both calculations repeated the practice set (the 4.8 g Mg
    # question word for word, and the 10 g CaCO3 numbers). New questions on the same point
    # (mass to moles, ratio, moles to mass); positions and ids kept.
    ("CALC('Calculate the mass of magnesium oxide formed when 4.8 g of magnesium burns completely. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.', ['Nothing to convert', 'Convert g to kg', 'Convert Mg to O₂'], 0, 8, 'g', ['g', 'mol', 'kg'], 'n(Mg) = 4.8 ÷ 24 = 0.2 mol; ratio 2 : 2 gives 0.2 mol MgO; m = 0.2 × 40 = 8.0 g.', 'Mass to moles, ratio, moles to mass.', ['C · nothing to convert', 'F · n = m ÷ Ar; ratio; m = n × Mr', 'I · n(Mg) = 4.8 ÷ 24 = 0.2; n(MgO) = 0.2 × 2 ÷ 2 = 0.2', 'F · m(MgO) = 0.2 × 40 = 8.0', 'A · 8.0 g'], 0.05),",
     "CALC('Calculate the mass of water formed when 0.4 g of hydrogen burns completely. 2H₂ + O₂ → 2H₂O. Ar: H = 1, O = 16.', ['Nothing to convert', 'Convert g to kg', 'Convert H₂ to H'], 0, 3.6, 'g', ['g', 'mol', 'kg'], 'n(H₂) = 0.4 ÷ 2 = 0.2 mol; ratio 2 : 2 gives 0.2 mol H₂O; m = 0.2 × 18 = 3.6 g.', 'Mass to moles, ratio, moles to mass. Hydrogen gas is H₂, so its Mr is 2.', ['C · nothing to convert', 'F · n = m ÷ Mr; ratio; m = n × Mr', 'I · n(H₂) = 0.4 ÷ 2 = 0.2; n(H₂O) = 0.2 × 2 ÷ 2 = 0.2', 'F · m(H₂O) = 0.2 × 18 = 3.6', 'A · 3.6 g'], 0.05),"),
    ("CALC('Calculate the mass of calcium oxide formed when 10 g of calcium carbonate decomposes. CaCO₃ → CaO + CO₂. Mr: CaCO₃ = 100, CaO = 56.', ['Nothing to convert', 'Convert g to kg', 'Convert Mr to g'], 0, 5.6, 'g', ['g', 'mol', 'kg'], 'n(CaCO₃) = 10 ÷ 100 = 0.1 mol; ratio 1 : 1; m(CaO) = 0.1 × 56 = 5.6 g.', 'Three steps: ÷ 100, × 1/1, × 56.', ['C · nothing to convert', 'F · n = m ÷ Mr; ratio; m = n × Mr', 'I · n(CaCO₃) = 10 ÷ 100 = 0.1; n(CaO) = 0.1', 'F · m(CaO) = 0.1 × 56 = 5.6', 'A · 5.6 g'], 0.05)",
     "CALC('Calculate the mass of carbon dioxide formed when 6.0 g of carbon burns completely. C + O₂ → CO₂. Ar: C = 12, O = 16.', ['Nothing to convert', 'Convert g to kg', 'Convert C to CO₂'], 0, 22, 'g', ['g', 'mol', 'kg'], 'n(C) = 6.0 ÷ 12 = 0.5 mol; ratio 1 : 1; m(CO₂) = 0.5 × 44 = 22 g.', 'Three steps: ÷ 12, × 1/1, × 44.', ['C · nothing to convert', 'F · n = m ÷ Ar; ratio; m = n × Mr', 'I · n(C) = 6.0 ÷ 12 = 0.5; n(CO₂) = 0.5', 'F · m(CO₂) = 0.5 × 44 = 22', 'A · 22 g'], 0.05)"),
]

LESSON = {
    "slug": "amounts-in-equations",
    "start": {
        "setup": "Magnesium reacts with hydrochloric acid: Mg + 2HCl → MgCl₂ + H₂.",
        "question": "If you had to guess, how many moles of hydrochloric acid react with one "
                    "mole of magnesium?",
        "options": [
            ("One mole",
             "Two moles. The 2 in front of HCl means two moles of hydrochloric acid react with "
             "every mole of magnesium."),
            ("Two moles",
             "Two moles. The 2 in front of HCl means two moles of hydrochloric acid react with "
             "every mole of magnesium."),
        ],
        "answer": 1,
    },
    "words": ["balanced symbol equation", "mole ratio", "relative formula mass", "reacting mass"],
    "knowledge": [
        {"kind": "card", "title": "Reading an equation in moles",
         "body": ["Chemical equations can be interpreted in terms of moles.",
                  "Mg + 2HCl → MgCl₂ + H₂ shows that one mole of magnesium reacts with two moles "
                  "of hydrochloric acid to produce one mole of magnesium chloride and one mole of "
                  "hydrogen gas.",
                  "The balancing numbers give the ratio of moles. Here "
                  "Mg : HCl : MgCl₂ : H₂ = 1 : 2 : 1 : 1."]},
        {"kind": "card", "title": "The mole ratio",
         "body": ["2Mg + O₂ → 2MgO: 2 mol of magnesium reacts with 1 mol of oxygen to make 2 mol "
                  "of magnesium oxide.",
                  {"slot": "fig:mole-ratio-bars"},
                  "The ratio stays the same whatever the amount. 0.2 mol of magnesium reacts with "
                  "0.1 mol of oxygen to make 0.2 mol of magnesium oxide.",
                  "To go from one substance to another: moles wanted = moles given × wanted "
                  "balancing number ÷ given balancing number."]},
        {"kind": "reveal", "title": "2Mg + O₂ → 2MgO in grams (Ar: Mg = 24, O = 16)",
         "cols": ["Working", "Mass"],
         "rows": [
             ("2Mg", "2 × 24", "48 g"),
             ("O₂", "1 × 32", "32 g"),
             ("2MgO", "2 × 40", "80 g"),
         ]},
        {"kind": "card", "title": "Masses in a balanced equation",
         "body": ["Multiply each balancing number by the M<sub>r</sub>. The equation then reads in "
                  "grams: 48 g + 32 g → 80 g.",
                  "Mass is conserved, so the masses on the two sides add up to the same total."]},
        {"kind": "card", "title": "Moles from mass",
         "body": [{"slot": "triangle:EQ_N"},
                  "n = m ÷ M<sub>r</sub>",
                  "You use it twice in a reacting-mass question: forwards for the substance you "
                  "are given, backwards for the one you want."]},
        {"kind": "card", "title": "Each step on its own",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Reacting masses in three steps",
         "body": [{"points": [
             "Step 1: turn the mass you are given into moles: n = m ÷ M<sub>r</sub>.",
             "Step 2: use the balancing numbers to find the moles of the substance you want.",
             "Step 3: turn those moles into a mass: m = n × M<sub>r</sub>.",
         ]},
                  "Keep every mass in grams.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("N₂ + 3H₂ → 2NH₃, so 0.6 mol of H₂ makes 0.6 × 3 ÷ 2 = 0.9 mol of NH₃.",
              "Wanted over given: 0.6 × 2 ÷ 3 = 0.4 mol of NH₃."),
             ("Oxygen gas has M<sub>r</sub> 16.",
              "Oxygen gas is O₂, so M<sub>r</sub> = 32. Hydrogen gas is H₂, so M<sub>r</sub> = 2."),
             ("Multiply by the balancing number again when working out the mass.",
              "Use each balancing number once, in Step 2."),
             ("Putting a mass in kilograms into n = m ÷ M<sub>r</sub>.",
              "Convert to grams first: 1 kg = 1000 g."),
         ]}]},
    ],
    "key_fact": "The balancing numbers in a symbol equation give the ratio of moles of each "
                "substance. To find a reacting mass, turn the given mass into moles "
                "(÷ M<sub>r</sub>), use the mole ratio, then turn the moles back into a mass "
                "(× M<sub>r</sub>).",
    "deeper": [
        {"kind": "card", "title": "Check your answer",
         "body": ["The total mass of the reactants equals the total mass of the products.",
                  "4.6 g of sodium burns in 1.6 g of oxygen to make 6.2 g of sodium oxide: "
                  "4.6 + 1.6 = 6.2."]},
        {"kind": "card", "title": "Where this goes next",
         "body": ["Balancing an equation from masses, and limiting reactants, are in Using moles "
                  "in calculations."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong>: one short answer, such as a mole ratio.",
             "<strong>Calculate</strong>: write all three steps, each with its unit.",
             "<strong>Explain</strong>: say what each step does, in order.",
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
    },
}
