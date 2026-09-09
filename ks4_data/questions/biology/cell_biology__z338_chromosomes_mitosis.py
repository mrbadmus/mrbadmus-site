"""Biology · Cell biology — the MRB-338 expansion of `chromosomes-mitosis`.

One leaf only: AQA 8461 §4.1.2.1–2, the chromosome and the cell cycle. The
original twelve rows in `cell_biology.py` take the 23 pairs, the definition of
a gene, interphase as the longest stage, the haploid gamete, the 92 chromatids
after replication, gut-lining replacement, chemotherapy, strawberry runners,
building organelles before division, radiotherapy, the halving misconception
and embryo-versus-wound mitosis. This file takes what they leave: what a
chromosome physically is and where it sits, the chromatid as a named object,
cytokinesis as a stage in its own right, chromosome and chromatid counts in
named organisms, deducing a cell's position in the cycle from what it is
doing, cycle-timing arithmetic, the loss of cycle control, and the whole
misconception set met from the wrong side.

The weight follows the CONTENT. `easier` stays at eight because recall in this
leaf is a short list — one definition, one location, two names and three
one-word facts — and asking it a ninth way is the same question in new words.
The demand lives in counting (chromosomes against chromatids, before against
after, in a fruit fly, an onion, a dog, a horse and a mule), in deducing a
stage from a description, and in reasoning about what fails when control of
the cycle is lost, so `standard` and `harder` carry twenty-two each. Every
number here comes out exactly, and none of it needs a diagram: mitotic index,
doubling time and percentage of cycle are the arithmetic this biology
genuinely supplies. Differentiation, meristems and the uses of stem cells
belong to the neighbouring leaves and appear here once only, as the
mitosis-is-not-differentiation misconception.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # What a chromosome is and where it is, the chromatid as a named object,
    # the two daughter cells, cytokinesis, the build-up of organelles,
    # asexual reproduction, and when in the cycle the DNA is copied.
    {
        "id": "ks4-chromosomes-mitosis-e05",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what one chromosome is made of and what it carries.",
        "options": [
            "A single gene, wound tightly around a spool of protein",
            "A short length of protein carrying one instruction for the cell",
            "A long molecule of DNA, carrying many genes",
            "A mixture of DNA and sugar that stores energy for the nucleus",
        ],
        "correct_index": 2,
        "why": "A chromosome is one very long DNA molecule, and along its "
               "length lie many genes, each coding for a protein.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e06",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the chromosomes of a human body cell are found.",
        "options": [
            "In the cytoplasm, alongside the ribosomes that build the cell's proteins",
            "In the nucleus, kept separate from the rest of the cell",
            "In the mitochondria",
            "In the cell membrane",
        ],
        "correct_index": 1,
        "why": "Chromosomes lie inside the nucleus, which holds the genetic "
               "material of the cell.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e07",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "After a chromosome has been copied, name the two identical "
                "copies that stay joined to one another.",
        "options": [
            "Chromatids",
            "Gametes",
            "Alleles",
            "Daughter nuclei",
        ],
        "correct_index": 0,
        "why": "DNA replication produces two chromatids, held together until "
               "mitosis pulls them apart.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e08",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many cells are produced each time one cell divides "
                "by mitosis.",
        "options": [
            "One, which is then twice the size of the cell that made it",
            "Two",
            "Four",
            "Twenty-three, one for each pair of chromosomes",
        ],
        "correct_index": 1,
        "why": "Mitosis and cytokinesis divide one parent cell into two "
               "daughter cells.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e09",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the cytoplasm and cell membrane once "
                "the nucleus has divided into two.",
        "options": [
            "They are broken down and then rebuilt inside each of the new nuclei",
            "They stay as one, so the cell ends up with two nuclei in one body",
            "They divide, so that two separate daughter cells are formed",
            "They are shared out only after the two new cells have grown to full size",
        ],
        "correct_index": 2,
        "why": "Cytokinesis divides the cytoplasm and cell membranes, "
               "completing the separation into two daughter cells.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e10",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the number of ribosomes and "
                "mitochondria in a cell before it divides.",
        "options": [
            "It increases, so there are enough for both of the new cells",
            "It falls by half, because the cell no longer needs so many",
            "It stays exactly the same throughout the whole of the cell cycle",
            "It increases only in the cells of plants",
        ],
        "correct_index": 0,
        "why": "During interphase the cell grows and the number of "
               "sub-cellular structures increases, so each daughter inherits "
               "a working set.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e11",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of reproduction in which the offspring are "
                "produced by mitosis alone.",
        "options": [
            "Fertilisation",
            "Pollination",
            "Asexual reproduction",
            "Sexual reproduction",
        ],
        "correct_index": 2,
        "why": "Asexual reproduction uses mitosis only, so every offspring "
               "is genetically identical to its single parent.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e12",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the part of the cell cycle in which a cell's DNA is "
                "copied.",
        "options": [
            "During cytokinesis, as the cytoplasm divides",
            "During mitosis, as the chromosomes line up in the middle",
            "In the moments just after the two daughter cells separate",
            "Interphase, in the hours before mitosis begins",
        ],
        "correct_index": 3,
        "why": "DNA replication happens in interphase, so that mitosis has "
               "two copies of every chromosome ready to separate.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Counting in named organisms, deducing the stage from a description,
    # cycle arithmetic that comes out exactly, the causes behind the facts,
    # and one question per misconception.
    {
        "id": "ks4-chromosomes-mitosis-s05",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fruit fly body cell contains 8 chromosomes. Determine the "
                "number of chromatids in that cell once its DNA has been "
                "replicated.",
        "options": [
            "4",
            "8",
            "16",
            "32",
        ],
        "correct_index": 2,
        "why": "Replication copies each of the 8 chromosomes once, giving "
               "two chromatids each: 8 × 2 = 16.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s06",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A garden pea root tip cell contains 14 chromosomes. "
                "Determine how many chromosomes each of the two cells it "
                "produces by mitosis will contain.",
        "options": [
            "7",
            "14",
            "28",
            "56",
        ],
        "correct_index": 1,
        "why": "Mitosis gives each daughter cell a complete copy of every "
               "chromosome, so the number stays at 14.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s07",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dog body cell contains 78 chromosomes. Determine how many "
                "pairs of chromosomes this is.",
        "options": [
            "39",
            "78",
            "156",
            "23",
        ],
        "correct_index": 0,
        "why": "Chromosomes are inherited as matching pairs, so 78 ÷ 2 = 39 "
               "pairs.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s08",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A human cell contains 92 chromatids and its nuclear "
                "membrane is still intact. Deduce which part of the cell "
                "cycle it has reached.",
        "options": [
            "It has finished mitosis and is now two separate cells",
            "It is in interphase, having replicated its DNA but not yet begun to divide",
            "It is halfway through mitosis, with the chromosomes being pulled apart",
            "It is in cytokinesis, dividing its cytoplasm",
        ],
        "correct_index": 1,
        "why": "92 chromatids show the DNA has been copied, and an intact "
               "nuclear membrane shows nuclear division has not yet started.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s09",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a cell, one copy of every chromosome is being pulled "
                "towards each end of the cell. Deduce which part of the cell "
                "cycle this is.",
        "options": [
            "Mitosis",
            "DNA replication",
            "Cytokinesis",
            "The growth stage of interphase",
        ],
        "correct_index": 0,
        "why": "Separating the two copies of each chromosome to opposite "
               "ends of the cell is nuclear division itself, which is "
               "mitosis.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s10",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is growing larger and building extra ribosomes and "
                "mitochondria, and its chromosomes are not visible. Deduce "
                "the stage it is in.",
        "options": [
            "Mitosis, because the chromosomes have not yet condensed",
            "Cytokinesis, because the cell is still one whole cell",
            "Interphase, the growth stage of the cycle",
            "It has left the cycle altogether and will never divide again",
        ],
        "correct_index": 2,
        "why": "Growth and an increase in the number of sub-cellular "
               "structures happen during interphase, well before mitosis.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s11",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell cycle lasts 20 hours, and mitosis takes 1 hour of "
                "that. Calculate the percentage of the cycle spent in "
                "mitosis.",
        "options": [
            "5%",
            "20%",
            "1%",
            "10%",
        ],
        "correct_index": 0,
        "why": "1 ÷ 20 = 0.05, and 0.05 × 100 gives 5% of the cycle spent in "
               "mitosis.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s12",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One cell divides by mitosis every 20 minutes. Calculate how "
                "many cells there will be after 2 hours.",
        "options": [
            "6",
            "12",
            "64",
            "128",
        ],
        "correct_index": 2,
        "why": "Two hours allows six divisions, and the number doubles each "
               "time: 1, 2, 4, 8, 16, 32, 64.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s13",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to the daughter cells if a cell "
                "began mitosis without copying its DNA first.",
        "options": [
            "Each one would receive only some of the chromosomes, so neither would have a full set",
            "Each one would still receive 46 chromosomes, because the cell makes extra copies as it divides",
            "Only one daughter cell would form, and it would be twice the usual size",
            "Both would be perfectly normal, because a cell copies its DNA immediately after it has divided",
        ],
        "correct_index": 0,
        "why": "Replication provides two copies of every chromosome so that "
               "each new cell can be given a complete set.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s14",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the two cells made by mitosis are genetically "
                "identical to one another.",
        "options": [
            "One chromosome from each of the 23 pairs goes to each cell, so the sets match",
            "They share the same cytoplasm for a short while after they separate",
            "The genes rearrange themselves after division until the two cells match",
            "Each receives an exact copy of every chromosome",
        ],
        "correct_index": 3,
        "why": "DNA replication makes an exact copy of every chromosome, and "
               "mitosis hands one full copy to each cell.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s15",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cell that has just been produced by mitosis "
                "cannot divide again straight away.",
        "options": [
            "Its chromosomes are still joined and must be pulled apart by the next division",
            "It must first grow and copy its DNA, which takes most of the cell cycle",
            "It has to wait until the other daughter cell has finished dividing",
            "It has used up all of its genes during the division and must make a completely new set",
        ],
        "correct_index": 1,
        "why": "A new cell has to complete interphase, growing and "
               "replicating its DNA, before it is ready to divide.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s16",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a loss of control over the cell cycle leads to "
                "a tumour.",
        "options": [
            "The cells divide over and over without stopping, so a mass of cells builds up",
            "The cells swell with water until the tissue around them is pushed out of shape",
            "The cells stop dividing, so the worn-out ones are never cleared away and pile up in the tissue",
            "The cells fuse together into one very large cell that then keeps on growing",
        ],
        "correct_index": 0,
        "why": "A tumour is a mass of cells produced by division that is no "
               "longer being controlled.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s17",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation occurs in a gene that controls the cell cycle. "
                "Explain the effect this has on cell division.",
        "options": [
            "Division stops completely, because that gene is needed to start the cycle",
            "Division becomes uncontrolled, because the checks on the cycle no longer work",
            "Division still happens, but each daughter cell now receives 23 chromosomes",
            "Division carries on normally, because one gene cannot affect the cycle",
        ],
        "correct_index": 1,
        "why": "Regulatory genes hold the cycle in check, so a mutation in "
               "one can leave division running unchecked.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s18",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tumour in the lung has shed cells that have started a new "
                "growth in the liver. Name this type of tumour and the "
                "process by which it has spread.",
        "options": [
            "A benign tumour, spreading by diffusion",
            "A malignant tumour, spreading by metastasis",
            "A benign tumour, spreading by mitosis alone",
            "A malignant tumour, spreading by differentiation",
        ],
        "correct_index": 1,
        "why": "Cells that break away and start secondary growths elsewhere "
               "make the tumour malignant, and that spreading is metastasis.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s19",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the offspring of asexual reproduction are "
                "described as clones.",
        "options": [
            "They are produced by meiosis, so they carry half the parent's chromosomes",
            "They are grown from a single gene taken out of the parent organism",
            "They are identical in size and shape, though their genes are all different",
            "They are produced by mitosis, so they are genetically identical to the parent",
        ],
        "correct_index": 3,
        "why": "Asexual reproduction uses mitosis only, and mitosis copies "
               "the parent's genes exactly.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s20",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One human chromosome carries about 1000 genes. Explain what "
                "happens to those genes when that chromosome is replicated.",
        "options": [
            "The 1000 genes are shared out, 500 going to each of the two chromatids",
            "Each of the two chromatids carries a copy of all 1000 genes",
            "The number of genes doubles to 2000 on a single chromatid",
            "Only the genes that the cell happens to be using at that moment are copied",
        ],
        "correct_index": 1,
        "why": "Replication copies the whole DNA molecule, so both "
               "chromatids carry the same full set of 1000 genes.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s21",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by saying that human chromosome 7 "
                "comes as a pair.",
        "options": [
            "It carries two copies of every gene along a single chromatid",
            "It is joined to chromosome 8, and the two are always inherited together",
            "There are two copies, one inherited from each parent, carrying genes for the same characteristics",
            "There are two copies, one made by the mother's cells and one made by the father's cells after birth",
        ],
        "correct_index": 2,
        "why": "A homologous pair is two matching chromosomes, one from each "
               "parent, carrying genes for the same characteristics.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s22",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that sperm cells are made by mitosis. "
                "Explain why this is wrong.",
        "options": [
            "Sperm cells are made by mitosis, but only in the testes, so the statement is nearly right",
            "Sperm cells are not made by cell division at all; they are assembled by the ribosomes of the testis",
            "Sperm cells are made by mitosis, and it is the egg cell that is made by meiosis",
            "Sperm cells are made by meiosis, which halves the chromosome number to 23",
        ],
        "correct_index": 3,
        "why": "Gametes are made by meiosis, which halves the chromosome "
               "number; mitosis makes body cells with the full 46.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s23",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the error in the statement that a cell's DNA is "
                "copied during mitosis.",
        "options": [
            "DNA is copied during cytokinesis, while the cytoplasm is dividing into two",
            "DNA is never copied; the two daughter cells share the original molecules between them",
            "DNA is copied twice, once in interphase and again while the chromosomes separate",
            "DNA is copied during interphase, before mitosis begins",
        ],
        "correct_index": 3,
        "why": "Replication is finished in interphase, so that mitosis has "
               "two copies of every chromosome to separate.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s24",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that the cells made by mitosis are 'very "
                "similar' to the parent cell. Explain why 'identical' is the "
                "better word.",
        "options": [
            "They are the same size and shape as the parent cell, whatever their genes are",
            "They contain some of the parent's genes and some new ones of their own",
            "Their genes are exact copies, so there is no genetic difference at all",
            "They are identical only until they start to grow, and after that they differ",
        ],
        "correct_index": 2,
        "why": "Mitosis copies every chromosome exactly, so the daughter "
               "cells carry the same genes as the parent, not merely similar "
               "ones.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s25",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the cells lining the small intestine divide far "
                "more often than nerve cells do.",
        "options": [
            "They are worn away quickly and must be replaced constantly",
            "They are smaller, so they reach full size and divide sooner",
            "They contain more chromosomes than a nerve cell contains",
            "They must divide in order to absorb the products of digestion",
        ],
        "correct_index": 0,
        "why": "Gut lining cells are constantly worn away by the food "
               "passing over them, so mitosis has to replace them.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s26",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A human cell has just finished replicating its DNA. "
                "Determine the number of chromosomes it now contains.",
        "options": [
            "23",
            "46",
            "92",
            "184",
        ],
        "correct_index": 1,
        "why": "Replication doubles the DNA but not the chromosome count: "
               "there are still 46, each now made of two chromatids.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar organisms and tissues, multi-step arithmetic, comparison and
    # evaluation, and the misconception set met from the wrong side.
    {
        "id": "ks4-chromosomes-mitosis-h05",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A horse body cell has 64 chromosomes and a donkey body cell "
                "has 62. A mule grows from a horse egg fertilised by a donkey "
                "sperm. Determine the number of chromosomes in a mule body "
                "cell.",
        "options": [
            "63",
            "126",
            "64",
            "31",
        ],
        "correct_index": 0,
        "why": "Each gamete carries half its parent's number, so 32 from the "
               "horse plus 31 from the donkey gives 63.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h06",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant leaf cell contains 24 chromosomes. Determine the "
                "total number of chromosomes present in the two cells formed "
                "when one of its root tip cells completes mitosis.",
        "options": [
            "24",
            "48",
            "12",
            "96",
        ],
        "correct_index": 1,
        "why": "Each daughter cell receives a full set of 24, so the two "
               "cells hold 24 + 24 = 48 between them.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h07",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a root tip, 50 of the 1200 cells examined are in the "
                "middle of mitosis. The whole cell cycle lasts 24 hours. "
                "Estimate the time one cell spends in mitosis.",
        "options": [
            "2 hours",
            "30 minutes",
            "1 hour",
            "12 hours",
        ],
        "correct_index": 2,
        "why": "50 out of 1200 is one twenty-fourth of the cells, so mitosis "
               "takes one twenty-fourth of 24 hours, which is 1 hour.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h08",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tumour cell divides every 12 hours. Calculate how long it "
                "takes for one such cell to become 64 cells.",
        "options": [
            "64 hours",
            "768 hours",
            "32 hours",
            "72 hours",
        ],
        "correct_index": 3,
        "why": "64 is 2 multiplied by itself 6 times, so 6 divisions are "
               "needed, and 6 × 12 = 72 hours.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h09",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that, because mitosis makes genetically "
                "identical cells, every cell in the body must do the same "
                "job.",
        "options": [
            "The claim is right: cells with identical genes must always behave identically",
            "The claim is right, except in the gametes, which are the only cells made another way",
            "The claim is wrong: the cells carry the same genes, but a different selection of those genes is switched on in each",
            "The claim is wrong: mitosis gives each new cell a slightly different set of genes",
        ],
        "correct_index": 2,
        "why": "Mitosis does give every body cell the same genes, but the "
               "cells differ because different genes are switched on in "
               "each.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h10",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the number of cells and the number of "
                "chromosomes in each differ between mitosis and meiosis "
                "in a human.",
        "options": [
            "Mitosis gives four cells of 23 chromosomes; meiosis gives two cells of 46",
            "Mitosis gives two cells of 23 chromosomes; meiosis gives two cells of 46",
            "Mitosis gives four cells of 46 chromosomes; meiosis gives four cells of 23",
            "Mitosis gives two cells of 46 chromosomes; meiosis gives four cells of 23",
        ],
        "correct_index": 3,
        "why": "Mitosis keeps the full 46 and makes two cells, while meiosis "
               "halves the number to 23 and makes four gametes.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h11",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the risk of developing cancer rises as a person "
                "gets older.",
        "options": [
            "Mutations build up over a lifetime of divisions, so control of the cycle is more likely to be lost",
            "Cells divide faster as a person ages, so any tumour grows more quickly",
            "Older cells contain more chromosomes, and the extra ones cause tumours",
            "Older people have fewer cells, so each remaining cell has to divide far more often",
        ],
        "correct_index": 0,
        "why": "Every division carries a small risk of mutation, and over a "
               "lifetime the chance of damaging a control gene grows.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h12",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a drug that prevents DNA replication also stops "
                "mitosis from taking place.",
        "options": [
            "Mitosis cannot start until the cell has grown to twice its usual size",
            "The drug also dissolves the nuclear membrane, so no new nucleus can form",
            "Mitosis separates two copies of each chromosome, and without replication there is only one",
            "Mitosis needs the energy that is released while the DNA is being copied",
        ],
        "correct_index": 2,
        "why": "Mitosis has nothing to pull apart unless replication has "
               "already made two chromatids for every chromosome.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h13",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemical stops the two copies of each chromosome being "
                "pulled apart, but the cell still divides its cytoplasm. "
                "Predict what the two new cells will contain.",
        "options": [
            "Each cell gets 23 chromosomes, so both of them are haploid",
            "Both cells get a full set, because the copies separate later on their own",
            "Each cell gets half of every chromosome, cut through the middle",
            "One cell gets all of the chromosomes and the other gets none",
        ],
        "correct_index": 3,
        "why": "If the copies are never separated they all finish at one end "
               "of the cell, so one daughter receives everything and the "
               "other nothing.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h14",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that after mitosis each daughter cell "
                "holds one chromosome from each of the 23 pairs. Evaluate "
                "this claim.",
        "options": [
            "It is right: that is exactly how the number is kept at 46",
            "It is right for body cells, but wrong for cells repairing a wound",
            "It is wrong: that describes meiosis, and after mitosis each cell holds all 46 chromosomes",
            "It is wrong: after mitosis each daughter cell holds 92 chromosomes",
        ],
        "correct_index": 2,
        "why": "Mitosis gives each daughter a copy of every chromosome, all "
               "46 of them; taking one of each pair is what meiosis does.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h15",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skin cell completes one cell cycle in about three weeks, "
                "while a liver cell may take over a year. Suggest what this "
                "difference tells you about the two tissues.",
        "options": [
            "Skin cells are smaller, so they take much less time to grow to full size",
            "Liver cells contain many more chromosomes to copy, and that is what makes their cycle so long",
            "Skin cells leave out interphase altogether, and that is how they get round the cycle so quickly",
            "Skin is worn away at the surface and must be replaced far more often than liver tissue is",
        ],
        "correct_index": 3,
        "why": "How often a tissue divides matches how fast its cells are "
               "lost, and skin is rubbed away from the surface constantly.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h16",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a benign tumour can still be dangerous, even "
                "though its cells do not spread through the body.",
        "options": [
            "It can press on the organ it is growing in, such as the brain, and stop it working",
            "Its cells release chemicals that force every nearby healthy cell to divide out of control",
            "It slowly turns every cell it touches into a copy of itself",
            "It uses up the body's whole supply of chromosomes as it grows",
        ],
        "correct_index": 0,
        "why": "A benign tumour stays in one place but keeps growing, and "
               "the pressure it puts on surrounding tissue can stop an organ "
               "working.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h17",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A human cell completes DNA replication, mitosis and "
                "cytokinesis. Determine the number of chromosomes and the "
                "number of chromatids in each new cell.",
        "options": [
            "46 chromosomes and 92 chromatids",
            "46 chromosomes and 46 chromatids",
            "23 chromosomes and 46 chromatids",
            "92 chromosomes and 92 chromatids",
        ],
        "correct_index": 1,
        "why": "Once the copies have been separated each chromosome is a "
               "single chromatid again, so it is 46 and 46.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h18",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the cell cycle includes a check that the DNA "
                "has been copied correctly before mitosis starts.",
        "options": [
            "It gives the chromosomes time to line up along the middle of the cell",
            "It allows the cell to decide how many chromosomes each daughter should get",
            "It makes sure the cell has grown large enough to split cleanly in two",
            "It stops faulty copies of the DNA being passed on to the new cells",
        ],
        "correct_index": 3,
        "why": "Checking before division means a copying error is not handed "
               "on to both daughter cells and every cell made after them.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h19",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the chromosomes of a human liver cell with those of "
                "a human sperm cell.",
        "options": [
            "The liver cell has 23 and the sperm cell has 46, because a sperm carries extra",
            "Both have 46 chromosomes, but in the sperm cell they are permanently joined in pairs",
            "The liver cell has 46 in 23 pairs; the sperm cell has 23, one from each pair",
            "Both have 23, because every human cell carries the haploid number",
        ],
        "correct_index": 2,
        "why": "Body cells are diploid, with 46 chromosomes in 23 pairs, "
               "while a gamete is haploid, with one chromosome from each "
               "pair.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h20",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flatworm cut into three pieces grows into three complete "
                "worms. Suggest how the missing tissue is made and how the "
                "three worms' genes compare.",
        "options": [
            "By mitosis, and all three worms are genetically identical to the original",
            "By meiosis, so each worm carries half the genes of the original animal",
            "By mitosis, but each worm ends up with only the genes its own piece contained",
            "By growth of the existing cells alone, so no new cells are made at all",
        ],
        "correct_index": 0,
        "why": "Regrowth is mitosis, which copies the genes exactly, so all "
               "three worms are clones of the original animal.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h21",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the first few divisions after fertilisation the embryo "
                "hardly changes in size, yet its cells get smaller. Suggest "
                "why.",
        "options": [
            "Each daughter cell receives only half the chromosomes, so it needs less room",
            "The cells lose water at every division so that the embryo can stay the same size",
            "The cells are dividing faster than they are growing, so the cytoplasm is shared into ever smaller portions",
            "The cells shrink so that a greater number of them will fit inside the uterus",
        ],
        "correct_index": 2,
        "why": "These early divisions come faster than the cells can grow, "
               "so the same cytoplasm is divided among more and more cells.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h22",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the amount of DNA in a cell doubles and then "
                "halves during one turn of the cell cycle.",
        "options": [
            "Mitosis doubles it, and interphase then breaks half of it down again",
            "It doubles as the cell grows, then halves as the cell uses DNA for energy",
            "Replication in interphase doubles it, and the two daughter cells then share it out",
            "It doubles at the moment the nucleus divides in two, and halves again when the cytoplasm divides",
        ],
        "correct_index": 2,
        "why": "The DNA is copied during interphase and then split between "
               "two cells, which returns each cell to the original amount.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h23",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that mitosis creates new genes.",
        "options": [
            "The claim is wrong: mitosis copies the genes already there, and new versions arise by mutation",
            "The claim is right: every division adds a few new genes, which is how an organism grows complex",
            "The claim is right for plants, whose cells gain genes as they divide at the shoot tip",
            "The claim is wrong: mitosis destroys genes rather than creating them",
        ],
        "correct_index": 0,
        "why": "Mitosis is a copying process, so it changes nothing; new "
               "versions of a gene come from mutation.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h24",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cell X holds 46 chromosomes each made of two chromatids. "
                "Cell Y holds 46 chromosomes each made of a single "
                "chromatid. Deduce which cell has already completed mitosis.",
        "options": [
            "Cell X, because two chromatids show that a division has just finished",
            "Cell Y",
            "Neither, because both cells are still in interphase",
            "Both, because the chromatid number always returns to normal after a division",
        ],
        "correct_index": 1,
        "why": "Mitosis separates the chromatids, so a cell that has "
               "finished it has one chromatid per chromosome.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h25",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why surgery alone is less likely to cure a cancer "
                "once it has spread to other organs.",
        "options": [
            "A spreading tumour grows back within hours of being removed by the surgeon",
            "Surgery cannot be carried out on any organ other than the one where the cancer started",
            "The cancer cells stop dividing once the main tumour is taken out, so surgery is pointless",
            "New tumours have formed in several places, so the surgeon cannot cut them all out",
        ],
        "correct_index": 3,
        "why": "Once cells have spread they start growths the surgeon cannot "
               "find or reach, so removing the first tumour does not remove "
               "the disease.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h26",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heart muscle cells divide only very rarely in an adult. "
                "Suggest what this means for the heart after a heart attack "
                "has killed some of its muscle.",
        "options": [
            "The dead muscle is replaced within a few days by mitosis of the cells beside it",
            "The remaining muscle cells divide by meiosis to make up the loss",
            "The heart makes new muscle by enlarging its cells until they split apart",
            "The dead muscle is not replaced by new muscle cells",
        ],
        "correct_index": 3,
        "why": "Replacing damaged tissue depends on mitosis, so a tissue "
               "whose cells barely divide cannot rebuild what it has lost.",
    },
]
