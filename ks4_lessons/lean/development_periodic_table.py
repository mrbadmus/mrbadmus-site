# -*- coding: utf-8 -*-
"""Development of the periodic table, in the lean shape. Spec table: ks4-development-periodic-table.md
(AQA 8464 5.1.2.2 / 8462 4.1.2.2, word for word the same; no HT-only or chemistry-only lines).

LEGACY (batch 4). The ladder and the practice set (the page's own bankSrc) stay from the Design page;
their fixes are logic_edits. Batch-4 logic writes \\u escapes, so the targets below do too.

logic_edits:
  1. Practice Q1 (why Mendeleev's table was accepted): credited option 106 characters with a dash,
     against 61 at most. Now "Elements he predicted were found and matched his predictions" (60,
     not the longest). Feedback plain; the Newlands and Ramsay asides go (beyond the spec).
  2. Practice Q2 (why the gaps): credited option the longest. Now "For elements not yet discovered";
     distractors keep their misconceptions, written a little longer.
  3. Practice Q3 "Why was Newlands' table rejected?" is REPLACED: Newlands is not in 5.1.2.2. The new
     item asks why early tables put some elements in the wrong groups (the spec's own line). New
     stem, so a new practice id; the old id retires (REPLACED in tools/lean_id_map.py).
  4. Practice Q4 (tellurium heavier than iodine): credited option 95 characters against 38. Now
     "Much of it is made of heavier isotopes" (38); two distractors written longer.
  5. Rung 1 Q2 (why the gaps): credited option the longest (31 against 24); the two distractors are
     written out longer, same misconceptions.
  6. Rung 2 Q1 (tellurium before iodine): credited option 58 against 36. Shortened to 43; the
     distractors are written out longer.
  7. Rung 3 chain 2 (isotopes and tellurium): the three links could be read in two orders (the
     conclusion first). Links 2 and 3 now refer back ("this average", "So, although"), so one
     order is valid. Same three ideas, same order credited.
  8. Rung 4 mark points: the Newlands point is replaced by the spec's own point on grouping by
     properties; the level descriptors are unchanged.
"""

