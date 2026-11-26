# -*- coding: utf-8 -*-
"""Cell specialisation and differentiation, in the lean shape. Spec table: ks4-cell-specialisation.md
(AQA 8464 4.1.1.3-4.1.1.4 / 8461 4.1.1.3-4.1.1.4, word for word the same; no HT-only or Biology-only
lines). The spec names six cells (sperm, nerve, muscle; root hair, xylem, phloem) and asks pupils to
explain structure and function "when provided with appropriate information", so the adaptations
taught are the standard ones and the last card is the method for a cell they have not met.

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is the
page's own hard-coded `bankSrc` (same five items on every route), so its fixes are logic_edits.
Every stem is kept, so every ks4q: id survives. Rung prompts keep their positions, so rung ids
survive. This batch's logic is plain ASCII with \\uXXXX escapes; the edits below are written that
way (generated from the post-ruling logic, so each `old` occurs exactly once).
"""

LOGIC_EDITS = \
[
    # Practice Q1 (sperm mitochondria), stem kept: credited the longest (+30), 'ATP' and 'flagellum' (not in the spec).
    ("opts: [['It needs large amounts of ATP energy to power its flagellum and swim to the egg', true], ['Mitochondria help the sperm digest through the egg membrane', false], ['More mitochondria make the sperm cell larger and more visible', false], ['Mitochondria store the sperm\\u2019s genetic material', false]],",
     "opts: [['To release energy for swimming to the egg', true], ['To digest a way through the egg membrane', false], ['To make the sperm cell bigger and easier to see', false], ['To store the genetic material for the egg', false]],"),
    ("wrong_explanations: { 1: 'Digesting the egg membrane is the function of the ACROSOME \\u2014 an enzyme-filled cap at the tip of the sperm head. Mitochondria provide energy.', 2: 'Sperm cells are actually very small and streamlined to reduce drag \\u2014 larger would mean slower swimming. Mitochondria provide energy, not bulk.', 3: 'Genetic material (DNA) is stored in the NUCLEUS, not in mitochondria. Mitochondria have their own small amount of DNA but this is not what carries genetic information to the egg.' } },",
     "wrong_explanations: { 1: 'Enzymes in the head digest a way into the egg. Mitochondria release energy.', 2: 'Sperm cells are small. Mitochondria release energy.', 3: 'The genetic material is in the nucleus.' } },"),
    # Practice Q2 (red blood cell), stem kept: credited the longest (+16).
    ("opts: [['More internal space for haemoglobin, allowing the cell to carry more oxygen', true], ['Without a nucleus it cannot be destroyed by white blood cells', false], ['It can reproduce more quickly without a nucleus getting in the way', false], ['The absence of a nucleus reduces the cell\\u2019s oxygen needs', false]],",
     "opts: [['More room for haemoglobin, so it carries more oxygen', true], ['It cannot then be destroyed by white blood cells', false], ['It can then divide more quickly to make new cells', false], ['It then needs less oxygen for its own respiration', false]],"),
    ("wrong_explanations: { 1: 'Red blood cells are destroyed: after about 120 days, old ones are removed by white blood cells (phagocytes) in the spleen and liver.', 2: 'Cells without a nucleus CANNOT reproduce \\u2014 red blood cells are made in bone marrow and released as mature, non-dividing cells.', 3: 'Red blood cells have no mitochondria, so they don\\u2019t use the oxygen they carry. Having no nucleus is about making room for haemoglobin.' } },",
     "wrong_explanations: { 1: 'Old red blood cells are destroyed and replaced.', 2: 'A cell with no nucleus cannot divide.', 3: 'Having no nucleus is about making room for haemoglobin.' } },"),
    # Practice Q3 (root hair, no chloroplasts), stem kept: credited the longest with a dash.
    ("opts: [['Root hair cells are underground \\u2014 there is no light available for photosynthesis', true], ['Root hair cells are too small to fit chloroplasts inside', false], ['Chloroplasts would prevent water absorption from the soil', false], ['Root hair cells are a type of prokaryotic cell and cannot have organelles', false]],",
     "opts: [['Roots get no light, so the cell cannot photosynthesise', true], ['Root hair cells are too small to hold chloroplasts', false], ['Chloroplasts would stop water entering the cell', false], ['Root hair cells are prokaryotic, with no organelles', false]],"),
    ("wrong_explanations: { 1: 'Root hair cells are of similar size to leaf cells \\u2014 size is not the limiting factor. The absence of light is the reason.', 2: 'Chloroplasts don\\u2019t block water entry \\u2014 they are simply absent because they would serve no purpose underground where there is no light.', 3: 'All plant cells are EUKARYOTIC. Root hair cells are eukaryotic plant cells \\u2014 they could have organelles, but chloroplasts specifically are not present due to the lack of light.' } },",
     "wrong_explanations: { 1: 'Size is not the reason. There is no light underground.', 2: 'Chloroplasts do not block water. They would have no light to use.', 3: 'Root hair cells are plant cells, which are eukaryotic.' } },"),
    # Practice Q4 (xylem), stem kept: credited the longest with a dash.
    ("opts: [['They are dead and hollow \\u2014 no cell contents blocking the continuous water column', true], ['They contain many chloroplasts to produce energy for pumping water upwards', false], ['They have a large vacuole to store water temporarily', false], ['They have very thin walls to allow water to pass through easily', false]],",
     "opts: [['They are dead and hollow, so water flows through', true], ['They have chloroplasts to make energy for pumping', false], ['They have a large vacuole to store the water', false], ['They have very thin walls to let water pass', false]],"),
    ("wrong_explanations: { 1: 'Xylem cells are dead, so they contain no chloroplasts. Nothing pumps water up the xylem: it is pulled up as water evaporates from the leaves.', 2: 'Xylem cells don\\u2019t store water \\u2014 they are a continuous flow pipe. Vacuoles are a feature of living plant cells for support.', 3: 'Xylem walls are actually THICK and reinforced with lignin \\u2014 this gives them strength to withstand the tension created as water is pulled upwards, preventing the xylem from collapsing.' } },",
     "wrong_explanations: { 1: 'Xylem cells are dead and have no chloroplasts. Nothing pumps the water.', 2: 'Xylem cells are dead, so they have no vacuole.', 3: 'Xylem walls are thick and strengthened by lignin.' } },"),
    # Rung 2 (i): the credited option was visibly the longest (+28).
    ("{ text: 'They give a larger surface area for absorption', correct: true }, { text: 'They help it swim', correct: false, reply: 'It doesn\\u2019t swim; it absorbs.' },\n            { text: 'They store the food', correct: false, reply: 'The folds are about surface area.' }, { text: 'They make it contract', correct: false,",
     "{ text: 'They give a larger surface area to absorb food', correct: true }, { text: 'They help the cell to swim through the gut', correct: false, reply: 'It doesn\\u2019t swim; it absorbs.' },\n            { text: 'They let the cell store more of the food', correct: false, reply: 'The folds are about surface area.' }, { text: 'They help the cell to contract like a muscle', correct: false,"),
    # Rung 2 (ii): the credited option was visibly the longest (+19).
    ("{ text: 'They make the protein fibres', correct: false, reply: 'Ribosomes make proteins.' },\n            { text: 'They carry the impulses', correct: false, reply: 'Nerve cells carry impulses.' }, { text: 'They store oxygen', correct: false,",
     "{ text: 'They make the protein fibres that contract', correct: false, reply: 'Ribosomes make proteins.' },\n            { text: 'They carry the impulses that start contraction', correct: false, reply: 'Nerve cells carry impulses.' }, { text: 'They store the oxygen the muscle needs', correct: false,"),
    # Rung 3 (i) chain: the surface-area link could go first or last. The chain is now the energy reasoning, one order.
    ("links: ['Its long hair-like part gives a large surface area in contact with the soil water.', 'Mineral ions are taken in by active transport, which needs energy.', 'Many mitochondria release that energy by respiration.'],",
     "links: ['Mineral ions are more concentrated inside the root hair cell than in the soil water.', 'So they are taken in by active transport, which needs energy.', 'Many mitochondria release that energy by respiration.'],"),
    # Rung 3 (ii) chain: the lignin link could go anywhere. Each link now follows from the one before.
    ("links: ['Xylem cells are dead and hollow, with no end walls.', 'So they join to form long, open tubes for water to flow through.', 'Lignin strengthens the walls, so the tubes don\\u2019t collapse.'],",
     "links: ['Xylem cells are dead and have no end walls.', 'So they join end to end to form long, hollow tubes.', 'Water flows up these tubes, whose walls are strengthened by lignin so they do not collapse.'],"),
]

