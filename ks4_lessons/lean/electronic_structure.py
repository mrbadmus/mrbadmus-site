# -*- coding: utf-8 -*-
"""Electronic structure, in the lean shape. Spec table: ks4-electronic-structure.md (AQA 8464
5.1.1.7 / 8462 4.1.1.7, word for word the same; no HT-only or Chemistry-only lines).

LEGACY (batch 11). The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the
same five items on every route) stay from the Design page; the practice set does not read the
subtopic `quiz` list, so its fixes are logic_edits. Every stem is kept, so every practice id is kept.

logic_edits (practice set only; the rungs were checked and are unchanged):
  1. Q1 (2.8.6, which group): the credited option carried its reason with a dash; replies in
     capitals; one distractor ("Period 3") was not a group at all. Options are now four groups.
  2. Q2 (lithium and sodium): credited option the longest (100 against 30 to 49). Rewritten.
  3. Q3 (calcium): credited "2,8,8,2" was the longest option by one character. "2,18" becomes
     "8,8,2,2" (writing the outer shell first), the same length.
  4. Q4 (helium in Group 0): credited option the longest (53 against 13 to 24). Rewritten.
  5. Q5 (how shells fill): credited option the longest (63 against 27 to 45). Rewritten in the
     spec's words ("lowest energy level").
"""

LOGIC_EDITS = [
    ('V("An element has the electronic configuration 2.8.6. Which group of the periodic table is it in?", [["Group 6 — it has 6 electrons in its outermost shell", true], ["Group 2 — there are 2 complete shells below the outer shell", false], ["Group 16 — add all the electrons together", false], ["Period 3 — it has 3 shells", false]], { "1": "The number of complete inner shells tells you the PERIOD — 2 inner shells means Period 3. Groups are determined by OUTER electrons.", "2": "16 is the total number of electrons (2+8+6) — this tells you the atomic number, not the group.", "3": "The NUMBER OF SHELLS tells you the PERIOD (3 shells = Period 3). The GROUP is determined by the number of OUTER electrons (6)." }),',
     'Q("An element has the electronic configuration 2.8.6. Which group of the periodic table is it in?", \'Group 6\', [[\'Group 2\', \'Two full inner shells do not give the group. The 6 outer electrons do.\'], [\'Group 8\', \'8 is the number of electrons in the second shell. The group comes from the 6 outer electrons.\'], [\'Group 3\', \'Three shells gives the period, period 3. The group comes from the 6 outer electrons.\']]),'),
    ('V("Why do lithium (2.1) and sodium (2.8.1) have similar chemical properties?", [["Both have 1 electron in their outer shell — they react in similar ways to achieve a full outer shell", true], ["Both have the same total number of electrons", false], ["Both are in the same period of the periodic table", false], ["Both have the same mass number", false]], { "1": "Li has 3 electrons total, Na has 11 — very different totals, but the same outer shell count (1) is what matters for reactivity.", "2": "Li is Period 2, Na is Period 3 — they are in different periods. Same GROUP, different periods.", "3": "Li has mass number 7, Na has mass number 23 — different mass numbers. Chemical similarity comes from electron configuration." }),',
     'Q("Why do lithium (2.1) and sodium (2.8.1) have similar chemical properties?", \'Both have 1 electron in their outer shell\', [[\'Both have the same total number of electrons\', \'Lithium has 3 electrons and sodium 11. The outer shell is what matters.\'], [\'Both are in the same period of the table\', \'Lithium is in period 2 and sodium in period 3. They are in the same group.\'], [\'Both have the same mass number\', \'Lithium-7 and sodium-23 have different mass numbers. Reactions depend on the outer electrons.\']]),'),
    ("['2,18', 'The second shell holds at most 8.']",
     "['8,8,2,2', 'Write the innermost shell first: 2,8,8,2.']"),
    ("Q('Helium is 2. Why is it in Group 0 rather than Group 2?', 'Its outer shell is full: the first shell holds only 2', [['It has 2 shells', 'Helium has one shell.'], ['It is a metal', 'Helium is a noble gas.'], ['It has 8 outer electrons', 'Helium has 2; the first shell is full at 2.']]),",
     "Q('Helium is 2. Why is it in Group 0 rather than Group 2?', 'Its one shell is full with 2 electrons', [['It has 8 electrons in its outer shell', 'Helium has only 2 electrons. Its first shell is full at 2.'], ['Group 2 is only for atoms with 2 shells', 'The group comes from the outer electrons. Helium’s outer shell is full, so it is in Group 0.'], ['It has no electrons in its outer shell', 'Group 0 does not mean no outer electrons. It means a full outer shell.']]),"),
    ("Q('Which statement describes how electrons fill shells?', 'The lowest available energy level (innermost shell) fills first', [['Electrons spread evenly across all the shells', 'Each shell fills before the next starts.'], ['The outer shell fills first', 'The innermost shell fills first.'], ['Any shell can take up to 8 electrons', 'The first shell holds only 2.']])",
     "Q('Which statement describes how electrons fill shells?', 'The lowest energy level fills first', [['Electrons spread evenly across all the shells', 'Each shell fills before the next starts.'], ['The outer shell fills first', 'The innermost shell, the lowest energy level, fills first.'], ['Any shell can take up to 8 electrons', 'The first shell holds only 2.']])"),
]

