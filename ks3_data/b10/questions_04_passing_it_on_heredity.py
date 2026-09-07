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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-04-e05",
        "band": "easier",
        "text": "Which of these describes a gamete?",
        "options": [
            {"text": "A fertilised egg, carrying a full set of chromosomes "
                     "with half from each of its parents.",
             "correct": False,
             "why": "That is what two gametes make between them. A gamete is "
                    "one of the two cells that fuse, and it carries half a "
                    "set."},
            {"text": "Any cell that is about to divide into two new cells of "
                     "the same kind.",
             "correct": False,
             "why": "Ordinary body cells divide all the time and are not "
                    "gametes. A gamete is a sex cell, made specially with half "
                    "a set of chromosomes."},
            {"text": "A version of a gene, such as the one for white flowers "
                     "rather than purple.",
             "correct": False,
             "why": "A version is part of the information. A gamete is a whole "
                    "cell that carries the information from one parent."},
            {"text": "A sex cell — a sperm, an egg or a pollen grain — with "
                     "one chromosome from every pair.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e06",
        "band": "easier",
        "text": "What happens at fertilisation?",
        "options": [
            {"text": "A seed takes in water and starts to grow into a young "
                     "plant.",
             "correct": False,
             "why": "That is germination, and it happens later. Fertilisation "
                    "is the moment two gametes fuse and the new combination is "
                    "fixed."},
            {"text": "Two gametes fuse, so the offspring has a full set of "
                     "chromosomes again, half from each parent.",
             "correct": True},
            {"text": "A parent's chromosomes are halved so that a gamete can "
                     "be made.",
             "correct": False,
             "why": "That is what happens before fertilisation, when the "
                    "gametes are made. Fertilisation is the joining that puts "
                    "the number back."},
            {"text": "The versions of a gene from the two parents blend into a "
                     "single new version.",
             "correct": False,
             "why": "Nothing blends. The two versions arrive whole, sit side "
                    "by side, and can be passed on separately for "
                    "generations."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e07",
        "band": "easier",
        "text": "In a cross, what does the word offspring refer to?",
        "options": [
            {"text": "The new organisms produced by a pair of parents.",
             "correct": True},
            {"text": "The characteristics an organism passes on to the next "
                     "generation.",
             "correct": False,
             "why": "Those are what is passed on. The offspring are the new "
                    "organisms that receive them."},
            {"text": "The gametes a parent makes before fertilisation.",
             "correct": False,
             "why": "A gamete is a cell, and two of them are needed. The "
                    "offspring is the organism that grows from the pair once "
                    "they have fused."},
            {"text": "Only the offspring that survive to become adults "
                     "themselves.",
             "correct": False,
             "why": "All of them count, whether they survive or not. Surviving "
                    "is a separate question from being offspring."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e08",
        "band": "easier",
        "text": "A pea plant is described as pure-breeding for flower colour. "
                "What does that mean?",
        "options": [
            {"text": "It has never been crossed with a plant of a different "
                     "colour.",
             "correct": False,
             "why": "Its own history is not what the word describes. "
                    "Pure-breeding is about the two versions the plant is "
                    "carrying right now."},
            {"text": "Its flowers are a stronger colour than an ordinary "
                     "plant's.",
             "correct": False,
             "why": "The shade of the flower has nothing to do with it. "
                    "Pure-breeding means the two versions it carries are "
                    "identical."},
            {"text": "It carries two identical versions of the gene, so every "
                     "offspring receives the same one.",
             "correct": True},
            {"text": "It always produces offspring that look exactly like both "
                     "of its parents.",
             "correct": False,
             "why": "What the offspring look like also depends on the other "
                    "parent. A pure-breeding white plant crossed with a "
                    "pure-breeding purple one gives purple offspring."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e09",
        "band": "easier",
        "text": "In the pea cross, flower colour is written with a capital P "
                "and a small p. What does the capital letter stand for?",
        "options": [
            {"text": "The version that came from the plant's mother rather "
                     "than its father.",
             "correct": False,
             "why": "Either version can arrive from either parent. The letters "
                    "say nothing about which parent supplied them."},
            {"text": "The version a pure-breeding plant carries, as opposed to "
                     "a mixed one.",
             "correct": False,
             "why": "A pure-breeding plant may carry two P versions or two p "
                    "versions. What the capital marks is the version that "
                    "shows."},
            {"text": "The version that is present in larger amounts inside the "
                     "cell.",
             "correct": False,
             "why": "There is one copy of each, sitting on the two "
                    "chromosomes of a pair. Amount is not what the capital is "
                    "recording."},
            {"text": "The version that shows — a plant with at least one P is "
                     "purple.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e10",
        "band": "easier",
        "text": "A pea plant has white flowers. Which pair of versions must "
                "it be carrying?",
        "options": [
            {"text": "PP",
             "correct": False,
             "why": "A plant carrying P shows purple. Two of them makes purple "
                    "doubly certain, not white."},
            {"text": "pp",
             "correct": True},
            {"text": "Pp",
             "correct": False,
             "why": "A Pp plant is purple. The one P is enough to show, which "
                    "is why a p version can be carried without being seen."},
            {"text": "It could be pp or Pp — you cannot tell from the flower.",
             "correct": False,
             "why": "That is true the other way round: a purple plant may be "
                    "PP or Pp. A white plant has nothing hidden, because a "
                    "single P would have shown."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-04-s05",
        "band": "standard",
        "text": "A Pp pea plant is crossed with a pp plant. About what "
                "proportion of the seeds would be expected to grow into white "
                "plants?",
        "options": [
            {"text": "None of them — one parent carries P, so every seed gets "
                     "one.",
             "correct": False,
             "why": "The Pp parent passes P into half its gametes and p into "
                    "the other half. Only half the seeds receive the P."},
            {"text": "About a quarter of them.",
             "correct": False,
             "why": "A quarter is what two Pp parents give. Here one parent "
                    "can only ever pass p, which raises the white share to a "
                    "half."},
            {"text": "About half of them.",
             "correct": True},
            {"text": "All of them — a plant crossed with a white plant gives "
                     "white offspring.",
             "correct": False,
             "why": "The Pp parent passes P to half its seeds, and one P is "
                    "enough to show. Those seeds grow into purple plants."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s06",
        "band": "standard",
        "text": "Both parents are Pp. Each passes one of its two versions "
                "into each seed. Why does about three quarters of the crop "
                "come out purple rather than about half?",
        "options": [
            {"text": "There are four ways the two versions can land, and three "
                     "of them include at least one P.",
             "correct": True},
            {"text": "P is passed on more often than p, because it is the "
                     "version that shows.",
             "correct": False,
             "why": "Each parent passes P and p equally often — one of the two "
                    "copies, chosen by chance. What is uneven is how many of "
                    "the four combinations end up purple."},
            {"text": "Three of the four seeds receive P from the first parent.",
             "correct": False,
             "why": "Half receive P from the first parent, and half receive it "
                    "from the second. The three quarters comes from combining "
                    "the two parents, not from one of them."},
            {"text": "The purple plants grow faster, so more of them survive "
                     "to be counted.",
             "correct": False,
             "why": "Nothing is being weeded out. The proportion is set at "
                    "fertilisation by which versions each seed happened to "
                    "receive."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s07",
        "band": "standard",
        "text": "A grower grows only his white-flowered pea plants together, "
                "lets them pollinate each other, and sows the seed. What "
                "colour are the plants that come up?",
        "options": [
            {"text": "About a quarter purple, because purple can reappear from "
                     "white parents.",
             "correct": False,
             "why": "Reappearing works the other way round. A hidden version "
                    "can only be hidden behind a P, and these plants have no "
                    "P to hide it behind."},
            {"text": "About three quarters white and a quarter purple.",
             "correct": False,
             "why": "That ratio comes from two Pp parents. Every one of these "
                    "parents is pp, so there is no P anywhere in the cross."},
            {"text": "All purple, because two white plants together produce "
                     "the version they lack.",
             "correct": False,
             "why": "Nothing is produced that was not there. A version has to "
                    "arrive from a parent, and neither parent has a P to "
                    "send."},
            {"text": "All white, because each parent has two p versions and "
                     "can pass nothing else.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s08",
        "band": "standard",
        "text": "Children usually resemble both of their parents without "
                "being identical to either. What explains that?",
        "options": [
            {"text": "The parents' characteristics are mixed together at "
                     "fertilisation, giving something between the two.",
             "correct": False,
             "why": "Nothing is mixed. Each version arrives whole, which is "
                    "why a characteristic can vanish for a generation and come "
                    "back unchanged."},
            {"text": "Each parent passes one of every pair, so the child gets "
                     "a combination neither parent had.",
             "correct": True},
            {"text": "The child receives most of its genes from one parent and "
                     "a few from the other.",
             "correct": False,
             "why": "The split is even — 23 chromosomes from each. What varies "
                    "is which member of each pair was sent, not how many."},
            {"text": "The child's genes change as it grows, drifting away from "
                     "both parents.",
             "correct": False,
             "why": "The combination is fixed at fertilisation, and every cell "
                    "afterwards is a copy of it. Growing up does not rewrite "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s09",
        "band": "standard",
        "text": "Every cell of a pea plant carries two versions of the "
                "flower-colour gene. Why does the plant put only one of them "
                "into each pollen grain?",
        "options": [
            {"text": "Because a pollen grain is too small to carry both.",
             "correct": False,
             "why": "Size is not the reason — a pollen grain carries a full "
                    "single set of chromosomes, which is a great deal. It "
                    "carries one of each pair so that fertilisation can "
                    "restore the pair."},
            {"text": "Because the second version is kept back in case the "
                     "first one is not needed.",
             "correct": False,
             "why": "Nothing is held in reserve. The two copies are shared out "
                    "between gametes, and which one a particular grain "
                    "receives is chance."},
            {"text": "Because the grain must carry half a set, so that fusing "
                     "with an ovule restores the full number.",
             "correct": True},
            {"text": "Because only the version the plant is showing can be "
                     "passed on.",
             "correct": False,
             "why": "A purple plant passes p just as readily as P. That is "
                    "exactly how a hidden version travels to the next "
                    "generation."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s10",
        "band": "standard",
        "text": "A pea plant carries two versions of the flower-colour gene. "
                "Where did those two versions come from?",
        "options": [
            {"text": "One arrived from each parent, in the two gametes that "
                     "fused.",
             "correct": True},
            {"text": "Both arrived from the parent whose flower colour the "
                     "plant shows.",
             "correct": False,
             "why": "Which colour shows does not decide where the versions "
                    "came from. One arrived from each parent, whichever of the "
                    "two is on display."},
            {"text": "One arrived from a parent and the plant made the second "
                     "itself as it grew.",
             "correct": False,
             "why": "A plant makes no new versions. The pair was complete at "
                    "fertilisation, and every cell since is a copy of that "
                    "first one."},
            {"text": "Both arrived from the pollen grain, since the ovule "
                     "carries no genes.",
             "correct": False,
             "why": "The ovule carries a full single set, exactly as the "
                    "pollen grain does. Half of everything the plant has came "
                    "from it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-04-h05",
        "band": "harder",
        "text": "A grower has a purple-flowered pea plant and needs to know "
                "whether it is carrying p. Which cross would settle it, and "
                "what would he look for?",
        "options": [
            {"text": "Cross it with a PP plant, and look for white offspring.",
             "correct": False,
             "why": "A PP parent sends P into every seed, so every plant comes "
                    "up purple whichever versions the unknown plant carries. "
                    "The cross can never tell him anything."},
            {"text": "Cross it with a white plant, and look for any white "
                     "offspring.",
             "correct": True},
            {"text": "Grow it in poorer soil, and look for the flowers to "
                     "fade.",
             "correct": False,
             "why": "Flower colour here is set by the versions the plant "
                    "received, not by its conditions. Starving the plant tells "
                    "him nothing about what it is carrying."},
            {"text": "Count the flowers on it, since a plant carrying p "
                     "produces fewer.",
             "correct": False,
             "why": "A carried version has no effect at all until it is passed "
                    "on and meets another p. Nothing about the plant itself "
                    "gives it away."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h06",
        "band": "harder",
        "text": "Two Pp plants are crossed and 480 seeds are grown. Of the "
                "480 plants, 96 have white flowers. What percentage of the "
                "crop is white?",
        "options": [
            {"text": "5 per cent",
             "correct": False,
             "why": "That is 480 divided by 96, which is the division the "
                    "wrong way round. A percentage is the part divided by the "
                    "total, then multiplied by 100."},
            {"text": "25 per cent",
             "correct": False,
             "why": "That is what you would expect, not what was counted. The "
                    "question asks what this crop actually gave, and 96 out of "
                    "480 is a little under a quarter."},
            {"text": "80 per cent",
             "correct": False,
             "why": "That is the purple share — the other 384 plants. It is "
                    "the right calculation done on the wrong group."},
            {"text": "20 per cent",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h07",
        "band": "harder",
        "text": "In one of Mendel's experiments on seed colour, 8,023 seeds "
                "came up as 6,022 yellow and 2,001 green. What ratio is that "
                "closest to, and what should be said about it?",
        "options": [
            {"text": "About 1 to 3, counting the green seeds against the "
                     "yellow.",
             "correct": False,
             "why": "The ratio is written the wrong way round. There are three "
                    "times as many yellow as green, so it reads 3 to 1."},
            {"text": "About 2 to 1, because the gene comes in two versions.",
             "correct": False,
             "why": "Two versions does not give two to one. There are four "
                    "ways the two versions can land, and three of the four "
                    "show yellow."},
            {"text": "About 3 to 1, which is what carrying a version without "
                     "showing it predicts.",
             "correct": True},
            {"text": "Exactly 3 to 1 — Mendel grew enough seeds to take chance "
                     "out of it altogether.",
             "correct": False,
             "why": "6,022 to 2,001 is 3.01 to 1, not exactly 3. Large numbers "
                    "bring a ratio close to the expected one; they never "
                    "remove chance."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h08",
        "band": "harder",
        "text": "A body cell of a pea plant has 14 chromosomes. How many are "
                "in one pollen grain, and how many in the first cell of a "
                "seed it fertilises?",
        "options": [
            {"text": "7 in the pollen grain and 14 in the seed's first cell.",
             "correct": True},
            {"text": "14 in the pollen grain and 28 in the seed's first cell.",
             "correct": False,
             "why": "Then the number would double every generation — 28, then "
                    "56, then 112. Gametes carry half a set precisely so that "
                    "it does not."},
            {"text": "7 in the pollen grain and 7 in the seed's first cell.",
             "correct": False,
             "why": "The pollen grain is right and the seed is not. Two "
                    "gametes fuse at fertilisation, so their halves add back "
                    "to 14."},
            {"text": "14 in the pollen grain and 14 in the seed's first cell.",
             "correct": False,
             "why": "If the pollen grain carried a full 14 and the ovule "
                    "another 14, the seed would start with 28. One of the two "
                    "numbers has to be halved, and it is the gamete's."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h09",
        "band": "harder",
        "text": "A student says a gamete is made by cutting a body cell's "
                "chromosomes in half, so each gamete gets half of every "
                "chromosome. What is wrong with that account?",
        "options": [
            {"text": "Nothing is cut in half — a gamete gets one whole "
                     "chromosome from each pair.",
             "correct": True},
            {"text": "Nothing is cut in half — a gamete gets all 46 and loses "
                     "half of them later.",
             "correct": False,
             "why": "There is no later losing. The chromosomes are shared out "
                    "as the gamete is made, one from each pair, and every one "
                    "of them is whole."},
            {"text": "The halving is right, but it happens at fertilisation "
                     "rather than before it.",
             "correct": False,
             "why": "Fertilisation is the joining, not the halving. Gametes "
                    "already carry one of each pair by the time they meet."},
            {"text": "The account is right for animals but not for plants, "
                     "where pollen carries a full set.",
             "correct": False,
             "why": "Pollen grains carry half a set exactly as sperm cells do. "
                    "That is why a pea seed starts with 14 rather than 28."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h10",
        "band": "harder",
        "text": "Mendel published his results in 1866 and was almost entirely "
                "ignored until three other botanists found the same rules in "
                "1900. What does that tell you about how science moves?",
        "options": [
            {"text": "That his counting must have been unconvincing, or "
                     "somebody would have taken it up.",
             "correct": False,
             "why": "His counts ran to tens of thousands of plants and were "
                    "sound. Being ignored is not the same as being "
                    "unconvincing."},
            {"text": "That his results were wrong in 1866 and only became "
                     "right once others confirmed them.",
             "correct": False,
             "why": "Confirmation does not make a result true — it was true "
                    "when he wrote it down. What changed was who was in a "
                    "position to use it."},
            {"text": "That a scientist's work only counts once it has been "
                     "published in the right place.",
             "correct": False,
             "why": "He did publish. The problem was that almost nobody "
                    "reading it had a question his answer fitted."},
            {"text": "That a correct answer can arrive before anyone has a use "
                     "for it, and wait.",
             "correct": True},
        ],
        "figure": None,
    },
]
