# -*- coding: utf-8 -*-
"""Relative atomic mass, in the lean shape. Spec table: ks4-relative-atomic-mass.md (AQA 8464
5.1.1.6 / 8462 4.1.1.6, word for word the same; no HT-only or Chemistry-only lines). Isotopes
(5.1.1.5) are taught in Subatomic particles; this page recaps them with chlorine, the example the
calculation uses.

LEGACY (batch 11). The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the
same five items on every route) stay from the Design page. The worked examples stay too: the
`cfifa` slot reuses the page's own cfExamples / cfQuestions (three examples, questions ram-q1..q3),
so the record carries no `cfifa` of its own and the logic keeps its `Object.assign(c, {` shape.

logic_edits:
  1. Worked example 1, Convert line: "Nothing to convert — the percentage abundances and the isotope
     mass numbers are already in matching, dimensionless units" (a dash, and wordy). Shortened.
  2. Rung 1 item 2 (Define isotopes): the credited option was the longest. Its text is kept; the
     distractors are now the real mix-ups (ions for isotopes; different elements), one longer than
     the key.
  3. Rung 2 item 2 (thallium) Convert choice: credited the longest (45 against 43). "3% and 7%"
     becomes the swapped "70% and 30%", the same length. Same index credited.
  4. to 7. Practice Q1, Q2, Q3, Q5: credited option the longest each time (Q2 and Q3 also carried
     their working; Q1 capitals and dashes). Stems kept, so ids kept; keys unchanged in meaning
     (Q3 now credits "200 + 8.8 = 208.8", the same 208.8).

All numbers recomputed (spec table, "Calculations").
"""

LOGIC_EDITS = [
    ("line: 'Nothing to convert — the percentage abundances and the isotope mass numbers are already in matching, dimensionless units for the formula.'",
     "line: 'Nothing to convert: both abundances are percentages.'"),
    ("MCQ('Define', 'Define isotopes.', 'Atoms of the same element with different numbers of neutrons.', ['Atoms of the same element with different numbers of neutrons', ['Atoms with the same mass number but different elements', 'Isotopes are one element.'], ['Atoms with different numbers of protons', 'Different protons means a different element.']])",
     "MCQ('Define', 'Define isotopes.', 'Atoms of the same element with different numbers of neutrons.', ['Atoms of the same element with different numbers of neutrons', ['Atoms of the same element with different numbers of electrons', 'Atoms that have gained or lost electrons are ions, not isotopes.'], ['Atoms of different elements with the same mass number', 'Isotopes are atoms of one element.']])"),
    ("['Nothing to convert', 'Convert the ratio to percentages: 30% and 70%', 'Convert the ratio to percentages: 3% and 7%'], 1,",
     "['Nothing to convert', 'Convert the ratio to percentages: Tl-203 30%, Tl-205 70%', 'Convert the ratio to percentages: Tl-203 70%, Tl-205 30%'], 1,"),
    ('V("Chlorine-35 and chlorine-37 are isotopes. What is the same and what differs between them?", [["Same: atomic number (17 protons and 17 electrons). Different: mass number — Cl-35 has 18 neutrons, Cl-37 has 20 neutrons.", true], ["Same: mass number. Different: atomic number and proton count.", false], ["Same: everything — isotopes are identical atoms.", false], ["Same: neutron number. Different: proton number.", false]], { "1": "If mass numbers were the same they would be identical — isotopes are DEFINED by having different mass numbers. Different atomic numbers would make them different elements.", "2": "Isotopes DO have the same chemical properties — but they are NOT identical. They differ in neutron count and mass.", "3": "If neutron numbers were the same but proton numbers differed, they would be different ELEMENTS — not isotopes." }),',
     'Q("Chlorine-35 and chlorine-37 are isotopes. What is the same and what differs between them?", \'Same protons; different neutrons (18 and 20)\', [[\'Same mass number; different numbers of protons\', \'Different numbers of protons would make different elements, and their mass numbers differ.\'], [\'Same everything: isotopes are identical atoms\', \'They have different numbers of neutrons, so different masses.\'], [\'Same neutrons; different numbers of protons\', \'Isotopes have the same number of protons. The neutrons differ.\']]),'),
    ('V("An element has two isotopes: 60% at mass 63 and 40% at mass 65. What is its Ar?", [["63.8 — Ar = (60 × 63 + 40 × 65) ÷ 100 = 6380 ÷ 100", true], ["64.0 — simple average of 63 and 65", false], ["128 — total of both mass numbers added together", false], ["63 — just the most abundant isotope mass", false]], { "1": "Simple average gives 64 only if BOTH isotopes are 50/50 abundant. Since there is more of the lighter isotope (60% at mass 63), the weighted average is pulled below 64.", "2": "Adding mass numbers has no physical meaning — Ar is a weighted average, not a sum.", "3": "Using only the most abundant isotope ignores the 40% contribution from mass 65 — the true Ar is pulled above 63 by the heavier isotope." }),',
     'Q("An element has two isotopes: 60% at mass 63 and 40% at mass 65. What is its Ar?", \'63.8\', [[\'64.0\', \'That is the simple average. There is more of the lighter isotope, so Ar is below 64.\'], [\'128\', \'Do not add the mass numbers. Ar = [(60 × 63) + (40 × 65)] ÷ 100 = 63.8.\'], [\'63\', \'That ignores the 40% at mass 65. Ar = 6380 ÷ 100 = 63.8.\']]),'),
    ("Q('Boron is 20% boron-10 and 80% boron-11. A pupil writes Ar = (20 × 10) + (80 × 11) ÷ 100. What does that line actually equal?', '208.8, because only 880 is divided by 100', [['10.8, the line is fine', 'Without the outer bracket, 200 + 8.8 = 208.8. Bracket the whole top.'], ['1080', 'That is the bracketed total before dividing.'], ['10.5', 'That is the simple average of 10 and 11, with no abundances.']]),",
     "Q('Boron is 20% boron-10 and 80% boron-11. A pupil writes Ar = (20 × 10) + (80 × 11) ÷ 100. What does that line actually equal?', '200 + 8.8 = 208.8', [['1080 ÷ 100 = 10.8', 'That is the bracketed line. As written, only 80 × 11 = 880 is divided by 100.'], ['200 + 880 = 1080', 'That leaves out the ÷ 100 altogether.'], ['(10 + 11) ÷ 2 = 10.5', 'That is the simple average, with no abundances.']]),"),
    ("Q('On the periodic table, copper is shown with 63.5 above the symbol and 29 below. What is 63.5?', 'The relative atomic mass, an average over copper’s isotopes', [['The mass number of every copper atom', 'No single atom has a mass number of 63.5; mass numbers are whole numbers for one isotope.'], ['The number of neutrons', 'Neutrons are not shown; you find them from a mass number minus 29.'], ['The number of electrons', 'A neutral copper atom has 29 electrons.']])",
     "Q('On the periodic table, copper is shown with 63.5 above the symbol and 29 below. What is 63.5?', 'The relative atomic mass of copper', [['The mass number of every copper atom', 'No atom has a mass number of 63.5. Mass numbers are whole numbers.'], ['The number of neutrons in copper', 'Neutrons are mass number minus atomic number, for one isotope.'], ['The mass of one copper atom in grams', 'One atom has a tiny mass. 63.5 is a relative mass, an average over copper’s isotopes.']])"),
]

