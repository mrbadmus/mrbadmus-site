# -*- coding: utf-8 -*-
"""Chromosomes, genes and DNA, in the lean shape. Spec table: docs/lessons/wave2/ks3-chromosomes-genes-and-dna.md."""

LESSON = {
    "slug": "chromosomes-genes-and-dna",
    "start": {
        "setup": "Uncoil the DNA from one of your cells, and it is about two metres long.",
        "question": "If you had to guess, how does two metres of DNA fit inside one tiny nucleus?",
        "options": [
            ("It is coiled up tightly",
             "Yes. DNA is very thin, and it is coiled up tightly into chromosomes."),
            ("Most of it is kept elsewhere",
             "All two metres are inside the nucleus. DNA is very thin and tightly coiled."),
        ],
        "answer": 0,
    },
    "words": ["DNA", "double helix", "chromosome", "gene"],
    "word_defs": {
        "DNA": "The chemical that carries the genetic code. It is found in the nucleus.",
        "double helix": "The shape of DNA: two strands twisted round each other.",
        "chromosome": "One long DNA molecule, coiled up tightly. It is found in the nucleus.",
        "gene": "A section of DNA that carries the code for one characteristic.",
    },
    "knowledge": [
        {"kind": "card", "title": "DNA, the code for life",
         "body": ["DNA is a chemical found in the nucleus of a cell.",
                  "It carries the instructions for building and running an organism.",
                  "These instructions are called the genetic code.",
                  "All living organisms have DNA."]},
        {"kind": "card", "title": "The shape of DNA",
         "body": [{"figure": "b10-double-helix"},
                  "A DNA molecule is made of two long strands.",
                  "The strands twist round each other. This shape is called a double helix.",
                  "Pairs of bases join the two strands, like the rungs of a ladder.",
                  "There are four bases, called A, T, C and G.",
                  "A always pairs with T. C always pairs with G.",
                  "The order of the bases along the DNA is the code."]},
        {"kind": "card", "title": "From nucleus to base",
         "body": [{"figure": "b10-nucleus-to-base"},
                  "The nucleus holds the chromosomes.",
                  "Each chromosome is one long DNA molecule, coiled up tightly.",
                  "A gene is a section of the DNA in a chromosome.",
                  "Each gene carries the code for one characteristic, such as blood group.",
                  "A chromosome is like a book. A gene is a chapter. The bases are the letters."]},
        {"kind": "reveal", "title": "Largest to smallest",
         "cols": ["What it is", "How many"],
         "rows": [
             ("Nucleus", "The part of the cell that holds the chromosomes.", "One in most cells"),
             ("Chromosome", "One long DNA molecule, coiled up tightly.", "46 in a human body cell"),
             ("Gene", "A section of DNA that codes for one characteristic.",
              "About 20,000 in a human"),
             ("Base", "One of four chemical units: A, T, C or G.", "Billions in each cell"),
         ]},
        {"kind": "card", "title": "Chromosomes come in pairs",
         "body": ["A human body cell has 46 chromosomes, in 23 pairs.",
                  "One chromosome of each pair came from your mother.",
                  "The other came from your father.",
                  "So you have two copies of most of your genes."]},
        {"kind": "card", "title": "Every cell has the full set",
         "body": ["Every body cell with a nucleus has a full set of your chromosomes.",
                  "So a cell in your foot has the genes for eye colour too.",
                  "Each cell only uses the genes it needs. The others are switched off.",
                  "Red blood cells have no nucleus, so they have no DNA."]},
        {"kind": "card", "title": "Why your DNA is yours",
         "body": ["Apart from identical twins, everyone has a different order of bases.",
                  "So one cell with a nucleus can identify a person.",
                  "A sample can be damaged, or mixed with someone else's DNA."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Chromosomes, genes and DNA are three different things in the nucleus.",
              "A chromosome is coiled DNA. A gene is a section of that DNA.", "GENE-03"),
             ("Only the cells that need a gene contain it.",
              "Every body cell with a nucleus has every gene. Only some are switched on.", "GENE-04"),
             ("A gene is bigger than a chromosome.",
              "A chromosome carries many genes."),
             ("DNA is a single strand.",
              "DNA has two strands, twisted into a double helix."),
         ]}]},
    ],
    "key_fact": "DNA is a chemical with a double helix shape that carries the genetic code. "
                "It is coiled into chromosomes in the nucleus. "
                "A gene is a section of DNA that codes for one characteristic.",
    "deeper": [
        {"kind": "card", "title": "Sperm and egg cells",
         "body": ["A sperm or egg cell has 23 chromosomes, one from each pair.",
                  "When they join, the new cell has 46 again."]},
        {"kind": "card", "title": "Chromosome numbers",
         "body": ["A human has 46 chromosomes. A dog has 78. A potato has 48.",
                  "More chromosomes does not mean a more complex organism."]},
    ],
    "try": None,
    "tutor_body": "Want to check how DNA, genes and chromosomes fit together?",
    "ks4_becomes": "The genome, alleles, and how the order of bases codes for proteins.",
    "figures": [
        {"id": "b10-double-helix", "kind": "diagram", "status": "drawn", "art": "b10-double-helix",
         "title": "The double helix of DNA",
         "desc": "Two dark strands twist round each other down the page. Rungs join the two strands. "
                 "Four of the widest rungs carry base letters. They read A with T, C with G, T with A "
                 "and G with C. Labels say: two strands, twisted together; bases pair across, A with T, "
                 "C with G. The lower part of the molecule is orange, both strands and rungs. A bracket "
                 "beside it says a gene is one section of the DNA.",
         "caption": "DNA is two strands twisted into a double helix, joined by pairs of bases.",
         "data": {"pairs": [["A", "T"], ["C", "G"], ["T", "A"], ["G", "C"]]}},
        {"id": "b10-nucleus-to-base", "kind": "diagram", "status": "drawn", "art": "b10-nucleus-to-base",
         "title": "Chromosomes, genes and DNA: one strand at five magnifications",
         "desc": "Five numbered frames, one under another. Each frame is a close-up of a dashed ring "
                 "in the frame above. A widening band joins each ring to the next frame. Frame 1 is a cell, "
                 "0.02 mm across. One orange fleck in its nucleus is the strand we follow. Frame 2 is that "
                 "nucleus, 0.006 mm across. It holds 46 grey chromosomes in 23 pairs. One of them is orange. "
                 "Frame 3 is that chromosome, 0.002 mm long. It is an orange strand coiled round "
                 "proteins, unwinding at the bottom. Labels say proteins and coiled DNA. Frame 4 is the "
                 "unwound strand: two orange backbones with orange rungs between them. A bracket marks one "
                 "length as one gene. Frame 5 shows four rungs of that length. Each is a pair of orange "
                 "lettered boxes. They read A with T, C with G, T with A and G with C. The bases are "
                 "0.0000003 mm apart. A key says orange is the one DNA molecule we follow. Grey is the "
                 "other chromosomes, which are DNA too.",
         "caption": "One DNA molecule, from the nucleus down to its bases.",
         "data": {}},
    ],
    "figure_caption": {
        "b10-double-helix": None,
    },
    "ladder_stem": {
        "explain": "A student says \"the nucleus contains chromosomes and DNA and genes\". "
                   "Rewrite the sentence so it is correct. Explain how the four things are related.",
        "produce": "A single cheek cell left on a glass can identify a person. Explain what makes this "
                   "possible. Use where genetic information is stored and which cells carry it.",
    },
    "ladder_ticks": [
        ["Says each chromosome is a long DNA molecule, coiled up — not a separate thing from DNA.",
         "Says each chromosome is one long DNA molecule, coiled up tightly."],
        ["Makes clear the three are not three separate contents of the nucleus but one structure at three levels.",
         "Makes clear they are one structure, seen at different sizes."],
        ["Uses a comparison or an ordering that shows the nesting clearly — for example largest to smallest, or a book, chapter and letters.",
         "Orders them largest to smallest, or compares them to a book, chapters and letters."],
        ["Says a single cell is enough because the whole instruction set is present in it, not just part of it.",
         "Says one cell is enough, as it holds the whole set of instructions."],
        ["Identifies a limitation — identical twins share their DNA, or the sample may be contaminated or degraded, or a red blood cell would not work because it has no nucleus.",
         "Gives a limit, such as identical twins sharing DNA, or a damaged sample."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "The nucleus holds the chromosomes, so it is the largest.",
            2: "A gene is a section of a chromosome, so it is smaller.",
            3: "The nucleus holds everything else, so it comes first.",
        },
        "apply": {
            1: "Every body cell with a nucleus has every gene. Genes are not sorted by organ.",
            2: "Everyone has the eye colour genes. People differ in which versions they carry.",
            3: "Genes cannot move. They are sections of the chromosomes in each nucleus.",
        },
    },
}
