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
    {
        "id": "b10-05-e11",
        "band": "easier",
        "text": "Which best defines the word 'hybrid'?",
        "options": [
            {"text": "Any animal that has been bred by humans rather than "
                     "occurring in the wild.",
             "correct": False,
             "why": "Plenty of human-bred animals, like a labrador, are still "
                    "just one species crossed with itself. A hybrid "
                    "specifically has two different species as parents."},
            {"text": "An animal that cannot be classified into any species at "
                     "all.",
             "correct": False,
             "why": "A hybrid is still classifiable — it simply has two "
                    "different species as its parents, rather than sitting "
                    "outside classification altogether."},
            {"text": "A variety of one species kept for a particular purpose, "
                     "such as a working dog.",
             "correct": False,
             "why": "That describes a breed, not a hybrid. A breed's parents "
                    "are both the same species; a hybrid's parents are two "
                    "different ones."},
            {"text": "The offspring of two different species.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e12",
        "band": "easier",
        "text": "Which best defines a 'cryptic species'?",
        "options": [
            {"text": 'Two species that look almost identical.',
             "correct": True},
            {"text": "A species that has not yet been given a scientific "
                     "name.",
             "correct": False,
             "why": "Naming is a separate matter. A cryptic species is one "
                    "that looks like another species, not one that lacks a "
                    "name."},
            {"text": "A species that lives underground or out of sight.",
             "correct": False,
             "why": "Nothing about where an organism lives is what "
                    "\"cryptic\" refers to here. It's about looking like a "
                    "different species."},
            {"text": "A species made entirely of clones of a single "
                     "original individual.",
             "correct": False,
             "why": "That describes something closer to the dandelion case. "
                    "A cryptic species is about resembling a DIFFERENT "
                    "species closely enough to be confused with it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e13",
        "band": "easier",
        "text": "Which of these is an example of a ring species?",
        "options": [
            {"text": "The two pipistrelle bats that were filed under one name.",
             "correct": False,
             "why": "The pipistrelles are a cryptic-species case, not a ring "
                    "species — nothing about them forms a chain of "
                    "populations."},
            {"text": "The great dane and the chihuahua.", "correct": False,
             "why": "Those are two breeds of one species, with no chain of "
                    "populations involved."},
            {"text": "The chain of gull populations circling the Arctic.",
             "correct": True},
            {"text": "The bacteria compared by their DNA.", "correct": False,
             "why": "Bacteria are grouped by comparing DNA, which has nothing "
                    "to do with a chain of interbreeding populations."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e14",
        "band": "easier",
        "text": "Two rabbits from the same breeding population mate and "
                "produce young that themselves go on to have young. What "
                "verdict does the fertile-offspring definition give for the "
                "two original rabbits?",
        "options": [
            {"text": "They cannot be judged until their young have also been "
                     "examined for looks.",
             "correct": False,
             "why": "Appearance plays no part in the test. The offspring being "
                    "able to reproduce is already enough to settle it."},
            {"text": "They must belong to different species, since crossing is "
                     "how new species form.",
             "correct": False,
             "why": "Crossing within one species is entirely ordinary — that's "
                    "how members of a single species always reproduce."},
            {"text": "The test cannot decide, since only one pair of rabbits "
                     "was observed.",
             "correct": False,
             "why": "One pair producing offspring that can themselves "
                    "reproduce is exactly what the test asks for. Nothing "
                    "further is needed here."},
            {"text": "They are the same species.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e15",
        "band": "easier",
        "text": "For most animals, why do biologists use the breeding test "
                "rather than comparing DNA to decide on species?",
        "options": [
            {"text": "Because DNA cannot be extracted from most animals.",
             "correct": False,
             "why": "DNA can be extracted from almost any living organism. The "
                    "reason breeding is preferred is that it answers the "
                    "species question directly."},
            {"text": "Because comparing DNA always gives the wrong answer for "
                     "animals.",
             "correct": False,
             "why": "DNA comparison isn't wrong, it's just not needed when "
                    "breeding CAN be tested directly. It becomes the fallback "
                    "only when breeding cannot be observed."},
            {"text": "Because the breeding test answers the question directly.",
             "correct": True},
            {"text": "Because the breeding test is quicker to carry out in a "
                     "laboratory.",
             "correct": False,
             "why": "The breeding test isn't really about speed. It's used "
                    "because it answers the actual question directly."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e16",
        "band": "easier",
        "text": "Fill the gap. Appearance is a ______, not the test.",
        "options": [
            {"text": "clue", "correct": True},
            {"text": "rule", "correct": False,
             "why": "Appearance is explicitly described as not being a "
                    "rule that decides anything on its own."},
            {"text": "requirement", "correct": False,
             "why": "Nothing about appearance is required for the test. "
                    "The test is entirely about whether offspring can "
                    "reproduce."},
            {"text": "guarantee", "correct": False,
             "why": "Appearance guarantees nothing about species membership "
                    "in either direction — that's the whole point of the "
                    "dogs and the bats."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e17",
        "band": "easier",
        "text": "How many chromosomes does a horse have, and how many does a "
                "donkey have?",
        "options": [
            {"text": "62 and 64.", "correct": False,
             "why": "The numbers are swapped. It's the horse that has 64, and "
                    "the donkey 62."},
            {"text": "63 and 63.", "correct": False,
             "why": "63 is the number in the MULE, not in either parent. The "
                    "horse has 64 and the donkey 62."},
            {"text": "64 and 64.", "correct": False,
             "why": "The two parent species do not share the same number. The "
                    "horse has 64 and the donkey 62 — why their hybrid ends up "
                    "with an odd 63."},
            {"text": "64 and 62.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e18",
        "band": "easier",
        "text": "How many chromosomes does a mule have, and is that number odd "
                "or even?",
        "options": [
            {"text": "63, an even number.", "correct": False,
             "why": "63 is odd, not even — which matters, because an odd "
                    "number cannot be sorted into matching pairs."},
            {"text": "63, an odd number.", "correct": True},
            {"text": "64, an even number.", "correct": False,
             "why": "64 is the horse's own number. The mule, receiving half "
                    "from each parent, ends up with 63."},
            {"text": "62, an even number.", "correct": False,
             "why": "62 is the donkey's own number, not the mule's. The mule "
                    "receives half from each parent, giving 63."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e19",
        "band": "easier",
        "text": "A labrador and a poodle can be crossed to produce a "
                "labradoodle, which can itself have puppies. What does that "
                "tell you about labradors and poodles?",
        "options": [
            {"text": "They are two breeds that happen to share a species name "
                     "by coincidence.",
             "correct": False,
             "why": "The shared species membership isn't a naming coincidence "
                    "— it follows directly from the labradoodle being able to "
                    "reproduce."},
            {"text": "They must be genetically identical to each other.",
             "correct": False,
             "why": "Being one species does not mean being genetically "
                    "identical. Breeds within one species can look and vary "
                    "enormously."},
            {"text": "They are one species.", "correct": True},
            {"text": "Nothing can be concluded without comparing their DNA as "
                     "well.",
             "correct": False,
             "why": "Nothing more is needed here. A fertile hybrid between "
                    "them is already the whole test, answered."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e20",
        "band": "easier",
        "text": "Why does the breeding test not work on bacteria?",
        "options": [
            {"text": "Bacteria are too small to observe breeding under a "
                     "microscope.",
             "correct": False,
             "why": "Size is not the obstacle. The real reason is that "
                    "bacteria don't breed at all — they divide."},
            {"text": "Bacteria live too briefly for the test to be carried "
                     "out.",
             "correct": False,
             "why": "How long an organism lives is not the issue. Bacteria "
                    "reproduce by dividing, not by breeding, so there is no "
                    "breeding to test."},
            {"text": "Bacteria only ever reproduce by dividing, never by "
                     "breeding.",
             "correct": True},
            {"text": "Bacteria have no DNA for scientists to compare.",
             "correct": False,
             "why": "Bacteria do have DNA, and comparing it is exactly the "
                    "method biologists fall back on. What fails is the "
                    "breeding test itself."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e21",
        "band": "easier",
        "text": "Why does the breeding test not work on most British "
                "dandelions?",
        "options": [
            {"text": "They grow too fast for the test to keep up with them.",
             "correct": False,
             "why": "Growth speed has nothing to do with it. The real reason "
                    "is that most produce seed without fertilisation at all."},
            {"text": "They produce seed without fertilisation, making clones.",
             "correct": True},
            {"text": "Dandelions have too few chromosomes to be tested.",
             "correct": False,
             "why": "Chromosome number is not the obstacle here. The issue is "
                    "that there is no interbreeding to observe in the first "
                    "place."},
            {"text": "Dandelion seeds cannot be grown in a school setting.",
             "correct": False,
             "why": "Growing conditions have nothing to do with why the test "
                    "fails. It's that most dandelions clone themselves rather "
                    "than interbreeding."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e22",
        "band": "easier",
        "text": "In a ring species, what is true of neighbouring populations "
                "along the chain?",
        "options": [
            {"text": "Each one interbreeds successfully with the "
                     "populations next to it.",
             "correct": True},
            {"text": "None of them can interbreed with any other "
                     "population in the chain.",
             "correct": False,
             "why": "That's the opposite of what makes it a ring species. "
                    "Neighbouring populations DO interbreed; it's only the "
                    "two ends that do not."},
            {"text": "They interbreed only with populations at the two "
                     "ends of the chain.",
             "correct": False,
             "why": "It's the other way round. Neighbours interbreed with "
                    "each other, while the two ends of the chain do not."},
            {"text": "They stop interbreeding once the chain reaches a "
                     "certain length.",
             "correct": False,
             "why": "Length of the chain doesn't switch anything off. Each "
                    "neighbouring pair simply interbreeds, all the way "
                    "round, except at the two ends."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e23",
        "band": "easier",
        "text": "What is the third verdict biologists can reach, alongside "
                "'same species' and 'different species'?",
        "options": [
            {"text": "The test does not settle it.", "correct": True},
            {"text": "Possibly the same species.", "correct": False,
             "why": "That's a hedge rather than the actual third verdict, "
                    "which is that the test itself cannot answer the question "
                    "in some cases."},
            {"text": "A new species is forming.", "correct": False,
             "why": "That might be true in some ring-species-like cases, but "
                    "it isn't the name of the third verdict itself."},
            {"text": "Insufficient data collected.", "correct": False,
             "why": "The third verdict isn't about needing more data — it's "
                    "that the breeding test cannot be applied to these "
                    "organisms, however much is collected."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e24",
        "band": "easier",
        "text": "What is true of most male ligers?",
        "options": [
            {"text": "They cannot survive past infancy.", "correct": False,
             "why": "Ligers can grow to adulthood and live for years. Being "
                    "unable to reproduce is separate from being unable to "
                    "survive."},
            {"text": "They can reproduce freely with either lions or tigers.",
             "correct": False,
             "why": "Male ligers are infertile and cannot reproduce with "
                    "either parent species."},
            {"text": "They are infertile.", "correct": True},
            {"text": "They are always born female.", "correct": False,
             "why": "Ligers are born of both sexes; it's specifically the "
                    "males that are infertile."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e25",
        "band": "easier",
        "text": "A mule is sometimes called a 'genetic dead end'. What does "
                "that phrase mean?",
        "options": [
            {"text": "It has fewer genes than either of its parents.",
             "correct": False,
             "why": "A mule inherits a full working set from each parent, just "
                    "as any offspring does. The phrase is about reproduction, "
                    "not gene count."},
            {"text": "It will die young, before either of its parents.",
             "correct": False,
             "why": "Mules are typically strong and long-lived. The phrase "
                    "describes its inability to reproduce, not its lifespan."},
            {"text": "It cannot reproduce, so its inheritance goes no further.",
             "correct": True},
            {"text": "Its genes are damaged by combining two different "
                     "species.",
             "correct": False,
             "why": "Nothing about a mule's genes is damaged. The problem is "
                    "purely about pairing 63 chromosomes for gamete formation."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e26",
        "band": "easier",
        "text": "A horse and a donkey mate and produce a mule, which cannot "
                "reproduce. What verdict does the definition give for the "
                "horse and the donkey?",
        "options": [
            {"text": "Same species, since they were able to produce offspring "
                     "together.",
             "correct": False,
             "why": "Producing offspring is only half the test. The offspring "
                    "must also be able to reproduce, and the mule cannot."},
            {"text": "The test does not settle it, since a mule did result "
                     "from the cross.",
             "correct": False,
             "why": "The test settles this cleanly — an infertile hybrid is "
                    "precisely the evidence for two species, not a reason to "
                    "call it unclear."},
            {"text": "Different species.", "correct": True},
            {"text": "Same species, because the mule looks like both its "
                     "parents.",
             "correct": False,
             "why": "Appearance plays no part in the test. What decides it is "
                    "whether the mule itself can reproduce, and it cannot."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e27",
        "band": "easier",
        "text": "Two neighbouring gull populations in the ring interbreed "
                "happily. What verdict would the definition give for those two "
                "populations, considered on their own?",
        "options": [
            {"text": "Different species, since they are part of a ring species "
                     "overall.",
             "correct": False,
             "why": "The ring as a WHOLE is what turns out unclear. Any one "
                    "neighbouring pair, looked at on its own, interbreeds "
                    "successfully."},
            {"text": "The test does not settle it, because the whole ring is "
                     "complicated.",
             "correct": False,
             "why": "The complication belongs to the ring taken as a whole, at "
                    "its two ends. A single neighbouring pair gives a clean "
                    "verdict."},
            {"text": "Same species, but only because they live in the same "
                     "region.",
             "correct": False,
             "why": "Living in the same region is not the test. What settles "
                    "it here is that this pair genuinely interbreeds."},
            {"text": "Same species — considered just as a pair, they "
                     "interbreed successfully.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e28",
        "band": "easier",
        "text": "Two dandelion clones, each a copy of a different parent "
                "plant, are compared. Why can't 'same species' or 'different "
                "species' be settled for them by the usual test?",
        "options": [
            {"text": "They look too similar to be told apart.",
             "correct": False,
             "why": "Looking alike is a separate issue from whether the test "
                    "can even be applied. These dandelions clone themselves "
                    "and never interbreed, which is the real obstacle."},
            {"text": "They have too many chromosomes for a fertility test to "
                     "work.",
             "correct": False,
             "why": "Chromosome number isn't the obstacle. It's that they "
                    "reproduce by cloning rather than breeding at all."},
            {"text": "They never interbreed, so there's nothing to test.",
             "correct": True},
            {"text": "Dandelions have not been studied for long enough.",
             "correct": False,
             "why": "How long they've been studied makes no difference. The "
                    "test fails here because there is no interbreeding to "
                    "observe."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e29",
        "band": "easier",
        "text": "Two bacteria are found to have very similar DNA. What do "
                "biologists do with that information, given that bacteria do "
                "not breed?",
        "options": [
            {"text": "Ignore it, since only breeding results count towards "
                     "deciding species.",
             "correct": False,
             "why": "For organisms that don't breed at all, DNA comparison "
                    "isn't ignored — it's exactly the fallback method used."},
            {"text": "Use it to judge species membership against a chosen "
                     "threshold.",
             "correct": True},
            {"text": "Use it to prove the two bacteria are exactly the same "
                     "individual.",
             "correct": False,
             "why": "Similar DNA between two bacteria says something about "
                    "species-level classification, not that they are literally "
                    "the same individual organism."},
            {"text": "Use it to work out how fertile the bacteria are.",
             "correct": False,
             "why": "Bacteria don't reproduce sexually at all, so fertility in "
                    "the usual sense doesn't apply to them."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-e30",
        "band": "easier",
        "text": "A student says 'the test does not settle it' really just "
                "means 'nobody knows the answer'. Is that a fair description?",
        "options": [
            {"text": "No — each unclear case names a reason and an alternative "
                     "method.",
             "correct": True},
            {"text": "Yes — the third verdict is exactly the same as saying "
                     "nobody knows.",
             "correct": False,
             "why": "Each 'unclear' case comes with a clear explanation of why "
                    "the ordinary test cannot apply, and a genuine alternative "
                    "method, which is more than not knowing."},
            {"text": "Yes, since biologists have never studied bacteria, "
                     "dandelions or gulls closely.",
             "correct": False,
             "why": "All three have been studied in detail — the "
                    "DNA-comparison method and the careful mapping of the gull "
                    "populations are themselves the result of that study."},
            {"text": "No, because the third verdict only ever applies to "
                     "gulls.",
             "correct": False,
             "why": "The third verdict applies to bacteria and dandelions as "
                    "well as the gulls, and all three are cases where the "
                    "ordinary test cannot be run."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s11",
        "band": "standard",
        "text": "Population X and Population Y of a fish can be bred together "
                "in a lab. The offspring survive well but none of them can "
                "produce young of their own. What verdict does the "
                "fertile-offspring test give, and why doesn't survival alone "
                "settle it?",
        "options": [
            {"text": "Same species — the offspring survived well, which is the "
                     "test.",
             "correct": False,
             "why": "Surviving is not what the definition asks for. It "
                    "specifically requires the offspring to be able to "
                    "reproduce, which none of them can here."},
            {"text": "Different species — surviving is not enough; the "
                     "offspring must be able to reproduce too.",
             "correct": True},
            {"text": "The test does not settle it, since survival and "
                     "reproduction give conflicting evidence.",
             "correct": False,
             "why": "There's no real conflict — surviving offspring that "
                    "cannot reproduce is exactly the pattern, as with the "
                    "mule, that gives a clean 'different species' verdict."},
            {"text": "Same species, because being bred successfully in a lab "
                     "is the test, wherever it happens.",
             "correct": False,
             "why": "Where the breeding takes place makes no difference. What "
                    "decides it is whether the resulting offspring can "
                    "themselves reproduce, and here they cannot."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s12",
        "band": "standard",
        "text": "In captivity, two closely related bird species produce hybrid "
                "offspring. Almost all the hybrids are infertile, but a "
                "handful of females have gone on to lay fertile eggs. Does "
                "that rare exception overturn a verdict of 'different "
                "species'?",
        "options": [
            {"text": "Yes — a single fertile hybrid is enough to reclassify "
                     "the two as one species.",
             "correct": False,
             "why": "A rare exception like this is a genuine complication, not "
                    "something that cancels out an otherwise consistent "
                    "pattern of infertility."},
            {"text": "Yes, because the definition allows no exceptions of any "
                     "kind.",
             "correct": False,
             "why": "Real biology does throw up occasional exceptions to a "
                    "clean rule, and the honest response is to weigh them "
                    "rather than abandon the whole definition."},
            {"text": "No, because the fertile females' eggs must have been "
                     "fertilised by males of only one of the two species.",
             "correct": False,
             "why": "Explaining the awkward result away isn't necessary. The "
                    "honest position is that the exception is real and does "
                    "not overturn the weight of the rest."},
            {"text": "No — a rare exception is weighed against the overall "
                     "pattern rather than allowed to overturn it on its own.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s13",
        "band": "standard",
        "text": "Biologists classifying bacteria draw their species boundary "
                "at a chosen level of DNA similarity. Why is 'chosen' the "
                "right word rather than 'discovered'?",
        "options": [
            {"text": "Because bacterial DNA is entirely random and contains no "
                     "real patterns at all.",
             "correct": False,
             "why": "Bacterial DNA is not random — there really are patterns "
                    "of similarity and difference. What's chosen is the level "
                    "treated as the species boundary."},
            {"text": "Because with no breeding to test, there's no natural "
                     "boundary to discover.",
             "correct": True},
            {"text": "Because bacteria evolve too quickly for any boundary to "
                     "stay accurate.",
             "correct": False,
             "why": "Speed of change is separate from why the line is "
                    "described as chosen. Even a slowly changing population "
                    "would still need a level of similarity decided on, with "
                    "no breeding test to fall back on."},
            {"text": "Because different countries use different definitions of "
                     "a bacterial species.",
             "correct": False,
             "why": "The reason the line is 'chosen' is about the biology "
                    "itself — no breeding test is available — not about "
                    "disagreement between countries."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s14",
        "band": "standard",
        "text": "A botanist studying a newly discovered cloning plant wants to "
                "know how many species are present in a collection of a "
                "thousand individuals. Why can genetics alone not give a "
                "single definite number?",
        "options": [
            {"text": "Because cloning plants have no DNA for comparison.",
             "correct": False,
             "why": "Cloning plants have DNA just as any organism does; "
                    "comparing it is exactly how such cases are approached. "
                    "The difficulty is the missing natural boundary."},
            {"text": "With no interbreeding to test, the number depends on how "
                     "finely differences are divided.",
             "correct": True},
            {"text": "Because a thousand individuals is not a large enough "
                     "sample to study properly.",
             "correct": False,
             "why": "Sample size is not the obstacle here. Even studying every "
                    "individual that exists, there's still no interbreeding to "
                    "define a natural boundary."},
            {"text": "Because clones are identical to their parent, so they "
                     "are automatically one species.",
             "correct": False,
             "why": "Clones being genetically identical to their SINGLE parent "
                    "doesn't settle how many different lines exist across the "
                    "whole population."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s15",
        "band": "standard",
        "text": "Explain, using the chromosome numbers, why a mule is almost "
                "always unable to reproduce.",
        "options": [
            {"text": "A mule has too few chromosomes overall to make "
                     "functioning gametes.",
             "correct": False,
             "why": "63 is not a small number — it's the ARITHMETIC (an odd "
                    "total) rather than the overall count that causes the "
                    "problem."},
            {"text": "A mule's chromosomes come entirely from its horse "
                     "parent, leaving none from the donkey.",
             "correct": False,
             "why": "A mule receives chromosomes from both parents — 32 from "
                    "the horse and 31 from the donkey. The issue is that 63 in "
                    "total is odd."},
            {"text": "A mule's cells actively destroy half its chromosomes as "
                     "it grows.",
             "correct": False,
             "why": "Nothing is destroyed. The mule keeps all 63 chromosomes "
                    "throughout its life; the problem is purely the odd total "
                    "for gamete formation."},
            {"text": "A mule has 63 chromosomes — an odd number that can never "
                     "be sorted into matching pairs.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s16",
        "band": "standard",
        "text": "A chain of four salamander populations runs along a valley. "
                "Each population breeds with its immediate neighbours, but the "
                "two populations at the ends of the chain do not breed with "
                "each other. What verdict does the test give for the whole "
                "chain?",
        "options": [
            {"text": "One species, because you can trace a path of "
                     "interbreeding from one end to the other.",
             "correct": False,
             "why": "That ignores the two ends, which genuinely do not "
                    "interbreed. A verdict that only looks at the middle "
                    "misses the point of a chain species."},
            {"text": "Four species, one for each population, since each is "
                     "somewhat separated from its neighbours.",
             "correct": False,
             "why": "Neighbouring populations DO interbreed successfully here, "
                    "so the test calls each neighbouring pair one species. "
                    "Only the two ends fail it."},
            {"text": "No single answer — the test's result depends on which "
                     "two populations you compare.",
             "correct": True},
            {"text": "Two species, split down the middle of the chain.",
             "correct": False,
             "why": "There's no natural midpoint where the test changes its "
                    "answer. Every neighbouring pair interbreeds; only the two "
                    "ends do not."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s17",
        "band": "standard",
        "text": "Before the 1990s, British pipistrelle bats were treated as "
                "one species. What kind of evidence changed that, and what "
                "kind of evidence did not?",
        "options": [
            {"text": "A difference in size changed it; frequency was not "
                     "involved at all.",
             "correct": False,
             "why": "No meaningful size difference was ever found between the "
                    "two groups. What changed the classification was their "
                    "echolocation frequency and their not interbreeding."},
            {"text": "A change in where the bats were found changed it; "
                     "breeding behaviour was not involved.",
             "correct": False,
             "why": "Location isn't part of the definition. What mattered was "
                    "that the two groups roosted apart and did not interbreed, "
                    "alongside their different frequencies."},
            {"text": "Echolocation frequency and breeding behaviour changed "
                     "it; appearance did not.",
             "correct": True},
            {"text": "New fossil evidence changed it; living bats were not "
                     "examined directly.",
             "correct": False,
             "why": "Pipistrelles are living animals, and it was direct study "
                    "of living bats — their calls and their breeding — that "
                    "revealed the split."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s18",
        "band": "standard",
        "text": "Fungi often reproduce by releasing spores rather than by the "
                "two-parent breeding most animals use. What would you predict "
                "about applying the fertile-offspring species test to fungi, "
                "and why?",
        "options": [
            {"text": "It would work perfectly, since spores are a kind of "
                     "gamete.",
             "correct": False,
             "why": "Producing spores is not the same as two individuals "
                    "breeding together. Without ordinary breeding to observe, "
                    "the usual test has nothing to test."},
            {"text": "It would face the same problem as bacteria and "
                     "dandelions.",
             "correct": True},
            {"text": "It would be easier than usual, since fungi produce huge "
                     "numbers of spores.",
             "correct": False,
             "why": "Producing large numbers of spores doesn't help apply a "
                    "test that depends on breeding between two individuals — "
                    "it's the ABSENCE of that reproduction that matters."},
            {"text": "It would not apply at all, because fungi have no DNA to "
                     "compare.",
             "correct": False,
             "why": "Fungi certainly have DNA, and it could be compared as "
                    "bacterial DNA is. The prediction is about the ordinary "
                    "breeding test running into difficulty."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s19",
        "band": "standard",
        "text": "A biologist finds two beetle populations that look identical "
                "under a microscope but never interbreed when kept together, "
                "and two other beetle populations that look very different but "
                "interbreed freely and produce fertile young. How many species "
                "are described here?",
        "options": [
            {"text": "Four — since all four populations look or behave "
                     "differently from each other in some way.",
             "correct": False,
             "why": "How many populations there are isn't the same question as "
                    "how many SPECIES there are. Four populations here work "
                    "out to two species-level verdicts."},
            {"text": "One, because looking alike is stronger evidence than "
                     "breeding behaviour.",
             "correct": False,
             "why": "It's the other way round. Breeding behaviour is the test; "
                    "looking alike is only a clue, and here it misleads for "
                    "the first pair."},
            {"text": "Two — the identical-looking pair are two species and the "
                     "different-looking pair are one species.",
             "correct": True},
            {"text": "Two species for the identical-looking pair, and two "
                     "species for the interbreeding pair as well.",
             "correct": False,
             "why": "The pair that interbreeds freely and produces fertile "
                    "young is exactly what the test calls ONE species, "
                    "whatever they happen to look like."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s20",
        "band": "standard",
        "text": "A museum has labelled two fossil skulls with two different "
                "scientific names, based on their shape. A student argues that "
                "since they already have two different names, they must be two "
                "different species. What is wrong with that argument?",
        "options": [
            {"text": "Nothing is wrong — a scientific name is only given once "
                     "the species question has been definitely settled.",
             "correct": False,
             "why": "Naming does not require the breeding question to be "
                    "settled first, and for fossils it usually cannot be "
                    "settled at all. A name can be given on shape alone."},
            {"text": "The argument is wrong because fossils cannot be given "
                     "scientific names.",
             "correct": False,
             "why": "Fossils are given scientific names all the time. The "
                    "problem is treating that name as proof of the species "
                    "question, when the breeding test can never be run."},
            {"text": "The argument is wrong because the two skulls must belong "
                     "to the same individual animal.",
             "correct": False,
             "why": "Nothing here suggests the two skulls are from one "
                    "individual. The argument's flaw is treating a name as "
                    "evidence, not the number of skulls."},
            {"text": "A name is a decision people made, possibly on shape "
                     "alone; it is not evidence of fertility.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s21",
        "band": "standard",
        "text": "A textbook says the line biologists draw when comparing "
                "bacterial DNA is 'invented, so it means nothing real'. "
                "Explain what is wrong with the word 'invented' here.",
        "options": [
            {"text": "Nothing is wrong — 'invented' is exactly the right word, "
                     "since people decided where to draw the line.",
             "correct": False,
             "why": "Choosing WHERE to draw a line is not the same as "
                    "inventing what's on either side of it. The DNA "
                    "differences themselves are real, measured data."},
            {"text": "The level of similarity is chosen, but the underlying "
                     "DNA differences are real, not invented.",
             "correct": True},
            {"text": "The word is wrong because every biologist draws the line "
                     "at exactly the same point.",
             "correct": False,
             "why": "The line is agreed by convention rather than forced to "
                    "sit at one exact point — which is part of why 'chosen' "
                    "rather than 'discovered' is accurate."},
            {"text": "The word is wrong because bacteria do not actually have "
                     "DNA to compare.",
             "correct": False,
             "why": "Bacteria do have DNA, and comparing it is precisely the "
                    "method used. The DNA differences being real is exactly "
                    "why 'invented' is the wrong word."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s22",
        "band": "standard",
        "text": "A mule (horse × donkey) and a male liger (lion × tiger) are "
                "both infertile. Is the reason the same in both cases?",
        "options": [
            {"text": "Yes — both must have an odd number of chromosomes, since "
                     "both are infertile.",
             "correct": False,
             "why": "Lions and tigers both have 38 chromosomes, so a liger has "
                    "an even 38 as well. Infertility here cannot be explained "
                    "by an odd total as the mule's can."},
            {"text": "Yes, because all hybrid infertility has one single cause "
                     "across every species.",
             "correct": False,
             "why": "The mule case shows one specific mechanism, but the same "
                    "explanation cannot be assumed to cover every hybrid, as "
                    "the liger's even chromosome count shows."},
            {"text": "No comparison is possible, since lions and tigers never "
                     "breed in the wild.",
             "correct": False,
             "why": "Whether they breed in the wild or only in captivity "
                    "doesn't prevent comparing the chromosome arithmetic of "
                    "the two hybrids."},
            {"text": "Not necessarily the same mechanism in both.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s23",
        "band": "standard",
        "text": "A wholphin (the hybrid of a false killer whale and a "
                "bottlenose dolphin) has been born in captivity and has itself "
                "gone on to have a calf. What does that additional fact do to "
                "the earlier verdict on the two parent species?",
        "options": [
            {"text": "It settles the question completely in favour of 'same "
                     "species', with no further discussion needed.",
             "correct": False,
             "why": "One fertile hybrid is real evidence, but rarity and "
                    "context matter too — it's a genuine complication to "
                    "weigh, not an instant, final verdict."},
            {"text": "It makes no difference at all, since the hybrid's own "
                     "fertility is irrelevant to its parents' species.",
             "correct": False,
             "why": "The hybrid's own ability to reproduce is exactly the kind "
                    "of evidence the definition is built on."},
            {"text": "It proves the parents were always considered the same "
                     "species by biologists.",
             "correct": False,
             "why": "False killer whales and bottlenose dolphins are usually "
                    "classified as different species; a fertile hybrid is a "
                    "genuine complication, not proof otherwise."},
            {"text": "It complicates it — a fertile hybrid is real evidence "
                     "toward 'same species', to be weighed carefully.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s24",
        "band": "standard",
        "text": "Two rabbit breeds differ hugely in size, much like the great "
                "dane and the chihuahua. What does the species test say about "
                "them, assuming any two breeds can interbreed and produce "
                "fertile young?",
        "options": [
            {"text": "One species — size difference is appearance, and "
                     "appearance is not the test.",
             "correct": True},
            {"text": "Two species, since the size difference is too large to "
                     "be within one species.",
             "correct": False,
             "why": "How large a size difference looks is not part of the "
                    "definition. The dog breeds show exactly how much "
                    "variation can exist within a single species."},
            {"text": "The test does not settle it, since the definition was "
                     "not written with rabbits in mind.",
             "correct": False,
             "why": "The same definition applies to any organism, not only the "
                    "ones usually used as examples. If they can interbreed and "
                    "produce fertile young, that answers it."},
            {"text": "Two species, unless the two breeds happen to live in the "
                     "same hutch.",
             "correct": False,
             "why": "Where the rabbits live plays no part in the definition. "
                    "What settles it is whether they can interbreed and "
                    "produce fertile offspring."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s25",
        "band": "standard",
        "text": "A cross between two plant populations produces offspring that "
                "are fertile, but far less fertile than either parent "
                "population on its own. Does that make the two populations one "
                "species or two?",
        "options": [
            {"text": "Two species, since reduced fertility is itself a sign of "
                     "a species boundary.",
             "correct": False,
             "why": "The definition asks a yes/no question — can the offspring "
                    "reproduce — not a question about how well. Being ABLE to "
                    "reproduce still satisfies the test."},
            {"text": "The clean answer is one species — the test only asks "
                     "whether offspring CAN reproduce.",
             "correct": True},
            {"text": "The test does not settle it, since 'far less fertile' is "
                     "too vague a description.",
             "correct": False,
             "why": "However reduced, the offspring being fertile at all is "
                    "what the test needs. This case does not carry the same "
                    "kind of doubt as the ring species or bacteria."},
            {"text": "One species, but only once every individual offspring "
                     "has been checked personally.",
             "correct": False,
             "why": "The test doesn't require checking every individual — the "
                    "offspring being able to reproduce, as a general fact "
                    "about the cross, is what the definition asks."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s26",
        "band": "standard",
        "text": "Some biologists label certain gull populations 'subspecies' "
                "rather than full species. Does that label alone tell you the "
                "fertile-offspring test result for those populations?",
        "options": [
            {"text": "No — 'subspecies' is only a naming decision, not a "
                     "statement about fertile offspring.",
             "correct": True},
            {"text": "Yes — 'subspecies' always means the populations cannot "
                     "produce fertile offspring together.",
             "correct": False,
             "why": "A naming choice like 'subspecies' doesn't by itself "
                    "report a breeding result. Biologists may use such labels "
                    "for populations that in fact interbreed successfully."},
            {"text": "Yes, because 'subspecies' is defined purely by DNA "
                     "comparison.",
             "correct": False,
             "why": "DNA comparison being involved in a naming decision "
                    "doesn't mean the fertile-offspring test has been left out "
                    "— the label alone still doesn't state the result."},
            {"text": "No, because the word 'subspecies' has no accepted "
                     "meaning in biology at all.",
             "correct": False,
             "why": "The word does have a real, if sometimes contested, "
                    "meaning in biology. The point is that a label is not the "
                    "same as the breeding evidence itself."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s27",
        "band": "standard",
        "text": "Sea anemones can reproduce by splitting into two identical "
                "copies of themselves, and can also breed sexually with "
                "another anemone. Can the fertile-offspring test be applied to "
                "them?",
        "options": [
            {"text": "No — any organism able to clone itself falls outside the "
                     "test altogether.",
             "correct": False,
             "why": "The test fails only where sexual breeding is absent, as "
                    "with most British dandelions. An anemone that also breeds "
                    "sexually can still be tested."},
            {"text": "No — two anemones that clone themselves may look "
                     "identical, which defeats the test.",
             "correct": False,
             "why": "Appearance is not the test, so looking identical defeats "
                    "nothing. What matters is that sexual breeding is "
                    "available to observe."},
            {"text": "Yes — they breed sexually as well, so the test still has "
                     "something to work on.",
             "correct": True},
            {"text": "Yes, but only once every anemone in the population has "
                     "been checked for cloning.",
             "correct": False,
             "why": "Nothing needs checking one animal at a time. Sexual "
                    "breeding happening at all is enough for the test to be "
                    "run."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s28",
        "band": "standard",
        "text": "A student learns that two species of big cat have "
                "together produced healthy cubs and immediately concludes "
                "'same species'. What single further fact would change that "
                "conclusion, if it turned out to be true?",
        "options": [
            {"text": "That the cubs themselves cannot go on to reproduce.",
             "correct": True},
            {"text": "That the cubs do not look exactly like either "
                     "parent.",
             "correct": False,
             "why": "Appearance was never part of the test to begin with, "
                    "so how the cubs look could not change the conclusion "
                    "either way."},
            {"text": "That the cross only happened once, in captivity.",
             "correct": False,
             "why": "Whether the cross happened once or many times, or in "
                    "captivity or the wild, does not change what the test "
                    "actually asks."},
            {"text": "That the two parent species have different coat "
                     "patterns.",
             "correct": False,
             "why": "Coat pattern is appearance, which the definition "
                    "explicitly does not use. Only whether the cubs can "
                    "reproduce would change the conclusion."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s29",
        "band": "standard",
        "text": "Mendel settled genetics questions by counting large "
                "numbers of offspring. Biologists deciding a bacterial "
                "species settle it by comparing DNA similarity. What do "
                "the two methods have in common?",
        "options": [
            {"text": 'Both answer a question that looking at the organisms alone cannot settle.',
             "correct": True},
            {"text": "Both involve breeding large numbers of individuals "
                     "together.",
             "correct": False,
             "why": "Bacterial DNA comparison involves no breeding at "
                    "all — bacteria don't breed sexually. That is not what "
                    "the two methods share."},
            {"text": "Both were developed by the same scientist working at "
                     "different times.",
             "correct": False,
             "why": "These are unrelated pieces of work by different "
                    "people in different fields, not one scientist's work "
                    "at two points in time."},
            {"text": "Both give a result of exactly one clear species "
                     "every time they are used.",
             "correct": False,
             "why": "The bacterial method draws a chosen, somewhat "
                    "arbitrary line rather than settling things exactly — "
                    "the opposite of always giving one clean answer."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-s30",
        "band": "standard",
        "text": "Consider these seven cases: two dog breeds, a mule, a liger, "
                "the two pipistrelle bats, bacteria, most British dandelions, "
                "and a ring of gull populations. How many can be settled by "
                "the ordinary breeding test at all, and how many need a "
                "different method?",
        "options": [
            {"text": "All seven can be settled by breeding, given enough "
                     "patience.",
             "correct": False,
             "why": "Bacteria, dandelions and the ring of gulls cannot be "
                    "settled by ordinary breeding at all, however much "
                    "patience is applied."},
            {"text": "Four can be settled by breeding, and three need a "
                     "different method.",
             "correct": True},
            {"text": "None of the seven can be settled cleanly; all seven need "
                     "DNA comparison.",
             "correct": False,
             "why": "Four of the seven — the dogs, the mule, the liger and the "
                    "pipistrelles — give the breeding test a clean, direct "
                    "answer without needing DNA comparison."},
            {"text": "Three can be settled by breeding, and four need a "
                     "different method.",
             "correct": False,
             "why": "It's the other way round. Four cases resolve cleanly by "
                    "breeding; three do not."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h11",
        "band": "harder",
        "text": "Species P has 20 chromosomes in a body cell and species Q has "
                "22. If they produced a hybrid, how many chromosomes would it "
                "have, and what would that predict about the hybrid's own "
                "fertility?",
        "options": [
            {"text": "42 — a full body cell's worth from each parent, "
                     "predicting normal fertility.",
             "correct": False,
             "why": "A hybrid receives a GAMETE from each parent, not a whole "
                    "body cell. Half of 20 is 10 and half of 22 is 11, giving "
                    "21, not 42."},
            {"text": "20 — matching the smaller parent's number, predicting "
                     "normal fertility.",
             "correct": False,
             "why": "The hybrid does not simply take on one parent's whole "
                    "number. It receives half from each: 10 from P and 11 from "
                    "Q, adding to 21."},
            {"text": "21 — an odd number, but predicting no effect on "
                     "fertility since 21 is close to both parents' numbers.",
             "correct": False,
             "why": "Being close to the parents' numbers is irrelevant. What "
                    "matters is that 21 is ODD, exactly the problem that makes "
                    "gamete formation fail in a mule."},
            {"text": "21 — an odd number, predicting the same pairing problem "
                     "that makes a mule almost always infertile.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h12",
        "band": "harder",
        "text": "A rare hybrid between two closely related dolphin species has "
                "been recorded three times independently, twice producing "
                "infertile offspring and once producing a fertile female. "
                "Weigh this evidence and state the best-supported verdict.",
        "options": [
            {"text": "Same species, since a fertile hybrid has now been "
                     "recorded at all.",
             "correct": False,
             "why": "One fertile record out of three does not outweigh two "
                    "records of infertility. The pattern still points to "
                    "different species, with a rare exception."},
            {"text": "Different species is still best-supported — infertility "
                     "dominates the record.",
             "correct": True},
            {"text": "The test does not settle it, since the three records "
                     "disagree with each other.",
             "correct": False,
             "why": "The records don't disagree so much as show a strong "
                    "pattern (infertile) with one rare exception — treated the "
                    "same way as the liger case, not as unresolved conflict."},
            {"text": "Same species, because three recorded hybrids is enough "
                     "evidence on its own, regardless of their fertility.",
             "correct": False,
             "why": "It isn't the NUMBER of recorded hybrids that decides it, "
                    "but whether they can reproduce. Two of the three could "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h13",
        "band": "harder",
        "text": "Chain A has five populations in a straight line, where the "
                "two end populations happen to interbreed successfully anyway. "
                "Chain B has five populations forming a genuine ring, where "
                "the two end populations do not interbreed. How do the "
                "verdicts for Chain A and Chain B differ, and why?",
        "options": [
            {"text": "Both give 'the test does not settle it', since both "
                     "involve a chain of populations.",
             "correct": False,
             "why": "Being arranged in a chain is not, by itself, what creates "
                    "the unclear verdict. Chain A resolves cleanly precisely "
                    "because even its two ends interbreed."},
            {"text": "Chain A gives 'different species' and Chain B gives "
                     "'same species', since a ring is a stronger arrangement "
                     "than a line.",
             "correct": False,
             "why": "Neither chain's shape by itself decides the verdict. What "
                    "decides it is which pairs of populations do or do not "
                    "interbreed."},
            {"text": "Both give one clean verdict, since five populations is "
                     "the same number in each case.",
             "correct": False,
             "why": "The number of populations in the chain is not what "
                    "decides the verdict. It's whether the two end populations "
                    "interbreed, and only Chain A's do."},
            {"text": "Chain A resolves cleanly since even its ends interbreed; "
                     "Chain B does not, since its ends don't.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h14",
        "band": "harder",
        "text": "Out of 500 recorded matings between two closely related "
                "toad populations, 485 produce no viable offspring at all "
                "and 15 produce offspring that survive but do not "
                "themselves reproduce. What percentage of matings produce "
                "NO viable offspring, and what verdict does the overall "
                "pattern support?",
        "options": [
            {"text": "97 per cent produce no viable offspring, and with no "
                     "fertile hybrid recorded, 'different species' is "
                     "supported.",
             "correct": True},
            {"text": "97 per cent produce no viable offspring, but the "
                     "pattern actually supports 'same species', since some "
                     "offspring did survive.",
             "correct": False,
             "why": "Surviving is not the test. None of the 500 matings "
                    "produced offspring able to reproduce, a clean signal "
                    "for 'different species'."},
            {"text": "3 per cent produce no viable offspring, and the "
                     "pattern is too mixed to give a verdict.",
             "correct": False,
             "why": "485 out of 500 is 97 per cent, not 3 per cent — the "
                    "calculation has been inverted. And none of the 500 "
                    "matings produced any reproducing offspring at all."},
            {"text": "97 per cent produce no viable offspring, and the "
                     "remaining 3 per cent settles the question in favour "
                     "of 'same species'.",
             "correct": False,
             "why": "That remaining 3 per cent (15 matings) produced "
                    "offspring that SURVIVED but could not reproduce — "
                    "still evidence for 'different species'."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h15",
        "band": "harder",
        "text": "Ancient DNA has been extracted from two fossil skeletons "
                "found in the same rock layer, and it shows the sequences are "
                "99.9% similar — closer than many living species pairs. A "
                "researcher claims this 'proves' the two fossils are one "
                "species. Evaluate the claim.",
        "options": [
            {"text": "The claim is fully justified, since 99.9% is close "
                     "enough to count as certain proof.",
             "correct": False,
             "why": "Even a very high similarity is still a matter of where "
                    "the chosen line is drawn, not a certainty. The DNA method "
                    "is a fallback precisely because breeding cannot be "
                    "tested."},
            {"text": "The claim is wrong, because DNA cannot survive at all in "
                     "fossils.",
             "correct": False,
             "why": "Ancient DNA genuinely can be extracted from some fossils, "
                    "and comparing it is a real, if imperfect, method. The "
                    "problem with the claim is the word \"proves\"."},
            {"text": "The claim overstates it — DNA similarity is a fallback "
                     "for fossils, but still means a chosen line, not "
                     "certainty.",
             "correct": True},
            {"text": "The claim is wrong, because the two skeletons are from "
                     "the same rock layer and must therefore be the same age.",
             "correct": False,
             "why": "Being found in the same rock layer is not what the claim "
                    "rests on. The issue is that even very close DNA "
                    "similarity is a chosen threshold, not proof beyond all "
                    "doubt."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h16",
        "band": "harder",
        "text": "A student argues that because ring species like the Arctic "
                "gulls show the definition giving two different answers "
                "depending on where you apply it, the whole definition of "
                "species must be flawed and should be abandoned. Evaluate this "
                "argument.",
        "options": [
            {"text": "The argument is correct, and biologists should replace "
                     "the definition with something that never strains.",
             "correct": False,
             "why": "Any definition of species has to cope with the fact that "
                    "speciation happens gradually — one that never strained "
                    "anywhere would likely be hiding that."},
            {"text": "The argument goes too far — a genuine strain is "
                     "informative, not a reason to abandon the definition.",
             "correct": True},
            {"text": "The argument is correct, because a definition that gives "
                     "two different answers can never be trusted for anything.",
             "correct": False,
             "why": "The definition gives one clean, trustworthy answer for "
                    "the great majority of cases. The ring case is a real but "
                    "narrow exception."},
            {"text": "The argument cannot be evaluated without knowing exactly "
                     "how many gull populations exist in the ring.",
             "correct": False,
             "why": "The exact number of populations in the chain doesn't "
                    "change the shape of the argument being evaluated, about "
                    "whether ONE hard case should discredit the whole "
                    "definition."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h17",
        "band": "harder",
        "text": "A student says: 'A great dane and a chihuahua must be "
                "different species, because a horse and a donkey look nothing "
                "alike either and THEY are different species.' Identify the "
                "two separate mistakes in this reasoning.",
        "options": [
            {"text": "There is only one mistake: the student has the great "
                     "dane and chihuahua the wrong way round.",
             "correct": False,
             "why": "There is more than one problem here. Even correcting "
                    "which pair is which, the argument would still be "
                    "reasoning from appearance, which is not the test."},
            {"text": "There is no mistake — looking very different from your "
                     "own kind is indeed evidence of being a different "
                     "species.",
             "correct": False,
             "why": "Appearance in either direction is not the test. The great "
                    "dane and chihuahua case exists to show that huge "
                    "appearance differences can sit within ONE species."},
            {"text": "The only mistake is that horses and donkeys can "
                     "occasionally produce fertile mules.",
             "correct": False,
             "why": "Mules are almost always infertile, which is exactly why "
                    "horses and donkeys count as different species; that is "
                    "not the error here. The error is reasoning from "
                    "appearance."},
            {"text": "It wrongly treats appearance as the test in both "
                     "directions, mistaking its role in each case.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h18",
        "band": "harder",
        "text": "A teacher is designing a set of species-classification cases "
                "and wants students to end on the ones where the definition "
                "runs out. She has: (1) two species of moth resolved by DNA "
                "since they never breed, (2) two dog breeds resolved by "
                "fertile offspring, (3) two bacteria resolved by DNA "
                "similarity. In what order should these be presented, and why?",
        "options": [
            {"text": "The two DNA-based cases first, saving the dog-breed case "
                     "for last, since DNA evidence is the more advanced "
                     "method.",
             "correct": False,
             "why": "How advanced a method sounds is not the reason for the "
                    "ordering. Ending on the harder cases is meant to show "
                    "where the ordinary test runs out — which only works if "
                    "the ordinary test comes first."},
            {"text": "The dog-breed case first, then the two DNA-based cases "
                     "last, matching cases the test can settle before those it "
                     "cannot.",
             "correct": True},
            {"text": "Any order works equally well, since all three cases "
                     "reach a definite verdict eventually.",
             "correct": False,
             "why": "Reaching SOME verdict eventually is not the same as the "
                    "intended teaching order. The order deliberately "
                    "establishes the ordinary test first."},
            {"text": "Alphabetically, by the name of the organism involved.",
             "correct": False,
             "why": "Alphabetical order has nothing to do with the reasoning "
                    "the case order is built to demonstrate."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h19",
        "band": "harder",
        "text": "A philosopher argues that because the bacterial "
                "DNA-similarity boundary is 'agreed and openly somewhat "
                "arbitrary', bacterial species are not real in the way horse "
                "and donkey species are. Evaluate this argument.",
        "options": [
            {"text": "The argument overreaches — 'chosen' describes where the "
                     "line sits, not whether the DNA differences are real.",
             "correct": True},
            {"text": "The argument is entirely correct — anything involving a "
                     "chosen threshold cannot be considered real.",
             "correct": False,
             "why": "Many real, useful scientific categories rest on a chosen "
                    "threshold without that making the underlying phenomenon "
                    "unreal. The DNA differences are real regardless of "
                    "exactly where the line sits."},
            {"text": "The argument is entirely wrong, because horse and donkey "
                     "species are also identified using a chosen threshold.",
             "correct": False,
             "why": "The horse/donkey case is settled directly by the "
                    "fertile-offspring test, with no threshold to choose — the "
                    "mule's infertility answers it outright."},
            {"text": "The argument cannot be evaluated, since 'real' is not a "
                     "word biologists ever use.",
             "correct": False,
             "why": "The argument can be evaluated on its own terms, by "
                    "examining what 'chosen' actually refers to and what it "
                    "does not refer to."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h20",
        "band": "harder",
        "text": "A hybrid between two frog species has 2n = 21 chromosomes, "
                "where its two parent species have 2n = 24 and 2n = 18 "
                "respectively. Using what you know about gamete formation, "
                "explain what is likely to happen when this hybrid tries to "
                "reproduce, and identify which parent contributed the "
                "larger share of its chromosomes.",
        "options": [
            {"text": 'Gamete formation is likely to fail, since 21 is odd; the 24-chromosome parent contributed the larger share, 12, versus 9.',
             "correct": True},
            {"text": "Gamete formation should work normally, because 21 is "
                     "close to both parents' numbers; the two parents "
                     "contributed equal shares.",
             "correct": False,
             "why": "Being close to the parents' numbers doesn't help — "
                    "what matters is that 21 is odd. And the shares are "
                    "not equal: 12 came from the 24-chromosome parent and "
                    "9 from the 18-chromosome parent."},
            {"text": "Gamete formation is likely to fail, because 21 is "
                     "odd; the parent with 18 chromosomes contributed the "
                     "larger share.",
             "correct": False,
             "why": "The odd-number reasoning is right, but the shares "
                    "are swapped. Half of 24 is 12, larger than half of "
                    "18, which is 9."},
            {"text": "Gamete formation should work normally, since the "
                     "hybrid's total falls between its two parents' "
                     "totals.",
             "correct": False,
             "why": "Falling between the two parents' totals says nothing "
                    "about whether 21 can be split into matching pairs. It "
                    "cannot, because it is odd."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h21",
        "band": "harder",
        "text": "Two closely related plant species readily form hybrids in the "
                "wild wherever their ranges overlap, and many of those hybrids "
                "are fertile. A student concludes that the two 'species' are "
                "really just one variable species. Evaluate this using the "
                "fertile-offspring definition.",
        "options": [
            {"text": "It's a reasonable challenge, not a settled conclusion — "
                     "the evidence is real, but needs weighing.",
             "correct": True},
            {"text": "The student is simply correct, and no biologist would "
                     "classify them as two species after this evidence.",
             "correct": False,
             "why": "Real cases of widespread hybridisation are exactly the "
                    "kind of borderline evidence biologists treat as a genuine "
                    "complication to weigh carefully, not as an automatic "
                    "final verdict."},
            {"text": "The student is simply wrong, because plants can never be "
                     "classified using the fertile-offspring test.",
             "correct": False,
             "why": "The fertile-offspring test does apply to plants that "
                    "breed sexually, exactly as it does to Mendel's peas. "
                    "Widespread fertile hybridisation is real, relevant "
                    "evidence."},
            {"text": "The evidence cannot be evaluated without knowing the "
                     "exact colour of the plants' flowers.",
             "correct": False,
             "why": "Flower colour is appearance, which plays no part in the "
                    "definition. What matters here is the fertility of the "
                    "hybrids."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h22",
        "band": "harder",
        "text": "Explain why Mendel's counting method for pea inheritance "
                "could never, by itself, settle whether two pea varieties "
                "belong to different species.",
        "options": [
            {"text": "It could settle it, since a 3:1 ratio is itself evidence "
                     "of two separate species.",
             "correct": False,
             "why": "A 3:1 ratio comes from crossing two carriers WITHIN one "
                    "species and says nothing about whether two different "
                    "varieties can interbreed at all."},
            {"text": "It could settle it, as long as enough plants were "
                     "counted.",
             "correct": False,
             "why": "No amount of counting turns an inheritance-ratio method "
                    "into a fertility test. The two methods answer different "
                    "questions, however large the sample."},
            {"text": "It reveals inheritance within a population, not whether "
                     "varieties can interbreed.",
             "correct": True},
            {"text": "It could never settle it, because Mendel's peas were not "
                     "a real species to begin with.",
             "correct": False,
             "why": "Mendel's pea plants were a genuine, single species. His "
                    "counting method cannot settle a species question because "
                    "it measures inheritance patterns, not interbreeding "
                    "across varieties."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h23",
        "band": "harder",
        "text": "Species R and Species S both have 40 chromosomes. Species R "
                "and Species T have 40 and 36 respectively. A student argues R "
                "and S are more likely to be the same species than R and T, "
                "purely from the chromosome numbers. Evaluate this.",
        "options": [
            {"text": "The argument is sound, since matching numbers are the "
                     "actual definition of same species.",
             "correct": False,
             "why": "The definition is about fertile offspring, not matching "
                    "chromosome numbers. Lions and tigers share the same "
                    "number and are still two species."},
            {"text": "The argument is unreliable — matching numbers can help a "
                     "cross succeed but isn't the test itself.",
             "correct": True},
            {"text": "The argument is sound, because a difference of four "
                     "chromosomes always prevents any breeding at all.",
             "correct": False,
             "why": "A chromosome difference makes a hybrid's own fertility "
                    "likely to fail, but it does not prevent the two species "
                    "from breeding TOGETHER in the first place, as the mule "
                    "shows."},
            {"text": "The argument cannot be evaluated without knowing every "
                     "species' full DNA sequence.",
             "correct": False,
             "why": "The reasoning can be evaluated on the logic alone — "
                    "matching chromosome number is simply not what the "
                    "definition tests."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h24",
        "band": "harder",
        "text": "Two populations of insect are kept together in one "
                "enclosure for five breeding seasons. In each season, each "
                "population breeds successfully within itself, and in "
                "season four, three individuals from different populations "
                "were seen mating, but no offspring resulted. What is the "
                "strongest available verdict, and what would strengthen it "
                "further?",
        "options": [
            {"text": 'Different species is the best-supported verdict so far, and more attempted crosses would strengthen it.',
             "correct": True},
            {"text": "Same species, since mating between the two "
                     "populations was observed at all.",
             "correct": False,
             "why": "Mating alone is not the test — no offspring resulted "
                    "from it. Attempted crosses that produce nothing point "
                    "toward 'different species'."},
            {"text": "The test does not settle it, since only three "
                     "individuals attempted to cross.",
             "correct": False,
             "why": "Three unsuccessful attempts, against five whole "
                    "seasons in which each population bred readily within "
                    "itself, is already a meaningful pattern."},
            {"text": "Same species, because the two populations chose to "
                     "live together for five seasons without conflict.",
             "correct": False,
             "why": "Living peacefully together says nothing about the "
                    "species question. What's relevant is whether crosses "
                    "between them produce reproducing offspring."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h25",
        "band": "harder",
        "text": "Fossils and bacteria are both cases where the ordinary "
                "breeding test cannot be applied. Is the reason the same in "
                "both?",
        "options": [
            {"text": "Yes — in neither case is there any DNA left that could "
                     "be compared.",
             "correct": False,
             "why": "Bacteria certainly have DNA available to compare, and "
                    "that is the fallback method used for them. Ancient DNA "
                    "can sometimes be recovered from fossils too."},
            {"text": "Yes — in both cases the organisms are far too rare in "
                     "nature.",
             "correct": False,
             "why": "Rarity has nothing to do with it. Bacteria are extremely "
                    "common, and many fossils come from once-common species."},
            {"text": "No — fossils are too fragile to study, and bacteria too "
                     "short-lived.",
             "correct": False,
             "why": "Neither fragility nor lifespan is the obstacle. Fossils "
                    "are not alive to be bred at all, and bacteria reproduce "
                    "by dividing rather than mating."},
            {"text": "No — fossils cannot be bred, while bacteria divide "
                     "rather than mate.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h26",
        "band": "harder",
        "text": "A textbook describes the gull ring-species example as "
                "'messier than the textbook version', and gives Mendel's total "
                "plant count as an approximate figure rather than an exact "
                "one. What do these two hedges have in common as examples of "
                "good scientific writing?",
        "options": [
            {"text": "Both hedges exist because the underlying science in each "
                     "case is probably wrong.",
             "correct": False,
             "why": "Hedging a figure or an example is not the same as "
                    "doubting the underlying science. Mendel's conclusion and "
                    "the general truth about ring species are both well "
                    "supported; the hedges are about precision."},
            {"text": "Both openly mark the limits of what is known, rather "
                     "than pretending exactness.",
             "correct": True},
            {"text": "Both hedges exist purely to make the writing sound more "
                     "careful than it needs to be.",
             "correct": False,
             "why": "The hedges track a real limit in each case — an estimated "
                    "historical count, and a real-world example known to be "
                    "more complicated than the textbook version — rather than "
                    "being decorative caution."},
            {"text": "Both hedges exist because neither topic can really be "
                     "taught at this level.",
             "correct": False,
             "why": "Both topics ARE taught at this level, hedges included. A "
                    "hedge marks a specific limit of precision; it does not "
                    "mean the whole topic is out of reach."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h27",
        "band": "harder",
        "text": "A student argues: 'If biologists can't even agree on the "
                "number of dandelion species, biology has failed to answer a "
                "basic question.' Evaluate this claim, considering why the "
                "number varies.",
        "options": [
            {"text": "The claim is correct, since a properly working science "
                     "should always give one exact number for any question "
                     "asked of it.",
             "correct": False,
             "why": "Some real biological situations, like organisms that "
                    "never interbreed, genuinely do not have one single "
                    "'correct' number waiting to be found."},
            {"text": "The claim is correct, because biologists have never "
                     "studied dandelions closely enough to know.",
             "correct": False,
             "why": "Dandelions have been studied closely — the "
                    "two-hundred-plus microspecies figure comes from careful "
                    "work. The variation in the count is explained by the "
                    "biology, not a lack of study."},
            {"text": "The claim cannot be evaluated without a complete list of "
                     "every dandelion species.",
             "correct": False,
             "why": "The claim can be evaluated from the REASON the count "
                    "varies, without needing an exhaustive list."},
            {"text": "The claim mistakes a real feature of biology for a "
                     "failure; biologists can explain why no single number "
                     "exists.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h28",
        "band": "harder",
        "text": "Two animal populations are observed over ten years. In that "
                "time, 40 attempted matings between the two populations are "
                "recorded, of which 2 produce offspring, and neither of those "
                "2 offspring goes on to reproduce. What percentage of "
                "attempted matings produced any offspring at all, and what "
                "does the overall ten-year picture support?",
        "options": [
            {"text": "5 per cent produced offspring, which by itself is enough "
                     "to call them the same species.",
             "correct": False,
             "why": "Producing SOME offspring is not the test — those "
                    "offspring must themselves be able to reproduce, and here "
                    "neither could."},
            {"text": "50 per cent produced offspring, since 2 out of 40 rounds "
                     "to about half when written as a simple fraction.",
             "correct": False,
             "why": "2 out of 40 is 5 per cent, not 50 per cent — dividing 2 "
                    "by 40 and multiplying by 100 gives 5, not 50."},
            {"text": "5 per cent produced offspring, and neither could "
                     "reproduce — a pattern supporting 'different species'.",
             "correct": True},
            {"text": "5 per cent produced offspring, and the picture is too "
                     "mixed over ten years to reach any verdict.",
             "correct": False,
             "why": "Ten years of data with zero reproducing hybrids out of 40 "
                    "attempts is a clear, consistent pattern, not a mixed one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h29",
        "band": "harder",
        "text": "Two bacterial strains are 97% similar in DNA, right at the "
                "boundary biologists commonly use to separate species. A "
                "researcher wants a more certain answer than the DNA "
                "comparison can give. Is there a way to get one, and why or "
                "why not?",
        "options": [
            {"text": "No reliable way — bacteria never breed sexually, so the fertile-offspring test is never available here.",
             "correct": True},
            {"text": "Yes — breeding the two strains together and "
                     "checking for fertile offspring, exactly as with "
                     "animals.",
             "correct": False,
             "why": "Bacteria reproduce by dividing, not by breeding, so "
                    "there is no fertile-offspring test to run on them at "
                    "all, however borderline the DNA result is."},
            {"text": "Yes — comparing their DNA a second time will remove "
                     "the uncertainty.",
             "correct": False,
             "why": "A second DNA comparison would only confirm the same "
                    "similarity figure. The uncertainty comes from being "
                    "close to a CHOSEN boundary, not an unreliable "
                    "measurement."},
            {"text": "No, because 97% similarity is already exact proof "
                     "either way.",
             "correct": False,
             "why": "97% sitting right at a commonly used, chosen boundary "
                    "is precisely the case where the result is LEAST "
                    "certain, not exact proof of anything."},
        ],
        "figure": None,
    },
    {
        "id": "b10-05-h30",
        "band": "harder",
        "text": "Among these cases — two dog breeds, a mule, a liger, two "
                "pipistrelle bats, bacteria, dandelions and a ring of gulls — "
                "which is the most straightforward for the ordinary breeding "
                "test, and which cannot have it run on them at all?",
        "options": [
            {"text": "Most straightforward: the ring of gulls, since the most "
                     "populations were studied; cannot be run at all: the dog "
                     "breeds, since dogs have been bred by humans for too long "
                     "to count.",
             "correct": False,
             "why": "The gulls are exactly where the test gives conflicting "
                    "answers depending on where you apply it — the opposite of "
                    "straightforward. And the dog breeds give a very clean, "
                    "direct result."},
            {"text": "Most straightforward: the mule case, since horses and "
                     "donkeys are large, well-known animals; cannot be run at "
                     "all: the liger, since lions and tigers never meet in the "
                     "wild.",
             "correct": False,
             "why": "The mule case does resolve cleanly, but so do the dog "
                    "breeds, with even less complication. The liger case is "
                    "not one the test fails on — captivity still lets it be "
                    "run, giving a clear 'different species' verdict."},
            {"text": "Most straightforward: the bacteria, since DNA comparison "
                     "gives one single precise number; cannot be run at all: "
                     "the dog breeds, since so many breeds exist.",
             "correct": False,
             "why": "DNA comparison for bacteria is described as agreed but "
                    "openly somewhat arbitrary, not precise. And the dog "
                    "breeds are one of the clearest cases in the whole bench, "
                    "however many breeds exist."},
            {"text": "Most straightforward: the dog breeds, with fertile "
                     "interbreeding observed directly; cannot be run at all: "
                     "the bacteria and dandelions.",
             "correct": True},
        ],
        "figure": None,
    },
]
