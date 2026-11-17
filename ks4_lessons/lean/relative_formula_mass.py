# -*- coding: utf-8 -*-
"""Relative formula mass, in the lean shape. Spec table: ks4-relative-formula-mass.md.

LEGACY (batch 2). The ladder (Ks4Ladder, r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank). Rung 1 used to be that list's calcium
carbonate question (K.find); since 16 Nov 2026 it is its own question (sulfuric acid, below), so
no rung repeats the practice set. Practice fixes are in quiz-relative-formula-mass.json.
"""

LOGIC_EDITS = [
    # Rung 2, Higher version. It asked for the mass of CaO made from CaCO₃ by reacting masses,
    # which is 8464 5.3.2.2 / 8462 4.3.2.2 (HT only, the amounts-in-equations lesson), on an
    # all-route lesson. Rewritten to this lesson's own all-route content, percentage by mass
    # applied to a mass, with the same convert step and the same 3 marks. Position kept (id kept).
    ("prompt: 'Calcium carbonate breaks down when heated: CaCO₃ → CaO + CO₂. Calculate the mass "
     "of calcium oxide, in grams, made from 0.50 kg of calcium carbonate. Aᵣ: Ca = 40, C = 12, "
     "O = 16. Work it on paper, then choose the conversion and give the answer and unit.',\n"
     "          convOptions: ['Nothing to convert', 'Convert kg to g: multiply by 1000', 'Convert "
     "kg to g: divide by 1000'], convAnswer: 1, answer: 280, tol: 1, unit: 'g', units: ['g', "
     "'kg', '%', 'no unit'],\n          right: '500 g ÷ 100 × 56 = 280 g.', wrong: 'Convert 0.50 "
     "kg to 500 g. 100 g of CaCO₃ gives 56 g of CaO, so 500 g gives 5 × 56 = 280 g.',\n"
     "          model: ['C · 0.50 kg × 1000 = 500 g', 'F · mass ratio = ratio of (number in front "
     "× Mᵣ)', 'I · CaCO₃ : CaO = 100 : 56', 'F · scale factor = 500 ÷ 100 = 5; mass of CaO = 56 "
     "× 5', 'A · 280 g'] }",
     "prompt: 'Calculate the mass of iron, in grams, in 0.320 kg of iron oxide, Fe₂O₃. Aᵣ: "
     "Fe = 56, O = 16. Work it on paper, then choose the conversion and give the answer and "
     "unit.',\n          convOptions: ['Nothing to convert', 'Convert kg to g: multiply by 1000', "
     "'Convert kg to g: divide by 1000'], convAnswer: 1, answer: 224, tol: 1, unit: 'g', units: "
     "['g', 'kg', '%', 'no unit'],\n          right: 'Mᵣ = (2 × 56) + (3 × 16) = 160. 112 ÷ 160 × "
     "320 = 224 g.', wrong: 'Convert 0.320 kg to 320 g. The two iron atoms are 112 of the 160, so "
     "mass of iron = 112 ÷ 160 × 320 = 224 g.',\n          model: ['C · 0.320 kg × 1000 = 320 g', "
     "'F · mass of element = (Aᵣ × number of atoms ÷ Mᵣ) × mass of compound', 'I · Mᵣ = 112 + 48 "
     "= 160; mass of Fe = (56 × 2 ÷ 160) × 320', 'F · 112 ÷ 160 = 0.70; 0.70 × 320 = 224', "
     "'A · 224 g'] }"),
    # Rung 1 (Mide, 16 Nov 2026): it WAS practice question 1 (K.find on the calcium carbonate
    # stem), so a pupil met the same question twice. A new question on the same point (Mr from
    # Ar, no brackets), through the same K.item path; position and id kept.
    ("K.find(slug, R.route, 'relative formula mass of calcium carbonate') || { options: [] }",
     "K.item({ q: 'What is the relative formula mass of sulfuric acid, H₂SO₄? Aᵣ: H = 1, S = 32, O = 16.', opts: [['98', true], ['49', false], ['50', false], ['97', false]], wrong_explanations: { '1': 'That counts one atom of each element. H₂SO₄ has two H and four O.', '2': 'That counts one oxygen. There are four: 4 × 16 = 64.', '3': 'That counts one hydrogen. There are two: 2 × 1 = 2.' } })"),
    ("why: 'One Ca, one C and three O: 40 + 12 + (3 × 16) = 100.'",
     "why: 'Two H, one S and four O: (2 × 1) + 32 + (4 × 16) = 98.'"),
]

