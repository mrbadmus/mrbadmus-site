# -*- coding: utf-8 -*-
"""Variation, in the lean shape. Spec table: docs/lessons/wave2/ks3-variation-continuous-and-discontinuous.md."""
# The height bins are the lesson's own survey, referenced rather than retyped.
from ks3_data.b10.lesson_01_variation_continuous_and_discontinuous import CHARACTERISTICS as _CHARS

LESSON = {
    "slug": "variation-continuous-and-discontinuous",
    "start": {
        "setup": "Line a class up by height, and the line runs smoothly. "
                 "Sort them by blood group, and you get four separate piles.",
        "question": "If you had to guess, is the number of pets each pupil has more like height, "
                    "or more like blood group?",
        "options": [
            ("More like height",
             "More like blood group. Nobody has two and a half pets. The counts fall into separate groups."),
            ("More like blood group",
             "Right. Nobody has two and a half pets. The counts fall into separate groups."),
        ],
        "answer": 1,
    },
    "words": ["variation", "continuous variation", "discontinuous variation", "inherited"],
    "word_defs": {
        "variation": "The differences between individuals of the same species.",
        "continuous variation": "Variation where any value in a range is possible, such as height.",
        "discontinuous variation": "Variation that falls into separate groups with nothing in between, such as blood group.",
        "inherited": "Passed on from parents to their offspring in genes.",
    },
    "knowledge": [
        {"kind": "card", "title": "What variation is",
         "body": ["Variation is the differences between individuals of the same species.",
                  "No two people are exactly alike.",
                  "Variation has two main causes: the genes you inherit and your environment.",
                  "Your environment is everything around you, such as your diet and lifestyle."]},
        {"kind": "reveal", "title": "What causes variation",
         "cols": ["What it means", "Examples"],
         "rows": [
             ("Inherited", "Passed on from your parents in your genes.",
              "Blood group, natural eye colour, natural hair colour"),
             ("Environmental", "Caused by how and where you live.",
              "Scars, the language you speak, dyed hair"),
             ("Both", "Genes set a range. Your environment decides where in that range you end up.",
              "Height, body mass"),
         ]},
        {"kind": "card", "title": "Two kinds of variation",
         "body": ["Continuous variation can take any value in a range.",
                  "Height is continuous. Someone can be 151 cm, 152 cm or anything in between.",
                  "Discontinuous variation falls into separate groups, with nothing in between.",
                  "Blood group is discontinuous. You are A, B, AB or O.",
                  "Counts are discontinuous too. A flower cannot have five and a half petals.",
                  "To decide, ask whether a value can sit in between two others."]},
        {"kind": "reveal", "title": "Continuous and discontinuous variation",
         "cols": ["Continuous", "Discontinuous"],
         "rows": [
             ("Values", "Any value in a range", "Separate groups, with nothing in between"),
             ("Examples", "Height, body mass, hand span, leaf length",
              "Blood group, number of petals on a flower"),
             ("How you collect it", "Measure it, for example with a tape measure",
              "Count how many fall into each group"),
             ("Graph", "Histogram, with the bars touching", "Bar chart, with gaps between the bars"),
             ("Usual cause", "Genes and the environment together", "Genes alone"),
         ]},
        {"kind": "card", "title": "Measuring variation",
         "body": [{"points": ["Measure lots of individuals. A bigger sample shows the pattern more clearly.",
                              "Choose them at random, not just the ones that catch your eye.",
                              "Measure each one the same way, with the same instrument.",
                              "Height: a tape measure, in centimetres. Mass: scales, in kilograms.",
                              "For separate groups, count how many fall into each group. A tally chart helps."]}]},
        {"kind": "card", "title": "Histograms for continuous data",
         "body": [{"figure": "b10-height-bars-lean"},
                  "Put the measurements into equal ranges, such as 145 to 150 cm.",
                  "Draw a histogram. The bars touch, because the ranges join up.",
                  "Most people are near the middle. Few are very short or very tall."]},
        {"kind": "card", "title": "Bar charts for discontinuous data",
         "body": [{"figure": "b10-blood-group-bars"},
                  "Draw a bar chart. Leave gaps between the bars, because the groups are separate.",
                  "Nobody is partway between blood group A and blood group B."]},
        {"kind": "card", "title": "Shape and cause are separate questions",
         "body": ["Continuous variation is usually caused by genes and the environment together.",
                  "Height is strongly inherited. Diet in childhood affects it too.",
                  "Height is affected by many genes, each adding a little. That gives a smooth range.",
                  "Discontinuous variation is usually caused by genes alone.",
                  "Blood group is controlled by one gene. Nothing in your environment changes it.",
                  "So the shape of a graph alone cannot tell you the cause."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Continuous variation is caused by the environment. Discontinuous variation is genetic.",
              "Height is continuous and strongly inherited. Shape and cause are separate questions.",
              "GENE-01"),
             ("If you can put a number on it, it is continuous.",
              "Counts are numbers too. Nothing sits between two and three pets.",
              "GENE-02"),
             ("Leave gaps between the bars of a histogram.",
              "Histogram bars touch. Gaps go on a bar chart of separate groups."),
             ("Every characteristic is caused either by genes or by the environment.",
              "Many are caused by both, such as height and body mass."),
         ]}]},
    ],
    "key_fact": "Variation is caused by genes, the environment, or both. "
                "Continuous variation can take any value in a range and is shown on a histogram. "
                "Discontinuous variation falls into separate groups and is shown on a bar chart.",
    "deeper": [
        {"kind": "card", "title": "Why people have grown taller",
         "body": ["The average height of Dutch men rose by about 20 cm in 150 years.",
                  "Their genes barely changed in that time.",
                  "Better food and health care made the difference.",
                  "Within a family, tall parents still tend to have tall children.",
                  "So height depends on genes and the environment together."]},
        {"kind": "card", "title": "Plants vary too",
         "body": ["All the leaves on one tree have the same genes.",
                  "Yet leaves in the shade grow larger than leaves in full sun.",
                  "That difference is caused by the environment."]},
    ],
    "try": None,
    "tutor_body": "Want to check whether a characteristic is continuous or discontinuous?",
    "ks4_becomes": "Variation caused by genes and the environment, and how new variation arises by mutation.",
    "convention_note": "The height and blood group data on this page are made up for the lesson. They follow real patterns.",
    "figures": [
        # The lesson's b10-height-bars-touching, drawn by 'frequency-bars-lean' so the
        # last axis label clears the frame. A new id: apply() ignores a record figure
        # whose id the lesson already has.
        {"id": "b10-height-bars-lean", "kind": "diagram", "status": "drawn", "art": "frequency-bars-lean",
         "title": "A histogram of student heights, with every bar touching the next",
         "desc": "A histogram of the heights of sixty students. Seven bars stand side by side "
                 "with no gaps. The axis along the bottom is height in centimetres. It is marked "
                 "every 5 cm, from 145 up to 180. The bars count 3, 7, 13, 16, 12, 6 and 3 students. "
                 "The tallest bar is in the middle.",
         "caption": "Heights of sixty students, in 5 cm ranges.",
         "data": {"bins": _CHARS[0]["bins"], "x_label": "height", "x_unit": "cm",
                  "y_label": "number of students", "touching": True}},
        {"id": "b10-blood-group-bars", "kind": "diagram", "status": "drawn", "art": "frequency-bars",
         "title": "A bar chart of blood groups, with gaps between the bars",
         "desc": "A bar chart of the blood groups of sixty students. Four separate bars, with a gap "
                 "between each: group O 28 students, group A 25, group B 5 and group AB 2. The vertical "
                 "axis counts the number of students.",
         "caption": "Blood groups of sixty students. The bars have gaps, because the groups are separate.",
         "data": {"bins": [{"label": "O", "n": 28}, {"label": "A", "n": 25},
                           {"label": "B", "n": 5}, {"label": "AB", "n": 2}],
                  "touching": False, "x_label": "blood group", "y_label": "number of students"}},
    ],
    "figure_caption": {
        "b10-height-bars-lean": "Heights of sixty students, in 5 cm ranges.",
        "b10-blood-group-bars": None,
    },
    "ladder_stem": {
        "explain": "Blood group falls into four groups. Height forms a smooth range. Both are strongly "
                   "affected by genes. Explain the difference. Say what part the environment plays in each.",
        "produce": "Plan an investigation into variation in leaf length on one tree. Say how you would "
                   "collect the data. Say how you would present it. Say how you would make your sample fair.",
    },
    "ladder_ticks": [
        ["Says blood group is controlled by a single gene with a small number of versions.",
         "Says blood group is controlled by one gene with a few versions."],
        ["Says a single gene therefore produces a small number of distinct categories with nothing in between.",
         "Says one gene gives a few separate groups, with nothing in between."],
        ["Says height is influenced by a large number of genes, each contributing a small amount.",
         "Says height is affected by many genes, each adding a small amount."],
        ["Says many small contributions added together produce a smooth range of values.",
         "Says many small effects added together give a smooth range of values."],
        ["Says the environment — nutrition and health — affects height but has no effect at all on blood group.",
         "Says diet and health affect height, but the environment does not change blood group."],
        ["Collects a large enough sample — at least fifty leaves — and says why a small sample is not enough.",
         "Measures a large sample, such as fifty leaves. Says why a few are not enough."],
        ["Chooses the leaves without bias, rather than picking ones that look interesting or are easy to reach.",
         "Picks leaves at random from all over the tree, without choosing by eye."],
        ["Measures each leaf the same way, from the same points, with a stated precision.",
         "Measures every leaf the same way, such as tip to stalk, to the nearest millimetre."],
        ["Groups the measurements into equal ranges and plots a histogram with touching bars, because the data is continuous.",
         "Groups the lengths into equal ranges and plots a histogram with touching bars."],
        ["Predicts a hump-shaped curve, and identifies a factor that could shift it — shade, height on the tree, or age of the shoot.",
         "Predicts most leaves near the middle length, and names a factor such as shade."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Arm length can take any value in a range. It is continuous.",
            1: "Body mass can take any value, such as 45.3 kg. It is continuous.",
            3: "Leaf length can take any value in a range. It is continuous.",
        },
        "apply": {
            0: "Height is continuous and strongly inherited. Continuous does not mean environmental.",
            1: "Diet in childhood also affects height. So genes alone is wrong.",
            3: "Many genes, each adding a little, give a smooth range like height.",
        },
    },
}
