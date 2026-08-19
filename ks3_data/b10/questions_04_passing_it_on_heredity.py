"""B10 lesson 04 — Passing it on: heredity: twelve questions (MRB-269).

These probe the one claim the lesson is built on — inherited information comes
in separate units that keep their identity, so a version can be carried for
generations without being shown and still be passed on unchanged. The
distractors are built from the lesson's two declared misconceptions: GENE-07
(characteristics blend, so a tall parent and a short parent give a medium
child) and GENE-08 (it skipped a generation, so the version must have
disappeared and come back). Four more come from the lesson's own hook, ladder
and bench notes — that the *stronger* version is the one a parent passes on,
that a quarter white means every fourth seed is white, that a seed "takes
after" one parent rather than receiving from both, and that flower colour could
be environmental. The `harder` band takes the mechanism to a human inherited
condition, asks what a hundred purple seeds do and do not prove about the
parents, joins fertilisation to copying (the hidden version is in every cell,
not only in the gametes), and turns the whole lesson back on the one
characteristic that still looks like blending.

Every question is answerable from this lesson alone, and none of the four
mastery-ladder rungs is restated. No question carries a figure: `figures[]` is
empty on this page and measured empty (schema §11) — the bench is this lesson's
picture and it is run, not looked at.

⛔ NOTES-B10 flag 13, ruled in schema §16, binds this file exactly as it binds
the lesson: **no "allele", no "dominant", no "recessive"**, in a question, an
option or a `why`. The page's own words are used throughout — "version of a
gene", "overrides", "hidden", "carrying". And the hidden version is never
described as weaker, lost or used up except inside a distractor whose `why`
refuses it, which is GENE-08 elicited in order to be marked.
"""

