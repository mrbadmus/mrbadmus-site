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
    {
        "id": "b10-04-e11",
        "band": "easier",
        "text": "A dog's body cells each have 78 chromosomes. How many "
                "chromosomes are in one of its gametes?",
        "options": [
            {"text": "39, half of the body-cell number.", "correct": True},
            {"text": "156, since two gametes are needed to make a full set.",
             "correct": False,
             "why": "Gametes carry HALF the number, not double it. Two gametes "
                    "together restore 78; one on its own carries less."},
            {"text": "78, the same as a body cell.", "correct": False,
             "why": "A gamete carries only one chromosome from each pair. If "
                    "it carried 78 as well, fertilisation would give 156."},
            {"text": "19, a quarter of the body-cell number.",
             "correct": False,
             "why": "A gamete carries half the body-cell number, not a "
                    "quarter. Halving 78 gives 39."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e12",
        "band": "easier",
        "text": "In a species where a gamete carries 10 chromosomes, how many "
                "chromosomes does the fertilised egg have?",
        "options": [
            {"text": "10 — the same as one gamete.", "correct": False,
             "why": "Two gametes fuse at fertilisation, not one. The number "
                    "doubles rather than staying the same."},
            {"text": "5 — half of the gamete's number.", "correct": False,
             "why": "Fertilisation is where the number is restored, not halved "
                    "again. Two gametes of 10 add back up to 20."},
            {"text": "40 — the two parents' body cells added together.",
             "correct": False,
             "why": "It is the two GAMETES that fuse, each carrying 10, not "
                    "the two parents' whole body-cell totals."},
            {"text": "20 — one full set from each of the two gametes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e13",
        "band": "easier",
        "text": "Which best describes what is meant by 'a version of a gene'?",
        "options": [
            {"text": "One of the alternative forms a gene can come in.",
             "correct": True},
            {"text": "A whole chromosome, carrying many genes at once.",
             "correct": False,
             "why": "A version is one alternative form of a single gene, not "
                    "a whole chromosome carrying many genes."},
            {"text": "The complete set of instructions inside a cell's "
                     "nucleus.",
             "correct": False,
             "why": "That describes all the DNA together. A version of a "
                    "gene is one form of just one gene within it."},
            {"text": "A cell that is passed from parent to offspring.",
             "correct": False,
             "why": "That describes a gamete. A version of a gene is "
                    "information, not a cell."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e14",
        "band": "easier",
        "text": "A fertilised egg divides again and again to build a new "
                "organism. What is true of the DNA in each new cell?",
        "options": [
            {"text": "It is an exact copy of the DNA in the fertilised egg.",
             "correct": True},
            {"text": "It is a fresh combination, reshuffled at every "
                     "division.",
             "correct": False,
             "why": "Reshuffling only happens when gametes are made, not "
                    "during ordinary cell division, which copies DNA "
                    "exactly."},
            {"text": "It carries only the genes that cell's own job needs.",
             "correct": False,
             "why": "Every cell keeps the full set of genes; only which "
                    "genes are switched on differs from cell to cell."},
            {"text": "It is halved compared to the fertilised egg's DNA.",
             "correct": False,
             "why": "Halving happens only when gametes are made, not during "
                    "ordinary body-cell division."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e15",
        "band": "easier",
        "text": "A pea plant is pure-breeding for seed shape. What must be "
                "true of the two versions of the seed-shape gene it carries?",
        "options": [
            {"text": "One overrides the other completely.", "correct": False,
             "why": "That can be true whether or not a plant is pure-breeding. "
                    "Pure-breeding is specifically about the two versions "
                    "matching."},
            {"text": "They are identical to each other.", "correct": True},
            {"text": "One of them is hidden and never passed on.",
             "correct": False,
             "why": "Nothing is ever unable to be passed on. Whichever version "
                    "a plant carries, it can pass either one on."},
            {"text": "They came from two different parent plants.",
             "correct": False,
             "why": "Which parent supplied each version says nothing about "
                    "whether they're identical — that is what pure-breeding "
                    "actually requires."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e16",
        "band": "easier",
        "text": "In peas, round seed shape overrides wrinkled. A plant carries "
                "one round version and one wrinkled version. What shape are "
                "its seeds?",
        "options": [
            {"text": "Wrinkled, because the wrinkled version is more common.",
             "correct": False,
             "why": "Commonness has nothing to do with it. One round version "
                    "is enough to override wrinkled, whatever proportion of "
                    "plants carry which."},
            {"text": "A shape in between, since the plant carries both "
                     "versions.",
             "correct": False,
             "why": "Nothing blends. One round version is enough to "
                    "override the wrinkled one completely."},
            {"text": "Round.", "correct": True},
            {"text": "It depends on which parent supplied the round "
                     "version.",
             "correct": False,
             "why": "Which parent supplied which version makes no "
                    "difference to which shows. Round overrides wrinkled "
                    "either way."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e17",
        "band": "easier",
        "text": "A parent carries two versions of a gene. What happens to "
                "those two versions when one of its gametes is made?",
        "options": [
            {"text": "Both go in, so the gamete carries a full pair of them.",
             "correct": False,
             "why": "A gamete carries one version, not a pair. If it carried "
                    "both, the offspring would end up with four."},
            {"text": "They combine into a single blended version first.",
             "correct": False,
             "why": "Nothing blends. Each version stays separate and "
                    "unchanged, and one of the two is passed on whole."},
            {"text": "Whichever version the parent shows is the one that "
                     "always goes in.",
             "correct": False,
             "why": "Which version shows makes no difference to which is "
                    "passed on. A hidden version goes into half the gametes "
                    "just as readily."},
            {"text": "Only one of the two goes into the gamete.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e18",
        "band": "easier",
        "text": "An organism carries two versions of each of its genes. Where "
                "does each of the two come from?",
        "options": [
            {"text": "One version from each of its two parents.",
             "correct": True},
            {"text": "Both from whichever parent the organism most resembles.",
             "correct": False,
             "why": "Resemblance has nothing to do with it. One version comes "
                    "from each parent whoever the offspring happens to look "
                    "like."},
            {"text": "Both from the mother, since the egg is the larger "
                     "gamete.",
             "correct": False,
             "why": "Size makes no difference to what a gamete carries. Each "
                    "parent contributes one version of every gene."},
            {"text": "One from each parent for some genes, and both from one "
                     "parent for others.",
             "correct": False,
             "why": "It is one from each parent for every gene alike. No gene "
                    "takes both its versions from a single parent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e19",
        "band": "easier",
        "text": "Two pure-breeding round-seeded pea plants are crossed. What "
                "seed shape do the offspring have?",
        "options": [
            {"text": "Wrinkled, because two identical versions cancel each "
                     "other out.",
             "correct": False,
             "why": "Identical versions do not cancel out. Two rounds passed "
                    "on give round seeds, simply reinforced."},
            {"text": "Half round and half wrinkled.", "correct": False,
             "why": "With only the round version present in either parent, "
                    "there is no wrinkled version anywhere in the cross to "
                    "produce a wrinkled seed."},
            {"text": "Round.", "correct": True},
            {"text": "A mixture of round and slightly wrinkled.",
             "correct": False,
             "why": "Nothing blends, and there is no wrinkled version in this "
                    "cross to blend with in any case."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e20",
        "band": "easier",
        "text": "An organism carries a hidden version of a gene that is "
                "overridden by the other version it carries. What effect does "
                "the hidden version have on how the organism looks?",
        "options": [
            {"text": "A small, partial effect that is hard to notice.",
             "correct": False,
             "why": "An overridden version is not a matter of subtlety — it "
                    "produces no visible effect while it is there in full."},
            {"text": "It weakens slightly each generation it stays hidden.",
             "correct": False,
             "why": "A version does not weaken through being hidden; it is "
                    "passed on completely unchanged."},
            {"text": "It becomes active again once the organism is fully "
                     "grown.",
             "correct": False,
             "why": "Nothing switches an overridden version back on as an "
                    "organism matures. It stays hidden until an offspring "
                    "receives it from both parents."},
            {"text": "None — it produces no visible effect while it is "
                     "overridden.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e21",
        "band": "easier",
        "text": "Where did Gregor Mendel carry out his pea experiments?",
        "options": [
            {"text": "At a university laboratory in England.",
             "correct": False,
             "why": "Mendel was a monk working in his monastery's own garden, "
                    "not a university researcher."},
            {"text": "On a farm in France, as a professional plant breeder.",
             "correct": False,
             "why": "He was a monk, not a professional breeder, and his garden "
                    "was in Brno, not France."},
            {"text": "In a monastery garden, in what is now the Czech "
                     "Republic.",
             "correct": True},
            {"text": "In a botanical garden in the Netherlands.",
             "correct": False,
             "why": "His work took place at his monastery in Brno, in what is "
                    "now the Czech Republic."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e22",
        "band": "easier",
        "text": "Roughly how many pea plants did Mendel grow altogether while "
                "collecting his results?",
        "options": [
            {"text": "About 28,000.", "correct": True},
            {"text": "About 2,800.", "correct": False,
             "why": "That is ten times too few. Mendel's total ran to tens of "
                    "thousands of plants."},
            {"text": "About 280,000.", "correct": False,
             "why": "That is ten times too many for Mendel's own count, "
                    "usually put at something like 28,000."},
            {"text": "About 280.", "correct": False,
             "why": "A count that small would never have shown a ratio as "
                    "clean as 3:1. Mendel's real total ran into the tens of "
                    "thousands."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e23",
        "band": "easier",
        "text": "Which of these is a genuine reason peas were a good choice "
                "for Mendel's experiments?",
        "options": [
            {"text": "They produce a new generation within a single day.",
             "correct": False,
             "why": "Peas grow over a season, not a single day. Their real "
                    "advantage was still speed, just not that fast."},
            {"text": "Every characteristic in a pea plant comes in exactly one "
                     "form.",
             "correct": False,
             "why": "The opposite is closer to true. Mendel picked "
                    "characteristics that came in two clean forms, such as "
                    "round or wrinkled seeds."},
            {"text": "They self-pollinate, giving pure-breeding lines to start "
                     "from.",
             "correct": True},
            {"text": "Pea plants cannot be crossed with each other at all.",
             "correct": False,
             "why": "Mendel's whole method depended on crossing pea plants "
                    "deliberately. Left alone they self-pollinate, but he "
                    "crossed them by hand."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e24",
        "band": "easier",
        "text": "What did Mendel do differently from earlier plant breeders "
                "who had also crossed plants and described the results?",
        "options": [
            {"text": "He was the first person ever to cross two pea plants.",
             "correct": False,
             "why": "Crossing plants was already common practice. What Mendel "
                    "added was counting the results precisely."},
            {"text": "He used a microscope to examine the seeds.",
             "correct": False,
             "why": "Nothing in his method needed a microscope — seed shape "
                    "and colour are visible to the naked eye. Counting was the "
                    "real innovation."},
            {"text": "He counted the offspring of every cross.",
             "correct": True},
            {"text": "He grew his plants for a much shorter time than anyone "
                     "before him.",
             "correct": False,
             "why": "His experiments ran for years, from 1856 to 1863. Speed "
                    "was not what set his work apart."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e25",
        "band": "easier",
        "text": "A plant is grown in poor soil and grows smaller than usual as "
                "a result. Will that change be passed on to its seeds?",
        "options": [
            {"text": "Yes — anything that happens to a parent in its life is "
                     "passed on to its offspring.",
             "correct": False,
             "why": "Nothing that happens during an organism's own lifetime is "
                    "written into its gametes. Only genetic information "
                    "already there can be passed on."},
            {"text": "Yes, but only if the poor soil lasts for more than one "
                     "generation.",
             "correct": False,
             "why": "The length of time makes no difference. A lifetime change "
                    "to one plant does not enter its gametes at all."},
            {"text": "It depends on which parent was affected by the poor "
                     "soil.",
             "correct": False,
             "why": "Neither parent's lifetime experience of soil quality is "
                    "written into the gametes, whichever parent it happened "
                    "to."},
            {"text": "No — only genetic information is passed on, and poor "
                     "soil does not change that.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e26",
        "band": "easier",
        "text": "Two purple pea plants look identical but one carries a hidden "
                "white version and the other does not. What does this show?",
        "options": [
            {"text": "That one of the two plants must actually be a slightly "
                     "different shade.",
             "correct": False,
             "why": "Nothing about their appearance differs — they are "
                    "described as looking identical. The difference is only in "
                    "what each is carrying."},
            {"text": "That two plants can look identical while carrying "
                     "different information.",
             "correct": True},
            {"text": "That the hidden version has already started to show a "
                     "small effect.",
             "correct": False,
             "why": "A hidden version, by definition, produces no visible "
                    "effect. Both plants are purple."},
            {"text": "That flower colour cannot really be inherited after all.",
             "correct": False,
             "why": "Flower colour here is exactly the inherited "
                    "characteristic. What varies between the two plants is "
                    "which versions they carry."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e27",
        "band": "easier",
        "text": "In one of Mendel's other experiments, yellow seed colour "
                "overrides green. A plant carries one yellow version and one "
                "green version. What colour are its seeds?",
        "options": [
            {"text": "Yellow.", "correct": True},
            {"text": "Green, because green is the rarer of the two colours "
                     "in this cross.",
             "correct": False,
             "why": "Rarity has nothing to do with it. A single yellow "
                    "version is enough to override green."},
            {"text": "A pale yellow-green blend.", "correct": False,
             "why": "Nothing blends. One yellow version is enough to "
                    "produce fully yellow seeds."},
            {"text": "It depends on whether the yellow version came from "
                     "the mother or father plant.",
             "correct": False,
             "why": "Which parent supplied the yellow version makes no "
                    "difference. Either way, one yellow version is enough to "
                    "override green."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e28",
        "band": "easier",
        "text": "A tall pea plant is crossed with a short pea plant and every "
                "offspring is tall. Is that the expected result when one "
                "version of a gene overrides the other?",
        "options": [
            {"text": "No — the offspring should be a height in between the two "
                     "parents.",
             "correct": False,
             "why": "That is the blending prediction, and the point of this "
                    "cross is that heights do not blend when a single gene "
                    "with two versions is involved."},
            {"text": "Yes — one version overrides the other, so an in-between "
                     "height is not expected.",
             "correct": True},
            {"text": "No — the offspring should all be short, since short is "
                     "the hidden version.",
             "correct": False,
             "why": "Whichever version overrides — tall in this cross — is "
                    "what shows in every offspring, not the hidden one."},
            {"text": "Yes, but the short parent must be unhealthy.",
             "correct": False,
             "why": "Nothing about the short parent's health is involved. The "
                    "result follows from which version overrides."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e29",
        "band": "easier",
        "text": "A guinea pig carries one black-coat version and one "
                "white-coat version. Which version will a given one of its "
                "gametes carry?",
        "options": [
            {"text": "Black, because black is the version the guinea pig "
                     "shows.",
             "correct": False,
             "why": "Which version shows does not decide which is passed on. "
                    "Both go into gametes equally often."},
            {"text": "Whichever the mate needs for the litter to survive.",
             "correct": False,
             "why": "Nothing about the mate reaches back into which version a "
                    "gamete carries. It is settled as the gamete is made."},
            {"text": "Either one — which of the two it carries is down to "
                     "chance.",
             "correct": True},
            {"text": "Both, so that the offspring is certain to receive the "
                     "pair.",
             "correct": False,
             "why": "A gamete carries one version of each gene. The "
                    "offspring's pair is made up from two gametes, not from "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-e30",
        "band": "easier",
        "text": "In what year did Mendel publish the results of his pea "
                "experiments?",
        "options": [
            {"text": "1900", "correct": False,
             "why": "That is the year three other botanists rediscovered the "
                    "same rules — not the year Mendel himself published."},
            {"text": "1856", "correct": False,
             "why": "That is the year Mendel began his experiments, seven "
                    "years before he published his results in 1866."},
            {"text": "1884", "correct": False,
             "why": "That is the year Mendel died, two decades after he had "
                    "already published his results."},
            {"text": "1866", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s11",
        "band": "standard",
        "text": "A species has 78 chromosomes in a body cell. Two individuals "
                "are crossed. How many chromosomes are in the fertilised egg "
                "of their offspring, and why?",
        "options": [
            {"text": "156 — each parent contributes a full body cell's worth.",
             "correct": False,
             "why": "Parents pass on gametes, each carrying only half the "
                    "number, not whole body cells. Adding two body cells' "
                    "worth would double the total every generation."},
            {"text": "39 — the fertilised egg only ever gets half of what a "
                     "body cell has.",
             "correct": False,
             "why": "Fertilisation is where the number gets restored, not "
                    "halved again. Two gametes of 39 each add up to 78."},
            {"text": "78 — two halved gametes add back to the full number.",
             "correct": True},
            {"text": "117 — one and a half body cells' worth are combined.",
             "correct": False,
             "why": "Fertilisation combines exactly two gametes, each with "
                    "half the body-cell number. There is no \"one and a half\" "
                    "step in the process."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s12",
        "band": "standard",
        "text": "A pure-breeding round-seeded plant is crossed with a "
                "pure-breeding wrinkled-seeded plant. Round overrides "
                "wrinkled. What seed shape are the offspring, and why?",
        "options": [
            {"text": "Half round and half wrinkled, because each parent passes "
                     "on its own shape to half the seeds.",
             "correct": False,
             "why": "Every seed here receives one version from EACH parent, "
                    "not a whole shape from one of them. Every single seed is "
                    "round-and-wrinkled combined, which shows as round."},
            {"text": "All wrinkled, because wrinkled is the hidden version and "
                     "hidden versions show first.",
             "correct": False,
             "why": "A hidden version does not show \"first\" — it shows only "
                    "when there is no overriding version present, which is not "
                    "the case here."},
            {"text": "All round — every offspring gets one round and one "
                     "wrinkled version, and round overrides.",
             "correct": True},
            {"text": "A shape between round and wrinkled, since both versions "
                     "are present in every seed.",
             "correct": False,
             "why": "Nothing blends. Every offspring here carries one round "
                    "and one wrinkled version, and round completely overrides "
                    "wrinkled."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s13",
        "band": "standard",
        "text": "A yellow-seeded pea plant is crossed with a green-seeded "
                "plant, and a mix of yellow and green seeds results. What must "
                "be true of the yellow-seeded parent?",
        "options": [
            {"text": "It must be pure-breeding for yellow seeds.",
             "correct": False,
             "why": "A pure-breeding yellow parent can only pass on the yellow "
                    "version, so none of the offspring could come out green. "
                    "Some green offspring rules that out."},
            {"text": "It has developed a new green version by chance during "
                     "this cross.",
             "correct": False,
             "why": "Nothing new appears during a cross. The green version "
                    "came from a parent that was already carrying it."},
            {"text": "The green-seeded parent must actually be carrying two "
                     "yellow versions.",
             "correct": False,
             "why": "A plant carrying two yellow versions could only pass on "
                    "yellow. The green offspring shows one of the true parents "
                    "is carrying green, not the other way round."},
            {"text": "It must be carrying a hidden green version as well as a "
                     "yellow one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s14",
        "band": "standard",
        "text": "A cross expected to give a quarter wrinkled seeds produces "
                "20 offspring, of which 6 are wrinkled. What percentage of "
                "the offspring is that?",
        "options": [
            {"text": "30 per cent.", "correct": True},
            {"text": "25 per cent, since that's what a quarter is expected "
                     "to be.",
             "correct": False,
             "why": "25 per cent is the EXPECTATION, not what this "
                    "particular batch of seeds actually gave. 6 out of 20 is "
                    "30 per cent."},
            {"text": "6 per cent, treating the count itself as the "
                     "percentage.",
             "correct": False,
             "why": "The count of wrinkled seeds is not the same as the "
                    "percentage. Dividing 6 by 20 and multiplying by 100 "
                    "gives 30 per cent, not 6."},
            {"text": "70 per cent, the round share rather than the wrinkled "
                     "share.",
             "correct": False,
             "why": "70 per cent is the ROUND share — the other 14 seeds. "
                    "The question asks for the wrinkled share, which is 30 "
                    "per cent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s15",
        "band": "standard",
        "text": "A plant breeder crosses two carriers of a hidden version and "
                "gets close to but not exactly a quarter showing it. Why might "
                "that be?",
        "options": [
            {"text": "The breeder must have made a mistake counting the "
                     "offspring.",
             "correct": False,
             "why": "A small sample landing close to but not exactly on the "
                    "expected ratio is normal, not a sign of a counting error."},
            {"text": "Chance means small samples rarely land exactly on the "
                     "expected ratio.",
             "correct": True},
            {"text": "The expected ratio only applies to Mendel's own pea "
                     "plants.",
             "correct": False,
             "why": "The same expectation applies to any cross of this kind. "
                    "What varies from sample to sample is the actual count, "
                    "not the underlying rule."},
            {"text": "The hidden version must be slightly weaker than usual in "
                     "this cross.",
             "correct": False,
             "why": "Nothing about a version's strength changes from sample to "
                    "sample. Chance in which gametes combine is enough on its "
                    "own to explain the gap."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s16",
        "band": "standard",
        "text": "Two full siblings, from the same two parents, carry different "
                "combinations of gene versions. What is the source of that "
                "difference?",
        "options": [
            {"text": "The parents' own gene versions must have changed between "
                     "having each child.",
             "correct": False,
             "why": "A parent's own versions do not change from one child to "
                    "the next. What differs is which of the two each gamete "
                    "happened to carry."},
            {"text": "One sibling inherited more genes from one parent than "
                     "the other sibling did.",
             "correct": False,
             "why": "Every child receives exactly the same amount, one version "
                    "of every gene from each parent. What varies is which "
                    "versions, not how many."},
            {"text": "Siblings only differ because of things that happened to "
                     "them after birth.",
             "correct": False,
             "why": "The combination of gene versions a sibling carries is "
                    "fixed at fertilisation, before birth. Later life events "
                    "do not rewrite it."},
            {"text": "Each gamete carried one version of each gene, chosen by "
                     "chance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s17",
        "band": "standard",
        "text": "In a simple model, curly hair overrides straight hair. A "
                "woman with a straight-haired father and a curly-haired mother "
                "has curly hair herself. Later she has a straight-haired child "
                "with a straight-haired partner. What must be true about the "
                "woman?",
        "options": [
            {"text": "She must have somehow regained her father's "
                     "straight-hair version as an adult.",
             "correct": False,
             "why": "Nothing is regained. If she carries the straight-hair "
                    "version, she has done so since fertilisation, without it "
                    "ever leaving."},
            {"text": "Her partner's straight-hair version must have overridden "
                     "her curly one in the child.",
             "correct": False,
             "why": "The child's own combination decides the child's hair, not "
                    "an override happening to the mother. She must be carrying "
                    "a hidden straight version for this outcome to be possible "
                    "at all."},
            {"text": "The straight-haired child's hair must be a coincidence "
                     "unrelated to genetics.",
             "correct": False,
             "why": "A straight-haired child from these parents is exactly "
                    "what carrying-without-showing predicts once both parents "
                    "happen to pass the straight version."},
            {"text": "She must be carrying a hidden straight-hair version as "
                     "well as the curly one she shows.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s18",
        "band": "standard",
        "text": "Why does Mendel deliberately start his crosses from "
                "pure-breeding lines rather than from ordinary plants of "
                "unknown ancestry?",
        "options": [
            {"text": 'Because he then knows exactly which versions each parent carries.',
             "correct": True},
            {"text": "Because pure-breeding plants produce more seeds than "
                     "other plants.",
             "correct": False,
             "why": "How many seeds a plant produces has nothing to do with "
                    "whether it's pure-breeding. The advantage is knowing "
                    "exactly what each parent carries."},
            {"text": "Because pure-breeding plants cannot be crossed with "
                     "plants of a different variety.",
             "correct": False,
             "why": "Pure-breeding plants can be crossed with anything — "
                    "that's exactly what Mendel did. The value is knowing "
                    "what they carry going in."},
            {"text": "Because ordinary plants of unknown ancestry cannot "
                     "make gametes.",
             "correct": False,
             "why": "Any pea plant makes gametes in the usual way. What's "
                    "unusable about an ordinary plant here is that you "
                    "can't be sure what it's carrying."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s19",
        "band": "standard",
        "text": "A cat with short fur has two kittens with a mate that also "
                "has short fur: one short-furred and one long-furred. What "
                "does the long-furred kitten show about both parents?",
        "options": [
            {"text": "Only the mother must be carrying the long-fur version.",
             "correct": False,
             "why": "For the long-fur version to show, the kitten must receive "
                    "it from BOTH parents. If only the mother carried it, the "
                    "kitten could not show it."},
            {"text": "Both parents must be carrying a hidden long-fur version.",
             "correct": True},
            {"text": "The father's fur must have changed length after mating.",
             "correct": False,
             "why": "An adult's own fur length does not rewrite what it passes "
                    "on. The kitten's long fur shows something both parents "
                    "were already carrying, hidden."},
            {"text": "The long-furred kitten must have a different father from "
                     "its litter-mate.",
             "correct": False,
             "why": "Litter-mates can differ in which versions they receive "
                    "from the very same two parents. There's no need to invent "
                    "a different father."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s20",
        "band": "standard",
        "text": "A round-seeded plant known to be carrying a hidden wrinkled "
                "version is crossed with a wrinkled-seeded plant. Out of 60 "
                "seeds grown, about how many would be expected to be wrinkled?",
        "options": [
            {"text": "About 15, a quarter of the total.", "correct": False,
             "why": "A quarter is the expectation when BOTH parents carry a "
                    "hidden version alongside a shown one. Here one parent can "
                    "only ever pass on wrinkled, which raises the wrinkled "
                    "share to about a half."},
            {"text": "None, since the round-seeded parent's version always "
                     "overrides.",
             "correct": False,
             "why": "Overriding decides what shows in a seed with both "
                    "versions present, but half these seeds will receive "
                    "wrinkled from BOTH parents, with nothing to override."},
            {"text": "All 60, since crossing with wrinkled makes every seed "
                     "wrinkled.",
             "correct": False,
             "why": "The round-seeded parent still passes its round version to "
                    "half the seeds, and one round version is enough for a "
                    "seed to show round."},
            {"text": "About 30.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s21",
        "band": "standard",
        "text": "A breeder crosses two plants, each carrying one shown version "
                "and one hidden version of the same gene, and expects close to "
                "a 3:1 ratio. In a different cross, one parent is "
                "pure-breeding for the shown version and the other still "
                "carries one of each. How does the second cross's ratio differ "
                "from the first, and why?",
        "options": [
            {"text": "Both crosses give the same 3:1 ratio, because the shown "
                     "version is involved in both.",
             "correct": False,
             "why": "The ratio isn't decided by which version shows — it's "
                    "decided by which versions each parent can pass on. A "
                    "pure-breeding parent can only ever pass the shown one."},
            {"text": "The second cross gives more hidden-version offspring, "
                     "because pure-breeding strengthens a version.",
             "correct": False,
             "why": "Nothing about being pure-breeding makes a version "
                    "\"stronger\". A pure-breeding parent for the shown "
                    "version simply has no hidden version to contribute."},
            {"text": "The second cross gives no offspring that show the hidden "
                     "version.",
             "correct": True},
            {"text": "The two crosses cannot be compared without knowing the "
                     "plants' exact ages.",
             "correct": False,
             "why": "Age plays no part in which versions a plant passes on. "
                    "What decides the ratio is which versions each parent is "
                    "carrying."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s22",
        "band": "standard",
        "text": "Out of 84 offspring from a cross expected to give close to "
                "three-quarters showing a version, 21 do not show it. What "
                "percentage does that represent, and is it close to the "
                "expectation?",
        "options": [
            {"text": "25 per cent, close to the quarter expected not to "
                     "show it.",
             "correct": True},
            {"text": "21 per cent, taking the count itself as the "
                     "percentage.",
             "correct": False,
             "why": "The count of offspring not showing the version is not "
                    "the same as a percentage. 21 out of 84 works out to 25 "
                    "per cent."},
            {"text": "75 per cent, the share that does show the version "
                     "rather than the share that doesn't.",
             "correct": False,
             "why": "75 per cent is the group that DOES show it — the "
                    "other 63 offspring. The question asks for the share "
                    "that does not, which is 25 per cent."},
            {"text": "4 per cent, dividing 84 by 21 the wrong way round.",
             "correct": False,
             "why": "That divides the total by the part instead of the "
                    "part by the total. 21 divided by 84, times 100, gives "
                    "25 per cent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s23",
        "band": "standard",
        "text": "Mendel followed one characteristic at a time, such as seed "
                "shape, rather than recording everything about each plant at "
                "once. Why did that matter?",
        "options": [
            {"text": "Because a pea plant only shows one characteristic that "
                     "can be recorded at a time.",
             "correct": False,
             "why": "A pea plant shows seed shape, seed colour, flower colour "
                    "and height all at once. Mendel chose to count them one by "
                    "one."},
            {"text": "Because a clean ratio can only be seen when one "
                     "characteristic is counted on its own.",
             "correct": True},
            {"text": "Because recording two characteristics at once would have "
                     "changed the plants themselves.",
             "correct": False,
             "why": "Writing something down changes nothing about the plant. "
                    "What it changes is how clearly a pattern can be read off."},
            {"text": "Because the other characteristics of a pea plant are not "
                     "inherited at all.",
             "correct": False,
             "why": "Seed colour, flower colour and height are every bit as "
                    "inherited as seed shape. Mendel went on to study them "
                    "too."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s24",
        "band": "standard",
        "text": "A plant with round seeds is crossed with a plant that is "
                "pure-breeding for wrinkled seeds, and all the offspring have "
                "round seeds. What can be concluded about the round-seeded "
                "parent?",
        "options": [
            {"text": "It must be carrying a hidden wrinkled version, since it "
                     "was crossed with wrinkled.",
             "correct": False,
             "why": "Being crossed with a wrinkled-seeded plant does not by "
                    "itself put a wrinkled version into the round parent. If "
                    "it carried one, close to half its many offspring would be "
                    "expected to show wrinkled — none did."},
            {"text": "It must be pure-breeding for round seeds.",
             "correct": True},
            {"text": "Nothing can be concluded, since seed shape does not "
                     "reveal what a plant carries.",
             "correct": False,
             "why": "Seed shape is exactly what the offspring reveal here. A "
                    "plant carrying a hidden wrinkled version crossed with "
                    "pure wrinkled would be expected to give close to half "
                    "wrinkled offspring, and none appeared."},
            {"text": "The wrinkled-seeded parent must actually be carrying a "
                     "round version too.",
             "correct": False,
             "why": "It was described as pure-breeding for wrinkled, so it "
                    "carries only the wrinkled version. The result instead "
                    "tells you about the round-seeded parent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s25",
        "band": "standard",
        "text": "A pea plant grown in very rich soil produces unusually "
                "large, round seeds one year. The next year, seeds from that "
                "plant are grown in ordinary soil, and the seed shape is "
                "still round, though the size is ordinary. What does that "
                "suggest?",
        "options": [
            {"text": "Seed shape is set by genetic information, while "
                     "environment can still affect other things like size.",
             "correct": True},
            {"text": "Seed shape must be affected by soil too, since the "
                     "plant experienced two different environments.",
             "correct": False,
             "why": "The plant's shape stayed round in BOTH environments, "
                    "exactly what you would expect from a characteristic "
                    "decided by genetic information rather than by soil."},
            {"text": "The plant must have changed which version of the "
                     "gene it carries.",
             "correct": False,
             "why": "Nothing about which version of a gene a plant carries "
                    "changes during its lifetime, whatever soil it is grown "
                    "in."},
            {"text": "The result proves nothing, since only one plant was "
                     "tested.",
             "correct": False,
             "why": "A single plant showing the SAME seed shape across two "
                    "very different environments, while its size changed, "
                    "is exactly the pattern that separates a genetic "
                    "characteristic from an environmental one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s26",
        "band": "standard",
        "text": "A species has 24 chromosomes in a body cell. How many are in "
                "one of its gametes, and how many will be in the fertilised "
                "egg once two gametes fuse?",
        "options": [
            {"text": "24 in the gamete, and 48 in the fertilised egg.",
             "correct": False,
             "why": "A gamete carries HALF the body-cell number, not the same "
                    "amount. Passing on 24 each would double the total to 48."},
            {"text": "12 in the gamete, and 24 in the fertilised egg.",
             "correct": True},
            {"text": "12 in the gamete, and 12 in the fertilised egg.",
             "correct": False,
             "why": "Fertilisation is where the number is restored, not halved "
                    "again. Two gametes of 12 each add back up to 24."},
            {"text": "6 in the gamete, and 24 in the fertilised egg.",
             "correct": False,
             "why": "A gamete carries half of 24, which is 12, not 6, though "
                    "the fertilised-egg figure here is right."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s27",
        "band": "standard",
        "text": "One round-seeded plant is pure-breeding, and another "
                "round-seeded plant is carrying a hidden wrinkled version. "
                "What can be said about their offspring?",
        "options": [
            {"text": "All offspring will show round, and none of them will "
                     "carry the hidden wrinkled version.",
             "correct": False,
             "why": "The carrier parent passes the wrinkled version to about "
                    "half its gametes. Those seeds still show round, but they "
                    "do carry the hidden version."},
            {"text": "About three-quarters of the offspring will show round, "
                     "and a quarter will be wrinkled.",
             "correct": False,
             "why": "Three-quarters showing and a quarter not showing is what "
                    "TWO carrier parents give. Here one parent is "
                    "pure-breeding and can only ever pass round."},
            {"text": "About half the offspring will show wrinkled, since one "
                     "parent is carrying it.",
             "correct": False,
             "why": "The pure-breeding round parent passes round to every "
                    "seed, which always overrides any wrinkled version the "
                    "other parent's gametes carry."},
            {"text": "All will show round, and about half will carry the "
                     "hidden wrinkled version.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s28",
        "band": "standard",
        "text": "A human gamete carries 23 chromosomes and a fruit fly "
                "gamete carries 4. Does the fruit fly having fewer "
                "chromosomes mean it has less genetic information than a "
                "human?",
        "options": [
            {"text": 'Not necessarily — chromosome number says nothing about the amount of information carried.',
             "correct": True},
            {"text": "Yes — fewer chromosomes always means less genetic "
                     "information overall.",
             "correct": False,
             "why": "Chromosome number on its own says nothing about how "
                    "much information is carried. A chromosome can hold "
                    "many or few genes."},
            {"text": "Yes, because a gamete's chromosome number always "
                     "matches how advanced the organism is.",
             "correct": False,
             "why": "Chromosome number reflects nothing about how "
                    "\"advanced\" an organism is. It is simply a feature of "
                    "that species' own set of chromosomes."},
            {"text": "No comparison is possible unless the two organisms "
                     "are the same species.",
             "correct": False,
             "why": "Chromosome numbers can be compared across species "
                    "readily enough — the comparison just doesn't tell you "
                    "what this option assumed it would."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s29",
        "band": "standard",
        "text": "A class of thirty pairs of students each cross two carrier "
                "plants and grow just two seeds per pair. Why is it a bad idea "
                "to expect every pair's two seeds to show the 3:1 ratio?",
        "options": [
            {"text": "The 3:1 ratio only applies once a hundred seeds have "
                     "been grown, never fewer.",
             "correct": False,
             "why": "There's no fixed number where the ratio \"switches on\". "
                    "Larger samples simply sit closer to 3:1 more often than "
                    "small ones do."},
            {"text": "A sample of two seeds is far too small for a proportion "
                     "like 3:1 to appear reliably.",
             "correct": True},
            {"text": "Two seeds from carrier plants can never come out as one "
                     "showing the hidden version, one not.",
             "correct": False,
             "why": "Two seeds can come out one and one, or two and none, or "
                    "none and two — that's the whole issue with such a small "
                    "sample."},
            {"text": "The class must be crossing the wrong kind of plant if "
                     "they don't see 3:1 straight away.",
             "correct": False,
             "why": "Which plants they crossed isn't the issue. Chance, "
                    "working on far too small a sample, is enough on its own "
                    "to explain any result from just two seeds."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-s30",
        "band": "standard",
        "text": "A couple wants to know if either of them is carrying a hidden "
                "version of an inherited condition. Why can looking at their "
                "own appearance not answer that question?",
        "options": [
            {"text": "Appearance can answer it, as long as you look closely "
                     "enough.",
             "correct": False,
             "why": "However closely you look, a hidden version produces no "
                    "visible sign while it is overridden. Appearance simply "
                    "cannot reach it."},
            {"text": "It can be answered by checking whether either parent "
                     "looks unusually healthy.",
             "correct": False,
             "why": "General health is unrelated to whether someone carries a "
                    "hidden version of a particular gene."},
            {"text": "It can be answered once their child is born, from the "
                     "child's appearance alone.",
             "correct": False,
             "why": "A child's own appearance tells you something once you see "
                    "it, but the question is about the PARENTS, whose own "
                    "appearance cannot show what they are carrying either "
                    "before or after the birth."},
            {"text": "A hidden version produces no visible effect at all while "
                     "it is overridden.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h11",
        "band": "harder",
        "text": "A cross between two carriers of a hidden version is expected "
                "to give close to 3:1. Out of 640 seeds grown, 152 show the "
                "hidden version. Express this as a ratio to one decimal place, "
                "and say whether it supports the 3:1 expectation.",
        "options": [
            {"text": "4.2 to 1 — comfortably outside the range chance alone "
                     "would explain.",
             "correct": False,
             "why": "488 divided by 152 gives about 3.2, not 4.2. The division "
                    "has gone wrong here, and 3.2 to 1 is close to what's "
                    "expected."},
            {"text": "1 to 3.2 — hidden version to shown, which reverses the "
                     "usual convention.",
             "correct": False,
             "why": "Writing the ratio the other way round changes nothing "
                    "about the working, but the usual convention puts the "
                    "SHOWN version first, giving 3.2 to 1."},
            {"text": "3.0 to 1 exactly, since 640 is a large enough sample to "
                     "remove chance.",
             "correct": False,
             "why": "No sample size removes chance entirely. 488 to 152 works "
                    "out at about 3.2 to 1, not exactly 3.0."},
            {"text": "3.2 to 1 — close to 3:1, consistent with chance "
                     "variation in a large sample.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h12",
        "band": "harder",
        "text": "A student claims that because a wrinkled-seeded plant crossed "
                "with a round-seeded plant sometimes gives all round offspring "
                "and sometimes gives about half round and half wrinkled, the "
                "wrinkled plant's own versions must be changing between "
                "crosses. Evaluate this claim.",
        "options": [
            {"text": "The claim is right — a plant's versions can shift "
                     "depending on which plant it is crossed with.",
             "correct": False,
             "why": "A plant's own versions do not shift depending on its "
                    "partner. What differs between the two outcomes is whether "
                    "the ROUND parent is pure-breeding or a carrier."},
            {"text": "The claim cannot be evaluated without knowing the exact "
                     "soil conditions of each cross.",
             "correct": False,
             "why": "Soil has no bearing on which versions of this gene either "
                    "plant carries. The explanation lies entirely in which "
                    "versions the round-seeded parent is carrying."},
            {"text": "The claim is wrong — what changes is which round-seeded "
                     "plant is used, not the wrinkled plant.",
             "correct": True},
            {"text": "The claim is right, but only because wrinkled is the "
                     "hidden version rather than the shown one.",
             "correct": False,
             "why": "Being the hidden version has no bearing on whether a "
                    "plant's OWN versions change. What varies is the other "
                    "parent, in either case."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h13",
        "band": "harder",
        "text": "A species of moth has 60 chromosomes in a body cell. A "
                "biologist claims a gamete from this moth, produced normally, "
                "could have 45 chromosomes. Is that possible, and why or why "
                "not?",
        "options": [
            {"text": "Yes — a gamete can carry any number under the full "
                     "body-cell total.",
             "correct": False,
             "why": "A gamete is not a random fraction of the body-cell "
                    "number. It carries exactly one chromosome from each of "
                    "the 30 pairs, giving 30."},
            {"text": "Yes — moths make gametes differently from most other "
                     "animals.",
             "correct": False,
             "why": "Gamete formation halves the chromosome number the same "
                    "way in every animal that reproduces sexually. There's no "
                    "moth-specific exception here."},
            {"text": "No — a gamete carries half the body-cell number: 30, not "
                     "45.",
             "correct": True},
            {"text": "No — the correct number would be 15, a quarter of the "
                     "body-cell total.",
             "correct": False,
             "why": "A gamete carries HALF the body-cell number, not a "
                    "quarter. Half of 60 is 30, not 15."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h14",
        "band": "harder",
        "text": "A textbook says Mendel 'proved' the 3:1 ratio in 1866. A "
                "historian points out that his own counts, like 6,022 to "
                "2,001, were never exactly 3:1. Whose account is more "
                "accurate, and why?",
        "options": [
            {"text": "The textbook's — 'proved' is the right word once a "
                     "result has been published in a scientific paper.",
             "correct": False,
             "why": "Publication does not turn a close approximation into an "
                    "exact one. Mendel's own numbers, like 6,022 to 2,001, "
                    "never landed on exactly 3:1."},
            {"text": "Neither — the true ratio could only have been "
                     "established using modern DNA sequencing.",
             "correct": False,
             "why": "Nothing about the ratio requires DNA sequencing. It is a "
                    "counting result, and Mendel's own counts already show the "
                    "approximate pattern clearly."},
            {"text": "The textbook's — a count of over 8,000 seeds is large "
                     "enough to remove all chance from the result.",
             "correct": False,
             "why": "No sample size removes chance completely; it only brings "
                    "the ratio closer to 3:1 on average. Mendel's count still "
                    "came out at 3.01 to 1, not exactly 3."},
            {"text": "The historian's — Mendel's counts were close to 3:1, "
                     "never exactly it, as any sample gives.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h15",
        "band": "harder",
        "text": "A round-seeded plant is crossed with a wrinkled-seeded plant. "
                "Of 200 offspring, 96 are wrinkled. What does this tell you "
                "about the round-seeded parent, and what percentage of the "
                "offspring is wrinkled?",
        "options": [
            {"text": "48 per cent are wrinkled, and the round parent must be "
                     "pure-breeding for round.",
             "correct": False,
             "why": "A pure-breeding round parent could only ever pass round, "
                    "giving no wrinkled offspring at all. Getting close to "
                    "half wrinkled points to the round parent carrying a "
                    "hidden wrinkled version."},
            {"text": "48 per cent are wrinkled, and the round parent must be "
                     "carrying a hidden wrinkled version.",
             "correct": True},
            {"text": "96 per cent are wrinkled, using the count itself as the "
                     "percentage.",
             "correct": False,
             "why": "96 is a COUNT, not a percentage. 96 out of 200, correctly "
                    "worked out, is 48 per cent."},
            {"text": "48 per cent are wrinkled, and nothing can be concluded "
                     "about the round-seeded parent.",
             "correct": False,
             "why": "Something clearly can be concluded — close to half the "
                    "offspring showing wrinkled is exactly what a round parent "
                    "carrying a hidden wrinkled version, crossed with pure "
                    "wrinkled, would be expected to give."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h16",
        "band": "harder",
        "text": "A biologist studies a species where a single gene has three "
                "versions rather than two, and any two of the three can be "
                "carried together. Does the usual heredity model — one gamete, "
                "one version, chosen by chance — still explain how versions "
                "are passed on?",
        "options": [
            {"text": "No — that mechanism only works when a gene has exactly "
                     "two versions in the first place.",
             "correct": False,
             "why": "Nothing about gametes carrying one version by chance "
                    "depends on there being only two versions in the "
                    "population as a whole. Each individual still carries and "
                    "passes on just two."},
            {"text": "No — with three versions, each gamete would need to "
                     "carry one and a half versions.",
             "correct": False,
             "why": "A gamete still carries exactly one version of the gene, "
                    "whichever versions exist elsewhere in the population. "
                    "Fractional versions are not possible."},
            {"text": "Yes — each parent still passes on one of its two "
                     "versions, whichever it carries.",
             "correct": True},
            {"text": "Yes, but only because a third version behaves "
                     "differently from the first two.",
             "correct": False,
             "why": "A third version passing on works by the very same "
                    "mechanism as the first two — one copy per gamete, chosen "
                    "by chance."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h17",
        "band": "harder",
        "text": "A species' gamete carries 17 chromosomes. A biologist wrongly "
                "states that its body cells therefore have 17 as well. What is "
                "the correct body-cell number, and what is wrong with the "
                "biologist's reasoning?",
        "options": [
            {"text": "17 — the biologist is correct, since fertilisation does "
                     "not change the number at all.",
             "correct": False,
             "why": "Fertilisation is exactly where the number is restored, by "
                    "fusing two gametes. A body cell has double a gamete's "
                    "number, not the same amount."},
            {"text": "8.5 — the biologist has the direction right but should "
                     "have halved rather than doubled.",
             "correct": False,
             "why": "The biologist's number needs correcting the OTHER way. A "
                    "gamete carries half the body-cell number, so the body "
                    "cell has double the gamete's, which is 34."},
            {"text": "34 — a gamete is HALF the body-cell number, so the body "
                     "cell has double the gamete's count.",
             "correct": True},
            {"text": "51 — three gametes' worth combine to make a body cell.",
             "correct": False,
             "why": "Fertilisation fuses exactly TWO gametes, not three. Two "
                    "gametes of 17 each add up to 34."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h18",
        "band": "harder",
        "text": "A pea plant carrying one round and one wrinkled version is "
                "crossed with a plant that is pure-breeding for wrinkled. "
                "Out of 320 offspring, how many would you expect to show "
                "each seed shape, and how close should the real count come "
                "to that expectation?",
        "options": [
            {"text": 'About 160 round and 160 wrinkled, though a real count will land near but not exactly there.',
             "correct": True},
            {"text": "About 240 round and 80 wrinkled, following the usual "
                     "3:1 ratio for this kind of cross.",
             "correct": False,
             "why": "3:1 is the ratio for TWO carrier parents crossed "
                    "together. Here one parent is pure-breeding for "
                    "wrinkled, which raises the wrinkled share to about a "
                    "half."},
            {"text": "Exactly 160 round and 160 wrinkled, since 320 is a "
                     "large enough sample to remove chance.",
             "correct": False,
             "why": "No sample size removes chance entirely; 320 is large "
                    "enough to land CLOSE to the expected split, not to "
                    "guarantee it exactly."},
            {"text": "All 320 round, since the round version always "
                     "overrides in every seed.",
             "correct": False,
             "why": "Overriding decides what shows when both versions are "
                    "present in one seed, but half of these offspring will "
                    "receive wrinkled from BOTH parents and have nothing to "
                    "override it with."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h19",
        "band": "harder",
        "text": "A characteristic disappears for two generations and then "
                "reappears unchanged in a great-grandchild. A student says "
                "this must mean the gene 'switched off' and then 'switched "
                "back on'. Evaluate this claim, using what you know about "
                "hidden versions of genes.",
        "options": [
            {"text": "The claim is wrong — the version was carried, hidden and "
                     "unchanged, the whole time.",
             "correct": True},
            {"text": "The claim is broadly right, since 'switched off' is "
                     "another way of saying 'hidden'.",
             "correct": False,
             "why": "\"Switched off\" implies something changes about the "
                    "version itself over time. What actually happens is that "
                    "the SAME unchanged version is carried the whole time."},
            {"text": "The claim is right, and explains why the reappeared "
                     "version is weaker than before.",
             "correct": False,
             "why": "Nothing about the reappeared characteristic is weaker. A "
                    "version passed on unchanged for generations is exactly as "
                    "complete as it always was."},
            {"text": "The claim cannot be evaluated without knowing which "
                     "generation carried the mutation.",
             "correct": False,
             "why": "No mutation needs to be invoked at all. A characteristic "
                    "reappearing after being hidden for generations is exactly "
                    "what carrying-without-showing predicts."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h20",
        "band": "harder",
        "text": "In one cross, two carriers of a hidden version produce 480 "
                "offspring with 118 showing it. In another cross, a carrier is "
                "crossed with a plant pure-breeding for the hidden version, "
                "producing 240 offspring with 116 showing it. What proportion, "
                "as a percentage, does each cross show, and which is closer to "
                "its own expectation?",
        "options": [
            {"text": "About 24.6 per cent and 48.3 per cent — both crosses are "
                     "equally close to their expectations.",
             "correct": False,
             "why": "24.6 per cent is only 0.4 points from the quarter "
                    "expected, while 48.3 per cent is 1.7 points from the half "
                    "expected — not an equally close match in each case."},
            {"text": "About 24.6% and 48.3% — the first cross lands closer to "
                     "its own expectation than the second.",
             "correct": True},
            {"text": "118 per cent and 116 per cent, using each count directly "
                     "as a percentage.",
             "correct": False,
             "why": "A count of offspring is not a percentage on its own. "
                    "Dividing each count by its own total and multiplying by "
                    "100 gives about 24.6 per cent and 48.3 per cent."},
            {"text": "About 24.6 per cent and 48.3 per cent — the second cross "
                     "lands closer to its own expectation than the first does.",
             "correct": False,
             "why": "It's the other way round. 24.6 per cent is only 0.4 "
                    "points off its quarter expectation, while 48.3 per cent "
                    "is 1.7 points off its half expectation."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h21",
        "band": "harder",
        "text": "A student says the 3:1 ratio idea is 'useless for humans', "
                "since human families rarely have more than three or four "
                "children. Evaluate that claim.",
        "options": [
            {"text": "It's partly right — a family of three or four is too small a sample for a clean ratio.",
             "correct": True},
            {"text": "It is entirely correct — the ratio does not apply to "
                     "human inheritance at all.",
             "correct": False,
             "why": "The underlying mechanism — each gamete carrying one "
                    "version by chance — applies to humans exactly as it "
                    "does to peas. What's limited is the SAMPLE SIZE a "
                    "human family provides."},
            {"text": "It is entirely wrong — every human family of four "
                     "children shows a visible 3:1 pattern.",
             "correct": False,
             "why": "A sample of four is nowhere near large enough to "
                    "reliably show a proportion like 3:1. Chance alone can "
                    "easily give four children the same outcome, or none of "
                    "one kind at all."},
            {"text": "It is correct, but only because human gametes work "
                     "differently from pea gametes.",
             "correct": False,
             "why": "Human gametes carry one version of each gene by "
                    "chance in exactly the same way pea gametes do. The "
                    "real limitation is sample size, not mechanism."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h22",
        "band": "harder",
        "text": "A round-seeded plant, pure-breeding, is crossed with a "
                "round-seeded plant of unknown status. All 150 offspring are "
                "round. A second cross of the same unknown plant with a "
                "wrinkled-seeded plant gives 76 round and 74 wrinkled. What "
                "can be concluded about the unknown plant from the two crosses "
                "together?",
        "options": [
            {"text": "It must be pure-breeding for round — the first cross "
                     "alone proves this on its own.",
             "correct": False,
             "why": "The first cross alone cannot distinguish a pure-breeding "
                    "plant from a carrier, since a pure round parent in that "
                    "cross would also give all round offspring. The second "
                    "cross is what settles it."},
            {"text": "It must be carrying a hidden wrinkled version, shown by "
                     "the even split in the second cross.",
             "correct": True},
            {"text": "Nothing can be concluded, since the two crosses give "
                     "conflicting results.",
             "correct": False,
             "why": "The two results are not in conflict. All round from a "
                    "cross with pure round is consistent with the unknown "
                    "plant carrying a hidden wrinkled version, and the "
                    "near-even split with wrinkled confirms it."},
            {"text": "It must be carrying two wrinkled versions, since "
                     "wrinkled offspring appeared in cross two.",
             "correct": False,
             "why": "A plant carrying two wrinkled versions would show "
                    "wrinkled seeds itself, not round. It is described as "
                    "round-seeded, so it carries at least one round version."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h23",
        "band": "harder",
        "text": "A farmer notices that a cow that survived a harsh winter "
                "produces calves that also cope well with cold. He concludes "
                "the mother's toughened body passed the toughness directly to "
                "her calves. Using what you know about how heredity works, "
                "evaluate his conclusion.",
        "options": [
            {"text": "It's the right explanation — heredity passes on whatever "
                     "a parent experiences during its life.",
             "correct": False,
             "why": "Heredity passes on genetic information that was already "
                    "present, not events a parent lived through. A hard winter "
                    "cannot rewrite what's in a cow's gametes."},
            {"text": "It's the wrong explanation — only genetic information "
                     "already in her gametes can be passed on.",
             "correct": True},
            {"text": "It's partly right — toughness from experience is passed "
                     "on, but only for one generation.",
             "correct": False,
             "why": "No lifetime experience is passed on for even one "
                    "generation, let alone more. Only genetic information "
                    "already in the gametes can be inherited."},
            {"text": "It cannot be evaluated without knowing the calves' own "
                     "winters.",
             "correct": False,
             "why": "The calves' own experience is irrelevant to evaluating "
                    "the farmer's claim about how the MOTHER's toughness was "
                    "supposedly passed on."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h24",
        "band": "harder",
        "text": "A cross gives close to a 3:1 ratio. If 45 offspring show the "
                "hidden version, about how many would you expect to show the "
                "other version, and how many offspring in total?",
        "options": [
            {"text": "About 15 showing the other version, and about 60 in "
                     "total, keeping the 3:1 ratio the other way round.",
             "correct": False,
             "why": "Reversing the ratio like this would make the HIDDEN "
                    "version the majority, which is not what 3:1 means here. "
                    "The shown version should be about three times the 45, "
                    "which is 135."},
            {"text": "About 45 showing the other version too, split evenly "
                     "between the two.",
             "correct": False,
             "why": "An even split is what a 1:1 ratio looks like, not 3:1. "
                    "With 45 as the smaller quarter, the larger group should "
                    "be about three times as many."},
            {"text": "About 135 showing the other version, and about 180 in "
                     "total.",
             "correct": True},
            {"text": "About 90 showing the other version, and about 135 in "
                     "total.",
             "correct": False,
             "why": "Three times 45 is 135, not 90, and the total should be 45 "
                    "plus that 135, which comes to 180, not 135."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h25",
        "band": "harder",
        "text": "One student says Mendel's 3:1 ratio 'proves' inherited "
                "information is passed in discrete particles. Another says it "
                "only makes that idea 'more likely than blending, but not "
                "certain'. Which is the more defensible position, and why?",
        "options": [
            {"text": "The first — a ratio matching a prediction exactly proves "
                     "the theory behind it beyond any possible doubt.",
             "correct": False,
             "why": "Matching a prediction supports a theory; it does not rule "
                    "out every conceivable alternative explanation with the "
                    "certainty the word \"proves\" claims."},
            {"text": "Neither — ratios can never be used as evidence for how "
                     "genetic information is passed on.",
             "correct": False,
             "why": "A ratio is exactly the kind of evidence Mendel used, and "
                    "it is real evidence for particulate inheritance over "
                    "blending."},
            {"text": "The first, because Mendel repeated his experiment enough "
                     "times to remove any uncertainty.",
             "correct": False,
             "why": "No number of repeats removes uncertainty completely from "
                    "a scientific conclusion. Strong, repeated evidence "
                    "supports a theory; it does not amount to certainty beyond "
                    "all possible doubt."},
            {"text": "The second — a ratio consistent with a theory supports "
                     "it without proving it beyond doubt.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h26",
        "band": "harder",
        "text": "A hybrid between two different plant varieties has 25 "
                "chromosomes in each body cell — an odd number. What problem "
                "does that create when the hybrid tries to make its own "
                "gametes, and why?",
        "options": [
            {"text": "None — any number of chromosomes can be shared out "
                     "evenly between gametes.",
             "correct": False,
             "why": "Gametes are formed by splitting pairs, one chromosome "
                    "from each pair into each gamete. An odd number like 25 "
                    "cannot be split into whole pairs to start with."},
            {"text": "The hybrid simply produces gametes with 12.5 chromosomes "
                     "each.",
             "correct": False,
             "why": "A gamete cannot carry half a chromosome. The odd total "
                    "causes gamete formation to fail rather than to produce a "
                    "fractional number."},
            {"text": "They cannot be sorted into matching pairs, so gamete "
                     "formation breaks down.",
             "correct": True},
            {"text": "The hybrid's body cells will double their chromosome "
                     "number to make it even.",
             "correct": False,
             "why": "Body cells do not spontaneously change their chromosome "
                    "number to fix an odd total. The odd number is a problem "
                    "for the pairing step of gamete formation."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h27",
        "band": "harder",
        "text": "A separate historical case: a scientist calculates a "
                "result correctly in a private notebook but never publishes "
                "it, and thirty years later someone else publishes the same "
                "result independently and gets the credit. Does this fit "
                "the same working-scientifically point Mendel's story "
                "makes?",
        "options": [
            {"text": 'Not quite — a published-but-unused result differs from one never made available.',
             "correct": True},
            {"text": "Yes — both show a correct result arriving before it "
                     "can be used.",
             "correct": False,
             "why": "There's a real difference. Mendel's case is about a "
                    "PUBLISHED result nobody used yet; an unpublished result "
                    "was never available to anyone at all."},
            {"text": "Yes, because in both cases the original scientist "
                     "received no credit at the time.",
             "correct": False,
             "why": "Mendel's case is not really about credit — he was "
                    "read, cited a little, then rediscovered independently "
                    "later. The two situations differ in whether the result "
                    "was ever made available to others."},
            {"text": "No, because private notebooks never contain correct "
                     "results.",
             "correct": False,
             "why": "Nothing about being unpublished makes a result more "
                    "or less likely to be correct. The distinction that "
                    "matters is whether it was ever made available to "
                    "others."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h28",
        "band": "harder",
        "text": "A carrier plant (round, hidden wrinkled) is crossed with a "
                "wrinkled plant, giving roughly half round, half wrinkled "
                "offspring. One of the round offspring from this cross is then "
                "crossed with another wrinkled plant. About what proportion of "
                "this second generation would be expected to be wrinkled, and "
                "why?",
        "options": [
            {"text": "About a quarter, the usual proportion for any cross "
                     "involving a hidden version.",
             "correct": False,
             "why": "A quarter is the expectation when BOTH parents are "
                    "carriers. Here the second cross is between a carrier "
                    "(necessarily) and a plant that is pure wrinkled, which "
                    "gives about a half."},
            {"text": "None, because a round offspring cannot be carrying a "
                     "hidden version at all.",
             "correct": False,
             "why": "This particular round offspring can ONLY be carrying a "
                    "hidden wrinkled version — it received wrinkled from one "
                    "parent and round from the other, with nothing else it "
                    "could have received."},
            {"text": "All of them, since crossing with wrinkled a second time "
                     "guarantees every offspring shows wrinkled.",
             "correct": False,
             "why": "The round offspring being crossed still carries one round "
                    "version, and one round version is always enough to "
                    "override wrinkled in half of the resulting seeds."},
            {"text": "About half again — every round offspring from the first "
                     "cross must itself be a carrier.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h29",
        "band": "harder",
        "text": "A biologist proposes replacing the phrase 'hidden version' "
                "with 'silent version' in future lessons, arguing the two mean "
                "exactly the same thing. Evaluate whether anything would be "
                "lost by the change.",
        "options": [
            {"text": "Nothing would be lost — the two words are perfect "
                     "synonyms with no different implications.",
             "correct": False,
             "why": "\"Silent\" carries a suggestion of being quietened or "
                    "turned down, which \"hidden\" does not. That is a real "
                    "difference in what a learner might infer from it."},
            {"text": "Something might be lost — 'silent' suggests the version "
                     "has been quietened or reduced.",
             "correct": True},
            {"text": "Something would be lost, because 'silent' is not an "
                     "English word that can describe a gene.",
             "correct": False,
             "why": "\"Silent\" is a perfectly ordinary word that could "
                    "describe a gene version; the real concern is what it "
                    "might wrongly suggest about strength, not whether it's a "
                    "valid word."},
            {"text": "Nothing would be lost, since neither word has any "
                     "settled meaning in biology.",
             "correct": False,
             "why": "\"Hidden\" is the ordinary word for this, chosen "
                    "precisely because of the distinction being weighed here."},
        ],
        "figure": None,
    },
    {
        "id": "b10-04-h30",
        "band": "harder",
        "text": "A family pedigree shows an inherited condition skipping from "
                "a great-grandparent to a great-grandchild, missing the two "
                "generations in between even though each had several children. "
                "A student calls this 'too improbable to be inheritance'. "
                "Evaluate the claim, using the chance mechanism behind how "
                "gametes combine.",
        "options": [
            {"text": "Right — a version that skips two whole generations must "
                     "have mutated back.",
             "correct": False,
             "why": "Nothing mutates back. The same unchanged version can sit "
                    "hidden in carrier after carrier for as long as no "
                    "offspring happens to receive it from both parents."},
            {"text": "Wrong — chance alone can easily skip several generations "
                     "of carriers.",
             "correct": True},
            {"text": "Right — with several children each generation, someone "
                     "should have shown it by chance.",
             "correct": False,
             "why": "\"Should have\" describes an average over many families, "
                    "not a guarantee for one. A quarter chance failing to "
                    "appear across two generations of children is "
                    "unremarkable."},
            {"text": "It cannot be evaluated without testing every family "
                     "member's DNA.",
             "correct": False,
             "why": "The claim can be judged on the chance mechanism alone — "
                    "testing every relative would confirm carriers but isn't "
                    "needed to see the pattern described is ordinary, not "
                    "improbable."},
        ],
        "figure": None,
    },
]
