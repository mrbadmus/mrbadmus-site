"""B10 lesson 05 — What makes a species: twelve questions (MRB-269).

These probe the one word the lesson turns on and the boundary the definition
has. The distractors are built from the lesson's two declared misconceptions —
GENE-09 (organisms that look alike are the same species) and GENE-10 (if two
animals can have a baby together, they are the same species) — and from the
wrong rules the page offers alongside them: that a shared chromosome number
settles it, that the name an organism already carries settles it, and that
where it lives settles it. GENE-09 is tested in BOTH directions, because that
is how the lesson refuses it: one species that looks wildly varied (the dogs)
and two species nobody could tell apart (the pipistrelles). A third seam runs
through the bank — that "the test does not settle it" is a real verdict rather
than a shrug — and its distractors are the two tidy answers a student reaches
for instead, one species or a definite number of them. The `harder` band takes
the lesson somewhere new each time: two fossils that can never be bred, a
grasshopper song mistaken for the test rather than the clue, a chain of frog
populations round a coastline, and a challenge that bacterial species are made
up.
"""

UNIT = "B10"
LESSON = "what-makes-a-species"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-05-e01",
        "band": "easier",
        "text": "Fill the gap in the definition. Two organisms are the same "
                "species if they can breed together to produce ______ "
                "offspring.",
        "options": [
            {"text": "healthy — offspring that survive and grow to a normal "
                     "size",
             "correct": False,
             "why": "A mule is healthy, strong and long-lived, and its parents "
                    "are still two species. Surviving is not the part of the "
                    "test that people drop."},
            {"text": "fertile — offspring that can go on to reproduce "
                     "themselves",
             "correct": True},
            {"text": "matching — offspring with the same number of chromosomes "
                     "as each parent",
             "correct": False,
             "why": "Chromosome number explains why the mule's cells run into "
                    "trouble, but it is not the test. Some different species "
                    "share a chromosome number."},
            {"text": "similar — offspring that clearly look like both of their "
                     "parents",
             "correct": False,
             "why": "Appearance is a clue, not the test. A mule looks like "
                    "both its parents and settles nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e02",
        "band": "easier",
        "text": "A liger has a lion for a father and a tiger for a mother. "
                "What is the word for an animal whose parents are two "
                "different species?",
        "options": [
            {"text": "A ring species, because the two parents sit at opposite "
                     "ends",
             "correct": False,
             "why": "A ring species is a chain of populations where each one "
                    "interbreeds with its neighbours but the two ends do not — "
                    "the gulls, not the liger."},
            {"text": "A cryptic species, because two species were filed under "
                     "a single name",
             "correct": False,
             "why": "Cryptic species look effectively identical, like "
                    "Britain's two pipistrelle bats. Nobody has ever confused "
                    "a lion with a tiger."},
            {"text": "A hybrid, the offspring of two different species",
             "correct": True},
            {"text": "A breed, a variety produced by crossing two kinds of "
                     "animal",
             "correct": False,
             "why": "A breed is a variety inside ONE species — a great dane is "
                    "a breed of dog. The liger's two parents are two species."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e03",
        "band": "easier",
        "text": "British pipistrelle bats were filed as one species for a "
                "century. What finally showed there were two?",
        "options": [
            {"text": "Two groups echolocated at different frequencies, roosted "
                     "apart and did not interbreed.",
             "correct": True},
            {"text": "Careful measurement showed that one group was slightly "
                     "larger than the other.",
             "correct": False,
             "why": "Nobody could separate these bats by looking, and "
                    "measuring harder would not have settled it either. "
                    "Appearance is a clue, not the test."},
            {"text": "They were found living in two different parts of "
                     "Britain.",
             "correct": False,
             "why": "One species can live in many places. Where an organism is "
                    "found is no part of the definition."},
            {"text": "Biologists gave the two groups different names, which "
                     "made them two species.",
             "correct": False,
             "why": "A name records a decision people made after the biology. "
                    "Naming them did not separate them; not interbreeding "
                    "did."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e04",
        "band": "easier",
        "text": "For organisms the breeding test cannot reach — bacteria, "
                "cloning dandelions, fossils — what do biologists use instead?",
        "options": [
            {"text": "They wait until the organisms breed, then apply the "
                     "usual test.",
             "correct": False,
             "why": "These are organisms that never breed sexually. Bacteria "
                    "divide in two and most British dandelions make clones of "
                    "themselves, so waiting changes nothing."},
            {"text": "They group together the ones that look alike and "
                     "separate the rest.",
             "correct": False,
             "why": "Appearance is where you start, not where you finish. One "
                    "species can look wildly varied, and two species can look "
                    "identical."},
            {"text": "They decide by whether the organisms already carry one "
                     "name or two.",
             "correct": False,
             "why": "A name is the conclusion somebody reached, not the "
                    "evidence for it. The biology has to come first."},
            {"text": "They compare DNA sequences and other inherited features.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-05-s01",
        "band": "standard",
        "text": "Four pairs from the bench. In which one does the breeding "
                "test fail to give an answer at all?",
        "options": [
            {"text": "A horse and a donkey, whose offspring is healthy but "
                     "cannot reproduce.",
             "correct": False,
             "why": "That is the test working exactly as designed. The "
                    "infertile mule is the evidence that its parents are two "
                    "species."},
            {"text": "A great dane and a chihuahua, which cannot mate without "
                     "veterinary help.",
             "correct": False,
             "why": "Awkward is not the same as impossible. With help the "
                    "puppies are healthy and can have puppies of their own, so "
                    "the test answers clearly: one species."},
            {"text": "Two bacteria in a dish, which reproduce by dividing "
                     "rather than breeding.",
             "correct": True},
            {"text": "A lion and a tiger, which never meet outside captivity.",
             "correct": False,
             "why": "They have bred in captivity, and the male hybrids are "
                    "infertile. The test reached a verdict: two species."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s02",
        "band": "standard",
        "text": "A false killer whale and a bottlenose dolphin have produced "
                "offspring in captivity. A student says that settles it — one "
                "species. What has she left out?",
        "options": [
            {"text": "Whether that offspring can itself reproduce, which is "
                     "the rest of the test.",
             "correct": True},
            {"text": "Nothing — producing offspring together is exactly what "
                     "the definition asks for.",
             "correct": False,
             "why": "The definition has a second word in it, and it is the one "
                    "people drop. The offspring has to be fertile, not just "
                    "born."},
            {"text": "Whether the two animals look similar enough to be "
                     "grouped together.",
             "correct": False,
             "why": "Appearance is no part of the definition. Two species can "
                    "be impossible to tell apart, and one species can vary "
                    "enormously."},
            {"text": "Whether they would ever have met and bred outside "
                     "captivity.",
             "correct": False,
             "why": "Lions and tigers only breed in captivity too, and the "
                    "test still settled them. What decides it is whether the "
                    "hybrid is fertile."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s03",
        "band": "standard",
        "text": "A great dane and a chihuahua look more different from each "
                "other than a wolf and a coyote do. What is that comparison "
                "there to show?",
        "options": [
            {"text": "That dogs vary more than any other animal, so they are a "
                     "special case.",
             "correct": False,
             "why": "Dogs are a vivid example, not an exception. The "
                    "pipistrelle bats make the same point running the other "
                    "way."},
            {"text": "That appearance can differ more within one species than "
                     "between two.",
             "correct": True},
            {"text": "That a wolf and a coyote ought to be counted as one "
                     "species after all.",
             "correct": False,
             "why": "It runs the other way. Looking alike does not make two "
                    "organisms one species, any more than looking different "
                    "makes them two."},
            {"text": "That great danes and chihuahuas are drifting apart into "
                     "two species.",
             "correct": False,
             "why": "Their puppies are fertile, so they are one species today. "
                    "Looking different is not a step on the way to becoming "
                    "two."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s04",
        "band": "standard",
        "text": "A student calls mules and ligers exceptions that break the "
                "species definition. Why is that the wrong way round?",
        "options": [
            {"text": "Because they are rare enough in nature for the "
                     "definition to ignore them.",
             "correct": False,
             "why": "Rarity is not the answer — mules have been bred "
                    "deliberately for four thousand years. The definition "
                    "handles them; it does not dodge them."},
            {"text": "Because they show the definition needs an extra rule for "
                     "animals bred by people.",
             "correct": False,
             "why": "No extra rule is needed. One sentence covers the dog "
                    "breeds, the mule and the liger alike."},
            {"text": "Because producing offspring at all proves the two "
                     "parents were one species.",
             "correct": False,
             "why": "That is the dropped word again. The offspring exists but "
                    "cannot reproduce, which is precisely why its parents "
                    "count as two species."},
            {"text": "Because their infertility is the evidence that each pair "
                     "of parents is two species.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-05-h01",
        "band": "harder",
        "text": "A palaeontologist has two fossil skeletons from one rock "
                "layer, alike except for the shape of the jaw. Why can she not "
                "use the definition this lesson gives?",
        "options": [
            {"text": "Because neither fossil can be bred, so the test can "
                     "never be run.",
             "correct": True},
            {"text": "Because two fossils are too few — she would need a much "
                     "larger sample first.",
             "correct": False,
             "why": "Sample size is a real worry, but a separate one. A "
                    "thousand fossils would still leave her with nothing she "
                    "could breed."},
            {"text": "Because the jaws differ, which already proves she has "
                     "two species.",
             "correct": False,
             "why": "One species varies enormously — think how far a great "
                    "dane is from a chihuahua. A difference you can see "
                    "settles nothing."},
            {"text": "Because the skeletons are alike, which already proves "
                     "she has one species.",
             "correct": False,
             "why": "The same mistake in reverse. Cryptic species look "
                    "effectively identical and are still two species."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h02",
        "band": "harder",
        "text": "Two groups of grasshopper in one meadow sing at clearly "
                "different pitches. A student concludes at once that they are "
                "two species. What is wrong with that?",
        "options": [
            {"text": "Nothing — a difference you can measure beats one you can "
                     "only see.",
             "correct": False,
             "why": "Measuring a difference more precisely does not change "
                    "what kind of evidence it is. Frequency separated the "
                    "pipistrelles too, and only the breeding settled them."},
            {"text": "She should have compared their appearance instead, which "
                     "is far more reliable.",
             "correct": False,
             "why": "Appearance is the weakest evidence of the lot. That is "
                    "exactly what the two identical-looking pipistrelles "
                    "show."},
            {"text": "She has treated a clue as the test; only breeding "
                     "settles it.",
             "correct": True},
            {"text": "Song is learned, so it can tell you nothing at all about "
                     "species.",
             "correct": False,
             "why": "A song can be an excellent clue — a difference in "
                    "frequency is what alerted researchers to the two "
                    "pipistrelles. The mistake is stopping at the clue."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h03",
        "band": "harder",
        "text": "Five frog populations run along a coastline. Each breeds "
                "freely with the one next to it, but the two at the ends of "
                "the chain will not breed at all. How many species is that?",
        "options": [
            {"text": "Two, because the populations at the two ends will not "
                     "breed together.",
             "correct": False,
             "why": "Tempting, but every population in between breeds with "
                    "both its neighbours, so there is nowhere along the chain "
                    "to put the boundary."},
            {"text": "No single answer — the test replies differently "
                     "depending where you apply it.",
             "correct": True},
            {"text": "Five, because each population is separated from the ones "
                     "on either side.",
             "correct": False,
             "why": "They breed freely with their neighbours, so the test "
                    "calls neighbours one species. Only the two ends fail it."},
            {"text": "One, because you can travel from either end to the other "
                     "through interbreeding populations.",
             "correct": False,
             "why": "That ignores the ends, where the test plainly says two. "
                    "Both answers are defensible, and that is the point."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h04",
        "band": "harder",
        "text": "Biologists sort bacteria by comparing DNA and drawing a line "
                "at a chosen level of similarity. A student says that makes "
                "bacterial species made up rather than real. Best reply?",
        "options": [
            {"text": "He is right — a boundary that people chose cannot be a "
                     "fact about nature.",
             "correct": False,
             "why": "What is chosen is where to draw the line, not whether the "
                    "differences are there. Chosen and useful is not the same "
                    "as invented."},
            {"text": "He is wrong, because bacteria do breed and the ordinary "
                     "test works on them.",
             "correct": False,
             "why": "Bacteria divide in two rather than breeding, and they "
                    "swap DNA with unrelated bacteria. That is precisely why a "
                    "different method is needed."},
            {"text": "He is wrong, because every biologist agrees on exactly "
                     "where the line goes.",
             "correct": False,
             "why": "The lesson calls that line agreed and openly somewhat "
                    "arbitrary. Pretending it is exact is not the defence."},
            {"text": "The line is chosen because breeding cannot be tested, "
                     "but the differences are real.",
             "correct": True},
        ],
        "figure": None,
    },
]
