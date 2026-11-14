# -*- coding: utf-8 -*-
"""Animal and plant cells, in the lean shape. Spec table: docs/lessons/wave1/ks3-animal-and-plant-cells.md."""

LESSON = {
    "slug": "animal-and-plant-cells",
    "start": {
        "setup": "Cells can have seven parts. Think of a cheek cell and an oak leaf cell.",
        "question": "If you had to guess, does a cheek cell have anything a leaf cell lacks?",
        "options": [
            ("Yes, at least one",
             "Of the seven parts, all of a cheek cell's are in a leaf cell. The leaf cell has three more."),
            ("No, not one",
             "Of the seven parts, all of a cheek cell's are in a leaf cell. The leaf cell has three more."),
        ],
        "answer": 1,
    },
    "words": ["nucleus", "cell membrane", "cell wall", "chloroplast"],
    "word_defs": {
        "nucleus": "Contains the genetic material that controls what the cell does.",
        "cell membrane": "A thin layer around every cell. It controls what goes in and out.",
        "cell wall": "A strong layer outside the membrane of a plant cell. It is made of cellulose.",
        "chloroplast": "The part of a plant cell where light is absorbed to make food.",
    },
    "knowledge": [
        {"kind": "card", "title": "Animal and plant cells",
         "body": [{"figure": "b1-cell-pair"},
                  "Of the seven parts here, every animal cell part is in a plant cell too.",
                  "Plant cells also have a cell wall and a large vacuole.",
                  "Plant cells that get light also have chloroplasts."]},
        {"kind": "reveal", "title": "Seven parts and their jobs",
         "cols": ["Job", "Animal cell", "Plant cell"],
         "rows": [
             ("Nucleus", "Contains the genetic material that controls the cell.", "Yes", "Yes"),
             ("Cytoplasm", "A jelly where most of the cell's chemical reactions happen.", "Yes", "Yes"),
             ("Cell membrane", "Controls what goes into and out of the cell.", "Yes", "Yes"),
             ("Mitochondria", "Where aerobic respiration releases energy from glucose.", "Yes", "Yes"),
             ("Cell wall", "Made of cellulose. It strengthens the cell and stops it bursting.", "No", "Yes"),
             ("Vacuole", "A large space filled with cell sap. It keeps the cell firm.", "No large vacuole", "Yes"),
             ("Chloroplasts", "Absorb light to make food by photosynthesis.", "No",
              "Only in cells that get light"),
         ]},
        {"kind": "card", "title": "Wall and membrane",
         "body": ["A plant cell has both. The wall is on the outside, with the membrane just inside it.",
                  "Water and dissolved substances pass straight through the wall.",
                  "The membrane controls what gets into the cell and what leaves it.",
                  "In pure water, cells take in water and swell.",
                  "An animal cell can burst. The wall stops a plant cell bursting."]},
        {"kind": "card", "title": "The vacuole keeps a plant firm",
         "body": ["The vacuole is full of cell sap. It pushes out against the cell wall.",
                  "This keeps the cell firm and helps hold the plant up.",
                  "When a plant is short of water, its vacuoles shrink.",
                  "The cells go soft and the plant wilts."]},
        {"kind": "card", "title": "Not every plant cell is green",
         "body": ["Chloroplasts are only made in cells that get light.",
                  "Root cells have no chloroplasts, because no light reaches them.",
                  "Onion bulb cells have none either.",
                  "A plant cell with no chloroplasts is still a plant cell."]},
        {"kind": "card", "title": "Other cells with walls",
         "body": ["Plants are not the only living things with cell walls.",
                  "Fungi, such as yeast, have cell walls. So do bacteria.",
                  "Their walls are not made of cellulose.",
                  "So a wall on its own does not prove a cell came from a plant."]},
        {"kind": "card", "title": "What a school microscope can show",
         "body": ["At ×400 you can see a leaf cell's wall, nucleus, vacuole and chloroplasts.",
                  "You cannot see its mitochondria or its membrane. They are still there.",
                  "A chloroplast is several times wider than a mitochondrion.",
                  "Mitochondria are too small to see clearly with a school microscope.",
                  "The membrane is only a few molecules thick. It is pressed against the wall.",
                  "In a cheek cell, the edge you see marks where the membrane is.",
                  "A light microscope cannot show detail below a certain size.",
                  "This limit is called its resolution.",
                  "Turning up the magnification then only gives a bigger, blurrier image."]},
        {"kind": "card", "title": "Staining cells",
         "body": ["Most cell parts are almost see-through, so stains are added.",
                  "Methylene blue stains a cheek cell. Its nucleus becomes the darkest thing you see.",
                  "Iodine solution is used to stain onion cells.",
                  "To get cheek cells, rub a clean cotton bud inside your cheek. Smear it on a slide."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A plant cell has a wall instead of a membrane.",
              "A plant cell has both. The membrane is just inside the wall."),
             ("Every plant cell has chloroplasts.",
              "Only cells that get light have them. Root cells have none."),
             ("If you cannot see mitochondria, the cell has none.",
              "They are there. They are too small to see with a school microscope."),
             ("Only plant cells have walls.",
              "Fungi and bacteria have cell walls too."),
         ]}]},
    ],
    "key_fact": "Animal and plant cells both have a nucleus, cytoplasm, a cell membrane and mitochondria. "
                "Plant cells also have a cell wall, a large vacuole and chloroplasts. Only plant cells "
                "that get light have chloroplasts.",
    "deeper": [
        {"kind": "card", "title": "More parts at GCSE",
         "body": ["Cells have other tiny parts too, such as ribosomes.",
                  "An electron microscope can show these, and the membrane, clearly."]},
        {"kind": "card", "title": "Cellulose in your kitchen",
         "body": ["Celery is stringy because of cellulose in its cell walls.",
                  "Paper is made mostly of cellulose from wood."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "A cell has a membrane, cytoplasm, a nucleus and mitochondria. It has no wall, large "
                  "vacuole or chloroplasts. Which of these could it be?",
        "apply": "A student says a root hair cell cannot be a plant cell, because it is not green. "
                 "Which answer best explains what is wrong with the reasoning?",
        "explain": "Down a school microscope you can see a leaf cell’s wall, nucleus, vacuole and "
                   "chloroplasts. You cannot see its mitochondria or its membrane. Explain why not.",
        "produce": "A single cell is found in pond water. It has a cell wall, a large vacuole, cytoplasm, a "
                   "nucleus and mitochondria. It has no chloroplasts. Can you say it came from a plant? "
                   "Say what you can conclude and what you cannot.",
    },
    "ladder_ticks": [
        ["Says both are still there — the microscope cannot show them, they are not absent.",
         "Says both are still there. The microscope cannot show them."],
        ["Says a chloroplast is several times wider than a mitochondrion, which is why one shows and the other does not.",
         "Says a chloroplast is several times wider than a mitochondrion, so only the chloroplast shows."],
        ["Says the membrane is thinner again — only a few molecules across.",
         "Says the membrane is only a few molecules thick, and is pressed against the wall."],
        ["Says turning the magnification up would not fix it, because the limit is what the microscope can separate, not how big it makes things.",
         "Says more magnification would not help. A light microscope cannot show detail that small."],
        ["Notes that having no chloroplasts does not rule a plant out — a root cell has none either.",
         "Notes that having no chloroplasts does not rule out a plant. Root cells have none."],
        ["Notes that a wall on its own is not proof, because things that are not plants have walls too.",
         "Notes that a wall is not proof, because fungi and bacteria have walls too."],
    ],
    "figures": [
        {"id": "b1-cell-pair", "kind": "diagram", "status": "drawn",
         "art": "b1-cell-pair",
         "title": "An animal cell and a plant cell, with their parts labelled",
         "desc": "Two cells, one above the other. At the top, an animal cell: a rounded, irregular outline (the "
                 "cell membrane) around pale cytoplasm, a round nucleus near the middle, and several small oval "
                 "mitochondria. Below it, a plant cell: a box shape with a thick outer layer (the cell wall) and a"
                 " thin line just inside it (the cell membrane), a large pale vacuole filling the middle, the "
                 "nucleus pushed to one side in the cytoplasm, green oval chloroplasts round the edge, and small "
                 "mitochondria. Every part has a ruled label line. The plant cell's three extra parts, the cell "
                 "wall, the vacuole and the chloroplasts, are labelled on tinted tags, and a key underneath says "
                 "these are only in plant cells.",
         "caption": "The plant cell has every part the animal cell has, plus three more.",
         "data": {"cells": [
             {"kind": "animal", "label": "Animal cell",
              "parts": ["cell membrane", "cytoplasm", "nucleus", "mitochondria"]},
             {"kind": "plant", "label": "Plant cell",
              "parts": ["cell wall", "cell membrane", "cytoplasm", "nucleus", "mitochondria",
                        "vacuole", "chloroplasts"]},
         ], "highlight_extras": ["cell wall", "vacuole", "chloroplasts"]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "A leaf cell also has a wall and a vacuole. Neither is here.",
            2: "A root hair cell has no chloroplasts. But it does have a wall and a vacuole.",
            3: "No wall and no vacuole rules out a plant cell. Only the cheek cell fits.",
        },
        "apply": {
            0: "Root cells make no chloroplasts at all, because no light reaches them.",
            1: "Roots are not green. Dig one up and look.",
            2: "The green is chlorophyll, inside the chloroplasts. The vacuole holds cell sap.",
        },
    },
    "figure_caption": {"b1-cell-pair": "Of the seven parts, the plant cell has all the animal cell's, plus three more."},
    "safety_note": "Only use cells from your own cheek. Put used cotton buds straight into disinfectant. "
                   "Methylene blue stains skin and clothes.",
}
