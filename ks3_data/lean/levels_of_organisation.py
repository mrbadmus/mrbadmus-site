# -*- coding: utf-8 -*-
"""Levels of organisation, in the lean shape. Spec table: docs/lessons/wave1/ks3-levels-of-organisation.md."""

LESSON = {
    "slug": "levels-of-organisation",
    "start": {
        "setup": "Living stomach cells in a dish make acid and enzymes. A sandwich in the dish barely changes.",
        "question": "If you had to guess, what lets a stomach do what the dish cannot?",
        "options": [
            ("Many more cells",
             "Tissues. Each tissue is a group of similar cells, such as muscle to churn food."),
            ("Cells in tissues",
             "Tissues. Each tissue is a group of similar cells, such as muscle to churn food."),
        ],
        "answer": 1,
    },
    "words": ["tissue", "organ", "organ system", "organism"],
    "word_defs": {
        "tissue": "A group of similar cells working together to do one job.",
        "organ": "A group of different tissues working together to do a job.",
        "organ system": "A group of organs working together to do a job.",
        "organism": "A whole living thing.",
    },
    "knowledge": [
        {"kind": "card", "title": "Five levels",
         "body": ["A multicellular organism is organised in levels, like the rungs of a ladder.",
                  "From smallest to largest: cell, tissue, organ, organ system, organism.",
                  "Cells make up tissues. Tissues make up organs.",
                  "Organs make up organ systems. Organ systems make up the organism.",
                  {"figure": "b1-levels"}]},
        {"kind": "reveal", "title": "The levels in an animal and a plant",
         "cols": ["In a human", "In a plant"],
         "rows": [
             ("Cell", "Muscle cell", "Palisade cell"),
             ("Tissue", "Muscle tissue", "Palisade tissue"),
             ("Organ", "Heart", "Leaf"),
             ("Organ system", "Circulatory system", "Transport system: roots, stem and leaves"),
             ("Organism", "A whole human", "A whole plant"),
         ]},
        {"kind": "card", "title": "Tissues",
         "body": ["A tissue is a group of similar cells doing the same job.",
                  "Muscle tissue contracts to move things.",
                  "Blood is a tissue too. It is several kinds of cell in a liquid, working together.",
                  "In plants, palisade tissue makes food. Xylem is a tissue that carries water."]},
        {"kind": "card", "title": "Organs",
         "body": ["An organ is several different tissues working together.",
                  "The stomach has muscle tissue to churn the food.",
                  "It has glandular tissue to make enzymes and acid.",
                  "It has epithelial tissue to line it.",
                  "The heart is an organ. It has muscle tissue, nerve tissue and connective tissue.",
                  "Skin is an organ too, made of several tissues."]},
        {"kind": "card", "title": "A leaf is an organ",
         "body": ["A leaf is made of several tissues working together.",
                  "Its tissues include the epidermis, palisade and spongy tissue, xylem and phloem.",
                  "Palisade tissue makes most of the food.",
                  "Other tissues bring water, let gases in and protect the leaf.",
                  "Together they let the leaf work as an organ."]},
        {"kind": "card", "title": "Organ systems",
         "body": ["The digestive system includes the mouth, stomach, intestines, liver and pancreas.",
                  "The circulatory system is the heart, blood vessels and blood.",
                  "In plants, the roots, stem and leaves work together as a transport system.",
                  "Each system does a job that no single organ could do alone."]},
        {"kind": "card", "title": "Each level does something new",
         "body": ["Stomach cells in a dish make acid and enzymes. They barely digest a sandwich.",
                  "Nothing churns the food, so the enzymes only reach its surface.",
                  "A stomach can, because its tissues are arranged to work together.",
                  "A stomach with no muscle tissue could not churn food, so digestion would be poor.",
                  "What changes from one level to the next is organisation, not size.",
                  "The cell is the lowest level. Parts of a cell, like chloroplasts, are not alive alone."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("An organ is just a bigger tissue.",
              "An organ has several different kinds of tissue working together."),
             ("Blood cannot be a tissue, because it is a liquid.",
              "Blood is a tissue. It is cells in a liquid, working together."),
             ("Skin is a tissue.",
              "Skin is an organ. It is made of several tissues."),
             ("Plants do not have organs.",
              "Leaves, stems and roots are all plant organs."),
         ]}]},
    ],
    "key_fact": "Multicellular organisms are organised in levels: cells, tissues, organs, organ systems and "
                "the whole organism. A tissue is a group of similar cells doing one job. An organ is "
                "several tissues working together.",
    "deeper": [
        {"kind": "card", "title": "Above the organism",
         "body": ["Organisms of one kind living in one place make a population.",
                  "A population can breed and last for many generations. One organism cannot."]},
        {"kind": "card", "title": "An organ on its own",
         "body": ["A donated kidney is kept cold on its way to a hospital.",
                  "On its own, it cannot clean blood. Nothing brings blood to it.",
                  "It works again once a surgeon joins it to blood vessels in a body."]},
    ],
    "try": None,
    "ladder_stem": {
        "apply": "A dish of living stomach cells makes acid and enzymes. It still cannot do the job of a stomach. Why not?",
        "explain": "A leaf is called an organ. The palisade layer inside it is called a tissue. Explain why. "
                   "Use the word “tissues” in your answer.",
        "produce": "A laboratory grows a sheet of living heart muscle cells. It beats steadily on its own. A "
                   "newspaper says they have grown a heart. Say what they have made, and which level it is "
                   "on. Say what a real heart has that the sheet does not.",
    },
    "ladder_ticks": [
        ["Says the leaf does a job that no one of those tissues could do on its own.",
         "Says the tissues each do a part, and together the leaf makes food."],
        ["Names tissues a real heart has that the sheet does not — valves, blood vessels, nerve tissue, connective tissue.",
         "Names something a real heart has, such as nerve tissue, valves or chambers."],
        ["Says the arrangement matters too: four chambers in a particular order, so blood is pushed the right way.",
         "Says the tissues must be arranged in the right way to work together."],
        ["Says that even a complete heart would need to be connected into the circulatory system to be any use.",
         "Says a heart only works as part of an organ system, the circulatory system."],
    ],
    "figures": [
        {"id": "b1-levels", "kind": "diagram", "status": "drawn",
         "art": "b1-levels",
         "title": "The five levels of organisation in a human",
         "desc": "Five pictures one under another, joined by arrows pointing down, each larger than the last. A "
                 "single striped muscle cell with one nucleus, labelled Cell, Muscle cell. A sheet of muscle cells"
                 " side by side, labelled Tissue, Muscle tissue. A heart, labelled Organ, Heart. A small heart "
                 "with blood vessels branching out from it towards the head, arms and legs, labelled Organ system,"
                 " Circulatory system. A whole human figure with the heart in its chest, labelled Organism, Human.",
         "caption": "Each level is made of the level before it.",
         "data": {"levels": [
             {"level": "Cell", "example": "Muscle cell"},
             {"level": "Tissue", "example": "Muscle tissue"},
             {"level": "Organ", "example": "Heart"},
             {"level": "Organ system", "example": "Circulatory system"},
             {"level": "Organism", "example": "Human"},
         ], "arrows": "left-to-right"}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Blood contains many cells, so it is above the cell level.",
            1: "An organ is several different tissues. Blood flows through organs.",
            2: "Blood is on the ladder. Being a liquid does not stop it being a tissue.",
        },
        "apply": {
            1: "A thousand times more cells would still not digest it. Number is not the problem.",
            2: "Lining cells cannot churn food. That needs muscle tissue working with the lining.",
            3: "Enzymes do work in a dish. But nothing churns the food to mix them in.",
        },
    },
    "ks4_becomes": "Organ systems in detail: digestion, circulation and gas exchange.",
}
