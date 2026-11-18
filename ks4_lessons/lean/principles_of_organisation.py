# -*- coding: utf-8 -*-
"""Principles of organisation, in the lean shape. Spec table: ks4-principles-of-organisation.md
(AQA 8464 4.2.1 / 8461 4.2.1, word for word the same; no HT-only or Biology-only lines).

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives; rung prompts keep their
positions, so rung ids survive.
"""

def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Rung 1 Q1 "Define an organ": the credited option was visibly the longest (+25).
    (r"{ text: 'A group of similar cells', correct: false, reply: 'That is a tissue.' }, "
     r"{ text: 'A group of organ systems', correct: false, reply: 'Organ systems together make an organism.' }",
     r"{ text: 'A group of similar cells with the same function', correct: false, reply: 'That is a tissue.' }, "
     r"{ text: 'A group of organ systems working together', correct: false, reply: 'Organ systems working together form an organism.' }"),
    # Rung 4 reject "Muscle is an organ": arguably true (a whole muscle, such as the biceps, is an
    # organ). Replaced by a definitely wrong statement.
    (r"reject: ['“Muscle is an organ.”', '“The heart is an organ system.”']",
     r"reject: ['“A tissue is made of several organs.”', '“The heart is an organ system.”']"),
    # Practice Q1 (order of levels), stem kept: dash asides in the replies.
    (r"wrong_explanations: { 1: 'Tissues are made of cells — cells always come before tissues in the hierarchy.', 2: 'Organs contain tissues, not the other way round — tissue must come before organ.', 3: 'This is the correct order in reverse — from most complex down to simplest.' }",
     r"wrong_explanations: { 1: 'Tissues are made of cells, so cells come before tissues.', 2: 'Organs are made of tissues, so tissue comes before organ.', 3: 'This is the right order backwards, from most complex to simplest.' }"),
    # Practice Q2 "What is a tissue?", stem kept: credited option visibly the longest (+28),
    # shouting capitals and dash asides in the replies. Credited option now AQA's own words.
    (r"opts: [['A group of similar cells working together to perform a specific function', true], ['A group of different organs working together', false], ['A single highly specialised cell', false], ['Another name for an organ', false]],",
     r"opts: [['A group of cells with a similar structure and function', true], ['A group of different organs working together', false], ['One specialised cell that does a single job', false], ['Another name for an organ in the body', false]],"),
    (r"wrong_explanations: { 1: 'A group of different organs = an ORGAN SYSTEM. Tissues are made of similar cells, not organs.', 2: 'A single specialised cell is just a cell — not a tissue. A tissue is a GROUP of cells.', 3: 'Tissues and organs are different levels. An organ is made of SEVERAL tissue types.' }",
     r"wrong_explanations: { 1: 'Organs working together make an organ system. A tissue is made of cells.', 2: 'One cell is a cell. A tissue is a group of cells.', 3: 'An organ is made of several different tissues.' }"),
    # Practice Q3 (stomach), stem kept: dash asides and capitals in the replies.
    (r"wrong_explanations: { 1: 'A tissue is one group of similar cells — the stomach has multiple tissue types, so it is an organ.', 2: 'An organ system is a GROUP of organs — the stomach is just one organ within the digestive system.', 3: 'An organism is the complete living thing — a human, plant or bacterium.' }",
     r"wrong_explanations: { 1: 'A tissue is one group of similar cells. The stomach has several tissues, so it is an organ.', 2: 'An organ system is several organs. The stomach is one organ in the digestive system.', 3: 'An organism is the whole living thing, such as a human.' }"),
    # Practice Q4 (organ system), stem kept: every option had a dash tail (the credited one the
    # longest), and the replies shouted.
    (r"opts: [['The digestive system — stomach, intestines, liver and pancreas working together', true], ['Muscle tissue — cells that contract to produce movement', false], ['The heart — contains cardiac muscle and valves', false], ['A liver cell — specialised to carry out chemical reactions', false]],",
     r"opts: [['The digestive system', true], ['Muscle tissue', false], ['The heart', false], ['A liver cell', false]],"),
    (r"wrong_explanations: { 1: 'Muscle tissue = a TISSUE (one cell type). Organ systems are made of multiple organs.', 2: 'The heart = an ORGAN (contains multiple tissue types). An organ system requires multiple organs.', 3: 'A liver cell = a CELL — the simplest level of organisation.' }",
     r"wrong_explanations: { 1: 'Muscle tissue is a tissue. An organ system is several organs working together.', 2: 'The heart is one organ. An organ system is several organs working together.', 3: 'A liver cell is a cell, the simplest level.' }"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("{ text: 'Tissue', correct: false, reply: 'A tissue is a group of cells.' }, { text: 'Organ system', correct: true }, { text: 'Cell', correct: false, reply: 'A cell is the smallest level.' }",
     "{ text: 'Tissue layer', correct: false, reply: 'A tissue is a group of cells.' }, { text: 'Organ system', correct: true }, { text: 'Single cell', correct: false, reply: 'A cell is the smallest level.' }"),
    ("links: ['A tissue is a group of cells with a similar structure and function.', 'The stomach contains muscle, glandular and epithelial tissue.', 'Several tissues working together to do one job make an organ.'],",
     "links: ['The stomach contains muscle, glandular and epithelial tissue.', 'These tissues work together to digest food.', 'Several tissues working together make an organ, so the stomach is an organ, not a tissue.'],"),
    ("['A group of different organs working together', false], ['One specialised cell that does a single job', false], ['Another name for an organ in the body', false]],",
     "['A group of different organs working together as one', false], ['One specialised cell that does a single job in the body', false], ['Another name for an organ, such as the heart', false]],"),
    ("opts: [['The digestive system', true], ['Muscle tissue', false], ['The heart', false], ['A liver cell', false]],",
     "opts: [['The digestive system', true], ['Muscle tissue', false], ['The human heart', false], ['A single liver cell', false]],"),
    ("2: 'That is the smaller divided by the bigger. Divide the bigger by the smaller.'",
     "2: 'That is 2 ÷ 20, with no conversion. Convert first: 2 mm = 2000 µm, then 2000 ÷ 20.'"),
    ("{ k: 2, n: 'Organ', size: 'a few cm' },",
     "{ k: 2, n: 'Organ', size: 'about 10 cm' },"),
    ('organ (a few cm)',
     'organ (about 10 cm)'),
    ("'Cells, e.g. a muscle cell, about 50 µm.'",
     "'Cells, e.g. a muscle cell, tens of µm across.'"),
    # Pupil walk, 18 Nov 2026: the lean page has no example-placing bench, so ladderFig's
    # right-hand examples column (x 350+) is always empty, and its dashed divider at x 330 ran
    # through the ends of the size labels. Drop the divider and trim the figure to what it draws.
    ("b += D.line(330, 40, 330, 386, 2, C.muted, ' stroke-dasharray=\"4 4\"') + D.T(256, 30, 'typical size',",
     "b += D.T(256, 30, 'typical size',"),
    ("return D.svg(560, 400, b, 'Ladder of organisation",
     "return D.svg(360, 400, b, 'Ladder of organisation"),
]

