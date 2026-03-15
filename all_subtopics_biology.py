#!/usr/bin/env python3
"""
Biology subtopics — Combined Foundation
AQA 8464 / Biology 8461

Cell Biology:          7 subtopics (updated)
Organisation:         11 subtopics (updated)
Infection & Response:  8 subtopics (updated)
Bioenergetics:         7 subtopics (updated)
Homeostasis:           8 subtopics (updated)
Inheritance:          12 subtopics (updated)
Ecology: unchanged
"""

BIOLOGY_COLOR = "#6BCB77"

BIOLOGY_SUBTOPICS_ALL = {

"cell-biology": [


    # ═══════════════════════════════════════════════
    # 1. EUKARYOTES AND PROKARYOTES
    # ═══════════════════════════════════════════════
    {
        "id": "eukaryotes-prokaryotes",
        "title": "Eukaryotes and Prokaryotes",
        "spec": "4.1.1.1",
        "summary": "Compare the key features of eukaryotic and prokaryotic cells, including scale and size.",
        "theory": [
            {
                "heading": "The Two Fundamental Types of Cell",
                "content": "Every living organism on Earth is made of one of two fundamentally different types of cell: eukaryotic or prokaryotic.\nThe single most important difference between them is whether the cell has a TRUE NUCLEUS — a membrane-bound compartment containing the DNA.\nEukaryotic cells HAVE a nucleus. Prokaryotic cells DO NOT.\nThis distinction is so fundamental that it defines two of the largest groupings of life on Earth."
            },
            {
                "heading": "Eukaryotic Cells",
                "content": "Eukaryotic cells are larger, more complex cells that have:\n• A true nucleus — DNA enclosed in a nuclear membrane.\n• Membrane-bound organelles — mitochondria, endoplasmic reticulum, Golgi apparatus etc.\n• A cytoskeleton — internal protein framework.\nAll animals, plants, fungi and protists are made of eukaryotic cells.\nTypical size: 10–100 micrometres (µm).\nThe nucleus protects DNA and allows its activity to be carefully regulated."
            },
            {
                "heading": "Prokaryotic Cells — Bacteria",
                "content": "Prokaryotic cells are smaller and simpler. All bacteria are prokaryotes.\nKey features:\n• NO nucleus — DNA is a SINGLE CIRCULAR LOOP floating free in the cytoplasm.\n• NO membrane-bound organelles — no mitochondria, no chloroplasts.\n• DO have: cytoplasm, a cell membrane, a cell wall (made of peptidoglycan — not cellulose), and ribosomes (smaller than eukaryotic ribosomes).\n• May also have: PLASMIDS (small extra circular loops of DNA, not essential for survival), a FLAGELLUM (rotating tail for movement), and a CAPSULE (slimy outer layer for protection and attachment).\nTypical size: 1–10 µm — roughly 10× smaller than a typical animal cell."
            },
            {
                "heading": "Why Size Matters — Surface Area to Volume Ratio",
                "content": "The small size of prokaryotic cells gives them a very HIGH surface area to volume ratio (SA:V).\nThis means that relative to their volume, bacteria have a lot of membrane surface available for absorbing nutrients and removing waste.\nThis is one reason bacteria can grow and reproduce extremely fast — every 20 minutes under ideal conditions.\nLarger eukaryotic cells have a lower SA:V ratio — they need specialised exchange surfaces and transport systems (e.g. lungs, circulatory system) to move substances efficiently."
            },
            {
                "heading": "Units and Scale",
                "content": "Working with cells requires understanding very small units:\n• 1 metre (m) = 1,000 millimetres (mm)\n• 1 mm = 1,000 micrometres (µm)\n• 1 µm = 1,000 nanometres (nm)\nSo: 1 m = 1,000,000 µm = 1,000,000,000 nm\nTypical sizes to remember:\n• Animal cell: ~20 µm\n• Plant cell: ~40–80 µm\n• Bacterium: ~1–5 µm\n• Virus: ~0.1 µm (100 nm)\n• Ribosome: ~20 nm\nYou need to be able to convert between these units and use them in magnification calculations."
            }
        ],
        "variables": [
            ("M", "Magnification", "no unit", "×"),
            ("I", "Image size", "mm or µm", "mm / µm"),
            ("A", "Actual size", "mm or µm", "mm / µm"),
        ],
        "equations": ["Magnification (M) = Image size (I) ÷ Actual size (A)"],
        "common_mistake": "Prokaryotic cells have NO nucleus and NO membrane-bound organelles. Students often write 'bacteria have a nucleus' — they do not. The DNA is a single circular loop loose in the cytoplasm. Also: the bacterial cell wall is made of PEPTIDOGLYCAN, not cellulose (cellulose = plant cell walls).",
        "key_note": "Eukaryote = nucleus present. Prokaryote = no nucleus, DNA floats free. Size: bacterium ~1–5 µm; animal cell ~20 µm; plant cell ~40–80 µm. Units: 1 mm = 1000 µm.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Eukaryote or Prokaryote?",
            "instruction": "Sort each feature — does it belong to eukaryotic cells, prokaryotic cells, or both?",
            "pairs": [
                ("Eukaryote only", "Has a true membrane-bound nucleus containing DNA"),
                ("Prokaryote only", "DNA is a single circular loop floating in cytoplasm"),
                ("Prokaryote only", "May have plasmids — small extra circular DNA rings"),
                ("Eukaryote only", "Contains mitochondria for aerobic respiration"),
                ("Both", "Has a cell membrane and cytoplasm"),
                ("Both", "Contains ribosomes for protein synthesis"),
            ]
        },
        "fifas": [
            {
                "label": "Magnification Calculation",
                "question": "A bacterium is drawn 30 mm long in a diagram. Its actual length is 0.003 mm. Calculate the magnification.",
                "steps": [
                    ("F", "Magnification = Image size ÷ Actual size"),
                    ("I", "M = 30 ÷ 0.003"),
                    ("F", "Both values already in mm — no conversion needed"),
                    ("A", "Magnification = ×10,000")
                ]
            },
            {
                "label": "Finding Actual Size",
                "question": "A cell is shown at ×500 magnification and measures 10 mm in the image. Calculate the actual size in µm.",
                "steps": [
                    ("F", "Actual size = Image size ÷ Magnification"),
                    ("I", "A = 10 mm ÷ 500 = 0.02 mm"),
                    ("F", "Convert to µm: 0.02 mm × 1000 = 20 µm"),
                    ("A", "Actual size = 20 µm")
                ]
            }
        ],
        "quiz": [
            {
                "q": "What is the key structural difference between eukaryotic and prokaryotic cells?",
                "opts": [
                    ("Eukaryotes have a membrane-bound nucleus; prokaryotes do not", True),
                    ("Prokaryotes are larger and more complex than eukaryotes", False),
                    ("Eukaryotes have no cell membrane", False),
                    ("Prokaryotes have mitochondria but eukaryotes do not", False)
                ],
                "wrong_explanations": {
                    1: "Prokaryotes are SMALLER and SIMPLER — roughly 10× smaller than a typical animal cell.",
                    2: "ALL cells have a cell membrane — it is the universal feature of all living cells.",
                    3: "It is the OPPOSITE — eukaryotes have mitochondria. Prokaryotes have NO membrane-bound organelles at all."
                }
            },
            {
                "q": "A bacterium is approximately 2 µm in length. How does this compare to a typical animal cell?",
                "opts": [
                    ("The animal cell is roughly 10× larger — approximately 20 µm", True),
                    ("They are about the same size", False),
                    ("The bacterium is larger — bacteria are bigger than animal cells", False),
                    ("The animal cell is 1000× larger than the bacterium", False)
                ],
                "wrong_explanations": {
                    1: "They are definitely not the same size — a bacterium at 2 µm vs an animal cell at ~20 µm is a clear 10× size difference.",
                    2: "Bacteria are SMALLER — roughly 10× smaller than animal cells, not larger.",
                    3: "1000× larger would make the animal cell 2000 µm — about 2 mm! Animal cells are only ~10× larger, not 1000×."
                }
            },
            {
                "q": "Which of the following is found in a bacterial cell but NOT in a typical animal cell?",
                "opts": [
                    ("Plasmids", True),
                    ("Mitochondria", False),
                    ("A nucleus", False),
                    ("A cell membrane", False)
                ],
                "wrong_explanations": {
                    1: "Animal cells have mitochondria for aerobic respiration — bacteria do not have mitochondria.",
                    2: "Animal cells HAVE a nucleus — bacteria do not. The question asks what bacteria have that animal cells don't.",
                    3: "Both animal cells AND bacteria have a cell membrane — it is a universal feature."
                }
            },
            {
                "q": "1 mm is equal to how many micrometres (µm)?",
                "opts": [
                    ("1,000 µm", True),
                    ("100 µm", False),
                    ("1,000,000 µm", False),
                    ("10 µm", False)
                ],
                "wrong_explanations": {
                    1: "100 µm = 0.1 mm. The conversion is 1 mm = 1000 µm.",
                    2: "1,000,000 µm = 1 metre. The conversion you need is: 1 mm = 1000 µm.",
                    3: "10 µm = 0.01 mm. Remember: milli means one thousandth, so 1 mm = 1000 µm."
                }
            },
            {
                "q": "What is a flagellum in a bacterial cell?",
                "opts": [
                    ("A rotating tail-like structure used for movement", True),
                    ("A small ring of extra DNA used for genetic transfer", False),
                    ("A thick outer layer that protects the bacterium", False),
                    ("The region of cytoplasm where the DNA is stored", False)
                ],
                "wrong_explanations": {
                    1: "A small ring of extra DNA = a PLASMID, not a flagellum.",
                    2: "A thick outer protective layer = the CAPSULE (or cell wall). The flagellum is the structure for movement.",
                    3: "The region where DNA sits loosely in the cytoplasm is called the nucleoid region — the flagellum is an external motor structure."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 2. ANIMAL AND PLANT CELLS
    # ═══════════════════════════════════════════════
    {
        "id": "animal-plant-cells",
        "title": "Animal and Plant Cells",
        "spec": "4.1.1.2",
        "summary": "Describe the sub-cellular structures of animal and plant cells and relate structure to function.",
        "theory": [
            {
                "heading": "Animal Cell Structures and Functions",
                "content": "All animal cells contain these five essential structures:\n\nNUCLEUS: contains the cell's DNA, organised into chromosomes. The nucleus controls all cell activity by determining which proteins are made. It has a double membrane called the nuclear envelope with pores that allow molecules to pass in and out.\n\nCELL MEMBRANE: a thin, flexible layer made of phospholipids and proteins. It controls what enters and leaves the cell — it is selectively permeable. It also plays a role in communication between cells.\n\nCYTOPLASM: a watery, gel-like substance that fills the cell. Most chemical reactions happen here. It contains dissolved enzymes, salts, sugars and other molecules, as well as all the organelles.\n\nMITOCHONDRIA: oval-shaped organelles with a folded inner membrane (cristae). This is where aerobic respiration occurs — glucose is broken down using oxygen to release energy as ATP. Cells that are very active (muscle cells, sperm cells, liver cells) have many more mitochondria than less active cells.\n\nRIBOSOMES: tiny structures found either floating in the cytoplasm or attached to the endoplasmic reticulum. This is where PROTEIN SYNTHESIS takes place — amino acids are joined in a specific sequence to build proteins. Every cell needs proteins, so all cells have ribosomes."
            },
            {
                "heading": "Plant Cells — What's Extra",
                "content": "Plant cells have all five animal cell structures PLUS up to three additional ones:\n\nCELL WALL: a rigid outer layer made of cellulose fibres. It surrounds the cell membrane and gives the cell a fixed shape. It prevents the cell from bursting when it absorbs water by osmosis — the wall resists the pressure. This is what makes plants structurally rigid (along with turgor pressure).\n\nCHLOROPLASTS: oval-shaped organelles containing the green pigment chlorophyll. Chlorophyll absorbs light energy, which is used to drive photosynthesis — converting CO₂ and water into glucose. IMPORTANT: only cells that are exposed to light have chloroplasts. Root cells, storage cells (e.g. in potato tubers) and cells deep inside stems do NOT have chloroplasts.\n\nPERMANENT VACUOLE: a large central compartment in mature plant cells, filled with cell sap (a solution of sugars, salts and pigments). The vacuole pushes against the cell wall and contributes to TURGOR PRESSURE — the pressure that keeps plant cells firm and gives the plant structural support. Without water in the vacuole, the plant wilts."
            },
            {
                "heading": "Why Structure Matches Function",
                "content": "The key principle to understand is that every structural feature exists because it serves a specific function.\n\nMore mitochondria = more aerobic respiration = more ATP energy. Cells with high energy demands (muscle, sperm, liver) have the most mitochondria.\n\nMore chloroplasts = more photosynthesis. Palisade mesophyll cells in leaves have up to 70 chloroplasts — they are the main photosynthetic cells of the plant.\n\nLarge vacuole = more turgor pressure = firmer cell. This is why plants wilt when they lose water — the vacuoles deflate and cells lose their rigidity.\n\nCell wall + vacuole together = turgid plant cell that holds its shape and provides structural support to the whole plant."
            },
            {
                "heading": "Using a Light Microscope to Observe Cells",
                "content": "To observe cells under a light microscope:\n1. Prepare a thin section of tissue (e.g. onion epidermis, cheek cells).\n2. Place on a glass slide with a drop of water or mounting fluid.\n3. Add a coverslip carefully to avoid air bubbles.\n4. Apply a stain if needed — iodine solution stains starch and nuclei blue/purple; methylene blue stains nuclei of animal cells.\n5. Focus using the coarse adjustment knob first, then the fine adjustment.\nYou can observe with a light microscope: nucleus, cytoplasm, cell wall, vacuole, chloroplasts.\nYou CANNOT see clearly: individual ribosomes (too small), cell membrane detail, internal mitochondria structure."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "NOT all plant cells have chloroplasts — ONLY cells exposed to light. Root cells are underground so never receive light and have NO chloroplasts. Students also often forget that plant cells have a cell wall AND a cell membrane — both are present. The cell wall is outside, the cell membrane is inside it.",
        "key_note": "Animal cells: nucleus, cell membrane, cytoplasm, mitochondria, ribosomes. Plant cells: all of the above PLUS cell wall (cellulose), chloroplasts (light-exposed cells only), permanent vacuole.",
        "higher": None,
        "triple_only": None,
        "rp": "RP1 — Use a light microscope to observe, draw and label plant and animal cells. Include a scale bar and calculate magnification.",
        "matching": {
            "title": "Match the Organelle to its Function",
            "instruction": "Drag each function to match the correct organelle.",
            "pairs": [
                ("Nucleus", "Contains DNA in chromosomes — controls all cell activity"),
                ("Cell membrane", "Selectively permeable barrier — controls what enters and leaves"),
                ("Mitochondria", "Site of aerobic respiration — releases energy as ATP"),
                ("Ribosomes", "Site of protein synthesis — builds proteins from amino acids"),
                ("Cell wall", "Made of cellulose — rigid support, prevents cell bursting"),
                ("Chloroplasts", "Contain chlorophyll — absorb light energy for photosynthesis"),
                ("Permanent vacuole", "Filled with cell sap — contributes to turgor pressure"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Which organelle is responsible for protein synthesis?",
                "opts": [
                    ("Ribosomes", True),
                    ("Mitochondria", False),
                    ("Nucleus", False),
                    ("Chloroplasts", False)
                ],
                "wrong_explanations": {
                    1: "Mitochondria are the site of aerobic RESPIRATION — they release energy from glucose, they don't make proteins.",
                    2: "The nucleus contains the DNA instructions for making proteins, but the actual assembly of amino acids into proteins happens at RIBOSOMES.",
                    3: "Chloroplasts carry out PHOTOSYNTHESIS — capturing light energy to make glucose. Not involved in protein synthesis."
                }
            },
            {
                "q": "A student looks at a plant cell from a root. They expect to see chloroplasts but find none. Why?",
                "opts": [
                    ("Root cells are underground — no light reaches them, so chloroplasts are not present", True),
                    ("Root cells are too small to contain chloroplasts", False),
                    ("Root cells are prokaryotic and cannot have chloroplasts", False),
                    ("Chloroplasts are only present in animal cells", False)
                ],
                "wrong_explanations": {
                    1: "Root cells are eukaryotic plant cells — size is not the reason. Palisade cells are similar in size and have many chloroplasts.",
                    2: "ALL plant cells are eukaryotic. Root cells are plant cells — they are eukaryotic. Only bacteria (and other prokaryotes) lack membrane-bound organelles.",
                    3: "Chloroplasts are found in PLANT cells — not animal cells. Animal cells never have chloroplasts."
                }
            },
            {
                "q": "What is the function of the permanent vacuole in a plant cell?",
                "opts": [
                    ("Filled with cell sap — contributes to turgor pressure, keeping the cell firm", True),
                    ("Stores chlorophyll for photosynthesis", False),
                    ("Acts as the site of aerobic respiration", False),
                    ("Controls what enters and leaves the cell", False)
                ],
                "wrong_explanations": {
                    1: "Chlorophyll is stored in CHLOROPLASTS — not the vacuole. The vacuole contains cell sap (sugars and salts).",
                    2: "Aerobic respiration occurs in MITOCHONDRIA. The vacuole is a storage compartment.",
                    3: "Controlling what enters and leaves = the CELL MEMBRANE. The vacuole is a storage structure filled with cell sap."
                }
            },
            {
                "q": "Which of the following is present in both animal and plant cells?",
                "opts": [
                    ("Mitochondria", True),
                    ("Cell wall", False),
                    ("Chloroplasts", False),
                    ("Permanent vacuole", False)
                ],
                "wrong_explanations": {
                    1: "Cell walls are only found in plant cells (and bacteria, fungi) — NOT in animal cells.",
                    2: "Chloroplasts are found only in plant cells that are exposed to light. Animal cells never have chloroplasts.",
                    3: "The permanent vacuole is a plant cell feature — animal cells do not have a large permanent vacuole (though they may have small temporary vacuoles)."
                }
            },
            {
                "q": "Why do very active muscle cells contain many more mitochondria than skin cells?",
                "opts": [
                    ("Muscle cells need much more ATP energy for contraction — more mitochondria produce more ATP", True),
                    ("Muscle cells are larger, so they need more organelles to fill the space", False),
                    ("Mitochondria help muscle cells to absorb oxygen from the blood", False),
                    ("Skin cells don't respire — they don't need mitochondria at all", False)
                ],
                "wrong_explanations": {
                    1: "Cell size doesn't directly dictate organelle number — it is energy demand that determines mitochondria count.",
                    2: "Oxygen is absorbed by diffusion through the cell membrane — mitochondria USE oxygen in respiration, they don't absorb it.",
                    3: "All living cells respire all the time — skin cells do have mitochondria. Active cells simply have FAR MORE."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 3. CELL SPECIALISATION
    # ═══════════════════════════════════════════════
    {
        "id": "cell-specialisation",
        "title": "Cell Specialisation and Differentiation",
        "spec": "4.1.1.3",
        "summary": "Explain how and why cells become specialised, with examples from animals and plants.",
        "theory": [
            {
                "heading": "What is Cell Differentiation?",
                "content": "All multicellular organisms begin life as a single fertilised egg cell (zygote). This one cell divides repeatedly by mitosis to produce all the billions of cells in the organism.\nAs cells divide, they become progressively more specialised — this process is called DIFFERENTIATION.\nDifferentiation means a cell switches on certain genes and switches off others, causing it to develop a specific structure suited to a specific function.\nThe result: specialised cells that are experts at one job, making the whole organism far more efficient.\nIn ANIMALS: most differentiation occurs early during embryonic development. Once differentiated, most animal cells lose the ability to become a different type — they are committed.\nIn PLANTS: differentiation can continue throughout the plant's life. Meristem cells (at root and shoot tips) remain undifferentiated and can keep producing new specialised cells."
            },
            {
                "heading": "Specialised Animal Cells",
                "content": "SPERM CELL — function: swim to and fertilise an egg.\nAdaptations:\n• Streamlined head — reduces drag when swimming.\n• Flagellum (tail) — rotates to propel the sperm through fluid.\n• Many mitochondria in the midpiece — aerobic respiration provides ATP energy for swimming.\n• Acrosome (cap on the head) — contains enzymes that digest through the egg's outer membrane.\n• Haploid nucleus — contains only 23 chromosomes (half the normal number) so that after fertilisation the normal 46 is restored.\n\nRED BLOOD CELL (erythrocyte) — function: carry oxygen from lungs to tissues.\nAdaptations:\n• Biconcave disc shape — large surface area for oxygen absorption; thin centre = short diffusion distance for O₂.\n• No nucleus — creates more space for HAEMOGLOBIN, the oxygen-carrying protein.\n• Flexible — can squeeze through narrow capillaries without tearing.\n• Packed with haemoglobin — each cell contains ~270 million haemoglobin molecules.\n\nNEURONE (nerve cell) — function: transmit electrical impulses rapidly over long distances.\nAdaptations:\n• Very long axon — can be over a metre long (e.g. sciatic nerve), allowing signals to travel from brain to toe without interruption.\n• Myelin sheath — fatty insulating layer that speeds up impulse conduction (signals jump between gaps called nodes of Ranvier).\n• Dendrites — short branching fibres that receive signals from other neurones.\n• Synaptic terminals — the axon ends in bulb-like structures that release neurotransmitters to communicate with the next cell.\n\nMUSCLE CELL — function: contract to produce movement.\nAdaptations:\n• Contains contractile proteins (actin and myosin) that slide past each other to shorten the cell.\n• Many mitochondria — large energy demand for constant contraction.\n• Can store glycogen as an energy reserve."
            },
            {
                "heading": "Specialised Plant Cells",
                "content": "ROOT HAIR CELL — function: absorb water and mineral ions from soil.\nAdaptations:\n• Long, thin hair-like projection extending from the cell — massively increases the surface area in contact with soil water.\n• No chloroplasts — underground, no light available for photosynthesis.\n• Thin cell wall — short diffusion distance for water and minerals.\n• Large permanent vacuole — maintains a low water potential inside the cell to draw water in by osmosis.\n\nXYLEM CELL — function: transport water and dissolved minerals from roots up to leaves.\nAdaptations:\n• Dead cells — no cytoplasm or nucleus (no living contents obstructing flow).\n• Hollow lumen — forms a continuous open tube for water to flow through.\n• Walls thickened with LIGNIN — a hard, waterproof substance that prevents collapse under pressure and makes xylem very strong.\n• No end walls — cells are stacked end-to-end to form an uninterrupted column.\n\nPHLOEM CELL — function: transport dissolved sugars (sucrose) from leaves to the rest of the plant.\nAdaptations:\n• Living cells with little cytoplasm.\n• Sieve plates — porous plates at the end walls that allow sugar solution to flow between cells.\n• Companion cells alongside each sieve tube cell — provide energy (ATP) for active loading of sugars.\n\nPALISADE MESOPHYLL CELL — function: photosynthesis.\nAdaptations:\n• Packed with many chloroplasts.\n• Found at the top of the leaf — closest to sunlight.\n• Tall, column shape — allows maximum chloroplasts to be stacked near the leaf surface."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Students often say 'root hair cells absorb water by active transport' — this is WRONG. Water enters by OSMOSIS (passive). Mineral IONS are absorbed by active transport. These are two different processes happening in the same cell. Don't mix them up.",
        "key_note": "Differentiation = cells becoming specialised by switching genes on/off. Animals: mostly at embryo stage. Plants: meristems continue throughout life. Every adaptation has a specific reason — always link structure to function.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Specialised Cell to its Key Adaptation",
            "instruction": "Match each cell type to the adaptation that makes it suited to its function.",
            "pairs": [
                ("Sperm cell", "Flagellum and many mitochondria — to swim to the egg"),
                ("Red blood cell", "Biconcave disc, no nucleus — maximises haemoglobin space"),
                ("Neurone", "Long axon with myelin sheath — fast impulse transmission"),
                ("Root hair cell", "Long projection, no chloroplasts — absorbs water and minerals from soil"),
                ("Xylem", "Hollow, dead, lignified walls — forms a tube for water transport"),
                ("Palisade cell", "Packed with chloroplasts near leaf surface — photosynthesis"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does a sperm cell contain many mitochondria?",
                "opts": [
                    ("It needs large amounts of ATP energy to power its flagellum and swim to the egg", True),
                    ("Mitochondria help the sperm digest through the egg membrane", False),
                    ("More mitochondria make the sperm cell larger and more visible", False),
                    ("Mitochondria store the sperm's genetic material", False)
                ],
                "wrong_explanations": {
                    1: "Digesting the egg membrane is the function of the ACROSOME — an enzyme-filled cap at the tip of the sperm head. Mitochondria provide energy.",
                    2: "Sperm cells are actually very small and streamlined to reduce drag — larger would mean slower swimming. Mitochondria provide energy, not bulk.",
                    3: "Genetic material (DNA) is stored in the NUCLEUS, not in mitochondria. Mitochondria have their own small amount of DNA but this is not what carries genetic information to the egg."
                }
            },
            {
                "q": "A red blood cell has no nucleus. How does this benefit its function?",
                "opts": [
                    ("More internal space for haemoglobin, allowing the cell to carry more oxygen", True),
                    ("Without a nucleus it cannot be destroyed by white blood cells", False),
                    ("It can reproduce more quickly without a nucleus getting in the way", False),
                    ("The absence of a nucleus reduces the cell's oxygen needs", False)
                ],
                "wrong_explanations": {
                    1: "White blood cells do patrol for pathogens, but red blood cell lifespan (~120 days) is determined by membrane wear — not by whether they have a nucleus.",
                    2: "Cells without a nucleus CANNOT reproduce — red blood cells are made in bone marrow and released as mature, non-dividing cells.",
                    3: "Cells don't 'need' oxygen for the nucleus — they need it for respiration in mitochondria. Red blood cells actually have very few mitochondria and mainly use anaerobic respiration."
                }
            },
            {
                "q": "Why does a root hair cell have no chloroplasts?",
                "opts": [
                    ("Root hair cells are underground — there is no light available for photosynthesis", True),
                    ("Root hair cells are too small to fit chloroplasts inside", False),
                    ("Chloroplasts would prevent water absorption from the soil", False),
                    ("Root hair cells are a type of prokaryotic cell and cannot have organelles", False)
                ],
                "wrong_explanations": {
                    1: "Root hair cells are of similar size to leaf cells — size is not the limiting factor. The absence of light is the reason.",
                    2: "Chloroplasts don't block water entry — they are simply absent because they would serve no purpose underground where there is no light.",
                    3: "All plant cells are EUKARYOTIC. Root hair cells are eukaryotic plant cells — they could have organelles, but chloroplasts specifically are not present due to the lack of light."
                }
            },
            {
                "q": "What structural feature of xylem cells makes them well-suited for water transport?",
                "opts": [
                    ("They are dead and hollow — no cell contents blocking the continuous water column", True),
                    ("They contain many chloroplasts to produce energy for pumping water upwards", False),
                    ("They have a large vacuole to store water temporarily", False),
                    ("They have very thin walls to allow water to pass through easily", False)
                ],
                "wrong_explanations": {
                    1: "Chloroplasts would only be present if the xylem cell was exposed to light — and the purpose of xylem is water transport, not photosynthesis. The hollow dead cells are the key feature.",
                    2: "Xylem cells don't store water — they are a continuous flow pipe. Vacuoles are a feature of living plant cells for support.",
                    3: "Xylem walls are actually THICK and reinforced with lignin — this gives them strength to withstand the tension created as water is pulled upwards, preventing the xylem from collapsing."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 4. MICROSCOPY
    # ═══════════════════════════════════════════════
    {
        "id": "microscopy",
        "title": "Microscopy",
        "spec": "4.1.1.5",
        "summary": "Compare light and electron microscopes, and carry out magnification calculations.",
        "theory": [
            {
                "heading": "Light Microscopes",
                "content": "Light microscopes use VISIBLE LIGHT focused by glass lenses to produce a magnified image of a specimen.\nKey facts:\n• Maximum magnification: approximately ×2,000\n• Maximum resolution: approximately 200 nm — cannot distinguish two points closer than this\n• Can view living specimens — no special preparation needed\n• Relatively cheap — used in schools and hospitals worldwide\n• Images are in colour (natural or stained)\nWhat you CAN see: cells, nucleus, cell wall, vacuole, chloroplasts, large organelles at high magnification\nWhat you CANNOT see clearly: ribosomes (~20 nm), internal membrane detail, individual proteins\nSTAINING: many specimens are colourless, so dyes are used:\n• Iodine solution: stains starch blue/black; stains nuclei light brown\n• Methylene blue: stains cell nuclei dark blue — great for animal cells\n• Toluidine blue: stains plant cell walls\nStaining kills cells — so stained specimens cannot be living."
            },
            {
                "heading": "Electron Microscopes",
                "content": "Electron microscopes use a BEAM OF ELECTRONS instead of light.\nBecause electrons have a much shorter wavelength than visible light, they can produce far more detailed images.\nKey facts:\n• Maximum magnification: approximately ×2,000,000\n• Maximum resolution: approximately 0.1 nm — 2000× better than light microscopes\n• Specimens must be dead — the electron beam operates in a vacuum (no air, so no living cells)\n• Very expensive — found in universities and research centres\n• Images are black and white (false colour can be added digitally afterwards)\nTwo main types:\n• Transmission electron microscope (TEM): beam passes THROUGH a very thin slice of specimen — shows internal detail of organelles\n• Scanning electron microscope (SEM): beam scans the SURFACE of a specimen — produces a 3D-looking image of the external structure\nElectron microscopes revealed: the detailed internal structure of mitochondria, ribosomes, the nuclear envelope, endoplasmic reticulum and many more previously unknown structures — transforming our understanding of cell biology."
            },
            {
                "heading": "Resolution vs Magnification",
                "content": "These two terms are often confused:\nMAGNIFICATION: how many times bigger the image is compared to the actual object. A ×1000 magnification makes things appear 1000× bigger.\nRESOLUTION: the ability to see fine detail — how clearly two close-together points can be distinguished as SEPARATE objects rather than blurring into one.\nYou can have high magnification but low resolution — like zooming in on a pixelated photo. The image is big but blurry.\nElectron microscopes gave scientists BOTH very high magnification AND very high resolution — this is what made them revolutionary.\nAnalogy: imagine trying to read a book from across a room. You could use a magnifying glass (high magnification) but if the lens is poor quality, the words are still blurry (low resolution). A high-quality telescope gives you both magnification and resolution."
            },
            {
                "heading": "The Magnification Formula",
                "content": "The formula: Magnification = Image size ÷ Actual size\nRearranged:\n• Actual size = Image size ÷ Magnification\n• Image size = Actual size × Magnification\nCRUCIAL RULE: both measurements must be in the SAME UNITS before you calculate.\nIf image size is in mm and actual size is in µm → convert before calculating.\nUnit conversions:\n• mm to µm: multiply by 1000 (1 mm = 1000 µm)\n• µm to mm: divide by 1000\nTip: use the formula triangle — write M at the top, I bottom-left, A bottom-right. Cover the one you want to find."
            }
        ],
        "variables": [
            ("M", "Magnification", "no unit", "×"),
            ("I", "Image size", "mm or µm", "mm / µm"),
            ("A", "Actual size", "mm or µm", "mm / µm"),
        ],
        "equations": ["M = I ÷ A", "A = I ÷ M", "I = A × M"],
        "common_mistake": "Units must be the same before calculating. If image size is in mm and actual size is in µm, you MUST convert first or your answer will be wrong by a factor of 1000. Always write out the units in your working — this forces you to spot when they don't match.",
        "key_note": "Light microscope: max ×2000, resolution 200 nm, can view living cells. Electron microscope: max ×2,000,000, resolution 0.1 nm, specimens must be dead. Resolution = sharpness. Magnification = size increase.",
        "higher": None,
        "triple_only": None,
        "rp": "RP1 — Use a light microscope to observe, draw and label plant and animal cells. Include a scale bar. Calculate the magnification of your drawing.",
        "matching": {
            "title": "Light Microscope or Electron Microscope?",
            "instruction": "Sort each statement to the correct type of microscope.",
            "pairs": [
                ("Electron microscope", "Resolution of 0.1 nm — can distinguish structures 2000× finer than a light microscope"),
                ("Light microscope", "Can be used to view living cells without any special preparation"),
                ("Electron microscope", "First revealed the detailed internal structure of mitochondria and ribosomes"),
                ("Light microscope", "Maximum magnification of approximately ×2,000"),
                ("Electron microscope", "Specimens must be dead — the beam operates in a vacuum"),
                ("Both", "Used to calculate magnification using M = I ÷ A"),
            ]
        },
        "fifas": [
            {
                "label": "Example 1 — Find magnification",
                "question": "A cell appears 54 mm wide in a diagram. Its actual width is 0.018 mm. Calculate the magnification.",
                "steps": [
                    ("F", "M = Image size ÷ Actual size"),
                    ("I", "M = 54 ÷ 0.018"),
                    ("F", "Both values are in mm — no unit conversion needed"),
                    ("A", "M = ×3000")
                ]
            },
            {
                "label": "Example 2 — Find actual size",
                "question": "A mitochondrion appears 12 mm long in an electron micrograph at ×80,000 magnification. Calculate its actual length in µm.",
                "steps": [
                    ("F", "Actual size = Image size ÷ Magnification"),
                    ("I", "A = 12 mm ÷ 80,000 = 0.00015 mm"),
                    ("F", "Convert mm to µm: 0.00015 × 1000 = 0.15 µm"),
                    ("A", "Actual length = 0.15 µm")
                ]
            },
            {
                "label": "Example 3 — Find image size",
                "question": "A bacterium has an actual diameter of 2 µm. It is drawn at ×2000 magnification. How large should the drawing be in mm?",
                "steps": [
                    ("F", "Image size = Actual size × Magnification"),
                    ("I", "I = 2 µm × 2000 = 4000 µm"),
                    ("F", "Convert µm to mm: 4000 ÷ 1000 = 4 mm"),
                    ("A", "Drawing should be 4 mm wide")
                ]
            }
        ],
        "quiz": [
            {
                "q": "What is the maximum magnification of a light microscope?",
                "opts": [
                    ("Approximately ×2,000", True),
                    ("Approximately ×2,000,000", False),
                    ("Approximately ×200", False),
                    ("Approximately ×20,000", False)
                ],
                "wrong_explanations": {
                    1: "×2,000,000 is the maximum for an ELECTRON microscope — far more powerful than a light microscope.",
                    2: "×200 is a common low-power objective on a school microscope — but the total maximum for light microscopes is around ×2,000.",
                    3: "×20,000 doesn't correspond to either type — light microscopes reach ~×2,000 and electron microscopes ~×2,000,000."
                }
            },
            {
                "q": "An image is 45 mm wide. The actual size is 0.009 mm. What is the magnification?",
                "opts": [
                    ("×5,000", True),
                    ("×500", False),
                    ("×50,000", False),
                    ("×4,500", False)
                ],
                "wrong_explanations": {
                    1: "Check: 45 ÷ 0.09 = 500, but actual size is 0.009 (not 0.09). 45 ÷ 0.009 = 5000.",
                    2: "45 ÷ 0.009 = 5000 not 50,000. Check you moved the decimal correctly.",
                    3: "45 minus 0.009 is not how you calculate magnification! Use M = I ÷ A = 45 ÷ 0.009 = 5000."
                }
            },
            {
                "q": "Why were ribosomes not discovered until electron microscopes became available?",
                "opts": [
                    ("Ribosomes (~20 nm) are far below the resolution limit of light microscopes (~200 nm)", True),
                    ("Ribosomes are only visible in living cells and electron microscopes can see living cells", True),
                    ("Ribosomes are colourless and no stain existed until recently", False),
                    ("Ribosomes only appear in plant cells which were studied less", False)
                ],
                "wrong_explanations": {
                    1: "Electron microscopes cannot view LIVING specimens — they require dead specimens in a vacuum. The key advantage is RESOLUTION, not viewing live cells.",
                    2: "Staining could make ribosomes coloured — but even stained, they are too small to be resolved by a light microscope.",
                    3: "Ribosomes are found in ALL cells — animal, plant and bacterial. They were not limited to plant cells."
                }
            },
            {
                "q": "What is the difference between magnification and resolution?",
                "opts": [
                    ("Magnification = how much bigger the image appears; resolution = how clearly fine detail can be distinguished", True),
                    ("They are the same thing — both refer to how large the image looks", False),
                    ("Magnification refers to electron microscopes only; resolution applies to light microscopes", False),
                    ("Resolution is measured in × and magnification is measured in nm", False)
                ],
                "wrong_explanations": {
                    1: "They are NOT the same. You can have a highly magnified but blurry image — that is high magnification but low resolution.",
                    2: "Both types of microscope have both magnification and resolution — the terms apply to all microscopes.",
                    3: "Magnification has no unit (×) — it is a ratio. Resolution is measured in nm (nanometres). You have these exactly the wrong way around."
                }
            },
            {
                "q": "A cell has an actual diameter of 50 µm. At ×400 magnification, how large will the image appear in µm?",
                "opts": [
                    ("20,000 µm", True),
                    ("0.125 µm", False),
                    ("450 µm", False),
                    ("2,000 µm", False)
                ],
                "wrong_explanations": {
                    1: "You divided instead of multiplying. Image = Actual × Magnification = 50 × 400 = 20,000 µm.",
                    2: "You added the magnification to the actual size. Image = Actual × Magnification = 50 × 400 = 20,000 µm.",
                    3: "You used the wrong magnification value. Image = 50 × 400 = 20,000 µm — not 2000 µm."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 5. CHROMOSOMES, THE CELL CYCLE AND MITOSIS
    # ═══════════════════════════════════════════════
    {
        "id": "chromosomes-mitosis",
        "title": "Chromosomes, the Cell Cycle and Mitosis",
        "spec": "4.1.2.1",
        "summary": "Describe chromosomes, the stages of the cell cycle and the process and purpose of mitosis.",
        "theory": [
            {
                "heading": "Chromosomes",
                "content": "The nucleus of every body cell contains chromosomes — long, tightly coiled molecules of DNA.\nEach chromosome is one very long DNA molecule associated with proteins called histones that help package it.\nEach chromosome carries many GENES — a gene is a specific section of DNA coding for one protein.\nHumans have 46 chromosomes in most body cells, arranged as 23 PAIRS of homologous chromosomes.\n'Homologous' means matching — each pair carries genes for the same characteristics, but may carry different alleles (versions) of those genes.\nOne chromosome in each pair came from the mother (via the egg) and one from the father (via the sperm).\nBODY CELLS: 46 chromosomes (diploid — 2n). All cells in your body except gametes.\nGAMETES (sperm and eggs): 23 chromosomes (haploid — n). When two gametes fuse at fertilisation: 23 + 23 = 46 — the full number is restored."
            },
            {
                "heading": "The Cell Cycle",
                "content": "The cell cycle is the ordered series of events that a cell goes through from its formation to its division into two new cells.\nThe cycle has three main phases:\n\nPHASE 1 — INTERPHASE (growth and preparation):\nThis is the longest phase — the cell spends most of its life here.\n• G1 phase: cell grows in size. Proteins are synthesised. Number of organelles increases (more ribosomes, mitochondria etc).\n• S phase (DNA synthesis): each chromosome is REPLICATED — a new copy of every DNA molecule is made. The cell now has 92 chromatids (2 copies of each of the 46 chromosomes, held together).\n• G2 phase: further growth. Cell checks that DNA has been copied accurately.\n\nPHASE 2 — MITOSIS (nuclear division):\nThe duplicated chromosomes are separated into two identical sets, each with 46 chromosomes.\n\nPHASE 3 — CYTOKINESIS (cytoplasm division):\nThe cytoplasm divides to form two separate daughter cells, each containing a complete nucleus with 46 chromosomes."
            },
            {
                "heading": "Mitosis — What Happens",
                "content": "Mitosis is the type of nuclear division that produces two genetically IDENTICAL nuclei.\nYou do NOT need to know the names of the specific phases (prophase, metaphase, anaphase, telophase) for Foundation GCSE.\nWhat you DO need to know is the overall process:\n1. Chromosomes condense and become visible (they have already been duplicated during interphase)\n2. The duplicated chromosomes line up along the middle of the cell\n3. The two copies of each chromosome are pulled to OPPOSITE ENDS of the cell\n4. The nuclear membrane reforms around each set — two new nuclei form\n5. The cytoplasm divides (cytokinesis) → two daughter cells, each with 46 chromosomes\nRESULT: two cells genetically identical to each other AND to the original parent cell."
            },
            {
                "heading": "Why Mitosis is Important",
                "content": "Mitosis is used for:\n• GROWTH: from a single fertilised egg, all the trillions of body cells are produced by repeated mitosis.\n• REPAIR: damaged tissues are repaired by producing new identical cells — e.g. healing a cut skin wound.\n• REPLACEMENT: some cells wear out quickly and must be continuously replaced — red blood cells (~120 days), gut lining cells (~5 days), skin cells (~2–4 weeks).\n• ASEXUAL REPRODUCTION: some organisms reproduce entirely through mitosis — all offspring are clones of the parent.\n\nCANCER — when the cell cycle goes wrong:\nNormally, the cell cycle is tightly controlled by regulatory genes.\nIf a MUTATION occurs in these regulatory genes, the control is lost and cells divide uncontrollably.\nThis produces a mass of cells called a TUMOUR.\nBenign tumour: grows in one place, does not invade surrounding tissue, usually not life-threatening.\nMalignant tumour (cancer): cells break away, travel through blood or lymph, and form NEW tumours elsewhere in the body — this spreading is called METASTASIS.\nTreatments: surgery (remove the tumour), radiotherapy (gamma rays damage tumour cell DNA), chemotherapy (drugs that kill rapidly dividing cells)."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Mitosis produces TWO daughter cells that are genetically IDENTICAL to each other and to the parent — same number of chromosomes (46 in humans). Do NOT confuse with meiosis (not required at Foundation but you will hear the word). Meiosis produces FOUR cells each with HALF the chromosomes — used only for making gametes. Mitosis = for the BODY. Meiosis = for GAMETES.",
        "key_note": "Mitosis: growth, repair, replacement. Two identical daughter cells. 46 → 46. DNA replicates BEFORE division. Cancer = uncontrolled mitosis caused by mutation in regulatory genes.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Cell Cycle — Match the Phase to What Happens",
            "instruction": "Match each description to the correct phase of the cell cycle.",
            "pairs": [
                ("Interphase — growth (G1)", "Cell grows in size and produces more organelles and proteins"),
                ("Interphase — DNA replication (S phase)", "Every chromosome is copied — cell now has double the DNA"),
                ("Mitosis", "Duplicated chromosomes separate to opposite ends of the cell — two new nuclei form"),
                ("Cytokinesis", "Cytoplasm divides — two genetically identical daughter cells produced"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "A human body cell has 46 chromosomes. How many chromosomes will each daughter cell have after mitosis?",
                "opts": [
                    ("46", True),
                    ("23", False),
                    ("92", False),
                    ("12", False)
                ],
                "wrong_explanations": {
                    1: "23 chromosomes = the haploid number found in GAMETES after meiosis. Mitosis maintains the FULL chromosome number.",
                    2: "92 is the number of chromatids DURING DNA replication — before the cell divides. After mitosis, each daughter cell has 46.",
                    3: "12 has no biological relevance here. The answer is always the same as the parent cell — mitosis maintains chromosome number."
                }
            },
            {
                "q": "What must happen to DNA before a cell can divide by mitosis?",
                "opts": [
                    ("It must be replicated — each chromosome is copied so the cell has double the DNA", True),
                    ("The DNA must be destroyed and completely rebuilt from scratch", False),
                    ("The chromosome number must be halved by meiosis first", False),
                    ("Nothing — the DNA divides automatically with no prior preparation", False)
                ],
                "wrong_explanations": {
                    1: "DNA is never destroyed during the cell cycle — it is carefully replicated and preserved. Destroying it would kill the cell.",
                    2: "Halving chromosomes = MEIOSIS. Mitosis MAINTAINS chromosome number. You cannot prepare for mitosis by halving DNA.",
                    3: "DNA replication MUST occur before division. Each daughter cell needs a complete set of chromosomes — if DNA wasn't replicated, one cell would get half and the other cell would get the other half."
                }
            },
            {
                "q": "What is the difference between a benign and a malignant tumour?",
                "opts": [
                    ("Benign stays in one place; malignant spreads to other parts of the body (metastasis)", True),
                    ("Benign is caused by genetics; malignant is caused by lifestyle only", False),
                    ("Malignant tumours are always fatal; benign tumours always disappear on their own", False),
                    ("Benign tumours are larger than malignant tumours", False)
                ],
                "wrong_explanations": {
                    1: "Both benign and malignant tumours can have genetic causes and both can be influenced by lifestyle. The defining difference is whether the tumour SPREADS.",
                    2: "Malignant tumours vary hugely in outlook — many can be treated successfully. And benign tumours don't always disappear — they may need surgical removal.",
                    3: "Tumour size does not define whether it is benign or malignant. Malignant tumours are defined by their ability to invade and spread."
                }
            },
            {
                "q": "Which of the following best describes the purpose of mitosis?",
                "opts": [
                    ("Growth, repair and replacement of body cells — producing genetically identical daughter cells", True),
                    ("Producing gametes (sperm and eggs) with half the chromosome number", False),
                    ("Creating genetic variation in the offspring of an organism", False),
                    ("Repairing damaged DNA before it can be copied", False)
                ],
                "wrong_explanations": {
                    1: "Producing gametes = MEIOSIS. Gametes need half the chromosome number — mitosis would give them the full 46.",
                    2: "Mitosis produces IDENTICAL cells — there is no genetic variation. Genetic variation comes from meiosis and mutation.",
                    3: "DNA repair mechanisms exist but are separate from mitosis. Mitosis is the division process, not the repair process."
                }
            },
            {
                "q": "Cancer is caused by...",
                "opts": [
                    ("Mutations in genes that control the cell cycle — causing uncontrolled cell division", True),
                    ("Too many mitochondria in a cell causing overproduction of ATP", False),
                    ("Cells reversing their differentiation and becoming stem cells again", False),
                    ("The immune system attacking healthy body cells", False)
                ],
                "wrong_explanations": {
                    1: "Mitochondria number has nothing to do with cancer. Cancer is caused by loss of cell cycle regulation due to gene mutation.",
                    2: "Some cancer cells do share characteristics with stem cells (undifferentiation), but cancer is specifically caused by mutations in regulatory genes — not by a deliberate reversal of differentiation.",
                    3: "The immune system attacking healthy cells = autoimmune disease (e.g. Type 1 diabetes, rheumatoid arthritis). Cancer is caused by mutated regulatory genes."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 6. STEM CELLS
    # ═══════════════════════════════════════════════
    {
        "id": "stem-cells",
        "title": "Stem Cells",
        "spec": "4.1.2.3",
        "summary": "Describe the properties and uses of stem cells, including embryonic, adult and plant meristem cells.",
        "theory": [
            {
                "heading": "What Are Stem Cells?",
                "content": "A stem cell is an undifferentiated cell — a cell that has not yet specialised.\nAll stem cells share two key properties:\n1. SELF-RENEWAL: they can divide by mitosis to produce more copies of themselves indefinitely.\n2. POTENCY: they can differentiate into one or more types of specialised cell.\nStem cells are essential during development — they provide the source from which all specialised cells of the body are produced.\nThey also play a role in maintenance and repair throughout life — replacing worn-out or damaged cells in certain tissues."
            },
            {
                "heading": "Embryonic Stem Cells",
                "content": "EMBRYONIC STEM CELLS are found in the inner cell mass of a human embryo at 3–5 days old (called a blastocyst).\nThey are TOTIPOTENT — they can differentiate into ANY of the more than 200 cell types in the human body.\nThis makes them the most versatile type of stem cell.\nHow they are obtained: the embryo is destroyed to extract the stem cells. This is usually done using embryos left over from IVF (in vitro fertilisation) treatment that would otherwise be discarded.\nPotential uses:\n• Replacing insulin-producing beta cells in the pancreas → treating Type 1 diabetes\n• Growing new neurones → treating Parkinson's disease or spinal cord injuries\n• Producing heart muscle cells → repairing damage after a heart attack\n• Growing skin for burns victims\nChallenges: immune rejection (the patient's immune system may attack the transplanted cells), and the risk of tumour formation if undifferentiated cells remain."
            },
            {
                "heading": "Adult Stem Cells",
                "content": "ADULT STEM CELLS are found in specific tissues throughout the body — even in fully-grown adults.\nThey are MULTIPOTENT — they can only differentiate into the cell types found in the tissue where they live.\nBone marrow stem cells are the most well-known and well-used:\n• Haematopoietic (blood-forming) stem cells in bone marrow produce ALL types of blood cell: red blood cells, white blood cells, platelets.\nClinical use — bone marrow transplant:\n• Used to treat leukaemia (cancer of blood cells).\n• The patient's cancerous bone marrow is destroyed by high-dose chemotherapy/radiotherapy.\n• Healthy donor bone marrow (containing stem cells) is transplanted → new, healthy blood cells are produced.\nAdvantages of adult over embryonic stem cells: no ethical controversy, the patient can be their own donor (if using their own stem cells — autologous transplant).\nDisadvantages: more limited range of cell types, harder to grow in large numbers."
            },
            {
                "heading": "Plant Meristem Cells",
                "content": "Plants have their own form of stem cells — MERISTEM CELLS, found in regions of the plant called MERISTEMS.\nMeristems are located:\n• At the tips of roots and shoots (apical meristems) — responsible for lengthening\n• Along the sides of stems (lateral meristems) — responsible for thickening\nUnlike most animal adult stem cells, plant meristem cells are essentially TOTIPOTENT — they can differentiate into ANY type of plant cell.\nThis is why plants can keep growing throughout their entire lives — a new leaf, root or flower can always be produced from meristem cells.\nApplications:\n• CLONING: a single meristem cell or small section of tissue can be grown into an entirely new, genetically identical plant (tissue culture / micropropagation).\n• Conserving rare or endangered plant species.\n• Mass-producing disease-resistant crop plants.\n• Creating large numbers of identical, high-quality plants quickly."
            },
            {
                "heading": "Ethical Issues around Stem Cell Research",
                "content": "Stem cell research — particularly using embryonic stem cells — raises significant ethical questions:\nARGUMENTS FOR:\n• Could cure debilitating diseases that currently have no treatment\n• Embryos used are from IVF treatment and would be destroyed anyway\n• Early embryos (blastocysts) are just a ball of ~100 cells — not yet a person\nARGUMENTS AGAINST:\n• Destroying an embryo destroys a potential human life — many religious groups hold this view\n• The embryo cannot consent to being used for research\n• Concerns that this could lead to cloning of humans ('slippery slope' argument)\n• Risk of exploitation — women may be pressured to donate eggs\nIn the UK, embryonic stem cell research is strictly regulated by the Human Fertilisation and Embryology Authority (HFEA) — research is permitted up to 14 days of embryo development."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Students often say stem cells 'replace organs' — they don't. They differentiate into SPECIFIC CELL TYPES that can be used to repair or replace damaged cells within an organ. Also: embryonic stem cells are TOTIPOTENT (any cell type). Adult stem cells are MULTIPOTENT (limited range). Don't mix these terms up.",
        "key_note": "Embryonic stem cells: totipotent (any cell type), ethically controversial, from IVF embryos. Adult stem cells: multipotent (limited types), bone marrow → all blood cells, used for leukaemia. Plant meristems: totipotent for plants, found at root/shoot tips, used for cloning.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Stem Cell Type to its Features",
            "instruction": "Match each description to the correct type of stem cell.",
            "pairs": [
                ("Embryonic stem cell", "Totipotent — can become any of the 200+ cell types in the body"),
                ("Adult stem cell (bone marrow)", "Produces all types of blood cell — used in bone marrow transplants for leukaemia"),
                ("Plant meristem cell", "Found at root and shoot tips — can differentiate into any plant cell type"),
                ("Embryonic stem cell", "Obtained from early embryos — raises ethical concerns about destroying potential life"),
                ("Adult stem cell", "Multipotent — more limited range of cell types than embryonic"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What does 'totipotent' mean when describing stem cells?",
                "opts": [
                    ("The cell can differentiate into any type of cell in the organism", True),
                    ("The cell can only differentiate into cells of one specific tissue type", False),
                    ("The cell can divide indefinitely without ever differentiating", False),
                    ("The cell has already partially specialised and cannot reverse", False)
                ],
                "wrong_explanations": {
                    1: "Differentiating into cells of one tissue type = MULTIPOTENT (e.g. bone marrow stem cells → blood cells only). Totipotent = ANY cell type.",
                    2: "The ability to divide indefinitely is SELF-RENEWAL — a separate property of stem cells. Totipotency refers to differentiation potential.",
                    3: "Partially specialised cells that cannot reverse are already differentiated cells — not stem cells at all."
                }
            },
            {
                "q": "How are stem cells used to treat leukaemia?",
                "opts": [
                    ("A bone marrow transplant: cancerous blood cells destroyed, then donor stem cells replace them and produce healthy blood cells", True),
                    ("Embryonic stem cells are injected into the blood to replace cancer cells", False),
                    ("Stem cells are used to make antibodies that kill cancer cells directly", False),
                    ("Stem cells repair the damaged DNA in leukaemia cells, reversing the cancer", False)
                ],
                "wrong_explanations": {
                    1: "Embryonic stem cells are not used for leukaemia treatment — adult bone marrow stem cells are used. They are donated or sometimes the patient's own (after treatment).",
                    2: "Antibodies that target cancer cells are a different therapy (monoclonal antibodies) — not how stem cells work in leukaemia treatment.",
                    3: "Stem cells don't repair cancer cell DNA — the cancer cells are destroyed by chemotherapy/radiotherapy first, then NEW healthy cells are produced from transplanted stem cells."
                }
            },
            {
                "q": "Why are embryonic stem cells ethically controversial?",
                "opts": [
                    ("Obtaining them requires destroying an embryo — which some consider to be destroying a potential human life", True),
                    ("They cause cancer in patients who receive them", False),
                    ("They are ineffective at treating disease", False),
                    ("They are too expensive to collect and store", False)
                ],
                "wrong_explanations": {
                    1: "Cancer risk is a technical concern — the main ETHICAL controversy is about the moral status of the embryo that is destroyed.",
                    2: "Embryonic stem cells are actually MORE effective than adult stem cells because they are totipotent — the concern is ethical, not about effectiveness.",
                    3: "Cost and practicality are challenges — but the defining controversy is ethical: is it acceptable to destroy a potential human life for medical research?"
                }
            },
            {
                "q": "What is special about plant meristem cells compared to adult animal stem cells?",
                "opts": [
                    ("Plant meristem cells are totipotent — they can form any plant cell type; adult animal stem cells are only multipotent", True),
                    ("Plant meristem cells can only form root cells; animal stem cells are more versatile", False),
                    ("Plant meristem cells are found throughout all plant tissues; animal stem cells are only in bone marrow", False),
                    ("There is no difference — both types have the same level of potency", False)
                ],
                "wrong_explanations": {
                    1: "It is almost the opposite — plant meristems are MORE versatile (totipotent), not less.",
                    2: "Meristems are found in specific regions (root tips, shoot tips, cambium) — not throughout all tissues. And they can form any plant cell type, not just root cells.",
                    3: "There is a significant difference in potency — plant meristem cells are essentially totipotent while most adult animal stem cells are multipotent."
                }
            }
        ]
    },

    # ═══════════════════════════════════════════════
    # 7. DIFFUSION, OSMOSIS AND ACTIVE TRANSPORT
    # ═══════════════════════════════════════════════
    {
        "id": "transport-in-cells",
        "title": "Diffusion, Osmosis and Active Transport",
        "spec": "4.1.3",
        "summary": "Describe and compare the three ways substances move into and out of cells.",
        "theory": [
            {
                "heading": "Diffusion",
                "content": "DIFFUSION is the net movement of particles (molecules or ions) from a region of HIGHER concentration to a region of LOWER concentration — down the concentration gradient.\nIt is a PASSIVE process — no energy (ATP) is required. Particles move due to their own random kinetic energy.\nDiffusion continues until concentrations are equal on both sides — this is called EQUILIBRIUM. Even at equilibrium, particles are still moving randomly — there's just no NET movement.\n\nFactors that increase the rate of diffusion:\n• STEEPER concentration gradient — bigger difference in concentration = faster net movement\n• HIGHER temperature — more kinetic energy → particles move faster\n• LARGER surface area — more space available for diffusion to occur across\n• SHORTER diffusion distance — thinner membrane → particles cross faster\n\nExamples in biology:\n• O₂ diffuses from alveoli (high [O₂]) → into blood (lower [O₂]) → into muscle cells (even lower [O₂])\n• CO₂ diffuses from respiring cells (high [CO₂]) → into blood → into alveoli (low [CO₂])\n• Glucose diffuses from the small intestine (high [glucose] after digestion) → into blood\n• Urea diffuses from liver cells (where it is made) → into blood → into kidney tubules → excreted in urine"
            },
            {
                "heading": "Osmosis",
                "content": "OSMOSIS is a special type of diffusion — it is the net movement of WATER MOLECULES ONLY across a PARTIALLY PERMEABLE MEMBRANE, from a DILUTE solution (more water molecules, high water potential) to a MORE CONCENTRATED solution (fewer water molecules, low water potential).\nA partially permeable membrane has tiny pores that allow small water molecules through but block larger solute molecules.\nOsmosis is also PASSIVE — no ATP energy is required.\n\nIn PLANT CELLS:\n• Cell placed in DILUTE solution: water enters by osmosis → vacuole swells → cell membrane pushes against rigid cell wall → cell becomes TURGID (firm). Turgid cells provide structural support to the plant.\n• Cell placed in CONCENTRATED solution: water leaves by osmosis → vacuole and cytoplasm shrink → cell membrane pulls away from cell wall → PLASMOLYSIS. Plant wilts.\n\nIn ANIMAL CELLS (no cell wall to limit swelling):\n• Cell in DILUTE solution: water enters by osmosis → cell SWELLS → may BURST (LYSIS) if too much water enters — e.g. red blood cells burst in pure water\n• Cell in CONCENTRATED solution: water leaves by osmosis → cell SHRINKS (CRENATION)\nThis is why the body carefully controls the concentration of blood and body fluids — deviations cause serious damage to cells."
            },
            {
                "heading": "Active Transport",
                "content": "ACTIVE TRANSPORT is the movement of substances from a region of LOWER concentration to a region of HIGHER concentration — AGAINST the concentration gradient.\nThis requires:\n1. ENERGY from ATP (produced by aerobic respiration)\n2. CARRIER PROTEINS embedded in the cell membrane\nBecause it requires ATP, active transport STOPS immediately if respiration is blocked (e.g. by cyanide, which blocks aerobic respiration, or by removing oxygen).\n\nExamples in biology:\n• ROOTS absorbing minerals: the concentration of mineral ions (e.g. nitrates, magnesium) inside root hair cells is ALREADY HIGHER than in the soil water. Yet plants need even more. Active transport pumps them in against the gradient.\n• SMALL INTESTINE absorbing glucose: once most glucose has been absorbed by diffusion, the remaining glucose must be moved from the gut (low [glucose]) into the blood (higher [glucose]) by active transport — ensuring all available glucose is absorbed."
            },
            {
                "heading": "Exchange Surfaces in Multicellular Organisms",
                "content": "Single-celled organisms have a high surface area to volume ratio — simple diffusion is sufficient.\nLarge multicellular organisms have a much LOWER surface area to volume ratio — the distance from surface to interior cells is too great for diffusion alone.\nThey need SPECIALISED EXCHANGE SURFACES and TRANSPORT SYSTEMS.\n\nFeatures of an efficient exchange surface:\n• LARGE SURFACE AREA: more area for particles to cross per unit time\n• THIN MEMBRANE: short diffusion path\n• STEEP CONCENTRATION GRADIENT: maintained by good blood supply (or ventilation for gas exchange)\n\nExamples:\n• ALVEOLI (lungs): surrounded by dense capillary network, one cell thick, highly folded — for O₂/CO₂ exchange\n• VILLI (small intestine): finger-like projections with microvilli (brush border), rich blood supply, one cell thick walls — for nutrient absorption\n• ROOT HAIR CELLS: long projections increase surface area enormously — for water and mineral absorption from soil"
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Osmosis involves WATER ONLY — through a PARTIALLY PERMEABLE MEMBRANE. Glucose, ions and other molecules do NOT move by osmosis. Active transport goes AGAINST the gradient and requires ATP energy — without ATP (no respiration) it stops. Diffusion and osmosis are both PASSIVE — no ATP needed. Never say 'diffusion requires energy'.",
        "key_note": "Diffusion: particles, high → low, passive. Osmosis: water only, dilute → concentrated, partially permeable membrane, passive. Active transport: low → high, against gradient, requires ATP + carrier proteins.",
        "higher": None,
        "triple_only": None,
        "rp": "RP2 — Investigate osmosis: place potato cylinders in different concentrations of sucrose solution. Measure mass before and after. Calculate % change in mass.",
        "matching": {
            "title": "Match the Transport Process",
            "instruction": "Match each description to diffusion, osmosis or active transport.",
            "pairs": [
                ("Diffusion", "Net movement of particles from high to low concentration — no energy needed"),
                ("Osmosis", "Movement of water molecules only across a partially permeable membrane — passive"),
                ("Active transport", "Movement against the concentration gradient — requires ATP and carrier proteins"),
                ("Diffusion", "Oxygen moving from alveoli into the blood — no ATP required"),
                ("Osmosis", "Water entering a root hair cell from the soil — the soil water is more dilute than cell contents"),
                ("Active transport", "Mineral ions absorbed into root hair cells from dilute soil water — against the gradient"),
            ]
        },
        "fifas": [
            {
                "label": "Osmosis — Percentage Change in Mass",
                "question": "A potato cylinder has a mass of 4.0 g before being placed in a concentrated sugar solution. After 30 minutes it has a mass of 3.4 g. Calculate the percentage change in mass.",
                "steps": [
                    ("F", "% change = (final mass − initial mass) ÷ initial mass × 100"),
                    ("I", "% change = (3.4 − 4.0) ÷ 4.0 × 100"),
                    ("F", "= (−0.6) ÷ 4.0 × 100 = −15%"),
                    ("A", "% change = −15% (a decrease — water left by osmosis into the concentrated solution)")
                ]
            }
        ],
        "quiz": [
            {
                "q": "Which process requires ATP energy to move substances across a cell membrane?",
                "opts": [
                    ("Active transport", True),
                    ("Diffusion", False),
                    ("Osmosis", False),
                    ("Both diffusion and osmosis", False)
                ],
                "wrong_explanations": {
                    1: "Diffusion is PASSIVE — particles move due to their own random kinetic energy, not ATP.",
                    2: "Osmosis is also PASSIVE — water moves down its own concentration gradient without energy input.",
                    3: "NEITHER diffusion nor osmosis requires ATP. Only active transport requires energy — that is what distinguishes it from the other two."
                }
            },
            {
                "q": "A potato cylinder is placed in pure water. What happens and why?",
                "opts": [
                    ("It gains mass — water enters by osmosis from the dilute water into the more concentrated cell contents", True),
                    ("It loses mass — salt leaves the potato into the water by diffusion", False),
                    ("Nothing — the potato is not permeable to water", False),
                    ("It gains mass because water enters by active transport", False)
                ],
                "wrong_explanations": {
                    1: "Salt does diffuse slightly — but the dominant effect is water moving by OSMOSIS into the cells, increasing mass.",
                    2: "Cell membranes are selectively permeable — water moves freely across them by osmosis. The potato is very much permeable to water.",
                    3: "Osmosis is PASSIVE — it requires no energy input. Water moves down its concentration gradient automatically."
                }
            },
            {
                "q": "Why does active transport stop if oxygen is removed from the environment of a cell?",
                "opts": [
                    ("No oxygen → aerobic respiration stops → no ATP produced → no energy for active transport", True),
                    ("Oxygen is a carrier protein that directly powers active transport", False),
                    ("Without oxygen, the cell membrane becomes impermeable to all substances", False),
                    ("Removing oxygen changes the concentration gradient, making active transport unnecessary", False)
                ],
                "wrong_explanations": {
                    1: "Oxygen doesn't directly power carrier proteins — it is needed for aerobic respiration to produce ATP, which then powers the carriers.",
                    2: "Membranes remain structurally intact without oxygen — it is the ATP supply that is lost, not membrane structure.",
                    3: "Removing oxygen doesn't change concentration gradients. It removes the ATP supply needed to pump substances against those gradients."
                }
            },
            {
                "q": "A plant cell is placed in a very concentrated salt solution. What will happen?",
                "opts": [
                    ("Water leaves by osmosis → the cell becomes flaccid → the cell membrane pulls away from the cell wall (plasmolysis)", True),
                    ("Water enters by osmosis → the cell becomes turgid and very firm", False),
                    ("Salt enters by active transport → the cell becomes denser", False),
                    ("The cell bursts because it cannot handle the osmotic pressure", False)
                ],
                "wrong_explanations": {
                    1: "Water enters when the EXTERNAL solution is MORE DILUTE than the cell contents. In concentrated salt solution, it is the other way round — water leaves.",
                    2: "Salt ions may slowly diffuse in, but the dominant effect is OSMOSIS — water moves to the MORE CONCENTRATED solution (the salt solution outside), not into the cell.",
                    3: "Plant cells have a rigid CELL WALL that prevents bursting — unlike animal cells. A plant cell can become flaccid or plasmolyse, but it won't burst."
                }
            },
            {
                "q": "What is the definition of osmosis?",
                "opts": [
                    ("The net movement of water molecules across a partially permeable membrane from a dilute solution to a more concentrated solution", True),
                    ("The movement of any particles from high to low concentration — passive", False),
                    ("The movement of water molecules against a concentration gradient using ATP", False),
                    ("The diffusion of water molecules through any membrane in any direction", False)
                ],
                "wrong_explanations": {
                    1: "The movement of ANY particles from high to low = DIFFUSION. Osmosis is specifically about WATER ONLY through a PARTIALLY PERMEABLE membrane.",
                    2: "Movement against a gradient using ATP = ACTIVE TRANSPORT. Osmosis is passive — water moves DOWN its concentration gradient.",
                    3: "Osmosis only occurs through a PARTIALLY PERMEABLE membrane, not any membrane. And it only moves water in ONE net direction — from dilute to concentrated."
                }
            }
        ]
    },
],

"organisation": [


    # ══════════════════════════════════════════════
    # 1. PRINCIPLES OF ORGANISATION
    # ══════════════════════════════════════════════
    {
        "id": "principles-of-organisation",
        "title": "Principles of Organisation",
        "spec": "4.2.1",
        "summary": "Describe the levels of organisation in living organisms from cells to organisms.",
        "theory": [
            {
                "heading": "The Hierarchy of Organisation",
                "content": "Living organisms are built from simple parts that are organised into increasingly complex levels.\n\nThe levels in order from simplest to most complex are:\nCELL → TISSUE → ORGAN → ORGAN SYSTEM → ORGANISM\n\nThis hierarchy is the foundation of biology — understanding it helps you understand how the body works as a whole, and why problems at one level (e.g. a faulty cell) can affect the whole organism."
            },
            {
                "heading": "Cells — The Basic Unit of Life",
                "content": "A cell is the smallest unit capable of carrying out all the processes of life.\n\nEvery living organism is made of at least one cell.\n\nDifferent cell types are specialised for different jobs — a muscle cell is built to contract, a red blood cell is built to carry oxygen, a root hair cell is built to absorb water.\n\nAll cells in one organism contain the same DNA, but different genes are switched on in different cell types."
            },
            {
                "heading": "Tissues",
                "content": "A tissue is a group of similar cells working together to carry out a particular function.\n\nKey examples of animal tissues:\nMuscle tissue — cells that can contract and relax to produce movement.\nEpithelial tissue — thin cells that line surfaces (e.g. gut lining, airway lining, skin surface).\nGlandular tissue — cells that produce and release substances such as enzymes, hormones or mucus.\nNervous tissue — neurones that carry electrical impulses.\n\nKey examples of plant tissues:\nMesophyll tissue — cells in leaves packed with chloroplasts for photosynthesis.\nXylem tissue — hollow dead cells that transport water upwards.\nPhloem tissue — living cells that transport dissolved sugars."
            },
            {
                "heading": "Organs",
                "content": "An organ is a structure made of several DIFFERENT types of tissue working together to perform a specific function.\n\nKey examples:\nThe STOMACH — contains muscle tissue (churns food), epithelial tissue (lines the stomach wall), glandular tissue (secretes HCl and pepsin enzymes).\n\nThe LEAF — contains mesophyll tissue (photosynthesis), xylem (water supply), phloem (sugar transport), epidermis (protection), guard cells (gas exchange).\n\nThe HEART — contains cardiac muscle tissue (pumps blood), valves (prevent backflow), coronary blood vessels (supply oxygen to heart muscle).\n\nThe KEY DIFFERENCE between a tissue and an organ: a tissue is made of ONE type of cell. An organ contains MULTIPLE different tissue types."
            },
            {
                "heading": "Organ Systems and Organisms",
                "content": "An organ system is a group of organs that work together to perform a major function.\n\nExamples:\nDigestive system — mouth, oesophagus, stomach, small intestine, large intestine, liver, pancreas. Function: breaks down food and absorbs nutrients.\n\nCirculatory system — heart, blood vessels, blood. Function: transports oxygen, nutrients and waste products.\n\nRespiratory system — lungs, trachea, bronchi, diaphragm. Function: gas exchange (O₂ in, CO₂ out).\n\nNervous system — brain, spinal cord, nerves. Function: detects stimuli and coordinates responses.\n\nAn ORGANISM is the complete living individual — all organ systems working together to sustain life."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Students confuse tissue and organ. Remember: a tissue is ONE type of cell doing ONE job. An organ contains MULTIPLE tissue types. The stomach is an ORGAN (it has muscle tissue, glandular tissue and epithelial tissue). Muscle is a TISSUE.",
        "key_note": "Cell → Tissue (same cells, one function) → Organ (multiple tissues) → Organ System (multiple organs) → Organism. Each level is more complex than the one before.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Level of Organisation",
            "instruction": "Match each example to its correct level of organisation.",
            "pairs": [
                ("Cell", "A single red blood cell carrying oxygen in the blood"),
                ("Tissue", "Muscle — a group of muscle cells that contract together"),
                ("Organ", "The stomach — contains muscle, glandular and epithelial tissue"),
                ("Organ system", "The digestive system — stomach, intestines, liver and pancreas"),
                ("Organism", "A complete human being — all systems functioning together"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the correct order of organisation from simplest to most complex?",
                "opts": [
                    ("Cell → Tissue → Organ → Organ system → Organism", True),
                    ("Tissue → Cell → Organ → Organ system → Organism", False),
                    ("Cell → Organ → Tissue → Organism → Organ system", False),
                    ("Organism → Organ system → Organ → Tissue → Cell", False)
                ],
                "wrong_explanations": {
                    1: "Tissues are made of cells — cells always come before tissues in the hierarchy.",
                    2: "Organs contain tissues, not the other way round — tissue must come before organ.",
                    3: "This is the correct order in reverse — from most complex down to simplest."
                }
            },
            {
                "q": "What is a tissue?",
                "opts": [
                    ("A group of similar cells working together to perform a specific function", True),
                    ("A group of different organs working together", False),
                    ("A single highly specialised cell", False),
                    ("Another name for an organ", False)
                ],
                "wrong_explanations": {
                    1: "A group of different organs = an ORGAN SYSTEM. Tissues are made of similar cells, not organs.",
                    2: "A single specialised cell is just a cell — not a tissue. A tissue is a GROUP of cells.",
                    3: "Tissues and organs are different levels. An organ is made of SEVERAL tissue types."
                }
            },
            {
                "q": "The stomach contains muscle tissue, glandular tissue and epithelial tissue. What level of organisation is the stomach?",
                "opts": [
                    ("Organ", True),
                    ("Tissue", False),
                    ("Organ system", False),
                    ("Organism", False)
                ],
                "wrong_explanations": {
                    1: "A tissue is made of ONE type of cell — the stomach has multiple tissue types, so it is an organ.",
                    2: "An organ system is a GROUP of organs — the stomach is just one organ within the digestive system.",
                    3: "An organism is the complete living thing — a human, plant or bacterium."
                }
            },
            {
                "q": "Which of these is an example of an organ system?",
                "opts": [
                    ("The digestive system — stomach, intestines, liver and pancreas working together", True),
                    ("Muscle tissue — cells that contract to produce movement", False),
                    ("The heart — contains cardiac muscle and valves", False),
                    ("A liver cell — specialised to carry out chemical reactions", False)
                ],
                "wrong_explanations": {
                    1: "Muscle tissue = a TISSUE (one cell type). Organ systems are made of multiple organs.",
                    2: "The heart = an ORGAN (contains multiple tissue types). An organ system requires multiple organs.",
                    3: "A liver cell = a CELL — the simplest level of organisation."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 2. THE DIGESTIVE SYSTEM
    # ══════════════════════════════════════════════
    {
        "id": "digestive-system",
        "title": "The Digestive System",
        "spec": "4.2.2.1",
        "summary": "Describe the organs of the digestive system and what happens to food at each stage.",
        "theory": [
            {
                "heading": "Why We Need to Digest Food",
                "content": "Food is made up of large, insoluble molecules — starch, proteins and fats — that are too big to pass through the wall of the small intestine into the blood.\n\nDigestion breaks these large molecules into small, soluble ones that CAN be absorbed.\n\nThere are two types of digestion:\nMECHANICAL DIGESTION — physical breakdown (chewing, churning). Increases surface area for enzymes.\nCHEMICAL DIGESTION — enzymes break chemical bonds to produce smaller molecules."
            },
            {
                "heading": "The Mouth",
                "content": "Digestion begins in the mouth.\n\nTeeth physically grind food into smaller pieces — increasing surface area for enzymes to work on.\n\nSalivary glands produce SALIVA, which contains:\nAmylase — begins the chemical digestion of starch → maltose (a sugar).\nMucus — lubricates food to make swallowing easier.\n\nThe tongue shapes food into a BOLUS (a soft ball) that is swallowed.\n\nThe OESOPHAGUS is a muscular tube that carries food from the mouth to the stomach using waves of muscle contractions called PERISTALSIS."
            },
            {
                "heading": "The Stomach",
                "content": "The stomach is a muscular bag that churns food (mechanical digestion) and carries out chemical digestion.\n\nGlandular tissue in the stomach wall produces GASTRIC JUICE, which contains:\nHydrochloric acid (HCl) — makes the stomach very acidic (pH ~2). This KILLS most bacteria in food and provides the optimum pH for the enzyme pepsin.\nPepsin (a PROTEASE enzyme) — breaks proteins into shorter chains of amino acids.\n\nFood stays in the stomach for several hours, slowly being mixed into a liquid called CHYME.\n\nChyme is released in small amounts into the small intestine through the pyloric sphincter."
            },
            {
                "heading": "The Small Intestine — Digestion and Absorption",
                "content": "The small intestine is the main site of both DIGESTION and ABSORPTION.\n\nThe PANCREAS produces digestive enzymes that are released into the small intestine:\nPancreatic AMYLASE — continues starch → maltose digestion.\nPancreatic PROTEASES — continue breaking proteins → amino acids.\nPancreatic LIPASE — breaks fats → fatty acids + glycerol.\n\nThe LIVER produces BILE, which is stored in the GALL BLADDER and released into the small intestine. Bile:\nEmulsifies fats — breaks large fat droplets into many small ones, increasing surface area for lipase.\nIs alkaline — neutralises the stomach acid, creating the correct pH (neutral/alkaline) for pancreatic enzymes to work.\n\nABSORPTION — digested molecules (glucose, amino acids, fatty acids, glycerol) pass through the wall of the small intestine into the blood.\n\nThe small intestine is adapted for absorption with VILLI — finger-like folds that massively increase surface area. Villi have:\nA large surface area for fast absorption.\nThin walls — only one cell thick — so the diffusion distance is very short.\nA rich blood supply — maintains the concentration gradient by constantly removing absorbed molecules."
            },
            {
                "heading": "The Large Intestine, Rectum and Anus",
                "content": "By the time food reaches the large intestine, most nutrients have already been absorbed.\n\nThe LARGE INTESTINE absorbs water from the remaining undigested material.\n\nToo little water absorbed → diarrhoea (watery faeces).\nToo much water absorbed → constipation (hard, dry faeces).\n\nThe RECTUM stores faeces (made of undigested fibre, dead cells, bacteria and bile pigments which give it the brown colour).\n\nFaeces are expelled through the ANUS."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Bile is NOT an enzyme and does NOT chemically digest fats. It EMULSIFIES them — a physical process that breaks large fat droplets into smaller ones to give lipase more surface area to work on. Students often say 'bile digests fat' — it does not. LIPASE chemically digests fat.",
        "key_note": "Mouth: amylase digests starch. Stomach: pepsin digests proteins, HCl creates pH 2. Small intestine: all three enzymes from pancreas + bile from liver. Large intestine: absorbs water.",
        "higher": None,
        "triple_only": None,
        "rp": "RP4 — Food tests: iodine solution tests for starch (blue-black = positive), Benedict's solution tests for glucose (brick red = positive), Biuret reagent tests for protein (purple = positive), ethanol emulsion test for fat (cloudy white = positive).",
        "matching": {
            "title": "Match the Organ to its Role in Digestion",
            "instruction": "Match each organ to what it does.",
            "pairs": [
                ("Mouth", "Amylase begins starch digestion — teeth grind food — bolus formed"),
                ("Stomach", "HCl + pepsin — proteins digested — chyme produced"),
                ("Pancreas", "Produces amylase, protease and lipase — released into small intestine"),
                ("Liver", "Produces bile — stored in gall bladder — emulsifies fats in small intestine"),
                ("Small intestine", "Main site of digestion and absorption — villi absorb nutrients"),
                ("Large intestine", "Absorbs water from undigested material — faeces formed"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the role of bile in digestion?",
                "opts": [
                    ("Emulsifies fats — breaks large droplets into smaller ones to increase surface area for lipase", True),
                    ("Chemically digests fats into fatty acids and glycerol", False),
                    ("Kills bacteria in the small intestine using its acidity", False),
                    ("Digests proteins into amino acids in the small intestine", False)
                ],
                "wrong_explanations": {
                    1: "Chemical digestion of fats = LIPASE. Bile only emulsifies — a physical process.",
                    2: "Bile is ALKALINE, not acidic. HCl in the stomach kills bacteria. Bile actually neutralises the stomach acid.",
                    3: "Protein digestion = PROTEASES (pepsin in the stomach, pancreatic proteases in the small intestine). Bile is not a protease."
                }
            },
            {
                "q": "Why does the small intestine have villi?",
                "opts": [
                    ("To provide a large surface area for absorbing digested nutrients into the blood", True),
                    ("To produce digestive enzymes for breaking down food", False),
                    ("To neutralise the acid from the stomach", False),
                    ("To store bile before it is released onto food", False)
                ],
                "wrong_explanations": {
                    1: "Digestive enzymes in the small intestine come from the PANCREAS — the villi are for absorption, not enzyme production.",
                    2: "Bile neutralises stomach acid — villi are surface-area adaptations for absorption.",
                    3: "Bile is stored in the GALL BLADDER, not in villi."
                }
            },
            {
                "q": "Where are proteins first chemically digested?",
                "opts": [
                    ("The stomach — by the enzyme pepsin in the presence of HCl", True),
                    ("The mouth — by salivary amylase", False),
                    ("The large intestine — by bacteria", False),
                    ("The liver — by bile salts", False)
                ],
                "wrong_explanations": {
                    1: "Salivary amylase in the mouth digests STARCH, not proteins. Amylase has no effect on protein.",
                    2: "Bacteria in the large intestine help break down some fibre but are not the main site of protein digestion.",
                    3: "The liver produces bile which emulsifies FATS — bile has no protein-digesting function."
                }
            },
            {
                "q": "What does the large intestine absorb?",
                "opts": [
                    ("Water — from the remaining undigested material", True),
                    ("Glucose — the final stage of carbohydrate absorption", False),
                    ("Amino acids — the final stage of protein absorption", False),
                    ("Fatty acids — the final stage of fat absorption", False)
                ],
                "wrong_explanations": {
                    1: "Glucose is absorbed in the SMALL INTESTINE — by the time food reaches the large intestine, glucose has already been absorbed.",
                    2: "Amino acids are absorbed in the SMALL INTESTINE — through the villi walls into the blood.",
                    3: "Fatty acids and glycerol are absorbed in the SMALL INTESTINE into the lacteals (lymph vessels in villi)."
                }
            },
            {
                "q": "Which enzyme is produced by the salivary glands?",
                "opts": [
                    ("Amylase — breaks down starch into maltose", True),
                    ("Pepsin — breaks down proteins", False),
                    ("Lipase — breaks down fats", False),
                    ("Bile — emulsifies fats", False)
                ],
                "wrong_explanations": {
                    1: "Pepsin is produced by glandular tissue in the STOMACH WALL — not the salivary glands.",
                    2: "Lipase is produced by the PANCREAS — not the salivary glands.",
                    3: "Bile is not an enzyme — it is produced by the LIVER and stored in the gall bladder."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 3. ENZYMES
    # ══════════════════════════════════════════════
    {
        "id": "enzymes",
        "title": "Enzymes",
        "spec": "4.2.2.2",
        "summary": "Explain how enzymes work, how temperature and pH affect them, and describe the lock and key model.",
        "theory": [
            {
                "heading": "What Are Enzymes?",
                "content": "Enzymes are biological catalysts — proteins that speed up chemical reactions in living organisms without being used up in the reaction.\n\nWithout enzymes, many reactions in the body would happen too slowly to sustain life.\n\nEvery enzyme is a protein with a specific 3D shape. Part of this shape forms the ACTIVE SITE — a region with a very specific shape that fits only ONE type of molecule (the SUBSTRATE).\n\nThis specificity (one enzyme = one substrate) is explained by the LOCK AND KEY MODEL."
            },
            {
                "heading": "The Lock and Key Model",
                "content": "The lock and key model explains enzyme specificity.\n\nThe ENZYME is the lock — its active site has a unique shape.\nThe SUBSTRATE is the key — only the correctly shaped substrate fits into the active site.\n\nWhat happens:\n1. The substrate collides with the enzyme's active site.\n2. The substrate binds to form an ENZYME-SUBSTRATE COMPLEX.\n3. The enzyme catalyses the reaction — substrate is converted into PRODUCTS.\n4. Products are released from the active site.\n5. The enzyme is UNCHANGED and ready to bind another substrate molecule.\n\nThis is why enzymes are NOT used up — they can be used over and over again.\n\nReal-life example: amylase (enzyme) has an active site that ONLY fits starch molecules (substrate). It will not break down proteins or fats — their shape is different."
            },
            {
                "heading": "Effect of Temperature on Enzyme Activity",
                "content": "Temperature has a huge effect on how fast enzymes work.\n\nLOW TEMPERATURE (e.g. 10°C):\nParticles have less kinetic energy.\nFewer enzyme-substrate collisions per second.\nReaction rate is slow.\n\nRISING TEMPERATURE:\nMore kinetic energy → more collisions → more enzyme-substrate complexes formed → faster reaction rate.\n\nOPTIMUM TEMPERATURE:\nThe temperature at which the enzyme works fastest.\nFor most human enzymes: approximately 37°C (body temperature).\n\nABOVE OPTIMUM TEMPERATURE:\nVibrations in the enzyme become too violent.\nThe shape of the active site is permanently changed — DENATURATION.\nSubstrate can no longer fit into the denatured active site.\nReaction rate falls rapidly to zero.\n\nIMPORTANT: denaturation is PERMANENT. Cooling the enzyme back down does NOT restore its activity."
            },
            {
                "heading": "Effect of pH on Enzyme Activity",
                "content": "Each enzyme also has an OPTIMUM pH — the pH at which it works best.\n\nPH AWAY FROM THE OPTIMUM:\nChanges in pH alter the charges on the amino acids that form the active site.\nHydrogen bonds in the enzyme are disrupted.\nThe shape of the active site changes.\nThe substrate no longer fits — enzyme activity decreases.\nAt extreme pH values, the enzyme DENATURES permanently.\n\nDifferent enzymes have different optimum pH values depending on where they work:\nSalivary amylase — optimum pH ~7 (neutral — the mouth).\nPepsin — optimum pH ~2 (acidic — the stomach, where HCl is present).\nPancreatic enzymes — optimum pH ~7–8 (neutral to slightly alkaline — small intestine, where bile has neutralised the acid).\n\nThis is WHY the body produces acid in the stomach and bile to neutralise it — creating the right pH for each enzyme in each location."
            },
            {
                "heading": "Factors That Affect Enzyme Rate — Summary",
                "content": "Three key factors affect the rate of enzyme-catalysed reactions:\n\n1. TEMPERATURE — increases rate up to optimum (~37°C for human enzymes), then denaturation causes rate to fall sharply.\n\n2. pH — each enzyme has an optimum pH. Too acidic or too alkaline = active site changes shape = slower reaction or denaturation.\n\n3. SUBSTRATE CONCENTRATION — more substrate molecules = more collisions with enzyme = faster rate (up to a point). Once all enzyme active sites are occupied, adding more substrate has no effect — the enzyme is saturated."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Enzymes are DENATURED at high temperatures — NOT killed. They are proteins, not living things. You cannot kill a protein. Denaturation means the active site shape is permanently changed. Cooling the enzyme down afterwards will NOT bring it back to life — the damage is permanent.",
        "key_note": "Lock and key: enzyme active site + specific substrate → enzyme-substrate complex → products released → enzyme reused. Denaturation is permanent — caused by high temperature or extreme pH.",
        "higher": None,
        "triple_only": None,
        "rp": "RP3 — Investigate the effect of pH on the rate of amylase activity. Use iodine solution to test for starch at regular intervals. Compare time taken to digest starch at different pH values.",
        "matching": {
            "title": "Match the Enzyme Concept",
            "instruction": "Match each term to its correct description.",
            "pairs": [
                ("Active site", "The specific region of an enzyme where the substrate binds"),
                ("Substrate", "The specific molecule that fits into an enzyme's active site"),
                ("Enzyme-substrate complex", "Formed when the substrate binds to the enzyme's active site"),
                ("Denaturation", "Permanent change in the shape of an enzyme's active site — caused by high temperature or extreme pH"),
                ("Optimum temperature", "The temperature at which an enzyme works at its maximum rate"),
                ("Lock and key model", "Explains why each enzyme only works with one specific substrate"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "An enzyme is heated to 80°C. What happens to it?",
                "opts": [
                    ("It denatures — the active site shape permanently changes and the substrate can no longer bind", True),
                    ("It works faster because higher temperature gives more energy", False),
                    ("It is killed by the heat", False),
                    ("It becomes temporarily inactive but recovers when cooled", False)
                ],
                "wrong_explanations": {
                    1: "Above the optimum (~37°C for human enzymes), the rate does increase — but 80°C is far above optimum, causing denaturation, not faster activity.",
                    2: "Enzymes are proteins, not living organisms — they cannot be 'killed'. Denaturation is the correct term.",
                    3: "Denaturation is PERMANENT. Once the active site shape is changed, cooling does NOT restore it."
                }
            },
            {
                "q": "Why does pepsin work best at pH 2?",
                "opts": [
                    ("Pepsin works in the stomach where HCl creates pH 2 — the active site shape is optimal at this pH", True),
                    ("All enzymes work best at pH 2 — it is the universal optimum", False),
                    ("pH 2 provides more substrate molecules for pepsin to work on", False),
                    ("Pepsin denatures at any pH above 2", False)
                ],
                "wrong_explanations": {
                    1: "Different enzymes have different optimum pH values. Salivary amylase works best at pH 7, pancreatic enzymes at pH 7–8. Only pepsin has an optimum around pH 2.",
                    2: "pH does not affect the number of substrate molecules — it affects the SHAPE of the active site.",
                    3: "Pepsin can work at a range of acidic pH values — though its optimum is around pH 2. It doesn't instantly denature above pH 2."
                }
            },
            {
                "q": "According to the lock and key model, why can amylase only digest starch — not proteins?",
                "opts": [
                    ("Amylase's active site is shaped to fit starch molecules only — proteins have a different shape and cannot bind", True),
                    ("Amylase is only produced in the mouth, where no proteins are found", False),
                    ("Amylase is too small to interact with large protein molecules", False),
                    ("Proteins repel enzymes and cannot form enzyme-substrate complexes", False)
                ],
                "wrong_explanations": {
                    1: "Amylase is produced in the mouth AND pancreas — it encounters proteins, but its active site shape doesn't match protein structure.",
                    2: "Enzyme size is not the issue — it's the shape of the ACTIVE SITE that determines which substrate can bind.",
                    3: "Proteins don't repel enzymes — proteases bind to proteins very effectively. It's specifically amylase whose active site doesn't fit proteins."
                }
            },
            {
                "q": "What happens to the rate of an enzyme-catalysed reaction when substrate concentration increases?",
                "opts": [
                    ("Rate increases — more substrate molecules collide with active sites — until all active sites are occupied", True),
                    ("Rate stays the same — substrate concentration does not affect enzyme activity", False),
                    ("Rate decreases — more substrate molecules compete for fewer active sites", False),
                    ("Rate immediately reaches maximum as soon as any substrate is added", False)
                ],
                "wrong_explanations": {
                    1: "Substrate concentration absolutely affects rate — more substrate = more collisions = faster rate (up to a limit).",
                    2: "Substrates don't 'compete' — each active site accepts substrate molecules one at a time. More substrate means MORE active sites occupied at any given moment.",
                    3: "Rate only reaches maximum when ALL active sites are occupied — the enzyme is then saturated. At low substrate concentrations, many active sites are empty."
                }
            },
            {
                "q": "After an enzyme-catalysed reaction, what happens to the enzyme?",
                "opts": [
                    ("It is released unchanged and can catalyse another reaction — it is not used up", True),
                    ("It is permanently bonded to the product and cannot be reused", False),
                    ("It is broken down and must be rebuilt before working again", False),
                    ("It loses its active site after each reaction and must reform it", False)
                ],
                "wrong_explanations": {
                    1: "Enzymes form temporary enzyme-SUBSTRATE complexes — once products are released, the enzyme is free and fully intact.",
                    2: "Enzymes are not broken down during catalysis — that's what makes them catalysts. They are reused many times.",
                    3: "Active sites are a permanent part of the enzyme's structure — they reform automatically because the enzyme is unchanged."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 4. THE HEART AND BLOOD VESSELS
    # ══════════════════════════════════════════════
    {
        "id": "heart-blood-vessels",
        "title": "The Heart and Blood Vessels",
        "spec": "4.2.3",
        "summary": "Describe the structure and function of the heart, the double circulatory system and the three types of blood vessel.",
        "theory": [
            {
                "heading": "The Double Circulatory System",
                "content": "Humans have a DOUBLE circulatory system — the blood passes through the heart twice for every complete circuit of the body.\n\nCircuit 1 — PULMONARY CIRCULATION:\nRight side of heart → lungs → left side of heart.\nDeoxygenated blood is pumped to the lungs to pick up oxygen and lose carbon dioxide.\n\nCircuit 2 — SYSTEMIC CIRCULATION:\nLeft side of heart → body organs and tissues → right side of heart.\nOxygenated blood is delivered to all body tissues at high pressure.\n\nWHY DOUBLE? Having two separate circuits means oxygenated blood is always kept separate from deoxygenated blood, and the left side can pump oxygenated blood to the body at high pressure — ensuring efficient oxygen delivery to even distant organs."
            },
            {
                "heading": "Structure of the Heart",
                "content": "The heart has FOUR chambers:\nRight atrium — receives deoxygenated blood from the body via the VENA CAVA.\nRight ventricle — pumps deoxygenated blood to the lungs via the PULMONARY ARTERY.\nLeft atrium — receives oxygenated blood from the lungs via the PULMONARY VEIN.\nLeft ventricle — pumps oxygenated blood to the whole body via the AORTA.\n\nThe LEFT VENTRICLE has much thicker, more muscular walls than the right ventricle because it must pump blood to the entire body — a much greater distance and requiring much higher pressure than the right ventricle (which only pumps to the nearby lungs).\n\nVALVES prevent blood flowing backwards:\nAtrioventricular (AV) valves — between atria and ventricles.\nSemilunar valves — in the pulmonary artery and aorta.\nValves open when pressure is higher on one side and snap shut to prevent backflow — this creates the 'lub-dub' heart sound.\n\nThe heart is made of CARDIAC MUSCLE — a special type of muscle that contracts and relaxes rhythmically, never getting tired.\n\nThe CORONARY ARTERIES supply the heart muscle itself with oxygenated blood. If these are blocked, the heart muscle is deprived of oxygen — causing a heart attack."
            },
            {
                "heading": "Arteries",
                "content": "Arteries carry blood AWAY from the heart.\n\nKey features:\nThick, muscular walls — to withstand the high pressure of blood pumped directly from the heart.\nElastic fibres in the walls — stretch as blood surges through with each heartbeat, then recoil to maintain smooth blood flow.\nNarrow lumen (central channel) — helps maintain high pressure.\nNO valves — pressure is high enough to keep blood flowing in the correct direction.\n\nMost arteries carry oxygenated blood — EXCEPT the PULMONARY ARTERY, which carries deoxygenated blood from the right ventricle to the lungs.\n\nMemory tip: Arteries = Away from heart."
            },
            {
                "heading": "Veins",
                "content": "Veins carry blood TOWARDS the heart.\n\nKey features:\nThinner walls — blood pressure is much lower in veins (far from the heart).\nWider lumen — accommodates the slower, lower-pressure flow.\nVALVES — essential to prevent backflow of blood. Without valves, gravity and low pressure would allow blood to pool in the legs and flow backwards.\n\nMost veins carry deoxygenated blood — EXCEPT the PULMONARY VEIN, which carries oxygenated blood from the lungs to the left atrium.\n\nMemory tip: Veins → towards the heart. Valves in Veins."
            },
            {
                "heading": "Capillaries",
                "content": "Capillaries are the smallest blood vessels — connecting arteries to veins.\n\nKey features:\nWalls are only ONE CELL THICK — the shortest possible diffusion distance.\nVery narrow — red blood cells must squeeze through in single file.\nForm a dense network throughout all body tissues.\nVery large total surface area — maximises exchange.\n\nAt the capillaries, EXCHANGE of substances takes place:\nOxygen and glucose diffuse OUT of the blood into body cells.\nCarbon dioxide and waste products diffuse INTO the blood from cells.\n\nThis exchange happens by DIFFUSION down concentration gradients — no energy required."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Arteries do NOT always carry oxygenated blood. The PULMONARY ARTERY carries DEOXYGENATED blood from the heart to the lungs. Veins do NOT always carry deoxygenated blood — the PULMONARY VEIN carries OXYGENATED blood from the lungs to the heart. The rule is: Arteries = Away from heart. Veins = to heart. Not about oxygen content.",
        "key_note": "Left ventricle = thickest wall (pumps to whole body). Right ventricle = pumps to lungs only. Arteries: away, thick walls, high pressure. Veins: to heart, valves, low pressure. Capillaries: one cell thick, exchange site.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Heart Structure to its Function",
            "instruction": "Match each structure to what it does.",
            "pairs": [
                ("Left ventricle", "Pumps oxygenated blood to the whole body via the aorta — thickest walls"),
                ("Right ventricle", "Pumps deoxygenated blood to the lungs via the pulmonary artery"),
                ("Valves", "Prevent backflow of blood — open and close with pressure changes"),
                ("Coronary arteries", "Supply the heart muscle itself with oxygenated blood"),
                ("Pulmonary vein", "Carries oxygenated blood FROM the lungs TO the left atrium"),
                ("Vena cava", "Carries deoxygenated blood FROM the body TO the right atrium"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does the left ventricle have thicker walls than the right ventricle?",
                "opts": [
                    ("It pumps blood to the whole body — needs much higher pressure than the right ventricle which only pumps to the nearby lungs", True),
                    ("It receives more blood than the right ventricle so needs to be stronger", False),
                    ("The left side of the body is larger so the heart must compensate", False),
                    ("The left ventricle contains oxygenated blood which is heavier", False)
                ],
                "wrong_explanations": {
                    1: "Both ventricles receive the same volume of blood per beat — the difference is in the distance the blood must be pumped, not the volume.",
                    2: "Body size has no relationship to heart wall thickness — it's purely about pumping distance and pressure.",
                    3: "Oxygenated and deoxygenated blood have essentially the same density — the thickness difference is purely about pressure requirements."
                }
            },
            {
                "q": "The pulmonary artery carries blood from the heart to the lungs. What type of blood does it carry?",
                "opts": [
                    ("Deoxygenated blood — it has just returned from the body and needs to be reoxygenated", True),
                    ("Oxygenated blood — all arteries carry oxygenated blood", False),
                    ("A mixture of oxygenated and deoxygenated blood", False),
                    ("Blood with no red blood cells — only plasma", False)
                ],
                "wrong_explanations": {
                    1: "This is the most common mistake in this topic! Arteries carry blood AWAY from the heart — but the pulmonary artery specifically carries deoxygenated blood to be oxygenated in the lungs.",
                    2: "Blood in the heart is kept completely separate — left side carries oxygenated, right side carries deoxygenated. There is no mixing.",
                    3: "All blood contains red blood cells — plasma alone would have no oxygen-carrying capacity."
                }
            },
            {
                "q": "Why do veins have valves but arteries do not?",
                "opts": [
                    ("Blood pressure in veins is low — valves prevent backflow. Arterial pressure is high enough to keep blood flowing in the right direction", True),
                    ("Arteries have thicker walls so they don't need valves", False),
                    ("Veins carry deoxygenated blood which needs extra support to flow", False),
                    ("Valves in arteries would slow down the high-pressure blood flow too much", False)
                ],
                "wrong_explanations": {
                    1: "Wall thickness helps arteries withstand pressure — but valves are specifically about preventing BACKFLOW, which is a problem in low-pressure veins, not high-pressure arteries.",
                    2: "The oxygen content of blood has nothing to do with the need for valves — the PRESSURE is what matters.",
                    3: "Valves in veins do slightly slow flow, but that's acceptable — their role is to prevent dangerous backflow in low-pressure vessels."
                }
            },
            {
                "q": "What makes capillaries efficient at exchanging substances?",
                "opts": [
                    ("Walls are only one cell thick — very short diffusion distance. Dense network = large surface area", True),
                    ("They have the highest blood pressure of all blood vessels", False),
                    ("They carry both oxygenated and deoxygenated blood simultaneously", False),
                    ("They have valves to keep substances moving in one direction", False)
                ],
                "wrong_explanations": {
                    1: "Capillaries have the LOWEST blood pressure — that is why they can be one cell thick without bursting.",
                    2: "Capillaries carry either oxygenated or deoxygenated blood depending on location — not both at once.",
                    3: "Capillaries have no valves — substances move by DIFFUSION driven by concentration gradients."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 5. BLOOD
    # ══════════════════════════════════════════════
    {
        "id": "blood",
        "title": "Blood",
        "spec": "4.2.3.2",
        "summary": "Describe the four components of blood and the function of each.",
        "theory": [
            {
                "heading": "Blood — A Tissue",
                "content": "Blood is a connective tissue — a liquid tissue that flows through blood vessels.\n\nIt has four main components:\n1. Red blood cells (erythrocytes)\n2. White blood cells (leucocytes)\n3. Platelets\n4. Plasma\n\nEach component has a distinct and essential function. Together they transport substances, defend against disease and maintain the body's internal environment."
            },
            {
                "heading": "Red Blood Cells",
                "content": "Red blood cells carry OXYGEN from the lungs to all body tissues.\n\nThey are uniquely adapted for this function:\nBICONCAVE DISC SHAPE — increases surface area for oxygen absorption and releases carbon dioxide. The thin centre reduces the diffusion distance for gas exchange.\nNO NUCLEUS — the nucleus is lost as red blood cells mature. This creates more space for HAEMOGLOBIN — the protein that binds and carries oxygen.\nPacked with HAEMOGLOBIN — each red blood cell contains ~270 million haemoglobin molecules.\nFLEXIBLE — can squeeze through narrow capillaries without tearing.\n\nIn the lungs, haemoglobin binds to oxygen (forming oxyhaemoglobin) where oxygen concentration is high.\nIn body tissues, oxyhaemoglobin releases oxygen where concentration is low.\n\nRed blood cells are made in the bone marrow and last about 120 days before being broken down in the spleen."
            },
            {
                "heading": "White Blood Cells",
                "content": "White blood cells are part of the IMMUNE SYSTEM — they defend the body against pathogens.\n\nUnlike red blood cells, white blood cells have a nucleus.\n\nThere are two main types:\n\nPHAGOCYTES:\nEngulf and destroy pathogens by PHAGOCYTOSIS — the cell membrane wraps around the pathogen and pulls it inside where enzymes digest it.\nNon-specific — they attack any pathogen they encounter.\nRespond quickly — first responders at an infection site.\n\nLYMPHOCYTES:\nProduce ANTIBODIES — proteins with a specific shape that binds to ANTIGENS on the surface of a specific pathogen.\nOne lymphocyte produces ONE type of antibody for ONE specific antigen.\nAntigens are molecules on the surface of pathogens that the immune system recognises as foreign.\nAfter infection, MEMORY LYMPHOCYTES remain in the blood for years or for life — if the same pathogen invades again, a rapid, large-scale antibody response destroys it before it can cause disease. This is the basis of IMMUNITY."
            },
            {
                "heading": "Platelets",
                "content": "Platelets are tiny cell FRAGMENTS — they are not complete cells and have no nucleus.\n\nWhen a blood vessel is damaged, platelets are involved in BLOOD CLOTTING:\n1. Platelets are activated and clump together at the wound site.\n2. A series of chemical reactions produces FIBRIN — a protein that forms a mesh of fibres.\n3. Red blood cells are trapped in the fibrin mesh → a CLOT forms.\n4. The clot dries to form a SCAB — sealing the wound, preventing blood loss and stopping pathogens from entering.\n\nWithout platelets, even a small cut could lead to dangerous blood loss and open infection."
            },
            {
                "heading": "Plasma",
                "content": "Plasma is the pale yellow LIQUID component of blood — it makes up about 55% of blood volume.\n\nPlasma transports almost everything in the blood:\nDigested food molecules — glucose and amino acids from the small intestine to cells.\nCarbon dioxide — from respiring cells to the lungs.\nUrea — from the liver (where it is made) to the kidneys (where it is excreted in urine).\nHormones — from endocrine glands to their target organs.\nAntibodies — produced by lymphocytes, carried to infection sites.\nHeat — distributes warmth from active muscles to cooler parts of the body, helping regulate body temperature."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Red blood cells carry oxygen — white blood cells do NOT carry oxygen. White blood cells fight infection. Platelets are NOT cells — they are cell fragments with no nucleus. They are involved in clotting, NOT in carrying oxygen or fighting infection.",
        "key_note": "Red blood cells: O₂ transport, haemoglobin, no nucleus, biconcave. White blood cells: immune defence — phagocytes engulf, lymphocytes make antibodies. Platelets: clotting. Plasma: liquid transport medium.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Blood Component to its Function",
            "instruction": "Match each blood component to its primary role.",
            "pairs": [
                ("Red blood cells", "Carry oxygen using haemoglobin — biconcave disc, no nucleus"),
                ("Phagocytes", "Engulf and destroy pathogens — non-specific immune defence"),
                ("Lymphocytes", "Produce specific antibodies that match pathogen antigens"),
                ("Platelets", "Involved in blood clotting — form a fibrin mesh to seal wounds"),
                ("Plasma", "Liquid that transports glucose, CO₂, urea, hormones and heat"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why do red blood cells have no nucleus?",
                "opts": [
                    ("To create more space for haemoglobin — allowing the cell to carry more oxygen", True),
                    ("So they can divide and replace themselves when worn out", False),
                    ("To reduce their weight so they flow faster through blood vessels", False),
                    ("So they can squeeze through capillaries more easily", False)
                ],
                "wrong_explanations": {
                    1: "Cells without a nucleus CANNOT divide — red blood cells are produced in bone marrow and cannot reproduce themselves.",
                    2: "Weight difference between a nucleus and haemoglobin molecules is negligible — the primary reason is space for haemoglobin.",
                    3: "Flexibility helps red blood cells squeeze through capillaries — but this is a result of their biconcave shape and flexibility, not the absence of a nucleus."
                }
            },
            {
                "q": "A patient has very few lymphocytes. What is the most likely consequence?",
                "opts": [
                    ("Unable to produce specific antibodies — prolonged or repeated infections that are hard to clear", True),
                    ("Unable to carry oxygen — severe anaemia", False),
                    ("Blood will not clot properly — excessive bleeding from wounds", False),
                    ("Unable to digest food properly — nutrients not absorbed", False)
                ],
                "wrong_explanations": {
                    1: "Oxygen carrying = RED BLOOD CELLS using haemoglobin. Lymphocytes are white blood cells.",
                    2: "Blood clotting = PLATELETS forming a fibrin mesh. Lymphocytes produce antibodies, not clotting factors.",
                    3: "Food digestion = digestive enzymes in the gut. Lymphocytes are part of the immune system."
                }
            },
            {
                "q": "What is the role of platelets in the body?",
                "opts": [
                    ("Blood clotting — they clump at wound sites and trigger fibrin mesh formation to seal the damage", True),
                    ("Carrying oxygen from the lungs to body tissues", False),
                    ("Producing antibodies to fight specific pathogens", False),
                    ("Engulfing and digesting bacteria by phagocytosis", False)
                ],
                "wrong_explanations": {
                    1: "Oxygen transport = RED BLOOD CELLS using haemoglobin.",
                    2: "Producing antibodies = LYMPHOCYTES (a type of white blood cell).",
                    3: "Engulfing bacteria = PHAGOCYTES (a type of white blood cell)."
                }
            },
            {
                "q": "Which substance does plasma NOT transport?",
                "opts": [
                    ("Oxygen — this is carried by haemoglobin inside red blood cells", True),
                    ("Glucose from the small intestine to body cells", False),
                    ("Urea from the liver to the kidneys", False),
                    ("Carbon dioxide from respiring cells to the lungs", False)
                ],
                "wrong_explanations": {
                    1: "Glucose IS carried in plasma — after absorption from the small intestine.",
                    2: "Urea IS carried in plasma — from the liver to the kidneys for excretion.",
                    3: "Carbon dioxide IS dissolved in plasma — most CO₂ travels as bicarbonate ions dissolved in plasma."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 6. CORONARY HEART DISEASE
    # ══════════════════════════════════════════════
    {
        "id": "coronary-heart-disease",
        "title": "Coronary Heart Disease",
        "spec": "4.2.3.3",
        "summary": "Describe the causes and treatments of coronary heart disease.",
        "theory": [
            {
                "heading": "What is Coronary Heart Disease?",
                "content": "Coronary heart disease (CHD) is a condition in which the CORONARY ARTERIES — the blood vessels that supply the heart muscle itself with oxygen and glucose — become narrowed and partially or completely blocked.\n\nThe heart muscle is always active, always respiring — it needs a continuous supply of oxygen. If this supply is reduced or cut off, the heart muscle cannot function properly.\n\nCHD is one of the leading causes of death in the UK and worldwide."
            },
            {
                "heading": "How CHD Develops — Atherosclerosis",
                "content": "CHD develops through a process called ATHEROSCLEROSIS:\n\n1. Over many years, fatty substances (mainly cholesterol) build up in the walls of the coronary arteries.\n2. These fatty deposits are called PLAQUES or ATHEROMAS.\n3. The plaques harden over time, making artery walls less elastic.\n4. The lumen (central channel) of the artery becomes progressively NARROWER.\n5. Blood flow to the heart muscle is reduced.\n6. If a plaque ruptures, a BLOOD CLOT can form at that site — this can completely block the artery.\n\nComplete blockage = HEART ATTACK. The heart muscle supplied by that artery receives no oxygen and begins to die. This causes severe chest pain, shortness of breath and can be fatal."
            },
            {
                "heading": "Risk Factors for CHD",
                "content": "Several factors increase the risk of developing CHD:\n\nLIFESTYLE FACTORS (can be changed):\nSMOKING — carbon monoxide damages artery walls; nicotine increases heart rate and blood pressure.\nHIGH BLOOD CHOLESTEROL — excess cholesterol deposits in artery walls forming plaques.\nHIGH BLOOD PRESSURE — damages artery walls, making them more susceptible to plaque formation.\nPOOR DIET — high in saturated fats and salt raises cholesterol and blood pressure.\nLACK OF EXERCISE — physical activity strengthens the heart and helps control weight and cholesterol.\nOBESITY — associated with high blood pressure, high cholesterol and type 2 diabetes.\n\nNON-LIFESTYLE FACTORS (cannot be changed):\nGENETICS — family history of CHD significantly increases risk.\nAGE — risk increases with age as arteries gradually narrow.\nSEX — males tend to develop CHD at younger ages than females (though risk equalises after menopause)."
            },
            {
                "heading": "Treatments for CHD",
                "content": "Several treatments can reduce the effects of CHD:\n\nSTATINS (medication):\nDrugs that reduce the level of LDL cholesterol in the blood.\nSlows the build-up of plaques in arteries.\nTaken daily — can significantly reduce heart attack and stroke risk.\nSide effects: muscle pain in some patients.\n\nSTENTS (surgical):\nA small metal mesh tube inserted into a narrowed coronary artery.\nHolds the artery open, restoring blood flow.\nInserted during a procedure called angioplasty — a thin tube is passed through a blood vessel to the narrowed area.\nEffective but does not treat the underlying cause.\n\nBYPASS SURGERY:\nA healthy blood vessel from another part of the body (e.g. leg vein) is grafted around the blocked section of coronary artery.\nCreates a new route for blood to reach the heart muscle.\nMajor surgery with risks, but effective for severe blockages.\n\nHEART TRANSPLANT:\nReplacing the entire diseased heart with a donor heart.\nLast resort for severe heart failure.\nRisks: immune rejection, waiting time for a suitable donor.\nPatient must take immunosuppressant drugs for life to prevent rejection."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A STENT holds a narrowed artery open — it does NOT bypass the blockage. A BYPASS SURGERY creates a new route around the blockage using a grafted blood vessel. Students often confuse these two treatments.",
        "key_note": "CHD = narrowed coronary arteries (atherosclerosis/plaques). Risk factors: smoking, high cholesterol, high blood pressure, poor diet, lack of exercise. Treatments: statins (lower cholesterol), stents (hold artery open), bypass surgery (reroute blood).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the CHD Treatment to How it Works",
            "instruction": "Match each treatment to its mechanism.",
            "pairs": [
                ("Statins", "Drugs that lower LDL cholesterol in the blood — slow plaque formation"),
                ("Stent", "Metal mesh tube inserted into a narrowed artery to hold it open"),
                ("Bypass surgery", "Grafts a healthy blood vessel around the blocked coronary artery"),
                ("Heart transplant", "Replaces the diseased heart — last resort, risk of rejection"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What causes coronary heart disease?",
                "opts": [
                    ("Fatty plaques (atherosclerosis) build up in the coronary arteries, narrowing them and reducing blood flow to the heart muscle", True),
                    ("The heart muscle becomes too weak to pump blood effectively due to overuse", False),
                    ("Blood becomes too thick and cannot flow through the coronary arteries", False),
                    ("The coronary arteries grow too narrow naturally with age", False)
                ],
                "wrong_explanations": {
                    1: "Heart muscle weakness (heart failure) is a consequence of CHD, not the cause — the cause is specifically fatty plaque build-up.",
                    2: "Blood viscosity can affect flow, but CHD is specifically about PLAQUE build-up in artery walls, not blood thickness.",
                    3: "Arteries don't naturally narrow with age — they narrow because of PLAQUES (fatty deposits) accumulating over time due to risk factors."
                }
            },
            {
                "q": "How does a stent treat coronary heart disease?",
                "opts": [
                    ("It is inserted into the narrowed artery and expands to hold it open — restoring blood flow", True),
                    ("It dissolves the fatty plaques blocking the artery", False),
                    ("It reroutes blood around the blocked artery using a grafted vessel", False),
                    ("It lowers blood cholesterol levels to prevent further plaque formation", False)
                ],
                "wrong_explanations": {
                    1: "Stents do not dissolve plaques — they physically hold the narrowed artery open.",
                    2: "Rerouting blood around a blockage using a grafted vessel = BYPASS SURGERY, not a stent.",
                    3: "Lowering cholesterol = STATINS (medication), not a stent."
                }
            },
            {
                "q": "Which of the following is a lifestyle risk factor for CHD that CAN be changed?",
                "opts": [
                    ("Smoking cigarettes", True),
                    ("Family history of heart disease (genetics)", False),
                    ("Being male", False),
                    ("Increasing age", False)
                ],
                "wrong_explanations": {
                    1: "Genetics is a risk factor — but you cannot change your DNA. It is a non-modifiable risk factor.",
                    2: "Sex (being male) slightly increases CHD risk, particularly at younger ages — but you cannot change this.",
                    3: "Age increases CHD risk, but everyone ages — you cannot avoid this risk factor."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 7. HEALTH, DISEASE AND RISK FACTORS
    # ══════════════════════════════════════════════
    {
        "id": "health-disease",
        "title": "Health, Disease and Risk Factors",
        "spec": "4.2.4",
        "summary": "Define health and disease, distinguish communicable from non-communicable diseases, and explain risk factors.",
        "theory": [
            {
                "heading": "Defining Health",
                "content": "The World Health Organisation (WHO) defines health as:\n'A state of complete physical, mental and social wellbeing — not merely the absence of disease or infirmity.'\n\nThis definition is important because it highlights that health is about more than just not being ill. A person can be free of physical disease but still be unhealthy if they have poor mental health or are isolated from society.\n\nGood health requires:\nPhysical wellbeing — the body functions properly, free from disease.\nMental wellbeing — good emotional and psychological state.\nSocial wellbeing — positive relationships and a functioning role in society."
            },
            {
                "heading": "Types of Disease",
                "content": "A disease is a condition that impairs the normal functioning of the body.\n\nCOMMUNICABLE DISEASES (infectious):\nCaused by pathogens — bacteria, viruses, fungi, protists.\nCan be spread from one organism to another.\nExamples: influenza, HIV, tuberculosis (TB), measles, malaria, salmonella food poisoning.\n\nNON-COMMUNICABLE DISEASES (non-infectious):\nCannot be spread from person to person.\nTypically caused by genetic factors, lifestyle choices or environmental exposure.\nExamples: coronary heart disease, type 2 diabetes, most cancers, asthma.\n\nInteractions between diseases: having one disease can affect the risk of developing another. For example:\nHIV weakens the immune system → patient more vulnerable to other infections.\nCancer treatment (chemotherapy) suppresses immunity → risk of other infections increases.\nDiabetes increases risk of cardiovascular disease."
            },
            {
                "heading": "Risk Factors",
                "content": "A risk factor is anything that increases the probability of developing a disease — but does NOT guarantee it.\n\nThere is an important distinction:\nCORRELATION — a statistical link between a risk factor and a disease.\nCAUSATION — evidence that the risk factor directly CAUSES the disease.\n\nMany risk factors show strong correlation with disease AND have been shown to cause disease through scientific study (e.g. smoking and lung cancer).\n\nOthers show correlation but causation is harder to prove.\n\nRisk factors can be:\nLIFESTYLE FACTORS (choices): smoking, diet, alcohol consumption, physical inactivity.\nENVIRONMENTAL FACTORS: air pollution, UV radiation, exposure to chemicals or asbestos.\nGENETIC FACTORS: inherited predispositions to certain diseases."
            },
            {
                "heading": "Non-Communicable Disease and Lifestyle",
                "content": "Non-communicable diseases are increasingly common in wealthy countries — often linked to lifestyle choices.\n\nKey links between lifestyle and non-communicable disease:\n\nSMOKING:\nStrongly linked to lung cancer, mouth cancer, throat cancer, bladder cancer.\nAlso linked to coronary heart disease and chronic obstructive pulmonary disease (COPD).\n\nALCOHOL:\nExcessive alcohol linked to liver disease (cirrhosis), liver cancer, mouth cancer, brain damage.\nIncreases risk of accidents and mental health problems.\n\nPOOR DIET:\nHigh saturated fat diet → high cholesterol → increased CHD risk.\nHigh sugar diet → type 2 diabetes, obesity.\nLow fibre diet → increased bowel cancer risk.\n\nLACK OF EXERCISE:\nIncreases risk of obesity, CHD, type 2 diabetes, some cancers.\n\nOBESITY (BMI > 30):\nStrongly linked to type 2 diabetes, CHD, high blood pressure, some cancers.\n\nUV RADIATION (from sunlight/sunbeds):\nCauses skin cancer (including melanoma — the most dangerous type)."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A risk factor INCREASES the probability of getting a disease — it does NOT mean you WILL get it. A non-smoker can develop lung cancer; a heavy smoker might not. Risk factors change the statistical likelihood, not the certainty. Also — correlation does NOT always mean causation, though for many lifestyle risk factors, both have been established.",
        "key_note": "Communicable = caused by pathogens, can spread. Non-communicable = cannot spread, often lifestyle-related. Risk factors: lifestyle (smoking, diet, alcohol), environmental (UV, pollution), genetic. Risk factor = increased probability, NOT certainty.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Communicable or Non-Communicable?",
            "instruction": "Sort each disease into communicable or non-communicable.",
            "pairs": [
                ("Communicable", "Influenza — caused by a virus, spread by droplets"),
                ("Non-communicable", "Coronary heart disease — caused by lifestyle factors and genetics"),
                ("Communicable", "Tuberculosis (TB) — caused by bacteria, spread by airborne droplets"),
                ("Non-communicable", "Type 2 diabetes — linked to obesity and diet, cannot be spread"),
                ("Communicable", "Malaria — caused by Plasmodium protist, spread by mosquito"),
                ("Non-communicable", "Skin cancer — caused by UV radiation, not spread between people"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the difference between a communicable and a non-communicable disease?",
                "opts": [
                    ("Communicable diseases are caused by pathogens and can spread between organisms. Non-communicable diseases cannot spread.", True),
                    ("Communicable diseases are always fatal. Non-communicable diseases are always mild.", False),
                    ("Communicable diseases are caused by lifestyle. Non-communicable diseases are caused by pathogens.", False),
                    ("They are the same thing — both terms describe infectious disease.", False)
                ],
                "wrong_explanations": {
                    1: "Neither type is always fatal or always mild — severity varies enormously in both categories.",
                    2: "This is exactly the wrong way round. Communicable = pathogens. Non-communicable = lifestyle, genetics, environment.",
                    3: "They are not the same — the key difference is whether the disease can be spread from person to person."
                }
            },
            {
                "q": "A study finds that people who eat more red meat have higher rates of bowel cancer. What does this show?",
                "opts": [
                    ("A correlation between red meat consumption and bowel cancer — further research is needed to establish causation", True),
                    ("Red meat DEFINITELY causes bowel cancer in everyone who eats it", False),
                    ("Bowel cancer causes people to eat more red meat", False),
                    ("This is meaningless data — correlations in diet studies are never reliable", False)
                ],
                "wrong_explanations": {
                    1: "Correlation does not automatically mean causation — the relationship could be due to other factors (e.g. diet quality overall, exercise levels).",
                    2: "This would be reverse causation — the data shows a link, but the disease developing before changing diet doesn't fit the timeline.",
                    3: "Epidemiological (population-based) data is valuable scientific evidence — correlation studies are an important first step in identifying risk factors."
                }
            },
            {
                "q": "Which of the following is a LIFESTYLE risk factor for non-communicable disease?",
                "opts": [
                    ("Smoking cigarettes", True),
                    ("Being 70 years old", False),
                    ("Having a family history of heart disease", False),
                    ("Living near a motorway (air pollution)", False)
                ],
                "wrong_explanations": {
                    1: "Age is a NON-LIFESTYLE (non-modifiable) risk factor — everyone ages and it cannot be changed.",
                    2: "Family history = GENETIC risk factor — also non-modifiable. You cannot choose your genes.",
                    3: "Living near a motorway = ENVIRONMENTAL risk factor — though this can sometimes be changed (by moving), it is generally classified as environmental rather than lifestyle."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 8. CANCER
    # ══════════════════════════════════════════════
    {
        "id": "cancer",
        "title": "Cancer",
        "spec": "4.2.4.1",
        "summary": "Explain how cancer develops, the difference between benign and malignant tumours, and how cancer is treated.",
        "theory": [
            {
                "heading": "What is Cancer?",
                "content": "Cancer is a disease caused by UNCONTROLLED CELL DIVISION.\n\nNormally, cell division is carefully regulated by genes that control the cell cycle — telling cells when to divide and when to stop.\n\nCancer begins when MUTATIONS occur in these regulatory genes:\nThe 'stop dividing' signals are ignored.\nCells keep dividing repeatedly, producing more and more abnormal cells.\nA mass of cells — called a TUMOUR — accumulates.\n\nCancers can develop in almost any tissue of the body. Common types include: breast cancer, lung cancer, bowel cancer, prostate cancer, skin cancer (melanoma)."
            },
            {
                "heading": "Benign vs Malignant Tumours",
                "content": "Not all tumours are cancerous. There are two types:\n\nBENIGN TUMOUR:\nGrows slowly and stays in ONE PLACE.\nDoes not invade surrounding tissues.\nCells remain enclosed in a capsule.\nDoes not spread to other parts of the body.\nUsually not life-threatening — can often be removed by surgery.\nCan cause problems if it presses on a vital structure (e.g. a benign brain tumour pressing on important brain regions).\n\nMALIGNANT TUMOUR (CANCER):\nGrows quickly and INVADES surrounding tissues.\nCells break away from the original tumour.\nTravel through the BLOOD or LYMPH system.\nSettle in other organs and form NEW TUMOURS — this spread is called METASTASIS.\nMuch harder to treat once it has spread.\nMalignant tumours are the dangerous, life-threatening form."
            },
            {
                "heading": "Risk Factors for Cancer",
                "content": "Several factors increase the risk of developing cancer:\n\nLIFESTYLE RISK FACTORS:\nSmoking — strongly linked to lung cancer, mouth cancer, throat cancer, bladder cancer. Carcinogens in tobacco smoke damage DNA in cells.\nAlcohol — linked to liver cancer, mouth and throat cancer.\nObesity — associated with bowel cancer, breast cancer, uterine cancer.\nPoor diet — low fibre linked to bowel cancer; processed meat linked to bowel cancer.\n\nENVIRONMENTAL RISK FACTORS:\nUV radiation — sunlight and sunbeds cause skin cancer by damaging DNA in skin cells.\nIonising radiation — X-rays, gamma rays and nuclear radiation can damage DNA.\nAsbestos — fibres lodge in lung tissue and damage cells → mesothelioma (lung cancer).\nCertain chemicals — industrial carcinogens.\n\nGENETIC RISK FACTORS:\nSome people inherit mutations in tumour suppressor genes (e.g. BRCA1/2 gene mutations increase breast and ovarian cancer risk).\nHaving a family history of certain cancers increases personal risk.\n\nVIRAL RISK FACTORS:\nHPV (Human Papillomavirus) — causes most cases of cervical cancer.\nHepatitis B and C viruses — linked to liver cancer."
            },
            {
                "heading": "Treatment of Cancer",
                "content": "Cancer is treated using several approaches, often in combination:\n\nSURGERY:\nPhysical removal of the tumour.\nEffective for localised (non-metastatic) tumours.\nCannot remove cancer that has spread throughout the body.\n\nRADIOTHERAPY:\nHigh-energy radiation (gamma rays or X-rays) is directed at tumour cells.\nDamages the DNA of cancer cells → they cannot divide → they die.\nSide effects: damages healthy cells near the tumour, causing fatigue, nausea, hair loss in the treatment area.\n\nCHEMOTHERAPY:\nDrugs that target rapidly dividing cells — killing cancer cells.\nCan reach cancer cells throughout the body, useful for metastatic cancer.\nSide effects: also damages rapidly dividing HEALTHY cells (hair follicles, gut lining, bone marrow) — causing hair loss, nausea, immune suppression."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "BENIGN tumours stay in one place and are not cancer. MALIGNANT tumours spread (metastasis) and are cancer. Students often use 'tumour' and 'cancer' interchangeably — a benign tumour is NOT cancer. Also: chemotherapy targets ALL rapidly dividing cells, not just cancer cells — that's why it causes hair loss and immune suppression as side effects.",
        "key_note": "Cancer = uncontrolled cell division caused by mutations in regulatory genes. Benign = stays put, not cancerous. Malignant = spreads via blood/lymph (metastasis) = cancer. Treatments: surgery, radiotherapy (gamma rays), chemotherapy (drugs).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Benign or Malignant?",
            "instruction": "Sort each description into benign tumour or malignant tumour.",
            "pairs": [
                ("Benign tumour", "Grows in one place — stays enclosed, does not invade surrounding tissues"),
                ("Malignant tumour", "Cells break away and travel through blood or lymph to form new tumours — metastasis"),
                ("Benign tumour", "Usually not life-threatening — often removed by surgery"),
                ("Malignant tumour", "Much harder to treat once it has spread to other organs"),
                ("Both", "Caused by uncontrolled cell division due to gene mutation"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the key difference between a benign and a malignant tumour?",
                "opts": [
                    ("Benign tumours stay in one place. Malignant tumours spread to other parts of the body (metastasis).", True),
                    ("Benign tumours grow faster than malignant tumours.", False),
                    ("Malignant tumours are caused by lifestyle; benign tumours are genetic.", False),
                    ("Benign tumours require chemotherapy; malignant tumours only need surgery.", False)
                ],
                "wrong_explanations": {
                    1: "Malignant tumours typically grow FASTER and spread — benign tumours tend to grow more slowly and stay localised.",
                    2: "Both types can have genetic or lifestyle causes — the distinction is about whether the tumour SPREADS, not its cause.",
                    3: "This is the wrong way round — surgery is often used for localised (benign or early malignant) tumours. Chemotherapy is used for cancer that has spread."
                }
            },
            {
                "q": "How does UV radiation cause skin cancer?",
                "opts": [
                    ("UV radiation damages DNA in skin cells — causing mutations in genes that control cell division", True),
                    ("UV radiation directly kills healthy skin cells, forcing the body to replace them rapidly", False),
                    ("UV radiation heats skin cells above their optimum temperature, causing them to mutate", False),
                    ("UV radiation reduces the immune system's ability to detect and destroy abnormal cells", False)
                ],
                "wrong_explanations": {
                    1: "UV radiation doesn't kill healthy cells en masse — it damages DNA specifically. Rapid replacement due to damage is related to wound healing, not cancer.",
                    2: "UV radiation doesn't work by heat — it carries photons that directly interact with and damage DNA molecules.",
                    3: "UV radiation can slightly suppress immunity, but the primary cancer-causing mechanism is direct DNA mutation in skin cells."
                }
            },
            {
                "q": "Why does chemotherapy cause hair loss as a side effect?",
                "opts": [
                    ("Chemotherapy targets all rapidly dividing cells — hair follicle cells divide rapidly, so they are also damaged", True),
                    ("Chemotherapy drugs are toxic to the scalp skin only", False),
                    ("The immune system attacks hair follicles as a reaction to chemotherapy drugs", False),
                    ("Chemotherapy only causes hair loss when combined with radiotherapy", False)
                ],
                "wrong_explanations": {
                    1: "Chemotherapy drugs are not scalp-specific — they circulate in the blood and affect rapidly dividing cells throughout the whole body.",
                    2: "The immune reaction to chemotherapy doesn't specifically target hair follicles — the damage is from the drugs directly targeting dividing cells.",
                    3: "Hair loss can occur from chemotherapy alone — it is caused by the drug mechanism, not only in combination with radiotherapy."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 9. PLANT TISSUES
    # ══════════════════════════════════════════════
    {
        "id": "plant-tissues",
        "title": "Plant Tissues and Organs",
        "spec": "4.2.5",
        "summary": "Describe the tissues found in plant organs and how they are adapted to their functions.",
        "theory": [
            {
                "heading": "Plant Organs",
                "content": "Plants are multicellular organisms with specialised organs, just like animals.\n\nThe main plant organs are:\nLEAF — the main site of photosynthesis and gas exchange.\nSTEM — provides support and transports substances between roots and leaves.\nROOT — anchors the plant and absorbs water and mineral ions from the soil.\nFLOWER — involved in reproduction.\n\nEach organ is made of different types of TISSUE, each adapted to its specific function."
            },
            {
                "heading": "Tissues in the Leaf",
                "content": "The leaf is the most important organ for photosynthesis. It contains several specialised tissues:\n\nEPIDERMIS (upper and lower):\nA thin, transparent layer covering the leaf surface.\nProduces a WAXY CUTICLE — a waterproof coating that reduces water loss by evaporation.\n\nPALISADE MESOPHYLL:\nFound in the upper part of the leaf — closest to sunlight.\nCells are tall and column-shaped, packed with many CHLOROPLASTS.\nThis is the main site of photosynthesis — receives maximum light.\n\nSPONGY MESOPHYLL:\nBelow the palisade layer.\nCells are loosely arranged with large AIR SPACES between them.\nAir spaces allow CO₂ to diffuse easily to photosynthesising cells.\nAlso allows O₂ produced by photosynthesis to diffuse out.\n\nGUARD CELLS and STOMATA:\nGuard cells are pairs of cells surrounding tiny pores called STOMATA (singular: stoma) on the lower leaf surface.\nStomata open to allow CO₂ in for photosynthesis and O₂ out — also allow water vapour to escape (transpiration).\nGuard cells control stomata opening: in the light, guard cells absorb water and become turgid → stomata OPEN. In the dark or when dehydrated, guard cells lose water → stomata CLOSE.\n\nXYLEM and PHLOEM:\nRun through the leaf as vascular bundles (veins).\nXylem brings water to the leaf. Phloem takes away sugars made by photosynthesis."
            },
            {
                "heading": "Xylem Tissue",
                "content": "Xylem is a tissue that transports WATER and dissolved MINERAL IONS from the roots upwards to the leaves.\n\nKey features of xylem cells:\nDEAD cells — no cytoplasm or nucleus, forming a completely hollow tube.\nNo end walls — cells are stacked end-to-end to form one continuous open column.\nWalls strengthened with LIGNIN — a hard, waterproof material that makes xylem very strong and prevents the tubes from collapsing.\nWater moves through xylem in one direction only — upwards.\n\nThe movement of water through xylem is driven by the TRANSPIRATION STREAM — water evaporating from leaves creates a pulling force that draws water up from the roots."
            },
            {
                "heading": "Phloem Tissue",
                "content": "Phloem is a tissue that transports dissolved SUGARS (mainly sucrose) from leaves to other parts of the plant. This process is called TRANSLOCATION.\n\nKey features of phloem cells:\nLIVING cells — unlike xylem, phloem cells are alive.\nSIEVE TUBES — cells with perforated end walls (sieve plates) that allow sugar solution to flow through.\nCOMPANION CELLS — next to each sieve tube cell, providing energy (ATP) for the active loading of sugars into the phloem.\n\nSugars travel in BOTH DIRECTIONS in phloem — from leaves (source) to roots, growing tips, fruits and other areas where sugar is needed (sinks)."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Xylem transports WATER and MINERALS. Phloem transports SUGARS. Students regularly mix these up. A good memory trick: Xylem = water (X for H2O is a stretch, but think: Xylem goes up like water). Phloem = food (sugars). Also: xylem cells are DEAD; phloem cells are LIVING.",
        "key_note": "Xylem: water + minerals, upwards only, dead cells, lignified walls. Phloem: sugars (translocation), both directions, living cells. Stomata: CO₂ in, O₂ and water vapour out. Controlled by guard cells.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Plant Tissue to its Function",
            "instruction": "Match each tissue to its role in the plant.",
            "pairs": [
                ("Xylem", "Transports water and mineral ions from roots to leaves — dead, hollow, lignified"),
                ("Phloem", "Transports dissolved sugars from leaves to the rest of the plant — translocation"),
                ("Palisade mesophyll", "Packed with chloroplasts near leaf surface — main site of photosynthesis"),
                ("Spongy mesophyll", "Air spaces between cells — allows CO₂ and O₂ to diffuse easily"),
                ("Guard cells", "Control opening and closing of stomata — regulate gas exchange and water loss"),
                ("Waxy cuticle", "Waterproof covering on epidermis — reduces water loss from the leaf"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is transported in xylem?",
                "opts": [
                    ("Water and dissolved mineral ions — upwards from roots to leaves", True),
                    ("Dissolved sugars from leaves to other parts of the plant", False),
                    ("Oxygen produced by photosynthesis", False),
                    ("Carbon dioxide for use in photosynthesis", False)
                ],
                "wrong_explanations": {
                    1: "Dissolved sugars = PHLOEM (translocation). Xylem carries water and minerals only.",
                    2: "Oxygen diffuses through air spaces in the spongy mesophyll and out through stomata — it doesn't travel in xylem.",
                    3: "CO₂ diffuses through stomata into air spaces — it doesn't travel in xylem."
                }
            },
            {
                "q": "Why are xylem cells dead?",
                "opts": [
                    ("Dead cells have no contents — forming a completely hollow tube for water to flow through without obstruction", True),
                    ("Xylem cells die because the lignin in their walls is toxic", False),
                    ("Dead cells are lighter, helping water move upwards against gravity", False),
                    ("Xylem cells die when the plant is no longer growing", False)
                ],
                "wrong_explanations": {
                    1: "Lignin is not toxic — it strengthens the walls. The cells die as part of their normal development, leaving behind a hollow lignified tube.",
                    2: "Dead cell content doesn't significantly change the weight of xylem — water moves upward due to the transpiration pull, not because of weight.",
                    3: "Xylem cells die as they mature during normal development, regardless of whether the plant is actively growing — this is a programmed developmental process."
                }
            },
            {
                "q": "What is the role of stomata in leaves?",
                "opts": [
                    ("Allow CO₂ in for photosynthesis and O₂ out — also allow water vapour to escape during transpiration", True),
                    ("Absorb water directly from the air into the leaf", False),
                    ("Produce the waxy cuticle to reduce water loss", False),
                    ("Store glucose produced by photosynthesis", False)
                ],
                "wrong_explanations": {
                    1: "Stomata can absorb some water vapour in humid conditions, but their primary function is gas EXCHANGE, not water absorption.",
                    2: "The waxy cuticle is produced by the EPIDERMIS cells — it is a secreted layer, not produced by stomata.",
                    3: "Glucose storage as starch happens in chloroplasts and other cells — stomata are pores for gas exchange."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 10. TRANSPIRATION
    # ══════════════════════════════════════════════
    {
        "id": "transpiration",
        "title": "Transpiration",
        "spec": "4.2.5.2",
        "summary": "Describe transpiration and the factors that affect its rate.",
        "theory": [
            {
                "heading": "What is Transpiration?",
                "content": "Transpiration is the evaporation of water from the leaves (and other aerial parts) of a plant.\n\nWater is absorbed by roots → travels up the stem through xylem → reaches the leaves → evaporates through stomata as water vapour into the atmosphere.\n\nThis continuous movement of water from roots to leaves through the xylem is called the TRANSPIRATION STREAM.\n\nHow it works: as water evaporates from leaf cells into the air spaces and out through stomata, the cells become slightly drier → they absorb water from neighbouring cells by osmosis → this creates a pulling force that draws water up through the xylem all the way from the roots.\n\nThis pull is called TRANSPIRATION PULL — it works because water molecules are attracted to each other (cohesion) and to the xylem walls (adhesion), forming a continuous column of water."
            },
            {
                "heading": "Why Transpiration Matters",
                "content": "Transpiration serves several important functions:\n\nWATER SUPPLY — transports water from roots to leaves where it is needed for photosynthesis.\n\nMINERAL TRANSPORT — mineral ions dissolved in water are carried up from the roots to the leaves.\n\nCOOLING — evaporation of water from leaf surfaces has a cooling effect — similar to sweating in humans.\n\nHowever, too much transpiration is a problem — excessive water loss can cause wilting and ultimately death. Plants have several adaptations to reduce water loss (waxy cuticle, closing stomata, reduced leaf surface area in dry environments)."
            },
            {
                "heading": "Factors That Increase the Rate of Transpiration",
                "content": "Four main factors affect how fast water evaporates from leaves:\n\n1. TEMPERATURE:\nHigher temperature → more kinetic energy → water molecules evaporate faster from leaf surface → steeper concentration gradient between leaf and air → faster transpiration.\n\n2. LIGHT INTENSITY:\nBrighter light → stomata open WIDER to allow more CO₂ in for photosynthesis → more water vapour can escape → faster transpiration.\nIn the dark, stomata close → transpiration almost stops.\n\n3. HUMIDITY:\nLow humidity (dry air) → large difference in water vapour concentration between inside the leaf and outside → steep diffusion gradient → faster transpiration.\nHigh humidity (moist air) → gradient is smaller → slower transpiration.\n\n4. AIR MOVEMENT / WIND:\nWind blows away water vapour that has accumulated near the stomata → prevents the air near the leaf becoming saturated → maintains a steep diffusion gradient → faster transpiration.\nIn still air, a layer of moist air builds up around the leaf → reduces the gradient → slows transpiration."
            },
            {
                "heading": "Measuring Transpiration — The Potometer",
                "content": "A POTOMETER is an apparatus used to measure the rate of water uptake by a plant shoot — used as an indicator of transpiration rate.\n\nHow it works:\nA leafy shoot is placed in a sealed tube of water with a capillary tube attached.\nAs the plant transpires and takes up water, an air bubble in the capillary tube moves towards the plant.\nThe DISTANCE the bubble moves per unit time = rate of water uptake.\n\nThe potometer measures water UPTAKE, not transpiration directly — but the two are closely related.\n\nYou can investigate the effect of each environmental factor by:\nChanging temperature (place near heater or in cold room).\nChanging light intensity (move lamp closer/further).\nChanging humidity (blow dry air at the plant or enclose in moist environment).\nChanging air movement (use a fan)."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Transpiration is fastest in HOT, BRIGHT, DRY and WINDY conditions. Students often get humidity wrong — LOW humidity means DRY air which INCREASES transpiration rate (bigger concentration gradient for water vapour). HIGH humidity SLOWS transpiration. Think of it like this: dry air 'pulls' the water out of the leaf faster.",
        "key_note": "Transpiration: water evaporates from stomata → transpiration pull draws water up xylem from roots. Fastest in: high temperature, high light intensity, low humidity, high wind. Measured with a potometer.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Does this Speed Up or Slow Down Transpiration?",
            "instruction": "Sort each condition — does it increase or decrease the rate of transpiration?",
            "pairs": [
                ("Increases transpiration", "High temperature — more kinetic energy, faster evaporation"),
                ("Increases transpiration", "Bright light — stomata open wider, more water vapour escapes"),
                ("Increases transpiration", "Low humidity (dry air) — steep concentration gradient for water vapour"),
                ("Increases transpiration", "Wind — blows away moist air near stomata, maintains steep gradient"),
                ("Decreases transpiration", "High humidity — gradient between leaf and air is reduced"),
                ("Decreases transpiration", "Darkness — stomata close, water vapour cannot escape"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is transpiration?",
                "opts": [
                    ("The evaporation of water from the leaves of a plant through the stomata", True),
                    ("The transport of dissolved sugars from leaves to the rest of the plant", False),
                    ("The absorption of water by root hair cells from the soil", False),
                    ("The process of photosynthesis producing water as a product", False)
                ],
                "wrong_explanations": {
                    1: "Transport of dissolved sugars = TRANSLOCATION (in phloem). Transpiration is specifically water evaporation from leaves.",
                    2: "Water absorption by roots = OSMOSIS through root hair cells. Transpiration is what happens at the LEAVES end.",
                    3: "Photosynthesis produces OXYGEN, not water — water is a REACTANT of photosynthesis (6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂)."
                }
            },
            {
                "q": "A plant is moved from a humid greenhouse to a dry, windy environment. What happens to its transpiration rate?",
                "opts": [
                    ("Transpiration increases significantly — lower humidity and wind both increase the rate", True),
                    ("Transpiration decreases — the plant closes its stomata to conserve water", False),
                    ("Transpiration stays the same — the two factors cancel each other out", False),
                    ("Transpiration increases due to humidity but decreases due to wind — net effect is zero", False)
                ],
                "wrong_explanations": {
                    1: "The plant may eventually close stomata if it loses too much water — but the immediate effect of moving to dry, windy conditions is faster transpiration. Stomata closing is a response to stress, not an immediate automatic reaction.",
                    2: "The two factors don't cancel out — both low humidity AND wind INCREASE transpiration rate. They act in the same direction.",
                    3: "Both low humidity and wind INCREASE transpiration — humidity and wind both affect the concentration gradient for water vapour in the same way (they both maintain a steep gradient)."
                }
            },
            {
                "q": "Why do plants transpire faster in brighter light?",
                "opts": [
                    ("Brighter light causes stomata to open wider — allowing more water vapour to escape", True),
                    ("Brighter light increases the temperature of the leaf, causing faster evaporation", False),
                    ("Brighter light increases the rate of photosynthesis, which produces more water", False),
                    ("Brighter light makes chlorophyll absorb water directly from the air", False)
                ],
                "wrong_explanations": {
                    1: "Brighter light does warm leaves slightly — but the PRIMARY mechanism is guard cells responding to light by opening stomata wider.",
                    2: "Photosynthesis uses water as a REACTANT — it consumes water, not produces it. Oxygen is the gas product.",
                    3: "Chlorophyll absorbs LIGHT energy — it does not absorb water from the air."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 11. TRANSLOCATION
    # ══════════════════════════════════════════════
    {
        "id": "translocation",
        "title": "Translocation",
        "spec": "4.2.5.3",
        "summary": "Describe translocation and how it differs from transpiration.",
        "theory": [
            {
                "heading": "What is Translocation?",
                "content": "Translocation is the transport of dissolved SUGARS (mainly SUCROSE) through the PHLOEM from where they are produced to where they are needed or stored.\n\nSource → Sink:\nSOURCE — the place where sugars are made or released (mainly the LEAVES, where photosynthesis takes place).\nSINK — any place where sugars are used or stored:\nGrowing shoot tips — sugars needed for cell division and growth.\nRoots — sugars needed for respiration and converted to starch for storage.\nFruits and seeds — sugars needed for development.\nFlowers — sugars needed for reproduction.\n\nUnlike the transpiration stream, translocation can move sugars in BOTH DIRECTIONS in the phloem — up to growing tips AND down to roots and storage organs."
            },
            {
                "heading": "How Translocation Works",
                "content": "Sucrose is ACTIVELY LOADED into phloem sieve tubes at the source (leaves) using energy (ATP) from companion cells.\n\nThis creates a high concentration of sucrose in the phloem at the source end.\n\nWater enters the phloem by osmosis (moving from xylem, where it's more dilute) → increases pressure at the source end.\n\nThis pressure drives the flow of sugar solution THROUGH the phloem towards the sink.\n\nAt the sink, sucrose is actively UNLOADED from the phloem and used or converted to starch for storage.\n\nThis reduces the concentration at the sink end, maintaining the pressure difference and keeping the flow going."
            },
            {
                "heading": "Transpiration vs Translocation — Key Differences",
                "content": "Students often confuse these two transport processes. Here is a clear comparison:\n\nTRANSPIRATION:\nSubstance moved: WATER (and dissolved minerals)\nVessel: XYLEM\nDirection: UPWARDS ONLY (roots → leaves)\nCells: DEAD cells\nDriving force: evaporation from leaves creating transpiration pull\nEnergy: PASSIVE (no ATP needed)\n\nTRANSLOCATION:\nSubstance moved: SUGARS (sucrose)\nVessel: PHLOEM\nDirection: BOTH DIRECTIONS (source → sink)\nCells: LIVING cells\nDriving force: active loading of sucrose creates pressure\nEnergy: ACTIVE (ATP required to load/unload sucrose)"
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Translocation = SUGARS in PHLOEM. Transpiration = WATER in XYLEM. These are the two most commonly confused terms in plant biology. Translocation moves in BOTH directions — transpiration only goes UPWARDS. Phloem cells are LIVING — xylem cells are DEAD.",
        "key_note": "Translocation: sucrose in phloem, source (leaves) to sink (roots, fruits, tips), both directions, living cells, uses ATP. NOT the same as transpiration (water in xylem, upwards only, dead cells, passive).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Transpiration or Translocation?",
            "instruction": "Sort each statement into transpiration or translocation.",
            "pairs": [
                ("Transpiration", "Water moves up through xylem from roots to leaves — pulled by evaporation"),
                ("Translocation", "Sucrose moves through phloem from leaves to growing roots and fruits"),
                ("Transpiration", "Involves dead, hollow, lignified cells"),
                ("Translocation", "Can move substances both upwards and downwards in the plant"),
                ("Transpiration", "Rate increases in hot, bright, dry and windy conditions"),
                ("Translocation", "Requires ATP energy — companion cells supply energy to sieve tubes"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the main substance transported in phloem?",
                "opts": [
                    ("Sucrose (dissolved sugar) — from leaves to other parts of the plant", True),
                    ("Water and dissolved mineral ions — from roots to leaves", False),
                    ("Oxygen produced by photosynthesis", False),
                    ("Carbon dioxide for use in photosynthesis", False)
                ],
                "wrong_explanations": {
                    1: "Water and minerals = XYLEM transport (transpiration stream). Phloem carries sugars.",
                    2: "Oxygen diffuses through air spaces and out through stomata — it is not transported in phloem.",
                    3: "CO₂ diffuses through stomata into the leaf — it is not transported in phloem."
                }
            },
            {
                "q": "In which direction does translocation move?",
                "opts": [
                    ("Both upwards and downwards — from source (leaves) to any sink where sugar is needed", True),
                    ("Upwards only — like the transpiration stream in xylem", False),
                    ("Downwards only — gravity pulls the sugar solution down to the roots", False),
                    ("Outwards only — from the centre of the stem to the leaf surfaces", False)
                ],
                "wrong_explanations": {
                    1: "Upwards only = TRANSPIRATION in XYLEM. Translocation in phloem moves in both directions depending on where the sink is.",
                    2: "If translocation were downwards only, growing shoot tips at the top of the plant could never receive sugars — but they clearly do.",
                    3: "Translocation moves along the length of the plant (up and down), not outwards from centre to leaf surface."
                }
            },
            {
                "q": "What is a 'sink' in the context of translocation?",
                "opts": [
                    ("Any part of the plant where sugars are used or stored — e.g. roots, fruits, growing tips", True),
                    ("The leaves — where sugars are produced by photosynthesis", False),
                    ("The phloem vessels that transport sugars through the plant", False),
                    ("The stomata — where water and gases are exchanged", False)
                ],
                "wrong_explanations": {
                    1: "The leaves are the SOURCE — where sugars are MADE. A sink is the DESTINATION where sugars are used or stored.",
                    2: "The phloem is the VESSEL — not the destination. Sinks are the organs that USE or STORE the sugars.",
                    3: "Stomata are gas exchange pores — they have no role in the source-sink relationship of translocation."
                }
            }
        ]
    },
],

"infection-response": [


    # ══════════════════════════════════════════════
    # 1. COMMUNICABLE DISEASES AND HUMAN DEFENCE
    # ══════════════════════════════════════════════
    {
        "id": "communicable-diseases-defence",
        "title": "Communicable Diseases and Human Defence Systems",
        "spec": "4.3.1",
        "summary": "Describe what communicable diseases are, how pathogens spread and how the body defends itself.",
        "theory": [
            {
                "heading": "What is a Communicable Disease?",
                "content": "A communicable disease (also called an infectious disease) is one caused by a PATHOGEN — a microorganism that infects and harms the host.\n\nCommunicable diseases can be SPREAD from one organism to another — either directly or through a vector (a carrier organism like a mosquito).\n\nThere are four main types of pathogen:\nBACTERIA — single-celled prokaryotes. Reproduce rapidly by binary fission inside the body. Cause disease mainly by producing TOXINS. Examples: Salmonella, Gonorrhoea, Tuberculosis.\nVIRUSES — not true cells. Much smaller than bacteria. Enter host cells and use the cell's machinery to replicate, destroying the host cell in the process. Examples: Measles, HIV, Influenza, TMV.\nFUNGI — eukaryotic organisms. Grow on or in host tissue. Examples: Athlete's foot, Rose black spot.\nPROTISTS — single-celled eukaryotes. Examples: Plasmodium (causes malaria)."
            },
            {
                "heading": "How Pathogens Spread",
                "content": "Pathogens use different routes to move from one host to another:\n\nAIRBORNE DROPLETS — coughing, sneezing, talking release tiny droplets containing pathogens. Examples: influenza, measles, COVID-19, tuberculosis.\n\nCONTAMINATED WATER — drinking or bathing in water containing pathogens. Example: cholera (bacteria), typhoid.\n\nDIRECT CONTACT — skin contact, sexual contact, touching contaminated surfaces. Examples: athlete's foot (skin contact), gonorrhoea (sexual contact), rose black spot (plant contact).\n\nVECTORS — an organism that carries the pathogen but doesn't cause the disease itself. Example: Anopheles mosquito carries Plasmodium (malaria) and injects it when it bites.\n\nCONTAMINATED FOOD — eating food containing pathogens. Example: Salmonella in undercooked poultry.\n\nBLOOD CONTACT — sharing needles, transfusions. Example: HIV, Hepatitis B."
            },
            {
                "heading": "The Body's Physical and Chemical Barriers",
                "content": "The body has several lines of defence against pathogens — the first line stops pathogens from entering at all.\n\nSKIN — a tough, continuous physical barrier. As long as the skin is unbroken, most pathogens cannot pass through it. The skin also produces slightly acidic secretions that inhibit bacterial growth.\n\nMUCUS — goblet cells in the lining of the airways, nose and throat produce sticky mucus. Pathogens and particles breathed in get trapped in this mucus before they can reach the lungs.\n\nCILIA — tiny hair-like structures on the cells lining the trachea and bronchi. They beat rhythmically, sweeping the mucus (with trapped pathogens) upwards towards the throat where it is swallowed. The stomach acid then kills any pathogens.\n\nSTOMACH ACID — hydrochloric acid (HCl) in the stomach is very acidic (pH ~2). Most pathogens that are swallowed are killed here before they can cause infection."
            },
            {
                "heading": "The Immune System — White Blood Cells",
                "content": "If pathogens get past the physical barriers, the IMMUNE SYSTEM takes over.\n\nPHAGOCYTES:\nThese are white blood cells that carry out PHAGOCYTOSIS — they identify and engulf (eat) pathogens.\nThe cell membrane wraps around the pathogen and pulls it inside the cell.\nEnzymes inside the phagocyte then digest and destroy it.\nPhagocytes are NON-SPECIFIC — they attack any pathogen they encounter without needing to learn its identity first.\n\nLYMPHOCYTES:\nThese white blood cells produce ANTIBODIES — proteins with a specific shape that binds to ANTIGENS on the surface of a particular pathogen.\nEach lymphocyte makes ONE type of antibody for ONE specific antigen.\nAntigens are molecules on the surface of pathogens that the immune system identifies as foreign.\nAntibodies can neutralise pathogens, mark them for destruction, or cause them to clump together.\nAfter an infection, MEMORY CELLS remain in the blood for years or for life.\nIf the same pathogen invades again, memory cells rapidly produce large quantities of antibodies — destroying the pathogen before it causes disease. This is IMMUNITY."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Antibiotics kill BACTERIA only — they have absolutely NO effect on viruses. Never say 'take antibiotics for a virus'. Flu is caused by a virus — antibiotics will not help. Also: phagocytes ENGULF pathogens. Lymphocytes PRODUCE ANTIBODIES. These are different white blood cells with different jobs.",
        "key_note": "Physical barriers: skin, mucus, cilia, stomach acid — first line of defence. Phagocytes: engulf and destroy (non-specific). Lymphocytes: make specific antibodies. Memory cells: rapid response on re-infection = immunity.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Defence to How it Works",
            "instruction": "Match each defence mechanism to its correct description.",
            "pairs": [
                ("Skin", "Physical barrier — prevents pathogens entering the body as long as it is unbroken"),
                ("Cilia", "Sweep mucus with trapped pathogens upwards towards the throat"),
                ("Stomach acid", "pH ~2 — kills most pathogens that are swallowed"),
                ("Phagocytes", "Engulf and digest pathogens — non-specific immune defence"),
                ("Lymphocytes", "Produce specific antibodies that bind to pathogen antigens"),
                ("Memory cells", "Remain after infection — allow rapid antibody response if same pathogen returns"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the difference between a phagocyte and a lymphocyte?",
                "opts": [
                    ("Phagocytes engulf pathogens non-specifically. Lymphocytes produce specific antibodies.", True),
                    ("Phagocytes produce antibodies. Lymphocytes engulf pathogens.", False),
                    ("Both engulf pathogens — they are the same type of white blood cell.", False),
                    ("Phagocytes fight bacterial infections only. Lymphocytes fight viral infections only.", False)
                ],
                "wrong_explanations": {
                    1: "This is exactly the wrong way around. Phagocytes = engulf. Lymphocytes = antibodies.",
                    2: "Both are white blood cells but they have completely different functions — phagocytes engulf, lymphocytes make antibodies.",
                    3: "Both types of white blood cell work against a wide range of pathogens — they are not limited to one type of infection."
                }
            },
            {
                "q": "Why are memory cells important for immunity?",
                "opts": [
                    ("They remain in the blood after infection and allow a rapid, large antibody response if the same pathogen is encountered again", True),
                    ("They physically block pathogens from entering the bloodstream", False),
                    ("They produce antibiotics to destroy bacterial infections", False),
                    ("They replace damaged body cells after an infection has passed", False)
                ],
                "wrong_explanations": {
                    1: "Memory cells are immune cells — they don't form physical barriers. That role belongs to skin, mucus and cilia.",
                    2: "Antibiotics are medicines — they are not produced by any body cells. Memory cells produce antibodies, not antibiotics.",
                    3: "Cell replacement is done by stem cells and normal cell division — memory cells specifically remember and respond to specific pathogens."
                }
            },
            {
                "q": "How does the Anopheles mosquito spread malaria?",
                "opts": [
                    ("It is a vector — it carries the Plasmodium protist and injects it into humans when it bites", True),
                    ("The mosquito itself causes malaria — it is the pathogen", False),
                    ("Mosquito bites break the skin, allowing malaria bacteria from the air to enter", False),
                    ("The mosquito contaminates water sources with Plasmodium", False)
                ],
                "wrong_explanations": {
                    1: "The MOSQUITO is the vector — Plasmodium is the pathogen. The mosquito carries and transmits Plasmodium but does not cause the disease itself.",
                    2: "Malaria is caused by a PROTIST (Plasmodium) — not bacteria. And it is injected through the bite, not from the air.",
                    3: "Malaria is transmitted through bites — not through water. Cholera spreads through contaminated water."
                }
            },
            {
                "q": "Why does the body produce mucus in the airways?",
                "opts": [
                    ("To trap inhaled pathogens and particles before they reach the lungs — cilia then sweep the mucus up to be swallowed", True),
                    ("To provide a moist surface for gas exchange in the lungs", False),
                    ("To produce antibodies that neutralise pathogens in the airways", False),
                    ("To prevent the airways from drying out in cold weather", False)
                ],
                "wrong_explanations": {
                    1: "Gas exchange occurs in the ALVEOLI — the main function of mucus in the airways is trapping pathogens, not gas exchange.",
                    2: "Antibodies are produced by LYMPHOCYTES in the blood — not by mucus. Mucus is a physical/chemical barrier.",
                    3: "Moisture in the airways is a secondary benefit — the PRIMARY function of mucus is trapping pathogens and particles."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 2. VIRAL DISEASES
    # ══════════════════════════════════════════════
    {
        "id": "viral-diseases",
        "title": "Viral Diseases",
        "spec": "4.3.1.2",
        "summary": "Describe the main viral diseases — measles, HIV/AIDS and tobacco mosaic virus.",
        "theory": [
            {
                "heading": "How Viruses Cause Disease",
                "content": "Viruses are not living cells — they are particles of genetic material (DNA or RNA) surrounded by a protein coat.\n\nThey cannot reproduce on their own — they must invade a HOST CELL and use the cell's own machinery to make copies of themselves.\n\nThis process destroys the host cell when new virus particles burst out.\n\nViruses cause disease by:\nDestroying cells as they replicate.\nTriggering an immune response (the fever, aches and fatigue you feel are largely your immune system fighting the virus).\nDisrupting normal organ function."
            },
            {
                "heading": "Measles",
                "content": "CAUSE: Measles virus (a paramyxovirus).\n\nTRANSMISSION: Airborne droplets — spread very easily through coughing, sneezing and close contact.\n\nSYMPTOMS:\nHigh fever.\nRed, blotchy skin rash spreading from face to body.\nRunny nose, cough, sore red eyes.\nWhite spots inside the mouth (Koplik's spots — a diagnostic sign).\n\nCOMPLICATIONS: Measles can be very serious — can lead to pneumonia (lung infection), encephalitis (brain inflammation) and death, particularly in malnourished children or immunocompromised individuals.\n\nPREVENTION: The MMR vaccine (measles, mumps, rubella) — given in two doses in childhood. Highly effective.\n\nTREATMENT: No specific antiviral drug — rest, fluids, paracetamol for fever. The immune system clears the infection."
            },
            {
                "heading": "HIV and AIDS",
                "content": "CAUSE: HIV (Human Immunodeficiency Virus) — a retrovirus.\n\nTRANSMISSION: Through bodily fluids — unprotected sexual contact, sharing needles, blood transfusions (in countries without screening), mother to baby (during pregnancy, birth or breastfeeding).\n\nWHAT HIV DOES: HIV specifically targets and destroys CD4+ T-helper lymphocytes — the very cells that coordinate the immune response. Over time, the immune system is progressively weakened.\n\nAIDS: AIDS (Acquired Immune Deficiency Syndrome) develops when HIV has destroyed so many lymphocytes that the immune system can no longer function. The patient becomes vulnerable to OPPORTUNISTIC INFECTIONS — infections that a healthy immune system would easily fight off (e.g. rare pneumonias, certain cancers).\n\nPREVENTION: Condoms, clean needles, screening blood supplies, antiretroviral drugs for pregnant women with HIV.\n\nTREATMENT: ANTIRETROVIRAL DRUGS (ARVs) — prevent HIV from replicating. Cannot cure HIV but allow patients to live near-normal lives. Must be taken for life."
            },
            {
                "heading": "Tobacco Mosaic Virus (TMV)",
                "content": "CAUSE: Tobacco mosaic virus — affects a wide range of plants including tobacco, tomatoes, peppers and cucumbers.\n\nTRANSMISSION: Direct contact between plants, contaminated tools, insects feeding on plants, and handling by humans.\n\nSYMPTOMS: A distinctive MOSAIC PATTERN of light and dark green or yellow patches on leaves. Leaves may also be distorted or stunted.\n\nWHY IT'S HARMFUL: Infected cells cannot produce chlorophyll properly. The mosaic-patterned leaves have LESS CHLOROPHYLL than healthy leaves → reduced rate of photosynthesis → plant grows poorly and produces less fruit/yield.\n\nPREVENTION: Removing and destroying infected plants, cleaning tools, using virus-free seeds, controlling insect vectors."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "HIV and AIDS are NOT the same thing. HIV is the VIRUS. AIDS is the CONDITION that develops when HIV has destroyed enough lymphocytes that the immune system collapses. You can have HIV for many years without having AIDS if treated with ARVs. Also: antibiotics DO NOT treat viral infections — not measles, not HIV, not flu.",
        "key_note": "Measles: droplets, rash + fever, MMR vaccine prevents it. HIV: bodily fluids, destroys lymphocytes → AIDS, managed with ARVs. TMV: plant virus, mosaic leaf pattern, reduced photosynthesis.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Viral Disease to its Key Features",
            "instruction": "Match each disease to its transmission route and key symptom.",
            "pairs": [
                ("Measles", "Airborne droplets — red skin rash and high fever — prevented by MMR vaccine"),
                ("HIV", "Bodily fluids — destroys T-lymphocytes — eventually causes AIDS"),
                ("Tobacco mosaic virus", "Contact/tools — mosaic discolouration of leaves — reduced photosynthesis"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does HIV lead to AIDS?",
                "opts": [
                    ("HIV destroys T-lymphocytes — the immune system becomes too weak to fight off infections", True),
                    ("HIV produces toxins that directly damage all organs simultaneously", False),
                    ("HIV causes the body to overproduce white blood cells, overwhelming the system", False),
                    ("HIV converts into the AIDS virus after several years in the body", False)
                ],
                "wrong_explanations": {
                    1: "HIV specifically targets immune cells — it doesn't produce toxins that damage other organs directly.",
                    2: "HIV destroys white blood cells (lymphocytes) — it does not cause overproduction.",
                    3: "HIV doesn't 'convert' into AIDS — AIDS is the CONDITION resulting from immune system collapse caused by HIV destroying lymphocytes."
                }
            },
            {
                "q": "How does tobacco mosaic virus affect plant growth?",
                "opts": [
                    ("It disrupts chlorophyll production — leaves develop mosaic discolouration and photosynthesise less efficiently", True),
                    ("It blocks the xylem, preventing water reaching the leaves", False),
                    ("It causes root cells to die, so the plant cannot absorb minerals", False),
                    ("It produces toxins that kill plant cells directly", False)
                ],
                "wrong_explanations": {
                    1: "TMV affects leaf cells and chlorophyll — not the xylem. The reduced photosynthesis from less chlorophyll is the key effect.",
                    2: "TMV infects leaf cells, not root cells. Mineral absorption is unaffected directly.",
                    3: "TMV disrupts chlorophyll production in leaf cells — it doesn't produce toxins that kill cells outright."
                }
            },
            {
                "q": "A measles patient is told to rest and take paracetamol. Why are they not given antibiotics?",
                "opts": [
                    ("Measles is caused by a virus — antibiotics only kill bacteria and have no effect on viruses", True),
                    ("Antibiotics would make the rash worse", False),
                    ("The patient is too young for antibiotics", False),
                    ("Paracetamol is stronger than antibiotics", False)
                ],
                "wrong_explanations": {
                    1: "Rash worsening from antibiotics is not a reason — the fundamental reason is that antibiotics target bacterial cell walls and structures that viruses simply don't have.",
                    2: "Age is not the deciding factor — the pathogen type is. Antibiotics don't work on viruses regardless of patient age.",
                    3: "Paracetamol relieves symptoms — it does not treat the infection. Antibiotics treat bacterial infections — but measles is viral."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 3. BACTERIAL DISEASES
    # ══════════════════════════════════════════════
    {
        "id": "bacterial-diseases",
        "title": "Bacterial Diseases",
        "spec": "4.3.1.3",
        "summary": "Describe Salmonella food poisoning and Gonorrhoea as examples of bacterial diseases.",
        "theory": [
            {
                "heading": "How Bacteria Cause Disease",
                "content": "Bacteria are single-celled prokaryotes. They can reproduce very rapidly — doubling every 20 minutes under ideal conditions.\n\nBacteria cause disease in two main ways:\nPRODUCING TOXINS — many bacteria secrete chemicals (toxins) that damage cells and tissues. It is often the toxins, not the bacteria themselves, that cause the symptoms of disease.\nDIRECT CELL DAMAGE — some bacteria invade and destroy body cells directly.\n\nUnlike viruses, bacteria CAN be treated with ANTIBIOTICS — drugs that specifically target bacterial structures (e.g. cell walls) that human cells don't have."
            },
            {
                "heading": "Salmonella Food Poisoning",
                "content": "CAUSE: Salmonella bacteria (various species).\n\nTRANSMISSION: Eating food contaminated with Salmonella — most commonly undercooked poultry, raw or undercooked eggs, unpasteurised milk. Also spread through poor kitchen hygiene (cross-contamination from raw to cooked food) and unwashed hands.\n\nSYMPTOMS: Begin 12–72 hours after eating contaminated food:\nFever.\nStomach cramps and abdominal pain.\nVomiting.\nDiarrhoea (which can be severe and bloody).\nSymptoms usually last 4–7 days.\n\nMECHANISM: Salmonella bacteria survive cooking if the food isn't heated properly. They reach the small intestine, colonise the gut lining and produce toxins — causing the symptoms.\n\nPREVENTION: Thorough cooking (bacteria are killed by heat), good hygiene (wash hands, clean surfaces), refrigeration (slows bacterial growth), pasteurisation of dairy products, vaccination of poultry flocks.\n\nTREATMENT: Most cases resolve without antibiotics — rest and plenty of fluids. Severe cases may need antibiotics and hospital treatment."
            },
            {
                "heading": "Gonorrhoea",
                "content": "CAUSE: Neisseria gonorrhoeae bacteria.\n\nTRANSMISSION: Sexual contact — a sexually transmitted infection (STI). Passed during vaginal, anal or oral sex without barrier contraception.\n\nSYMPTOMS:\nIN FEMALES: Often NO symptoms (asymptomatic) — this makes it particularly dangerous as it can spread unknowingly. When symptoms occur: thick yellow/green vaginal discharge, pain when urinating.\nIN MALES: Thick yellow/green discharge from the penis, burning pain when urinating.\n\nCOMPLICATIONS: If untreated:\nPelvic inflammatory disease (PID) in females → can cause infertility.\nIncreased risk of HIV infection.\nCan be passed from mother to baby during birth → eye infection in newborn.\n\nPREVENTION: Using condoms (barrier contraception), reducing number of sexual partners, regular STI testing.\n\nTREATMENT: Antibiotics — however, ANTIBIOTIC-RESISTANT strains have emerged, making gonorrhoea increasingly difficult to treat. This is a serious and growing public health problem.\n\nANTIBIOTIC RESISTANCE in gonorrhoea happens through natural selection:\nRandom mutations in bacteria can produce resistance.\nAntibiotics kill non-resistant bacteria but resistant ones survive.\nResistant bacteria reproduce, passing on resistance genes.\nOver time, the population becomes resistant."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Gonorrhoea IS treatable with antibiotics — but antibiotic-resistant strains are emerging. Do not say 'gonorrhoea cannot be treated'. Say instead: 'it can be treated, but resistance is a growing problem'. Also: Salmonella causes disease primarily through TOXINS — not just by the bacteria damaging cells directly.",
        "key_note": "Salmonella: bacteria, contaminated food, symptoms = fever/vomiting/diarrhoea, prevented by cooking thoroughly. Gonorrhoea: bacteria, STI, discharge and pain, treated by antibiotics (resistance growing).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Bacterial Disease to its Features",
            "instruction": "Match each feature to Salmonella or Gonorrhoea.",
            "pairs": [
                ("Salmonella", "Spread through undercooked food — prevented by thorough cooking and hygiene"),
                ("Gonorrhoea", "Sexually transmitted — thick discharge and pain when urinating"),
                ("Salmonella", "Bacteria produce toxins in the gut — causing vomiting and diarrhoea"),
                ("Gonorrhoea", "Antibiotic-resistant strains have emerged — major public health concern"),
                ("Salmonella", "Often resolves without antibiotics — rest and fluids usually sufficient"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "How is Salmonella food poisoning prevented?",
                "opts": [
                    ("Thorough cooking to kill bacteria, good food hygiene, refrigeration and hand washing", True),
                    ("Taking antibiotics before eating suspected food", False),
                    ("Avoiding all animal products entirely", False),
                    ("Vaccinating all humans against Salmonella", False)
                ],
                "wrong_explanations": {
                    1: "Taking antibiotics preventatively is dangerous — it promotes antibiotic resistance without benefit.",
                    2: "Thorough cooking makes animal products safe — you don't need to avoid them entirely.",
                    3: "Human Salmonella vaccines are not routinely used — poultry vaccination is used in the UK to reduce the source."
                }
            },
            {
                "q": "Why is gonorrhoea becoming harder to treat?",
                "opts": [
                    ("Antibiotic-resistant strains have evolved — bacteria with resistance mutations survive antibiotic treatment and pass on resistance genes", True),
                    ("Gonorrhoea has mutated into a virus, which antibiotics cannot target", False),
                    ("New strains produce proteins that destroy antibiotic molecules before they can work", False),
                    ("People have developed immunity to the antibiotics used to treat it", False)
                ],
                "wrong_explanations": {
                    1: "Gonorrhoea remains a bacterium — bacteria cannot evolve into viruses. The issue is antibiotic resistance in bacterial populations.",
                    2: "Some resistant bacteria do produce enzymes (like beta-lactamases) that break down antibiotics — this is one mechanism of resistance, but the question is about the broader process of natural selection producing resistant strains.",
                    3: "People develop immunity to pathogens, not to medicines. Antibiotic resistance is a property of the BACTERIA, not of human patients."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 4. FUNGAL AND PROTIST DISEASES
    # ══════════════════════════════════════════════
    {
        "id": "fungal-protist-diseases",
        "title": "Fungal and Protist Diseases",
        "spec": "4.3.1.4",
        "summary": "Describe rose black spot (fungal) and malaria (protist) as examples of these disease types.",
        "theory": [
            {
                "heading": "Fungal Diseases — Rose Black Spot",
                "content": "CAUSE: Diplocarpon rosae — a fungal pathogen that infects rose plants.\n\nTRANSMISSION: Fungal spores spread through WATER (rain splashing from leaf to leaf) and by WIND. Spores land on leaves and germinate when conditions are warm and wet.\n\nSYMPTOMS:\nPurple or black spots appearing on rose leaves.\nLeaves turn yellow around the spots.\nAffected leaves drop off the plant prematurely — DEFOLIATION.\n\nWHY IT MATTERS: The loss of leaves is the key problem. Fewer leaves → less surface area for photosynthesis → the plant grows poorly, produces fewer flowers and is weakened overall. Severely infected plants may die.\n\nPREVENTION AND TREATMENT:\nRemove and destroy infected leaves immediately — do NOT compost them (spores can survive).\nApply FUNGICIDE sprays to remaining leaves — kills fungal growth.\nChoose disease-resistant rose varieties.\nAvoid overhead watering — wet leaves encourage fungal growth."
            },
            {
                "heading": "Protist Diseases — Malaria",
                "content": "CAUSE: Plasmodium — a protist (single-celled eukaryote). Several species cause malaria; Plasmodium falciparum is the most deadly.\n\nVECTOR: The female Anopheles mosquito — she bites infected humans, picks up Plasmodium, and injects it into the next person she bites. The mosquito is the VECTOR, not the pathogen.\n\nLIFE CYCLE IN BRIEF:\nPlasmodium is injected into the human bloodstream during a mosquito bite.\nIt travels to the liver and multiplies.\nIt then infects and DESTROYS red blood cells in cycles.\nThe destruction of red blood cells causes the characteristic RECURRING FEVER.\n\nSYMPTOMS: High fever (cyclical — comes and goes in waves), headache, vomiting, muscle pain and fatigue. Severe malaria can cause: anaemia (from red blood cell destruction), kidney failure, cerebral malaria (affecting the brain), coma and death.\n\nPREVENTION (breaking the transmission cycle):\nMosquito nets (especially insecticide-treated bed nets — ITNs).\nInsecticide sprays to kill mosquitoes.\nDraining standing water where mosquitoes breed.\nAnti-malarial drugs taken before and during travel to high-risk areas.\n\nTREATMENT: Anti-malarial drugs (e.g. artemisinin-based combination therapies). Resistance to some anti-malarials is also emerging."
            },
            {
                "heading": "Comparing Fungal and Protist Diseases",
                "content": "It helps to compare these two types side by side:\n\nROSE BLACK SPOT:\nPathogen type: FUNGUS.\nHost: Rose plants.\nSpread: Water and wind carrying spores.\nDamage: Leaf spots and defoliation → reduced photosynthesis.\nTreatment: Fungicide, removing infected leaves.\n\nMALARIA:\nPathogen type: PROTIST (Plasmodium).\nHost: Humans (and other primates).\nSpread: Via the Anopheles mosquito VECTOR.\nDamage: Destroys red blood cells → recurring fever, anaemia, can be fatal.\nTreatment: Anti-malarial drugs."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "The MOSQUITO is the VECTOR for malaria — not the pathogen. Plasmodium (the protist) is the pathogen that causes disease. The mosquito carries and transmits it. This distinction is a very common exam question. Also: rose black spot is caused by a FUNGUS — not bacteria, not a virus.",
        "key_note": "Rose black spot: fungus, water/wind spread, leaf spots → defoliation → less photosynthesis. Malaria: Plasmodium protist, Anopheles mosquito = vector, destroys red blood cells, recurring fever.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Rose Black Spot or Malaria?",
            "instruction": "Sort each feature to the correct disease.",
            "pairs": [
                ("Rose black spot", "Caused by a fungus — spreads via water and wind"),
                ("Malaria", "Caused by a protist — transmitted by Anopheles mosquito bites"),
                ("Rose black spot", "Black spots on leaves — causes defoliation and reduced photosynthesis"),
                ("Malaria", "Destroys red blood cells — causes cyclical fever and can be fatal"),
                ("Rose black spot", "Treated with fungicide — infected leaves removed and destroyed"),
                ("Malaria", "Prevented with mosquito nets and insecticides — anti-malarial drugs for treatment"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does rose black spot cause poor plant growth?",
                "opts": [
                    ("Infected leaves develop spots and fall off — less leaf area means less photosynthesis and less glucose for growth", True),
                    ("The fungus blocks the xylem, preventing water reaching the leaves", False),
                    ("The fungus produces toxins that directly kill root cells", False),
                    ("Spores block stomata, preventing CO₂ from entering the leaf", False)
                ],
                "wrong_explanations": {
                    1: "Rose black spot infects LEAF CELLS — it doesn't block xylem. The impact is through reduced photosynthetic capacity.",
                    2: "Rose black spot is a leaf disease — it doesn't specifically target roots.",
                    3: "Blocking stomata is not the primary mechanism — the main effect is leaf loss through defoliation reducing total photosynthesis."
                }
            },
            {
                "q": "What is the role of the Anopheles mosquito in malaria?",
                "opts": [
                    ("It is the vector — it carries Plasmodium from one human to another when it bites", True),
                    ("It is the pathogen — the mosquito itself causes the disease", False),
                    ("It injects its own saliva which contains the fever-causing toxin", False),
                    ("It is only involved in spreading malaria in tropical countries — not elsewhere", False)
                ],
                "wrong_explanations": {
                    1: "The PATHOGEN is Plasmodium (the protist). The mosquito is the VECTOR — it carries and transmits the pathogen without being the cause of disease itself.",
                    2: "Mosquito saliva can cause local irritation — but the disease malaria is caused specifically by Plasmodium being injected, not by the saliva itself.",
                    3: "Malaria is predominantly tropical because Anopheles mosquitoes thrive in warm, wet environments — but the mosquito's role as vector is the same wherever it lives."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 5. VACCINATION
    # ══════════════════════════════════════════════
    {
        "id": "vaccination",
        "title": "Vaccination",
        "spec": "4.3.2",
        "summary": "Explain how vaccines work, why they protect populations and what herd immunity means.",
        "theory": [
            {
                "heading": "How Vaccines Work",
                "content": "A vaccine introduces a small, harmless amount of a pathogen (or part of one) into the body to stimulate an immune response WITHOUT causing the actual disease.\n\nVaccines can contain:\nDead or inactivated pathogens — can't cause disease but still have antigens.\nWeakened (attenuated) live pathogens — cause only a very mild or no illness.\nAntigens only (fragments of the pathogen surface) — the pathogen itself is never introduced.\nmRNA coding for a pathogen antigen (e.g. COVID-19 mRNA vaccines).\n\nWhat happens after vaccination:\n1. Phagocytes engulf the vaccine material.\n2. Lymphocytes recognise the pathogen antigens and produce specific antibodies.\n3. MEMORY CELLS are produced — these remain in the blood for many years or for life.\n4. If the real pathogen later invades, memory cells respond RAPIDLY and MASSIVELY — producing antibodies so fast that the pathogen is destroyed before it causes symptoms.\n\nThe KEY POINT: vaccines work by training the immune system in advance, so it is ready to respond instantly if the real pathogen ever arrives."
            },
            {
                "heading": "Herd Immunity",
                "content": "HERD IMMUNITY is achieved when enough of a population is immune (through vaccination or past infection) that the pathogen cannot spread efficiently — even unvaccinated individuals are protected.\n\nHow it works:\nIf most people are immune, a newly infected person encounters mostly immune individuals.\nThe pathogen cannot find enough new hosts to continue spreading.\nThe chain of transmission is broken.\n\nWhy it matters:\nSome people CANNOT be vaccinated — newborn babies (too young), immunocompromised patients (e.g. on chemotherapy), people with certain allergies.\nHerd immunity protects these vulnerable individuals indirectly.\n\nThe percentage of the population needed for herd immunity varies by disease:\nMeasles requires ~95% vaccination coverage (because it spreads very easily).\nPolio requires ~80–85%.\n\nWhen vaccination rates drop below the threshold, outbreaks occur — as happened with measles in some countries after false concerns about the MMR vaccine."
            },
            {
                "heading": "Examples of Successful Vaccination",
                "content": "MMR vaccine: protects against measles, mumps and rubella. Given at 12–15 months and again at 3–5 years. Highly effective.\n\nSMALLPOX: The only human disease to be completely ERADICATED (wiped out globally) — achieved entirely through worldwide vaccination. The last natural case was in 1977.\n\nPOLIO: Nearly eradicated through global vaccination campaigns — still circulating in a small number of countries.\n\nFLU VACCINE: Updated each year because influenza virus mutates rapidly — last year's vaccine may not protect against this year's strains.\n\nCOVID-19: mRNA vaccines developed and deployed at record speed (2020–21), demonstrating new vaccine technology.\n\nHPV VACCINE: Protects against Human Papillomavirus — which causes most cervical cancers. Given to teenagers before sexual activity begins."
            },
            {
                "heading": "Are Vaccines Safe?",
                "content": "Vaccines are among the most extensively tested and monitored medicines in existence.\n\nAll vaccines undergo rigorous testing before approval:\nLaboratory and animal testing.\nPhase 1, 2 and 3 clinical trials (see Drug Development subtopic).\nRegulatory review by agencies like the MHRA (UK) or FDA (USA).\n\nCommon side effects are mild and temporary:\nSoreness at injection site.\nLow-grade fever for 1–2 days.\nFatigue.\n\nSERIOUS side effects are extremely rare — and the risk of serious illness from the actual disease is far greater than any risk from the vaccine.\n\nMisinformation about vaccine safety has caused vaccination rates to drop in some communities, leading to preventable outbreaks of serious diseases."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Vaccines do NOT give you the disease. They contain harmless forms of the pathogen (dead, weakened or just antigens) — they cannot cause the actual disease. The immune response to the vaccine (mild fever, soreness) is your body's NORMAL reaction to stimulation — not the disease itself.",
        "key_note": "Vaccine → harmless antigen → immune response → memory cells → rapid response on real infection. Herd immunity: enough vaccinated → pathogen can't spread → vulnerable people protected. Smallpox = only disease fully eradicated by vaccination.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Vaccination Concept",
            "instruction": "Match each concept to its correct description.",
            "pairs": [
                ("Memory cells", "Produced during vaccination — allow rapid antibody production if real pathogen is later encountered"),
                ("Herd immunity", "When enough of the population is immune that the pathogen cannot spread — protects unvaccinated individuals"),
                ("MMR vaccine", "Protects against measles, mumps and rubella — given in two doses in childhood"),
                ("Smallpox", "The only human disease ever fully eradicated — achieved through global vaccination"),
                ("Flu vaccine", "Updated annually because the influenza virus mutates its surface antigens each year"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "How does a vaccine protect against future infection?",
                "opts": [
                    ("It stimulates an immune response and produces memory cells — so the body responds rapidly if the real pathogen invades", True),
                    ("It kills any pathogen that enters the body for the rest of your life", False),
                    ("It strengthens all aspects of the immune system permanently", False),
                    ("It prevents the pathogen from ever entering the body", False)
                ],
                "wrong_explanations": {
                    1: "Vaccines don't provide a permanent killing effect — they prepare MEMORY CELLS that respond quickly if the pathogen arrives.",
                    2: "Vaccines provide SPECIFIC immunity to one pathogen — they don't generally boost the whole immune system.",
                    3: "Pathogens can still enter the body after vaccination — the vaccine means the immune system destroys them so quickly they don't cause disease."
                }
            },
            {
                "q": "What is herd immunity?",
                "opts": [
                    ("When enough of a population is immune that the pathogen cannot spread effectively — protecting even unvaccinated individuals", True),
                    ("When every single person in a population has been vaccinated", False),
                    ("When an entire herd of animals is vaccinated against a disease", False),
                    ("When a person becomes naturally immune after recovering from a disease", False)
                ],
                "wrong_explanations": {
                    1: "Herd immunity doesn't require 100% vaccination — it just needs enough people to be immune to break the chain of transmission.",
                    2: "'Herd' refers to any population — not just animal herds. Herd immunity applies to human populations too.",
                    3: "Natural immunity after infection DOES contribute to herd immunity — but vaccination is the safer way to achieve it without suffering the disease."
                }
            },
            {
                "q": "Why is the flu vaccine updated every year?",
                "opts": [
                    ("The influenza virus mutates rapidly — its surface antigens change, so last year's vaccine may no longer match this year's strains", True),
                    ("Memory cells from flu vaccines only last one year before disappearing", False),
                    ("Flu vaccines contain live viruses that must be freshly prepared each season", False),
                    ("The government changes the vaccine composition each year as a precaution", False)
                ],
                "wrong_explanations": {
                    1: "Memory cells from vaccines can last many years or a lifetime — the issue is not memory cell lifespan but viral mutation.",
                    2: "Many flu vaccines use inactivated (killed) viruses — not live ones. The reason for annual updates is viral mutation.",
                    3: "The composition is updated based on scientific surveillance of which influenza strains are circulating — it's not an arbitrary precaution."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 6. ANTIBIOTICS AND PAINKILLERS
    # ══════════════════════════════════════════════
    {
        "id": "antibiotics-painkillers",
        "title": "Antibiotics and Painkillers",
        "spec": "4.3.3",
        "summary": "Explain how antibiotics work, why antibiotic resistance is a threat, and the role of painkillers.",
        "theory": [
            {
                "heading": "Antibiotics",
                "content": "Antibiotics are drugs that kill bacteria or prevent them from reproducing — they are used to treat BACTERIAL infections.\n\nHow they work: Antibiotics target specific structures in bacteria that are NOT present in human cells — for example:\nPENICILLIN (and similar antibiotics) disrupts bacterial CELL WALL synthesis. Human cells have no cell wall, so penicillin doesn't harm them.\nOther antibiotics target bacterial ribosomes or DNA replication.\n\nDifferent antibiotics work on different bacteria:\nBROAD SPECTRUM antibiotics work against many different bacterial species.\nNARROW SPECTRUM antibiotics target specific types of bacteria.\n\nAntibiotics CANNOT treat viral infections because:\nViruses have no cell walls, no bacterial ribosomes and no bacterial DNA replication machinery — there is nothing for antibiotics to target.\nViruses live INSIDE host cells — drugs that killed them would also damage the host cell.\n\nAntibiotics were discovered by Alexander Fleming in 1928 — he noticed Penicillium mould was killing bacteria on a petri dish."
            },
            {
                "heading": "Antibiotic Resistance — A Global Crisis",
                "content": "Antibiotic resistance is one of the greatest threats to global health.\n\nHow it develops through NATURAL SELECTION:\n1. Within a population of bacteria, random MUTATIONS occur naturally during reproduction.\n2. Occasionally, a mutation gives a bacterium resistance to an antibiotic.\n3. When antibiotics are used, non-resistant bacteria are killed.\n4. Resistant bacteria SURVIVE and REPRODUCE — passing on the resistance gene to offspring.\n5. Over time, the entire population becomes resistant — the antibiotic no longer works.\n\nWhy resistance is spreading:\nOVER-PRESCRIBING — doctors prescribing antibiotics for viral infections or 'just in case'.\nNOT COMPLETING COURSES — stopping early leaves some bacteria alive; the survivors are more likely to be partially resistant.\nAGRICULTURE — antibiotics used to promote growth in livestock, creating resistant bacteria in food chains.\n\nConsequences: Infections once easily treated (e.g. tuberculosis, some pneumonias) are becoming dangerous again. MRSA (methicillin-resistant Staphylococcus aureus) is an example of a serious antibiotic-resistant bacterium.\n\nHow to slow resistance:\nOnly use antibiotics when genuinely necessary.\nAlways complete the full course.\nNever share or save antibiotics for later.\nReduce agricultural antibiotic use."
            },
            {
                "heading": "Painkillers",
                "content": "Painkillers (analgesics) relieve pain and reduce fever — but they do NOT kill pathogens or treat the cause of infection.\n\nCommon painkillers: paracetamol, ibuprofen, aspirin.\n\nThey treat SYMPTOMS — making the patient feel more comfortable — but the immune system still needs to fight the infection.\n\nA patient with a bacterial infection may take BOTH:\nAntibiotics — to kill the bacteria (treating the cause).\nPainkillers — to manage fever, pain and discomfort (treating the symptoms).\n\nANTIVIRAL DRUGS are medicines that do treat viral infections — but they are much harder to develop than antibiotics because viruses use the host cell's own machinery.\nExamples: oseltamivir (Tamiflu) for influenza, antiretroviral drugs (ARVs) for HIV.\nAntivirals don't kill viruses outright — they usually prevent replication."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Painkillers do NOT treat infections — they only relieve symptoms. A patient taking only paracetamol for a bacterial infection is NOT treating the infection. Also: always complete antibiotic courses — stopping early is a major driver of resistance because the bacteria that survive are likely to be the more resistant ones.",
        "key_note": "Antibiotics: kill bacteria, NO effect on viruses, target bacterial cell walls/ribosomes. Antibiotic resistance: natural selection of resistant mutants — avoid misuse. Painkillers: treat symptoms only, don't kill pathogens.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Antibiotic, Painkiller or Antiviral?",
            "instruction": "Sort each statement to the correct type of drug.",
            "pairs": [
                ("Antibiotic", "Kills bacteria — works by targeting bacterial cell walls or ribosomes"),
                ("Painkiller", "Relieves fever and pain — does not kill any pathogens"),
                ("Antiviral", "Prevents viral replication — used for HIV and influenza"),
                ("Antibiotic", "Has no effect on viral infections — useless against flu or measles"),
                ("Painkiller", "Examples: paracetamol, ibuprofen, aspirin"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why can't antibiotics treat viral infections?",
                "opts": [
                    ("Viruses don't have cell walls or bacterial ribosomes — the structures antibiotics target don't exist in viruses", True),
                    ("Viruses are too small for antibiotics to reach", False),
                    ("Antibiotics are absorbed too slowly to reach viruses in the bloodstream", False),
                    ("Viruses produce enzymes that destroy antibiotics", False)
                ],
                "wrong_explanations": {
                    1: "Viruses are smaller than bacteria — but size is not why antibiotics don't work. Antibiotics target specific bacterial structures that viruses simply don't have.",
                    2: "Antibiotics are absorbed into the bloodstream — but they have no biological target in virus particles, so reaching them makes no difference.",
                    3: "Some resistant bacteria do produce enzymes that destroy antibiotics — but this is a bacterial resistance mechanism, not a general viral property."
                }
            },
            {
                "q": "Why is it important to always complete a full course of antibiotics?",
                "opts": [
                    ("Stopping early leaves the most resistant bacteria alive — they survive and reproduce, increasing resistance", True),
                    ("Stopping early means the antibiotics already taken are wasted and have no effect", False),
                    ("Partial courses make the bacteria grow faster as a response", False),
                    ("It doesn't matter — stopping early is fine if symptoms improve", False)
                ],
                "wrong_explanations": {
                    1: "The antibiotics already taken do have effect — they kill susceptible bacteria. The problem is that the resistant survivors are left to reproduce.",
                    2: "Bacteria don't 'grow faster' in response to antibiotics stopping — the issue is selective survival of resistant variants.",
                    3: "This is a dangerous misconception — symptoms improving means the immune system and antibiotics are working, but bacteria may still be present. Stopping early increases resistance risk."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 7. DRUG DISCOVERY AND DEVELOPMENT
    # ══════════════════════════════════════════════
    {
        "id": "drug-discovery-development",
        "title": "Drug Discovery and Development",
        "spec": "4.3.4",
        "summary": "Describe how new drugs are discovered, tested and approved before being used on patients.",
        "theory": [
            {
                "heading": "Where New Drugs Come From",
                "content": "Throughout history, many important drugs were discovered from NATURAL SOURCES:\n\nPENICILLIN — discovered by Alexander Fleming (1928) from the Penicillium mould. He noticed bacteria on a petri dish were being killed near a mould contamination.\n\nASPIRIN — derived from salicylic acid found in willow bark. Used as a pain reliever for centuries before the active compound was isolated.\n\nMORPHINE — derived from opium poppies — a powerful painkiller still used today.\n\nQUININE — extracted from cinchona tree bark — historically the main treatment for malaria.\n\nModern drug discovery also uses:\nSynthetic chemistry — designing molecules in the laboratory.\nComputer modelling — predicting how molecules interact with biological targets.\nBiotechnology — using genetically modified organisms to produce medicines (e.g. human insulin produced by GM bacteria)."
            },
            {
                "heading": "Pre-Clinical Testing",
                "content": "Before any new drug is tested on humans, it must undergo PRE-CLINICAL TESTING:\n\nCELL CULTURES — the drug is tested on cells grown in the laboratory. Checks basic toxicity and whether the drug has any biological effect.\n\nCOMPUTER MODELS — simulate the drug's behaviour and interactions in the body before any living organism is used.\n\nANIMAL TESTING — the drug is tested on animals (usually mice or rats) to check:\nWhether it is safe in a living organism.\nHow it is absorbed, distributed and broken down.\nWhat side effects occur.\nWhether it has any effect on the target disease.\n\nMany potential drugs fail at this stage and are abandoned. Only those that show promise and acceptable safety proceed to human trials."
            },
            {
                "heading": "Clinical Trials — Testing on Humans",
                "content": "Drugs that pass pre-clinical testing move to CLINICAL TRIALS — testing in human volunteers. This happens in three phases:\n\nPHASE 1 — Safety:\nSmall group of healthy volunteers.\nVery low doses given initially, then gradually increased.\nAim: check the drug is safe in humans and identify any side effects.\n\nPHASE 2 — Efficacy:\nLarger group of patients who have the condition the drug treats.\nAim: check the drug actually works and find the optimal dose.\n\nPHASE 3 — Large-scale comparison:\nHundreds or thousands of patients.\nThe drug is compared to either an EXISTING TREATMENT or a PLACEBO.\nDOUBLE-BLIND TRIALS are used — neither the patients nor the doctors administering the trial know who is receiving the real drug or the placebo. This eliminates bias.\nA PLACEBO is an inactive dummy treatment (e.g. a sugar pill) that looks identical to the real drug. Used to control for the PLACEBO EFFECT — where patients improve simply because they believe they are receiving treatment.\n\nIf Phase 3 is successful, the drug is submitted for regulatory approval. In the UK this is the MHRA (Medicines and Healthcare products Regulatory Agency)."
            },
            {
                "heading": "Thalidomide — A Cautionary Tale",
                "content": "Thalidomide was developed in the 1950s as a sedative and treatment for morning sickness in pregnancy.\n\nIt had not been adequately tested for effects on developing embryos.\n\nWhen taken by pregnant women, it caused severe birth defects — particularly abnormal limb development (phocomelia — very short or absent limbs).\n\nAn estimated 10,000 babies were affected worldwide before the drug was withdrawn in 1961.\n\nThis case led directly to much stricter drug testing requirements worldwide — particularly the requirement to test drugs on pregnant animals before use in humans.\n\nThalidomide's lesson: drugs must be tested thoroughly for ALL potential uses and ALL population groups, including pregnant women.\n\nInterestingly, thalidomide is now used again under very strict controls to treat some cancers (multiple myeloma) and leprosy — illustrating that even a harmful drug can have safe medical uses in the right context."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A DOUBLE-BLIND trial means NEITHER the patient NOR the doctor knows who is getting the real drug. A SINGLE-BLIND trial means only the patient doesn't know. Double-blind removes bias from both sides. A PLACEBO is a dummy treatment — not a low dose of the real drug.",
        "key_note": "Drug testing: pre-clinical (cells → computer → animals) → Phase 1 (safety, healthy volunteers) → Phase 2 (efficacy, patients) → Phase 3 (large comparison, double-blind, placebo) → regulatory approval.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Stage of Drug Development",
            "instruction": "Match each description to the correct stage of drug testing.",
            "pairs": [
                ("Pre-clinical — cells and animals", "Drug tested in lab on cells and then animals — checks basic safety before human trials"),
                ("Phase 1 clinical trial", "Small group of healthy volunteers — checks the drug is safe in humans"),
                ("Phase 2 clinical trial", "Patients with the condition — checks the drug actually works at the right dose"),
                ("Phase 3 clinical trial", "Large-scale, double-blind, placebo-controlled — compares to existing treatment"),
                ("Double-blind trial", "Neither patient nor doctor knows who is receiving the real drug — eliminates bias"),
                ("Placebo", "Inactive dummy treatment — controls for the psychological placebo effect"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is a double-blind clinical trial?",
                "opts": [
                    ("Neither the patients nor the doctors know who is receiving the real drug or the placebo — eliminates bias from both sides", True),
                    ("Only the patients don't know which treatment they are receiving", False),
                    ("The trial uses two different drugs tested simultaneously against each other", False),
                    ("The trial is conducted in the dark to prevent visual identification of the drug", False)
                ],
                "wrong_explanations": {
                    1: "If only the PATIENT doesn't know = single-blind. Double-blind means BOTH patient AND doctor are unaware — this prevents the doctor's expectations influencing how they assess patient progress.",
                    2: "A trial testing two real drugs against each other is a comparative trial — double-blind refers to who knows about treatment allocation, not how many drugs are tested.",
                    3: "'Blind' in a clinical context means 'unaware of treatment allocation' — it has nothing to do with actual darkness."
                }
            },
            {
                "q": "Why is a placebo used in clinical trials?",
                "opts": [
                    ("To control for the placebo effect — some patients improve just because they believe they are being treated", True),
                    ("To give patients a low starting dose before they receive the real drug", False),
                    ("To ensure every patient receives some form of medical benefit during the trial", False),
                    ("To test the side effects of inactive substances", False)
                ],
                "wrong_explanations": {
                    1: "A placebo is not a low dose — it is INACTIVE and contains no active ingredient.",
                    2: "Patients in the placebo group receive no active treatment — this is ethically managed carefully and only used when ethically appropriate.",
                    3: "Placebos by definition have no pharmacological activity — any side effects are psychological or coincidental."
                }
            },
            {
                "q": "What was the key lesson from the thalidomide tragedy?",
                "opts": [
                    ("Drugs must be rigorously tested for all potential effects including effects on embryos — testing requirements were significantly strengthened", True),
                    ("Natural drugs are always safer than synthetic ones", False),
                    ("Sedatives should never be prescribed during pregnancy", False),
                    ("Clinical trials are unnecessary if a drug has been shown to be safe in adults", False)
                ],
                "wrong_explanations": {
                    1: "Thalidomide was a synthetic drug — but many synthetic drugs are completely safe. The lesson was specifically about testing for effects on ALL groups, especially embryos.",
                    2: "The lesson was specifically about testing for ALL effects in ALL populations — not a blanket ban on sedatives in pregnancy.",
                    3: "The thalidomide case showed exactly WHY clinical trials must be thorough — an adult-safe drug was devastating to embryos."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 8. PLANT DISEASE DETECTION AND DEFENCE
    # ══════════════════════════════════════════════
    {
        "id": "plant-disease-detection-defence",
        "title": "Plant Disease Detection and Defence",
        "spec": "4.3.5",
        "summary": "Describe how plant diseases are identified and how plants defend themselves against pathogens and pests.",
        "theory": [
            {
                "heading": "Identifying Plant Disease",
                "content": "Plants can be infected by bacteria, viruses, fungi and other parasites — just like animals. Recognising disease symptoms is important for farmers, gardeners and conservationists.\n\nCommon symptoms of plant disease:\nSTUNTED GROWTH — plant is smaller or grows more slowly than expected for its age and growing conditions.\nSPOTS ON LEAVES — discoloured patches, often black, brown or orange.\nAREAS OF DECAY (ROT) — brown, soft, collapsing tissue in stems, roots or fruit.\nABNORMAL GROWTHS — unusual swellings, galls or distorted structures.\nMALFORMED LEAVES OR STEMS — twisted, curled or distorted plant parts.\nDISCOLOURATION — yellowing (chlorosis), bleaching, mosaic patterns.\n\nHow to identify the specific cause:\nLook up symptoms in a plant disease identification guide or database.\nSend a sample to a laboratory for microscopic examination.\nTest using specific diagnostic kits (e.g. lateral flow tests for specific pathogens).\nObserve when and where the disease appears — conditions often give clues (e.g. fungal diseases favour wet, warm weather)."
            },
            {
                "heading": "Physical Defences in Plants",
                "content": "Plants have evolved a range of physical defences that act as barriers to prevent pathogens and pests from entering:\n\nCELL WALLS made of cellulose — provide a rigid physical barrier around each cell. Much harder for pathogens to penetrate than a soft cell membrane alone.\n\nWAXY CUTICLE on leaves and stems — a waterproof, waxy layer secreted by epidermal cells. Prevents pathogens from landing and colonising the leaf surface. Also reduces water loss.\n\nBARK on woody stems — tough outer layers protect living tissue (phloem and cambium) underneath from physical damage and pathogen entry.\n\nTHORNS and SPINES — physical deterrents to herbivores, reducing the chances of wounds through which pathogens can enter.\n\nCLOSING OF STOMATA — when plants detect pathogen attack, they can close stomata to prevent pathogen entry through these openings."
            },
            {
                "heading": "Chemical Defences in Plants",
                "content": "Plants also produce a wide range of chemicals that deter herbivores and fight pathogens:\n\nANTIBACTERIAL COMPOUNDS — some plants produce substances with antimicrobial properties:\nAllicin in garlic — shown to have antibacterial and antifungal activity.\nTannins in oak bark and tea leaves — bitter astringent compounds that deter herbivores and have some antimicrobial properties.\n\nPOISONS (ALKALOIDS) — plants produce toxic secondary metabolites to deter animals from eating them:\nNicotine in tobacco plants — highly toxic to insects (used as an insecticide).\nCaffeine in coffee and tea plants — deters insects from feeding.\nQuinine in cinchona trees — bitter taste deters herbivores; also has antimicrobial properties.\nDigitalis (foxglove) — toxic to vertebrates including humans if eaten in large quantities.\n\nINSECT-REPELLING COMPOUNDS — volatile chemicals released from leaves deter insects from landing and laying eggs.\n\nSTICKY RESINS and LATEX — trap insects on the surface or clog their mouthparts if they try to feed."
            },
            {
                "heading": "Responding to Attack",
                "content": "Plants can also mount active responses when they detect pathogen invasion:\n\nHYPERSENSITIVE RESPONSE — when a pathogen is detected, the plant rapidly KILLS the cells immediately surrounding the infection site, creating a zone of dead cells.\nThis dead zone acts as a firebreak — the pathogen cannot spread through dead cells, containing the infection.\n\nSYSTEMIC ACQUIRED RESISTANCE (SAR) — after a localised infection, the whole plant can become more resistant to future attacks.\nThe plant produces signalling molecules (like salicylic acid) that travel to uninfected parts of the plant, 'warning' them to prepare chemical defences.\n\nMany of the chemicals plants produce for defence have also been used by humans:\nAspirin derived from salicylic acid.\nQuinine — antimalarial drug.\nMorphine and codeine — painkillers from poppies.\nMany modern medicines originated as plant defence chemicals."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Plants do NOT have an immune system like animals — no antibodies, no lymphocytes, no phagocytes. Their defences are physical (walls, wax, bark) and chemical (poisons, antimicrobials). They are passive or triggered responses, not a learned adaptive immune system.",
        "key_note": "Plant physical defences: cell walls, waxy cuticle, bark, thorns, closing stomata. Chemical defences: antibacterial compounds (e.g. allicin), poisons/alkaloids (e.g. nicotine, caffeine, quinine). Active responses: hypersensitive response (kills cells around infection), systemic acquired resistance.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Physical or Chemical Plant Defence?",
            "instruction": "Sort each plant defence into physical or chemical.",
            "pairs": [
                ("Physical", "Cell walls — rigid cellulose barrier around each cell"),
                ("Physical", "Waxy cuticle — waterproof surface layer prevents colonisation"),
                ("Chemical", "Nicotine in tobacco — highly toxic to insects, deters feeding"),
                ("Physical", "Thorns — deter herbivores from eating the plant"),
                ("Chemical", "Allicin in garlic — antibacterial and antifungal compound"),
                ("Chemical", "Tannins in oak bark — bitter taste deters herbivores"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "A gardener notices black spots on their rose leaves and the leaves are turning yellow. What is most likely causing this?",
                "opts": [
                    ("Rose black spot — a fungal disease caused by Diplocarpon rosae", True),
                    ("Tobacco mosaic virus — a viral disease causing discolouration", False),
                    ("Salmonella — a bacterial infection from contaminated soil", False),
                    ("The plant is simply overwatered and needs less water", False)
                ],
                "wrong_explanations": {
                    1: "TMV causes a mosaic pattern of light and dark green/yellow patches — not specific black spots with yellowing leaves around them.",
                    2: "Salmonella affects animals, not plants — it does not cause leaf spots in roses.",
                    3: "Overwatering can cause some yellowing, but the distinctive BLACK SPOTS specifically indicate rose black spot fungal infection."
                }
            },
            {
                "q": "Why does the waxy cuticle on leaves help protect the plant from disease?",
                "opts": [
                    ("It provides a waterproof physical barrier that prevents pathogens from landing and colonising the leaf surface", True),
                    ("It contains antibiotics that kill any bacteria landing on the leaf", False),
                    ("It absorbs UV radiation to prevent DNA damage in leaf cells", False),
                    ("It makes leaves slippery so insects cannot grip and feed on them", False)
                ],
                "wrong_explanations": {
                    1: "The cuticle does not contain antibiotics — it is a physical, waterproof barrier. Plant chemical defences (like tannins or allicin) are separate from the cuticle.",
                    2: "UV protection is a secondary function in some plants — but the PRIMARY defensive role of the cuticle is as a physical barrier to pathogens and water loss.",
                    3: "Waxiness can make leaves slippery, but the main function is waterproofing — creating an inhospitable surface for pathogen growth."
                }
            },
            {
                "q": "What is the hypersensitive response in plants?",
                "opts": [
                    ("The plant rapidly kills cells around an infection site, creating a dead zone that contains the pathogen and prevents it spreading", True),
                    ("The plant produces excess antibodies to destroy the invading pathogen", False),
                    ("The plant overreacts to harmless stimuli and closes all its stomata", False),
                    ("The plant produces spores to spread its own genetic material before dying", False)
                ],
                "wrong_explanations": {
                    1: "Plants don't produce antibodies — that is an animal immune system response. Plants' active responses involve chemical signalling and cell death.",
                    2: "Closing stomata IS a response to pathogens — but the 'hypersensitive response' specifically refers to deliberately killing cells around the infection site as a containment strategy.",
                    3: "Sporulation is a reproductive or survival strategy in some fungi and bacteria — not part of the plant hypersensitive response."
                }
            }
        ]
    },
],

"bioenergetics": [


    # ══════════════════════════════════════════════
    # 1. PHOTOSYNTHESIS
    # ══════════════════════════════════════════════
    {
        "id": "photosynthesis",
        "title": "Photosynthesis",
        "spec": "4.4.1.1",
        "summary": "Describe photosynthesis — what it is, where it happens and what the equation means.",
        "theory": [
            {
                "heading": "What is Photosynthesis?",
                "content": "Photosynthesis is the process by which green plants (and some other organisms) use LIGHT ENERGY to make their own food.\n\nIt converts two simple raw materials — carbon dioxide and water — into glucose and oxygen.\n\nPhotosynthesis is an ENDOTHERMIC reaction — it takes in energy (from light) and stores it as chemical energy in glucose molecules.\n\nThis is the opposite of respiration, which releases energy from glucose.\n\nPhotosynthesis is the foundation of almost all food chains on Earth — it is the process that converts the Sun's energy into a form that living organisms can use."
            },
            {
                "heading": "Where Photosynthesis Happens",
                "content": "Photosynthesis takes place in the CHLOROPLASTS — organelles found in the cells of green plants and algae.\n\nChloroplasts contain a green pigment called CHLOROPHYLL.\n\nChlorophyll absorbs LIGHT ENERGY — mainly red and blue wavelengths of light.\n\nGreen light is REFLECTED by chlorophyll — this is why plants appear green to our eyes.\n\nNot all plant cells have chloroplasts:\nLeaf palisade cells — packed with chloroplasts (maximum photosynthesis).\nRoot cells — no chloroplasts (underground, no light available).\nStorage cells — no chloroplasts (no photosynthesis needed)."
            },
            {
                "heading": "The Equation for Photosynthesis",
                "content": "Word equation:\ncarbon dioxide + water → glucose + oxygen\n\nSymbol equation:\n6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂\n\nThis equation requires LIGHT ENERGY — usually written above the arrow.\n\nREACTANTS (what goes in):\nCarbon dioxide (CO₂) — absorbed from the air through stomata in the leaves.\nWater (H₂O) — absorbed from the soil by root hair cells, transported up to leaves through xylem.\n\nPRODUCTS (what comes out):\nGlucose (C₆H₁₂O₆) — a sugar used by the plant for energy and building materials.\nOxygen (O₂) — released as a by-product through stomata."
            },
            {
                "heading": "Photosynthesis vs Respiration",
                "content": "Students often confuse these two processes. Here is the key difference:\n\nPHOTOSYNTHESIS:\nOccurs ONLY in light.\nOccurs ONLY in cells that have chloroplasts.\nTakes in CO₂ and water → makes glucose and O₂.\nStores energy in glucose (endothermic).\n\nRESPIRATION:\nOccurs ALL THE TIME — day and night.\nOccurs in ALL living cells (including animals, bacteria).\nBreaks down glucose + O₂ → CO₂ and water.\nReleases energy from glucose (exothermic).\n\nIn BRIGHT LIGHT: rate of photosynthesis > rate of respiration → net release of oxygen.\nIn LOW LIGHT: rate of photosynthesis < rate of respiration → net release of carbon dioxide.\nAt the COMPENSATION POINT: rate of photosynthesis = rate of respiration → no net gas exchange."
            }
        ],
        "variables": [],
        "equations": ["6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  (light energy)"],
        "common_mistake": "Photosynthesis only happens in LIGHT and only in cells with CHLOROPLASTS. Respiration happens ALL THE TIME in ALL living cells. Never say 'plants don't respire' — they do, constantly. In bright light they photosynthesise faster than they respire, which is why we see net O₂ production.",
        "key_note": "Photosynthesis: CO₂ + H₂O → glucose + O₂. Needs light energy. Occurs in chloroplasts. Endothermic — stores energy. Chlorophyll absorbs red and blue light, reflects green.",
        "higher": None,
        "triple_only": None,
        "rp": "RP5 — Investigate the effect of light intensity on the rate of photosynthesis using aquatic plants (e.g. Elodea or Cabomba). Count oxygen bubbles per minute at different distances from a lamp.",
        "matching": {
            "title": "Photosynthesis — Match the Term",
            "instruction": "Match each item to the correct category.",
            "pairs": [
                ("Reactant", "Carbon dioxide — enters through stomata from the air"),
                ("Reactant", "Water — absorbed by roots, travels up through xylem"),
                ("Product", "Glucose — used for energy, building and storage"),
                ("Product", "Oxygen — released as a by-product through stomata"),
                ("Where it happens", "Chloroplasts — contain chlorophyll that absorbs light"),
                ("Energy type", "Endothermic — light energy absorbed and stored in glucose"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the word equation for photosynthesis?",
                "opts": [
                    ("Carbon dioxide + water → glucose + oxygen", True),
                    ("Glucose + oxygen → carbon dioxide + water", False),
                    ("Carbon dioxide + glucose → water + oxygen", False),
                    ("Water + oxygen → carbon dioxide + glucose", False)
                ],
                "wrong_explanations": {
                    1: "That is the equation for AEROBIC RESPIRATION — the exact reverse of photosynthesis.",
                    2: "CO₂ and glucose are never on the same side. CO₂ is a reactant; glucose is a product of photosynthesis.",
                    3: "Oxygen is a PRODUCT — it is produced by photosynthesis and released. It doesn't go in."
                }
            },
            {
                "q": "Why do plants appear green?",
                "opts": [
                    ("Chlorophyll reflects green light — it absorbs red and blue wavelengths instead", True),
                    ("Plants produce green light as a by-product of photosynthesis", False),
                    ("Green light is needed most for photosynthesis so it is absorbed", False),
                    ("All plant cells are filled with green-coloured water", False)
                ],
                "wrong_explanations": {
                    1: "Plants don't produce or emit light — they only reflect it. Green is the colour reflected, not produced.",
                    2: "Green is actually the LEAST useful wavelength for photosynthesis — red and blue are absorbed most efficiently.",
                    3: "Cell sap in vacuoles is usually colourless — the green colour comes from chlorophyll in chloroplasts."
                }
            },
            {
                "q": "In a dark room, does a plant carry out photosynthesis?",
                "opts": [
                    ("No — photosynthesis requires light energy and cannot occur in darkness", True),
                    ("Yes — plants always photosynthesise, day and night", False),
                    ("Yes — plants store light energy during the day and use it at night", False),
                    ("Only partially — stomata close so photosynthesis slows but doesn't stop", False)
                ],
                "wrong_explanations": {
                    1: "Respiration occurs day and night — but PHOTOSYNTHESIS specifically requires light energy. Without light, it stops completely.",
                    2: "Plants do store glucose — but photosynthesis itself cannot run without light. The stored glucose is used in respiration at night.",
                    3: "Stomata closing does reduce gas exchange in the dark, but photosynthesis stops specifically because there is no light energy, not because stomata are closed."
                }
            },
            {
                "q": "Where exactly in a plant cell does photosynthesis take place?",
                "opts": [
                    ("Chloroplasts — which contain the chlorophyll pigment that absorbs light", True),
                    ("Mitochondria — which produce the energy needed for photosynthesis", False),
                    ("The nucleus — which contains the genes controlling photosynthesis", False),
                    ("The vacuole — which stores the raw materials for photosynthesis", False)
                ],
                "wrong_explanations": {
                    1: "Mitochondria are the site of RESPIRATION — they produce ATP energy but do not carry out photosynthesis.",
                    2: "The nucleus contains the DNA instructions but is not the location where photosynthesis reactions actually occur.",
                    3: "The vacuole stores cell sap (sugars and salts) — it is not involved in carrying out photosynthesis."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 2. RATE OF PHOTOSYNTHESIS
    # ══════════════════════════════════════════════
    {
        "id": "rate-of-photosynthesis",
        "title": "Rate of Photosynthesis",
        "spec": "4.4.1.2",
        "summary": "Explain what limits the rate of photosynthesis and how to investigate it.",
        "theory": [
            {
                "heading": "What is a Limiting Factor?",
                "content": "A LIMITING FACTOR is any factor that, when in short supply, restricts the rate of a reaction — even if all other factors are in abundance.\n\nImagine a factory with three workers on a production line. If one worker is absent (or working slowly), the whole line slows down — even if the other two are working perfectly.\n\nFor photosynthesis, the three main limiting factors are:\n1. LIGHT INTENSITY\n2. CARBON DIOXIDE CONCENTRATION\n3. TEMPERATURE\n\nAt any given moment, the rate of photosynthesis is limited by whichever of these three factors is in shortest supply."
            },
            {
                "heading": "Light Intensity",
                "content": "Light provides the ENERGY for photosynthesis.\n\nAs light intensity INCREASES:\nMore energy available → chlorophyll absorbs more light → faster reactions → rate of photosynthesis increases.\n\nBut once light is no longer the limiting factor, increasing it further has NO effect — another factor takes over as the bottleneck.\n\nIn very LOW light:\nRate is slow — not enough energy to drive the reactions.\nThis is why plants grow more slowly in winter (shorter days, lower light levels).\n\nEVIDENCE in experiments:\nAquatic plants (e.g. Elodea) produce oxygen bubbles.\nMoving a lamp CLOSER increases bubble rate.\nMoving it FURTHER decreases bubble rate.\n\nNOTE: Light intensity decreases with distance from a source."
            },
            {
                "heading": "Carbon Dioxide Concentration",
                "content": "Carbon dioxide is a RAW MATERIAL for photosynthesis — needed to build glucose molecules.\n\nAs CO₂ concentration INCREASES:\nMore raw material available → more glucose can be produced → rate increases.\n\nIf CO₂ falls too low:\nRate is limited even if light and temperature are optimal.\n\nThis is why GREENHOUSES often pump extra CO₂ into the air — raising CO₂ concentration above the normal atmospheric level (~0.04%) can significantly increase crop yields.\n\nNormal atmospheric CO₂ is quite low — for many plants, CO₂ is often the limiting factor during a warm, sunny day."
            },
            {
                "heading": "Temperature",
                "content": "Temperature affects the ENZYMES that control the reactions of photosynthesis.\n\nAs temperature INCREASES (below optimum):\nEnzyme molecules and substrate molecules have more kinetic energy.\nMore frequent and more successful collisions.\nRate of photosynthesis increases.\n\nAt OPTIMUM TEMPERATURE (~25–40°C depending on the plant):\nMaximum rate of photosynthesis.\n\nABOVE OPTIMUM TEMPERATURE:\nEnzymes in the chloroplast BEGIN TO DENATURE.\nActive site shape changes permanently.\nEnzyme-substrate complexes can no longer form.\nRate of photosynthesis FALLS SHARPLY — eventually to zero.\n\nThis explains why very hot conditions reduce photosynthesis even in good light with plenty of CO₂ — the enzyme system has broken down."
            },
            {
                "heading": "Investigating Photosynthesis Rate",
                "content": "The rate of photosynthesis can be measured by:\nCounting the number of O₂ bubbles produced per minute by an aquatic plant.\nMeasuring the volume of O₂ collected over a set time.\nUsing a CO₂ sensor to measure how fast CO₂ is being absorbed.\n\nIn RP5 you investigate the effect of LIGHT INTENSITY:\nSet up a beaker of water with an aquatic plant (Elodea or Cabomba).\nPlace a lamp at a measured distance.\nCount bubbles per minute (or collect gas).\nMove the lamp to different distances and repeat.\nPlot a graph of rate (bubbles/min) against light intensity.\n\nKey controls:\nKeep temperature constant (use a water bath or ice).\nKeep CO₂ constant (add sodium bicarbonate solution to the water).\nThis ensures only light intensity is the independent variable."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "When a graph of photosynthesis rate levels off (plateaus), students often say 'the plant has run out of chlorophyll' or 'there is no more light'. The correct answer is that ANOTHER FACTOR has become limiting — usually CO₂ or temperature. The plant hasn't run out of anything — a different factor is now the bottleneck.",
        "key_note": "Three limiting factors: light intensity, CO₂ concentration, temperature. Rate increases with each up to a point, then another factor limits. Above optimum temperature — enzymes denature, rate falls.",
        "higher": None,
        "triple_only": None,
        "rp": "RP5 — Investigate the effect of light intensity on rate of photosynthesis using aquatic plants. Count bubbles per minute. Move lamp to change light intensity. Control CO₂ (add sodium bicarbonate) and temperature.",
        "matching": {
            "title": "Match the Limiting Factor to its Effect",
            "instruction": "Match each condition to what happens to the rate of photosynthesis.",
            "pairs": [
                ("Low light intensity", "Not enough energy — rate is slow even if CO₂ and temperature are optimal"),
                ("Low CO₂ concentration", "Not enough raw material to build glucose — rate is slow"),
                ("Low temperature", "Enzymes have less kinetic energy — fewer successful collisions, slow rate"),
                ("Temperature above optimum", "Enzymes denature permanently — rate falls sharply to zero"),
                ("Rate levels off (plateau)", "Another factor has become limiting — not that the plant ran out of chlorophyll"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "A plant is given very bright light and high CO₂. The rate of photosynthesis stops increasing. What is now the most likely limiting factor?",
                "opts": [
                    ("Temperature — enzyme activity is now the bottleneck", True),
                    ("Light intensity — the plant needs even more light", False),
                    ("Carbon dioxide — the plant needs more CO₂", False),
                    ("The plant has used up all its chlorophyll", False)
                ],
                "wrong_explanations": {
                    1: "Light is already very bright — it is NOT the limiting factor.",
                    2: "CO₂ is already high — it is NOT the limiting factor.",
                    3: "Chlorophyll is not used up — it is a pigment that absorbs light and is not consumed. Another factor is now limiting the rate."
                }
            },
            {
                "q": "In an experiment, moving a lamp further from an aquatic plant reduces the bubble count. What does this show?",
                "opts": [
                    ("Light intensity is the limiting factor at that distance — reducing it reduces the rate of photosynthesis", True),
                    ("The plant needs to be closer to warm water", False),
                    ("CO₂ levels decrease as the lamp moves further away", False),
                    ("The plant becomes stressed when the lamp moves", False)
                ],
                "wrong_explanations": {
                    1: "The lamp produces light, not heat — the water bath controls temperature.",
                    2: "Moving a lamp doesn't change CO₂ levels — CO₂ comes from the water/air around the plant.",
                    3: "Plants don't have a stress response in the same way animals do — the reduced bubble rate is a direct physical consequence of reduced light energy."
                }
            },
            {
                "q": "Why does photosynthesis rate decrease at temperatures above the optimum?",
                "opts": [
                    ("Enzymes in the chloroplast denature — their active sites change shape permanently and can no longer function", True),
                    ("The plant closes its stomata to prevent water loss in the heat", False),
                    ("High temperatures cause chlorophyll to break down permanently", False),
                    ("More CO₂ evaporates from the leaf at higher temperatures", False)
                ],
                "wrong_explanations": {
                    1: "Stomata closing reduces CO₂ entry — but the primary reason for rate decrease above optimum temperature is ENZYME DENATURATION.",
                    2: "Chlorophyll can be affected by extreme heat, but at typical above-optimum temperatures (e.g. 45–50°C) the main limiting effect is enzyme denaturation.",
                    3: "CO₂ is a gas that dissolves in water — it doesn't 'evaporate from the leaf'. The CO₂ supply issue is about stomata and diffusion rates."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 3. USES OF GLUCOSE FROM PHOTOSYNTHESIS
    # ══════════════════════════════════════════════
    {
        "id": "uses-of-glucose",
        "title": "Uses of Glucose from Photosynthesis",
        "spec": "4.4.1.3",
        "summary": "Describe how plants use the glucose produced by photosynthesis.",
        "theory": [
            {
                "heading": "What Does a Plant Do with Glucose?",
                "content": "After photosynthesis produces glucose, the plant uses it in several important ways.\n\nGlucose is the plant's primary fuel and building material — it is used for energy, for constructing cell structures, and for making other essential molecules.\n\nUnderstanding the uses of glucose helps explain how plants grow, store energy and support animal life."
            },
            {
                "heading": "Respiration",
                "content": "The PRIMARY use of glucose is AEROBIC RESPIRATION — breaking down glucose to release energy (ATP).\n\nThis energy powers everything the plant does:\nActive transport — moving mineral ions into root cells against concentration gradients.\nCell division — growing new cells during growth.\nProtein synthesis — making enzymes and structural proteins.\nMovement — opening and closing stomata (guard cells).\n\nRespiration occurs in ALL living plant cells, day and night — using glucose produced by photosynthesis."
            },
            {
                "heading": "Making Cellulose",
                "content": "Glucose molecules are joined together to form CELLULOSE — a structural carbohydrate.\n\nCellulose makes up the CELL WALLS of plant cells — providing rigidity and structural support.\n\nThis is why plants can stand upright and have firm stems and leaves.\n\nCellulose is the most abundant organic molecule on Earth — made entirely from glucose produced by photosynthesis."
            },
            {
                "heading": "Making Starch for Storage",
                "content": "When glucose is produced faster than it can be used, plants convert it into STARCH for storage.\n\nWhy starch and not glucose?\nGlucose is SOLUBLE — it would dissolve in cell sap and change the water potential of cells, causing osmosis problems.\nStarch is INSOLUBLE — it does not dissolve, so it doesn't affect osmosis and can be packed into cells safely.\nStarch can be converted BACK to glucose when energy is needed.\n\nWhere starch is stored:\nLeaves — starch grains in chloroplasts and cells.\nRoots — e.g. carrots, parsnips are swollen roots packed with starch.\nSeeds — energy store for germination.\nTubers — e.g. potato tubers are storage organs filled with starch."
            },
            {
                "heading": "Making Proteins and Fats",
                "content": "PROTEINS:\nGlucose provides the CARBON SKELETON for making amino acids.\nNITRATE IONS (absorbed from the soil through roots) provide the NITROGEN needed to make the amino group (–NH₂) part of amino acids.\nAmino acids are joined to make PROTEINS — enzymes, structural proteins, transport proteins.\n\nFATS AND OILS:\nGlucose is also used to make LIPIDS (fats and oils).\nUsed in cell membranes (phospholipids).\nUsed as energy-rich storage in seeds (oils in sunflower seeds, olive oil etc).\nAlso used to make the waxy cuticle on leaf surfaces."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Starch is stored instead of glucose because starch is INSOLUBLE — it doesn't affect osmosis. Glucose is soluble and would draw water into cells by osmosis if it accumulated. Students often say 'starch is easier to digest' — that's not the reason plants store starch instead of glucose.",
        "key_note": "Glucose uses: respiration (energy), cellulose (cell walls), starch (storage — insoluble), proteins (needs nitrate ions from soil), fats/oils (membranes, seeds). Starch stored not glucose because starch is insoluble.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Use of Glucose",
            "instruction": "Match each molecule to how it is made from glucose.",
            "pairs": [
                ("Respiration", "Glucose broken down to release ATP energy for all cell processes"),
                ("Cellulose", "Glucose polymerised to make plant cell walls — structural support"),
                ("Starch", "Glucose converted to insoluble storage carbohydrate in leaves, roots and seeds"),
                ("Proteins", "Glucose + nitrate ions → amino acids → proteins (enzymes, structure)"),
                ("Fats and oils", "Glucose converted to lipids — used in membranes and as energy-rich seed stores"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why do plants store glucose as starch rather than keeping it as glucose?",
                "opts": [
                    ("Starch is insoluble — it doesn't affect osmosis or water potential inside cells", True),
                    ("Starch contains more energy per molecule than glucose", False),
                    ("Starch is easier to transport around the plant than glucose", False),
                    ("Glucose would be eaten by bacteria if stored directly", False)
                ],
                "wrong_explanations": {
                    1: "Glucose and starch (a polymer of glucose) contain the same energy per gram — starch isn't more energy-dense.",
                    2: "It's actually GLUCOSE that is transported in the phloem (as sucrose) — not starch. Starch is specifically an insoluble store.",
                    3: "Bacteria can break down starch too — the reason is osmosis, not bacterial protection."
                }
            },
            {
                "q": "A plant is grown in soil with no nitrate ions. Which molecule will it struggle to make?",
                "opts": [
                    ("Proteins — amino acids need nitrogen (from nitrates) to form the amino group", True),
                    ("Glucose — nitrates are needed for photosynthesis", False),
                    ("Starch — nitrate ions are needed to convert glucose to starch", False),
                    ("Cellulose — cell walls require nitrogen to polymerise glucose", False)
                ],
                "wrong_explanations": {
                    1: "Glucose is produced by photosynthesis using CO₂ and water — nitrates are not needed.",
                    2: "Starch is made from glucose polymerisation — no nitrogen is needed for this process.",
                    3: "Cellulose is made from glucose joined by glycosidic bonds — no nitrogen involved."
                }
            },
            {
                "q": "What is the main use of glucose in plants?",
                "opts": [
                    ("Aerobic respiration — releasing energy (ATP) to power all cell processes", True),
                    ("Making starch — all glucose is stored for later use", False),
                    ("Building cell walls from cellulose — the plant's primary structural need", False),
                    ("Making proteins — converting glucose to amino acids", False)
                ],
                "wrong_explanations": {
                    1: "Not all glucose is stored — plants use glucose continuously for growth, which means some becomes cellulose, but energy supply via respiration is the primary ongoing use.",
                    2: "Cellulose is important but only for cell walls — energy supply through respiration is the primary ongoing requirement.",
                    3: "Protein synthesis is important, but requires nitrogen — not all glucose goes to proteins."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 4. AEROBIC RESPIRATION
    # ══════════════════════════════════════════════
    {
        "id": "aerobic-respiration",
        "title": "Aerobic Respiration",
        "spec": "4.4.2.1",
        "summary": "Describe aerobic respiration — what it is, where it happens and what it produces.",
        "theory": [
            {
                "heading": "What is Respiration?",
                "content": "Respiration is the process by which ALL living cells release energy from organic molecules — mainly GLUCOSE — to produce ATP (adenosine triphosphate).\n\nATENTION: Respiration is NOT the same as BREATHING. Breathing (ventilation) moves air in and out of the lungs. Respiration is a CHEMICAL PROCESS happening inside every cell.\n\nATP is the ENERGY CURRENCY of cells — it is the molecule that directly powers all cellular processes:\nMuscle contraction.\nActive transport.\nProtein synthesis.\nCell division.\nMaintaining body temperature.\n\nRespiration is continuous — happening in every living cell, day and night, throughout your entire life."
            },
            {
                "heading": "The Equation for Aerobic Respiration",
                "content": "Aerobic respiration uses OXYGEN to completely break down glucose.\n\nWord equation:\nglucose + oxygen → carbon dioxide + water (+ energy released as ATP)\n\nSymbol equation:\nC₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O\n\nKey points:\nGlucose is completely broken down — all the carbon atoms end up as CO₂.\nWater is produced — the hydrogen from glucose combines with oxygen.\nLarge amount of ENERGY is released — approximately 36–38 ATP molecules per glucose.\nThis is the most efficient form of respiration."
            },
            {
                "heading": "Where Aerobic Respiration Occurs",
                "content": "Aerobic respiration takes place in the MITOCHONDRIA — the 'powerhouses' of the cell.\n\nThe mitochondria have a folded inner membrane (called cristae) which increases the surface area for the reactions.\n\nCells with HIGH energy demands have MORE mitochondria:\nMuscle cells — need large amounts of ATP for contraction.\nLiver cells — highly metabolically active, many chemical reactions.\nSperm cells — need ATP to power the flagellum for swimming.\nHeart muscle cells — never stop contracting, need a constant ATP supply.\n\nCells with lower energy demands have fewer mitochondria."
            },
            {
                "heading": "Why Aerobic Respiration is so Efficient",
                "content": "Aerobic respiration releases approximately 36–38 ATP molecules per glucose molecule — far more than anaerobic respiration (which produces only about 2 ATP).\n\nThis is because oxygen allows the complete breakdown of glucose:\nAll six carbon atoms → 6 CO₂ (carbon fully released).\nAll hydrogen atoms → 6 H₂O (hydrogen fully removed).\nAll the chemical energy stored in the C–H bonds of glucose is harvested.\n\nWithout oxygen, only a small fraction of this energy can be released — the rest remains locked in the waste products (lactic acid or ethanol).\n\nThis is why we breathe — to supply the constant oxygen demand of aerobic respiration in every cell."
            }
        ],
        "variables": [],
        "equations": [
            "glucose + oxygen → carbon dioxide + water",
            "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O"
        ],
        "common_mistake": "RESPIRATION is not the same as BREATHING. Breathing is ventilation — moving air in and out of lungs. Respiration is the CHEMICAL PROCESS in cells that releases energy from glucose. Also: aerobic respiration happens in MITOCHONDRIA — not in the nucleus, not in chloroplasts.",
        "key_note": "Aerobic respiration: glucose + oxygen → CO₂ + water. In mitochondria. Releases ~36–38 ATP. Continuous in all living cells. Exothermic — energy released.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Aerobic Respiration — Match the Term",
            "instruction": "Match each term to its correct description.",
            "pairs": [
                ("Glucose", "The fuel molecule broken down in respiration"),
                ("Oxygen", "Needed for aerobic respiration — allows complete breakdown of glucose"),
                ("ATP", "The energy molecule produced — directly powers all cell processes"),
                ("Carbon dioxide", "Waste product — produced when glucose is completely broken down"),
                ("Mitochondria", "The organelle where aerobic respiration takes place"),
                ("Water", "Produced when hydrogen from glucose combines with oxygen"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Where in the cell does aerobic respiration take place?",
                "opts": [
                    ("Mitochondria", True),
                    ("Chloroplasts", False),
                    ("Nucleus", False),
                    ("Ribosomes", False)
                ],
                "wrong_explanations": {
                    1: "Chloroplasts carry out PHOTOSYNTHESIS — they capture energy from light. Mitochondria RELEASE energy from glucose.",
                    2: "The nucleus contains DNA and controls the cell — it is not the site of aerobic respiration.",
                    3: "Ribosomes build proteins — they are not involved in energy release from glucose."
                }
            },
            {
                "q": "What is the difference between respiration and breathing?",
                "opts": [
                    ("Breathing moves air in and out of the lungs. Respiration is the chemical process in cells that releases energy from glucose.", True),
                    ("They are the same process — both refer to taking in oxygen and releasing carbon dioxide.", False),
                    ("Breathing produces ATP. Respiration produces oxygen.", False),
                    ("Respiration only occurs in the lungs. Breathing occurs throughout the body.", False)
                ],
                "wrong_explanations": {
                    1: "Breathing and respiration are NOT the same — confusing them is one of the most common biology mistakes. Breathing is a mechanical process; respiration is a chemical one.",
                    2: "Breathing takes in air (including O₂) — but ATP is produced by RESPIRATION in cells. Oxygen is produced by photosynthesis, not breathing.",
                    3: "Respiration occurs in ALL living cells throughout the body — not just the lungs."
                }
            },
            {
                "q": "Why do muscle cells contain more mitochondria than skin cells?",
                "opts": [
                    ("Muscle cells need much more ATP energy for contraction — more mitochondria produce more ATP", True),
                    ("Mitochondria are heavier than other organelles and sink to the bottom of active cells", False),
                    ("Skin cells are too small to contain many mitochondria", False),
                    ("Muscle cells use more oxygen, so they need more mitochondria to absorb it", False)
                ],
                "wrong_explanations": {
                    1: "Organelles don't 'sink' — they are distributed throughout the cytoplasm based on cellular need.",
                    2: "Skin cells are actually similar in size to muscle cells — it's energy demand, not size, that determines mitochondria number.",
                    3: "Mitochondria do use oxygen in respiration — but they use it to produce ATP. The driving factor for more mitochondria is the ENERGY DEMAND, not simply oxygen availability."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 5. ANAEROBIC RESPIRATION
    # ══════════════════════════════════════════════
    {
        "id": "anaerobic-respiration",
        "title": "Anaerobic Respiration",
        "spec": "4.4.2.2",
        "summary": "Describe anaerobic respiration in animals and yeast and explain its uses.",
        "theory": [
            {
                "heading": "What is Anaerobic Respiration?",
                "content": "Anaerobic respiration is respiration WITHOUT OXYGEN.\n\nIt occurs when oxygen is in short supply — for example, during very intense exercise when muscles cannot get enough oxygen fast enough.\n\nAnaerobic respiration:\nDoes NOT require oxygen.\nStarts with glucose, like aerobic respiration.\nProduces MUCH LESS ATP than aerobic respiration (only about 2 ATP per glucose compared to ~36 for aerobic).\nProduces different waste products depending on the organism.\n\nIt is a short-term emergency measure — useful for bursts of intense activity but not sustainable for long."
            },
            {
                "heading": "Anaerobic Respiration in Animals (including Humans)",
                "content": "In animal muscles (and some bacteria):\n\nWord equation:\nglucose → lactic acid\n\nNo oxygen needed. Only a small amount of ATP is produced.\n\nLactic acid is produced because glucose cannot be fully broken down without oxygen — lactic acid is the incomplete breakdown product.\n\nEffects of lactic acid:\nLactic acid LOWERS the pH inside muscle cells.\nThis disrupts enzyme activity → muscles stop contracting properly.\nThis causes the BURNING SENSATION in muscles during intense exercise.\nLeads to MUSCLE FATIGUE — the muscles cannot maintain maximum effort.\n\nLactic acid is NOT toxic long-term — after exercise, it is transported to the LIVER where it is converted back to glucose (or broken down further in aerobic respiration)."
            },
            {
                "heading": "Anaerobic Respiration in Yeast (Fermentation)",
                "content": "In YEAST (and also in plants under waterlogged conditions):\n\nWord equation:\nglucose → ethanol + carbon dioxide\n\nThis process is called FERMENTATION.\n\nFermentation is enormously important in food and drink production:\n\nBREAD MAKING:\nYeast is added to dough.\nYeast ferments sugars in the dough → produces CO₂.\nCO₂ bubbles make the dough RISE (become light and airy).\nEthanol produced evaporates during baking.\n\nALCOHOLIC DRINKS (beer, wine, cider):\nYeast ferments sugars in grain (beer), grapes (wine) or fruit (cider).\nEthanol accumulates → forms the alcohol in the drink.\nCO₂ also produced → gives fizzy drinks their bubbles.\n\nBIOFUELS:\nEthanol from fermentation can be used as a biofuel — a renewable energy source."
            },
            {
                "heading": "Comparing Aerobic and Anaerobic Respiration",
                "content": "Here is a clear side-by-side comparison:\n\nAEROBIC RESPIRATION:\nNeeds oxygen? YES.\nProducts: CO₂ + water.\nATP produced: ~36–38 per glucose.\nWhere: Mitochondria.\nWhen used: Normal conditions.\n\nANAEROBIC RESPIRATION (animals):\nNeeds oxygen? NO.\nProducts: Lactic acid.\nATP produced: ~2 per glucose.\nWhere: Cytoplasm.\nWhen used: Intense exercise, emergency.\n\nANAEROBIC RESPIRATION (yeast):\nNeeds oxygen? NO.\nProducts: Ethanol + CO₂.\nATP produced: ~2 per glucose.\nWhere: Cytoplasm.\nWhen used: Absence of oxygen (e.g. in dough, in fermenting liquid)."
            }
        ],
        "variables": [],
        "equations": [
            "Anaerobic (animals): glucose → lactic acid",
            "Anaerobic (yeast): glucose → ethanol + carbon dioxide"
        ],
        "common_mistake": "Anaerobic respiration in ANIMALS produces LACTIC ACID. Anaerobic respiration in YEAST produces ETHANOL + CO₂. These are different products — this distinction comes up repeatedly in exams. Do NOT say 'lactic acid' when asked about yeast fermentation.",
        "key_note": "Animals: glucose → lactic acid (no O₂, little ATP, causes muscle fatigue). Yeast: glucose → ethanol + CO₂ (fermentation — used in bread, beer, wine). Both produce far less ATP than aerobic respiration.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Aerobic or Anaerobic — and Which Organism?",
            "instruction": "Sort each statement into the correct type of respiration.",
            "pairs": [
                ("Aerobic", "Requires oxygen — produces CO₂, water and ~36 ATP"),
                ("Anaerobic — animals", "No oxygen — produces lactic acid, causes burning feeling in muscles"),
                ("Anaerobic — yeast", "No oxygen — produces ethanol and CO₂, used in bread and alcohol production"),
                ("Anaerobic — animals", "Causes muscle fatigue during intense exercise"),
                ("Anaerobic — yeast", "CO₂ produced makes bread dough rise"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is produced by anaerobic respiration in yeast?",
                "opts": [
                    ("Ethanol and carbon dioxide", True),
                    ("Lactic acid", False),
                    ("Glucose and oxygen", False),
                    ("Carbon dioxide and water", False)
                ],
                "wrong_explanations": {
                    1: "Lactic acid is produced by ANIMAL muscles during anaerobic respiration — NOT by yeast. Yeast produces ethanol + CO₂.",
                    2: "Glucose and oxygen are the REACTANTS in aerobic respiration — they go in, not come out of anaerobic respiration.",
                    3: "CO₂ and water = products of AEROBIC respiration. Anaerobic respiration in yeast produces ethanol + CO₂ (not water)."
                }
            },
            {
                "q": "Why does bread dough rise when yeast is added?",
                "opts": [
                    ("Yeast ferments sugars in the dough — the CO₂ produced forms bubbles that make the dough expand", True),
                    ("Yeast produces oxygen which inflates the dough", False),
                    ("Yeast absorbs water from the dough, making it lighter", False),
                    ("Yeast produces lactic acid which reacts with flour to create gas", False)
                ],
                "wrong_explanations": {
                    1: "Yeast produces CO₂ and ethanol during fermentation — not oxygen. The ethanol evaporates when the bread is baked.",
                    2: "Yeast absorbs sugars for fermentation — it doesn't absorb significant water from the dough.",
                    3: "Yeast (not animals) in bread produces ethanol and CO₂ — not lactic acid."
                }
            },
            {
                "q": "During a sprint race, an athlete's muscles switch to anaerobic respiration. Why?",
                "opts": [
                    ("The muscles are working so hard that oxygen cannot be delivered fast enough — anaerobic respiration continues without it", True),
                    ("Anaerobic respiration produces more ATP, so athletes switch to it for maximum performance", False),
                    ("The lungs stop absorbing oxygen during intense exercise", False),
                    ("Glucose runs out during sprinting so the muscles use a different fuel", False)
                ],
                "wrong_explanations": {
                    1: "Anaerobic respiration produces FAR LESS ATP (~2 vs ~36) — it is not chosen for maximum performance. It is an emergency fallback when oxygen supply is insufficient.",
                    2: "The lungs work harder during exercise, not less — breathing rate and depth increase. But even this can't supply enough oxygen for maximum muscle output.",
                    3: "Muscles use glucose during sprinting — glycogen stores are broken down to supply glucose. Glucose shortage ('hitting the wall') is different from the short-term switch to anaerobic respiration."
                }
            },
            {
                "q": "Which process produces more ATP per glucose molecule?",
                "opts": [
                    ("Aerobic respiration — approximately 36–38 ATP compared to 2 ATP from anaerobic", True),
                    ("Anaerobic respiration — it happens faster so produces more total ATP", False),
                    ("They produce the same amount — both start with glucose", False),
                    ("Anaerobic respiration — the lactic acid contains extra energy", False)
                ],
                "wrong_explanations": {
                    1: "Anaerobic can produce ATP FASTER per unit time in emergencies — but produces FAR LESS per glucose molecule.",
                    2: "They both start with glucose but have completely different efficiencies. Aerobic: ~36–38 ATP. Anaerobic: ~2 ATP.",
                    3: "Lactic acid does retain some chemical energy (glucose isn't fully broken down) — but from the cell's perspective, anaerobic yields only ~2 ATP of USABLE energy."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 6. RESPONSE TO EXERCISE
    # ══════════════════════════════════════════════
    {
        "id": "response-to-exercise",
        "title": "Response to Exercise",
        "spec": "4.4.2.3",
        "summary": "Describe how the body responds during and after exercise, including oxygen debt.",
        "theory": [
            {
                "heading": "Why Exercise Demands More from the Body",
                "content": "During exercise, muscles work harder — contracting more frequently and with more force.\n\nThis increased muscle activity requires:\nMORE GLUCOSE — the fuel for respiration.\nMORE OXYGEN — for aerobic respiration.\nFASTER REMOVAL of carbon dioxide and lactic acid — waste products.\n\nThe body must respond to these increased demands almost immediately.\n\nThree systems work together to meet the demands of exercise:\nThe HEART — pumps blood faster and harder.\nThe LUNGS — breathe faster and deeper.\nThe BLOOD VESSELS — redistribute blood flow to muscles."
            },
            {
                "heading": "Changes During Exercise",
                "content": "The body makes several rapid adjustments when exercise begins:\n\nHEART RATE INCREASES:\nThe heart beats faster (higher rate) and contracts more strongly (higher stroke volume).\nMore blood circulates per minute → more O₂ and glucose delivered to muscles.\nMore CO₂ and waste removed per minute.\n\nBREATHING RATE AND DEPTH INCREASE:\nYou breathe faster and take deeper breaths.\nMore O₂ inhaled per minute.\nMore CO₂ exhaled per minute.\nMaintains the concentration gradients in the alveoli.\n\nVASODILATION — blood vessels to muscles widen:\nMore blood is redirected to active muscles.\nSkin flushes (more blood near surface for cooling).\nBlood flow reduced to non-essential organs (e.g. digestive system) temporarily.\n\nGLYCOGEN BREAKDOWN:\nGlycogen stored in the LIVER and MUSCLES is converted back to glucose.\nIncreases the blood glucose supply to muscles."
            },
            {
                "heading": "Lactic Acid and Oxygen Debt",
                "content": "During very intense exercise (e.g. sprinting), the body cannot supply oxygen fast enough.\n\nMuscles switch to ANAEROBIC RESPIRATION:\nglucose → lactic acid\n\nLACTIC ACID ACCUMULATES in muscles:\nLowers the pH of the muscle tissue.\nDisrupts enzyme activity.\nCauses the burning, aching sensation during intense effort.\nLeads to muscle fatigue.\n\nOXYGEN DEBT (also called EPOC — Excess Post-Exercise Oxygen Consumption):\nAfter exercise stops, the body continues to breathe faster than normal.\nThis extra oxygen is used to process the accumulated lactic acid.\nLactic acid is transported in the blood to the LIVER.\nIn the liver, lactic acid is converted BACK into glucose — this requires oxygen.\nThe amount of extra oxygen needed after exercise to clear the lactic acid = the OXYGEN DEBT.\n\nThe harder the exercise, the more lactic acid produced, the larger the oxygen debt, and the longer recovery takes."
            },
            {
                "heading": "Why Training Improves Performance",
                "content": "Regular exercise training causes adaptations that improve the body's response:\n\nHEART:\nCardiac muscle becomes stronger — heart pumps more blood per beat (larger stroke volume).\nResting heart rate falls (a sign of cardiovascular fitness).\n\nMUSCLES:\nMore mitochondria develop in muscle cells — greater capacity for aerobic respiration.\nLarger glycogen stores — more fuel available.\nImproved blood vessel density — more efficient oxygen delivery.\n\nLUNGS:\nLarger lung capacity.\nMore efficient gas exchange.\n\nBLOOD:\nHigher red blood cell count in trained athletes — more haemoglobin → more O₂ carried per litre of blood."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Oxygen debt is NOT the lack of oxygen in the blood during exercise. It is the EXTRA oxygen needed AFTER exercise to convert the lactic acid that accumulated. Students often say 'you breathe harder during exercise to repay oxygen debt' — you breathe harder DURING exercise to supply O₂, and continue breathing hard AFTER to repay the debt.",
        "key_note": "Exercise → more O₂ and glucose needed → heart rate up, breathing rate up, vasodilation. Intense exercise → anaerobic → lactic acid → muscle fatigue. After exercise → oxygen debt → lactic acid converted to glucose in liver.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Exercise Response to its Purpose",
            "instruction": "Match each change to why it happens during exercise.",
            "pairs": [
                ("Heart rate increases", "Delivers more O₂ and glucose to muscles, removes CO₂ faster"),
                ("Breathing rate and depth increase", "Takes in more O₂ and expels more CO₂ per minute"),
                ("Vasodilation in muscles", "More blood redirected to active muscles — better O₂ supply"),
                ("Glycogen breakdown in liver", "Converts stored glycogen to glucose to fuel muscles"),
                ("Continued heavy breathing after exercise", "Repaying oxygen debt — extra O₂ to convert lactic acid back to glucose"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does heart rate increase during exercise?",
                "opts": [
                    ("To deliver more oxygen and glucose to muscles and remove CO₂ and lactic acid faster", True),
                    ("To raise body temperature to improve enzyme efficiency", False),
                    ("To produce more red blood cells for the increased demand", False),
                    ("To increase blood pressure so more oxygen enters through the skin", False)
                ],
                "wrong_explanations": {
                    1: "Exercise does raise body temperature slightly — but this is a consequence, not the purpose of increased heart rate.",
                    2: "New red blood cells take days to produce — the immediate response is to pump existing blood faster.",
                    3: "Oxygen doesn't enter through the skin in humans — it enters through the lungs. The skin's increased blood flow is for COOLING, not oxygen absorption."
                }
            },
            {
                "q": "Why do you continue to breathe heavily for several minutes after stopping intense exercise?",
                "opts": [
                    ("Repaying the oxygen debt — extra O₂ is needed to convert accumulated lactic acid back to glucose in the liver", True),
                    ("The lungs take time to slow down after being stimulated", False),
                    ("To replace all the oxygen used during exercise", False),
                    ("Lactic acid in the blood stimulates the lungs to keep working hard", False)
                ],
                "wrong_explanations": {
                    1: "The lungs respond to chemical signals from the blood — they slow down when CO₂ and lactic acid levels normalise.",
                    2: "All the oxygen used during exercise was already replaced during exercise — the post-exercise breathing is specifically about the lactic acid that accumulated.",
                    3: "Lactic acid in the blood does stimulate breathing — but the reason breathing stays elevated is specifically to process that lactic acid in the liver."
                }
            },
            {
                "q": "What is oxygen debt?",
                "opts": [
                    ("The extra oxygen needed after exercise to convert accumulated lactic acid back to glucose in the liver", True),
                    ("The oxygen missing from muscle cells during intense exercise", False),
                    ("The difference between oxygen inhaled and oxygen used during exercise", False),
                    ("The oxygen stored in myoglobin in muscles before exercise", False)
                ],
                "wrong_explanations": {
                    1: "The lack of oxygen in muscles during exercise is what CAUSES anaerobic respiration — oxygen debt specifically refers to the post-exercise oxygen requirement to process the resulting lactic acid.",
                    2: "Difference between inhaled and used oxygen relates to metabolic efficiency — oxygen debt is specifically post-exercise processing of lactic acid.",
                    3: "Myoglobin stores oxygen in muscles — this is used during exercise, but 'oxygen debt' refers to the post-exercise recovery process."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 7. METABOLISM
    # ══════════════════════════════════════════════
    {
        "id": "metabolism",
        "title": "Metabolism",
        "spec": "4.4.2.4",
        "summary": "Define metabolism and describe the key metabolic reactions in living organisms.",
        "theory": [
            {
                "heading": "What is Metabolism?",
                "content": "METABOLISM is the sum of ALL the chemical reactions taking place in a cell or organism at any given time.\n\nEvery reaction that builds something up or breaks something down is part of metabolism.\n\nMetabolism is what keeps you alive — it powers growth, movement, repair, digestion, nerve signals, and every other process your body performs.\n\nMetabolic reactions fall into two broad categories:\nCATABOLISM — breaking large molecules into smaller ones (releasing energy).\nANABOLISM — building large molecules from smaller ones (requires energy)."
            },
            {
                "heading": "Building Reactions (Anabolism)",
                "content": "These reactions USE energy (ATP) to build large molecules from small ones:\n\nProtein synthesis:\nAmino acids → proteins (e.g. enzymes, haemoglobin, structural proteins).\nRequires ATP and takes place at ribosomes.\n\nCellulose synthesis:\nGlucose molecules → cellulose (for plant cell walls).\n\nStarch and glycogen synthesis:\nGlucose → starch (storage in plants).\nGlucose → glycogen (storage in animal liver and muscles).\n\nFat synthesis:\nFatty acids + glycerol → triglycerides (for cell membranes, energy storage, insulation).\n\nDNA replication:\nNucleotides → new DNA strands (before cell division)."
            },
            {
                "heading": "Breaking-Down Reactions (Catabolism)",
                "content": "These reactions RELEASE energy by breaking large molecules into smaller ones:\n\nRespiration (the most important catabolic reaction):\nGlucose + oxygen → carbon dioxide + water (releases ATP).\n\nDigestion:\nStarch → maltose → glucose (by amylase).\nProteins → amino acids (by proteases).\nFats → fatty acids + glycerol (by lipase).\n\nGlycolysis:\nGlucose broken down in the cytoplasm — the first step of respiration.\n\nDeamination (in the liver):\nExcess amino acids → removed amino group → excreted as urea.\nThe remaining carbon skeleton → used in respiration.\n\nAll these reactions are controlled by ENZYMES — which is why temperature and pH are so important for survival."
            },
            {
                "heading": "Why Metabolism Matters",
                "content": "Metabolic rate is the overall speed at which an organism's metabolism runs.\n\nFactors affecting metabolic rate:\nBODY SIZE — larger organisms have a higher total metabolic rate (but lower per gram).\nMUSCLE MASS — muscle tissue is metabolically very active; more muscle = higher metabolic rate.\nEXERCISE — physical activity greatly increases metabolic rate.\nTEMPERATURE — ectothermic organisms (e.g. reptiles) have metabolic rates heavily influenced by external temperature.\nHORMONES — thyroxine (from the thyroid gland) controls the basal metabolic rate.\n\nUREA PRODUCTION is a key metabolic waste product:\nExcess amino acids cannot be stored.\nThe liver removes the amino group (–NH₂) through DEAMINATION.\nAmmonia is produced → converted to UREA (less toxic).\nUrea is carried in the blood to the KIDNEYS where it is filtered out and excreted in urine."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Metabolism is the TOTAL of ALL chemical reactions — not just respiration. Students often say 'metabolism = respiration' but metabolism includes digestion, protein synthesis, DNA replication, urea production and many more reactions. Respiration is the most central metabolic process, but not the only one.",
        "key_note": "Metabolism = all chemical reactions in the body. Anabolism = building up (uses ATP). Catabolism = breaking down (releases ATP). Key examples: protein synthesis, respiration, digestion, glycogen synthesis, urea production.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Anabolism or Catabolism?",
            "instruction": "Sort each reaction into building up (anabolism) or breaking down (catabolism).",
            "pairs": [
                ("Anabolism — building up", "Amino acids joined to make proteins at ribosomes"),
                ("Catabolism — breaking down", "Glucose broken down in aerobic respiration to release ATP"),
                ("Anabolism — building up", "Glucose polymerised to make glycogen in liver and muscles"),
                ("Catabolism — breaking down", "Proteins in food broken down to amino acids by proteases"),
                ("Catabolism — breaking down", "Excess amino acids deaminated in the liver to produce urea"),
                ("Anabolism — building up", "Fatty acids and glycerol joined to form triglycerides for fat storage"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is metabolism?",
                "opts": [
                    ("The sum of all chemical reactions taking place in a cell or organism", True),
                    ("Only the reactions that release energy — such as respiration", False),
                    ("The process of digesting food in the gut", False),
                    ("How quickly a person breathes and moves", False)
                ],
                "wrong_explanations": {
                    1: "Metabolism includes ALL reactions — both energy-releasing (catabolism) and energy-using (anabolism). Respiration is just one part.",
                    2: "Digestion is one part of metabolism — but metabolism includes protein synthesis, DNA replication, glycogen synthesis, and many more reactions.",
                    3: "Breathing rate and movement speed are consequences of metabolic activity — metabolism itself refers to the chemical reactions, not the physical movements."
                }
            },
            {
                "q": "Why is urea produced in the liver?",
                "opts": [
                    ("Excess amino acids cannot be stored — the amino group is removed (deamination) and converted to urea for excretion", True),
                    ("Urea is produced when glucose is broken down in anaerobic respiration", False),
                    ("The liver converts CO₂ and water into urea to reduce acid in the blood", False),
                    ("Urea is made when fat molecules are broken down into fatty acids", False)
                ],
                "wrong_explanations": {
                    1: "Anaerobic respiration in animals produces LACTIC ACID — not urea. Urea comes specifically from amino acid breakdown.",
                    2: "CO₂ is transported in the blood and exhaled — it is not converted to urea.",
                    3: "Fat breakdown produces fatty acids and glycerol — not urea. Urea specifically comes from amino acid deamination."
                }
            },
            {
                "q": "Which of the following is an example of an ANABOLIC (building) reaction?",
                "opts": [
                    ("Amino acids joined together at ribosomes to make a protein", True),
                    ("Glucose broken down in aerobic respiration to release ATP", False),
                    ("Starch digested by amylase into maltose in the mouth", False),
                    ("Lactic acid produced in muscles during anaerobic respiration", False)
                ],
                "wrong_explanations": {
                    1: "Aerobic respiration BREAKS DOWN glucose — this is a catabolic reaction.",
                    2: "Digestion BREAKS DOWN starch — another catabolic reaction.",
                    3: "Lactic acid production is the result of breaking down glucose — catabolic."
                }
            }
        ]
    },
],

"homeostasis": [


    # ══════════════════════════════════════════════
    # 1. HOMEOSTASIS
    # ══════════════════════════════════════════════
    {
        "id": "homeostasis",
        "title": "Homeostasis",
        "spec": "4.5.1",
        "summary": "Define homeostasis and explain how negative feedback maintains a stable internal environment.",
        "theory": [
            {
                "heading": "What is Homeostasis?",
                "content": "HOMEOSTASIS is the maintenance of a stable internal environment despite changes in external conditions or internal activity.\n\nThe body must keep the following conditions within very narrow limits:\nBODY TEMPERATURE — maintained at ~37°C for optimal enzyme activity.\nBLOOD GLUCOSE CONCENTRATION — maintained at ~5 mmol/L for cell function.\nWATER CONTENT of blood and tissue fluid — controlled to prevent cells shrinking or swelling.\n\nIf any of these deviate significantly from their set points, cells and organs begin to malfunction — potentially causing death.\n\nHomeostasis is what allows warm-blooded animals like humans to survive in very different environments, from Arctic tundra to tropical desert."
            },
            {
                "heading": "Negative Feedback",
                "content": "All homeostatic control systems use NEGATIVE FEEDBACK.\n\nNegative feedback means: when a variable moves AWAY from the set point, the system responds to bring it BACK.\n\nThe word 'negative' means the response OPPOSES the change — it works against the deviation, not with it.\n\nExample: if body temperature rises, the response is to COOL the body (opposing the rise). If body temperature falls, the response is to WARM the body (opposing the fall).\n\nNegative feedback keeps variables oscillating slightly around a set point — rarely exactly at it, but always returning to it."
            },
            {
                "heading": "The Three Components of Homeostatic Control",
                "content": "Every homeostatic control system has the same three components:\n\n1. RECEPTOR (sensor):\nDetects changes in the variable being controlled.\nGenerates a signal proportional to the degree of change.\nExamples: thermoreceptors in skin (detect temperature), osmoreceptors in hypothalamus (detect blood water content), glucose receptors in pancreas.\n\n2. COORDINATION CENTRE (control centre):\nReceives information from receptors.\nCompares the actual value to the set point.\nDetermines the appropriate response.\nExamples: the hypothalamus in the brain (temperature, water), the pancreas (blood glucose).\n\n3. EFFECTOR:\nCarries out the response that corrects the deviation.\nCan be a MUSCLE (e.g. skeletal muscles shivering) or a GLAND (e.g. sweat glands, endocrine glands releasing hormones).\n\nThe effector's response reduces the original stimulus — this completes the negative feedback loop."
            },
            {
                "heading": "Why Homeostasis is Essential",
                "content": "Enzymes control almost every biochemical reaction in the body — and enzymes are extremely sensitive to temperature, pH and concentration.\n\nIF TEMPERATURE RISES TOO HIGH:\nEnzymes denature → active site shape changes permanently → reactions stop → cells die.\nBody temperature above ~40°C causes proteins to denature → organ failure → death.\n\nIF BLOOD GLUCOSE FALLS TOO LOW (hypoglycaemia):\nBrain cells are starved of glucose → confusion, unconsciousness, brain damage, coma.\n\nIF BLOOD GLUCOSE STAYS TOO HIGH (hyperglycaemia):\nLong-term damage to blood vessels → blindness, kidney failure, nerve damage, cardiovascular disease.\n\nIF WATER CONTENT IS WRONG:\nToo little water → cells shrink → dehydration of tissues → organ failure.\nToo much water → cells swell → can burst (lysis) in animal cells.\n\nHomeostasis protects all these systems from harmful fluctuations."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Negative feedback does NOT mean the response is negative or harmful. It means the response OPPOSES the change — it is a corrective response. If temperature rises, the negative feedback brings it back DOWN. If temperature falls, it brings it back UP. The 'negative' refers to the direction of the response relative to the change.",
        "key_note": "Homeostasis: stable internal environment via negative feedback. Receptor → coordination centre → effector. Controls: temperature (37°C), blood glucose (~5 mmol/L), water content. Essential because enzymes are sensitive to these conditions.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Homeostatic Component",
            "instruction": "Match each component to its role in the homeostatic control system.",
            "pairs": [
                ("Receptor", "Detects a change in the variable — generates a signal"),
                ("Coordination centre", "Receives the signal, compares to set point, decides the response"),
                ("Effector", "Carries out the response — a muscle or gland"),
                ("Negative feedback", "The response opposes the original change — brings the variable back to the set point"),
                ("Set point", "The target value the body aims to maintain — e.g. 37°C for temperature"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is homeostasis?",
                "opts": [
                    ("Maintaining a stable internal environment using negative feedback mechanisms", True),
                    ("Increasing body temperature when the environment is hot", False),
                    ("Removing waste products from the body through excretion", False),
                    ("Controlling how fast organisms grow", False)
                ],
                "wrong_explanations": {
                    1: "Increasing body temperature when hot would make things WORSE — homeostasis CORRECTS deviations. When the body is hot, homeostasis acts to COOL it down.",
                    2: "Excretion is important but homeostasis specifically refers to maintaining STABLE internal conditions like temperature, blood glucose and water content.",
                    3: "Growth rate is controlled by hormones and genetics — not by homeostatic mechanisms."
                }
            },
            {
                "q": "Why is maintaining body temperature at 37°C so important?",
                "opts": [
                    ("Enzymes in the body work best at this temperature — deviations cause slower reactions or denaturation", True),
                    ("Bacteria cannot survive at 37°C, so the body stays infection-free", False),
                    ("The heart muscle can only contract at exactly 37°C", False),
                    ("Red blood cells carry oxygen most efficiently at 37°C", False)
                ],
                "wrong_explanations": {
                    1: "Bacteria can survive at 37°C — indeed, body temperature of ~37°C is actually ideal for many pathogens like Staphylococcus.",
                    2: "Cardiac muscle can contract across a range of temperatures — the critical issue is enzyme function at the cellular level.",
                    3: "Red blood cells do function across a range of temperatures — the enzyme sensitivity argument is the primary reason for temperature homeostasis."
                }
            },
            {
                "q": "A person's blood glucose level drops too low. What type of response will occur?",
                "opts": [
                    ("Negative feedback — mechanisms are activated to raise blood glucose back to the set point", True),
                    ("Positive feedback — more insulin is released to lower it further", False),
                    ("No response — the body cannot detect blood glucose levels", False),
                    ("The person's temperature rises to compensate for the energy loss", False)
                ],
                "wrong_explanations": {
                    1: "Positive feedback would make the problem WORSE — releasing more insulin when glucose is already low would be dangerous. Homeostasis uses negative feedback to correct deviations.",
                    2: "The pancreas and liver continuously monitor and respond to blood glucose levels — receptors in the pancreas detect low glucose and release glucagon.",
                    3: "Temperature and blood glucose are regulated independently by different systems — a drop in glucose does not trigger a temperature rise."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 2. THE HUMAN NERVOUS SYSTEM
    # ══════════════════════════════════════════════
    {
        "id": "nervous-system",
        "title": "The Human Nervous System",
        "spec": "4.5.2",
        "summary": "Describe the structure and function of the nervous system, neurones and synapses.",
        "theory": [
            {
                "heading": "Overview of the Nervous System",
                "content": "The nervous system detects changes (stimuli) in the environment and coordinates rapid responses.\n\nIt is divided into two main parts:\nCENTRAL NERVOUS SYSTEM (CNS): the BRAIN and SPINAL CORD. Processes all incoming information and determines the appropriate response.\nPERIPHERAL NERVOUS SYSTEM (PNS): all the NERVES that connect the CNS to the rest of the body — carrying signals to and from every organ, muscle and sense organ.\n\nThe nervous system communicates via ELECTRICAL IMPULSES — signals that travel along specialised cells called NEURONES at speeds of up to 120 m/s.\n\nThis is much faster than hormonal communication, making the nervous system ideal for rapid, precise responses."
            },
            {
                "heading": "Types of Neurone",
                "content": "There are three types of neurone, each with a specific role:\n\nSENSORY NEURONE:\nCarries electrical impulses FROM receptors (sense organs) TO the CNS.\nLong dendron carrying signal towards the cell body, then axon to the CNS.\nExample: carries pain signal from finger to spinal cord when you burn yourself.\n\nRELAY NEURONE:\nFound entirely WITHIN the CNS (brain and spinal cord).\nConnects sensory neurones to motor neurones.\nActs as a processing junction — signals can be passed on, filtered or directed to the appropriate response pathway.\n\nMOTOR NEURONE:\nCarries impulses FROM the CNS TO effectors (muscles or glands).\nLong axon — can be over 1 metre long (e.g. from spinal cord to foot).\nCovered in a MYELIN SHEATH — a fatty insulating layer that speeds up signal conduction.\nExample: carries signal to leg muscle to pull foot away from a sharp object."
            },
            {
                "heading": "The Synapse",
                "content": "A SYNAPSE is the junction between two neurones — a tiny gap called the SYNAPTIC CLEFT.\n\nElectrical impulses CANNOT jump across this gap — transmission across a synapse is CHEMICAL.\n\nHow a synapse works:\n1. An electrical impulse arrives at the end of the pre-synaptic neurone (the sending neurone).\n2. Vesicles containing NEUROTRANSMITTER molecules fuse with the membrane.\n3. Neurotransmitters are released into the synaptic cleft.\n4. They DIFFUSE across the gap.\n5. They bind to RECEPTOR PROTEINS on the post-synaptic neurone (the receiving neurone).\n6. This triggers a new electrical impulse in the next neurone.\n7. Neurotransmitters are then broken down by enzymes or reabsorbed — resetting the synapse.\n\nTransmission is ONE-WAY only — neurotransmitters are released from the pre-synaptic side and receptors are only on the post-synaptic side."
            },
            {
                "heading": "How Drugs Affect Synapses",
                "content": "Many drugs affect the nervous system by interfering with synapse function:\n\nSTIMULANTS (e.g. caffeine, nicotine, cocaine, amphetamines):\nIncrease neurotransmitter activity at synapses.\nMore impulses transmitted → increased alertness, faster heart rate, increased energy.\nCan cause addiction — the brain adapts to higher neurotransmitter levels and requires the drug to function normally.\n\nDEPRESSANTS (e.g. alcohol, benzodiazepines, sleeping tablets):\nReduce neurotransmitter activity.\nFewer impulses transmitted → slowed reactions, reduced anxiety, drowsiness, loss of coordination.\nAlcohol specifically slows the CNS — increasing reaction time significantly.\n\nSSRIs (antidepressants, e.g. fluoxetine):\nBlock the reabsorption of serotonin after it has been released.\nSerotonin stays in the synapse longer — improves mood.\nUsed to treat depression and anxiety."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Transmission WITHIN a neurone is electrical (an impulse). Transmission ACROSS a synapse is CHEMICAL (neurotransmitters). Students often say 'electrical signals cross the synapse' — they cannot. The synapse is a gap and must be crossed using chemical neurotransmitters that then trigger a new electrical impulse in the next neurone.",
        "key_note": "CNS = brain + spinal cord. PNS = all nerves. Sensory: receptor → CNS. Relay: within CNS. Motor: CNS → effector. Synapse: electrical → chemical (neurotransmitter) → electrical. One-way transmission.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Nervous System Component",
            "instruction": "Match each component to its correct role.",
            "pairs": [
                ("Sensory neurone", "Carries impulse FROM receptor TO CNS"),
                ("Relay neurone", "Connects sensory and motor neurones — found within the CNS"),
                ("Motor neurone", "Carries impulse FROM CNS TO effector (muscle or gland)"),
                ("Synapse", "Junction between neurones — signal crosses via chemical neurotransmitters"),
                ("Myelin sheath", "Fatty insulating layer around axon — speeds up impulse conduction"),
                ("CNS", "Brain and spinal cord — processes information and coordinates responses"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the correct pathway for a nerve signal from receptor to effector?",
                "opts": [
                    ("Receptor → sensory neurone → relay neurone → motor neurone → effector", True),
                    ("Receptor → motor neurone → relay neurone → sensory neurone → effector", False),
                    ("Effector → sensory neurone → CNS → motor neurone → receptor", False),
                    ("Receptor → CNS → sensory neurone → motor neurone", False)
                ],
                "wrong_explanations": {
                    1: "Motor and sensory neurones are in the wrong order. SENSORY carries to the CNS; MOTOR carries away from the CNS.",
                    2: "The pathway runs from receptor to effector — not in reverse.",
                    3: "Sensory neurones carry signals TO the CNS. They come AFTER the receptor, not after the CNS."
                }
            },
            {
                "q": "How does a nerve signal cross a synapse?",
                "opts": [
                    ("Neurotransmitters are released, diffuse across the gap and bind to receptors on the next neurone", True),
                    ("The electrical impulse jumps across the gap directly", False),
                    ("The two neurones fuse temporarily to allow the signal through", False),
                    ("Blood vessels carry chemical signals across the synaptic gap", False)
                ],
                "wrong_explanations": {
                    1: "The synapse is a liquid-filled gap — electrical impulses cannot jump across it. Chemical neurotransmitters are essential.",
                    2: "Neurones never physically fuse — the synaptic gap is always maintained. Fusion would prevent the one-way transmission that synapses provide.",
                    3: "Synaptic transmission takes microseconds — blood flow is far too slow. Neurotransmitters diffuse across the tiny gap."
                }
            },
            {
                "q": "Why is synaptic transmission one-directional?",
                "opts": [
                    ("Neurotransmitters are released only from the pre-synaptic side, and receptors are only on the post-synaptic side", True),
                    ("Electrical impulses can only travel in one direction through an axon", False),
                    ("The synaptic gap is too narrow for signals to travel both ways", False),
                    ("Enzymes on the post-synaptic side destroy neurotransmitters before they can go back", False)
                ],
                "wrong_explanations": {
                    1: "Electrical impulses technically can propagate in both directions in an isolated axon — the one-way nature of synapse transmission comes from the asymmetry of neurotransmitter release and receptor location.",
                    2: "Gap width has nothing to do with directionality — it's the arrangement of vesicles and receptors that enforces one-way flow.",
                    3: "Enzymes do break down neurotransmitters after binding — but this prevents prolonged stimulation, not directionality."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 3. REFLEX ACTIONS
    # ══════════════════════════════════════════════
    {
        "id": "reflex-actions",
        "title": "Reflex Actions",
        "spec": "4.5.2",
        "summary": "Describe reflex actions, the reflex arc and why reflexes are faster than voluntary responses.",
        "theory": [
            {
                "heading": "What is a Reflex?",
                "content": "A REFLEX is a rapid, automatic response to a stimulus that does not require conscious thought.\n\nReflexes are protective — they allow the body to respond to potentially harmful stimuli BEFORE the conscious brain can process the situation.\n\nKey features of a reflex:\nAUTOMATIC — happens without thinking.\nRAPID — much faster than a voluntary response.\nINVOLUNTARY — you cannot choose not to do it.\nSTEREOTYPED — always the same response to the same stimulus.\n\nExamples:\nWithdrawing your hand from a hot surface.\nKnee-jerk reflex (tapping the patellar tendon).\nPupil constricting in bright light (pupil reflex).\nSneezing and coughing.\nBlinking when an object moves towards the eye.\nBaby's grasp reflex."
            },
            {
                "heading": "The Reflex Arc",
                "content": "A reflex arc is the specific nerve pathway along which a reflex signal travels. Crucially, it passes through the SPINAL CORD rather than up to the conscious brain — this is what makes it so fast.\n\nThe pathway of a reflex arc:\n1. STIMULUS — a change detected by a sense organ (e.g. heat on the skin).\n2. RECEPTOR — specialised cells detect the stimulus and generate an electrical impulse.\n3. SENSORY NEURONE — carries the impulse to the spinal cord (part of the CNS).\n4. RELAY NEURONE — in the spinal cord, receives the impulse and passes it on. Also sends a signal UP to the brain — so the brain becomes aware AFTER the reflex has already occurred.\n5. MOTOR NEURONE — carries impulse from spinal cord to the effector.\n6. EFFECTOR — the muscle contracts (or gland secretes) to produce the response.\n7. RESPONSE — e.g. the hand moves away from the heat source.\n\nThe brain is aware of the reflex — but AFTER the response has already happened."
            },
            {
                "heading": "Why Reflexes are Faster than Voluntary Responses",
                "content": "VOLUNTARY response pathway:\nReceptor → sensory neurone → spinal cord → UP to brain → conscious processing → DOWN from brain → motor neurone → effector.\n\nREFLEX pathway:\nReceptor → sensory neurone → spinal cord (relay neurone) → motor neurone → effector.\n\nThe reflex bypasses the conscious brain (cerebral cortex) — this eliminates the time needed for:\nSignal travelling up to the brain.\nConscious processing and decision-making.\nSignal travelling back down from the brain.\n\nTypical voluntary reaction time: 0.2–0.3 seconds.\nTypical reflex reaction time: 0.04–0.1 seconds.\n\nThis 3–5× speed advantage can prevent serious injury — for example, moving your hand away from a sharp object or flame before the pain signal has even reached consciousness."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A reflex bypasses the CONSCIOUS BRAIN (cerebral cortex) — it is processed in the SPINAL CORD. The brain does receive the signal (that's why you become aware of it), but it does NOT initiate the reflex. Students often say 'the brain controls reflexes' — the brain is only aware of them afterwards.",
        "key_note": "Reflex arc: stimulus → receptor → sensory neurone → relay neurone (spinal cord) → motor neurone → effector → response. Faster than voluntary because it bypasses the conscious brain. Involuntary and automatic.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match Each Step of the Reflex Arc",
            "instruction": "Match each component to its role in the reflex arc.",
            "pairs": [
                ("Stimulus", "The change that triggers the reflex — e.g. touching a sharp object"),
                ("Receptor", "Detects the stimulus and generates an electrical impulse"),
                ("Sensory neurone", "Carries the impulse from the receptor to the spinal cord"),
                ("Relay neurone", "In the spinal cord — connects sensory to motor neurone"),
                ("Motor neurone", "Carries impulse from spinal cord to the effector"),
                ("Effector", "Muscle contracts or gland secretes — produces the response"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why are reflexes faster than voluntary responses?",
                "opts": [
                    ("They bypass the conscious brain — the signal is processed in the spinal cord using a shorter pathway", True),
                    ("Reflex neurones conduct impulses faster than voluntary neurones", False),
                    ("Reflexes use fewer neurotransmitters so synaptic delay is reduced", False),
                    ("The brain prioritises reflex signals over other information", False)
                ],
                "wrong_explanations": {
                    1: "Neurone conduction speed varies by myelination — not fundamentally by whether it's a reflex or voluntary pathway.",
                    2: "Synaptic delay is similar in both — the key saving is the elimination of the brain processing step entirely.",
                    3: "The brain doesn't 'prioritise' reflexes — it is simply not involved in initiating them."
                }
            },
            {
                "q": "You touch a hot surface and pull your hand away before you feel pain. What does this demonstrate?",
                "opts": [
                    ("The reflex arc bypasses the conscious brain — the withdrawal response occurred before pain was processed", True),
                    ("Pain receptors in the hand don't work under extreme heat", False),
                    ("The brain sends an emergency signal faster than normal in dangerous situations", False),
                    ("Motor neurones are faster than sensory neurones", False)
                ],
                "wrong_explanations": {
                    1: "Pain receptors DO work — you feel the pain a fraction of a second after your hand has already moved away.",
                    2: "The brain doesn't speed up for emergencies — the reflex works independently of conscious brain processing.",
                    3: "Motor and sensory neurones have similar conduction speeds — the key is the PATHWAY length, not individual neurone speed."
                }
            },
            {
                "q": "In which part of the CNS is a spinal reflex arc processed?",
                "opts": [
                    ("The spinal cord — relay neurones connect sensory and motor neurones here", True),
                    ("The cerebral cortex — the thinking part of the brain", False),
                    ("The cerebellum — which coordinates movement", False),
                    ("The medulla oblongata — which controls heart rate and breathing", False)
                ],
                "wrong_explanations": {
                    1: "The cerebral cortex is the conscious thinking brain — reflex arcs specifically BYPASS this to be fast.",
                    2: "The cerebellum coordinates balance and smooth movement — it is not the site of spinal reflex processing.",
                    3: "The medulla oblongata controls automatic functions like heart rate — but reflex arcs for quick withdrawal responses are processed in the spinal cord."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 4. THERMOREGULATION
    # ══════════════════════════════════════════════
    {
        "id": "thermoregulation",
        "title": "Thermoregulation",
        "spec": "4.5.1",
        "summary": "Describe how the body maintains a constant core temperature of 37°C.",
        "theory": [
            {
                "heading": "Why Temperature Must Be Controlled",
                "content": "The human body must maintain a core temperature of approximately 37°C.\n\nThis is the OPTIMUM TEMPERATURE for human enzymes — the temperature at which they work most efficiently.\n\nIf temperature rises above ~40°C: enzymes denature → reactions stop → organ failure → death (hyperthermia).\n\nIf temperature falls below ~34°C: enzyme activity decreases dramatically → brain and heart function affected → loss of consciousness → death (hypothermia).\n\nThe body is constantly generating heat (from respiration in all cells) and losing heat (to the environment). Thermoregulation balances these."
            },
            {
                "heading": "The Hypothalamus — The Body's Thermostat",
                "content": "The HYPOTHALAMUS — a region in the brain — acts as the body's thermostat.\n\nIt has two types of thermoreceptors:\nCENTRAL THERMORECEPTORS in the hypothalamus itself — monitor the temperature of blood flowing through the brain.\nPERIPHERAL THERMORECEPTORS in the skin — detect changes in surface temperature (giving advance warning of environmental temperature changes).\n\nWhen the hypothalamus detects deviation from 37°C, it sends signals via the nervous system and hormones to trigger corrective responses."
            },
            {
                "heading": "Responses When Too Hot",
                "content": "When body temperature rises ABOVE 37°C, the hypothalamus triggers responses to LOSE heat:\n\nSWEATING:\nSweat glands in the skin produce sweat (mainly water + salts).\nSweat spreads over the skin surface.\nAs water EVAPORATES from the skin, it absorbs latent heat from the body → body cools.\nMore sweating occurs in hot conditions or during exercise.\n\nVASODILATION:\nBlood vessels (arterioles) near the skin surface WIDEN.\nMore blood flows close to the skin surface.\nMore heat is lost by radiation and convection from the skin.\nThis is why the skin looks flushed or red when hot.\n\nHAIRS LIE FLAT:\nErector pili muscles RELAX → hairs lie flat.\nNo trapped air layer → less insulation → more heat can escape.\n(More significant in other mammals than in humans due to less body hair.)"
            },
            {
                "heading": "Responses When Too Cold",
                "content": "When body temperature falls BELOW 37°C, the hypothalamus triggers responses to GENERATE and RETAIN heat:\n\nSHIVERING:\nSkeletal muscles contract rapidly and repeatedly.\nMuscle contractions require RESPIRATION → releases heat as a by-product.\nShivering can increase heat production up to 5× the resting rate.\n\nVASOCONSTRICTION:\nBlood vessels near the skin surface NARROW.\nLess blood flows close to the skin surface.\nLess heat lost by radiation from the skin.\nFingers and toes may become pale or blue in extreme cold.\n\nHAIRS STAND ON END:\nErector pili muscles CONTRACT → hairs raise upright.\nTraps a layer of warm air close to the skin → insulation layer.\n(More effective in other mammals — in humans this causes 'goosebumps').\n\nREDUCED SWEATING:\nSweat glands become less active.\nLess evaporative cooling.\n\nADRENALINE RELEASED:\nHormone that increases metabolic rate → more respiration → more heat produced."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "VASODILATION means blood vessels WIDEN — MORE blood near skin surface — MORE heat lost — occurs when TOO HOT. VASOCONSTRICTION means blood vessels NARROW — LESS blood near skin surface — LESS heat lost — occurs when TOO COLD. Students often get these mixed up. Remember: Dilation = Diameter increases = more heat lost.",
        "key_note": "Too hot: sweat (evaporation cools), vasodilation (more heat lost from skin), hairs flat. Too cold: shiver (respiration generates heat), vasoconstriction (less heat lost), hairs raised (insulation). Hypothalamus = the thermostat.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Too Hot or Too Cold?",
            "instruction": "Sort each response — does it happen when the body is too hot or too cold?",
            "pairs": [
                ("Too hot", "Sweating — evaporation removes heat from the body surface"),
                ("Too hot", "Vasodilation — blood vessels widen, more heat lost from skin surface"),
                ("Too cold", "Shivering — rapid muscle contractions generate heat via respiration"),
                ("Too cold", "Vasoconstriction — blood vessels narrow, less heat lost from skin"),
                ("Too hot", "Hairs lie flat — less insulation, more heat can escape"),
                ("Too cold", "Hairs stand on end — traps air for insulation (causes goosebumps)"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why does sweating cool the body down?",
                "opts": [
                    ("Water evaporating from the skin surface absorbs latent heat energy from the body — cooling it", True),
                    ("Sweat removes hot blood from deep in the body and cools it at the surface", False),
                    ("The salt in sweat chemically reacts with the skin to absorb heat", False),
                    ("Sweating increases blood flow to the skin, which cools the blood", False)
                ],
                "wrong_explanations": {
                    1: "Sweating doesn't involve blood — it is a secretion from sweat glands. The cooling effect is from EVAPORATION.",
                    2: "Salt in sweat helps retain water on the skin surface longer — the cooling mechanism is evaporation of water, not a chemical reaction.",
                    3: "Vasodilation increases blood flow to the skin for cooling — sweating itself is a separate mechanism that works through evaporation."
                }
            },
            {
                "q": "What is vasodilation and when does it occur?",
                "opts": [
                    ("Blood vessels near the skin widen — occurs when the body is too hot, allowing more heat to be lost", True),
                    ("Blood vessels narrow — occurs when the body is too cold, to conserve heat", False),
                    ("Blood vessels widen — occurs when the body is too cold, to warm the skin", False),
                    ("Blood vessels contract — occurs when the body is too hot, to prevent overheating", False)
                ],
                "wrong_explanations": {
                    1: "Blood vessels NARROWING = VASOCONSTRICTION — this happens when cold, to reduce heat loss. Vasodilation is widening.",
                    2: "If blood vessels widened when cold, more heat would be LOST — that would make the cold problem worse. Vasodilation occurs when HOT.",
                    3: "Blood vessels CONTRACTING = VASOCONSTRICTION — occurs when cold, not hot."
                }
            },
            {
                "q": "Why does shivering help when you are cold?",
                "opts": [
                    ("Rapid muscle contractions require aerobic respiration — heat is released as a by-product of respiration", True),
                    ("Shivering increases blood flow to the skin, warming the surface", False),
                    ("The vibration of muscles generates electrical energy that heats the body", False),
                    ("Shivering activates sweat glands which release warm fluid to the skin", False)
                ],
                "wrong_explanations": {
                    1: "Increased blood flow to the skin (vasodilation) increases heat LOSS — when cold, vasoconstriction REDUCES blood flow to the skin. Shivering warms the body through metabolic heat.",
                    2: "Muscles generate heat through CHEMICAL energy released in respiration — not by converting movement to electrical energy.",
                    3: "Sweat glands are LESS active when cold — sweating causes heat loss, which is the opposite of what's needed."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 5. THE ENDOCRINE SYSTEM
    # ══════════════════════════════════════════════
    {
        "id": "endocrine-system",
        "title": "The Endocrine System",
        "spec": "4.5.3",
        "summary": "Describe the endocrine system, the main glands and hormones, and compare hormonal with nervous communication.",
        "theory": [
            {
                "heading": "What is the Endocrine System?",
                "content": "The ENDOCRINE SYSTEM is the body's chemical communication system.\n\nIt uses HORMONES — chemical messenger molecules — to coordinate responses across the body.\n\nHormones are produced by ENDOCRINE GLANDS and secreted DIRECTLY INTO THE BLOODSTREAM — they have no ducts (unlike exocrine glands like salivary glands which have ducts).\n\nThe blood carries hormones to every organ in the body — but only TARGET ORGANS respond, because only they have the correct RECEPTOR PROTEINS for that hormone.\n\nHormonal responses are:\nSLOWER to start than nervous responses (blood must carry the hormone to the target).\nLONGER LASTING than nervous responses.\nMore WIDESPREAD — hormones reach all organs (though only targets respond)."
            },
            {
                "heading": "Key Endocrine Glands and Their Hormones",
                "content": "PITUITARY GLAND (in the brain — below the hypothalamus):\nThe 'master gland' — releases hormones that control other endocrine glands.\nProduces: FSH and LH (control reproduction), growth hormone, ADH (water balance).\n\nTHYROID GLAND (in the neck):\nProduces THYROXINE — controls METABOLIC RATE (the speed of chemical reactions in cells).\nAlso involved in growth and development.\n\nADRENAL GLANDS (above the kidneys — one on each kidney):\nProduce ADRENALINE — the 'fight or flight' hormone.\nReleased in response to stress, fear or excitement.\nEffects: increased heart rate, increased breathing rate, pupils dilate, blood redirected to muscles.\nPrepares the body for rapid physical action.\n\nPANCREAS:\nProduces INSULIN and GLUCAGON — regulate blood glucose concentration (see next subtopic).\n\nOVARIES (females):\nProduce OESTROGEN and PROGESTERONE — control the menstrual cycle and female secondary sexual characteristics.\n\nTESTES (males):\nProduce TESTOSTERONE — controls male secondary sexual characteristics and sperm production."
            },
            {
                "heading": "Nervous vs Hormonal Communication",
                "content": "The nervous system and endocrine system both communicate and coordinate responses, but work differently:\n\nNERVOUS SYSTEM:\nSignal type: electrical impulse along neurones.\nSpeed: very fast — up to 120 m/s.\nDuration: short-lived (milliseconds to seconds).\nTarget: specific cells connected by nerve fibres.\nResponse: immediate and precise.\nExamples: muscle contraction, reflex arc, heart rate control.\n\nENDOCRINE SYSTEM:\nSignal type: chemical hormone in bloodstream.\nSpeed: slower — limited by blood flow speed.\nDuration: longer lasting (minutes to hours or even days).\nTarget: any organ with the correct receptor.\nResponse: prolonged, broader.\nExamples: blood glucose regulation, puberty, growth, stress response.\n\nBOTH SYSTEMS WORK TOGETHER:\nFor example, during an emergency:\nThe NERVOUS SYSTEM detects danger and triggers an immediate response (e.g. jump back).\nThe ENDOCRINE SYSTEM releases adrenaline to sustain the response over the next few minutes."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Hormones travel in the BLOOD to target organs — they do NOT travel along nerves. Do not confuse the two systems. Also: not all organs respond to every hormone — only TARGET ORGANS with the correct receptor proteins respond.",
        "key_note": "Endocrine system: hormones in blood → target organs. Key glands: pituitary (master), thyroid (metabolism), adrenal (adrenaline), pancreas (insulin/glucagon), ovaries/testes (sex hormones). Slower but longer-lasting than nervous communication.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Gland to its Hormone and Function",
            "instruction": "Match each gland to what it produces and what that hormone does.",
            "pairs": [
                ("Pituitary gland", "FSH, LH and growth hormone — controls other glands — 'master gland'"),
                ("Thyroid gland", "Thyroxine — controls metabolic rate and development"),
                ("Adrenal gland", "Adrenaline — fight or flight, increases heart rate and breathing"),
                ("Pancreas", "Insulin and glucagon — regulate blood glucose concentration"),
                ("Ovaries", "Oestrogen and progesterone — menstrual cycle and female characteristics"),
                ("Testes", "Testosterone — male characteristics and sperm production"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "How do hormones reach their target organs?",
                "opts": [
                    ("Via the bloodstream — secreted directly into the blood by endocrine glands", True),
                    ("Via nerve fibres — along the same pathways as electrical impulses", False),
                    ("Through ducts that lead directly to the target organ", False),
                    ("They diffuse through tissue fluid between neighbouring cells only", False)
                ],
                "wrong_explanations": {
                    1: "Hormones travel in BLOOD, not along nerves — this is the fundamental difference between the two communication systems.",
                    2: "EXOCRINE glands (e.g. salivary glands, sweat glands) use ducts. ENDOCRINE glands secrete directly into the blood — they have no ducts.",
                    3: "Hormones travel long distances in the blood — they don't diffuse locally like paracrine signals."
                }
            },
            {
                "q": "Which hormone prepares the body for 'fight or flight'?",
                "opts": [
                    ("Adrenaline — released by the adrenal glands in response to stress or danger", True),
                    ("Insulin — released by the pancreas to lower blood glucose", False),
                    ("Thyroxine — released by the thyroid to increase metabolic rate", False),
                    ("Oestrogen — released by the ovaries to prepare the body for reproduction", False)
                ],
                "wrong_explanations": {
                    1: "Insulin lowers blood glucose — it is released after eating, not in response to danger.",
                    2: "Thyroxine controls long-term metabolic rate — it is not the emergency stress hormone.",
                    3: "Oestrogen is involved in the menstrual cycle — not in acute stress responses."
                }
            },
            {
                "q": "Which best describes the difference between nervous and hormonal communication?",
                "opts": [
                    ("Nervous = fast, short-lived, specific target via nerves. Hormonal = slower, longer-lasting, via bloodstream to target organs.", True),
                    ("Nervous = slow, long-lasting. Hormonal = fast, short-lived.", False),
                    ("They work in the same way — both use chemicals to transmit signals.", False),
                    ("Nervous system only controls muscles. Hormonal system only controls glands.", False)
                ],
                "wrong_explanations": {
                    1: "This is exactly the wrong way round. Nervous is FAST and SHORT. Hormonal is SLOWER and LONGER-LASTING.",
                    2: "Both do use chemicals at some point (neurotransmitters at synapses / hormones in blood) — but their overall mechanisms, speeds and targets are very different.",
                    3: "The nervous system controls both muscles AND glands. Hormones affect many different tissues — not just glands."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 6. BLOOD GLUCOSE CONTROL AND DIABETES
    # ══════════════════════════════════════════════
    {
        "id": "blood-glucose-diabetes",
        "title": "Blood Glucose Control and Diabetes",
        "spec": "4.5.3",
        "summary": "Describe how insulin and glucagon regulate blood glucose, and explain Type 1 and Type 2 diabetes.",
        "theory": [
            {
                "heading": "Why Blood Glucose Must Be Controlled",
                "content": "Blood glucose concentration must be kept within a narrow range — approximately 4–6 mmol/L.\n\nTOO LOW (hypoglycaemia):\nBrain cells are deprived of glucose → confusion, weakness, loss of consciousness, coma, brain damage.\nThe brain depends almost entirely on glucose as its energy source.\n\nTOO HIGH (hyperglycaemia):\nLong-term: glucose draws water out of cells by osmosis → dehydration of tissues.\nDamages blood vessel walls → reduced blood supply → blindness, kidney failure, poor wound healing.\nDamages nerves → neuropathy (tingling, pain, numbness in hands and feet).\nIncreased risk of heart attack and stroke.\n\nThe PANCREAS is the organ that monitors and regulates blood glucose — it contains specialised cells that detect glucose concentration and release hormones accordingly."
            },
            {
                "heading": "Insulin — Lowering Blood Glucose",
                "content": "After eating a meal:\nCarbohydrates are digested → glucose absorbed into blood → blood glucose RISES.\nPancreas BETA CELLS detect the rise and release INSULIN into the bloodstream.\n\nInsulin travels to the LIVER and MUSCLE CELLS and causes them to:\nAbsorb MORE glucose from the blood.\nConvert glucose → GLYCOGEN (a storage polymer) — this is called GLYCOGENESIS.\n\nBlood glucose concentration FALLS back to the set point.\n\nThis is NEGATIVE FEEDBACK — the response (insulin release + glucose storage) opposes the original change (rising glucose)."
            },
            {
                "heading": "Glucagon — Raising Blood Glucose",
                "content": "Between meals, during fasting or after exercise:\nCells use glucose for respiration → blood glucose FALLS.\nPancreas ALPHA CELLS detect the fall and release GLUCAGON into the bloodstream.\n\nGlucagon travels to the LIVER and causes it to:\nBreak down stored GLYCOGEN back into glucose — this is called GLYCOGENOLYSIS.\nRelease glucose back into the blood.\n\nBlood glucose concentration RISES back to the set point.\n\nAgain this is NEGATIVE FEEDBACK — glucagon release opposes the fall in glucose."
            },
            {
                "heading": "Type 1 and Type 2 Diabetes",
                "content": "Both types of diabetes result in poorly controlled blood glucose — but for different reasons.\n\nTYPE 1 DIABETES:\nCause: The immune system attacks and destroys the BETA CELLS in the pancreas (autoimmune condition).\nResult: Little or no insulin produced — blood glucose cannot be lowered after eating.\nOnset: Usually in childhood or adolescence.\nTreatment: INSULIN INJECTIONS (or insulin pump) — insulin cannot be taken as a tablet because it is a protein and would be digested.\nPatients must monitor blood glucose and adjust insulin doses accordingly.\n\nTYPE 2 DIABETES:\nCause: Body cells become RESISTANT to insulin — they no longer respond to it properly. The pancreas may still produce insulin, but it doesn't work.\nResult: Blood glucose remains elevated after eating.\nRisk factors: Obesity, lack of exercise, poor diet (high sugar/refined carbs), family history, age.\nTreatment: Lifestyle changes — weight loss, increased exercise, healthier diet.\nMedication: Metformin (increases cell sensitivity to insulin).\nIn advanced cases: insulin injections may also be needed."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "INSULIN lowers blood glucose by promoting GLYCOGEN STORAGE (glucose → glycogen). GLUCAGON raises blood glucose by promoting GLYCOGEN BREAKDOWN (glycogen → glucose). Students constantly confuse which hormone does which. Memory trick: INsulin = INto storage. Glucagon = Get glucose out of storage.",
        "key_note": "Glucose too high → pancreas releases INSULIN → glycogen stored → glucose falls. Glucose too low → pancreas releases GLUCAGON → glycogen broken down → glucose rises. Type 1: no insulin (autoimmune). Type 2: insulin resistance (lifestyle).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Insulin or Glucagon?",
            "instruction": "Match each statement to the correct hormone — insulin or glucagon.",
            "pairs": [
                ("Insulin", "Released when blood glucose is TOO HIGH — after eating a meal"),
                ("Glucagon", "Released when blood glucose is TOO LOW — between meals or after exercise"),
                ("Insulin", "Causes liver and muscle cells to convert glucose → glycogen for storage"),
                ("Glucagon", "Causes liver cells to break down glycogen → glucose and release it into blood"),
                ("Insulin", "Missing or ineffective in diabetes — leads to hyperglycaemia if untreated"),
            ]
        },
        "fifas": [
            {
                "label": "Blood Glucose Negative Feedback",
                "question": "Describe what happens to blood glucose and hormones after a person eats a meal containing a large amount of carbohydrates.",
                "steps": [
                    ("F", "Identify the change: carbohydrates digested → glucose absorbed → blood glucose RISES"),
                    ("I", "Pancreas beta cells detect the rise → release INSULIN into the blood"),
                    ("F", "Insulin travels to liver and muscles → glucose converted to glycogen (glycogenesis)"),
                    ("A", "Blood glucose FALLS back to ~5 mmol/L — negative feedback complete")
                ]
            }
        ],
        "quiz": [
            {
                "q": "Blood glucose rises after eating. Which hormone is released and what does it do?",
                "opts": [
                    ("Insulin — released by pancreas beta cells, causes glucose to be converted to glycogen in the liver", True),
                    ("Glucagon — released by pancreas alpha cells, causes glycogen to be broken down", False),
                    ("Adrenaline — released by adrenal glands, increases blood glucose further", False),
                    ("Thyroxine — released by thyroid, converts glucose to glycogen", False)
                ],
                "wrong_explanations": {
                    1: "Glucagon is released when blood glucose is TOO LOW — it would make a post-meal rise even worse.",
                    2: "Adrenaline does raise blood glucose (for fight or flight) — but is not the routine homeostatic response to eating.",
                    3: "Thyroxine controls metabolic rate — it does not regulate blood glucose directly."
                }
            },
            {
                "q": "Why must Type 1 diabetics inject insulin rather than take it as a tablet?",
                "opts": [
                    ("Insulin is a protein — it would be digested and destroyed by proteases in the gut before reaching the blood", True),
                    ("Insulin tablets haven't been invented yet", False),
                    ("The stomach acid destroys insulin too slowly for it to work", False),
                    ("Tablets cannot reach the pancreas where insulin needs to work", False)
                ],
                "wrong_explanations": {
                    1: "Oral insulin formulations are being researched (with special protective coatings) but the traditional reason is protein digestion in the gut.",
                    2: "It's not about speed — insulin is a large protein molecule that gets broken down into amino acids by digestive enzymes before being absorbed.",
                    3: "Insulin doesn't work IN the pancreas — it is secreted by the pancreas and works on LIVER and MUSCLE cells. The issue is gut digestion."
                }
            },
            {
                "q": "What is the key difference between Type 1 and Type 2 diabetes?",
                "opts": [
                    ("Type 1: pancreas produces no insulin (autoimmune). Type 2: cells become resistant to insulin (lifestyle-related).", True),
                    ("Type 1 is more common than Type 2", False),
                    ("Type 2 requires insulin injections; Type 1 can be managed with diet alone", False),
                    ("Both types are caused by the immune system destroying pancreas cells", False)
                ],
                "wrong_explanations": {
                    1: "Type 2 is FAR MORE COMMON — it makes up about 90% of all diabetes cases. Type 1 is less common.",
                    2: "This is the wrong way round. TYPE 1 requires insulin injections because the pancreas cannot make it. TYPE 2 is usually managed first with diet, exercise and tablets.",
                    3: "Only TYPE 1 is autoimmune. TYPE 2 develops due to insulin resistance — the immune system is not the cause."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 7. HUMAN REPRODUCTION AND HORMONES
    # ══════════════════════════════════════════════
    {
        "id": "human-reproduction-hormones",
        "title": "Human Reproduction and Hormones",
        "spec": "4.5.4",
        "summary": "Describe puberty, the menstrual cycle and the hormones that control human reproduction.",
        "theory": [
            {
                "heading": "Puberty and Sex Hormones",
                "content": "PUBERTY is the period of physical and hormonal development that prepares the body for reproduction.\n\nIn FEMALES: the pituitary gland releases FSH and LH → ovaries begin producing OESTROGEN.\nOestrogen causes female secondary sexual characteristics:\nBreast development.\nWidening of the pelvis.\nPubic and underarm hair growth.\nBeginning of the menstrual cycle.\nGrowth spurt.\n\nIn MALES: the pituitary gland releases LH → testes begin producing TESTOSTERONE.\nTestosterone causes male secondary sexual characteristics:\nEnlargement of the penis and testes.\nVoice breaking (larynx enlarges).\nFacial, pubic and body hair growth.\nMuscle mass increase.\nSperm production begins (spermatogenesis).\nGrowth spurt."
            },
            {
                "heading": "The Menstrual Cycle — Overview",
                "content": "The menstrual cycle is approximately 28 days long (varies between individuals).\n\nIt prepares the female reproductive system for potential pregnancy each month.\n\nDay 1: MENSTRUATION begins — the uterus lining (endometrium) is shed as the lining breaks down.\nDays 1–13: The uterus lining rebuilds and thickens — stimulated by oestrogen.\nDay ~14: OVULATION — a mature egg is released from one of the ovaries.\nDays 14–28: The uterus lining remains thick (prepared for implantation if fertilisation occurs) — maintained by progesterone.\n\nIf FERTILISATION occurs: the embryo implants in the uterus wall and pregnancy begins. Progesterone remains high.\nIf NO FERTILISATION: progesterone falls, the uterus lining breaks down → menstruation begins and the cycle repeats."
            },
            {
                "heading": "Hormones Controlling the Menstrual Cycle",
                "content": "Four hormones work together to control the menstrual cycle:\n\nFSH (Follicle Stimulating Hormone) — from the PITUITARY GLAND:\nCauses an egg inside a follicle to mature in the ovary.\nStimulates the ovaries to produce oestrogen.\n\nOESTROGEN — from the OVARIES:\nRepairs and thickens the uterus lining after menstruation.\nAt low levels: inhibits FSH production (prevents too many eggs maturing at once).\nAt HIGH levels (mid-cycle): triggers a surge in LH production.\n\nLH (Luteinising Hormone) — from the PITUITARY GLAND:\nThe LH surge at approximately Day 14 triggers OVULATION — the egg is released from the follicle.\n\nPROGESTERONE — from the CORPUS LUTEUM (the remains of the follicle after ovulation):\nMaintains the thickened uterus lining during the second half of the cycle.\nInhibits FSH and LH production (negative feedback).\nIf no pregnancy: corpus luteum breaks down → progesterone falls → lining breaks down → menstruation begins."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "FSH stimulates EGG MATURATION (not ovulation). LH triggers OVULATION. Oestrogen REBUILDS the uterus lining. Progesterone MAINTAINS the lining. The pituitary produces FSH and LH. The ovaries produce oestrogen and progesterone. Students often confuse which gland makes which hormone.",
        "key_note": "FSH (pituitary) → egg matures, oestrogen produced. Oestrogen (ovary) → uterus lining rebuilds. LH surge → ovulation (Day ~14). Progesterone (corpus luteum) → maintains lining. If no pregnancy → progesterone falls → menstruation.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Reproductive Hormone",
            "instruction": "Match each hormone to its source and main function.",
            "pairs": [
                ("FSH", "From pituitary — causes egg to mature in follicle, stimulates oestrogen production"),
                ("Oestrogen", "From ovaries — repairs uterus lining, triggers LH surge at high levels"),
                ("LH", "From pituitary — surge at Day ~14 triggers ovulation"),
                ("Progesterone", "From corpus luteum — maintains uterus lining in second half of cycle"),
                ("Testosterone", "From testes — causes male secondary sexual characteristics and sperm production"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Which hormone triggers ovulation?",
                "opts": [
                    ("LH (Luteinising Hormone) — a surge at around Day 14 releases the egg from the follicle", True),
                    ("FSH — it stimulates the follicle to release the egg", False),
                    ("Oestrogen — high oestrogen directly causes egg release", False),
                    ("Progesterone — it relaxes the follicle wall to release the egg", False)
                ],
                "wrong_explanations": {
                    1: "FSH stimulates EGG MATURATION — it prepares the follicle but doesn't trigger the release. The LH SURGE causes ovulation.",
                    2: "High oestrogen causes the RELEASE OF LH from the pituitary — it's the subsequent LH surge that triggers ovulation, not oestrogen directly.",
                    3: "Progesterone is produced AFTER ovulation by the corpus luteum — it maintains the uterus lining. It does not trigger ovulation."
                }
            },
            {
                "q": "What happens to progesterone levels if fertilisation does NOT occur?",
                "opts": [
                    ("Progesterone falls — the uterus lining breaks down — menstruation begins and the cycle restarts", True),
                    ("Progesterone rises — signalling the body to prepare for pregnancy anyway", False),
                    ("Progesterone stays the same indefinitely until the next menstrual cycle", False),
                    ("Progesterone triggers FSH release to immediately start a new cycle", False)
                ],
                "wrong_explanations": {
                    1: "Progesterone rising would signal PREGNANCY — which hasn't occurred. Without an embryo producing hormones, the corpus luteum degenerates and progesterone falls.",
                    2: "Progesterone cannot stay elevated indefinitely — the corpus luteum degenerates after about 14 days without an embryo implanting.",
                    3: "FSH is released at the start of a new cycle as progesterone falls — but it is oestrogen and progesterone levels, not progesterone directly stimulating FSH."
                }
            },
            {
                "q": "What is the role of oestrogen in the menstrual cycle?",
                "opts": [
                    ("Repairs and thickens the uterus lining after menstruation — also triggers the LH surge at high levels", True),
                    ("Triggers ovulation directly at low concentrations", False),
                    ("Maintains the uterus lining in the second half of the cycle", False),
                    ("Stimulates egg maturation in the follicle", False)
                ],
                "wrong_explanations": {
                    1: "Oestrogen at HIGH concentrations triggers LH release, and LH causes ovulation — but at LOW concentrations, oestrogen inhibits FSH, not triggers ovulation.",
                    2: "Maintaining the uterus lining in the second half = PROGESTERONE. Oestrogen rebuilds it in the first half.",
                    3: "Stimulating egg maturation = FSH. Oestrogen is produced AS A RESULT of FSH stimulation, not a cause of egg maturation."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 8. CONTRACEPTION AND FERTILITY TREATMENT
    # ══════════════════════════════════════════════
    {
        "id": "contraception-fertility",
        "title": "Contraception and Fertility Treatment",
        "spec": "4.5.4",
        "summary": "Describe methods of contraception and fertility treatments including IVF.",
        "theory": [
            {
                "heading": "Methods of Contraception",
                "content": "Contraception prevents pregnancy by interfering with fertilisation, ovulation or implantation.\n\nHORMONAL METHODS — prevent ovulation:\nCOMBINED PILL — contains oestrogen and progesterone. Oestrogen inhibits FSH production → no egg maturation → no ovulation. Taken daily.\nPROGESTERONE-ONLY PILL (mini-pill) — thickens cervical mucus (stops sperm reaching egg) and may also prevent ovulation.\nIMPLANT — small rod inserted under skin of upper arm, releases progesterone for up to 3 years. Prevents ovulation.\nINJECTION — progesterone injected every 8–12 weeks. Prevents ovulation.\nHORMONAL IUD (Mirena coil) — releases progesterone locally in the uterus.\n\nBARRIER METHODS — prevent sperm reaching the egg:\nMALE CONDOM — placed over the penis. ALSO protects against STIs — the only contraceptive that does this.\nFEMALE CONDOM — inserted into the vagina. Also protects against STIs.\nDIAPHRAGM — placed over the cervix before sex.\n\nNON-HORMONAL:\nCOPPER IUD (copper coil) — T-shaped device placed in the uterus. Copper ions are toxic to sperm. No hormones involved.\n\nSURGICAL (permanent):\nVASECTOMY — vas deferens cut or tied in males → sperm cannot be released.\nTUBAL LIGATION — fallopian tubes cut or tied in females → eggs cannot reach the uterus."
            },
            {
                "heading": "Fertility Treatments",
                "content": "Some couples have difficulty conceiving naturally. Medical treatments can help.\n\nFSH AND LH TREATMENT (fertility drugs):\nWomen who don't ovulate regularly are prescribed FSH (and sometimes LH) to stimulate egg maturation and ovulation.\nRisk: can cause multiple eggs to mature at once → multiple pregnancy (twins, triplets).\n\nIN VITRO FERTILISATION (IVF):\n'In vitro' means 'in glass' — fertilisation takes place in a laboratory dish, outside the body.\n\nThe IVF process:\n1. The woman is given FSH (and LH) to stimulate the ovaries to produce multiple eggs.\n2. Eggs are collected from the ovaries using a fine needle under sedation.\n3. Eggs are mixed with sperm in a laboratory dish — fertilisation occurs.\n4. Embryos develop for 2–5 days in the laboratory.\n5. One or two embryos are placed into the woman's uterus through the cervix.\n6. Progesterone is given to help maintain the uterus lining for implantation.\n7. If an embryo implants successfully, pregnancy begins.\n\nSuccess rates: approximately 30–40% per cycle for women under 35, declining with age."
            },
            {
                "heading": "Ethical Considerations",
                "content": "Both contraception and fertility treatment raise important ethical questions.\n\nCONTRACEPTION:\nSome religious groups oppose artificial contraception (e.g. the Catholic Church teaches natural family planning only).\nEmergency contraception ('morning-after pill') is controversial — some consider it preventing implantation of a fertilised egg.\nCondoms are widely supported as they also prevent spread of STIs.\n\nFERTILITY TREATMENT (IVF):\nMultiple embryos are often created — unused embryos may be frozen, destroyed or donated to research. This raises questions about the moral status of embryos.\nPre-implantation genetic diagnosis (PGD) — testing embryos for genetic conditions before implantation. Raises concerns about 'designer babies'.\nIVF is expensive — raises questions about who should have access.\nThe physical and emotional burden on women undergoing IVF is significant.\nDonor eggs or sperm raise questions about identity and donor anonymity."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "The contraceptive pill does NOT protect against STIs — only BARRIER METHODS (condoms) protect against both pregnancy AND sexually transmitted infections. The combined pill prevents OVULATION by inhibiting FSH — without ovulation, there is no egg to fertilise. In IVF, FSH is given to stimulate MULTIPLE egg production — not to help with implantation (progesterone does that).",
        "key_note": "Hormonal contraception: prevents ovulation (pill, implant, injection). Barrier methods: prevent sperm reaching egg, ALSO prevent STIs. IVF: FSH → multiple eggs → fertilised in lab → embryo implanted. Copper IUD: no hormones, sperm toxic.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Contraceptive to its Mechanism",
            "instruction": "Match each method to how it prevents pregnancy.",
            "pairs": [
                ("Combined pill", "Contains oestrogen — inhibits FSH → prevents egg maturation and ovulation"),
                ("Male condom", "Barrier method — stops sperm reaching egg — ALSO prevents STIs"),
                ("Copper IUD", "Copper ions are toxic to sperm — no hormones involved"),
                ("Implant", "Releases progesterone under the skin for up to 3 years — prevents ovulation"),
                ("Vasectomy", "Cuts the vas deferens — sperm cannot be released during ejaculation"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Which contraceptive method ALSO protects against sexually transmitted infections?",
                "opts": [
                    ("Condoms (male or female) — barrier methods prevent both pregnancy and STI transmission", True),
                    ("The combined contraceptive pill", False),
                    ("The copper IUD", False),
                    ("The contraceptive implant", False)
                ],
                "wrong_explanations": {
                    1: "The pill prevents pregnancy hormonally but does not prevent STI transmission — pathogens can still be exchanged.",
                    2: "The copper IUD works inside the uterus — it doesn't prevent STI transmission during sexual contact.",
                    3: "The implant prevents ovulation — it provides no barrier against pathogen transmission."
                }
            },
            {
                "q": "In IVF, why is FSH given to the woman at the start of treatment?",
                "opts": [
                    ("To stimulate the ovaries to produce multiple eggs so more can be collected and fertilised", True),
                    ("To prepare the uterus lining for embryo implantation", False),
                    ("To prevent the immune system from rejecting the embryo", False),
                    ("To fertilise the eggs in the laboratory", False)
                ],
                "wrong_explanations": {
                    1: "Preparing the uterus lining for implantation = PROGESTERONE — given later in IVF treatment. FSH specifically stimulates egg production.",
                    2: "Immune suppression is managed separately — FSH is specifically a reproductive hormone that drives follicle development and egg production.",
                    3: "Fertilisation is done by adding sperm to eggs in a laboratory dish — FSH is a hormone, not a fertilisation agent."
                }
            },
            {
                "q": "How does the combined contraceptive pill prevent pregnancy?",
                "opts": [
                    ("The oestrogen it contains inhibits FSH production — no FSH means no egg maturation and no ovulation", True),
                    ("It thickens the cervical mucus so sperm cannot swim through", False),
                    ("It prevents sperm from entering the vagina during sex", False),
                    ("It causes the uterus lining to shed more frequently", False)
                ],
                "wrong_explanations": {
                    1: "Thickening cervical mucus = PROGESTERONE-ONLY PILL (mini-pill). The COMBINED pill works primarily by suppressing ovulation through oestrogen inhibiting FSH.",
                    2: "Preventing sperm entering = BARRIER METHODS (condoms, diaphragm). The pill has no physical barrier effect.",
                    3: "The combined pill actually STABILISES the uterus lining — frequent shedding would be a side effect of other hormone imbalances, not the pill's mechanism."
                }
            }
        ]
    },
],

"inheritance": [


    # ══════════════════════════════════════════════
    # 1. SEXUAL AND ASEXUAL REPRODUCTION
    # ══════════════════════════════════════════════
    {
        "id": "sexual-asexual-reproduction",
        "title": "Sexual and Asexual Reproduction",
        "spec": "4.6.1",
        "summary": "Compare sexual and asexual reproduction and explain the role of meiosis in sexual reproduction.",
        "theory": [
            {
                "heading": "Asexual Reproduction",
                "content": "ASEXUAL REPRODUCTION involves only ONE parent organism — no gametes (sex cells) are involved.\n\nNew offspring are produced by MITOSIS — cell division that creates genetically IDENTICAL copies of the parent.\n\nOffspring from asexual reproduction are called CLONES — they are genetically identical to the parent and to each other.\n\nADVANTAGES:\nFast — large numbers of offspring can be produced very quickly.\nNo mate needed — energy efficient.\nAll offspring are well-adapted if the parent is well-adapted to its environment.\nUseful in stable environments where the parent's traits are advantageous.\n\nDISADVANTAGES:\nNo genetic variation — all offspring identical.\nIf the environment changes or a new disease emerges, ALL offspring are equally vulnerable.\nCannot adapt to new conditions.\n\nEXAMPLES: Bacteria (binary fission), plants via runners (strawberries), bulbs (daffodils), tubers (potatoes), budding (hydra), some fungi."
            },
            {
                "heading": "Sexual Reproduction",
                "content": "SEXUAL REPRODUCTION involves TWO parent organisms — each contributes a GAMETE (sex cell).\n\nGametes are produced by MEIOSIS — a special type of cell division that HALVES the chromosome number.\n\nFERTILISATION: a male gamete and female gamete FUSE to form a ZYGOTE (fertilised egg), restoring the full chromosome number.\n\nBecause DNA from TWO different individuals is combined, offspring are genetically DIFFERENT from both parents and from each other.\n\nADVANTAGES:\nCreates genetic VARIATION — offspring differ from parents and from each other.\nVariation means some offspring may be better adapted if the environment changes.\nDrives EVOLUTION — natural selection can act on the variation produced.\n\nDISADVANTAGES:\nRequires two parents — time and energy needed to find a mate.\nSlower — fewer offspring produced.\nSome offspring may inherit unfavourable gene combinations."
            },
            {
                "heading": "Meiosis — Producing Gametes",
                "content": "MEIOSIS is the type of cell division used to produce gametes (sperm, eggs, pollen).\n\nStarting cell: a body cell with 46 chromosomes (23 pairs).\n\nIn meiosis:\nThe chromosome number is HALVED — each gamete receives 23 chromosomes (one from each pair).\nFOUR daughter cells are produced.\nEach daughter cell is GENETICALLY DIFFERENT from the others.\n\nWHY halve the chromosome number? When two gametes fuse at fertilisation, 23 + 23 = 46 — restoring the correct number. If gametes had 46 chromosomes each, the offspring would have 92 — doubling every generation.\n\nGenetic variation in meiosis arises because:\nChromosomes are shuffled before dividing (independent assortment).\nSections of chromosomes can be exchanged between homologous pairs (crossing over).\nThis means every gamete has a unique combination of alleles."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "MITOSIS produces IDENTICAL cells (used for growth and repair). MEIOSIS produces GAMETES with HALF the chromosome number — and they are genetically different from each other. Students often confuse these two. Remember: MEiosis → gamEtes. Mitosis → most body cells.",
        "key_note": "Asexual: 1 parent, mitosis, clones, fast, no variation. Sexual: 2 parents, meiosis + fertilisation, variation, drives evolution. Meiosis halves chromosome number: 46 → 23. Fertilisation restores: 23 + 23 = 46.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Sexual or Asexual Reproduction?",
            "instruction": "Sort each feature into sexual or asexual reproduction.",
            "pairs": [
                ("Asexual", "Offspring are genetically identical clones of the parent — produced by mitosis"),
                ("Sexual", "Involves fusion of gametes — offspring are genetically different from both parents"),
                ("Asexual", "Only one parent needed — fast, energy efficient"),
                ("Sexual", "Creates genetic variation — allows populations to adapt and evolve"),
                ("Sexual", "Gametes produced by meiosis — chromosome number halved"),
                ("Asexual", "Strawberry plants reproducing via runners — all offspring identical"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the main genetic advantage of sexual reproduction over asexual reproduction?",
                "opts": [
                    ("It creates genetic variation — offspring differ from parents, allowing adaptation to changing environments", True),
                    ("It is faster — more offspring are produced in less time", False),
                    ("Only one parent is needed — saving time and energy", False),
                    ("All offspring are perfectly adapted — no risk of poor survival", False)
                ],
                "wrong_explanations": {
                    1: "ASEXUAL reproduction is faster — producing large numbers of identical offspring quickly. Sexual reproduction is slower but creates variation.",
                    2: "Requiring only ONE parent = ASEXUAL reproduction. Sexual reproduction needs two parents.",
                    3: "It is ASEXUAL reproduction where all offspring are identical clones of a well-adapted parent. Sexual reproduction means offspring vary."
                }
            },
            {
                "q": "Why does meiosis halve the chromosome number?",
                "opts": [
                    ("So that when two gametes fuse at fertilisation, the offspring has the correct number (46) and not double (92)", True),
                    ("To create more genetic variation by reducing the number of genes", False),
                    ("Because cells with fewer chromosomes divide more easily", False),
                    ("Meiosis does not halve chromosome number — it doubles it", False)
                ],
                "wrong_explanations": {
                    1: "Fewer chromosomes do allow more combinations, but the PRIMARY reason for halving is to prevent the chromosome number doubling each generation.",
                    2: "Cell division speed is not the biological reason — the function is specifically to allow fertilisation to restore the correct diploid number.",
                    3: "Meiosis HALVES chromosome number (46 → 23). Doubling occurs at fertilisation when two haploid gametes combine to make a diploid zygote."
                }
            },
            {
                "q": "Bacteria reproduce by binary fission — splitting into two identical cells. What type of reproduction is this?",
                "opts": [
                    ("Asexual reproduction — one parent, offspring are genetically identical clones", True),
                    ("Sexual reproduction — two bacteria combine to share genetic material", False),
                    ("Meiosis — the chromosome number is halved in each new bacterium", False),
                    ("Fertilisation — two gametes fuse to form a new bacterium", False)
                ],
                "wrong_explanations": {
                    1: "Some bacteria do exchange genetic material (conjugation) — but binary fission specifically produces identical copies from one parent. It is asexual.",
                    2: "Binary fission produces identical cells from ONE parent — it does not involve halving chromosome numbers. Bacteria are haploid anyway.",
                    3: "Gametes are specialised sex cells — bacteria don't produce gametes in binary fission."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 2. DNA AND THE GENOME
    # ══════════════════════════════════════════════
    {
        "id": "dna-genome",
        "title": "DNA and the Genome",
        "spec": "4.6.2",
        "summary": "Describe the structure of DNA, what genes are, and what the human genome project achieved.",
        "theory": [
            {
                "heading": "DNA Structure",
                "content": "DNA (Deoxyribonucleic Acid) is the molecule that carries genetic information in all living organisms.\n\nDNA is a POLYMER made of repeating units called NUCLEOTIDES.\n\nEach nucleotide contains:\nA deoxyribose SUGAR.\nA PHOSPHATE group.\nOne of four BASES: Adenine (A), Thymine (T), Cytosine (C) or Guanine (G).\n\nTwo strands of nucleotides wind around each other to form the famous DOUBLE HELIX — like a twisted ladder.\n\nThe strands are held together by hydrogen bonds between complementary BASE PAIRS:\nA always pairs with T (adenine — thymine).\nC always pairs with G (cytosine — guanine).\n\nThis base pairing rule (A-T, C-G) is fundamental — it allows DNA to be replicated accurately before cell division."
            },
            {
                "heading": "Genes and Chromosomes",
                "content": "A GENE is a specific sequence of DNA bases that codes for the production of a specific PROTEIN.\n\nThe sequence of bases in a gene determines the sequence of AMINO ACIDS in a protein — different base sequences produce different proteins with different functions.\n\nGenes are located on CHROMOSOMES — long, tightly coiled DNA molecules.\n\nHumans have 46 chromosomes arranged as 23 PAIRS. One chromosome in each pair came from the mother; one from the father.\n\nEach chromosome contains thousands of genes — there are approximately 20,000–25,000 protein-coding genes in the human genome.\n\nALLELES are different versions of the same gene, caused by slightly different base sequences at the same position on homologous chromosomes."
            },
            {
                "heading": "The Human Genome",
                "content": "The GENOME is the complete set of genetic information in an organism — every gene in every chromosome.\n\nThe HUMAN GENOME PROJECT was an international scientific collaboration that:\nRan from 1990 to 2003.\nMapped and sequenced all approximately 3 BILLION base pairs of the human genome.\nIdentified the location and sequence of all human genes.\n\nWhy it matters:\nIdentifying genes linked to INHERITED DISEASES — e.g. BRCA1/2 (breast cancer risk), cystic fibrosis gene.\nDeveloping PERSONALISED MEDICINE — treatments tailored to an individual's genetic make-up.\nUnderstanding HUMAN EVOLUTION and our relationship to other species.\nForensic science — DNA profiling to identify individuals.\nUnderstanding gene function in health and disease."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A GENE is not the same as a CHROMOSOME. A chromosome contains THOUSANDS of genes. The GENOME is the COMPLETE set of ALL genetic information — all genes on all chromosomes. Base pairing: A pairs with T only. C pairs with G only. Never A-G or C-T.",
        "key_note": "DNA = double helix. A-T and C-G base pairs. Gene = section of DNA coding for a protein. Chromosome = contains thousands of genes. Genome = complete genetic information of an organism. Human genome: ~20,000 genes, ~3 billion base pairs.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "DNA and Genome Vocabulary",
            "instruction": "Match each term to its correct definition.",
            "pairs": [
                ("Nucleotide", "The monomer unit of DNA — contains a sugar, phosphate and one base"),
                ("Gene", "A specific sequence of DNA bases that codes for a particular protein"),
                ("Chromosome", "A long coiled DNA molecule — contains thousands of genes"),
                ("Allele", "A different version of the same gene — slightly different base sequence"),
                ("Genome", "The complete set of genetic information in an organism"),
                ("Base pairing", "A always pairs with T; C always pairs with G — holds DNA strands together"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "In DNA, which bases pair together?",
                "opts": [
                    ("A with T, and C with G", True),
                    ("A with G, and C with T", False),
                    ("A with C, and G with T", False),
                    ("All four bases pair randomly", False)
                ],
                "wrong_explanations": {
                    1: "Wrong pairing — A pairs with T (2 hydrogen bonds) and C pairs with G (3 hydrogen bonds). A-G pairings do not occur.",
                    2: "Wrong pairing — A-C and G-T pairings do not occur in DNA. Base pairing is strictly A-T and C-G.",
                    3: "Base pairing in DNA is NOT random — it is strictly determined by molecular structure. A-T and C-G only."
                }
            },
            {
                "q": "What is a gene?",
                "opts": [
                    ("A specific sequence of DNA bases that codes for a particular protein", True),
                    ("A complete chromosome containing all the genetic information", False),
                    ("A unit of heredity that controls physical appearance only", False),
                    ("Any section of DNA — all DNA constitutes genes", False)
                ],
                "wrong_explanations": {
                    1: "A complete chromosome contains thousands of genes — it is not itself a gene.",
                    2: "Genes code for proteins, which then influence characteristics — but genes control far more than physical appearance (e.g. enzyme production, cell signalling).",
                    3: "Not all DNA codes for proteins — a significant portion of the genome is non-coding DNA. Genes are specifically the protein-coding sequences."
                }
            },
            {
                "q": "What was the Human Genome Project?",
                "opts": [
                    ("An international project that sequenced all ~3 billion base pairs of human DNA and mapped all human genes", True),
                    ("A project to create genetically modified humans with improved characteristics", False),
                    ("A database of all known genetic diseases and their cures", False),
                    ("A study comparing the DNA of humans to chimpanzees", False)
                ],
                "wrong_explanations": {
                    1: "The Human Genome Project was about SEQUENCING and MAPPING the genome — not about genetically modifying humans.",
                    2: "While comparisons with other species were made using genome data, the primary goal was mapping and sequencing the HUMAN genome itself.",
                    3: "While the HGP has helped identify disease genes, it was a mapping and sequencing project — not a medical treatment database."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 3. GENETIC INHERITANCE
    # ══════════════════════════════════════════════
    {
        "id": "genetic-inheritance",
        "title": "Genetic Inheritance",
        "spec": "4.6.3",
        "summary": "Explain dominant and recessive inheritance and use Punnett squares to predict offspring ratios.",
        "theory": [
            {
                "heading": "Alleles — Dominant and Recessive",
                "content": "Each individual has TWO copies of most genes — one on each chromosome of a homologous pair. These copies may be the same allele or different alleles.\n\nDOMINANT allele:\nExpressed in the phenotype (physical characteristic) even if ONLY ONE COPY is present.\nWritten as a CAPITAL letter (e.g. B for brown eyes).\n\nRECESSIVE allele:\nOnly expressed if TWO COPIES are present — hidden by dominant allele if only one copy exists.\nWritten as a LOWERCASE letter (e.g. b for blue eyes).\n\nGENOTYPE — the alleles an organism has (e.g. BB, Bb, bb).\nPHENOTYPE — the observable characteristic expressed (e.g. brown eyes, blue eyes).\n\nHOMOZYGOUS — both alleles are the same (BB or bb).\nHETEROZYGOUS — alleles are different (Bb).\n\nCARRIER — an individual with one recessive allele that is not expressed (Bb). They appear normal but can pass the recessive allele to offspring."
            },
            {
                "heading": "Using Punnett Squares",
                "content": "A PUNNETT SQUARE is a grid used to predict the probability of offspring genotypes and phenotypes from a genetic cross.\n\nHow to draw one:\n1. Write the alleles of one parent across the top.\n2. Write the alleles of the other parent down the side.\n3. Fill in each box by combining the alleles from the row and column.\n4. The boxes show all possible offspring genotypes.\n\nEXAMPLE — Heterozygous cross (Bb × Bb):\n\nParents: Bb × Bb\nOffspring genotypes: BB, Bb, Bb, bb\nRatio: 1 BB : 2 Bb : 1 bb\nPhenotype ratio: 3 dominant (BB and Bb) : 1 recessive (bb)\nSo 75% show dominant phenotype, 25% show recessive phenotype.\n\nEXAMPLE — Carrier × Normal (Bb × BB):\nOffspring: BB, BB, Bb, Bb\nAll offspring show dominant phenotype — but 50% are carriers (Bb)."
            },
            {
                "heading": "Probability in Genetics",
                "content": "Punnett squares give us PROBABILITIES — the likelihood of each outcome, not a guarantee.\n\nIf a cross gives a 1 in 4 (25%) chance of an affected offspring, this means:\nEach pregnancy independently has a 25% chance.\nIt does NOT mean that exactly 1 in every 4 children will be affected.\nSmall sample sizes may not reflect the expected ratio.\n\nProbability can be expressed as:\nA fraction: 1/4.\nA percentage: 25%.\nA ratio: 1 in 4.\n\nGenetic counsellors use Punnett squares to advise couples on the risk of inherited conditions in their children."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A CARRIER (Bb) has the recessive allele but does NOT show the condition — they appear completely normal. Students often say carriers 'have the disease mildly' — this is WRONG. A carrier is phenotypically normal but genotypically heterozygous. Two carriers (Bb × Bb) have a 25% chance of an affected (bb) child.",
        "key_note": "Dominant (capital) = expressed with one copy. Recessive (lowercase) = needs two copies. Genotype = alleles present. Phenotype = observable trait. Homozygous = both same. Heterozygous = different. Carrier = Bb, appears normal.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Genetics Vocabulary",
            "instruction": "Match each genetics term to its correct definition.",
            "pairs": [
                ("Genotype", "The alleles present in an organism — e.g. Bb"),
                ("Phenotype", "The observable characteristic — e.g. brown eyes"),
                ("Homozygous", "Both alleles are the same — e.g. BB or bb"),
                ("Heterozygous", "Alleles are different — e.g. Bb"),
                ("Dominant allele", "Expressed in the phenotype even if only one copy is present"),
                ("Carrier", "Heterozygous individual with one recessive allele — appears normal but can pass it on"),
            ]
        },
        "fifas": [
            {
                "label": "Punnett Square — Heterozygous Cross",
                "question": "Two parents are both heterozygous for brown eyes (Bb). Brown (B) is dominant over blue (b). Calculate the probability of a child having blue eyes.",
                "steps": [
                    ("F", "Draw a Punnett square: Bb × Bb"),
                    ("I", "Offspring: BB, Bb, Bb, bb → genotype ratio 1:2:1"),
                    ("F", "Only bb gives blue eyes (recessive phenotype) = 1 out of 4"),
                    ("A", "Probability of blue eyes = 1/4 = 25%")
                ]
            }
        ],
        "quiz": [
            {
                "q": "In a Bb × Bb cross, what fraction of offspring will show the RECESSIVE phenotype?",
                "opts": [
                    ("1/4 (25%)", True),
                    ("1/2 (50%)", False),
                    ("3/4 (75%)", False),
                    ("0 — recessive cannot appear from two heterozygous parents", False)
                ],
                "wrong_explanations": {
                    1: "50% occurs when one parent is homozygous recessive (bb × Bb). Two heterozygotes give 1 BB : 2 Bb : 1 bb → 25% recessive.",
                    2: "3/4 is the proportion showing the DOMINANT phenotype (BB and Bb). Only 25% (bb) show recessive.",
                    3: "Two heterozygous parents (Bb × Bb) absolutely CAN produce a recessive child — 25% chance (bb)."
                }
            },
            {
                "q": "A person is described as a 'carrier' of cystic fibrosis. What does this mean?",
                "opts": [
                    ("They have one recessive allele (Ff) — they appear healthy but can pass the allele to offspring", True),
                    ("They have the disease mildly — they have some symptoms but not severe ones", False),
                    ("They are homozygous recessive (ff) — they have the full condition", False),
                    ("They have been exposed to cystic fibrosis but their immune system fought it off", False)
                ],
                "wrong_explanations": {
                    1: "A carrier appears COMPLETELY NORMAL — there are no mild symptoms. Having one recessive allele (Ff) is masked by the dominant allele.",
                    2: "Homozygous recessive (ff) = HAS the condition. A carrier is HETEROZYGOUS (Ff) and does NOT have the condition.",
                    3: "Cystic fibrosis is a GENETIC condition — it is not an infection that can be 'fought off' by the immune system."
                }
            },
            {
                "q": "If a Punnett square shows a 1 in 4 chance of having an affected child, what does this mean for a couple?",
                "opts": [
                    ("Each pregnancy independently has a 25% chance of being affected — it does not mean exactly 1 in 4 children will be affected", True),
                    ("Exactly one child out of every four they have will be affected", False),
                    ("If their first three children are unaffected, the fourth will definitely be affected", False),
                    ("The chance reduces after each unaffected child — the probability changes", False)
                ],
                "wrong_explanations": {
                    1: "Probability is not a guarantee of exact outcomes — with only 4 children, you might have 0, 1, 2, 3 or even 4 affected children.",
                    2: "Each pregnancy is INDEPENDENT — the outcome of previous pregnancies does not affect future ones. This is like flipping a coin.",
                    3: "Probability doesn't 'accumulate' — each pregnancy always has the same 25% chance regardless of previous outcomes."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 4. INHERITED DISORDERS
    # ══════════════════════════════════════════════
    {
        "id": "inherited-disorders",
        "title": "Inherited Disorders",
        "spec": "4.6.3.2",
        "summary": "Describe cystic fibrosis and polydactyly as examples of inherited genetic disorders.",
        "theory": [
            {
                "heading": "Cystic Fibrosis",
                "content": "Cystic fibrosis (CF) is caused by a RECESSIVE allele — written as 'f' (faulty) while 'F' is the normal allele.\n\nGENOTYPES:\nFF — unaffected, not a carrier.\nFf — carrier — appears healthy but carries one copy of the faulty allele.\nff — affected — has cystic fibrosis.\n\nFor a child to have CF, they must inherit TWO recessive alleles — one from each parent.\nTwo carriers (Ff × Ff) have a 25% chance of an affected child per pregnancy.\n\nEFFECTS OF CYSTIC FIBROSIS:\nThe faulty allele affects a protein that controls the movement of salt and water across cell membranes.\nThis causes a build-up of THICK, STICKY MUCUS in:\nThe LUNGS — makes breathing difficult, blocks airways, traps bacteria → repeated chest infections → lung damage.\nThe DIGESTIVE SYSTEM — blocks ducts from the pancreas → digestive enzymes cannot reach the gut → poor absorption of nutrients.\n\nTREATMENT: physiotherapy to loosen mucus, antibiotics for infections, enzyme supplements with food. No cure (though gene therapy is in development).\n\nCF is the most common serious inherited disorder in the UK — approximately 1 in 25 people carry the allele."
            },
            {
                "heading": "Polydactyly",
                "content": "Polydactyly is caused by a DOMINANT allele — written as 'D' while 'd' is the normal allele.\n\nGENOTYPES:\nDD — affected (rare — very few people have two copies of the dominant allele).\nDd — affected — only ONE copy needed to show the condition.\ndd — unaffected.\n\nA person with polydactyly has one or more EXTRA FINGERS OR TOES.\n\nBecause the allele is DOMINANT:\nOnly ONE copy is needed — so an affected parent (Dd) has a 50% chance of passing the condition to each child.\nThe condition appears in EVERY GENERATION that carries the allele.\nAn affected person has at least one affected parent (unless it arose from a new mutation).\n\nPolydactyly is not life-threatening and can be surgically corrected.\n\nKEY CONTRAST with cystic fibrosis:\nCF = recessive — can skip generations (carriers appear normal).\nPolydactyly = dominant — appears in every generation that carries it."
            },
            {
                "heading": "Genetic Testing and Ethical Issues",
                "content": "GENETIC TESTING can identify whether a person carries alleles for inherited conditions.\n\nTypes of testing:\nPRE-CONCEPTION testing — couples who have a family history of a genetic condition can be tested to find out if they are carriers before having children.\nPRE-NATAL testing — testing the embryo or foetus during pregnancy. Methods: amniocentesis (sampling amniotic fluid), chorionic villus sampling (CVS — sampling placental tissue).\nNEWBORN SCREENING — blood spot test (heel prick) shortly after birth screens for several conditions including CF.\n\nETHICAL CONSIDERATIONS:\nPrivacy — who has access to genetic information? Could affect insurance or employment.\nDecision-making — if a foetus tests positive, should the pregnancy continue? Raises difficult ethical questions.\nPsychological impact — knowing you carry an allele for a serious condition causes anxiety.\nSocial stigma — discrimination against those known to have certain genetic profiles.\nThese are genuine ethical debates with no single correct answer — the key is to consider multiple perspectives."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Cystic fibrosis is RECESSIVE — both parents can be unaffected carriers. Polydactyly is DOMINANT — at least one parent will always be affected (unless it arose from a new mutation). Students often apply these rules the wrong way round. Remember: recessive conditions can SKIP GENERATIONS (via carriers). Dominant conditions CANNOT skip generations.",
        "key_note": "CF: recessive (ff), thick mucus in lungs and gut, 1 in 25 carriers in UK. Polydactyly: dominant (Dd), extra digits, appears every generation. Recessive can skip generations. Dominant cannot (unless new mutation).",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Cystic Fibrosis or Polydactyly?",
            "instruction": "Match each feature to the correct inherited disorder.",
            "pairs": [
                ("Cystic fibrosis", "Caused by a recessive allele — both copies needed for the condition to show"),
                ("Polydactyly", "Caused by a dominant allele — only one copy needed to show the condition"),
                ("Cystic fibrosis", "Causes thick sticky mucus in lungs and digestive system"),
                ("Polydactyly", "Causes extra fingers or toes — not life-threatening"),
                ("Cystic fibrosis", "Can skip generations — carriers appear healthy"),
                ("Polydactyly", "Appears in every generation — an affected person always has at least one affected parent"),
            ]
        },
        "fifas": [
            {
                "label": "CF Inheritance Cross",
                "question": "Two carriers for cystic fibrosis (Ff × Ff) are expecting a child. What is the probability the child will have CF?",
                "steps": [
                    ("F", "Draw Punnett square: Ff × Ff. CF allele = f (recessive). Normal = F"),
                    ("I", "Offspring: FF, Ff, Ff, ff → ratio 1:2:1"),
                    ("F", "Only ff has cystic fibrosis = 1 out of 4 boxes"),
                    ("A", "Probability of CF = 1/4 = 25%")
                ]
            }
        ],
        "quiz": [
            {
                "q": "Both parents appear healthy but have a child with cystic fibrosis. What must be true of the parents?",
                "opts": [
                    ("Both parents are carriers — genotype Ff — they have one copy of the recessive allele each", True),
                    ("One parent must have cystic fibrosis but is hiding it", False),
                    ("The child developed CF through a random environmental mutation", False),
                    ("The parents must be closely related — CF only occurs in related families", False)
                ],
                "wrong_explanations": {
                    1: "CF is a genetic condition — you cannot 'hide' it. If a parent had CF (ff) they would have serious symptoms.",
                    2: "CF is caused by inheriting TWO recessive alleles — both alleles must come from parents. The parents must both be carriers (Ff).",
                    3: "While CF is more common in some populations, it is not caused by family relatedness — it requires two carriers regardless of family relationship."
                }
            },
            {
                "q": "Why does polydactyly appear in every generation, while cystic fibrosis can skip generations?",
                "opts": [
                    ("Polydactyly is dominant — one copy is enough to show it. CF is recessive — carriers (Ff) appear normal and don't show it.", True),
                    ("Polydactyly is caused by a different chromosome than cystic fibrosis", False),
                    ("Cystic fibrosis is more severe so the body suppresses it in some generations", False),
                    ("Polydactyly affects more people so it appears more often", False)
                ],
                "wrong_explanations": {
                    1: "The chromosomal location of a gene is irrelevant to whether the condition skips generations — it's the dominant/recessive nature that matters.",
                    2: "The body doesn't suppress genetic conditions — whether a condition shows depends entirely on genotype and allele dominance.",
                    3: "Prevalence doesn't determine whether a condition skips generations — dominance/recessiveness does."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 5. SEX DETERMINATION
    # ══════════════════════════════════════════════
    {
        "id": "sex-determination",
        "title": "Sex Determination",
        "spec": "4.6.3.3",
        "summary": "Explain how biological sex is determined by the X and Y chromosomes.",
        "theory": [
            {
                "heading": "Sex Chromosomes",
                "content": "In humans, biological sex is determined by a pair of SEX CHROMOSOMES — one of the 23 pairs of chromosomes.\n\nFEMALES: XX — two X chromosomes.\nMALES: XY — one X chromosome and one Y chromosome.\n\nThe Y chromosome is smaller than the X chromosome and contains fewer genes. It carries the genes responsible for male development, including the SRY gene which triggers the development of testes.\n\nAll other 22 chromosome pairs are called AUTOSOMES — they are the same in males and females."
            },
            {
                "heading": "How Sex is Determined at Fertilisation",
                "content": "All eggs produced by a female contain ONE X chromosome (since females are XX).\n\nSperm produced by a male contain EITHER:\nan X chromosome (approximately 50% of sperm), OR\na Y chromosome (approximately 50% of sperm).\n\nAt fertilisation:\nIf an X-bearing sperm fertilises the egg: XX → FEMALE.\nIf a Y-bearing sperm fertilises the egg: XY → MALE.\n\nTherefore: the SPERM determines the biological sex of the offspring — not the egg.\n\nProbability: 50% chance of a female child, 50% chance of a male child in each pregnancy."
            },
            {
                "heading": "Punnett Square for Sex Determination",
                "content": "We can use a Punnett square to show sex determination:\n\nMother (XX) × Father (XY)\n\nSperm: X or Y (50/50)\nEggs: X only (100%)\n\nOffspring:\nXX = female (50%)\nXY = male (50%)\n\nThis shows why the sex ratio in human populations is approximately 50:50.\n\nKey point: the sex of a child is determined RANDOMLY at fertilisation — it cannot be predicted in advance for a specific pregnancy. The 50:50 ratio is the probability, not a guarantee for any given family."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "It is the SPERM that determines the sex of the child — not the egg. All eggs contain an X chromosome. Sperm can contain either X or Y. If a Y-carrying sperm fertilises the egg, the child is male (XY). Historically, women were sometimes blamed for not producing sons — this is biologically incorrect.",
        "key_note": "Female = XX. Male = XY. All eggs carry X. Sperm carry X or Y (50/50). Y-sperm → male (XY). X-sperm → female (XX). Sex determined at fertilisation by which sperm fertilises the egg. 50% probability each time.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Sex Determination Match",
            "instruction": "Match each statement to the correct sex chromosome fact.",
            "pairs": [
                ("Female", "Has sex chromosomes XX — both are X chromosomes"),
                ("Male", "Has sex chromosomes XY — one X and one smaller Y chromosome"),
                ("All eggs", "Contain one X chromosome — females are XX so can only pass on X"),
                ("Sperm", "Contain either X or Y — determines the sex of the offspring"),
                ("50%", "Probability of a male offspring — same as probability of female offspring"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What determines the biological sex of a human offspring?",
                "opts": [
                    ("Which type of sperm (X or Y) fertilises the egg — Y-sperm → male, X-sperm → female", True),
                    ("The egg — females produce X and Y eggs, one type producing a boy and the other a girl", False),
                    ("The environment during pregnancy — temperature affects sex", False),
                    ("The age of the parents — older parents are more likely to have girls", False)
                ],
                "wrong_explanations": {
                    1: "Females (XX) can only produce X-bearing eggs — all eggs contain X. It is the SPERM that carries either X or Y.",
                    2: "Temperature does affect sex determination in some reptiles — but in humans, sex is determined genetically by which sperm fertilises the egg.",
                    3: "Parental age can affect fertility and some genetic risks — but does not determine sex."
                }
            },
            {
                "q": "A couple have three daughters. What is the probability their next child will be a son?",
                "opts": [
                    ("50% — each pregnancy is independent, the sex ratio is always 50:50", True),
                    ("Higher than 50% — after three girls they are 'due' a boy", False),
                    ("Lower than 50% — this couple clearly produce more girls than boys", False),
                    ("0% — if they have had three girls their sperm cannot produce Y chromosomes", False)
                ],
                "wrong_explanations": {
                    1: "Each pregnancy is INDEPENDENT — like flipping a coin, the outcomes of previous pregnancies have no effect. This is a common misconception known as the gambler's fallacy.",
                    2: "Having three girls does not indicate a bias — small sample sizes often show runs of one outcome by chance. Males produce X and Y sperm equally.",
                    3: "Males always produce roughly 50% X-bearing and 50% Y-bearing sperm — three daughters doesn't change this."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 6. VARIATION
    # ══════════════════════════════════════════════
    {
        "id": "variation",
        "title": "Variation",
        "spec": "4.6.4",
        "summary": "Describe the causes of variation and distinguish between genetic, environmental and combination variation.",
        "theory": [
            {
                "heading": "What is Variation?",
                "content": "VARIATION refers to the differences in characteristics between individuals of the same species.\n\nVariation is absolutely essential for life on Earth:\nIt is the raw material on which NATURAL SELECTION acts.\nWithout variation, all individuals would be identical and no evolutionary change would be possible.\nVariation allows populations to adapt to changing environments.\n\nVariation can be:\nCONTINUOUS — characteristics that show a range of values with no distinct categories (e.g. height, weight, skin colour).\nDISCONTINUOUS — characteristics that fall into distinct categories with no in-between values (e.g. blood group A, B, AB or O; tongue rolling ability; ability to taste PTC)."
            },
            {
                "heading": "Causes of Variation",
                "content": "Variation arises from three main sources:\n\n1. GENETIC VARIATION:\nDifferences in DNA sequences between individuals.\nArises through: MUTATIONS (random changes in DNA sequence), MEIOSIS (shuffling of chromosomes and crossing over), SEXUAL REPRODUCTION (combining DNA from two parents).\nGenetic variation is INHERITED — passed from parents to offspring.\n\n2. ENVIRONMENTAL VARIATION:\nDifferences caused by conditions an organism experiences during its lifetime.\nExamples: height (affected by nutrition during childhood), skin colour (affected by sun exposure), language spoken (learned from environment), scars and injuries.\nEnvironmental variation is NOT inherited — you cannot pass on a learned language or a scar to your offspring.\n\n3. COMBINATION OF BOTH:\nMany characteristics are influenced by BOTH genes AND environment.\nExamples: height (genes set the potential maximum; nutrition determines whether that potential is reached), body weight (genes influence metabolism; diet and exercise are environmental), skin colour (genes determine base colour; UV exposure adds a tan)."
            },
            {
                "heading": "Mutations",
                "content": "A MUTATION is a change in the sequence of DNA bases in a gene or chromosome.\n\nMutations can be:\nSpontaneous — occurring randomly during DNA replication (copying errors).\nInduced — caused by MUTAGENS: chemicals (e.g. carcinogens in tobacco smoke), radiation (UV, gamma rays, X-rays), certain viruses.\n\nEffects of mutations:\nMost mutations are NEUTRAL — they occur in non-coding DNA or don't change the protein significantly.\nSome mutations are HARMFUL — they alter a protein so it cannot function properly (e.g. mutations causing cystic fibrosis, sickle cell disease).\nVery occasionally, a mutation is BENEFICIAL — it improves the function of a protein or produces a new useful function (e.g. mutations that gave early humans more efficient enzymes or better immune responses).\n\nBeneficial mutations are the ultimate source of all new variation in a species — they are the raw material on which natural selection acts."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Environmental variation is NOT inherited — you cannot pass your experiences, injuries or learned skills to your children through DNA. Genetic variation IS inherited. Most mutations are neutral — not harmful. Students often assume all mutations are dangerous, but the vast majority have no detectable effect.",
        "key_note": "Variation: continuous (range of values) or discontinuous (distinct categories). Causes: genetic (mutation, meiosis, sexual reproduction), environmental (nutrition, sun, learned). Many traits = combination of both. Mutations: neutral, harmful or rarely beneficial.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Genetic, Environmental or Both?",
            "instruction": "Match each example to the cause of variation.",
            "pairs": [
                ("Genetic", "Blood group — determined entirely by inherited alleles"),
                ("Environmental", "A scar from a childhood accident — not passed to offspring"),
                ("Both", "Height — genes set the maximum potential; nutrition determines if it is reached"),
                ("Environmental", "Language spoken — entirely learned from the surrounding environment"),
                ("Genetic", "Cystic fibrosis — caused by inheriting two copies of the recessive allele"),
                ("Both", "Body weight — metabolic rate is genetic; diet and exercise are environmental"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "A child is taller than expected given their parents' heights. What is the most likely cause?",
                "opts": [
                    ("A combination of genetic potential and favourable environmental factors — e.g. excellent nutrition during childhood", True),
                    ("A mutation that occurred during development, making the child taller", False),
                    ("The child inherited more height genes from distant ancestors than from parents", False),
                    ("Environmental factors alone — height is entirely determined by diet", False)
                ],
                "wrong_explanations": {
                    1: "A random mutation could theoretically increase height, but this is rare. The more likely explanation is that parents didn't reach their own genetic potential due to environmental factors.",
                    2: "Genes don't skip generations in this simple way — the child can only inherit alleles from their parents.",
                    3: "Height is strongly influenced by genetics — children of tall parents tend to be taller. But environmental factors (particularly nutrition) also play a significant role."
                }
            },
            {
                "q": "Which of the following is an example of DISCONTINUOUS variation?",
                "opts": [
                    ("Blood group — a person is type A, B, AB or O with no intermediate values", True),
                    ("Height — people range from very short to very tall with all values in between", False),
                    ("Body weight — a continuous range from very light to very heavy", False),
                    ("Skin colour — a continuous range from very light to very dark", False)
                ],
                "wrong_explanations": {
                    1: "Height is a classic example of CONTINUOUS variation — there is a smooth range from shortest to tallest with all intermediate heights present.",
                    2: "Body weight is CONTINUOUS — it forms a normal distribution curve across the population.",
                    3: "Skin colour is CONTINUOUS — determined by multiple genes and environmental factors (sun exposure), producing a smooth range of values."
                }
            },
            {
                "q": "What is a mutation?",
                "opts": [
                    ("A change in the sequence of DNA bases — can be neutral, harmful or rarely beneficial", True),
                    ("A change in an organism's body caused by the environment during its lifetime", False),
                    ("The process of chromosomes being shuffled during meiosis", False),
                    ("A genetic disease inherited from parents", False)
                ],
                "wrong_explanations": {
                    1: "Environmental changes to the body (like a tan or muscle growth) are not mutations — they are phenotypic responses that are not passed on through DNA.",
                    2: "Chromosome shuffling during meiosis = INDEPENDENT ASSORTMENT and CROSSING OVER — these create variation but are not mutations.",
                    3: "Inherited diseases are caused by specific alleles — mutations can create new alleles, but the inherited disease itself is not a mutation."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 7. EVOLUTION AND NATURAL SELECTION
    # ══════════════════════════════════════════════
    {
        "id": "evolution-natural-selection",
        "title": "Evolution and Natural Selection",
        "spec": "4.6.5",
        "summary": "Describe Darwin's theory of evolution by natural selection and explain how populations change over time.",
        "theory": [
            {
                "heading": "What is Evolution?",
                "content": "EVOLUTION is the change in the inherited characteristics of a population over many generations.\n\nIt is driven by natural selection — the process by which individuals with characteristics better suited to their environment are more likely to survive and reproduce.\n\nEvolution explains:\nWhy species change over time.\nWhy there are so many different species on Earth.\nWhy species share features with each other (common ancestry).\nWhy organisms are so well adapted to their environments.\n\nEvolution is the central organising principle of modern biology — it is one of the most well-supported theories in all of science, supported by evidence from fossils, genetics, anatomy and direct observation."
            },
            {
                "heading": "Darwin's Theory of Natural Selection",
                "content": "Charles DARWIN (1809–1882) developed the theory of natural selection after extensive observation of wildlife, particularly during his voyage on HMS Beagle (1831–1836).\n\nDarwin's theory in five steps:\n1. VARIATION — individuals within a population show differences in their characteristics.\n2. OVERPRODUCTION — populations produce more offspring than the environment can support.\n3. STRUGGLE FOR SURVIVAL — competition for resources (food, water, mates, territory). Not all offspring survive.\n4. SURVIVAL OF THE FITTEST — individuals with characteristics best adapted to the environment are more likely to SURVIVE and REPRODUCE.\n5. INHERITANCE — surviving individuals pass on their ALLELES to offspring. The next generation has more individuals with the advantageous characteristics.\n\nOver many generations → advantageous alleles become MORE COMMON in the population → the population changes → EVOLUTION has occurred."
            },
            {
                "heading": "Why Darwin's Theory Took Time to be Accepted",
                "content": "Darwin published his theory in 'On the Origin of Species' in 1859.\n\nIt was NOT immediately accepted — reasons include:\nReligious opposition — contradicted the biblical account of creation and the idea that species were fixed and created by God.\nLack of a mechanism — Darwin did not know HOW inheritance worked (DNA and genetics were not yet understood). He could not fully explain HOW traits were passed on.\nInsufficient evidence at the time — the fossil record had many gaps.\nDifficulty of the concept — evolution over millions of years is hard to observe directly.\n\nOver time, as genetics was discovered (first Mendel, then Watson and Crick with DNA structure), and as more fossil evidence accumulated, Darwin's theory gained overwhelming scientific support.\n\nToday, evolution by natural selection is the scientific consensus — one of the most strongly evidenced theories in science."
            },
            {
                "heading": "Alfred Russel Wallace",
                "content": "ALFRED RUSSEL WALLACE (1823–1913) independently developed a theory of evolution by natural selection at approximately the same time as Darwin.\n\nWallace sent his ideas to Darwin in 1858 — this prompted Darwin to publish his own work.\n\nBoth men's papers were presented to the Linnean Society of London in 1858.\n\nWallace made important contributions to biogeography — the study of how species are distributed across the Earth — and the patterns of species distribution supported the theory of evolution.\n\nHis work in Southeast Asia led to him identifying what is now called 'Wallace's line' — a boundary between Asian and Australian species distributions."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Natural selection does NOT cause mutations — mutations happen randomly. Natural selection SELECTS from variation that already exists. Also: individuals do NOT evolve — POPULATIONS evolve over many generations. And: 'survival of the fittest' does not mean 'strongest' — it means best adapted to the environment.",
        "key_note": "Evolution = change in inherited characteristics over generations. Darwin's steps: variation → overproduction → struggle for survival → survival of the fittest → inheritance. Natural selection acts on existing variation — it does not cause mutations.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Step of Natural Selection",
            "instruction": "Match each step of natural selection to its correct description.",
            "pairs": [
                ("Variation", "Individuals in a population show differences in their characteristics"),
                ("Overproduction", "More offspring are produced than the environment can support"),
                ("Struggle for survival", "Competition for resources — not all offspring survive"),
                ("Survival of the fittest", "Individuals best adapted to the environment are more likely to survive and reproduce"),
                ("Inheritance", "Surviving individuals pass on advantageous alleles to offspring"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "A population of mice lives on dark soil. Over many generations, the population becomes predominantly dark-coloured. What explains this?",
                "opts": [
                    ("Natural selection — dark mice are better camouflaged, survive predation better and reproduce more, passing on dark colour alleles", True),
                    ("The mice deliberately changed colour to match their environment", False),
                    ("Dark soil contains minerals that cause mice to become darker", False),
                    ("Dark-coloured mice migrated from elsewhere and replaced the lighter mice", False)
                ],
                "wrong_explanations": {
                    1: "Animals cannot deliberately change their genetic traits — they cannot 'choose' to become better adapted.",
                    2: "Environmental exposure doesn't directly change DNA — this would be Lamarckian evolution, which has been disproved. Colour is a genetic trait, not caused by soil minerals.",
                    3: "While migration is possible, natural selection is the primary explanation — lighter mice are more visible to predators and are caught more often."
                }
            },
            {
                "q": "Why was Darwin's theory of natural selection initially controversial?",
                "opts": [
                    ("It contradicted religious beliefs about creation, and Darwin lacked knowledge of the mechanism of inheritance", True),
                    ("It was based on observations from only one location and no experiments were done", False),
                    ("Darwin published it before collecting sufficient evidence, making it speculative", False),
                    ("The theory was too simple — scientists thought evolution must be more complicated", False)
                ],
                "wrong_explanations": {
                    1: "Darwin travelled extensively (including the Galapagos, South America, Australia) and collected extensive evidence over many years.",
                    2: "Darwin actually delayed publication for over 20 years while gathering more evidence — he published when he felt the evidence was compelling.",
                    3: "The theory was considered TOO radical and COMPLICATED for many — particularly the idea of species changing over millions of years."
                }
            },
            {
                "q": "What does 'survival of the fittest' mean in evolution?",
                "opts": [
                    ("Individuals best adapted to their environment are most likely to survive and reproduce — not necessarily the strongest", True),
                    ("The physically strongest and fastest individuals always survive", False),
                    ("Only the largest organisms in a population will reproduce", False),
                    ("Individuals that are most intelligent always out-compete others", False)
                ],
                "wrong_explanations": {
                    1: "Strength is one possible advantage in some environments — but 'fittest' specifically means best suited to the environment. A slow, toxic frog is 'fitter' than a fast but tasty one in a predator-rich environment.",
                    2: "Size can be a disadvantage — larger organisms often need more food and may be more visible to predators.",
                    3: "Intelligence is advantageous in some contexts — but many highly successful organisms (bacteria, insects) have no intelligence."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 8. SELECTIVE BREEDING
    # ══════════════════════════════════════════════
    {
        "id": "selective-breeding",
        "title": "Selective Breeding",
        "spec": "4.6.6",
        "summary": "Describe how selective breeding works and its applications and disadvantages.",
        "theory": [
            {
                "heading": "What is Selective Breeding?",
                "content": "SELECTIVE BREEDING (also called artificial selection) is the process by which HUMANS choose organisms with DESIRED CHARACTERISTICS to breed together, over many generations, in order to enhance those characteristics.\n\nHumans have been selectively breeding animals and plants for approximately 10,000 years — since the beginning of agriculture.\n\nThe process:\n1. Identify individuals in a population that show the desired characteristic most strongly.\n2. Breed these selected individuals together.\n3. From the offspring, select those that best show the desired characteristic.\n4. Repeat over many generations.\n5. After many generations, the desired trait becomes strongly established in the population."
            },
            {
                "heading": "Examples of Selective Breeding",
                "content": "ANIMALS:\nDOGS — bred for specific behaviours and appearances: border collies (herding instinct), greyhounds (speed), St. Bernards (size and rescue ability), bulldogs (appearance — though controversial due to health issues).\nCATTLE — bred for high milk yield (dairy breeds like Holstein) or high meat yield (beef breeds like Angus).\nCHICKENS — bred for rapid growth, high egg production, or both.\nSHEEP — bred for high wool production, high meat yield or specific fleece qualities.\n\nPLANTS:\nWHEAT — bred for disease resistance, high yield, drought tolerance, shorter stems (reduces lodging in wind).\nCORN (MAIZE) — from a small, wild grass (teosinte) to modern maize with large cobs over thousands of years.\nSTRAWBERRIES — bred for larger fruit, sweeter taste, disease resistance.\nROSES — bred for specific colours, petal arrangements and scent.\nBROCCOLI, CABBAGE, KALE, CAULIFLOWER — all bred from the same wild plant (Brassica oleracea) by selecting for different features."
            },
            {
                "heading": "Advantages and Disadvantages of Selective Breeding",
                "content": "ADVANTAGES:\nProduces organisms with highly desirable characteristics — increased yield, disease resistance, better flavour.\nHas dramatically increased food production — helping feed a growing global population.\nCan produce animals better suited to human purposes — working dogs, guide dogs, therapy animals.\n\nDISADVANTAGES:\nREDUCED GENETIC DIVERSITY — by continually selecting the same traits, populations become genetically very similar (inbreeding).\nINBREEDING problems — reduced variation means if a new disease or environmental change occurs, the entire population may be vulnerable.\nHEALTH PROBLEMS — selection for extreme traits can cause welfare issues. Examples: bulldogs have such flat faces they struggle to breathe; some large dog breeds have hip problems; high-yield dairy cows often suffer from mastitis.\nINHERITED DISEASES — concentrated in small gene pool over generations.\nThe process is slow — takes many generations to achieve significant change."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Selective breeding is NOT genetic engineering. Selective breeding uses natural reproduction — choosing which organisms breed. Genetic engineering directly inserts, removes or modifies specific genes. Selective breeding also does NOT create new genes — it selects and concentrates alleles that already exist in the population.",
        "key_note": "Selective breeding: humans choose organisms with desired traits to breed. Takes many generations. Increases desired characteristics. Disadvantages: reduced genetic diversity, inbreeding, health problems in extreme cases.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Selective Breeding Example",
            "instruction": "Match each organism to the characteristic that has been selectively bred.",
            "pairs": [
                ("Dairy cattle", "Selectively bred for increased milk yield — e.g. Holstein Friesian"),
                ("Wheat", "Selectively bred for disease resistance and high grain yield"),
                ("Dogs (greyhounds)", "Selectively bred for speed in racing"),
                ("Chickens", "Selectively bred for rapid growth and/or high egg production"),
                ("Maize (corn)", "Selectively bred from a small wild grass to produce large cobs over thousands of years"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What is the main disadvantage of selective breeding over many generations?",
                "opts": [
                    ("Reduced genetic diversity — the gene pool narrows, making populations vulnerable to new diseases or environmental changes", True),
                    ("Selective breeding always produces weaker offspring than wild populations", False),
                    ("It produces organisms that cannot survive outside captivity or cultivation", False),
                    ("The desired traits always disappear after a few generations", False)
                ],
                "wrong_explanations": {
                    1: "Selectively bred organisms are often very productive — but reduced genetic diversity is the key long-term risk.",
                    2: "Many selectively bred organisms can survive in natural conditions — though some extreme examples (like bulldogs) do have welfare issues.",
                    3: "Selective breeding fixes desired traits into the genome — they don't disappear unless the selection pressure is removed and interbreeding with different varieties occurs."
                }
            },
            {
                "q": "How is selective breeding different from genetic engineering?",
                "opts": [
                    ("Selective breeding uses natural reproduction to concentrate existing alleles. Genetic engineering directly inserts, modifies or removes specific genes.", True),
                    ("Selective breeding is faster than genetic engineering", False),
                    ("Selective breeding creates entirely new genes. Genetic engineering uses existing ones.", False),
                    ("They are essentially the same process — both involve deliberately changing an organism's DNA", False)
                ],
                "wrong_explanations": {
                    1: "Selective breeding is SLOW — it takes many generations. Genetic engineering can produce results in one generation.",
                    2: "Selective breeding works with EXISTING genetic variation — it cannot create new genes. Genetic engineering can introduce genes from completely different species.",
                    3: "Selective breeding does NOT directly change DNA sequences — it selects which individuals reproduce. Genetic engineering directly manipulates DNA."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 9. GENETIC ENGINEERING
    # ══════════════════════════════════════════════
    {
        "id": "genetic-engineering",
        "title": "Genetic Engineering",
        "spec": "4.6.7",
        "summary": "Describe genetic engineering — how it works, examples and ethical considerations.",
        "theory": [
            {
                "heading": "What is Genetic Engineering?",
                "content": "GENETIC ENGINEERING (also called recombinant DNA technology or genetic modification) is the direct manipulation of an organism's DNA — inserting, removing or modifying specific genes.\n\nUnlike selective breeding, genetic engineering:\nCan introduce genes from COMPLETELY DIFFERENT SPECIES — e.g. human genes into bacteria.\nWorks in a single generation — no need to wait many generations.\nIs extremely precise — targets a specific gene.\n\nThe basic process:\n1. The desired gene is CUT from the source organism's DNA using restriction enzymes (molecular scissors).\n2. The gene is INSERTED into a VECTOR — usually a bacterial PLASMID (a small circular piece of DNA).\n3. The vector is introduced into the target organism's cells.\n4. The target organism's cells now EXPRESS the new gene — producing the desired protein."
            },
            {
                "heading": "Examples of Genetic Engineering",
                "content": "INSULIN PRODUCTION:\nHuman insulin gene inserted into BACTERIA.\nBacteria grow rapidly in large vats → produce large quantities of human insulin.\nUsed to treat Type 1 diabetes.\nBefore this (before ~1982), diabetics used insulin extracted from pig or cattle pancreases — which caused immune reactions in some patients.\nHuman insulin from GM bacteria is identical to natural human insulin → fewer side effects.\n\nGM CROPS (Genetically Modified crops):\nHERBICIDE RESISTANCE — a gene for herbicide resistance inserted into crop plants (e.g. GM soybean). Farmers can spray the field to kill weeds without harming the crop.\nPEST RESISTANCE — Bt crops: a gene from the bacterium Bacillus thuringiensis produces a natural insecticide within the plant. Reduces need for chemical pesticides.\nGOLDEN RICE — a gene from daffodils (and a bacterium) inserted into rice to produce beta-carotene (precursor to vitamin A). Addresses vitamin A deficiency in developing countries.\nDROUGHT TOLERANCE — genes that increase water efficiency inserted into crops for use in dry regions."
            },
            {
                "heading": "Ethical Considerations of Genetic Engineering",
                "content": "Genetic engineering raises significant ethical debates:\n\nARGUMENTS FOR:\nCan save lives — GM insulin prevents deaths from diabetes.\nCan increase food security — GM crops produce higher yields, resist disease and pests.\nCan address nutritional deficiencies — e.g. Golden Rice.\nMay reduce environmental impact — pest-resistant crops need fewer chemical pesticides.\n\nARGUMENTS AGAINST:\nUNCERTAINTY about long-term effects — what happens when GM organisms interact with wild ecosystems?\nBIODIVERSITY risks — modified genes could spread to wild relatives ('gene escape').\nMONOCULTURES — large-scale GM crop production may reduce genetic diversity.\nCORPORATE CONTROL — major biotechnology companies own patents on GM seeds, preventing farmers from saving seeds.\nANIMAL WELFARE — concerns about use of genetically modified animals in research.\nCONSUMER CONCERNS — some people don't want to eat GM food, regardless of scientific evidence of safety.\nReligious/ethical objections — interfering with 'nature' or 'playing God'."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Genetic engineering is NOT the same as selective breeding. Genetic engineering can transfer genes between completely different species (e.g. human genes into bacteria). Selective breeding can only work with organisms that can naturally reproduce together. Also: eating GM food does not alter the consumer's own DNA.",
        "key_note": "Genetic engineering: cut gene with restriction enzymes → insert into vector (plasmid) → introduce to target organism. Examples: human insulin from GM bacteria, herbicide-resistant crops, Golden Rice. Ethical debate: benefits vs risks to biodiversity and ecosystems.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Genetic Engineering Example",
            "instruction": "Match each application to how genetic engineering is used.",
            "pairs": [
                ("GM bacteria → insulin", "Human insulin gene inserted into bacteria — bacteria produce insulin for diabetics"),
                ("Herbicide-resistant crops", "Gene for herbicide resistance inserted into crop plants — farmer can spray without harming the crop"),
                ("Bt crops", "Gene from Bacillus thuringiensis inserted — crop produces natural insecticide to repel pests"),
                ("Golden Rice", "Gene inserted to produce beta-carotene — addresses vitamin A deficiency in developing countries"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why is GM bacterial insulin better for diabetics than insulin extracted from pigs or cattle?",
                "opts": [
                    ("GM bacterial insulin is identical to human insulin — fewer immune reactions and side effects", True),
                    ("Bacterial insulin is cheaper to produce so more people can afford it", False),
                    ("Animal-derived insulin is no longer available — GM insulin is the only option", False),
                    ("GM bacteria produce insulin faster so it acts more quickly in the body", False)
                ],
                "wrong_explanations": {
                    1: "Cost is an advantage, but the primary medical reason is that human sequence insulin causes fewer immune problems than animal sequence insulin.",
                    2: "Animal-derived insulin still exists in some countries — GM insulin has largely replaced it due to superior compatibility.",
                    3: "The speed of action is determined by the formulation (how the insulin is prepared), not where it came from."
                }
            },
            {
                "q": "What is the basic process of introducing a new gene into an organism?",
                "opts": [
                    ("Cut the desired gene using restriction enzymes → insert into a plasmid vector → introduce the vector into the target cell", True),
                    ("Inject the desired gene directly into the cell nucleus using a syringe", False),
                    ("Breed the organism with another species that carries the desired gene", False),
                    ("Expose the organism to radiation to trigger the mutation needed", False)
                ],
                "wrong_explanations": {
                    1: "While microinjection into cells is a real technique used in some contexts, the standard recombinant DNA approach uses restriction enzymes and plasmid vectors.",
                    2: "Breeding between different species = selective breeding (and only works between related species). Genetic engineering specifically allows cross-species gene transfer.",
                    3: "Radiation causes RANDOM mutations — not the specific targeted change needed for genetic engineering."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 10. EVIDENCE FOR EVOLUTION
    # ══════════════════════════════════════════════
    {
        "id": "evidence-for-evolution",
        "title": "Evidence for Evolution",
        "spec": "4.6.5",
        "summary": "Describe the main types of evidence that support the theory of evolution.",
        "theory": [
            {
                "heading": "The Fossil Record",
                "content": "FOSSILS are the preserved remains or traces of organisms from the past.\n\nFossils form when an organism's hard parts (bones, shells, teeth) are buried and slowly replaced by minerals over millions of years. Soft tissue rarely fossilises — so the fossil record is incomplete.\n\nOther types of fossil: trace fossils (footprints, burrows), preserved organisms in amber, ice or tar pits.\n\nHow fossils support evolution:\nOlder rock layers (deeper in the ground) contain simpler, more primitive organisms.\nYounger rocks (closer to the surface) contain more complex, more modern-looking organisms.\nTransitional fossils show intermediate forms between ancient and modern species — e.g. Tiktaalik (fish-tetrapod transition), Archaeopteryx (dinosaur-bird transition).\nGradual changes in fossil series show how species changed over millions of years.\n\nLimitation: the fossil record is incomplete — most organisms never fossilise, and many fossils are yet to be discovered."
            },
            {
                "heading": "Homologous Structures",
                "content": "HOMOLOGOUS STRUCTURES are body parts that have the SAME UNDERLYING STRUCTURE but are adapted for DIFFERENT FUNCTIONS in different species.\n\nThe classic example is the PENTADACTYL LIMB (five-digit limb):\nHuman arm — for grasping and manipulating objects.\nWhale flipper — for swimming.\nBat wing — for flying.\nHorse leg — for running.\nFrog limb — for swimming and jumping.\n\nAll of these limbs have the same arrangement of bones (humerus, radius, ulna, carpals, metacarpals, phalanges) — just modified in shape and proportion for different uses.\n\nThis shared fundamental structure strongly suggests they all evolved from a COMMON ANCESTOR that had a basic five-digit limb — the limbs diverged as each lineage adapted to different environments.\n\nIf these structures had evolved independently, there would be no reason for them to share the same underlying bone arrangement."
            },
            {
                "heading": "DNA and Molecular Evidence",
                "content": "Modern molecular biology provides some of the strongest evidence for evolution.\n\nDNA COMPARISONS:\nAll living organisms use the same genetic code (the same triplet of bases codes for the same amino acid, in virtually all species).\nThis UNIVERSAL GENETIC CODE strongly suggests all life descended from a common ancestor.\nThe more closely related two species are, the MORE SIMILAR their DNA sequences are.\nExample: humans and chimpanzees share approximately 98.7% of their DNA — reflecting our recent common ancestor.\nHumans and yeast share about 25% of their genes — both are eukaryotes descended from the same original eukaryotic ancestor.\n\nPROTEIN COMPARISONS:\nSimilarly, closely related species share more similar protein structures.\nHaemoglobin (the oxygen-carrying protein in blood) has a very similar structure in all vertebrates — with differences reflecting evolutionary distance.\n\nVIRUSES and BACTERIA evolving in real time:\nAntibiotic resistance in bacteria.\nNew influenza strains each year.\nCOVID-19 variants (Alpha, Delta, Omicron).\nAll demonstrate evolution by natural selection occurring today — observable directly."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "The fossil record is INCOMPLETE — most organisms never fossilise. This means gaps in the fossil record are EXPECTED and do not disprove evolution. Students often say 'if there are gaps in the fossil record, evolution can't be proven' — but the overall pattern of fossils strongly supports evolution, even with gaps.",
        "key_note": "Evidence: fossils (older = simpler, gradual change), homologous structures (pentadactyl limb — common ancestor), DNA comparisons (similar species = similar DNA), direct observation (antibiotic resistance, flu evolution). All support evolution.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Evidence to What it Shows",
            "instruction": "Match each piece of evidence to what it demonstrates about evolution.",
            "pairs": [
                ("Fossil record", "Shows gradual changes in organisms over millions of years — older fossils are simpler"),
                ("Pentadactyl limb", "Same bone structure in human, whale, bat and horse limbs — suggests common ancestor"),
                ("DNA comparisons", "Closely related species have more similar DNA sequences — reflects evolutionary distance"),
                ("Antibiotic resistance", "Bacteria evolving resistance in real time — direct observation of natural selection"),
                ("Universal genetic code", "All life uses the same DNA code — suggests all organisms descended from a common ancestor"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why do the pentadactyl (five-digit) limbs of humans, whales and bats support evolution?",
                "opts": [
                    ("They share the same underlying bone structure despite very different functions — suggesting a common ancestor whose limb adapted differently in each lineage", True),
                    ("They show that all vertebrates use their limbs in the same way — a universal design", False),
                    ("Five-digit limbs are the most efficient design, so evolution always produces them independently", False),
                    ("It shows that whales were once land animals that walked on five-toed feet", False)
                ],
                "wrong_explanations": {
                    1: "Vertebrate limbs are used very differently — for flying, swimming, running and grasping. The similarity in structure, despite different functions, is precisely what makes it evidence of common ancestry.",
                    2: "If five digits were universally optimal, we'd expect to see it in insects and fish too — but they don't have this arrangement. The pattern is phylogenetic (family-tree based), not design-based.",
                    3: "While it's true whales evolved from land mammals, the pentadactyl limb evidence is specifically about STRUCTURAL SIMILARITY across multiple species, not specifically about whale evolution."
                }
            },
            {
                "q": "Why does antibiotic resistance in bacteria provide evidence for evolution?",
                "opts": [
                    ("It demonstrates natural selection occurring in real time — resistant variants survive and reproduce, changing the population", True),
                    ("It shows that bacteria can deliberately change their DNA in response to threats", False),
                    ("It proves that antibiotics cause mutations in bacteria", False),
                    ("It shows that evolution only happens in very simple organisms like bacteria", False)
                ],
                "wrong_explanations": {
                    1: "Bacteria cannot choose or deliberately change their DNA — resistance arises from RANDOM mutations that existed before antibiotic exposure.",
                    2: "Antibiotics SELECT resistant variants — they don't cause the mutations. The mutations existed before the antibiotic was used.",
                    3: "Evolution occurs in all organisms — bacteria just evolve faster because they reproduce rapidly (millions of generations in days). Natural selection has been directly observed in larger organisms too."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 11. FOSSILS AND EXTINCTION
    # ══════════════════════════════════════════════
    {
        "id": "fossils-extinction",
        "title": "Fossils and Extinction",
        "spec": "4.6.5",
        "summary": "Describe how fossils form and explain why species become extinct.",
        "theory": [
            {
                "heading": "How Fossils Form",
                "content": "A FOSSIL is the preserved remains or traces of an organism from the geological past.\n\nFossils form in several ways:\n\nMINERALISATION:\nAn organism dies and is quickly buried by sediment (mud, sand).\nSoft tissue decays, but hard parts (bones, teeth, shells) remain.\nOver millions of years, minerals from the surrounding rock slowly replace the original material.\nEventually all original material is replaced by rock → a fossil.\n\nPRESERVATION in extreme conditions:\nAMBER — tree resin traps small organisms (insects, spiders) which are perfectly preserved.\nICE — frozen conditions preserve soft tissue (woolly mammoths found almost intact in Siberia).\nTAR PITS — organisms become trapped in natural asphalt and are preserved.\nPEAT BOGS — acidic, anaerobic conditions preserve soft tissue (bog bodies found in northern Europe).\n\nTRACE FOSSILS:\nFootprints, burrows, bite marks or droppings preserved in rock.\nProvide evidence of behaviour as well as body structure."
            },
            {
                "heading": "Why the Fossil Record is Incomplete",
                "content": "The fossil record does not contain every organism that ever lived — it is significantly INCOMPLETE.\n\nReasons:\nSOFT TISSUE rarely fossilises — decay is usually faster than mineralisation.\nSMALL OR FRAGILE organisms are less likely to leave fossils.\nCONDITIONS must be exactly right — rapid burial, appropriate chemistry, absence of scavengers.\nFOSSILS may be DESTROYED by geological processes — volcanic activity, erosion, subduction.\nFOSSILS are simply not yet found — much of the Earth's rock has not been excavated.\n\nDespite being incomplete, the fossil record is remarkably consistent with evolution — older fossils are simpler, newer fossils are more complex, and transitional forms have been found."
            },
            {
                "heading": "Extinction",
                "content": "EXTINCTION occurs when every individual member of a species dies — the species is gone forever.\n\nExtinction is permanent — once a species is gone, it cannot return.\n\nCauses of extinction:\nCATASTROPHIC EVENTS — e.g. asteroid impact (linked to mass extinction of dinosaurs ~66 million years ago), volcanic eruptions producing climate change.\nHABITAT DESTRUCTION — deforestation, draining of wetlands, urbanisation → species lose their living space.\nNEW COMPETITORS or PREDATORS — introduced species outcompeting or preying on native species.\nNEW DISEASES — disease spreading through a population with no natural immunity.\nCLIMATE CHANGE — rapid shifts in temperature or rainfall patterns that species cannot adapt to quickly enough.\nOVERHUNTING/OVERFISHING — human hunting reducing populations below viable levels (e.g. dodo, passenger pigeon, woolly mammoth — possibly).\n\nCurrent extinction crisis:\nScientists estimate we are currently experiencing a mass extinction event caused primarily by human activity — habitat destruction, climate change, pollution and overexploitation."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Extinction is PERMANENT — a species cannot come back once all individuals are dead. The fossil record being incomplete does NOT disprove evolution — it is expected and understandable given how rare fossilisation is. Most organisms that ever lived left no fossil at all.",
        "key_note": "Fossils form by mineralisation, preservation in amber/ice/tar, or trace fossils. Record is incomplete because soft tissue rarely fossilises and conditions must be exact. Extinction = all individuals of species die — permanent. Causes: catastrophe, habitat loss, competition, disease, climate change, human activity.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Fossil Type or Extinction Cause",
            "instruction": "Match each term to its correct description.",
            "pairs": [
                ("Mineralisation", "Hard parts replaced by minerals over millions of years as the organism is buried in sediment"),
                ("Amber preservation", "Small organisms trapped in tree resin — perfectly preserved for millions of years"),
                ("Trace fossil", "Footprints, burrows or droppings preserved in rock — evidence of behaviour"),
                ("Habitat destruction", "Forests cleared, wetlands drained — species lose living space — extinction risk"),
                ("Introduced species", "New predator or competitor arrives in an ecosystem — native species may be outcompeted"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "Why are soft-bodied organisms rarely found as fossils?",
                "opts": [
                    ("Soft tissue decays quickly — it usually decomposes before mineralisation can occur", True),
                    ("Soft-bodied organisms don't have cells, so they cannot be fossilised", False),
                    ("Soft-bodied organisms only live in water — fossils only form on land", False),
                    ("Soft tissue is preserved perfectly but scientists cannot identify it", False)
                ],
                "wrong_explanations": {
                    1: "All living things have cells — soft-bodied organisms (jellyfish, worms etc.) are eukaryotes with normal cells.",
                    2: "Many fossils DO form in water and marine sediments — in fact, aquatic environments are often BETTER for fossilisation because rapid burial in sediment is more likely.",
                    3: "Soft tissue can be preserved in exceptional circumstances (amber, ice, peat bogs) — but in most cases it decays before preservation can occur."
                }
            },
            {
                "q": "The dodo became extinct in the 17th century. What caused its extinction?",
                "opts": [
                    ("Human hunting and introduced species (rats and pigs eating eggs) — the dodo had no natural predators and was not afraid of humans", True),
                    ("A catastrophic volcanic eruption on Mauritius wiped out the entire population", False),
                    ("Climate change caused the fruit the dodo ate to disappear", False),
                    ("A deadly virus spread through the population before any could survive and develop immunity", False)
                ],
                "wrong_explanations": {
                    1: "No major volcanic eruption caused the dodo's extinction — it was a combination of human hunting and the introduction of invasive species.",
                    2: "Some habitat change occurred, but the primary drivers were hunting and invasive species, not climate-driven food loss.",
                    3: "While disease can cause extinction, the primary documented causes for the dodo are human hunting and introduced species."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════
    # 12. RESISTANT BACTERIA
    # ══════════════════════════════════════════════
    {
        "id": "resistant-bacteria",
        "title": "Resistant Bacteria",
        "spec": "4.6.5",
        "summary": "Explain how antibiotic resistance develops through natural selection and why it is a global health threat.",
        "theory": [
            {
                "heading": "How Antibiotic Resistance Develops",
                "content": "Antibiotic resistance is a direct example of EVOLUTION BY NATURAL SELECTION occurring in our lifetimes.\n\nThe process:\n1. VARIATION — within a population of bacteria, individuals vary slightly due to random mutations. A very small number may have a mutation that gives RESISTANCE to a particular antibiotic.\n2. SELECTION PRESSURE — when antibiotics are used, they KILL bacteria that are NOT resistant. The resistant bacteria SURVIVE.\n3. REPRODUCTION — resistant bacteria reproduce (bacteria can double every 20 minutes). They pass on the resistance gene to offspring.\n4. SPREAD — resistant bacteria become increasingly common in the population. The antibiotic no longer works.\n\nThis is natural selection in real time — the antibiotic acts as the selection pressure. The resistant mutation existed BEFORE the antibiotic was used — the antibiotic didn't create the mutation, it selected for it."
            },
            {
                "heading": "MRSA — A Serious Example",
                "content": "MRSA (Methicillin-resistant Staphylococcus aureus) is a bacterium that has developed resistance to many commonly used antibiotics.\n\nStaphylococcus aureus is normally a relatively harmless skin bacterium found on about 30% of people.\n\nMRSA has acquired resistance through repeated exposure to antibiotics — particularly in hospital settings where antibiotics are widely used.\n\nWhy MRSA is dangerous:\nDifficult to treat — standard antibiotics don't work.\nCan cause serious infections: bloodstream infections (sepsis), pneumonia, wound infections.\nParticularly dangerous for hospital patients who are already weakened or have wounds.\nFew effective antibiotics remain — some strains are resistant to almost everything.\n\nMRSA shows what can happen when antibiotic resistance goes unchecked — a common bacterium becomes a serious, life-threatening pathogen."
            },
            {
                "heading": "Why Antibiotic Resistance is a Global Crisis",
                "content": "Antibiotic resistance is one of the greatest threats to global health, food security and development — according to the World Health Organisation.\n\nThe problem is accelerating because:\nOVER-PRESCRIPTION — antibiotics given for viral infections (where they have no effect) or 'just in case'.\nINCOMPLETE COURSES — stopping antibiotics early leaves the most resistant bacteria alive to reproduce.\nAGRICULTURAL USE — antibiotics widely used in livestock farming to prevent disease and promote growth → resistant bacteria enter food chains.\nGLOBAL SPREAD — resistant bacteria travel with people internationally.\nSLOW DEVELOPMENT of new antibiotics — pharmaceutical companies have reduced investment because new antibiotics are not as profitable as drugs for chronic diseases.\n\nWhat can be done:\nPrescribe antibiotics ONLY when necessary.\nPatients must COMPLETE FULL COURSES.\nDevelop NEW antibiotics and alternative treatments (e.g. phage therapy — using viruses that kill bacteria).\nReduce agricultural antibiotic use.\nBetter hygiene to prevent spread of resistant bacteria."
            }
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Antibiotics do NOT CAUSE mutations — they SELECT resistant bacteria that already exist. The mutation happened randomly, long before the antibiotic was used. The antibiotic is the selection pressure that determines which bacteria survive. This is a key distinction — evolution acts on existing variation, it doesn't create new variation in response to need.",
        "key_note": "Resistance develops by natural selection: random resistance mutation exists → antibiotic kills non-resistant bacteria → resistant bacteria survive and reproduce → resistance spreads. Antibiotics select for resistance — they don't cause it. MRSA = serious hospital-acquired resistant bacterium.",
        "higher": None,
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Steps in Developing Antibiotic Resistance",
            "instruction": "Put the steps of antibiotic resistance development in order by matching each step.",
            "pairs": [
                ("Step 1 — Variation", "A random mutation gives one bacterium resistance to an antibiotic — before any antibiotic is used"),
                ("Step 2 — Selection pressure", "Antibiotic is used — kills all non-resistant bacteria, resistant one survives"),
                ("Step 3 — Reproduction", "Resistant bacterium reproduces — passing resistance gene to millions of offspring"),
                ("Step 4 — Population change", "Resistant bacteria dominate the population — the antibiotic no longer works"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "How does antibiotic resistance develop in bacteria?",
                "opts": [
                    ("A random mutation gives some bacteria resistance — antibiotics kill non-resistant bacteria but resistant ones survive and reproduce", True),
                    ("Bacteria deliberately mutate themselves when exposed to antibiotics to survive", False),
                    ("Antibiotics cause the mutation that produces resistance in bacteria", False),
                    ("Resistant bacteria migrate from other areas after non-resistant bacteria are killed", False)
                ],
                "wrong_explanations": {
                    1: "Bacteria cannot deliberately change their DNA — mutations are RANDOM and SPONTANEOUS. Bacteria cannot respond to threats by choosing to mutate.",
                    2: "Antibiotics are the SELECTION PRESSURE — they select pre-existing resistant variants. They do not cause the mutations that produce resistance.",
                    3: "Migration can spread resistance — but the PRIMARY mechanism of resistance developing in a population is natural selection of pre-existing resistant mutants."
                }
            },
            {
                "q": "Why is it important to complete a full course of antibiotics even if you feel better?",
                "opts": [
                    ("Stopping early leaves the most resistant bacteria alive — they survive to reproduce and pass on resistance genes", True),
                    ("The remaining antibiotics are needed to prevent the infection returning to full strength", False),
                    ("Unfinished antibiotics are wasted medicine that could have been used by others", False),
                    ("Stopping early makes the side effects of antibiotics worse", False)
                ],
                "wrong_explanations": {
                    1: "Infections can return if bacteria are not fully cleared — but the MORE IMPORTANT reason in terms of antibiotic resistance is that the survivors of partial treatment are the most resistant bacteria.",
                    2: "While waste is a concern, the primary medical reason is resistance selection — the survivors of an incomplete course are more likely to be resistant.",
                    3: "Side effects are not affected by course completion — the resistance argument is the primary public health reason."
                }
            },
            {
                "q": "MRSA is resistant to many antibiotics. How did this resistance arise?",
                "opts": [
                    ("Through natural selection — repeated antibiotic use in hospitals selected for bacteria with resistance mutations, which then multiplied", True),
                    ("MRSA was deliberately engineered in a laboratory as a biological weapon", False),
                    ("MRSA infected humans from animals and naturally carries more mutations than other bacteria", False),
                    ("Hospital cleaning products cause bacteria to mutate and become resistant", False)
                ],
                "wrong_explanations": {
                    1: "MRSA arose naturally through the evolutionary process of natural selection — not deliberate engineering.",
                    2: "Staphylococcus aureus is primarily a human pathogen — while zoonotic transmission does occur, MRSA's resistance arose through natural selection in hospital environments.",
                    3: "Cleaning products can select for resistance to disinfectants — but antibiotic resistance specifically arises from exposure to antibiotics, not cleaning agents."
                }
            }
        ]
    },
],

"ecology": [
    {
        "id": "ecosystems-food-webs",
        "title": "Ecosystems, Food Webs and Population",
        "spec": "4.7",
        "summary": "Describe ecosystems, food chains and webs, and factors affecting population size.",
        "theory": [
            {"heading": "Ecosystems and Communities",
             "content": "Ecosystem: all the living organisms (community) AND non-living factors (abiotic) in an area.\nPopulation: all individuals of one species in an area.\nCommunity: all populations of different species in an area.\nHabitat: the place where an organism lives."},
            {"heading": "Abiotic and Biotic Factors",
             "content": "Abiotic (non-living): temperature, light, water/rainfall, pH, CO₂ and O₂ levels, mineral content of soil.\nBiotic (living): food availability, predators, competition, disease, parasites.\nBoth types affect the distribution and abundance of organisms.\nIf conditions change, populations change in response."},
            {"heading": "Food Chains and Webs",
             "content": "Food chain: shows feeding relationships — producer → primary consumer → secondary consumer → tertiary consumer.\nProducer: green plant — makes its own food by photosynthesis.\nConsumer: animal — eats other organisms.\nPredator: hunts prey. Prey: is eaten by predator.\nFood web: many interconnected food chains — more realistic picture of ecosystem.\nRemoving one species can affect many others (cascade effect)."},
            {"heading": "Sampling Techniques",
             "content": "Quadrats: count organisms in a sample area — calculate population size from mean × total area.\nTransects: survey along a line through a habitat — show how organisms change with distance.\nMark-recapture: catch, mark, release, recapture — estimate population size.\nFormula: N = (first catch × second catch) ÷ number of marked individuals in second catch."}
        ],
        "variables": [],
        "equations": ["N = (n₁ × n₂) ÷ m  (mark-recapture)"],
        "common_mistake": "Energy is LOST at each stage of a food chain (as heat, movement, waste). This is why food chains rarely have more than 4-5 levels — not enough energy reaches the top. Less energy = fewer organisms that can be supported.",
        "key_note": "Energy transfer between trophic levels is only about 10% efficient — most is lost as heat.",
        "higher": "Efficiency of energy transfer = (energy available at next level ÷ energy available at previous level) × 100%. Pyramids of biomass always decrease upward. Pyramids of number can be inverted (e.g. one tree supports many insects).",
        "triple_only": None,
        "rp": "RP6 — Use quadrats to estimate population size of a species in a habitat. Calculate mean count and scale up to total area.",
        "matching": {
            "title": "Match the Term to its Definition",
            "instruction": "Match each ecology term to its correct definition.",
            "pairs": [
                ("Population", "All individuals of one species in a given area"),
                ("Community", "All populations of different species in an area"),
                ("Ecosystem", "Community + all abiotic (non-living) factors"),
                ("Producer", "An organism that makes its own food via photosynthesis"),
                ("Primary consumer", "An organism that eats producers (herbivore)"),
                ("Decomposer", "Breaks down dead organisms — releases nutrients back into soil"),
            ]
        },
        "fifas": [
            {"label": "Example — Mark-recapture population estimate",
             "question": "50 woodlice are caught, marked and released. Later, 40 are caught and 8 are marked. Estimate the population.",
             "steps": [("F","N = (n₁ × n₂) ÷ m"), ("I","N = (50 × 40) ÷ 8 = 2000 ÷ 8"), ("F","No unit conversion needed"), ("A","N = 250 woodlice")]}
        ],
        "quiz": [
            {"q": "What is an abiotic factor?",
             "opts": [("A non-living factor affecting organisms — e.g. temperature, light, water", True), ("A living factor such as predation or disease", False), ("A type of organism in the ecosystem", False), ("The physical size of an ecosystem", False)],
             "wrong_explanations": {1: "Living factors like predation and disease are BIOTIC factors — abiotic means non-living.", 2: "Organisms are part of the community — not abiotic factors.", 3: "Ecosystem size isn't classified as abiotic or biotic — it's a spatial measurement."}},
            {"q": "Why do food chains rarely have more than 5 levels?",
             "opts": [("Energy is lost at each level — not enough energy remains to support more levels", True), ("Predators at the top become too large", False), ("Species at the top are too rare to form chains", False), ("Higher levels have no natural predators", False)],
             "wrong_explanations": {1: "Size can increase with trophic level — but that's not the limiting factor for chain length.", 2: "Rarity at higher levels is a consequence of energy loss — not the primary reason.", 3: "Whether they have predators or not, energy limits the number of organisms that can survive at the top."}},
            {"q": "30 beetles are marked and released. 20 are caught later; 6 are marked. Estimate the population.",
             "opts": [("100", True), ("3.6", False), ("180", False), ("600", False)],
             "wrong_explanations": {1: "You divided n₁ by m. N = (n₁ × n₂) ÷ m = (30 × 20) ÷ 6 = 100.", 2: "You added instead of multiplying. N = (30 × 20) ÷ 6 = 600 ÷ 6 = 100.", 3: "You multiplied all three numbers. N = (n₁ × n₂) ÷ m = (30 × 20) ÷ 6 = 100."}},
            {"q": "What is a producer in a food chain?",
             "opts": [("A photosynthetic organism that makes its own food — e.g. a plant", True), ("An animal that produces offspring", False), ("A factory that produces food", False), ("A top predator that produces the most energy", False)],
             "wrong_explanations": {1: "In ecology, 'producer' specifically means photosynthetic organism — not an animal that reproduces.", 2: "Factories are not part of natural ecosystems!", 3: "Top predators receive the LEAST energy — they're at the far end of the food chain."}},
            {"q": "What effect does removing a predator from an ecosystem have?",
             "opts": [("Prey population increases, which may reduce the plants/organisms they eat — cascade effect", True), ("No effect — prey adapts quickly", False), ("Predator's prey also decreases", False), ("The ecosystem becomes more stable", False)],
             "wrong_explanations": {1: "Prey doesn't instantly adapt — populations respond through birth/death rates, not instant evolution.", 2: "If a predator is removed, its prey population INCREASES (less predation) — not decreases.", 3: "Removing a keystone predator typically DESTABILIZES the ecosystem — it can cause population crashes further down the chain."}}
        ]
    },
    {
        "id": "nutrient-cycles",
        "title": "Nutrient Cycles and Biodiversity",
        "spec": "4.7.3",
        "summary": "Describe the carbon and water cycles, and explain the importance of biodiversity.",
        "theory": [
            {"heading": "The Carbon Cycle",
             "content": "Carbon moves between the atmosphere, organisms and the Earth in a continuous cycle.\nRemoved from atmosphere: photosynthesis (plants absorb CO₂).\nReturned to atmosphere: respiration (all organisms), decomposition (bacteria/fungi break down dead material), combustion (burning fossil fuels).\nFossil fuels = ancient carbon locked underground — burning releases it → increases atmospheric CO₂."},
            {"heading": "The Water Cycle",
             "content": "Evaporation: water evaporates from oceans, lakes and plants (transpiration).\nCondensation: water vapour cools → clouds form.\nPrecipitation: rain, snow, hail returns water to land and sea.\nRunoff: water flows into rivers → back to sea.\nAll living organisms need water — it's the solvent for all biochemical reactions."},
            {"heading": "The Nitrogen Cycle",
             "content": "Nitrogen makes up 78% of air — but plants can't use N₂ directly.\nNitrogen fixation: N₂ converted to ammonia/nitrates by nitrogen-fixing bacteria (in soil or root nodules of legumes).\nNitrification: ammonia converted to nitrates by nitrifying bacteria.\nDenitrification: nitrates converted back to N₂ by denitrifying bacteria.\nDecomposers: break down dead organisms → ammonia released (ammonification)."},
            {"heading": "Biodiversity and Conservation",
             "content": "Biodiversity = variety of species in an area AND genetic diversity within species.\nHigh biodiversity: more stable ecosystem — more connections, more resilience.\nThreats to biodiversity: habitat destruction, pollution, invasive species, climate change, overexploitation.\nConservation: protecting habitats, captive breeding programmes, seed banks, legislation.\nBenefits: ecosystem services (clean air/water, pollination, food), potential medicines, ethical responsibility."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Decomposers are fungi and bacteria — NOT worms or woodlice (these are detritivores that break material into smaller pieces but don't chemically decompose it). Both are important — but don't confuse the terms in exams.",
        "key_note": "Carbon cycle: photosynthesis removes CO₂; respiration, combustion, decomposition return CO₂. Fossil fuels are stored carbon.",
        "higher": "Indicator species: lichens indicate clean air (sensitive to SO₂). Mayfly larvae indicate clean water (sensitive to pollutants). Used to measure pollution levels.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Process to its Role in the Carbon Cycle",
            "instruction": "Match each process to whether it removes carbon from or returns it to the atmosphere.",
            "pairs": [
                ("Photosynthesis", "Removes CO₂ from atmosphere — locked into glucose"),
                ("Respiration", "Returns CO₂ to atmosphere — all living organisms do this"),
                ("Combustion", "Returns CO₂ from fossil fuels to atmosphere rapidly"),
                ("Decomposition", "Returns CO₂ as bacteria/fungi break down dead organic matter"),
                ("Fossilisation", "Locks carbon underground for millions of years"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What role do decomposers play in nutrient cycles?",
             "opts": [("Break down dead organisms — releasing nutrients back into the soil", True), ("Convert atmospheric nitrogen into nitrates", False), ("Remove CO₂ from the atmosphere", False), ("Transfer energy between trophic levels", False)],
             "wrong_explanations": {1: "Converting N₂ to nitrates = NITROGEN FIXATION by nitrogen-fixing bacteria.", 2: "Removing CO₂ = PHOTOSYNTHESIS by plants.", 3: "Energy transfer between trophic levels happens through feeding — not decomposers."}},
            {"q": "Why does burning fossil fuels increase atmospheric CO₂?",
             "opts": [("Carbon locked underground for millions of years is rapidly released as CO₂", True), ("Fossil fuels contain oxygen which becomes CO₂", False), ("Burning destroys the carbon cycle", False), ("Fire produces new carbon atoms", False)],
             "wrong_explanations": {1: "Fossil fuels are carbon-rich — burning them combines carbon with O₂ from air to make CO₂.", 2: "Burning doesn't destroy cycles — it just adds carbon to the atmosphere faster than natural processes can remove it.", 3: "Atoms can't be created or destroyed — combustion releases pre-existing carbon as CO₂."}},
            {"q": "Why is high biodiversity important for ecosystem stability?",
             "opts": [("More species = more connections = more resilience if one species is lost", True), ("More species always means more food for humans", False), ("Biodiversity prevents all environmental change", False), ("High biodiversity means more CO₂ is absorbed", False)],
             "wrong_explanations": {1: "More species doesn't automatically mean more human-edible food.", 2: "Biodiversity increases RESILIENCE to change — it doesn't prevent all change.", 3: "More plants would increase CO₂ absorption, but biodiversity includes all species — animals don't absorb CO₂."}},
            {"q": "How do plants absorb nitrogen for making proteins?",
             "opts": [("As nitrate ions (NO₃⁻) absorbed through roots", True), ("Directly from the atmosphere as N₂", False), ("As ammonia through their leaves", False), ("As protein from the soil", False)],
             "wrong_explanations": {1: "Plants cannot use atmospheric N₂ directly — they need it fixed into nitrates first.", 2: "Some plants absorb small amounts of ammonia but the main route is nitrate ions through roots.", 3: "Plants can't absorb proteins from soil — they build their own from amino acids synthesised from nitrates."}}
        ]
    },
],
}
