"""B10 lesson 02 — Chromosomes, genes and DNA: twelve questions (MRB-269).

The lesson's single claim is that nucleus, chromosome, gene and base are four
levels of one structure rather than four contents of a nucleus — "a chromosome
is not a different substance from DNA; it is DNA, packed". These twelve probe
that claim from every side the page offers: what a chromosome is made of, the
46/23 counts and where a sperm's 23 come from, the four model-card jobs
(molecule, package, instruction, alphabet), the red blood cell exception, the
two-metres-into-0.002 mm packing, and — in the harder band — the same rule
carried into contexts the page only gestures at: the sheep grown from one udder
cell, the chromosome counts in the stretch layer, the "one gene, one job"
simplification the legal line admits to, and a stained cheek cell whose
chromosomes refuse to show.

The distractors are built from the lesson's two declared misconceptions —
GENE-03 "chromosomes, genes and DNA are three different things in the nucleus"
(which reappears as a different substance stored beside the DNA, as thousands of
separate genes strung end to end, and as a protein box with the DNA loose
inside) and GENE-04 "only the cells that need a gene contain it" (as a skin cell
that kept only skin genes, as two cells that discarded what they did not use, as
an udder cell that had to be unspecialised to work) — plus the hook's own three
wrong wagers about the two metres (it is shared out, only part is in the
nucleus, the number is a figure of speech), rung 2's presence-follows-appearance
reading pushed onto eye colour between people, and the stretch layer's own
warning that a count is not the thing to look at.
"""

