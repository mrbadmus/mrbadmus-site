# -*- coding: utf-8 -*-
"""Microscopy, in the lean shape. Spec table: ks4-microscopy.md (AQA 8464 4.1.1.5 / 8461 4.1.1.5, word
for word the same; no HT-only or Biology-only lines: the calculations and standard form are on every
route). Required practical 1 (8464 RP 1, 8461 RP 1, the same number in both) sits under 4.1.1.2 in
the spec; its method lives here, and Animal and plant cells points to it.

LEGACY (batch 3). The ladder and the practice set stay from the Design page. The practice set and
Rung 1 come from the route's subtopic quiz list (K.bank, and K.find with the needle "difference
between magnification and resolution"), so their fixes are in all_subtopics_biology*.py (all four
routes, the same five items, every stem kept), not here. This batch's logic is literal Unicode.

The header binds its spec per route itself ("AQA {{ specName }} ({{ specCode }}) 4.1.1.5"); lean_ks4
reads that form as the literal (25 Nov 2026), so the page gets the usual per-route eyebrow.

logic_edits:
  1. The first worked example was built from the subtopic `fifas` by K.cfifa, whose Fine-tune line
     read "Both values are in mm — no unit conversion needed". Written out, same numbers
     (54 ÷ 0.018 = 3000).
"""

LOGIC_EDITS = [
    ("steps: fq(F[0], 'Nothing to convert.') },",
     "steps: [{ letter: 'C', label: 'Convert', line: 'Nothing to convert: both lengths are in mm.', note: '' }, "
     "{ letter: 'F', label: 'Formula', line: 'M = image size ÷ actual size', note: '' }, "
     "{ letter: 'I', label: 'Insert', line: 'M = 54 ÷ 0.018', note: '' }, "
     "{ letter: 'F', label: 'Fine-tune', line: '54 ÷ 0.018 = 3000', note: '' }, "
     "{ letter: 'A', label: 'Answer', line: 'Magnification = ×3000', note: 'Magnification has no unit.' }] },"),
    # Examiner, 26 Nov 2026: Rung 3 herring. Living versus dead specimens is outside the spec's limit
    # ("the differences in magnification and resolution"); the new herring contradicts link 1, so the
    # chain keeps its one order.
    ("{ text: 'An electron microscope can be used to study living cells.', why: 'The specimen sits in a vacuum, so it must be dead.' }",
     "{ text: 'A light microscope has a higher resolution than an electron microscope.', why: 'It is the other way round: the electron microscope has a much higher resolution.' }"),
    # Examiner, 26 Nov 2026: Rung 1 why, in the spec's words.
    ("why: 'Magnification is a ratio with no unit; resolution is the smallest gap that can be seen, measured in nm.'",
     "why: 'Magnification is how many times bigger the image is. Resolution is the ability to distinguish between two points that are close together.'"),
]

# Examiner, 26 Nov 2026: the header chip names the practical's number (RP 1 in 8464 and 8461, so
# the same on all four routes).
TEMPLATE_EDITS = [
    (">Required practical \u00b7 observing cells<", ">Required practical 1 \u00b7 observing cells<"),
]

EQUATIONS = {
    "EQ_MAG": {"name": "Magnification", "written": "magnification = size of image ÷ size of real object",
               "source": "none",
               "top": {"s": "I", "name": "size of image", "unit": "µm"},
               "bottom": [{"s": "M", "name": "magnification", "unit": "no unit"},
                          {"s": "A", "name": "size of real object", "unit": "µm"}]},
}

