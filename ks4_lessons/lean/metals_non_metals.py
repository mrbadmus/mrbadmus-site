# -*- coding: utf-8 -*-
"""Metals and non-metals, in the lean shape. Spec table: ks4-metals-non-metals.md (AQA 8464 5.1.2.3 /
8462 4.1.2.3, word for word the same; no HT-only or chemistry-only lines).

LEGACY (batch 5). The ladder and the practice set (the page's own bankSrc) stay from the Design page;
their fixes are logic_edits. Every practice stem is kept. Batch-5 logic writes \\u escapes.

logic_edits (option text and feedback; every credited answer is the same answer):
  1. Practice Q1 (why metals conduct): credited option the longest (93). Now "They have delocalised
     electrons that can move" (45). Feedback plain, no capitals.
  2. Practice Q2 (SO2 is acidic): every option carried a dash; distractor 1 contradicted itself
     ("Metal, metal oxides are always basic" is a reason to say non-metal). Options rewritten with
     the same misconceptions; credited "Non-metal" (49, not the longest).
  3. Practice Q4 (graphite conducts): credited option the longest. Now "One electron from each
     carbon atom can move" (43); two distractors written out longer.
  4. Practice Q5 (Group 2): credited option the longest (53). Now "It is a metal that forms 2+
     ions" (32).
  5. Rung 1 Q2 (where metals are): credited option the longest (34 against 20); distractors longer.
  6. Rung 2 Q1 (7 outer electrons): credited "Non-metal; forms a 1- ion" was one character longer
     than any other; one distractor reworded so it is not the longest.
  7. Rung 3 chain 2 (chlorine): links 2 and 3 could be read in either order. Rewritten as a strict
     cause chain: 7 outer electrons and Group 7; gains 1 electron; forms Cl- and no positive ion, so
     a non-metal. Same ideas, one valid order.
"""

LOGIC_EDITS = [
    # 1. Practice Q1
    ("opts: [['Metals have delocalised (free) electrons that can move through the structure and carry charge', true],",
     "opts: [['They have delocalised electrons that can move', true],"),
    ("wrong_explanations: { 1: 'Atomic size does not determine conductivity \\u2014 it is the presence of FREE electrons, not large atoms, that allows charge to flow.', 2: 'Proton count determines the element, not conductivity. Non-metals also have many protons but are poor conductors.', 3: 'Solid metals conduct electricity \\u2014 not dissolved ions. Ionic conductivity in solution is different from metallic conductivity in a solid.' } },",
     "wrong_explanations: { 1: 'The size of the atoms is not the reason. Metals conduct because they have electrons that are free to move.', 2: 'The number of protons does not decide this. Many non-metal atoms have more protons and do not conduct.', 3: 'A solid metal conducts with no water present. Its delocalised electrons carry the charge.' } },"),
    # 2. Practice Q2
    ("opts: [['Non-metal \\u2014 non-metal oxides form acidic solutions when dissolved in water', true], ['Metal \\u2014 metal oxides are always basic', false], ['Metalloid \\u2014 SO\\u2082 is both acidic and basic', false], ['It could be either \\u2014 the acidity of its oxide doesn\\u2019t indicate the type of element', false]],",
     "opts: [['Non-metal: non-metal oxides form acidic solutions', true], ['Metal: all oxides dissolve to form acids', false], ['Metalloid: SO\\u2082 is both acidic and basic', false], ['Either: the oxide does not show the type of element', false]],"),
    ("wrong_explanations: { 1: 'Metal oxides are BASIC \\u2014 they neutralise acids. SO\\u2082 forms an acidic solution, which is the behaviour of NON-METAL oxides.', 2: 'SO\\u2082 is not amphoteric (both acidic and basic) \\u2014 it is distinctly acidic. Sulfur is clearly a non-metal.', 3: 'The type of oxide (acidic or basic) is a reliable indicator of whether the element is a metal or non-metal.' } },",
     "wrong_explanations: { 1: 'Metal oxides are basic: they neutralise acids. An acidic oxide comes from a non-metal.', 2: 'Sulfur dioxide is acidic, not both. Sulfur is a non-metal.', 3: 'An acidic oxide is good evidence that the element is a non-metal.' } },"),
    # 3. Practice Q4
    ("opts: [['One electron from each carbon atom is delocalised and can move', true], ['Carbon forms positive ions that move', false], ['Graphite contains metal atoms', false], ['All non-metals conduct electricity', false]],",
     "opts: [['One electron from each carbon atom can move', true], ['Carbon atoms form positive ions that move through it', false], ['Graphite has metal atoms mixed in with the carbon', false], ['All non-metals conduct electricity', false]],"),
    # 4. Practice Q5
    ("opts: [['It is a metal that loses 2 electrons to form a 2+ ion', true],",
     "opts: [['It is a metal that forms 2+ ions', true],"),
    # 5. Rung 1 Q2
    ("{ text: 'To the right and top', correct: false, reply: 'That is where the non-metals are.' },",
     "{ text: 'To the right and towards the top of the table', correct: false, reply: 'That is where the non-metals are.' },"),
    ("{ text: 'Only in the middle', correct: false, reply: 'Groups 1 and 2 are metals too. Most elements are metals.' }] }",
     "{ text: 'Only in the middle block of the table', correct: false, reply: 'Groups 1 and 2 are metals too. Most elements are metals.' }] }"),
    # 6. Rung 2 Q1
    ("{ text: 'Non-metal; forms no ions', correct: false,",
     "{ text: 'Non-metal; it forms no ions', correct: false,"),
    # 7. Rung 3 chain 2
    ("links: ['A chlorine atom has 7 electrons in its outer shell.', 'The number of outer electrons is the group number, so chlorine is in Group 7, on the right.', 'Chlorine gains 1 electron to form a negative ion; it does not form positive ions, so it is a non-metal.'],",
     "links: ['A chlorine atom has 7 outer electrons, so it is in Group 7, on the right of the table.', 'When chlorine reacts, it gains 1 electron to fill its outer shell.', 'So it forms a negative ion, Cl\\u207b, and never a positive ion: it is a non-metal.'],"),
    # Examiner fix round (26 Nov), M3: two replies did not answer the option they sit on.
    # Practice Q5, reply to "It does not form ions".
    ("3: 'Only Group 0 elements, with full outer shells, do not form ions.'",
     "3: 'Group 2 atoms lose their 2 outer electrons when they react, so they form 2+ ions.'"),
    # Rung 2 item 1 (element Y, 7 outer electrons), reply to "Non-metal; it forms no ions".
    ("reply: 'Only Group 0 elements, with full outer shells, form no ions.'",
     "reply: 'With 7 outer electrons, Y gains 1 electron to form a 1\u2212 ion.'"),
]

