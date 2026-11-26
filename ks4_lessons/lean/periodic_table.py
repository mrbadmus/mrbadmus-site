# -*- coding: utf-8 -*-
"""The periodic table, in the lean shape. Spec table: ks4-periodic-table.md (AQA 8464 5.1.2.1 /
8462 4.1.2.1, word for word the same; no HT-only or chemistry-only lines).

LEGACY (batch 4). The ladder (Ks4Practice rungs) and the practice set (the page's own bankSrc, the
same five on every route) stay from the Design page. The practice set does not read the subtopic
`quiz` list, so its fixes are logic_edits, and every stem is kept (no practice id changes).
Batch-4 logic writes \\u escapes, so the targets below do too.

logic_edits (option text and feedback only; every credited answer is the same answer):
  1. Practice Q1 (Period 3, Group 2): every option carried its reasoning after a dash, and the
     credited one was the longest. Options are now the bare structures (2,8,2 credited); the
     feedback teaches the reasoning.
  2. Practice Q2 (why Group 7 elements react alike): credited option 117 characters against 53 at
     most. Now "They all have 7 electrons in their outer shell" (46, not the longest).
  3. Practice Q4 (why the noble gases are unreactive): credited option the longest. Now "Their
     atoms have a full outer shell" (35); one distractor reworded to the same misconception.
  4. Practice Q5 (potassium below sodium): credited option 106 characters against 63. Now "More
     reactive: its outer electron is lost more easily" (52); distractors keep their misconceptions.
  5. Practice feedback for Q1, Q2 and Q5 used dashes and \\u2019-heavy asides; rewritten plainly.
"""

LOGIC_EDITS = [
    # 1. Practice Q1
    ("opts: [['2.8.2 \\u2014 3 shells (Period 3) and 2 outer electrons (Group 2)', true], ['3.2 \\u2014 period number first, then group number', false], ['2.2 \\u2014 two shells and two outer electrons', false], ['2.8.3 \\u2014 Period 3 means 3 electrons in the outer shell', false]],",
     "opts: [['2,8,2', true], ['3,2', false], ['2,2', false], ['2,8,3', false]],"),
    ("wrong_explanations: { 1: 'The periodic table doesn\\u2019t give configurations directly \\u2014 the group number is the outer electrons, but you must fill the inner shells first.', 2: 'Period 3 means 3 SHELLS, not 3 electrons in the outer shell. The shells fill as 2.8.2 \\u2014 inner shells full, outer shell has 2.', 3: 'Period 3 means 3 SHELLS \\u2014 not 3 electrons in the outermost shell. The Group number (2) gives the outer electron count.' } },",
     "wrong_explanations: { 1: 'That is the period and the group, not the electrons. Period 3 means three shells and Group 2 means two outer electrons: 2,8,2.', 2: 'That has only two shells. Period 3 means three shells, with the inner two full: 2,8,2.', 3: 'Period 3 means three shells, not three outer electrons. Group 2 means two outer electrons: 2,8,2.' } },"),
    # 2. Practice Q2
    ("opts: [['They all have 7 electrons in their outer shell \\u2014 they react similarly by gaining one electron to achieve a full shell', true],",
     "opts: [['They all have 7 electrons in their outer shell', true],"),
    ("wrong_explanations: { 1: 'Fluorine is a gas but iodine is a solid at room temperature \\u2014 physical state varies within Group 7.', 2: 'Different Group 7 elements have different numbers of electrons (F:9, Cl:17, Br:35) \\u2014 the OUTER electron count (7) is what\\u2019s the same.', 3: 'Elements in the same group are in DIFFERENT periods \\u2014 they share the same outer electron count, not the same period.' } },",
     "wrong_explanations: { 1: 'Fluorine and chlorine are gases, but bromine is a liquid and iodine is a solid.', 2: 'Each has a different total number of electrons. The number of outer electrons, 7, is the same.', 3: 'A group is a column, so its elements are in different periods. They share the number of outer electrons.' } },"),
    # 3. Practice Q4
    ("opts: [['Their atoms have a full outer shell of electrons', true], ['Their atoms have no outer electrons', false],",
     "opts: [['Their atoms have a full outer shell', true], ['Their atoms have no electrons in an outer shell', false],"),
    # 4. Practice Q5
    ("opts: [['Potassium is more reactive, because its outer electron is further from the nucleus and is lost more easily', true], ['Potassium is less reactive, because it has more shells', false], ['They are equally reactive, because they are in the same group', false], ['Potassium is more reactive, because it has more outer electrons', false]],",
     "opts: [['More reactive: its outer electron is lost more easily', true], ['Less reactive: it has more shells, so it holds its electron tighter', false], ['Equally reactive, because they are in the same group', false], ['More reactive, because it has more outer electrons', false]],"),
    ("wrong_explanations: { 1: 'More shells puts the outer electron further from the nucleus, so it is lost more easily: more reactive.', 2: 'Same group means similar reactions, but reactivity still changes down the group.', 3: 'Both have one outer electron. The difference is its distance from the nucleus.' } }",
     "wrong_explanations: { 1: 'More shells put the outer electron further from the nucleus, so it is held less strongly and lost more easily.', 2: 'Same group means similar reactions, but reactivity still increases down Group 1.', 3: 'Both atoms have one outer electron. The difference is its distance from the nucleus.' } }"),
    # Examiner fix round (26 Nov), M5: "Period 3, Group 15" is not a group on this course's table.
    ("{ text: 'Period 3, Group 15', correct: false, reply: '15 is the total number of electrons. The group is the outer count.' }",
     "{ text: 'Period 3, Group 2', correct: false, reply: '2 is the number of electrons in the first shell. The group is the outer count: 5.' }"),
]