LESSON = {
    "slug": "cell-specialisation",
    "start": {
        "setup": None,
        "question": "If you had to guess, would a cell that has to swim look the same as a cell that has to soak up water?",
        "options": [
            ("Yes, cells all look the same",
             "Each type of cell is shaped for its job. A sperm cell has a tail to swim. A root hair "
             "cell has a long root hair with a large surface area."),
            ("No, each is shaped for its job",
             "Each type of cell is shaped for its job. A sperm cell has a tail to swim. A root hair "
             "cell has a long root hair with a large surface area."),
        ],
        "answer": 1,
    },
    "words": ["differentiation", "specialised cell", "sub-cellular structure"],
    "knowledge": [
        {"kind": "card", "title": "Differentiation",
         "body": ["As an organism develops, cells differentiate to form different types of cells. As "
                  "a cell differentiates, it gains different sub-cellular structures so it can carry "
                  "out a certain job. It has become a specialised cell.",
                  {"points": [
                      "Most types of animal cell differentiate at an early stage.",
                      "Many types of plant cell keep the ability to differentiate throughout life.",
                      "In mature animals, cell division is mainly for repair and replacement.",
                  ]},
                  "Differentiation matters because it gives an organism many types of cell, each one "
                  "suited to its own job."]},
        {"kind": "card", "title": "Sperm cells",
         "body": [{"slot": "fig:sperm-cell"},
                  "Job: to swim to an egg and fertilise it.",
                  {"points": [
                      "A tail, to swim to the egg.",
                      "Many mitochondria, to release the energy needed to swim.",
                      "Enzymes in the head, to digest a way into the egg.",
                      "A nucleus with half the number of chromosomes, so the fertilised egg has the "
                      "full number.",
                  ]}]},
        {"kind": "card", "title": "Nerve cells",
         "body": [{"slot": "fig:nerve-cell"},
                  "Job: to carry electrical impulses around the body.",
                  {"points": [
                      "A long axon, to carry impulses over long distances.",
                      "Branched endings, to connect with many other nerve cells.",
                  ]}]},
        {"kind": "card", "title": "Muscle cells",
         "body": ["Job: to contract, so part of the body moves.",
                  {"points": [
                      "Protein fibres that contract, to shorten the cell.",
                      "Many mitochondria, to release the energy needed to contract.",
                  ]}]},
        {"kind": "card", "title": "Root hair cells",
         "body": [{"slot": "fig:root-hair-cell"},
                  "Job: to take in water and mineral ions from the soil.",
                  {"points": [
                      "A long root hair, which gives a large surface area for absorbing water and "
                      "mineral ions.",
                      "Many mitochondria, to release energy for the active transport of mineral ions.",
                      "No chloroplasts, because no light reaches the roots.",
                  ]}]},
        {"kind": "reveal", "title": "Xylem and phloem cells",
         "cols": ["Job", "How it is adapted"],
         "rows": [
             ("Xylem", "Carries water and mineral ions up from the roots",
              "Dead cells with no end walls, joined into hollow tubes. The walls are strengthened "
              "with lignin."),
             ("Phloem", "Carries dissolved sugars around the plant",
              "Elongated living cells. Pores in the end walls let cell sap move from one cell to "
              "the next."),
         ]},
        {"kind": "card", "title": "A cell you have not met",
         "body": ["Use the information you are given. Name a feature, then say how it helps the cell "
                  "do its job.",
                  {"points": [
                      "Many mitochondria: the cell needs a lot of energy from respiration.",
                      "A large surface area, such as folds or a long thin part: the cell absorbs "
                      "something.",
                      "No nucleus: more room for something else, such as haemoglobin in a red blood "
                      "cell.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Root hair cells take in water by active transport.",
              "Water enters by osmosis. Mineral ions enter by active transport."),
             ("Mitochondria make energy.",
              "Mitochondria release energy by respiration."),
             ("Xylem cells are living.",
              "Xylem cells are dead, which leaves hollow tubes for water."),
         ]}]},
    ],
    "key_fact": "As a cell differentiates it gains the sub-cellular structures it needs for its job, "
                "so it becomes a specialised cell. Most animal cells differentiate at an early stage, "
                "but many plant cells can differentiate throughout life.",
    "deeper": [
        {"kind": "card", "title": "Nerve signals",
         "body": ["A signal from the brain to a toe crosses at least one junction between nerve "
                  "cells, called a synapse. No single nerve cell runs the whole way."]},
        {"kind": "card", "title": "Where this goes next",
         "body": ["Cells that can still become many types are stem cells. How water and ions get "
                  "into root hair cells is in Transport in cells. Xylem and phloem are in "
                  "Transpiration and Translocation."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> a feature: what it looks like.",
             "<strong>Explain how</strong> a cell is adapted: the feature, then how it helps the job.",
             "<strong>Suggest</strong> for a cell you are given: use its job.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": LOGIC_EDITS},
}
