# -*- coding: utf-8 -*-
"""B8 lesson 05 — Aerobic vs anaerobic: twelve questions (MRB-269).

This is the CONTRAST lesson, and its whole argument is that two different
questions keep getting run together: how much energy comes out of each glucose
molecule, and how fast energy can be supplied. The bank probes the three
clauses of `KS3.B.RESP.04` in turn — the reactants (oxygen, and glucose broken
down completely or only partly), the products (carbon dioxide and water;
lactic acid in humans, ethanol and carbon dioxide in yeast), and the
implications for the organism (yield, location in the cell, and which route is
actually supplying the energy in a given situation).

The distractors are built from the lesson's two declared misconceptions.
RESP-09 ("aerobic respiration is the fast one, because that is the one
athletes train for") supplies every option in which working hard is treated as
the test of which route is running — the marathon runner called anaerobic
because she is working hard, the sprint said to prove anaerobic respiration
yields more, the compost bacteria said to speed up on air, and the "anaerobic
is the slower route" reading of the body-size claim. RESP-10 ("anaerobic
respiration is the emergency backup — something has gone wrong when it
happens") supplies the yeast that ferments only because it is in trouble, and
the obligate anaerobes for whom the arrival of oxygen is the emergency rather
than its absence. Five further errors the lesson exists to correct are worked
as well: that the two routes take turns rather than run together, that a
muscle or a root holds a store of oxygen to run down, that human anaerobic
respiration produces carbon dioxide, that ethanol rather than carbon dioxide
raises a loaf, and that respiration of any kind needs mitochondria.

No question restates a ladder rung. Rungs 1 and 2 already own the two
tell-them-apart MCQs, so the bank works around them: the location, the
products and the yield are approached through consequences a student can be
asked to predict, not through a second "which statement is true of anaerobic
but not aerobic". Rung 3's sprinter-and-marathon explanation and rung 4's
obligate-anaerobe essay are left alone too — the marathon appears here only as
the bench's own route judgement, and the anaerobes only through what happens
to a compost heap when it is turned.

`figure` is `None` throughout: the lesson declares no figures at all
(`figures: []`, measured against the approved page), and every stem here is
self-contained.
"""

