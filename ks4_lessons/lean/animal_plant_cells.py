# -*- coding: utf-8 -*-
"""Animal and plant cells, in the lean shape. Spec table: ks4-animal-plant-cells.md (AQA 8464 4.1.1.2 /
8461 4.1.1.2, word for word the same; no HT-only or Biology-only lines). Required practical 1
(microscope: observe, draw and label plant and animal cells) has the same number in both specs; the
full method is on Microscopy, so this card names it and says what can be seen.

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is the
page's own hard-coded `bankSrc` (same five items on every route), so its fixes are logic_edits. Every
stem is kept, so every ks4q: id survives. Rung prompts keep their positions, so rung ids survive.
This batch's logic is plain ASCII with \\uXXXX escapes; the edits below are written that way
(generated from the post-ruling logic, so each `old` occurs exactly once).
"""

LOGIC_EDITS = \
[
    # Practice Q1 (protein synthesis), stem and options kept: replies in capitals with dashes.
    ("wrong_explanations: { 1: 'Mitochondria are the site of aerobic RESPIRATION \\u2014 they release energy from glucose, they don\\u2019t make proteins.', 2: 'The nucleus contains the DNA instructions for making proteins, but the actual assembly of amino acids into proteins happens at RIBOSOMES.', 3: 'Chloroplasts carry out PHOTOSYNTHESIS \\u2014 capturing light energy to make glucose. Not involved in protein synthesis.' } },",
     "wrong_explanations: { 1: 'Mitochondria are where aerobic respiration takes place.', 2: 'The nucleus holds the genetic material. Proteins are made at the ribosomes.', 3: 'Chloroplasts absorb light for photosynthesis.' } },"),
    # Practice Q2 (root cell, no chloroplasts), stem kept: credited option visibly the longest (+33), dash.
    ("opts: [['Root cells are underground \\u2014 no light reaches them, so chloroplasts are not present', true], ['Root cells are too small to contain chloroplasts', false], ['Root cells are prokaryotic and cannot have chloroplasts', false], ['Chloroplasts are only present in animal cells', false]],",
     "opts: [['Roots get no light, so they cannot photosynthesise', true], ['Root cells are too small to hold chloroplasts', false], ['Root cells are prokaryotic, so they have none', false], ['Chloroplasts are only found in animal cells', false]],"),
    ("wrong_explanations: { 1: 'Root cells are eukaryotic plant cells \\u2014 size is not the reason. Palisade cells are similar in size and have many chloroplasts.', 2: 'ALL plant cells are eukaryotic. Root cells are plant cells \\u2014 they are eukaryotic. Only bacteria (and other prokaryotes) lack membrane-bound organelles.', 3: 'Chloroplasts are found in PLANT cells \\u2014 not animal cells. Animal cells never have chloroplasts.' } },",
     "wrong_explanations: { 1: 'Size is not the reason. Leaf cells of a similar size have many chloroplasts.', 2: 'Root cells are plant cells, which are eukaryotic.', 3: 'Animal cells never have chloroplasts.' } },"),
    # Practice Q3 (vacuole), stem kept: credited the longest (+40), dash, 'turgor pressure' (not in the spec).
    ("opts: [['Filled with cell sap \\u2014 contributes to turgor pressure, keeping the cell firm', true], ['Stores chlorophyll for photosynthesis', false], ['Acts as the site of aerobic respiration', false], ['Controls what enters and leaves the cell', false]],",
     "opts: [['It holds cell sap, which keeps the cell firm', true], ['It stores chlorophyll for photosynthesis', false], ['It is where aerobic respiration takes place', false], ['It controls what enters and leaves the cell', false]],"),
    ("wrong_explanations: { 1: 'Chlorophyll is stored in CHLOROPLASTS \\u2014 not the vacuole. The vacuole contains cell sap (sugars and salts).', 2: 'Aerobic respiration occurs in MITOCHONDRIA. The vacuole is a storage compartment.', 3: 'Controlling what enters and leaves = the CELL MEMBRANE. The vacuole is a storage structure filled with cell sap.' } },",
     "wrong_explanations: { 1: 'Chlorophyll is in the chloroplasts. The vacuole holds cell sap.', 2: 'Aerobic respiration takes place in the mitochondria.', 3: 'The cell membrane controls what enters and leaves the cell.' } },"),
    # Practice Q4 (in both cells), stem and options kept: replies in capitals with dashes.
    ("wrong_explanations: { 1: 'Cell walls are only found in plant cells (and bacteria, fungi) \\u2014 NOT in animal cells.', 2: 'Chloroplasts are found only in plant cells that are exposed to light. Animal cells never have chloroplasts.', 3: 'The permanent vacuole is a plant cell feature \\u2014 animal cells do not have a large permanent vacuole (though they may have small temporary vacuoles).' } },",
     "wrong_explanations: { 1: 'Only plant cells have a cell wall. Animal cells never do.', 2: 'Animal cells never have chloroplasts.', 3: 'Animal cells do not have a permanent vacuole.' } },"),
    # Practice Q5 (muscle mitochondria), stem kept: credited the longest, 'ATP' (not in the spec).
    ("opts: [['Muscle cells need much more ATP energy for contraction \\u2014 more mitochondria produce more ATP', true], ['Muscle cells are larger, so they need more organelles to fill the space', false], ['Mitochondria help muscle cells to absorb oxygen from the blood', false], ['Skin cells don\\u2019t respire \\u2014 they don\\u2019t need mitochondria at all', false]],",
     "opts: [['Muscle cells need more energy, released by respiration', true], ['Muscle cells are larger, so they need more organelles', false], ['Mitochondria help muscle cells absorb oxygen from blood', false], ['Skin cells do not respire, so they need no mitochondria', false]],"),
    ("wrong_explanations: { 1: 'Cell size doesn\\u2019t directly dictate organelle number \\u2014 it is energy demand that determines mitochondria count.', 2: 'Oxygen is absorbed by diffusion through the cell membrane \\u2014 mitochondria USE oxygen in respiration, they don\\u2019t absorb it.', 3: 'All living cells respire all the time \\u2014 skin cells do have mitochondria. Active cells simply have FAR MORE.' } }",
     "wrong_explanations: { 1: 'Size is not the reason. Muscle cells need more energy.', 2: 'Oxygen diffuses into cells. Mitochondria use it in respiration.', 3: 'All living cells respire, so skin cells have mitochondria too.' } }"),
    # Rung 3 (ii) chain: links 1 and 2 could be put in either order. Each link now names the one before it.
    ("links: ['Muscle cells contract, which needs a lot of energy.', 'Aerobic respiration takes place in mitochondria, releasing energy.', 'More mitochondria release more energy for contraction.'],",
     "links: ['Muscle cells contract, which needs a lot of energy.', 'That energy is released by aerobic respiration, which takes place in mitochondria.', 'So the more mitochondria a muscle cell has, the more energy it can release.'],"),
]

