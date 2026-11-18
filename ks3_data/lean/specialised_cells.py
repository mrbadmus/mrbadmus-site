# -*- coding: utf-8 -*-
"""Specialised cells, in the lean shape. Spec table: docs/lessons/wave1/ks3-specialised-cells.md.

This lesson owns KS3.B.CELLS.04 (diffusion), which the old page never taught. The diffusion
cards below are new teaching.
"""

LESSON = {
    "slug": "specialised-cells",
    "start": {
        "setup": "A red blood cell starts out with a nucleus. As it matures, it pushes the nucleus out.",
        "question": "If you had to guess, what does the cell gain by losing its nucleus?",
        "options": [
            ("More room inside",
             "More room. The space fills with haemoglobin, which carries oxygen."),
            ("A faster trip",
             "More room. The space fills with haemoglobin, which carries oxygen."),
        ],
        "answer": 0,
    },
    "words": ["specialised cell", "adaptation", "diffusion", "surface area"],
    "word_defs": {
        "specialised cell": "A cell with a shape or parts that suit it to one job.",
        "adaptation": "A feature that helps a cell or an organism do its job.",
        "diffusion": "The spreading out of particles from a high concentration to a low concentration.",
        "surface area": "The area of the outside surface of something.",
    },
    "knowledge": [
        {"kind": "card", "title": "The same parts, suited to a job",
         "body": ["Most cells in a plant or animal are specialised. Each is suited to one job.",
                  "It has the same basic parts as other cells.",
                  "It may have more of some parts, fewer of others, or a special shape.",
                  "Some have extra parts too, such as a tail or cilia.",
                  {"figure": "b1-specialised-cells"}]},
        {"kind": "reveal", "title": "Specialised cells and their adaptations",
         "cols": ["Job", "Adaptations"],
         "rows": [
             ("Red blood cell", "Carries oxygen around the body.",
              "No nucleus, so more room for haemoglobin. No mitochondria, so it uses none of the oxygen it carries. "
              "A disc shape, dished in on both sides, gives a large surface. It is thin and bendy, "
              "to squeeze through narrow blood vessels."),
             ("Sperm cell", "Swims to the egg and joins with it.",
              "A tail to swim. Many mitochondria in the middle section release energy for the tail. "
              "The head carries genetic material."),
             ("Nerve cell", "Carries electrical signals around the body.",
              "Very long, to carry signals a long way. Branched ends connect to other cells."),
             ("Muscle cell", "Contracts to move parts of the body.",
              "Many mitochondria release the energy it needs to contract."),
             ("Ciliated cell", "Lines the airways and sweeps mucus and dust away from the lungs.",
              "Tiny hair-like parts called cilia beat together. Many mitochondria release the energy."),
             ("Root hair cell", "Takes in water and minerals from the soil.",
              "A long thin hair gives a large surface area. No chloroplasts, as no light reaches it. "
              "Many mitochondria."),
             ("Palisade cell", "Makes food by photosynthesis.",
              "Packed with chloroplasts. Tall cells near the top of the leaf, to absorb light."),
         ]},
        {"kind": "card", "title": "Life without a nucleus",
         "body": ["Without a nucleus, a red blood cell cannot repair itself or divide.",
                  "It lasts about 120 days. Bone marrow keeps making new ones."]},
        {"kind": "card", "title": "Why shape matters",
         "body": ["Substances get into a cell through its surface.",
                  "More surface lets substances get in faster.",
                  "A root hair's long thin shape gives a much larger surface than a round cell.",
                  "The hair also reaches between soil particles, where the water is.",
                  "The plant needs water to stay firm, and minerals to grow.",
                  "A red blood cell's disc shape gives more surface than a ball of equal volume."]},
        {"kind": "card", "title": "Diffusion in and out of cells",
         "body": ["Particles spread out from where there are many to where there are few.",
                  "This is diffusion. It goes from a high concentration to a low concentration.",
                  "Diffusion needs no energy from the cell.",
                  {"figure": "b1-diffusion"},
                  "Cells use oxygen for respiration, so the concentration inside stays low.",
                  "So oxygen diffuses into cells through the cell membrane.",
                  "Respiration makes carbon dioxide. It diffuses out of the cell.",
                  "In the lungs, oxygen diffuses into red blood cells."]},
        {"kind": "card", "title": "Busy cells have many mitochondria",
         "body": ["Mitochondria release energy by respiration.",
                  "Cells that work hard all the time have many of them.",
                  "Muscle cells, sperm cells, ciliated cells and root hair cells all do.",
                  "A root hair cell uses this energy to take in minerals.",
                  "Water moves in without the cell using energy."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Specialised cells are made of different parts.",
              "They have the same basic parts. Some add extras, like a tail.", "CELL-14"),
             ("A red blood cell is not a real cell, as it has no nucleus.",
              "It is a cell. It pushed out its nucleus to make room for haemoglobin.", "CELL-15"),
             ("Every cell in your body has a nucleus.",
              "Red blood cells have none.", "CELL-05"),
             ("Diffusion needs energy.",
              "Diffusion needs no energy. Particles spread out from high to low concentration."),
         ]}]},
    ],
    "key_fact": "Specialised cells have adaptations that suit them to one job. Examples are a special "
                "shape or many mitochondria. Oxygen and carbon dioxide move in and out of cells by diffusion. "
                "Diffusion is from a high concentration to a low concentration.",
    "deeper": [
        {"kind": "card", "title": "A very long cell",
         "body": ["The nerve cell from your spine to your toe can be over a metre long.",
                  "Each jump from one cell to the next slows a signal down.",
                  "One long cell carries the signal faster than a chain of short ones."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "A cell is long and thin. It has a wall and a vacuole, but no chloroplasts. It has "
                  "many mitochondria. What is it built for?",
        "explain": "A root hair cell has a long thin hair. Explain how this shape helps the whole plant. "
                   "Explain why a round cell of the same volume would be worse.",
        "produce": "Design a cell to line your windpipe and stop dust reaching your lungs. "
                   "Say which parts it would have more of. Say what would "
                   "go wrong in the body if it stopped working. You may invent a structure, but say which "
                   "problem it solves.",
    },
    "ladder_ticks": [
        ["Says water and dissolved minerals can only enter through the surface, so more surface means a faster rate of absorption.",
         "Says water and minerals enter through the surface, so more surface means faster absorption."],
        ["Gives the cell something on its exposed surface that can move dust along — a fringe of hair-like structures, or your own equivalent, with a reason.",
         "Gives its surface something to move dust along, such as cilia, and says why."],
        ["Turns up mitochondria, because constant sweeping is constant work.",
         "Gives it many mitochondria, because sweeping all the time needs energy."],
        ["Says the surface facing the airway is the one that matters, and the cells sit in a sheet so they can sweep together in one direction.",
         "Says the cilia face the airway and beat together, sweeping one way."],
        ["Follows a failure out to the whole body: dust and mucus stay in the airway instead of being cleared, so infections take hold.",
         "Says if it fails, mucus and dust build up and can reach the lungs."],
    ],
    "figures": [
        {"id": "b1-specialised-cells", "kind": "diagram", "status": "drawn",
         "art": "b1-specialised-cells",
         "title": "Four specialised cells, each with its adaptations labelled",
         "desc": "Four cells, one under another, not to scale. A red blood cell drawn twice: from above, a red "
                 "disc with a paler middle and no nucleus, labelled No nucleus; from the side, a disc thinner in "
                 "the middle than at the rim, labelled Disc shape. A sperm cell with a head holding the nucleus, a"
                 " middle section packed with small mitochondria, and a long wavy tail, labelled Head with genetic"
                 " material, Mitochondria and Tail. A nerve cell with a cell body and short branches, one very "
                 "long fibre and branched ends, labelled Long fibre and Branched ends. A root hair cell, a box "
                 "with a nucleus and a vacuole and one long thin hair growing out between soil particles. A cell "
                 "wall runs outside the membrane all the way round, including round the hair. The hair is "
                 "labelled Long hair, and the words No chloroplasts are written under the cell with no label line.",
         "caption": "The same basic parts, with a different shape or amount for each job. Not to scale.",
         "data": {"cells": [
             {"kind": "red", "label": "Red blood cell", "marks": ["No nucleus", "Disc shape"]},
             {"kind": "sperm", "label": "Sperm cell",
              "marks": ["Head with genetic material", "Mitochondria", "Tail"]},
             {"kind": "nerve", "label": "Nerve cell", "marks": ["Long fibre", "Branched ends"]},
             {"kind": "root", "label": "Root hair cell", "marks": ["Long hair", "No chloroplasts"]},
         ], "to_scale": False}},
        {"id": "b1-diffusion", "kind": "diagram", "status": "drawn",
         "art": "b1-diffusion",
         "title": "Oxygen diffusing into a cell through its membrane",
         "desc": "A section of cell membrane drawn as a double line down the middle. On the left, outside the "
                 "cell, fourteen oxygen molecules crowded together, each drawn as two joined atoms. On the right, "
                 "inside the cell, only three. Three arrows cross the membrane from left to right. The left side "
                 "is labelled High concentration and the right side Low concentration. A key says two joined "
                 "circles are one oxygen molecule.",
         "caption": "Particles diffuse from a high concentration to a low concentration.",
         "data": {"particle": "oxygen", "left": {"label": "Outside the cell", "tag": "High concentration",
                                                  "count": 14},
                  "right": {"label": "Inside the cell", "tag": "Low concentration", "count": 3},
                  "arrows": 3, "direction": "left-to-right", "barrier": "Cell membrane"}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "A red blood cell has no wall, no vacuole and no mitochondria.",
            1: "A cell that traps light is packed with chloroplasts. This one has none.",
            3: "A nerve cell is an animal cell. Animal cells have no wall.",
        },
        "apply": {
            0: "It has a membrane and cytoplasm, and it does a job. It is a cell.",
            1: "It really has no nucleus. The nucleus is pushed out as the cell matures.",
            3: "A nucleus that was switched off would still take up room.",
        },
    },
}
