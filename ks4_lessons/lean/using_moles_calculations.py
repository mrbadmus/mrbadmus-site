# -*- coding: utf-8 -*-
"""Using moles: calculations and limiting reactants, in the lean shape.
Spec table: ks4-using-moles-calculations.md.

LEGACY (batch 2, Ks4Ladder). Routes CH and TH only (8464 5.3.2.3 and 5.3.2.4 / 8462 4.3.2.3 and
4.3.2.4, all HT only). The ladder stays from the Design page. The practice set reads the
route's `quiz` list (`K.bank(slug, R.route)`), so its five questions per route are in
quiz-using-moles-calculations.json. The CFIFA examples and questions (`cfifa`) are the legacy
page's own: two balancing-from-masses examples, the limiting-reactant example from the subtopic
`fifas`, and questions um-q1, um-q2.

The page's eyebrow is already route-aware (`{{ eyebrowLine }}`), so it needs no edit.
Moles in solution (mol/dm³, 8462 4.3.4) left this page: it is taught in Concentration of
solutions.
"""

LOGIC_EDITS = [
    # Rung 1 (using-moles-calculations#r1): the reply to "fewest moles" named "Mix A", the
    # reaction bench this lean page no longer has. Option texts unchanged (keys kept).
    ("'Moles must be compared with the equation ratio. In Mix A, magnesium had fewer moles and was still in excess.'",
     "'Moles must be compared with the equation ratio. A reactant with fewer moles can still be in excess.'"),
]

