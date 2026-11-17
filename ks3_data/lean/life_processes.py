# -*- coding: utf-8 -*-
"""Life processes, in the lean shape. Spec table: docs/lessons/wave1/ks3-life-processes.md.

DRAFT (B1 lean run). HELD until Mide reloads Rung 2: its stored options carry spaced
dashes and two of them would both read "It is not alive" if shortened (see NOTES.md).
"""

LESSON = {
    "slug": "life-processes",
    "start": {
        "setup": "A candle flame moves and grows. It takes in oxygen and gives out waste gases.",
        "question": "If you had to guess, is a candle flame alive?",
        "options": [
            ("Yes, it is alive",
             "It seems to do some life processes. But a flame is not made of cells, so it is not alive."),
            ("No, it is not alive",
             "It seems to do some life processes. But a flame is not made of cells, so it is not alive."),
        ],
        "answer": 1,
    },
    "words": ["organism", "cell", "life processes", "excretion"],
    "word_defs": {
        "organism": "A single living thing. It can be one cell or many cells.",
        "cell": "The smallest living unit. Every living thing is made of one or more cells.",
        "life processes": "The seven things every living thing does. MRS GREN helps you remember them.",
        "excretion": "Getting rid of waste made by the body's own cells.",
    },
    "knowledge": [
        {"kind": "reveal", "title": "MRS GREN: the seven life processes",
         "cols": ["What it means"],
         "rows": [
             ("M: Movement", "Moving all or part of the body. Plants move slowly, like leaves turning to light."),
             ("R: Respiration", "Releasing energy from food. It happens in every living cell."),
             ("S: Sensitivity", "Detecting changes around it and responding to them."),
             ("G: Growth", "Getting bigger over its life."),
             ("R: Reproduction", "Making more living things of the same kind."),
             ("E: Excretion", "Getting rid of waste made by its own cells."),
             ("N: Nutrition", "Taking in food, or making it. Plants make their own food."),
         ]},
        {"kind": "card", "title": "Across a whole life",
         "body": ["Living things carry out these processes across their lives.",
                  "They do not have to do them all at once.",
                  "An acorn in a drawer is not growing or moving. It is still alive.",
                  "Its cells are respiring very slowly."]},
        {"kind": "card", "title": "Every living thing is made of cells",
         "body": ["A cell is the smallest living unit.",
                  "Every living thing is made of one or more cells.",
                  "Yeast is just one cell. You are made of about thirty trillion.",
                  "Some things seem to do life processes but have no cells. They are not alive.",
                  "To check, look at a sample under a microscope.",
                  "Cells show up as many small separate units, each with an edge around it."]},
        {"kind": "reveal", "title": "Alive or not",
         "cols": ["What it does", "Made of cells", "Alive"],
         "rows": [
             ("Candle flame", "Moves, grows, uses oxygen and gives out waste gases",
              "No. It is hot glowing gas.", "No"),
             ("Robot vacuum", "Moves on its own and senses walls and stairs",
              "No. It is plastic, metal and a battery.", "No"),
             ("Acorn in a drawer", "Hardly anything you can see", "Yes", "Yes. Its cells respire slowly."),
             ("Yeast in bread dough", "Respires, grows and reproduces", "Yes, one cell each", "Yes"),
         ]},
        {"kind": "card", "title": "Things that only look like life processes",
         "body": [{"points": [
             "Burning is not respiration. Respiration is a set of reactions inside living cells.",
             "Emptying out dust is not excretion. Excretion removes waste made by the body's own cells.",
             "Charging a battery is not nutrition. No food goes in.",
         ]}]},
        {"kind": "reveal", "title": "Living, once living, never living",
         "cols": ["Which group", "Why"],
         "rows": [
             ("Moss on a wall", "Living", "Its cells are working now."),
             ("A wooden spoon", "Once living", "Wood comes from a tree, which was made of cells."),
             ("A leather boot", "Once living", "Leather is animal skin, which was made of cells."),
             ("A lump of coal", "Once living", "It formed from plants that died millions of years ago."),
             ("A granite pebble", "Never living", "It formed from cooled molten rock. No cells were involved."),
             ("A candle flame", "Never living", "It is hot glowing gas, with no cells."),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("If it moves, it is alive.",
              "A flame moves but is not alive. A tree stays in one place and is alive.", "LIFE-01"),
             ("If something grows on its own, it is alive.",
              "Fire and crystals both grow, but neither is alive. "
              "Living things do all seven life processes and are made of cells.", "LIFE-02"),
             ("A seed in a packet is dead.",
              "Its cells are alive and respiring very slowly."),
             ("Every living thing takes in oxygen.",
              "Some cells respire without oxygen. All living things are made of cells."),
         ]}]},
    ],
    "key_fact": "All living things carry out seven life processes, remembered as MRS GREN. Every living "
                "thing is made of one or more cells. A thing with no cells, like a flame, is not alive.",
    "deeper": [
        {"kind": "card", "title": "Viruses",
         "body": ["A virus is not made of cells.",
                  "It can only copy itself inside a living cell.",
                  "Many biologists say viruses are not alive. Others disagree."]},
        {"kind": "card", "title": "The first cells seen",
         "body": ["In 1665, Robert Hooke looked at a thin slice of cork under a microscope.",
                  "He saw tiny boxes and called them cells.",
                  "They were the walls of dead cork cells."]},
    ],
    "try": None,
    # render-only: the stored rung text stays as it is in the database
    "ladder_stem": {
        "apply": "A robot vacuum crosses the floor on its own. It senses the stairs. It drives to its "
                 "charger when its battery is low. Which statement is right?",
        "produce": "A probe on Mars finds an orange crust. It spreads across rock. It takes in one gas and "
                   "gives out another. Write the one test you would use to decide if it is alive. Say what "
                   "result would mean it is alive.",
    },
    "ladder_ticks": [
        ["I said the flame does several of the seven life processes.",
         "I said the flame seems to do several of the life processes."],
        ["I said the seven processes describe living things — they do not decide the case on their own.",
         "I said doing some life processes is not enough to show a thing is alive."],
        ["I described what alive would look like — separate units, each with a boundary around it, repeating.",
         "I described what cells look like: small separate units, each with an edge."],
        ["I said spreading and swapping gases are not enough on their own, because a chemical reaction can do both.",
         "I said chemical reactions can also spread and swap gases, so these are not enough."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "A tree stays in one place all its life, and it is alive.",
            2: "Growth happens during a life, not every day. An adult has stopped growing.",
            3: "Some cells respire without oxygen. Every living thing is made of cells.",
        },
        "apply": {
            0: "A flame seems to do several life processes, but it is not alive.",
            1: "That is not the reason. Plants cannot think, and they are alive.",
            2: "Watching for longer will not help. It is parts, wires and a battery, with no cells.",
        },
    },
    # render-only endmatter. NOTE: ks3_data/lean/__init__.py apply() overlays only ks4_becomes and
    # safety_note today; this key needs adding to that tuple (the stored line carries a spaced dash).
    "before_this": "Nothing. This is where the unit starts.",
}
