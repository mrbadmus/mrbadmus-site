# -*- coding: utf-8 -*-
"""Using a microscope, in the lean shape. Spec table: docs/lessons/wave1/ks3-using-a-microscope.md."""

LESSON = {
    "slug": "using-a-microscope",
    "start": {
        "setup": "You have a slide of onion skin. The microscope has three objective lenses.",
        "question": "If you had to guess, which lens should you start with to find the cells?",
        "options": [
            ("The weakest lens",
             "Start on the weakest lens. You see more of the slide, so cells are easier to find."),
            ("The strongest lens",
             "Start on the weakest lens. You see more of the slide, so cells are easier to find."),
        ],
        "answer": 0,
    },
    "words": ["magnification", "eyepiece lens", "objective lens", "field of view"],
    "word_defs": {
        "magnification": "How many times bigger the image is than the real thing.",
        "eyepiece lens": "The lens you look through, at the top of the microscope.",
        "objective lens": "The lens just above the slide. School microscopes usually have three or four.",
        "field of view": "The circle of the slide you can see at one time.",
    },
    "knowledge": [
        {"kind": "card", "title": "Parts of a light microscope",
         "body": [{"figure": "b1-light-microscope"},
                  {"points": [
                      "Eyepiece lens: the lens you look through.",
                      "Objective lenses: lenses of different powers, just above the slide.",
                      "Stage: where the slide sits, held in place by clips.",
                      "Coarse focus: the large knob, for focusing roughly.",
                      "Fine focus: the small knob, for a sharp image.",
                      "Lamp or mirror: shines light up through the slide.",
                      "Diaphragm: controls how much light gets through.",
                  ]},
                  "Light passes up through the specimen. So the specimen must be thin."]},
        {"kind": "card", "title": "Total magnification",
         "body": ["total magnification = eyepiece magnification × objective magnification",
                  {"figure": "b1-magnification-triangle"},
                  "Multiply the two. Never add them.",
                  "A ×10 eyepiece with a ×40 objective gives ×400.",
                  "To work back, divide. A total of ×100 with a ×10 eyepiece needs a ×10 objective."]},
        {"kind": "card", "title": "Worked example",
         "body": ["Riya's eyepiece is ×10. Her objective is ×40. Find the total magnification.",
                  {"points": ["Formula: total magnification = eyepiece × objective",
                              "Insert: total magnification = 10 × 40",
                              "Fine-tune: nothing to convert.",
                              "Answer: ×400"]}]},
        {"kind": "card", "title": "More magnification, less to see",
         "body": [{"figure": "b1-field-of-view"},
                  "As magnification goes up, the field of view gets smaller.",
                  "You see more detail, but less of the slide.",
                  "At high power, only a thin layer is in focus. The rest looks blurred.",
                  "So find the cells on low power first. Then move up."]},
        {"kind": "reveal", "title": "Onion skin with a ×10 eyepiece",
         "cols": ["Total magnification", "Field of view", "Onion cells across it"],
         "rows": [
             ("×4 objective", "×40", "4.5 mm", "About 15"),
             ("×10 objective", "×100", "1.8 mm", "About 6"),
             ("×40 objective", "×400", "0.45 mm", "One or two"),
         ]},
        {"kind": "card", "title": "Estimating the size of a cell",
         "body": ["Divide the field of view by the number of cells across it.",
                  "At ×40 total, 4.5 mm ÷ 15 cells = 0.3 mm per cell."]},
        {"kind": "card", "title": "Making a slide",
         "body": [{"points": [
             "Peel a thin layer of onion skin. Light must be able to pass through it.",
             "Lay it flat on a drop of water on the slide.",
             "Add a drop of iodine solution to stain the cells.",
             "Lower the coverslip at an angle, starting from one edge.",
         ]},
                  "This stops air bubbles being trapped.",
                  "Air bubbles look like neat circles with thick black edges. They are not cells."]},
        {"kind": "card", "title": "Finding the cells",
         "body": [{"points": [
             "Turn the lowest-power objective into place.",
             "Clip the slide onto the stage, over the hole.",
             "Watch from the side. Use the coarse focus to bring the lens close to the slide.",
             "Look down the eyepiece. Turn the coarse focus slowly to move the lens and slide apart.",
             "Stop when the cells appear. Sharpen them with the fine focus.",
             "Move the cells to the middle. Turn to a higher power.",
             "Refocus with the fine focus only.",
         ]},
                  "Watching from the side stops the lens hitting the slide and breaking it."]},
        {"kind": "card", "title": "A biological drawing",
         "body": [{"figure": "b1-biological-drawing"},
                  {"points": [
                      "Use a sharp pencil.",
                      "Draw clear single lines, with no shading or colouring in.",
                      "Draw what you see, not what you expect to see.",
                      "Label the parts with straight lines drawn with a ruler.",
                      "Write the magnification beside the drawing.",
                  ]},
                  "Without the magnification, no one can tell how big the real cells were."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A ×10 eyepiece and a ×40 objective make ×50.",
              "Multiply them. 10 × 40 makes ×400."),
             ("Start on the highest power to see the most.",
              "Start on the lowest power. You see more of the slide."),
             ("Neat circles with thick black edges are cells.",
              "They are air bubbles trapped under the coverslip."),
             ("Magnification is measured in mm.",
              "Magnification has no unit. Write it as ×400."),
         ]}]},
    ],
    "key_fact": "Total magnification = eyepiece magnification × objective magnification. Always multiply. "
                "Start on the lowest power, because higher magnification shows a smaller field of view.",
    "deeper": [
        {"kind": "card", "title": "Electron microscopes",
         "body": ["An electron microscope uses electrons instead of light.",
                  "It can show far smaller things than a light microscope.",
                  "It can show the inside of a mitochondrion."]},
        {"kind": "card", "title": "The first microscopes",
         "body": ["In the 1670s, Antonie van Leeuwenhoek made tiny microscopes with one lens.",
                  "He was one of the first people to see single-celled living things."]},
    ],
    "try": None,
    "ladder_stem": {
        "explain": "Ade finds his cells on ×4. He turns straight to ×40, and the cells vanish. "
                   "Explain what has happened and what he should do.",
        "produce": "Two students disagree about onion cells. Are cells from an outer layer longer than "
                   "cells from an inner layer? Write a method they could use to find out.",
    },
    "ladder_ticks": [
        ["I said that means less of the slide is in front of him — so what he wants can end up outside the view.",
         "I said less of the slide is in view, so the cells can be outside it."],
        ["I said the depth in focus shrinks too, so it can be there and still look blurred.",
         "I said only a thin layer is in focus, so the cells may look blurred."],
        ["I said he should go back to ×4, move what he wants into the middle, then climb through ×10 and refocus at each step.",
         "I said go back to ×4, centre the cells, then go up one lens at a time."],
        ["I said which layer the onion strip comes from — that is the thing being changed.",
         "I said the layer the onion skin comes from is the thing being changed."],
        ["I said the magnification stays the same for every slide, or the comparison is worthless.",
         "I said the magnification stays the same for every slide."],
        ["I said what gets measured and how — cells counted across a known field of view, or measured against the field.",
         "I said what is measured, such as cells counted across a known field."],
    ],
    "figures": [
        {"id": "b1-light-microscope", "kind": "diagram", "status": "drawn",
         "art": "b1-light-microscope",
         "title": "A light microscope with its parts labelled",
         "desc": "A school light microscope seen from the side. From the top down: the eyepiece lens; the body "
                 "tube; a turret holding three objective lenses of different lengths; the stage with two clips "
                 "holding a glass slide over a hole; the diaphragm under the stage; and the lamp at the base. A "
                 "large coarse focus knob and a smaller fine focus knob sit on the arm. Each part has a ruled "
                 "label line to its name. A dashed arrow runs straight up from the lamp, through the hole in the "
                 "stage, the slide, the objective lens and the tube, and out of the eyepiece.",
         "caption": "Light goes up from the lamp, through the slide and the lenses, to your eye.",
         "data": {"labels": [
             {"part": "eyepiece", "text": "Eyepiece lens"},
             {"part": "objectives", "text": "Objective lenses"},
             {"part": "stage", "text": "Stage"},
             {"part": "clips", "text": "Clips"},
             {"part": "coarse", "text": "Coarse focus"},
             {"part": "fine", "text": "Fine focus"},
             {"part": "diaphragm", "text": "Diaphragm"},
             {"part": "lamp", "text": "Lamp"},
         ], "light_path": True}},
        {"id": "b1-magnification-triangle", "kind": "diagram", "status": "drawn", "art": "formula-triangle",
         "title": "The formula triangle for total magnification",
         "desc": "A triangle split by a horizontal line. Total magnification, T, sits in the top part. "
                 "Eyepiece magnification, E, and objective magnification, O, sit side by side in the "
                 "bottom part, with a multiplication sign between them.",
         "caption": "Cover the one you want. Side by side means multiply. One over the other means divide.",
         "data": {"top": {"s": "T", "name": "total", "unit": "×"},
                  "bottom": [{"s": "E", "name": "eyepiece", "unit": "×"},
                             {"s": "O", "name": "objective", "unit": "×"}]}},
        {"id": "b1-field-of-view", "kind": "diagram", "status": "drawn", "art": "scale-bars",
         "title": "The field of view on three objective lenses, drawn to scale",
         "desc": "Three horizontal bars, one under another. The top bar, labelled ×4 objective, runs the full width "
                 "and is marked 4.5 mm. The middle bar, labelled ×10 objective, is two fifths as long and is marked "
                 "1.8 mm. The bottom bar, labelled ×40 objective, is one tenth as long and is marked 0.45 mm.",
         "caption": "Width of slide you can see with a ×10 eyepiece, to scale.",
         "data": {"rows": [
             {"id": "x4", "name": "×4 objective", "size": "4.5 mm across", "pct": 100},
             {"id": "x10", "name": "×10 objective", "size": "1.8 mm across", "pct": 40},
             {"id": "x40", "name": "×40 objective", "size": "0.45 mm across", "pct": 10},
         ]}},
        {"id": "b1-biological-drawing", "kind": "diagram", "status": "drawn",
         "art": "b1-biological-drawing",
         "title": "A good and a poor drawing of the same onion cells",
         "desc": "Two drawings of the same three onion cells, one above the other. The top one, marked with a tick"
                 " and headed Good drawing, has the title Onion cells and is in thin single pencil lines with no "
                 "shading. Each cell is a long box with a small nucleus. Ruled label lines point to Cell wall, "
                 "Nucleus and Cytoplasm, and the words Magnification ×100 are written underneath. The bottom one, "
                 "marked with a cross and headed Poor drawing, has sketchy doubled lines, shading and colouring "
                 "in, no labels and no magnification.",
         "caption": "Single lines, ruled labels and the magnification. No shading.",
         "data": {"cells": 3, "specimen": "onion",
                  "good": {"labels": ["Cell wall", "Nucleus", "Cytoplasm"], "magnification": "×100"},
                  "poor": {"faults": ["sketchy lines", "shading", "colouring", "no labels",
                                      "no magnification"]}}},
    ],
    "ladder_feedback": {
        "recall": {
            1: "The ×40 objective shows only 0.45 mm of slide. The cells are very hard to find.",
            2: "Better than ×40, but not the best start. Always start on the lowest power.",
            3: "The last person may have left ×40 in place. Turn to the lowest power first.",
        },
        "apply": {
            0: "That is 15 + 40. Multiply the two: 15 × 40 = 600.",
            1: "That is the objective on its own. Multiply it by the eyepiece too.",
            3: "One zero too many. 15 × 40 = 600, so it is ×600.",
        },
    },
    "figure_caption": {"b1-biological-drawing": None},      # the bullets under it already say it
    "safety_note": "Microscope lamps get hot, and slides and coverslips are glass. Handle them with care. "
                   "Iodine solution stains skin. Never point a mirror at the Sun.",
}
