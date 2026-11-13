# -*- coding: utf-8 -*-
"""Elements, in the lean shape. Spec table: docs/lessons/wave1/ks3-elements.md."""

LESSON = {
    "slug": "elements",
    "start": {
        "setup": None,
        "question": "If you had to guess, how would you test if a sample is an element?",
        "options": [
            ("Try to break it down", "Try to break it down. If anything simpler comes out, it is not an element."),
            ("Look at it closely", "Try to break it down. If anything simpler comes out, it is not an element."),
        ],
        "answer": 0,
    },
    "words": ["element", "periodic table", "compound", "mixture"],
    "word_defs": {
        "element": "A substance made of only one kind of atom.",
        "periodic table": "The table that lists every known element, with its symbol.",
        "compound": "Two or more elements chemically joined together.",
        "mixture": "Two or more substances mixed together, not chemically joined.",
    },
    "knowledge": [
        {"kind": "card", "title": "What an element is",
         "body": ["An element is a substance made of only one kind of atom.",
                  "Copper is only copper atoms. Sulfur is only sulfur atoms.",
                  "An element cannot be broken down into anything simpler.",
                  "There are over 100 known elements."]},
        {"kind": "card", "title": "Atoms or molecules",
         "body": ["In some elements, like copper, the atoms are joined in one giant structure.",
                  "In others, the atoms join in small groups called molecules.",
                  "Each oxygen molecule is two oxygen atoms joined together.",
                  "Oxygen is still an element. It has only one kind of atom.",
                  {"figure": "c2-element-particles"}]},
        {"kind": "card", "title": "The periodic table",
         "body": ["Every known element is listed in the periodic table.",
                  "Each element has its own name and symbol.",
                  "Most elements are metals, but not all.",
                  "Sulfur, oxygen and carbon are non-metals.",
                  "Water, air and brass are not in the periodic table. None of them is an element."]},
        {"kind": "card", "title": "Testing for an element",
         "body": ["Looks cannot tell you. Different substances can look alike.",
                  "Instead, try to break the substance down.",
                  "Heat it on its own, or pass electricity through it.",
                  "If anything simpler comes out, it is not an element.",
                  "Electricity splits water into hydrogen and oxygen. So water is not an element."]},
        {"kind": "reveal", "title": "Element or not",
         "cols": ["Element", "Why"],
         "rows": [
             ("Copper", "Yes", "Nothing simpler can be got out of it."),
             ("Sulfur", "Yes", "It is a non-metal, but it is only sulfur atoms."),
             ("Sodium", "Yes", "It reacts with water, but the hydrogen given off comes from the water."),
             ("Water", "No, a compound", "Electricity splits it into hydrogen and oxygen."),
             ("Brass", "No, a mixture", "It is copper and zinc mixed together."),
             ("Air", "No, a mixture", "It is a mix of gases, mostly nitrogen and oxygen."),
         ]},
        {"kind": "card", "title": "When the list changed",
         "body": ["Some substances were once thought to be elements.",
                  "Heating and acids could not split them.",
                  "Then chemists used electricity, and these substances split up.",
                  "So they were never elements. The list was wrong.",
                  "The early chemists were not careless. They listed what their methods could show.",
                  "The list of elements depends on the methods we have."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Brass is a metal, so it is an element.",
              "Brass is copper and zinc mixed. Being a metal does not make something an element."),
             ("Anything pure is an element.",
              "Pure means only one substance. Pure water is a compound."),
             ("Sodium reacting with water means it is breaking down.",
              "The sodium joins with the water. The hydrogen given off comes from the water."),
         ]}]},
    ],
    "key_fact": "An element is a substance made of only one kind of atom. It cannot be broken down "
                "into anything simpler. Every known element is listed in the periodic table.",
    "deeper": [
        {"kind": "card", "title": "Humphry Davy",
         "body": ["In 1807, Humphry Davy used electricity to split substances that heat could not.",
                  "He was the first to make pure sodium and potassium."]},
        {"kind": "card", "title": "Elements in your body",
         "body": ["Most of your body is oxygen, carbon, hydrogen and nitrogen.",
                  "Most of the oxygen and hydrogen is in water."]},
    ],
    "try": None,
    "ladder_stem": {
        "apply": "A student tests an unknown silvery solid in four ways. One test melts it, then passes "
                 "electricity through it. Which result shows it is not an element?",
        "explain": "A student says gold is an element because it is shiny and expensive. They say "
                   "brass is not, because it is cheap. They are right about both, for the wrong reasons. "
                   "Explain why. Give the reasoning that works.",
        "produce": "Before electricity was used, chemists thought some compounds were elements. Electricity "
                   "later split them up. Explain how a new method can take a substance off the list of "
                   "elements. Were the earlier chemists careless?",
    },
    "ladder_ticks": [
        ["Notes that getting the right answer for the wrong reason will fail on the next sample.",
         "Gives the reasoning that works: test whether the substance can be broken down."],
        ["Says gold cannot be broken down into anything simpler, and that this is the reason.",
         "Says gold cannot be broken down into anything simpler by chemical means."],
        ["Says brass is made of copper and zinc, so it is more than one kind of atom.",
         "Says brass is copper and zinc, so it has more than one kind of atom."],
        ["Says a substance is called an element when nothing simpler can be got out of it by the methods "
         "available.",
         "Says a substance counts as an element while no method can split it."],
        ["Says a new method — electricity — could take apart things that heating and acids could not.",
         "Says electricity could split things that heating and acids could not."],
        ["Draws the general point — the list depends on what can be done, so it can change.",
         "Says the list depends on the methods we have, so it can change."],
    ],
    "figures": [
        {"id": "c2-element-particles", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Two elements and a compound",
         "desc": "Three boxes side by side. The first, labelled Copper, element, is filled with "
                 "identical orange circles marked Cu, packed in touching rows. The second, labelled "
                 "Oxygen, element, holds five separate pairs of red circles marked O, each pair joined. "
                 "The third, labelled Water, compound, holds five separate groups, each one red O "
                 "circle joined to two small white H circles.",
         "caption": "Copper and oxygen each have one kind of atom. Water has two.",
         "data": {"boxes": [
             {"label": "Copper", "tag": "element", "layout": "grid", "rows": 4, "cols": 5, "atom": "Cu"},
             {"label": "Oxygen", "tag": "element", "layout": "spread", "groups": [["O", "O"]] * 5},
             {"label": "Water", "tag": "compound", "layout": "spread", "shape": "bent",
              "groups": [["H", "O", "H"]] * 5},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Sulfur, oxygen and carbon are elements, and none of them is a metal.",
            1: "Melting and boiling do not break a substance down.",
            3: "Some elements are made in laboratories. They are still elements.",
        },
        "apply": {
            1: "Brass conducts too, and it is a mixture. Conducting shows nothing here.",
            2: "Brass and steel are shiny and can be hammered flat. Both are mixtures.",
            3: "Pure compounds melt at a definite temperature too. Water melts at 0 °C.",
        },
    },
}