LESSON = {
    "slug": "relative-atomic-mass",
    "start": {
        "setup": "Chlorine atoms are 75% chlorine-35 and 25% chlorine-37.",
        "question": "If you had to guess, is the relative atomic mass of chlorine nearer 35 or 37?",
        "options": [
            ("Nearer 35",
             "Nearer 35. There are three chlorine-35 atoms for every chlorine-37, so the average is "
             "35.5."),
            ("Nearer 37",
             "It is 35.5, nearer 35. There are three chlorine-35 atoms for every chlorine-37, so "
             "the average leans towards 35."),
        ],
        "answer": 0,
    },
    "words": ["isotope", "abundance", "relative atomic mass"],
    "knowledge": [
        {"kind": "card", "title": "Isotopes",
         "body": [{"slot": "fig:isotopes-hydrogen"},
                  "Atoms of the same element can have different numbers of neutrons. These atoms "
                  "are called isotopes of that element.",
                  "Isotopes have the same number of protons and electrons, so they have the "
                  "same chemical properties. Their mass numbers are different."]},
        {"kind": "reveal", "title": "Chlorine-35 and chlorine-37",
         "cols": ["Chlorine-35", "Chlorine-37"],
         "rows": [
             ("Protons", "17", "17"),
             ("Neutrons", "35 − 17 = 18", "37 − 17 = 20"),
             ("Electrons", "17", "17"),
             ("Mass number", "35", "37"),
         ]},
        {"kind": "card", "title": "Relative atomic mass",
         "body": [{"slot": "fig:chlorine-abundance"},
                  "The relative atomic mass (A<sub>r</sub>) of an element is an average value that "
                  "takes account of the abundance of the isotopes of the element.",
                  "Abundance means how common each isotope is, as a percentage of the atoms.",
                  "It is the number above the symbol in the periodic table. It is often not a whole "
                  "number, because it is an average over isotopes with different masses."]},
        {"kind": "card", "title": "Calculating relative atomic mass",
         "body": ["Multiply each isotope's mass number by its percentage abundance. Add the results. "
                  "Then divide the total by 100.",
                  "A<sub>r</sub> = [(abundance × mass number) + (abundance × mass "
                  "number)] ÷ 100",
                  "Chlorine: A<sub>r</sub> = [(75 × 35) + (25 × 37)] ÷ 100 = "
                  "(2625 + 925) ÷ 100 = 35.5",
                  "Bracket the whole top before you divide by 100.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A<sub>r</sub> = (20 × 10) + (80 × 11) ÷ 100",
              "Bracket the whole top: [(20 × 10) + (80 × 11)] ÷ 100 = 10.8."),
             ("Boron is 10.5, the average of 10 and 11.",
              "There is more boron-11, so A<sub>r</sub> = 10.8."),
             ("A ratio of 3 : 1 means 3% and 1%.",
              "Turn a ratio into percentages first: 3 : 1 is 75% and 25%."),
             ("Each chlorine atom has a mass of 35.5.",
              "Each atom is 35 or 37. 35.5 is the average."),
         ]}]},
    ],
    "key_fact": "The relative atomic mass of an element is an average value that takes account of "
                "the abundance of its isotopes. Multiply each mass number by its percentage "
                "abundance, add, then divide by 100: for chlorine, [(75 × 35) + "
                "(25 × 37)] ÷ 100 = 35.5.",
    "deeper": [
        {"kind": "card", "title": "Three isotopes",
         "body": ["The method works for any number of isotopes. Silicon is 92% silicon-28, 5% "
                  "silicon-29 and 3% silicon-30.",
                  "A<sub>r</sub> = [(92 \u00d7 28) + (5 \u00d7 29) + (3 \u00d7 30)] \u00f7 100 = "
                  "(2576 + 145 + 90) \u00f7 100 = 2811 \u00f7 100 = 28.1"]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: show the bracketed working, then the answer with no unit.",
             "<strong>Explain</strong>: why A<sub>r</sub> is not a whole number. Name the isotopes "
             "and their abundances.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
