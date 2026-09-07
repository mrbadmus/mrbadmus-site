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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-05-e05",
        "band": "easier",
        "text": "A horse has 64 chromosomes in a body cell and a donkey has "
                "62. How many does a mule have?",
        "options": [
            {"text": "62, matching its donkey parent.",
             "correct": False,
             "why": "A mule gets half its chromosomes from each parent, not "
                    "all of them from one. Half of 64 and half of 62 make 63."},
            {"text": "63, half from each parent.",
             "correct": True},
            {"text": "126, a full set from each parent.",
             "correct": False,
             "why": "Gametes carry half a set. Adding two full sets would "
                    "double the number every generation, which is not what "
                    "happens."},
            {"text": "64, matching its horse parent.",
             "correct": False,
             "why": "It receives 32 from the horse and 31 from the donkey. "
                    "Taking one parent's total would ignore the other parent "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e06",
        "band": "easier",
        "text": "What is a ring species?",
        "options": [
            {"text": "A species whose members live in a circle around a "
                     "single feature, such as a lake.",
             "correct": False,
             "why": "The shape on the map is not what the term is about. It is "
                    "about who will breed with whom along a chain of "
                    "populations."},
            {"text": "A species that has been divided into two by a barrier "
                     "such as a mountain range.",
             "correct": False,
             "why": "That is two populations separated. A ring species is the "
                    "harder case, where the populations are still joined all "
                    "the way round and only the two ends refuse each other."},
            {"text": "A chain of populations where each breeds with its "
                     "neighbours but the two ends do not.",
             "correct": True},
            {"text": "A group of species that all descended from one original "
                     "species.",
             "correct": False,
             "why": "Shared ancestry is a fact about history. A ring species "
                    "is defined by which populations will breed together "
                    "today."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e07",
        "band": "easier",
        "text": "How many species do all the breeds of dog belong to?",
        "options": [
            {"text": "One, because the offspring of any two breeds can "
                     "themselves have offspring.",
             "correct": True},
            {"text": "Two, one for the large breeds and one for the small.",
             "correct": False,
             "why": "Size is appearance, and appearance is not the test. A "
                    "great dane and a chihuahua produce fertile offspring, so "
                    "they are one species."},
            {"text": "As many as there are breeds, since each breeds true.",
             "correct": False,
             "why": "Breeding true within a kennel is not the test either. Any "
                    "two breeds can produce offspring that go on to have "
                    "offspring of their own."},
            {"text": "One for every breed that can be told apart from a "
                     "single bone.",
             "correct": False,
             "why": "A vet really can do that, and it still settles nothing. "
                    "Skulls differ enormously within this one species."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e08",
        "band": "easier",
        "text": "Lions and tigers have produced ligers in captivity. What is "
                "true of the male ligers?",
        "options": [
            {"text": "They are unable to survive to adulthood.",
             "correct": False,
             "why": "Ligers grow large and live. Being unable to reproduce is "
                    "a different thing from being unable to survive."},
            {"text": "They can reproduce, which is why lions and tigers are "
                     "one species.",
             "correct": False,
             "why": "The male hybrids are infertile, and that is the evidence "
                    "that lions and tigers are two species rather than one."},
            {"text": "They can only reproduce with a lion, never with a "
                     "tiger.",
             "correct": False,
             "why": "They cannot reproduce with either. A few female hybrids "
                    "have had offspring, and the males have not."},
            {"text": "They are infertile.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e09",
        "band": "easier",
        "text": "Most British dandelions produce seed without fertilisation. "
                "What does each of those seeds grow into?",
        "options": [
            {"text": "A plant with half the parent's chromosomes.",
             "correct": False,
             "why": "Halving happens when gametes are made for fertilisation. "
                    "With no fertilisation involved, the new plant carries the "
                    "parent's full set."},
            {"text": "A clone of the parent plant.",
             "correct": True},
            {"text": "A hybrid of the parent and whichever plant pollinated "
                     "it.",
             "correct": False,
             "why": "Nothing pollinated it — that is the whole point. With no "
                    "second parent there is no mixing of any kind."},
            {"text": "A plant that varies from the parent as much as any "
                     "seedling does.",
             "correct": False,
             "why": "Ordinary seedlings vary because they receive versions "
                    "from two parents. Here the new plant is a copy of one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e10",
        "band": "easier",
        "text": "Which of these pairs is two different species?",
        "options": [
            {"text": "A great dane and a chihuahua.",
             "correct": False,
             "why": "One species, however unalike they look. Their offspring "
                    "can themselves have offspring, which is the only thing "
                    "the test asks."},
            {"text": "A labrador and a poodle.",
             "correct": False,
             "why": "Two breeds of one species. A labradoodle can have "
                    "puppies of its own, so the test is satisfied."},
            {"text": "A horse and a donkey.",
             "correct": True},
            {"text": "Two herring gulls from the same colony.",
             "correct": False,
             "why": "Birds of one population that breed together and raise "
                    "fertile young. The interesting gull case is at the two "
                    "ends of a long chain, not inside one colony."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-05-s05",
        "band": "standard",
        "text": "Botanists have named over two hundred British dandelion "
                "microspecies. Why does that number depend on the botanists "
                "rather than on the dandelions?",
        "options": [
            {"text": "Because the plants do not interbreed, so the botanists "
                     "must choose how finely to divide their inherited "
                     "differences.",
             "correct": True},
            {"text": "Because dandelions are so common that nobody has counted "
                     "them all properly yet.",
             "correct": False,
             "why": "Effort is not the difficulty. However carefully they are "
                    "studied, there is no breeding to test, so no natural line "
                    "appears in the data."},
            {"text": "Because dandelions change so quickly that the number is "
                     "out of date as soon as it is published.",
             "correct": False,
             "why": "The plants are not shifting under the botanists' feet. "
                    "The problem is that the usual test cannot be run on "
                    "organisms that clone themselves."},
            {"text": "Because botanists disagree about what the word species "
                     "means.",
             "correct": False,
             "why": "They agree on the definition perfectly well. It simply "
                    "has nothing to grip on when the organisms never "
                    "interbreed."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s06",
        "band": "standard",
        "text": "A great dane and a chihuahua cannot mate without veterinary "
                "help. Does that practical difficulty make them two species?",
        "options": [
            {"text": "Yes — if two animals cannot mate unaided, they have "
                     "separated into two species.",
             "correct": False,
             "why": "The obstacle here is a difference in size, not in "
                    "biology. Once the puppies exist they are healthy and can "
                    "have puppies of their own."},
            {"text": "Yes — needing human help means the offspring are not "
                     "natural offspring.",
             "correct": False,
             "why": "The offspring are ordinary dogs. How the mating was "
                    "arranged does not change whether the young can "
                    "reproduce."},
            {"text": "It cannot be decided, because the test can only be "
                     "applied to animals that mate unaided.",
             "correct": False,
             "why": "The test can be applied here, and it has been. What it "
                    "asks is whether the offspring are fertile, and these "
                    "are."},
            {"text": "No — the puppies are fertile, and that is the whole of "
                     "the test.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s07",
        "band": "standard",
        "text": "Lions and tigers do not meet in the wild. A student says "
                "that alone makes them two species. What is wrong with the "
                "argument?",
        "options": [
            {"text": "Nothing is wrong — living apart is exactly what "
                     "separates one species into two.",
             "correct": False,
             "why": "Living apart may be how two species came to form, but it "
                    "is not the test. Two populations of one species can be "
                    "separated by an ocean and stay one species."},
            {"text": "Living apart is not the test — what settles it here is "
                     "that the hybrids cannot reproduce.",
             "correct": True},
            {"text": "It is wrong because they do meet after all, since ligers "
                     "and tigons exist.",
             "correct": False,
             "why": "Ligers are born in captivity, where people put the "
                    "parents together. The student's fact is right; it is the "
                    "reasoning from it that fails."},
            {"text": "It is wrong because two species always have different "
                     "numbers of chromosomes.",
             "correct": False,
             "why": "They often do not. Lions and tigers have the same number, "
                    "and some quite different species share a chromosome "
                    "count."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s08",
        "band": "standard",
        "text": "Bacteria swap sections of DNA with unrelated bacteria. Why "
                "does that make deciding their species harder still, on top "
                "of their not breeding?",
        "options": [
            {"text": "Because it means bacteria are all really one species.",
             "correct": False,
             "why": "Swapping sections does not merge everything into one "
                    "group. It blurs the boundaries between groups that are "
                    "otherwise clearly different."},
            {"text": "Because it means their DNA changes far too fast for any "
                     "measurement to keep pace with it.",
             "correct": False,
             "why": "Sequences can be measured perfectly well. The difficulty "
                    "is that similarity between two bacteria may come from "
                    "swapping rather than from shared ancestry."},
            {"text": "Because the fallback method compares DNA, and DNA moving "
                     "between unrelated bacteria blurs those differences.",
             "correct": True},
            {"text": "Because swapping DNA counts as breeding, so the usual "
                     "test does apply after all.",
             "correct": False,
             "why": "Breeding means two parents producing offspring. Passing a "
                    "section of DNA to a neighbour produces no offspring at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s09",
        "band": "standard",
        "text": "A small number of female ligers have had offspring. Does "
                "that overturn the verdict that lions and tigers are two "
                "species?",
        "options": [
            {"text": "No — it is a real complication, and it is why biologists "
                     "ask how strongly two populations are separated.",
             "correct": True},
            {"text": "Yes — a single fertile hybrid is enough to show that the "
                     "two parents were one species all along.",
             "correct": False,
             "why": "The male hybrids are infertile and the two animals never "
                    "breed together in nature. A rare exception is weighed "
                    "against all of that, not allowed to cancel it."},
            {"text": "No — those offspring must have been fathered by a lion "
                     "or a tiger, so they do not count.",
             "correct": False,
             "why": "Explaining the awkward result away is not needed. The "
                    "honest position is that the exception is real and does "
                    "not overturn the weight of the rest."},
            {"text": "Yes — the definition allows no exceptions, so it must be "
                     "abandoned here.",
             "correct": False,
             "why": "A definition that strains at the edges is what you should "
                    "expect if species form gradually. Abandoning it would "
                    "throw away the answer it gives in every clear case."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s10",
        "band": "standard",
        "text": "Two animals are found to have the same number of "
                "chromosomes. Does that make them the same species?",
        "options": [
            {"text": "Yes — matching numbers are what allow two animals to "
                     "breed at all.",
             "correct": False,
             "why": "Lions and tigers both have 38 and are two species. A "
                    "matching count helps a cross work; it does not answer the "
                    "question the definition asks."},
            {"text": "Yes, as long as they also look alike enough to be "
                     "grouped together.",
             "correct": False,
             "why": "Two conditions that are both clues do not add up to a "
                    "test. Cryptic species look identical and do not "
                    "interbreed."},
            {"text": "Only if the two animals also live in the same place and "
                     "meet each other.",
             "correct": False,
             "why": "Where they live is another clue rather than the test. "
                    "Populations of one species may be separated by a "
                    "continent."},
            {"text": "No — the test is fertile offspring, and some different "
                     "species share a chromosome number.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-05-h05",
        "band": "harder",
        "text": "Around the Arctic, each gull population breeds with its "
                "neighbours, but where the two ends of the chain meet in "
                "Britain the birds behave as two species. Why is that what "
                "you should expect?",
        "options": [
            {"text": "Because gulls are unusually willing to breed with birds "
                     "unlike themselves.",
             "correct": False,
             "why": "Willingness is not what makes the chain. What matters is "
                    "that each neighbouring pair of populations is only "
                    "slightly different, and the differences add up round the "
                    "ring."},
            {"text": "Because species form gradually as populations drift "
                     "apart, so a process caught halfway has no sharp line.",
             "correct": True},
            {"text": "Because the birds at the two ends have been counted as "
                     "two species by mistake.",
             "correct": False,
             "why": "The two ends genuinely do not interbreed where they meet. "
                    "The awkwardness is real, and it is informative rather "
                    "than an error."},
            {"text": "Because the definition only applies to animals that stay "
                     "in one place all their lives.",
             "correct": False,
             "why": "There is no such restriction. The definition works "
                    "wherever breeding can be observed, and here it works "
                    "perfectly well — it simply gives different answers at "
                    "different points on the ring."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h06",
        "band": "harder",
        "text": "Two populations of fish that look alike are kept together in "
                "one large tank for three breeding seasons. Each population "
                "breeds within itself every season, nothing prevents them "
                "physically, and the two never cross. What does that suggest?",
        "options": [
            {"text": "Two species — they had the opportunity and did not "
                     "breed together, which is what separated the "
                     "pipistrelles.",
             "correct": True},
            {"text": "Nothing yet — fish often refuse to breed in captivity, "
                     "so the result cannot mean anything.",
             "correct": False,
             "why": "Each population bred within itself for three seasons, so "
                    "captivity was not stopping them. What they did not do was "
                    "cross."},
            {"text": "One species — looking alike is strong evidence, and no "
                     "hybrid was produced to contradict it.",
             "correct": False,
             "why": "Looking alike is precisely what cryptic species do. The "
                    "absence of a hybrid is evidence against one species, not "
                    "for it."},
            {"text": "One species — until a hybrid is produced and tested, the "
                     "definition cannot be applied at all.",
             "correct": False,
             "why": "Waiting for a hybrid that never comes is not neutral. "
                    "Refusing to breed when they easily could is itself the "
                    "observation."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h07",
        "band": "harder",
        "text": "Two kinds of frog share a pond and occasionally produce "
                "tadpoles together. Those tadpoles always die before reaching "
                "adulthood. One species or two?",
        "options": [
            {"text": "One — they produced offspring together, which is what "
                     "the definition asks for.",
             "correct": False,
             "why": "The definition asks for fertile offspring. A tadpole that "
                    "never becomes an adult never reproduces, so the two lines "
                    "go nowhere together."},
            {"text": "It cannot be decided — the tadpoles died before they "
                     "could be tested.",
             "correct": False,
             "why": "Dying before adulthood is the test result. Offspring that "
                    "cannot possibly reproduce answer the question as "
                    "definitely as infertile adults do."},
            {"text": "One — sharing a pond and breeding at all shows they have "
                     "not separated.",
             "correct": False,
             "why": "Horses and donkeys mate readily and are two species. "
                    "Being able to start offspring is only half of what the "
                    "definition requires."},
            {"text": "Two — no offspring of the cross ever reproduces, so the "
                     "test fails.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h08",
        "band": "harder",
        "text": "A mule is called a genetic dead end. A student takes that to "
                "mean a mule is a weak or unhealthy animal. Why is that the "
                "wrong reading?",
        "options": [
            {"text": "Mules are strong, long-lived and healthy — the dead end "
                     "is that nothing passes on beyond them.",
             "correct": True},
            {"text": "Mules are indeed weak, unhealthy animals, which is the "
                     "reason they cannot reproduce at all.",
             "correct": False,
             "why": "They have been bred deliberately for four thousand years "
                    "because they are strong and hardy. Their infertility has "
                    "nothing to do with poor health."},
            {"text": "The phrase describes the horse and donkey rather than "
                     "the mule.",
             "correct": False,
             "why": "Horses and donkeys both reproduce perfectly well within "
                    "their own species. It is the mule's own line that stops."},
            {"text": "The phrase is about the mule's own short life rather "
                     "than about its offspring.",
             "correct": False,
             "why": "Mules are notably long-lived. What ends is the line, not "
                    "the animal."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h09",
        "band": "harder",
        "text": "A mule has 63 chromosomes and is infertile. A lion and a "
                "tiger each have 38, so a liger has 38 — an even number — and "
                "male ligers are infertile too. What does the pair of cases "
                "show?",
        "options": [
            {"text": "That chromosome number has nothing to do with hybrid "
                     "infertility in either of the two cases.",
             "correct": False,
             "why": "It has a great deal to do with the mule: 63 cannot be "
                    "sorted into pairs. What the liger adds is narrower than "
                    "throwing the explanation out."},
            {"text": "That the liger numbers must be wrong, since an even "
                     "total should pair up.",
             "correct": False,
             "why": "The numbers are right, and correcting the awkward case "
                    "away is the wrong move. It is the rule being tested that "
                    "needs narrowing."},
            {"text": "That an odd number explains the mule, but an even total "
                     "is no guarantee — the sets must match.",
             "correct": True},
            {"text": "That infertility in hybrids is always caused by the two "
                     "parents having lived in different places.",
             "correct": False,
             "why": "Where the parents live cannot reach inside a cell. Lions "
                    "and tigers kept together still produce infertile male "
                    "hybrids."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h10",
        "band": "harder",
        "text": "A student says the species definition is a poor one, because "
                "it fails for bacteria, for cloning dandelions and for "
                "fossils. What is the best reply?",
        "options": [
            {"text": "He is right, and biologists should replace it with a "
                     "rule based on comparing DNA in every case.",
             "correct": False,
             "why": "A DNA rule needs a line drawn at a chosen level of "
                    "similarity. Where breeding can be tested, the definition "
                    "answers the question directly and no line has to be "
                    "chosen."},
            {"text": "It answers the question directly wherever breeding can "
                     "be tested, and where it cannot, biologists say so and "
                     "use another method.",
             "correct": True},
            {"text": "He is right, and it is why the number of species on "
                     "Earth can never be known.",
             "correct": False,
             "why": "The difficulty is real for some groups and does not "
                    "spread to all of them. For most animals and plants the "
                    "test can be applied and does settle the case."},
            {"text": "He is wrong, because the definition works for bacteria "
                     "and dandelions as well once you look closely enough.",
             "correct": False,
             "why": "Looking closely does not help when the organisms do not "
                    "breed. The honest position is that the test has known "
                    "limits, not that it secretly covers everything."},
        ],
        "figure": None,
    },
]
