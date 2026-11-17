# -*- coding: utf-8 -*-
"""Sampling techniques, in the lean shape. Spec table: ks4-sampling-techniques.md.

LEGACY (batch 10). The ladder, the practice set, the CFIFA examples and questions, and the two
Step 1 / Step 2 widgets stay from the Design page. The practice set is the page's own BANK (all
routes), so its fixes are logic_edits. No practice-set stem is edited; rung prompts reworded in place keep their position, so their ids survive.

The record adds one equation (EQ_POP, the legacy page's own EQ_P) so the population triangle can be
placed with `triangle:EQ_POP`. lean_ks4 then needs `return Object.assign({}, R, {` in the logic;
this batch-10 page writes `return Object.assign(c, {`, so the last logic_edit below rewrites that
line into the shape the builder expects. Behaviour is unchanged: `c` is the same object, and the
returned props are a copy of it with the page's own values on top.
"""

LOGIC_EDITS = [
    # Practice set Q4 (bluebell transect), stem kept: the credited option was visibly the longest.
    ("'Bluebells are most abundant at a medium light intensity; very low and very high light both give fewer'",
     "'Most bluebells are found at a medium light intensity'"),
    ("['Bluebells increase steadily with light', 'The count falls again at 3500 lux.']",
     "['Bluebells increase steadily as light increases', 'The count falls again at 3500 lux.']"),
    ("['Light has no effect', 'The counts change a lot along the line.']",
     "['Light intensity has no effect on bluebells', 'The counts change a lot along the line.']"),
    ("['Bluebells need shade', 'There were none at the shadiest point.']",
     "['Bluebells grow best in the deepest shade', 'There were none at the shadiest point.']"),
    # Rung 2 calc 2 (50 cm quadrat), the Convert choice: the credited choice was the only one that
    # gave the whole working. Same three choices, same index (1), same answer.
    ("['Nothing to convert', 'Convert 50 cm to 0.5 m: quadrat area 0.25 m², so 1 per quadrat is 4 per m²', 'Convert 50 cm to 5 m']",
     "['Nothing to convert', 'Convert 50 cm to 0.5 m, so the area is 0.25 m²', 'Convert 50 cm to 5 m, so the area is 25 m²']"),
    # Builder seam for the record's equation (see the docstring).
    ("return Object.assign(c, {",
     "const R = c;\n    return Object.assign({}, R, {"),
    # Blind doubt r2-2 (MED): "A 50 cm quadrat" can be misread. Say the sides, as practice Q5
    # does. Position kept (id kept).
    ("'A 50 cm quadrat gives a mean of 1 dandelion per quadrat.",
     "'A quadrat with sides of 50 cm gives a mean of 1 dandelion per quadrat."),
    # Same wording in the worked example and the CFIFA question 2 that the cfifa slot shows.
    ("head: 'A 50 cm quadrat is used.",
     "head: 'A quadrat with sides of 50 cm is used."),
    ("head: 'A 50 cm quadrat gives a mean of 2 snails per quadrat.",
     "head: 'A quadrat with sides of 50 cm gives a mean of 2 snails per quadrat."),
    # Examiner NOTE practice Q2 (why random): explanations used "specifically" and dash asides.
    # Options unchanged.
    ('"Quadrat size is fixed by the frame — it doesn\'t change with placement method."',
     '"The frame fixes the size of a quadrat. Where you place it does not change that."'),
    ('"Disturbance is minimised by careful technique — but the reason for random placement is specifically about statistical validity and avoiding bias."',
     '"Careful work keeps disturbance low. Quadrats are placed at random to avoid bias."'),
    ('"There is no legal requirement for randomness — it is a scientific requirement to ensure the sample is representative of the whole habitat."',
     '"There is no such law. Random placement makes the sample represent the whole habitat."'),
]