LESSON = {
    "slug": "relative-formula-mass",
    "start": {
        "setup": "A water molecule, H₂O, has three atoms. An oxygen molecule, O₂, has two.",
        "question": "If you had to guess, which has the bigger relative formula mass?",
        "options": [
            ("Water, H₂O",
             "Oxygen. O₂ is 16 + 16 = 32. H₂O is 1 + 1 + 16 = 18, because hydrogen atoms are "
             "very light."),
            ("Oxygen, O₂",
             "Oxygen. O₂ is 16 + 16 = 32. H₂O is 1 + 1 + 16 = 18, because hydrogen atoms are "
             "very light."),
        ],
        "answer": 1,
    },
    "words": ["relative atomic mass (Ar)", "relative formula mass (Mr)", "percentage by mass"],
    "knowledge": [
        {"kind": "card", "title": "Relative atomic mass, Ar",
         "body": ["Every element has a relative atomic mass, A<sub>r</sub>. You read it from the "
                  "periodic table you are given in the exam.",
                  {"points": ["H = 1", "C = 12", "N = 14", "O = 16", "Na = 23", "Mg = 24",
                              "Cl = 35.5", "Ca = 40"]}]},
        {"kind": "card", "title": "Relative formula mass, Mr",
         "body": ["The relative formula mass (M<sub>r</sub>) of a compound is the sum of the "
                  "relative atomic masses of the atoms in the numbers shown in the formula.",
                  "CO₂ has 1 C and 2 O: M<sub>r</sub> = 12 + (2 × 16) = 44",
                  "M<sub>r</sub> has no unit."]},
        {"kind": "card", "title": "Brackets",
         "body": ["A number after a bracket multiplies everything inside the bracket.",
                  "Ca(OH)₂ has 1 Ca, 2 O and 2 H.",
                  "M<sub>r</sub> = 40 + (2 × 16) + (2 × 1) = 74"]},
        {"kind": "reveal", "title": "Work out the Mr",
         "cols": ["Working", "Mr"],
         "rows": [
             ("H₂O", "(2 × 1) + 16", "18"),
             ("NaCl", "23 + 35.5", "58.5"),
             ("Ca(OH)₂", "40 + (2 × 16) + (2 × 1)", "74"),
             ("Al₂(SO₄)₃", "(2 × 27) + (3 × 32) + (12 × 16)", "342"),
         ]},
        {"kind": "card", "title": "Mr in a balanced equation",
         "body": ["In a balanced chemical equation, the sum of the relative formula masses of the "
                  "reactants in the quantities shown equals the sum of the relative formula masses "
                  "of the products in the quantities shown.",
                  "2Mg + O₂ → 2MgO",
                  "Reactants: (2 × 24) + 32 = 80. Products: 2 × 40 = 80.",
                  "This is conservation of mass: the same atoms are on both sides."]},
        {"kind": "card", "title": "Percentage by mass",
         "body": ["percentage by mass of an element = (A<sub>r</sub> × number of atoms of that "
                  "element) ÷ M<sub>r</sub> × 100",
                  "Oxygen in CO₂: M<sub>r</sub> = 44, and the two O atoms are 2 × 16 = 32.",
                  "32 ÷ 44 × 100 = 72.7%"]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Ca(OH)₂ has 1 O and 1 H.",
              "The 2 after the bracket doubles everything inside: 2 O and 2 H."),
             ("The M<sub>r</sub> of MgO is 80, because the equation says 2MgO.",
              "The M<sub>r</sub> of MgO is 40. The 2 means two of them: 2 × 40 = 80 in the "
              "equation."),
             ("Oxygen in CO₂ is 16 ÷ 44 × 100.",
              "Count every atom of the element. CO₂ has two O, so use 2 × 16 = 32."),
         ]}]},
    ],
    "key_fact": "The relative formula mass (Mr) of a compound is the sum of the relative atomic "
                "masses of the atoms in the numbers shown in the formula. In a balanced equation, "
                "the total Mr of the reactants equals the total Mr of the products, in the "
                "quantities shown.",
    "deeper": [
        {"kind": "card", "title": "Mr and reacting masses", "routes": ["CH", "TH"],
         "body": ["2Mg + O₂ → 2MgO",
                  "The M<sub>r</sub> values give the masses in the quantities shown: 48 g of "
                  "magnesium makes 80 g of magnesium oxide.",
                  "12 g of magnesium is 12 ÷ 48 = 0.25 of that, so it makes 0.25 × 80 = 20 g of "
                  "magnesium oxide."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: write each atom's A<sub>r</sub> times how many there "
             "are, then add.",
             "<strong>Explain</strong>: say which atoms are counted and why the totals match.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
