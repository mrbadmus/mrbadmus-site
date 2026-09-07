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
            {"text": "A small object attached to the outside of a chromosome",
             "correct": False,
             "why": "Nothing is attached. A gene is part of the chromosome "
                    "itself, the way a chapter is part of a book rather than a "
                    "bookmark in one"},
            {"text": "A section of the DNA in a chromosome, carrying the "
                     "instruction for one characteristic",
             "correct": True},
            {"text": "A whole chromosome, which is why a human body cell "
                     "contains exactly 46 of them",
             "correct": False,
             "why": "A human carries around twenty thousand genes and only 46 "
                    "chromosomes, so a gene must be far smaller than a whole "
                    "chromosome"},
            {"text": "One of the four bases, A, T, C or G",
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
            {"text": "It supplies the cell with the energy it needs to work",
             "correct": False,
             "why": "Energy comes from respiration. DNA is not a fuel — it is "
                    "the store of instructions"},
            {"text": "It carries the instructions for building and running an "
                     "organism",
             "correct": True},
            {"text": "It holds the cell's shape, like a frame inside it",
             "correct": False,
             "why": "DNA is coiled into chromosomes for storage, not for "
                    "support. Its job is to carry information"},
            {"text": "It carries the waste out of the nucleus",
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
            {"text": "So that the cell can decide which genes to keep and "
                     "which to throw away",
             "correct": False,
             "why": "Nothing is thrown away. Every cell with a nucleus keeps "
                    "the complete set; packing is about storage, not "
                    "selection"},
            {"text": "So that the instructions cannot be read by mistake",
             "correct": False,
             "why": "The instructions have to be readable — that is what they "
                    "are for. Packing is what makes a very long molecule "
                    "manageable"},
            {"text": "So that about two metres of a very thin molecule can be "
                     "stored and moved without tangling",
             "correct": True},
            {"text": "So that the DNA takes up less space by becoming shorter "
                     "and thinner",
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
            {"text": "It carries no chromosomes at all, unlike almost every "
                     "other cell in the body",
             "correct": True},
            {"text": "It carries only the genes it needs for making "
                     "haemoglobin",
             "correct": False,
             "why": "It carries none. Losing the nucleus means losing the "
                    "whole set, not keeping a useful part of it"},
            {"text": "It cannot be a living cell, since every living cell has "
                     "a nucleus",
             "correct": False,
             "why": "It is a living cell doing a demanding job. What it has "
                    "given up is the storage space its chromosomes took, in "
                    "exchange for room to carry oxygen"},
            {"text": "It reads its instructions from the cells around it "
                     "instead",
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
            {"text": "Because they are stored in the nucleus two at a time, "
                     "side by side",
             "correct": False,
             "why": "How they sit in the nucleus is not the reason. They are "
                    "called pairs because the two members of a pair match each "
                    "other"},
            {"text": "Because the two members of each pair match, carrying the "
                     "same genes, one having come from each parent",
             "correct": True},
            {"text": "Because a cell always makes a spare copy of each "
                     "chromosome in case one is damaged",
             "correct": False,
             "why": "Neither is a spare. Both are used, and the two came from "
                    "different parents rather than from a copying step"},
            {"text": "Because 46 is an even number, so the chromosomes can be "
                     "counted in twos",
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
            {"text": "Yes — 23 is half a set, so a sperm is missing half the "
                     "instructions",
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
                     "complete copy rather than the usual two",
             "correct": True},
            {"text": "No — a sperm cell has 46 like every other cell, and 23 "
                     "is the number of pairs",
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
            {"text": "Because the twenty thousand is only an estimate, and the "
                     "true number is much larger",
             "correct": False,
             "why": "The estimate is good, and its being an estimate is not "
                    "the flaw. The flaw is treating one gene and one "
                    "characteristic as a matching pair"},
            {"text": "Because some genes are switched off, so those "
                     "characteristics never appear",
             "correct": False,
             "why": "A gene switched off in one cell is switched on in "
                    "another. Switching is about where a gene is used, not "
                    "about characteristics going missing from the count"},
            {"text": "Because one gene to one characteristic is a "
                     "simplification — most characteristics take many genes, "
                     "and many genes affect several",
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
                     "many genes rather than one",
             "correct": False,
             "why": "Many genes per characteristic is true and is a separate "
                    "matter. It is not a patch for a shortage of letters, "
                    "because there is no shortage"},
            {"text": "She is right about DNA on its own, and the proteins "
                     "wound through a chromosome supply the rest",
             "correct": False,
             "why": "The proteins are packing, not information. Every "
                    "instruction is in the order of the bases"},
            {"text": "A sequence millions of bases long gives an "
                     "unimaginable number of possible orders, so four is "
                     "plenty",
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
]
