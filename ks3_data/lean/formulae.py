# -*- coding: utf-8 -*-
"""Formulae, in the lean shape. Spec table: docs/lessons/wave1/ks3-formulae.md."""

LESSON = {
    "slug": "formulae",
    "start": {
        "setup": "Water is H2O. Hydrogen peroxide, H2O2, bleaches hair and can burn skin.",
        "question": "If you had to guess, would bubbling oxygen through water make hydrogen peroxide?",
        "options": [
            ("Yes, it would", "No, it would not. Mixing does not join an extra oxygen atom into each water molecule."),
            ("No, it would not", "No, it would not. Mixing does not join an extra oxygen atom into each water molecule."),
        ],
        "answer": 1,
    },
    "words": ["formula", "molecule", "giant structure", "ratio"],
    "word_defs": {
        "formula": "Symbols and numbers showing the elements in a substance and how many atoms of each.",
        "molecule": "Two or more atoms chemically joined together, as one separate particle.",
        "giant structure": "A huge repeating pattern of joined particles, with no separate molecules.",
        "ratio": "How many of one thing there are for each of another.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a formula tells you",
         "body": ["A formula shows which elements are in a substance.",
                  "It also shows how many atoms of each there are.",
                  "A small number after a symbol counts the atoms of that element.",
                  "No number means one atom. A 1 is never written.",
                  {"points": ["H2O: two hydrogen atoms and one oxygen atom.",
                              "CO2: one carbon atom and two oxygen atoms."]}]},
        {"kind": "card", "title": "Molecules",
         "body": ["A molecule is two or more atoms chemically joined together.",
                  "Some elements are made of molecules, like oxygen, O2.",
                  "Many compounds are too, like water, H2O, and carbon dioxide, CO2.",
                  {"figure": "c2-molecules"}]},
        {"kind": "reveal", "title": "Reading a formula",
         "cols": ["Elements in it", "Atoms of each"],
         "rows": [
             ("H2O", "Hydrogen and oxygen", "2 hydrogen, 1 oxygen"),
             ("CO2", "Carbon and oxygen", "1 carbon, 2 oxygen"),
             ("SO2", "Sulfur and oxygen", "1 sulfur, 2 oxygen"),
             ("CH4", "Carbon and hydrogen", "1 carbon, 4 hydrogen"),
             ("CaCO3", "Calcium, carbon and oxygen", "1 calcium, 1 carbon, 3 oxygen"),
             ("CuSO4", "Copper, sulfur and oxygen", "1 copper, 1 sulfur, 4 oxygen"),
         ]},
        {"kind": "card", "title": "Writing a formula",
         "body": [{"points": ["Write the symbol for each element.",
                              "Count the atoms of each element in one molecule.",
                              "Write each count as a small number just after its symbol.",
                              "Leave out any 1."]},
                  "A small number counts atoms of the element just before it.",
                  "One carbon atom joined to four hydrogen atoms is CH4."]},
        {"kind": "card", "title": "Your turn",
         "body": ["This is one ammonia molecule.",
                  {"figure": "c2-ammonia"},
                  "Write its formula."]},
        {"kind": "reveal", "title": "The answer",
         "cols": ["Formula"],
         "rows": [("Ammonia", "NH3")]},
        {"kind": "card", "title": "Big numbers and small numbers",
         "body": ["A small number after a symbol counts atoms inside one molecule.",
                  "A big number in front counts whole molecules.",
                  "2H2O is two molecules of water.",
                  "H2O2 is one molecule of hydrogen peroxide, a different substance.",
                  {"figure": "c2-big-small"}]},
        {"kind": "card", "title": "Change a number, change the substance",
         "body": ["Each hydrogen peroxide molecule has one more oxygen atom than a water molecule.",
                  "That one atom makes it a different substance.",
                  "Water is safe to drink. Hydrogen peroxide is not.",
                  "Changing the atoms in a molecule needs a chemical reaction.",
                  "Hydrogen peroxide slowly breaks down into water and oxygen. That is a chemical reaction."]},
        {"kind": "card", "title": "Giant structures",
         "body": ["Salt, sodium chloride, has no separate molecules.",
                  "It is a giant structure: a huge repeating pattern of sodium and chlorine.",
                  "Its formula, NaCl, gives the ratio. There is one sodium for every chlorine.",
                  {"figure": "c2-salt-lattice"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The small number shows how much of the substance there is.",
              "It counts atoms in one molecule. Changing it makes a different substance."),
             ("2H2O and H2O2 are the same thing.",
              "2H2O is two water molecules. H2O2 is one molecule of a different substance."),
             ("NaCl is one molecule with one sodium and one chlorine.",
              "Salt is a giant structure. NaCl gives the ratio, one to one."),
         ]}]},
    ],
    "key_fact": "A formula shows which elements are in a substance and how many atoms of each. A small "
                "number counts atoms of the element just before it. A big number in front counts molecules.",
    "deeper": [
        {"kind": "card", "title": "Same ratio, different substance",
         "body": ["Glucose is C6H12O6. Ethanoic acid, in vinegar, is C2H4O2.",
                  "Both have one carbon atom for every two hydrogen atoms and one oxygen atom.",
                  "They are different substances, because their molecules are different."]},
    ],
    "try": None,
    "ladder_stem": {
        "explain": "Explain why H2O and H2O2 are different substances, and not different amounts of one "
                   "substance. Say what it takes to make water from hydrogen peroxide by removing an oxygen atom.",
        "produce": "A student writes salt as Na1Cl1. They say it means one particle with one sodium and "
                   "one chlorine atom. Two things are wrong. Say what they are. Write the formula a "
                   "chemist would use.",
    },
    "ladder_ticks": [
        ["Says each particle of hydrogen peroxide has one more oxygen atom than a particle of water.",
         "Says each hydrogen peroxide molecule has one more oxygen atom than a water molecule."],
        ["Says a change inside the particle makes a different substance, not more or less of the same one.",
         "Says changing the atoms in a molecule makes a different substance."],
        ["Says a 1 is never written — a symbol with no number after it already means one.",
         "Says a 1 is never written. A symbol with no number means one atom."],
        ["Says it is a giant structure of atoms in a repeating stack.",
         "Says salt is a giant structure, a huge repeating pattern."],
    ],
    "figures": [
        {"id": "c2-molecules", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Four molecules and their formulae",
         "desc": "Four molecules in a row, each with its formula and name underneath. Water, H2O: a red "
                 "O circle with two small white H circles joined to it at an angle. Carbon dioxide, CO2: "
                 "a black C circle joined to a red O circle on each side, in a straight line. Oxygen, "
                 "O2: two red O circles joined. Hydrogen peroxide, H2O2: two red O circles joined, with "
                 "a white H circle joined to each.",
         "caption": "Each formula counts the atoms in one molecule.",
         "data": {"boxes": [
             {"label": "H2O", "tag": "water", "layout": "single", "groups": [["H", "O", "H"]], "shape": "bent"},
             {"label": "CO2", "tag": "carbon dioxide", "layout": "single", "groups": [["O", "C", "O"]],
              "shape": "straight"},
             {"label": "O2", "tag": "oxygen", "layout": "single", "groups": [["O", "O"]]},
             {"label": "H2O2", "tag": "hydrogen peroxide", "layout": "single", "groups": [["H", "O", "O", "H"]],
              "shape": "chain"},
         ]}},
        {"id": "c2-big-small", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "2H2O and H2O2",
         "desc": "Two boxes side by side. The left box, labelled 2H2O, two molecules of water, holds two "
                 "separate water molecules, each a red O circle joined to two white H circles. Under it: "
                 "4 hydrogen atoms, 2 oxygen atoms. The right box, labelled H2O2, one molecule of hydrogen "
                 "peroxide, holds one molecule: two red O circles joined, with a white H circle on each. "
                 "Under it: 2 hydrogen atoms, 2 oxygen atoms.",
         "caption": "The big number counts molecules. The small numbers count atoms.",
         "data": {"boxes": [
             {"label": "2H2O", "tag": "two molecules of water", "layout": "spread",
              "shape": "bent",
              "groups": [["H", "O", "H"]] * 2, "count": "4 hydrogen atoms, 2 oxygen atoms"},
             {"label": "H2O2", "tag": "one molecule of hydrogen peroxide", "layout": "spread", "shape": "chain",
              "groups": [["H", "O", "O", "H"]], "count": "2 hydrogen atoms, 2 oxygen atoms"},
         ]}},
        {"id": "c2-salt-lattice", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Sodium chloride, a giant structure",
         "desc": "One box, labelled Sodium chloride, NaCl, filled edge to edge with touching circles in "
                 "rows and columns. Small purple circles marked Na and larger green circles marked Cl take "
                 "turns along every row and every column, and the pattern runs off every edge of the "
                 "box. Under it: one sodium for every chlorine.",
         "caption": "Salt has no separate molecules. NaCl gives the ratio.",
         "data": {"boxes": [
             {"label": "Sodium chloride, NaCl", "layout": "grid", "rows": 5, "cols": 6,
              "atoms": ["Na", "Cl"], "pattern": "alternate", "edges": "continue",
              "count": "one sodium for every chlorine"},
         ]}},
        {"id": "c2-ammonia", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "An ammonia molecule",
         "desc": "One box, labelled Ammonia, holding one molecule: a blue circle marked N in the middle, "
                 "with three small white circles marked H joined around it. No formula is written.",
         "caption": "Count the atoms of each element.",
         "data": {"boxes": [
             {"label": "Ammonia", "layout": "single", "groups": [["N", "H", "H", "H"]], "shape": "pyramid"},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Three is the number of elements. Add up the atoms of each element.",
            1: "Four is just the oxygen atoms. Add the two hydrogens and the sulfur.",
            2: "No number after S means one sulfur atom. So it is 2 + 1 + 4.",
        },
        "apply": {
            0: "The atoms are the same, but the molecules are different. That makes different substances.",
            1: "Both have two carbon atoms and four oxygen atoms. Neither has more.",
            3: "The 2 in front counts molecules. It does not make a mixture.",
        },
    },
}