UNIT = "B8"
LESSON = "aerobic-vs-anaerobic"
LESSON_NUMBER = 5

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-05-e01",
        "band": "easier",
        "text": "Aerobic respiration happens in the mitochondria. Where does "
                "anaerobic respiration happen?",
        "options": [
            {"text": "In the mitochondria as well, so both routes stop if "
                     "those are damaged",
             "correct": False,
             "why": "Only the aerobic route runs in the mitochondria. The "
                    "anaerobic route runs outside them, which is exactly why "
                    "a cell with very few mitochondria can still use it."},
            {"text": "Outside them, so a cell with few mitochondria can "
                     "still do it", "correct": True},
            {"text": "In the blood, which is where the lactic acid ends up "
                     "afterwards",
             "correct": False,
             "why": "Respiration happens inside cells, not in the blood. The "
                    "blood carries lactic acid away to the liver after it is "
                    "made, but the reaction itself was in the muscle cell."},
            {"text": "In the mitochondria first, then outside them once the "
                     "oxygen runs out",
             "correct": False,
             "why": "There is no handover from one part of the cell to "
                    "another. Anaerobic respiration happens outside the "
                    "mitochondria from the start, whether oxygen is short or "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e02",
        "band": "easier",
        "text": "In aerobic respiration the glucose is broken down "
                "completely. What is it broken down into?",
        "options": [
            {"text": "Lactic acid and water, which the liver then has to deal "
                     "with",
             "correct": False,
             "why": "Lactic acid is what human muscle is left with when there "
                    "is no oxygen. Break the glucose down completely and no "
                    "lactic acid is made at all."},
            {"text": "Ethanol and carbon dioxide, the two products yeast is "
                     "used for",
             "correct": False,
             "why": "Those come from fermentation — yeast respiring without "
                    "oxygen. The ethanol still holds energy, which is the "
                    "sign the glucose was not taken all the way apart."},
            {"text": "Carbon dioxide and water, with no energy-rich product "
                     "left over", "correct": True},
            {"text": "Carbon dioxide and oxygen, which is why you breathe "
                     "both of them out",
             "correct": False,
             "why": "Oxygen goes into aerobic respiration; it does not come "
                    "out of it. What you breathe out is the carbon dioxide "
                    "the glucose was broken down into."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e03",
        "band": "easier",
        "text": "Which of these best describes when aerobic respiration is "
                "running in your body?",
        "options": [
            {"text": "Almost all the time — it is the default route, in every "
                     "cell", "correct": True},
            {"text": "Only during exercise, because that is when your cells "
                     "need energy",
             "correct": False,
             "why": "Your cells need energy every second of your life, "
                    "sitting still included. Aerobic respiration is the route "
                    "running right now, while you read this."},
            {"text": "Only at rest — as soon as you exercise you change over "
                     "to anaerobic",
             "correct": False,
             "why": "Nothing changes over. During exercise aerobic "
                    "respiration works harder than ever, and anaerobic "
                    "respiration only covers what is left uncovered."},
            {"text": "Only when there is oxygen spare after you have finished "
                     "breathing hard",
             "correct": False,
             "why": "Oxygen is not left over and saved up. It is used the "
                    "moment it reaches a cell, so aerobic respiration is "
                    "running continuously, not in gaps."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e04",
        "band": "easier",
        "text": "Anaerobic respiration does not give the same products in a "
                "human muscle cell as it does in yeast. Which pairing is "
                "right?",
        "options": [
            {"text": "Human muscle: lactic acid and carbon dioxide. Yeast: "
                     "ethanol.",
             "correct": False,
             "why": "Human muscle produces lactic acid and no carbon dioxide "
                    "at all — that gas comes from the aerobic route. And "
                    "yeast produces carbon dioxide as well as ethanol."},
            {"text": "Human muscle: ethanol and carbon dioxide. Yeast: lactic "
                     "acid.",
             "correct": False,
             "why": "The right two products, in the wrong two places. Ethanol "
                    "comes from yeast, and lactic acid is what your own "
                    "muscles are left holding."},
            {"text": "Both make lactic acid, and only the amount produced "
                     "differs.",
             "correct": False,
             "why": "Yeast makes no lactic acid. Its anaerobic route gives "
                    "ethanol and carbon dioxide, which is the whole reason we "
                    "can bake and brew with it."},
            {"text": "Human muscle: lactic acid. Yeast: ethanol and carbon "
                     "dioxide.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-05-s01",
        "band": "standard",
        "text": "A marathon runner two hours into a race is holding a steady "
                "pace, and working far harder than you are sitting reading "
                "this. Which route is supplying most of her energy?",
        "options": [
            {"text": "Anaerobic — she is working hard, and hard work needs "
                     "the fast route",
             "correct": False,
             "why": "Hard is not the question — whether the oxygen supply "
                    "keeps up is. She is holding a pace chosen to sit just "
                    "below the point where the anaerobic route would take "
                    "over."},
            {"text": "Anaerobic — after two hours the oxygen in her muscles "
                     "has been used up",
             "correct": False,
             "why": "There is no store of oxygen in a muscle to run down. It "
                    "arrives continuously in the blood, and what matters is "
                    "whether it arrives as fast as it is being used."},
            {"text": "Aerobic — the pace is one her oxygen supply can still "
                     "keep up with", "correct": True},
            {"text": "Aerobic — running for two hours is gentle compared with "
                     "a sprint",
             "correct": False,
             "why": "The route is right and the reason is not. A marathon is "
                    "not gentle; it is paced so that oxygen delivery still "
                    "covers the demand, which is a different claim."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s02",
        "band": "standard",
        "text": "Yeast in a sealed ball of bread dough is rising on a warm "
                "shelf. What is going on inside it?",
        "options": [
            {"text": "It is fermenting: glucose to ethanol and carbon "
                     "dioxide, and that gas raises it", "correct": True},
            {"text": "It is respiring aerobically, because the warm shelf "
                     "means plenty of oxygen gets in",
             "correct": False,
             "why": "Warmth is not oxygen. Almost none reaches the inside of "
                    "a sealed ball of dough, which is precisely why the yeast "
                    "ferments instead."},
            {"text": "It is fermenting, and the ethanol turning into gas is "
                     "what raises the loaf",
             "correct": False,
             "why": "Fermentation is right, but the gas is carbon dioxide. "
                    "The ethanol stays in the dough and mostly bakes off in "
                    "the oven."},
            {"text": "It is in trouble, and ferments only because it cannot "
                     "get the oxygen it needs",
             "correct": False,
             "why": "Fermenting is not an emergency for yeast, it is a "
                    "living. It is doing the only thing available to it and "
                    "doing it deliberately, and we built an industry on the "
                    "result."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s03",
        "band": "standard",
        "text": "A houseplant is left standing in waterlogged soil and its "
                "root cells begin to die. Why?",
        "options": [
            {"text": "So much water enters the root cells that they swell up "
                     "and burst open",
             "correct": False,
             "why": "The trouble is not the water getting in, it is the air "
                    "being pushed out. Water has filled the spaces in the "
                    "soil that oxygen used to reach the roots through."},
            {"text": "The water washes minerals out of the soil, so the roots "
                     "starve of nutrients",
             "correct": False,
             "why": "Minerals are not what is missing here. The flooded soil "
                    "holds no air, so the root cells cannot respire "
                    "aerobically and cannot pay for active transport."},
            {"text": "The roots cannot take in any water, so the plant dries "
                     "out from below",
             "correct": False,
             "why": "The plant is standing in water — there is plenty to take "
                    "in. It looks like a plant with no water because the root "
                    "cells are failing, not because water is short."},
            {"text": "No oxygen reaches them, so they respire anaerobically "
                     "and get far too little energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s04",
        "band": "standard",
        "text": "Sitting in class is labelled almost entirely aerobic. What "
                "does the word almost tell you?",
        "options": [
            {"text": "Anaerobic respiration is switched off, and switches "
                     "back on when you exercise",
             "correct": False,
             "why": "Nothing is switched off. Both routes are running in "
                    "every living example, and the label only says which one "
                    "is supplying most of the energy."},
            {"text": "Both routes are running, and aerobic is supplying "
                     "nearly all of the energy", "correct": True},
            {"text": "The cell picks one route at a time and shuts the other "
                     "one down",
             "correct": False,
             "why": "A cell does not choose between them. Both run at once, "
                    "and what changes from one situation to the next is how "
                    "much of the energy each one supplies."},
            {"text": "A few of your cells are aerobic and all the rest of "
                     "them are anaerobic",
             "correct": False,
             "why": "It is not a split between cells. Inside every cell both "
                    "routes are running, and while you sit still the aerobic "
                    "one is supplying almost all of the energy."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-05-h01",
        "band": "harder",
        "text": "The middle of a compost heap holds no oxygen. A gardener "
                "turns the heap with a fork and lets air right into the "
                "centre. What happens to the bacteria that were living there?",
        "options": [
            {"text": "Nothing much — they switch to the aerobic route now "
                     "that oxygen has arrived",
             "correct": False,
             "why": "Some bacteria could, but not an obligate anaerobe. "
                    "Oxygen is poisonous to it, so air arriving is not an "
                    "upgrade it can take — it is fatal."},
            {"text": "They speed up, because oxygen gets them about twenty "
                     "times more from each glucose",
             "correct": False,
             "why": "That yield is real, but it is only on offer to an "
                    "organism that can use oxygen at all. These ones are "
                    "killed by it, so the twentyfold gain never arrives."},
            {"text": "The obligate anaerobes among them are killed — for "
                     "those, oxygen is the emergency", "correct": True},
            {"text": "They stop respiring and wait until the oxygen in the "
                     "heap has been used up",
             "correct": False,
             "why": "They cannot wait it out. Oxygen is toxic to an obligate "
                    "anaerobe rather than merely unhelpful, and the survivors "
                    "are the ones the air never reached."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h02",
        "band": "harder",
        "text": "A mature red blood cell has no mitochondria at all. Using "
                "the comparison in this lesson, what can you say about how it "
                "respires?",
        "options": [
            {"text": "It can respire anaerobically only, because that route "
                     "runs outside the mitochondria", "correct": True},
            {"text": "It cannot respire at all, because respiration only "
                     "happens in mitochondria",
             "correct": False,
             "why": "Only the aerobic route needs mitochondria. Anaerobic "
                    "respiration runs outside them, which is how a cell with "
                    "none of them keeps itself alive."},
            {"text": "It respires aerobically, using a little of the oxygen "
                     "it is carrying",
             "correct": False,
             "why": "That oxygen is cargo for other cells, and the aerobic "
                    "route needs mitochondria this cell does not have. What "
                    "is left to it is the anaerobic route."},
            {"text": "It respires aerobically, but more slowly than a cell "
                     "with mitochondria",
             "correct": False,
             "why": "Few mitochondria would mean slower. None at all means "
                    "the aerobic route cannot run there — this is a "
                    "difference in kind, not in rate."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h03",
        "band": "harder",
        "text": "A brewer grows the same yeast twice: once with air bubbled "
                "through, once sealed with no oxygen. Both cultures release "
                "the same total amount of energy. Which one used more sugar?",
        "options": [
            {"text": "The one with air, because aerobic respiration is the "
                     "more powerful route",
             "correct": False,
             "why": "Getting more out of each molecule means needing fewer "
                    "molecules, not more. The high yield is exactly what lets "
                    "the aerated culture spend less sugar."},
            {"text": "Both used the same, because a glucose molecule holds "
                     "the energy it holds",
             "correct": False,
             "why": "The molecule holds the same energy either way, but the "
                    "two routes do not get the same amount out of it. The "
                    "sealed culture leaves most of it behind in the ethanol."},
            {"text": "The sealed one used less, because fermentation is the "
                     "faster of the two routes",
             "correct": False,
             "why": "Faster is not cheaper. Fermentation gets far less from "
                    "each glucose molecule, so it has to break down far more "
                    "of them for the same energy."},
            {"text": "The sealed one, because each glucose gives far less "
                     "energy without oxygen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h04",
        "band": "harder",
        "text": "The lesson says the aerobic route is most of the reason "
                "anything larger than a bacterium exists. Which reasoning is "
                "that claim built on?",
        "options": [
            {"text": "Oxygen makes cells grow bigger, so the organisms that "
                     "use it end up larger",
             "correct": False,
             "why": "Oxygen does not inflate a cell. The argument is about an "
                    "energy budget: a large body costs far more to run, and "
                    "only the high-yield route can pay the bill."},
            {"text": "A large body costs far more energy than the anaerobic "
                     "route could supply", "correct": True},
            {"text": "The oxygen wiped out the anaerobic organisms, so only "
                     "the large ones were left",
             "correct": False,
             "why": "The extinction is real, but it did not sort organisms by "
                    "size — plenty of the survivors are anaerobic bacteria "
                    "today. The claim is about what a large body costs."},
            {"text": "Anaerobic respiration is slower, so an anaerobic "
                     "organism could never grow large",
             "correct": False,
             "why": "Anaerobic respiration is the faster of the two, not the "
                    "slower — speed is its whole advantage. What it cannot do "
                    "is get enough energy out of the food available."},
        ],
        "figure": None,
    },
]
