"""Biology · Inheritance, variation and evolution — part B (MRB-332).

Nine of the topic's nineteen subtopics: the history of the theory of evolution,
selective breeding, genetic engineering, cloning, the evidence for evolution,
Mendel, fossils and extinction, antibiotic resistance and classification.

Distractors are built from the brief's declared mistakes: selective breeding
confused with genetic engineering, a clone read as a same-age copy of its
donor, "organisms choose to adapt", the fossil record read as complete,
classification by appearance rather than by molecular evidence, and — the one
that matters most here — resistance arising *because of* exposure to the drug.
Every Lamarckian phrasing in this file is a distractor and never a key.

Four subtopics are TRIPLE-only (theory-of-evolution, cloning,
understanding-genetics, classification-living-organisms); the other five are
BASE, so nothing Higher-only appears in them — no ligase, no speciation, no
convergent evolution, no potato-famine case study.
"""

TOPIC = "inheritance"
SUBJECT = "biology"

QUESTIONS = [
    # ── theory-of-evolution ───────────────────────────────────────────────
    {
        "id": "ks4-theory-of-evolution-e01",
        "subtopic_slug": "theory-of-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In which year did Darwin publish 'On the Origin of Species'?",
        "options": ["1858", "1859", "1866", "1900"],
        "correct_index": 1,
        "why": "Darwin published in 1859, the year after his and Wallace's "
               "ideas were read together to the Linnean Society in 1858.",
    },
    {
        "id": "ks4-theory-of-evolution-e02",
        "subtopic_slug": "theory-of-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Before the Industrial Revolution the tree bark in British "
                "woodland was pale and covered in lichen. Which form of the "
                "peppered moth was more common then, and why?",
        "options": [
            "The dark form, because dark wings absorb more heat in a cool "
            "climate",
            "The dark form, because factory soot had already darkened the "
            "bark",
            "The two forms were equally common, because bark colour has no "
            "effect on moths",
            "The light form, because it was camouflaged against the pale bark "
            "and was eaten less",
        ],
        "correct_index": 3,
        "why": "Light moths matched the pale lichen-covered bark, so birds "
               "found fewer of them and more survived to breed.",
    },
    {
        "id": "ks4-theory-of-evolution-e03",
        "subtopic_slug": "theory-of-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name of the process in which individuals with "
                "advantageous inherited characteristics are more likely to "
                "survive and reproduce.",
        "options": [
            "Natural selection",
            "Selective breeding",
            "Adaptation",
            "Mutation",
        ],
        "correct_index": 0,
        "why": "In natural selection the environment, not the organism, "
               "decides which inherited variations are passed on.",
    },
    {
        "id": "ks4-theory-of-evolution-e04",
        "subtopic_slug": "theory-of-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Alfred Russel Wallace pioneered the idea of 'warning "
                "colouration'. What did he suggest an animal's bright colours "
                "signal to a predator?",
        "options": [
            "That the animal is ready to mate and so should not be disturbed "
            "by a predator",
            "That the animal is young and would make a larger meal later on",
            "That the animal is poisonous or tastes unpleasant, so should not "
            "be eaten",
            "That the animal can run faster than the predator can chase it",
        ],
        "correct_index": 2,
        "why": "Bright warning colours advertise toxicity, so predators that "
               "learn to avoid them leave those individuals to breed.",
    },
    {
        "id": "ks4-theory-of-evolution-s01",
        "subtopic_slug": "theory-of-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "On an island with dark volcanic soil, birds hunt beetles by "
                "sight. Over 50 years the beetle population changes from "
                "mostly pale to mostly dark. Explain how natural selection "
                "produced this change.",
        "options": [
            "Dark beetles were already present by chance; birds spotted them "
            "less often, so more survived to pass on the dark allele",
            "The dark volcanic soil gradually stained the beetles' shells, "
            "and their offspring then inherited the darker colour from them",
            "The beetles changed their own colour to match the soil so that "
            "the hunting birds could not see them",
            "The birds developed a taste for pale beetles and deliberately "
            "left the darker beetles alone",
        ],
        "correct_index": 0,
        "why": "The variation came first, by chance mutation; the birds then "
               "selected which of those variants survived to breed.",
    },
    {
        "id": "ks4-theory-of-evolution-s02",
        "subtopic_slug": "theory-of-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "After clean-air laws cut the soot in British cities, the "
                "proportion of dark peppered moths fell again. Explain why.",
        "options": [
            "The dark allele mutated back into the light allele once the air "
            "was clean again",
            "Dark moths migrated away from the cities to find sootier "
            "woodland elsewhere in the north of the country",
            "Bark became pale again, so light moths were better camouflaged "
            "and survived to breed more often",
            "The moths sensed the cleaner air and gradually began to produce "
            "paler offspring",
        ],
        "correct_index": 2,
        "why": "The selection pressure reversed: on pale bark it is the light "
               "moths that predators miss, so their allele spreads.",
    },
    {
        "id": "ks4-theory-of-evolution-s03",
        "subtopic_slug": "theory-of-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Darwin collected evidence for around 20 years before "
                "publishing his theory. Suggest the best explanation for the "
                "delay.",
        "options": [
            "He was waiting for Mendel to publish his breeding experiments on "
            "pea plants",
            "He had not yet visited the Galapagos Islands and still needed "
            "the finch data",
            "He needed Wallace's written permission before he was allowed to "
            "publish",
            "He was gathering more evidence and knew the idea would be "
            "strongly opposed",
        ],
        "correct_index": 3,
        "why": "Darwin expected religious and scientific opposition, so he "
               "built the evidence base before publishing.",
    },
    {
        "id": "ks4-theory-of-evolution-s04",
        "subtopic_slug": "theory-of-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Giraffes stretched their necks to reach "
                "high leaves, and their offspring inherited the longer "
                "necks.' Explain why this is not natural selection.",
        "options": [
            "Because there is no variation at all in neck length between the "
            "individual giraffes that make up a wild population of the "
            "species",
            "Because it says a characteristic gained during life is "
            "inherited, while selection acts on inherited variation already "
            "present",
            "Because a giraffe's neck length is decided entirely by how much "
            "food it manages to eat",
            "Because natural selection changes only the individual animal and "
            "never the population",
        ],
        "correct_index": 1,
        "why": "Stretching a neck does not change the alleles in the gametes, "
               "so an acquired characteristic cannot be inherited.",
    },
    {
        "id": "ks4-theory-of-evolution-h01",
        "subtopic_slug": "theory-of-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that Darwin's theory is accepted today "
                "because his book was so detailed. Evaluate this claim.",
        "options": [
            "It is correct — a sufficiently detailed and carefully written "
            "book is what persuades the scientific community of the day to "
            "accept an idea",
            "It is correct, because no further evidence for evolution has "
            "been found since 1859",
            "It is weak — acceptance came from later independent evidence: "
            "genetics, DNA comparisons, transitional fossils and observed "
            "evolution",
            "It is weak, because Darwin's book was in fact shorter and less "
            "detailed than Wallace's account",
        ],
        "correct_index": 2,
        "why": "A theory is accepted on the evidence that accumulates after "
               "it, not on how well the first account was written.",
    },
    {
        "id": "ks4-theory-of-evolution-h02",
        "subtopic_slug": "theory-of-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Darwin is usually given more credit than Wallace for the "
                "theory of natural selection. Suggest the strongest "
                "scientific reason for this.",
        "options": [
            "Darwin published his ideas several years before Wallace had "
            "thought of them at all",
            "Darwin had around 20 years more collected evidence and set out a "
            "far more detailed case",
            "Wallace later rejected natural selection and argued against his "
            "own earlier work",
            "Wallace's work was about the geography of species and had "
            "nothing to do with selection",
        ],
        "correct_index": 1,
        "why": "Both men reached the same explanation, but Darwin's two "
               "decades of evidence made the published case far stronger.",
    },
    {
        "id": "ks4-theory-of-evolution-h03",
        "subtopic_slug": "theory-of-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Darwin could not explain how variation arose or how "
                "characteristics were passed on. Which later development "
                "supplied that missing mechanism?",
        "options": [
            "The discovery of Archaeopteryx and other transitional fossils in "
            "European quarries during the 19th century",
            "Wallace's work on why different species are found in different "
            "regions of the world",
            "Woese's division of all living things into the three domains of "
            "life",
            "Genetics — heritable units, later identified as genes made of "
            "DNA, with mutation producing variation",
        ],
        "correct_index": 3,
        "why": "Genetics supplied what Darwin lacked: a source of new "
               "variation and a mechanism for passing it on.",
    },
    {
        "id": "ks4-theory-of-evolution-h04",
        "subtopic_slug": "theory-of-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes four sentences about a population of "
                "rabbits hunted by foxes. Identify the sentence that contains "
                "a scientific error.",
        "options": [
            "'The rabbits that ran fastest built up stronger leg muscles, and "
            "their young inherited those muscles.'",
            "'Rabbits within the population vary in how fast they are able to "
            "run from a predator.'",
            "'Faster rabbits are more likely to escape the foxes and survive "
            "long enough to breed.'",
            "'Over many generations the alleles for fast running become "
            "steadily more common in the rabbit population.'",
        ],
        "correct_index": 0,
        "why": "Muscle built during an animal's life is an acquired "
               "characteristic and is not passed to its offspring.",
    },

    # ── selective-breeding ────────────────────────────────────────────────
    {
        "id": "ks4-selective-breeding-e01",
        "subtopic_slug": "selective-breeding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Selective breeding is also known by another name. State it.",
        "options": [
            "Natural selection",
            "Genetic modification",
            "Artificial selection",
            "Cloning",
        ],
        "correct_index": 2,
        "why": "Humans, rather than the environment, choose which organisms "
               "breed — so the selection is artificial.",
    },
    {
        "id": "ks4-selective-breeding-e02",
        "subtopic_slug": "selective-breeding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Approximately how long have humans been selectively breeding "
                "crops and farm animals?",
        "options": [
            "About 10 000 years — since farming began",
            "About 200 years — since Darwin described natural selection",
            "About 70 years — since the structure of DNA was worked out",
            "About 500 years — since the first scientific societies formed",
        ],
        "correct_index": 0,
        "why": "Selective breeding is as old as agriculture itself and long "
               "predates any understanding of genes.",
    },
    {
        "id": "ks4-selective-breeding-e03",
        "subtopic_slug": "selective-breeding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Broccoli, cabbage, kale and cauliflower were all produced by "
                "selecting different features of one wild plant. Name that "
                "plant.",
        "options": [
            "Teosinte, a wild grass native to Central America",
            "Wild wheat, the ancestor of modern bread wheat",
            "Wild rice, grown in flooded fields for thousands of years",
            "Wild cabbage, Brassica oleracea, a coastal European plant",
        ],
        "correct_index": 3,
        "why": "Selecting the bud, stem, leaf or flower of wild cabbage "
               "produced four very different vegetables from one species.",
    },
    {
        "id": "ks4-selective-breeding-e04",
        "subtopic_slug": "selective-breeding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the first step a farmer takes in a selective "
                "breeding programme.",
        "options": [
            "Cut the gene for the desired characteristic out of the animal's "
            "own DNA",
            "Choose the individuals that show the desired characteristic most "
            "strongly",
            "Cross the animal with a member of a completely different species "
            "of animal",
            "Treat the whole herd with hormones so that the characteristic "
            "appears in them",
        ],
        "correct_index": 1,
        "why": "The programme starts by identifying the parents that already "
               "show the characteristic most strongly.",
    },
    {
        "id": "ks4-selective-breeding-s01",
        "subtopic_slug": "selective-breeding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer wants a flock of sheep that produces more wool. "
                "Describe how selective breeding would achieve this.",
        "options": [
            "Insert a wool-production gene taken from another breed of sheep "
            "directly into the flock's sperm cells before mating",
            "Feed the flock a high-protein diet so that their fleeces grow "
            "thicker each year",
            "Cross the sheep with a goat, which produces a different kind of "
            "useful fibre",
            "Breed the highest-yielding sheep together, then breed the best "
            "of their offspring, over many generations",
        ],
        "correct_index": 3,
        "why": "Each generation the alleles for high wool yield are "
               "concentrated a little further by choosing the best parents.",
    },
    {
        "id": "ks4-selective-breeding-s02",
        "subtopic_slug": "selective-breeding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why selective breeding cannot give a crop a "
                "characteristic that no plant in the population has.",
        "options": [
            "Because a breeding programme is not allowed to run for more than "
            "ten generations",
            "Because breeding only concentrates alleles that already exist — "
            "it does not create new genes",
            "Because the breeder must always use natural pollination rather "
            "than hand pollination",
            "Because mutations never occur in plants that are grown on a farm "
            "rather than in the wild",
        ],
        "correct_index": 1,
        "why": "Selection can only work on variation that is already in the "
               "gene pool; it cannot invent an allele that is absent.",
    },
    {
        "id": "ks4-selective-breeding-s03",
        "subtopic_slug": "selective-breeding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Wheat has been selectively bred to have shorter stems. "
                "Suggest the advantage of this to a farmer.",
        "options": [
            "Shorter stems are less easily flattened by wind and rain, so "
            "more grain can be harvested",
            "Shorter stems allow the plant to photosynthesise without needing "
            "any sunlight at all",
            "Shorter plants need no water, so the crop can be grown "
            "successfully in a desert",
            "Shorter stems let the grain ripen without the plant ever having "
            "to produce flowers",
        ],
        "correct_index": 0,
        "why": "A short, stiff stem resists lodging, so the crop stays "
               "standing and the combine can gather the grain.",
    },
    {
        "id": "ks4-selective-breeding-s04",
        "subtopic_slug": "selective-breeding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower breeds only from the strawberry plants with the "
                "largest fruit, for ten generations. Predict what happens to "
                "fruit size and to genetic variation.",
        "options": [
            "Fruit size increases and genetic variation also increases",
            "Fruit size stays the same, because the variation was already "
            "there at the start",
            "Fruit size increases and genetic variation falls",
            "Fruit size falls, because inbreeding always weakens the selected "
            "characteristic",
        ],
        "correct_index": 2,
        "why": "Breeding from a narrow group concentrates the alleles for "
               "large fruit while discarding most of the others.",
    },
    {
        "id": "ks4-selective-breeding-h01",
        "subtopic_slug": "selective-breeding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field of one selectively bred wheat variety is destroyed "
                "by a new fungal disease, while a neighbouring field sown "
                "with a mixture of older varieties loses only some plants. "
                "Explain the difference.",
        "options": [
            "The fungus mutated only in the first field, and the mixture of "
            "older varieties in the neighbouring field was never exposed to "
            "it at all that season",
            "The bred variety's plants are almost genetically identical, so "
            "all are susceptible; the mixed field held plants carrying "
            "resistance alleles",
            "Selectively bred plants are always weaker than older varieties, "
            "because breeding damages them",
            "The older varieties grow more slowly, so the fungus was unable "
            "to keep pace with their growth",
        ],
        "correct_index": 1,
        "why": "A narrow gene pool means that whatever kills one plant can "
               "kill them all; a mixed population usually holds resistance.",
    },
    {
        "id": "ks4-selective-breeding-h02",
        "subtopic_slug": "selective-breeding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist wants a crop plant to make a protein that is "
                "found only in a soil bacterium. Explain why selective "
                "breeding cannot achieve this.",
        "options": [
            "Because selective breeding can only be used on farm animals such "
            "as cattle and sheep, and never on crop plants at all",
            "Because the protein would be broken down by the plant before it "
            "could ever be used",
            "Because the crop and the bacterium cannot reproduce together, so "
            "the allele can never enter the crop's gene pool",
            "Because selective breeding works in a single generation and this "
            "change would need longer",
        ],
        "correct_index": 2,
        "why": "Breeding can only move alleles between organisms that can "
               "reproduce together, which a plant and a bacterium cannot.",
    },
    {
        "id": "ks4-selective-breeding-h03",
        "subtopic_slug": "selective-breeding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A campaigner argues that selective breeding is safe because "
                "it is natural, unlike genetic engineering. Evaluate this "
                "argument.",
        "options": [
            "It is weak — both deliberately change the alleles a population "
            "carries, and selective breeding causes inbreeding, welfare "
            "problems and lost diversity",
            "It is strong — selective breeding involves no deliberate human "
            "decisions at all, so no harm of any kind can possibly result "
            "from the practice over time",
            "It is strong, because selective breeding cannot change the DNA "
            "of an organism in any way whatever",
            "It is weak, because selective breeding is in fact far more "
            "precise than genetic engineering is",
        ],
        "correct_index": 0,
        "why": "Being slower does not make selective breeding harmless: "
               "flat-faced dogs and lame dairy cattle are its own results.",
    },
    {
        "id": "ks4-selective-breeding-h04",
        "subtopic_slug": "selective-breeding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Breeder A breeds only from the two highest-yielding cows "
                "each generation. Breeder B keeps a much larger herd and "
                "breeds from the best fifth of it. Predict which herd keeps "
                "more genetic variation, and why.",
        "options": [
            "Breeder A's herd, because selecting only the very best animals "
            "keeps all the useful alleles",
            "Both herds lose variation at exactly the same rate, since both "
            "breeders are selecting",
            "Breeder B's herd, because a larger herd of cattle always grows "
            "faster than a small one",
            "Breeder B's herd, because breeding from more individuals keeps "
            "more alleles in the population",
        ],
        "correct_index": 3,
        "why": "The fewer parents a generation has, the fewer alleles pass on "
               "— so a wider selection retains more variation.",
    },

    # ── genetic-engineering ───────────────────────────────────────────────
    {
        "id": "ks4-genetic-engineering-e01",
        "subtopic_slug": "genetic-engineering",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a plasmid is.",
        "options": [
            "A small circular piece of DNA found in bacteria, used as a "
            "vector",
            "An enzyme that cuts a DNA molecule at one particular sequence of "
            "bases",
            "The membrane-bound nucleus found inside a bacterial cell",
            "A protein that carries oxygen around the bloodstream",
        ],
        "correct_index": 0,
        "why": "A plasmid is a small ring of bacterial DNA, which makes it a "
               "convenient carrier for an inserted gene.",
    },
    {
        "id": "ks4-genetic-engineering-e02",
        "subtopic_slug": "genetic-engineering",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An organism has had a gene from another species inserted "
                "into its DNA. Which term describes it?",
        "options": [
            "A clone of the parent",
            "A mutant",
            "Genetically modified",
            "A hybrid",
        ],
        "correct_index": 2,
        "why": "Its genome has been deliberately altered by inserting a gene, "
               "which is what genetic modification means.",
    },
    {
        "id": "ks4-genetic-engineering-e03",
        "subtopic_slug": "genetic-engineering",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Before genetically modified bacteria were used, where did "
                "the insulin injected by people with type 1 diabetes come "
                "from?",
        "options": [
            "It was built entirely from chemicals in a laboratory",
            "It was extracted from the pancreases of pigs and cattle",
            "It was collected from blood donated by healthy volunteers",
            "It was extracted from genetically modified rice plants",
        ],
        "correct_index": 1,
        "why": "Animal pancreases were the only source until about 1982, when "
               "GM bacteria began producing human insulin.",
    },
    {
        "id": "ks4-genetic-engineering-e04",
        "subtopic_slug": "genetic-engineering",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why bacteria are used to manufacture human insulin "
                "rather than farm animals.",
        "options": [
            "Bacteria already make human insulin naturally, so the gene only "
            "speeds the process up",
            "Insulin is a protein that only prokaryotic cells are able to "
            "build correctly",
            "Bacteria cannot be harmed by a human gene, whereas animal cells "
            "can be harmed by it",
            "Bacteria reproduce very quickly in large vats, so huge "
            "quantities are made in days",
        ],
        "correct_index": 3,
        "why": "A vat of bacteria doubles in minutes, so the inserted gene is "
               "copied into billions of insulin-making cells.",
    },
    {
        "id": "ks4-genetic-engineering-s01",
        "subtopic_slug": "genetic-engineering",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why eating a genetically modified soya bean does not "
                "change the DNA in the eater's own cells.",
        "options": [
            "The inserted gene is completely destroyed by cooking, so none of "
            "it ever reaches the stomach or the small intestine",
            "The inserted gene is too heavy to pass through the wall of the "
            "small intestine",
            "DNA in food is digested into small molecules and absorbed as "
            "nutrients — it is not inserted into the eater's cells",
            "Human cells already contain that gene, so eating more of it "
            "makes no difference at all",
        ],
        "correct_index": 2,
        "why": "Digestion breaks all dietary DNA down to nucleotides, whether "
               "it came from a modified plant or an ordinary one.",
    },
    {
        "id": "ks4-genetic-engineering-s02",
        "subtopic_slug": "genetic-engineering",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one environmental concern about growing a "
                "herbicide-resistant GM crop.",
        "options": [
            "The crop would poison the insects that pollinate the flowers in "
            "the hedgerows around the field",
            "The crop would need far more water each season than the "
            "unmodified variety does",
            "The crop would be unable to reproduce, so the field could never "
            "be sown from its seed",
            "Pollen could carry the resistance gene to wild relatives, "
            "producing herbicide-resistant weeds",
        ],
        "correct_index": 3,
        "why": "Genes can escape in pollen, and a weed that inherits "
               "herbicide resistance can no longer be sprayed out.",
    },
    {
        "id": "ks4-genetic-engineering-s03",
        "subtopic_slug": "genetic-engineering",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterium is able to make a human protein when "
                "the human gene is put into it.",
        "options": [
            "The genetic code is essentially the same in all organisms, so "
            "the bacterium reads the gene and builds the same protein",
            "The plasmid first rewrites the human gene into a bacterial gene "
            "before the cell is able to read and use it to build a protein",
            "Bacteria are descended from human cells, so they already share "
            "most of the same proteins",
            "Human and bacterial DNA are chemically different, and that "
            "difference makes the gene work faster",
        ],
        "correct_index": 0,
        "why": "Because the same base triplets code for the same amino acids "
               "in nearly all life, a bacterium can read a human gene.",
    },
    {
        "id": "ks4-genetic-engineering-s04",
        "subtopic_slug": "genetic-engineering",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer says the drawback of GM seed is that he is not "
                "allowed to keep seed from his crop to sow the next year. "
                "Which concern is this an example of?",
        "options": [
            "Gene escape from the crop into wild relatives growing nearby",
            "Corporate control — biotechnology companies hold patents on GM "
            "seed",
            "Loss of biodiversity caused by planting one crop over a very "
            "large area",
            "Animal welfare in the use of genetically modified farm livestock",
        ],
        "correct_index": 1,
        "why": "The objection here is economic and social: the patent, not "
               "the biology, is what stops the farmer saving seed.",
    },
    {
        "id": "ks4-genetic-engineering-h01",
        "subtopic_slug": "genetic-engineering",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A commentator argues that GM crops must be completely safe "
                "because millions of people have eaten them for years without "
                "harm. Evaluate this argument.",
        "options": [
            "It is sound — long-term consumption by humans tests every "
            "possible risk that a GM crop could ever carry with it",
            "It is unsound, because no one anywhere has ever actually eaten a "
            "genetically modified crop",
            "It is sound, because a crop that is safe to eat cannot possibly "
            "affect anything else",
            "It is limited — it is evidence about human health, but says "
            "nothing about ecological risks such as gene escape",
        ],
        "correct_index": 3,
        "why": "Evidence of safe eating answers one question only; the "
               "ecological risks are a separate question needing separate "
               "evidence.",
    },
    {
        "id": "ks4-genetic-engineering-h02",
        "subtopic_slug": "genetic-engineering",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes four statements about genetic engineering. "
                "Identify the statement that is incorrect.",
        "options": [
            "'A gene taken from a bacterium can be inserted into a crop "
            "plant.'",
            "'Genetic engineering builds a brand new gene that no organism "
            "has ever carried before.'",
            "'Genes can be transferred between species that could never breed "
            "together.'",
            "'Pollen from a GM crop can carry the inserted gene to a wild "
            "relative growing in a hedge nearby.'",
        ],
        "correct_index": 1,
        "why": "Genetic engineering moves a gene that already exists in "
               "another organism — it does not invent a new one.",
    },
    {
        "id": "ks4-genetic-engineering-h03",
        "subtopic_slug": "genetic-engineering",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bt crops carry a bacterial gene so that the plant makes its "
                "own insecticide. Evaluate this technology.",
        "options": [
            "It has no drawbacks, because the insecticide is made by the "
            "plant rather than sprayed onto it",
            "It is useless, because an insect cannot be killed by a substance "
            "made inside a plant",
            "It cuts the pesticide that must be sprayed, but pests may be "
            "selected for resistance to the toxin",
            "It removes the need to plant seed at all, because the crop "
            "regrows itself each season",
        ],
        "correct_index": 2,
        "why": "A toxin present in every plant all season is a constant "
               "selection pressure, so resistant pests are favoured.",
    },
    {
        "id": "ks4-genetic-engineering-h04",
        "subtopic_slug": "genetic-engineering",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A regulator must decide whether to approve a "
                "drought-tolerant GM maize. Which evidence would be the most "
                "useful scientifically?",
        "options": [
            "Field trials over several growing seasons measuring yield and "
            "checking whether the gene spreads to wild plants",
            "A national opinion poll asking the public whether they would be "
            "willing to eat the maize",
            "A laboratory measurement of the total mass of DNA contained in a "
            "single maize seed",
            "A published statement from the company that developed the seed, "
            "setting out the benefits it expects the crop to bring",
        ],
        "correct_index": 0,
        "why": "Repeated field trials test both the claimed benefit and the "
               "main ecological risk under real growing conditions.",
    },

    # ── cloning ───────────────────────────────────────────────────────────
    {
        "id": "ks4-cloning-e01",
        "subtopic_slug": "cloning",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In which year was Dolly the sheep, the first mammal cloned "
                "from an adult body cell, produced?",
        "options": ["1953", "1977", "1990", "1996"],
        "correct_index": 3,
        "why": "Dolly was born in 1996 and was the first mammal produced by "
               "nuclear transfer from an adult body cell.",
    },
    {
        "id": "ks4-cloning-e02",
        "subtopic_slug": "cloning",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In tissue culture, the tiny piece of plant tissue used is "
                "usually taken from which part of the plant?",
        "options": [
            "The waxy cuticle on the upper surface of a fully grown green "
            "leaf",
            "The growing tip, or meristem, where cells are still dividing",
            "The root hair cells that absorb water from the soil",
            "The anther, in which the plant's pollen grains are made",
        ],
        "correct_index": 1,
        "why": "Meristem cells are still unspecialised and dividing, so they "
               "can be made to grow into whole new plants.",
    },
    {
        "id": "ks4-cloning-e03",
        "subtopic_slug": "cloning",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a clone.",
        "options": [
            "An organism produced by combining gametes from two different "
            "parents",
            "An organism whose genes have been deliberately altered in a "
            "laboratory",
            "An organism genetically identical to the organism it was "
            "produced from",
            "An organism that looks exactly the same as another organism does",
        ],
        "correct_index": 2,
        "why": "A clone is defined by its genes being identical, not by "
               "looking the same — environment still shapes the phenotype.",
    },
    {
        "id": "ks4-cloning-e04",
        "subtopic_slug": "cloning",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which type of cell division produces the cells of a cloned "
                "organism?",
        "options": [
            "Mitosis",
            "Meiosis",
            "Fertilisation",
            "Differentiation",
        ],
        "correct_index": 0,
        "why": "Mitosis copies the whole genome exactly, so every daughter "
               "cell carries the same alleles as the parent cell.",
    },
    {
        "id": "ks4-cloning-s01",
        "subtopic_slug": "cloning",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two cloned calves are raised on different farms, one on rich "
                "pasture and one on poor grazing. At two years old their "
                "masses differ by 90 kg. Explain why.",
        "options": [
            "The cloning process failed for one of the two calves, so it is "
            "not really a clone at all",
            "They have identical genes, but the environment affects how their "
            "characteristics develop",
            "The DNA of the two calves mutated in different ways after they "
            "were born on the farms",
            "One calf was in fact the natural offspring of the surrogate "
            "mother that carried it",
        ],
        "correct_index": 1,
        "why": "Genotype is identical but phenotype is not: nutrition and "
               "conditions decide how far the shared genes are expressed.",
    },
    {
        "id": "ks4-cloning-s02",
        "subtopic_slug": "cloning",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A botanic garden must produce several thousand plants from "
                "one rare specimen. Explain why tissue culture is chosen "
                "rather than taking cuttings.",
        "options": [
            "A tiny piece of tissue yields thousands of plants, so very "
            "little of the rare parent is removed",
            "Cuttings produce plants that are not genetically identical to "
            "the parent plant they came from",
            "Tissue culture is cheaper and needs no special equipment or "
            "sterile working conditions",
            "Cuttings require a second parent plant to supply the pollen "
            "needed for fertilisation",
        ],
        "correct_index": 0,
        "why": "Micropropagation multiplies a minute explant into thousands "
               "of plants, so a rare specimen is barely damaged.",
    },
    {
        "id": "ks4-cloning-s03",
        "subtopic_slug": "cloning",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In nuclear transfer, an electric shock is applied to the egg "
                "cell after the donor nucleus has been put in. Explain why.",
        "options": [
            "To fuse the donor nucleus with the egg cell's own original "
            "nucleus",
            "To kill any bacteria that may have entered the egg cell during "
            "the procedure",
            "To stimulate the cell to start dividing so that an embryo begins "
            "to form",
            "To cause a mutation that makes the newly formed cell divide more "
            "rapidly",
        ],
        "correct_index": 2,
        "why": "The shock triggers cell division, which normally starts at "
               "fertilisation — an event that has not happened here.",
    },
    {
        "id": "ks4-cloning-s04",
        "subtopic_slug": "cloning",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an embryo transplant the embryo is split before its cells "
                "have differentiated. Explain why the splitting must happen "
                "at that stage.",
        "options": [
            "Because a larger embryo would be too big to fit inside the "
            "surrogate mother's uterus",
            "Because the surrogate mother's immune system would reject an "
            "older embryo on transfer",
            "Because splitting a later embryo would produce animals belonging "
            "to a different species",
            "Because the cells are still unspecialised, so each piece can "
            "grow into a whole embryo",
        ],
        "correct_index": 3,
        "why": "Only unspecialised cells retain the ability to form every "
               "tissue, so each fragment can develop into a whole animal.",
    },
    {
        "id": "ks4-cloning-h01",
        "subtopic_slug": "cloning",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Dolly developed arthritis and lung disease unusually early "
                "in her life. Explain what this raised concerns about.",
        "options": [
            "That animals cloned from an adult cell may suffer health "
            "problems earlier than normal",
            "That cloned animals cannot reproduce and so die without ever "
            "leaving any offspring",
            "That the cloning process gradually turns the animal into a "
            "member of a different species",
            "That clones age far more slowly than animals produced by "
            "ordinary sexual reproduction",
        ],
        "correct_index": 0,
        "why": "Dolly's early illnesses suggested cloning from an adult cell "
               "may carry a health cost, which is a real welfare concern.",
    },
    {
        "id": "ks4-cloning-h02",
        "subtopic_slug": "cloning",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pet owner is told that a cloned puppy will be 'exactly the "
                "same dog' as the pet that died. Explain the two ways this "
                "claim is misleading.",
        "options": [
            "The clone would share none of the original dog's genes and would "
            "be a completely different breed",
            "The clone would be the same age as the original dog was and "
            "would share all of its memories",
            "The clone would be born sterile, and would carry only half of "
            "the original dog's genetic material in each and every one of its "
            "cells",
            "The clone is a newborn with the same genes, not the same "
            "individual, and environment will make its characteristics differ",
        ],
        "correct_index": 3,
        "why": "A clone starts life again from the beginning, and identical "
               "genes in a different environment give a different animal.",
    },
    {
        "id": "ks4-cloning-h03",
        "subtopic_slug": "cloning",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nuclear transfer has a low success rate — many attempts are "
                "needed for each viable clone. Explain why this is a "
                "particular problem when cloning an endangered animal.",
        "options": [
            "It means the clones that are produced would belong to a slightly "
            "different species",
            "Large numbers of egg cells and surrogate mothers are needed, and "
            "both are very scarce for a rare species",
            "A low success rate means that the clones which are born will "
            "always turn out to be sterile",
            "Repeated attempts alter the DNA, so the clones are not "
            "genetically identical to the donor",
        ],
        "correct_index": 1,
        "why": "Each attempt consumes an egg and a surrogate, and a species "
               "with few individuals left can supply very few of either.",
    },
    {
        "id": "ks4-cloning-h04",
        "subtopic_slug": "cloning",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare therapeutic cloning and reproductive cloning.",
        "options": [
            "Therapeutic cloning produces a whole new organism; reproductive "
            "cloning produces tissue for a patient",
            "Both produce a whole new organism, and both are opposed by most "
            "of the scientific community",
            "Therapeutic cloning produces tissues to treat a patient; "
            "reproductive cloning produces a whole new organism",
            "Both produce tissue only, so neither of them raises any ethical "
            "objection at all",
        ],
        "correct_index": 2,
        "why": "The two differ in what is grown: matched tissue for "
               "treatment, or a complete new individual.",
    },

    # ── evidence-for-evolution ────────────────────────────────────────────
    {
        "id": "ks4-evidence-for-evolution-e01",
        "subtopic_slug": "evidence-for-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Approximately what percentage of their DNA do humans and "
                "chimpanzees share?",
        "options": ["About 75%", "About 99%", "About 50%", "About 25%"],
        "correct_index": 1,
        "why": "Humans and chimpanzees share close to 99% of their DNA, which "
               "reflects a very recent common ancestor.",
    },
    {
        "id": "ks4-evidence-for-evolution-e02",
        "subtopic_slug": "evidence-for-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Humans and yeast share about a quarter of their genes. What "
                "does this suggest?",
        "options": [
            "Both are eukaryotes descended from a shared ancestor that lived "
            "a very long time ago",
            "Humans evolved directly from yeast within the last few million "
            "years of Earth's history",
            "A quarter of a yeast cell is made of exactly the same material "
            "as a human cell is",
            "The similarity is a coincidence, because the two organisms are "
            "completely unrelated",
        ],
        "correct_index": 0,
        "why": "Shared genes mean shared ancestry — a distant one here, which "
               "is why the proportion is low rather than high.",
    },
    {
        "id": "ks4-evidence-for-evolution-e03",
        "subtopic_slug": "evidence-for-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which protein has a very similar structure in all "
                "vertebrates, with the small differences between species "
                "reflecting how closely related they are?",
        "options": ["Amylase enzyme", "Keratin", "Insulin", "Haemoglobin"],
        "correct_index": 3,
        "why": "Haemoglobin carries oxygen in every vertebrate, and its small "
               "sequence differences track evolutionary distance.",
    },
    {
        "id": "ks4-evidence-for-evolution-e04",
        "subtopic_slug": "evidence-for-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give an example of evolution that scientists can observe "
                "happening within a human lifetime.",
        "options": [
            "The five-digit bone pattern shared by a human arm and a bat's "
            "wing",
            "The change from simple to complex organisms through the layers "
            "of rock",
            "New strains of the influenza virus appearing every year",
            "The extinction of the dinosaurs about 66 million years ago",
        ],
        "correct_index": 2,
        "why": "Influenza changes fast enough for the population to be seen "
               "evolving from one year to the next.",
    },
    {
        "id": "ks4-evidence-for-evolution-s01",
        "subtopic_slug": "evidence-for-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A geologist examines four rock layers. The deepest contains "
                "only simple shelled animals; the shallowest contains fish "
                "with jaws. What can be concluded?",
        "options": [
            "Simple shelled animals lived earlier and more complex forms "
            "appeared later — species have changed over time",
            "The fish evolved out of the rock itself as the deeper layers of "
            "sediment were slowly compressed into stone over time",
            "The deepest fossils must be the youngest, because material sinks "
            "downwards as it decays",
            "The shelled animals were badly adapted, which is why they are "
            "found deeper in the rock",
        ],
        "correct_index": 0,
        "why": "Deeper rock is older, so the order of fossils records the "
               "order in which those forms of life existed.",
    },
    {
        "id": "ks4-evidence-for-evolution-s02",
        "subtopic_slug": "evidence-for-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The DNA of a horse and a donkey differs at far fewer bases "
                "than the DNA of a horse and a cow. Explain what this shows.",
        "options": [
            "The horse and the cow are more closely related, because larger "
            "animals share more of their DNA",
            "All three species are related to the same degree, because every "
            "organism shares some DNA",
            "The horse and the donkey are less closely related, because "
            "similar DNA means less shared time",
            "The horse and the donkey are more closely related — fewer "
            "differences means a more recent shared ancestor",
        ],
        "correct_index": 3,
        "why": "Differences accumulate over time, so the fewer there are, the "
               "less time has passed since the lineages split.",
    },
    {
        "id": "ks4-evidence-for-evolution-s03",
        "subtopic_slug": "evidence-for-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues: 'There are gaps in the fossil record, so "
                "evolution has not been proved.' Explain the flaw in this "
                "argument.",
        "options": [
            "There are in fact no gaps at all in the fossil record — every "
            "single species that has ever lived has left a fossil behind "
            "somewhere in the rocks",
            "The gaps show that only some species evolved while all the "
            "others remained unchanged",
            "Gaps are expected because fossilisation is rare, and the overall "
            "pattern, DNA evidence and observed evolution still support the "
            "theory",
            "Gaps matter only for extinct species, and evolution applies only "
            "to the species still living",
        ],
        "correct_index": 2,
        "why": "Fossilisation is a rare accident, so an incomplete record is "
               "exactly what the theory predicts, not a problem for it.",
    },
    {
        "id": "ks4-evidence-for-evolution-s04",
        "subtopic_slug": "evidence-for-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Archaeopteryx had feathers and wings like a bird but also "
                "teeth and a long bony tail like a small dinosaur. What kind "
                "of fossil is this, and what does it show?",
        "options": [
            "A trace fossil, showing how a dinosaur moved across ground that "
            "was still soft",
            "A transitional fossil, showing intermediate features between two "
            "groups of animals",
            "A hybrid fossil, formed when a dinosaur and a bird bred together "
            "successfully",
            "A damaged fossil, in which the bones of a bird and a dinosaur "
            "became mixed in the rock",
        ],
        "correct_index": 1,
        "why": "A fossil carrying features of two groups is what you expect "
               "if one group descended from the other.",
    },
    {
        "id": "ks4-evidence-for-evolution-h01",
        "subtopic_slug": "evidence-for-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that the fossil record is the single "
                "strongest piece of evidence for evolution. Evaluate this "
                "claim.",
        "options": [
            "It is correct — fossils are the only evidence we have anywhere "
            "that reaches back to a time before written records begin at all",
            "It is correct, because the DNA of two different species cannot "
            "be compared with each other",
            "It is questionable — the fossil record is incomplete, while DNA "
            "comparisons cover every living species and agree with it",
            "It is wrong, because fossils give no useful information about "
            "the organisms of the past",
        ],
        "correct_index": 2,
        "why": "Fossils are powerful but patchy; molecular evidence covers "
               "all living species and independently confirms the pattern.",
    },
    {
        "id": "ks4-evidence-for-evolution-h02",
        "subtopic_slug": "evidence-for-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The influenza vaccine must be reformulated most years, but "
                "the measles vaccine does not. Explain the difference in "
                "terms of natural selection.",
        "options": [
            "Influenza is a bacterium and measles is a virus, so only "
            "influenza is able to evolve",
            "Influenza mutates rapidly and variants that escape existing "
            "immunity are selected, so the virus population changes; measles "
            "changes very little",
            "The influenza vaccine wears off after about a year, while the "
            "measles vaccine does not",
            "People catch influenza far more often than they catch measles, "
            "and each new infection makes the vaccine a little less effective "
            "than before each year",
        ],
        "correct_index": 1,
        "why": "Population immunity is the selection pressure: flu variants "
               "that it does not recognise are the ones that spread.",
    },
    {
        "id": "ks4-evidence-for-evolution-h03",
        "subtopic_slug": "evidence-for-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student says 'evolution is only a theory, so it might be "
                "wrong'. Another says 'in science a theory is an explanation "
                "supported by a large body of evidence'. Evaluate.",
        "options": [
            "The second student is right — evolution is supported by fossils, "
            "shared body structures, DNA comparisons and directly observed "
            "change",
            "The first student is right — a theory in science simply means an "
            "idea that somebody has suggested but that has not yet been "
            "tested at all",
            "Both are wrong — evolution is a law rather than a theory, so it "
            "can never be questioned",
            "Both are right — the word theory means the same in science as it "
            "does in everyday speech",
        ],
        "correct_index": 0,
        "why": "In science a theory is a well-evidenced explanation, and this "
               "one is supported by several independent lines of evidence.",
    },
    {
        "id": "ks4-evidence-for-evolution-h04",
        "subtopic_slug": "evidence-for-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Scientists predicted that fossils with both fish features "
                "and the beginnings of limbs should lie in rocks of a "
                "particular age, searched such rocks and found Tiktaalik. "
                "Explain why this was a strong test of the theory.",
        "options": [
            "It showed that fossils can only be found when scientists already "
            "know what they are looking for",
            "It proved that the fossil record is complete, since the fossil "
            "that was predicted was found",
            "It showed that fish are still turning into land animals in "
            "rivers at the present day",
            "The theory made a risky prediction about what would be found and "
            "where, and the prediction was confirmed",
        ],
        "correct_index": 3,
        "why": "A theory that could have been refuted by an empty search, and "
               "was not, has passed a genuine test.",
    },

    # ── understanding-genetics ────────────────────────────────────────────
    {
        "id": "ks4-understanding-genetics-e01",
        "subtopic_slug": "understanding-genetics",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which organism did Gregor Mendel use for his breeding "
                "experiments?",
        "options": [
            "Fruit flies",
            "Laboratory mice",
            "Pea plants",
            "Bacteria",
        ],
        "correct_index": 2,
        "why": "Pea plants have clear either/or characteristics and can be "
               "crossed by hand, which made the ratios easy to count.",
    },
    {
        "id": "ks4-understanding-genetics-e02",
        "subtopic_slug": "understanding-genetics",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In which year did Mendel publish the results of his breeding "
                "experiments?",
        "options": ["1859", "1900", "1953", "1866"],
        "correct_index": 3,
        "why": "Mendel published in 1866, and his work was then largely "
               "ignored until it was rediscovered in 1900.",
    },
    {
        "id": "ks4-understanding-genetics-e03",
        "subtopic_slug": "understanding-genetics",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mendel crossed a pure-breeding tall pea plant with a "
                "pure-breeding short one. State what the first generation of "
                "offspring were like.",
        "options": [
            "All of them were tall",
            "All of them were short",
            "Half were tall and half were short",
            "Three were tall for every one that was short",
        ],
        "correct_index": 0,
        "why": "Every offspring inherited one tall and one short unit, and "
               "the tall one is dominant, so all appeared tall.",
    },
    {
        "id": "ks4-understanding-genetics-e04",
        "subtopic_slug": "understanding-genetics",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mendel is now given which title?",
        "options": [
            "The father of evolution",
            "The father of genetics",
            "The father of classification",
            "The father of medicine",
        ],
        "correct_index": 1,
        "why": "His breeding experiments established the rules of "
               "inheritance, which is the foundation of genetics.",
    },
    {
        "id": "ks4-understanding-genetics-s01",
        "subtopic_slug": "understanding-genetics",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mendel grew 928 plants in a generation produced by crossing "
                "two heterozygous tall pea plants (Tt × Tt). Calculate "
                "approximately how many would be expected to be short.",
        "options": ["696 plants", "464 plants", "309 plants", "232 plants"],
        "correct_index": 3,
        "why": "Tt × Tt gives 3 tall : 1 short, so a quarter of 928 — about "
               "232 plants — are short.",
    },
    {
        "id": "ks4-understanding-genetics-s02",
        "subtopic_slug": "understanding-genetics",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why Mendel counted thousands of pea plants rather "
                "than a few dozen.",
        "options": [
            "Growing more plants made each individual plant grow faster and "
            "more strongly than before",
            "Large numbers allowed him to see the heritable units directly "
            "through a microscope",
            "Large samples make the ratios reliable, because chance has less "
            "effect on the overall result",
            "A large enough sample forces the offspring to fall into a 3 : 1 "
            "ratio automatically",
        ],
        "correct_index": 2,
        "why": "Inheritance is a matter of probability, so only a large "
               "sample shows the underlying ratio clearly.",
    },
    {
        "id": "ks4-understanding-genetics-s03",
        "subtopic_slug": "understanding-genetics",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mendel proposed that a pair of heritable units separates "
                "when gametes are made. Which process, described long after "
                "his death, explains this?",
        "options": [
            "Mitosis, in which two genetically identical body cells are "
            "produced from one",
            "Meiosis, in which the chromosomes of each pair go into different "
            "gametes",
            "Fertilisation, in which two gametes fuse together to form a "
            "zygote",
            "Mutation, in which the sequence of bases in a gene is altered",
        ],
        "correct_index": 1,
        "why": "Meiosis separates the members of each chromosome pair, which "
               "is exactly the behaviour Mendel's units required.",
    },
    {
        "id": "ks4-understanding-genetics-s04",
        "subtopic_slug": "understanding-genetics",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which statement about Mendel and DNA is correct?",
        "options": [
            "Mendel's work came decades before the structure of DNA was known "
            "— he had no idea what his units were made of",
            "Mendel discovered DNA inside the cells of his pea plants and "
            "named it the heritable unit of the plant he had found",
            "Mendel used the structure of DNA to explain why some "
            "characteristics are dominant",
            "DNA was already well understood, but Mendel chose not to refer "
            "to it anywhere in his paper",
        ],
        "correct_index": 0,
        "why": "Mendel worked out the rules of inheritance without knowing "
               "the physical substance that obeyed them.",
    },
    {
        "id": "ks4-understanding-genetics-h01",
        "subtopic_slug": "understanding-genetics",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In 1900 three scientists working separately obtained the "
                "same ratios Mendel had reported. Explain why independent "
                "replication strengthened confidence in his results.",
        "options": [
            "The same result found separately by different workers is very "
            "unlikely to be one person's error or a fluke",
            "Three sets of results can be added together, which makes the "
            "ratio three times more accurate",
            "A finding is only accepted in science once exactly three "
            "separate groups have reported it",
            "The three scientists were better known than Mendel, so their "
            "word carried far more authority",
        ],
        "correct_index": 0,
        "why": "Independent workers share no method, apparatus or bias, so "
               "agreement between them is hard to explain by accident.",
    },
    {
        "id": "ks4-understanding-genetics-h02",
        "subtopic_slug": "understanding-genetics",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Darwin and Mendel worked at the same time, but Darwin never "
                "saw Mendel's results. Explain how Mendel's work would have "
                "strengthened Darwin's theory.",
        "options": [
            "It would have shown that species do not change over time, which "
            "is what Darwin needed to be able to rule out",
            "It supplied the mechanism Darwin lacked — characteristics pass "
            "on as discrete units that selection can act on",
            "It would have given Darwin a reliable way of dating the fossils "
            "he had collected on his voyage",
            "It would have proved that characteristics acquired during life "
            "are passed to the next generation",
        ],
        "correct_index": 1,
        "why": "Natural selection needs heritable variation, and Mendel had "
               "shown exactly how characteristics are inherited.",
    },
    {
        "id": "ks4-understanding-genetics-h03",
        "subtopic_slug": "understanding-genetics",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mendel's paper was barely cited before 1900. Suggest the "
                "single most important change after his death that made his "
                "ideas acceptable.",
        "options": [
            "The double-helix structure of the DNA molecule was described for "
            "the first time",
            "The electron microscope was invented, which allowed individual "
            "genes to be seen",
            "Darwin's 'On the Origin of Species' was republished in a cheaper "
            "and shorter edition",
            "Chromosomes were seen separating during cell division, giving "
            "his units a physical basis",
        ],
        "correct_index": 3,
        "why": "Once chromosomes were seen to behave as his units required, "
               "the model had something real to be about.",
    },
    {
        "id": "ks4-understanding-genetics-h04",
        "subtopic_slug": "understanding-genetics",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In peas, round seed shape (R) is dominant to wrinkled (r). "
                "Mendel crossed a wrinkled-seeded plant with a heterozygous "
                "round-seeded plant. Predict the ratio of round to wrinkled "
                "seeds in the offspring.",
        "options": [
            "3 round : 1 wrinkled",
            "All of the seeds round",
            "1 round : 1 wrinkled",
            "1 round : 3 wrinkled",
        ],
        "correct_index": 2,
        "why": "Rr × rr gives Rr and rr in equal numbers, so half the seeds "
               "are round and half are wrinkled.",
    },

    # ── fossils-extinction ────────────────────────────────────────────────
    {
        "id": "ks4-fossils-extinction-e01",
        "subtopic_slug": "fossils-extinction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by extinction.",
        "options": [
            "Every individual of a species has died, and the species exists "
            "nowhere on Earth",
            "A species has become very rare and is now found in only a few "
            "places",
            "A species has moved out of its habitat and settled somewhere "
            "else instead",
            "A species has stopped changing and no longer evolves any further",
        ],
        "correct_index": 0,
        "why": "Extinction means the last individual has died, and it is "
               "permanent — the species cannot return.",
    },
    {
        "id": "ks4-fossils-extinction-e02",
        "subtopic_slug": "fossils-extinction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Approximately how long ago was the mass extinction linked to "
                "an asteroid impact, in which the dinosaurs died out?",
        "options": [
            "66 thousand years ago",
            "66 million years ago",
            "6 million years ago",
            "660 million years ago",
        ],
        "correct_index": 1,
        "why": "The impact-linked mass extinction was about 66 million years "
               "ago, at the end of the Cretaceous period.",
    },
    {
        "id": "ks4-fossils-extinction-e03",
        "subtopic_slug": "fossils-extinction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woolly mammoth was found in Siberia with its soft tissue "
                "almost intact. Which condition preserved it?",
        "options": [
            "Mineralisation, in which the soft tissue was slowly replaced by "
            "minerals from the rock",
            "Burial in tree resin, which then hardened around the body",
            "Freezing, which stopped the microorganisms that cause decay from "
            "working",
            "Trapping in natural asphalt, which sealed the body from the air",
        ],
        "correct_index": 2,
        "why": "Decay is caused by microorganisms, and freezing stops them "
               "working, so even soft tissue survives.",
    },
    {
        "id": "ks4-fossils-extinction-e04",
        "subtopic_slug": "fossils-extinction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Human bodies thousands of years old have been found almost "
                "intact in northern Europe. Name the conditions that "
                "preserved them.",
        "options": [
            "Dry salt flats, where all the water evaporated out of the tissue",
            "Warm shallow seas, where sediment settled quickly over the body",
            "Sand dunes, where the body was buried under constantly moving "
            "sand",
            "Acidic, oxygen-poor peat bogs, in which decay could not take "
            "place",
        ],
        "correct_index": 3,
        "why": "Decay microorganisms need oxygen and cannot tolerate strong "
               "acid, so a peat bog preserves soft tissue.",
    },
    {
        "id": "ks4-fossils-extinction-s01",
        "subtopic_slug": "fossils-extinction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an organism must usually be buried quickly if it "
                "is to become a fossil.",
        "options": [
            "Rapid burial supplies all the minerals that immediately replace "
            "the whole of the animal's bones and teeth at once",
            "Burial protects the remains from scavengers and slows decay, so "
            "the hard parts last long enough to mineralise",
            "Being buried keeps the organism alive for long enough for the "
            "rock around it to harden",
            "Deep burial makes the bones much heavier, so they sink into the "
            "rock layer below",
        ],
        "correct_index": 1,
        "why": "Mineralisation takes millions of years, so the hard parts "
               "must survive scavengers and decay long enough to begin it.",
    },
    {
        "id": "ks4-fossils-extinction-s02",
        "subtopic_slug": "fossils-extinction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A species of frog is found only in one small area of cloud "
                "forest. Suggest why such species are at especially high risk "
                "of extinction.",
        "options": [
            "Small populations reproduce asexually, so no variation is ever "
            "produced in them",
            "A species with such a small range carries no genes that would "
            "let it adapt to any change at all in conditions",
            "A single fire, disease or clearance could kill every individual, "
            "as the species lives nowhere else",
            "Living in a small area means the frogs are far more likely to be "
            "hunted by humans",
        ],
        "correct_index": 2,
        "why": "With no population anywhere else, one local event removes the "
               "whole species at once.",
    },
    {
        "id": "ks4-fossils-extinction-s03",
        "subtopic_slug": "fossils-extinction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Grey squirrels were introduced to Britain and the native red "
                "squirrel then declined sharply. Explain the mechanism.",
        "options": [
            "Grey squirrels hunt and eat the red squirrels, reducing their "
            "numbers a little each year that passes",
            "Grey and red squirrels interbreed, and their offspring are "
            "always sterile",
            "Red squirrels evolved into grey squirrels as the population "
            "gradually changed colour",
            "Greys compete for the same food and shelter and carry a disease "
            "the reds have no immunity to",
        ],
        "correct_index": 3,
        "why": "An introduced species can drive a native one out by "
               "outcompeting it and by bringing a disease it has never met.",
    },
    {
        "id": "ks4-fossils-extinction-s04",
        "subtopic_slug": "fossils-extinction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The fossil record contains far more sea shells than land "
                "insects. Suggest why.",
        "options": [
            "Shells are hard and settle on sea-floor sediment where burial is "
            "quick; insects are small and fragile and usually decay first",
            "Insects were not present on Earth until long after fossils had "
            "stopped forming in rock",
            "Insects live on land, and a fossil can only ever form underwater "
            "in a sea or lake",
            "Sea shells are already made of mineral, so they turn into "
            "fossils the very moment the animal living inside them dies and "
            "sinks",
        ],
        "correct_index": 0,
        "why": "Fossilisation needs hard parts and fast burial, and a shell "
               "on a sea floor has both far more often than an insect does.",
    },
    {
        "id": "ks4-fossils-extinction-h01",
        "subtopic_slug": "fossils-extinction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A conservationist says that if the last two individuals of a "
                "species die, the species could be brought back later from a "
                "preserved museum specimen. Evaluate this claim.",
        "options": [
            "It is sound — a preserved museum specimen contains everything "
            "that a species would need in order to return one day",
            "It is sound, because extinction only counts once the species' "
            "fossils have also been destroyed",
            "It is unsound, because museum specimens are always far too badly "
            "damaged to be studied",
            "It is unsound — once every individual is dead the species is "
            "gone, and a specimen is not a breeding population",
        ],
        "correct_index": 3,
        "why": "Extinction is permanent: a species is a living, breeding "
               "population, which no preserved specimen can restore.",
    },
    {
        "id": "ks4-fossils-extinction-h02",
        "subtopic_slug": "fossils-extinction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species may still become extinct even though a "
                "few individuals survive for several more years.",
        "options": [
            "Below a certain number there are too few breeding individuals "
            "and too little variation for the population to recover",
            "The surviving individuals always stop reproducing altogether as "
            "soon as their species has become genuinely rare in the wild",
            "The last individuals of any species lose the ability to feed "
            "themselves in the wild",
            "A species is counted as extinct as soon as its numbers fall "
            "below one thousand",
        ],
        "correct_index": 0,
        "why": "A handful of survivors cannot rebuild a population: too few "
               "mates, and too little variation to withstand any change.",
    },
    {
        "id": "ks4-fossils-extinction-h03",
        "subtopic_slug": "fossils-extinction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the mass extinction linked to an asteroid impact "
                "with the loss of species happening today. State the main "
                "difference.",
        "options": [
            "Today's losses are all caused by one single sudden event, while "
            "the asteroid impact acted very slowly over a long time instead",
            "Today's losses are driven mainly by human activity — habitat "
            "destruction, climate change, pollution and overexploitation",
            "Today's losses affect only plants, while the asteroid impact "
            "affected only the animals",
            "There is no difference — both were caused by a rapid change in "
            "the Earth's orbit around the Sun",
        ],
        "correct_index": 1,
        "why": "The present extinction crisis has a human cause, which also "
               "means it is one humans can act to slow.",
    },
    {
        "id": "ks4-fossils-extinction-h04",
        "subtopic_slug": "fossils-extinction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A palaeontologist argues that because no fossils of a "
                "species appear in a particular rock layer, the species "
                "cannot have been alive then. Explain the error.",
        "options": [
            "Rock layers form in a random order, so the age of any given "
            "layer cannot be worked out",
            "Fossils move upwards through rock over time, so the layer a "
            "fossil is found in means nothing",
            "Absence of fossils is weak evidence — fossilisation is rare, and "
            "many rocks are eroded or not yet excavated",
            "Fossils only ever form for species that were already close to "
            "becoming extinct",
        ],
        "correct_index": 2,
        "why": "Most organisms leave no fossil at all, so finding none is not "
               "evidence that none were there.",
    },

    # ── resistant-bacteria ────────────────────────────────────────────────
    {
        "id": "ks4-resistant-bacteria-e01",
        "subtopic_slug": "resistant-bacteria",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where is Staphylococcus aureus normally found, and in "
                "roughly what proportion of people?",
        "options": [
            "In the lungs of about 5% of people, where it causes no symptoms",
            "Only in hospital patients who are already seriously ill",
            "In the gut of every person, where it helps to digest food",
            "Harmlessly on the skin of about 30% of people",
        ],
        "correct_index": 3,
        "why": "It is an ordinary skin bacterium on roughly a third of "
               "people; resistance is what makes MRSA dangerous, not the "
               "species.",
    },
    {
        "id": "ks4-resistant-bacteria-e02",
        "subtopic_slug": "resistant-bacteria",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Antibiotics are effective against which kind of infection?",
        "options": [
            "Viral infections only",
            "Fungal infections only",
            "Bacterial infections only",
            "All infections, whatever their cause",
        ],
        "correct_index": 2,
        "why": "Antibiotics attack structures and processes that only "
               "bacteria have, so they do nothing to a virus.",
    },
    {
        "id": "ks4-resistant-bacteria-e03",
        "subtopic_slug": "resistant-bacteria",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Under good conditions, roughly how often can a population of "
                "bacteria double in number?",
        "options": [
            "Every 20 seconds",
            "Every 20 minutes",
            "Every 20 hours",
            "Every 20 days",
        ],
        "correct_index": 1,
        "why": "Doubling every 20 minutes is why a few surviving resistant "
               "bacteria can take over a population so quickly.",
    },
    {
        "id": "ks4-resistant-bacteria-e04",
        "subtopic_slug": "resistant-bacteria",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a selection pressure.",
        "options": [
            "A factor in the environment that makes some individuals more "
            "likely to survive and reproduce than others",
            "A substance that causes new mutations to appear in the DNA of "
            "any organism that comes into contact with it",
            "The physical force a predator applies to its prey at the moment "
            "it catches it",
            "The change an organism makes to its own body in order to help it "
            "survive",
        ],
        "correct_index": 0,
        "why": "A selection pressure decides who survives; it does not create "
               "the variation it acts on.",
    },
    {
        "id": "ks4-resistant-bacteria-s01",
        "subtopic_slug": "resistant-bacteria",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An infection contains about 10 million bacteria, two of "
                "which happen to carry a resistance mutation. The patient is "
                "given the antibiotic. Predict what the surviving population "
                "is like a week later.",
        "options": [
            "All of the bacteria will have become resistant, because the drug "
            "made them mutate in order to survive",
            "The two resistant bacteria will be outnumbered and killed off by "
            "all of the others",
            "Almost all will be descendants of those two — the antibiotic "
            "killed the rest, and the survivors reproduced",
            "The population will be unchanged, because two bacteria out of 10 "
            "million are too few to matter",
        ],
        "correct_index": 2,
        "why": "The antibiotic removes the competition, and bacteria "
               "reproduce fast enough for two survivors to refill the "
               "population.",
    },
    {
        "id": "ks4-resistant-bacteria-s02",
        "subtopic_slug": "resistant-bacteria",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why prescribing an antibiotic for a sore throat that "
                "is caused by a virus still makes resistance worse.",
        "options": [
            "The drug cannot touch the virus, but it still kills "
            "non-resistant bacteria in the body and leaves resistant ones "
            "behind",
            "The virus itself becomes resistant to the antibiotic and passes "
            "that resistance on",
            "The antibiotic causes the virus to mutate until it turns into a "
            "bacterium",
            "An antibiotic that has been used against a virus loses its "
            "strength and no longer works on any bacteria afterwards at all",
        ],
        "correct_index": 0,
        "why": "The patient gets no benefit, but the harmless bacteria they "
               "carry are still selected for resistance.",
    },
    {
        "id": "ks4-resistant-bacteria-s03",
        "subtopic_slug": "resistant-bacteria",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Antibiotics are widely used in livestock farming. Explain "
                "how this contributes to resistance in bacteria that infect "
                "people.",
        "options": [
            "Antibiotic residues in the meat mutate the bacteria living in "
            "the person who eats it",
            "Farm animals pass their own immunity to people, who then need "
            "stronger drugs to recover",
            "Antibiotics given to animals build up in the soil and destroy "
            "only the useful bacteria",
            "Resistant bacteria selected in the animals can reach people "
            "through food and the environment",
        ],
        "correct_index": 3,
        "why": "Selection happens in the animal, but the resistant bacteria "
               "do not stay there — they travel into the food chain.",
    },
    {
        "id": "ks4-resistant-bacteria-s04",
        "subtopic_slug": "resistant-bacteria",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital ward introduces strict hand hygiene for all staff "
                "and visitors. Explain how this reduces the harm caused by "
                "MRSA.",
        "options": [
            "Washing the hands thoroughly with soap makes the MRSA bacteria "
            "lose the resistance gene that they have been carrying on the "
            "ward until then",
            "It stops resistant bacteria being carried between patients, so "
            "fewer people are infected with a strain the antibiotics cannot "
            "treat",
            "Soap prevents bacteria from mutating, so no new resistance is "
            "able to appear",
            "Clean hands allow the antibiotics to work on bacteria that are "
            "already resistant",
        ],
        "correct_index": 1,
        "why": "Hygiene cannot remove resistance, but it does stop the "
               "resistant strain reaching the next patient.",
    },
    {
        "id": "ks4-resistant-bacteria-h01",
        "subtopic_slug": "resistant-bacteria",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'When bacteria are exposed to an "
                "antibiotic they change their DNA so that they can survive.' "
                "Explain what is wrong with this.",
        "options": [
            "Nothing is wrong with it — bacteria are able to alter their own "
            "DNA whenever the environment around them changes in some way, as "
            "it does here",
            "Bacteria do not change in response to the drug — resistance "
            "comes from random mutations already present, and the antibiotic "
            "only selects them",
            "Bacteria cannot change their DNA at all, so the resistance must "
            "have been inherited from another species",
            "The antibiotic changes the bacteria's DNA for them, rather than "
            "the bacteria doing it themselves",
        ],
        "correct_index": 1,
        "why": "The mutation happens by chance before the drug arrives; the "
               "antibiotic is the filter, never the cause.",
    },
    {
        "id": "ks4-resistant-bacteria-h02",
        "subtopic_slug": "resistant-bacteria",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why pharmaceutical companies have reduced their "
                "investment in developing new antibiotics.",
        "options": [
            "There are no bacteria left against which a new antibiotic could "
            "be properly tested",
            "New antibiotics can no longer be manufactured in large enough "
            "quantities to be useful",
            "Governments have made the development of any new antibiotic "
            "illegal in most countries",
            "A short course of antibiotics earns far less than a drug taken "
            "daily for a long-term illness",
        ],
        "correct_index": 3,
        "why": "A drug used for a week brings in far less than one taken for "
               "years, so the commercial incentive is weak.",
    },
    {
        "id": "ks4-resistant-bacteria-h03",
        "subtopic_slug": "resistant-bacteria",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phage therapy uses viruses that infect and destroy bacteria. "
                "Evaluate it as an alternative to antibiotics.",
        "options": [
            "It can kill bacteria that antibiotics no longer affect, but "
            "bacteria may be selected for resistance to phages too, and it is "
            "not yet widely available",
            "It is a complete and permanent solution, because no bacterium "
            "anywhere is capable of resisting a virus that attacks it in the "
            "way that a phage does",
            "It is of no use at all, because viruses can only infect the "
            "cells of animals and of plants",
            "It works only on those bacteria that are still sensitive to "
            "every antibiotic in current use",
        ],
        "correct_index": 0,
        "why": "Phages attack by a different route, so resistant bacteria are "
               "vulnerable — but selection acts on phage resistance too.",
    },
    {
        "id": "ks4-resistant-bacteria-h04",
        "subtopic_slug": "resistant-bacteria",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says resistance is a problem because 'antibiotics "
                "get weaker the more they are used'. Explain why this is "
                "wrong.",
        "options": [
            "The antibiotic does gradually weaken with use, but only if it "
            "has been stored somewhere warm for far too long before it is "
            "given to a patient",
            "The antibiotic gets stronger with use, so the dose given has to "
            "be reduced over time instead",
            "The antibiotic molecule is unchanged — it is the bacterial "
            "population that has changed, because resistant bacteria now make "
            "up most of it",
            "Antibiotics never weaken, and antibiotic resistance is not "
            "actually a real problem at all",
        ],
        "correct_index": 2,
        "why": "The drug is the same drug; what has evolved is the population "
               "of bacteria it is being used against.",
    },

    # ── classification-living-organisms ───────────────────────────────────
    {
        "id": "ks4-classification-living-organisms-e01",
        "subtopic_slug": "classification-living-organisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A biologist writes the lion's name as Panthera leo and the "
                "tiger's as Panthera tigris. What does this tell you about "
                "the two animals?",
        "options": [
            "They are the same species, known by two different Latin names",
            "They are different species belonging to the same genus, so they "
            "are closely related",
            "They belong to one species but are placed in two separate "
            "kingdoms",
            "The lion must be a variety of tiger, since both of their names "
            "begin with Panthera in Latin",
        ],
        "correct_index": 1,
        "why": "The first word of a binomial name is the genus, so a shared "
               "first word means two closely related species.",
    },
    {
        "id": "ks4-classification-living-organisms-e02",
        "subtopic_slug": "classification-living-organisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Put the Linnaean groups in order from the largest group to "
                "the smallest.",
        "options": [
            "Kingdom, Class, Phylum, Family, Order, Genus, Species",
            "Species, Genus, Family, Order, Class, Phylum, Kingdom",
            "Kingdom, Phylum, Class, Order, Family, Genus, Species",
            "Phylum, Kingdom, Order, Class, Genus, Family, Species",
        ],
        "correct_index": 2,
        "why": "Each group is contained inside the one before it, from "
               "kingdom down to the single species.",
    },
    {
        "id": "ks4-classification-living-organisms-e03",
        "subtopic_slug": "classification-living-organisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Who proposed the three-domain system, and when?",
        "options": [
            "Linnaeus, in the 18th century",
            "Darwin, in 1859",
            "Mendel, in 1866",
            "Woese, in 1977",
        ],
        "correct_index": 3,
        "why": "Carl Woese proposed the three domains in 1977, on the "
               "evidence of ribosomal RNA sequences.",
    },
    {
        "id": "ks4-classification-living-organisms-e04",
        "subtopic_slug": "classification-living-organisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which domain contains all the organisms whose cells have a "
                "nucleus?",
        "options": ["Eukarya", "Archaea", "Bacteria", "Protista"],
        "correct_index": 0,
        "why": "Eukarya covers every organism with a membrane-bound nucleus — "
               "animals, plants, fungi and protists.",
    },
    {
        "id": "ks4-classification-living-organisms-s01",
        "subtopic_slug": "classification-living-organisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A horse and a donkey can breed together, but the mule they "
                "produce is sterile. Explain why horses and donkeys are "
                "classed as two different species.",
        "options": [
            "Because a mule looks quite different from both of the parent "
            "animals that produced it originally",
            "Because the horse and the donkey are usually kept on different "
            "kinds of farm",
            "Because members of one species must produce fertile offspring, "
            "and the mule cannot reproduce",
            "Because the horse and the donkey are placed in two entirely "
            "different kingdoms",
        ],
        "correct_index": 2,
        "why": "The test for one species is fertile offspring, not appearance "
               "or the ability to mate at all.",
    },
    {
        "id": "ks4-classification-living-organisms-s02",
        "subtopic_slug": "classification-living-organisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A prokaryote is found in a hot spring at 90 °C. Its "
                "ribosomal RNA sequence is more similar to that of yeast than "
                "to that of E. coli. Which domain does it belong to?",
        "options": ["Archaea", "Bacteria", "Eukarya", "Protista"],
        "correct_index": 0,
        "why": "Archaea are prokaryotes whose rRNA shows a more recent shared "
               "ancestor with eukaryotes than bacteria have.",
    },
    {
        "id": "ks4-classification-living-organisms-s03",
        "subtopic_slug": "classification-living-organisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two beetle species are in the same family but different "
                "genera. Two other beetle species are in the same genus. "
                "Which pair is more closely related?",
        "options": [
            "The pair in the same family, because a family contains a much "
            "larger number of species",
            "The pair in the same genus, because a genus is a smaller group "
            "sharing more recent ancestry",
            "Both pairs are related to each other to exactly the same degree",
            "The pair in the same family, because family comes lower down the "
            "classification hierarchy",
        ],
        "correct_index": 1,
        "why": "The smaller the shared group, the more recently the two "
               "lineages separated.",
    },
    {
        "id": "ks4-classification-living-organisms-s04",
        "subtopic_slug": "classification-living-organisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest one reason DNA sequences are now used alongside body "
                "structure when an organism is classified.",
        "options": [
            "DNA is a great deal easier to see and to measure than the "
            "structure of an organism's body",
            "DNA shows which of two organisms is the more advanced and highly "
            "evolved of the pair",
            "An organism's own DNA gradually changes over time to match "
            "whichever habitat it happens to be living in at that moment",
            "DNA gives a direct measure of how similar two organisms' genes "
            "are, so it reveals relationships that appearance would hide",
        ],
        "correct_index": 3,
        "why": "Observable features can mislead; the base sequence records "
               "ancestry directly.",
    },
    {
        "id": "ks4-classification-living-organisms-h01",
        "subtopic_slug": "classification-living-organisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "On an evolutionary tree, species W and X branch from one "
                "node. That node and species Y branch from an older node. "
                "That older node and species Z branch from the oldest node of "
                "all. Which species share their most recent common ancestor "
                "with Y?",
        "options": [
            "Z only, because Z branches nearest to the base of the whole tree",
            "W only, because W is the species named first when the tree is "
            "described",
            "Neither of them — Y has no common ancestor with the other three "
            "species",
            "W and X equally, because Y's line joined the tree before those "
            "two separated",
        ],
        "correct_index": 3,
        "why": "Y branches from the node ancestral to both W and X, so it is "
               "equally related to each of them.",
    },
    {
        "id": "ks4-classification-living-organisms-h02",
        "subtopic_slug": "classification-living-organisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says humans are 'more evolved' than bacteria "
                "because humans sit at the top of the evolutionary tree. "
                "Evaluate this.",
        "options": [
            "It is correct — whichever species is drawn highest up on a tree "
            "must be the one that has evolved the furthest of them all so far",
            "It is wrong — every living species has been evolving for the "
            "same length of time, and a tree shows relationships, not rank",
            "It is correct, because bacteria stopped evolving as soon as more "
            "complex life appeared",
            "It is wrong, because bacteria are in fact the most highly "
            "evolved organisms on the tree",
        ],
        "correct_index": 1,
        "why": "A tree records who is related to whom, and every branch tip "
               "on it is equally modern.",
    },
    {
        "id": "ks4-classification-living-organisms-h03",
        "subtopic_slug": "classification-living-organisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A new prokaryote is discovered in a salt lake. Suggest what "
                "evidence a biologist would need to decide whether it is a "
                "bacterium or an archaeon.",
        "options": [
            "Sequence its ribosomal RNA and compare it with known groups, "
            "since the two look alike under a microscope",
            "Measure the size of its cells under a light microscope and "
            "compare them with those of E. coli bacteria in a lab",
            "Test whether it can survive in salty water, since only archaea "
            "are able to do this",
            "Check whether it has a nucleus, which archaea possess and "
            "bacteria do not possess",
        ],
        "correct_index": 0,
        "why": "Archaea and bacteria are indistinguishable by eye, so the "
               "decision has to be made on molecular evidence.",
    },
    {
        "id": "ks4-classification-living-organisms-h04",
        "subtopic_slug": "classification-living-organisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a tree built from DNA sequences can group two "
                "organisms differently from a tree built only on what they "
                "look like.",
        "options": [
            "DNA sequences change at random, so any tree built from them is "
            "unreliable and can be ignored",
            "Appearance is fixed entirely by an organism's genes, so the two "
            "kinds of tree can never disagree",
            "Appearance can be similar in organisms with similar ways of "
            "life, while DNA records ancestry directly",
            "A tree built from DNA always places the largest organisms "
            "nearest to the top of the tree",
        ],
        "correct_index": 2,
        "why": "Living the same way can make unrelated organisms look alike, "
               "but it does not make their base sequences alike.",
    },
]
