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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-05-e05",
        "band": "easier",
        "text": "Roughly how much more energy does aerobic respiration get "
                "from each glucose molecule than anaerobic respiration does?",
        "options": [
            {"text": "About twice as much.", "correct": False,
             "why": "Far more than that. The gap is about twentyfold, which "
                    "is why the aerobic route is the default in every "
                    "organism that can use it."},
            {"text": "About twenty times as much.", "correct": True},
            {"text": "About the same — the difference is in speed alone.",
             "correct": False,
             "why": "Speed is one difference, but not the only one. The "
                    "anaerobic route leaves a product that still holds most "
                    "of the energy."},
            {"text": "About a hundred times as much.", "correct": False,
             "why": "An overestimate. The figure is about twenty, which is "
                    "already large enough to decide how big an organism can "
                    "be."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e06",
        "band": "easier",
        "text": "Anaerobic respiration in yeast and other micro-organisms has "
                "a name of its own. What is it?",
        "options": [
            {"text": "Digestion", "correct": False,
             "why": "Digestion breaks large food molecules into small ones so "
                    "they can be absorbed. What happens to the small ones "
                    "inside the cell is respiration."},
            {"text": "Photosynthesis", "correct": False,
             "why": "Photosynthesis builds glucose using light. This process "
                    "breaks glucose down, and it needs no light at all."},
            {"text": "Excretion", "correct": False,
             "why": "Excretion is getting rid of waste an organism has made. "
                    "This is the reaction that made it."},
            {"text": "Fermentation", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e07",
        "band": "easier",
        "text": "Which of these is supplied almost entirely by aerobic "
                "respiration?",
        "options": [
            {"text": "A student sitting still and reading a page.",
             "correct": True},
            {"text": "The last three seconds of a 100 m race.",
             "correct": False,
             "why": "Aerobic respiration is flat out there, but it is nowhere "
                    "near enough. A large part of the energy is coming "
                    "anaerobically."},
            {"text": "Yeast in a sealed ball of bread dough.",
             "correct": False,
             "why": "Almost no oxygen reaches the middle of a dough ball, so "
                    "the yeast is fermenting — glucose to ethanol and carbon "
                    "dioxide."},
            {"text": "The root cells of a plant in waterlogged soil.",
             "correct": False,
             "why": "Water has filled the air spaces in the soil, so no "
                    "oxygen reaches those cells and they respire "
                    "anaerobically."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e08",
        "band": "easier",
        "text": "Which of these is supplied almost entirely by anaerobic "
                "respiration?",
        "options": [
            {"text": "A student sitting still, reading a page.",
             "correct": False,
             "why": "Demand is low and the oxygen supply covers it several "
                    "times over, so this is the aerobic route almost "
                    "entirely."},
            {"text": "A marathon runner two hours into a race.",
             "correct": False,
             "why": "She is working hard, but at a pace her oxygen supply "
                    "still keeps up with. Hard work is not the test — whether "
                    "oxygen keeps up is."},
            {"text": "Yeast in a sealed ball of bread dough.", "correct": True},
            {"text": "A resting muscle with blood flowing normally through "
                     "it.",
             "correct": False,
             "why": "Being a muscle is not what makes respiration anaerobic — "
                    "running short of oxygen is. A resting muscle has the "
                    "easiest case of all: low demand, and blood delivering "
                    "oxygen faster than the cells can use it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e09",
        "band": "easier",
        "text": "Which of these can respire anaerobically?",
        "options": [
            {"text": "Only micro-organisms, such as yeast and bacteria.",
             "correct": False,
             "why": "Your own muscles do it, and so do plant roots in flooded "
                    "soil. It is not a micro-organism speciality."},
            {"text": "Humans, plants and micro-organisms can all do it.",
             "correct": True},
            {"text": "Only animals, since plants have photosynthesis "
                     "instead.",
             "correct": False,
             "why": "Photosynthesis is not a substitute for respiration. A "
                    "root cell in waterlogged soil respires anaerobically "
                    "exactly as a sprinting muscle does."},
            {"text": "Only organisms that have no mitochondria at all.",
             "correct": False,
             "why": "A muscle cell is full of mitochondria and still uses the "
                    "anaerobic route when oxygen runs short, because that "
                    "route runs outside them."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-e10",
        "band": "easier",
        "text": "Anaerobic respiration needs no oxygen. Which substance does "
                "it still need, exactly as aerobic respiration does?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "Water is a product of the aerobic route, not something "
                    "either route has to be supplied with. What both must "
                    "have is a fuel."},
            {"text": "Carbon dioxide", "correct": False,
             "why": "Carbon dioxide comes out of aerobic respiration, and "
                    "nothing respires it. Both routes need a fuel to break "
                    "down."},
            {"text": "Lactic acid", "correct": False,
             "why": "Lactic acid is what the human anaerobic route leaves "
                    "behind. It is a product, not a starting material."},
            {"text": "Glucose", "correct": True},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-05-s05",
        "band": "standard",
        "text": "Bacteria in the middle of a compost heap and yeast in a "
                "sealed ball of dough are both respiring anaerobically. What "
                "do the two situations have in common?",
        "options": [
            {"text": "Both organisms are short of food, so they take the "
                     "cheaper route.",
             "correct": False,
             "why": "Neither is short of food — the dough is full of sugar "
                    "and so is the compost. What is missing in both cases is "
                    "oxygen."},
            {"text": "Both are too cold for aerobic respiration to run at "
                     "all.",
             "correct": False,
             "why": "Temperature does not decide which route runs. The middle "
                    "of a compost heap is warm, and dough is proved somewhere "
                    "warm on purpose."},
            {"text": "No oxygen reaches either of them, so the anaerobic "
                     "route supplies the energy.",
             "correct": True},
            {"text": "Neither organism has mitochondria, so the aerobic route "
                     "is closed to them.",
             "correct": False,
             "why": "Yeast is a fungus and has mitochondria. What stops it "
                    "using them here is the absence of oxygen, not the "
                    "absence of machinery."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s06",
        "band": "standard",
        "text": "Which of these shows most clearly that anaerobic respiration "
                "is not simply an emergency measure?",
        "options": [
            {"text": "Yeast ferments in dough for a living, and an industry "
                     "is built on the result.",
             "correct": True},
            {"text": "A sprinter uses it in the last seconds of a race and "
                     "recovers afterwards.",
             "correct": False,
             "why": "That is the case that makes it look like an emergency — "
                    "a shortfall covered and then repaid. The convincing case "
                    "is an organism in no trouble at all."},
            {"text": "Root cells use it when their soil floods, and often die "
                     "soon after.",
             "correct": False,
             "why": "That genuinely is an emergency, and the cells lose it. "
                    "It is evidence for the other side of the argument."},
            {"text": "Muscles use it when heart and lungs cannot keep up with "
                     "demand.",
             "correct": False,
             "why": "Again a shortfall being covered. What settles the "
                    "question is an organism that lives this way by "
                    "preference."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s07",
        "band": "standard",
        "text": "Two identical yeast cultures are given the same amount of "
                "sugar. One is sealed; the other has air bubbled through it. "
                "Which produces more new yeast cells?",
        "options": [
            {"text": "The sealed one, because fermentation is the faster of "
                     "the two routes.",
             "correct": False,
             "why": "A faster supply is not a bigger total. The sealed "
                    "culture gets far less from each sugar molecule, so it "
                    "can build far less."},
            {"text": "The sealed one, because the ethanol it makes is used "
                     "as material for the new cells.",
             "correct": False,
             "why": "Ethanol is a waste product leaving the cell, not "
                    "building material. It still holds energy, which is "
                    "exactly why the sealed route is the wasteful one."},
            {"text": "Both the same, since they were given the same amount of "
                     "sugar.",
             "correct": False,
             "why": "The same sugar is not the same energy. Aerobic "
                    "respiration gets about twenty times more out of each "
                    "molecule."},
            {"text": "The aerated one — aerobic respiration gets far more "
                     "per molecule.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s08",
        "band": "standard",
        "text": "A student says that because you breathe harder during "
                "exercise, exercise must be anaerobic. Where is the error?",
        "options": [
            {"text": "Breathing harder shows the anaerobic route has taken "
                     "over from the aerobic one.",
             "correct": False,
             "why": "Nothing takes over. Aerobic respiration is working "
                    "harder than ever, and that is exactly what the harder "
                    "breathing is for."},
            {"text": "Breathing harder is the aerobic route being supplied "
                     "faster, not replaced.",
             "correct": True},
            {"text": "Breathing harder is how the body gets rid of lactic "
                     "acid, through the lungs.",
             "correct": False,
             "why": "Lactic acid is not a gas and does not leave in your "
                    "breath. The blood carries it to the liver, and the extra "
                    "oxygen is what the liver needs."},
            {"text": "Breathing has nothing to do with respiration, so it "
                     "shows nothing either way.",
             "correct": False,
             "why": "Too strong. Breathing supplies the oxygen the aerobic "
                    "route uses, so harder breathing is evidence about that "
                    "route — just not the evidence the student thought."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s09",
        "band": "standard",
        "text": "The anaerobic route gets far less energy out of each glucose "
                "molecule. Why is it worth having at all?",
        "options": [
            {"text": "Because it can run for hours once the aerobic route is "
                     "exhausted.",
             "correct": False,
             "why": "The aerobic route does not get exhausted; it runs "
                    "continuously. The anaerobic one is the short-term "
                    "option, not the long one."},
            {"text": "Because it leaves a product the body can store up for "
                     "later use.",
             "correct": False,
             "why": "Lactic acid is a debt to be dealt with, not a store to "
                    "draw on. What this route buys is time, not storage."},
            {"text": "Because it supplies energy faster than oxygen can be "
                     "delivered, for short bursts.",
             "correct": True},
            {"text": "Because it uses less glucose, so the body's fuel lasts "
                     "longer.",
             "correct": False,
             "why": "The opposite is true. Getting less from each molecule "
                    "means breaking down far more of them for the same "
                    "work."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-s10",
        "band": "standard",
        "text": "A student says fermentation and anaerobic respiration are "
                "two completely different processes. What is the best reply?",
        "options": [
            {"text": "Fermentation is anaerobic respiration, carried out by a "
                     "micro-organism.",
             "correct": True},
            {"text": "They differ because fermentation needs no glucose and "
                     "respiration does.",
             "correct": False,
             "why": "Both start from glucose. What differs between one "
                    "organism and another is what is left at the end of it."},
            {"text": "They differ because fermentation happens outside a cell "
                     "and respiration inside.",
             "correct": False,
             "why": "Fermentation happens inside the yeast or bacterial "
                    "cells, exactly as respiration happens inside yours."},
            {"text": "They differ because fermentation releases no energy, so "
                     "it is not respiration.",
             "correct": False,
             "why": "It releases energy — that is why the organism does it. "
                    "There is simply far less of it than the aerobic route "
                    "would give."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-05-h05",
        "band": "harder",
        "text": "Respiring 5 g of glucose aerobically transfers about 78 kJ. "
                "The anaerobic route gets about a twentieth as much per gram. "
                "What mass of glucose would it need for the same 78 kJ?",
        "options": [
            {"text": "0.25 g", "correct": False,
             "why": "That is 5 ÷ 20, dividing where you should multiply. "
                    "Getting less out of each gram means needing more grams, "
                    "not fewer."},
            {"text": "5 g", "correct": False,
             "why": "That would be right only if the two routes gave the same "
                    "energy per gram. The anaerobic route gives about a "
                    "twentieth, so it needs about twenty times the glucose."},
            {"text": "100 g", "correct": True},
            {"text": "25 g", "correct": False,
             "why": "That is 5 × 5. The factor in the question is twenty, so "
                    "the mass needed is 5 × 20 = 100 g."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h06",
        "band": "harder",
        "text": "The middle of a compost heap and a sealed ball of dough both "
                "hold no oxygen. Air is let into each of them. What happens "
                "to the organisms living there?",
        "options": [
            {"text": "Both die, because both are adapted to living without "
                     "oxygen.",
             "correct": False,
             "why": "Only some compost bacteria are killed by oxygen. Yeast "
                    "is not one of them — it thrives on air, which is how "
                    "baker's yeast is manufactured."},
            {"text": "The yeast switches to the aerobic route and grows fast; "
                     "obligate anaerobes are killed.",
             "correct": True},
            {"text": "Both switch to the aerobic route and give us more of "
                     "what we wanted from them.",
             "correct": False,
             "why": "The yeast does switch, but the loaf then gets less of "
                    "what a baker wants, not more. And an obligate anaerobe "
                    "cannot switch at all, because oxygen kills it."},
            {"text": "Neither changes, since each carries on with the route "
                     "it was already using.",
             "correct": False,
             "why": "Oxygen changes everything for both, in opposite "
                    "directions. The yeast takes the better route; the "
                    "obligate anaerobes do not survive to take any."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h07",
        "band": "harder",
        "text": "A sprinter's muscle and a yeast in dough both start with "
                "glucose and both run short of oxygen, yet they do not end up "
                "with the same product. What decides which product forms?",
        "options": [
            {"text": "How long the shortage of oxygen lasts in each case.",
             "correct": False,
             "why": "Time changes how much is made, not what it is. Ten "
                    "seconds and ten hours both leave a human muscle cell "
                    "with lactic acid."},
            {"text": "How completely the glucose is broken down inside each "
                     "of the two cells.",
             "correct": False,
             "why": "In both the breakdown is incomplete — that is what they "
                    "share. What differs is where each of them stops."},
            {"text": "The temperature each of them is at when the oxygen runs "
                     "out.",
             "correct": False,
             "why": "Temperature changes the rate, never the products. A cold "
                    "dough gives the same two products as a warm one."},
            {"text": "Which organism it is: human muscle gives lactic acid, "
                     "yeast gives ethanol and carbon dioxide.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h08",
        "band": "harder",
        "text": "Ethanol from yeast and lactic acid from your muscles are "
                "both said to still hold energy. What is the evidence for "
                "that, in each case?",
        "options": [
            {"text": "Ethanol burns as a fuel, and the liver recovers energy "
                     "from lactic acid.",
             "correct": True},
            {"text": "Both taste strong or sour, which is the energy left in "
                     "them being detected.",
             "correct": False,
             "why": "Taste is no evidence of energy content. The evidence is "
                    "that both substances can still be used as a source of "
                    "energy afterwards."},
            {"text": "Both are gases, and a gas carries energy away from the "
                     "cell that made it.",
             "correct": False,
             "why": "Neither is a gas. Ethanol is a liquid in the dough, and "
                    "lactic acid stays dissolved in the muscle."},
            {"text": "Both are broken down further by the organism that made "
                     "them, on the spot.",
             "correct": False,
             "why": "Yeast does not break its ethanol down at all — it is got "
                    "rid of. Lactic acid leaves the muscle and is dealt with "
                    "by the liver."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h09",
        "band": "harder",
        "text": "In a 90-minute football match a player sprints repeatedly, "
                "and blood lactate rises during the sprints and falls between "
                "them. Which route supplies most of the energy overall?",
        "options": [
            {"text": "Anaerobic, because the sprints are what a match is "
                     "really made of.",
             "correct": False,
             "why": "The sprints are short and the running between them is "
                    "long. For most of the ninety minutes the demand is "
                    "inside what oxygen delivery covers."},
            {"text": "Anaerobic, because lactate can be measured and so must "
                     "be the main route.",
             "correct": False,
             "why": "Measurable is not the same as dominant. Lactate rises "
                    "because a gap opened for a few seconds, not because the "
                    "anaerobic route did most of the work."},
            {"text": "Aerobic, because most of the match is inside what "
                     "oxygen delivery covers.",
             "correct": True},
            {"text": "Aerobic, because the anaerobic route only starts once "
                     "the player is exhausted.",
             "correct": False,
             "why": "It starts whenever demand rises above delivery, which is "
                    "as true of the first sprint as the last. The route is "
                    "right and the reason is not."},
        ],
        "figure": None,
    },
    {
        "id": "b8-05-h10",
        "band": "harder",
        "text": "A patient who has not exercised at all is found to have a "
                "raised level of lactic acid in their blood. Using the two "
                "routes, what does that suggest?",
        "options": [
            {"text": "That they have been respiring too fast, and should "
                     "breathe more slowly.",
             "correct": False,
             "why": "A fast rate on its own makes no lactic acid. It is made "
                    "only when demand climbs above what oxygen delivery can "
                    "cover."},
            {"text": "That oxygen is not reaching some of their cells fast "
                     "enough.",
             "correct": True},
            {"text": "That their muscles have used up the lactic acid they "
                     "had stored.",
             "correct": False,
             "why": "Lactic acid is not stored anywhere. It is made when a "
                    "shortfall opens, so a raised level means it is being "
                    "produced now."},
            {"text": "That they have eaten too much sugar for their cells to "
                     "respire aerobically.",
             "correct": False,
             "why": "Extra glucose does not force the anaerobic route. Only a "
                    "shortage of oxygen, relative to demand, does that."},
        ],
        "figure": None,
    },
]

_MRB338_NEW_QUESTIONS = [
    {
        "id": 'b8-05-e11',
        "band": 'easier',
        "text": 'Which substance is the starting fuel for both aerobic and anaerobic respiration?',
        "options": [
            {"text": 'Glucose.', "correct": True},
            {"text": 'Oxygen.', "correct": False,
             "why": 'Oxygen is needed only for the aerobic route; the fuel both routes start from is glucose.'},
            {"text": 'Carbon dioxide.', "correct": False,
             "why": 'Carbon dioxide is a product of the aerobic route, not the starting fuel of either route.'},
            {"text": 'Lactic acid.', "correct": False,
             "why": 'Lactic acid is a product of the anaerobic route in humans, not the starting fuel.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e12',
        "band": 'easier',
        "text": 'What are the products of aerobic respiration?',
        "options": [
            {"text": 'Lactic acid.', "correct": False,
             "why": 'That is the anaerobic product in human muscle, not the aerobic one.'},
            {"text": 'Carbon dioxide and water.', "correct": True},
            {"text": 'Ethanol and carbon dioxide.', "correct": False,
             "why": "Those are yeast's anaerobic products, not the aerobic ones."},
            {"text": 'Glucose and oxygen.', "correct": False,
             "why": 'Those are the reactants that go in, not the products that come out.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e13',
        "band": 'easier',
        "text": 'Which of these is true of aerobic respiration but not anaerobic respiration?',
        "options": [
            {"text": 'It uses glucose.', "correct": False,
             "why": 'Both routes use glucose as their starting fuel.'},
            {"text": 'It releases energy.', "correct": False,
             "why": 'Both routes release energy from glucose; that is not what tells them apart.'},
            {"text": 'It uses oxygen.', "correct": True},
            {"text": 'It happens inside a living cell.', "correct": False,
             "why": 'Both routes happen inside living cells.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e14',
        "band": 'easier',
        "text": 'Which statement best describes when anaerobic respiration happens in a person?',
        "options": [
            {"text": 'When energy is needed faster than oxygen can be delivered, or when no oxygen is available at all.', "correct": True},
            {"text": 'Only during sleep, when the body needs to save energy.', "correct": False,
             "why": 'Anaerobic respiration is not linked to sleep; it happens when demand outruns oxygen supply.'},
            {"text": 'Only in cells that have just been made.', "correct": False,
             "why": 'Anaerobic respiration is not about how new a cell is; it depends on oxygen supply against demand.'},
            {"text": 'Every single time a muscle contracts at all.', "correct": False,
             "why": 'Gentle, everyday movement stays well within the oxygen supply and is aerobic.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e15',
        "band": 'easier',
        "text": 'In which part of the cell does aerobic respiration take place?',
        "options": [
            {"text": 'The nucleus.', "correct": False,
             "why": "The nucleus holds the cell's genetic information; aerobic respiration happens in the mitochondria."},
            {"text": 'The mitochondria.', "correct": True},
            {"text": 'The cell membrane.', "correct": False,
             "why": 'The cell membrane controls what enters and leaves the cell, not where aerobic respiration happens.'},
            {"text": 'The cytoplasm generally, with no particular part involved.', "correct": False,
             "why": 'Aerobic respiration happens in a specific part of the cell, the mitochondria.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e16',
        "band": 'easier',
        "text": 'A marathon runner keeps a steady pace for two hours without becoming out of breath. Which route is mostly supplying their energy?',
        "options": [
            {"text": 'The anaerobic route.', "correct": False,
             "why": 'Running for two hours without becoming badly out of breath is exactly what staying aerobic looks like.'},
            {"text": 'Neither route — the muscles use stored energy instead.', "correct": False,
             "why": 'Muscles do not hold a store of ready energy like this; they respire continuously to release it.'},
            {"text": 'The aerobic route.', "correct": True},
            {"text": 'Both routes equally, the whole time.', "correct": False,
             "why": 'A well-paced marathon stays mostly aerobic; it is not an even split between the two.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e17',
        "band": 'easier',
        "text": 'Yeast sealed in a flask of sugar solution with no air is bubbling steadily. It is respiring which way?',
        "options": [
            {"text": 'Aerobically.', "correct": False,
             "why": 'There is no oxygen in the sealed flask, so the yeast ferments anaerobically.'},
            {"text": 'Neither — yeast is not a living organism.', "correct": False,
             "why": 'Yeast is a living, single-celled fungus, and it respires like any other living cell.'},
            {"text": 'Both equally, at all times.', "correct": False,
             "why": 'Sealed away from air, the yeast is respiring almost entirely anaerobically.'},
            {"text": 'Anaerobically.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e18',
        "band": 'easier',
        "text": 'The root cells of a houseplant standing in waterlogged soil are most likely respiring which way?',
        "options": [
            {"text": 'Anaerobically.', "correct": True},
            {"text": 'Aerobically.', "correct": False,
             "why": 'Waterlogged soil has no air spaces left, so little or no oxygen reaches the roots.'},
            {"text": 'Neither — roots do not respire at all.', "correct": False,
             "why": 'Root cells are living cells and respire continuously, just like any other living cell.'},
            {"text": 'Both equally, exactly as they would in normal, well-drained soil.', "correct": False,
             "why": 'Waterlogging removes the oxygen the roots need for the aerobic route, so the balance shifts strongly towards anaerobic.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e19',
        "band": 'easier',
        "text": 'A student sitting still, reading a page, is respiring almost entirely which way?',
        "options": [
            {"text": 'Anaerobically.', "correct": False,
             "why": 'Sitting still is very low demand, well within what the oxygen supply can cover, so it stays aerobic.'},
            {"text": 'Aerobically.', "correct": True},
            {"text": 'Neither — the body does not respire at rest.', "correct": False,
             "why": 'Every living cell respires continuously, including at rest.'},
            {"text": 'Both equally, exactly as during a hard sprint.', "correct": False,
             "why": 'A sprint pushes demand far above the oxygen supply; sitting still does not, so the two are not equal.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e20',
        "band": 'easier',
        "text": 'Which of these organisms can respire anaerobically?',
        "options": [
            {"text": 'Only micro-organisms such as yeast and bacteria.', "correct": False,
             "why": 'Human muscle and plant root cells can both respire anaerobically too, not only micro-organisms.'},
            {"text": 'Only animals, since plants photosynthesise instead.', "correct": False,
             "why": 'Photosynthesis is a separate process; plant cells can still respire anaerobically when short of oxygen.'},
            {"text": 'Humans, plants and micro-organisms can all do it.', "correct": True},
            {"text": 'Only organisms that have no mitochondria at all.', "correct": False,
             "why": 'Organisms with mitochondria, humans included, can still respire anaerobically when needed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e21',
        "band": 'easier',
        "text": 'An obligate anaerobe is an organism for which oxygen is what?',
        "options": [
            {"text": 'Poisonous.', "correct": True},
            {"text": 'Essential for survival.', "correct": False,
             "why": 'For an obligate anaerobe oxygen is harmful, not essential; it can live only where none is present.'},
            {"text": 'Completely irrelevant to it.', "correct": False,
             "why": 'Oxygen is not irrelevant to an obligate anaerobe; being poisoned by it is exactly why it avoids oxygen-rich places.'},
            {"text": 'A store of extra energy.', "correct": False,
             "why": 'Oxygen is not a store of energy for any organism; it is used up in the aerobic reaction, or avoided by an obligate anaerobe.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e22',
        "band": 'easier',
        "text": 'In which sort of place would you expect to find an obligate anaerobe living?',
        "options": [
            {"text": 'On a leaf surface, exposed to full sunlight and air.', "correct": False,
             "why": 'That is a well-aerated place; an obligate anaerobe needs somewhere with little or no oxygen.'},
            {"text": 'Deep in a compost heap, away from the air.', "correct": True},
            {"text": 'Floating on the surface of a pond.', "correct": False,
             "why": 'The surface of open water is well oxygenated; an obligate anaerobe needs an oxygen-free place.'},
            {"text": 'Inside a bubble of air trapped underwater.', "correct": False,
             "why": 'A bubble of air is full of oxygen, which is exactly what an obligate anaerobe cannot tolerate.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e23',
        "band": 'easier',
        "text": 'Which statement about anaerobic respiration is correct?',
        "options": [
            {"text": 'It only ever happens when something has gone wrong in the body.', "correct": False,
             "why": 'Yeast fermenting in a vat and bacteria in a compost heap are not in any trouble; anaerobic respiration is a normal process for them.'},
            {"text": 'It happens only in humans, never in any other organism.', "correct": False,
             "why": 'Anaerobic respiration happens in yeast, bacteria and plants as well as in humans.'},
            {"text": 'It is a normal, everyday process, not only something that happens in an emergency.', "correct": True},
            {"text": 'It always uses up far more glucose overall than the aerobic route ever would for exactly the same job.', "correct": False,
             "why": 'Anaerobic respiration typically uses glucose faster for a given burst of energy, not more glucose overall for the same total energy released.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e24',
        "band": 'easier',
        "text": 'For roughly how long has life on Earth existed without much oxygen in the atmosphere, before photosynthetic organisms began releasing it?',
        "options": [
            {"text": 'Around the first two hundred years.', "correct": False,
             "why": 'Two hundred years is far too short; the oxygen-free period lasted roughly two billion years.'},
            {"text": 'Around the first two weeks.', "correct": False,
             "why": 'Two weeks is far too short a time for the early history of life on Earth.'},
            {"text": 'There has never been a time with little oxygen in the atmosphere.', "correct": False,
             "why": 'For roughly the first two billion years of life, there was very little oxygen in the atmosphere at all.'},
            {"text": 'Around the first two billion years.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e25',
        "band": 'easier',
        "text": 'Which row of a comparison table correctly matches ‘what it is for’ to each route?',
        "options": [
            {"text": 'Aerobic: only during exercise. Anaerobic: everything else, all the time.', "correct": False,
             "why": 'Aerobic respiration is the default running all the time, not only during exercise.'},
            {"text": 'Aerobic: everything, all the time, the default. Anaerobic: when energy is needed faster than oxygen arrives, or none is available.', "correct": True},
            {"text": 'Aerobic: only in plants. Anaerobic: only in animals.', "correct": False,
             "why": 'Both routes can occur in plants, animals and micro-organisms; the difference is not about which kingdom an organism belongs to.'},
            {"text": 'Aerobic and anaerobic are genuinely used for exactly the same jobs in every organism, with no real difference at all.', "correct": False,
             "why": 'The two routes are used differently — aerobic as the constant default, anaerobic as the extra route for a shortfall or no oxygen at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e26',
        "band": 'easier',
        "text": 'A cell with very few mitochondria relies mostly on which route?',
        "options": [
            {"text": 'The aerobic route.', "correct": False,
             "why": 'Aerobic respiration happens in the mitochondria; a cell with very few of them cannot rely mainly on that route.'},
            {"text": 'Neither route — it does not respire at all.', "correct": False,
             "why": 'Even a cell with very few mitochondria still respires to get some energy; it simply relies more on the anaerobic route.'},
            {"text": 'The anaerobic route.', "correct": True},
            {"text": 'Both routes equally, all the time.', "correct": False,
             "why": 'With very few mitochondria, the aerobic route is barely available, so the balance tips heavily towards anaerobic.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e27',
        "band": 'easier',
        "text": 'Fermentation, as carried out by yeast and some bacteria, is another name for what?',
        "options": [
            {"text": 'Aerobic respiration in a micro-organism.', "correct": False,
             "why": 'Fermentation specifically describes the anaerobic route in a micro-organism, not the aerobic one.'},
            {"text": 'A micro-organism photosynthesising.', "correct": False,
             "why": 'Fermentation is a form of respiration, not photosynthesis.'},
            {"text": 'Food simply going off on its own.', "correct": False,
             "why": 'Fermentation is a controlled reaction carried out by a chosen living organism, not random spoilage.'},
            {"text": 'Anaerobic respiration in a micro-organism.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e28',
        "band": 'easier',
        "text": 'Which statement correctly links the amount of energy released to the size of a living thing?',
        "options": [
            {"text": 'Getting far more energy from aerobic respiration is a big part of why anything larger than a bacterium can exist.', "correct": True},
            {"text": 'The size of an organism has absolutely nothing at all to do with how it respires, whichever route it relies on most.', "correct": False,
             "why": 'The far greater energy yield of the aerobic route is closely linked to how large and active an organism can afford to be.'},
            {"text": 'Only anaerobic respiration can support a large body.', "correct": False,
             "why": 'Anaerobic respiration releases far less energy per glucose molecule, which is why it cannot support a large, active body on its own.'},
            {"text": 'Every living thing, however large, respires only anaerobically.', "correct": False,
             "why": 'Most large organisms rely mainly on aerobic respiration, which releases far more energy per glucose molecule.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-e29',
        "band": 'easier',
        "text": 'Which single word best completes this sentence: aerobic respiration happens in the mitochondria; anaerobic respiration happens ___ them?',
        "options": [
            {"text": 'Only inside.', "correct": False,
             "why": 'Anaerobic respiration happens outside the mitochondria, not only inside them.'},
            {"text": 'Outside.', "correct": True},
            {"text": 'Nowhere near.', "correct": False,
             "why": 'Anaerobic respiration still happens within the cell, in the cytoplasm, just not inside the mitochondria.'},
            {"text": 'Exclusively above.', "correct": False,
             "why": 'Location inside a cell is not about being physically ‘above’ anything; anaerobic respiration happens outside the mitochondria.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s11',
        "band": 'standard',
        "text": 'A student is given two flasks of the same yeast culture: one is stirred and open to air, the other sealed. Both start with the same amount of glucose. Explain why testing the gas released will not tell you which flask fermented more of its glucose.',
        "options": [
            {"text": 'Aerobic respiration in the open flask also releases carbon dioxide, so gas alone cannot separate the two routes.', "correct": True},
            {"text": 'Only the sealed flask releases gas, so the open one tells you nothing.', "correct": False,
             "why": 'The open, aerated flask is respiring aerobically, which also releases carbon dioxide, just as fermentation does.'},
            {"text": 'Gas volume always increases at exactly the same rate regardless of which route is running.', "correct": False,
             "why": 'The rate of gas release does typically differ between the two routes; that is not the reason gas alone cannot separate them here.'},
            {"text": 'Fermentation releases no gas at all in yeast, only ethanol.', "correct": False,
             "why": 'Yeast fermentation releases both ethanol and carbon dioxide gas; the gas readings from both flasks look similar for a different reason.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s12',
        "band": 'standard',
        "text": 'A student asks whether anaerobic respiration in a human muscle produces the same products as the aerobic route, only in smaller amounts. Explain the flaw.',
        "options": [
            {"text": 'It is broadly right; anaerobic respiration just makes much smaller amounts of the same two products.', "correct": False,
             "why": 'Human anaerobic respiration does not make carbon dioxide or water in any amount; its only product is lactic acid.'},
            {"text": 'Human anaerobic respiration makes lactic acid only; it produces no carbon dioxide and no water at all.', "correct": True},
            {"text": 'It is right for carbon dioxide, but anaerobic respiration makes no water.', "correct": False,
             "why": 'Human anaerobic respiration makes neither carbon dioxide nor water; both statements need correcting, not just one.'},
            {"text": 'It is right for water, but anaerobic respiration makes no carbon dioxide.', "correct": False,
             "why": 'Human anaerobic respiration makes neither carbon dioxide nor water; both statements need correcting, not just one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s13',
        "band": 'standard',
        "text": 'A cyclist rides at a pace that stays entirely aerobic for the first hour, then speeds up until they can no longer hold a conversation. Explain what has changed about which route is supplying their energy.',
        "options": [
            {"text": 'The aerobic route has switched off completely and the anaerobic route has taken over on its own.', "correct": False,
             "why": 'The aerobic route keeps running at its highest rate; the anaerobic route adds to it rather than replacing it.'},
            {"text": 'Nothing about their respiration has changed; only their breathing pattern is different.', "correct": False,
             "why": 'A change severe enough to stop them talking reflects a real shift in how much of their energy now comes anaerobically.'},
            {"text": 'Demand has risen above what their oxygen supply can cover.', "correct": True},
            {"text": 'Their muscles have simply run out of oxygen completely and stopped respiring.', "correct": False,
             "why": 'The muscles have not stopped respiring; they are still respiring aerobically at full rate, with anaerobic respiration adding to it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s14',
        "band": 'standard',
        "text": 'A biology class is told that ‘aerobic respiration gets about twenty times more energy from glucose than anaerobic respiration’. A student asks whether this means an anaerobic reaction wastes most of the glucose. Explain why this is not quite right.',
        "options": [
            {"text": 'Yes, that is exactly right — most of the glucose is destroyed without releasing any energy at all.', "correct": False,
             "why": 'Glucose is never destroyed without releasing energy; the anaerobic route just leaves much of the stored energy still trapped in its product.'},
            {"text": 'Yes, and the wasted energy simply disappears as heat, unlike in the aerobic route.', "correct": False,
             "why": 'The energy is not wasted or destroyed; it remains stored in the product molecule rather than being released.'},
            {"text": 'No, because anaerobic respiration actually gets more energy out than aerobic respiration does.', "correct": False,
             "why": 'It is aerobic respiration that gets far more energy out of each glucose molecule, not the anaerobic route.'},
            {"text": 'No glucose is wasted; the energy stays stored in the lactic acid or ethanol produced.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s15',
        "band": 'standard',
        "text": 'A sports scientist says an untrained jogger and a trained runner can run at the same speed, yet one stays aerobic and the other does not. Explain how this is possible for the same running speed.',
        "options": [
            {"text": "The trained runner's higher ceiling covers that speed's demand; the jogger's lower one does not.", "correct": True},
            {"text": 'It is not really possible; the same running speed must demand exactly the same energy from anyone.', "correct": False,
             "why": 'The same speed does demand similar energy from both runners; what differs is how much oxygen each of them can deliver to cover it.'},
            {"text": "The trained runner's muscles need less energy to run at that speed than the untrained jogger's do.", "correct": False,
             "why": 'Energy demand for a given speed is similar for both; the real difference is in how much oxygen each can deliver.'},
            {"text": "The untrained jogger's muscles contain no mitochondria at all, unlike the trained runner's.", "correct": False,
             "why": "Both runners' muscles contain mitochondria; the difference is in overall oxygen delivery, not in whether mitochondria are present."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s16',
        "band": 'standard',
        "text": 'A gardener finds that a plant recovers completely after being waterlogged for two days, but a similar plant left waterlogged for two weeks dies. Explain the difference using respiration.',
        "options": [
            {"text": 'The two-day plant switched entirely to aerobic respiration, which saved it.', "correct": False,
             "why": 'Waterlogged soil has no air spaces for oxygen at either point; both plants are respiring mostly anaerobically while flooded.'},
            {"text": 'Two days of low energy from anaerobic respiration is survivable.', "correct": True},
            {"text": 'Two weeks of flooding stops the plant respiring at all, which is why it dies.', "correct": False,
             "why": "The plant's cells keep respiring, just anaerobically and with far less energy; it is the prolonged shortage of energy that eventually kills them."},
            {"text": 'There is no real difference; both plants should recover or die at the same rate.', "correct": False,
             "why": 'A longer period without enough energy for active transport does far more lasting damage than a short one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s17',
        "band": 'standard',
        "text": 'A student says obligate anaerobes ‘prove that oxygen is bad for life’. Evaluate this claim.',
        "options": [
            {"text": 'Oxygen genuinely harms every kind of living cell to some degree.', "correct": False,
             "why": 'Oxygen is essential, not harmful, to the aerobic organisms that make up most of life, including humans.'},
            {"text": 'Aerobic respiration is really just a slower, safer version of anaerobic respiration.', "correct": False,
             "why": 'Aerobic respiration is not a safer version of anaerobic respiration; it releases far more energy and depends on oxygen rather than avoiding it.'},
            {"text": 'It overstates it — oxygen is toxic only to organisms adapted to living without it.', "correct": True},
            {"text": 'Obligate anaerobes do not actually exist.', "correct": False,
             "why": 'Obligate anaerobes are real organisms, found in places such as compost heaps, mud and the gut, for which oxygen is genuinely toxic.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s18',
        "band": 'standard',
        "text": 'A student argues that because both routes ‘release energy from glucose’, comparing them on ‘what they are for’ is pointless, since they are for the same thing. Evaluate this argument.',
        "options": [
            {"text": 'Both routes are always running for exactly the same reason at exactly the same rate.', "correct": False,
             "why": 'The two routes are not running for the same reason at the same rate; one is the constant default and the other is an occasional top-up.'},
            {"text": 'The argument is correct, because anaerobic respiration only exists to replace the aerobic route entirely when it fails.', "correct": False,
             "why": 'Anaerobic respiration adds to the aerobic route rather than replacing it, and aerobic respiration does not typically fail outright.'},
            {"text": 'Anaerobic respiration never actually releases any energy at all.', "correct": False,
             "why": 'Anaerobic respiration does release real energy from glucose, just far less of it per molecule than the aerobic route.'},
            {"text": 'It misses the point — aerobic respiration is the constant default; anaerobic respiration only adds on top.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s19',
        "band": 'standard',
        "text": "A marathon runner's coach says the runner should aim to feel ‘comfortably hard’ rather than ‘all-out’ for most of the race. Explain this advice in terms of the two respiration routes.",
        "options": [
            {"text": 'A comfortably hard pace stays within the aerobic ceiling.', "correct": True},
            {"text": 'An all-out pace is actually more efficient, since it uses only the aerobic route at its very fastest.', "correct": False,
             "why": 'An all-out pace demands far more energy than the aerobic route alone can supply, forcing a large anaerobic contribution instead.'},
            {"text": 'Comfortably hard and all-out use exactly the same mixture of the two routes, just at different speeds.', "correct": False,
             "why": 'The mixture of routes changes with pace; a comfortably hard pace stays mostly aerobic, while all-out effort adds a large anaerobic contribution.'},
            {"text": "The advice has nothing to do with respiration; it is only about the runner's breathing technique.", "correct": False,
             "why": 'The advice is directly about staying within the pace the oxygen supply can cover, which is a respiration issue, not simply a breathing technique.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s20',
        "band": 'standard',
        "text": 'A microbiologist compares an obligate anaerobe from a compost heap with ordinary yeast, and notes that yeast can survive with or without oxygen but the compost organism cannot survive with any oxygen at all. Explain this difference.',
        "options": [
            {"text": 'Yeast cannot actually respire aerobically at all, which is why it survives without oxygen too.', "correct": False,
             "why": 'Yeast can respire aerobically when oxygen is available, which is exactly why it can survive in either kind of condition.'},
            {"text": 'Yeast can switch between routes depending on conditions; the obligate anaerobe is poisoned by oxygen and cannot.', "correct": True},
            {"text": 'The obligate anaerobe simply has not yet evolved the ability to use oxygen, and could learn to given time.', "correct": False,
             "why": 'An obligate anaerobe is poisoned by oxygen rather than merely lacking a skill it could pick up; oxygen exposure harms it directly.'},
            {"text": 'Both organisms behave identically, and the difference described here is a mistake.', "correct": False,
             "why": 'The two organisms genuinely differ: one can use either route, the other is restricted to, and can be harmed outside of, the anaerobic one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s21',
        "band": 'standard',
        "text": 'A student reads that early life on Earth had no oxygen to respire with for roughly two billion years, and asks how anything survived at all during that time. Explain.',
        "options": [
            {"text": 'Nothing did survive; all early life died out once oxygen levels eventually rose.', "correct": False,
             "why": "Some organisms, the ancestors of today's obligate anaerobes, survived by staying in oxygen-free environments rather than dying out."},
            {"text": 'Early organisms stored oxygen from the future to use in advance.', "correct": False,
             "why": 'Storing oxygen from a time before it existed in the atmosphere is not possible; the organisms of that period simply respired anaerobically.'},
            {"text": 'Every living thing at that time respired anaerobically, since anaerobic respiration needs no oxygen at all to work.', "correct": True},
            {"text": 'Life did not exist yet during that period at all.', "correct": False,
             "why": 'Life is understood to have existed for roughly this whole period, respiring anaerobically before atmospheric oxygen became widespread.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s22',
        "band": 'standard',
        "text": "A cyclist's legs demand 180 units of energy for a hard climb, while their aerobic ceiling delivers 150 units. How many units are being supplied anaerobically?",
        "options": [
            {"text": '180 units', "correct": False,
             "why": 'That is the total demand, not just the anaerobic share of it.'},
            {"text": '150 units', "correct": False,
             "why": 'That is the aerobic contribution, not the anaerobic shortfall.'},
            {"text": '330 units', "correct": False,
             "why": 'That comes from adding the two figures together instead of subtracting one from the other.'},
            {"text": '30 units', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s23',
        "band": 'standard',
        "text": 'If aerobic respiration releases about 15.6 kJ per gram of glucose and anaerobic respiration in human muscle releases about one twentieth of that, roughly how much energy does anaerobic respiration release per gram of glucose?',
        "options": [
            {"text": 'About 0.78 kJ', "correct": True},
            {"text": 'About 7.8 kJ', "correct": False,
             "why": 'That treats the anaerobic yield as one half of the aerobic figure, not one twentieth.'},
            {"text": 'About 15.6 kJ', "correct": False,
             "why": 'That is the full aerobic figure, not the much smaller anaerobic one.'},
            {"text": 'About 312 kJ', "correct": False,
             "why": 'That multiplies by twenty instead of dividing by twenty.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s24',
        "band": 'standard',
        "text": 'A student examines a red blood cell and a liver cell under a microscope and finds the red blood cell has no mitochondria while the liver cell is packed with them. Predict how each cell mainly respires, and explain why.',
        "options": [
            {"text": 'Both cells respire mainly aerobically, since every human cell needs the same large amount of energy.', "correct": False,
             "why": 'A cell with no mitochondria at all cannot rely mainly on the aerobic route, which specifically depends on having them.'},
            {"text": 'The red blood cell relies mainly on anaerobic respiration, since aerobic respiration needs mitochondria.', "correct": True},
            {"text": 'The red blood cell does not respire at all, since it has no mitochondria to respire with.', "correct": False,
             "why": 'A cell without mitochondria can still respire anaerobically, which does not require them; it simply cannot use the aerobic route.'},
            {"text": 'The liver cell relies mainly on the anaerobic route, since it needs energy quickly for its many reactions.', "correct": False,
             "why": 'A cell packed with mitochondria is well equipped for the aerobic route, which gets far more energy from each glucose molecule.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s25',
        "band": 'standard',
        "text": 'A student says that since a 100 m sprinter and a compost-heap bacterium both use the anaerobic route, they must be in a similar situation. Evaluate this claim.',
        "options": [
            {"text": 'The comparison is exactly right, since both are entirely reliant on the anaerobic route with nothing else happening.', "correct": False,
             "why": "The sprinter's aerobic respiration is still running flat out at the same time; the two situations are not the same."},
            {"text": 'The comparison is wrong, but only because sprinters never actually use the anaerobic route at all.', "correct": False,
             "why": 'Sprinters do rely heavily on the anaerobic route during an all-out effort; the flaw in the comparison is elsewhere.'},
            {"text": 'The comparison is weak — the sprinter briefly tops up still-running aerobic respiration.', "correct": True},
            {"text": 'The comparison is wrong, but only because bacteria are incapable of anaerobic respiration.', "correct": False,
             "why": 'Many bacteria, including obligate anaerobes, respire anaerobically; the flaw in the comparison is about how each situation differs, not whether bacteria can do it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s26',
        "band": 'standard',
        "text": 'A student notices that a plant root growing normally in well-drained soil and the same species of root in waterlogged soil look outwardly similar for the first day, even though one is aerobic and the other mostly anaerobic. Suggest why the outward appearance takes longer to change than the respiration route does.',
        "options": [
            {"text": 'The respiration route only actually changes once visible wilting has already begun.', "correct": False,
             "why": 'The route a cell is respiring by depends on the oxygen reaching it right now, not on how the plant looks; it changes as soon as the oxygen supply does.'},
            {"text": 'There is no real difference between the two roots at any point, inside or out.', "correct": False,
             "why": 'Internally the two roots are respiring differently from very early on, even while they still look outwardly similar.'},
            {"text": 'Waterlogged roots take days to start respiring anaerobically, unlike the immediate switch in animal muscle.', "correct": False,
             "why": 'The shift to anaerobic respiration in a waterlogged root happens as soon as the oxygen supply is cut, not after a delay of days.'},
            {"text": 'The route shifts almost at once when oxygen is cut off; visible wilting builds up more slowly.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s27',
        "band": 'standard',
        "text": 'A comparison of the two respiration routes sets out an ‘energy per glucose’ row and a ‘what it is for’ row. A student asks why both are needed. What does the energy row tell you that the other one does not?',
        "options": [
            {"text": 'The energy row tells you how efficient each route is.', "correct": True},
            {"text": 'Both rows say exactly the same thing in different words, so only one is really needed.', "correct": False,
             "why": 'The two rows answer different questions — how much energy each route yields, and when each route is actually called upon — so neither one alone tells the whole story.'},
            {"text": 'The ‘what it is for’ row is only needed for anaerobic respiration, since aerobic respiration is never used for anything specific.', "correct": False,
             "why": 'Aerobic respiration is used for something specific too — it is the constant, everyday default — so the row applies to both routes.'},
            {"text": 'The energy row only matters for micro-organisms, not for humans or plants.', "correct": False,
             "why": 'The energy yield of each route matters for any organism using it, humans and plants included, not only micro-organisms.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s28',
        "band": 'standard',
        "text": 'A student says fermentation must be a lesser or incomplete version of respiration compared with what happens in human muscle, because it is carried out by organisms as simple as yeast and bacteria. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since fermentation releases no energy at all to the organism doing it.', "correct": False,
             "why": 'Fermentation does release usable energy to the micro-organism performing it, just as human anaerobic respiration releases energy to the muscle.'},
            {"text": 'The claim is misleading — fermentation is the same process, anaerobic respiration, just carried out by a different organism.', "correct": True},
            {"text": 'The claim is correct, because fermentation is really a form of aerobic respiration in disguise.', "correct": False,
             "why": 'Fermentation is the anaerobic route, not a disguised form of the aerobic one; it uses no oxygen.'},
            {"text": 'The claim is wrong, but only because fermentation and human anaerobic respiration always make exactly identical products.', "correct": False,
             "why": 'The products differ — lactic acid in human muscle, ethanol and carbon dioxide in yeast — even though both are the anaerobic route.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s29',
        "band": 'standard',
        "text": 'A cave explorer finds a pool of stagnant water rich in dissolved sugars but with almost no dissolved oxygen, and notices bubbles of gas rising from it. Suggest what is most likely producing the bubbles, and why.',
        "options": [
            {"text": 'The sugar dissolving in the water is producing the bubbles on its own, without any living organism involved.', "correct": False,
             "why": 'Dissolving sugar does not produce gas bubbles by itself; a living organism respiring is a far more likely source.'},
            {"text": 'Aerobic respiration by micro-organisms in the water is producing the bubbles.', "correct": False,
             "why": 'Almost no dissolved oxygen is available, which makes the aerobic route an unlikely main source of ongoing gas production here.'},
            {"text": 'Micro-organisms in the water respiring anaerobically, most likely fermenting.', "correct": True},
            {"text": 'The bubbles must be air trapped in the rock, unrelated to anything living in the water.', "correct": False,
             "why": 'Rich dissolved sugar and ongoing gas production point strongly towards living organisms respiring, most likely by fermentation.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s30',
        "band": 'standard',
        "text": 'A student compares two identical bacterial cultures, one grown with a steady supply of oxygen and one grown without any oxygen at all, using the same amount of glucose. Predict which culture grows into a larger population, and explain why.',
        "options": [
            {"text": 'The culture without oxygen, because anaerobic respiration is the faster of the two routes.', "correct": False,
             "why": 'Being faster does not mean getting more total energy; the oxygenated culture gets far more energy from the same glucose overall.'},
            {"text": 'Both cultures should grow to exactly the same size, since they start with identical amounts of glucose.', "correct": False,
             "why": 'Identical starting glucose does not guarantee identical growth, because the two routes release very different amounts of usable energy from it.'},
            {"text": 'Neither culture can grow at all without a supply of extra sugar beyond what was given.', "correct": False,
             "why": 'Both cultures can grow using only the glucose provided; what differs between them is how much growth that same glucose can support.'},
            {"text": 'The culture grown with oxygen, since aerobic respiration releases far more energy from each glucose molecule.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s31',
        "band": 'standard',
        "text": 'A student argues that since humans, yeast and lactic acid bacteria can all respire anaerobically, the anaerobic route must always make the same product in every organism. Evaluate this claim.',
        "options": [
            {"text": 'The claim is wrong — human muscle makes lactic acid, yeast makes ethanol and carbon dioxide.', "correct": True},
            {"text": 'The claim is correct, since anaerobic respiration by definition always produces exactly the same single product.', "correct": False,
             "why": 'The products genuinely differ by organism — lactic acid in humans and in these bacteria, ethanol and carbon dioxide in yeast.'},
            {"text": 'The claim is correct, because yeast and lactic acid bacteria are actually the same organism.', "correct": False,
             "why": 'Yeast is a fungus and lactic acid bacteria are bacteria; they are different kinds of organism making different anaerobic products.'},
            {"text": 'The claim is wrong, but only because humans cannot actually respire anaerobically at all.', "correct": False,
             "why": 'Human muscle cells do respire anaerobically, making lactic acid, when demand outruns the oxygen supply.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-s32',
        "band": 'standard',
        "text": 'A student says the twentyfold energy advantage of aerobic respiration means anaerobic respiration should have disappeared entirely once aerobic respiration evolved. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, and anaerobic respiration genuinely has disappeared from every living organism alive today.', "correct": False,
             "why": 'Anaerobic respiration is still used by humans, yeast, many bacteria and plants under low-oxygen conditions; it has not disappeared.'},
            {"text": 'The claim ignores speed — anaerobic respiration still supplies energy faster and without waiting for oxygen.', "correct": True},
            {"text": 'The claim is correct, because the twentyfold energy advantage means aerobic respiration is better in absolutely every way.', "correct": False,
             "why": 'Aerobic respiration is not better in every way; anaerobic respiration wins on speed and on working without any oxygen at all.'},
            {"text": 'The claim is wrong, but only because the energy advantage is much smaller than twenty times in reality.', "correct": False,
             "why": 'The size of the energy advantage is not the flaw here; the flaw is ignoring the genuine advantage anaerobic respiration keeps in speed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h11',
        "band": 'harder',
        "text": 'A researcher proposes that any organism found respiring anaerobically must be under some kind of stress, since the aerobic route is so much more efficient. Evaluate this proposal using named examples.',
        "options": [
            {"text": 'The proposal is wrong — yeast, lactic acid bacteria and obligate anaerobes all use it as a normal, unstressed part of their biology.', "correct": True},
            {"text": 'The proposal is correct, since every organism that respires anaerobically is always responding to some kind of emergency.', "correct": False,
             "why": 'Yeast fermenting sugar, lactic acid bacteria in yoghurt and obligate anaerobes are not in any emergency; anaerobic respiration is their normal way of life.'},
            {"text": 'The proposal is correct, because efficiency always determines which route any organism is forced to use.', "correct": False,
             "why": 'Many organisms use the anaerobic route by default, not because they are forced into it by circumstances; efficiency is not the only factor.'},
            {"text": 'The proposal is wrong, but only because the aerobic route is not actually more efficient than the anaerobic one.', "correct": False,
             "why": 'The aerobic route genuinely does release far more energy per glucose molecule; the flaw in the proposal is elsewhere.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h12',
        "band": 'harder',
        "text": 'A student claims that since both routes start with glucose, a chemical test on the starting material of a reaction could never tell you which route a cell used. Evaluate this claim.',
        "options": [
            {"text": 'The claim is entirely correct, and no test of any kind could ever distinguish the two routes from each other.', "correct": False,
             "why": 'Testing the products — carbon dioxide and water for one route, lactic acid or ethanol for the other — can distinguish the two routes clearly.'},
            {"text": 'The claim is right about the starting material, but a test on the products, rather than the glucose, could easily tell the two routes apart.', "correct": True},
            {"text": 'The claim is wrong, because the two routes actually start from different substances, not the same glucose.', "correct": False,
             "why": 'Both routes genuinely start from the same glucose molecule; that part of the claim is correct.'},
            {"text": 'The claim is wrong, but only because glucose itself looks visibly different depending on which route respires it.', "correct": False,
             "why": 'Glucose does not change its appearance depending on which route will respire it; the real point is that the products, not the starting glucose, reveal the route.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h13',
        "band": 'harder',
        "text": "A physiologist measures a runner's oxygen uptake rising smoothly right up to a plateau as the runner accelerates, and notes that beyond that point speed keeps increasing anyway. What does the plateau itself show?",
        "options": [
            {"text": "Beyond the plateau the runner's oxygen uptake must still be rising, just too slowly to measure with the equipment used.", "correct": False,
             "why": 'A genuine plateau means oxygen uptake has stopped rising at all; the extra speed beyond it has to come from a different source, the anaerobic route.'},
            {"text": 'The plateau shows that the runner has stopped needing oxygen altogether from that point onwards.', "correct": False,
             "why": 'Oxygen uptake plateauing at a maximum does not mean it drops to zero; the aerobic route continues running flat out at that ceiling.'},
            {"text": "The plateau marks the runner's aerobic ceiling.", "correct": True},
            {"text": 'Speed cannot actually keep increasing once oxygen uptake plateaus, so the measurement must be a mistake.', "correct": False,
             "why": 'Speed increasing past an oxygen-uptake plateau is exactly what happens once the anaerobic route starts covering the extra demand.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h14',
        "band": 'harder',
        "text": 'A study finds that a species of deep-sea worm living beside a hydrothermal vent has mitochondria in every cell, despite living somewhere with very little dissolved oxygen. A student argues this must mean the worm cannot really be using its mitochondria for very much. Evaluate this argument.',
        "options": [
            {"text": 'The argument is correct, since an organism can only ever use its mitochondria if oxygen is abundant everywhere it lives.', "correct": False,
             "why": 'Even a low, patchy oxygen supply can still be used by mitochondria for some genuine aerobic respiration; abundance everywhere is not required for them to do useful work.'},
            {"text": 'The argument is correct, because mitochondria are only ever found in organisms that respire purely aerobically.', "correct": False,
             "why": 'Organisms that rely heavily on anaerobic respiration can still have mitochondria and use them when any oxygen is available.'},
            {"text": 'The argument is wrong, but only because deep-sea worms do not actually contain any mitochondria at all.', "correct": False,
             "why": "The situation states the worm's cells do contain mitochondria; the flaw in the argument lies in assuming they must therefore be doing little."},
            {"text": 'The argument is weak — the mitochondria could still be doing real aerobic work whenever any oxygen is available.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h15',
        "band": 'harder',
        "text": 'A textbook states that ‘about twenty times more energy’ is released by aerobic respiration than by anaerobic respiration, while a research paper gives the ratio as closer to fifteen. A student says one of these must be wrong. Evaluate this claim.',
        "options": [
            {"text": 'Neither source needs to be wrong — both are estimates of a ratio that can genuinely vary depending on exactly how the accounting is done and which organism or tissue is measured.', "correct": True},
            {"text": "The student is right, and the textbook's rounder figure must simply be an error copied from an older source.", "correct": False,
             "why": 'A rounder figure is not automatically an error; both values can be reasonable estimates of a ratio that varies with how it is measured.'},
            {"text": 'A true scientific ratio can only ever have one single correct value.', "correct": False,
             "why": 'Ratios like this one can genuinely vary with measurement conditions and organism, so more than one reasonable value can exist.'},
            {"text": 'The student is wrong, but only because anaerobic respiration actually releases more energy than aerobic respiration.', "correct": False,
             "why": 'Aerobic respiration is the one releasing far more energy per glucose molecule; the disagreement here is only about the precise size of that ratio.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h16',
        "band": 'harder',
        "text": 'A coach trains two athletes to the same fitness level, but one is given breathing exercises that increase how deeply they breathe, while the other trains their heart and blood vessels through interval running. After some weeks, only the second athlete can sustain a faster pace before their legs begin to burn. Explain this difference.',
        "options": [
            {"text": 'Breathing exercises should have worked just as well, since taking in more air with each breath always delivers more oxygen to working muscles.', "correct": False,
             "why": 'Delivery to the muscles depends on the whole cardiovascular system carrying the oxygen there, not simply on how much air fills the lungs each breath.'},
            {"text": 'Sustaining a faster aerobic pace depends on how much oxygen the heart and blood can deliver to the muscles, not on how deeply the lungs fill with air.', "correct": True},
            {"text": "The interval-trained athlete's muscles must now need less oxygen overall to run at any given pace.", "correct": False,
             "why": 'The improvement described is in how much oxygen can be delivered to the muscles, not in how little the muscles need to do the same work.'},
            {"text": "Neither form of training should make any real difference to how far a runner's aerobic ceiling extends.", "correct": False,
             "why": 'Cardiovascular training of the kind the second athlete did is well known to raise the pace at which the aerobic ceiling is reached.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h17',
        "band": 'harder',
        "text": 'A student proposes that since obligate anaerobes are killed by oxygen, and humans need oxygen to survive, humans and obligate anaerobes must have completely unrelated biology with nothing meaningfully in common. Evaluate this claim.',
        "options": [
            {"text": "Human cells and an obligate anaerobe's cells work by two entirely different kinds of chemistry with nothing shared at all.", "correct": False,
             "why": 'Both kinds of cell break down glucose to release energy, and human muscle can even use the identical anaerobic route an obligate anaerobe relies on permanently.'},
            {"text": 'Obligate anaerobes do not actually respire in any way at all.', "correct": False,
             "why": 'Obligate anaerobes do respire, using the anaerobic route exclusively; the flaw in the claim is elsewhere.'},
            {"text": 'The claim overstates the difference — both still respire by breaking down glucose to release energy.', "correct": True},
            {"text": 'Obligate anaerobes can survive perfectly well in the presence of oxygen too.', "correct": False,
             "why": 'Obligate anaerobes are specifically harmed by oxygen and cannot survive well where it is present; that part of the original claim is correct.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h18',
        "band": 'harder',
        "text": "A patient with severe lung disease is found to rely more heavily on anaerobic respiration during everyday activities than a healthy person doing the same tasks. A doctor explains this is not really a difference in the patient's muscles at all. Explain what the doctor most likely means.",
        "options": [
            {"text": "The doctor most likely means the patient's muscles have started fermenting glucose the way yeast does.", "correct": False,
             "why": 'Human muscle produces lactic acid anaerobically, not ethanol as yeast does when fermenting; the mechanism the doctor is describing is the oxygen delivery ceiling, not a change to fermentation.'},
            {"text": 'The doctor most likely means everyday activity itself now demands far more total energy than it used to.', "correct": False,
             "why": "The energy an everyday activity demands has not changed; what has changed is how much of that demand the patient's reduced oxygen delivery can cover."},
            {"text": "The doctor most likely means the patient's muscles have permanently lost the ability to respire aerobically at all.", "correct": False,
             "why": 'The muscles can still respire aerobically; the limiting factor described is how much oxygen the diseased lungs can deliver to them, not a loss of the aerobic route itself.'},
            {"text": "The patient's oxygen delivery ceiling is lower because of the lung disease.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h19',
        "band": 'harder',
        "text": 'A biologist argues that because the Great Oxygenation Event was caused by early photosynthetic organisms, and photosynthesis is unrelated to respiration, the rise of atmospheric oxygen and the story of aerobic respiration are two completely separate topics. Evaluate this argument.',
        "options": [
            {"text": 'The argument is wrong — that released oxygen is exactly what made aerobic respiration possible afterwards.', "correct": True},
            {"text": 'The argument is correct, since photosynthesis and aerobic respiration share no connection of any kind whatsoever.', "correct": False,
             "why": 'The oxygen released by early photosynthesis is precisely what supplied the aerobic route with the gas it needs; the two are closely linked historically.'},
            {"text": 'The argument is correct, because aerobic respiration existed on Earth long before there was any oxygen in the atmosphere at all.', "correct": False,
             "why": 'Aerobic respiration depends on oxygen being available, so it could not have existed in any meaningful way before atmospheric oxygen rose.'},
            {"text": 'The argument is wrong, but only because photosynthesis and respiration are actually the exact same chemical reaction happening in reverse.', "correct": False,
             "why": 'Photosynthesis and respiration are different reactions with different purposes; the real connection is that one made the atmospheric oxygen the other depends on.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h20',
        "band": 'harder',
        "text": "A rowing crew and a marathon runner both finish their events breathing hard, but the crew recovers to a normal breathing rate within two minutes while the runner takes almost as long despite covering the race at a steadier effort throughout. Suggest why the crew's recovery pattern fits an oxygen debt story more clearly than the runner's does.",
        "options": [
            {"text": 'The crew must not really be experiencing any oxygen debt at all, since two minutes is too short a time for one to be repaid.', "correct": False,
             "why": 'Two minutes is a perfectly plausible recovery time for repaying an oxygen debt built up over a short, intense race such as rowing.'},
            {"text": "The crew's event demands an intense, short burst well above their aerobic ceiling.", "correct": True},
            {"text": 'The marathon runner cannot be experiencing any oxygen debt, since a well-paced marathon is supposed to stay mostly aerobic.', "correct": False,
             "why": 'Staying mostly aerobic does not rule out some anaerobic contribution and a resulting oxygen debt, especially towards the end of a hard race; the debt is simply smaller and more gradually built.'},
            {"text": 'Both events should produce an identical recovery pattern, since both athletes are described as breathing hard at the finish.', "correct": False,
             "why": 'Breathing hard at the finish does not guarantee an identical recovery pattern; how the effort was distributed through the event affects how the debt built up and is repaid.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h21',
        "band": 'harder',
        "text": 'A student proposes a rule: ‘any cell containing mitochondria must be respiring mainly aerobically.’ A colleague objects that this rule is too simple, citing red blood cells that lack mitochondria entirely and still function. Evaluate the proposed rule using this and one further example of your own.',
        "options": [
            {"text": 'The rule is correct, and the sprinting muscle example does not actually challenge it in any way.', "correct": False,
             "why": 'A sprinting muscle cell has plenty of mitochondria yet relies heavily on the anaerobic route during an all-out effort, which is exactly the kind of case that challenges the rule.'},
            {"text": 'The rule only needs the word ‘always’ instead of ‘mainly’ to become completely correct.', "correct": False,
             "why": 'Making the rule stricter would make it fail even more clearly, since plenty of mitochondria-rich cells rely heavily on the anaerobic route at times of very high demand.'},
            {"text": 'The rule is too simple — a sprinting muscle cell has plenty of mitochondria yet relies heavily on the anaerobic route.', "correct": True},
            {"text": 'The rule is wrong, but only because mitochondria are not actually where aerobic respiration happens.', "correct": False,
             "why": 'Mitochondria genuinely are where aerobic respiration happens; the flaw in the rule is assuming their presence guarantees which route currently dominates.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h22',
        "band": 'harder',
        "text": "A researcher proposes measuring ‘how anaerobic’ an organism's lifestyle is purely by counting how many of its genes are devoted to anaerobic enzymes, arguing that gene count alone settles the question. Evaluate this proposal.",
        "options": [
            {"text": 'The proposal is sound, since the number of genes an organism has for a process always matches exactly how much it uses that process.', "correct": False,
             "why": 'An organism can carry genes for a route it rarely uses; gene count does not automatically match how the organism actually behaves.'},
            {"text": 'The proposal is sound, because only obligate anaerobes carry any genes for anaerobic enzymes at all.', "correct": False,
             "why": 'Organisms that are not obligate anaerobes, including humans, also carry genes for the anaerobic route, since they can use it too.'},
            {"text": 'The proposal is flawed, but only because genes for anaerobic enzymes do not actually exist in any organism.', "correct": False,
             "why": 'Genes for anaerobic enzymes do exist and are used by many organisms; the flaw in the proposal is treating gene count as equivalent to actual behaviour.'},
            {"text": 'The proposal is too narrow — an organism could carry the genes for both routes yet spend almost all its life using only one of them.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h23',
        "band": 'harder',
        "text": "A study compares the mitochondria count in flight muscle from a hovering hummingbird with that in a similarly sized muscle from an animal that relies heavily on short anaerobic bursts, such as a crocodile's tail. Predict which has more mitochondria, and explain the link to each animal's typical use of energy.",
        "options": [
            {"text": "The hummingbird's flight muscle, since sustained hovering demands a continuous, very high rate of aerobic respiration.", "correct": True},
            {"text": "The crocodile's tail muscle, since anaerobic respiration is the faster route and therefore needs more mitochondria to keep up.", "correct": False,
             "why": 'Anaerobic respiration happens outside the mitochondria; a muscle relying mainly on that route does not need large numbers of them for that purpose.'},
            {"text": 'Both muscles should contain an identical number of mitochondria, since mitochondria count depends only on muscle size, not on how it is used.', "correct": False,
             "why": 'How a muscle is typically used, sustained aerobic effort or short anaerobic bursts, is closely linked to how many mitochondria it contains, not size alone.'},
            {"text": 'Neither muscle should contain any meaningful number of mitochondria, since both animals also rely on anaerobic respiration at times.', "correct": False,
             "why": 'Using the anaerobic route sometimes does not prevent a muscle built mainly for sustained aerobic work from containing large numbers of mitochondria.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h24',
        "band": 'harder',
        "text": 'A team recovers an ancient, oxygen-free sediment sample from deep underground and finds living bacteria still active inside it after being sealed away for thousands of years. A student argues this proves aerobic respiration is not really necessary for complex life. Evaluate this argument.',
        "options": [
            {"text": 'The argument is correct, since any organism surviving without oxygen proves aerobic respiration is unnecessary for complex life of any kind.', "correct": False,
             "why": 'Simple bacterial survival without oxygen does not show that complex, multicellular life could be sustained the same way; the two are very different scales of organisation.'},
            {"text": 'The argument overreaches — it shows simple bacteria can survive without oxygen, not that complex life could too.', "correct": True},
            {"text": 'The argument is correct, because complex life and simple bacterial life have identical energy requirements.', "correct": False,
             "why": 'Complex, multicellular organisms generally have far higher and more sustained energy demands than simple single-celled bacteria.'},
            {"text": 'The argument is wrong, but only because bacteria that old could not possibly still be alive.', "correct": False,
             "why": "The situation states the bacteria were found still active; the flaw in the argument is about what this evidence can and cannot show, not about the bacteria's survival itself."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h25',
        "band": 'harder',
        "text": 'A student notices that the ‘energy per glucose’ row in a comparison table and the ‘rate’ row seem to pull in opposite directions, and asks why evolution has not simply settled on whichever route is ‘better’. Explain why both routes have persisted.',
        "options": [
            {"text": 'Evolution has not yet had enough time to eliminate whichever route is worse, and eventually only one will remain.', "correct": False,
             "why": 'Both routes offer a genuine, lasting advantage in different situations, rather than one simply being an inferior route awaiting elimination.'},
            {"text": 'The aerobic route is simply better in every way, and anaerobic respiration survives only in organisms too simple to have evolved past it.', "correct": False,
             "why": 'Even complex organisms with full access to aerobic respiration, humans included, still rely on the anaerobic route when speed matters more than yield.'},
            {"text": 'Neither route is better overall — aerobic wins on yield, anaerobic wins on speed, so both remain useful.', "correct": True},
            {"text": 'The two rows do not actually pull in opposite directions at all, and the student has misread the table.', "correct": False,
             "why": 'The two properties genuinely do pull in different directions — the faster route yields less, and the higher-yielding route is slower — which is exactly why both persist.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h26',
        "band": 'harder',
        "text": 'A pharmaceutical company wants to grow an anaerobic bacterium industrially to harvest a chemical it excretes, and an engineer suggests improving yield by pumping extra oxygen into the fermenter to speed up growth. Evaluate this suggestion.',
        "options": [
            {"text": 'The suggestion is sound, since extra oxygen always speeds up the growth of any bacterium being grown industrially.', "correct": False,
             "why": 'Extra oxygen only speeds up organisms that can use it; a strict anaerobe would be harmed rather than helped by it.'},
            {"text": 'The suggestion is sound, because anaerobic bacteria secretly rely on small amounts of oxygen to grow properly.', "correct": False,
             "why": 'A strict, obligate anaerobe does not rely on any oxygen at all to grow; oxygen is specifically what harms it.'},
            {"text": 'The suggestion makes no difference, since oxygen never affects bacterial growth rate.', "correct": False,
             "why": 'Oxygen levels can matter a great deal to bacterial growth rate, in either direction, depending on whether the species can tolerate or use it.'},
            {"text": 'The suggestion is likely to backfire — added oxygen would harm a strict anaerobe rather than speed it up.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h27',
        "band": 'harder',
        "text": 'A comparison table states that anaerobic respiration ‘needs no oxygen’. A student argues this single fact makes anaerobic respiration strictly better than aerobic respiration in every real situation, since it removes a limiting factor. Evaluate this argument.',
        "options": [
            {"text": 'The argument ignores the huge trade-off in energy yield.', "correct": True},
            {"text": 'The argument is correct, since removing any limiting factor from a reaction always makes it better in every situation.', "correct": False,
             "why": 'Removing the need for oxygen brings a large cost in energy yield, so it is not automatically an advantage in every situation, only where oxygen delivery is genuinely the bottleneck.'},
            {"text": 'The argument is correct, because oxygen is always in short supply for every organism, everywhere, all the time.', "correct": False,
             "why": 'Oxygen is often readily available, which is exactly why the aerobic route is the default for most everyday activity in most organisms.'},
            {"text": 'The argument is wrong, but only because anaerobic respiration does actually need a small amount of oxygen to run.', "correct": False,
             "why": 'Anaerobic respiration genuinely needs no oxygen at all; the flaw in the argument is about weighing this fact against the yield trade-off, not about the fact itself.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h28',
        "band": 'harder',
        "text": 'A student proposes that since anaerobic respiration ‘came first’ in the history of life, it must be the more primitive and therefore less useful process today. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since anything that evolved earlier in the history of life is automatically less useful than anything that evolved later.', "correct": False,
             "why": 'Being older does not make a process less useful; anaerobic respiration still provides real, current advantages such as speed and independence from oxygen.'},
            {"text": 'The claim confuses age with usefulness — anaerobic respiration still offers real speed and needs no oxygen today.', "correct": True},
            {"text": 'The claim is correct, because only obligate anaerobes, which are considered primitive organisms, still use the anaerobic route today.', "correct": False,
             "why": 'Humans, yeast and many other organisms that are not considered primitive still use the anaerobic route regularly, not only obligate anaerobes.'},
            {"text": 'The claim is wrong, but only because anaerobic respiration evolved after the aerobic route.', "correct": False,
             "why": 'Anaerobic respiration is understood to have come first, since life existed for a long period before atmospheric oxygen became available; the flaw in the claim is elsewhere.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h29',
        "band": 'harder',
        "text": 'A student is asked to design an experiment to find out whether a newly discovered single-celled organism respires aerobically, anaerobically, or both, without knowing anything about it in advance. Suggest a sensible first step, and explain what result would point towards each possibility.',
        "options": [
            {"text": 'Simply look at the organism under a microscope, since aerobic and anaerobic organisms always look visibly different from each other.', "correct": False,
             "why": 'Appearance under a microscope does not reliably reveal which route an organism uses; testing its behaviour and products under different conditions is more informative.'},
            {"text": 'Assume it must be anaerobic, since most newly discovered single-celled organisms turn out to be anaerobic.', "correct": False,
             "why": 'Assuming an answer without testing does not establish anything reliably; a proper comparison under different oxygen conditions is needed.'},
            {"text": 'Grow it with and without oxygen and test the products; aerobic-only, anaerobic-only or both growing reveals the answer.', "correct": True},
            {"text": "There is no way to find this out experimentally, and it would have to be assumed from the organism's genes alone.", "correct": False,
             "why": 'Growing the organism under different oxygen conditions and testing its products is a genuinely practical experimental approach to this question.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h30',
        "band": 'harder',
        "text": 'A student argues that because both routes ultimately just ‘release energy’, the entire topic of aerobic versus anaerobic respiration is really only about chemistry and has no real relevance to how an organism actually lives its life. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since the chemistry of releasing energy is identical in every organism regardless of which route it uses.', "correct": False,
             "why": 'The chemistry differs significantly between the two routes, and which one an organism relies on has real, visible consequences for how it lives.'},
            {"text": 'The claim is correct, because only humans are affected by which respiration route they use, not any other organism.', "correct": False,
             "why": 'Yeast, bacteria and plants are all affected by which respiration route dominates for them too, not only humans.'},
            {"text": 'The claim is wrong, but only because anaerobic respiration does not actually release any energy that an organism can use.', "correct": False,
             "why": 'Anaerobic respiration does release genuinely usable energy; the flaw in the claim is dismissing the real-life relevance of which route dominates, not the energy release itself.'},
            {"text": 'The claim badly understates the relevance.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h31',
        "band": 'harder',
        "text": 'A student says that because oxygen delivery is a ‘ceiling’ that limits the aerobic route, training to raise that ceiling must eventually let an athlete do everything aerobically, with no anaerobic contribution ever needed again. Evaluate this claim.',
        "options": [
            {"text": 'The claim overreaches — an all-out sprint will always demand more than any realistic ceiling can supply.', "correct": True},
            {"text": "The claim is correct, since there is no upper limit to how high training can raise a person's oxygen delivery ceiling.", "correct": False,
             "why": 'Training raises the ceiling considerably but not without limit; extreme, sudden efforts can still demand more than even a highly trained ceiling can supply.'},
            {"text": 'The claim is correct, because elite athletes never use the anaerobic route at any point in any event.', "correct": False,
             "why": 'Even elite athletes use the anaerobic route during genuinely maximal efforts, such as an all-out sprint finish.'},
            {"text": "The claim is wrong, but only because training cannot raise a person's oxygen delivery ceiling at all.", "correct": False,
             "why": "Training genuinely can raise a person's oxygen delivery ceiling considerably; the flaw in the claim is assuming this removes the need for the anaerobic route entirely."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-05-h32',
        "band": 'harder',
        "text": 'A student concludes from this whole topic that ‘anaerobic respiration is always worse than aerobic respiration, just sometimes necessary’. Write a brief evaluation of whether ‘worse’ is really the right word, using the idea of a trade-off.',
        "options": [
            {"text": '‘Worse’ is exactly right, since anaerobic respiration is simply a broken or incomplete version of aerobic respiration.', "correct": False,
             "why": 'Anaerobic respiration is a complete, functioning reaction in its own right, not a broken version of the aerobic route; it simply trades yield for speed.'},
            {"text": '‘Worse’ misses the point of a trade-off.', "correct": True},
            {"text": '‘Worse’ is exactly right, because organisms would always choose the aerobic route if they had any real choice in the matter.', "correct": False,
             "why": 'Organisms genuinely rely on the anaerobic route by choice in situations where its speed or oxygen-independence is what is actually needed, not only when forced.'},
            {"text": 'Neither word applies, since the two routes cannot be compared or evaluated against each other in any way at all.', "correct": False,
             "why": 'The two routes can be meaningfully compared, on yield and on speed in particular; the evaluation here is about which word best describes the result of that comparison.'},
        ],
        "figure": None,
    },
]

QUESTIONS.extend(_MRB338_NEW_QUESTIONS)
