# -*- coding: utf-8 -*-
"""Reactions rearrange atoms, in the lean shape. Spec table: docs/lessons/wave2/ks3-reactions-rearrange-atoms.md."""

LESSON = {
    "slug": "reactions-rearrange-atoms",
    "start": {
        "setup": "Hydrogen and oxygen are both colourless gases. When they burn together, they make water.",
        "question": "If you had to guess, would the two gases, mixed in one balloon and left alone, "
                    "turn into water on their own?",
        "options": [
            ("No, they need starting",
             "Right. The mixture can sit for a long time. A flame or spark breaks the first joins."),
            ("Yes, on their own",
             "They need starting. The atoms in each gas are joined in pairs. Those joins must break first."),
        ],
        "answer": 0,
    },
    "words": ["atom", "reactant", "product", "rearrange"],
    "word_defs": {
        "atom": "The smallest particle of an element.",
        "reactant": "A substance you start with in a reaction.",
        "product": "A substance a reaction makes.",
        "rearrange": "To keep the same things but put them together in a new way.",
    },
    "knowledge": [
        {"kind": "card", "title": "Atoms are joined together",
         "body": ["Everything is made of atoms.",
                  "In most substances, atoms are joined to other atoms.",
                  "In hydrogen gas, the atoms are joined in pairs. Each pair is one particle.",
                  "Oxygen gas is made of pairs of oxygen atoms too.",
                  "A water particle is one oxygen atom joined to two hydrogen atoms."]},
        {"kind": "card", "title": "What a reaction does to atoms",
         "body": ["In a chemical reaction, the joins between atoms break.",
                  "The same atoms then join up in a new way.",
                  "The new particles make new substances, the products.",
                  {"figure": "c4-water-steps"},
                  "The middle box is a model. In a real reaction, the atoms are never all loose at once."]},
        {"kind": "card", "title": "Count the atoms",
         "body": ["No atoms are made or destroyed in a chemical reaction.",
                  "Each atom stays the same kind of atom. A hydrogen atom stays a hydrogen atom.",
                  "So the products have exactly the same atoms as the reactants.",
                  "Hydrogen and oxygen: 4 hydrogen and 2 oxygen atoms before. The same 4 and 2 after.",
                  "This is why the total mass stays the same in a reaction."]},
        {"kind": "card", "title": "Burning methane",
         "body": ["Methane is the gas burnt on a gas hob.",
                  "One methane particle is a carbon atom joined to four hydrogen atoms.",
                  "It reacts with oxygen to make carbon dioxide and water.",
                  {"figure": "c4-methane-steps"},
                  "All 9 atoms are used. None are left over, and none are new."]},
        {"kind": "card", "title": "Burning magnesium",
         "body": ["Magnesium burns with a bright white light. It leaves a white powder, magnesium oxide.",
                  "Magnesium atoms join with oxygen atoms from the air.",
                  "Magnesium oxide is a compound: two elements chemically joined.",
                  "There is no such thing as a magnesium oxide atom.",
                  "The powder is heavier than the ribbon. The oxygen atoms add their mass.",
                  {"points": ["mass of magnesium + mass of oxygen = mass of magnesium oxide"]}]},
        {"kind": "card", "title": "A reaction cannot make new atoms",
         "body": ["A reaction can only use the atoms it starts with.",
                  "Hydrogen and oxygen can make water.",
                  "They can never make ammonia, as ammonia contains nitrogen atoms.",
                  "Gold is an element. Gold can only come out of a reaction if gold went in.",
                  "Changing the heat or pressure cannot help. No chemical reaction makes new atoms.",
                  "Turning one element into another needs a nuclear reaction. That changes the atoms themselves."]},
        {"kind": "reveal", "title": "In a chemical reaction",
         "cols": ["What happens"],
         "rows": [
             ("The joins between atoms", "They break, and new joins form"),
             ("The atoms themselves", "They stay the same kind of atom"),
             ("The number of each kind of atom", "It stays the same"),
             ("The substances", "New substances are made"),
             ("The total mass", "It stays the same"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("When magnesium burns, its atoms turn into magnesium oxide atoms.",
              "There are no magnesium oxide atoms. Magnesium atoms join to oxygen atoms.",
              "REACT-03"),
             ("New atoms can be made if the conditions are right.",
              "No chemical reaction makes new atoms, whatever the conditions.",
              "REACT-04"),
             ("When something burns, its atoms are destroyed.",
              "Its atoms join with oxygen. They are still there, in the products."),
             ("The water from burning methane is made of new atoms.",
              "Its hydrogen atoms were in the methane. Its oxygen atoms were in the air."),
         ]}]},
    ],
    "key_fact": "In a chemical reaction, the joins between atoms break and new joins form. No atoms "
                "are made or destroyed, so the same atoms are there before and after.",
    "deeper": [
        {"kind": "card", "title": "Why some reactions need starting",
         "body": ["Breaking the joins between atoms takes energy.",
                  "Making new joins gives energy out.",
                  "Hydrogen and oxygen give out a lot of energy when they react.",
                  "But some joins must break before any new ones can form.",
                  "A spark or flame breaks the first few. The energy given out breaks the rest."]},
        {"kind": "card", "title": "Same atoms, different substance",
         "body": ["Water and hydrogen peroxide are both made of hydrogen and oxygen atoms.",
                  "A hydrogen peroxide particle has one more oxygen atom than a water particle.",
                  "That makes it a different substance. It bleaches hair."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why no chemical reaction can make gold?",
    "connects_heading": None,
    "ks4_becomes": "Bond breaking and bond making as the energy story of a reaction, and balanced "
                   "symbol equations.",
    "figures": [
        {"id": "c4-water-steps", "kind": "diagram", "status": "drawn", "art": "c4-rearrange-steps",
         "title": "Hydrogen and oxygen rearranged into water",
         "desc": "Three boxes, one under the other, joined by drawn arrows. The first box, labelled "
                 "Before: hydrogen and oxygen, holds two pairs of joined white H circles and one pair "
                 "of joined red O circles. Under it: 4 hydrogen atoms, 2 oxygen atoms. An arrow "
                 "labelled joins break points to the second box, labelled Separate atoms, holding "
                 "four separate H circles and two separate O circles. Under it: the same counts. An "
                 "arrow labelled new joins form points to the third box, labelled After: water, "
                 "holding two water particles, each a red O circle with two white H circles joined "
                 "to it at an angle. Under it: 4 hydrogen atoms, 2 oxygen atoms.",
         "caption": "The same 6 atoms all the way through. Only the joins change.",
         "data": {
             "stages": [
                 {"label": "Before: hydrogen and oxygen",
                  "groups": [["H", "H"], ["H", "H"], ["O", "O"]],
                  "count": "4 hydrogen atoms, 2 oxygen atoms"},
                 {"label": "Separate atoms",
                  "groups": [["H"], ["H"], ["H"], ["H"], ["O"], ["O"]],
                  "count": "4 hydrogen atoms, 2 oxygen atoms"},
                 {"label": "After: water", "shape": "bent",
                  "groups": [["H", "O", "H"], ["H", "O", "H"]],
                  "count": "4 hydrogen atoms, 2 oxygen atoms"},
             ],
             "arrows": ["joins break", "new joins form"],
         }},
        {"id": "c4-methane-steps", "kind": "diagram", "status": "drawn", "art": "c4-rearrange-steps",
         "title": "Methane and oxygen rearranged into carbon dioxide and water",
         "desc": "Three boxes, one under the other, joined by drawn arrows. The first box, labelled "
                 "Before: methane and oxygen, holds one methane particle, a black C circle with four "
                 "white H circles joined to it above, below, left and right, and two pairs of joined "
                 "red O circles. Under it: 1 carbon, 4 hydrogen, 4 oxygen atoms. An arrow labelled "
                 "joins break points to the second box, labelled Separate atoms, holding one C, four "
                 "H and four O circles, all separate. An arrow labelled new joins form points to the "
                 "third box, labelled After: carbon dioxide and water. It holds one carbon dioxide "
                 "particle, a black C circle with a red O circle on each side in a line, and two water "
                 "particles. Under each box: 1 carbon, 4 hydrogen, 4 oxygen atoms.",
         "caption": "Every atom in the products was in the methane or the oxygen.",
         "data": {
             "stages": [
                 {"label": "Before: methane and oxygen",
                  "groups": [["C", "H", "H", "H", "H"], ["O", "O"], ["O", "O"]],
                  "shapes": ["cross", "straight", "straight"],
                  "count": "1 carbon, 4 hydrogen, 4 oxygen atoms"},
                 {"label": "Separate atoms",
                  "groups": [["C"], ["H"], ["H"], ["H"], ["H"], ["O"], ["O"], ["O"], ["O"]],
                  "count": "1 carbon, 4 hydrogen, 4 oxygen atoms"},
                 {"label": "After: carbon dioxide and water",
                  "groups": [["O", "C", "O"], ["H", "O", "H"], ["H", "O", "H"]],
                  "shapes": ["straight", "bent", "bent"],
                  "count": "1 carbon, 4 hydrogen, 4 oxygen atoms"},
             ],
             "arrows": ["joins break", "new joins form"],
         }},
    ],
    "ladder_stem": {
        "produce": "A student plans to make gold by reacting two cheap substances. They say nobody "
                   "has found the right conditions yet. Explain why the plan cannot work. Say what "
                   "would be needed instead.",
    },
    "ladder_ticks": [
        ["Says no atoms were created — the oxygen atoms already existed, in the air.",
         "Says no atoms were created. The oxygen atoms were already in the air."],
        ["Says conditions — heat, pressure, catalyst — change how a reaction goes, not which atoms exist.",
         "Says changing conditions, such as heat or pressure, cannot change which atoms there are."],
        ["Notes that weighing the air is what makes the sum come out right, and that this is why an open dish seems to gain mass.",
         "Says the oxygen was not weighed at the start, so the mass seems to appear."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "No atoms are made or destroyed in a reaction. Count them: the numbers match.",
            1: "Changing one kind of atom into another needs a nuclear reaction. Burning cannot do it.",
            2: "Then nothing would have happened. New joins are what make a reaction.",
        },
        "apply": {
            0: "Each water particle has two, but two water particles are made. That makes four.",
            2: "Burning does not destroy atoms. The hydrogen atoms end up in the water.",
            3: "Each water particle has only two hydrogen atoms. Two water particles hold four.",
        },
    },
}