LESSON = {
    "slug": "sampling-techniques",
    "start": {
        "setup": "You are asked how many daisies there are on the school field.",
        "question": "If you had to guess, would you count every daisy, or count a few small "
                    "squares and scale up?",
        "options": [
            ("Count every daisy",
             "Count a few squares and scale up. There are far too many daisies to count one by "
             "one. That is sampling."),
            ("Count a few squares and scale up",
             "Count a few squares and scale up. There are far too many daisies to count one by "
             "one. That is sampling."),
        ],
        "answer": 1,
    },
    "words": ["quadrat", "transect", "abundance", "distribution"],
    "knowledge": [
        {"kind": "card", "title": "Required practical activity 7", "routes": ["CF", "CH"],
         "body": ["Measure the population size of a common species in a habitat. Use sampling "
                  "techniques to investigate the effect of a factor on the distribution of this "
                  "species."]},
        {"kind": "card", "title": "Required practical activity 9", "routes": ["TF", "TH"],
         "body": ["Measure the population size of a common species in a habitat. Use sampling "
                  "techniques to investigate the effect of a factor on the distribution of this "
                  "species."]},
        {"kind": "card", "title": "Quadrats and transects",
         "body": ["A quadrat is a square frame. You count the organisms of one species inside it.",
                  "A transect is a line across a habitat, usually a tape measure.",
                  "Ecologists use quadrats and transects to find the abundance of a species (how "
                  "many there are) and its distribution (where they are)."]},
        {"kind": "card", "title": "Estimating a population with random quadrats",
         "body": [{"points": [
             "Lay two tape measures at right angles along two edges of the area.",
             "Use a random number generator to give pairs of coordinates.",
             "Place the quadrat at each pair of coordinates. Count the plants of your species "
             "inside it.",
             "Repeat for many quadrats, at least ten.",
             "Work out the mean number per quadrat, then scale up to the whole area.",
         ]},
                  {"slot": "fig:random-quadrats"}]},
        {"kind": "card", "title": "Why random, and why many",
         "body": ["Placing quadrats at random avoids bias. If you choose where they go, you may "
                  "pick the patches with the most plants, and your estimate will be too high.",
                  "Never throw a quadrat. The thrower still chooses where it lands, and it is "
                  "unsafe.",
                  "More quadrats give a mean that better represents the whole area. One quadrat "
                  "might land on an unusual patch."]},
        {"kind": "reveal", "title": "Daisies in ten quadrats: 1, 2, 2, 2, 3, 4, 5, 6, 7, 8",
         "cols": ["How to find it", "For these counts"],
         "rows": [
             ("Mean", "Add the values and divide by how many there are", "40 ÷ 10 = 4"),
             ("Mode", "The most common value", "2"),
             ("Median", "The middle value when they are in order. With an even number of values, "
              "halfway between the two middle ones", "Halfway between 3 and 4 = 3.5"),
             ("Range", "The largest value minus the smallest", "8 − 1 = 7"),
         ]},
        {"kind": "card", "title": "Scaling up",
         "body": ["population = mean per m² × habitat area",
                  "With a 1 m² quadrat, the mean per quadrat is already the mean per m².",
                  "With any other quadrat, divide: mean per m² = mean per quadrat ÷ quadrat area.",
                  "Convert a side in centimetres to metres before you square it: 50 cm = 0.5 m, "
                  "so the area is 0.5 × 0.5 = 0.25 m².",
                  {"slot": "triangle:EQ_POP"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "From raw counts: two steps",
         "body": ["Find the mean first. Then scale up.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Distribution along a transect",
         "body": ["A transect shows how the distribution of a species changes with an abiotic "
                  "factor, such as light from a hedge out into a field.",
                  {"points": [
                      "Lay a tape measure from the hedge out into the field.",
                      "Place a quadrat at regular intervals along the tape, such as every 2 m. "
                      "Count the species in each.",
                      "Measure the abiotic factor at each quadrat, such as light intensity with a "
                      "light meter.",
                  ]},
                  {"slot": "fig:belt-transect"}]},
        {"kind": "reveal", "title": "Daisies along the transect (made-up data)",
         "cols": ["Light (lux)", "Daisies in the quadrat"],
         "rows": [
             ("0 m", "150", "0"),
             ("2 m", "400", "1"),
             ("4 m", "900", "3"),
             ("6 m", "1800", "6"),
             ("8 m", "2600", "9"),
             ("10 m", "3000", "11"),
         ]},
        {"kind": "card", "title": "Plotting the results",
         "body": ["Plot the number of daisies on the y-axis against distance, or against light "
                  "intensity, on the x-axis.",
                  "Choose scales so the points spread across most of the grid.",
                  "Here, as light intensity increases, the number of daisies increases."]},
        {"kind": "reveal", "title": "Random quadrats and transects",
         "cols": ["Use it to find"],
         "rows": [
             ("Random quadrats", "How many: the abundance of a species in an area"),
             ("A transect", "Where: how the distribution of a species changes across a habitat"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The population is the number I counted.",
              "The count is a sample. Find the mean per m², then multiply by the area."),
             ("Throw the quadrat to make it random.",
              "Use random coordinates from a random number generator."),
             ("A quadrat with sides of 50 cm has an area of 0.5 m².",
              "Square the side in metres: 0.5 × 0.5 = 0.25 m²."),
         ]}]},
    ],
    "key_fact": "Quadrats placed at random coordinates give the mean number of a species per m², "
                "and population = mean per m² × habitat area. A transect, with quadrats at regular "
                "intervals and an abiotic factor measured at each, shows how the distribution of a "
                "species changes across a habitat.",
    "deeper": [
        {"kind": "card", "title": "Two kinds of belt transect",
         "body": ["In an interrupted belt transect, the quadrats are placed at regular intervals "
                  "along the line.",
                  "In a continuous belt transect, the quadrats are placed end to end along the "
                  "whole line, with no gaps. It gives more data but takes longer."]},
        {"kind": "card", "title": "Evaluating your results",
         "body": [{"points": [
             "Decide a rule for plants on the edge of a quadrat, and keep to it.",
             "More quadrats, or repeating the transect, make the results more representative.",
             "Other factors can change along a transect too, such as moisture or trampling.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: give the method in order.",
             "<strong>Calculate</strong>: work out a mean, a median or a population and show each "
             "line.",
             "<strong>Explain</strong>: say why quadrats are placed at random, or why more "
             "quadrats help.",
             "<strong>Plot</strong>: draw the graph with sensible scales.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
    "equations": {
        "EQ_POP": {"name": "Population estimate",
                   "written": "population = mean per m² × habitat area",
                   "source": "none",
                   "top": {"s": "N", "name": "estimated population", "unit": "individuals"},
                   "bottom": [{"s": "m", "name": "mean number per m²", "unit": "per m²"},
                              {"s": "A", "name": "habitat area", "unit": "m²"}]},
    },
}
