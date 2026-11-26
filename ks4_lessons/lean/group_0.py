# -*- coding: utf-8 -*-
"""Group 0, in the lean shape. Spec table: ks4-group-0.md (AQA 8464 5.1.2.4 / 8462 4.1.2.4, word for
word the same; no HT-only or chemistry-only lines).

LEGACY (batch 5). The ladder and the practice set (the page's own bankSrc) stay from the Design page;
their fixes are logic_edits. Every practice stem is kept. Batch-5 logic writes \\u escapes.

Boiling points used on the page and in the figure (degC, rounded): He -269, Ne -246, Ar -186,
Kr -153, Xe -108, Rn -62 (the Design page's own values; data-book values 4.2, 27.1, 87.3, 119.9,
165.0 and 211.5 K, minus 273.15).

logic_edits (option text and feedback; every credited answer is the same answer):
  1. Practice Q1 (why unreactive): credited option 105 characters with a dash. Now "They have full
     outer shells of electrons" (40); distractors keep their misconceptions, without dashes.
  2. Practice Q2 (argon boils higher than neon): the credited option named "London dispersion
     forces" (beyond GCSE) and was the longest. Now "Argon atoms are heavier, so the forces between
     the atoms are stronger" (67, not the longest). Feedback plain.
  3. Practice Q5 (sodium ion like neon): credited option 31 characters against 11. Now the four
     options are bare names.
"""

LOGIC_EDITS = [
    # 1. Practice Q1
    ("opts: [['They have full outer electron shells \\u2014 no tendency to gain, lose or share electrons to become more stable', true], ['They are gases \\u2014 gases cannot react with solid or liquid substances', false], ['They have no electrons in their outer shell \\u2014 so they cannot form bonds', false], ['They are too small to collide effectively with other atoms', false]],",
     "opts: [['They have full outer shells of electrons', true], ['They are gases, and gases cannot react with solids or liquids', false], ['They have no electrons in their outer shell', false], ['They are too small to collide with other atoms', false]],"),
    ("wrong_explanations: { 1: 'Many gases are highly reactive \\u2014 chlorine gas (Cl\\u2082), oxygen gas (O\\u2082) etc. Being a gas doesn\\u2019t make something unreactive.', 2: 'Noble gases have FULL outer shells, not empty ones. Helium has 2 electrons (full 1st shell), others have 8 outer electrons.', 3: 'Atomic size affects reactivity in some cases, but noble gases are unreactive because of electron configuration, not size.' } },",
     "wrong_explanations: { 1: 'Many gases are very reactive, such as chlorine and oxygen.', 2: 'Their outer shells are full: 8 electrons, or 2 for helium.', 3: 'Size is not the reason. Their atoms have a stable arrangement of electrons.' } },"),
    # 2. Practice Q2
    ("opts: [['Argon is a larger atom with more electrons \\u2014 stronger London dispersion forces between atoms need more energy to overcome', true], ['Argon has a higher atomic number, so its electrons are more strongly attracted to the nucleus', false], ['Argon forms molecules (Ar\\u2082) while neon is monatomic \\u2014 more bonds to break', false], ['Argon is radioactive, releasing energy that raises its boiling point', false]],",
     "opts: [['Argon atoms are heavier, so the forces between the atoms are stronger', true], ['Argon has a higher atomic number, so its electrons are more strongly attracted to the nucleus', false], ['Argon forms Ar\\u2082 molecules, but neon exists as single atoms', false], ['Argon is radioactive, releasing energy that raises its boiling point', false]],"),
    ("wrong_explanations: { 1: 'Stronger nuclear attraction would make electrons harder to remove but doesn\\u2019t directly raise boiling point \\u2014 the intermolecular forces between atoms are what matter.', 2: 'Noble gases are ALL monatomic \\u2014 they never form Ar\\u2082 or Ne\\u2082 molecules under normal conditions.', 3: 'Argon is stable and not radioactive. Radon is the radioactive noble gas.' } },",
     "wrong_explanations: { 1: 'Boiling separates the atoms from each other. What matters is the forces between the atoms.', 2: 'All the noble gases exist as single atoms. Neither forms molecules.', 3: 'Argon is not radioactive. Radon is the radioactive noble gas.' } },"),
    # 3. Practice Q5
    ("opts: [['Neon\\u2019s: a noble gas arrangement', true], ['Magnesium\\u2019s', false], ['Chlorine\\u2019s', false], ['Argon\\u2019s', false]],",
     "opts: [['Neon\\u2019s', true], ['Magnesium\\u2019s', false], ['Chlorine\\u2019s', false], ['Argon\\u2019s', false]],"),
]

LESSON = {
    "slug": "group-0",
    "start": {
        "setup": "Party balloons are filled with helium, a Group 0 element.",
        "question": "If you had to guess, does helium react easily, or hardly at all?",
        "options": [
            ("It reacts easily",
             "It hardly reacts at all. Helium atoms have a full outer shell, which is stable."),
            ("It hardly reacts at all",
             "Yes. Helium atoms have a full outer shell, which is stable."),
        ],
        "answer": 1,
    },
    "words": ["noble gases", "stable arrangement", "outer shell", "boiling point"],
    "knowledge": [
        {"kind": "card", "title": "The noble gases",
         "body": ["The elements in Group 0 of the periodic table are called the noble gases: helium, "
                  "neon, argon, krypton, xenon and radon.",
                  "They are unreactive and do not easily form molecules, because their atoms have "
                  "stable arrangements of electrons. They exist as single atoms."]},
        {"kind": "card", "title": "Full outer shells",
         "body": [{"slot": "fig:noble-gas-shells"},
                  "The noble gases have eight electrons in their outer shell, except for helium, "
                  "which has only two.",
                  "A full outer shell is stable, so the atoms have no tendency to gain, lose or "
                  "share electrons."]},
        {"kind": "card", "title": "Boiling points down the group",
         "body": [{"slot": "fig:noble-gas-boiling"},
                  "The boiling points of the noble gases increase with increasing relative atomic "
                  "mass, going down the group.",
                  "Heavier atoms have stronger forces between them, so more energy is needed to "
                  "separate them. Density also increases down the group."]},
        {"kind": "card", "title": "Predicting from a trend",
         "body": ["Krypton boils at −153 °C and xenon at −108 °C. Radon is next down the group, so "
                  "predict a boiling point higher than −108 °C. Radon's is −62 °C."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Noble gases do not react because they are gases.",
              "Oxygen and chlorine are gases and react easily. Noble gases are unreactive because "
              "their atoms have a full outer shell."),
             ("Noble gases have no outer electrons.",
              "Their outer shell is full: 8 electrons, or 2 for helium."),
             ("Boiling a noble gas breaks bonds inside its atoms.",
              "Boiling separates the atoms from each other. Nothing inside an atom changes."),
         ]}]},
    ],
    "key_fact": "The noble gases are unreactive and do not easily form molecules, because their "
                "atoms have stable arrangements of electrons: a full outer shell of 8, or 2 for "
                "helium. Their boiling points increase with increasing relative atomic mass, going "
                "down the group.",
    "deeper": [
        {"kind": "card", "title": "The noble gas arrangement",
         "body": ["When atoms of other elements react, they lose, gain or share electrons and end "
                  "up with the electron arrangement of a noble gas. A sodium ion, Na⁺, is 2,8: the "
                  "same as neon."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: start from the electrons: full outer shell, so stable, so "
             "unreactive.",
             "<strong>Predict</strong>: follow the trend in the data, and say which way.",
             "<strong>Compare</strong>: the property for both elements, with the reason.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-5", "logic_edits": LOGIC_EDITS},
}