# The magnification triangle the Design page drew (its EQ_M, unchanged).
EQUATIONS = {
    "EQ_MAG": {"name": "Magnification", "written": "magnification = size of image ÷ size of real object",
               "source": "none",
               "top": {"s": "I", "name": "size of image", "unit": "µm"},
               "bottom": [{"s": "M", "name": "magnification", "unit": "no unit"},
                          {"s": "A", "name": "size of real object", "unit": "µm"}]},
}

LESSON = {
    "slug": "animal-plant-cells",
    "start": {
        "setup": "Your skin is soft and bendy, but a raw carrot snaps cleanly.",
        "question": "If you had to guess, do plant cells have something stiff around them that our cells do not?",
        "options": [
            ("Yes, something stiff",
             "Plant cells have a cell wall made of cellulose, outside the cell membrane. It "
             "strengthens the cell."),
            ("No, they are the same as ours",
             "Plant cells have a cell wall made of cellulose, outside the cell membrane. It "
             "strengthens the cell."),
        ],
        "answer": 0,
    },
    "words": ["nucleus", "mitochondria", "chloroplasts", "cell wall"],
    "knowledge": [
        {"kind": "card", "title": "Parts of animal and plant cells",
         "body": [{"slot": "fig:animal-plant-cells"},
                  "Plant cells have every part an animal cell has. Plant and algal cells also have a "
                  "cell wall made of cellulose, which strengthens the cell. Plant cells often have "
                  "chloroplasts and a permanent vacuole filled with cell sap too."]},
        {"kind": "reveal", "title": "What each part does",
         "cols": ["Job"],
         "rows": [
             ("Nucleus", "Contains genetic material, which controls the activities of the cell"),
             ("Cytoplasm", "Where most chemical reactions happen, controlled by enzymes"),
             ("Cell membrane", "Controls the movement of substances into and out of the cell"),
             ("Mitochondria", "Where aerobic respiration takes place, releasing energy"),
             ("Ribosomes", "Where proteins are made"),
             ("Chloroplasts", "Absorb light for photosynthesis"),
             ("Permanent vacuole", "Filled with cell sap, which keeps the cell firm"),
             ("Cell wall", "Made of cellulose. Strengthens the cell"),
         ]},
        {"kind": "reveal", "title": "Animal cell or plant cell",
         "cols": ["Animal cell", "Plant cell"],
         "rows": [
             ("Nucleus, cytoplasm, cell membrane", "Yes", "Yes"),
             ("Mitochondria and ribosomes", "Yes", "Yes"),
             ("Cell wall", "No", "Yes, made of cellulose"),
             ("Permanent vacuole", "No", "Yes, filled with cell sap"),
             ("Chloroplasts", "No", "Often, in cells that get light"),
         ]},
        {"kind": "card", "title": "Plasmids in bacteria",
         "body": ["Bacterial cells may have plasmids: small rings of DNA, separate from the main "
                  "DNA loop, that carry extra genes. Eukaryotes and prokaryotes has the details."]},
        {"kind": "card", "title": "Required practical 1: looking at cells",
         "body": [{"points": [
                      "Use a light microscope to observe, draw and label plant and animal cells. "
                      "Include a magnification scale.",
                      "You can see the nucleus, cytoplasm, cell membrane, cell wall, vacuole and "
                      "chloroplasts. Ribosomes are too small to see.",
                      "Iodine solution stains the nuclei of onion cells. Methylene blue stains the "
                      "nuclei of cheek cells.",
                  ]},
                  "Microscopy has the full method."]},
        {"kind": "card", "title": "Estimating sizes",
         "body": ["Use an estimate when you only need to compare sizes, for example how much of a "
                  "plant cell its vacuole fills. Compare the part with something you know, such as "
                  "the width of the whole cell."]},
        {"kind": "card", "title": "Magnification",
         "body": [{"slot": "triangle:EQ_MAG"},
                  "Put both sizes in the same unit first: 1 mm = 1000 µm. Magnification has no "
                  "unit, so write it as ×400.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Every plant cell has chloroplasts.",
              "Root cells get no light, so they have no chloroplasts."),
             ("Plant cells have a cell wall instead of a cell membrane.",
              "Plant cells have both. The cell wall is outside the cell membrane."),
             ("Plant cells do not have mitochondria.",
              "Plant cells respire, so they have mitochondria too."),
         ]}]},
    ],
    "key_fact": "Animal cells have a nucleus, cytoplasm, a cell membrane, mitochondria and ribosomes. "
                "Plant cells have these too, plus a cellulose cell wall, a permanent vacuole and "
                "often chloroplasts. Each part has a job, such as aerobic respiration in the "
                "mitochondria and making proteins in the ribosomes.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Name</strong>: the part, using its proper name.",
             "<strong>Compare</strong>: what both cells have, then what only plant cells have.",
             "<strong>Calculate</strong>: convert to one unit, then image size ÷ real size.",
         ]}]},
    ],
    "equations": EQUATIONS,
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": LOGIC_EDITS},
}
