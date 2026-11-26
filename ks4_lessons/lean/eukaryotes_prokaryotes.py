# -*- coding: utf-8 -*-
"""Eukaryotes and prokaryotes, in the lean shape. Spec table: ks4-eukaryotes-prokaryotes.md (AQA 8464
4.1.1.1 / 8461 4.1.1.1, word for word the same; no HT-only or Biology-only lines). Magnification
itself is 4.1.1.5 (Microscopy); it is kept here only as the CFIFA the page already had, because
working out a real size from an image is how the scale of cells is examined.

LEGACY (batch 2). The ladder and the practice set stay from the Design page. The practice set and
Rung 1 come from the route's subtopic quiz list (K.bank, and K.find with the needle "key structural
difference"), so their fixes are in all_subtopics_biology*.py (all four routes, the same five
items), not here. This batch's logic is written with literal Unicode (no \\u escapes).

logic_edits:
  1. The first worked example was built from the subtopic `fifas` by K.cfifa, whose Fine-tune
     line read "Both values already in mm — no conversion needed". It is written out here, with
     the same numbers (30 ÷ 0.003 = 10 000 = 1 × 10⁴).
"""

LOGIC_EDITS = [
    ("steps: withNote(K.cfifa(F[0], 'Nothing to convert: both lengths are in mm.'), 4, 'In standard form: 1 × 10⁴.') },",
     "steps: [{ letter: 'C', label: 'Convert', line: 'Nothing to convert: both lengths are in mm.', note: '' }, "
     "{ letter: 'F', label: 'Formula', line: 'Magnification = Image size ÷ Actual size', note: '' }, "
     "{ letter: 'I', label: 'Insert', line: 'M = 30 ÷ 0.003', note: '' }, "
     "{ letter: 'F', label: 'Fine-tune', line: 'Nothing to rearrange: 30 ÷ 0.003 = 10 000', note: '' }, "
     "{ letter: 'A', label: 'Answer', line: 'Magnification = ×10 000', note: 'In standard form: 1 × 10⁴.' }] },"),
    # Examiner, 26 Nov 2026 (ep-q1, Higher): plant cells are not all 40-80 µm; the check gives the usual range.
    ("close: 'Check: 60 µm sits inside the 40–80 µm typical of a plant cell.'",
     "close: 'Check: 60 µm is a sensible size for a plant cell, which is usually 10–100 µm long.'"),
]

LESSON = {
    "slug": "eukaryotes-prokaryotes",
    "start": {
        "setup": "A liver cell keeps its DNA inside a nucleus.",
        "question": "If you had to guess, is a bacterium's DNA inside a nucleus too, or loose in the cell?",
        "options": [
            ("Inside a nucleus too",
             "A bacterium has no nucleus. Its DNA is a single loop, loose in the cytoplasm."),
            ("Loose in the cell",
             "A bacterium has no nucleus. Its DNA is a single loop, loose in the cytoplasm."),
        ],
        "answer": 1,
    },
    "words": ["eukaryotic", "prokaryotic", "plasmid", "order of magnitude"],
    "knowledge": [
        {"kind": "card", "title": "Eukaryotic cells",
         "body": ["Plant and animal cells are eukaryotic cells. They have a cell membrane, cytoplasm "
                  "and genetic material enclosed in a nucleus."]},
        {"kind": "card", "title": "Prokaryotic cells",
         "body": [{"slot": "fig:prokaryote-cell"},
                  {"points": [
                      "Bacterial cells are prokaryotic cells. They are much smaller than eukaryotic "
                      "cells.",
                      "They have cytoplasm and a cell membrane surrounded by a cell wall.",
                      "The genetic material is not enclosed in a nucleus. It is a single DNA loop.",
                      "There may be one or more small rings of DNA called plasmids.",
                  ]}]},
        {"kind": "reveal", "title": "Animal cell and bacterium compared",
         "cols": ["Animal cell", "Bacterium"],
         "rows": [
             ("Nucleus", "Yes", "No"),
             ("Genetic material", "In chromosomes inside the nucleus",
              "A single DNA loop in the cytoplasm"),
             ("Plasmids", "No", "There may be one or more"),
             ("Cell wall", "No", "Yes"),
             ("Cell membrane and cytoplasm", "Yes", "Yes"),
             ("Mitochondria", "Yes", "No"),
             ("Ribosomes", "Yes", "Yes"),
         ]},
        {"kind": "card", "title": "Units for very small things",
         "body": ["Cells are measured in micrometres (µm). Parts of cells are measured in "
                  "nanometres (nm).",
                  {"points": [
                      "centi (c) means a hundredth: 1 cm = 10 mm",
                      "milli (m) means a thousandth: 1 m = 1000 mm",
                      "micro (µ) means a millionth: 1 mm = 1000 µm",
                      "nano (n) means a billionth (a thousand-millionth): 1 µm = 1000 nm",
                  ]},
                  "Between mm, µm and nm, multiply by 1000 to go to the smaller unit. Divide by "
                  "1000 to go to the bigger unit."]},
        {"kind": "card", "title": "Size and orders of magnitude",
         "body": [{"slot": "fig:cell-bacterium-scale"},
                  "An order of magnitude is a factor of 10. Put both sizes in the same unit, then "
                  "divide the bigger by the smaller.",
                  {"points": [
                      "A liver cell is about 20 µm across and a bacterium about 2 µm long. "
                      "20 ÷ 2 = 10 = 10¹, so the liver cell is one order of magnitude "
                      "bigger.",
                      "A ribosome is about 20 nm across. 2 µm = 2000 nm, and 2000 ÷ 20 = "
                      "100 = 10², so a bacterium is two orders of magnitude longer than a "
                      "ribosome.",
                  ]}]},
        {"kind": "card", "title": "Standard form",
         "body": ["Very small and very large numbers are written in standard form.",
                  {"points": [
                      "A bacterium 2 µm long is 0.002 mm long, which is 2 × 10⁻³ mm.",
                      "A magnification of ×10 000 is ×(1 × 10⁴).",
                  ]}]},
        {"kind": "card", "title": "Working out sizes from an image",
         "body": ["magnification = size of image ÷ size of real object. Put both sizes in the "
                  "same unit first. Microscopy has the full method.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Bacteria have a small nucleus.",
              "Bacteria have no nucleus. Their DNA is a single loop in the cytoplasm."),
             ("A bacterium has a cellulose cell wall.",
              "A bacterium has a cell wall, but it is not made of cellulose."),
             ("1 mm = 100 µm.", "1 mm = 1000 µm."),
         ]}]},
    ],
    "key_fact": "Eukaryotic cells, such as plant and animal cells, have their genetic material "
                "enclosed in a nucleus. Prokaryotic cells, such as bacteria, are much smaller. Their "
                "genetic material is a single DNA loop that is not in a nucleus, and they may also "
                "have plasmids.",
    "deeper": [
        {"kind": "card", "title": "Other eukaryotes",
         "body": ["The cells of fungi and protists are eukaryotic too. Only bacteria are "
                  "prokaryotic in this course."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Compare</strong>: both cells in every sentence, such as \"a bacterium has no "
             "nucleus, whereas an animal cell does\".",
             "<strong>Estimate</strong>: an approximate answer, here to the nearest power of ten.",
             "<strong>Calculate</strong>: units matched before you divide, and a unit on the answer.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
