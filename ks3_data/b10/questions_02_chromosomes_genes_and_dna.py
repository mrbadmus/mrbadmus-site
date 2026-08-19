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
            {"text": "Height varies smoothly across a population, because "
                     "many genes affect it together", "correct": True},
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
]