LOGIC_EDITS = [
    # 1. Practice Q1
    ("opts: [['He predicted properties of undiscovered elements \\u2014 and when they were found, the predictions were accurate', true],",
     "opts: [['Elements he predicted were found and matched his predictions', true],"),
    ("wrong_explanations: { 1: 'Newlands had also arranged by atomic mass \\u2014 Mendeleev\\u2019s key advance was leaving gaps and making testable predictions.', 2: 'Noble gases were discovered by other scientists (Ramsay and others) after Mendeleev\\u2019s original table \\u2014 they were later added as Group 0.', 3: 'Science accepts models based on EVIDENCE and PREDICTIVE POWER, not simplicity alone.' } },",
     "wrong_explanations: { 1: 'Earlier tables were also in order of atomic weight. His key step was leaving gaps and making predictions that could be tested.', 2: 'The noble gases were discovered after his first table and added later as Group 0.', 3: 'Scientists accept a model because of evidence, such as predictions that come true.' } },"),
    # 2. Practice Q2
    ("opts: [['For elements he thought had not yet been discovered', true], ['Because he ran out of space', false], ['To separate metals from non-metals', false], ['Because some elements had no atomic weight', false]],",
     "opts: [['For elements not yet discovered', true], ['Because he ran out of space on the page', false], ['To separate metals from non-metals', false], ['Because some elements had no atomic weight', false]],"),
    # 3. Practice Q3: replaced (Newlands is beyond the spec)
    ("{ q: 'Why was Newlands\\u2019 table rejected?', opts: [['His pattern only worked for the first elements, he forced elements into groups where they did not fit, and he left no gaps', true], ['He ordered the elements by atomic number', false], ['He left too many gaps', false], ['He was the first to use atomic weights', false]],\n        wrong_explanations: { 1: 'Atomic numbers were not known; he used atomic weights.', 2: 'He left no gaps at all; that was part of the problem.', 3: 'Using atomic weights was normal then; the problem was the forced fit.' } },",
     "{ q: 'Why did early periodic tables put some elements in the wrong groups?', opts: [['They followed the strict order of atomic weights', true], ['They put elements in order of atomic number instead', false], ['They sorted the elements by the date they were found', false], ['They left too many gaps for missing elements', false]],\n        wrong_explanations: { 1: 'Atomic numbers were not known then. Early tables used atomic weights.', 2: 'The date of discovery played no part. The order was by atomic weight.', 3: 'Early tables left no gaps, so some elements were forced into groups they did not fit.' } },"),
    # 4. Practice Q4
    ("opts: [['Natural tellurium contains a high proportion of heavier isotopes, so its average mass is higher', true], ['Tellurium has more protons than iodine', false], ['Iodine atoms have no neutrons', false], ['Relative atomic mass ignores neutrons', false]],",
     "opts: [['Much of it is made of heavier isotopes', true], ['Tellurium has more protons than iodine', false], ['Iodine atoms have no neutrons in the nucleus', false], ['Relative atomic mass does not count neutrons', false]],"),
    # 5. Rung 1 Q2
    ("{ text: 'To separate the metals', correct: false, reply: 'The gaps were for missing elements.' },\n            { text: 'Because he made mistakes', correct: false, reply: 'The gaps were deliberate.' }] }",
     "{ text: 'To separate the metals from the non-metals', correct: false, reply: 'The gaps were for missing elements.' },\n            { text: 'Because he made mistakes in his weighing', correct: false, reply: 'The gaps were left on purpose.' }] }"),
    # 6. Rung 2 Q1
    ("{ text: 'So each was in a group with elements of similar properties', correct: true },\n            { text: 'Because tellurium is lighter', correct: false, reply: 'Tellurium is heavier: 127.6 against 126.9.' },\n            { text: 'Because he knew their atomic numbers', correct: false, reply: 'Atomic numbers were not yet known.' }] },",
     "{ text: 'To keep each in a group of similar elements', correct: true },\n            { text: 'Because tellurium has the lower relative atomic mass', correct: false, reply: 'Tellurium is heavier: 127.6 against 126.9.' },\n            { text: 'Because he already knew their atomic numbers', correct: false, reply: 'Atomic numbers were not yet known.' }] },"),
    # 7. Rung 3 chain 2
    ("'Much of natural tellurium is made of its heavier isotopes, so its relative atomic mass is higher than iodine\\u2019s.', 'Tellurium has fewer protons (52 against 53), so by atomic number it comes first.'],",
     "'Much of natural tellurium is made of its heavier isotopes, so this average is higher for tellurium than for iodine.', 'So, although tellurium is heavier on average, it has fewer protons (52 against 53) and comes first by atomic number.'],"),
    # 8. Rung 4 mark points
    ("'Newlands\\u2019 octaves: every eighth element similar, but it failed after the first elements and left no gaps.',",
     "'Mendeleev also used atomic weights, but put elements with similar properties in the same group.',"),
]