LESSON = {
    "slug": "periodic-table",
    "start": {
        "setup": None,
        "question": "If you had to guess, do the elements in one column of the periodic table react "
                    "alike or differently?",
        "options": [
            ("Alike",
             "Alike. Elements in one column have the same number of outer electrons."),
            ("Differently",
             "They react alike, because elements in one column have the same number of outer "
             "electrons."),
        ],
        "answer": 0,
    },
    "words": ["group", "period", "outer electrons", "atomic number"],
    "knowledge": [
        {"kind": "card", "title": "In order of atomic number",
         "body": [{"slot": "fig:pt-first-twenty"},
                  "The elements in the periodic table are arranged in order of atomic (proton) "
                  "number.",
                  "Elements with similar properties are in columns, known as groups. The rows are "
                  "periods.",
                  "It is called a periodic table because similar properties occur at regular "
                  "intervals."]},
        {"kind": "card", "title": "Groups and outer electrons",
         "body": ["Elements in the same group have the same number of electrons in their outer "
                  "shell (outer electrons). This gives them similar chemical properties.",
                  "Lithium (2,1), sodium (2,8,1) and potassium (2,8,8,1) each have 1 outer "
                  "electron, so all three are in Group 1."]},
        {"kind": "card", "title": "Position from the electrons",
         "body": [{"slot": "fig:na-cl-shells"},
                  {"points": [
                      "The period number is the number of occupied shells.",
                      "The group number is the number of outer electrons.",
                  ]},
                  "Atomic number 15 means 15 electrons: 2,8,5 (also written 2.8.5). Three shells, "
                  "so Period 3. Five outer electrons, so Group 5. This is phosphorus."]},
        {"kind": "reveal", "title": "Predicting reactivity from position",
         "cols": ["Group 1", "Group 7"],
         "rows": [
             ("Outer electrons", "1", "7"),
             ("When they react", "Lose 1 electron", "Gain 1 electron"),
             ("Going down the group, the outer shell is", "Further from the nucleus",
              "Further from the nucleus"),
             ("Going down the group, reactivity", "Increases", "Decreases"),
         ]},
        {"kind": "card", "title": "Why the two trends go opposite ways",
         "body": [{"points": [
             "Group 1: the outer electron is further from the nucleus, so it is less strongly "
             "attracted and is lost more easily.",
             "Group 7: an electron coming into the outer shell is less strongly attracted, so it "
             "is gained less easily.",
             "Group 0: the outer shell is full (8, or 2 for helium), so the noble gases are "
             "unreactive.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The group number is the number of shells.",
              "The group number is the number of outer electrons. The period number is the "
              "number of shells."),
             ("Group 0 atoms have no outer electrons.",
              "Group 0 atoms have a full outer shell: 8 electrons, or 2 for helium."),
             ("Every group gets more reactive going down.",
              "Group 1 gets more reactive going down. Group 7 gets less reactive."),
         ]}]},
    ],
    "key_fact": "The elements are arranged in order of atomic number. The period number is the "
                "number of occupied shells and the group number is the number of outer electrons. "
                "Elements in the same group have the same number of outer electrons, so they have "
                "similar chemical properties.",
    "deeper": [
        {"kind": "card", "title": "Where the metals are",
         "body": ["Metals are to the left and towards the bottom of the table. Non-metals are towards "
                  "the right and top."]},
        {"kind": "card", "title": "The transition metals",
         "routes": ["TF", "TH"],
         "body": ["The block between Groups 2 and 3 holds the transition metals."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong>: a short answer, such as the group, the period or the "
             "electronic structure.",
             "<strong>Predict</strong>: use the element's position and the group trend.",
             "<strong>Explain</strong>: shells, distance from the nucleus, attraction, then lost "
             "or gained more or less easily.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": LOGIC_EDITS},
}