UNIT = "B10"
LESSON = "passing-it-on-heredity"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-04-e01",
        "band": "easier",
        "text": "The lesson uses the word heredity for one particular thing. "
                "Which is it?",
        "options": [
            {"text": "The genetic information itself — the genes an organism "
                     "is carrying.",
             "correct": False,
             "why": "Close, but the wrong half. Heredity is the process, not "
                    "the information: what gets passed on is genes, and "
                    "heredity is the passing on of them."},
            {"text": "The passing of genetic information from parents to "
                     "their offspring.",
             "correct": True},
            {"text": "The characteristics you can see in an organism, such as "
                     "the colour of its flowers.",
             "correct": False,
             "why": "Those are what the information produces. Two purple "
                    "plants can be carrying different versions and still look "
                    "exactly the same."},
            {"text": "The changes an organism goes through during its own "
                     "lifetime.",
             "correct": False,
             "why": "Heredity happens between generations, not within one. "
                    "Nothing you pick up during your own life is put into a "
                    "gamete."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e02",
        "band": "easier",
        "text": "Each pea plant carries two copies of the flower-colour gene. "
                "How many of them does it put into one seed?",
        "options": [
            {"text": "Both of them, so the seed ends up with four copies "
                     "altogether.",
             "correct": False,
             "why": "Then the number would double every generation. Each "
                    "parent passes one, so the seed has two — one from each "
                    "side."},
            {"text": "Whichever of the two is the stronger version.",
             "correct": False,
             "why": "Nothing is decided by strength. Which version goes into "
                    "a gamete is pure chance; P only overrides p once the two "
                    "are together inside a plant."},
            {"text": "Neither. The seed builds its own version from scratch.",
             "correct": False,
             "why": "Nothing is built from scratch. A seed can only ever "
                    "receive versions that were already in its two parents."},
            {"text": "One of the two, chosen by chance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e03",
        "band": "easier",
        "text": "On the bench you set both parent plants to pp and grow a "
                "hundred seeds. What comes up?",
        "options": [
            {"text": "About a quarter of them white, as in Mendel's cross.",
             "correct": False,
             "why": "A quarter white needs both parents to be carrying P as "
                    "well as p. There is no P anywhere in this cross to pass "
                    "on."},
            {"text": "All purple — a pp plant still carries a hidden purple "
                     "version.",
             "correct": False,
             "why": "There is nothing hidden in a pp plant. It has p twice, "
                    "and p is what shows when there is no P there to override "
                    "it."},
            {"text": "Every one white, because there is no P anywhere in this "
                     "cross.",
             "correct": True},
            {"text": "Half purple and half white, because each seed takes "
                     "after one parent.",
             "correct": False,
             "why": "A seed takes a version from both parents, never after "
                    "one of them. With only p available on both sides, every "
                    "seed gets p twice."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e04",
        "band": "easier",
        "text": "At which moment is a new plant's combination of gene "
                "versions fixed?",
        "options": [
            {"text": "When two gametes fuse and the full number of "
                     "chromosomes is back.",
             "correct": True},
            {"text": "When the seed germinates and the young plant begins to "
                     "grow.",
             "correct": False,
             "why": "Growth only copies what is already there. The "
                    "combination was settled the moment the two gametes "
                    "fused."},
            {"text": "Every time a cell divides, because a new mixture is "
                     "made each time.",
             "correct": False,
             "why": "Cell division copies the DNA exactly — it never "
                    "reshuffles it. Every cell of the plant carries the same "
                    "combination the fertilised egg had."},
            {"text": "When the plant flowers and the colour of the petals "
                     "appears.",
             "correct": False,
             "why": "The colour only displays what was fixed at "
                    "fertilisation. Showing a characteristic and receiving it "
                    "are two different moments."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-04-s01",
        "band": "standard",
        "text": "A student sets both parents to Pp, presses \"Grow one seed\" "
                "once, and gets a white plant. She says the bench must be "
                "broken. What is the best reply?",
        "options": [
            {"text": "The parents cannot both have been Pp, or the first seed "
                     "would be purple.",
             "correct": False,
             "why": "Pp × Pp can give white on the very first press. Roughly a "
                    "quarter of the seeds are white, and nothing stops the "
                    "first one being one of them."},
            {"text": "Nothing is broken. Chance decides each seed, so one "
                     "seed shows no proportion.",
             "correct": True},
            {"text": "A quarter white means every fourth seed is white, so "
                     "she counted wrong.",
             "correct": False,
             "why": "The seeds do not take turns. Each one has its own "
                    "one-in-four chance, so white can come first, twice "
                    "running, or not at all in ten."},
            {"text": "White seeds only start appearing once twenty seeds have "
                     "been grown.",
             "correct": False,
             "why": "Twenty seeds is where a proportion becomes readable, not "
                    "where white becomes possible. Any single seed can come "
                    "out white."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s02",
        "band": "standard",
        "text": "One parent plant is PP and the other is pp. Predict what the "
                "seeds from that cross will be like.",
        "options": [
            {"text": "A medium shade, halfway between the purple parent and "
                     "the white one.",
             "correct": False,
             "why": "Nothing blends. Each seed receives a whole P and a whole "
                    "p, and P overrides p, so the flowers are ordinary "
                    "purple."},
            {"text": "Half purple and half white, since one parent gives "
                     "each.",
             "correct": False,
             "why": "Every seed receives one version from each parent, not a "
                    "whole plant's worth from one of them. Every seed here is "
                    "Pp, so every seed is purple."},
            {"text": "All purple, and every single one of them carrying p.",
             "correct": True},
            {"text": "All purple, and none of them carrying p at all.",
             "correct": False,
             "why": "The p has to go somewhere. The pp parent has nothing "
                    "else to pass on, so every seed receives a p and carries "
                    "it hidden."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s03",
        "band": "standard",
        "text": "Two groups each grow a hundred seeds from Pp × Pp. One reads "
                "2.85 : 1, the other 3.35 : 1, and neither gets 3.00 : 1. "
                "What should they conclude?",
        "options": [
            {"text": "One of the groups must have miscounted its purple "
                     "plants.",
             "correct": False,
             "why": "Both counts can be right. Two runs of a hundred seeds "
                    "give two different numbers, and neither of them is a "
                    "mistake."},
            {"text": "The 3:1 result only holds for pea plants grown by "
                     "Mendel himself.",
             "correct": False,
             "why": "The expectation holds for any cross of this kind. What "
                    "varies from run to run is the sample, not the rule "
                    "underneath it."},
            {"text": "They should keep growing seeds until the ratio reads "
                     "exactly 3.00 : 1.",
             "correct": False,
             "why": "It essentially never will. A bigger sample sits closer "
                    "to 3:1, but chance keeps the exact figure moving either "
                    "side of three."},
            {"text": "Both are normal — a 3:1 ratio only emerges over large "
                     "numbers.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s04",
        "band": "standard",
        "text": "Two seeds from the same two parent plants grow into plants "
                "of different colours. How is that possible?",
        "options": [
            {"text": "Each gamete carries one version of the gene, and chance "
                     "decides which.",
             "correct": True},
            {"text": "One seed received more of its parents' genes than the "
                     "other one did.",
             "correct": False,
             "why": "Every seed receives exactly the same amount — one "
                    "version of every gene from each parent. What differs is "
                    "which versions."},
            {"text": "The parent plants changed between making the first seed "
                     "and the second.",
             "correct": False,
             "why": "The parents' own versions never change. What changes "
                    "from seed to seed is which of the two each gamete "
                    "happens to carry."},
            {"text": "The two seeds landed in different soil, and soil sets "
                     "the flower colour.",
             "correct": False,
             "why": "Flower colour here is set by the versions the seed "
                    "received. Soil would not produce a proportion as clean "
                    "as a quarter."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-04-h01",
        "band": "harder",
        "text": "Two parents who do not have an inherited condition, and who "
                "know of nobody in either family who has it, have a child who "
                "does. What is the most likely explanation?",
        "options": [
            {"text": "The condition began as a brand-new change in the child "
                     "alone.",
             "correct": False,
             "why": "That would be a rare event, and it leaves both parents "
                    "out of the story. The far commoner route is that each "
                    "was carrying the version and neither showed it."},
            {"text": "Both parents carried the version hidden, and the child "
                     "received it from both.",
             "correct": True},
            {"text": "The version came down from a grandparent and grew "
                     "stronger by the time it reached the child.",
             "correct": False,
             "why": "Versions do not gather strength as they travel. It was "
                    "passed on unchanged; what changed is that the child "
                    "received it twice, with nothing to override it."},
            {"text": "One parent must have a mild form of the condition "
                     "without realising it.",
             "correct": False,
             "why": "Someone carrying one such version and one that overrides "
                    "it does not have a mild form — they show nothing at all. "
                    "Carrying and showing are different things."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h02",
        "band": "harder",
        "text": "A grower crosses two purple pea plants and all hundred of "
                "the seeds grow into purple plants. What can he safely say "
                "about the parents?",
        "options": [
            {"text": "Both parents must carry two P versions, since no white "
                     "appeared.",
             "correct": False,
             "why": "One PP parent is enough — PP × Pp gives all purple as "
                    "well. He cannot tell which of the two cases he has by "
                    "looking at them."},
            {"text": "Neither parent carries p, because a hidden version "
                     "always shows up eventually.",
             "correct": False,
             "why": "A hidden version shows only when a seed receives it "
                    "twice. Against a PP parent that can never happen, "
                    "however many seeds are grown."},
            {"text": "At least one of them has two P versions to pass on.",
             "correct": True},
            {"text": "Both parents are Pp, and a hundred seeds is too few to "
                     "show white.",
             "correct": False,
             "why": "A hundred seeds from Pp × Pp gives roughly twenty-five "
                    "white ones. Getting none at all that way would be "
                    "extraordinary."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h03",
        "band": "harder",
        "text": "A purple pea plant carries a p version that never shows "
                "anywhere on it. Where in the plant is that p version?",
        "options": [
            {"text": "Only in its gametes, since that is the one place it "
                     "gets passed on from.",
             "correct": False,
             "why": "Gametes are made from body cells that already carry it. "
                    "The p was in the plant long before any gamete of its own "
                    "existed."},
            {"text": "Only in the flowers, where the colour of the plant is "
                     "decided.",
             "correct": False,
             "why": "The flowers only display the result. The instruction is "
                    "in the DNA, and every cell of the plant holds the same "
                    "DNA as every other."},
            {"text": "Only in cells where it has been switched on and is "
                     "being used.",
             "correct": False,
             "why": "It is switched on nowhere in this plant — that is what "
                    "hidden means — and it is there all the same. Unused is "
                    "not the same as absent."},
            {"text": "In every cell — each one is a copy of the fertilised "
                     "egg.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h04",
        "band": "harder",
        "text": "Human height does not come in two clean forms — people range "
                "smoothly from short to tall. Does that show that some "
                "characteristics really do blend?",
        "options": [
            {"text": "No — hundreds of genes are involved, and each one is "
                     "still passed on whole.",
             "correct": True},
            {"text": "Yes — height is the one characteristic that is passed "
                     "on as a mixture.",
             "correct": False,
             "why": "Nothing is passed on as a mixture. If characteristics "
                    "blended, variation would halve every generation and a "
                    "classroom would look identical — it does not."},
            {"text": "Yes, because a child's height usually lands between its "
                     "two parents' heights.",
             "correct": False,
             "why": "Landing in between is what many separate genes adding up "
                    "looks like. Every one of those genes is still passed on "
                    "unchanged."},
            {"text": "No — height is set entirely by diet, so no genes are "
                     "involved at all.",
             "correct": False,
             "why": "Diet does affect height, but height is inherited too. "
                    "The smooth range comes from many genes at once, not from "
                    "the absence of genes."},
        ],
        "figure": None,
    },
]