LESSON = {
    "slug": "development-periodic-table",
    "start": {
        "setup": "Mendeleev left gaps in his periodic table.",
        "question": "If you had to guess, did the gaps make other scientists more likely or less "
                    "likely to accept his table?",
        "options": [
            ("More likely",
             "More likely. He predicted the elements that would fill the gaps, and when they were "
             "found, his predictions matched."),
            ("Less likely",
             "More likely, in the end. He predicted the elements that would fill the gaps, and "
             "when they were found, his predictions matched."),
        ],
        "answer": 0,
    },
    "words": ["atomic weight", "gaps", "isotopes", "atomic number"],
    "knowledge": [
        {"kind": "card", "title": "Early tables: atomic weight",
         "body": ["Before protons, neutrons and electrons were discovered, scientists classified the "
                  "elements by arranging them in order of their atomic weights.",
                  "The early periodic tables were incomplete. Some elements were placed in "
                  "inappropriate groups when the strict order of atomic weights was followed."]},
        {"kind": "card", "title": "Mendeleev's gaps",
         "body": [{"slot": "fig:mendeleev-gap"},
                  "Mendeleev left gaps for elements that he thought had not been discovered, and "
                  "predicted their properties.",
                  "Elements with the properties he predicted were discovered later and filled the "
                  "gaps. Germanium filled the gap below silicon."]},
        {"kind": "card", "title": "Mendeleev's swaps",
         "body": [{"slot": "fig:te-i-swap"},
                  "In some places Mendeleev changed the order based on atomic weights, so that each "
                  "element sat in a group with elements like it.",
                  "By atomic weight, iodine (126.9) comes before tellurium (127.6). Iodine reacts "
                  "like chlorine and bromine, so he put tellurium first."]},
        {"kind": "card", "title": "Why his table was accepted",
         "body": ["His predictions could be tested. When elements such as germanium were found with "
                  "the properties he had predicted, other scientists accepted his table."]},
        {"kind": "card", "title": "Isotopes explain the swaps",
         "body": ["Isotopes are atoms of the same element with different numbers of neutrons. "
                  "Relative atomic mass is an average that takes account of the abundance of each "
                  "isotope.",
                  "Tellurium has fewer protons than iodine (52 against 53), but much of it is made "
                  "of heavier isotopes, so its relative atomic mass is higher.",
                  "So knowledge of isotopes explained why the order based on atomic weights was "
                  "not always correct. The modern table is in order of atomic number, and "
                  "tellurium comes first, where Mendeleev put it."]},
        {"kind": "reveal", "title": "Early tables and Mendeleev's table",
         "cols": ["Early tables", "Mendeleev's table"],
         "rows": [
             ("Order", "Strict order of atomic weight", "Atomic weight, with some pairs swapped"),
             ("Gaps", "None, so some elements were in the wrong groups",
              "Gaps left for undiscovered elements"),
             ("Predictions", "None", "Properties of the missing elements"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Mendeleev put the elements in order of atomic number.",
              "He used atomic weight. Protons, and so atomic numbers, were not yet known."),
             ("The gaps were mistakes.",
              "The gaps were left on purpose, for elements not yet discovered."),
             ("Isotopes of an element have different numbers of protons.",
              "Isotopes have the same number of protons and different numbers of neutrons."),
         ]}]},
    ],
    "key_fact": "Early tables put the elements in order of atomic weight. Mendeleev left gaps for "
                "undiscovered elements and swapped some pairs, and elements found later matched his "
                "predictions. Knowledge of isotopes explained why the order based on atomic weights "
                "was not always correct.",
    "deeper": [
        {"kind": "card", "title": "Eka-silicon and germanium",
         "body": ["Mendeleev called the missing element below silicon eka-silicon. He predicted a "
                  "relative atomic mass of about 72 and a density of about 5.5 g/cm³. Germanium, "
                  "found in 1886, has 72.6 and 5.3 g/cm³."]},
        {"kind": "card", "title": "Argon and potassium",
         "body": ["Argon (18 protons, relative atomic mass 39.9) comes before potassium (19 protons, "
                  "39.1). The reason is the same as for tellurium and iodine."]},
        {"kind": "card", "title": "Newlands",
         "body": ["Before Mendeleev, John Newlands noticed that every eighth element seemed similar. "
                  "The pattern only worked for the first elements and he left no gaps, so his "
                  "table was not accepted."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: the steps in order: atomic weights, gaps and swaps, "
             "predictions found, isotopes.",
             "<strong>Explain</strong>: why the table was accepted: predictions made, tested and "
             "found correct.",
             "<strong>Suggest</strong>: use protons and relative atomic mass to explain a pair "
             "that looks out of order.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": LOGIC_EDITS},
}