LESSON = {
    "slug": "metals-non-metals",
    "start": {
        "setup": "A sodium atom has 1 outer electron. A chlorine atom has 7.",
        "question": "If you had to guess, which one forms a positive ion when it reacts?",
        "options": [
            ("Sodium",
             "Sodium. It loses its outer electron to form Na⁺. Elements that form positive ions "
             "are metals."),
            ("Chlorine",
             "Sodium does. Chlorine gains 1 electron to form Cl⁻, a negative ion. Elements that "
             "form positive ions are metals."),
        ],
        "answer": 0,
    },
    "words": ["metal", "non-metal", "positive ion", "outer electrons"],
    "knowledge": [
        {"kind": "card", "title": "The definitions",
         "body": [{"points": [
             "Elements that react to form positive ions are metals.",
             "Elements that do not form positive ions are non-metals.",
         ]}]},
        {"kind": "card", "title": "Where they are",
         "body": [{"slot": "fig:pt-metals-nonmetals"},
                  "The majority of elements are metals. Metals are found to the left and towards "
                  "the bottom of the periodic table. Non-metals are found towards the right and top."]},
        {"kind": "card", "title": "Outer electrons decide",
         "body": [{"points": [
             "Atoms of metals such as sodium, magnesium and aluminium have 1, 2 or 3 outer "
             "electrons. When they react they lose them and form positive ions: Na⁺, Mg²⁺, Al³⁺.",
             "Carbon (2,4), oxygen (2,6) and chlorine (2,8,7) are non-metals, with 4, 6 and 7 outer "
             "electrons. They gain or share electrons instead. Chlorine gains 1 to form Cl⁻.",
             "The arrangement of electrons comes from the atomic number. The number of outer "
             "electrons is the group number, so it decides both how the element reacts and where "
             "it is in the table.",
         ]}]},
        {"kind": "reveal", "title": "Typical properties",
         "cols": ["Metals", "Non-metals"],
         "rows": [
             ("Conduct electricity", "Good conductors: delocalised electrons can move through the metal", "Poor conductors"),
             ("Melting and boiling points", "Usually high", "Usually low"),
             ("As a solid", "Shiny and malleable (can be hammered into shape)", "Dull and brittle"),
             ("Oxides", "Basic: they neutralise acids", "Acidic when they dissolve in water"),
             ("Ions", "Positive", "Negative, or they share electrons"),
         ]},
        {"kind": "card", "title": "Two exceptions",
         "body": [{"points": [
             "Graphite and graphene, forms of carbon, conduct electricity, because one electron from each "
             "carbon atom is delocalised and can move.",
             "Carbon and silicon are non-metals with very high melting points.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Metals gain electrons when they react.",
              "Metals lose electrons and form positive ions."),
             ("Any solid element is a metal.",
              "Carbon, sulfur and iodine are solid non-metals. A metal is an element that forms "
              "positive ions."),
             ("Hydrogen is a metal because it is at the top of Group 1.",
              "Hydrogen is a non-metal. It sits on its own at the top of the table."),
         ]}]},
    ],
    "key_fact": "Elements that react to form positive ions are metals. Elements that do not form "
                "positive ions are non-metals. Most elements are metals: they are to the left and "
                "towards the bottom of the periodic table, and non-metals are towards the right and "
                "top.",
    "deeper": [
        {"kind": "card", "title": "Why most non-metals melt easily",
         "body": ["Most non-metals are small molecules with weak forces between the molecules, so "
                  "they have low melting and boiling points. Carbon and silicon are giant "
                  "structures instead."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: use the evidence given: conducts, bends, oxide acidic or "
             "basic.",
             "<strong>Explain</strong>: start from the outer electrons: how many, then lost, "
             "gained or shared.",
             "<strong>Compare</strong>: the property for both elements, side by side.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-5", "logic_edits": LOGIC_EDITS},
}
