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
            {"text": "The sealed one, because the ethanol it makes is used to "
                     "build new cells.",
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
            {"text": "The aerated one, because aerobic respiration gets far "
                     "more from each molecule.",
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