LESSON = {
    "slug": "principles-of-organisation",
    "start": {
        "setup": "The stomach churns food, makes digestive juices and has a lining.",
        "question": "If you had to guess, is it made of one kind of cell or several kinds?",
        "options": [
            ("One kind of cell",
             "Several kinds. The stomach has muscle tissue, glandular tissue and epithelial "
             "tissue, and each tissue is made of a different kind of cell."),
            ("Several kinds of cell",
             "Several kinds. The stomach has muscle tissue, glandular tissue and epithelial "
             "tissue, and each tissue is made of a different kind of cell."),
        ],
        "answer": 1,
    },
    "words": ["tissue", "organ", "organ system", "organism"],
    "knowledge": [
        {"kind": "card", "title": "Cells, tissues and organs",
         "body": ["Cells are the basic building blocks of all living organisms.",
                  "A tissue is a group of cells with a similar structure and function.",
                  "Organs are aggregations of tissues performing specific functions. An organ is "
                  "several different tissues working together.",
                  "Organs are organised into organ systems, which work together to form "
                  "organisms."]},
        {"kind": "reveal", "title": "The five levels",
         "cols": ["What it is", "Example"],
         "rows": [
             ("Cell", "The basic building block of all living organisms", "A muscle cell"),
             ("Tissue", "A group of cells with a similar structure and function", "Muscle tissue"),
             ("Organ", "Several tissues working together to do a specific job", "The stomach"),
             ("Organ system", "Several organs working together", "The digestive system"),
             ("Organism", "Organ systems working together", "A human"),
         ]},
        {"kind": "card", "title": "The stomach is an organ",
         "body": ["The stomach contains three tissues.",
                  {"points": [
                      "Muscle tissue contracts to churn the food.",
                      "Glandular tissue produces digestive juices.",
                      "Epithelial tissue covers the inside and outside of the stomach.",
                  ]},
                  "Several tissues working together make it an organ. The stomach is one organ in "
                  "the digestive system."]},
        {"kind": "card", "title": "Size and scale",
         "body": ["Each level is many times bigger than the one below it.",
                  {"slot": "legacy-fig:ladderFig"},
                  "To compare two sizes, put them in the same unit, then divide the bigger size "
                  "by the smaller size.",
                  {"points": ["1 mm = 1000 µm", "1 cm = 10 mm", "1 m = 100 cm"]},
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A tissue is a group of different organs.",
              "A tissue is a group of cells with a similar structure and function."),
             ("The heart is an organ system.",
              "The heart is one organ. Several organs working together make an organ system."),
             ("Divide a size in mm by a size in µm.",
              "Put both sizes in the same unit first, then divide the bigger by the smaller."),
         ]}]},
    ],
    "key_fact": "Cells are the basic building blocks of all living organisms. A tissue is a group of "
                "cells with a similar structure and function, organs are aggregations of tissues "
                "performing specific functions, and organs are organised into organ systems, which "
                "work together to form organisms.",
    "deeper": [
        {"kind": "card", "title": "Plants are organised the same way",
         "body": ["A leaf is a plant organ. Its tissues include the epidermis, the palisade "
                  "mesophyll, and the xylem and phloem.",
                  "The roots, stem and leaves together form a plant organ system. Plant tissues "
                  "has the details."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Define</strong>: give the meaning, such as \"a tissue is a group of cells "
             "with a similar structure and function\".",
             "<strong>Describe</strong> the levels: name them in order, with an example of "
             "each.",
             "<strong>Calculate</strong> how many times bigger: same unit first, then bigger "
             "÷ smaller.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
