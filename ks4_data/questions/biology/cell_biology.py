"""Biology · Cell biology — the eight subtopics of AQA 4.1.

Covers `eukaryotes-prokaryotes` through `culturing-microorganisms`: cell
types and scale, sub-cellular structures, specialisation and
differentiation, microscopy and magnification, chromosomes and the cell
cycle, stem cells, transport across membranes, and the Triple-only
culturing practical.

Seven of the eight subtopics are BASE — a Foundation Combined class sits
all of them — so nothing in those stems or options reaches into the Higher
extension prose (therapeutic cloning, the inverse square law, percentage
change in mass, surface area to volume ratio calculations). Only
`culturing-microorganisms` is Triple-only, and it is flagged as such.

The distractors are built from the misconceptions the pages themselves
declare: bacteria credited with a nucleus or with mitochondria, the
bacterial wall called cellulose, root cells expected to hold chloroplasts,
water at a root hair said to enter by active transport, mitosis confused
with meiosis, stem cells described as always embryonic or as growing whole
organs, osmosis described as moving solute rather than water, active
transport described as needing no energy, and school plates incubated at
body temperature. Magnification questions state every number in the stem
and every distractor comes from a real slip — a missing mm-to-micrometre
conversion, a dropped power of ten, or dividing where you should multiply.

Nothing here restates a lesson page's own "Test yourself" question, its
worked FIFA examples or its matching block — those are a different pool,
printed with their answers on a page the child can open at will.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ── eukaryotes-prokaryotes ──────────────────────────────────────────
    {
        "id": "ks4-eukaryotes-prokaryotes-e01",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the material that the cell wall of a bacterium is "
                "made from.",
        "options": [
            "Peptidoglycan, a mesh of sugars and amino acids",
            "Cellulose, the same material as a plant cell wall",
            "Keratin, the same material as hair and nails",
            "Phospholipid, the same material as a cell membrane",
        ],
        "correct_index": 0,
        "why": "Bacterial walls are peptidoglycan; cellulose is the material "
               "of a plant cell wall, not a bacterial one.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e02",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some bacteria have a slimy protective layer outside the "
                "cell wall. Name this structure.",
        "options": [
            "The plasmid",
            "The capsule",
            "The flagellum",
            "The cytoskeleton",
        ],
        "correct_index": 1,
        "why": "The capsule is the slimy outer layer that protects a "
               "bacterium and helps it stick to surfaces.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e03",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many nanometres there are in one micrometre.",
        "options": [
            "10 nm",
            "100 nm",
            "1000 nm",
            "1 000 000 nm",
        ],
        "correct_index": 2,
        "why": "Each step down the scale is a factor of 1000, so "
               "1 µm = 1000 nm, just as 1 mm = 1000 µm.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-e04",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these groups of organisms is made of "
                "prokaryotic cells.",
        "options": [
            "Fungi",
            "Protists",
            "Plants",
            "Bacteria",
        ],
        "correct_index": 3,
        "why": "All bacteria are prokaryotes; fungi, protists, plants and "
               "animals are all made of eukaryotic cells.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s01",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterium can absorb enough nutrients across "
                "its outer surface without any transport system.",
        "options": [
            "It has a very low surface area to volume ratio, so little is wasted",
            "It is very small, so it has a very high surface area to volume ratio",
            "It has mitochondria that pump nutrients in across the membrane",
            "Its loop of circular DNA speeds up the movement of nutrients in",
        ],
        "correct_index": 1,
        "why": "A very small cell has a large surface relative to its "
               "volume, so diffusion across the surface alone can supply it.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s02",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ribosome is about 20 nm across and a typical animal cell "
                "is about 20 µm across. Determine how many times wider the "
                "animal cell is than the ribosome.",
        "options": [
            "10 times wider",
            "100 times wider",
            "1000 times wider",
            "1 000 000 times wider",
        ],
        "correct_index": 2,
        "why": "20 µm is 20 000 nm, and 20 000 ÷ 20 = 1000, so the cell is "
               "a thousand times wider.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s03",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Bacteria carry out aerobic respiration "
                "in their mitochondria.' Identify the error.",
        "options": [
            "Bacteria do not respire at all, so no organelle is involved",
            "Bacteria respire, but only inside their loop of circular DNA",
            "Bacteria respire in their ribosomes, which are smaller than ours",
            "Bacteria have no mitochondria — no membrane-bound organelles",
        ],
        "correct_index": 3,
        "why": "Prokaryotes have no membrane-bound organelles at all, so "
               "there are no mitochondria for respiration to happen in.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-s04",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is described as having a nucleus, mitochondria and "
                "a cell wall. Deduce what kind of cell it is.",
        "options": [
            "A eukaryotic plant or fungal cell",
            "A prokaryotic bacterial cell",
            "A eukaryotic animal cell",
            "A virus, which has all three features",
        ],
        "correct_index": 0,
        "why": "A nucleus and mitochondria make it eukaryotic, and the cell "
               "wall rules out an animal cell.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h01",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium is 4 µm long. In a photograph it measures "
                "24 mm. Calculate the magnification of the photograph.",
        "options": [
            "×6",
            "×600",
            "×6000",
            "×60 000",
        ],
        "correct_index": 2,
        "why": "24 mm is 24 000 µm, and 24 000 ÷ 4 = 6000, so the image is "
               "6000 times the real length.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h02",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that because prokaryotes have no nucleus "
                "they cannot make proteins. Evaluate this claim.",
        "options": [
            "Correct — protein synthesis needs a nucleus, so bacteria absorb theirs",
            "Correct — a bacterium makes protein only after taking up a plasmid",
            "Incorrect — bacteria build their proteins in their mitochondria",
            "Incorrect — bacteria have ribosomes, and ribosomes build proteins",
        ],
        "correct_index": 3,
        "why": "Protein synthesis happens at ribosomes, and prokaryotes have "
               "ribosomes even though they have no nucleus.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h03",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a plasmid with the main loop of DNA in a bacterial "
                "cell.",
        "options": [
            "Both are circular DNA, but a plasmid is small and not essential",
            "Both are circular DNA, but a plasmid is larger and holds every gene",
            "The plasmid is DNA and the main loop is protein, so only one codes",
            "The plasmid sits in the nucleus and the main loop in the cytoplasm",
        ],
        "correct_index": 0,
        "why": "Both are circular DNA in the cytoplasm, but a plasmid is a "
               "small extra ring the cell can survive without.",
    },
    {
        "id": "ks4-eukaryotes-prokaryotes-h04",
        "subtopic_slug": "eukaryotes-prokaryotes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newly found single-celled organism is 30 µm across, has "
                "a cell wall, and keeps its DNA inside a membrane. Predict "
                "how it should be classified, and give the reason.",
        "options": [
            "Prokaryotic, because it has a cell wall just as a bacterium does",
            "Eukaryotic, because its DNA is enclosed in a membrane-bound nucleus",
            "Prokaryotic, because 30 µm is a normal size for a bacterium",
            "Eukaryotic, because any cell wider than 1 µm must be eukaryotic",
        ],
        "correct_index": 1,
        "why": "A true nucleus — DNA enclosed in a membrane — is the feature "
               "that defines a eukaryotic cell, whatever else it has.",
    },

    # ── animal-plant-cells ──────────────────────────────────────────────
    {
        "id": "ks4-animal-plant-cells-e01",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the structure that surrounds the nucleus and contains "
                "pores.",
        "options": [
            "The cell wall",
            "The permanent vacuole",
            "The nuclear envelope",
            "The cytoplasm",
        ],
        "correct_index": 2,
        "why": "The nuclear envelope is the double membrane around the "
               "nucleus, and its pores let molecules pass in and out.",
    },
    {
        "id": "ks4-animal-plant-cells-e02",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which stain is used to make the nuclei of animal "
                "cells easier to see under a light microscope.",
        "options": [
            "Methylene blue",
            "Iodine solution",
            "Distilled water",
            "Sodium hydroxide",
        ],
        "correct_index": 0,
        "why": "Methylene blue stains animal cell nuclei dark blue, so they "
               "stand out against the pale cytoplasm.",
    },
    {
        "id": "ks4-animal-plant-cells-e03",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the folded inner membrane of a mitochondrion.",
        "options": [
            "Stomata",
            "Sieve plates",
            "Cell sap",
            "Cristae",
        ],
        "correct_index": 3,
        "why": "The cristae are the folds of the inner membrane, and they "
               "increase the surface area for respiration reactions.",
    },
    {
        "id": "ks4-animal-plant-cells-e04",
        "subtopic_slug": "animal-plant-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant cell has both a cell wall and a cell membrane. "
                "State how the two are arranged.",
        "options": [
            "The membrane is outside the wall, and the wall touches the cytoplasm",
            "The wall is outside the membrane, and the membrane touches the cytoplasm",
            "Only the wall is present — plant cells have no cell membrane at all",
            "Both lie inside the vacuole, which surrounds the rest of the cell",
        ],
        "correct_index": 1,
        "why": "The cellulose wall is the outermost layer, and the cell "
               "membrane lies just inside it against the cytoplasm.",
    },
    {
        "id": "ks4-animal-plant-cells-s01",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf palisade cell may contain up to 70 chloroplasts. "
                "Explain why it holds so many.",
        "options": [
            "Chloroplasts store the water that arrives in the leaf by xylem",
            "Chloroplasts make the cell rigid so the leaf can hold its shape",
            "Palisade cells respire faster than any other cell in the plant",
            "Palisade cells sit near the surface and do most of the photosynthesis",
        ],
        "correct_index": 3,
        "why": "Palisade cells are the leaf's main photosynthetic cells, so "
               "packing in chloroplasts captures the most light.",
    },
    {
        "id": "ks4-animal-plant-cells-s02",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cut flower is left out of water for a day and its stem "
                "droops. Explain, in terms of cell structure, why the stem "
                "can no longer hold itself up.",
        "options": [
            "The cell walls dissolve away, so the cells lose their fixed shape",
            "The vacuoles lose water, so the cells are no longer firm and turgid",
            "The chloroplasts shrink, so less photosynthesis supports the stem",
            "The cell membranes harden, so the cells can no longer bend at all",
        ],
        "correct_index": 1,
        "why": "A full vacuole presses the cell contents against the wall; "
               "lose that water and the cells go flaccid and the stem droops.",
    },
    {
        "id": "ks4-animal-plant-cells-s03",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is found to contain a cell wall, a permanent vacuole "
                "and mitochondria, but no chloroplasts. Suggest where in the "
                "plant this cell came from.",
        "options": [
            "A root, where no light reaches the cells at all",
            "The palisade layer, just below the upper leaf surface",
            "Nowhere — without chloroplasts it cannot be a plant cell",
            "A guard cell, on either side of a stoma in the leaf",
        ],
        "correct_index": 0,
        "why": "The wall and vacuole make it a plant cell, and only cells "
               "that never see light — such as root cells — lack chloroplasts.",
    },
    {
        "id": "ks4-animal-plant-cells-s04",
        "subtopic_slug": "animal-plant-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the roles of the cytoplasm and the cell membrane.",
        "options": [
            "Both control what enters and leaves the cell, although the cytoplasm is slower",
            "The cytoplasm holds the cell's DNA and the membrane holds the organelles",
            "Most chemical reactions happen in the cytoplasm; the membrane controls entry",
            "The cytoplasm builds the cell's proteins and the membrane releases energy",
        ],
        "correct_index": 2,
        "why": "The cytoplasm is where most reactions take place; the "
               "membrane is a selectively permeable barrier round the outside.",
    },
    {
        "id": "ks4-animal-plant-cells-h01",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student draws an onion bulb epidermis cell and labels a "
                "chloroplast in it. Explain why that label must be wrong.",
        "options": [
            "Onion bulbs grow underground in the dark, so their cells have none",
            "Onion cells are prokaryotic, so they hold no membrane-bound organelles",
            "Chloroplasts occur only in animal cells and never in any plant cell",
            "A chloroplast would be far too small to draw at that magnification",
        ],
        "correct_index": 0,
        "why": "Only plant cells exposed to light contain chloroplasts, and a "
               "bulb sits underground where no light reaches it.",
    },
    {
        "id": "ks4-animal-plant-cells-h02",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student lowers a coverslip onto a slide and then sees "
                "dark circles across the whole field of view. Suggest the "
                "cause and the improvement.",
        "options": [
            "Too much stain was used — add far less iodine solution next time",
            "The section was too thick — cut a much thinner section next time",
            "Air bubbles were trapped — lower the coverslip slowly at an angle",
            "The image was out of focus — use the fine adjustment knob next time",
        ],
        "correct_index": 2,
        "why": "Trapped air appears as dark-edged circles, and lowering the "
               "coverslip slowly at an angle lets the air escape.",
    },
    {
        "id": "ks4-animal-plant-cells-h03",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sperm cells, heart muscle cells and liver cells all "
                "contain very many mitochondria. Explain what these three "
                "cell types have in common.",
        "options": [
            "They are all found only in animals and are never found in plants",
            "They all use large amounts of energy, released by aerobic respiration",
            "They are all far larger than average, so they need more organelles",
            "They all have to divide by mitosis far more often than any other cells do",
        ],
        "correct_index": 1,
        "why": "Mitochondria are the site of aerobic respiration, so a cell "
               "with a high energy demand carries a large number of them.",
    },
    {
        "id": "ks4-animal-plant-cells-h04",
        "subtopic_slug": "animal-plant-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant cell and an animal cell are placed in the same very "
                "dilute solution. Only the animal cell bursts. Explain why.",
        "options": [
            "The plant cell's chloroplasts absorb the extra water as it enters",
            "The plant cell's vacuole is already full, so no more water enters it",
            "The plant cell's membrane is much thicker than an animal cell's",
            "The plant cell's cellulose wall is rigid and resists the pressure",
        ],
        "correct_index": 3,
        "why": "The rigid cellulose wall pushes back as water enters, so a "
               "plant cell becomes turgid rather than bursting.",
    },

    # ── cell-specialisation ─────────────────────────────────────────────
    {
        "id": "ks4-cell-specialisation-e01",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a cell's genes during "
                "differentiation.",
        "options": [
            "All of its genes are switched on at the same moment",
            "Some genes are switched on and others are switched off",
            "The genes it will not need are permanently deleted",
            "Its genes are copied so that it has twice as many",
        ],
        "correct_index": 1,
        "why": "A cell specialises by switching some genes on and others "
               "off, so it makes only the proteins that job needs.",
    },
    {
        "id": "ks4-cell-specialisation-e02",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the region of a plant where cells stay "
                "undifferentiated throughout the plant's life.",
        "options": [
            "The xylem",
            "The phloem",
            "The palisade layer",
            "The meristem",
        ],
        "correct_index": 3,
        "why": "Meristem cells stay undifferentiated, which is why a plant "
               "can keep producing new tissues for as long as it lives.",
    },
    {
        "id": "ks4-cell-specialisation-e03",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the function of the acrosome on the head of a sperm "
                "cell.",
        "options": [
            "It holds enzymes that digest through the egg's outer layers",
            "It holds the mitochondria that supply energy for swimming",
            "It holds the 23 chromosomes the sperm carries to the egg",
            "It holds the flagellum until the sperm reaches the egg",
        ],
        "correct_index": 0,
        "why": "The acrosome is an enzyme-filled cap that digests a path "
               "through the egg's outer layers at fertilisation.",
    },
    {
        "id": "ks4-cell-specialisation-e04",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the specialised plant cell that transports dissolved "
                "sugars around the plant.",
        "options": [
            "Xylem",
            "Root hair cell",
            "Phloem",
            "Palisade mesophyll",
        ],
        "correct_index": 2,
        "why": "Phloem carries dissolved sugars from the leaves to the rest "
               "of the plant; xylem carries water the other way.",
    },
    {
        "id": "ks4-cell-specialisation-s01",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how sieve plates suit phloem to its function.",
        "options": [
            "Their pores let the sugar solution flow from one cell to the next",
            "They are thickened with lignin so the tube cannot collapse inwards",
            "They filter out mineral ions so that only sugars are carried along",
            "They hold chloroplasts in place so sugar is made inside the tube",
        ],
        "correct_index": 0,
        "why": "The pores in a sieve plate leave the tube open end to end, so "
               "the sugar solution can flow along it.",
    },
    {
        "id": "ks4-cell-specialisation-s02",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that a root hair cell takes in water from "
                "the soil by active transport. Correct this statement.",
        "options": [
            "Water enters by diffusion through the wall, not by active transport",
            "Water enters by active transport, but only when the soil is dry",
            "Water enters by osmosis; active transport is used for mineral ions",
            "Water enters by osmosis and the mineral ions enter by osmosis too",
        ],
        "correct_index": 2,
        "why": "Water always moves by osmosis, which is passive; active "
               "transport is how the same cell pulls in mineral ions.",
    },
    {
        "id": "ks4-cell-specialisation-s03",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the myelin sheath helps a neurone carry out "
                "its function.",
        "options": [
            "It supplies the neurone with the glucose it needs to respire",
            "It insulates the axon so the electrical impulse travels faster",
            "It lets the neurone branch and connect to many other neurones",
            "It stores the neurotransmitter released at the next synapse",
        ],
        "correct_index": 1,
        "why": "The fatty myelin sheath insulates the axon, letting the "
               "impulse travel far faster than along a bare fibre.",
    },
    {
        "id": "ks4-cell-specialisation-s04",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why differentiation in an adult animal is far more "
                "limited than in an adult plant.",
        "options": [
            "Adult animals have no stem cells anywhere in their bodies at all",
            "Adult plant cells divide by meiosis, which animal cells simply cannot do",
            "Animal cells are much smaller, so they cannot change their shape",
            "Most animal cells commit to one type early and cannot change again",
        ],
        "correct_index": 3,
        "why": "In animals differentiation is mostly finished in the embryo "
               "and is not reversible, whereas plant meristems never stop.",
    },
    {
        "id": "ks4-cell-specialisation-h01",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A red blood cell is a biconcave disc rather than a sphere "
                "of the same volume. Explain the advantage of that shape.",
        "options": [
            "It lets the cell hold more haemoglobin than a sphere could hold",
            "It stops white blood cells from attacking it as it passes them",
            "It makes the cell heavier so that it sinks faster through a capillary",
            "It gives a larger surface and a shorter path for oxygen to diffuse",
        ],
        "correct_index": 3,
        "why": "Dishing the disc raises its surface area and thins the "
               "middle, so oxygen diffuses in and out over a shorter distance.",
    },
    {
        "id": "ks4-cell-specialisation-h02",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Xylem walls are thickened with lignin. Explain what would "
                "go wrong in a tall plant without it.",
        "options": [
            "The xylem would fill with cytoplasm and the flow would be blocked",
            "The tubes would collapse under the pressure of the water column",
            "The xylem could not take up mineral ions from the soil water",
            "The xylem cells would keep dividing and close the tube off",
        ],
        "correct_index": 1,
        "why": "Lignin is a hard waterproof thickening that stops the hollow "
               "tubes collapsing as water is pulled up under tension.",
    },
    {
        "id": "ks4-cell-specialisation-h03",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sperm cell carries 23 chromosomes rather than the 46 in "
                "a body cell. Explain why.",
        "options": [
            "So the sperm is light enough to be driven along by its flagellum",
            "So there is spare room in the head for the acrosome enzymes",
            "So that when sperm and egg fuse, the new cell has the full 46",
            "So that the sperm can divide by mitosis on its way to the egg",
        ],
        "correct_index": 2,
        "why": "Each gamete carries half the chromosomes so that "
               "fertilisation restores the normal 46, not doubles it.",
    },
    {
        "id": "ks4-cell-specialisation-h04",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Companion cells lie alongside phloem sieve tubes and are "
                "packed with mitochondria. Suggest why.",
        "options": [
            "Loading sugar into the sieve tube needs energy from respiration",
            "The mitochondria break the sugars down before they are carried",
            "The mitochondria make the sugars that the sieve tube then carries",
            "The mitochondria are kept there because sieve tubes have no room",
        ],
        "correct_index": 0,
        "why": "Sugars are loaded into the sieve tube against a gradient, and "
               "that active loading needs ATP from respiration.",
    },

    # ── microscopy ──────────────────────────────────────────────────────
    {
        "id": "ks4-microscopy-e01",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of electron microscope that scans the surface "
                "of a specimen to give a three-dimensional image.",
        "options": [
            "A transmission electron microscope (TEM)",
            "A light microscope used at its highest magnification",
            "A compound microscope fitted with an oil lens",
            "A scanning electron microscope (SEM)",
        ],
        "correct_index": 3,
        "why": "The SEM scans the outside of a specimen, which is why its "
               "images look three-dimensional; a TEM passes through a slice.",
    },
    {
        "id": "ks4-microscopy-e02",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation used to calculate the actual size of a "
                "specimen.",
        "options": [
            "Actual size = image size × magnification",
            "Actual size = magnification ÷ image size",
            "Actual size = image size ÷ magnification",
            "Actual size = image size × magnification ÷ 1000",
        ],
        "correct_index": 2,
        "why": "Magnification = image ÷ actual, so rearranging gives "
               "actual = image ÷ magnification.",
    },
    {
        "id": "ks4-microscopy-e03",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate resolution of a light microscope.",
        "options": [
            "0.1 nm",
            "200 nm",
            "2000 nm",
            "200 µm",
        ],
        "correct_index": 1,
        "why": "Light microscopes resolve to about 200 nm, set by the "
               "wavelength of visible light; an electron beam reaches 0.1 nm.",
    },
    {
        "id": "ks4-microscopy-e04",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one disadvantage of staining a specimen before "
                "viewing it.",
        "options": [
            "The stain kills the cells, so the specimen is no longer living",
            "The stain raises the magnification but lowers the resolution",
            "The stain makes the specimen too thick for light to pass through",
            "The stain removes the nucleus, which can then not be seen at all",
        ],
        "correct_index": 0,
        "why": "Stains kill cells, so a stained slide can never be used to "
               "watch a living process.",
    },
    {
        "id": "ks4-microscopy-s01",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is 60 µm wide. In a drawing it measures 120 mm "
                "wide. Calculate the magnification of the drawing.",
        "options": [
            "×2",
            "×200",
            "×2000",
            "×20 000",
        ],
        "correct_index": 2,
        "why": "120 mm is 120 000 µm, and 120 000 ÷ 60 = 2000; forgetting "
               "the mm-to-µm conversion gives ×2.",
    },
    {
        "id": "ks4-microscopy-s02",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A structure measures 40 mm long in a micrograph taken at "
                "×5000 magnification. Calculate its actual length in µm.",
        "options": [
            "8 µm",
            "0.8 µm",
            "80 µm",
            "800 µm",
        ],
        "correct_index": 0,
        "why": "40 ÷ 5000 = 0.008 mm, and 0.008 mm × 1000 = 8 µm.",
    },
    {
        "id": "ks4-microscopy-s03",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an electron microscope can show detail that a "
                "light microscope cannot.",
        "options": [
            "An electron beam is brighter than light, so the image is clearer",
            "Electron microscopes use thicker specimens, which hold more detail",
            "Electron microscopes add false colour, making structures stand out",
            "Electrons have a far shorter wavelength, giving a higher resolution",
        ],
        "correct_index": 3,
        "why": "Resolution is limited by wavelength, and an electron's "
               "wavelength is thousands of times shorter than light's.",
    },
    {
        "id": "ks4-microscopy-s04",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to watch a living pond organism swimming. "
                "Suggest which microscope should be used, and why.",
        "options": [
            "An electron microscope, because it gives the highest magnification",
            "A light microscope, because living specimens can be viewed with it",
            "A scanning electron microscope, because it shows the surface well",
            "A transmission electron microscope, because it shows inside the cell",
        ],
        "correct_index": 1,
        "why": "Electron beams work in a vacuum, so the specimen must be "
               "dead; only a light microscope can show something alive.",
    },
    {
        "id": "ks4-microscopy-h01",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chloroplast is 5 µm long. Calculate how long its image "
                "would be, in mm, at ×3000 magnification.",
        "options": [
            "1.5 mm",
            "15 mm",
            "150 mm",
            "15 000 mm",
        ],
        "correct_index": 1,
        "why": "5 µm × 3000 = 15 000 µm, and 15 000 ÷ 1000 = 15 mm; leaving "
               "the answer in µm gives the 15 000 option.",
    },
    {
        "id": "ks4-microscopy-h02",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students measure the same cell. One records the image "
                "as 36 mm and the actual size as 0.012 mm; the other records "
                "the image as 36 mm and the actual size as 12 µm. Compare "
                "the magnifications they calculate.",
        "options": [
            "The first gets ×3000 and the second ×3, because their units differ",
            "The first gets ×3 and the second ×3000, because their units differ",
            "The first gets ×3000 and the second ×300, a tenfold difference",
            "Both get ×3000, because 0.012 mm and 12 µm are the same length",
        ],
        "correct_index": 3,
        "why": "0.012 mm is 12 µm, so once the units match both calculations "
               "give 36 000 µm ÷ 12 µm = ×3000.",
    },
    {
        "id": "ks4-microscopy-h03",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that a microscope set to ×1 000 000 would "
                "show a ribosome clearly whatever its lenses were like. "
                "Evaluate this claim.",
        "options": [
            "Wrong — without enough resolution the image is only large and blurred",
            "Right — magnification on its own decides how much detail is seen",
            "Wrong — no microscope can ever reach a magnification of ×1 000 000",
            "Right — but only if the ribosome is stained with methylene blue",
        ],
        "correct_index": 0,
        "why": "Magnification without resolution just enlarges a blur; only "
               "resolution decides whether two close points stay separate.",
    },
    {
        "id": "ks4-microscopy-h04",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drawing of a cell carries a scale bar labelled 50 µm, and "
                "the bar itself measures 25 mm on the page. Determine the "
                "magnification of the drawing.",
        "options": [
            "×0.5",
            "×50",
            "×500",
            "×5000",
        ],
        "correct_index": 2,
        "why": "25 mm is 25 000 µm, and 25 000 ÷ 50 = 500, so the drawing is "
               "500 times life size.",
    },

    # ── chromosomes-mitosis ─────────────────────────────────────────────
    {
        "id": "ks4-chromosomes-mitosis-e01",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many pairs of chromosomes there are in a human "
                "body cell.",
        "options": [
            "23 pairs",
            "46 pairs",
            "22 pairs",
            "92 pairs",
        ],
        "correct_index": 0,
        "why": "46 chromosomes are arranged as 23 matching pairs, one of "
               "each pair from each parent.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e02",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a gene is.",
        "options": [
            "A whole molecule of DNA wound around its histone proteins",
            "A matching pair of chromosomes, one inherited from each parent",
            "A section of DNA that codes for one particular protein",
            "A copy of a chromosome made just before a cell divides",
        ],
        "correct_index": 2,
        "why": "A gene is a length of DNA carrying the code for a single "
               "protein; a chromosome carries many genes.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e03",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which phase of the cell cycle a cell spends most of "
                "its time in.",
        "options": [
            "Mitosis",
            "Cytokinesis",
            "The moment the chromosomes separate",
            "Interphase",
        ],
        "correct_index": 3,
        "why": "Interphase — growth, DNA replication and checking — is by "
               "far the longest part of the cell cycle.",
    },
    {
        "id": "ks4-chromosomes-mitosis-e04",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give the number of chromosomes in a human egg cell.",
        "options": [
            "46",
            "23",
            "92",
            "22",
        ],
        "correct_index": 1,
        "why": "Gametes are haploid, carrying 23 chromosomes, so that "
               "fertilisation restores the diploid 46.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s01",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "After DNA replication but before the cell divides, "
                "determine how many chromatids a human cell contains.",
        "options": [
            "23",
            "46",
            "69",
            "92",
        ],
        "correct_index": 3,
        "why": "Each of the 46 chromosomes has been copied, giving two "
               "chromatids each: 46 × 2 = 92.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s02",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Gut lining cells are replaced about every five days. "
                "Explain which process produces the replacements.",
        "options": [
            "Mitosis, which makes cells genetically identical to those lost",
            "Meiosis, which makes four new cells each time one cell divides",
            "Differentiation alone, with no cell division taking place at all",
            "Fertilisation, which makes new cells from two existing cells",
        ],
        "correct_index": 0,
        "why": "Replacing worn-out body cells needs identical copies, and "
               "mitosis is the division that produces them.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s03",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chemotherapy drugs kill rapidly dividing cells. Explain "
                "why a patient taking them often loses their hair.",
        "options": [
            "The drugs are carried in the blood and collect in hair follicles",
            "Hair follicle cells also divide rapidly, so the drugs affect them",
            "Hair follicle cells are the only healthy cells with a nucleus",
            "Hair follicle cells have already mutated in a cancer patient",
        ],
        "correct_index": 1,
        "why": "The drug cannot tell a tumour cell from any other fast "
               "divider, and hair follicle cells divide very fast.",
    },
    {
        "id": "ks4-chromosomes-mitosis-s04",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A strawberry plant grows new plants along runners, using "
                "mitosis only. Predict the genetic make-up of the new "
                "plants.",
        "options": [
            "Each new plant has half the chromosome number of the parent",
            "Each new plant is a mixture of the parent and a nearby plant",
            "Each new plant is genetically identical to the parent plant",
            "Each new plant has twice the chromosome number of the parent",
        ],
        "correct_index": 2,
        "why": "Mitosis copies the genome exactly, so offspring produced "
               "this way are clones of the parent.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h01",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cell must grow and make more organelles "
                "before it divides.",
        "options": [
            "So that the chromosomes have something to attach to as they move",
            "So that the cell can hold twice the usual number of chromosomes",
            "So that each daughter cell receives enough organelles to work",
            "So that the cell membrane becomes thin enough to pinch in two",
        ],
        "correct_index": 2,
        "why": "One cell's organelles are shared between two daughters, so "
               "the stock has to be built up first.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h02",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radiotherapy aims gamma rays at a tumour. Explain how this "
                "treats the cancer.",
        "options": [
            "The rays warm the tumour so that its cells can no longer respire",
            "The rays damage the DNA of tumour cells so they cannot divide",
            "The rays dissolve the tumour so that it drains away in the blood",
            "The rays make the immune system attack the tumour cells directly",
        ],
        "correct_index": 1,
        "why": "Gamma rays damage DNA, and a cell with badly damaged DNA "
               "cannot complete the cell cycle and divide.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h03",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that mitosis 'halves the chromosome number "
                "so that cells stay the right size'. Identify the error and "
                "give the correct statement.",
        "options": [
            "Mitosis keeps the number at 46; meiosis halves it, for gametes",
            "Mitosis halves the number to 23, and fertilisation restores it",
            "Mitosis doubles the number to 92, which is why cells grow first",
            "Mitosis takes one chromosome from each pair to make room to grow",
        ],
        "correct_index": 0,
        "why": "Mitosis is the division that keeps the chromosome number the "
               "same; only meiosis, which makes gametes, halves it.",
    },
    {
        "id": "ks4-chromosomes-mitosis-h04",
        "subtopic_slug": "chromosomes-mitosis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the cells produced by mitosis in a growing embryo "
                "with the cells produced by mitosis healing a cut.",
        "options": [
            "Embryo cells are all identical, while each wound cell has a mutation",
            "Embryo cells are haploid with 23 chromosomes; wound cells have 46",
            "Embryo cells divide by mitosis, while cells healing a wound use meiosis",
            "Both are genetically identical to the parent cell — only the purpose differs",
        ],
        "correct_index": 3,
        "why": "Mitosis is one process wherever it happens: identical "
               "daughter cells, whether the job is growth or repair.",
    },

    # ── stem-cells ──────────────────────────────────────────────────────
    {
        "id": "ks4-stem-cells-e01",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an undifferentiated cell.",
        "options": [
            "A cell that has lost its nucleus and can no longer divide",
            "A cell that has not yet become a particular specialised type",
            "A cell that has been damaged and can no longer do its job",
            "A cell that carries half the normal number of chromosomes",
        ],
        "correct_index": 1,
        "why": "Undifferentiated means the cell has not yet switched on the "
               "genes that would commit it to one specialised job.",
    },
    {
        "id": "ks4-stem-cells-e02",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which a whole new plant is grown from a "
                "small piece of meristem tissue.",
        "options": [
            "Tissue culture, which produces plants identical to the parent",
            "Fertilisation, which produces plants with two different parents",
            "Deamination, which removes waste from the growing young plant",
            "Differentiation, which halves the chromosome number first",
        ],
        "correct_index": 0,
        "why": "Tissue culture grows a clone from undifferentiated meristem "
               "cells, so every plant produced is genetically identical.",
    },
    {
        "id": "ks4-stem-cells-e03",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two properties that every stem cell has.",
        "options": [
            "It can divide, and it can travel to any tissue in the body",
            "It can divide, and it always carries just 23 chromosomes",
            "It can divide to make more of itself, and it can differentiate",
            "It can differentiate, and it can never be rejected by a patient",
        ],
        "correct_index": 2,
        "why": "Self-renewal and the ability to differentiate are what make a "
               "cell a stem cell.",
    },
    {
        "id": "ks4-stem-cells-e04",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of stem cell taken from a human embryo that "
                "is about five days old.",
        "options": [
            "A multipotent adult stem cell",
            "A specialised bone marrow cell",
            "A plant meristem cell",
            "A totipotent embryonic stem cell",
        ],
        "correct_index": 3,
        "why": "Cells in the inner mass of a 3–5 day embryo are embryonic "
               "stem cells, and they are totipotent.",
    },
    {
        "id": "ks4-stem-cells-s01",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why bone marrow stem cells cannot be used to grow "
                "new nerve cells for a patient.",
        "options": [
            "Adult stem cells cannot divide, so they produce no new cells",
            "Adult stem cells are always rejected by a patient's immune system",
            "They are multipotent — they make only the cell types of their tissue",
            "They are totipotent, so they would make every cell type at once",
        ],
        "correct_index": 2,
        "why": "Adult stem cells are multipotent: a bone marrow stem cell can "
               "make blood cells, but not cells of a different tissue.",
    },
    {
        "id": "ks4-stem-cells-s02",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain one advantage of treating a patient with their own "
                "adult stem cells rather than with donor stem cells.",
        "options": [
            "The patient's own stem cells are totipotent, while any donor cells are not",
            "The patient's own stem cells divide far faster than any donor cells",
            "The patient's own stem cells can be collected without any surgery",
            "The patient's own stem cells will not be rejected by their immune system",
        ],
        "correct_index": 3,
        "why": "Cells carrying the patient's own antigens are not recognised "
               "as foreign, so the immune system does not attack them.",
    },
    {
        "id": "ks4-stem-cells-s03",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower needs 5000 plants of one rare orchid variety, all "
                "identical. Suggest how meristem cells make this possible.",
        "options": [
            "Meristem cells can be crossed with pollen to give identical seeds",
            "Each small piece of meristem tissue grows into a whole new plant",
            "Meristem cells release a hormone that makes other plants split in two",
            "Meristem cells can be divided into gametes that each grow into a plant",
        ],
        "correct_index": 1,
        "why": "Meristem cells stay totipotent, so each small piece of tissue "
               "can be grown on into a complete, genetically identical plant.",
    },
    {
        "id": "ks4-stem-cells-s04",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says stem cell therapy works by 'growing a whole "
                "new organ and swapping it in'. Correct this statement.",
        "options": [
            "Stem cells differentiate into the cell types needed to repair a tissue",
            "Stem cells dissolve the damaged organ so that a healthy one can be fitted",
            "Stem cells carry new DNA into the damaged organ so it repairs itself",
            "Stem cells release enzymes that make the damaged organ divide again",
        ],
        "correct_index": 0,
        "why": "Stem cell treatments supply specific replacement cells that "
               "repair a tissue from within, not a ready-made organ.",
    },
    {
        "id": "ks4-stem-cells-h01",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One risk of treating a patient with embryonic stem cells is "
                "that some may stay undifferentiated. Explain why that "
                "matters.",
        "options": [
            "Undifferentiated cells cannot respire, so they die and then release toxins",
            "Undifferentiated cells would use up the patient's supply of nitrates",
            "Undifferentiated cells would turn nearby cells back into stem cells",
            "Undifferentiated cells may keep dividing uncontrollably and form a tumour",
        ],
        "correct_index": 3,
        "why": "A cell that never commits to a job keeps dividing, and "
               "uncontrolled division is exactly what a tumour is.",
    },
    {
        "id": "ks4-stem-cells-h02",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the UK, research on human embryos is allowed only up to "
                "14 days of development. Evaluate the purpose of this limit.",
        "options": [
            "It makes sure the embryos being used are old enough to give usable stem cells",
            "It guarantees the stem cells produced can never be rejected",
            "It balances the possible medical benefits against respect for the embryo",
            "It stops researchers using embryos left over from IVF treatment",
        ],
        "correct_index": 2,
        "why": "The limit is a compromise: research that could cure disease is "
               "permitted, but only within a boundary set out of respect for the embryo.",
    },
    {
        "id": "ks4-stem-cells-h03",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why replacing a diabetic patient's insulin-producing "
                "cells using stem cells could be better than daily insulin "
                "injections.",
        "options": [
            "New cells would release insulin in response to the blood glucose level",
            "New cells would remove all of the glucose from the bloodstream permanently",
            "Injected insulin is broken down before it ever reaches the blood",
            "Injected insulin cannot be manufactured in large enough quantities",
        ],
        "correct_index": 0,
        "why": "Replacement cells respond moment to moment to blood glucose, "
               "which a fixed injection cannot do.",
    },
    {
        "id": "ks4-stem-cells-h04",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher argues that using leftover IVF embryos is "
                "acceptable because they would be destroyed anyway. Evaluate "
                "this argument.",
        "options": [
            "It fails, because IVF clinics do not produce any spare embryos at all",
            "It has force, but does not answer the objection that an embryo cannot consent",
            "It settles the whole matter, because no reasonable objection to it then remains",
            "It fails, because embryos from IVF are too old to yield usable stem cells",
        ],
        "correct_index": 1,
        "why": "The argument answers the 'wasted life' objection but leaves "
               "the consent objection untouched, so it is partial, not decisive.",
    },

    # ── transport-in-cells ──────────────────────────────────────────────
    {
        "id": "ks4-transport-in-cells-e01",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens once diffusion has reached equilibrium.",
        "options": [
            "Particles stop moving completely on both sides of the membrane",
            "Particles move only from the left-hand side to the right-hand side",
            "Particles keep moving randomly, but there is no net movement",
            "Particles start to move from low concentration to high concentration",
        ],
        "correct_index": 2,
        "why": "Random movement never stops; at equilibrium as many particles "
               "cross each way, so there is no net movement.",
    },
    {
        "id": "ks4-transport-in-cells-e02",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of protein in a cell membrane that active "
                "transport needs.",
        "options": [
            "Enzyme proteins",
            "Haemoglobin proteins",
            "Histone proteins",
            "Carrier proteins",
        ],
        "correct_index": 3,
        "why": "Carrier proteins in the membrane use ATP to move substances "
               "against a concentration gradient.",
    },
    {
        "id": "ks4-transport-in-cells-e03",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to an animal cell placed in pure water.",
        "options": [
            "It shrinks, and its membrane pulls away from its cell wall",
            "It takes in water by osmosis, swells, and may burst",
            "It stays the same size, because water cannot cross its membrane",
            "It loses water, because pure water is the more concentrated solution",
        ],
        "correct_index": 1,
        "why": "With no cell wall to resist the pressure, an animal cell "
               "swells as water enters by osmosis and can burst.",
    },
    {
        "id": "ks4-transport-in-cells-e04",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the term for a plant cell that is firm because its "
                "vacuole is full of water.",
        "options": [
            "Turgid",
            "Flaccid",
            "Plasmolysed",
            "Crenated",
        ],
        "correct_index": 0,
        "why": "A turgid cell has its contents pressed hard against the cell "
               "wall, and turgid cells hold a plant upright.",
    },
    {
        "id": "ks4-transport-in-cells-s01",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the pair of changes that would each increase the "
                "rate of diffusion across a membrane.",
        "options": [
            "A lower temperature and a smaller surface area",
            "A higher temperature and a steeper concentration gradient",
            "A thicker membrane and a shallower concentration gradient",
            "A lower temperature and a thicker membrane to cross",
        ],
        "correct_index": 1,
        "why": "Heat gives particles more kinetic energy and a steeper "
               "gradient means a bigger difference to move down.",
    },
    {
        "id": "ks4-transport-in-cells-s02",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how urea moves out of liver cells and into the "
                "blood.",
        "options": [
            "It diffuses down a gradient, being more concentrated in the cells",
            "It is pumped by active transport, using ATP made in the liver",
            "It moves by osmosis, because the blood is more concentrated",
            "It is carried by carrier proteins, because urea cannot diffuse",
        ],
        "correct_index": 0,
        "why": "Urea is made in the liver, so it is more concentrated there "
               "and simply diffuses down the gradient into the blood.",
    },
    {
        "id": "ks4-transport-in-cells-s03",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the wall of an alveolus is only one cell thick.",
        "options": [
            "So that each alveolus can hold more air than a thicker wall would",
            "So that the alveoli can be squeezed flat and then refilled again",
            "So that oxygen has only a short distance to diffuse into the blood",
            "So that less energy is needed, as thin walls use less ATP to keep",
        ],
        "correct_index": 2,
        "why": "A short diffusion path means oxygen crosses into the blood "
               "quickly — one of the features of every good exchange surface.",
    },
    {
        "id": "ks4-transport-in-cells-s04",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is bathed in a solution containing cyanide, which "
                "stops aerobic respiration. Predict which process across its "
                "membrane stops first.",
        "options": [
            "Diffusion, because it needs the energy released by respiration",
            "Osmosis, because water can only cross a membrane by using ATP",
            "All three processes, because none of them can work without ATP",
            "Active transport, because it is the only one that uses ATP",
        ],
        "correct_index": 3,
        "why": "Diffusion and osmosis are passive; only active transport "
               "depends on ATP, so only it stops when respiration stops.",
    },
    {
        "id": "ks4-transport-in-cells-h01",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Root hair cells take in nitrate ions from soil water even "
                "though nitrate is already more concentrated inside the cell. "
                "Explain how.",
        "options": [
            "By active transport — carrier proteins use ATP to pump ions in",
            "By diffusion — ions always move into a cell whatever the gradient",
            "By osmosis — the water carries the dissolved nitrate ions in with it",
            "By diffusion through the cell wall, which is thin enough for ions",
        ],
        "correct_index": 0,
        "why": "Moving a substance from a lower to a higher concentration is "
               "active transport, and it costs ATP from respiration.",
    },
    {
        "id": "ks4-transport-in-cells-h02",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two potato samples of equal mass are put in the same "
                "sucrose solution — one a whole cylinder, one cut into small "
                "pieces. Predict which loses mass faster, and why.",
        "options": [
            "The whole cylinder, because its cells are packed more tightly",
            "The cut pieces, because they have a greater surface area for osmosis",
            "The whole cylinder, because water can travel further along it",
            "Neither — surface area has no effect at all on the rate of osmosis",
        ],
        "correct_index": 1,
        "why": "Cutting the potato up exposes far more surface, and a larger "
               "surface area means water leaves by osmosis faster.",
    },
    {
        "id": "ks4-transport-in-cells-h03",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single-celled organism absorbs all its oxygen straight "
                "across its surface, but a mouse cannot. Explain the "
                "difference.",
        "options": [
            "The mouse's cells cannot use diffusion, so it needs active transport",
            "The mouse has a much larger surface area, which slows diffusion down",
            "The single-celled organism uses no oxygen, so it absorbs none at all",
            "The mouse has far less surface for its volume, and a longer path in",
        ],
        "correct_index": 3,
        "why": "A large organism has a low surface area to volume ratio and a "
               "long way to its inner cells, so it needs exchange surfaces.",
    },
    {
        "id": "ks4-transport-in-cells-h04",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Late in digestion, most glucose in the small intestine has "
                "already been absorbed. Explain how the rest is still taken "
                "into the blood.",
        "options": [
            "By osmosis, because the blood is now more concentrated than the gut",
            "By diffusion, because glucose always moves from the gut into blood",
            "By active transport, moving glucose from a low to a higher level",
            "It is not absorbed — the glucose left over passes out as waste",
        ],
        "correct_index": 2,
        "why": "Once the gut is more dilute than the blood, only active "
               "transport can move the remaining glucose against the gradient.",
    },

    # ── culturing-microorganisms ────────────────────────────────────────
    {
        "id": "ks4-culturing-microorganisms-e01",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gel, made from seaweed, used as a culture medium "
                "in a Petri dish.",
        "options": [
            "Gelatin",
            "Cellulose",
            "Starch",
            "Agar",
        ],
        "correct_index": 3,
        "why": "Agar is the seaweed gel that nutrients are dissolved into "
               "before it sets in the dish.",
    },
    {
        "id": "ks4-culturing-microorganisms-e02",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the temperature at which an autoclave sterilises "
                "Petri dishes and culture media.",
        "options": [
            "25 °C",
            "121 °C",
            "37 °C",
            "100 °C",
        ],
        "correct_index": 1,
        "why": "An autoclave uses steam under pressure at 121 °C, hot enough "
               "to kill bacterial spores as well as bacteria.",
    },
    {
        "id": "ks4-culturing-microorganisms-e03",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the nutrient a culture medium must supply so that "
                "bacteria can build proteins.",
        "options": [
            "A nitrogen source, such as nitrate ions",
            "A carbon source, such as glucose",
            "Distilled water, added to the agar",
            "Vitamins, added in small amounts",
        ],
        "correct_index": 0,
        "why": "Amino acids contain nitrogen, so protein synthesis needs a "
               "nitrogen source in the medium as well as a sugar for energy.",
    },
    {
        "id": "ks4-culturing-microorganisms-e04",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what it means when no clear zone forms around an "
                "antibiotic disc.",
        "options": [
            "The antibiotic diffused too far and spread over the whole plate",
            "The plate was left unsealed, so contaminants filled in the zone",
            "The bacteria on that plate are resistant to that antibiotic",
            "The antibiotic killed every bacterium on the whole of the plate",
        ],
        "correct_index": 2,
        "why": "No zone means the bacteria grew right up to the disc, so that "
               "antibiotic does not stop them — they are resistant.",
    },
    {
        "id": "ks4-culturing-microorganisms-s01",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a Petri dish lid is lifted only slightly and "
                "briefly during inoculation.",
        "options": [
            "To reduce the chance of airborne microorganisms landing on the agar",
            "To stop the agar from drying out and cracking during the transfer",
            "To keep the inside of the dish warm enough for the bacteria to grow",
            "To prevent the antibiotic on the discs from evaporating into the air",
        ],
        "correct_index": 0,
        "why": "Every second the dish is open is a chance for a contaminant "
               "to settle on the agar and spoil the result.",
    },
    {
        "id": "ks4-culturing-microorganisms-s02",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain the purpose of a disc soaked only in distilled "
                "water on an agar plate.",
        "options": [
            "It keeps the agar moist so that the bacteria growing do not dry out",
            "It provides the water that the bacteria need in order to grow a lawn",
            "It dilutes any antibiotic that has spread too far across the plate",
            "It is a control: a clear zone must be due to the substance, not the disc",
        ],
        "correct_index": 3,
        "why": "The water disc shows the filter paper itself causes no "
               "inhibition, so any zone elsewhere is due to the substance.",
    },
    {
        "id": "ks4-culturing-microorganisms-s03",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "One bacterium divides every 20 minutes. Calculate how many "
                "bacteria are present after 3 hours.",
        "options": [
            "9 bacteria",
            "18 bacteria",
            "512 bacteria",
            "180 bacteria",
        ],
        "correct_index": 2,
        "why": "3 hours is 180 minutes, which is 9 divisions, and the number "
               "doubles each time: 2 to the power 9 = 512.",
    },
    {
        "id": "ks4-culturing-microorganisms-s04",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the neck of a culture bottle is passed through "
                "a Bunsen flame before the bottle is opened.",
        "options": [
            "To warm the culture so that the bacteria become active for transfer",
            "To kill any microorganisms on the rim that could fall into the culture",
            "To make a current of air that draws contaminants down into the bottle",
            "To soften the glass so that the lid can be removed without cracking",
        ],
        "correct_index": 1,
        "why": "Flaming the rim destroys microorganisms sitting on the glass "
               "that would otherwise drop straight into the culture.",
    },
    {
        "id": "ks4-culturing-microorganisms-h01",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An inhibition zone has a diameter of 20 mm. Calculate its "
                "area, giving your answer to 3 significant figures.",
        "options": [
            "31.4 mm\u00b2",
            "314 mm\u00b2",
            "1260 mm\u00b2",
            "62.8 mm\u00b2",
        ],
        "correct_index": 1,
        "why": "The radius is 10 mm, so area = \u03c0 \u00d7 10\u00b2 = 314 mm\u00b2; "
               "using the diameter as the radius gives 1260 mm\u00b2.",
    },
    {
        "id": "ks4-culturing-microorganisms-h02",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Antibiotic A gives an inhibition zone of radius 6 mm and "
                "antibiotic B a zone of radius 12 mm. Determine how many "
                "times larger the area of B's zone is.",
        "options": [
            "Twice as large",
            "Three times as large",
            "Four times as large",
            "Six times as large",
        ],
        "correct_index": 2,
        "why": "Area depends on the radius squared, so doubling the radius "
               "makes the area 2 squared = 4 times larger.",
    },
    {
        "id": "ks4-culturing-microorganisms-h03",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student decides to incubate a school agar plate at 37 °C "
                "so that the bacteria grow faster. Evaluate this decision.",
        "options": [
            "Sensible — 37 °C is the optimum growth temperature, so the results come through sooner",
            "Sensible — the agar gel sets more firmly at 37 °C than it does at 25 °C",
            "Unwise — the antibiotics used in schools break down above about 30 °C",
            "Unwise — it favours bacteria that grow at body temperature, which may harm people",
        ],
        "correct_index": 3,
        "why": "School plates are held at 25 °C precisely so that organisms "
               "suited to the human body are not encouraged to grow.",
    },
    {
        "id": "ks4-culturing-microorganisms-h04",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A clear inhibition zone forms around the antibiotic disc, "
                "but a second, fluffy kind of colony grows right across the "
                "plate, including inside that clear zone. Suggest the most "
                "likely explanation.",
        "options": [
            "The plate was contaminated by an airborne organism the antibiotic does not affect",
            "The antibiotic disc was too weak, so it inhibited nothing at all",
            "The agar was poured too thinly for a clear zone ever to appear",
            "The bacteria had not been spread evenly across the agar surface",
        ],
        "correct_index": 0,
        "why": "A zone did form, so the antibiotic worked on the bacteria "
               "spread on the plate; a different organism growing through it "
               "must have arrived from outside.",
    },
]
