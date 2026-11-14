# -*- coding: utf-8 -*-
"""Unicellular organisms, in the lean shape. Spec table: docs/lessons/wave1/ks3-unicellular-organisms.md."""

LESSON = {
    "slug": "unicellular-organisms",
    "start": {
        "setup": "A Paramecium is one cell, about a quarter of a millimetre long. It swims, feeds and "
                 "splits in two.",
        "question": "If you had to guess, what makes the Paramecium a whole organism?",
        "options": [
            ("It does every job itself",
             "It does every life process itself. Nothing else feeds it or cleans up after it."),
            ("It can swim about freely",
             "It does every life process itself. Nothing else feeds it or cleans up after it."),
        ],
        "answer": 0,
    },
    "words": ["unicellular", "multicellular", "cilia", "flagellum"],
    "word_defs": {
        "unicellular": "Made of just one cell. That one cell is the whole organism.",
        "multicellular": "Made of many cells, which are usually specialised.",
        "cilia": "Tiny hair-like parts on a cell's surface. They beat together, like oars.",
        "flagellum": "A long tail like a whip, which a cell beats to swim.",
    },
    "knowledge": [
        {"kind": "card", "title": "One cell, a whole organism",
         "body": ["A unicellular organism is made of one cell.",
                  "That one cell carries out all seven life processes by itself.",
                  "A cell in your body does one job. The rest of your body does the others for it.",
                  {"figure": "b1-unicellular"},
                  "At ×400 you can see a Paramecium's cilia and its contractile vacuole."]},
        {"kind": "reveal", "title": "How some unicellular organisms are adapted",
         "cols": ["How it moves", "How it feeds", "Another adaptation"],
         "rows": [
             ("Amoeba", "Changes shape, pushing out parts of itself.",
              "Flows around food and takes it inside itself.",
              "A contractile vacuole pumps out extra water."),
             ("Paramecium", "Beats its cilia.",
              "Cilia sweep food into a groove, called the oral groove.",
              "Contractile vacuoles pump out extra water."),
             ("Euglena", "Beats its flagellum.",
              "Makes food in its chloroplasts, using light. It can also take in food.",
              "An eyespot helps it find light."),
             ("Yeast", "It does not swim.",
              "Takes in sugar through its surface.",
              "A cell wall. It reproduces by budding off new cells."),
         ]},
        {"kind": "reveal", "title": "A Paramecium and one of your cheek cells",
         "cols": ["Paramecium", "Your cheek cell"],
         "rows": [
             ("Movement", "Swims by beating its cilia.", "Does not move. It is held in place."),
             ("Nutrition", "Sweeps food into its oral groove and digests it inside itself.",
              "Is fed. The blood brings it glucose."),
             ("Excretion", "Waste such as carbon dioxide diffuses out through its membrane.",
              "Waste passes into the blood. Organs such as the kidneys remove it."),
             ("Water", "Contractile vacuoles pump out water that keeps seeping in.",
              "Your body keeps the fluid around it steady."),
             ("Sensitivity", "Senses an obstacle and backs away.", "Nerve cells do this for the whole body."),
             ("Reproduction", "Splits in two, making two organisms.",
              "Divides to replace worn-out cells. You are still one organism."),
         ]},
        {"kind": "card", "title": "Why a Paramecium needs a contractile vacuole",
         "body": ["Water keeps moving into a Paramecium from the pond.",
                  "Its contractile vacuole fills with the extra water and squeezes it out.",
                  "Your body keeps the fluid around your cells steady, so they need no such vacuole."]},
        {"kind": "card", "title": "Bacteria have no nucleus",
         "body": ["A bacterium is a single cell with no nucleus.",
                  "Its DNA is a loose loop in the cytoplasm. Its instructions are still there.",
                  "So a bacterium can divide, sometimes every twenty minutes.",
                  "A red blood cell lost its nucleus and its DNA. It can never divide.",
                  {"figure": "b1-cell-sizes"},
                  "A bacterium is about 0.002 mm long. At ×400 it still looks like a dot."]},
        {"kind": "card", "title": "Telling an organism from part of one",
         "body": ["Moving, size and shape do not decide it. Sperm cells swim, and they are part of a body.",
                  "Check whether the cell does every life process for itself.",
                  "A whole organism finds or makes its own food, and reproduces on its own.",
                  "A cell fed or held in place by a body is part of an organism.",
                  "A cell wall does not prove it is a plant. Yeast and bacteria have walls too.",
                  "No chloroplasts does not rule out a plant cell. Root cells have none."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A single cell cannot be a whole living thing.",
              "A unicellular organism is one cell that does all seven life processes."),
             ("No nucleus means no instructions, so a bacterium cannot divide.",
              "Its DNA is loose in the cytoplasm, so it can divide."),
             ("A single-celled organism is simpler than one of your cells.",
              "It often has more parts, like cilia, because it must do every job itself."),
             ("If a cell swims, it must be a whole organism.",
              "Sperm cells swim, and they are part of an organism."),
         ]}]},
    ],
    "key_fact": "A unicellular organism is a single cell that carries out all seven life processes itself. "
                "Adaptations such as cilia, a flagellum and a contractile vacuole help it survive alone.",
    "deeper": [
        {"kind": "card", "title": "Plant or animal",
         "body": ["Euglena makes food from light, like a plant.",
                  "It also swims and can take in food, like an animal.",
                  "Single-celled life does not sort neatly into plants and animals."]},
        {"kind": "card", "title": "Cilia in you",
         "body": ["Cells lining your airways have cilia too.",
                  "On a Paramecium, cilia move the whole organism.",
                  "In your airways, the cells stay still. The cilia sweep mucus and dust along."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "A single cell moves on its own. It has mitochondria and is about 0.05 mm long. Which "
                  "fact would best show whether it is an organism or part of one?",
        "apply": "A red blood cell has no nucleus and can never divide. A bacterium has no nucleus and "
                 "can divide every twenty minutes. What explains the difference?",
        "explain": "A Paramecium and your cheek cell are both single cells. Explain why the Paramecium needs "
                   "cilia, an oral groove and a contractile vacuole. Explain why your cheek cell needs none "
                   "of them.",
        "produce": "A student finds a single cell in water from a plant pot. It has a wall. "
                   "It has no chloroplasts. It buds off smaller copies of itself. The student says it "
                   "must be part of a plant, because it has a wall. Are they right? Which fact would you use "
                   "instead? What would you still want to check?",
    },
    "ladder_ticks": [
        ["Links each of the three structures to a process it does for itself — moving, feeding, and getting rid of water.",
         "Says cilia are for moving, the groove for feeding, the vacuole for removing water."],
        ["Names at least one thing the body does for the cheek cell — feeds it, moves things to it, holds it in place, or keeps the fluid around it steady.",
         "Names one thing the body does for the cheek cell, like feeding or holding it."],
        ["Ends on the discriminator rather than on size or on how interesting either cell looks.",
         "Ends by saying what makes the difference: doing every life process alone."],
        ["Says a wall does not settle it, and gives a reason — walls are not unique to plants.",
         "Says a wall does not prove it is a plant. Yeast and bacteria have walls too."],
        ["Picks budding off copies of itself as the fact that does the work, and says why: it is reproducing on its own.",
         "Picks budding off copies as the key fact, because it is reproducing on its own."],
        ["Names something they would still check — whether it feeds itself, or whether it is attached to anything larger.",
         "Names a check, such as whether it feeds itself or is attached to something larger."],
    ],
    "figures": [
        {"id": "b1-unicellular", "kind": "diagram", "status": "drawn",
         "art": "b1-unicellular",
         "title": "Three unicellular organisms, with their adaptations labelled",
         "desc": "Three single cells, one under another, not to scale. An Amoeba, an irregular blob pushing out "
                 "two rounded arms, with a nucleus, a food vacuole holding a smaller cell, and a contractile "
                 "vacuole. A Paramecium, a slipper shape fringed all round with short hairs, with an oral groove "
                 "on one side, a nucleus and two star-shaped contractile vacuoles. A Euglena, a long spindle shape"
                 " with one whip-like flagellum at the front, a red eyespot near its base, green chloroplasts and "
                 "a nucleus. Each feature has a ruled label line.",
         "caption": "Each one is a whole organism in a single cell. Not to scale.",
         "data": {"organisms": [
             {"kind": "amoeba", "label": "Amoeba",
              "parts": ["nucleus", "food vacuole", "contractile vacuole", "cell membrane"]},
             {"kind": "paramecium", "label": "Paramecium",
              "parts": ["cilia", "oral groove", "nucleus", "contractile vacuole"]},
             {"kind": "euglena", "label": "Euglena",
              "parts": ["flagellum", "eyespot", "chloroplasts", "nucleus"]},
         ], "to_scale": False}},
        {"id": "b1-cell-sizes", "kind": "diagram", "status": "drawn", "art": "scale-bars",
         "title": "A Paramecium, a cheek cell and a bacterium, compared to scale",
         "desc": "Three horizontal bars, one under another. The top bar, labelled Paramecium, runs the full "
                 "width and is marked 0.25 mm long. The middle bar, labelled Cheek cell, is about a quarter "
                 "as long and is marked 0.06 mm across. The bottom bar, labelled Bacterium, is a tiny "
                 "sliver and is marked 0.002 mm long.",
         "caption": "Lengths drawn to scale.",
         "data": {"rows": [
             {"id": "paramecium", "name": "Paramecium", "size": "0.25 mm long", "pct": 100},
             {"id": "cheek", "name": "Cheek cell", "size": "0.06 mm across", "pct": 24},
             {"id": "bacterium", "name": "Bacterium", "size": "0.002 mm long", "pct": 0.8},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Speed tells you nothing. Sperm cells move fast, and they are part of a body.",
            2: "Busy cells of every kind have many mitochondria. That cannot tell them apart.",
            3: "Size does not decide it. Single-celled organisms come in many sizes.",
        },
        "apply": {
            1: "Size is not the reason. The difference is whether the DNA is still there.",
            2: "The red blood cell lost its DNA with its nucleus. The bacterium never had a nucleus.",
            3: "Nothing divides without instructions. Each new bacterium gets a copy of the DNA loop.",
        },
    },
    "safety_note": "Pond water can carry germs. Keep it away from your mouth and any cuts. Wash your hands "
                   "afterwards.",
}