LESSON = {
    "slug": "microscopy",
    "start": {
        "setup": "Ribosomes are in every cell, but no light microscope has ever shown one.",
        "question": "If you had to guess, to see a ribosome would you need a microscope that makes things even bigger, or one that shows finer detail?",
        "options": [
            ("One that makes things even bigger",
             "Finer detail, which is resolution. Enlarging a blur only gives a bigger blur. The "
             "electron microscope's higher resolution showed ribosomes for the first time."),
            ("One that shows finer detail",
             "Finer detail, which is resolution. Enlarging a blur only gives a bigger blur. The "
             "electron microscope's higher resolution showed ribosomes for the first time."),
        ],
        "answer": 1,
    },
    "words": ["magnification", "resolution", "light microscope", "electron microscope"],
    "knowledge": [
        {"kind": "card", "title": "Magnification and resolution",
         "body": [{"points": [
             "Magnification is how many times bigger the image is than the real object.",
             "Resolution is the ability to distinguish between two points that are close "
             "together.",
         ]},
                  "Making an image bigger does not add detail. Without a higher resolution you just "
                  "get a bigger blur."]},
        {"kind": "reveal", "title": "Light and electron microscopes",
         "cols": ["Light microscope", "Electron microscope"],
         "rows": [
             ("Uses", "Light", "A beam of electrons"),
             ("Magnification", "Up to about ×2000", "Much higher, up to about ×2 000 000"),
             ("Resolution", "Lower: about 200 nm", "Much higher: about 0.1 nm"),
             ("Shows", "Cells, nuclei and chloroplasts",
              "Ribosomes, and the inside of mitochondria and chloroplasts"),
         ]},
        {"kind": "card", "title": "How electron microscopes changed biology",
         "body": ["Microscopes have improved over time. The first electron microscopes were made "
                  "in the 1930s.",
                  "An electron microscope has much higher magnification and resolving power than a "
                  "light microscope. So it can be used to study cells in much finer detail.",
                  "This has let biologists see and understand many more sub-cellular structures, "
                  "such as ribosomes."]},
        {"kind": "card", "title": "The magnification equation",
         "body": [{"slot": "triangle:EQ_MAG"},
                  {"points": [
                      "magnification = size of image ÷ size of real object",
                      "size of real object = size of image ÷ magnification",
                      "size of image = size of real object × magnification",
                  ]},
                  "Put both sizes in the same unit first: 1 mm = 1000 µm and 1 µm = 1000 nm. "
                  "Magnification has no unit, so write it as ×400."]},
        {"kind": "card", "title": "Calculating with magnification",
         "body": ["Give very large or very small answers in standard form when it helps. "
                  "×50 000 is ×5 × 10⁴, and 0.00015 mm is 1.5 × 10⁻⁴ mm.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Required practical 1: observing cells",
         "body": [{"slot": "legacy-fig:slideFig"},
                  {"points": [
                      "Peel a thin layer of onion epidermis with forceps. Lay it flat on a slide in a "
                      "drop of iodine solution.",
                      "Lower a coverslip at an angle with a mounted needle, so no air bubbles are "
                      "trapped.",
                      "Start with the lowest-power objective. Watching from the side, raise the stage "
                      "until the slide is just below the lens.",
                      "Look through the eyepiece and lower the stage with the coarse focus until the "
                      "cells appear. Sharpen them with the fine focus.",
                      "Switch to a higher-power objective and refocus with the fine focus only.",
                      "Draw what you see with a sharp pencil: clear lines and no shading. Label with "
                      "ruled lines, and add a title and the magnification or a scale bar.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Resolution is how big the image is.",
              "Resolution is the ability to distinguish two points that are close together."),
             ("An image 12 mm wide of a cell 40 µm wide is 12 ÷ 40 = ×0.3.",
              "Convert first: 12 mm = 12 000 µm, so 12 000 ÷ 40 = ×300."),
             ("Magnification is measured in mm.", "Magnification has no unit."),
         ]}]},
    ],
    "key_fact": "Magnification = size of image ÷ size of real object, with both sizes in the same "
                "unit. An electron microscope has much higher magnification and resolution than a "
                "light microscope, so biologists can see many more sub-cellular structures, such as "
                "ribosomes.",
    "deeper": [
        {"kind": "card", "title": "Total magnification",
         "body": ["A light microscope's total magnification is the eyepiece lens's magnification "
                  "times the objective lens's. A ×10 eyepiece with a ×40 objective gives "
                  "×400."]},
        {"kind": "card", "title": "Safety in the practical",
         "body": ["Iodine solution irritates the eyes and stains skin, so wear eye protection. Slides "
                  "and coverslips are thin glass, so hold them by the edges."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>State</strong> what resolution is: \"the ability to distinguish two points "
             "close together\", not \"how clear it is\".",
             "<strong>Calculate</strong>: units matched first, then the equation, the numbers, and "
             "the answer.",
             "<strong>Explain</strong> how electron microscopes helped: higher resolution, so more "
             "detail, so more sub-cellular structures seen.",
         ]}]},
    ],
    "equations": EQUATIONS,
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS, "template_edits": TEMPLATE_EDITS},
}
