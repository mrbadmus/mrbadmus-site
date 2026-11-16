# -*- coding: utf-8 -*-
"""Deforestation, in the lean shape. Legacy Design page (batch 10): the ladder and the practice
set stay from it, with the fixes in logic_edits below.
Spec table: ks4-deforestation.md (AQA 8464 4.7.3.4 / 8461 4.7.3.4, the same words in both)."""

LESSON = {
    "slug": "deforestation",
    "start": {
        "setup": "A patch of rainforest is cut down and burned to make room for cattle.",
        "question": "If you had to guess, what happens to the carbon dioxide in the atmosphere?",
        "options": [
            ("It increases",
             "It increases. Burning releases carbon dioxide, and fewer trees are left to take it in "
             "by photosynthesis."),
            ("It decreases",
             "It increases. Burning releases carbon dioxide, and fewer trees are left to take it in "
             "by photosynthesis."),
        ],
        "answer": 0,
    },
    "words": ["deforestation", "biofuel", "decay", "biodiversity"],
    "knowledge": [
        {"kind": "card", "title": "Why tropical forest is cleared",
         "body": ["Large-scale deforestation in tropical areas has occurred to:",
                  {"points": ["provide land for cattle and rice fields",
                              "grow crops for biofuels"]},
                  "A biofuel is a fuel made from plants, such as ethanol made from sugar cane."]},
        {"kind": "card", "title": "Two reasons carbon dioxide rises",
         "body": [{"points": [
             "<strong>Less is taken in</strong>: fewer trees means less photosynthesis, so less "
             "carbon dioxide is removed from the atmosphere.",
             "<strong>More is released</strong>: burning the trees releases the carbon in the wood "
             "as carbon dioxide. Microorganisms that decay the leftover wood respire, and release "
             "carbon dioxide too.",
         ]},
                  "Look at the arrows for photosynthesis, burning and decay.",
                  {"slot": "legacy-fig:fFig"}]},
        {"kind": "card", "title": "What happens to biodiversity",
         "body": ["Clearing the forest destroys the habitat of many species.",
                  "They lose their food and shelter, so biodiversity is reduced."]},
        {"kind": "reveal", "title": "Weighing up deforestation",
         "cols": ["What it means"],
         "rows": [
             ("Gain: food", "Cattle and rice feed a growing human population."),
             ("Gain: fuel", "Biofuel crops replace some fossil fuel."),
             ("Cost: carbon dioxide",
              "Carbon dioxide in the atmosphere rises, which contributes to global warming."),
             ("Cost: biodiversity", "Habitats are destroyed, so species are lost."),
         ]},
        {"kind": "card", "title": "Evaluating deforestation",
         "body": ["To evaluate, give a gain, give the costs, then make a judgement using the "
                  "information you are given."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Only burning releases carbon dioxide.",
              "Decay releases it too, because microorganisms respire."),
             ("Carbon dioxide rises for one reason.",
              "Two: less is taken in by photosynthesis, and more is released by burning and decay."),
             ("Trees release oxygen that destroys carbon dioxide.",
              "Trees take carbon dioxide in by photosynthesis."),
         ]}]},
    ],
    "key_fact": "Large-scale deforestation in tropical areas has occurred to provide land for cattle "
                "and rice fields, and to grow crops for biofuels. It increases carbon dioxide in the "
                "atmosphere, because less is taken in by photosynthesis and more is released by "
                "burning and decay, and it reduces biodiversity because habitats are destroyed.",
    "deeper": [
        {"kind": "card", "title": "Species we have not studied yet",
         "body": ["Tropical forests hold a huge variety of species.",
                  "Some may be lost before we know their value, such as plants that could give new "
                  "medicines."]},
        {"kind": "card", "title": "Cattle and rice fields give off methane",
         "body": ["Cattle and rice fields both release methane.",
                  "Methane is the other gas whose rising level contributes to global warming."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say why tropical forest is cleared.",
             "<strong>Explain</strong>: say what happens and why, for example the two reasons carbon "
             "dioxide rises.",
             "<strong>Evaluate</strong>: a gain, the costs, then a judgement from the information.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # The kept Design figure has no switch any more: draw the cleared forest, the state that
            # shows photosynthesis, burning and decay together.
            ("fFig: fig(() => this.fFig(s.f))", "fFig: fig(() => this.fFig(1))"),
            # Rung 3, chain 1: the three links were parallel reasons, so any order was
            # scientifically right. Rewritten as one forced sequence (cut and burn, burning
            # releases, decay of what is left releases more). Same position, same id.
            ("'Explain how deforestation raises the level of carbon dioxide in the atmosphere. Put "
             "the links in order.'",
             "'Explain how clearing a forest by cutting and burning the trees releases carbon "
             "dioxide into the atmosphere. Put the links in order.'"),
            ("['Fewer trees means less photosynthesis, so less carbon dioxide is taken in.', 'As well "
             "as that, burning the felled trees releases carbon dioxide.', 'Then microorganisms "
             "decaying the wood left after burning respire, releasing more carbon dioxide.']",
             "['The trees are cut down and burned.', 'Burning releases the carbon stored in the wood "
             "as carbon dioxide.', 'Microorganisms then decay the wood left after burning, and their "
             "respiration releases more carbon dioxide.']"),
            # Practice set 1 (stem kept, id kept): "increases the number of decomposers" was
            # arguable (felled wood feeds decomposers). Feedback dashes removed.
            ('["Deforestation increases the number of decomposers", false]',
             '["Cattle on the cleared land take in carbon dioxide", false]'),
            ('"Cutting trees does not trap CO₂ in the soil — it means less CO₂ is taken in by '
             'photosynthesis."',
             '"Cutting trees does not trap CO₂ in the soil. It means less CO₂ is taken in by '
             'photosynthesis."'),
            ('"Decomposers feeding on felled wood RELEASE CO₂ by respiration — that adds CO₂; it does '
             'not explain why less is removed."',
             '"Cattle respire, so they give out carbon dioxide. They do not take it in."'),
            # Practice set 2 (stem kept, id kept): "Only burning releases CO₂ — decay does not"
            # contradicted the stem and had a dash tail. Feedback dashes removed.
            ('["Only burning releases CO₂ — decay does not", false]',
             '["Decay releases oxygen, not carbon dioxide", false]'),
            ('"Decay is a biological process — microorganisms carry it out; wood does not turn into '
             'CO₂ on its own."',
             '"Decay is carried out by microorganisms. Wood does not turn into CO₂ on its own."'),
            ('"Decay releases CO₂, it does not absorb it — decomposers respire."',
             '"Decay releases CO₂. It does not absorb it, because decomposers respire."'),
            ('"Decay releases CO₂ too: decomposer microorganisms respire as they break down the wood."',
             '"Decomposers respire, and respiration releases carbon dioxide, not oxygen."'),
            # Practice set 3 (stem kept): the right option was visibly the longest.
            ("[['To grow more trees', 'Clearing removes trees.'], ['To reduce carbon dioxide', "
             "'Clearing raises carbon dioxide.'], ['To protect rare species', 'Clearing destroys "
             "their habitat.']]",
             "[['To plant new forests in their place', 'Clearing removes trees.'], ['To reduce the "
             "carbon dioxide in the air', 'Clearing raises carbon dioxide.'], ['To make more space "
             "for rare species', 'Clearing destroys their habitat.']]"),
            # Practice set 4 (stem kept): the right option was visibly the longest.
            ("'The habitat of many species is destroyed, so those species are lost from the area'",
             "'The habitats of many species are destroyed'"),
            # Practice set 5 (stem kept): the right option was visibly the longest, and "lower
            # carbon dioxide" as a biofuel benefit was arguable.
            ("'Benefit: fuel to replace some fossil fuel. Cost: carbon dioxide released and habitat "
             "lost'",
             "'Benefit: fuel. Cost: habitat is lost'"),
            ("['Benefit: lower carbon dioxide. Cost: fewer cattle', 'Clearing raises carbon "
             "dioxide.']",
             "['Benefit: more habitat. Cost: less fuel', 'Clearing destroys habitat, and the crop "
             "gives fuel.']"),
            # Examiner MUST FIX r2.1: the credited option was visibly the longest.
            ("['The carbon dioxide kills them'",
             "['The carbon dioxide from burning kills the animals'"),
            # Examiner MUST FIX practice Q4: the credited option was still the longest. Distractors
            # lengthened; replies still true.
            ("['Cattle eat all the animals'",
             "['Cattle on the cleared land eat the animals'"),
            ("['Biodiversity is not affected'",
             "['Biodiversity is not affected by clearing'"),
            # Examiner NOTE r4.0: the judgement point read as the only creditable verdict. AQA credits
            # any judgement supported by the information.
            ("'Judgement: a 1% fuel saving is small against those costs, so the plan is hard to justify; a smaller area or already-cleared land would reduce the harm.'",
             "'Judgement: any reasoned judgement that weighs the 1% fuel saving against the carbon dioxide released and the loss of 800 tree species and the monkey; for example, the saving is small against those costs.'"),
        ],
    },
}
