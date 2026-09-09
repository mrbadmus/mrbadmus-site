"""Biology · Cell biology — the MRB-338 expansion of `animal-plant-cells`.

One leaf only: AQA 8461 §4.1.1.2, the sub-cellular structures of animal and
plant cells and what each one does. The original twelve rows in
`cell_biology.py` take the nuclear envelope, methylene blue, the cristae, the
wall/membrane ordering, palisade chloroplast counts, wilting, a root cell's
missing chloroplasts, cytoplasm-versus-membrane, the onion bulb, trapped air
bubbles, mitochondria-rich cells and the bursting animal cell. This file takes
what they leave: the functions of the cytoplasm, ribosomes and nucleus in their
own right, the wall/membrane permeability split, the whole misconception set
(wall = membrane, "plants do not respire", animal vacuoles, ribosomes as
membrane-bound organelles, mitochondria "producing" energy), the light
microscope's limits, and the scale arithmetic — mm to µm to nm, and
magnification rearranged — that RP1 rests on.

The weight follows the CONTENT. `easier` stays at eight because straight
recall here is nine named structures and one unit conversion, and asking the
same structure a second way is the same question; the demand lives in
`standard`, where a structure has to be inferred from what a cell is doing,
and in `harder`, where an inventory has to be read backwards, a claim
evaluated, or a magnification rearranged through two unit changes.

Numbers come out exact: every conversion is a clean power of ten, and every
magnification divides without a remainder.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The five functions the original four rows never state (cytoplasm,
    # ribosome, wall material, vacuole contents, chlorophyll's home), the
    # nucleus's control role, the membrane's defining property, and the one
    # unit conversion the rest of the leaf's arithmetic rests on.
    {
        "id": "ks4-animal-plant-cells-e05",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where in a cell most of its chemical reactions take "
                "place.",
        "options": [
            "In the nucleus, alongside the chromosomes",
            "Inside the phospholipid layer of the cell membrane",
            "In the cytoplasm",
            "In the permanent vacuole, among the cell sap",
        ],
        "correct_index": 2,
        "why": "The cytoplasm is a watery gel holding the cell's dissolved "
               "enzymes, and most of its chemical reactions happen there.",
    },
    {
        "id": "ks4-animal-plant-cells-e06",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the structure at which amino acids are joined "
                "together to build a protein.",
        "options": [
            "A ribosome",
            "A mitochondrion, using the energy released by respiration",
            "The nuclear envelope, at one of its pores",
            "A chloroplast, using the glucose made in photosynthesis",
        ],
        "correct_index": 0,
        "why": "Ribosomes are the site of protein synthesis, joining amino "
               "acids in the order the cell's DNA specifies.",
    },
    {
        "id": "ks4-animal-plant-cells-e07",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance that a plant cell wall is made of.",
        "options": [
            "Protein",
            "Cellulose",
            "Phospholipid",
            "Starch",
        ],
        "correct_index": 1,
        "why": "A plant cell wall is built from cellulose fibres, which make "
               "it rigid enough to hold the cell's shape.",
    },
    {
        "id": "ks4-animal-plant-cells-e08",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the liquid that fills the permanent vacuole of a "
                "mature plant cell.",
        "options": [
            "Chlorophyll, the green pigment that absorbs light energy",
            "Cytoplasm, the gel that also fills the rest of the cell",
            "Water alone, with nothing dissolved in it",
            "Cell sap, a solution of sugars, salts and pigments",
        ],
        "correct_index": 3,
        "why": "The permanent vacuole is filled with cell sap, a solution of "
               "sugars, salts and pigments.",
    },
    {
        "id": "ks4-animal-plant-cells-e09",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which sub-cellular structure holds the green pigment "
                "chlorophyll.",
        "options": [
            "The permanent vacuole",
            "The cell wall",
            "The chloroplasts",
            "The cytoplasm",
        ],
        "correct_index": 2,
        "why": "Chlorophyll is held inside the chloroplasts, where it "
               "absorbs the light energy used in photosynthesis.",
    },
    {
        "id": "ks4-animal-plant-cells-e10",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the nucleus contains, and what this lets it "
                "control.",
        "options": [
            "The cell's DNA in chromosomes, so it controls which proteins "
            "the cell makes",
            "The cell's store of glucose, so it controls how fast the cell "
            "respires",
            "The cell's enzymes, so it controls the temperature the cell "
            "works at",
            "The cell's water, so it controls how firm the cell stays",
        ],
        "correct_index": 0,
        "why": "The nucleus holds the DNA as chromosomes, and the genes it "
               "carries decide which proteins the cell builds.",
    },
    {
        "id": "ks4-animal-plant-cells-e11",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many micrometres there are in one millimetre.",
        "options": [
            "10",
            "100",
            "1 000 000",
            "1000",
        ],
        "correct_index": 3,
        "why": "One millimetre is one thousand micrometres, so a cell 20 µm "
               "across is 0.02 mm across.",
    },
    {
        "id": "ks4-animal-plant-cells-e12",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the property of the cell membrane that lets it "
                "control what enters the cell.",
        "options": [
            "It is rigid, so nothing at all can pass through it in either "
            "direction",
            "It is selectively permeable, so only some substances cross it",
            "It is made of cellulose, which filters particles by their size",
            "It is freely permeable, so every substance passes straight "
            "through",
        ],
        "correct_index": 1,
        "why": "The membrane is selectively permeable: it lets some "
               "substances through and holds others back, which is how the "
               "cell controls its contents.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Apply a structure to a familiar context, or read a cell's job from what
    # it contains. The misconception rows sit here deliberately: a pupil who
    # holds one can recall the structure perfectly and still answer wrongly.
    {
        "id": "ks4-animal-plant-cells-s05",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the cellulose cell wall cannot be the structure "
                "that controls which substances enter a plant cell.",
        "options": [
            "The wall lies inside the membrane, so substances meet the "
            "membrane first",
            "The wall is only present in plant cells that are exposed to "
            "light",
            "The wall dissolves away whenever the cell takes in water by "
            "osmosis",
            "The wall is freely permeable, so dissolved substances and water "
            "pass straight through it",
        ],
        "correct_index": 3,
        "why": "The cellulose wall is freely permeable and sorts nothing; "
               "the selectively permeable membrane just inside it is what "
               "controls entry.",
    },
    {
        "id": "ks4-animal-plant-cells-s06",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is kept in complete darkness for two days. Explain "
                "why its cells still need mitochondria.",
        "options": [
            "Mitochondria store the glucose the plant made before it was put "
            "in the dark",
            "All living cells respire all the time, in their mitochondria",
            "Mitochondria take over photosynthesis whenever no light is "
            "available",
            "Mitochondria make the chlorophyll the plant will need when the "
            "light returns",
        ],
        "correct_index": 1,
        "why": "Respiration runs continuously in every living cell, light or "
               "no light, and aerobic respiration happens in the "
               "mitochondria.",
    },
    {
        "id": "ks4-animal-plant-cells-s07",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the vacuoles of animal cells with the permanent "
                "vacuole of a plant cell.",
        "options": [
            "Animal vacuoles are small and temporary; a plant's is large and "
            "permanent",
            "Animal cells never contain a vacuole of any kind at any stage "
            "of their lives",
            "Both are large and permanent, and both are filled with cell "
            "sap under pressure",
            "Animal vacuoles hold the cell sap; plant vacuoles hold pure "
            "water",
        ],
        "correct_index": 0,
        "why": "Animal cells may form small temporary vacuoles, but only "
               "plant cells carry one large permanent vacuole filled with "
               "cell sap.",
    },
    {
        "id": "ks4-animal-plant-cells-s08",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ribosomes are not counted as membrane-bound "
                "organelles.",
        "options": [
            "They are far too small for any membrane to fit around them, "
            "unlike a mitochondrion or a chloroplast",
            "They occur only in prokaryotes, which have no internal "
            "membranes",
            "They sit free in the cytoplasm or on the endoplasmic reticulum, "
            "with no membrane of their own",
            "They are built out of folded membrane themselves, so a "
            "further covering would serve them no purpose",
        ],
        "correct_index": 2,
        "why": "A ribosome has no surrounding membrane — it lies free in the "
               "cytoplasm or attached to the endoplasmic reticulum.",
    },
    {
        "id": "ks4-animal-plant-cells-s09",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell holds a nucleus, cytoplasm, a membrane, ribosomes "
                "and very many mitochondria, but no wall. Suggest what kind "
                "of cell it is.",
        "options": [
            "A plant cell taken from a root, where no light ever reaches it",
            "A bacterial cell, because bacteria respire more quickly than "
            "anything else",
            "A plant cell from a potato tuber, which is storing starch "
            "underground",
            "An animal cell with a high energy demand",
        ],
        "correct_index": 3,
        "why": "No cell wall rules out a plant cell, and a large number of "
               "mitochondria points to a cell that respires a great deal.",
    },
    {
        "id": "ks4-animal-plant-cells-s10",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell in the pancreas makes and releases large amounts of "
                "digestive enzyme. Predict which structure it holds in "
                "unusually large numbers.",
        "options": [
            "Chloroplasts, because enzymes are made from the glucose of "
            "photosynthesis",
            "Ribosomes, because enzymes are proteins and ribosomes build "
            "proteins",
            "Permanent vacuoles, because the enzyme has to be stored in the "
            "cell sap",
            "Nuclear pores, because each enzyme molecule leaves through a "
            "pore",
        ],
        "correct_index": 1,
        "why": "Enzymes are proteins, and proteins are assembled at "
               "ribosomes, so a cell exporting enzymes carries very many of "
               "them.",
    },
    {
        "id": "ks4-animal-plant-cells-s11",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A typical animal cell is about 20 µm across. Calculate this "
                "width in millimetres.",
        "options": [
            "0.02 mm",
            "0.2 mm",
            "2 mm",
            "0.002 mm",
        ],
        "correct_index": 0,
        "why": "There are 1000 µm in 1 mm, so 20 ÷ 1000 = 0.02 mm.",
    },
    {
        "id": "ks4-animal-plant-cells-s12",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant cell 50 µm wide appears 50 mm wide in a photograph. "
                "Calculate the magnification.",
        "options": [
            "×100",
            "×1",
            "×1000",
            "×1 000 000",
        ],
        "correct_index": 2,
        "why": "Both sizes must be in the same unit: 50 mm is 50 000 µm, and "
               "50 000 ÷ 50 = 1000.",
    },
    {
        "id": "ks4-animal-plant-cells-s13",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glucose molecules pass into a liver cell from the blood, "
                "while the cell's enzymes stay inside it. Explain what this "
                "shows.",
        "options": [
            "The membrane is completely impermeable, so no substance at all "
            "can cross it in either direction",
            "The membrane is freely permeable, so every molecule crosses it "
            "whenever it happens to arrive",
            "The membrane is made of cellulose and sorts molecules by their "
            "charge",
            "The membrane is selectively permeable, letting some molecules "
            "cross and holding others in",
        ],
        "correct_index": 3,
        "why": "A boundary that admits glucose but keeps enzymes in the "
               "cytoplasm is behaving as a selectively permeable membrane.",
    },
    {
        "id": "ks4-animal-plant-cells-s14",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a healthy young plant stands upright without "
                "any skeleton.",
        "options": [
            "Its cell walls contain bone-like fibres that stiffen as the "
            "plant grows",
            "Full vacuoles press the cell contents out against rigid walls, "
            "making the cells firm",
            "Its chloroplasts swell in the light and push the stem straight",
            "Its cell membranes harden once the plant has finished growing",
        ],
        "correct_index": 1,
        "why": "Water in the permanent vacuoles presses outwards against the "
               "rigid cellulose walls, and the turgid cells together hold "
               "the plant up.",
    },
    {
        "id": "ks4-animal-plant-cells-s15",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cells from inside a potato tuber have a wall and a "
                "permanent vacuole but no chloroplasts. Explain why.",
        "options": [
            "A tuber grows underground, out of the light chloroplasts need",
            "A tuber stores starch, and starch grains take the place of "
            "chloroplasts",
            "A tuber is part of a stem, and chloroplasts are only ever found "
            "in leaves",
            "Tuber cells are prokaryotic, so they hold no membrane-bound "
            "organelles",
        ],
        "correct_index": 0,
        "why": "Only plant cells exposed to light contain chloroplasts, and "
               "a tuber develops below the soil surface.",
    },
    {
        "id": "ks4-animal-plant-cells-s16",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student can see no ribosomes at all in their onion cells "
                "under a light microscope. Explain why not.",
        "options": [
            "Onion cells are plant cells, and plant cells contain no "
            "ribosomes",
            "The iodine solution used on onion cells destroys the ribosomes",
            "Ribosomes are about 20 nm across, well below what a light "
            "microscope can show",
            "Ribosomes are only present while a cell is actively dividing",
        ],
        "correct_index": 2,
        "why": "A ribosome is only about 20 nm across, far smaller than the "
               "detail a light microscope can separate.",
    },
    {
        "id": "ks4-animal-plant-cells-s17",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mature red blood cell has no nucleus. Predict what this "
                "means the cell can no longer do.",
        "options": [
            "Respire, because the nucleus is where respiration happens",
            "Take in oxygen, because oxygen enters through the nuclear pores",
            "Hold its shape, because the nucleus supports the cell from "
            "inside",
            "Make new proteins, because it has lost the DNA that codes for "
            "them",
        ],
        "correct_index": 3,
        "why": "The DNA in the nucleus carries the instructions for every "
               "protein, so a cell without one can make no new proteins.",
    },
    {
        "id": "ks4-animal-plant-cells-s18",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a stain is added when preparing cells to be "
                "viewed under a light microscope.",
        "options": [
            "It kills the cells so that they stop moving about on the slide",
            "It adds contrast, so structures such as the nucleus stand out",
            "It magnifies the cells so that a lower power lens can be used",
            "It flattens the cells so that light can pass through them",
        ],
        "correct_index": 1,
        "why": "Most cell structures are almost transparent, so a stain is "
               "used to add contrast and make them visible.",
    },
    {
        "id": "ks4-animal-plant-cells-s19",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that mitochondria produce energy. Give the "
                "scientifically correct version of that sentence.",
        "options": [
            "Mitochondria transfer energy from glucose by aerobic "
            "respiration",
            "Mitochondria create brand new energy from oxygen and water",
            "Mitochondria store energy until the cell asks them to let it go",
            "Mitochondria destroy the energy a cell no longer has any use "
            "for",
        ],
        "correct_index": 0,
        "why": "Energy cannot be created; aerobic respiration in the "
               "mitochondria transfers energy from glucose into a form the "
               "cell can use.",
    },
    {
        "id": "ks4-animal-plant-cells-s20",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the sub-cellular structures of a leaf palisade cell "
                "with those of a human liver cell.",
        "options": [
            "Both have a cell wall and ribosomes, but only the liver cell "
            "has mitochondria, because only animal cells release energy by "
            "respiration",
            "Only the palisade cell has mitochondria, because it is the "
            "only one of the two that makes its own glucose",
            "Both share the five animal-cell structures; the palisade cell "
            "adds a wall, a vacuole and chloroplasts",
            "Both have chloroplasts, though the liver cell keeps its own "
            "loose in the cytoplasm",
        ],
        "correct_index": 2,
        "why": "Plant cells have everything an animal cell has, plus a "
               "cellulose wall, a permanent vacuole and — in the light — "
               "chloroplasts.",
    },
    {
        "id": "ks4-animal-plant-cells-s21",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The inner membrane of a mitochondrion is folded. Explain "
                "the advantage of those folds to the cell.",
        "options": [
            "They make the mitochondrion strong enough to resist the "
            "pressure inside the cell",
            "They trap light so that the mitochondrion can photosynthesise "
            "as well",
            "They store the glucose that the mitochondrion will respire "
            "later on",
            "They give a much larger surface area for the reactions of "
            "aerobic respiration to take place on",
        ],
        "correct_index": 3,
        "why": "Folding the inner membrane packs more surface into the same "
               "space, giving more room for the reactions of aerobic "
               "respiration.",
    },
    {
        "id": "ks4-animal-plant-cells-s22",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the opposite roles played by chloroplasts and "
                "mitochondria in one leaf cell.",
        "options": [
            "Chloroplasts release the energy in glucose; mitochondria build "
            "glucose using light",
            "Chloroplasts build glucose using light; mitochondria release "
            "its energy",
            "Chloroplasts build the cell's proteins; mitochondria build its "
            "carbohydrates",
            "Chloroplasts control the whole cell; mitochondria control what "
            "enters it",
        ],
        "correct_index": 1,
        "why": "Photosynthesis in the chloroplasts stores energy in glucose; "
               "aerobic respiration in the mitochondria transfers that "
               "energy back out.",
    },
    {
        "id": "ks4-animal-plant-cells-s23",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why tissue placed on a microscope slide has to be a "
                "very thin section.",
        "options": [
            "So that light can pass through it and an image can form",
            "So that the cells are killed at once and stop moving",
            "So that the stain does not have to travel far into the tissue",
            "So that the coverslip is not lifted by the tissue beneath it",
        ],
        "correct_index": 0,
        "why": "A light microscope builds its image from light shone through "
               "the specimen, so the section must be thin enough to let "
               "light through.",
    },
    {
        "id": "ks4-animal-plant-cells-s24",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chloroplast is 5 µm long and the palisade cell holding it "
                "is 50 µm long. Determine how many times longer the cell is.",
        "options": [
            "5 times longer",
            "100 times longer",
            "10 times longer",
            "1000 times longer",
        ],
        "correct_index": 2,
        "why": "50 µm ÷ 5 µm = 10, so the cell is ten times the length of "
               "one chloroplast.",
    },
    {
        "id": "ks4-animal-plant-cells-s25",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an animal cell has no fixed shape while a plant "
                "cell does.",
        "options": [
            "An animal cell has no cytoplasm to hold its organelles in place",
            "An animal cell has a membrane of cellulose, which bends easily",
            "An animal cell is always far smaller, so its shape changes more "
            "readily",
            "An animal cell has only a thin flexible membrane, and no rigid "
            "wall",
        ],
        "correct_index": 3,
        "why": "A plant cell's shape is fixed by its rigid cellulose wall; "
               "an animal cell is bounded only by the flexible membrane, so "
               "it can change shape.",
    },
    {
        "id": "ks4-animal-plant-cells-s26",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The cytoplasm is the site of most of a cell's chemical "
                "reactions. State what this tells you it must hold.",
        "options": [
            "Chlorophyll, to absorb the light those reactions need",
            "Dissolved enzymes, which catalyse those reactions",
            "Cellulose fibres, to hold the reacting molecules still",
            "Cell sap, drawn in from the permanent vacuole",
        ],
        "correct_index": 1,
        "why": "Reactions in cells are catalysed by enzymes, so the "
               "cytoplasm must hold enzymes in solution.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # An inventory read backwards, a claim evaluated, or a magnification
    # rearranged through two unit changes. The calculations all divide
    # exactly; every wrong answer is one identifiable slip.
    {
        "id": "ks4-animal-plant-cells-h05",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell drawn at a magnification of ×400 measures 60 mm "
                "across on the page. Calculate its actual width in "
                "micrometres.",
        "options": [
            "24 000 µm",
            "150 µm",
            "0.15 µm",
            "1500 µm",
        ],
        "correct_index": 1,
        "why": "Actual size = image ÷ magnification = 60 mm ÷ 400 = 0.15 mm, "
               "and 0.15 mm is 150 µm.",
    },
    {
        "id": "ks4-animal-plant-cells-h06",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drawing of a cell carries a scale bar 20 mm long, "
                "labelled 10 µm. Determine the magnification of the drawing.",
        "options": [
            "×2",
            "×200",
            "×0.0005",
            "×2000",
        ],
        "correct_index": 3,
        "why": "20 mm is 20 000 µm, and 20 000 ÷ 10 = 2000, so the drawing "
               "is ×2000.",
    },
    {
        "id": "ks4-animal-plant-cells-h07",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ribosome is 20 nm across and an animal cell 20 µm across. "
                "Calculate how many ribosomes laid side by side would span "
                "the cell.",
        "options": [
            "1000",
            "100",
            "20",
            "1 000 000",
        ],
        "correct_index": 0,
        "why": "20 µm is 20 000 nm, and 20 000 ÷ 20 = 1000 ribosomes across.",
    },
    {
        "id": "ks4-animal-plant-cells-h08",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that the cell wall stops water getting "
                "into a plant cell. Evaluate this claim.",
        "options": [
            "Correct — the wall is waterproof, and that is why a plant cell "
            "left in pure water never bursts open",
            "Wrong — a plant cell cannot take in water at all, however "
            "dilute the solution surrounding it happens to be",
            "Wrong — water passes freely through the wall, and the wall "
            "resists the pressure that builds inside",
            "Correct — but only in root cells, which would otherwise be "
            "flooded",
        ],
        "correct_index": 2,
        "why": "Water passes straight through the freely permeable wall; "
               "what the wall does is push back as the cell swells, so it "
               "becomes turgid rather than bursting.",
    },
    {
        "id": "ks4-animal-plant-cells-h09",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that the cell wall and the cell membrane "
                "do the same job. Explain the mistake.",
        "options": [
            "Both control what crosses them, but the wall works far more "
            "slowly than the membrane",
            "The wall gives rigid support; the membrane controls what "
            "crosses it",
            "The wall controls what crosses it, while the membrane simply "
            "holds the cell's shape",
            "The wall is the living layer, while the membrane is a dead "
            "outer covering",
        ],
        "correct_index": 1,
        "why": "The cellulose wall supports and shapes the cell but sorts "
               "nothing; only the selectively permeable membrane controls "
               "what enters and leaves.",
    },
    {
        "id": "ks4-animal-plant-cells-h10",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cell A holds very many mitochondria and cell B very many "
                "ribosomes. Suggest the job each of them is doing.",
        "options": [
            "A makes a great deal of protein; B releases a great deal of "
            "energy by respiration",
            "A photosynthesises quickly; B stores starch for the plant to "
            "use later",
            "A divides very often; B has stopped dividing altogether",
            "A releases a lot of energy by respiration; B makes a lot of "
            "protein",
        ],
        "correct_index": 3,
        "why": "Mitochondria are the site of aerobic respiration and "
               "ribosomes the site of protein synthesis, so the organelle "
               "count names the cell's main job.",
    },
    {
        "id": "ks4-animal-plant-cells-h11",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A poison stops the mitochondria working in a root hair "
                "cell. Predict the effect on its uptake of mineral ions from "
                "the soil.",
        "options": [
            "It stops, because active transport needs energy released by "
            "respiration",
            "It speeds up, because the ions no longer have to pass the "
            "mitochondria",
            "It is unchanged, because mineral ions enter the cell by osmosis",
            "It stops, because mineral ions are manufactured inside the "
            "mitochondria",
        ],
        "correct_index": 0,
        "why": "Mineral ions are taken up against a concentration gradient "
               "by active transport, which is powered by energy from "
               "respiration in the mitochondria.",
    },
    {
        "id": "ks4-animal-plant-cells-h12",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug destroys a cell's ribosomes and leaves every other "
                "structure intact. Predict the consequence for that cell.",
        "options": [
            "It can no longer respire, so it runs out of energy within "
            "minutes",
            "It can no longer control what enters it, so it fills up with "
            "water",
            "It can no longer build proteins, so it cannot replace its "
            "enzymes",
            "It can no longer hold its shape, so it collapses into the "
            "cytoplasm",
        ],
        "correct_index": 2,
        "why": "Ribosomes are the only site of protein synthesis, so without "
               "them a cell makes no new proteins, including the enzymes it "
               "needs.",
    },
    {
        "id": "ks4-animal-plant-cells-h13",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf is covered so that no light reaches it for three "
                "weeks. Predict what becomes of the chloroplasts already "
                "inside its cells.",
        "options": [
            "They are broken down and rebuilt as mitochondria for "
            "respiration",
            "They stay in the cells but photosynthesise no longer",
            "They leave the cell through the pores of the nuclear envelope",
            "They fill with cell sap and merge into the permanent vacuole",
        ],
        "correct_index": 1,
        "why": "Chloroplasts are permanent structures; without light they "
               "simply stop photosynthesising, and only cells that never "
               "receive light lack them altogether.",
    },
    {
        "id": "ks4-animal-plant-cells-h14",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cells are mounted in a drop of water before the "
                "coverslip is lowered onto them.",
        "options": [
            "The water stains the nuclei so that they can be seen",
            "The water dissolves the cell walls and flattens the cells",
            "The water magnifies the cells, so a lower power lens will do",
            "The water stops the cells drying out and helps keep air "
            "bubbles out",
        ],
        "correct_index": 3,
        "why": "Mounting in water keeps the cells hydrated and fills the "
               "space under the coverslip, so fewer air bubbles are trapped.",
    },
    {
        "id": "ks4-animal-plant-cells-h15",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wilted houseplant is watered and its leaves are firm "
                "again by morning. Explain that recovery.",
        "options": [
            "The vacuoles refill, so the cells push out against their walls "
            "again",
            "The cell walls thicken as the plant takes up water from the "
            "soil through its roots",
            "New chloroplasts are made, and these hold the leaves out flat",
            "The cell membranes stiffen once the plant has water enough",
        ],
        "correct_index": 0,
        "why": "Water taken up refills the vacuoles, the cells become turgid "
               "and press on their rigid walls, and the leaves stiffen.",
    },
    {
        "id": "ks4-animal-plant-cells-h16",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two liver cells respire equally fast. One holds 500 "
                "mitochondria with shallow folds, the other 250 with deeply "
                "folded cristae. Explain how this is possible.",
        "options": [
            "The number of mitochondria has no effect on how fast a cell "
            "respires",
            "Deeply folded mitochondria hold far more glucose than shallow "
            "ones",
            "The total inner membrane surface area can be similar in both",
            "Liver cells respire in the cytoplasm, so mitochondria make no "
            "difference",
        ],
        "correct_index": 2,
        "why": "It is the area of inner membrane that limits respiration, "
               "and fewer, more folded mitochondria can provide as much of "
               "it as many shallow ones.",
    },
    {
        "id": "ks4-animal-plant-cells-h17",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A photograph printed at ×1500 shows a cell 45 mm wide. "
                "Determine the cell's actual width in micrometres.",
        "options": [
            "0.03 µm",
            "30 µm",
            "3 µm",
            "67 500 µm",
        ],
        "correct_index": 1,
        "why": "45 mm ÷ 1500 = 0.03 mm, and 0.03 mm × 1000 = 30 µm.",
    },
    {
        "id": "ks4-animal-plant-cells-h18",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A row of 12 identical onion cells stretches across 3.0 mm "
                "of a slide. Calculate the length of one of those cells in "
                "micrometres.",
        "options": [
            "36 µm",
            "4 µm",
            "2500 µm",
            "250 µm",
        ],
        "correct_index": 3,
        "why": "3.0 mm is 3000 µm, and 3000 ÷ 12 = 250 µm for one cell.",
    },
    {
        "id": "ks4-animal-plant-cells-h19",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that plant cells have no need of "
                "mitochondria because their chloroplasts already supply the "
                "energy. Evaluate that argument.",
        "options": [
            "Wrong — chloroplasts store energy in glucose, and only "
            "respiration releases it",
            "Correct, provided the plant is standing in the light for part "
            "of every day",
            "Correct — chloroplasts carry out aerobic respiration as well "
            "as photosynthesis",
            "Wrong — plant cells contain no chloroplasts at all, only "
            "mitochondria and ribosomes",
        ],
        "correct_index": 0,
        "why": "Photosynthesis stores energy as glucose, and the cell can "
               "only use that energy once respiration in the mitochondria "
               "transfers it, so plant cells respire too.",
    },
    {
        "id": "ks4-animal-plant-cells-h20",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Under the same light microscope a stained onion cell shows "
                "a clear outline and a stained cheek cell does not. Explain "
                "the difference.",
        "options": [
            "The onion cell takes up stain, whereas a cheek cell cannot be "
            "stained at all",
            "The cheek cell has no cell membrane, so there is no outline to "
            "see",
            "The onion cell has a thick cellulose wall, giving a clear "
            "boundary",
            "The cheek cell is far larger, so its edges fall outside the "
            "field of view",
        ],
        "correct_index": 2,
        "why": "The rigid cellulose wall gives a plant cell a sharp outline; "
               "an animal cell is bounded only by a thin membrane, which is "
               "much harder to see.",
    },
    {
        "id": "ks4-animal-plant-cells-h21",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skin cell holds far fewer mitochondria than a heart "
                "muscle cell. Explain what that does, and does not, tell you "
                "about the skin cell.",
        "options": [
            "It does not respire at all, because respiration only happens in "
            "muscle",
            "It respires less than the heart cell, but it still respires all "
            "the time",
            "It must be dying, because a healthy cell always holds many "
            "mitochondria",
            "It must be a plant cell, because plant cells need fewer "
            "mitochondria",
        ],
        "correct_index": 1,
        "why": "Every living cell respires; fewer mitochondria means a lower "
               "energy demand, not the absence of respiration.",
    },
    {
        "id": "ks4-animal-plant-cells-h22",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is measured as 0.045 mm wide. Determine that width "
                "first in micrometres and then in nanometres.",
        "options": [
            "4.5 µm and 4500 nm",
            "450 µm and 450 000 nm",
            "45 µm and 4500 nm",
            "45 µm and 45 000 nm",
        ],
        "correct_index": 3,
        "why": "0.045 mm × 1000 = 45 µm, and 45 µm × 1000 = 45 000 nm.",
    },
    {
        "id": "ks4-animal-plant-cells-h23",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A light microscope drawing labels one mitochondrion inside "
                "a cheek cell. Suggest why an examiner would query that "
                "label.",
        "options": [
            "A light microscope cannot show a mitochondrion clearly enough "
            "to identify one",
            "Cheek cells are the only animal cells that contain no "
            "mitochondria at all",
            "Mitochondria dissolve in the methylene blue used to stain cheek "
            "cells",
            "Mitochondria are found only in plant cells, alongside the "
            "chloroplasts",
        ],
        "correct_index": 0,
        "why": "A light microscope shows the nucleus, cytoplasm and cell "
               "outline, but a single mitochondrion is below the detail it "
               "can resolve.",
    },
    {
        "id": "ks4-animal-plant-cells-h24",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student views onion epidermis unstained and sees only "
                "faint outlines. Evaluate adding iodine solution before "
                "viewing again.",
        "options": [
            "Pointless — iodine solution only shows up on animal cells",
            "Harmful — iodine solution dissolves the cellulose of the cell "
            "walls",
            "Worthwhile — iodine stains the nuclei and raises the contrast",
            "Unnecessary — a higher power lens would add the contrast "
            "instead",
        ],
        "correct_index": 2,
        "why": "Iodine solution stains starch and nuclei, so structures a "
               "light microscope would otherwise show only faintly stand "
               "out.",
    },
    {
        "id": "ks4-animal-plant-cells-h25",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens to a plant cell and to an animal cell "
                "when each loses a large amount of water.",
        "options": [
            "Both burst open, because the water leaving pulls the membrane "
            "apart",
            "The plant cell goes flaccid inside its wall; the animal cell "
            "shrinks and wrinkles",
            "The plant cell shrinks away to nothing, while the animal cell "
            "keeps its shape",
            "Neither changes at all, because both are protected by a rigid "
            "cellulose wall",
        ],
        "correct_index": 1,
        "why": "The plant cell's wall keeps its outline while the contents "
               "shrink back from it; an animal cell has no wall, so the "
               "whole cell shrivels.",
    },
    {
        "id": "ks4-animal-plant-cells-h26",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell measures 60 mm across in a photograph printed at "
                "×3000. Determine its actual size and state which kind of "
                "cell it is likely to be.",
        "options": [
            "20 µm, so it is more likely to be a bacterial cell",
            "2 µm, so it is more likely to be a bacterium",
            "180 µm, which is far too large to be either of them",
            "20 µm, so it is more likely to be an animal cell",
        ],
        "correct_index": 3,
        "why": "60 mm ÷ 3000 = 0.02 mm = 20 µm, the size of a typical animal "
               "cell and many times the width of a bacterium.",
    },
]