LESSON = {
    "slug": "using-moles-calculations",
    "start": {
        "setup": "Magnesium reacts with hydrochloric acid: Mg + 2HCl → MgCl₂ + H₂. A student mixes "
                 "2.4 g of magnesium with 3.65 g of hydrogen chloride.",
        "question": "If you had to guess, which one runs out first?",
        "options": [
            ("The magnesium",
             "The hydrogen chloride. There is 0.1 mol of each, but every mole of magnesium needs "
             "two moles of hydrogen chloride."),
            ("The hydrogen chloride",
             "The hydrogen chloride. There is 0.1 mol of each, but every mole of magnesium needs "
             "two moles of hydrogen chloride."),
        ],
        "answer": 1,
    },
    "words": ["balancing numbers", "limiting reactant", "excess", "whole number ratio"],
    "knowledge": [
        {"kind": "card", "title": "Balancing an equation from masses",
         "body": ["The balancing numbers in a symbol equation can be calculated from the masses "
                  "of reactants and products by converting the masses in grams to amounts in "
                  "moles and converting the numbers of moles to simple whole number ratios.",
                  {"points": ["Convert each mass in grams to moles: n = m ÷ M<sub>r</sub>.",
                              "Divide every number of moles by the smallest one.",
                              "If you get a .5, double every number.",
                              "The whole numbers are the balancing numbers."]},
                  "Use each formula as written: hydrogen gas is H₂ (M<sub>r</sub> 2), oxygen gas "
                  "is O₂ (M<sub>r</sub> 32), chlorine gas is Cl₂ (M<sub>r</sub> 71)."]},
        {"kind": "reveal",
         "title": "11.2 g of iron reacts with 21.3 g of chlorine to make 32.5 g of iron chloride. "
                  "Fe + Cl₂ → FeCl₃",
         "cols": ["Moles", "÷ smallest"],
         "rows": [
             ("Fe (A<sub>r</sub> 56)", "11.2 ÷ 56 = 0.20", "1"),
             ("Cl₂ (M<sub>r</sub> 71)", "21.3 ÷ 71 = 0.30", "1.5"),
             ("FeCl₃ (M<sub>r</sub> 162.5)", "32.5 ÷ 162.5 = 0.20", "1"),
         ]},
        {"kind": "card", "title": "Whole numbers only",
         "body": ["1 : 1.5 : 1 has a .5 in it, so double every number: 2 : 3 : 2.",
                  "2Fe + 3Cl₂ → 2FeCl₃",
                  "Check: 6 chlorine atoms on each side. Never round 1.5 up or down."]},
        {"kind": "card", "title": "Limiting reactants",
         "body": ["In a chemical reaction involving two reactants, it is common to use an excess "
                  "of one of the reactants to ensure that all of the other reactant is used.",
                  "The reactant that is completely used up is called the limiting reactant "
                  "because it limits the amount of products.",
                  "The other reactant is in excess. Some of it is left over."]},
        {"kind": "card", "title": "Finding the limiting reactant",
         "body": [{"points": ["Convert each reactant's mass to moles.",
                              "Use the balancing numbers to work out how many moles of the second "
                              "reactant the first one needs.",
                              "If there is less than that, the second reactant is limiting. If "
                              "there is more, the first reactant is limiting."]},
                  "Mg + 2HCl → MgCl₂ + H₂. 2.4 g of Mg is 0.1 mol and 3.65 g of HCl is 0.1 mol.",
                  "0.1 mol of Mg needs 0.2 mol of HCl. There is only 0.1 mol, so HCl is the "
                  "limiting reactant and some magnesium is left over."]},
        {"kind": "reveal", "title": "Which reactant runs out first: Mg + 2HCl → MgCl₂ + H₂",
         "cols": ["HCl needed", "Limiting reactant"],
         "rows": [
             ("0.10 mol Mg + 0.30 mol HCl", "0.20 mol", "Magnesium"),
             ("0.10 mol Mg + 0.15 mol HCl", "0.20 mol", "Hydrogen chloride"),
             ("0.05 mol Mg + 0.08 mol HCl", "0.10 mol", "Hydrogen chloride"),
             ("1.2 g Mg + 7.3 g HCl", "0.05 mol of Mg needs 0.10 mol. There is 0.20 mol.",
              "Magnesium"),
         ]},
        {"kind": "card", "title": "The limiting reactant sets the amount of product",
         "body": ["Work out the product from the limiting reactant only.",
                  "0.1 mol of HCl makes 0.1 × 1 ÷ 2 = 0.05 mol of H₂, which is "
                  "0.05 × 2 = 0.1 g of hydrogen.",
                  "Adding more of the reactant in excess makes no more product.",
                  "Doubling the limiting reactant, with the other still in excess, doubles the "
                  "amount of product."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The reactant with the smaller mass is the limiting reactant.",
              "Convert to moles and compare with the ratio in the equation."),
             ("The reactant with fewer moles is the limiting reactant.",
              "0.05 mol of Mg needs 0.10 mol of HCl. With 0.08 mol of HCl, the HCl runs out first."),
             ("A ratio of 1 : 1.5 : 1 rounds to 1 : 2 : 1.",
              "Double it to 2 : 3 : 2. Balancing numbers are whole numbers."),
             ("Hydrogen gas has M<sub>r</sub> 1.",
              "Hydrogen gas is H₂, so M<sub>r</sub> = 2."),
         ]}]},
    ],
    "key_fact": "To balance an equation from masses, convert each mass in grams to moles and turn "
                "the moles into the simplest whole number ratio. The limiting reactant is the "
                "reactant that is completely used up, so it limits the amount of products.",
    "deeper": [
        {"kind": "card", "title": "Excess in the lab",
         "body": ["When you make a salt from an insoluble metal oxide and an acid, you add the "
                  "oxide in excess.",
                  "Then all of the acid reacts. The leftover oxide is filtered off."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Balance</strong>: find the moles of every substance, divide by the smallest, "
             "and put the whole numbers into the equation.",
             "<strong>Determine</strong>: use the data to decide which reactant runs out.",
             "<strong>Calculate</strong>: show the moles, the ratio, the moles of product, then "
             "the mass with its unit.",
             "<strong>Explain</strong>: link the limiting reactant to the amount of product.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
