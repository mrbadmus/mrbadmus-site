# -*- coding: utf-8 -*-
"""Atom economy, in the lean shape. Spec table: ks4-atom-economy.md.

LEGACY (batch 3, Ks4Ladder). Routes TF and TH only (8462 4.3.3.2, chemistry only; choosing a
reaction pathway is HT only). The ladder stays from the Design page; Rung 2 and Rung 4 are
already route-aware (TH gets the titanium calculation and the 6-mark "evaluate" on the
fermentation / hydration table). The practice set reads the route's `quiz` list
(`K.bank(slug, R.route)`, shown when the list is not empty), so its five questions per route are
in quiz-atom-economy.json. The `cfifa` slot shows the legacy page's own cfExamples (ethanol from
the subtopic `fifas`, then copper) and its route-aware cfQuestions (ae-q1, ae-q2).

TH Rung 4 asks pupils to "Use the data in the Choose a route table". The legacy table goes with
its section, so the record carries the same rows as a TH-only reveal table titled
"Choose a route".
"""

LOGIC_EDITS = [
    # Rung 1 (atom-economy#r1): credited option visibly the longest (79 against 72). Trimmed to
    # 73; same meaning, same position and index.
    ("{ text: 'The percentage of the mass of the reactants that ends up in the desired product', correct: true",
     "{ text: 'The percentage of the reactants’ mass that ends up in the desired product', correct: true"),
    # Rung 1: a reply named "the strip", the mass-strip activity this lean page no longer has.
    ("'That is the waste share, the other part of the strip. Atom economy is the useful share.'",
     "'That is the waste share. Atom economy is the useful share.'"),
    # Rung 3 (atom-economy#r3): links 1 and 2 could be read in either order. "So" makes the
    # single product the result of the addition reaction, so only one order is right.
    ("'Ethanol is the only product formed.'",
     "'So ethanol is the only product formed.'"),
    # Examiner SHOULD FIX (13 Nov), exactly as in EXAMINER.md / _exam/proposed.py. Foundation rung 2 unit chips: no 'g/mol'.
    ("answer: 72.0, tol: 0.15, unit: '%', units: ['%', 'g', 'g/mol', 'no unit']",
     "answer: 72.0, tol: 0.15, unit: '%', units: ['%', 'g', 'kg', 'no unit']"),
]

