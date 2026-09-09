"""Biology · Cell biology — the MRB-338 expansion of `eukaryotes-prokaryotes`.

One leaf only: AQA 8461 §4.1.1.1, the two cell types, what each one has and
has not got, and the scale they live at. The original twelve rows in
`cell_biology.py` take the peptidoglycan wall, the capsule, the nm-to-µm
conversion, which group is prokaryotic, the SA:V explanation, one ribosome
comparison, the mitochondria misconception, one classification, one
magnification, the protein-synthesis claim and the plasmid comparison; this
file takes everything else — the defining nucleus test, where prokaryotic DNA
actually sits, the flagellum, the shared structures, typical sizes, standard
form and the full conversion ladder, SA:V as a ratio that can be calculated
and compared, what plasmids are FOR, and the misconception set from the wrong
side.

The weight follows the CONTENT. `easier` stays at eight because recall in this
leaf is a handful of names and two sizes, and asking them a ninth way is the
same question. The demand lives in `standard` and `harder`, where a described
organism has to be classified from features that pull in different directions,
and where a length in one unit has to be turned into another and then reasoned
with — so those are the twenty-two-row bands.

Numbers stay inside this leaf's own scale-and-units material: conversions
between mm, µm and nm, standard form, orders of magnitude, and SA:V for cubes
where the arithmetic comes out exact. Magnification appears twice at most,
because that calculation belongs to `microscopy` and would be that leaf's
question wearing this leaf's slug.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The defining nucleus test, where prokaryotic DNA sits, the plasmid and
    # the flagellum, what both cell types share, two typical sizes, and one
    # standard-form conversion.
    {
        "id": "ks4-eukaryotes-prokaryotes-e05",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the feature that makes a cell eukaryotic.",
        "options": [
            "It is bigger than a prokaryotic cell, since size is what "
            "separates the two types",
            "It has a cell wall on the outside of its cell membrane",
            "Its genetic material is enclosed inside a nucleus",
            "It contains ribosomes, which prokaryotic cells do not have",
        ],
        "correct_index": 2,
        "why": "A eukaryotic cell keeps its DNA inside a membrane-bound "
               "nucleus, and that single feature is what the word means.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e06",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the main genetic material of a bacterium is "
                "found.",
        "options": [
            "Free in the cytoplasm, as one circular loop of DNA",
            "Inside a nucleus at the centre of the cell",
            "Built into the cell wall, which is what makes the wall rigid",
            "Inside the mitochondria, next to the respiratory enzymes",
        ],
        "correct_index": 0,
        "why": "A prokaryote has no nucleus, so its DNA lies loose in the "
               "cytoplasm as a single circular chromosome.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e07",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the small extra ring of DNA found in many bacteria.",
        "options": [
            "A chromosome",
            "A ribosome",
            "A flagellum",
            "A plasmid",
        ],
        "correct_index": 3,
        "why": "A plasmid is a small circular piece of DNA that sits apart "
               "from the bacterium's main loop.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e08",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one structure found in both eukaryotic and "
                "prokaryotic cells.",
        "options": [
            "A true nucleus, holding the DNA",
            "Ribosomes, where proteins are built",
            "Mitochondria, releasing energy",
            "A permanent vacuole, storing cell sap",
        ],
        "correct_index": 1,
        "why": "Ribosomes are found in every cell, prokaryotic or "
               "eukaryotic, because every cell has to build proteins.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e09",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a flagellum does for a bacterium.",
        "options": [
            "It rotates like a propeller and drives the bacterium through "
            "liquid",
            "It carries antibiotic-resistance genes from one cell to another",
            "It anchors the circular DNA to the inside of the cell wall",
            "It builds the proteins the cell needs",
        ],
        "correct_index": 0,
        "why": "A flagellum is a rotating tail, and its job is to move the "
               "bacterium along.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e10",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the typical length of a bacterial cell.",
        "options": [
            "About 20 nm, the same size as a ribosome",
            "About 0.1 mm, the same size as a grain of fine sand",
            "About 50 µm, the same size as a plant cell",
            "About 2 µm, roughly ten times smaller than an animal cell",
        ],
        "correct_index": 3,
        "why": "Bacteria are typically 1–5 µm long, about ten times smaller "
               "across than a typical animal cell.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e11",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these is never found in a prokaryotic cell.",
        "options": [
            "A cell membrane",
            "Mitochondria",
            "Cytoplasm",
            "A cell wall",
        ],
        "correct_index": 1,
        "why": "Prokaryotes have no membrane-bound organelles at all, so a "
               "mitochondrion is never among their parts.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e12",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one micrometre written in metres in standard form.",
        "options": [
            "1 × 10⁻³ m, because a micrometre is one thousandth of a metre",
            "1 × 10⁻⁹ m, because a micrometre is the same as a nanometre",
            "1 × 10⁻⁶ m",
            "1 × 10⁶ m",
        ],
        "correct_index": 2,
        "why": "There are 1 000 000 micrometres in a metre, so 1 µm is "
               "1 × 10⁻⁶ m.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Conversions applied to real cell sizes, structure linked to function,
    # unfamiliar organisms classified, and the misconception set answered
    # from the wrong side.
    {
        "id": "ks4-eukaryotes-prokaryotes-s05",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single Escherichia coli cell measures 2 µm from end to "
                "end. Determine that length in millimetres.",
        "options": [
            "0.2 mm",
            "0.002 mm",
            "2000 mm",
            "0.000002 mm",
        ],
        "correct_index": 1,
        "why": "There are 1000 µm in 1 mm, so 2 ÷ 1000 = 0.002 mm.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s06",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two ways the DNA of a bacterium differs from the "
                "DNA of a human cheek cell.",
        "options": [
            "It is made of protein rather than nucleotides, and there is far "
            "less of it",
            "It is linear and kept in a nucleus, while human DNA is circular "
            "and free in the cytoplasm",
            "It is stored inside mitochondria, and it is copied only when "
            "the cell is about to divide",
            "It is circular rather than linear, and it lies free in the "
            "cytoplasm rather than in a nucleus",
        ],
        "correct_index": 3,
        "why": "Bacterial DNA is a single circular chromosome loose in the "
               "cytoplasm, while human DNA is linear chromosomes held inside "
               "a nucleus.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s07",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why plasmids can make a population of bacteria "
                "harder to treat with antibiotics.",
        "options": [
            "A plasmid can carry a resistance gene, and copies of it pass to "
            "other bacteria",
            "A plasmid replaces the main loop of DNA as soon as an antibiotic "
            "is given",
            "A plasmid thickens the peptidoglycan cell wall so that no "
            "antibiotic molecule can cross it",
            "A plasmid is where all of the bacterium's proteins are built, "
            "so it works faster",
        ],
        "correct_index": 0,
        "why": "Plasmids often carry antibiotic-resistance genes, and "
               "bacteria can pass copies of a plasmid between cells.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s08",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium respires aerobically. Suggest how it does so "
                "with no mitochondria.",
        "options": [
            "It cannot respire at all, which is why bacteria must absorb "
            "ready-made energy from their surroundings",
            "Its plasmids take over the job that mitochondria do in our cells",
            "Respiratory enzymes work in its cytoplasm and on its cell "
            "membrane",
            "Its ribosomes carry out respiration as well as building proteins",
        ],
        "correct_index": 2,
        "why": "A prokaryote holds its respiratory enzymes in the cytoplasm "
               "and on the cell membrane instead of inside an organelle.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s09",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Yeast is a single-celled fungus whose DNA is held in a "
                "nucleus. Classify yeast.",
        "options": [
            "Prokaryotic, because a one-celled organism is always a "
            "prokaryote",
            "Prokaryotic, because it has a cell wall as a bacterium does",
            "Neither, because a fungus is not built from cells at all",
            "Eukaryotic, because its DNA is enclosed inside a membrane-bound "
            "nucleus",
        ],
        "correct_index": 3,
        "why": "Being one cell says nothing about cell type; the nucleus "
               "makes yeast eukaryotic, as all fungi are.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s10",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a virus is a kind of prokaryote. Explain why "
                "this is wrong.",
        "options": [
            "A virus is a prokaryote, but a very small one with no cell wall "
            "of its own",
            "A virus is not a cell at all, so it has no cytoplasm and no "
            "ribosomes",
            "A virus is eukaryotic, because its genetic material is enclosed "
            "inside a protein coat",
            "A virus is a prokaryote only for as long as it is inside a host "
            "cell",
        ],
        "correct_index": 1,
        "why": "Prokaryote and eukaryote both name types of cell, and a "
               "virus is not a cell at all.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s11",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium is 3 µm long. Express this length in metres in "
                "standard form.",
        "options": [
            "3 × 10⁻³ m, taking a micrometre as one thousandth of a metre",
            "3 × 10⁻⁹ m, taking a micrometre as the same as a nanometre",
            "3 × 10⁻⁶ m",
            "3 × 10⁶ m, since a metre contains a million micrometres",
        ],
        "correct_index": 2,
        "why": "1 µm is 1 × 10⁻⁶ m, so 3 µm is 3 × 10⁻⁶ m.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s12",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to a cell's surface area to volume "
                "ratio as the cell grows larger.",
        "options": [
            "It decreases, because the volume increases faster than the "
            "surface area",
            "It increases, because a larger cell has a much larger outer "
            "surface area",
            "It stays the same, because the surface and the volume grow in "
            "step",
            "It falls only if the cell changes shape as it grows",
        ],
        "correct_index": 0,
        "why": "Volume grows with the cube of the length while surface area "
               "grows with the square, so the ratio falls as a cell enlarges.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s13",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a large animal needs a circulatory system when "
                "a single bacterium does not.",
        "options": [
            "A bacterium has no need for oxygen, so nothing has to be "
            "carried to it",
            "A large animal has a low surface area to volume ratio, so "
            "diffusion alone is too slow",
            "A bacterium has a low surface area to volume ratio, so "
            "substances reach its centre quickly",
            "A large animal has a high surface area to volume ratio, so it "
            "loses substances too fast",
        ],
        "correct_index": 1,
        "why": "A big organism has a small surface relative to its volume "
               "and long diffusion distances, so it needs a transport system.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s14",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterium bursts when a drug stops it "
                "building its cell wall.",
        "options": [
            "The wall holds the loop of circular DNA in place, and the DNA "
            "escapes without it",
            "The wall stores all of the cell's water, so that store floods "
            "out the moment the wall goes",
            "The wall carries out respiration, so the cell runs out of "
            "energy and splits open",
            "The wall supports the cell, so without it the membrane cannot "
            "resist the pressure inside",
        ],
        "correct_index": 3,
        "why": "A bacterial cell wall gives the cell its shape and strength, "
               "resisting the outward pressure of the cytoplasm.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s15",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one advantage to a bacterium of having a capsule.",
        "options": [
            "It allows the bacterium to swim towards a source of food",
            "It carries the extra genes a bacterium needs before it can divide",
            "It protects the cell from attack and helps it stick to surfaces",
            "It provides the enzymes the bacterium uses to digest its food",
        ],
        "correct_index": 2,
        "why": "A capsule is a slimy outer layer that protects the bacterium "
               "and helps it attach to surfaces.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s16",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the group of structures that eukaryotic and "
                "prokaryotic cells both possess.",
        "options": [
            "Cell membrane, cytoplasm and ribosomes",
            "Nucleus, cytoplasm and ribosomes",
            "Cell membrane, mitochondria and cytoplasm",
            "Cell wall, chloroplasts and cell membrane",
        ],
        "correct_index": 0,
        "why": "Every cell has a membrane, cytoplasm and ribosomes; only "
               "eukaryotes add a nucleus and other membrane-bound organelles.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s17",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A human cheek cell measures 20 µm across. Calculate how "
                "many bacteria of 2 µm length would span it, laid end to "
                "end.",
        "options": [
            "2",
            "100",
            "1000",
            "10",
        ],
        "correct_index": 3,
        "why": "Both lengths are already in micrometres, so 20 ÷ 2 = 10.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s18",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that bacteria have no genetic material "
                "because they have no nucleus. Correct this statement.",
        "options": [
            "Bacteria have genetic material only while a plasmid is present "
            "in the cell",
            "Bacteria do have DNA; it is simply not enclosed in a nucleus",
            "Bacteria have genetic material, but it is made of protein "
            "instead of DNA",
            "Bacteria take up genetic material from their food as they grow",
        ],
        "correct_index": 1,
        "why": "A prokaryote has DNA, as every living cell must; the "
               "difference is only that it is not packaged inside a nucleus.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s19",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what the ribosomes of a bacterium do, and how they "
                "compare with human ribosomes.",
        "options": [
            "They build proteins, and they are smaller than the ribosomes in "
            "a human cell",
            "They release energy in respiration, and they are the same size "
            "as ours",
            "They store the cell's DNA, and they are larger than the "
            "ribosomes in a human cell",
            "They control what enters the cell, and they are the same size "
            "as ours",
        ],
        "correct_index": 0,
        "why": "Ribosomes build proteins in every cell; prokaryotic "
               "ribosomes do the same job but are smaller than ours.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s20",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one advantage of keeping DNA inside a nucleus "
                "rather than loose in the cytoplasm.",
        "options": [
            "It makes the DNA circular, which is a more stable shape for a "
            "long molecule",
            "It removes the need for ribosomes, since the nucleus builds the "
            "proteins itself",
            "It protects the DNA and allows its activity to be controlled "
            "closely",
            "It allows the cell to divide far more quickly than any "
            "prokaryote can divide",
        ],
        "correct_index": 2,
        "why": "The nuclear membrane keeps DNA separate from the rest of the "
               "cell, protecting it and allowing gene activity to be "
               "regulated.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s21",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil measures a bacterium as 3 µm but records it as "
                "3 mm. Determine how many times too large the record is.",
        "options": [
            "10 times too large",
            "1000 times too large",
            "100 times too large",
            "1 000 000 times too large",
        ],
        "correct_index": 1,
        "why": "1 mm is 1000 µm, so writing mm in place of µm multiplies the "
               "value by 1000.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s22",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is 50 µm across and contains a nucleus, "
                "chloroplasts and a cell wall. Classify it.",
        "options": [
            "A prokaryotic cell, because only prokaryotes are built with a cell wall",
            "A prokaryotic cell, because 50 µm is a normal bacterial size",
            "A eukaryotic animal cell, because it has a nucleus",
            "A eukaryotic plant cell, because it has a nucleus and "
            "chloroplasts",
        ],
        "correct_index": 3,
        "why": "The nucleus makes it eukaryotic, and chloroplasts alongside "
               "a cell wall make it a plant cell rather than an animal one.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s23",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An organism's cells are 1.5 µm long, have no nucleus and "
                "contain plasmids. Classify them.",
        "options": [
            "Prokaryotic, because the DNA is not enclosed in a nucleus",
            "Eukaryotic, because plasmids are only ever found in eukaryotic "
            "cells",
            "Prokaryotic, because plasmids are what define a prokaryotic cell",
            "Eukaryotic, because 1.5 µm is far too small for a bacterium",
        ],
        "correct_index": 0,
        "why": "The absence of a nucleus is what makes a cell prokaryotic; "
               "the plasmids and the small size fit, but the nucleus is the "
               "test.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s24",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A colony of bacteria measures 0.5 mm across. Determine "
                "this width in micrometres.",
        "options": [
            "5 µm",
            "50 µm",
            "500 µm",
            "500 000 µm",
        ],
        "correct_index": 2,
        "why": "There are 1000 µm in 1 mm, so 0.5 × 1000 = 500 µm.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s25",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the size and the complexity of a prokaryotic cell "
                "with those of a eukaryotic cell.",
        "options": [
            "Prokaryotes are larger and more complex, which is why they came "
            "first",
            "The two are the same size, but a prokaryote holds more "
            "organelles inside it",
            "Prokaryotes are larger but simpler, since a bigger cell needs "
            "fewer parts",
            "Prokaryotes are smaller and simpler, with no membrane-bound "
            "organelles",
        ],
        "correct_index": 3,
        "why": "Prokaryotic cells are around ten times smaller across and "
               "hold no membrane-bound organelles at all.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s26",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a bacterium can copy its genetic material far "
                "faster than a human cell can.",
        "options": [
            "It has no genetic material to copy until a plasmid enters the "
            "cell",
            "It has one small circular chromosome, not many long linear ones",
            "It copies its DNA inside its mitochondria, which work very "
            "quickly",
            "Its nucleus is smaller, so there is less distance for the "
            "copying to cover",
        ],
        "correct_index": 1,
        "why": "A prokaryote has a single small circular chromosome to copy, "
               "while a human cell must copy 46 long linear ones.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # SA:V calculated and compared, standard form reasoned with rather than
    # recited, magnification rearranged, and unfamiliar organisms and drugs
    # used to force the nucleus test to be applied rather than remembered.
    {
        "id": "ks4-eukaryotes-prokaryotes-h05",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium is shaped like a cube 3 µm along each edge. "
                "Determine its surface area to volume ratio.",
        "options": [
            "1:1, since the surface area and the volume are both 27",
            "6:1, using an edge length of 1 µm instead of 3 µm",
            "1:2, dividing the volume by the surface area",
            "2:1",
        ],
        "correct_index": 3,
        "why": "Surface area is 6 × 3 × 3 = 54 µm² and volume is "
               "3 × 3 × 3 = 27 µm³, so 54 ÷ 27 gives 2:1.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h06",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two cube-shaped cells have sides of 2 µm and 4 µm. "
                "Determine which has the greater surface area to volume "
                "ratio, and by how much.",
        "options": [
            "The 2 µm cell, whose ratio of 3:1 is twice the 4 µm cell's "
            "1.5:1",
            "The 4 µm cell, whose ratio of 6:1 is four times the 2 µm cell's "
            "1.5:1",
            "The 4 µm cell, because it has the larger total surface area",
            "Neither, because the ratio comes out the same for cubes of any "
            "size",
        ],
        "correct_index": 0,
        "why": "For a cube the ratio is 6 ÷ side, so 6 ÷ 2 = 3:1 and "
               "6 ÷ 4 = 1.5:1 — twice as large for the smaller cube.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h07",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium is 2 × 10⁻⁶ m long and an animal cell is "
                "4 × 10⁻⁵ m across. Determine how many times longer the "
                "animal cell is.",
        "options": [
            "2 times longer",
            "2000 times longer",
            "20 times longer",
            "200 times longer",
        ],
        "correct_index": 2,
        "why": "(4 × 10⁻⁵) ÷ (2 × 10⁻⁶) = 2 × 10¹ = 20, so the animal cell "
               "is 20 times longer.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h08",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drawing of a bacterium is 60 mm long at a magnification "
                "of ×20 000. Calculate the real length of the bacterium.",
        "options": [
            "0.3 µm",
            "3 µm",
            "30 µm",
            "300 µm",
        ],
        "correct_index": 1,
        "why": "Actual size is image ÷ magnification, so 60 ÷ 20 000 = "
               "0.003 mm, which is 3 µm.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h09",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A eukaryotic cell is 10 times wider than a bacterium of the "
                "same shape. Determine how many times greater its volume is.",
        "options": [
            "1000 times greater",
            "10 times greater",
            "100 times greater",
            "30 times greater",
        ],
        "correct_index": 0,
        "why": "Volume scales with the cube of the length, and 10³ = 1000.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h10",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a bacterium is simply a very small "
                "animal cell.",
        "options": [
            "Correct, because both keep their DNA in a nucleus and both "
            "respire using aerobic enzymes",
            "Correct, because the only real difference between them is their "
            "size",
            "Incorrect, because a bacterium has no nucleus and no "
            "membrane-bound organelles",
            "Incorrect, because a bacterium contains no DNA and no ribosomes "
            "of any kind",
        ],
        "correct_index": 2,
        "why": "Size is only part of it: a bacterium is a different kind of "
               "cell, with no nucleus and no membrane-bound organelles.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h11",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital finds that resistance to one antibiotic spreads "
                "between different species of bacteria. Suggest how.",
        "options": [
            "Each species mutates in the same way at the same time by chance",
            "The antibiotic alters the main chromosome of every bacterium it "
            "meets",
            "The bacteria pass ribosomes to one another, and resistance is "
            "built in the ribosome",
            "Plasmids carrying the resistance gene are passed from one "
            "bacterium to another",
        ],
        "correct_index": 3,
        "why": "Plasmids are small rings of DNA that bacteria can transfer "
               "between cells, carrying resistance genes with them.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h12",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Penicillin stops bacteria building peptidoglycan. Explain "
                "why it does not damage human cells.",
        "options": [
            "Human cells build peptidoglycan more slowly, so the drug has no "
            "time to act",
            "Human cells have no cell wall, so there is no peptidoglycan for "
            "it to attack",
            "Human cells build their walls from cellulose, which penicillin "
            "cannot break",
            "Human cells are eukaryotic, so penicillin cannot cross their "
            "nuclear membrane",
        ],
        "correct_index": 1,
        "why": "Animal cells have no cell wall at all, so a drug that blocks "
               "cell-wall building has nothing to act on in them.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h13",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some antibiotics work by binding to bacterial ribosomes. "
                "Suggest why a human cell is not harmed.",
        "options": [
            "Human cells have no ribosomes, because their proteins are built "
            "in the nucleus",
            "Human ribosomes are protected inside mitochondria, where the "
            "drug cannot reach",
            "Human ribosomes are a different size, so the drug does not bind "
            "to them",
            "Human cells are larger, so the same dose of drug is spread far "
            "more thinly",
        ],
        "correct_index": 2,
        "why": "Prokaryotic ribosomes are smaller than eukaryotic ones, so a "
               "drug shaped to fit a bacterial ribosome does not fit ours.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h14",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microbe is 1.5 µm long, has a wall that is not "
                "peptidoglycan, and keeps its DNA as a circular loop in the "
                "cytoplasm. Classify it.",
        "options": [
            "Prokaryotic, because its genetic material is not enclosed in a "
            "nucleus",
            "Eukaryotic, because a wall that is not peptidoglycan must be a plant wall",
            "Eukaryotic, because only a eukaryote keeps its DNA loose in the cytoplasm",
            "Prokaryotic, because peptidoglycan is what defines a prokaryotic cell",
        ],
        "correct_index": 0,
        "why": "The defining test is whether the DNA is enclosed in a "
               "nucleus, and the chemistry of the wall does not decide it.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h15",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that any cell with a cell wall must be "
                "prokaryotic.",
        "options": [
            "Correct, because a cell wall is one of the features that "
            "defines a prokaryote",
            "Incorrect, because plant and fungal cells are eukaryotic and "
            "have cell walls",
            "Incorrect, because prokaryotes are the only cells that never "
            "have a cell wall",
            "Correct, because a eukaryotic cell is held in shape by its "
            "cytoskeleton instead",
        ],
        "correct_index": 1,
        "why": "Plant and fungal cells have walls and a nucleus, so a wall "
               "says nothing about whether a cell is prokaryotic.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h16",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant cell is 100 µm across and a bacterium is 1 µm long. "
                "State the difference between them as an order of magnitude.",
        "options": [
            "One order of magnitude",
            "Three orders of magnitude",
            "Four orders of magnitude",
            "Two orders of magnitude",
        ],
        "correct_index": 3,
        "why": "100 ÷ 1 = 100, which is 10², so the plant cell is two orders "
               "of magnitude wider.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h17",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to a bacterium that loses its plasmid "
                "but keeps its main loop of DNA.",
        "options": [
            "It survives, but loses any extra characteristic the plasmid's "
            "genes gave it",
            "It dies at once, because the plasmid holds the genes it needs "
            "in order to respire",
            "It survives unchanged, because a plasmid carries no genes of "
            "any kind",
            "It survives, but can no longer build any of the proteins that "
            "it needs in order to grow",
        ],
        "correct_index": 0,
        "why": "Plasmids are not essential for survival, but they carry "
               "extra genes such as those for antibiotic resistance.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h18",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a single cell cannot keep growing larger "
                "without limit.",
        "options": [
            "Its cell membrane would eventually stop being able to hold any "
            "shape at all",
            "Its DNA would run out, because one chromosome can control only "
            "so much cytoplasm",
            "Its surface area to volume ratio would fall until diffusion "
            "could no longer supply it",
            "Its ribosomes would be too far apart to pass proteins from one "
            "to the next",
        ],
        "correct_index": 2,
        "why": "As a cell grows, volume rises faster than surface area, so "
               "the membrane can no longer supply the inside by diffusion.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h19",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cell A is 3 µm long with no internal membranes. Cell B is "
                "25 µm long with membrane-bound compartments. Deduce which "
                "is prokaryotic.",
        "options": [
            "Cell B, because membrane-bound compartments are a prokaryotic "
            "feature",
            "Cell A, because it is small and has no membrane-bound "
            "organelles",
            "Both, because neither description mentions a nucleus by name",
            "Neither, because size alone can never decide the type of a cell",
        ],
        "correct_index": 1,
        "why": "Prokaryotes are the small cells with no internal membranes "
               "at all, so Cell A is the prokaryote.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h20",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil converts 5 µm into metres and writes 5 × 10⁻³ m. "
                "Identify the error.",
        "options": [
            "They should have written 5 × 10⁻³ mm, since micro is the prefix "
            "meaning one thousandth",
            "There is no error, because 1 µm really is 1 × 10⁻³ m, as a "
            "micrometre is a thousandth",
            "They have used the conversion for nanometres instead, so the answer "
            "is far too small",
            "They have used the millimetre conversion, so the answer is a "
            "thousand times too large",
        ],
        "correct_index": 3,
        "why": "1 µm is 1 × 10⁻⁶ m, so 5 µm is 5 × 10⁻⁶ m; 10⁻³ is the "
               "conversion for millimetres.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h21",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some bacteria photosynthesise. Evaluate the claim that this "
                "is impossible without chloroplasts.",
        "options": [
            "The claim is right, so those organisms must in fact be "
            "eukaryotic protists",
            "The claim is right, because photosynthesis can only ever happen "
            "in a chloroplast",
            "The claim is wrong: their pigments sit on folded membranes in "
            "the cytoplasm",
            "The claim is wrong, because bacteria carry chloroplasts inside "
            "their plasmids",
        ],
        "correct_index": 2,
        "why": "Photosynthetic bacteria hold their pigments on membranes "
               "folded into the cytoplasm rather than inside a chloroplast.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h22",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate how many bacteria, each 1 µm long, would fit end "
                "to end along a line 0.1 mm long.",
        "options": [
            "100 bacteria",
            "10 bacteria",
            "1000 bacteria",
            "0.1 of a bacterium",
        ],
        "correct_index": 0,
        "why": "0.1 mm is 100 µm, and 100 ÷ 1 = 100 bacteria.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h23",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium holds one circular chromosome and three "
                "plasmids. Determine how many separate DNA molecules it "
                "contains.",
        "options": [
            "One, because the plasmids are all joined onto the chromosome",
            "Three",
            "Two, because the plasmids together count as a single unit",
            "Four",
        ],
        "correct_index": 3,
        "why": "The chromosome and each plasmid are separate rings of DNA, "
               "so 1 + 3 = 4 molecules.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h24",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a bacterium and a human obtain the oxygen their "
                "cells need.",
        "options": [
            "The bacterium uses a flagellum to draw oxygen in; the human "
            "uses lungs and blood",
            "Oxygen diffuses straight across the bacterium's surface; a "
            "human needs lungs and blood",
            "Both rely on diffusion alone, because oxygen molecules are "
            "extremely small",
            "The bacterium makes its own oxygen inside itself; a human must "
            "take it from the air",
        ],
        "correct_index": 1,
        "why": "A bacterium's high surface area to volume ratio lets "
               "diffusion supply it directly, while a human needs exchange "
               "surfaces and a transport system.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h25",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterium can complete a whole cycle of "
                "growth and division in about 20 minutes.",
        "options": [
            "It has no DNA to copy, so dividing is little more than "
            "splitting in two",
            "It has a low surface area to volume ratio, which keeps its "
            "contents tightly concentrated",
            "It is small and simple, with a high surface area to volume "
            "ratio and one chromosome",
            "It has many mitochondria, so it can release the energy for "
            "division very quickly",
        ],
        "correct_index": 2,
        "why": "A small simple cell absorbs nutrients rapidly across its "
               "large relative surface and has only one short chromosome to "
               "copy.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h26",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newly discovered microbe must be classified. Determine "
                "the single feature that settles whether it is prokaryotic.",
        "options": [
            "Whether its DNA is enclosed within a membrane",
            "Whether it is under ten micrometres wide",
            "Whether it has a cell wall around its cell membrane",
            "Whether it is able to move using a tail-like structure",
        ],
        "correct_index": 0,
        "why": "Prokaryote and eukaryote are defined by the absence or "
               "presence of a nucleus, not by size, wall or movement.",
    },
]
