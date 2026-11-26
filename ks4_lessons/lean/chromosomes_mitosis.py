# -*- coding: utf-8 -*-
"""Chromosomes, the cell cycle and mitosis, in the lean shape. Spec table: ks4-chromosomes-mitosis.md
(AQA 8464 4.1.2.1-4.1.2.2 / 8461 4.1.2.1-4.1.2.2, word for word the same; no HT-only or Biology-only
lines). Cancer is 4.2.2.7 (Organisation): it was taught and quizzed here, and is now one Dive deeper
line pointing to Cancer. The spec says pupils do not need the phases of mitosis.

LEGACY (batch 2). The ladder and the practice set stay from the Design page. The practice set and
Rung 1 come from the route's subtopic quiz list (K.bank, and K.find with the needle "How many
chromosomes will each daughter cell have"), so their fixes are in all_subtopics_biology*.py (all
four routes, the same five items): three stems kept, two replaced (the benign/malignant tumour item
and "Cancer is caused by...", both 4.2.2.7 content), so those two ks4q: ids retire and two new ids
are added. This batch's logic is literal Unicode.

logic_edits:
  1. Rung 2 part (b): the credited option was visibly the longest; one distractor lengthened.
"""

LOGIC_EDITS = [
    ("options: ['The cell breaks down half of its DNA', 'The cytoplasm and membrane divide: one cell becomes two',",
     "options: ['The cell breaks down half of the DNA it copied', 'The cytoplasm and membrane divide: one cell becomes two',"),
    # Examiner, 26 Nov 2026: Rung 2 part (c) asked for 46 chromosomes "each made of two copies" at Q,
    # a chromatid count beyond the spec. It now asks about S, on the flat stretch after the drop at R
    # (one new cell, before its DNA replicates again from S to T), where the answer is the full set.
    ("{ label: 'How many chromosomes does a human cell hold at Q?', options: ['92 separate chromosomes', '23, half the full set', '46, each made of two copies'], answer: 2 }",
     "{ label: 'How many chromosomes does each new human cell have at S?', options: ['92, double the full set', '23, half the full set', '46, the full set'], answer: 2 }"),
    ("so each new cell has half. Copying doubles the DNA, not the number of chromosomes.'", "so each new cell has half the DNA. Each new cell still gets the full set of 46 chromosomes.'"),
    ("'At Q a human cell still has 46 chromosomes, each now two identical copies.']",
     "'At S each new cell has the full set of 46 chromosomes.']"),
]

LESSON = {
    "slug": "chromosomes-mitosis",
    "start": {
        "setup": "A cell with 4 chromosomes divides into two cells, and each new cell needs all 4.",
        "question": "If you had to guess, does the cell copy its chromosomes before it divides, or share out the 4 it has?",
        "options": [
            ("Copy them first",
             "It copies them first. The DNA replicates, so each new cell gets a full set of 4."),
            ("Share out the 4 it has",
             "It copies them first. Sharing out 4 would give each new cell only 2, half a set."),
        ],
        "answer": 0,
    },
    "words": ["chromosome", "gene", "cell cycle", "mitosis"],
    "knowledge": [
        {"kind": "card", "title": "Chromosomes and genes",
         "body": [{"points": [
             "The nucleus of a cell contains chromosomes made of DNA molecules.",
             "Each chromosome carries a large number of genes.",
             "In body cells the chromosomes are normally found in pairs. A human body cell has 46 "
             "chromosomes, in 23 pairs.",
         ]}]},
        {"kind": "card", "title": "The cell cycle",
         "body": [{"slot": "fig:cell-cycle-stages"},
                  "Cells divide in a series of stages called the cell cycle. The genetic material is "
                  "doubled and then divided into two identical cells."]},
        {"kind": "reveal", "title": "The three stages",
         "cols": ["What happens"],
         "rows": [
             ("Stage 1: growth and DNA replication",
              "The cell grows and increases the number of sub-cellular structures, such as "
              "ribosomes and mitochondria. The DNA replicates to form two copies of each chromosome."),
             ("Stage 2: mitosis",
              "One set of chromosomes is pulled to each end of the cell, and the nucleus divides."),
             ("Stage 3: division",
              "The cytoplasm and cell membranes divide to form two identical cells."),
         ]},
        {"kind": "card", "title": "Why mitosis matters",
         "body": ["Cell division by mitosis is important in the growth and development of "
                  "multicellular organisms. The new cells are genetically identical to the parent "
                  "cell.",
                  {"points": [
                      "Growth: one fertilised egg divides again and again to make a whole body.",
                      "Repair: new cells heal a cut or a broken bone.",
                      "Replacement: worn-out cells, such as skin cells, are replaced.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The DNA is copied after the cell divides.",
              "The DNA replicates before the cell divides, so each new cell gets a full set of "
              "chromosomes."),
             ("Mitosis makes four cells, each with half the chromosomes.",
              "Mitosis makes two identical cells with the full set. Halving happens in meiosis, which "
              "makes sperm and egg cells."),
             ("Mitosis is the whole cell cycle.",
              "Mitosis is one stage: the chromosomes are pulled apart and the nucleus divides."),
         ]}]},
    ],
    "key_fact": "In the cell cycle the cell grows and its DNA replicates. In mitosis one set of "
                "chromosomes is pulled to each end of the cell and the nucleus divides. Then the "
                "cytoplasm and cell membranes divide, forming two identical cells, which is how "
                "multicellular organisms grow and develop.",
    "deeper": [
        {"kind": "card", "title": "Mitosis and cancer",
         "body": ["Cancer is the result of changes in cells that lead to uncontrolled growth and "
                  "division. Cancer has the details."]},
        {"kind": "card", "title": "What you do not need",
         "body": ["AQA does not ask for the separate phases inside mitosis. Learn the three stages "
                  "of the cell cycle."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> the cell cycle: the three stages, in order.",
             "<strong>Explain</strong> why the new cells are identical: the DNA is copied, then one "
             "copy of each chromosome goes to each new cell.",
             "<strong>Use</strong> a graph: quote the values you read from it.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
