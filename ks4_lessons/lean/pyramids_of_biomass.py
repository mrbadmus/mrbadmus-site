# -*- coding: utf-8 -*-
"""Pyramids of biomass, in the lean shape. LEGACY: the live batch-10 Design page.
Spec table: ks4-pyramids-of-biomass.md (AQA 8461 4.7.4.2, biology only; the page exists on TF
and TH).

The ladder (rungs) and the practice set (BANK, written in the logic, five items, the same on TF
and TH) stay from the legacy page, so their ids survive. The practice set does NOT read the
subtopic `quiz` list, so its fixes are logic_edits. Every edit keeps the item in its place and
keeps its question text, so every id survives."""

LESSON = {
    "slug": "pyramids-of-biomass",
    "start": {
        "setup": "Thousands of caterpillars feed on one oak tree.",
        "question": "If you had to guess, which has more biomass: the oak tree, or all the "
                    "caterpillars together?",
        "options": [
            ("The oak tree",
             "The oak tree. One tree has far more mass than all the caterpillars on it, even "
             "though there are thousands of them."),
            ("All the caterpillars",
             "The oak tree. One tree has far more mass than all the caterpillars on it, even "
             "though there are thousands of them."),
        ],
        "answer": 0,
    },
    "words": ["biomass", "pyramid of biomass", "trophic level", "scale"],
    "knowledge": [
        {"kind": "card", "title": "What a pyramid of biomass shows",
         "body": ["Pyramids of biomass can be constructed to represent the relative amount of "
                  "biomass in each level of a food chain.",
                  "Each bar is one trophic level. The width of the bar shows the total biomass "
                  "at that level, for example in g/m².",
                  "Trophic level 1 is at the bottom of the pyramid."]},
        {"kind": "card", "title": "Constructing one accurately",
         "body": [{"points": [
             "1. Choose a scale so the widest bar fits the page, for example 1 cm = 40 g/m².",
             "2. Make every value the same unit as the scale. 1 kg = 1000 g.",
             "3. Work out each width: bar width = biomass ÷ scale value.",
             "4. Draw trophic level 1 at the bottom. Centre each bar on the one below.",
             "5. Label each bar with its organism, and write the scale on the drawing.",
         ]}]},
        {"kind": "card", "title": "Worked example",
         "body": ["Grass 400 g/m², grasshoppers 80 g/m², frogs 16 g/m². Scale: 1 cm = 40 g/m².",
                  {"points": [
                      "grass: 400 ÷ 40 = 10 cm",
                      "grasshoppers: 80 ÷ 40 = 2 cm",
                      "frogs: 16 ÷ 40 = 0.4 cm",
                  ]},
                  {"slot": "legacy-fig:pFig"}]},
        {"kind": "card", "title": "Converting kg to g",
         "body": ["Oak leaves 0.8 kg/m². Scale: 1 cm = 80 g/m².",
                  {"points": [
                      "Convert first: 0.8 kg/m² = 800 g/m²",
                      "bar width = 800 ÷ 80 = 10 cm",
                  ]}]},
        {"kind": "card", "title": "Why each bar is narrower",
         "body": ["Biomass is lost between trophic levels.",
                  {"points": [
                      "Not all the ingested material is absorbed. Some is egested as faeces.",
                      "Some absorbed material is lost as waste: carbon dioxide and water in "
                      "respiration, and water and urea in urine.",
                  ]},
                  "Only about 10% of the biomass from each trophic level is transferred to the "
                  "level above it. The Transfer of biomass lesson goes further."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The bar shows how many organisms there are.",
              "The bar shows the total biomass at that level."),
             ("The producers go at the top, because they come first.",
              "Trophic level 1 is at the bottom of the pyramid."),
             ("Draw each bar a bit smaller than the one below.",
              "Work out each width from the data: biomass ÷ scale value."),
             ("0.8 kg/m² with a scale of 1 cm = 80 g/m² gives 0.01 cm.",
              "Convert to 800 g/m² first. The bar is 10 cm."),
         ]}]},
    ],
    "key_fact": "A pyramid of biomass shows the relative amount of biomass at each trophic level, "
                "with trophic level 1 at the bottom. To construct one accurately, bar width = "
                "biomass ÷ scale value, after converting every value to the scale's unit.",
    "deeper": [
        {"kind": "card", "title": "Pyramids of numbers",
         "body": ["A pyramid of numbers counts the organisms at each level instead.",
                  "One oak tree with thousands of caterpillars gives a very narrow bar for the "
                  "tree under a very wide bar for the caterpillars.",
                  "A pyramid of biomass shows the oak as the widest bar, because it has the most "
                  "mass."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Construct</strong>: draw the pyramid to a scale, from the data, and label "
             "it.",
             "<strong>Calculate</strong>: work out each bar width and show each line.",
             "<strong>Explain</strong>: say why the biomass falls at each level.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Practice Q1 (question text kept, id kept): each option carried its own working
            # after a dash, so the right sum gave the answer away. Plain values now; the
            # distractors are the grass bar (500 ÷ 50) and the frog bar (5 ÷ 50).
            ('''[["1 cm — grasshopper biomass = 50 g; 50 ÷ 50 = 1 cm", true], ["10 cm — grasshopper biomass = 50 g; 50 ÷ 5 = 10 cm", false], ["5 cm — grasshopper biomass = 50 g; 50 ÷ 10 = 5 cm", false], ["50 cm — each gram = 1 cm, so 50 g = 50 cm", false]], { "1": "Scale is 1 cm = 50 g, not 1 cm = 5 g. So 50 g ÷ 50 = 1 cm, not 10 cm.", "2": "Scale is 1 cm = 50 g, not 1 cm = 10 g. So 50 ÷ 50 = 1 cm.", "3": "Scale is 1 cm = 50 g, not 1 cm = 1 g. Must divide by the scale factor." }''',
             '''[["1 cm", true], ["10 cm", false], ["0.1 cm", false], ["50 cm", false]], { "1": "10 cm is the grass bar, 500 ÷ 50. The grasshopper bar is 50 ÷ 50 = 1 cm.", "2": "0.1 cm is the frog bar, 5 ÷ 50. The grasshopper bar is 50 ÷ 50 = 1 cm.", "3": "Divide the biomass by the scale value: 50 ÷ 50 = 1 cm." }'''),
            # Practice Q4 (question text kept): "as the widest bar" is not always true of real
            # pyramids; the spec says only that trophic level 1 is at the bottom.
            ("'At the bottom, as the widest bar', [['At the top, because it comes first', "
             "'Level 1 has the most biomass and goes at the base.']",
             "'At the bottom', [['At the top, because it comes first', "
             "'Trophic level 1 is always at the bottom of the pyramid.']"),
            # Practice Q5 (question text kept): the credited option was the longest by far.
            ("'It decreases at each level, because biomass is lost as faeces, as carbon dioxide "
             "and water in respiration, and as urea and water in urine', [['It increases, "
             "because predators are bigger', 'Total mass at each level falls, whatever the size "
             "of one animal.'], ['It stays the same', 'Only about 10% is passed on.'], "
             "['It decreases because the animals are smaller', 'The loss is of biomass between "
             "levels, not animal size.']]",
             "'It decreases, as some biomass is lost at each level', [['It increases, because "
             "predators are bigger', 'Total mass at each level falls, whatever the size of one "
             "animal.'], ['It stays the same at every level', 'Only about 10% is passed on.'], "
             "['It decreases, because the animals are smaller', 'Biomass is lost between levels "
             "as faeces, in respiration and in urine. Animal size is not the reason.']]"),
            # Examiner MUST FIX r1.0 (width of each bar): the credited option was plainly the longest.
            ("['The number of organisms', 'A pyramid of biomass shows mass, not numbers.'], ['The size of one organism', 'It is the total for the level.']",
             "['The number of organisms at that level', 'A pyramid of biomass shows mass, not numbers.'], ['The mass of one organism at that level', 'It is the total for the level, not one organism.']"),
        ],
    },
}
