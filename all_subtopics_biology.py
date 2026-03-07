#!/usr/bin/env python3
"""Biology subtopics — all topics"""

BIOLOGY_COLOR = "#6BCB77"

BIOLOGY_SUBTOPICS_ALL = {

"cell-biology": [
    {
        "id": "cell-structure",
        "title": "Animal, Plant and Prokaryotic Cells",
        "spec": "4.1.1",
        "summary": "Describe the structure and function of animal, plant and prokaryotic cells.",
        "theory": [
            {"heading": "Animal Cells — The Basics",
             "content": "Nucleus: contains DNA — controls cell activity.\nCell membrane: controls what enters and leaves.\nCytoplasm: where most chemical reactions happen.\nMitochondria: site of aerobic respiration — produces ATP energy.\nRibosomes: where proteins are made."},
            {"heading": "Plant Cells — Extra Components",
             "content": "All animal cell components PLUS:\nCell wall: made of cellulose — provides support and shape.\nChloroplasts: contain chlorophyll — absorb light for photosynthesis.\nPermanent vacuole: filled with cell sap — helps maintain cell shape (turgor pressure).\nSome plant cells lack chloroplasts (e.g. root cells — no light underground)."},
            {"heading": "Prokaryotic Cells (Bacteria)",
             "content": "Much smaller than eukaryotic cells.\nNO nucleus — DNA is a single loop in the cytoplasm.\nNO membrane-bound organelles.\nHave: cell membrane, cell wall (not cellulose), cytoplasm, ribosomes.\nMay have: plasmids (small circular DNA loops), flagella (tail for movement), capsule (slime layer)."},
            {"heading": "Microscopy",
             "content": "Light microscopes: use light — max magnification ~×2000, can see cells and large organelles.\nElectron microscopes: use electrons — max magnification ~×2,000,000, can see mitochondria, ribosomes in detail.\nMagnification = image size ÷ actual size.\nResolution: ability to distinguish two close points as separate — electron microscopes have much higher resolution."}
        ],
        "variables": [
            ("M", "Magnification", "no unit", "×"),
            ("I", "Image size", "millimetres or micrometres", "mm / µm"),
            ("A", "Actual size", "millimetres or micrometres", "mm / µm"),
        ],
        "equations": ["Magnification = image size ÷ actual size"],
        "common_mistake": "Plant cells don't ALL have chloroplasts — only cells that are exposed to light. Root cells and storage cells don't have them. Also — prokaryotic cells have NO nucleus and NO membrane-bound organelles.",
        "key_note": "1 mm = 1000 µm. 1 µm = 1000 nm. Scale bars on micrographs are your friend — use them to calculate actual size.",
        "higher": "Culturing bacteria: aseptic technique — sterilise equipment, work near Bunsen, seal petri dishes. Inhibition zones show antibiotic effectiveness.",
        "triple_only": None, "rp": "RP1 — Use a light microscope to observe and draw plant or animal cells. Calculate magnification.",
        "matching": {
            "title": "Match the Organelle to its Function",
            "instruction": "Match each cell component to its correct function.",
            "pairs": [
                ("Nucleus", "Contains DNA — controls cell activity"),
                ("Mitochondria", "Site of aerobic respiration — releases energy (ATP)"),
                ("Ribosomes", "Where proteins are synthesised"),
                ("Chloroplasts", "Absorb light energy for photosynthesis"),
                ("Cell wall", "Provides structural support (plant cells only)"),
                ("Vacuole", "Stores cell sap, helps maintain turgor pressure"),
            ]
        },
        "fifas": [
            {"label": "Example — Magnification calculation",
             "question": "A cell appears 30 mm in a drawing. The actual cell is 0.03 mm. Calculate the magnification.",
             "steps": [("F","Magnification = image size ÷ actual size"), ("I","Magnification = 30 ÷ 0.03"), ("F","Both measurements in same units (mm)"), ("A","Magnification = ×1000")]}
        ],
        "quiz": [
            {"q": "Which organelle is the site of aerobic respiration?",
             "opts": [("Mitochondria", True), ("Nucleus", False), ("Ribosome", False), ("Chloroplast", False)],
             "wrong_explanations": {1: "The nucleus contains DNA — it controls the cell but doesn't do respiration.", 2: "Ribosomes make proteins — not involved in energy release.", 3: "Chloroplasts do photosynthesis — they capture energy, not release it via respiration."}},
            {"q": "Which feature is present in plant cells but NOT animal cells?",
             "opts": [("Cell wall", True), ("Cell membrane", False), ("Mitochondria", False), ("Nucleus", False)],
             "wrong_explanations": {1: "Animal cells have a cell membrane — but no cell wall.", 2: "Both animal and plant cells have mitochondria for respiration.", 3: "Both have a nucleus containing DNA."}},
            {"q": "What is the key difference between prokaryotic and eukaryotic cells?",
             "opts": [("Prokaryotes have no nucleus — DNA floats free in cytoplasm", True), ("Prokaryotes are larger", False), ("Prokaryotes have more mitochondria", False), ("Prokaryotes have no cell membrane", False)],
             "wrong_explanations": {1: "Prokaryotes are SMALLER than eukaryotic cells.", 2: "Prokaryotes have NO membrane-bound organelles including mitochondria.", 3: "Prokaryotes DO have a cell membrane — it's the nucleus they lack."}},
            {"q": "A cell appears 15 mm under a microscope. Actual size = 0.015 mm. What is the magnification?",
             "opts": [("×1000", True), ("×100", False), ("×10", False), ("×0.001", False)],
             "wrong_explanations": {1: "You divided by a wrong value. M = image ÷ actual = 15 ÷ 0.015 = 1000.", 2: "Check your division: 15 ÷ 0.015 = 1000, not 10.", 3: "You divided actual by image. M = IMAGE ÷ actual = 15 ÷ 0.015 = 1000."}},
            {"q": "Why don't root cells have chloroplasts?",
             "opts": [("They are underground — no light for photosynthesis", True), ("Roots don't need energy", False), ("Root cells are prokaryotic", False), ("Chloroplasts only form in summer", False)],
             "wrong_explanations": {1: "Roots absolutely need energy — they get it from respiration, not photosynthesis.", 2: "All cells are eukaryotic in plants — root cells are plant eukaryotic cells.", 3: "Chloroplasts are permanent organelles — they don't appear seasonally."}}
        ]
    },
    {
        "id": "transport-in-cells",
        "title": "Diffusion, Osmosis and Active Transport",
        "spec": "4.1.3",
        "summary": "Describe and compare diffusion, osmosis and active transport across cell membranes.",
        "theory": [
            {"heading": "Diffusion",
             "content": "Diffusion = net movement of particles from HIGH concentration to LOW concentration.\nDown the concentration gradient — no energy required (passive).\nFaster if: higher concentration gradient, higher temperature, shorter distance, larger surface area.\nExamples: O₂ into cells, CO₂ out of cells, glucose into cells from gut."},
            {"heading": "Osmosis",
             "content": "Osmosis = diffusion of WATER molecules across a partially permeable membrane.\nWater moves from dilute solution (high water potential) to concentrated solution (low water potential).\nDown the water potential gradient — passive, no energy needed.\nPlant cells in dilute solution → swell → turgor (firm).\nPlant cells in concentrated solution → shrink → plasmolysis."},
            {"heading": "Active Transport",
             "content": "Movement of substances from LOW to HIGH concentration — against the gradient.\nRequires ENERGY (ATP from respiration) and carrier proteins.\nExamples: mineral ions from soil into root hair cells; glucose from gut into blood.\nIf respiration is inhibited, active transport stops — unlike diffusion and osmosis."},
            {"heading": "Exchange Surfaces",
             "content": "Efficient exchange surfaces have:\nLarge surface area (many folds/villi).\nThin membrane (short diffusion distance).\nConcentration gradient maintained (good blood supply, ventilation).\nExamples: alveoli in lungs, villi in small intestine, root hair cells in plants."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Osmosis is a SPECIAL TYPE of diffusion — only water molecules, across a partially permeable membrane. Active transport goes AGAINST the gradient and needs ENERGY. Diffusion and osmosis are both passive (no energy needed).",
        "key_note": "Diffusion and osmosis: passive (no ATP). Active transport: needs ATP from respiration.",
        "higher": "Water potential: more solute = lower water potential. Osmosis moves water from high to low water potential. Turgor pressure: plant cell wall resists swelling — provides firmness.",
        "triple_only": None, "rp": "RP2 — Investigate osmosis in plant tissue (e.g. potato cylinders in different concentrations of sugar solution).",
        "matching": {
            "title": "Match the Process to its Description",
            "instruction": "Match diffusion, osmosis or active transport to each description.",
            "pairs": [
                ("Diffusion", "Movement of particles from high to low concentration — passive"),
                ("Osmosis", "Movement of water from dilute to concentrated solution across a membrane — passive"),
                ("Active transport", "Movement against concentration gradient — requires ATP energy"),
                ("Diffusion", "CO₂ moving out of a respiring cell"),
                ("Osmosis", "Water entering a plant root hair cell from the soil"),
                ("Active transport", "Mineral ions absorbed from soil into root cells against a gradient"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Which process requires energy (ATP) to move substances?",
             "opts": [("Active transport", True), ("Diffusion", False), ("Osmosis", False), ("Both diffusion and osmosis", False)],
             "wrong_explanations": {1: "Diffusion is passive — it moves down the concentration gradient without energy.", 2: "Osmosis is a type of diffusion — also passive, no ATP needed.", 3: "Both are passive processes — active transport is the only one needing ATP."}},
            {"q": "A potato chip is placed in a very concentrated salt solution. What happens?",
             "opts": [("It shrinks — water leaves by osmosis", True), ("It swells — water enters by osmosis", False), ("It gains mass — salt enters by diffusion", False), ("Nothing happens", False)],
             "wrong_explanations": {1: "Water moves from the DILUTE side (inside the potato, more water) to the CONCENTRATED side (salt solution). Potato shrinks.", 2: "Salt ions can't easily enter through the partially permeable membrane. The mass change is due to water leaving.", 3: "The concentration difference is a strong driving force — osmosis definitely occurs."}},
            {"q": "Why must active transport stop if respiration is inhibited?",
             "opts": [("Active transport requires ATP from respiration — no respiration = no ATP = no active transport", True), ("Inhibiting respiration changes the concentration gradient", False), ("Respiration controls cell membrane permeability", False), ("Active transport and respiration share the same proteins", False)],
             "wrong_explanations": {1: "Inhibiting respiration doesn't directly change concentration gradients — it removes the energy supply.", 2: "Membrane permeability is relatively constant — active transport stops because it has no fuel.", 3: "They have separate proteins — the shared requirement is ATP, which respiration produces."}},
            {"q": "What makes the small intestine efficient at absorbing nutrients?",
             "opts": [("Villi give a large surface area; thin walls give short diffusion distance; blood supply maintains gradient", True), ("It is very long only", False), ("It contains acid to break down food", False), ("It is very wide", False)],
             "wrong_explanations": {1: "Length helps but alone isn't the key — villi increase surface area and blood supply maintains the gradient.", 2: "Acid is in the STOMACH — the small intestine is alkaline to allow enzyme activity.", 3: "Width would help slightly but the crucial adaptations are villi, thin walls and blood supply."}},
            {"q": "What happens to a plant cell placed in pure water?",
             "opts": [("It becomes turgid — water enters by osmosis, cell wall prevents bursting", True), ("It bursts", False), ("It shrinks", False), ("Nothing changes", False)],
             "wrong_explanations": {1: "Animal cells can burst (lyse) in pure water — plant cells have a rigid cell wall that prevents this.", 2: "Shrinking = plasmolysis — that happens in concentrated solutions. In pure water, water ENTERS.", 3: "The concentration gradient between cell cytoplasm and pure water drives osmosis — water definitely enters."}}
        ]
    },
    {
        "id": "cell-division",
        "title": "Cell Division — Mitosis and Stem Cells",
        "spec": "4.1.4",
        "summary": "Describe mitosis, the cell cycle and the role of stem cells.",
        "theory": [
            {"heading": "The Cell Cycle and Mitosis",
             "content": "Mitosis = cell division producing two genetically identical daughter cells.\nUsed for: growth, repair of tissues, replacement of worn-out cells.\nBefore division: DNA is replicated (copied) — so each new cell gets a full set.\nStages: interphase (growth + DNA replication) → mitosis (division) → two daughter cells.\nEach daughter cell has the same chromosome number as the parent cell."},
            {"heading": "Cancer — Uncontrolled Cell Division",
             "content": "Cancer occurs when cells divide uncontrollably.\nMutation in genes that control the cell cycle → cells keep dividing → tumour.\nBenign tumour: doesn't spread. Malignant tumour: spreads to other tissues (metastasis).\nTreatment: surgery, radiotherapy (gamma rays), chemotherapy (drugs)."},
            {"heading": "Stem Cells",
             "content": "Stem cells are undifferentiated cells that can divide and specialise.\nEmbryonic stem cells: found in early embryos — can become any cell type (totipotent).\nAdult stem cells: found in bone marrow etc — more limited range of cell types.\nTherapeutic use: treating leukaemia, type 1 diabetes, Parkinson's disease.\nEthical issues: embryonic stem cell use destroys embryos — significant debate."},
            {"heading": "Cell Differentiation",
             "content": "As organisms develop, cells differentiate — become specialised for specific functions.\nRed blood cells: no nucleus, biconcave disc — maximises oxygen carrying.\nNeurone: long axon with myelin sheath — fast signal transmission.\nRoot hair cell: long projection — large surface area for water and mineral absorption.\nSperm cell: streamlined, lots of mitochondria, acrosome — adapted to reach and fertilise egg."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Mitosis produces TWO identical daughter cells with the SAME chromosome number as the parent. Meiosis (Higher) produces FOUR genetically different cells with HALF the chromosome number. Don't confuse them!",
        "key_note": "Mitosis = growth and repair (genetically identical). Used for asexual reproduction too.",
        "higher": "Meiosis: produces gametes (sperm and eggs) — four cells, each with half the chromosome number. Creates genetic variation through independent assortment and crossing over.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Specialised Cell to its Adaptation",
            "instruction": "Match each cell to the adaptation that makes it suited to its function.",
            "pairs": [
                ("Red blood cell", "Biconcave shape, no nucleus — maximum surface area for haemoglobin"),
                ("Neurone (nerve cell)", "Long axon with myelin sheath — fast electrical signal transmission"),
                ("Root hair cell", "Long extension — large surface area for absorbing water and minerals"),
                ("Sperm cell", "Flagellum (tail), many mitochondria, acrosome — swim to and fertilise egg"),
                ("Palisade leaf cell", "Many chloroplasts, near surface — maximum light absorption for photosynthesis"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What is the purpose of mitosis?",
             "opts": [("Growth, repair and replacement of cells — produces identical daughter cells", True), ("Producing gametes (sex cells)", False), ("Increasing genetic variation", False), ("Reducing chromosome number", False)],
             "wrong_explanations": {1: "Gamete production = MEIOSIS — not mitosis.", 2: "Mitosis produces genetically IDENTICAL cells. Genetic variation comes from meiosis and mutation.", 3: "Mitosis MAINTAINS chromosome number — meiosis HALVES it."}},
            {"q": "What makes embryonic stem cells more useful for therapy than adult stem cells?",
             "opts": [("They can become any cell type (totipotent)", True), ("They are easier to obtain", False), ("They cause less immune rejection", False), ("They divide faster", False)],
             "wrong_explanations": {1: "Embryonic stem cells are actually HARDER and more ethically controversial to obtain — their advantage is versatility.", 2: "Rejection depends on genetic match — embryonic stem cells can still be rejected.", 3: "Division rate isn't the key advantage — it's the ability to become any cell type."}},
            {"q": "Before mitosis, what must happen to the cell's DNA?",
             "opts": [("It must be replicated (copied)", True), ("It must be halved", False), ("It must be destroyed", False), ("Nothing — DNA stays the same", False)],
             "wrong_explanations": {1: "Halving DNA happens in MEIOSIS — mitosis needs a FULL copy for each daughter cell.", 2: "DNA is preserved — it's the basis of heredity and cell function.", 3: "DNA must be copied before division — each daughter cell must receive a complete set of chromosomes."}},
            {"q": "A red blood cell has no nucleus. How does this help its function?",
             "opts": [("More space for haemoglobin — carries more oxygen", True), ("It divides faster", False), ("It can destroy bacteria more easily", False), ("It lives longer without a nucleus", False)],
             "wrong_explanations": {1: "Cells without nuclei can't divide — they have a fixed lifespan.", 2: "Bacteria destruction = white blood cells. Red blood cells carry oxygen.", 3: "Without a nucleus, red blood cells can't repair themselves — they actually last only ~120 days before being replaced."}},
            {"q": "What is a malignant tumour?",
             "opts": [("A cancerous tumour that can spread to other tissues (metastasize)", True), ("A benign tumour that stays in one place", False), ("A tumour caused by a virus", False), ("Any lump or swelling", False)],
             "wrong_explanations": {1: "Benign tumour = stays in one place, doesn't spread.", 2: "Some cancers can be triggered by viruses (e.g. HPV and cervical cancer) — but malignant refers to spreading behaviour.", 3: "Not all lumps are malignant — benign tumours also cause lumps."}}
        ]
    },
],

"organisation": [
    {
        "id": "enzymes-digestion",
        "title": "Enzymes and the Digestive System",
        "spec": "4.2.1",
        "summary": "Describe enzyme action and the role of the digestive system.",
        "theory": [
            {"heading": "What are Enzymes?",
             "content": "Enzymes are biological catalysts — proteins that speed up chemical reactions.\nEach enzyme has an active site — a specific shape that fits one substrate (lock and key model).\nLower activation energy → faster reaction.\nDenatured enzyme: active site shape changes permanently → no longer works.\nCaused by high temperature or extreme pH."},
            {"heading": "Effect of Temperature on Enzymes",
             "content": "Low temperature: slow reaction — particles have less energy, fewer successful collisions.\nOptimum temperature: maximum rate — active site and substrate fit perfectly, many collisions.\nAbove optimum: enzyme denatures — active site shape distorted permanently.\nHuman enzymes: optimum ~37°C (body temperature). Plant enzymes may differ."},
            {"heading": "Effect of pH on Enzymes",
             "content": "Each enzyme has an optimum pH.\npH changes the shape of the active site by affecting hydrogen bonds.\nWrong pH → active site distorted → enzyme less effective → denaturation.\nPepsin (stomach): works best at pH ~2 (acidic). Amylase (mouth): works best at pH ~7 (neutral)."},
            {"heading": "The Digestive System",
             "content": "Mouth: amylase digests starch → maltose.\nStomach: pepsin + HCl digests proteins → peptides. pH ~2.\nSmall intestine: lipase digests fats → fatty acids + glycerol. Protease + amylase from pancreas.\nBile (from liver, stored in gall bladder): emulsifies fats — breaks large fat droplets into smaller ones → more surface area for lipase.\nLarge intestine: absorbs water. Rectum: stores faeces."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Enzymes are DENATURED at high temperature — NOT killed. They are proteins whose shape changes permanently. Also — bile EMULSIFIES fats; it doesn't chemically digest them. Lipase does the actual chemical digestion.",
        "key_note": "Lock and key model: enzyme active site (lock) + specific substrate (key) → enzyme-substrate complex → products released → enzyme reused.",
        "higher": "Induced fit model: active site changes shape slightly to fit the substrate — more accurate than lock and key for explaining enzyme specificity.",
        "triple_only": "Respiratory system gas exchange details. Blood clotting cascade.",
        "rp": ["RP3 — Investigate effect of pH on amylase activity", "RP4 — Food tests: iodine (starch), Benedict's (glucose), Biuret (protein), ethanol (fat)"],
        "matching": {
            "title": "Match the Enzyme to its Substrate and Product",
            "instruction": "Match each enzyme to what it breaks down and what it produces.",
            "pairs": [
                ("Amylase", "Starch → maltose (sugars)"),
                ("Protease", "Proteins → amino acids"),
                ("Lipase", "Lipids (fats) → fatty acids + glycerol"),
                ("Bile", "Emulsifies fats — large drops → small droplets (not digestion)"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "An enzyme is placed in a solution at 80°C. What happens?",
             "opts": [("It denatures — active site permanently changes shape", True), ("It works faster at higher temperature", False), ("It becomes more soluble", False), ("It breaks down into amino acids", False)],
             "wrong_explanations": {1: "Enzyme rate does increase up to the OPTIMUM — but above optimum, denaturing occurs.", 2: "Solubility of proteins can increase with temperature slightly — but the activity is permanently lost.", 3: "Denaturation changes shape — the enzyme doesn't break into amino acids unless it's also digested."}},
            {"q": "Which enzyme breaks down proteins?",
             "opts": [("Protease", True), ("Amylase", False), ("Lipase", False), ("Bile salts", False)],
             "wrong_explanations": {1: "Amylase breaks down STARCH into sugars.", 2: "Lipase breaks down FATS into fatty acids and glycerol.", 3: "Bile salts are not enzymes — they emulsify fats to give more surface area."}},
            {"q": "What does bile do to fats?",
             "opts": [("Emulsifies them — breaks large fat drops into smaller ones", True), ("Chemically digests fats into fatty acids", False), ("Neutralises stomach acid", False), ("Transports fats in the blood", False)],
             "wrong_explanations": {1: "Chemical digestion of fats = LIPASE. Bile emulsifies — a physical change, not chemical.", 2: "Bile is alkaline and does neutralise stomach acid — but in the context of fat digestion, its role is emulsification.", 3: "Lipoproteins transport fats in blood — bile works in the small intestine."}},
            {"q": "Why does enzyme activity decrease at very low pH?",
             "opts": [("Extreme pH changes the shape of the active site — enzyme less effective or denatured", True), ("Low pH destroys the substrate", False), ("Low pH lowers the temperature", False), ("Enzymes dissolve in acid", False)],
             "wrong_explanations": {1: "Substrates can sometimes be affected by pH but the main effect is on the ENZYME active site shape.", 2: "pH and temperature are independent factors. pH doesn't lower temperature.", 3: "Enzymes don't simply dissolve — their 3D structure is altered by pH changes affecting hydrogen bonds."}},
            {"q": "Where is bile produced and where is it stored?",
             "opts": [("Produced in the liver, stored in the gall bladder", True), ("Produced in the pancreas, stored in the stomach", False), ("Produced in the stomach, stored in the liver", False), ("Produced and stored in the small intestine", False)],
             "wrong_explanations": {1: "Pancreas produces digestive enzymes — bile is from the liver.", 2: "Stomach produces HCl and pepsin — bile comes from the liver.", 3: "Bile is released INTO the small intestine — it's not made there."}}
        ]
    },
    {
        "id": "heart-circulation",
        "title": "The Heart and Circulatory System",
        "spec": "4.2.3",
        "summary": "Describe the structure of the heart and the role of blood vessels.",
        "theory": [
            {"heading": "The Double Circulatory System",
             "content": "Humans have a DOUBLE circulatory system — two loops.\nLoop 1: heart → lungs → heart (picks up O₂, drops off CO₂).\nLoop 2: heart → body → heart (delivers O₂, collects CO₂).\nDouble system maintains high pressure for efficient delivery to all body tissues."},
            {"heading": "Structure of the Heart",
             "content": "Four chambers: right atrium, right ventricle, left atrium, left ventricle.\nRight side: pumps deoxygenated blood to lungs.\nLeft side: pumps oxygenated blood to body — thicker walls (higher pressure needed).\nValves prevent backflow: atrioventricular valves between atria and ventricles, semilunar valves in arteries.\nNatural pacemaker (SA node) controls heart rate."},
            {"heading": "Blood Vessels",
             "content": "Arteries: carry blood AWAY from heart. Thick muscular walls, small lumen, no valves. High pressure.\nVeins: carry blood TOWARDS heart. Thin walls, large lumen, VALVES to prevent backflow. Low pressure.\nCapillaries: one cell thick — allow exchange of O₂, CO₂, glucose, waste between blood and tissues."},
            {"heading": "Blood Components",
             "content": "Red blood cells: carry O₂ using haemoglobin. Biconcave, no nucleus.\nWhite blood cells: immune response — phagocytes engulf pathogens, lymphocytes produce antibodies.\nPlatelets: small fragments — involved in blood clotting.\nPlasma: liquid — transports glucose, CO₂, urea, hormones, heat."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "The LEFT ventricle has thicker walls than the right — it pumps to the WHOLE BODY (further distance, higher pressure needed). The right pumps only to the lungs (nearby). Students often get this backwards.",
        "key_note": "Arteries = Away from heart. Veins = towards heart. Capillaries = exchange sites.",
        "higher": "Coronary heart disease: fatty deposits (atherosclerosis) narrow coronary arteries → reduced blood flow to heart muscle → angina or heart attack. Treatments: statins, stents, bypass surgery.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Blood Vessel to its Properties",
            "instruction": "Match each vessel type to its correct properties.",
            "pairs": [
                ("Artery", "Thick muscular walls, small lumen, carries blood away from heart, high pressure"),
                ("Vein", "Thin walls, large lumen, has valves, carries blood toward heart, low pressure"),
                ("Capillary", "One cell thick, allows exchange of O₂/CO₂/glucose between blood and tissues"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Why does the left ventricle have thicker walls than the right?",
             "opts": [("It pumps blood to the whole body — needs higher pressure than the right ventricle (pumps only to lungs)", True), ("It receives blood from the lungs", False), ("It is larger so needs more muscle", False), ("The left side works harder because humans are right-handed", False)],
             "wrong_explanations": {1: "The atria receive blood — the ventricles pump it out. Left ventricle sends blood body-wide.", 2: "Size and wall thickness are both due to pressure requirements — the left pumps further.", 3: "Handedness has nothing to do with heart anatomy."}},
            {"q": "Which blood vessel carries oxygenated blood away from the heart to the body?",
             "opts": [("Aorta (an artery)", True), ("Vena cava (a vein)", False), ("Pulmonary artery", False), ("Pulmonary vein", False)],
             "wrong_explanations": {1: "Vena cava returns deoxygenated blood FROM the body TO the right side of the heart.", 2: "Pulmonary artery carries DEoxygenated blood TO the lungs — not to the body.", 3: "Pulmonary vein carries oxygenated blood FROM the lungs back TO the heart (left side)."}},
            {"q": "What do capillaries do?",
             "opts": [("Allow exchange of substances between blood and body tissues — walls are one cell thick", True), ("Carry blood at high pressure away from the heart", False), ("Prevent backflow of blood", False), ("Store blood when pressure drops", False)],
             "wrong_explanations": {1: "Arteries carry blood at high pressure — capillaries are for exchange, not high-pressure flow.", 2: "Valves prevent backflow — capillaries are too small for significant backflow.", 3: "Veins act as blood reservoirs — capillaries are exchange surfaces."}},
            {"q": "What is the function of white blood cells?",
             "opts": [("Immune response — phagocytes engulf pathogens, lymphocytes produce antibodies", True), ("Carry oxygen using haemoglobin", False), ("Clot blood at wound sites", False), ("Transport glucose and CO₂ in plasma", False)],
             "wrong_explanations": {1: "Oxygen is carried by RED blood cells using haemoglobin.", 2: "Blood clotting involves PLATELETS — not white blood cells.", 3: "Glucose and CO₂ are dissolved in PLASMA — not in white blood cells."}}
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
