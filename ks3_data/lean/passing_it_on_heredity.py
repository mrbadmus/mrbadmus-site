# -*- coding: utf-8 -*-
"""Passing it on: heredity, in the lean shape. Spec table: docs/lessons/wave2/ks3-passing-it-on-heredity.md.

The Rainford scheme (14b, 15c) asks for dominant and recessive characteristics and for the
probability of inheriting one. The old page taught neither; both are new teaching here.
"""

LESSON = {
    "slug": "passing-it-on-heredity",
    "start": {
        "setup": "Cross tall pea plants with short ones, and all the offspring are tall. "
                 "Breed those tall offspring together, and some short plants come back.",
        "question": "If you had to guess, what happened to the shortness while every plant grew tall?",
        "options": [
            ("Hidden, but still there",
             "Yes. The version for short was carried, unchanged, by plants that looked tall."),
            ("Mixed in and watered down",
             "It came back at full strength, so it was never watered down. It was hidden."),
        ],
        "answer": 0,
    },
    "words": ["heredity", "gamete", "dominant", "recessive"],
    "word_defs": {
        "heredity": "The passing of genetic information from parents to their offspring.",
        "gamete": "A sex cell, such as a sperm or an egg. It has half the chromosomes.",
        "dominant": "A version of a gene that shows even when only one copy is present.",
        "recessive": "A version of a gene that shows only when both copies are that version.",
    },
    "knowledge": [
        {"kind": "card", "title": "Heredity",
         "body": ["Heredity is how genetic information passes from one generation to the next.",
                  "You get half your chromosomes from your mother and half from your father.",
                  "That is why children share features with both parents."]},
        {"kind": "card", "title": "From parents to child",
         "body": [{"points": ["Each human body cell has 46 chromosomes, in 23 pairs.",
                              "A sperm or an egg gets one chromosome from each pair: 23 in all.",
                              "At fertilisation, a sperm from the father joins an egg from the mother.",
                              "The fertilised egg has 46 chromosomes again, half from each parent.",
                              "It divides many times. Every new cell gets a copy of the same DNA."]},
                  "Which chromosome of each pair goes into a gamete is down to chance.",
                  "So brothers and sisters get different mixes from the same parents."]},
        {"kind": "card", "title": "Two versions of each gene",
         "body": ["You have two copies of most genes, one from each parent.",
                  "The two copies can be different versions of the gene.",
                  "A pea plant's flower colour gene has a purple version and a white version.",
                  "We write the purple version as P and the white version as p."]},
        {"kind": "card", "title": "Dominant and recessive",
         "body": ["A dominant version shows even when only one copy is present.",
                  "A recessive version only shows when both copies are recessive.",
                  "In pea plants, purple (P) is dominant. White (p) is recessive.",
                  "A dominant version is written with a capital letter. A recessive one is lower case."]},
        {"kind": "reveal", "title": "Which flower colour shows",
         "cols": ["Flower colour", "Why"],
         "rows": [
             ("PP", "Purple", "Two copies of the dominant version."),
             ("Pp", "Purple", "One P is enough to show purple. The p is hidden."),
             ("pp", "White", "Both copies are recessive, so there is no P to hide them."),
         ]},
        {"kind": "card", "title": "Hidden, but still there",
         "body": ["A Pp plant looks purple, but it carries p.",
                  "It can pass p on to its offspring.",
                  "You cannot tell a PP plant from a Pp plant by looking.",
                  "Two Pp plants can each pass on p. That offspring is pp, so it is white.",
                  "So a characteristic can skip a generation. The recessive version was carried all along.",
                  "Versions of a gene are passed on whole. They never blend together."]},
        {"kind": "card", "title": "Punnett squares",
         "body": ["A Punnett square shows every way two parents can pass on their versions.",
                  "Write one parent's two versions along the top. Write the other parent's down the side.",
                  "Each square gets one letter from the top and one from the side.",
                  "Each of the four squares is an equally likely outcome."]},
        {"kind": "card", "title": "Worked example: two Pp parents",
         "body": ["Two purple pea plants are both Pp. Find the probability that an offspring is white.",
                  {"figure": "b10-punnett-pp"},
                  {"points": ["Convert: write each parent as letters. Both are Pp, so each passes on P or p.",
                              "Formula: probability = squares with that result ÷ total squares",
                              "Insert: 1 square is pp, which is white. There are 4 squares. So 1 ÷ 4.",
                              "Fine-tune: 1 ÷ 4 = 0.25 = 25%",
                              "Answer: a 1/4 chance, which is 25%, or 1 in 4"]},
                  "The other 3 squares are purple. That is a 3/4 chance, or 75%."]},
        {"kind": "card", "title": "Worked example: Pp and pp",
         "body": ["A purple Pp plant is crossed with a white plant. Find the probability that an offspring is white.",
                  {"figure": "b10-punnett-pp-pp"},
                  {"points": ["Convert: white is recessive, so the white parent must be pp.",
                              "Formula: probability = squares with that result ÷ total squares",
                              "Insert: 2 squares are pp, which is white. There are 4 squares. So 2 ÷ 4.",
                              "Fine-tune: 2 ÷ 4 = 1/2 = 0.5 = 50%",
                              "Answer: a 1/2 chance, which is 50%, or 1 in 2"]}]},
        {"kind": "card", "title": "Chance for each offspring",
         "body": ["A probability is the chance for each offspring. It is not a promise.",
                  "Each seed is a new chance, like a new roll of a dice.",
                  "In a small batch of seeds, the numbers can be far from 3 to 1.",
                  "With hundreds of seeds, the results come close to 3 to 1."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Characteristics blend. A tall and a short pea plant give medium plants.",
              "Their offspring are all tall, not medium. Versions of a gene do not mix.", "GENE-07"),
             ("It skipped a generation, so the gene disappeared and came back.",
              "The recessive version was carried, hidden, all along.", "GENE-08"),
             ("A 1 in 4 chance means exactly one in every four offspring.",
              "It is the chance for each offspring. A small family can differ."),
             ("Dominant means more common.",
              "Dominant means it shows when only one copy is present."),
         ]}]},
    ],
    "key_fact": "Heredity is the passing of genetic information from parents to offspring. "
                "Each parent passes on one version of each gene. "
                "A dominant version shows with one copy. A recessive version only shows with two copies.",
    "deeper": [
        {"kind": "card", "title": "The word allele",
         "body": ["Scientists call a version of a gene an allele.",
                  "At GCSE you will use it, with Punnett squares like the ones here."]},
        {"kind": "card", "title": "Gregor Mendel",
         "body": ["Gregor Mendel was a monk who bred pea plants in the 1850s and 1860s.",
                  "He counted the offspring of each cross. He found ratios close to 3 to 1.",
                  "He published in 1866. His work was ignored until 1900."]},
    ],
    "try": None,
    "tutor_body": "Want to work out the chances for a cross of your own?",
    "ks4_becomes": "Alleles, genotype and phenotype, Punnett squares, and inherited disorders.",
    "figures": [
        {"id": "b10-punnett-pp-pp", "kind": "diagram", "status": "drawn", "art": "b10-punnett-cross",
         "title": "A Punnett square for a Pp plant crossed with a pp plant",
         "desc": "Parent 1, Pp and purple, is written across the top. Its two versions, P and p, head the "
                 "two columns. Parent 2, pp and white, is written down the side. Its two versions, p and p, "
                 "head the two rows. The four squares read Pp, pp, Pp and pp. The two Pp squares have a filled "
                 "flower and say purple. The two pp squares are shaded, with an open flower, and say white. "
                 "Under the grid: white, 2 of the 4 squares; 2/4 = 1/2 = 50% = 1 in 2.",
         "caption": "Two of the four squares are pp, so the chance of white is 1 in 2.",
         "data": {"parent1": "Pp", "parent2": "pp", "dominant": "purple", "recessive": "white",
                  "find": "recessive"}},
    ],
    "figure_caption": {
        "b10-punnett-pp": "Two Pp parents. Three squares are purple and one is white.",
        "b10-punnett-pp-pp": None,
    },
    "ladder_stem": {
        "explain": "A characteristic shows in a grandparent. It is missing in the parents. It shows again "
                   "in a grandchild. Explain how, using versions of genes and how gametes are made.",
        "produce": "A dog breeder wants white puppies. White is the recessive version of the coat colour gene. "
                   "Her two coloured dogs have each had a white puppy before. Explain what she can predict "
                   "and what she cannot. Explain why breeding for a recessive characteristic is easier than "
                   "breeding one out.",
    },
    "ladder_ticks": [
        ["Says one version can override the other, so an individual can carry a version without showing it.",
         "Says a dominant version hides a recessive one, so it can be carried unseen."],
        ["Says the grandchild received that version from both parents, so there was nothing to override it.",
         "Says the grandchild got the recessive version from both parents."],
        ["Makes clear the version was never lost or recreated — it was carried the whole time.",
         "Makes clear the version was never lost. It was carried the whole time."],
        ["Says she cannot predict any individual puppy — which version each gamete carries is chance.",
         "Says she cannot predict any one puppy, as each gamete's version is chance."],
        ["Says a small litter may not show the ratio at all, so the prediction is about large numbers.",
         "Says a small litter may not show the ratio. It works over large numbers."],
        ["Explains that a white dog must carry two white versions and so breeds true, while a coloured dog may or may not be carrying white and cannot be identified by looking.",
         "Says a white dog must have two white versions. A coloured dog may hide one."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Then a fertilised egg would have 92. Gametes carry half the chromosomes.",
            1: "Chromosomes are passed on whole. The sperm gets one from each pair.",
            2: "The number is halved in a gamete, not doubled.",
        },
        "apply": {
            0: "A new change is far too rare to explain a quarter. Both parents carried white.",
            1: "Nothing blended. The white version was passed on unchanged.",
            2: "One in four is the pattern of two parents carrying a hidden version.",
        },
    },
}
