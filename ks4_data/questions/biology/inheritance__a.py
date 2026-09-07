"""Biology · Inheritance, variation and evolution — part A (10 of 19 subtopics).

Covers sexual-asexual-reproduction, meiosis, advantages-sexual-asexual,
dna-genome, dna-structure, genetic-inheritance, inherited-disorders,
sex-determination, variation and evolution-natural-selection.

Distractors are built from the declared misconceptions in each subtopic's
brief: mitosis/meiosis outcomes swapped (2 vs 4 cells, identical vs varied,
diploid vs haploid), a carrier believed to show the disorder, genotype
confused with phenotype, "dominant means more common", the mother blamed for
a child's sex, acquired characteristics believed heritable, and natural
selection described as an organism choosing or needing to adapt. Every
genetic cross is written out in words — no question needs a figure.
"""

TOPIC = "inheritance"
SUBJECT = "biology"

QUESTIONS = [
    # ── sexual-asexual-reproduction ─────────────────────────────────────
    {
        "id": "ks4-sexual-asexual-reproduction-e01",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of parent organisms needed for asexual "
                "reproduction.",
        "options": [
            "Two parents, each providing one gamete",
            "Two parents, but only one of them contributes DNA",
            "One parent, with no gametes involved at all",
            "One parent, but two gametes are still needed",
        ],
        "correct_index": 2,
        "why": "Asexual reproduction uses a single parent dividing by "
               "mitosis, so no gametes are made and none fuse.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-e02",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener grows a new potato plant from a tuber of an "
                "existing plant. State the term used for the offspring "
                "produced this way.",
        "options": [
            "Clones — genetically identical to the parent plant",
            "Hybrids — a mixture of two different parent plants",
            "Zygotes — formed when two gametes fuse together",
            "Mutants — each one differs slightly from the parent",
        ],
        "correct_index": 0,
        "why": "A tuber produces new plants by mitosis, so every plant "
               "carries exactly the same alleles as the parent.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-e03",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process in which a male gamete and a female gamete "
                "fuse together.",
        "options": [
            "Meiosis — halving the chromosome number",
            "Mitosis — copying a cell exactly",
            "Binary fission — splitting one cell into two",
            "Fertilisation — forming a zygote",
        ],
        "correct_index": 3,
        "why": "Fertilisation is the fusion of two gametes to form a zygote "
               "with the full chromosome number restored.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-e04",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of chromosomes in a human zygote "
                "immediately after fertilisation.",
        "options": [
            "23 chromosomes, because only one gamete's set is kept",
            "46 chromosomes, because 23 from each gamete combine",
            "92 chromosomes, because each gamete carried 46",
            "46 chromosomes, because the zygote doubles its 23",
        ],
        "correct_index": 1,
        "why": "Each gamete carries 23 chromosomes, and fertilisation adds "
               "them together to restore the full number of 46.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-s01",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower wants every strawberry plant in a field to produce "
                "fruit of exactly the same size. Explain which method of "
                "reproduction the grower should use.",
        "options": [
            "Asexual reproduction from runners, because every plant is a "
            "clone of the parent",
            "Sexual reproduction from seed, because offspring inherit the "
            "best of both parents",
            "Sexual reproduction from seed, because meiosis copies the "
            "parent plant exactly",
            "Asexual reproduction from runners, because mitosis produces "
            "varied offspring",
        ],
        "correct_index": 0,
        "why": "Runners produce offspring by mitosis, so every plant is "
               "genetically identical to the parent and to each other.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-s02",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fish releases thousands of eggs, which are fertilised in "
                "the water by sperm from a male. Explain why the young fish "
                "are not identical to one another.",
        "options": [
            "Each young fish was produced by mitosis, which shuffles the "
            "parent's genes",
            "The eggs were laid in different places, and position decides "
            "which alleles are inherited",
            "Fertilisation copies the mother's DNA into every egg in a "
            "slightly different way",
            "Each egg and sperm carries a different combination of alleles, "
            "and pairing is random",
        ],
        "correct_index": 3,
        "why": "Gametes are made by meiosis, so each carries its own "
               "combination of alleles, and which sperm meets which egg is "
               "a matter of chance.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-s03",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell in a human testis divides by meiosis. Describe the "
                "cells that are produced.",
        "options": [
            "Two cells, each with 46 chromosomes, identical to the parent "
            "cell",
            "Four cells, each with 23 chromosomes, genetically different "
            "from one another",
            "Two cells, each with 23 chromosomes, genetically identical to "
            "one another",
            "Four cells, each with 46 chromosomes, genetically different "
            "from one another",
        ],
        "correct_index": 1,
        "why": "Meiosis halves the chromosome number and produces four "
               "gametes, each with its own combination of alleles.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-s04",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why offspring produced by asexual reproduction are "
                "genetically identical to their parent.",
        "options": [
            "Because they are produced by meiosis, which halves the "
            "chromosome number",
            "Because two gametes from the same parent fuse together at "
            "fertilisation",
            "Because they are produced by mitosis, which copies the "
            "parent's DNA exactly",
            "Because they grow in the same environment as the parent "
            "organism did",
        ],
        "correct_index": 2,
        "why": "Mitosis makes an exact copy of the parent's DNA, so no new "
               "combinations of alleles can arise.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-h01",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Asexual reproduction is better than "
                "sexual reproduction because all the offspring are perfectly "
                "adapted.' Evaluate this statement.",
        "options": [
            "It is correct, because clones always inherit the parent's best "
            "characteristics",
            "It is correct, because asexual reproduction is faster in every "
            "kind of environment",
            "It is wrong, because asexual offspring are always less well "
            "adapted than their parent",
            "It is true only while the environment stays the same, because "
            "clones cannot adapt to change",
        ],
        "correct_index": 3,
        "why": "Clones inherit the parent's adaptations exactly, which helps "
               "only for as long as conditions stay the ones the parent was "
               "suited to.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-h02",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aphids reproduce asexually through the summer and sexually "
                "in the autumn. Explain, in terms of chromosome number, why "
                "only the autumn offspring involve meiosis.",
        "options": [
            "Meiosis is needed in autumn because cold damages chromosomes "
            "and they must be repaired",
            "Meiosis is needed only when gametes are made, so that fusion "
            "restores the full number",
            "Meiosis is needed in summer too, but the summer offspring lose "
            "the extra chromosomes",
            "Meiosis is needed in autumn because sexual reproduction "
            "doubles the chromosome number",
        ],
        "correct_index": 1,
        "why": "Only sexual reproduction involves two gametes fusing, so "
               "only then must the chromosome number be halved first.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-h03",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two sisters with the same parents are not genetically "
                "identical, but two strawberry plants grown from the same "
                "runner are. Explain this difference.",
        "options": [
            "The sisters were produced by mitosis and the plants by meiosis",
            "The sisters inherited different genes, while the plants "
            "inherited genes from two parents",
            "The sisters came from different gametes joined at "
            "fertilisation; the plants came from one parent by mitosis",
            "The sisters grew up in different conditions, while the two "
            "plants grew in the same soil",
        ],
        "correct_index": 2,
        "why": "Every gamete carries a different combination of alleles, so "
               "each fertilisation gives a unique genotype, while mitosis "
               "copies one parent exactly.",
    },
    {
        "id": "ks4-sexual-asexual-reproduction-h04",
        "subtopic_slug": "sexual-asexual-reproduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An entire field of a crop is grown from cuttings taken from "
                "one high-yielding plant. Suggest the greatest long-term "
                "risk of doing this.",
        "options": [
            "A new disease could destroy the whole crop, because every "
            "plant has the same alleles",
            "The plants would gradually become smaller, because cuttings "
            "lose DNA each generation",
            "The plants would begin to reproduce sexually, because clones "
            "cannot survive on their own",
            "The yield would fall each year, because mitosis copies DNA "
            "less accurately over time",
        ],
        "correct_index": 0,
        "why": "Genetically identical plants are all equally susceptible to "
               "the same pathogen, so one disease can reach every plant.",
    },

    # ── meiosis ─────────────────────────────────────────────────────────
    {
        "id": "ks4-meiosis-e01",
        "subtopic_slug": "meiosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a haploid cell.",
        "options": [
            "A cell containing two of each type of chromosome",
            "A cell containing one of each type of chromosome",
            "A cell containing twice the normal number of chromosomes",
            "A cell containing no chromosomes at all",
        ],
        "correct_index": 1,
        "why": "Haploid means a single set of chromosomes — in humans 23, "
               "one taken from each pair.",
    },
    {
        "id": "ks4-meiosis-e02",
        "subtopic_slug": "meiosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the organs in which meiosis takes place in humans.",
        "options": [
            "The liver and the kidneys",
            "The bone marrow and the skin",
            "The lungs and the heart",
            "The testes and the ovaries",
        ],
        "correct_index": 3,
        "why": "Meiosis produces gametes, and gametes are made only in the "
               "gonads — the testes and the ovaries.",
    },
    {
        "id": "ks4-meiosis-e03",
        "subtopic_slug": "meiosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how many divisions take place during meiosis, and how "
                "many cells result.",
        "options": [
            "Two divisions, giving four cells in total",
            "One division, giving two cells in total",
            "Three divisions, giving six cells in total",
            "Four divisions, giving eight cells in total",
        ],
        "correct_index": 0,
        "why": "Meiosis I separates the homologous pairs and meiosis II "
               "separates the chromatids, so one cell becomes four.",
    },
    {
        "id": "ks4-meiosis-e04",
        "subtopic_slug": "meiosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the homologous pairs during the first "
                "division of meiosis.",
        "options": [
            "The two chromatids of each chromosome are pulled apart",
            "The pairs are copied, so each new cell receives a double set",
            "The two chromosomes of each pair are separated into different "
            "cells",
            "The pairs fuse together to form single longer chromosomes",
        ],
        "correct_index": 2,
        "why": "Separating the homologous pairs in meiosis I is the step "
               "that halves the chromosome number.",
    },
    {
        "id": "ks4-meiosis-s01",
        "subtopic_slug": "meiosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An organism has 12 chromosomes in each of its body cells. "
                "Determine the number of chromosomes in each cell produced "
                "when one of these cells divides by meiosis.",
        "options": [
            "12 chromosomes, because the number is kept the same",
            "24 chromosomes, because the chromosomes are copied first",
            "6 chromosomes, because the number is halved",
            "3 chromosomes, because the number is halved twice",
        ],
        "correct_index": 2,
        "why": "Meiosis halves the chromosome number once — the second "
               "division separates chromatids, not pairs — so 12 becomes 6.",
    },
    {
        "id": "ks4-meiosis-s02",
        "subtopic_slug": "meiosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens during the second division of "
                "meiosis.",
        "options": [
            "Homologous chromosomes pair up and exchange sections of DNA "
            "with each other",
            "The two chromatids of each chromosome separate, giving four "
            "haploid cells",
            "The chromosome number is halved for a second time, giving four "
            "haploid cells",
            "The DNA is replicated a second time so each cell receives a "
            "full set",
        ],
        "correct_index": 1,
        "why": "The chromosome number was already halved in meiosis I, so "
               "meiosis II simply separates the chromatids of each "
               "chromosome.",
    },
    {
        "id": "ks4-meiosis-s03",
        "subtopic_slug": "meiosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what physically happens to chromosomes during "
                "crossing over.",
        "options": [
            "Whole chromosomes swap between the two new cells at random",
            "Chromatids are pulled apart and shared out between four cells",
            "Extra copies of some genes are made and inserted into the "
            "chromosome",
            "Homologous chromosomes exchange matching sections of DNA with "
            "each other",
        ],
        "correct_index": 3,
        "why": "Matching lengths are swapped between the chromosome from the "
               "mother and the one from the father, putting new "
               "combinations of alleles on each.",
    },
    {
        "id": "ks4-meiosis-s04",
        "subtopic_slug": "meiosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plant species has 20 chromosomes in each body cell. "
                "Determine the number of chromosomes in a cell of an embryo "
                "formed after fertilisation.",
        "options": [
            "20, because two haploid gametes of 10 chromosomes fused",
            "10, because the gametes that fused were haploid",
            "40, because two body cells of 20 chromosomes fused",
            "20, because one gamete of 20 chromosomes divided by mitosis",
        ],
        "correct_index": 0,
        "why": "Meiosis makes gametes with 10 chromosomes, and fertilisation "
               "adds two of them to restore the diploid number of 20.",
    },
    {
        "id": "ks4-meiosis-h01",
        "subtopic_slug": "meiosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cell containing four pairs of chromosomes divides by "
                "meiosis. Explain why the gametes produced are unlikely to "
                "be identical, even if no crossing over occurs.",
        "options": [
            "Each pair separates independently, so gametes receive "
            "different mixtures of the parent's chromosomes",
            "Each gamete keeps only the chromosomes that were inherited "
            "from the mother, so all four of them differ",
            "Meiosis copies chromosomes inaccurately, so small differences "
            "appear in every gamete",
            "The four gametes each receive a different number of "
            "chromosomes from the parent cell",
        ],
        "correct_index": 0,
        "why": "Which chromosome of each pair goes to which cell is decided "
               "at random and separately for every pair, so the "
               "combinations differ.",
    },
    {
        "id": "ks4-meiosis-h02",
        "subtopic_slug": "meiosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fault in meiosis produces a human gamete containing 24 "
                "chromosomes instead of 23. Predict the number of "
                "chromosomes in a zygote formed from this gamete and a "
                "normal one.",
        "options": [
            "46 chromosomes, because the extra chromosome is destroyed",
            "23 chromosomes, because the extra chromosome prevents fusion",
            "47 chromosomes, which is one chromosome too many",
            "48 chromosomes, because both gametes gain one chromosome",
        ],
        "correct_index": 2,
        "why": "Fertilisation simply adds the two gametes' chromosomes "
               "together: 24 + 23 = 47.",
    },
    {
        "id": "ks4-meiosis-h03",
        "subtopic_slug": "meiosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a species reproducing by mitosis alone would be "
                "expected to evolve more slowly than one using meiosis and "
                "fertilisation.",
        "options": [
            "Mitosis produces haploid cells, so useful alleles are lost "
            "each generation",
            "Mitosis makes no new combinations of alleles, so selection has "
            "far less variation to act on",
            "Mitosis prevents mutations from occurring, so no new alleles "
            "can ever arise",
            "Mitosis doubles the chromosome number each generation, which "
            "limits reproduction",
        ],
        "correct_index": 1,
        "why": "Evolution needs variation to select from, and only meiosis "
               "and fertilisation reshuffle alleles into new combinations "
               "each generation.",
    },
    {
        "id": "ks4-meiosis-h04",
        "subtopic_slug": "meiosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the cells produced by meiosis in a testis "
                "cannot be used to repair damaged muscle tissue.",
        "options": [
            "They are too small to be able to divide again once formed",
            "They contain DNA from the father only, so they cannot be used "
            "to build any body cells",
            "They have not replicated their DNA, so they are unable to grow",
            "They are haploid, so they carry only half the genetic "
            "information a body cell needs",
        ],
        "correct_index": 3,
        "why": "Repair requires diploid cells with a full set of "
               "chromosomes, and meiosis produces haploid cells instead.",
    },

    # ── advantages-sexual-asexual ───────────────────────────────────────
    {
        "id": "ks4-advantages-sexual-asexual-e01",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the proportion of its genes a parent passes on to "
                "each offspring in asexual reproduction.",
        "options": [
            "100% — the offspring is a genetic copy of the single parent",
            "50% — the other half comes from the surrounding environment",
            "50% — the other half comes from a second parent organism",
            "25% — the genes are shared out between four offspring",
        ],
        "correct_index": 0,
        "why": "Only one parent is involved and mitosis copies its DNA "
               "exactly, so all of its alleles are passed on.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-e02",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one disadvantage of sexual reproduction compared with "
                "asexual reproduction.",
        "options": [
            "The offspring produced are all genetically identical",
            "The chromosome number doubles with every generation",
            "Time and energy must be spent finding a mate",
            "The population cannot adapt to a changing environment",
        ],
        "correct_index": 2,
        "why": "Sexual reproduction needs two parents, so an organism must "
               "find a mate before it can reproduce at all.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-e03",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which type of reproduction allows a population to "
                "increase in number more quickly.",
        "options": [
            "Sexual reproduction, because two parents each produce offspring",
            "Asexual reproduction, because no mate has to be found first",
            "Sexual reproduction, because meiosis makes four cells at a time",
            "Neither — both types produce offspring at the same rate",
        ],
        "correct_index": 1,
        "why": "A single parent can divide again and again without the delay "
               "and energy cost of finding a mate.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-e04",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of cell division used by an organism that is "
                "reproducing asexually.",
        "options": [
            "Meiosis, which halves the chromosome number",
            "Meiosis, followed immediately by fertilisation",
            "Binary fission, followed by meiosis in the offspring",
            "Mitosis, which produces genetically identical cells",
        ],
        "correct_index": 3,
        "why": "Asexual reproduction copies the parent by mitosis, which is "
               "why the offspring are clones.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-s01",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A coral living on a reef whose conditions have been stable "
                "for centuries reproduces asexually. Suggest why this is an "
                "advantage in that habitat.",
        "options": [
            "Variation among the offspring would allow the coral to survive "
            "if conditions on the reef changed",
            "Two parents are needed, so the colony spreads over a wider area",
            "The offspring each inherit half of both parents' successful "
            "alleles",
            "The parent is already well suited to the reef, and every clone "
            "inherits that suitability",
        ],
        "correct_index": 3,
        "why": "In unchanging conditions the parent's combination of alleles "
               "is already successful, so copying it exactly is the best "
               "strategy.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-s02",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A grower plants 500 apple trees grown from cuttings of one "
                "tree and 500 grown from seed. Compare the variation within "
                "the two groups.",
        "options": [
            "The trees from cuttings are genetically identical; the trees "
            "from seed all differ",
            "The trees from cuttings all differ; the trees from seed are "
            "genetically identical",
            "Both groups are genetically identical, because they belong to "
            "the same species",
            "Both groups vary equally, because every tree grows in slightly "
            "different soil",
        ],
        "correct_index": 0,
        "why": "Cuttings are produced by mitosis and are clones, while seeds "
               "come from fertilisation, which combines alleles from two "
               "parents.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-s03",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why sexual reproduction is described as slower than "
                "asexual reproduction.",
        "options": [
            "Because meiosis happens twice, which doubles the time each "
            "division takes",
            "Because fertilisation can only take place once a year in most "
            "species",
            "Because a mate must be found and far fewer offspring are "
            "produced at a time",
            "Because the chromosome number must be halved and then restored "
            "again",
        ],
        "correct_index": 2,
        "why": "The time and energy spent finding a mate, together with "
               "smaller numbers of offspring, make sexual reproduction the "
               "slower route to a large population.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-s04",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a species that reproduces only asexually is at "
                "greater risk if its habitat changes quickly.",
        "options": [
            "Its offspring would inherit only half of the parent's alleles",
            "There are no differently adapted individuals for selection to "
            "favour",
            "Its chromosome number would fall with every generation that "
            "passed",
            "It would need far more energy for each offspring it produced",
        ],
        "correct_index": 1,
        "why": "Without variation, every individual responds to the new "
               "conditions in the same way, so none is better placed to "
               "survive them.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-h01",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim: 'Offspring produced asexually are "
                "always genetically identical to their parent.'",
        "options": [
            "Correct — mitosis can never introduce a genetic change of any "
            "kind",
            "Almost always true, but a mutation during DNA replication can "
            "make an offspring differ",
            "Wrong — asexual offspring show just as much variation as "
            "sexually produced offspring do",
            "Wrong — asexual offspring inherit half of their alleles from a "
            "second parent",
        ],
        "correct_index": 1,
        "why": "Mitosis copies DNA exactly, but random copying errors still "
               "happen, so clones are not guaranteed to be identical.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-h02",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A single seed of a plant lands on a bare volcanic island "
                "and the plant then spreads asexually. Explain why asexual "
                "reproduction is an advantage here, even though it produces "
                "no variation.",
        "options": [
            "It produces varied offspring quickly, so many types colonise "
            "the island at once",
            "It allows the plant to fertilise itself, which creates new "
            "allele combinations",
            "It halves the chromosome number, so less energy is spent on "
            "each offspring",
            "There is no mate available, and one parent can colonise the "
            "empty island rapidly",
        ],
        "correct_index": 3,
        "why": "A lone coloniser has no mate, and asexual reproduction lets "
               "one individual fill empty habitat quickly.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-h03",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the effect of one hundred generations of asexual "
                "reproduction with one hundred generations of sexual "
                "reproduction on the combinations of alleles in a "
                "population.",
        "options": [
            "Asexual reproduction keeps the parent's combination; sexual "
            "reproduction reshuffles it each generation",
            "Asexual reproduction creates brand new alleles in every "
            "generation, while sexual reproduction removes them again",
            "Both leave the combinations unchanged, because neither creates "
            "any new DNA",
            "Asexual reproduction halves the number of alleles present; "
            "sexual reproduction doubles it",
        ],
        "correct_index": 0,
        "why": "Only meiosis and fertilisation build new combinations from "
               "the alleles already present, so an asexual line keeps the "
               "parent's combination.",
    },
    {
        "id": "ks4-advantages-sexual-asexual-h04",
        "subtopic_slug": "advantages-sexual-asexual",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Sexual reproduction is always the better "
                "strategy, because variation is useful.' Evaluate this "
                "statement.",
        "options": [
            "It is correct — variation is an advantage in every possible "
            "environment",
            "It is wrong — variation is never useful, as new combinations "
            "are always harmful",
            "It is too strong — variation also gives poorly adapted "
            "offspring, and mates cost time and energy",
            "It is wrong — sexual reproduction produces no variation at all "
            "unless a mutation happens to occur",
        ],
        "correct_index": 2,
        "why": "Variation cuts both ways: it includes disadvantageous "
               "combinations, and sexual reproduction carries a real cost "
               "in time, energy and numbers of offspring.",
    },

    # ── dna-genome ──────────────────────────────────────────────────────
    {
        "id": "ks4-dna-genome-e01",
        "subtopic_slug": "dna-genome",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where in a human cell the chromosomes are found.",
        "options": [
            "In the cytoplasm, attached to the ribosomes",
            "In the cell membrane, spread across the surface",
            "In the mitochondria, where energy is released",
            "In the nucleus, as long coiled DNA molecules",
        ],
        "correct_index": 3,
        "why": "Chromosomes are the tightly coiled DNA molecules held inside "
               "the nucleus of the cell.",
    },
    {
        "id": "ks4-dna-genome-e02",
        "subtopic_slug": "dna-genome",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of pairs of chromosomes in a human body "
                "cell.",
        "options": [
            "46 pairs, making 92 chromosomes in total",
            "23 pairs, making 46 chromosomes in total",
            "23 pairs, making 23 chromosomes in total",
            "20 000 pairs, one pair for each gene",
        ],
        "correct_index": 1,
        "why": "Human body cells carry 46 chromosomes arranged as 23 pairs, "
               "with one of each pair inherited from each parent.",
    },
    {
        "id": "ks4-dna-genome-e03",
        "subtopic_slug": "dna-genome",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of molecule that a gene codes for.",
        "options": [
            "A carbohydrate, such as starch",
            "A lipid, such as a fat",
            "A protein, such as an enzyme",
            "A chromosome, such as chromosome 7",
        ],
        "correct_index": 2,
        "why": "The base sequence of a gene sets the order of amino acids, "
               "and therefore the protein, that the cell builds.",
    },
    {
        "id": "ks4-dna-genome-e04",
        "subtopic_slug": "dna-genome",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State approximately how many protein-coding genes were "
                "found in human DNA.",
        "options": [
            "About 20 000 genes",
            "About 46 genes",
            "About 3 billion genes",
            "About 250 genes",
        ],
        "correct_index": 0,
        "why": "Around 20 000 protein-coding genes were identified among "
               "roughly 3 billion base pairs of human DNA.",
    },
    {
        "id": "ks4-dna-genome-s01",
        "subtopic_slug": "dna-genome",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A length of one DNA strand contains 40 adenine bases. "
                "Determine the number of thymine bases directly opposite "
                "them on the other strand.",
        "options": [
            "20 thymine bases, because bases are shared between the strands",
            "40 thymine bases, because every adenine pairs with a thymine",
            "80 thymine bases, because each adenine pairs with two thymines",
            "It cannot be worked out without knowing the cytosine count",
        ],
        "correct_index": 1,
        "why": "Adenine only ever pairs with thymine, so each of the 40 "
               "adenines lies opposite exactly one thymine.",
    },
    {
        "id": "ks4-dna-genome-s02",
        "subtopic_slug": "dna-genome",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why changing a single base in a gene can change the "
                "protein that the gene codes for.",
        "options": [
            "Because a changed base breaks the chromosome into two pieces",
            "Because a changed base stops the gene being copied at all",
            "Because the base sequence sets the amino acid sequence, and so "
            "the protein",
            "Because each base becomes an amino acid in the finished protein",
        ],
        "correct_index": 2,
        "why": "The order of bases sets the order of amino acids, so "
               "altering a base can alter an amino acid and change the "
               "protein.",
    },
    {
        "id": "ks4-dna-genome-s03",
        "subtopic_slug": "dna-genome",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two people have different eye colours. Explain this "
                "difference using the word allele.",
        "options": [
            "They have different versions of the same gene at the same "
            "place on their chromosomes",
            "They have a different number of eye-colour genes on their "
            "chromosomes",
            "One of them has the eye-colour gene and the other does not "
            "have it",
            "They carry their eye-colour genes on completely different "
            "chromosomes from one another",
        ],
        "correct_index": 0,
        "why": "Alleles are different versions of the same gene, and which "
               "alleles a person carries decides the characteristic they "
               "show.",
    },
    {
        "id": "ks4-dna-genome-s04",
        "subtopic_slug": "dna-genome",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how knowing the sequence of the human genome has "
                "helped in the treatment of disease.",
        "options": [
            "Doctors can now remove a faulty gene from every cell in an "
            "adult patient",
            "A cure has been produced for every inherited disorder that was "
            "identified",
            "A patient's whole genome can be replaced with a healthy copy "
            "of it",
            "Genes linked to a disease can be identified and treatment "
            "matched to a patient",
        ],
        "correct_index": 3,
        "why": "Knowing which genes are linked to a disorder allows risk to "
               "be identified and medicines to be tailored to a patient's "
               "own genes.",
    },
    {
        "id": "ks4-dna-genome-h01",
        "subtopic_slug": "dna-genome",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Every cell in a person's body contains a "
                "different genome.' Explain why this is wrong.",
        "options": [
            "Only gametes contain a genome; body cells contain single genes "
            "instead",
            "Each cell contains a set of chromosomes chosen at random from "
            "the parents",
            "Body cells are all produced by mitosis, so each carries the "
            "same complete set",
            "The genome is stored in the blood and shared out to cells as "
            "they need it",
        ],
        "correct_index": 2,
        "why": "All body cells descend by mitosis from one zygote, so each "
               "holds the same complete genome.",
    },
    {
        "id": "ks4-dna-genome-h02",
        "subtopic_slug": "dna-genome",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forensic scientist compares DNA from a crime scene with "
                "DNA from several people. Explain why this can identify one "
                "individual.",
        "options": [
            "Every person's base sequence differs slightly, so a sample "
            "matches only one of them",
            "Every person has a different number of chromosomes, which can "
            "be counted in a sample",
            "Every person's DNA contains different bases, not just A, T, C "
            "and G",
            "Every person's DNA is a different shape, so the double helix "
            "can be recognised",
        ],
        "correct_index": 0,
        "why": "Apart from identical twins, no two people share the same "
               "base sequence, so a DNA profile is effectively unique.",
    },
    {
        "id": "ks4-dna-genome-h03",
        "subtopic_slug": "dna-genome",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two species are found to have very similar base sequences "
                "in many of their genes. Suggest what this indicates about "
                "the two species.",
        "options": [
            "They must live in the same habitat and eat the same food",
            "One of them must have evolved directly from the other very "
            "recently",
            "They must have exactly the same number of chromosomes as each "
            "other",
            "They are closely related and share a recent common ancestor",
        ],
        "correct_index": 3,
        "why": "The more of their base sequence two species share, the more "
               "recently they diverged from a common ancestor.",
    },
    {
        "id": "ks4-dna-genome-h04",
        "subtopic_slug": "dna-genome",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A length of double-stranded DNA contains 600 bases in "
                "total, of which 180 are cytosine. Determine the number of "
                "adenine bases it contains.",
        "options": [
            "60 adenine bases",
            "120 adenine bases",
            "180 adenine bases",
            "240 adenine bases",
        ],
        "correct_index": 1,
        "why": "Cytosine always pairs with guanine, so 180 of each makes "
               "360; the remaining 240 bases split equally into 120 adenine "
               "and 120 thymine.",
    },

    # ── dna-structure ───────────────────────────────────────────────────
    {
        "id": "ks4-dna-structure-e01",
        "subtopic_slug": "dna-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of bond that holds the two strands of a DNA "
                "molecule together.",
        "options": [
            "Ionic bonds between the sugar molecules",
            "Covalent bonds between the phosphate groups",
            "Hydrogen bonds between the paired bases",
            "Metallic bonds between the two strands",
        ],
        "correct_index": 2,
        "why": "Weak hydrogen bonds form between the paired bases, holding "
               "the strands together but still allowing them to separate.",
    },
    {
        "id": "ks4-dna-structure-e02",
        "subtopic_slug": "dna-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to the overall shape of a DNA "
                "molecule.",
        "options": [
            "A single spiral of nucleotides",
            "A branched chain of nucleotides",
            "A flat folded sheet of nucleotides",
            "A double helix of two strands",
        ],
        "correct_index": 3,
        "why": "Two nucleotide strands twist around one another, which is "
               "what gives DNA its double helix shape.",
    },
    {
        "id": "ks4-dna-structure-e03",
        "subtopic_slug": "dna-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the molecule that carries a copy of a gene out of the "
                "nucleus to a ribosome.",
        "options": [
            "mRNA, made by copying the gene",
            "DNA, the original strand itself",
            "An amino acid from the cytoplasm",
            "A whole chromosome from the nucleus",
        ],
        "correct_index": 0,
        "why": "The gene is transcribed into messenger RNA, which leaves the "
               "nucleus and is read at a ribosome.",
    },
    {
        "id": "ks4-dna-structure-e04",
        "subtopic_slug": "dna-structure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the hydrogen bonds when DNA "
                "replication begins.",
        "options": [
            "They become stronger, holding the two strands more tightly",
            "They break, allowing the two strands to separate",
            "They join the two newly made molecules together",
            "They change into covalent bonds along the backbone",
        ],
        "correct_index": 1,
        "why": "The hydrogen bonds between the bases break so the helix can "
               "unwind and each strand can act as a template.",
    },
    {
        "id": "ks4-dna-structure-s01",
        "subtopic_slug": "dna-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why free nucleotides can only join a template "
                "strand in one particular order.",
        "options": [
            "Because each base can only pair with its complementary base — "
            "A with T and G with C",
            "Because the free nucleotides arrive in exactly the order they "
            "are needed",
            "Because the template strand chooses which free nucleotides it "
            "will accept",
            "Because all four bases are the same shape and so fit into any "
            "position",
        ],
        "correct_index": 0,
        "why": "Complementary base pairing means only one base will bond "
               "opposite each base of the template, which is what makes the "
               "copy accurate.",
    },
    {
        "id": "ks4-dna-structure-s02",
        "subtopic_slug": "dna-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens during translation.",
        "options": [
            "The DNA double helix unwinds and each of its strands is copied",
            "The base sequence of mRNA is read at a ribosome and amino acids "
            "are joined in that order",
            "A gene is copied into a molecule of mRNA inside the nucleus",
            "Two separate strands of DNA are joined together to form a "
            "chromosome",
        ],
        "correct_index": 1,
        "why": "Translation is the stage at the ribosome where the mRNA "
               "sequence is used to assemble amino acids into a protein "
               "chain.",
    },
    {
        "id": "ks4-dna-structure-s03",
        "subtopic_slug": "dna-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the function of a protein depends on its shape.",
        "options": [
            "Because larger proteins always work faster than smaller ones do",
            "Because the shape decides how many amino acids the protein "
            "contains",
            "Because a protein can only work while folded into a straight "
            "chain",
            "Because the shape decides what the protein can bind to, and so "
            "what it can do",
        ],
        "correct_index": 3,
        "why": "The order of amino acids sets how the chain folds, and a "
               "protein such as an enzyme only works if its shape fits what "
               "it acts on.",
    },
    {
        "id": "ks4-dna-structure-s04",
        "subtopic_slug": "dna-structure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A mutation changes one base in a gene. Suggest why this may "
                "have no effect at all on the organism.",
        "options": [
            "All mutations are repaired before the cell is able to divide "
            "again",
            "One base is too small a change to be copied into a molecule of "
            "mRNA",
            "The protein produced may be unchanged, or may still work "
            "normally",
            "A single base is not part of any gene, so it is never read at "
            "all",
        ],
        "correct_index": 2,
        "why": "Many base changes leave the protein's shape and function "
               "unaltered, so the organism is unaffected.",
    },
    {
        "id": "ks4-dna-structure-h01",
        "subtopic_slug": "dna-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A coding section of a gene is 24 bases long. Determine the "
                "number of amino acids it codes for.",
        "options": [
            "24 amino acids",
            "8 amino acids",
            "12 amino acids",
            "72 amino acids",
        ],
        "correct_index": 1,
        "why": "Each amino acid is coded for by three bases, so 24 ÷ 3 = 8 "
               "amino acids.",
    },
    {
        "id": "ks4-dna-structure-h02",
        "subtopic_slug": "dna-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the roles of the template strand and of the free "
                "nucleotides during DNA replication.",
        "options": [
            "Both are copied, so that two new strands of identical bases are "
            "made",
            "The free nucleotides act as the template and the old strand is "
            "then discarded",
            "The template sets the order to follow; the free nucleotides "
            "are the units built into the new strand",
            "The template supplies the sugar and the phosphate, while the "
            "free nucleotides supply only the bases",
        ],
        "correct_index": 2,
        "why": "The old strand's base sequence dictates the order, and the "
               "new strand is assembled from free nucleotides pairing with "
               "it.",
    },
    {
        "id": "ks4-dna-structure-h03",
        "subtopic_slug": "dna-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a wrong base built into a strand during "
                "replication may be passed on to every cell that follows.",
        "options": [
            "Because errors always occur at the same place on the same "
            "chromosome",
            "Because the error changes the sugar-phosphate backbone "
            "permanently",
            "Because errors are only made in cells that are about to divide "
            "again",
            "Because the altered strand becomes the template for every "
            "later copy",
        ],
        "correct_index": 3,
        "why": "Once a wrong base is built in, that strand is the template "
               "for all later replications, so the change is copied "
               "onwards.",
    },
    {
        "id": "ks4-dna-structure-h04",
        "subtopic_slug": "dna-structure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why DNA must be replicated before a cell divides, "
                "but not before a protein is made.",
        "options": [
            "Replication makes a whole second copy for a new cell; making a "
            "protein only reads the gene",
            "Replication destroys the original DNA molecule, so a completely "
            "new copy must always be made first",
            "Proteins are built directly out of DNA, so the DNA is used up "
            "each time one is made",
            "Cell division halves the amount of DNA, so extra copies have "
            "to be made in advance",
        ],
        "correct_index": 0,
        "why": "Division needs a whole second copy of the DNA, whereas "
               "transcription only reads the gene and leaves the molecule "
               "unchanged.",
    },

    # ── genetic-inheritance ─────────────────────────────────────────────
    {
        "id": "ks4-genetic-inheritance-e01",
        "subtopic_slug": "genetic-inheritance",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In pea plants, tall (T) is dominant to dwarf (t). State the "
                "phenotype of a plant with the genotype Tt.",
        "options": [
            "Dwarf, because a recessive allele is present",
            "Tall, because one dominant allele is enough",
            "Halfway in height between tall and dwarf",
            "It cannot be decided from the genotype",
        ],
        "correct_index": 1,
        "why": "A dominant allele is expressed whenever at least one copy is "
               "present, so a Tt plant is tall.",
    },
    {
        "id": "ks4-genetic-inheritance-e02",
        "subtopic_slug": "genetic-inheritance",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gene has the alleles R and r. State the genotype of an "
                "organism that is homozygous recessive for this gene.",
        "options": [
            "rr — two recessive alleles",
            "Rr — one allele of each kind",
            "RR — two dominant alleles",
            "Either Rr or rr, depending on the phenotype",
        ],
        "correct_index": 0,
        "why": "Homozygous means both alleles are the same, and recessive "
               "means both are the lowercase allele.",
    },
    {
        "id": "ks4-genetic-inheritance-e03",
        "subtopic_slug": "genetic-inheritance",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In mice, black fur (B) is dominant to brown fur (b). State "
                "all of the genotypes that give a black mouse.",
        "options": [
            "bb only, because brown is recessive",
            "Bb only, because heterozygous mice are black",
            "BB only, because two dominant alleles are needed",
            "Both BB and Bb, because one B allele is enough",
        ],
        "correct_index": 3,
        "why": "One dominant allele is enough for the dominant phenotype, so "
               "BB and Bb mice are both black.",
    },
    {
        "id": "ks4-genetic-inheritance-e04",
        "subtopic_slug": "genetic-inheritance",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dwarf pea plant (tt) is crossed with another dwarf pea "
                "plant (tt). Predict the offspring.",
        "options": [
            "All tall, because two recessive alleles give the dominant form",
            "Half of them tall and half of them dwarf",
            "All dwarf, because the only allele either parent can pass on "
            "is t",
            "Three dwarf plants for every one tall plant",
        ],
        "correct_index": 2,
        "why": "Neither parent carries the dominant allele, so every "
               "offspring must be tt and therefore dwarf.",
    },
    {
        "id": "ks4-genetic-inheritance-s01",
        "subtopic_slug": "genetic-inheritance",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In mice, black fur (B) is dominant to brown fur (b). A "
                "heterozygous black mouse (Bb) is crossed with a brown mouse "
                "(bb). Predict the ratio of black to brown offspring.",
        "options": [
            "3 black : 1 brown",
            "1 black : 3 brown",
            "4 black : 0 brown",
            "1 black : 1 brown",
        ],
        "correct_index": 3,
        "why": "The Bb parent passes B or b equally often and the bb parent "
               "always passes b, so half the offspring are Bb and half are "
               "bb.",
    },
    {
        "id": "ks4-genetic-inheritance-s02",
        "subtopic_slug": "genetic-inheritance",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pea plant that is homozygous tall (TT) is crossed with a "
                "dwarf plant (tt). Determine the genotypes of the "
                "offspring.",
        "options": [
            "Half of them TT and half of them tt",
            "One quarter TT, one half Tt and one quarter tt",
            "All of them Tt, one allele from each parent",
            "All of them TT, exactly like the tall parent",
        ],
        "correct_index": 2,
        "why": "Every gamete from the TT parent carries T and every gamete "
               "from the tt parent carries t, so all offspring must be Tt.",
    },
    {
        "id": "ks4-genetic-inheritance-s03",
        "subtopic_slug": "genetic-inheritance",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two heterozygous tall pea plants (Tt) are crossed. "
                "Determine the ratio of the offspring genotypes.",
        "options": [
            "3 TT : 0 Tt : 1 tt",
            "1 TT : 2 Tt : 1 tt",
            "1 TT : 1 Tt : 1 tt",
            "2 TT : 1 Tt : 1 tt",
        ],
        "correct_index": 1,
        "why": "The four equally likely combinations are TT, Tt, Tt and tt, "
               "which is one homozygous dominant to two heterozygous to one "
               "homozygous recessive.",
    },
    {
        "id": "ks4-genetic-inheritance-s04",
        "subtopic_slug": "genetic-inheritance",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a breed of chicken, feathered legs (F) are dominant to "
                "bare legs (f). Two feather-legged birds are bred together "
                "and some of their chicks have bare legs. Determine the "
                "genotypes of the two parent birds.",
        "options": [
            "Both parents are Ff — one allele of each kind",
            "Both parents are FF — two dominant alleles",
            "One parent is Ff and the other is FF",
            "Neither parent carries f, so the chicks' allele arose by "
            "mutation",
        ],
        "correct_index": 0,
        "why": "A bare-legged chick must be ff, so each parent passed on an "
               "f allele while still showing feathered legs — both must be "
               "Ff.",
    },
    {
        "id": "ks4-genetic-inheritance-h01",
        "subtopic_slug": "genetic-inheritance",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In guinea pigs, black fur (B) is dominant to brown (b). A "
                "black guinea pig of unknown genotype is crossed with a "
                "brown one and produces eight black offspring and no brown "
                "ones. Deduce the most likely genotype of the black parent.",
        "options": [
            "BB, because a Bb parent would be expected to give about half "
            "brown offspring",
            "Bb, because half the offspring would be black and half would "
            "be brown",
            "bb, because brown parents are able to produce black offspring",
            "It cannot be decided, because BB and Bb both give only black "
            "offspring",
        ],
        "correct_index": 0,
        "why": "A Bb parent crossed with bb would give roughly half brown "
               "offspring, so eight black and no brown points to BB.",
    },
    {
        "id": "ks4-genetic-inheritance-h02",
        "subtopic_slug": "genetic-inheritance",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a flower, red (R) is dominant to white (r). A grower "
                "crosses a heterozygous red plant with a white plant and "
                "raises 60 seedlings. Estimate how many are expected to be "
                "white.",
        "options": [
            "0 seedlings",
            "15 seedlings",
            "45 seedlings",
            "30 seedlings",
        ],
        "correct_index": 3,
        "why": "Rr crossed with rr gives half Rr (red) and half rr (white), "
               "so about half of 60 — that is 30 — are expected to be "
               "white.",
    },
    {
        "id": "ks4-genetic-inheritance-h03",
        "subtopic_slug": "genetic-inheritance",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two organisms showing the same characteristic "
                "may not have the same genotype for it.",
        "options": [
            "Because the environment an organism grows in can change its "
            "alleles",
            "Because a phenotype is decided by only one of the two alleles "
            "present",
            "Because a dominant characteristic is shown by both the "
            "homozygous and the heterozygous genotype",
            "Because a recessive characteristic can be shown by two "
            "different genotypes",
        ],
        "correct_index": 2,
        "why": "One dominant allele is enough for the dominant phenotype, so "
               "BB and Bb organisms look the same although their genotypes "
               "differ.",
    },
    {
        "id": "ks4-genetic-inheritance-h04",
        "subtopic_slug": "genetic-inheritance",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'A dominant allele is always the more "
                "common allele in a population.' Evaluate this statement.",
        "options": [
            "Correct — a dominant allele is passed on more often than a "
            "recessive one",
            "Wrong — dominance decides whether an allele is expressed, not "
            "how common it is",
            "Correct — a recessive allele gradually disappears from a "
            "population over time",
            "Wrong — a recessive allele is always the more common of the "
            "two in a population",
        ],
        "correct_index": 1,
        "why": "Dominance describes how an allele behaves when paired with "
               "another one, and says nothing about how many individuals "
               "carry it.",
    },

    # ── inherited-disorders ─────────────────────────────────────────────
    {
        "id": "ks4-inherited-disorders-e01",
        "subtopic_slug": "inherited-disorders",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The normal allele is F and the faulty cystic fibrosis "
                "allele is f. State the genotype of a person who has cystic "
                "fibrosis.",
        "options": [
            "ff — two faulty alleles",
            "Ff — one faulty allele only",
            "FF — two normal alleles",
            "Either Ff or ff — one faulty allele is enough",
        ],
        "correct_index": 0,
        "why": "Cystic fibrosis is recessive, so both alleles must be the "
               "faulty f allele for the condition to show.",
    },
    {
        "id": "ks4-inherited-disorders-e02",
        "subtopic_slug": "inherited-disorders",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main effect of polydactyly on a person who has "
                "it.",
        "options": [
            "Thick sticky mucus builds up in the lungs",
            "The ducts leading from the pancreas become blocked",
            "Repeated chest infections damage the airways",
            "One or more extra fingers or toes develop",
        ],
        "correct_index": 3,
        "why": "Polydactyly is the development of extra digits, and it is "
               "not life-threatening.",
    },
    {
        "id": "ks4-inherited-disorders-e03",
        "subtopic_slug": "inherited-disorders",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one treatment used to help a person who has cystic "
                "fibrosis.",
        "options": [
            "A single course of antibiotics that cures the condition",
            "Surgery to remove the faulty allele from the lung cells",
            "Physiotherapy to loosen the mucus in the airways",
            "A change of diet that removes the faulty allele",
        ],
        "correct_index": 2,
        "why": "There is no cure, so treatment manages the symptoms — "
               "physiotherapy loosens the mucus so that it can be cleared.",
    },
    {
        "id": "ks4-inherited-disorders-e04",
        "subtopic_slug": "inherited-disorders",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State approximately how many people in the UK carry the "
                "cystic fibrosis allele.",
        "options": [
            "About 1 in 4 people",
            "About 1 in 25 people",
            "About 1 in 1000 people",
            "About 1 in 2 people",
        ],
        "correct_index": 1,
        "why": "Roughly one person in 25 is a healthy carrier, which is why "
               "cystic fibrosis is the most common serious inherited "
               "disorder in the UK.",
    },
    {
        "id": "ks4-inherited-disorders-s01",
        "subtopic_slug": "inherited-disorders",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person with polydactyly has the genotype Dd. Their "
                "partner has the genotype dd. Predict the percentage of "
                "their children expected to have polydactyly.",
        "options": [
            "0%",
            "25%",
            "50%",
            "100%",
        ],
        "correct_index": 2,
        "why": "The affected parent passes D to half of their children, and "
               "one copy of D is enough to cause the condition.",
    },
    {
        "id": "ks4-inherited-disorders-s02",
        "subtopic_slug": "inherited-disorders",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cystic fibrosis affects digestion as well as "
                "breathing.",
        "options": [
            "Thick mucus blocks the ducts from the pancreas, so digestive "
            "enzymes cannot reach the gut",
            "The faulty allele stops the stomach from producing any acid at "
            "all",
            "Mucus made in the lungs is swallowed and then coats the lining "
            "of the intestine",
            "The faulty allele prevents the liver from being able to "
            "produce bile",
        ],
        "correct_index": 0,
        "why": "The same faulty protein makes mucus thick and sticky "
               "wherever it is produced, and in the pancreas that blocks the "
               "ducts carrying enzymes to the gut.",
    },
    {
        "id": "ks4-inherited-disorders-s03",
        "subtopic_slug": "inherited-disorders",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe one way of finding out, before a baby is born, "
                "whether it has an inherited disorder.",
        "options": [
            "A blood spot taken from the baby's heel shortly after the birth",
            "Amniocentesis — testing cells taken from a sample of amniotic "
            "fluid",
            "Testing both parents' DNA to see which alleles their child "
            "received",
            "Measuring the growth of the foetus during a routine ultrasound "
            "scan",
        ],
        "correct_index": 1,
        "why": "Amniocentesis, like chorionic villus sampling, tests cells "
               "from the pregnancy itself, so the foetus's own alleles can "
               "be examined.",
    },
    {
        "id": "ks4-inherited-disorders-s04",
        "subtopic_slug": "inherited-disorders",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two parents both have polydactyly and both have the "
                "genotype Dd. Calculate the percentage of their children "
                "expected to be unaffected.",
        "options": [
            "0%",
            "50%",
            "75%",
            "25%",
        ],
        "correct_index": 3,
        "why": "Only the dd combination is unaffected, and it is one of the "
               "four equally likely outcomes.",
    },
    {
        "id": "ks4-inherited-disorders-h01",
        "subtopic_slug": "inherited-disorders",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A child is born with polydactyly, although their parents "
                "and all four grandparents are unaffected. Suggest an "
                "explanation.",
        "options": [
            "The allele skipped two generations, because it is recessive in "
            "some families",
            "Both parents must have been unaffected carriers of the "
            "dominant allele",
            "The child inherited two normal alleles, which combined to give "
            "the condition",
            "A new mutation produced the dominant allele in one of the "
            "parents' gametes",
        ],
        "correct_index": 3,
        "why": "A dominant condition cannot be hidden in a carrier, so an "
               "affected child of unaffected parents points to a new "
               "mutation.",
    },
    {
        "id": "ks4-inherited-disorders-h02",
        "subtopic_slug": "inherited-disorders",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woman who has cystic fibrosis (ff) has children with a "
                "man who is a carrier (Ff). Predict the proportion of their "
                "children expected to have cystic fibrosis.",
        "options": [
            "None of their children",
            "About half of their children",
            "About one quarter of their children",
            "All of their children",
        ],
        "correct_index": 1,
        "why": "The mother can only pass on f, and the father passes on f "
               "half of the time, so about half the children are ff.",
    },
    {
        "id": "ks4-inherited-disorders-h03",
        "subtopic_slug": "inherited-disorders",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate one argument against routine genetic testing of "
                "adults for inherited disorders.",
        "options": [
            "The results are private information that insurers or employers "
            "could use against a person",
            "A genetic test changes a person's alleles, which may cause new "
            "disorders to appear",
            "A negative result would mean that a person could never develop "
            "any disease",
            "Testing removes the faulty allele from a population within a "
            "single generation",
        ],
        "correct_index": 0,
        "why": "Genetic results reveal information a person cannot change, "
               "which raises real concerns about privacy and "
               "discrimination.",
    },
    {
        "id": "ks4-inherited-disorders-h04",
        "subtopic_slug": "inherited-disorders",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a couple with cystic fibrosis in their family "
                "might choose genetic testing before starting a family.",
        "options": [
            "Testing would remove the faulty allele from their gametes "
            "before conception",
            "Testing would guarantee that any child they had would be "
            "unaffected",
            "Testing would show whether both are carriers, so the risk to a "
            "child can be explained",
            "Testing would show whether their child has already developed "
            "the condition",
        ],
        "correct_index": 2,
        "why": "Pre-conception testing identifies carriers, which is what "
               "allows the risk for each pregnancy to be worked out and "
               "explained.",
    },

    # ── sex-determination ───────────────────────────────────────────────
    {
        "id": "ks4-sex-determination-e01",
        "subtopic_slug": "sex-determination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the 22 pairs of human chromosomes that are not the sex "
                "chromosomes.",
        "options": [
            "Gametes",
            "Alleles",
            "Homologues",
            "Autosomes",
        ],
        "correct_index": 3,
        "why": "The 22 pairs that are the same in both sexes are the "
               "autosomes; only the 23rd pair determines sex.",
    },
    {
        "id": "ks4-sex-determination-e02",
        "subtopic_slug": "sex-determination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of the two human sex chromosomes is smaller and "
                "carries fewer genes.",
        "options": [
            "The X chromosome, but only in males",
            "The X chromosome, in both sexes",
            "The Y chromosome",
            "Neither — they are the same size",
        ],
        "correct_index": 2,
        "why": "The Y chromosome is much smaller than the X chromosome and "
               "carries far fewer genes.",
    },
    {
        "id": "ks4-sex-determination-e03",
        "subtopic_slug": "sex-determination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gene carried on the Y chromosome that triggers the "
                "development of testes.",
        "options": [
            "The SRY gene",
            "The XY gene",
            "The BRCA1 gene",
            "The CFTR gene",
        ],
        "correct_index": 0,
        "why": "The SRY gene on the Y chromosome switches on male "
               "development, including the formation of the testes.",
    },
    {
        "id": "ks4-sex-determination-e04",
        "subtopic_slug": "sex-determination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the point at which the sex of a human offspring is "
                "decided.",
        "options": [
            "During the first weeks of pregnancy, as the organs form",
            "At fertilisation, when a sperm fuses with the egg",
            "At birth, when the chromosomes finish pairing up",
            "During meiosis in the mother, when the egg is made",
        ],
        "correct_index": 1,
        "why": "The egg always carries an X, so sex is fixed the moment an "
               "X-bearing or Y-bearing sperm fuses with it.",
    },
    {
        "id": "ks4-sex-determination-s01",
        "subtopic_slug": "sex-determination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why approximately half of all human babies born are "
                "male.",
        "options": [
            "Half of all eggs carry a Y chromosome and half carry an X "
            "chromosome",
            "About half of all sperm carry a Y chromosome and half carry an "
            "X chromosome",
            "Half of all fertilised eggs lose their Y chromosome as they "
            "develop",
            "Parents produce male and female offspring in turn, so the "
            "numbers balance",
        ],
        "correct_index": 1,
        "why": "Meiosis puts an X into half the sperm and a Y into the other "
               "half, so each fertilisation is an even chance.",
    },
    {
        "id": "ks4-sex-determination-s02",
        "subtopic_slug": "sex-determination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gamete is found to contain a Y chromosome. Deduce which "
                "parent produced it and the sex of any child formed from it.",
        "options": [
            "The mother produced it, and the child would be female",
            "The mother produced it, and the child would be male",
            "The father produced it, and the child would be female",
            "The father produced it, and the child would be male",
        ],
        "correct_index": 3,
        "why": "Only males have a Y chromosome to pass on, and a Y-bearing "
               "sperm gives an XY zygote, which develops as male.",
    },
    {
        "id": "ks4-sex-determination-s03",
        "subtopic_slug": "sex-determination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the sex ratio in a large human population is "
                "close to 50:50 but not exactly 50:50.",
        "options": [
            "Because slightly more Y-bearing sperm are made than X-bearing "
            "sperm",
            "Because the sex of a child is decided after birth rather than "
            "at fertilisation",
            "Because each fertilisation is a random event, so the numbers "
            "only average out",
            "Because a small number of embryos change sex as they develop",
        ],
        "correct_index": 2,
        "why": "Sex determination is a matter of chance at each "
               "fertilisation, and chance gives an approximate rather than "
               "an exact split.",
    },
    {
        "id": "ks4-sex-determination-s04",
        "subtopic_slug": "sex-determination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why all 22 pairs of autosomes are the same in males "
                "and in females.",
        "options": [
            "Because only the 23rd pair carries the genes that determine "
            "sex",
            "Because the autosomes are inherited from the mother only",
            "Because the autosomes do not carry any genes at all",
            "Because autosomes are copied by mitosis and sex chromosomes by "
            "meiosis",
        ],
        "correct_index": 0,
        "why": "Sex is determined by the 23rd pair alone, so the other 22 "
               "pairs are the same set in both sexes.",
    },
    {
        "id": "ks4-sex-determination-h01",
        "subtopic_slug": "sex-determination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In some reptiles, the temperature of the nest decides the "
                "sex of the young. Compare this with sex determination in "
                "humans.",
        "options": [
            "Both are decided by the environment during development",
            "Both are decided by which of the eggs is fertilised first",
            "In humans it is decided by chromosomes at fertilisation; in "
            "these reptiles by the environment afterwards",
            "In humans it is decided by the temperature of the womb, but "
            "only during the first few weeks after conception",
        ],
        "correct_index": 2,
        "why": "Human sex is fixed by the sex chromosomes at fertilisation, "
               "whereas in these reptiles an environmental factor decides it "
               "after the egg is laid.",
    },
    {
        "id": "ks4-sex-determination-h02",
        "subtopic_slug": "sex-determination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher separates a sample of sperm so that 90% of "
                "them carry an X chromosome. Predict the effect on the sex "
                "ratio of offspring produced using that sample.",
        "options": [
            "About 90% would be female, because an X-bearing sperm gives XX",
            "About 90% would be male, because the extra X chromosomes give "
            "XY",
            "The ratio would stay at 50:50, because the egg decides the sex",
            "About 10% would be female, because Y-bearing sperm are more "
            "successful",
        ],
        "correct_index": 0,
        "why": "Each X-bearing sperm gives an XX zygote, so raising the "
               "proportion of X sperm raises the proportion of female "
               "offspring.",
    },
    {
        "id": "ks4-sex-determination-h03",
        "subtopic_slug": "sex-determination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In birds the female has two different sex chromosomes (ZW) "
                "and the male has two of the same kind (ZZ). Deduce which "
                "parent decides the sex of a chick.",
        "options": [
            "The male, because the male parent decides the sex in every "
            "species of animal",
            "The female, because only her gametes differ — half carry Z and "
            "half carry W",
            "Neither, because the sex of a chick is decided by the "
            "temperature of the nest",
            "Both equally, because each parent passes on one of the two sex "
            "chromosomes",
        ],
        "correct_index": 1,
        "why": "Sex is decided by whichever parent makes two kinds of "
               "gamete: every sperm here carries Z, so it is the egg, "
               "carrying Z or W, that settles it.",
    },
    {
        "id": "ks4-sex-determination-h04",
        "subtopic_slug": "sex-determination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the sex chromosomes are the only pair in a "
                "human body cell whose two members may not match each other.",
        "options": [
            "Because one of the pair comes from the father and the other "
            "from the mother",
            "Because the sex chromosomes are not copied before the cell "
            "divides",
            "Because the sex chromosomes are not really a matching pair at "
            "all",
            "Because a male inherits an X from his mother and a differently "
            "shaped Y from his father",
        ],
        "correct_index": 3,
        "why": "Every other pair is two chromosomes of the same type, but in "
               "a male the 23rd pair is one X and one much smaller Y.",
    },

    # ── variation ───────────────────────────────────────────────────────
    {
        "id": "ks4-variation-e01",
        "subtopic_slug": "variation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by variation.",
        "options": [
            "The changes an individual goes through during the course of "
            "its own lifetime",
            "The differences in characteristics between individuals of the "
            "same species",
            "The differences between one species and another species",
            "The number of different species living in one habitat",
        ],
        "correct_index": 1,
        "why": "Variation is the range of differences in characteristics "
               "found between members of the same species.",
    },
    {
        "id": "ks4-variation-e02",
        "subtopic_slug": "variation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give an example of continuous variation in humans.",
        "options": [
            "Blood group",
            "Tongue-rolling ability",
            "Body mass",
            "Ability to taste PTC",
        ],
        "correct_index": 2,
        "why": "Body mass can take any value across a range, with no "
               "separate categories, which is what makes it continuous.",
    },
    {
        "id": "ks4-variation-e03",
        "subtopic_slug": "variation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one factor that increases the rate at which mutations "
                "occur.",
        "options": [
            "A diet that is low in protein and in vitamins",
            "Regular vigorous exercise",
            "A change in the environment that would make a new feature "
            "useful",
            "Ultraviolet radiation from the Sun",
        ],
        "correct_index": 3,
        "why": "Ultraviolet radiation is a mutagen — it damages DNA and "
               "raises the chance of the base sequence being changed.",
    },
    {
        "id": "ks4-variation-e04",
        "subtopic_slug": "variation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect that most mutations have on an organism.",
        "options": [
            "No detectable effect at all",
            "A harmful effect on a protein",
            "A beneficial effect on a protein",
            "The death of the organism",
        ],
        "correct_index": 0,
        "why": "The great majority of mutations are neutral and change "
               "nothing that can be detected in the organism.",
    },
    {
        "id": "ks4-variation-s01",
        "subtopic_slug": "variation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identical twins are brought up in different countries and "
                "come to differ in body mass. Explain this difference.",
        "options": [
            "They have the same alleles, so the difference must come from "
            "diet and exercise",
            "Their alleles have changed to suit the country each of them "
            "lives in",
            "Identical twins do not in fact share the same alleles for body "
            "mass",
            "Body mass is entirely genetic, so one of the twins must have "
            "mutated",
        ],
        "correct_index": 0,
        "why": "Twins share a genotype, so any difference between them has "
               "to come from the environment they have experienced.",
    },
    {
        "id": "ks4-variation-s02",
        "subtopic_slug": "variation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the three sources of genetic variation in a population "
                "that reproduces sexually.",
        "options": [
            "Diet, exercise and climate",
            "Mutation, the shuffling of chromosomes in meiosis, and "
            "fertilisation",
            "Mitosis, cloning and asexual reproduction",
            "Selective breeding, cloning and genetic engineering carried "
            "out by humans",
        ],
        "correct_index": 1,
        "why": "New alleles come from mutation, and new combinations of them "
               "come from meiosis and from two parents' gametes joining.",
    },
    {
        "id": "ks4-variation-s03",
        "subtopic_slug": "variation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One plant in a field of a single variety produces much "
                "larger fruit than the rest. Suggest two possible causes.",
        "options": [
            "Selective breeding, or that plant belonging to a different "
            "species",
            "That plant being a clone, or that plant reproducing asexually",
            "A mutation in that plant, or better growing conditions in that "
            "part of the field",
            "Meiosis in that plant, or that plant being older than all the "
            "others",
        ],
        "correct_index": 2,
        "why": "A characteristic can differ because of a genetic change or "
               "because of the conditions that individual experienced.",
    },
    {
        "id": "ks4-variation-s04",
        "subtopic_slug": "variation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a learned skill such as playing the piano "
                "cannot be inherited.",
        "options": [
            "Because the skill is stored in the brain, which is not passed "
            "on in an egg",
            "Because the skill would be lost in meiosis when the "
            "chromosomes are halved",
            "Because only characteristics controlled by dominant alleles "
            "can be inherited",
            "Because learning does not change the base sequence of the DNA "
            "in the gametes",
        ],
        "correct_index": 3,
        "why": "Only changes to the DNA carried in the gametes are passed "
               "on, and practising a skill does not alter that sequence.",
    },
    {
        "id": "ks4-variation-h01",
        "subtopic_slug": "variation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a mutation can only be described as beneficial "
                "in relation to a particular environment.",
        "options": [
            "Because beneficial mutations only ever occur at times when the "
            "environment is already changing",
            "Because every mutation is beneficial in some environment "
            "somewhere",
            "Because the environment decides which mutations are going to "
            "occur",
            "Because an allele that helps survival in one environment may "
            "be a disadvantage in another",
        ],
        "correct_index": 3,
        "why": "Whether a change to a protein helps or harms depends "
               "entirely on the conditions the organism has to survive in.",
    },
    {
        "id": "ks4-variation-h02",
        "subtopic_slug": "variation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why variation caused by the environment cannot "
                "drive evolution.",
        "options": [
            "Because a change to an individual's body does not change the "
            "DNA passed to its offspring",
            "Because variation caused by the environment is always far too "
            "small for selection to notice",
            "Because natural selection only acts on characteristics that "
            "never vary",
            "Because the environment changes too quickly for selection to "
            "act on it",
        ],
        "correct_index": 0,
        "why": "Evolution needs heritable differences, and only genetic "
               "variation is passed on to the next generation.",
    },
    {
        "id": "ks4-variation-h03",
        "subtopic_slug": "variation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Mutations are dangerous, so a species "
                "would be better off without them.' Evaluate this "
                "statement.",
        "options": [
            "Correct — every mutation damages a protein and reduces the "
            "chance of survival",
            "Too strong — most mutations are neutral, and rare beneficial "
            "ones give the only new alleles",
            "Correct — a species with no mutations at all could still evolve "
            "through meiosis and fertilisation",
            "Wrong — mutations are always beneficial and are needed for "
            "every adaptation",
        ],
        "correct_index": 1,
        "why": "Without mutation there would be no new alleles at all, so "
               "natural selection would eventually have nothing new to act "
               "on.",
    },
    {
        "id": "ks4-variation-h04",
        "subtopic_slug": "variation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two brothers have noticeably different skin colours after "
                "one spends a summer working outdoors. Explain how both "
                "genes and the environment contribute to skin colour.",
        "options": [
            "Their genes decide the tan and the Sun decides their base skin "
            "colour",
            "The Sun has changed the alleles for skin colour in the brother "
            "who worked outdoors",
            "Their inherited alleles set their base skin colour, and "
            "exposure to UV darkens it further",
            "Skin colour is entirely environmental, so their alleles make "
            "no difference at all",
        ],
        "correct_index": 2,
        "why": "Skin colour is a characteristic where inherited alleles set "
               "a starting point that environmental exposure then modifies.",
    },

    # ── evolution-natural-selection ─────────────────────────────────────
    {
        "id": "ks4-evolution-natural-selection-e01",
        "subtopic_slug": "evolution-natural-selection",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by evolution.",
        "options": [
            "A change in an individual organism during its own lifetime",
            "The appearance of a new characteristic in a single generation",
            "A change in the inherited characteristics of a population over "
            "many generations",
            "The movement of a whole species into a new and unfamiliar "
            "habitat somewhere else",
        ],
        "correct_index": 2,
        "why": "Evolution is a change in the inherited characteristics of a "
               "population, built up across many generations.",
    },
    {
        "id": "ks4-evolution-natural-selection-e02",
        "subtopic_slug": "evolution-natural-selection",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the ship on which Darwin made the voyage that led to "
                "his observations of wildlife.",
        "options": [
            "HMS Endeavour",
            "HMS Beagle",
            "HMS Victory",
            "HMS Discovery",
        ],
        "correct_index": 1,
        "why": "Darwin's observations during the voyage of HMS Beagle "
               "(1831–1836) formed the basis of his theory.",
    },
    {
        "id": "ks4-evolution-natural-selection-e03",
        "subtopic_slug": "evolution-natural-selection",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who independently developed a theory of "
                "natural selection at about the same time as Darwin.",
        "options": [
            "Alfred Russel Wallace",
            "Gregor Mendel",
            "Francis Crick",
            "Rosalind Elsie Franklin",
        ],
        "correct_index": 0,
        "why": "Wallace reached the same idea independently and sent it to "
               "Darwin in 1858, which prompted Darwin to publish.",
    },
    {
        "id": "ks4-evolution-natural-selection-e04",
        "subtopic_slug": "evolution-natural-selection",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what natural selection acts upon within a population.",
        "options": [
            "The characteristics an organism gains during its own lifetime",
            "The needs of each individual organism as conditions change",
            "The number of offspring each individual chooses to produce",
            "The variation that already exists between individuals",
        ],
        "correct_index": 3,
        "why": "Selection can only favour differences that are already "
               "present — it does not create new ones to order.",
    },
    {
        "id": "ks4-evolution-natural-selection-s01",
        "subtopic_slug": "evolution-natural-selection",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A faster predator arrives in an area where rabbits live. "
                "Explain how the rabbit population may change over many "
                "generations.",
        "options": [
            "Each rabbit runs faster as it gets used to the predator, and "
            "passes this on",
            "The rabbits choose to produce faster offspring so as to escape "
            "the predator",
            "A mutation for greater speed appears because the rabbits now "
            "need one",
            "Faster rabbits survive and reproduce more, so alleles for "
            "speed become more common",
        ],
        "correct_index": 3,
        "why": "The predator does not create fast rabbits; it removes slow "
               "ones, so the survivors' alleles increase in the population.",
    },
    {
        "id": "ks4-evolution-natural-selection-s02",
        "subtopic_slug": "evolution-natural-selection",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is wrong to say that an individual organism "
                "evolves.",
        "options": [
            "Evolution is a change in the alleles present in a population, "
            "not a change in one individual",
            "Individuals do evolve, but only if they survive long enough to "
            "reproduce more than once themselves",
            "Evolution happens only in species that reproduce asexually as "
            "clones",
            "An individual can evolve, but only its body changes and not "
            "its alleles",
        ],
        "correct_index": 0,
        "why": "An individual keeps the alleles it was born with; it is the "
               "make-up of the whole population that shifts across "
               "generations.",
    },
    {
        "id": "ks4-evolution-natural-selection-s03",
        "subtopic_slug": "evolution-natural-selection",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a characteristic must be inherited before "
                "natural selection can make it more common in a population.",
        "options": [
            "Because only inherited characteristics can be detected by a "
            "predator",
            "Because only alleles are passed to offspring, so only they can "
            "increase in later generations",
            "Because characteristics that are inherited are always more "
            "useful to an organism than learned ones",
            "Because natural selection removes every characteristic that is "
            "not inherited",
        ],
        "correct_index": 1,
        "why": "Selection changes a population only by changing which "
               "alleles are passed on, so a useful feature must be coded "
               "for in DNA.",
    },
    {
        "id": "ks4-evolution-natural-selection-s04",
        "subtopic_slug": "evolution-natural-selection",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the contribution Alfred Russel Wallace made to "
                "science besides co-developing the theory of natural "
                "selection.",
        "options": [
            "He worked out the structure of the DNA molecule",
            "He first described the inheritance of alleles in pea plants",
            "He studied how species are distributed across the Earth",
            "He collected the first fossil evidence of extinct species",
        ],
        "correct_index": 2,
        "why": "Wallace's work on biogeography — the distribution of species "
               "— gave further support to the theory of evolution.",
    },
    {
        "id": "ks4-evolution-natural-selection-h01",
        "subtopic_slug": "evolution-natural-selection",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Giraffes stretched their necks to reach "
                "high leaves, so their offspring were born with longer "
                "necks.' Explain the error in this reasoning.",
        "options": [
            "Stretching a neck does not change the alleles in the gametes, "
            "so it cannot be inherited",
            "Giraffes with longer necks would not survive better, so the "
            "change could not spread",
            "Neck length is an environmental characteristic, and "
            "characteristics like that are always inherited",
            "The offspring would be born with shorter necks, because "
            "characteristics reverse",
        ],
        "correct_index": 0,
        "why": "Only changes to the DNA carried in the gametes are "
               "inherited, so a characteristic gained during life is not "
               "passed on.",
    },
    {
        "id": "ks4-evolution-natural-selection-h02",
        "subtopic_slug": "evolution-natural-selection",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species can still become extinct even though "
                "natural selection is acting on its population.",
        "options": [
            "Because natural selection always removes the most successful "
            "individuals first",
            "Because natural selection stops working once a population "
            "becomes small",
            "Because there may be no individual with a useful variation "
            "when conditions change",
            "Because extinction only happens to species that have never "
            "varied at all",
        ],
        "correct_index": 2,
        "why": "Selection can only favour a variation that already exists, "
               "so if nobody in the population suits the new conditions, all "
               "of them may die.",
    },
    {
        "id": "ks4-evolution-natural-selection-h03",
        "subtopic_slug": "evolution-natural-selection",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect of a sudden change in the environment on "
                "a population with high genetic variation and on one with "
                "very low genetic variation.",
        "options": [
            "The varied population is wiped out first, because more of its "
            "individuals are poorly adapted",
            "Both are affected equally, because the environment acts on "
            "every individual alike",
            "The population with low variation adapts faster, because all "
            "its individuals are the same",
            "The varied population is more likely to contain individuals "
            "that survive and reproduce",
        ],
        "correct_index": 3,
        "why": "The more variation a population holds, the greater the "
               "chance that some individuals are already suited to the new "
               "conditions.",
    },
    {
        "id": "ks4-evolution-natural-selection-h04",
        "subtopic_slug": "evolution-natural-selection",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a population of beetles, the proportion that are dark "
                "rises from 5% to 80% over fifty years. Suggest what must be "
                "true for this to count as evolution.",
        "options": [
            "The beetles must have changed colour during their own "
            "lifetimes",
            "Beetle colour must be inherited, and dark beetles must have "
            "survived and reproduced more",
            "A mutation must have occurred in every dark beetle at the same "
            "time",
            "The dark beetles must have moved into the area from a "
            "different population",
        ],
        "correct_index": 1,
        "why": "A shift in how common a characteristic is counts as "
               "evolution only if the characteristic is heritable and "
               "selection favoured it.",
    },
]
