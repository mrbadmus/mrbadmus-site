# -*- coding: utf-8 -*-
"""Diffusion, osmosis and active transport, in the lean shape. Spec table: ks4-transport-in-cells.md
(AQA 8464 4.1.3.1-4.1.3.3 / 8461 4.1.3.1-4.1.3.3, word for word the same; no HT-only or Biology-only
lines). The osmosis practical is 8464 Required practical 2 and 8461 Required practical 3 (8461
numbers microbiology, 4.1.1.6, as its RP 2), so the practical card is written twice, one per spec
family, and the header chip already reads "Required practical 2" or "3" per route.

LEGACY (batch 4). The ladder and the practice set stay from the Design page. The practice set is the
page's own hard-coded `bankSrc` (same five items on every route), so its fixes are logic_edits. One
practice stem is replaced (it asked for "ATP energy"), so that ks4q: id retires and a new one is
added; the other four stems are kept. Rung prompts keep their positions, so rung ids survive, and
the SA:V worked and attempt steps (sav-w, sav-a) are placed in a card as they were.
This batch's logic is plain ASCII with \\uXXXX escapes; the edits below are written that way
(generated from the post-ruling logic, so each `old` occurs exactly once).
"""

LOGIC_EDITS = \
[
    # Practice Q1 REPLACED (new stem, new id; the old id retires): the stem asked for 'ATP energy', which is not in the spec. Same options and answer.
    ("{ q: 'Which process requires ATP energy to move substances across a cell membrane?', opts: [['Active transport', true], ['Diffusion', false], ['Osmosis', false], ['Both diffusion and osmosis', false]],\n        wrong_explanations: { 1: 'Diffusion is PASSIVE \\u2014 particles move due to their own random kinetic energy, not ATP.', 2: 'Osmosis is also PASSIVE \\u2014 water moves down its own concentration gradient without energy input.', 3: 'NEITHER diffusion nor osmosis requires ATP. Only active transport requires energy \\u2014 that is what distinguishes it from the other two.' } },",
     "{ q: 'Which process needs energy from respiration to move substances across a cell membrane?', opts: [['Active transport', true], ['Diffusion', false], ['Osmosis', false], ['Both diffusion and osmosis', false]],\n        wrong_explanations: { 1: 'Diffusion needs no energy from the cell.', 2: 'Osmosis needs no energy from the cell.', 3: 'Neither needs energy from respiration. Only active transport does.' } },"),
    # Practice Q2 (potato in pure water), stem kept: credited the longest (+40), dash.
    ("opts: [['It gains mass \\u2014 water enters by osmosis from the dilute water into the more concentrated cell contents', true], ['It loses mass \\u2014 salt leaves the potato into the water by diffusion', false], ['Nothing \\u2014 the potato is not permeable to water', false], ['It gains mass because water enters by active transport', false]],",
     "opts: [['It gains mass: water enters the cells by osmosis', true], ['It loses mass: sugar leaves the cells by diffusion', false], ['Its mass stays the same: water cannot get in', false], ['It gains mass: water enters by active transport', false]],"),
    ("wrong_explanations: { 1: 'Salt does diffuse slightly \\u2014 but the dominant effect is water moving by OSMOSIS into the cells, increasing mass.', 2: 'Cell membranes are selectively permeable \\u2014 water moves freely across them by osmosis. The potato is very much permeable to water.', 3: 'Osmosis is PASSIVE \\u2014 it requires no energy input. Water moves down its concentration gradient automatically.' } },",
     "wrong_explanations: { 1: 'The cells are more concentrated than pure water, so water moves in by osmosis.', 2: 'Cell membranes let water through.', 3: 'Osmosis needs no energy. This is osmosis, not active transport.' } },"),
    # Practice Q3 (oxygen removed), stem kept: credited option visibly longer than two of the others.
    ("opts: [['Less oxygen means less aerobic respiration, so less energy is transferred for active transport', true], ['Oxygen is a carrier protein that directly powers active transport', false], ['Without oxygen, the cell membrane becomes impermeable to all substances', false], ['Removing oxygen changes the concentration gradient, making active transport unnecessary', false]],",
     "opts: [['Less aerobic respiration, so less energy is released', true], ['Oxygen itself is the energy that powers the transport', false], ['Without oxygen, the membrane lets nothing through', false], ['Without oxygen, there is no concentration gradient', false]],"),
    ("wrong_explanations: { 1: 'Oxygen does not power active transport directly. It is needed for aerobic respiration, which transfers the energy.', 2: 'The membrane stays intact. What is lost is energy from respiration.', 3: 'Removing oxygen doesn\\u2019t change the gradient. It reduces the energy available to move substances against it.' } },",
     "wrong_explanations: { 1: 'Oxygen does not power it directly. It is needed for aerobic respiration, which releases the energy.', 2: 'The membrane stays the same. What is lost is energy from respiration.', 3: 'The gradient is still there. There is less energy to move substances against it.' } },"),
    # Practice Q4 (plant cell in concentrated salt), stem kept: credited the longest (+50), arrows, 'plasmolysis'.
    ("opts: [['Water leaves by osmosis \\u2192 the cell becomes flaccid \\u2192 the cell membrane pulls away from the cell wall (plasmolysis)', true], ['Water enters by osmosis \\u2192 the cell becomes turgid and very firm', false], ['Salt enters by active transport \\u2192 the cell becomes denser', false], ['The cell bursts because it cannot handle the osmotic pressure', false]],",
     "opts: [['Water leaves the cell by osmosis, so it becomes less firm', true], ['Water enters the cell by osmosis, so it becomes very firm', false], ['Salt enters by active transport, so the cell gets heavier', false], ['The cell bursts, because too much water rushes in', false]],"),
    ("wrong_explanations: { 1: 'Water enters when the EXTERNAL solution is MORE DILUTE than the cell contents. In concentrated salt solution, it is the other way round \\u2014 water leaves.', 2: 'Salt ions may slowly diffuse in, but the dominant effect is OSMOSIS \\u2014 water moves to the MORE CONCENTRATED solution (the salt solution outside), not into the cell.', 3: 'Plant cells have a rigid CELL WALL that prevents bursting \\u2014 unlike animal cells. A plant cell can become flaccid or plasmolyse, but it won\\u2019t burst.' } },",
     "wrong_explanations: { 1: 'Water enters only when the solution outside is more dilute than the cell contents.', 2: 'Osmosis moves water, from the dilute cell contents to the concentrated salt solution.', 3: 'The cell wall stops a plant cell bursting. Here, water leaves.' } },"),
    # Practice Q5 (osmosis definition), stem kept: credited the longest (+48); now the spec's wording, with distractors of the same length.
    ("opts: [['The net movement of water molecules across a partially permeable membrane from a dilute solution to a more concentrated solution', true], ['The movement of any particles from high to low concentration \\u2014 passive', false], ['The movement of water molecules against a concentration gradient using ATP', false], ['The diffusion of water molecules through any membrane in any direction', false]],",
     "opts: [['The diffusion of water from a dilute to a concentrated solution through a partially permeable membrane', true], ['The diffusion of water from a concentrated to a dilute solution through a partially permeable membrane', false], ['The movement of water from a dilute to a concentrated solution using energy from respiration', false], ['The diffusion of dissolved particles from a dilute to a concentrated solution through a membrane', false]],"),
    ("wrong_explanations: { 1: 'The movement of ANY particles from high to low = DIFFUSION. Osmosis is specifically about WATER ONLY through a PARTIALLY PERMEABLE membrane.', 2: 'Movement against a gradient using ATP = ACTIVE TRANSPORT. Osmosis is passive \\u2014 water moves DOWN its concentration gradient.', 3: 'Osmosis only occurs through a PARTIALLY PERMEABLE membrane, not any membrane. And it only moves water in ONE net direction \\u2014 from dilute to concentrated.' } }",
     "wrong_explanations: { 1: 'That is the wrong way. Water moves from the dilute solution to the concentrated solution.', 2: 'Osmosis needs no energy from the cell.', 3: 'Osmosis is the movement of water only.' } }"),
    # First worked example: the Convert and Answer lines were wordy, with dashes. Same numbers: (3.4 − 4.0) ÷ 4.0 × 100 = −15%.
    ("{ letter: 'C', label: 'Convert', line: 'Nothing to convert \\u2014 percentage change is a dimensionless ratio, so the masses may stay in grams (g) as given; the units cancel in the division.' }",
     "{ letter: 'C', label: 'Convert', line: 'Nothing to convert: both masses are in grams.' }"),
    ("{ letter: 'A', label: 'Answer', line: '% change = \\u221215% (a decrease \\u2014 water left by osmosis into the concentrated solution)' }",
     "{ letter: 'A', label: 'Answer', line: '% change = \\u221215% (a loss: water left the cells by osmosis)' }"),
    # Rung 3 (i) chain: links 1 and 2 could be swapped. Link 2 now follows from link 1.
    ("links: ['The sugar solution is more concentrated than the cell contents.', 'Water moves out of the cells by osmosis, from the dilute solution to the more concentrated solution, through the partially permeable membrane.', 'So the cylinder loses mass.'],",
     "links: ['The sugar solution is more concentrated than the cell contents.', 'So water moves out of the cells by osmosis, from the more dilute cell contents to the sugar solution.', 'So the cylinder loses mass.'],"),
    # Rung 3 (ii) chain: links 1 and 2 could be swapped. Link 2 now follows from link 1.
    ("links: ['As an organism gets bigger, its surface area to volume ratio gets smaller.', 'Diffusion across its outer surface alone cannot supply all of its cells: many are a long way from the surface.', 'So it needs exchange surfaces with a large surface area, and a transport system.'],",
     "links: ['As an organism gets bigger, its surface area to volume ratio gets smaller.', 'So diffusion across its outer surface alone cannot supply all of its cells, many of which are far from the surface.', 'So it needs exchange surfaces with a large surface area, and a transport system.'],"),
]

