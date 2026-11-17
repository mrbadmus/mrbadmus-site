# -*- coding: utf-8 -*-
"""Conservation of mass and balanced equations, in the lean shape. Spec table:
ks4-conservation-of-mass.md.

LEGACY (batch 3). The ladder (Ks4Ladder, r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank), so its fixes are in
quiz-conservation-of-mass.json, not here. The CFIFA examples and questions (`cfifa` slot) are the
page's own. The two logic_edits below keep each rung in its position, so the rung ids survive.
"""

LOGIC_EDITS = [
    # Rung 3 (chain). The first two links were two independent facts, so either order was right.
    # Mide's rule: one right order only. The second link now starts "So" and builds on the first.
    ("links: ['No atoms are made or destroyed: the atoms of the reactants are only rearranged "
     "into the products.', 'The flask is sealed, so no atoms can get in or out.', 'So the total "
     "mass inside the flask stays the same.'],",
     "links: ['No atoms are made or destroyed in a reaction. The atoms of the reactants are only "
     "rearranged into the products.', 'So the products contain exactly the same atoms as the "
     "reactants, and the sealed flask stops any of them getting in or out.', 'So the total mass "
     "inside the flask stays the same.'],"),
    # Rung 2, Foundation version: the unit chips offered "mol" and "g/mol", which are Higher-only
    # units (8464 5.3.2.1 / 8462 4.3.2.1, HT only). Same answer, same correct unit (g).
    ("answer: 2.2, tol: 0.05, unit: 'g', units: ['g', 'kg', 'mol', 'g/mol']",
     "answer: 2.2, tol: 0.05, unit: 'g', units: ['g', 'kg', 'cm³', 'g/dm³']"),
]

LESSON = {
    "slug": "conservation-of-mass",
    "start": {
        "setup": "Methane and oxygen are sealed inside a flask on a balance. A spark makes the "
                 "methane burn.",
        "question": "If you had to guess, once the flask has cooled, does the reading go down or "
                    "stay the same?",
        "options": [
            ("It goes down",
             "It stays the same. Nothing can get in or out of the sealed flask, and the atoms are "
             "only rearranged."),
            ("It stays the same",
             "It stays the same. Nothing can get in or out of the sealed flask, and the atoms are "
             "only rearranged."),
        ],
        "answer": 1,
    },
    "words": ["conservation of mass", "reactants", "products", "balanced equation"],
    "knowledge": [
        {"kind": "card", "title": "The law of conservation of mass",
         "body": ["The law of conservation of mass states that no atoms are lost or made during a "
                  "chemical reaction, so the mass of the products equals the mass of the "
                  "reactants.",
                  "In a reaction, bonds break and new bonds form. The same atoms are only "
                  "rearranged into new substances."]},
        {"kind": "card", "title": "Using it to find a missing mass",
         "body": ["total mass of reactants = total mass of products",
                  "24 g of magnesium reacts with 16 g of oxygen. 24 + 16 = 40 g of magnesium "
                  "oxide forms.",
                  "If you know every mass but one, add up the side you know. Then subtract to "
                  "find the missing mass."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Balanced symbol equations",
         "body": ["Because no atoms are lost or made, a symbol equation must be balanced.",
                  "A balanced equation has the same number of atoms of each element on both sides."]},
        {"kind": "card", "title": "Big numbers and small numbers",
         "body": [{"points": [
             "A big number in front of a formula multiplies the whole formula. 2H₂O is 4 H atoms "
             "and 2 O atoms.",
             "A small number written low in a formula counts the atom just before it. H₂O has "
             "2 H atoms and 1 O atom.",
             "A small number after a bracket multiplies everything inside the bracket. Ca(OH)₂ "
             "has 1 Ca, 2 O and 2 H.",
             "To balance an equation, change only the big numbers. Never change a formula.",
         ]}]},
        {"kind": "reveal", "title": "Count the atoms",
         "cols": ["Atoms shown"],
         "rows": [
             ("H₂O", "2 H and 1 O"),
             ("2H₂O", "4 H and 2 O"),
             ("Ca(OH)₂", "1 Ca, 2 O and 2 H"),
             ("2Fe₂O₃", "4 Fe and 6 O"),
         ]},
        {"kind": "card", "title": "Balancing, step by step",
         "body": [{"points": [
             "Write the correct formulae: H₂ + O₂ → H₂O",
             "Count the atoms. Left: 2 H and 2 O. Right: 2 H and 1 O. The oxygen does not balance.",
             "Put a 2 in front of H₂O: H₂ + O₂ → 2H₂O. The right is now 4 H and 2 O.",
             "Put a 2 in front of H₂: 2H₂ + O₂ → 2H₂O. Both sides now have 4 H and 2 O. "
             "Balanced.",
         ]}]},
        {"kind": "card", "title": "Word equations, symbol equations and state symbols",
         "body": ["A word equation names the substances:",
                  "magnesium + hydrochloric acid → magnesium chloride + hydrogen",
                  "A symbol equation uses their formulae, and is balanced:",
                  "Mg + 2HCl → MgCl₂ + H₂",
                  "State symbols show the state of each substance: (s) solid, (l) liquid, (g) gas "
                  "and (aq) aqueous, which means dissolved in water.",
                  "Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g)"]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Balance H₂ + O₂ → H₂O by writing H₂O₂.",
              "Never change a formula. H₂O₂ is a different substance. Change only the big numbers."),
             ("2H₂ + O₂ → 2H₂O has three molecules on the left and two on the right, so the mass "
              "goes down.",
              "Mass depends on the atoms. There are 4 H and 2 O on each side, so the mass stays "
              "the same."),
             ("2H₂O has 2 hydrogen atoms.",
              "The 2 in front multiplies the whole formula: 4 H and 2 O."),
         ]}]},
    ],
    "key_fact": "No atoms are lost or made during a chemical reaction, so the mass of the products "
                "equals the mass of the reactants. A balanced symbol equation shows the same number "
                "of atoms of each element on both sides.",
    "deeper": [
        {"kind": "card", "title": "Seeing it on a balance",
         "body": ["Lead nitrate solution and potassium iodide solution are mixed in a flask on a "
                  "balance. A yellow solid forms, but the reading does not change.",
                  "Pb(NO₃)₂(aq) + 2KI(aq) → PbI₂(s) + 2KNO₃(aq)",
                  "No gas is made, so nothing leaves the flask."]},
        {"kind": "card", "title": "The big numbers are amounts in moles", "routes": ["CH", "TH"],
         "body": ["2H₂ + O₂ → 2H₂O means 2 moles of H₂ react with 1 mole of O₂ to give 2 moles of "
                  "H₂O."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Balance</strong>: put numbers in front of formulae until every element has "
             "the same number of atoms on each side.",
             "<strong>Write</strong>: correct formulae, balancing numbers, and state symbols when "
             "the question asks for them.",
             "<strong>Calculate</strong>: show each line of working and give the unit.",
             "<strong>Explain</strong>: give each reason as a step that leads to the next.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
}