LESSON = {
    "slug": "electronic-structure",
    "start": {
        "setup": None,
        "question": "If you had to guess, which shell do an atom's electrons fill first?",
        "options": [
            ("The one nearest the nucleus",
             "The innermost shell, the lowest energy level, fills first. Sodium's 11 electrons go "
             "2, then 8, then 1."),
            ("The outermost one",
             "The innermost shell, the lowest energy level, fills first. Sodium's 11 electrons go "
             "2, then 8, then 1."),
        ],
        "answer": 0,
    },
    "words": ["energy level", "shell", "electronic structure"],
    "knowledge": [
        {"kind": "card", "title": "Filling the shells",
         "body": ["The electrons in an atom occupy the lowest available energy levels (innermost "
                  "available shells).",
                  {"points": [
                      "The first shell holds up to 2 electrons.",
                      "The second shell holds up to 8.",
                      "For the first 20 elements, the third shell holds up to 8. Then the fourth "
                      "shell starts.",
                  ]},
                  "You may answer in terms of energy levels or shells."]},
        {"kind": "card", "title": "Numbers and diagrams",
         "body": [{"slot": "fig:sodium-shells"},
                  "The electronic structure of an atom can be written as numbers or drawn as a "
                  "diagram. Sodium has 11 electrons: 2,8,1. That is two electrons in the lowest "
                  "energy level, eight in the second and one in the third.",
                  {"slot": "fig:shell-examples"}]},
        {"kind": "reveal", "title": "Write the electronic structure",
         "cols": ["Electrons", "Electronic structure"],
         "rows": [
             ("Carbon", "6", "2,4"),
             ("Magnesium", "12", "2,8,2"),
             ("Phosphorus", "15", "2,8,5"),
             ("Argon", "18", "2,8,8"),
             ("Potassium", "19", "2,8,8,1"),
             ("Calcium", "20", "2,8,8,2"),
         ]},
        {"kind": "card", "title": "Group and period",
         "body": ["The number of electrons in the outer shell is the group number. A full outer "
                  "shell means Group 0.",
                  "The number of shells holding electrons is the period number.",
                  "Sulfur is 2,8,6: six outer electrons, so Group 6. Three shells, so period 3."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Potassium has 19 electrons, so it is 2,8,9.",
              "The third shell holds 8, then the fourth starts: 2,8,8,1."),
             ("The outer shell fills first.",
              "The innermost shell, the lowest energy level, fills first."),
             ("2,8,6 is in Group 3, because it has three shells.",
              "Three shells gives period 3. Six outer electrons gives Group 6."),
         ]}]},
    ],
    "key_fact": "The electrons in an atom occupy the lowest available energy levels (innermost "
                "available shells). The first shell holds up to 2 electrons and the next two hold "
                "up to 8 each, so sodium, with 11 electrons, is 2,8,1.",
    "deeper": [
        {"kind": "card", "title": "Commas or dots",
         "body": ["AQA writes electronic structures with commas, 2,8,1. Dots, 2.8.1, are also "
                  "accepted."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong>: the electronic structure, in numbers or as a diagram.",
             "<strong>Identify</strong>: the group and period from a structure such as 2,8,6.",
             "<strong>Explain</strong>: why elements in a group are similar. They have the same "
             "number of outer electrons.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