_RP = [
    {"points": [
        "Cut potato cylinders of the same length and diameter. Blot them dry and record the mass "
        "of each.",
        "Put one cylinder in each of a range of sugar or salt solutions, and one in distilled "
        "water, with the same volume of solution each time.",
        "Leave them for the same time, for example 30 minutes, at the same temperature.",
        "Remove each cylinder, blot it dry in the same way, and record its final mass.",
        "Calculate the percentage change in mass for each, and plot it against the concentration.",
    ]},
    {"slot": "fig:osmosis-mass-graph"},
    "percentage change in mass = (final mass − initial mass) ÷ initial mass × 100. Use the "
    "percentage change, because the cylinders start with different masses.",
    "Where the line crosses 0%, there is no net movement of water: that solution has about the "
    "same concentration as the potato cells. Here it is about 0.37 mol/dm³.",
]

LESSON = {
    "slug": "transport-in-cells",
    "start": {
        "setup": "Someone opens a bag of hot chips at the far end of a room with no breeze.",
        "question": "If you had to guess, do the smell particles spread from where there are lots of them to where there are few, or the other way?",
        "options": [
            ("From lots to few",
             "From lots to few. That is diffusion: a net movement from an area of higher "
             "concentration to an area of lower concentration."),
            ("From few to lots",
             "From lots to few. That is diffusion: a net movement from an area of higher "
             "concentration to an area of lower concentration."),
        ],
        "answer": 0,
    },
    "words": ["diffusion", "osmosis", "active transport", "partially permeable"],
    "knowledge": [
        {"kind": "card", "title": "Three ways across a membrane",
         "body": [{"slot": "fig:transport-processes"},
                  "Substances move into and out of cells across the cell membrane by diffusion, "
                  "osmosis and active transport."]},
        {"kind": "card", "title": "Diffusion",
         "body": ["Diffusion is the spreading out of the particles of any substance in solution, or "
                  "particles of a gas, resulting in a net movement from an area of higher "
                  "concentration to an area of lower concentration.",
                  {"points": [
                      "Oxygen and carbon dioxide move by diffusion in gas exchange.",
                      "The waste product urea diffuses from cells into the blood plasma, to be "
                      "removed by the kidneys.",
                  ]}]},
        {"kind": "card", "title": "What makes diffusion faster",
         "body": [{"points": [
             "A bigger difference in concentrations (a steeper concentration gradient).",
             "A higher temperature, because the particles move faster.",
             "A larger surface area of the membrane.",
         ]}]},
        {"kind": "card", "title": "Osmosis",
         "body": ["Osmosis is the diffusion of water from a dilute solution to a concentrated "
                  "solution through a partially permeable membrane.",
                  "A partially permeable membrane lets small molecules, such as water, through but "
                  "not larger ones, such as sugar.",
                  {"points": [
                      "In a more dilute solution than its contents, a cell takes in water by "
                      "osmosis. An animal cell may burst. A plant cell's wall stops it bursting.",
                      "In a more concentrated solution, water leaves the cell by osmosis and it "
                      "shrinks.",
                  ]}]},
        {"kind": "card", "title": "Active transport",
         "body": ["Active transport moves substances from a more dilute solution to a more "
                  "concentrated solution, against a concentration gradient. This requires energy "
                  "from respiration.",
                  {"points": [
                      "Root hairs absorb mineral ions from very dilute solutions in the soil. Plants "
                      "need these ions for healthy growth.",
                      "Sugar molecules are absorbed from lower concentrations in the gut into the "
                      "blood, which has a higher sugar concentration. The sugar is used for "
                      "respiration.",
                  ]}]},
        {"kind": "reveal", "title": "Comparing the three",
         "cols": ["Which way", "Energy from respiration"],
         "rows": [
             ("Diffusion", "From higher to lower concentration", "Not needed"),
             ("Osmosis", "Water only, from a dilute to a concentrated solution", "Not needed"),
             ("Active transport", "From lower to higher concentration, against the gradient",
              "Needed"),
         ]},
        {"kind": "card", "title": "Surface area to volume ratio",
         "body": ["SA:V = surface area ÷ volume, written as n : 1. A single-celled organism has a "
                  "relatively large SA:V, so diffusion across its surface meets its needs.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "reveal", "title": "Bigger cube, smaller SA:V",
         "cols": ["Surface area ÷ volume", "SA:V"],
         "rows": [
             ("1 cm cube", "6 cm² ÷ 1 cm³", "6 : 1"),
             ("2 cm cube", "24 cm² ÷ 8 cm³", "3 : 1"),
             ("3 cm cube", "54 cm² ÷ 27 cm³", "2 : 1"),
         ]},
        {"kind": "card", "title": "Why large organisms need exchange surfaces",
         "body": ["As an organism gets bigger, its SA:V gets smaller and many cells are far from the "
                  "surface. So multicellular organisms need exchange surfaces and a transport "
                  "system.",
                  "An exchange surface works better when it has:",
                  {"points": [
                      "a large surface area",
                      "a thin membrane, for a short diffusion path",
                      "in animals, an efficient blood supply",
                      "in animals, for gas exchange, ventilation",
                  ]}]},
        {"kind": "reveal", "title": "Exchange surfaces",
         "cols": ["How it is adapted"],
         "rows": [
             ("Small intestine", "Villi give a large surface area. Thin walls and a good blood "
                                 "supply."),
             ("Lungs", "Many alveoli give a large surface area. Thin walls, a good blood supply, "
                       "and ventilated by breathing."),
             ("Gills in fish", "Many thin filaments give a large surface area. A good blood supply, "
                               "and water flows over them."),
             ("Roots", "Root hair cells give a large surface area for taking in water and mineral "
                       "ions."),
             ("Leaves", "Flat and thin, with stomata to let gases in and out, and air spaces "
                        "inside."),
         ]},
        {"kind": "card", "title": "Required practical 2: osmosis in potato", "routes": ["CF", "CH"],
         "body": _RP},
        {"kind": "card", "title": "Required practical 3: osmosis in potato", "routes": ["TF", "TH"],
         "body": _RP},
        {"kind": "card", "title": "Calculations",
         "body": ["Rate of water uptake = change in mass ÷ time. Put the time in the unit the "
                  "question asks for first.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("In osmosis, water moves from the concentrated solution to the dilute one.",
              "Water moves from the dilute solution to the more concentrated solution."),
             ("Osmosis is the movement of salt or sugar.",
              "Osmosis is the movement of water only."),
             ("Active transport moves substances down the concentration gradient.",
              "Active transport moves them against the gradient, using energy from respiration."),
             ("Bigger organisms have a bigger SA:V.",
              "SA:V gets smaller as an organism gets bigger."),
         ]}]},
    ],
    "key_fact": "Diffusion is the net movement of particles from a higher to a lower concentration, "
                "and osmosis is the diffusion of water from a dilute solution to a concentrated "
                "solution through a partially permeable membrane. Neither needs energy. Active "
                "transport moves substances against a concentration gradient, using energy from "
                "respiration.",
    "deeper": [
        {"kind": "card", "title": "Turgid and flaccid",
         "body": ["A plant cell full of water presses against its wall and is turgid, which keeps a "
                  "plant firm. A cell that loses water becomes flaccid, and the plant wilts. In a "
                  "very concentrated solution the membrane pulls away from the wall."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Compare</strong> the three processes: the direction, what moves, and whether "
             "energy is needed.",
             "<strong>Explain</strong> an osmosis result: say which solution is more concentrated, "
             "which way water moves, and what happens to the mass.",
             "<strong>Calculate</strong>: keep the minus sign for a loss, and write SA:V as n : 1.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": LOGIC_EDITS},
}