UNIT = "B10"
LESSON = "chromosomes-genes-and-dna"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-e01",
        "band": "easier",
        "text": "A human body cell holds 46 chromosomes inside its nucleus. "
                "What is one of those chromosomes actually made of?",
        "options": [
            {"text": "One long DNA molecule, coiled tightly with proteins so "
                     "it can be stored", "correct": True},
            {"text": "A different substance from DNA, stored beside the DNA "
                     "in the nucleus", "correct": False,
             "why": "A chromosome is not a different substance from DNA. It "
                    "is DNA, packed — the same molecule wound around proteins "
                    "so it can be moved around without tangling."},
            {"text": "Thousands of separate genes, joined end to end into one "
                     "long strand", "correct": False,
             "why": "Genes are not separate objects strung together. A "
                    "chromosome is one continuous DNA molecule and a gene is "
                    "a section of it — a chapter in the book, not a bead on a "
                    "string."},
            {"text": "A container made of protein, with the DNA held loosely "
                     "inside it", "correct": False,
             "why": "The proteins are what the DNA is wound around, not a box "
                    "it sits in. Take the proteins away and the chromosome is "
                    "still one DNA molecule."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e02",
        "band": "easier",
        "text": "How many chromosomes does a human body cell contain, and how "
                "are they arranged?",
        "options": [
            {"text": "23, arranged in pairs, with one of each pair from each "
                     "parent", "correct": False,
             "why": "23 is the number of pairs, and it is also the number of "
                    "single chromosomes in a sperm or egg cell. A body cell "
                    "has 46 altogether."},
            {"text": "46, all different from each other, with no matching "
                     "pairs at all", "correct": False,
             "why": "They come in 23 matched pairs. You inherited one of each "
                    "pair from each parent, which is why they match."},
            {"text": "46, arranged in 23 pairs, with one of each pair from "
                     "each parent", "correct": True},
            {"text": "Around twenty thousand, one chromosome for every gene "
                     "you carry", "correct": False,
             "why": "Twenty thousand is roughly the number of genes. "
                    "Thousands of genes sit along each of the 46 chromosomes "
                    "— genes and chromosomes are not counted one for one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e03",
        "band": "easier",
        "text": "Almost every cell in your body keeps an identical copy of "
                "the same complete instructions. Which cell is the famous "
                "exception, and why?",
        "options": [
            {"text": "A nerve cell — it is far too long to hold a whole set "
                     "of chromosomes", "correct": False,
             "why": "Length has nothing to do with it. A nerve cell has a "
                    "nucleus like almost every other cell, and the full 46 "
                    "chromosomes are inside it."},
            {"text": "A red blood cell — it loses its nucleus to make room "
                     "for haemoglobin", "correct": True},
            {"text": "An egg cell — it carries no chromosomes at all until it "
                     "is fertilised", "correct": False,
             "why": "An egg cell does carry chromosomes — 23 single ones. "
                    "Fertilisation adds the sperm's 23, which is how the new "
                    "cell reaches 46."},
            {"text": "A skin cell — it keeps only the genes it needs for "
                     "being skin", "correct": False,
             "why": "Every cell with a nucleus carries the whole set, skin "
                    "cells included. What makes a skin cell a skin cell is "
                    "which genes are switched on, not which ones it kept."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e04",
        "band": "easier",
        "text": "The model names four things by the job each one does: the "
                "molecule, the package, the instruction and the alphabet. "
                "Which one is the package?",
        "options": [
            {"text": "A base", "correct": False,
             "why": "Bases are the alphabet — the four letters, A, T, C and "
                    "G, that the instruction is written in."},
            {"text": "A gene", "correct": False,
             "why": "A gene is the instruction: one section of the DNA, "
                    "carrying the instruction for one characteristic."},
            {"text": "The nucleus", "correct": False,
             "why": "The nucleus is the room the packages are kept in, not "
                    "the packaging. A chromosome is the DNA itself, packed."},
            {"text": "A chromosome", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-02-s01",
        "band": "standard",
        "text": "A nerve cell and a skin cell from the same person contain "
                "exactly the same 46 chromosomes. So why do the two cells "
                "look and behave so differently?",
        "options": [
            {"text": "Each cell kept only the genes for its own job and got "
                     "rid of the rest", "correct": False,
             "why": "Nothing is thrown away. Both cells hold the complete "
                    "set; what they differ in is which of those genes they "
                    "are using."},
            {"text": "The nerve cell's chromosomes are arranged in a "
                     "different order inside it", "correct": False,
             "why": "There is no order for the cell to rearrange. The two "
                    "cells carry identical chromosomes carrying identical "
                    "genes in identical places."},
            {"text": "A different set of genes is switched on in each of the "
                     "two cells", "correct": True},
            {"text": "The nerve cell has been given extra chromosomes to make "
                     "it that long", "correct": False,
             "why": "Every body cell has 46, however big or oddly shaped it "
                    "is. Extra chromosomes are not how a cell becomes "
                    "specialised."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s02",
        "band": "standard",
        "text": "Uncoiled, the DNA from one of your cells stretches about two "
                "metres. Packed into chromosomes it measures thousandths of a "
                "millimetre. What happened to it in between?",
        "options": [
            {"text": "It was wound around proteins and coiled again and "
                     "again, with nothing removed", "correct": True},
            {"text": "Only a small part of it stayed in the nucleus, and the "
                     "rest is elsewhere", "correct": False,
             "why": "All of it is in the nucleus, in every cell, all the "
                    "time. The two metres is not shared out between cells or "
                    "stored anywhere else."},
            {"text": "It was squashed so hard that the molecule itself became "
                     "shorter and thinner", "correct": False,
             "why": "Coiling does not shrink the molecule. It is still two "
                    "metres of DNA, folded and wound and coiled — the way a "
                    "long rope fits into a small bag."},
            {"text": "Nothing — the two metres is a figure of speech, not a "
                     "real length", "correct": False,
             "why": "It is a real measured length. DNA is extraordinarily "
                    "thin, which is how something two metres long fits into a "
                    "nucleus 0.006 mm across."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s03",
        "band": "standard",
        "text": "Everybody carries the gene for eye colour, and yet people's "
                "eyes are different colours. What explains that?",
        "options": [
            {"text": "Only people with brown eyes carry the gene, and "
                     "blue-eyed people are missing it", "correct": False,
             "why": "The gene for eye colour is in everybody. What differs "
                    "between people is the version of it they carry, not "
                    "whether they have it."},
            {"text": "The gene is switched on in some people and switched off "
                     "in others", "correct": False,
             "why": "Switching genes on and off explains why a liver cell "
                    "differs from an eye cell in one person. Between two "
                    "people, what differs is the version of the gene."},
            {"text": "People carry different numbers of the eye colour gene "
                     "on their chromosomes", "correct": False,
             "why": "Everyone has the same genes in the same places along the "
                    "same 46 chromosomes. It is the sequence of bases along "
                    "that section that differs."},
            {"text": "People carry different versions of the same gene in the "
                     "same place", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s04",
        "band": "standard",
        "text": "A sperm cell carries 23 chromosomes rather than 46. Why is "
                "23 the right number for it to carry?",
        "options": [
            {"text": "Because a sperm cell is tiny, so only half of them will "
                     "fit inside it", "correct": False,
             "why": "Size does not decide it. The number is halved so that "
                    "fertilisation puts it back to 46 — a sperm cell twice "
                    "the size would still carry 23."},
            {"text": "Because it joins an egg cell's 23, and the new cell "
                     "then has the full 46", "correct": True},
            {"text": "Because a sperm carries the father's 23 pairs and the "
                     "egg carries the mother's", "correct": False,
             "why": "23 pairs would be 46 chromosomes, which is a whole set. "
                    "A sperm carries 23 single chromosomes — one taken from "
                    "each of the father's pairs."},
            {"text": "Because half of the 46 are identical copies, so half of "
                     "them can be discarded", "correct": False,
             "why": "The two chromosomes in a pair are matched, not "
                    "identical. One came from each parent, and they carry "
                    "different versions of the same genes."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-h01",
        "band": "harder",
        "text": "A whole sheep was once grown from a single cell taken from "
                "an adult sheep's udder. Which fact about that udder cell "
                "made it possible?",
        "options": [
            {"text": "Udder cells are unspecialised, so they are the only "
                     "cells that keep every gene", "correct": False,
             "why": "An udder cell is specialised, and that is the point. "
                    "Specialisation is about which genes are switched on, not "
                    "about which genes are present."},
            {"text": "It held the complete set of chromosomes, not only the "
                     "genes an udder uses", "correct": True},
            {"text": "The genes it was missing were supplied from a second "
                     "sheep's cells", "correct": False,
             "why": "Nothing was missing. Every cell with a nucleus already "
                    "holds the complete instructions, which is exactly why "
                    "one cell was enough."},
            {"text": "Udder cells carry spare copies of the chromosomes that "
                     "other cells do not have", "correct": False,
             "why": "Every body cell has the same 46 chromosomes. No cell "
                    "type carries spares, and no cell type carries a reduced "
                    "set."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h02",
        "band": "harder",
        "text": "A potato has 48 chromosomes and a human has 46. A student "
                "concludes that potatoes must be slightly more complex than "
                "humans. What is wrong with that reasoning?",
        "options": [
            {"text": "The comparison only works between animals, so a plant "
                     "cannot be included", "correct": False,
             "why": "It fails between animals too — a dog has 78 chromosomes "
                    "and a chimpanzee 48. The count is not a complexity scale "
                    "for anything."},
            {"text": "Humans have far more genes than potatoes, so humans win "
                     "the count that matters", "correct": False,
             "why": "Gene counts do not rank organisms either. A water flea "
                    "has more genes than you do, and humans turned out to "
                    "have only around twenty thousand."},
            {"text": "Potatoes have 48 because plant cells are larger than "
                     "animal cells", "correct": False,
             "why": "Cell size has nothing to do with chromosome number. A "
                    "fern carries over a thousand chromosomes without having "
                    "enormous cells."},
            {"text": "Chromosome number is only how the DNA is packaged, not "
                     "how much it says", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h03",
        "band": "harder",
        "text": "The model says a gene is an instruction for one job, and "
                "then admits that this is a deliberate simplification. Which "
                "observation shows the simplification straining?",
        "options": [
            {"text": "Height varies smoothly in a population, because many "
                     "genes affect it", "correct": True},
            {"text": "Every cell in one person's body carries the same gene "
                     "for eye colour", "correct": False,
             "why": "That is about where genes are kept, not about how many "
                    "genes shape one characteristic. It supports the simple "
                    "model rather than straining it."},
            {"text": "A human carries around twenty thousand genes but only "
                     "46 chromosomes", "correct": False,
             "why": "That tells you thousands of genes sit along each "
                    "chromosome, which is a fact about packaging. It says "
                    "nothing about how many genes make one characteristic."},
            {"text": "Two people with the same gene can carry different "
                     "versions of it", "correct": False,
             "why": "Different versions of one gene is the simple model "
                    "working. The strain comes from characteristics that need "
                    "many genes at once, like height."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h04",
        "band": "harder",
        "text": "A scientist stains a cheek cell and looks at its nucleus "
                "down a microscope. The chromosomes are in there, but she "
                "cannot see any of them. Why not?",
        "options": [
            {"text": "The chromosomes had moved out into the cytoplasm before "
                     "she stained the cell", "correct": False,
             "why": "Chromosomes cannot move out. They are the coiled DNA "
                    "stored in that nucleus, and nothing carries them into "
                    "the cytoplasm."},
            {"text": "Cheek cells throw their chromosomes away, in the same "
                     "way red blood cells do", "correct": False,
             "why": "The red blood cell is the exception, not the rule. A "
                    "cheek cell keeps its nucleus and its whole set of 46 "
                    "chromosomes."},
            {"text": "Chromosomes are only visible when a cell is about to "
                     "divide and the DNA coils tightly", "correct": True},
            {"text": "A school microscope cannot show anything at all that "
                     "sits inside a cell", "correct": False,
             "why": "A school microscope shows a stained nucleus easily. What "
                    "decides whether chromosomes show is how tightly the DNA "
                    "inside it is coiled at that moment."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-e05",
        "band": "easier",
        "text": "What is a gene?",
        "options": [
            {"text": "A small separate object attached to the outside of a "
                     "chromosome, like a bead threaded on a string",
             "correct": False,
             "why": "Nothing is attached. A gene is part of the chromosome "
                    "itself, the way a chapter is part of a book rather than a "
                    "bookmark in one"},
            {"text": "A length of DNA in a chromosome carrying the "
                     "instruction for one characteristic",
             "correct": True},
            {"text": "A whole chromosome, which is why a human body cell "
                     "is said to contain exactly 46 genes altogether in "
                     "its nucleus",
             "correct": False,
             "why": "A human carries around twenty thousand genes and only 46 "
                    "chromosomes, so a gene must be far smaller than a whole "
                    "chromosome"},
            {"text": "One of the four bases — A, T, C or G — from which "
                     "DNA is built",
             "correct": False,
             "why": "The bases are the units the instruction is written in. A "
                    "gene is a length of them, the way a word is a run of "
                    "letters rather than one letter"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e06",
        "band": "easier",
        "text": "The instruction in a gene is written using four units known "
                "by their initials. Which four?",
        "options": [
            {"text": "A, B, C and D",
             "correct": False,
             "why": "A tempting guess because they are the first four letters, "
                    "but the four bases are A, T, C and G"},
            {"text": "A, T, C and P",
             "correct": False,
             "why": "P is not one of them. Phosphate is a part of DNA but it "
                    "is not one of the four bases; the fourth is G"},
            {"text": "A, C, G and X",
             "correct": False,
             "why": "X is not a base. Three of these are right, and the "
                    "missing one is T"},
            {"text": "A, T, C and G",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e07",
        "band": "easier",
        "text": "A cheek cell, a liver cell and a plant's root hair cell all "
                "keep their instructions in the same part of the cell. Which "
                "part?",
        "options": [
            {"text": "The nucleus",
             "correct": True},
            {"text": "The cytoplasm",
             "correct": False,
             "why": "The cytoplasm is where most of the cell's chemistry "
                    "happens. The instructions are kept apart from it, in the "
                    "nucleus"},
            {"text": "The cell membrane",
             "correct": False,
             "why": "The membrane controls what enters and leaves the cell. It "
                    "stores nothing — the chromosomes are inside, in the "
                    "nucleus"},
            {"text": "A plant cell keeps them in the nucleus and an animal "
                     "cell in the cytoplasm",
             "correct": False,
             "why": "Both keep them in the nucleus. That is why a root hair "
                    "cell was listed alongside the two animal cells"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e08",
        "band": "easier",
        "text": "Roughly how many genes does a human carry altogether?",
        "options": [
            {"text": "23",
             "correct": False,
             "why": "23 is the number of pairs of chromosomes, and the number "
                    "of chromosomes in a sperm or egg cell. Genes are far more "
                    "numerous than that"},
            {"text": "46",
             "correct": False,
             "why": "46 is the number of chromosomes in a body cell. Each of "
                    "those chromosomes carries many genes along its length"},
            {"text": "Around twenty thousand",
             "correct": True},
            {"text": "Around thirty trillion",
             "correct": False,
             "why": "That is roughly the number of cells in a person, not the "
                    "number of genes. Almost every one of those cells carries "
                    "the same twenty thousand or so"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e09",
        "band": "easier",
        "text": "What does the DNA in a cell do?",
        "options": [
            {"text": "It is the fuel that supplies the cell with the "
                     "energy it needs for growing and for working",
             "correct": False,
             "why": "Energy comes from respiration. DNA is not a fuel — it is "
                    "the store of instructions"},
            {"text": "It carries the instructions for building and running an "
                     "organism",
             "correct": True},
            {"text": "It holds the cell in shape, acting like a stiff "
                     "frame running through the cell",
             "correct": False,
             "why": "DNA is coiled into chromosomes for storage, not for "
                    "support. Its job is to carry information"},
            {"text": "It carries the cell's waste out of the nucleus",
             "correct": False,
             "why": "Nothing about DNA is waste. It is the set of instructions "
                    "the cell is built and run from, and it stays in the "
                    "nucleus"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e10",
        "band": "easier",
        "text": "A person is built from around thirty trillion cells. What is "
                "true of almost every one of them?",
        "options": [
            {"text": "Each carries a different quarter of the person's "
                     "instructions",
             "correct": False,
             "why": "Nothing is shared out. Each cell carries a whole copy, "
                    "which is why one cell left on a glass is enough to "
                    "identify somebody"},
            {"text": "Each carries only the genes its own organ makes use of",
             "correct": False,
             "why": "A cell in your foot carries the gene for eye colour. What "
                    "differs between cells is which genes are switched on, not "
                    "which ones are there"},
            {"text": "Each grows its own set of instructions as it develops",
             "correct": False,
             "why": "Nothing is grown from scratch. Every cell's set is a copy "
                    "of the one the person started from"},
            {"text": "Each carries an identical copy of the same complete "
                     "instructions",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e11",
        "band": "easier",
        "text": "Why is the DNA in a cell packed into chromosomes rather than "
                "left as it is?",
        "options": [
            {"text": "So that the cell can decide which of its own genes "
                     "to keep and which ones it should throw away as waste",
             "correct": False,
             "why": "Nothing is thrown away. Every cell with a nucleus keeps "
                    "the complete set; packing is about storage, not "
                    "selection"},
            {"text": "So that the instructions cannot be read by mistake",
             "correct": False,
             "why": "The instructions have to be readable — that is what they "
                    "are for. Packing is what makes a very long molecule "
                    "manageable"},
            {"text": "So that about two metres of thin molecule can be "
                     "stored and moved without tangling",
             "correct": True},
            {"text": "So that the DNA molecule itself takes up much less "
                     "space by becoming both shorter and thinner",
             "correct": False,
             "why": "The molecule itself is unchanged — nothing is removed and "
                    "nothing shrinks. It is wound and coiled, the way a long "
                    "rope is coiled to be carried"},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-02-s05",
        "band": "standard",
        "text": "A student says a chromosome is where the genes are kept, in "
                "the way a tin keeps a set of pencils. What is wrong with the "
                "comparison?",
        "options": [
            {"text": "A gene is part of the chromosome itself, not an object "
                     "held inside it",
             "correct": True},
            {"text": "The genes are kept in the nucleus, and the chromosomes "
                     "are kept somewhere else",
             "correct": False,
             "why": "The chromosomes are in the nucleus and the genes are "
                    "lengths of those chromosomes. Nothing is kept anywhere "
                    "else"},
            {"text": "A chromosome holds far too many genes for a tin to be a "
                     "fair comparison",
             "correct": False,
             "why": "The number is not the problem. Even a tin holding "
                    "thousands of pencils would still be a container with "
                    "separate objects in it, and that is the part that fails"},
            {"text": "Nothing is wrong with it — a chromosome is a package, "
                     "which is what a tin is",
             "correct": False,
             "why": "A chromosome is packed DNA, and packed is not the same as "
                    "packaging. There is no wrapper: the container and the "
                    "contents are one molecule"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s06",
        "band": "standard",
        "text": "Two genes are the same length and contain exactly the same "
                "numbers of A, T, C and G, yet they carry different "
                "instructions. How is that possible?",
        "options": [
            {"text": "One of them must be on a chromosome from the mother and "
                     "one from the father",
             "correct": False,
             "why": "Which parent a chromosome came from does not change what "
                    "its genes say. The information is in the sequence"},
            {"text": "One of them must be switched on and the other switched "
                     "off",
             "correct": False,
             "why": "Switching decides whether a gene is being used, not what "
                    "it says. A switched-off gene carries exactly the same "
                    "instruction it always did"},
            {"text": "The bases are in a different order, and the order is the "
                     "instruction",
             "correct": True},
            {"text": "They cannot carry different instructions if they are "
                     "made of the same bases",
             "correct": False,
             "why": "The same twenty-six letters write every book in a "
                    "library. What differs between two genes is the order the "
                    "four bases run in"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s07",
        "band": "standard",
        "text": "A human body cell has 46 chromosomes and a human carries "
                "around twenty thousand genes. How do 46 chromosomes hold "
                "twenty thousand genes?",
        "options": [
            {"text": "Most of the genes are stored outside the chromosomes, "
                     "elsewhere in the nucleus",
             "correct": False,
             "why": "There is nowhere else. Every gene is a length of the DNA "
                    "in one of the 46 chromosomes"},
            {"text": "Each chromosome is one very long DNA molecule with many "
                     "genes along its length",
             "correct": True},
            {"text": "Each chromosome is used over and over, carrying a "
                     "different gene at different times",
             "correct": False,
             "why": "A gene does not move about and a chromosome does not take "
                    "turns. Every gene sits at its own place on its own "
                    "chromosome, permanently"},
            {"text": "The twenty thousand is counted across all the person's "
                     "cells added together",
             "correct": False,
             "why": "Around twenty thousand is the number in one cell, and "
                    "almost every cell has the same set. Adding cells up would "
                    "give the same genes counted thirty trillion times"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s08",
        "band": "standard",
        "text": "A skin cell divides into two new skin cells. What does each "
                "of the two new cells end up with?",
        "options": [
            {"text": "23 chromosomes each, because the 46 were shared between "
                     "them",
             "correct": False,
             "why": "That is what happens when gametes are made, and it would "
                    "leave a skin cell with half a set. Ordinary body cells "
                    "each keep the full 46"},
            {"text": "Only the genes a skin cell has switched on, since the "
                     "rest were not needed",
             "correct": False,
             "why": "Nothing is left behind. Both new cells carry the complete "
                    "set, and switching decides only which of it gets used"},
            {"text": "Half the DNA each, so the molecule has to be rebuilt "
                     "afterwards",
             "correct": False,
             "why": "Nothing is torn in half. Each new cell receives a "
                    "complete copy of all 46 chromosomes"},
            {"text": "A complete copy of all 46 chromosomes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s09",
        "band": "standard",
        "text": "A mature red blood cell has no nucleus. What follows from "
                "that?",
        "options": [
            {"text": "It carries no chromosomes at all, unlike almost "
                     "every other cell",
             "correct": True},
            {"text": "It keeps only the genes needed to make haemoglobin",
             "correct": False,
             "why": "It carries none. Losing the nucleus means losing the "
                    "whole set, not keeping a useful part of it"},
            {"text": "It cannot really be a living cell, since every "
                     "living cell must have a nucleus to work from",
             "correct": False,
             "why": "It is a living cell doing a demanding job. What it has "
                    "given up is the storage space its chromosomes took, in "
                    "exchange for room to carry oxygen"},
            {"text": "It reads the instructions it needs from the "
                     "neighbouring cells around it instead",
             "correct": False,
             "why": "Instructions do not pass between cells like that. A red "
                    "blood cell simply works without a set, which is why it "
                    "has a short life"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s10",
        "band": "standard",
        "text": "A student writes: \"Genes are made of DNA, and chromosomes "
                "are made of genes.\" One half of that is right. Which, and "
                "why is the other half wrong?",
        "options": [
            {"text": "Both halves are right — a chromosome is a row of genes "
                     "made of DNA",
             "correct": False,
             "why": "A chromosome is one continuous DNA molecule. The genes "
                    "are lengths marked out along it, with more DNA between "
                    "them, so it is not built out of genes"},
            {"text": "The first half is right; a chromosome is one DNA "
                     "molecule with genes marked out along it",
             "correct": True},
            {"text": "The second half is right; a gene is not made of DNA but "
                     "sits on top of it",
             "correct": False,
             "why": "That is the wrong way round. A gene is DNA — a section of "
                    "it — and nothing sits on top of anything"},
            {"text": "Neither half is right; genes, chromosomes and DNA are "
                     "three separate things in the nucleus",
             "correct": False,
             "why": "They are one thing at three magnifications. Asking "
                    "whether the nucleus holds chromosomes or DNA is like "
                    "asking whether a library holds books or paper"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s11",
        "band": "standard",
        "text": "The 46 chromosomes in a human body cell are described as 23 "
                "pairs rather than as 46 separate chromosomes. Why?",
        "options": [
            {"text": "Because they sit side by side in the nucleus, two at "
                     "a time",
             "correct": False,
             "why": "How they sit in the nucleus is not the reason. They are "
                    "called pairs because the two members of a pair match each "
                    "other"},
            {"text": "Because the two in each pair carry the same genes, "
                     "one from each parent",
             "correct": True},
            {"text": "Because a cell always makes a spare copy of each "
                     "chromosome in case the first one is ever damaged",
             "correct": False,
             "why": "Neither is a spare. Both are used, and the two came from "
                    "different parents rather than from a copying step"},
            {"text": "Because 46 is an even number, so the chromosomes can "
                     "always be counted off in twos",
             "correct": False,
             "why": "Counting in twos is not pairing. The pairs are real — "
                    "each is two matching chromosomes, one from each parent"},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-h05",
        "band": "harder",
        "text": "A forensic scientist can read a person's DNA from a hair "
                "pulled out at the root, but not from a cut length of the "
                "hair shaft. Explain the difference.",
        "options": [
            {"text": "Cutting a hair damages the DNA inside it, while pulling "
                     "it leaves the DNA whole",
             "correct": False,
             "why": "The scissors are not the problem. The shaft has no cells "
                    "with nuclei in it to hold DNA in the first place"},
            {"text": "The root is still growing, so it is making new DNA that "
                     "the shaft has used up",
             "correct": False,
             "why": "DNA is not used up. What the root has and the shaft has "
                    "not is living cells with nuclei"},
            {"text": "The shaft is further from the head, so its DNA has been "
                     "worn away by washing",
             "correct": False,
             "why": "Washing does not strip DNA out of cells. The shaft never "
                    "carried nucleated cells to begin with"},
            {"text": "The root carries living cells with nuclei; the shaft "
                     "does not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h06",
        "band": "harder",
        "text": "A water flea carries more genes than a human does. What is "
                "the strongest thing that fact tells you?",
        "options": [
            {"text": "That counting genes is not a way of measuring how "
                     "complex an organism is",
             "correct": True},
            {"text": "That water fleas are more complex than humans, which "
                     "biologists had not expected",
             "correct": False,
             "why": "That is the same reasoning with a different answer. The "
                    "count does not track complexity in either direction, "
                    "which is precisely the finding"},
            {"text": "That the water flea's genes must each be much shorter "
                     "than a human gene",
             "correct": False,
             "why": "Nothing in the count says anything about length. The "
                    "point is that a gene total does not measure what people "
                    "assumed it measured"},
            {"text": "That humans must have lost genes they once had",
             "correct": False,
             "why": "An invented history to rescue the assumption. Two species "
                    "having different gene totals needs no story about loss — "
                    "the totals simply do not rank anything"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h07",
        "band": "harder",
        "text": "Every cell with a nucleus is said to carry the complete set "
                "of instructions. A sperm cell has a nucleus and carries 23 "
                "chromosomes. Is the claim broken?",
        "options": [
            {"text": "Yes — 23 is only half a set, so a sperm must be "
                     "missing half of the instructions altogether",
             "correct": False,
             "why": "It has one of every pair, so every instruction is there "
                    "once. What it lacks is the second copy, not half the "
                    "information"},
            {"text": "Yes — a sperm keeps only the genes needed to fertilise "
                     "an egg",
             "correct": False,
             "why": "No cell selects its genes that way. A sperm carries a "
                    "complete single set, chosen one from each pair"},
            {"text": "No — it carries one of each pair, so it holds one "
                     "complete copy instead of two",
             "correct": True},
            {"text": "No — a sperm cell has 46 chromosomes like every "
                     "other body cell, and 23 is simply the number of "
                     "pairs",
             "correct": False,
             "why": "A sperm really does carry 23 single chromosomes. If it "
                    "carried 46 the fertilised egg would have 92"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h08",
        "band": "harder",
        "text": "A student says the DNA in a daffodil must be a different "
                "substance from the DNA in a dog, because the two organisms "
                "are so unlike each other. What is the best reply?",
        "options": [
            {"text": "She is right — plant DNA uses different bases from "
                     "animal DNA",
             "correct": False,
             "why": "The same four bases, A, T, C and G, are used throughout "
                    "living things. Different bases would make the two "
                    "unrelated substances, and they are not"},
            {"text": "It is the same kind of molecule with the same four "
                     "bases, in a different order",
             "correct": True},
            {"text": "She is right, because a plant cell has no nucleus to "
                     "keep DNA in",
             "correct": False,
             "why": "Plant cells have nuclei — a root hair cell keeps its "
                    "chromosomes in exactly the same place a cheek cell does"},
            {"text": "It is the same molecule, and the two organisms differ "
                     "because a daffodil has fewer chromosomes",
             "correct": False,
             "why": "Chromosome number is only how the DNA is packaged. A dog "
                    "has 78 and a potato 48, and neither number says what the "
                    "instructions are"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h09",
        "band": "harder",
        "text": "A gene is described as the instruction for one "
                "characteristic. A student concludes that a person with "
                "twenty thousand genes must have exactly twenty thousand "
                "characteristics. Why does the arithmetic fail?",
        "options": [
            {"text": "Because a person has far more than twenty thousand "
                     "characteristics, so some genes must do more than one "
                     "job",
             "correct": False,
             "why": "Half right, and it misses the other half. Many genes do "
                    "affect more than one characteristic, but many "
                    "characteristics also need a great many genes at once"},
            {"text": "Because the twenty thousand is only a rough "
                     "estimate, and the true number of genes is much "
                     "larger",
             "correct": False,
             "why": "The estimate is good, and its being an estimate is not "
                    "the flaw. The flaw is treating one gene and one "
                    "characteristic as a matching pair"},
            {"text": "Because genes that are switched off produce no "
                     "characteristic",
             "correct": False,
             "why": "A gene switched off in one cell is switched on in "
                    "another. Switching is about where a gene is used, not "
                    "about characteristics going missing from the count"},
            {"text": "Because most characteristics take many genes, and "
                     "many genes affect more than one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h10",
        "band": "harder",
        "text": "A gene is switched off in a skin cell for the whole of that "
                "cell's life. When the cell divides, is that gene passed to "
                "the two new cells?",
        "options": [
            {"text": "Yes — the copy includes every gene, whether it was being "
                     "used or not",
             "correct": True},
            {"text": "No — a gene that is never used is lost when the cell "
                     "divides",
             "correct": False,
             "why": "Nothing is dropped for being unused. If it were, the "
                    "skin cells of a person's arm would slowly lose the genes "
                    "for everything else"},
            {"text": "Only if the new cells will need it, because a cell "
                     "copies what its daughters will use",
             "correct": False,
             "why": "A dividing cell cannot know what will be needed later, "
                    "and does not choose. It copies all 46 chromosomes"},
            {"text": "No — switched-off genes are stored separately and stay "
                     "in the parent cell",
             "correct": False,
             "why": "There is no separate store. A switched-off gene sits in "
                    "its own place on its own chromosome, and the chromosome "
                    "is copied whole"},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h11",
        "band": "harder",
        "text": "A student says four bases is far too small an alphabet to "
                "hold the instructions for a whole organism. What is the best "
                "reply?",
        "options": [
            {"text": "She is right, which is why most characteristics need "
                     "many genes working together rather than one",
             "correct": False,
             "why": "Many genes per characteristic is true and is a separate "
                    "matter. It is not a patch for a shortage of letters, "
                    "because there is no shortage"},
            {"text": "She is right about DNA on its own, and it is the "
                     "proteins wound through a chromosome that supply the "
                     "rest of it",
             "correct": False,
             "why": "The proteins are packing, not information. Every "
                    "instruction is in the order of the bases"},
            {"text": "Millions of bases in a row give a vast number of "
                     "possible orders, so four is plenty",
             "correct": True},
            {"text": "There are really twenty thousand bases, one for each "
                     "gene",
             "correct": False,
             "why": "There are four bases and around twenty thousand genes. "
                    "Each gene is a long run of those same four, which is "
                    "exactly how four is enough"},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    #
    # The seam this block works is the one the first two passes left alone:
    # the six-level scale column itself (1.6 m, 0.02 mm, 0.006 mm, 0.002 mm,
    # 0.0000003 mm), the stretch layer's counts, and the four model cards read
    # as four jobs rather than four objects. Nothing here reproduces a ladder
    # rung: rung 1's ordering task and rung 4's crime-scene task are both
    # deliberately absent, and rung 2's "does a cell in your foot carry the
    # gene for eye colour" is approached only from the side (where the
    # difference between two people actually lies), never re-asked.
    #
    # ⚠️ The gamete arithmetic (a body cell's count halved to make a sex cell)
    # is b10-04's and is NOT worked here — this leaf keeps chromosome PAIRS,
    # b10-04 keeps gametes. Brief §9.4's shared-fact rule.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-e12",
        "band": "easier",
        "text": "Roughly how wide is a single human cell?",
        "options": [
            {"text": "About 0.2 mm",
             "correct": False,
             "why": "Ten times too wide. Something 0.2 mm across can be seen "
                    "as a speck without a microscope, and a cell cannot."},
            {"text": "About 0.02 mm",
             "correct": True},
            {"text": "About 0.006 mm",
             "correct": False,
             "why": "That is the width of the nucleus sitting inside the cell, "
                    "which is roughly three times narrower than the cell."},
            {"text": "About 0.002 mm",
             "correct": False,
             "why": "That is the length of one chromosome. A whole cell is "
                    "about ten times wider than a single chromosome is long."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e13",
        "band": "easier",
        "text": "A chromosome is DNA wound around something else and then "
                "coiled. Wound around what?",
        "options": [
            {"text": "Fat",
             "correct": False,
             "why": "There is no fat in a chromosome. The DNA is wound around "
                    "proteins, and that is what lets a very long molecule be "
                    "stored without tangling."},
            {"text": "Proteins",
             "correct": True},
            {"text": "Other genes",
             "correct": False,
             "why": "A gene is a section of the DNA itself, so there is no "
                    "separate object there for the strand to wind around."},
            {"text": "The nucleus",
             "correct": False,
             "why": "The nucleus is the part of the cell the packed "
                    "chromosomes are kept in, not something they wind around."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e14",
        "band": "easier",
        "text": "What is the name for a single one of the four units A, T, C "
                "and G?",
        "options": [
            {"text": "A base",
             "correct": True},
            {"text": "A gene",
             "correct": False,
             "why": "A gene is a long run of those units, the way a word is a "
                    "run of letters rather than a single letter."},
            {"text": "A chromosome",
             "correct": False,
             "why": "A chromosome is the whole coiled molecule, carrying "
                    "millions of these units along its length."},
            {"text": "A nucleus",
             "correct": False,
             "why": "The nucleus is the part of the cell that holds the "
                    "chromosomes. It is not a unit of the writing."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e15",
        "band": "easier",
        "text": "A gene carries an instruction. What is it about the bases "
                "that carries that instruction?",
        "options": [
            {"text": "How many bases the gene contains altogether",
             "correct": False,
             "why": "Two genes can hold the same number of bases and say "
                    "completely different things, so counting cannot be it."},
            {"text": "The proteins the bases are wound around",
             "correct": False,
             "why": "Those proteins hold the molecule in a tidy package. They "
                    "carry no instruction of their own at all."},
            {"text": "The order they run in along the gene",
             "correct": True},
            {"text": "The amount of each base the cell can make",
             "correct": False,
             "why": "A cell does not read amounts. What is read is the "
                    "sequence of the four letters from one end to the other."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e16",
        "band": "easier",
        "text": "How many chromosomes does a human egg cell carry?",
        "options": [
            {"text": "23",
             "correct": True},
            {"text": "46",
             "correct": False,
             "why": "46 is the number in a body cell. An egg carries one "
                    "chromosome out of each pair instead of both."},
            {"text": "92",
             "correct": False,
             "why": "No human cell carries 92. That is twice a full set, and "
                    "nothing in the body ever holds that many."},
            {"text": "Around twenty thousand",
             "correct": False,
             "why": "That is roughly how many genes a person carries. Genes "
                    "and chromosomes are not counted one for one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e17",
        "band": "easier",
        "text": "A human body cell holds 46 chromosomes. How many of them came "
                "from the father?",
        "options": [
            {"text": "23 — one of each pair",
             "correct": True},
            {"text": "46 — the whole set",
             "correct": False,
             "why": "Half the set came from each parent, and that is exactly "
                    "what makes the 46 fall into 23 matching pairs."},
            {"text": "None — the cell builds its own",
             "correct": False,
             "why": "No cell builds a chromosome from scratch. Every one of "
                    "the 46 arrived from a parent and has been copied since."},
            {"text": "It differs from cell to cell",
             "correct": False,
             "why": "Every body cell holds a copy of the same original set, so "
                    "the share from each parent is the same in all of them."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e18",
        "band": "easier",
        "text": "The lesson says that a chromosome is DNA, packed. What does "
                "that mean?",
        "options": [
            {"text": "It is a wrapper with the DNA folded up inside it",
             "correct": False,
             "why": "There is no wrapper. Unwind the proteins and what is left "
                    "is still a single DNA molecule."},
            {"text": "It is a store of DNA the cell can draw on",
             "correct": False,
             "why": "It is not a supply of spare material. It is one "
                    "particular DNA molecule, coiled up so it can be kept."},
            {"text": "It is DNA squashed until the molecule is shorter",
             "correct": False,
             "why": "Nothing shrinks. The molecule is as long as it ever was, "
                    "wound around proteins and then coiled."},
            {"text": "It is the same molecule as the DNA, wound up small",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e19",
        "band": "easier",
        "text": "A gene is often compared to a chapter in a book. What does "
                "the book stand for?",
        "options": [
            {"text": "The nucleus, where the chapters are stored",
             "correct": False,
             "why": "The nucleus is the room the books are kept in. The book "
                    "is the molecule the chapter is a part of."},
            {"text": "The whole DNA molecule of a chromosome",
             "correct": True},
            {"text": "The single base at the start of the gene",
             "correct": False,
             "why": "A base is one letter. A book is far more than the first "
                    "letter of one of its chapters."},
            {"text": "The proteins the DNA is wound around",
             "correct": False,
             "why": "The proteins are what the book is rolled up with for "
                    "storage. They are no part of what is written."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e20",
        "band": "easier",
        "text": "How does the DNA in a person's liver cell compare with the "
                "DNA in the same person's skin cell?",
        "options": [
            {"text": "It differs, because each organ keeps its own set",
             "correct": False,
             "why": "Every cell with a nucleus holds the complete set. What "
                    "differs between the two is which genes are switched on."},
            {"text": "It differs, because a liver cell is bigger",
             "correct": False,
             "why": "Size makes no difference to the instructions. Both cells "
                    "carry the same 46 chromosomes as each other."},
            {"text": "It is the same, but only until the person grows up",
             "correct": False,
             "why": "Nothing rewrites the set later on. Each cell is a copy of "
                    "the one the person started life as."},
            {"text": "It is the same, down to the last base",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e21",
        "band": "easier",
        "text": "In which of these human cells would you find 46 chromosomes?",
        "options": [
            {"text": "A sperm cell",
             "correct": False,
             "why": "A sperm carries 23 single chromosomes, one taken from "
                    "each of the father's pairs."},
            {"text": "An egg cell",
             "correct": False,
             "why": "An egg carries 23 as well. The 46 comes back when the two "
                    "of them join at fertilisation."},
            {"text": "A cheek cell",
             "correct": True},
            {"text": "A mature red blood cell",
             "correct": False,
             "why": "A mature red blood cell has thrown its nucleus away, so "
                    "it carries no chromosomes at all."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e22",
        "band": "easier",
        "text": "Roughly how many cells is one person built from?",
        "options": [
            {"text": "Around twenty thousand",
             "correct": False,
             "why": "That is roughly the number of genes a person carries. "
                    "There are vastly more cells than there are genes."},
            {"text": "Around forty-six",
             "correct": False,
             "why": "46 is the number of chromosomes in one body cell, not a "
                    "number of cells."},
            {"text": "Around two hundred",
             "correct": False,
             "why": "Two hundred is closer to the number of different kinds of "
                    "cell in a person than to how many cells there are."},
            {"text": "Around thirty trillion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e23",
        "band": "easier",
        "text": "Of these four, which has the most chromosomes in a body cell: "
                "a human, a chimpanzee, a dog or a potato?",
        "options": [
            {"text": "The human, with 46",
             "correct": False,
             "why": "46 is the smallest of these four numbers. A chimpanzee "
                    "and a potato both have 48, and a dog has more still."},
            {"text": "The chimpanzee, with 48",
             "correct": False,
             "why": "48 beats the human's 46 and ties with the potato, but the "
                    "dog is well ahead of all three."},
            {"text": "The potato, with 48",
             "correct": False,
             "why": "The potato ties with the chimpanzee on 48. Neither of "
                    "them comes close to the dog."},
            {"text": "The dog, with 78",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e24",
        "band": "easier",
        "text": "In which year did the Human Genome Project finish and report "
                "how many genes a human carries?",
        "options": [
            {"text": "2003",
             "correct": True},
            {"text": "1903",
             "correct": False,
             "why": "Nobody could read a sequence of bases in 1903. The "
                    "structure of DNA itself was not worked out until 1953."},
            {"text": "1953",
             "correct": False,
             "why": "1953 is the year the structure of DNA was published. "
                    "Counting the genes took another fifty years."},
            {"text": "2023",
             "correct": False,
             "why": "The project had been finished for twenty years by then. "
                    "The count of about twenty thousand dates from 2003."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e25",
        "band": "easier",
        "text": "A stained cheek cell shows a clear nucleus but no chromosomes "
                "inside it. What is in that nucleus?",
        "options": [
            {"text": "Nothing — the chromosomes are made when they are needed",
             "correct": False,
             "why": "Nothing is made to order. The full 46 are in there the "
                    "whole time, whether or not they can be seen."},
            {"text": "Half the chromosomes, with the rest in the cytoplasm",
             "correct": False,
             "why": "The chromosomes never leave the nucleus. All 46 are "
                    "inside it, and none is out in the cytoplasm."},
            {"text": "Proteins only, with the DNA stored somewhere else",
             "correct": False,
             "why": "The proteins are in there with the DNA, not instead of "
                    "it. There is nowhere else in the cell for DNA to go."},
            {"text": "The same DNA, spread out so thinly it can never be seen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e26",
        "band": "easier",
        "text": "A human body cell contains 46 chromosomes. How many separate "
                "DNA molecules is that?",
        "options": [
            {"text": "One, shared between all 46",
             "correct": False,
             "why": "A single molecule cannot be in 46 packages at once. Each "
                    "chromosome is its own molecule, complete in itself."},
            {"text": "23, one for each pair",
             "correct": False,
             "why": "The two chromosomes in a pair are two separate molecules, "
                    "one from each parent, not two ends of one."},
            {"text": "46, one for each chromosome",
             "correct": True},
            {"text": "Around twenty thousand, one for each gene",
             "correct": False,
             "why": "A gene is a section of a molecule rather than a molecule "
                    "of its own, so genes are not counted this way."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e27",
        "band": "easier",
        "text": "Compare the DNA of two unrelated people. Which of these is "
                "different between them?",
        "options": [
            {"text": "The order the bases run in at particular places",
             "correct": True},
            {"text": "Which four bases their DNA is written with",
             "correct": False,
             "why": "Every living thing uses the same four, A, T, C and G. "
                    "There is no fifth base for anybody to have instead."},
            {"text": "The number of chromosomes in a body cell",
             "correct": False,
             "why": "Every person has 46 in a body cell. That number is the "
                    "same for the species, not a difference between people."},
            {"text": "The place along a chromosome each gene sits",
             "correct": False,
             "why": "A given gene sits in the same place on the same "
                    "chromosome in everybody. What differs is what it says."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e28",
        "band": "easier",
        "text": "Which two of these have the same number of chromosomes in a "
                "body cell?",
        "options": [
            {"text": "A human and a chimpanzee",
             "correct": False,
             "why": "A human has 46 and a chimpanzee 48, so the two do not "
                    "match, however closely related they are."},
            {"text": "A chimpanzee and a potato",
             "correct": True},
            {"text": "A human and a dog",
             "correct": False,
             "why": "A dog has 78 against the human's 46, which is the widest "
                    "gap of any pair on this list."},
            {"text": "A dog and a potato",
             "correct": False,
             "why": "A dog has 78 and a potato 48. They are thirty apart, so "
                    "they are not the matching pair."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e29",
        "band": "easier",
        "text": "What does it mean to say that a gene is switched on in a "
                "particular cell?",
        "options": [
            {"text": "The cell has kept that gene and thrown the others away",
             "correct": False,
             "why": "Nothing is thrown away. Every gene stays in place, "
                    "switched on or not, in every cell with a nucleus."},
            {"text": "That gene is being used in that cell",
             "correct": True},
            {"text": "The gene has moved into the cytoplasm to be read",
             "correct": False,
             "why": "Genes cannot move. A gene is a section of a chromosome, "
                    "and the chromosomes stay inside the nucleus."},
            {"text": "The cell has made itself an extra copy of that gene",
             "correct": False,
             "why": "No extra copies are made. Using a gene does not change "
                    "how many of it a cell is carrying."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-e30",
        "band": "easier",
        "text": "Uncoil all the DNA in one of your cells and lay it end to "
                "end. Roughly how long is it?",
        "options": [
            {"text": "About two millimetres",
             "correct": False,
             "why": "Two millimetres would sit comfortably in a cell without "
                    "any packing at all, and the packing is the whole story."},
            {"text": "About two centimetres",
             "correct": False,
             "why": "Still far too short. The figure is a thousand times "
                    "larger than this, which is why the coiling matters."},
            {"text": "About two kilometres",
             "correct": False,
             "why": "A thousand times too long. Two metres is the measured "
                    "figure for a single human cell."},
            {"text": "About two metres",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-02-s12",
        "band": "standard",
        "text": "A nucleus is about 0.006 mm across and a chromosome about "
                "0.002 mm long. Roughly how many chromosome-lengths would fit "
                "across the nucleus?",
        "options": [
            {"text": "Six",
             "correct": False,
             "why": "The 6 in 0.006 is not a count of anything. One length has "
                    "to be divided by the other, which gives three."},
            {"text": "Forty-six",
             "correct": False,
             "why": "46 is how many chromosomes there are, not how many fit "
                    "across. They fit because each one is coiled up small."},
            {"text": "Three thousand",
             "correct": False,
             "why": "This is 0.006 divided by 0.000002. The chromosome figure "
                    "is 0.002 mm, so three zeros have been added to it."},
            {"text": "Three",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s13",
        "band": "standard",
        "text": "What job do the proteins inside a chromosome do?",
        "options": [
            {"text": "They carry half of the instructions, with DNA "
                     "carrying the rest",
             "correct": False,
             "why": "Every instruction is written in the order of the bases. "
                    "The proteins carry none of it."},
            {"text": "They join one chromosome to the next along a row",
             "correct": False,
             "why": "The 46 chromosomes are separate from one another. Nothing "
                    "strings them together into a row."},
            {"text": "They read the genes and decide which are switched on",
             "correct": False,
             "why": "Switching is not what these proteins are for. Their job "
                    "here is storage: they are what the strand winds around."},
            {"text": "They give the DNA something to wind around, so it packs "
                     "without tangling",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s14",
        "band": "standard",
        "text": "A scientist examines two cells from one person. One holds 46 "
                "chromosomes and the other holds 23. What are the two cells?",
        "options": [
            {"text": "Both are body cells, and one is about to divide",
             "correct": False,
             "why": "A body cell about to divide still has its full 46. "
                    "Dividing never leaves a body cell with half a set."},
            {"text": "A body cell and a sex cell",
             "correct": True},
            {"text": "A healthy cell and one that has lost chromosomes",
             "correct": False,
             "why": "23 is a normal, expected number in one kind of cell. "
                    "Nothing has been lost from it."},
            {"text": "A cell from the mother's side and one from the father's",
             "correct": False,
             "why": "Every body cell holds chromosomes from both parents, 23 "
                    "from each. No cell is built from one parent's set."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s15",
        "band": "standard",
        "text": "A school microscope can show chromosomes in a cell that is "
                "about to divide, but never shows a single gene. Why not?",
        "options": [
            {"text": "Genes are kept outside the nucleus, where the stain does "
                     "not reach them",
             "correct": False,
             "why": "Every gene is a section of a chromosome, and the "
                    "chromosomes are inside the nucleus with the stain."},
            {"text": "A gene is a short section of one chromosome, far below "
                     "what the microscope can show",
             "correct": True},
            {"text": "Genes are only made at the moment a cell needs to use "
                     "one of them",
             "correct": False,
             "why": "Genes are not made to order. They are lengths of DNA that "
                    "are present the whole time, used or not."},
            {"text": "Genes are colourless, so no stain will ever pick one "
                     "out of the nucleus",
             "correct": False,
             "why": "The chromosome the gene sits in is stained along its "
                    "whole length. Size, not colour, is what defeats it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s16",
        "band": "standard",
        "text": "Why is it fair to say that a chromosome, a gene and the bases "
                "are one thing seen at three magnifications?",
        "options": [
            {"text": "Because the nucleus builds all three out of the same "
                     "raw materials, one after the other, as it needs them",
             "correct": False,
             "why": "It is not that they are made of similar stuff. They are "
                    "literally the same molecule, looked at more closely."},
            {"text": "Because a microscope can be adjusted until all three "
                     "come into view together",
             "correct": False,
             "why": "No microscope can show a gene or a base at all. The claim "
                    "is about what they are, not about what can be seen."},
            {"text": "Because the three of them are always found beside each "
                     "other in the same nucleus",
             "correct": False,
             "why": "Sitting side by side is exactly what they do not do. Each "
                    "one is part of the one above it."},
            {"text": "Because a chromosome is coiled DNA, a gene is a section "
                     "of it, and the bases are its units",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s17",
        "band": "standard",
        "text": "A dog body cell holds 78 chromosomes. How many matching pairs "
                "is that, and where did each pair come from?",
        "options": [
            {"text": "78 pairs, one pair for each chromosome",
             "correct": False,
             "why": "That would mean 156 chromosomes altogether. A pair is two "
                    "of the 78, so there are half as many pairs."},
            {"text": "156 pairs, since every chromosome pairs twice",
             "correct": False,
             "why": "A chromosome has one partner, not two. Pairing twice "
                    "would need four of each, which no cell has."},
            {"text": "39 pairs, with one of each pair from each parent",
             "correct": True},
            {"text": "39 pairs, both members of a pair from the mother",
             "correct": False,
             "why": "The number of pairs is right and the source is not. One "
                    "member of each pair came from each parent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s18",
        "band": "standard",
        "text": "A student says a cell with more of its genes switched on must "
                "hold more DNA than one with fewer. What is wrong with that?",
        "options": [
            {"text": "Switched-off genes are stored in a smaller, tighter form "
                     "than switched-on ones",
             "correct": False,
             "why": "No gene is filed away in a different form. Every cell "
                    "holds the same 46 chromosomes, coiled the same way."},
            {"text": "Every cell with a nucleus holds the same DNA; switching "
                     "changes use, not amount",
             "correct": True},
            {"text": "A cell using more genes has actually thrown some of its "
                     "DNA away to make room",
             "correct": False,
             "why": "Using a gene costs no space and nothing is discarded. The "
                    "complete set stays put in every cell."},
            {"text": "The amount of DNA rises and falls through the day as "
                     "genes are switched on",
             "correct": False,
             "why": "The amount is fixed. A cell's DNA is copied only when it "
                    "is about to divide, and never in response to use."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s19",
        "band": "standard",
        "text": "The gene count reported in 2003 came as a surprise. Why was "
                "about twenty thousand a surprising number?",
        "options": [
            {"text": "Because a count that large could not have been made with "
                     "the equipment of the time",
             "correct": False,
             "why": "The counting itself worked. It was the size of the answer "
                    "that people had not expected."},
            {"text": "Because estimates beforehand had run as high as a "
                     "hundred thousand",
             "correct": True},
            {"text": "Because it is fewer genes than a human has chromosomes",
             "correct": False,
             "why": "Twenty thousand genes against 46 chromosomes is far more "
                    "genes, not fewer. Each chromosome carries many."},
            {"text": "Because it was the first time anybody had suggested that "
                     "humans carry genes at all",
             "correct": False,
             "why": "Genes had been known about for a century by then. What "
                    "was new in 2003 was how many there turned out to be."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s20",
        "band": "standard",
        "text": "Suppose half of one chromosome were missing from a cell. What "
                "would that cell have lost?",
        "options": [
            {"text": "Half of its 46 chromosomes, since they work in pairs",
             "correct": False,
             "why": "Losing part of one chromosome leaves the other 45 "
                    "untouched. Pairing does not make them share a fate."},
            {"text": "A run of genes — a length of instructions",
             "correct": True},
            {"text": "Half of every gene it carries, since genes run the whole "
                     "length of a chromosome",
             "correct": False,
             "why": "A gene is a short section, so a chromosome carries many "
                    "of them end to end rather than one long one."},
            {"text": "Nothing that matters, as the other chromosomes hold "
                     "copies of the same instructions",
             "correct": False,
             "why": "Each chromosome carries its own genes. The other 45 do "
                    "not duplicate what this one was carrying."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s21",
        "band": "standard",
        "text": "A student says the two chromosomes in a matching pair are "
                "identical copies of each other. What is the correction?",
        "options": [
            {"text": "They carry completely different genes, which is why a "
                     "cell needs both of them",
             "correct": False,
             "why": "If they carried different genes they would not be a "
                    "matching pair. The match is what makes them one."},
            {"text": "One of them is a working copy and the other is kept "
                     "spare in case of damage",
             "correct": False,
             "why": "Neither is a spare. Both are used, and the two arrived "
                    "from different parents rather than from a copying step."},
            {"text": "They are identical, which is exactly how a cell knows "
                     "the two belong together",
             "correct": False,
             "why": "They are matched rather than identical: one came from "
                    "each parent, carrying its own version of each gene."},
            {"text": "They carry the same genes in the same places, but may "
                     "carry different versions of them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s22",
        "band": "standard",
        "text": "The lesson gives a size for a cell, a nucleus and a "
                "chromosome, but for a gene it says only \"a section of the "
                "strand\". Why give no number?",
        "options": [
            {"text": "Because genes differ in length, so a single figure "
                     "would never be right",
             "correct": True},
            {"text": "Because a gene is too small for anybody to have measured "
                     "one yet",
             "correct": False,
             "why": "The bases are measured, and they are far smaller still. "
                    "Measurement is not what stops it."},
            {"text": "Because a gene has no length at all, being an "
                     "instruction rather than an object",
             "correct": False,
             "why": "A gene is a real length of a real molecule. It simply is "
                    "not the same length from one gene to the next."},
            {"text": "Because the length of a gene changes each time the cell "
                     "switches it on",
             "correct": False,
             "why": "Switching a gene on does not stretch or shrink it. Its "
                    "length is fixed by where it starts and ends."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s23",
        "band": "standard",
        "text": "Most of the DNA in a human cell is described as regulatory "
                "rather than instructional. What does that mean?",
        "options": [
            {"text": "Most of it is spare material with no job of any kind",
             "correct": False,
             "why": "Regulating is a job, and an important one. Calling it "
                    "spare is exactly the reading the word rules out."},
            {"text": "Most of it controls when and where genes are switched "
                     "on, rather than coding for a characteristic",
             "correct": True},
            {"text": "Most of it is used to hold the chromosome in its coiled "
                     "shape",
             "correct": False,
             "why": "Holding the coil is the proteins' job. Regulatory DNA is "
                    "about controlling genes, not about packing."},
            {"text": "Most of it belongs to other species and was picked up "
                     "along the way",
             "correct": False,
             "why": "It is the person's own DNA, inherited like the rest. "
                    "Where it came from is not what the word describes."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s24",
        "band": "standard",
        "text": "Human and chimpanzee DNA differ by about one per cent of the "
                "letters. Why does that not make the two species almost the "
                "same as each other?",
        "options": [
            {"text": "Because the one per cent was measured on a single "
                     "chromosome rather than on the whole set of them, which "
                     "is where the real difference lies",
             "correct": False,
             "why": "The figure is for the DNA as a whole. Inventing a fault "
                    "in the measurement is not needed to answer this."},
            {"text": "Because chimpanzees have 48 chromosomes and humans 46, "
                     "which is the real difference",
             "correct": False,
             "why": "Chromosome number is only how the DNA is packaged. A "
                    "potato has 48 as well and is not almost a chimpanzee."},
            {"text": "Because percentages cannot be used to compare two "
                     "different species at all",
             "correct": False,
             "why": "The comparison is a fair one and the figure is real. What "
                    "it does not tell you is how much each letter matters."},
            {"text": "Because one per cent of a very long molecule is still an "
                     "enormous number of letters, and much of it is switching",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s25",
        "band": "standard",
        "text": "Two genes are described as lying on the same chromosome. What "
                "does that tell you about them?",
        "options": [
            {"text": "They must control two characteristics that are closely "
                     "connected",
             "correct": False,
             "why": "Genes sitting near one another need have nothing to do "
                    "with each other. Position is not a subject heading."},
            {"text": "They are two lengths of the same DNA molecule",
             "correct": True},
            {"text": "They must be switched on and off together in every cell",
             "correct": False,
             "why": "Each gene is switched on or off in its own right. Sharing "
                    "a chromosome does not tie them together."},
            {"text": "One of them must be a copy of the other, made when the "
                     "chromosome formed",
             "correct": False,
             "why": "No copying is involved. They are two different sections "
                    "of the strand, each with its own sequence."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s26",
        "band": "standard",
        "text": "A student asks which of her cells holds the real copy of her "
                "DNA, with the rest holding duplicates. What is the reply?",
        "options": [
            {"text": "The first cell she ever was holds the real one, and "
                     "every later cell holds a duplicate",
             "correct": False,
             "why": "That cell divided long ago and is not around to be the "
                    "original. Every cell now carries an equally good set."},
            {"text": "The cells of the nervous system hold it, because they "
                     "last a lifetime",
             "correct": False,
             "why": "Living a long time does not make a cell's set more "
                    "genuine than a skin cell's. All of them match."},
            {"text": "Her sex cells hold it, because those are the ones that "
                     "get passed on",
             "correct": False,
             "why": "A sex cell carries half a set, so if anything it holds "
                    "less. Being passed on does not make a copy the original."},
            {"text": "No cell is the original — every cell with a nucleus "
                     "carries an identical complete copy",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s27",
        "band": "standard",
        "text": "What is the strongest reason for saying that a gene is not an "
                "object attached to a chromosome?",
        "options": [
            {"text": "Genes are far too small to be attached to anything",
             "correct": False,
             "why": "Size is not the argument. Something very small can still "
                    "be attached to something larger."},
            {"text": "A chromosome is one continuous molecule, so a gene is a "
                     "stretch of it with nothing to detach",
             "correct": True},
            {"text": "Genes are found in the cytoplasm rather than on the "
                     "chromosomes themselves",
             "correct": False,
             "why": "Genes are in the nucleus, in the chromosomes. Nothing of "
                    "the sort is kept out in the cytoplasm."},
            {"text": "A chromosome carries thousands of genes, which is too "
                     "many for them all to be attached",
             "correct": False,
             "why": "The number is not the problem. Even one attached gene "
                    "would be the wrong picture of what a gene is."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s28",
        "band": "standard",
        "text": "In a sample of cheek cells, a few show 46 clear chromosomes "
                "and most show none. Which statement about the sample is "
                "true?",
        "options": [
            {"text": "Only the cells showing chromosomes have a full set; the "
                     "others have lost theirs",
             "correct": False,
             "why": "Nothing has been lost. A cell showing no chromosomes has "
                    "the same 46 in it, spread out and far too thin to see."},
            {"text": "The cells showing none are dead, which is why their "
                     "chromosomes have broken down",
             "correct": False,
             "why": "These are ordinary living cells. Being invisible is the "
                    "normal state of a chromosome, not a sign of damage."},
            {"text": "Every cell holds 46, and only the few about to divide "
                     "show them, with the DNA coiled tight",
             "correct": True},
            {"text": "The sample must hold cells from two different people, "
                     "since one group differs from the other",
             "correct": False,
             "why": "One person's cells look like this routinely. What differs "
                    "is the moment each cell was caught at, not the donor."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s29",
        "band": "standard",
        "text": "Suppose two species turn out to have exactly the same number "
                "of chromosomes in a body cell. Does that make them closely "
                "related?",
        "options": [
            {"text": "Yes — sharing a chromosome number is what being related "
                     "means",
             "correct": False,
             "why": "Relatedness is about shared ancestry and shared sequence, "
                    "not about how many packages the DNA is divided into."},
            {"text": "Yes, but only because both are living things with cells "
                     "that have a nucleus",
             "correct": False,
             "why": "That is true of a fern with a thousand chromosomes as "
                    "well, so it explains nothing about a matching count."},
            {"text": "No — the number is how the DNA is packaged, and says "
                     "nothing at all about what it holds",
             "correct": True},
            {"text": "No, because the number of chromosomes varies so much "
                     "within one species that it cannot be compared",
             "correct": False,
             "why": "A species has its own steady number — 46 for a human, 78 "
                    "for a dog. The count is reliable; it is just not a "
                    "measure of kinship."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-s30",
        "band": "standard",
        "text": "One of the things the gene count misses is that a single gene "
                "can be read in more than one way. What does that do to the "
                "figure of twenty thousand?",
        "options": [
            {"text": "It means the number of genes has been badly "
                     "over-counted",
             "correct": False,
             "why": "The count of genes is about right. What is understated is "
                    "how much those genes between them can specify."},
            {"text": "It means the number of instructions available is larger "
                     "than the number of genes",
             "correct": True},
            {"text": "It means each gene must sit on more than one chromosome "
                     "at a time",
             "correct": False,
             "why": "A gene sits in one place on one chromosome. Being read in "
                    "several ways does not move it about."},
            {"text": "It means the twenty thousand should be divided between "
                     "the different readings",
             "correct": False,
             "why": "Dividing goes the wrong way. Several readings from one "
                    "gene make the total larger, not smaller."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-02-h12",
        "band": "harder",
        "text": "The DNA in one cell measures about two metres uncoiled, and "
                "the cell itself is 0.02 mm across. How many times longer is "
                "the DNA than the cell is wide?",
        "options": [
            {"text": "One hundred times",
             "correct": False,
             "why": "Two metres is 2000 mm, and 2000 divided by 0.02 is a "
                    "great deal more than a hundred."},
            {"text": "One thousand times",
             "correct": False,
             "why": "This would be right if the cell were 2 mm across. It is a "
                    "hundred times narrower than that."},
            {"text": "One hundred million times",
             "correct": False,
             "why": "A thousand times too large. 2000 divided by 0.02 comes to "
                    "one hundred thousand exactly."},
            {"text": "One hundred thousand times",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h13",
        "band": "harder",
        "text": "The bases along a DNA strand are about 0.0000003 mm apart. "
                "About how long is a stretch of one million bases?",
        "options": [
            {"text": "About 0.3 mm",
             "correct": True},
            {"text": "About 0.003 mm",
             "correct": False,
             "why": "A hundred times too short. A million multiplied by "
                    "0.0000003 mm comes to 0.3 mm."},
            {"text": "About 3 mm",
             "correct": False,
             "why": "Ten times too long, which is the answer you get by "
                    "dropping one of the zeros in the spacing."},
            {"text": "About 300 mm",
             "correct": False,
             "why": "A thousand times too long. A stretch of DNA 30 cm long "
                    "would need a thousand million bases, not a million."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h14",
        "band": "harder",
        "text": "A plant has 20 chromosomes in a body cell and about 30 000 "
                "genes. On average, how many genes does one of its "
                "chromosomes carry?",
        "options": [
            {"text": "About 20",
             "correct": False,
             "why": "That is the chromosome count read back as an answer. The "
                    "genes have to be shared out between the 20."},
            {"text": "About 600 000",
             "correct": False,
             "why": "This is 30 000 multiplied by 20, which gives more genes "
                    "than the plant has. Sharing out means dividing."},
            {"text": "About 30 000",
             "correct": False,
             "why": "Each chromosome carries its own genes, not a copy of all "
                    "of them. The 30 000 are spread across the 20."},
            {"text": "About 1 500",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h15",
        "band": "harder",
        "text": "With four bases to choose from at each position, how many "
                "different sequences of three bases are possible?",
        "options": [
            {"text": "12",
             "correct": False,
             "why": "This is four multiplied by three, and that is not how "
                    "choices combine. Each position has all four available."},
            {"text": "7",
             "correct": False,
             "why": "This is four added to three, which is further off still. "
                    "Four choices at three positions are multiplied."},
            {"text": "24",
             "correct": False,
             "why": "24 is the number of ways of arranging four things in a "
                    "row using each once. Here the bases may repeat."},
            {"text": "64",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h16",
        "band": "harder",
        "text": "Two people have different eye colours. Given that both carry "
                "the gene for eye colour in the same place on the same "
                "chromosome, where does the difference actually lie?",
        "options": [
            {"text": "In the order of the bases along that stretch of DNA",
             "correct": True},
            {"text": "In how many copies of that gene each person carries",
             "correct": False,
             "why": "Each carries two copies, one on each chromosome of the "
                    "pair. The number is the same for both people."},
            {"text": "In which chromosome that gene has ended up on in each "
                     "person",
             "correct": False,
             "why": "A given gene sits on the same chromosome in everybody. "
                    "Genes do not move between chromosomes."},
            {"text": "In whether the gene is present at all, since one of them "
                     "must be missing it",
             "correct": False,
             "why": "The gene for eye colour is in everybody. What differs "
                    "between two people is the version they carry."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h17",
        "band": "harder",
        "text": "A student multiplies thirty trillion cells by two metres of "
                "DNA each and says the total would stretch far beyond the Sun. "
                "Is the reasoning sound?",
        "options": [
            {"text": "No — the two metres is a total for the whole body, not "
                     "for each cell",
             "correct": False,
             "why": "The two metres is the figure for a single cell. Almost "
                    "every cell holds its own complete copy."},
            {"text": "No — you cannot add up lengths of a molecule that is "
                     "coiled",
             "correct": False,
             "why": "The two metres is already the uncoiled length, so adding "
                    "those lengths is a fair thing to do."},
            {"text": "Yes — both figures are the lesson's own, and the "
                     "multiplication is straightforward",
             "correct": True},
            {"text": "Yes, but only if the DNA of the red blood cells is "
                     "included in the count",
             "correct": False,
             "why": "Red blood cells carry no DNA at all, and leaving them out "
                    "barely dents a total that size."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h18",
        "band": "harder",
        "text": "A student proposes lifting the DNA out of one nucleus with "
                "tweezers and measuring it against a ruler to check the two "
                "metres. What is the difficulty?",
        "options": [
            {"text": "The DNA in a nucleus is far shorter than two metres "
                     "until it is stretched",
             "correct": False,
             "why": "Stretching does not add length. The molecule is two "
                    "metres long; it is folded, not compressed."},
            {"text": "There is nothing there to lift, because DNA forms only "
                     "when a cell divides",
             "correct": False,
             "why": "The DNA is in the nucleus the whole time. Division "
                    "changes how tightly it is coiled, not whether it exists."},
            {"text": "It is 46 separate molecules, each so thin that no "
                     "tweezers could find one",
             "correct": True},
            {"text": "The nucleus would have to be opened, and opening one "
                     "destroys the chromosomes inside it",
             "correct": False,
             "why": "A nucleus can be broken open and its contents studied. "
                    "The obstacle is the thinness of the strands, not the "
                    "opening."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h19",
        "band": "harder",
        "text": "Explain why changing a single base in the middle of a gene "
                "could matter at all, when the gene has thousands of them.",
        "options": [
            {"text": "Because the instruction is the order of the bases, so "
                     "one letter changed changes what is written",
             "correct": True},
            {"text": "Because losing one base leaves the chromosome one base "
                     "shorter, and length is what matters",
             "correct": False,
             "why": "Nothing here is lost — one letter is exchanged for "
                    "another, and the length is unchanged."},
            {"text": "Because a gene stops working unless all four bases "
                     "appear in equal numbers within it",
             "correct": False,
             "why": "Genes do not hold equal numbers of the four. What carries "
                    "meaning is the order, not the proportions."},
            {"text": "Because a single change spreads along the strand and "
                     "alters every base after it",
             "correct": False,
             "why": "One base changed is one base changed. Nothing runs down "
                    "the strand rewriting the rest."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h20",
        "band": "harder",
        "text": "A student says the nucleus must be the biggest part of a "
                "cell, since two metres of DNA has to fit inside it. What is "
                "wrong with that?",
        "options": [
            {"text": "The DNA is kept outside the nucleus for that very "
                     "reason, and only visits it",
             "correct": False,
             "why": "The DNA never leaves the nucleus. There is no store "
                    "elsewhere for any of it."},
            {"text": "The nucleus is about 0.006 mm in a cell of 0.02 mm, and "
                     "the DNA fits because it is so thin and coiled",
             "correct": True},
            {"text": "The nucleus holds only a small part of the DNA, with the "
                     "rest shared among neighbouring cells",
             "correct": False,
             "why": "Every cell holds its own complete two metres. Nothing is "
                    "shared out between cells."},
            {"text": "The two metres is measured after the DNA has been pulled "
                     "out and stretched thin",
             "correct": False,
             "why": "The molecule is that long already. Pulling it out only "
                    "lets it be laid end to end and measured."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h21",
        "band": "harder",
        "text": "A team reads the DNA of a liver cell and a skin cell from one "
                "person and finds no differences at all. A student says the "
                "experiment must have failed. What is the best reply?",
        "options": [
            {"text": "The student is right, since two cells doing completely "
                     "different jobs must be holding different instructions "
                     "from one another",
             "correct": False,
             "why": "That is the belief the result refutes. Both cells hold "
                    "the whole set and use different parts of it."},
            {"text": "The student is right, and the team must have read the "
                     "same cell twice by mistake",
             "correct": False,
             "why": "No mistake is needed to explain a matching result. Two "
                    "different cells from one person genuinely do match."},
            {"text": "The result shows that the liver cell had not yet "
                     "specialised when it was taken",
             "correct": False,
             "why": "A fully specialised liver cell gives the same reading. "
                    "Specialising changes use rather than content."},
            {"text": "The result is exactly what was expected: the two cells "
                     "differ in which genes are used, not in what they carry",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h22",
        "band": "harder",
        "text": "Why could the six levels — a person, a cell, a nucleus, a "
                "chromosome, a gene and the bases — never be drawn to scale "
                "together on one sheet of paper?",
        "options": [
            {"text": "Because the sizes involved differ by more than a hundred "
                     "thousand times",
             "correct": True},
            {"text": "Because a gene has no length that could be drawn on a "
                     "scale at all",
             "correct": False,
             "why": "A gene is a real length of the strand. Its size is not "
                    "fixed, but that is not what defeats the drawing."},
            {"text": "Because nobody has measured the sizes accurately enough "
                     "for a scale drawing",
             "correct": False,
             "why": "All six sizes are known. Knowing them is not the problem; "
                    "fitting them on one page is."},
            {"text": "Because the bases are too close together to be told "
                     "apart in a drawing",
             "correct": False,
             "why": "A drawing can magnify them as much as you like. The "
                    "trouble is showing them beside a person on one sheet."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h23",
        "band": "harder",
        "text": "Human chromosome 1 is several times longer than chromosome "
                "21. What would you expect of the number of genes each "
                "carries, and why?",
        "options": [
            {"text": "The same number, because every chromosome carries an "
                     "equal share of the genes",
             "correct": False,
             "why": "There is no rule sharing them out equally. Genes lie "
                    "along the strand, so a longer strand holds more room."},
            {"text": "More on chromosome 21, because shorter chromosomes pack "
                     "their genes closer together",
             "correct": False,
             "why": "Packing tightly is what a chromosome does with its whole "
                    "length. It does not squeeze extra genes in."},
            {"text": "More on chromosome 1, because a gene is a length of that "
                     "chromosome's DNA",
             "correct": True},
            {"text": "One gene each, because a chromosome is the package for a "
                     "single instruction",
             "correct": False,
             "why": "46 chromosomes against twenty thousand genes rules that "
                    "out at once. Each carries many."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h24",
        "band": "harder",
        "text": "Before 2003, serious estimates of the human gene count ran to "
                "a hundred thousand. A student says those scientists must have "
                "been careless. What is a better reading?",
        "options": [
            {"text": "They were careless, because the true figure could have "
                     "been read off the chromosome count many years "
                     "beforehand",
             "correct": False,
             "why": "The chromosome count tells you nothing about the number "
                    "of genes. There was no shortcut to the answer."},
            {"text": "The estimate followed from taking one gene, one job "
                     "seriously, and the result is what loosened that model",
             "correct": True},
            {"text": "They were guessing without evidence, so the figure meant "
                     "nothing either way",
             "correct": False,
             "why": "The estimates were reasoned from how much a body appears "
                    "to do. Being wrong is not the same as being baseless."},
            {"text": "The 2003 figure is itself unreliable, which is why the "
                     "older estimates survive",
             "correct": False,
             "why": "The older estimates did not survive. Around twenty "
                    "thousand is the figure that has held since."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h25",
        "band": "harder",
        "text": "Asking whether a nucleus contains chromosomes or DNA is "
                "compared to asking whether a library contains books or paper. "
                "What does the comparison establish?",
        "options": [
            {"text": "That the question names a real choice, and the answer to "
                     "both is the first of the two",
             "correct": False,
             "why": "There is no choice to make. A library holds books, and a "
                    "book is made of paper; both answers are true at once."},
            {"text": "That the two are not alternatives, because one of them "
                     "is what the other is made of",
             "correct": True},
            {"text": "That a nucleus is a store of separate items, as a "
                     "library is a store of separate books",
             "correct": False,
             "why": "The comparison is about the question, not about storage. "
                    "Its point is that paper and books are not rivals."},
            {"text": "That comparisons drawn from everyday life break down "
                     "when they are applied to a cell",
             "correct": False,
             "why": "This one holds up well. It is used precisely because the "
                    "same mistake is easy to make in both cases."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h26",
        "band": "harder",
        "text": "If the bases lie about 0.0000003 mm apart, roughly how many "
                "of them lie along one millimetre of DNA?",
        "options": [
            {"text": "About three thousand",
             "correct": False,
             "why": "A thousand times too few. Dividing 1 by 0.0000003 gives a "
                    "figure in the millions."},
            {"text": "About three million",
             "correct": True},
            {"text": "About three hundred",
             "correct": False,
             "why": "Far too few, by a factor of ten thousand. The spacing has "
                    "seven decimal places, which makes the count very large."},
            {"text": "About three billion",
             "correct": False,
             "why": "A thousand times too many. Three billion bases is closer "
                    "to a whole human set than to one millimetre of it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h27",
        "band": "harder",
        "text": "A student argues that two metres of DNA can only fit in a "
                "nucleus because it is broken into 46 pieces. How much of that "
                "is right?",
        "options": [
            {"text": "All of it — 46 shorter lengths take up less room than "
                     "one long one",
             "correct": False,
             "why": "Cutting something into pieces does not reduce how much "
                    "material there is. The total length is unchanged."},
            {"text": "None of it — the two metres is a single unbroken "
                     "molecule in every cell",
             "correct": False,
             "why": "It really is divided between 46 chromosomes, each its own "
                    "molecule. That part of the argument is sound."},
            {"text": "The fit is right but the number is wrong, since the DNA "
                     "is divided into 23 pieces rather than 46",
             "correct": False,
             "why": "23 is the number of pairs. A body cell carries 46 "
                    "chromosomes, and so 46 separate molecules."},
            {"text": "The 46 pieces are real, but the fit comes from the "
                     "molecule being extremely thin and tightly coiled",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h28",
        "band": "harder",
        "text": "A student suggests that a skin cell could save room by "
                "throwing away the genes it never uses, as a red blood cell "
                "throws away its nucleus. What is the objection?",
        "options": [
            {"text": "Every cell the skin cell went on to make would inherit "
                     "an incomplete set",
             "correct": True},
            {"text": "A skin cell has no room to save, since its nucleus is "
                     "already the smallest part of it",
             "correct": False,
             "why": "Room is not the issue at all. The cost is to everything "
                    "the cell's descendants would need later."},
            {"text": "Genes cannot be removed from a chromosome by any means "
                     "at all, in any cell",
             "correct": False,
             "why": "The red blood cell disposes of the lot, so removal is "
                    "clearly possible. The question is what it costs."},
            {"text": "The red blood cell keeps the genes it needs, so the "
                     "comparison does not hold in the first place",
             "correct": False,
             "why": "It keeps none of them — it loses the whole nucleus. The "
                    "comparison is fair; the consequences are what differ."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h29",
        "band": "harder",
        "text": "Books usually draw a chromosome as a neat X shape, while this "
                "lesson calls it a long thin molecule. How do the two "
                "pictures fit together?",
        "options": [
            {"text": "The X shape is what a chromosome looks like in a plant "
                     "cell, and the long thin strand is the form it takes in "
                     "an animal cell instead",
             "correct": False,
             "why": "Plants and animals package their DNA the same way. The "
                    "difference is the moment, not the kingdom."},
            {"text": "The X shape is two chromosomes of a pair lying across "
                     "each other in the nucleus",
             "correct": False,
             "why": "The two members of a pair are separate and do not lie "
                    "crossed. The shape belongs to one chromosome."},
            {"text": "The X is what the molecule looks like when it is coiled "
                     "tightly, which happens only around cell division",
             "correct": True},
            {"text": "The X is simply a symbol, and no chromosome has ever "
                     "looked anything like it",
             "correct": False,
             "why": "It is drawn from what is genuinely seen down a microscope "
                    "in a dividing cell, so it is not merely a symbol."},
        ],
        "figure": None,
    },
    {
        "id": "b10-02-h30",
        "band": "harder",
        "text": "A biologist says a human cell can be told from a chimpanzee "
                "cell by counting its chromosomes. Is the claim sound, and "
                "what does the count not tell her?",
        "options": [
            {"text": "Sound — 46 against 48 — but the count says nothing about "
                     "how alike the two sets of instructions are",
             "correct": True},
            {"text": "Sound, and it also shows that the chimpanzee carries "
                     "more genes than the human does",
             "correct": False,
             "why": "Two more chromosomes is not two more genes' worth of "
                    "anything. The count is about packaging alone."},
            {"text": "Unsound, because humans and chimpanzees have the same "
                     "number of chromosomes as each other",
             "correct": False,
             "why": "A human has 46 and a chimpanzee 48, so the counts really "
                    "do differ and can be told apart."},
            {"text": "Unsound, because chromosomes cannot be counted in a cell "
                     "under any circumstances",
             "correct": False,
             "why": "They are counted routinely in a cell caught as it starts "
                    "to divide, which is when they become visible."},
        ],
        "figure": None,
    },
]
