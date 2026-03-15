#!/usr/bin/env python3
"""
Biology subtopics — Combined Foundation
AQA 8464 / Biology 8461

Cell Biology:    7 subtopics (updated)
Organisation:    11 subtopics (updated)
All other topics: unchanged from previous version
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
    {
        "id": "pathogens-immunity",
        "title": "Pathogens, Disease and the Immune System",
        "spec": "4.3",
        "summary": "Describe types of pathogens, how diseases spread and how the immune system responds.",
        "theory": [
            {"heading": "Types of Pathogen",
             "content": "Bacteria: single-celled prokaryotes — reproduce rapidly inside body, produce toxins.\nViruses: not living cells — inject genetic material into host cells, replicate using host machinery.\nFungi: e.g. athlete's foot — grow on/in host tissue.\nProtists: single-celled eukaryotes — e.g. Plasmodium causes malaria (spread by mosquito)."},
            {"heading": "How Pathogens Spread",
             "content": "Water: cholera — contaminated drinking water.\nAir: influenza, COVID-19 — droplets from coughs/sneezes.\nDirect contact: rose black spot fungus on roses — direct touch.\nVectors: malaria — Plasmodium transmitted by Anopheles mosquito bite.\nSexual contact: HIV — transmitted in bodily fluids."},
            {"heading": "The Immune System",
             "content": "Physical barriers: skin, mucus in nose/airways, cilia.\nPhagocytosis: white blood cells (phagocytes) engulf and digest pathogens.\nAntibody production: lymphocytes produce specific antibodies that match pathogen antigens.\nMemory cells: remain after infection — rapid response if same pathogen returns → immunity."},
            {"heading": "Vaccination",
             "content": "Vaccine contains dead/weakened/parts of pathogen → triggers immune response without disease.\nMemory cells produced → rapid antibody response if real pathogen encountered.\nHerd immunity: if enough people are vaccinated, pathogen can't spread easily — even unvaccinated people protected.\nExamples: MMR, flu, COVID-19, HPV vaccines."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Antibiotics kill BACTERIA — they have NO effect on viruses. Students often say 'take antibiotics for flu' — this is wrong! Flu is caused by a virus. Antivirals are needed for viral infections (and are much harder to develop).",
        "key_note": "Bacteria: reproduce independently, treated with antibiotics. Viruses: use host cell machinery, NOT treated with antibiotics.",
        "higher": "Monoclonal antibodies: produced from a single B-lymphocyte clone. Used in pregnancy tests, cancer treatment (target tumour cells), COVID lateral flow tests.",
        "triple_only": None,
        "rp": None,
        "matching": {
            "title": "Match the Disease to its Pathogen and Transmission",
            "instruction": "Match each disease to the correct pathogen type and how it spreads.",
            "pairs": [
                ("Measles", "Virus — spread by airborne droplets"),
                ("Salmonella", "Bacteria — spread through contaminated food"),
                ("Malaria", "Protist (Plasmodium) — spread by Anopheles mosquito vector"),
                ("Athlete's foot", "Fungus — direct contact"),
                ("HIV/AIDS", "Virus — spread through bodily fluids"),
                ("Rose black spot", "Fungus — direct contact, spreads in water"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "A patient has a viral infection. Should they take antibiotics?",
             "opts": [("No — antibiotics only kill bacteria, not viruses", True), ("Yes — antibiotics kill all pathogens", False), ("Yes — antibiotics boost the immune system", False), ("Only if the infection is severe", False)],
             "wrong_explanations": {1: "Antibiotics kill ALL pathogens — this is wrong and a dangerous misconception. Antibiotics only target bacteria.", 2: "Antibiotics have no effect on the immune system — they don't boost it.", 3: "Even severe viral infections shouldn't be treated with antibiotics — antivirals or immune support are needed."}},
            {"q": "How does a vaccine protect against future infection?",
             "opts": [("Stimulates immune response and creates memory cells for rapid future response", True), ("Kills pathogens directly", False), ("Makes the body stronger by giving it a mild disease", False), ("Prevents the pathogen from ever entering the body", False)],
             "wrong_explanations": {1: "Vaccines don't contain active killing agents — they stimulate YOUR immune system.", 2: "The key mechanism is MEMORY CELLS — not just a mild disease. Memory cells give rapid response on re-exposure.", 3: "Pathogens can still enter — the vaccine means your immune system responds so fast the infection is cleared quickly."}},
            {"q": "How is malaria transmitted?",
             "opts": [("By Anopheles mosquito bites — mosquito is the vector for Plasmodium", True), ("By contaminated water", False), ("By breathing in droplets", False), ("By touching an infected person", False)],
             "wrong_explanations": {1: "Contaminated water transmits cholera and typhoid — not malaria.", 2: "Droplets transmit respiratory diseases like flu, COVID, measles — not malaria.", 3: "Malaria can't be caught by touch — it needs the mosquito to inject Plasmodium into the bloodstream."}},
            {"q": "What is herd immunity?",
             "opts": [("When enough people are vaccinated that the pathogen can't spread, protecting unvaccinated people too", True), ("When the whole herd of animals is vaccinated", False), ("When everyone has had the disease and recovered", False), ("When only children are vaccinated", False)],
             "wrong_explanations": {1: "Herd immunity applies to any population — not just animals.", 2: "Natural immunity from infection also contributes to herd immunity — but vaccination is safer.", 3: "Childhood vaccination is important — but herd immunity applies to the whole population."}},
            {"q": "Which white blood cell type produces antibodies?",
             "opts": [("Lymphocytes", True), ("Phagocytes", False), ("Red blood cells", False), ("Platelets", False)],
             "wrong_explanations": {1: "Phagocytes ENGULF and digest pathogens — they don't produce antibodies.", 2: "Red blood cells carry oxygen — they have no immune function.", 3: "Platelets are involved in blood clotting — not antibody production."}}
        ]
    },
],

"bioenergetics": [
    {
        "id": "photosynthesis",
        "title": "Photosynthesis",
        "spec": "4.4.1",
        "summary": "Describe photosynthesis, its equation and the factors that limit its rate.",
        "theory": [
            {"heading": "What is Photosynthesis?",
             "content": "Plants use light energy to convert CO₂ and water into glucose and oxygen.\nChloroplasts contain chlorophyll which absorbs light (mainly red and blue, reflects green).\nPhotosynthesis is ENDOTHERMIC — light energy is stored as chemical energy in glucose.\nOccurs in two stages: light reactions and the Calvin cycle (simplified at GCSE)."},
            {"heading": "The Word and Symbol Equation",
             "content": "Carbon dioxide + water → glucose + oxygen (using light energy).\n6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂\nGlucose is used for: respiration (energy), making cellulose (cell walls), making proteins, stored as starch."},
            {"heading": "Limiting Factors",
             "content": "If any one factor is in short supply, it limits the rate regardless of other conditions.\nLight intensity: more light → faster rate (up to a limit).\nCO₂ concentration: more CO₂ → faster rate (up to a limit).\nTemperature: higher temp → faster rate (up to ~40°C — then enzymes denature).\nAt high light and CO₂, temperature is often the limiting factor."},
            {"heading": "Inverse Square Law and Light",
             "content": "Light intensity ∝ 1/distance².\nDouble the distance → ¼ the light intensity.\nUsed in experiments: moving a lamp further reduces light intensity predictably.\nGreenhouses use artificial lighting and added CO₂ to maximise photosynthesis rate and crop yield."}
        ],
        "variables": [],
        "equations": ["6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (light energy)"],
        "common_mistake": "Photosynthesis only happens in LIGHT. Respiration happens ALL THE TIME (day and night). In bright light, rate of photosynthesis > rate of respiration → net O₂ release. At the compensation point they are equal.",
        "key_note": "Limiting factors: light intensity, CO₂ concentration, temperature. Any one can be the bottleneck.",
        "higher": "Inverse square law: light intensity = 1/d². Light-dependent reactions (chlorophyll absorbs light, produces ATP, splits water). Light-independent reactions (Calvin cycle — CO₂ fixed using ATP to make glucose).",
        "triple_only": None,
        "rp": "RP5 — Investigate the effect of light intensity on the rate of photosynthesis using aquatic plants (counting bubbles or measuring O₂).",
        "matching": {
            "title": "Match the Factor to How it Limits Photosynthesis",
            "instruction": "Match each factor to its role as a limiting factor.",
            "pairs": [
                ("Low light intensity", "Not enough energy to drive light reactions — rate is slow"),
                ("Low CO₂ concentration", "Not enough raw material for glucose production — rate is slow"),
                ("Low temperature", "Enzymes work slower — fewer collisions per second"),
                ("High temperature", "Enzymes denature — active sites change shape permanently"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What is the word equation for photosynthesis?",
             "opts": [("Carbon dioxide + water → glucose + oxygen", True), ("Glucose + oxygen → carbon dioxide + water", False), ("Carbon dioxide + glucose → water + oxygen", False), ("Water + oxygen → carbon dioxide + glucose", False)],
             "wrong_explanations": {1: "That's the equation for AEROBIC RESPIRATION — the reverse of photosynthesis!", 2: "Carbon dioxide and glucose are on different sides — CO₂ is a REACTANT, glucose is a PRODUCT.", 3: "Oxygen is a product — it comes FROM photosynthesis, it doesn't go in."}},
            {"q": "A plant is well-lit and has plenty of CO₂. What might now be the limiting factor?",
             "opts": [("Temperature", True), ("Light intensity", False), ("CO₂", False), ("Oxygen", False)],
             "wrong_explanations": {1: "Light is already plentiful — it's not the limiting factor.", 2: "CO₂ is plentiful — not limiting. When these are satisfied, temperature (enzyme rate) becomes the bottleneck.", 3: "Oxygen is a PRODUCT of photosynthesis — high O₂ doesn't limit the rate."}},
            {"q": "Where in the cell does photosynthesis take place?",
             "opts": [("Chloroplasts", True), ("Mitochondria", False), ("Nucleus", False), ("Vacuole", False)],
             "wrong_explanations": {1: "Mitochondria are for RESPIRATION — releasing energy from glucose. Chloroplasts are for photosynthesis.", 2: "The nucleus contains DNA — it controls the cell but doesn't carry out photosynthesis.", 3: "The vacuole stores cell sap — it's not involved in photosynthesis."}},
            {"q": "Why do plants appear green?",
             "opts": [("Chlorophyll reflects green light and absorbs red and blue light", True), ("They contain green pigments that produce green light", False), ("Green light makes them grow", False), ("All plants contain green water in their cells", False)],
             "wrong_explanations": {1: "Plants don't PRODUCE light — they reflect it. Chlorophyll reflects the green wavelengths we see.", 2: "Green light actually makes plants grow slightly slower — red and blue are most useful for photosynthesis.", 3: "Cell sap in vacuoles is usually colourless or slightly coloured — not green."}},
            {"q": "How is glucose used by plants after photosynthesis?",
             "opts": [("Respiration (energy), cellulose (cell walls), proteins, stored as starch", True), ("Immediately released as oxygen", False), ("Converted to carbon dioxide and excreted", False), ("Sent to roots as the only use", False)],
             "wrong_explanations": {1: "Oxygen is a PRODUCT of photosynthesis — not made from glucose.", 2: "CO₂ is exhaled in RESPIRATION but glucose is also used for many other things.", 3: "Glucose is used throughout the whole plant — not just in roots."}}
        ]
    },
    {
        "id": "respiration",
        "title": "Aerobic and Anaerobic Respiration",
        "spec": "4.4.2",
        "summary": "Describe and compare aerobic and anaerobic respiration.",
        "theory": [
            {"heading": "Aerobic Respiration",
             "content": "Glucose + oxygen → carbon dioxide + water (+ energy as ATP).\nC₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP.\nOccurs in MITOCHONDRIA.\nReleases large amount of energy — most efficient method.\nOccurs continuously in all living cells, day and night."},
            {"heading": "Anaerobic Respiration",
             "content": "Respiration WITHOUT oxygen — releases much less energy.\nIn animals/bacteria: glucose → lactic acid + small amount of ATP.\nIn yeast/plants: glucose → ethanol + CO₂ + small amount of ATP (fermentation).\nYeast fermentation is used for making bread (CO₂ makes dough rise) and alcohol (ethanol)."},
            {"heading": "Oxygen Debt",
             "content": "During intense exercise, not enough O₂ reaches muscles → anaerobic respiration → lactic acid builds up.\nLactic acid causes muscle fatigue and pain.\nAfter exercise: continue breathing hard — extra O₂ oxidises lactic acid to CO₂ and water.\nThis extra O₂ needed = oxygen debt (excess post-exercise oxygen consumption, EPOC)."},
            {"heading": "Response to Exercise",
             "content": "Heart rate increases — delivers more O₂ and glucose to muscles.\nBreathing rate and depth increase — takes in more O₂, removes more CO₂.\nBlood flow redirected to muscles.\nAfter prolonged exercise: glycogen (stored glucose in muscles and liver) depleted."}
        ],
        "variables": [],
        "equations": [
            "Aerobic: glucose + oxygen → carbon dioxide + water",
            "Anaerobic (animals): glucose → lactic acid",
            "Anaerobic (yeast): glucose → ethanol + carbon dioxide"
        ],
        "common_mistake": "Anaerobic respiration in ANIMALS produces LACTIC ACID. Anaerobic respiration in YEAST produces ETHANOL + CO₂. These are different products — students often mix them up!",
        "key_note": "Aerobic = lots of ATP, needs O₂. Anaerobic = little ATP, no O₂ needed. Both start with glucose.",
        "higher": "ATP is the immediate energy currency of cells. Glucose → ATP via respiration → ATP drives cell processes (muscle contraction, active transport, protein synthesis).",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Aerobic or Anaerobic?",
            "instruction": "Sort each statement into aerobic or anaerobic respiration.",
            "pairs": [
                ("Aerobic", "Needs oxygen, occurs in mitochondria, produces lots of ATP"),
                ("Anaerobic — animals", "No oxygen, produces lactic acid, causes muscle fatigue"),
                ("Anaerobic — yeast", "No oxygen, produces ethanol + CO₂, used in brewing and baking"),
                ("Both", "Starts with glucose"),
                ("Aerobic", "Produces CO₂ and water as waste products"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Where does aerobic respiration take place in cells?",
             "opts": [("Mitochondria", True), ("Nucleus", False), ("Chloroplasts", False), ("Cell membrane", False)],
             "wrong_explanations": {1: "Nucleus contains DNA — it doesn't carry out respiration.", 2: "Chloroplasts do PHOTOSYNTHESIS. Mitochondria do respiration.", 3: "Cell membrane controls transport — respiration occurs in mitochondria."}},
            {"q": "What is produced by anaerobic respiration in yeast?",
             "opts": [("Ethanol and carbon dioxide", True), ("Lactic acid", False), ("Glucose and oxygen", False), ("Carbon dioxide and water", False)],
             "wrong_explanations": {1: "Lactic acid is produced by ANIMAL muscles — not yeast. Yeast produces ethanol + CO₂.", 2: "Glucose + oxygen are REACTANTS in aerobic respiration — not products of anaerobic.", 3: "CO₂ + water = AEROBIC respiration. Anaerobic in yeast = ethanol + CO₂."}},
            {"q": "What causes the 'burning' feeling in muscles during intense exercise?",
             "opts": [("Lactic acid build-up from anaerobic respiration", True), ("Oxygen being used up too fast", False), ("Glucose being depleted", False), ("Mitochondria overheating", False)],
             "wrong_explanations": {1: "Oxygen depletion triggers anaerobic respiration — but the burning sensation is specifically from LACTIC ACID accumulation.", 2: "Glucose depletion causes tiredness and 'hitting the wall' — but burning feeling = lactic acid.", 3: "Mitochondria don't overheat — the burning is a chemical effect of lactic acid lowering pH in muscles."}},
            {"q": "What is oxygen debt?",
             "opts": [("Extra O₂ needed after exercise to oxidise lactic acid back to CO₂ and water", True), ("The amount of O₂ missing from the blood", False), ("The O₂ stored in muscles before exercise", False), ("The difference in O₂ between inhaled and exhaled air", False)],
             "wrong_explanations": {1: "O₂ levels in blood vary — oxygen debt specifically refers to post-exercise O₂ needed to process lactic acid.", 2: "Myoglobin in muscles stores O₂ — oxygen debt is about post-exercise metabolism of lactic acid.", 3: "O₂ difference between inhaled/exhaled air is related to metabolic rate — oxygen debt is specifically post-exercise."}},
            {"q": "Which type of respiration releases the most energy from glucose?",
             "opts": [("Aerobic — produces about 36-38 ATP per glucose", True), ("Anaerobic — faster so releases more energy", False), ("They release the same amount", False), ("Anaerobic — produces lactic acid which has more energy", False)],
             "wrong_explanations": {1: "Anaerobic is faster at producing ATP in a crisis — but produces only 2 ATP per glucose vs ~36 for aerobic.", 2: "They don't release the same: aerobic ≈ 36-38 ATP per glucose, anaerobic ≈ 2 ATP.", 3: "Lactic acid is a waste product containing unused chemical energy — but anaerobic releases far less usable ATP."}}
        ]
    },
],

"homeostasis": [
    {
        "id": "nervous-system",
        "title": "The Nervous System and Homeostasis",
        "spec": "4.5",
        "summary": "Describe the nervous system, reflex arc and principles of homeostasis.",
        "theory": [
            {"heading": "What is Homeostasis?",
             "content": "Homeostasis = maintaining a constant internal environment.\nControlled conditions: body temperature (37°C), blood glucose levels, water balance.\nNegative feedback: if a variable goes above/below the set point, the system responds to bring it back.\nInvolves: receptor (detects change), coordination centre (processes signal), effector (muscle or gland responds)."},
            {"heading": "The Nervous System",
             "content": "Central nervous system (CNS): brain + spinal cord — processes information.\nPeripheral nervous system: sensory and motor neurones connecting CNS to body.\nSensory neurone: carries signal FROM receptor TO CNS.\nMotor neurone: carries signal FROM CNS TO effector (muscle/gland).\nRelay neurone: connects sensory and motor neurones in the CNS."},
            {"heading": "Synapses",
             "content": "Gap between neurones — signals can't jump across electrically.\nNeurotransmitters released from one neurone → diffuse across gap → bind to receptors on next neurone.\nOne-way transmission — neurotransmitters only released in one direction.\nDrugs can affect synapses: stimulants increase neurotransmitter release; sedatives block receptors."},
            {"heading": "The Reflex Arc",
             "content": "Reflex = fast, automatic response to stimulus — bypasses conscious brain.\nPathway: stimulus → receptor → sensory neurone → relay neurone (in spinal cord) → motor neurone → effector (muscle/gland).\nFaster than a voluntary response — protects from harm.\nExamples: knee-jerk reflex, pupil response to light, withdrawing hand from hot object."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A reflex arc goes through the SPINAL CORD (or brainstem), not the thinking brain. That's why reflexes are faster — they don't wait for conscious processing. Students often say 'the brain controls reflexes' — it doesn't (except for certain brainstem reflexes).",
        "key_note": "Reflex order: stimulus → receptor → sensory neurone → relay neurone → motor neurone → effector → response.",
        "higher": "The brain: cerebral cortex (thinking, memory), cerebellum (balance, coordination), medulla oblongata (breathing, heart rate). Brain mapping via MRI and stimulation experiments.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Component to its Role",
            "instruction": "Match each part of the nervous system to its function.",
            "pairs": [
                ("Receptor", "Detects a stimulus (change in environment)"),
                ("Sensory neurone", "Carries impulse from receptor to CNS"),
                ("Relay neurone", "Connects sensory and motor neurones in CNS"),
                ("Motor neurone", "Carries impulse from CNS to effector"),
                ("Effector", "Muscle or gland — produces the response"),
                ("Synapse", "Gap between neurones — signals cross via neurotransmitters"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What is homeostasis?",
             "opts": [("Maintaining a stable internal environment using negative feedback", True), ("Increasing body temperature when hot", False), ("Removing waste products from the body", False), ("Regulating body size", False)],
             "wrong_explanations": {1: "Increasing temperature when hot is the PROBLEM — homeostasis CORRECTS it back to normal.", 2: "Excretion is important but homeostasis specifically refers to maintaining STABLE CONDITIONS.", 3: "Body size isn't regulated by homeostasis — it's controlled by genetics and nutrition."}},
            {"q": "What is the correct order of a reflex arc?",
             "opts": [("Stimulus → receptor → sensory neurone → relay neurone → motor neurone → effector", True), ("Stimulus → brain → motor neurone → effector", False), ("Effector → receptor → motor neurone → response", False), ("Receptor → brain → spinal cord → effector", False)],
             "wrong_explanations": {1: "Reflexes BYPASS the conscious brain — they go through the spinal cord, not the cerebral cortex.", 2: "The pathway goes forward — receptors detect, then neurones carry signals to effectors.", 3: "The reflex goes through the SPINAL CORD but it doesn't go up to the brain first — that's the key to its speed."}},
            {"q": "How does a synapse allow a signal to pass from one neurone to the next?",
             "opts": [("Neurotransmitters released, diffuse across gap, bind to receptors on next neurone", True), ("Electrical signal jumps directly across the gap", False), ("The two neurones fuse together", False), ("Blood carries the signal across the gap", False)],
             "wrong_explanations": {1: "The synapse is specifically a GAP — electricity can't jump across. It must use chemical neurotransmitters.", 2: "Neurones never physically fuse — the synapse is always maintained as a gap.", 3: "Signal transmission in nerves is far too fast for blood transport — it uses chemical neurotransmitters."}},
            {"q": "Why are reflexes faster than voluntary responses?",
             "opts": [("They bypass the conscious brain — processed in the spinal cord", True), ("Reflex neurones are longer", False), ("Reflexes use more neurotransmitters", False), ("The brain processes reflex signals first", False)],
             "wrong_explanations": {1: "Longer neurones = slower, not faster. Reflexes are fast because of the SHORT pathway through the spinal cord.", 2: "More neurotransmitters would actually slow things down slightly — speed comes from fewer synapses and bypassing the brain.", 3: "The brain does receive information AFTER the reflex has occurred — it's aware of it, but doesn't initiate the response."}}
        ]
    },
    {
        "id": "endocrine-system",
        "title": "The Endocrine System and Blood Glucose",
        "spec": "4.5.3",
        "summary": "Describe how hormones regulate blood glucose and compare nervous and hormonal control.",
        "theory": [
            {"heading": "The Endocrine System",
             "content": "Hormones = chemical messengers secreted by glands into the blood.\nCarried by blood to target organs — slower than nerves but longer-lasting effects.\nPituitary gland: 'master gland' — controls other glands (releases FSH, LH, ADH etc).\nAdrenal gland: adrenaline (fight or flight response).\nPancreas: insulin and glucagon (blood glucose control).\nThyroid: thyroxine (metabolism)."},
            {"heading": "Blood Glucose Regulation",
             "content": "After eating: blood glucose RISES → pancreas releases INSULIN.\nInsulin: causes liver and muscles to convert glucose → glycogen (storage). Blood glucose falls.\nIf too low: pancreas releases GLUCAGON → liver converts glycogen back to glucose. Blood glucose rises.\nThis is negative feedback — maintains blood glucose at ~5 mmol/L."},
            {"heading": "Diabetes",
             "content": "Type 1 diabetes: pancreas produces little/no insulin (autoimmune). Treated with insulin injections.\nType 2 diabetes: cells become resistant to insulin. Linked to obesity, poor diet.\nTreated with: diet, exercise, tablets (sometimes insulin).\nBoth types cause dangerously high blood glucose if untreated — damage to blood vessels, nerves, kidneys, eyes."},
            {"heading": "Nervous vs Hormonal Control",
             "content": "Nervous: electrical signals along neurones, fast, short duration, precise target.\nHormonal: chemicals in blood, slower, longer lasting, affects many target organs.\nBoth work together: e.g. adrenaline (hormonal) prepares the body for emergency while nervous system coordinates the response."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "INSULIN causes blood glucose to FALL (glucose → glycogen storage). GLUCAGON causes blood glucose to RISE (glycogen → glucose released). Students often confuse which hormone does which.",
        "key_note": "Insulin: blood glucose too high → falls. Glucagon: blood glucose too low → rises. Negative feedback.",
        "higher": "ADH and water balance: ADH from pituitary controls kidney water reabsorption. More ADH → more water reabsorbed → small amount of concentrated urine.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Gland to its Hormone and Function",
            "instruction": "Match each gland to the hormone it produces and its effect.",
            "pairs": [
                ("Pancreas (β cells)", "Insulin — lowers blood glucose by promoting glycogen storage"),
                ("Pancreas (α cells)", "Glucagon — raises blood glucose by breaking down glycogen"),
                ("Adrenal gland", "Adrenaline — fight or flight, increases heart rate and breathing"),
                ("Pituitary gland", "FSH and LH — control menstrual cycle and reproduction"),
                ("Thyroid gland", "Thyroxine — controls metabolic rate"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Blood glucose rises after a meal. Which hormone is released?",
             "opts": [("Insulin", True), ("Glucagon", False), ("Adrenaline", False), ("Thyroxine", False)],
             "wrong_explanations": {1: "Glucagon is released when glucose is TOO LOW — it raises blood glucose.", 2: "Adrenaline is the fight-or-flight hormone — not involved in routine blood glucose control.", 3: "Thyroxine controls metabolic rate — not blood glucose levels."}},
            {"q": "A person with Type 1 diabetes doesn't produce insulin. What happens if untreated?",
             "opts": [("Blood glucose stays dangerously high — damages blood vessels and organs", True), ("Blood glucose becomes dangerously low", False), ("The pancreas produces extra glucagon to compensate", False), ("No symptoms — insulin isn't essential", False)],
             "wrong_explanations": {1: "Without insulin, glucose can't enter cells easily — it STAYS HIGH in the blood, causing damage.", 2: "Glucagon would be produced — but without insulin to balance it, glucose just keeps rising.", 3: "Insulin is absolutely essential — without it, cells starve and blood glucose becomes toxic."}},
            {"q": "How does insulin reduce blood glucose?",
             "opts": [("Causes liver and muscle cells to convert glucose into glycogen for storage", True), ("Causes the kidneys to excrete excess glucose", False), ("Causes cells to burn glucose faster", False), ("Blocks glucagon from working", False)],
             "wrong_explanations": {1: "The kidneys do excrete glucose in diabetes — but insulin's mechanism is specifically glycogen STORAGE.", 2: "Respiration does increase with insulin signalling — but the primary mechanism is glycogen synthesis.", 3: "Insulin and glucagon are both active — insulin doesn't directly block glucagon."}},
            {"q": "How does hormonal communication differ from nervous communication?",
             "opts": [("Hormones travel in blood — slower but longer lasting and affect many target organs", True), ("Hormones travel faster than nerve signals", False), ("Hormones only affect one specific cell", False), ("Nervous signals are permanent; hormones are temporary", False)],
             "wrong_explanations": {1: "Hormones are SLOWER — nerve signals travel at up to 120 m/s, hormones travel at blood flow speed.", 2: "Hormones travel in blood to MANY organs. Nerve signals are specific to the cells the nerve connects to.", 3: "Both are temporary — but hormonal effects tend to last longer (minutes to hours vs milliseconds for nerves)."}}
        ]
    },
],

"inheritance": [
    {
        "id": "dna-genetics",
        "title": "DNA, Inheritance and Genetic Crosses",
        "spec": "4.6",
        "summary": "Describe DNA structure, inheritance patterns and construct Punnett squares.",
        "theory": [
            {"heading": "DNA and Genes",
             "content": "DNA (deoxyribonucleic acid) is a double helix polymer of nucleotides.\nLocated in chromosomes in the nucleus.\nA gene = a section of DNA that codes for a specific protein.\nHumans have 46 chromosomes (23 pairs).\nAlleles = different versions of the same gene (e.g. blue eye allele vs brown eye allele)."},
            {"heading": "Dominant and Recessive Alleles",
             "content": "Dominant allele (written as capital letter, e.g. B): expressed even if only one copy is present.\nRecessive allele (lower case, e.g. b): only expressed if TWO copies are present.\nGenotype: the alleles present (e.g. BB, Bb, bb).\nPhenotype: the observable characteristic (e.g. brown eyes, blue eyes).\nHomozygous: both alleles the same (BB or bb). Heterozygous: different alleles (Bb)."},
            {"heading": "Punnett Squares",
             "content": "A grid used to predict offspring ratios.\nExample: Bb × Bb (both parents heterozygous):\nOffspring: BB (1), Bb (2), bb (1) → 3:1 ratio of dominant:recessive phenotype.\n75% show dominant phenotype. 25% show recessive.\nBb is a 'carrier' — has the recessive allele but doesn't show it."},
            {"heading": "Inherited Diseases",
             "content": "Cystic fibrosis: caused by recessive allele (f). Affects cell membranes → thick mucus in lungs/gut.\nPolydactyly: caused by dominant allele (P). Extra fingers/toes.\nSickle cell anaemia: recessive. Abnormal haemoglobin → sickle-shaped red blood cells.\nGenetic testing can identify carriers — ethical considerations around privacy and insurance."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "A carrier of a recessive condition (Ff) has the allele but does NOT show the disease — they appear normal but can pass it on. Two carriers have a 25% chance of an affected child. Students often say carriers 'have the disease mildly' — wrong!",
        "key_note": "Dominant (capital) = shown if even one copy. Recessive (lowercase) = only shown if two copies present.",
        "higher": "Sex determination: females = XX, males = XY. Sperm determine sex — 50% carry X, 50% carry Y. X-linked inheritance: recessive alleles on the X chromosome affect males more (only one X).",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Genetics Vocabulary Match",
            "instruction": "Match each term to its correct definition.",
            "pairs": [
                ("Genotype", "The alleles present in an organism (e.g. Bb)"),
                ("Phenotype", "The observable characteristic expressed (e.g. brown eyes)"),
                ("Homozygous", "Both alleles are the same (BB or bb)"),
                ("Heterozygous", "Alleles are different (Bb)"),
                ("Dominant allele", "Expressed even if only one copy is present"),
                ("Recessive allele", "Only expressed if two copies are present"),
                ("Carrier", "Has one recessive allele but doesn't show the condition"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "In the cross Bb × Bb, what fraction of offspring will show the recessive phenotype (bb)?",
             "opts": [("1/4 (25%)", True), ("1/2 (50%)", False), ("3/4 (75%)", False), ("0% — recessive can't appear if parents are heterozygous", False)],
             "wrong_explanations": {1: "50% would be the chance if one parent was homozygous recessive. Bb × Bb gives 1 BB : 2 Bb : 1 bb = 25% bb.", 2: "75% show the DOMINANT phenotype (BB and Bb). Only 25% are bb.", 3: "Two carriers can absolutely produce a recessive child — 25% chance (bb)."}},
            {"q": "Cystic fibrosis is caused by a recessive allele (f). Two carriers (Ff × Ff) have a child. What are the chances of the child being affected?",
             "opts": [("25%", True), ("50%", False), ("75%", False), ("0% — carriers can't have affected children", False)],
             "wrong_explanations": {1: "50% would mean the trait is dominant or one parent is homozygous — Ff × Ff gives 25% ff (affected).", 2: "75% is the UNAFFECTED proportion. Only 25% (ff) will be affected.", 3: "Carriers absolutely CAN have affected children — 25% chance with two carriers."}},
            {"q": "What is a dominant allele?",
             "opts": [("Expressed in the phenotype even if only one copy is present", True), ("Only expressed when two copies are present", False), ("A stronger, better version of a gene", False), ("An allele that causes disease", False)],
             "wrong_explanations": {1: "Only expressed when two copies = RECESSIVE allele.", 2: "Dominant and recessive don't imply 'better' or 'stronger' — they're just expression patterns.", 3: "Dominant alleles can cause disease (polydactyly) or be normal — 'dominant' refers to expression pattern."}},
            {"q": "What is the sex chromosome combination in a human male?",
             "opts": [("XY", True), ("XX", False), ("YY", False), ("X only", False)],
             "wrong_explanations": {1: "XX = FEMALE. Males have one X and one Y chromosome.", 2: "YY is not viable — sperm carry either X or Y, but the egg always contributes X.", 3: "X only = Turner syndrome (a condition) — normal males are XY."}},
            {"q": "A child inherits cystic fibrosis. Both parents appear healthy. What are the parents' genotypes?",
             "opts": [("Both parents are carriers — Ff × Ff", True), ("One parent is FF, one is ff", False), ("Both parents are FF", False), ("One parent has CF — Ff × ff", False)],
             "wrong_explanations": {1: "If one parent is ff, they would HAVE cystic fibrosis and appear unwell — the question says both parents are healthy.", 2: "If both parents are FF, all children would be FF — impossible to have an ff child.", 3: "Both parents appear healthy but have the condition — only Ff × Ff allows healthy parents to have an ff child."}}
        ]
    },
    {
        "id": "evolution-classification",
        "title": "Evolution, Natural Selection and Classification",
        "spec": "4.6.4",
        "summary": "Describe natural selection, evidence for evolution and modern classification.",
        "theory": [
            {"heading": "Darwin's Theory of Natural Selection",
             "content": "1. All organisms show variation (differences in characteristics).\n2. All populations overproduce offspring — struggle for survival.\n3. Some variants are better adapted to the environment — greater chance of survival.\n4. Better-adapted individuals survive and reproduce — passing on favourable alleles.\n5. Over many generations, advantageous traits become more common in the population."},
            {"heading": "Evidence for Evolution",
             "content": "Fossil record: shows gradual changes in organisms over time.\nAntibiotic resistance: bacteria evolve resistance rapidly — direct observation of natural selection.\nHomologous structures: similar bone structure in different organisms (e.g. human arm, whale flipper, bat wing) suggest common ancestor.\nDNA comparisons: closely related species have more similar DNA sequences."},
            {"heading": "Classification",
             "content": "Traditional classification: based on physical characteristics (Linnaeus, 1700s).\nModern classification: based on evolutionary relationships and DNA evidence.\nThe five kingdoms (simplified): animals, plants, fungi, prokaryotes, protists.\nBinomial nomenclature: two-part Latin name — genus + species (e.g. Homo sapiens).\nPhylogenetic trees show evolutionary relationships between species."},
            {"heading": "Selective Breeding and Genetic Engineering",
             "content": "Selective breeding: humans choose organisms with desired traits to breed together.\nOver generations: traits enhanced (e.g. large wheat seeds, docile cattle, fast racehorses).\nGenetic engineering: inserting a specific gene into an organism's DNA.\nExamples: insulin-producing bacteria (human insulin gene inserted), GM crops (herbicide resistant, higher yield).\nBoth have ethical considerations — reducing genetic diversity, unknown long-term effects."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Natural selection acts on VARIATION that already EXISTS in a population — it does NOT cause mutations. Evolution is the change in allele frequency over many generations. Individuals don't evolve; populations do.",
        "key_note": "Natural selection: variation → selection pressure → survival of the fittest → reproduction → allele frequency changes over generations.",
        "higher": "Speciation: populations become reproductively isolated (geographic barrier etc) → different selection pressures → allele frequencies diverge → can no longer interbreed = new species.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Evidence to what it Supports",
            "instruction": "Match each piece of evidence to what it demonstrates about evolution.",
            "pairs": [
                ("Fossil record", "Shows gradual changes in organisms over millions of years"),
                ("Antibiotic resistance in bacteria", "Direct observation of natural selection happening rapidly"),
                ("Homologous structures (e.g. limb bones)", "Similar bone structure in different species suggests common ancestor"),
                ("DNA sequence comparisons", "More similar DNA = more closely related species"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What provides the variation in a population that natural selection acts on?",
             "opts": [("Mutations and sexual reproduction", True), ("Natural selection itself creates variation", False), ("All members of a species are identical", False), ("The environment creates new traits directly", False)],
             "wrong_explanations": {1: "Natural selection SELECTS from existing variation — it doesn't create it.", 2: "Members of a species show variation in traits — that's what makes selection possible.", 3: "The environment selects for or against traits — it doesn't directly change DNA to create new traits."}},
            {"q": "Bacteria develop antibiotic resistance. How does this happen through natural selection?",
             "opts": [("Resistant mutations already existed — antibiotic kills non-resistant bacteria, resistant ones survive and reproduce", True), ("Bacteria learn to resist antibiotics over time", False), ("Antibiotics cause bacteria to mutate into resistant forms", False), ("All bacteria become resistant at the same time", False)],
             "wrong_explanations": {1: "Bacteria don't 'learn' — they can't choose. Natural selection: pre-existing resistant variants survive.", 2: "Antibiotics don't cause mutations — they select FROM pre-existing mutations.", 3: "Resistance spreads through the population as resistant bacteria have more offspring — not all at once."}},
            {"q": "What is binomial nomenclature?",
             "opts": [("A two-part Latin naming system — genus + species (e.g. Homo sapiens)", True), ("A system based on counting chromosomes", False), ("Classification into five kingdoms", False), ("A method of measuring biodiversity", False)],
             "wrong_explanations": {1: "Chromosome counting is a technique in genetics — not the naming system.", 2: "Five kingdoms is a classification SYSTEM — binomial nomenclature is specifically about the two-part name.", 3: "Biodiversity indices measure variety of species — binomial nomenclature is the naming convention."}},
            {"q": "Human arms, whale flippers and bat wings have similar bone structures. What does this suggest?",
             "opts": [("They share a common ancestor — the bones evolved differently for different functions", True), ("All species developed the same bones independently", False), ("The bones are made of the same material", False), ("These species all live in similar environments", False)],
             "wrong_explanations": {1: "Convergent evolution can produce similar structures independently — but homologous structures (same bones, different functions) specifically suggest common ancestry.", 2: "All bones are made of similar materials (calcium phosphate) — but structure is what matters here.", 3: "Bats fly, humans walk, whales swim — very different environments. The shared bone structure points to ancestry, not environment."}}
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
