# -*- coding: utf-8 -*-
"""Trophic levels, in the lean shape. LEGACY: the live batch-10 Design page.
Spec table: ks4-trophic-levels.md (AQA 8461 4.7.4.1, biology only; the page exists on TF and TH).

The ladder (rungs) and the practice set (BANK, written in the logic, five items, the same on TF
and TH) stay from the legacy page, so their ids survive. The practice set does NOT read the
subtopic `quiz` list, so its fixes are logic_edits, not a quiz JSON. Every edit keeps the item in
its place and keeps its question text, so every id survives."""

LESSON = {
    "slug": "trophic-levels",
    "start": {
        "setup": "A food chain: grass → rabbit → fox.",
        "question": "If you had to guess, which one is at trophic level 1?",
        "options": [
            ("The grass",
             "The grass. Level 1 is always the producer, which makes its own food. The rabbit is "
             "level 2 and the fox is level 3."),
            ("The fox",
             "The grass. Level 1 is always the producer, which makes its own food. The rabbit is "
             "level 2 and the fox is level 3."),
        ],
        "answer": 0,
    },
    "words": ["trophic level", "producer", "apex predator", "decomposer"],
    "knowledge": [
        {"kind": "card", "title": "Numbering the levels",
         "body": ["Trophic levels can be represented by numbers, starting at level 1 with plants "
                  "and algae.",
                  "Further trophic levels are numbered according to how far the organism is "
                  "along the food chain.",
                  "Each arrow points from the organism that is eaten to the organism that eats "
                  "it.",
                  {"slot": "fig:oak-trophic-levels"}]},
        {"kind": "reveal", "title": "The four levels",
         "cols": ["Name", "Which organisms"],
         "rows": [("Level 1", "Producers", "Plants and algae. They make their own food."),
                  ("Level 2", "Primary consumers", "Herbivores that eat plants or algae."),
                  ("Level 3", "Secondary consumers", "Carnivores that eat herbivores."),
                  ("Level 4", "Tertiary consumers", "Carnivores that eat other carnivores.")]},
        {"kind": "card", "title": "Apex predators",
         "body": ["Apex predators are carnivores with no predators.",
                  "In the oak tree chain, the sparrowhawk is the apex predator. Nothing eats it."]},
        {"kind": "card", "title": "One animal, two levels",
         "body": ["The level depends on what the organism eats in that food chain.",
                  {"points": [
                      "Grass → rabbit → fox: the fox is at level 3.",
                      "Blackberries → fox: the fox is at level 2, because it eats the producer "
                      "directly.",
                  ]}]},
        {"kind": "card", "title": "Decomposers",
         "body": ["Decomposers break down dead plant and animal matter by secreting enzymes into "
                  "the environment.",
                  "Small soluble food molecules then diffuse into the microorganism.",
                  {"slot": "fig:decomposer-feeding"}]},
        {"kind": "card", "title": "Why food chains are short",
         "body": ["Only about 10% of the biomass from each trophic level is transferred to the "
                  "level above it.",
                  "After four or five levels, too little biomass is left to support another "
                  "level.",
                  "The Transfer of biomass lesson explains where the rest goes."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The arrow points to what the animal eats.",
              "The arrow points from the organism eaten to the organism that eats it."),
             ("The apex predator is level 1, because it is the top.",
              "Level 1 is always the producer."),
             ("A fox is always at level 3.",
              "Count from the producer in that chain."),
             ("Decomposers swallow dead leaves.",
              "They secrete enzymes onto the dead matter, then small soluble molecules diffuse "
              "in."),
         ]}]},
    ],
    "key_fact": "Trophic levels are numbered along the food chain from level 1, the producers "
                "(plants and algae): level 2 primary consumers, level 3 secondary consumers, "
                "level 4 tertiary consumers. Apex predators are carnivores with no predators.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: give the trophic level of an organism in a given chain.",
             "<strong>Describe</strong>: say how the levels differ, using the level number and "
             "the feeding role.",
             "<strong>Explain</strong>: say what happens and why, for example why the same "
             "animal can be at two levels.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Figure: the "apex predator" label sat between the blue tit and the sparrowhawk.
            # Centre it under the sparrowhawk (box x 535 to 665).
            ("TXN(535, 235, 'apex predator: no predators'",
             "TXN(600, 235, 'apex predator: no predators'"),
            # Rung 2 Q2: the credited option was visibly the longest. Same shape distractors.
            ("['Level 3 with rabbits, level 2 with blackberries', ['Level 3 in both', "
             "'With blackberries it eats a producer directly.'], ['Level 2 in both', "
             "'Rabbits are level 2, so a fox eating them is level 3.']]",
             "['Level 3 with rabbits, level 2 with blackberries', ['Level 2 with rabbits, "
             "level 3 with blackberries', 'Count from the producer: grass 1, rabbit 2, so the "
             "fox eating rabbits is level 3.'], ['Level 3 in both, because a fox is a "
             "carnivore', 'With blackberries it eats a producer directly, so it is level 2.']]"),
            # Practice Q1 (question text kept, id kept): the credited option was the longest by
            # far, called grass "prey", and every option had a dash tail.
            ('''[["Arrows point from prey to predator — they show the direction of energy flow from grass to rabbit to fox", true], ["Arrows point from predator to prey — they show what each animal eats", false], ["Arrows point both ways — energy flows in both directions between organisms", false], ["Arrows are just organisational — they don't have a specific meaning in food chains", false]], { "1": "Arrows point FROM prey TO predator — showing the direction of energy transfer. So the arrow goes Grass → Rabbit, meaning energy flows FROM grass TO rabbit (rabbit eats grass).", "2": "Energy does not flow backwards in a food chain — energy is transferred in one direction only, from prey to predator.", "3": "Arrows have a precise meaning in food chains — they show the direction of energy flow, which is always one-way." }''',
             '''[["From food to eater: the way biomass is transferred", true], ["From eater to food: what each animal has eaten", false], ["Both ways: biomass flows in both directions at once", false], ["No direction: they only join the names together", false]], { "1": "The arrow points to the eater. Grass → rabbit means the rabbit eats the grass.", "2": "Biomass only passes one way, from the organism eaten to the organism that eats it.", "3": "Each arrow shows the direction biomass is transferred, from food to eater." }'''),
            # Practice Q2 (question text kept): spec says biomass, not energy; the credited
            # option was the longest by far, with a dash tail.
            ('''[["Only about 10% of energy is transferred between each level — so little energy remains at higher levels that another level cannot be supported", true], ["There are not enough different species to fill more levels", false], ["Higher levels contain too many organisms — there is not enough space", false], ["Predators at higher levels are too large to eat anything at a lower level", false]], { "1": "The number of species is not the limiting factor — energy availability is. The 10% transfer rule means each successive level has drastically less energy.", "2": "Higher trophic levels have FEWER organisms (less energy = fewer individuals can be sustained), not more.", "3": "Predator size is not the reason — many small organisms occupy higher trophic levels (e.g. parasites, some insects)." }''',
             '''[["Only about 10% of the biomass passes to each next level", true], ["There are not enough different species to fill more levels", false], ["Higher levels have too many organisms to fit in", false], ["Top predators are too large to eat anything else", false]], { "1": "The limit is biomass. Only about 10% passes up each level, so little is left.", "2": "Higher levels have fewer organisms, because less biomass reaches them.", "3": "Size is not the reason. Too little biomass is left to support another level." }'''),
            # Practice Q4 (question text kept): the credited option was the longest by far.
            ("'They secrete enzymes into the environment; small soluble food molecules then "
             "diffuse into the microorganism', [['They swallow the dead matter whole', "
             "'Microorganisms have no mouth.'], ['They absorb large molecules directly', "
             "'Large molecules must be broken down first.'], ['They photosynthesise', "
             "'Decomposers feed on dead matter.']]",
             "'They secrete enzymes; small soluble molecules diffuse in', "
             "[['They swallow it whole and digest it inside a stomach', 'Microorganisms have no "
             "mouth or stomach. The enzymes work outside them.'], ['They take in the large "
             "molecules whole, without enzymes', 'Large molecules must be broken down first.'], "
             "['They make their own food from it by photosynthesis', 'Decomposers feed on dead "
             "matter.']]"),
        ],
    },
}