LESSON = {
    "slug": "atom-economy",
    "start": {
        "setup": "Factory A makes ethanol by fermenting sugar: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂. "
                 "Factory B adds steam to ethene: C₂H₄ + H₂O → C₂H₅OH.",
        "question": "If you had to guess, which factory turns more of its starting mass into "
                    "ethanol?",
        "options": [
            ("Factory A",
             "Factory B. Ethanol is its only product. Factory A also makes carbon dioxide, which "
             "it does not want."),
            ("Factory B",
             "Factory B. Ethanol is its only product. Factory A also makes carbon dioxide, which "
             "it does not want."),
        ],
        "answer": 1,
    },
    "words": ["atom economy", "desired product", "by-product", "sustainable development"],
    "knowledge": [
        {"kind": "card", "title": "What atom economy means",
         "body": ["The atom economy (atom utilisation) is a measure of the amount of starting "
                  "materials that end up as useful products.",
                  "It comes from the balanced equation, so you can work it out before the "
                  "reaction is ever run."]},
        {"kind": "card", "title": "The equation",
         "body": ["% atom economy = (relative formula mass of desired product from equation ÷ "
                  "sum of relative formula masses of all reactants from equation) × 100",
                  {"points": ["Use the balancing numbers: 2Fe counts as 2 × 56 = 112.",
                              "Add up every reactant on the bottom, not just one.",
                              "Mass is conserved, so the sum of the M<sub>r</sub> of the reactants "
                              "equals the sum of the M<sub>r</sub> of the products."]},
                  "You need to remember this equation."]},
        {"kind": "reveal", "title": "Three reactions (M<sub>r</sub> or A<sub>r</sub> in brackets)",
         "cols": ["Working", "Atom economy"],
         "rows": [
             ("Making ethanol: C₂H₄ (28) + H₂O (18) → C₂H₅OH (46)",
              "46 ÷ (28 + 18) × 100", "100%"),
             ("Making calcium oxide: CaCO₃ (100) → CaO (56) + CO₂ (44)",
              "56 ÷ 100 × 100", "56%"),
             ("Making iron: Fe₂O₃ (160) + 3CO (28) → 2Fe (56) + 3CO₂ (44)",
              "(2 × 56) ÷ (160 + 3 × 28) × 100", "45.9%"),
         ]},
        {"kind": "card", "title": "One product means 100%",
         "body": ["When a reaction makes only one product, such as an addition reaction, every "
                  "atom in the reactants ends up in the desired product.",
                  "Its atom economy is 100%."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Why a high atom economy matters",
         "body": ["It is important for sustainable development and for economic reasons to use "
                  "reactions with high atom economy.",
                  {"points": ["Less of the starting materials is wasted, so raw materials last "
                              "longer.",
                              "There is less waste to deal with.",
                              "It costs less to make the same mass of product."]}]},
        {"kind": "reveal", "title": "Atom economy and percentage yield",
         "cols": ["Atom economy", "Percentage yield"],
         "rows": [
             ("Worked out from", "The balanced equation", "The mass of product actually made"),
             ("Can change from one run to the next", "No", "Yes"),
             ("Tells you", "How much of the starting mass can end up in the desired product",
              "How much product you made compared with the maximum"),
         ]},
        {"kind": "card", "title": "Choosing a reaction pathway", "routes": ["TH"],
         "body": ["Chemists choose a reaction pathway using the atom economy together with the "
                  "yield, the rate, the equilibrium position and how useful any by-products are.",
                  "Atom economy alone does not decide it. A by-product that can be sold or used "
                  "is not wasted."]},
        {"kind": "reveal", "title": "Choose a route", "routes": ["TH"],
         "cols": ["Fermentation", "Hydration of ethene"],
         "rows": [
             ("Raw material", "Sugar from crops (renewable)", "Ethene from crude oil (finite)"),
             ("Atom economy", "51%", "100%"),
             ("Conditions", "About 30 °C, normal pressure", "300 °C and 60–70 atm"),
             ("Rate", "Slow, in batches", "Fast and continuous"),
             ("Product", "Dilute ethanol that must be distilled", "Pure ethanol"),
             ("By-product", "Carbon dioxide", "None"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Divide by the mass of the waste product.",
              "Divide by the sum of the M<sub>r</sub> of all the reactants."),
             ("2NaCl → 2Na + Cl₂, so the top is 23.",
              "The equation makes 2Na, so the top is 2 × 23 = 46."),
             ("Atom economy is how much product you collect.",
              "That is percentage yield. Atom economy comes from the equation."),
             ("An atom economy of more than 100%.",
              "The desired product can never have more mass than all the reactants."),
         ]}]},
    ],
    "key_fact": "% atom economy = (M<sub>r</sub> of the desired product from the equation ÷ sum of "
                "the M<sub>r</sub> of all the reactants) × 100. A high atom economy means less "
                "waste, which matters for sustainable development and for economic reasons.",
    "deeper": [
        {"kind": "card", "title": "One equation, three useful products",
         "body": ["Electrolysing brine: 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂.",
                  "The reactants add up to 2 × 58.5 + 2 × 18 = 153.",
                  {"points": ["Sodium hydroxide: 80 ÷ 153 × 100 = 52.3%",
                              "Chlorine: 71 ÷ 153 × 100 = 46.4%",
                              "Hydrogen: 2 ÷ 153 × 100 = 1.3%"]},
                  "All three products are sold, so very little of the mass is wasted."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: show the working from the equation and give the answer "
             "as a percentage, usually to 3 significant figures.",
             "<strong>Give</strong>: one short answer.",
             "<strong>Explain</strong>: give the reason as linked steps.",
             "<strong>Evaluate</strong> (Higher): use the data for both sides, weigh them, and end "
             "with a justified conclusion.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
}
